"""Shared slide builders for the Çorum decks. Every builder returns one <section> string."""
import base64, html, os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(ROOT, "..", "fonts")
LATIN_EXT = "U+0100-02BA,U+02BD-02C5,U+02C7-02CC,U+02CE-02D7,U+02DD-02FF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+20A0-20C0,U+2C60-2C7F,U+A720-A7FF"
SPEAKER = "Prof. Dr. Ahmet Altun"
AFFIL = "Sivas Cumhuriyet University · Faculty of Medicine"
EVENT = "Cyberbiosecurity Training Workshop · Hitit University · Çorum"


def esc(s):
    return html.escape(s, quote=False)


def notes(txt):
    paras = [p.strip() for p in txt.strip().split("\n\n") if p.strip()]
    return '<aside class="notes">' + "".join(f"<p>{esc(p)}</p>" for p in paras) + "</aside>"


def section(sid, inner, theme="light", t="fade", cls="", attrs="", note="", foot=None):
    a = f' data-t="{t}"' if t else ""
    if foot is False:
        a += " data-nofoot"
    elif foot:
        a += f' data-foot="{esc(foot)}"'
    return f'<section class="slide {theme} {cls}" id="{sid}"{a} {attrs}>\n{inner}\n{notes(note) if note else ""}\n</section>'


def font_css():
    def face(fam, f, w, style="normal", rng=None):
        b = base64.b64encode(open(os.path.join(FONTS, f), "rb").read()).decode()
        stretch = "font-stretch:62% 125%;" if "wdth" in f else ""
        r = f"unicode-range:{rng};" if rng else ""
        return f"@font-face{{font-family:'{fam}';font-style:{style};font-weight:{w};{stretch}font-display:block;src:url(data:font/woff2;base64,{b}) format('woff2');{r}}}"
    out = [
        face("Archivo", "archivo-latin-wdth-normal.woff2", "100 900"),
        face("Archivo", "archivo-latin-ext-wdth-normal.woff2", "100 900", rng=LATIN_EXT),
    ]
    for w in (400, 500, 600):
        out.append(face("Plex Sans", f"ibm-plex-sans-latin-{w}-normal.woff2", w))
        out.append(face("Plex Sans", f"ibm-plex-sans-latin-ext-{w}-normal.woff2", w, rng=LATIN_EXT))
    out.append(face("Plex Sans", "ibm-plex-sans-latin-400-italic.woff2", 400, "italic"))
    for w in (400, 500):
        out.append(face("Plex Mono", f"ibm-plex-mono-latin-{w}-normal.woff2", w))
    return "\n".join(out)


def build(out_path, title, minutes, deck_title, sections, extra_css="", extra_js=""):
    css = open(os.path.join(ROOT, "engine.css")).read()
    js = open(os.path.join(ROOT, "engine.js")).read()
    page = f"""<title>{esc(title)}</title>
<style>
{font_css()}
{css}
{extra_css}
</style>
<div id="viewport"><div id="stage">
{chr(10).join(sections)}
</div></div>
<script>window.DECK = {{ title: {deck_title!r}, minutes: {minutes} }};</script>
<script>
{extra_js}
</script>
<script>
{js}
</script>
"""
    # every section id must be unique
    ids = re.findall(r'<section class="slide[^"]*" id="([^"]+)"', page)
    assert len(ids) == len(set(ids)), "duplicate slide ids"
    open(out_path, "w").write(page)
    return len(ids)


# ── reusable slide patterns ─────────────────────────────────────────────

def lobby(sid, day, time, title_lines, sub, note):
    tl = "".join(f'<div class="h1" data-k="rise" data-d="{200 + i * 160}">{l}</div>' for i, l in enumerate(title_lines))
    inner = f"""<canvas class="fx" data-fx="helix" data-x="1500"></canvas>
<div class="col" style="gap:20px;max-width:1150px">
  <p class="label" data-in="fade">{day} · {time}</p>
  {tl}
  <p class="lead muted" data-in="up" data-d="700" style="margin-top:18px">{sub}</p>
</div>
<div class="spacer"></div>
<div class="row" style="align-items:flex-end;gap:48px" data-in="fade" data-d="900">
  <div class="col" style="gap:6px"><p class="h3">{SPEAKER}</p><p class="small muted">{AFFIL}</p></div>
  <div class="spacer"></div>
  <p class="label muted" style="color:var(--mute)">Press → to begin</p>
</div>"""
    return section(sid, inner, "dark", "fade", "grid-bg", note=note, foot=EVENT)


def video(sid, src, poster, note):
    inner = f'<video src="{src}" poster="{poster}" muted playsinline preload="auto" data-auto data-next style="position:absolute;inset:0;width:1920px;height:1080px;object-fit:cover"></video>'
    return section(sid, inner, "dark", "fade", attrs='style="padding:0"', note=note, foot=False)


def sources(sid, items, deck_foot, note="Sources for this session. Every DOI on this slide has been checked against Crossref."):
    lis = "".join(f'<li class="small" style="padding-left:0">{i}</li>' for i in items)
    inner = f"""<p class="label">Sources</p>
<h2 class="h2">References and further reading</h2>
<ol style="margin:0;padding-left:34px;display:flex;flex-direction:column;gap:12px;columns:1;max-width:1660px">{lis}</ol>"""
    return section(sid, inner, "light", "fade", note=note, foot=deck_foot)


def thanks(sid, line, sub, note, deck_foot):
    inner = f"""<canvas class="fx" data-fx="net"></canvas>
<div class="spacer"></div>
<p class="label" data-in="fade">Questions &amp; discussion</p>
<div class="mega" data-k="stretch" data-wdth="110">{line}</div>
<p class="lead muted" data-in="up" data-d="500">{sub}</p>
<div class="spacer"></div>
<div class="row" style="gap:64px" data-in="fade" data-d="800">
  <div class="col" style="gap:4px"><p class="h3">{SPEAKER}</p><p class="small muted">{AFFIL}</p></div>
  <div class="col" style="gap:4px"><p class="small mono" style="user-select:all">aaltun@cumhuriyet.edu.tr</p><p class="small muted mono">ORCID 0000-0003-2056-8683</p></div>
</div>"""
    return section(sid, inner, "dark", "iris", "grid-bg", note=note, foot=deck_foot)
