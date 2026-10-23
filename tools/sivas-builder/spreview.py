"""Local preview for the Sivas decks: renders every slide (fully built) to JPEG with Sora / IBM Plex (latin + latin-ext)
and real lucide icons, and reports overflow (text past the footer line, past the right margin, clipped paragraphs).
usage: python3 spreview.py <deckroot> <outdir> [slide ids...]   env FONTPKGS=<dir with node_modules>"""
import asyncio, base64, glob, json, os, re, sys
from playwright.async_api import async_playwright

PK = os.environ.get("FONTPKGS", "/tmp/claude-0/-home-claude/41cc5063-6be5-5d52-9413-622dff0b42e8/scratchpad/fontpkgs") + "/node_modules"
EXT = "U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+20A0-20C0"


def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()


def face(fam, pkg, base, w):
    out = ""
    for sub, rng in (("latin", ""), ("latin-ext", EXT)):
        p = f"{PK}/@fontsource/{pkg}/files/{base}-{sub}-{w}-normal.woff2"
        ur = f";unicode-range:{rng}" if rng else ""
        out += f"@font-face{{font-family:'{fam}';font-weight:{w};src:url(data:font/woff2;base64,{b64(p)}){ur}}}"
    return out


FONT_CSS = ("".join(face("Sora", "sora", "sora", w) for w in (400, 600, 700, 800))
            + "".join(face("IBM Plex Sans", "ibm-plex-sans", "ibm-plex-sans", w) for w in (400, 500, 600, 700))
            + "".join(face("IBM Plex Mono", "ibm-plex-mono", "ibm-plex-mono", w) for w in (400, 500, 600)))


def kebab(n):
    return re.sub(r"(?<=[a-z0-9])([A-Z])", r"-\1", n).lower()


RT = {"Book": "BookOpen", "Chart": "ChartColumn", "Chat": "MessageCircle", "CheckCircle": "CircleCheck", "Home": "House", "Lightning": "Zap",
      "PaperPlane": "Send", "Tool": "Hammer", "Trust": "Handshake", "Verified": "BadgeCheck", "Warning": "TriangleAlert"}


def lucide(name, style):
    name = RT.get(name, name)
    p = f"{PK}/lucide-static/icons/{kebab(name)}.svg"
    if not os.path.exists(p):
        return f'<span data-missing-icon="{name}" style="{style};display:inline-block;background:red"></span>'
    s = open(p).read()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    s = re.sub(r'\s(width|height|class)="[^"]*"', "", s, count=3)
    return s.replace("<svg", f'<svg style="{style};flex:none"', 1)


def convert(sec):
    sec = re.sub(r"<aside>.*?</aside>", "", sec, flags=re.S)
    sec = re.sub(r'<x-embed[^>]*style="([^"]*)"[^>]*>(.*?)</x-embed>',
                 lambda m: f'<iframe style="{m.group(1)};border:0" srcdoc="{m.group(2).replace("&", "&amp;").replace(chr(34), "&quot;")}"></iframe>', sec, flags=re.S)
    sec = re.sub(r'<x-icon name="([^"]*)" style="([^"]*)"></x-icon>', lambda m: lucide(m.group(1), m.group(2)), sec)
    sec = re.sub(r'<section ([^>]*)style="', r'<div class="sl" \1style="position:relative;width:1920px;height:1080px;box-sizing:border-box;overflow:hidden;', sec, count=1)
    return re.sub(r"</section>\s*$", "</div>", sec.strip())


CHECK = """(()=>{const out=[];document.querySelectorAll('.sl p,.sl h1,.sl h2,.sl li').forEach(e=>{const r=e.getBoundingClientRect();if(!r.height)return;
if(e.style.bottom==='64px')return;if(r.bottom>968)out.push('LOW:'+(e.textContent||'').trim().slice(0,36)+'@'+Math.round(r.bottom));
if(r.right>1800)out.push('R:'+(e.textContent||'').trim().slice(0,30)+'@'+Math.round(r.right));
if(e.scrollHeight>e.clientHeight+4||e.scrollWidth>e.clientWidth+4)out.push('CLIP:'+(e.textContent||'').trim().slice(0,30))});
document.querySelectorAll('[data-missing-icon]').forEach(e=>out.push('ICON:'+e.dataset.missingIcon));
document.querySelectorAll('.sl > div[style*="position:absolute"]').forEach(e=>{const r=e.getBoundingClientRect();if(e.scrollHeight>e.clientHeight+4&&e.style.height)out.push('BOX:'+(e.textContent||'').trim().slice(0,30))});
return out.slice(0,6)})()"""


async def main(root, out, only=None):
    order = json.load(open(os.path.join(root, "project/deck.json")))["order"]
    os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1920, "height": 1080})
        for i, sid in enumerate(order):
            if only and sid not in only:
                continue
            sec = open(os.path.join(root, f"project/slides/{sid}.html"), encoding="utf-8").read()
            html = (f"<!doctype html><html lang='tr'><head><meta charset='utf-8'><style>{FONT_CSS} body{{margin:0}} p,h1,h2,h3,ul,ol{{margin:0}}"
                    f" ul,ol{{padding-left:1.2em}} .sl{{font-size:32px}} .sl *{{box-sizing:border-box}}</style></head><body>{convert(sec)}</body></html>")
            await pg.set_content(html)
            await pg.wait_for_timeout(int(os.environ.get("WAIT", "2600")))
            bad = await pg.evaluate(CHECK)
            if bad:
                print("CHECK", i + 1, sid, bad)
            await pg.screenshot(path=os.path.join(out, f"{i + 1:02d}_{sid}.jpg"), type="jpeg", quality=74)
        await b.close()
    print("rendered", len(order) if not only else len(only))


def sheet(out, cols=4, start=0, cnt=16, name="sheet"):
    from PIL import Image
    fs = sorted(glob.glob(os.path.join(out, "[0-9]*.jpg")))[start:start + cnt]
    ims = [Image.open(f).resize((640, 360)) for f in fs]
    rows = (len(ims) + cols - 1) // cols
    c = Image.new("RGB", (640 * cols + 8 * (cols - 1), 360 * rows + 8 * (rows - 1)), "#888")
    for i, im in enumerate(ims):
        c.paste(im, ((i % cols) * 648, (i // cols) * 368))
    path = os.path.join(out, f"{name}_{start}.jpg")
    c.save(path, quality=80)
    return path


if __name__ == "__main__":
    if sys.argv[1] == "sheet":
        print(sheet(sys.argv[2], start=int(sys.argv[3]) if len(sys.argv) > 3 else 0, cnt=int(sys.argv[4]) if len(sys.argv) > 4 else 16))
    else:
        asyncio.run(main(sys.argv[1], sys.argv[2], sys.argv[3:] or None))
