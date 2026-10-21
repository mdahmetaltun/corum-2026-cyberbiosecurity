"""Local preview of Slides-format files: renders each section to a PNG (final, fully built state)."""
import asyncio, base64, glob, os, re, sys
from playwright.async_api import async_playwright

FONTS = "/home/claude/corum/fonts"
F2 = "/home/claude/corum/openers/public/fonts"


def b64(p):
    return base64.b64encode(open(p, "rb").read()).decode()


FONT_CSS = "".join([
    f"@font-face{{font-family:'Source Serif 4';font-weight:200 900;src:url(data:font/woff2;base64,{b64(F2 + '/source-serif-4-latin-wght-normal.woff2')})}}",
    f"@font-face{{font-family:'Source Serif 4';font-weight:200 900;src:url(data:font/woff2;base64,{b64(F2 + '/source-serif-4-latin-ext-wght-normal.woff2')});unicode-range:U+0100-02FF}}",
    *[f"@font-face{{font-family:'IBM Plex Sans';font-weight:{w};src:url(data:font/woff2;base64,{b64(FONTS + f'/ibm-plex-sans-latin-{w}-normal.woff2')})}}" for w in (400, 500, 600)],
    *[f"@font-face{{font-family:'IBM Plex Sans';font-weight:{w};src:url(data:font/woff2;base64,{b64(FONTS + f'/ibm-plex-sans-latin-ext-{w}-normal.woff2')});unicode-range:U+0100-02FF}}" for w in (400, 500, 600)],
    f"@font-face{{font-family:'IBM Plex Sans';font-weight:700;src:url(data:font/woff2;base64,{b64(FONTS + '/ibm-plex-sans-latin-600-normal.woff2')})}}",
    *[f"@font-face{{font-family:'IBM Plex Mono';font-weight:{w};src:url(data:font/woff2;base64,{b64(FONTS + f'/ibm-plex-mono-latin-{w}-normal.woff2')})}}" for w in (400, 500)],
    f"@font-face{{font-family:'IBM Plex Mono';font-weight:600;src:url(data:font/woff2;base64,{b64(FONTS + '/ibm-plex-mono-latin-500-normal.woff2')})}}",
])


def convert(sec):
    sec = re.sub(r"<aside>.*?</aside>", "", sec, flags=re.S)

    def emb(m):
        st, inner = m.group(1), m.group(2)
        srcdoc = inner.replace("&", "&amp;").replace('"', "&quot;")
        return f'<iframe style="{st};border:0" srcdoc="{srcdoc}"></iframe>'
    sec = re.sub(r'<x-embed[^>]*style="([^"]*)"[^>]*>(.*?)</x-embed>', emb, sec, flags=re.S)
    def svg2img(m):
        s = m.group(0)
        mm = re.search(r'style="([^"]*)"', s); st = mm.group(1) if mm else ''
        s2 = s.replace("<svg ", '<svg xmlns="http://www.w3.org/2000/svg" ', 1).replace(f'style="{st}"', "", 1)
        return f'<img src="data:image/svg+xml;base64,{base64.b64encode(s2.encode()).decode()}" style="{st}">'
    sec = re.sub(r"<svg .*?</svg>", svg2img, sec, flags=re.S) if True else sec

    sec = re.sub(r'<x-icon name="([^"]*)" style="([^"]*)"></x-icon>', lambda m: f'<span title="{m.group(1)}" style="{m.group(2)};display:inline-block;border-radius:10px;border:3px solid currentColor;box-sizing:border-box;flex:none"></span>', sec)
    sec = re.sub(r'<section ([^>]*)style="', r'<div class="sl" \1style="position:relative;width:1920px;height:1080px;box-sizing:border-box;overflow:hidden;', sec, count=1)
    sec = re.sub(r"</section>\s*$", "</div>", sec.strip())
    return sec


async def main(root, out, only=None):
    files = sorted(glob.glob(os.path.join(root, "project/slides/*.html")))
    import json
    order = json.load(open(os.path.join(root, "project/deck.json")))["order"]
    os.makedirs(out, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width": 1920, "height": 1080})
        for i, sid in enumerate(order):
            if only and sid not in only and str(i) not in only:
                continue
            sec = open(os.path.join(root, f"project/slides/{sid}.html")).read()
            html = f"<!doctype html><html><head><meta charset='utf-8'><style>{FONT_CSS} body{{margin:0}} p,h1,h2,h3,ul,ol{{margin:0}} ul,ol{{padding-left:1.2em}} .sl{{font-size:32px}} .sl *{{box-sizing:border-box}}</style></head><body>{convert(sec)}</body></html>"
            await pg.set_content(html)
            await pg.wait_for_timeout(1200)
            # overflow check: pinned text past y 960 or overlapping footers
            bad = await pg.evaluate("""(()=>{const out=[];document.querySelectorAll('.sl p,.sl h2,.sl h3,.sl div').forEach(e=>{const r=e.getBoundingClientRect();if(!r.height)return;const fs=parseFloat(getComputedStyle(e).fontSize);if(e.style.bottom==='64px')return;if(r.bottom>965&&r.top<1000)out.push((e.textContent||'').trim().slice(0,40)+'@'+Math.round(r.bottom));if(r.right>1800&&e.tagName!=='DIV')out.push('R:'+(e.textContent||'').trim().slice(0,30)+'@'+Math.round(r.right));if(e.scrollHeight>e.clientHeight+4&&e.tagName==='P')out.push('CLIP:'+(e.textContent||'').trim().slice(0,30))});return out.slice(0,4)})()""")
            if bad:
                print("CHECK", i + 1, sid, bad)
            await pg.screenshot(path=os.path.join(out, f"{i + 1:02d}_{sid}.jpg"), type="jpeg", quality=72)
        await b.close()


def sheet(out, cols=4, start=0, cnt=16, name="sheet"):
    from PIL import Image
    fs = sorted(glob.glob(os.path.join(out, "[0-9]*.jpg")))[start:start + cnt]
    ims = [Image.open(f).resize((640, 360)) for f in fs]
    rows = (len(ims) + cols - 1) // cols
    c = Image.new("RGB", (640 * cols, 360 * rows), "white")
    for i, im in enumerate(ims):
        c.paste(im, ((i % cols) * 640, (i // cols) * 360))
    path = os.path.join(out, f"{name}_{start}.jpg")
    c.save(path, quality=78)
    return path


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2], sys.argv[3:] or None))
