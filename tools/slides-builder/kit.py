"""Slides-format builder in the Skill Tracker visual language (paper + navy, Source Serif / IBM Plex, blue-teal-orange,
shimmering progress bar, a topic illustration on every slide, staged build-ins)."""
import html, json, math, os

NAVY, PAPER, TEXT, BODY2, MUTE = "#13294B", "#F7F9FC", "#1F2D45", "#3A4A63", "#5A6A82"
BLUE, LBLUE, PALE, PALE2 = "#1662E8", "#5B9BFF", "#D6E6FF", "#E8F0FF"
TEAL, TEALT, MINT, AQUA = "#00C2B2", "#00968A", "#7FD1C9", "#3EDBCB"
ORANGE, ORANGET, GOLD, SAND = "#FF7A1A", "#EA5A0C", "#FFB547", "#F0C27A"
GREEN, GREY, CREAM, SKY = "#22C55E", "#DCE3EC", "#F5F3EE", "#B9C7DA"
SERIF = "'Source Serif 4', Georgia, serif"
SANS = "'IBM Plex Sans', Arial, sans-serif"
MONO = "'IBM Plex Mono', monospace"
RM = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"


def esc(s):
    return html.escape(s, quote=False)


# ───────────────────────── chrome ─────────────────────────
def progress(i, n, dark=False):
    w = max(60, round(1920 * (i + 1) / n))
    track = "#FFFFFF" if dark else NAVY
    return (f'<svg aria-label="" width="1920" height="8" viewBox="0 0 1920 8" style="position:absolute;left:0px;top:0px;width:1920px;height:8px">'
            f'<style>.sh{{animation:sh 3.2s ease-in-out infinite}}@keyframes sh{{from{{transform:translateX(-240px)}}to{{transform:translateX({w}px)}}}}{RM}</style>'
            f'<defs><linearGradient id="pg" x1="0" x2="1"><stop offset="0" stop-color="{BLUE}"/><stop offset=".55" stop-color="{TEAL}"/><stop offset="1" stop-color="{GREEN}"/></linearGradient>'
            f'<linearGradient id="sg" x1="0" x2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset=".5" stop-color="#FFFFFF" stop-opacity=".75"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>'
            f'<clipPath id="pc"><rect width="{w}" height="8"/></clipPath></defs><rect width="1920" height="8" fill="{track}" fill-opacity=".06"/>'
            f'<rect width="{w}" height="8" fill="url(#pg)"/><g clip-path="url(#pc)"><rect class="sh" width="240" height="8" fill="url(#sg)"/></g></svg>')


def footer(left, num, dark=False):
    c = SKY if dark else MUTE
    return (f'<p style="position:absolute;left:128px;bottom:64px;width:1300px;font-size:24px;color:{c}">{left}</p>'
            f'<p style="position:absolute;right:128px;bottom:64px;width:120px;font-size:24px;color:{c};text-align:right">{num}</p>')


def head(eyebrow, title, dark=False, width=1320):
    eb = MINT if dark else TEALT
    tc = CREAM if dark else NAVY
    return (f'<div style="width:{width}px;display:flex;flex-direction:column;gap:12px">'
            f'<p style="font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{eb}">{eyebrow}</p>'
            f'<h2 style="font-family:{SERIF};font-size:60px;font-weight:600;line-height:1.1;color:{tc}">{title}</h2></div>')


def section(sid, inner, dark=False, transition="fade", notes="", bg=None):
    bgc = bg or (NAVY if dark else PAPER)
    col = CREAM if dark else TEXT
    n = f"<aside>{esc(notes.strip())}</aside>" if notes else ""
    return (f'<section id="{sid}" data-transition="{transition}" style="background:{bgc};color:{col};font-family:{SANS};'
            f'padding:128px 128px 160px;display:flex;flex-direction:column;gap:12px">\n{inner}\n{n}\n</section>\n')


def pin(left, top, width, inner, build=None, height=None, style="", tag="div", eid=None):
    b = f' data-build-in="{build}"' if build else ""
    h = f"height:{height}px;" if height else ""
    i = f' id="{eid}"' if eid else ""
    return f'<{tag}{i}{b} style="position:absolute;left:{left}px;top:{top}px;width:{width}px;{h}{style}">{inner}</{tag}>'


def P(text, size=28, color=None, weight=None, lh=1.4, extra=""):
    c = f"color:{color};" if color else ""
    w = f"font-weight:{weight};" if weight else ""
    return f'<p style="font-size:{size}px;line-height:{lh};{c}{w}{extra}">{text}</p>'


def card(inner, accent=BLUE, bg="#FFFFFF", pad="30px 32px", gap=12, shadow=True, radius=20, top_border=True, extra=""):
    sh = "box-shadow:0 10px 32px rgba(19,41,75,0.08);" if shadow else ""
    bt = f"border-top:6px solid {accent};" if top_border and accent else ""
    return f'display:flex;flex-direction:column;gap:{gap}px;background:{bg};padding:{pad};border-radius:{radius}px;{bt}{sh}{extra}', inner


def cards_row(items, top, n=None, gap=24, left=128, total=1664, build_start=1, kind="rise", height=None, accent_cycle=None, pad="30px 32px", bg="#FFFFFF", topb=True):
    """items: list of inner-html strings. Returns pinned card divs."""
    n = n or len(items)
    w = (total - gap * (n - 1)) / n
    out = []
    accents = accent_cycle or [BLUE, TEAL, ORANGE, GREEN, LBLUE, GOLD]
    for k, inner in enumerate(items):
        r, c = divmod(k, n)
        st, _ = card("", accent=accents[k % len(accents)], pad=pad, bg=bg, top_border=topb)
        h = f"height:{height}px;" if height else ""
        y = top + r * ((height or 0) + gap)
        out.append(f'<div data-build-in="{kind} {build_start + k} auto" style="position:absolute;left:{left + c * (w + gap):.0f}px;top:{y}px;width:{w:.0f}px;{h}{st}">{inner}</div>')
    return "".join(out)


def callout(top, text, label="Key point", icon="Lightbulb", build="rise 9 auto", bg=PALE2, left=128, width=1664, color=TEXT, labelc=NAVY, iconc=ORANGET):
    return (f'<div data-build-in="{build}" style="position:absolute;left:{left}px;top:{top}px;width:{width}px;display:flex;flex-direction:row;gap:24px;align-items:center;padding:22px 40px;background:{bg};border-radius:20px">'
            f'<x-icon name="{icon}" style="width:44px;height:44px;color:{iconc}"></x-icon>'
            f'<p style="width:230px;font-size:24px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:{labelc}">{label}</p>'
            f'<p style="flex:1;font-size:28px;line-height:1.35;color:{color}">{text}</p></div>')


def chip(text, bg=PALE2, color=NAVY, size=24):
    return f'<p style="font-family:{MONO};font-size:{size}px;font-weight:600;color:{color};background:{bg};padding:6px 14px;border-radius:10px">{text}</p>'


def bignum(text, color=NAVY, size=72):
    return f'<p style="font-family:{SERIF};font-size:{size}px;font-weight:600;line-height:1.02;color:{color}">{text}</p>'


# ───────────────────────── illustrations (360×236, animated, no text) ─────────────────────────
def _svg(body, style, w=360, h=236, left=1480, top=48, label=""):
    return (f'<svg aria-label="{label}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{h}px">'
            f'<style>{style}{RM}</style>{body}</svg>')


def il_shield(**k):
    st = (".rg{transform-box:fill-box;transform-origin:center;animation:rg 2.6s ease-out infinite}@keyframes rg{0%{transform:scale(.7);opacity:.7}100%{transform:scale(1.5);opacity:0}}"
          ".ck{stroke-dasharray:120;stroke-dashoffset:120;animation:ck 3s ease-in-out infinite}@keyframes ck{0%,15%{stroke-dashoffset:120}45%,85%{stroke-dashoffset:0}100%{stroke-dashoffset:0;opacity:0}}"
          ".fl{animation:fl 4s ease-in-out infinite}@keyframes fl{50%{transform:translateY(-6px)}}")
    b = (f'<circle class="rg" cx="180" cy="118" r="90" fill="none" stroke="{TEAL}" stroke-width="4"/><circle class="rg" style="animation-delay:1.3s" cx="180" cy="118" r="90" fill="none" stroke="{LBLUE}" stroke-width="4"/>'
         f'<g class="fl"><path d="M180 28 L250 54 V112 C250 160 218 192 180 208 C142 192 110 160 110 112 V54 Z" fill="{NAVY}"/><path d="M180 44 L236 65 V112 C236 150 212 176 180 190 C148 176 124 150 124 112 V65 Z" fill="{BLUE}"/>'
         f'<path class="ck" d="M150 116 L172 138 L214 92" fill="none" stroke="#FFFFFF" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></g>')
    return _svg(b, st, **k)


def il_helix(**k):
    st = ".a{animation:a 2.8s ease-in-out infinite alternate}@keyframes a{from{transform:translateX(-46px)}to{transform:translateX(46px)}}.b{animation:b 2.8s ease-in-out infinite alternate}@keyframes b{from{transform:translateX(46px)}to{transform:translateX(-46px)}}"
    b = ""
    for i in range(11):
        y = 18 + i * 20
        d = f"animation-delay:-{i * 0.36:.2f}s"
        col = ORANGE if i % 4 == 1 else LBLUE
        b += (f'<g class="a" style="{d}"><circle cx="180" cy="{y}" r="8" fill="{col}"/></g><g class="b" style="{d}"><circle cx="180" cy="{y}" r="8" fill="{TEAL}"/></g>'
              f'<line x1="140" y1="{y}" x2="220" y2="{y}" stroke="{GREY}" stroke-width="3" stroke-linecap="round" opacity=".6"/>')
    return _svg(b, st, **k)


def il_network(**k):
    st = ".fw{stroke-dasharray:6 14;animation:fw 1.2s linear infinite}@keyframes fw{to{stroke-dashoffset:-40}}.np{transform-box:fill-box;transform-origin:center;animation:np 3s ease-in-out infinite}@keyframes np{50%{transform:scale(1.18)}}"
    pts = [(60, 50, BLUE), (60, 190, TEAL), (300, 50, ORANGE), (300, 190, GREEN), (180, 24, GOLD)]
    b = ""
    for x, y, c in pts:
        b += f'<path d="M180 128 L{x} {y}" stroke="{GREY}" stroke-width="8" stroke-linecap="round"/><path class="fw" d="M180 128 L{x} {y}" stroke="{c}" stroke-width="5" stroke-linecap="round"/>'
    for i, (x, y, c) in enumerate(pts):
        b += f'<circle class="np" style="animation-delay:{i * .5}s" cx="{x}" cy="{y}" r="20" fill="{c}"/>'
    b += f'<circle cx="180" cy="128" r="34" fill="{NAVY}"/><path d="M164 128 h32 M180 112 v32" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/>'
    return _svg(b, st, **k)


def _arc(cx, cy, r0, r1, a0, a1):
    p = lambda r, a: f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}"
    L = 1 if a1 - a0 > math.pi else 0
    return f"M{p(r1, a0)} A{r1},{r1} 0 {L} 1 {p(r1, a1)} L{p(r0, a1)} A{r0},{r0} 0 {L} 0 {p(r0, a0)} Z"


def il_wheel(**k):
    st = ".sg{animation:sg 5s ease-in-out infinite}@keyframes sg{0%,100%{fill:" + PALE + "}10%,22%{fill:" + BLUE + "}32%{fill:" + PALE + "}}.rot{transform-origin:180px 118px;animation:rot 30s linear infinite}@keyframes rot{to{transform:rotate(360deg)}}"
    b = '<g class="rot">'
    seg = 2 * math.pi / 5
    for i in range(5):
        a0 = -math.pi / 2 - seg / 2 + i * seg + 0.05
        b += f'<path class="sg" style="animation-delay:{i}s" d="{_arc(180, 118, 56, 108, a0, a0 + seg - 0.1)}" fill="{PALE}"/>'
    b += f'</g><circle cx="180" cy="118" r="44" fill="{ORANGE}"/><circle cx="180" cy="118" r="18" fill="#FFFFFF" opacity=".9"/>'
    return _svg(b, st, **k)


def il_radar(**k):
    st = ".sw{transform-origin:180px 118px;animation:sw 4s linear infinite}@keyframes sw{to{transform:rotate(360deg)}}.bl{transform-box:fill-box;transform-origin:center;animation:bl 4s ease-out infinite;opacity:0}@keyframes bl{0%{opacity:0;transform:scale(.3)}8%{opacity:1;transform:scale(1.2)}40%{opacity:.6;transform:scale(1)}100%{opacity:0}}"
    b = (f'<defs><linearGradient id="rgd" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="{TEAL}" stop-opacity="0"/><stop offset="1" stop-color="{TEAL}" stop-opacity=".45"/></linearGradient></defs>'
         f'<g fill="none" stroke="{TEALT}" stroke-opacity=".3" stroke-width="2"><circle cx="180" cy="118" r="36"/><circle cx="180" cy="118" r="72"/><circle cx="180" cy="118" r="108"/><path d="M72 118 H288 M180 10 V226"/></g>'
         f'<path class="sw" d="M180 118 L180 10 A108 108 0 0 1 273 64 Z" fill="url(#rgd)"/>'
         f'<circle class="bl" style="animation-delay:.5s" cx="226" cy="70" r="8" fill="{ORANGE}"/><circle class="bl" style="animation-delay:1.6s" cx="250" cy="150" r="7" fill="{TEAL}"/><circle class="bl" style="animation-delay:2.7s" cx="128" cy="168" r="8" fill="{ORANGE}"/><circle class="bl" style="animation-delay:3.4s" cx="120" cy="80" r="6" fill="{TEAL}"/>')
    return _svg(b, st, **k)


def il_lock(**k):
    st = ".sk{animation:sk 3.2s ease-in-out infinite}@keyframes sk{0%,20%{transform:translateY(-18px)}40%,85%{transform:translateY(0)}100%{transform:translateY(-18px)}}.gl{animation:gl 3.2s ease-in-out infinite}@keyframes gl{0%,35%{fill:" + LBLUE + "}45%,85%{fill:" + GREEN + "}100%{fill:" + LBLUE + "}}"
    b = (f'<g class="sk"><path d="M136 112 V76 a44 44 0 0 1 88 0 V112" fill="none" stroke="{NAVY}" stroke-width="16" stroke-linecap="round"/></g>'
         f'<rect x="110" y="104" width="140" height="112" rx="22" fill="{BLUE}"/><circle class="gl" cx="180" cy="150" r="14" fill="{LBLUE}"/><rect x="174" y="156" width="12" height="32" rx="6" fill="{NAVY}"/>'
         f'<circle cx="64" cy="70" r="6" fill="{TEAL}"/><circle cx="300" cy="96" r="8" fill="{GOLD}"/><circle cx="292" cy="190" r="5" fill="{TEAL}"/>')
    return _svg(b, st, **k)


def il_scan(**k):
    st = ".mg{animation:mg 6s ease-in-out infinite}@keyframes mg{0%{transform:translate(0,0)}25%{transform:translate(170px,0)}50%{transform:translate(170px,90px)}75%{transform:translate(0,90px)}100%{transform:translate(0,0)}}.bx{animation:bx 6s linear infinite}@keyframes bx{0%,8%{fill:" + GREY + "}12%,100%{fill:" + TEAL + "}}"
    b = ""
    k2 = 0
    for r in range(3):
        for c in range(5):
            b += f'<rect class="bx" style="animation-delay:{(k2 * 0.4):.1f}s" x="{40 + c * 58}" y="{40 + r * 56}" width="44" height="40" rx="8" fill="{GREY}"/>'
            k2 += 1
    b += f'<g class="mg"><circle cx="78" cy="70" r="38" fill="#FFFFFF" fill-opacity=".35" stroke="{NAVY}" stroke-width="9"/><path d="M106 98 L134 126" stroke="{NAVY}" stroke-width="14" stroke-linecap="round"/></g>'
    return _svg(b, st, **k)


def il_bell(**k):
    st = ".bl{transform-origin:180px 40px;animation:bl 1.4s ease-in-out infinite}@keyframes bl{0%,100%{transform:rotate(-14deg)}50%{transform:rotate(14deg)}}.wv{animation:wv 1.4s ease-out infinite}@keyframes wv{0%{opacity:0}30%{opacity:1}100%{opacity:0}}"
    b = (f'<g class="bl"><path d="M180 40 C130 40 122 92 122 132 L104 168 H256 L238 132 C238 92 230 40 180 40 Z" fill="{ORANGE}"/><circle cx="180" cy="184" r="18" fill="{NAVY}"/><rect x="172" y="24" width="16" height="22" rx="8" fill="{NAVY}"/></g>'
         f'<g fill="none" stroke="{ORANGET}" stroke-width="6" stroke-linecap="round"><path class="wv" d="M78 82 C64 104 64 132 78 154"/><path class="wv" style="animation-delay:.3s" d="M52 66 C30 100 30 136 52 170"/>'
         f'<path class="wv" d="M282 82 C296 104 296 132 282 154"/><path class="wv" style="animation-delay:.3s" d="M308 66 C330 100 330 136 308 170"/></g>')
    return _svg(b, st, **k)


def il_backup(**k):
    st = ".rt{transform-origin:180px 118px;animation:rt 4s linear infinite}@keyframes rt{to{transform:rotate(360deg)}}.dl{animation:dl 2s ease-in-out infinite}@keyframes dl{0%,100%{opacity:.35}50%{opacity:1}}"
    b = (f'<g class="rt"><path d="M180 22 A96 96 0 1 1 86 98" fill="none" stroke="{TEAL}" stroke-width="10" stroke-linecap="round"/><path d="M70 92 L86 120 L106 94 Z" fill="{TEAL}"/></g>'
         f'<ellipse cx="180" cy="86" rx="54" ry="16" fill="{BLUE}"/><path d="M126 86 V150 C126 162 234 162 234 150 V86" fill="{BLUE}"/><ellipse cx="180" cy="86" rx="54" ry="16" fill="{LBLUE}"/>'
         f'<path d="M126 118 C126 130 234 130 234 118" fill="none" stroke="{NAVY}" stroke-width="3" opacity=".5"/>'
         f'<circle class="dl" cx="210" cy="110" r="5" fill="{GREEN}"/><circle class="dl" style="animation-delay:.6s" cx="210" cy="140" r="5" fill="{GREEN}"/>')
    return _svg(b, st, **k)


def il_scale(**k):
    st = ".bm{transform-origin:180px 70px;animation:bm 4s ease-in-out infinite}@keyframes bm{0%,100%{transform:rotate(-8deg)}50%{transform:rotate(8deg)}}"
    b = (f'<rect x="174" y="70" width="12" height="130" rx="6" fill="{NAVY}"/><rect x="120" y="196" width="120" height="16" rx="8" fill="{NAVY}"/><circle cx="180" cy="62" r="14" fill="{GOLD}"/>'
         f'<g class="bm"><rect x="70" y="66" width="220" height="10" rx="5" fill="{NAVY}"/><path d="M90 76 L62 140 H118 Z" fill="none" stroke="{MUTE}" stroke-width="3"/><path d="M270 76 L242 140 H298 Z" fill="none" stroke="{MUTE}" stroke-width="3"/>'
         f'<path d="M56 140 H124 A34 18 0 0 1 56 140 Z" fill="{BLUE}"/><path d="M236 140 H304 A34 18 0 0 1 236 140 Z" fill="{ORANGE}"/></g>')
    return _svg(b, st, **k)


def il_stairs(**k):
    st = ".br{transform-box:fill-box;transform-origin:center bottom;animation:br 6s cubic-bezier(.2,.8,.2,1) infinite}@keyframes br{0%,8%{transform:scaleY(.2)}40%,85%{transform:scaleY(1)}100%{transform:scaleY(.2)}}.ds{animation:ds 6s ease-in-out infinite}@keyframes ds{0%,15%{transform:translate(0,0)}35%{transform:translate(70px,-40px)}55%{transform:translate(140px,-80px)}75%,90%{transform:translate(210px,-120px)}100%{transform:translate(0,0)}}"
    cols = [PALE, LBLUE, BLUE, NAVY]
    b = "".join(f'<rect class="br" style="animation-delay:{i * .25}s" x="{40 + i * 70}" y="{176 - i * 40}" width="58" height="{40 + i * 40}" rx="8" fill="{c}"/>' for i, c in enumerate(cols))
    b += f'<rect x="24" y="216" width="312" height="6" rx="3" fill="{NAVY}"/><circle class="ds" cx="69" cy="162" r="11" fill="{ORANGE}"/>'
    return _svg(b, st, **k)


def il_profile(**k):
    st = ".in{transform-origin:180px 118px;animation:in 4s ease-in-out infinite}@keyframes in{0%,100%{transform:scale(.55)}50%{transform:scale(.8)}}.ot{stroke-dasharray:12 10;animation:ot 2s linear infinite}@keyframes ot{to{stroke-dashoffset:-44}}"
    hexp = lambda r: " ".join(f"{180 + r * math.cos(-math.pi / 2 + i * math.pi / 3):.1f},{118 + r * math.sin(-math.pi / 2 + i * math.pi / 3):.1f}" for i in range(6))
    b = (f'<polygon points="{hexp(100)}" fill="none" stroke="{GREY}" stroke-width="2"/><polygon points="{hexp(66)}" fill="none" stroke="{GREY}" stroke-width="2"/>'
         f'<polygon class="ot" points="{hexp(96)}" fill="{ORANGE}" fill-opacity=".08" stroke="{ORANGE}" stroke-width="5"/>'
         f'<g class="in"><polygon points="{hexp(100)}" fill="{BLUE}" fill-opacity=".25" stroke="{BLUE}" stroke-width="6"/></g>')
    return _svg(b, st, **k)


def il_timeline(**k):
    st = ".pr{animation:pr 6s ease-in-out infinite}@keyframes pr{0%{width:0}70%,100%{width:280px}}.dt{transform-box:fill-box;transform-origin:center;animation:dt 6s ease-out infinite;transform:scale(0)}@keyframes dt{0%{transform:scale(0)}8%,90%{transform:scale(1)}100%{transform:scale(0)}}"
    b = f'<rect x="40" y="114" width="280" height="8" rx="4" fill="{GREY}"/><rect class="pr" x="40" y="114" width="280" height="8" rx="4" fill="{TEAL}"/>'
    for i, c in enumerate([BLUE, TEAL, ORANGE]):
        x = 60 + i * 120
        b += f'<g class="dt" style="animation-delay:{0.6 + i * 1.3}s"><circle cx="{x}" cy="118" r="22" fill="{c}"/><rect x="{x - 26}" y="{56 if i % 2 == 0 else 160}" width="52" height="24" rx="8" fill="{c}" opacity=".35"/></g>'
    return _svg(b, st, **k)


def il_molecule(**k):
    st = ".or{transform-origin:180px 118px;animation:or 9s linear infinite}@keyframes or{to{transform:rotate(360deg)}}.pu{transform-box:fill-box;transform-origin:center;animation:pu 2s ease-in-out infinite}@keyframes pu{50%{transform:scale(1.15)}}"
    b = '<g class="or">'
    atoms = [(180, 40, ORANGE, 18), (264, 86, BLUE, 16), (248, 178, TEAL, 18), (112, 178, BLUE, 16), (96, 86, GOLD, 14)]
    for x, y, c, r in atoms:
        b += f'<line x1="180" y1="118" x2="{x}" y2="{y}" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/>'
    for i, (x, y, c, r) in enumerate(atoms):
        b += f'<circle class="pu" style="animation-delay:{i * .4}s" cx="{x}" cy="{y}" r="{r}" fill="{c}"/>'
    b += f'</g><circle cx="180" cy="118" r="28" fill="{NAVY}"/>'
    return _svg(b, st, **k)


def il_neural(**k):
    st = ".sg{stroke-dasharray:10 90;animation:sg 1.8s linear infinite}@keyframes sg{from{stroke-dashoffset:100}to{stroke-dashoffset:0}}.nd{transform-box:fill-box;transform-origin:center;animation:nd 2.4s ease-in-out infinite}@keyframes nd{50%{transform:scale(1.25)}}"
    L = [[(60, 50), (60, 118), (60, 186)], [(180, 34), (180, 92), (180, 150), (180, 208)], [(300, 80), (300, 156)]]
    b = ""
    k2 = 0
    for a, bb in ((0, 1), (1, 2)):
        for p in L[a]:
            for q in L[bb]:
                b += f'<path d="M{p[0]} {p[1]} L{q[0]} {q[1]}" stroke="{GREY}" stroke-width="3"/><path class="sg" pathLength="100" style="animation-delay:{(k2 % 7) * .25:.2f}s" d="M{p[0]} {p[1]} L{q[0]} {q[1]}" stroke="{TEAL}" stroke-width="4" stroke-linecap="round"/>'
                k2 += 1
    cols = [BLUE, LBLUE, ORANGE]
    for li, layer in enumerate(L):
        for j, (x, y) in enumerate(layer):
            b += f'<circle class="nd" style="animation-delay:{(li + j) * .3:.1f}s" cx="{x}" cy="{y}" r="15" fill="{cols[li]}"/>'
    return _svg(b, st, **k)


def il_eye(**k):
    st = ".lid{transform-origin:180px 118px;animation:lid 5s ease-in-out infinite}@keyframes lid{0%,44%,52%,100%{transform:scaleY(1)}48%{transform:scaleY(.08)}}.pp{animation:pp 5s ease-in-out infinite}@keyframes pp{0%,20%{transform:translateX(0)}30%,40%{transform:translateX(-30px)}60%,70%{transform:translateX(30px)}85%,100%{transform:translateX(0)}}"
    b = (f'<g class="lid"><path d="M40 118 C100 40 260 40 320 118 C260 196 100 196 40 118 Z" fill="#FFFFFF" stroke="{NAVY}" stroke-width="8"/>'
         f'<g class="pp"><circle cx="180" cy="118" r="44" fill="{BLUE}"/><circle cx="180" cy="118" r="20" fill="{NAVY}"/><circle cx="194" cy="104" r="8" fill="#FFFFFF"/></g></g>')
    return _svg(b, st, **k)


def il_phish(**k):
    st = ".hk{animation:hk 3.4s ease-in-out infinite}@keyframes hk{0%,100%{transform:translateY(-40px)}45%,60%{transform:translateY(0)}}.en{animation:en 3.4s ease-in-out infinite}@keyframes en{0%,45%{transform:translateY(0)}60%{transform:translateY(-6px)}100%{transform:translateY(0)}}"
    b = (f'<g class="hk"><path d="M250 0 V96 C250 122 220 122 220 100" fill="none" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/><path d="M220 100 l-10 -10" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/></g>'
         f'<g class="en"><rect x="80" y="110" width="200" height="110" rx="14" fill="#FFFFFF" stroke="{BLUE}" stroke-width="6"/><path d="M84 116 L180 180 L276 116" fill="none" stroke="{BLUE}" stroke-width="6" stroke-linejoin="round"/>'
         f'<circle cx="270" cy="114" r="22" fill="{ORANGE}"/><rect x="267" y="100" width="6" height="18" rx="3" fill="#FFFFFF"/><circle cx="270" cy="125" r="3.5" fill="#FFFFFF"/></g>')
    return _svg(b, st, **k)


def il_people(**k):
    st = ".cp{transform-box:fill-box;transform-origin:center;animation:cp 6s ease-out infinite;opacity:0}@keyframes cp{0%{transform:scale(0);opacity:0}8%,88%{transform:scale(1);opacity:1}100%{opacity:0}}"
    b = ""
    cols = [BLUE, TEAL, LBLUE, ORANGE, TEAL, BLUE]
    for i in range(6):
        r, c = divmod(i, 3)
        x, y = 90 + c * 90, 60 + r * 100
        b += f'<g class="cp" style="animation-delay:{i * .3:.1f}s;fill:{cols[i]}"><circle cx="{x}" cy="{y}" r="20"/><path d="M{x - 32} {y + 64} C{x - 32} {y + 24} {x + 32} {y + 24} {x + 32} {y + 64} Z"/></g>'
    return _svg(b, st, **k)


def il_clock(**k):
    st = ".mh{transform-origin:180px 118px;animation:mh 6s linear infinite}@keyframes mh{to{transform:rotate(360deg)}}.hh{transform-origin:180px 118px;animation:mh 72s linear infinite}.ar{animation:ar 6s linear infinite;stroke-dasharray:540;stroke-dashoffset:540}@keyframes ar{to{stroke-dashoffset:0}}"
    b = (f'<circle cx="180" cy="118" r="96" fill="#FFFFFF" stroke="{NAVY}" stroke-width="10"/><circle class="ar" cx="180" cy="118" r="86" fill="none" stroke="{ORANGE}" stroke-width="10" transform="rotate(-90 180 118)"/>'
         f'<g class="hh"><path d="M180 118 V76" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"/></g><g class="mh"><path d="M180 118 V52" stroke="{BLUE}" stroke-width="6" stroke-linecap="round"/></g><circle cx="180" cy="118" r="9" fill="{NAVY}"/>')
    return _svg(b, st, **k)


def il_checklist(**k):
    st = ".ck{stroke-dasharray:60;stroke-dashoffset:60;animation:ck 6s ease-in-out infinite}@keyframes ck{0%,10%{stroke-dashoffset:60}20%,90%{stroke-dashoffset:0}100%{stroke-dashoffset:60}}"
    b = f'<rect x="70" y="14" width="220" height="208" rx="16" fill="#FFFFFF" stroke="{GREY}" stroke-width="3"/>'
    for i in range(3):
        y = 50 + i * 60
        b += (f'<rect x="96" y="{y}" width="36" height="36" rx="8" fill="{PALE2}" stroke="{BLUE}" stroke-width="3"/><rect x="150" y="{y + 12}" width="{110 - i * 14}" height="12" rx="6" fill="{GREY}"/>'
              f'<path class="ck" style="animation-delay:{0.4 + i * 0.9:.1f}s" d="M104 {y + 18} L113 {y + 28} L128 {y + 8}" fill="none" stroke="{GREEN}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>')
    return _svg(b, st, **k)


def il_server(**k):
    st = ".ld{animation:ld 1.2s steps(2) infinite}@keyframes ld{50%{opacity:.2}}"
    b = ""
    for i in range(4):
        y = 22 + i * 50
        b += (f'<rect x="96" y="{y}" width="168" height="40" rx="8" fill="{NAVY}"/><rect x="116" y="{y + 16}" width="70" height="8" rx="4" fill="{LBLUE}" opacity=".5"/>'
              f'<circle class="ld" style="animation-delay:{i * .3:.1f}s" cx="228" cy="{y + 20}" r="6" fill="{GREEN if i != 2 else ORANGE}"/><circle class="ld" style="animation-delay:{i * .3 + .15:.2f}s" cx="246" cy="{y + 20}" r="6" fill="{TEAL}"/>')
    b += f'<path d="M40 216 H320" stroke="{GREY}" stroke-width="6" stroke-linecap="round"/>'
    return _svg(b, st, **k)


def il_freezer(**k):
    st = ".lv{transform-box:fill-box;transform-origin:center bottom;animation:lv 5s ease-in-out infinite}@keyframes lv{0%,100%{transform:scaleY(1)}50%{transform:scaleY(.35)}}.sn{transform-origin:270px 70px;animation:sn 8s linear infinite}@keyframes sn{to{transform:rotate(360deg)}}.al{animation:al 5s ease-in-out infinite}@keyframes al{0%,40%,100%{opacity:0}50%,80%{opacity:1}}"
    b = (f'<rect x="150" y="16" width="44" height="160" rx="22" fill="#FFFFFF" stroke="{NAVY}" stroke-width="8"/><circle cx="172" cy="190" r="34" fill="{BLUE}" stroke="{NAVY}" stroke-width="8"/>'
         f'<rect class="lv" x="164" y="60" width="16" height="130" rx="8" fill="{BLUE}"/>'
         f'<g class="sn" stroke="{TEAL}" stroke-width="6" stroke-linecap="round"><path d="M270 30 V110 M235 50 L305 90 M235 90 L305 50"/></g>'
         f'<g class="al"><circle cx="86" cy="80" r="30" fill="{ORANGE}"/><rect x="82" y="62" width="8" height="24" rx="4" fill="#FFFFFF"/><circle cx="86" cy="96" r="5" fill="#FFFFFF"/></g>')
    return _svg(b, st, **k)


def il_chat(**k):
    st = ".tp{animation:tp 1.2s ease-in-out infinite}@keyframes tp{0%,100%{transform:translateY(0);opacity:.4}50%{transform:translateY(-8px);opacity:1}}.wb{transform-box:fill-box;transform-origin:center;animation:wb 2.4s ease-in-out infinite}@keyframes wb{0%,100%{transform:rotate(-8deg)}50%{transform:rotate(8deg)}}"
    b = (f'<path d="M50 30 H270 a20 20 0 0 1 20 20 V140 a20 20 0 0 1 -20 20 H130 L90 196 V160 H50 a20 20 0 0 1 -20 -20 V50 a20 20 0 0 1 20 -20 Z" fill="#FFFFFF" stroke="{BLUE}" stroke-width="6"/>'
         f'<circle class="tp" cx="110" cy="96" r="12" fill="{LBLUE}"/><circle class="tp" style="animation-delay:.2s" cx="160" cy="96" r="12" fill="{LBLUE}"/><circle class="tp" style="animation-delay:.4s" cx="210" cy="96" r="12" fill="{LBLUE}"/>'
         f'<g class="wb"><circle cx="296" cy="176" r="34" fill="{ORANGE}"/><path d="M286 162 C286 150 306 150 306 162 C306 172 296 172 296 182" fill="none" stroke="#FFFFFF" stroke-width="6" stroke-linecap="round"/><circle cx="296" cy="194" r="4" fill="#FFFFFF"/></g>')
    return _svg(b, st, **k)


def il_book(**k):
    b = (f'<path d="M180 50 C150 30 90 30 60 40 V190 C90 180 150 180 180 200 Z" fill="{PALE2}" stroke="{SKY}" stroke-width="4"/>'
         f'<path d="M180 50 C210 30 270 30 300 40 V190 C270 180 210 180 180 200 Z" fill="{PALE2}" stroke="{SKY}" stroke-width="4"/>'
         + "".join(f'<path d="M84 {70 + i * 22} C110 {64 + i * 22} 140 {64 + i * 22} 160 {74 + i * 22}" stroke="{SKY}" stroke-width="4" fill="none"/>' for i in range(5)))
    return _svg(b, "", **k)


def il_flag(**k):
    st = ".t{stroke-dasharray:1000;stroke-dashoffset:1000;animation:d 6s ease-in-out infinite}@keyframes d{0%{stroke-dashoffset:1000}60%,90%{stroke-dashoffset:0}100%{stroke-dashoffset:0;opacity:0}}.fl{transform-box:fill-box;transform-origin:bottom left;animation:w 1.6s ease-in-out infinite alternate}@keyframes w{to{transform:skewY(-8deg)}}"
    b = (f'<path d="M20 220 C110 220 90 140 180 140 C270 140 250 70 330 60" fill="none" stroke="{GREY}" stroke-width="5" stroke-dasharray="4 12" stroke-linecap="round"/>'
         f'<path class="t" pathLength="1000" d="M20 220 C110 220 90 140 180 140 C270 140 250 70 330 60" fill="none" stroke="{ORANGE}" stroke-width="6" stroke-linecap="round"/>'
         f'<circle cx="20" cy="220" r="9" fill="{ORANGE}"/><circle cx="180" cy="140" r="9" fill="{ORANGE}"/><path d="M330 60 V10" stroke="{NAVY}" stroke-width="6" stroke-linecap="round"/><path class="fl" d="M330 12 H290 L302 26 L290 40 H330 Z" fill="{TEAL}"/>')
    return _svg(b, st, **k)


def il_target(**k):
    st = ".ar{animation:ar 3s cubic-bezier(.5,0,.2,1) infinite}@keyframes ar{0%{transform:translate(120px,-70px);opacity:0}30%{opacity:1}45%,85%{transform:translate(0,0);opacity:1}100%{opacity:0}}.hit{transform-box:fill-box;transform-origin:center;animation:hit 3s ease-out infinite;opacity:0}@keyframes hit{0%,44%{transform:scale(.4);opacity:0}48%{opacity:.8}75%{transform:scale(1.6);opacity:0}100%{opacity:0}}"
    b = (f'<circle cx="160" cy="128" r="92" fill="#FFFFFF" stroke="{GREY}" stroke-width="4"/><circle cx="160" cy="128" r="64" fill="{PALE}"/><circle cx="160" cy="128" r="38" fill="{LBLUE}"/><circle cx="160" cy="128" r="14" fill="{NAVY}"/>'
         f'<circle class="hit" cx="160" cy="128" r="30" fill="none" stroke="{ORANGE}" stroke-width="5"/>'
         f'<g class="ar"><path d="M160 128 L286 52" stroke="{NAVY}" stroke-width="7" stroke-linecap="round"/><path d="M286 52 l-4 22 l22 -10 z M286 52 l-22 -2 l12 16 z" fill="{ORANGE}"/></g>')
    return _svg(b, st, **k)


def il_layers(**k):
    st = ".ly{animation:ly 4s ease-in-out infinite}@keyframes ly{50%{transform:translateY(-10px)}}"
    b = ""
    for i, c in enumerate([ORANGE, TEAL, BLUE]):
        y = 150 - i * 52
        b += f'<g class="ly" style="animation-delay:{i * .4:.1f}s"><path d="M180 {y - 40} L300 {y} L180 {y + 40} L60 {y} Z" fill="{c}" opacity=".92"/></g>'
    return _svg(b, st, **k)


def il_chain(**k):
    st = ".mv{animation:mv 3s linear infinite}@keyframes mv{from{transform:translateX(0)}to{transform:translateX(220px)}}"
    b = ""
    for i, c in enumerate([BLUE, TEAL, ORANGE]):
        x = 30 + i * 110
        b += f'<rect x="{x}" y="86" width="80" height="64" rx="14" fill="{c}"/><rect x="{x + 18}" y="104" width="44" height="10" rx="5" fill="#FFFFFF" opacity=".7"/><rect x="{x + 18}" y="122" width="30" height="10" rx="5" fill="#FFFFFF" opacity=".5"/>'
    b += f'<path d="M110 118 H140 M220 118 H250" stroke="{NAVY}" stroke-width="6" stroke-dasharray="4 6"/>'
    b += "".join(f'<circle class="mv" style="animation-delay:-{j}s" cx="40" cy="190" r="8" fill="{GOLD}"/>' for j in range(3))
    b += f'<path d="M30 190 H300" stroke="{GREY}" stroke-width="4"/>'
    return _svg(b, st, **k)


def il_gauge(**k):
    st = ".nd{transform-origin:180px 180px;animation:nd 5s ease-in-out infinite}@keyframes nd{0%,100%{transform:rotate(-70deg)}50%{transform:rotate(50deg)}}"
    b = (f'<path d="{_arc(180, 180, 110, 140, math.pi, math.pi * 1.33)}" fill="{ORANGE}"/><path d="{_arc(180, 180, 110, 140, math.pi * 1.34, math.pi * 1.66)}" fill="{GOLD}"/><path d="{_arc(180, 180, 110, 140, math.pi * 1.67, math.pi * 2)}" fill="{GREEN}"/>'
         f'<g class="nd"><path d="M180 180 L180 66" stroke="{NAVY}" stroke-width="10" stroke-linecap="round"/></g><circle cx="180" cy="180" r="18" fill="{NAVY}"/>')
    return _svg(b, st, **k)


def il_ai(**k):
    st = ".sp{transform-box:fill-box;transform-origin:center;animation:sp 2s ease-in-out infinite}@keyframes sp{0%,100%{transform:scale(.5);opacity:.3}50%{transform:scale(1);opacity:1}}"
    star = lambda x, y, r, c: f'<path class="sp" style="animation-delay:{(x % 7) * .2:.1f}s" d="M{x} {y - r} C{x + r * .2} {y - r * .2} {x + r * .2} {y - r * .2} {x + r} {y} C{x + r * .2} {y + r * .2} {x + r * .2} {y + r * .2} {x} {y + r} C{x - r * .2} {y + r * .2} {x - r * .2} {y + r * .2} {x - r} {y} C{x - r * .2} {y - r * .2} {x - r * .2} {y - r * .2} {x} {y - r} Z" fill="{c}"/>'
    b = (f'<rect x="100" y="56" width="160" height="124" rx="28" fill="{NAVY}"/><circle cx="146" cy="116" r="14" fill="{AQUA}"/><circle cx="214" cy="116" r="14" fill="{AQUA}"/><rect x="150" y="146" width="60" height="8" rx="4" fill="{LBLUE}"/>'
         f'<path d="M180 56 V30" stroke="{NAVY}" stroke-width="6"/><circle cx="180" cy="26" r="9" fill="{ORANGE}"/>' + star(60, 70, 22, GOLD) + star(300, 60, 16, TEAL) + star(296, 180, 22, ORANGE) + star(54, 180, 14, LBLUE))
    return _svg(b, st, **k)


def il_pulse_bar():
    """ECG along the bottom edge (x-embed, like the Skill Tracker cover)."""
    return ('<x-embed style="position:absolute;top:968px;left:0px;width:1920px;height:96px"><!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;height:100%;background:transparent;overflow:hidden}svg{display:block;width:100%;height:100%}'
            'path{fill:none;stroke-linecap:round;stroke-linejoin:round}.b{stroke:#7FD1C9;stroke-opacity:.2;stroke-width:3}.p{stroke:#7FD1C9;stroke-width:4;stroke-dasharray:120 880;animation:m 3.6s linear infinite}@keyframes m{from{stroke-dashoffset:1000}to{stroke-dashoffset:0}}@media (prefers-reduced-motion:reduce){.p{animation:none}}</style></head><body>'
            '<svg viewBox="0 0 1920 96" preserveAspectRatio="none"><path class="b" pathLength="1000" d="M0 60H620l24 0 18-36 24 66 26-82 24 70 18-18H1180l24 0 18-36 24 66 26-82 24 70 18-18H1920"/><path class="p" pathLength="1000" d="M0 60H620l24 0 18-36 24 66 26-82 24 70 18-18H1180l24 0 18-36 24 66 26-82 24 70 18-18H1920"/></svg></body></html></x-embed>')


def bg_network():
    """Full-bleed animated network for dark slides (inline SVG)."""
    import random
    rnd = random.Random(7)
    pts = [(rnd.randint(30, 1890), rnd.randint(30, 1050)) for _ in range(34)]
    lines = ""
    for i, (x, y) in enumerate(pts):
        best = sorted(pts, key=lambda q: (q[0] - x) ** 2 + (q[1] - y) ** 2)[1:3]
        for q in best:
            lines += f'<line x1="{x}" y1="{y}" x2="{q[0]}" y2="{q[1]}"/>'
    nodes = "".join(f'<circle class="n" style="animation-delay:-{(i * 0.37) % 4:.2f}s" cx="{x}" cy="{y}" r="{4 if i % 3 else 6}"/>' for i, (x, y) in enumerate(pts))
    st = (".g1{animation:dr 26s ease-in-out infinite alternate}.l line{stroke:#7FD1C9;stroke-opacity:.12;stroke-width:1.5}.n{fill:#7FD1C9;opacity:.25;animation:tw 4s ease-in-out infinite}"
          "@keyframes tw{0%,100%{opacity:.12}50%{opacity:.6}}@keyframes dr{from{transform:translate(0,0)}to{transform:translate(18px,-12px)}}")
    b = (f'<defs><radialGradient id="ga" cx="1500" cy="540" r="800" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#24507F" stop-opacity=".55"/><stop offset="1" stop-color="#13294B" stop-opacity="0"/></radialGradient>'
         f'<radialGradient id="gb" cx="0" cy="1080" r="900" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="#0E7C7B" stop-opacity=".22"/><stop offset="1" stop-color="#13294B" stop-opacity="0"/></radialGradient></defs>'
         f'<rect width="1920" height="1080" fill="url(#ga)"/><rect width="1920" height="1080" fill="url(#gb)"/><g class="g1"><g class="l">{lines}</g>{nodes}</g>')
    return _svg(b, st, w=1920, h=1080, left=0, top=0)


ILLUS = {n[3:]: f for n, f in globals().items() if n.startswith("il_") and n != "il_pulse_bar"}


def illus(name, **k):
    return ILLUS[name](**k)


# ───────────────────────── big CSF wheel (no text; labels painted as <p>) ─────────────────────────
FN = [("ID", "Identify"), ("PR", "Protect"), ("DE", "Detect"), ("RS", "Respond"), ("RC", "Recover")]


def wheel_svg(size, active=(), pulse=False, left=0, top=0, eid=None, dark=False):
    """CSF 2.0 wheel. active: codes lit (GV + any of ID PR DE RS RC). Returns (svg, centres) where centres maps code→(x,y) in slide px."""
    c = size / 2
    r0, r1 = size * 0.215, size * 0.49
    seg = 2 * math.pi / 5
    base = "#1B3866" if dark else "#FFFFFF"
    strk = "#36578A" if dark else GREY
    st = ".pl{transform-box:fill-box;transform-origin:center;animation:pl 2.4s ease-in-out infinite}@keyframes pl{50%{transform:scale(1.04)}}.rg{transform-box:fill-box;transform-origin:center;animation:rg 2.6s ease-out infinite}@keyframes rg{0%{transform:scale(.9);opacity:.6}100%{transform:scale(1.35);opacity:0}}"
    body = ""
    cents = {}
    for i, (code, _) in enumerate(FN):
        a0 = -math.pi / 2 - seg / 2 + i * seg + 0.02
        a1 = a0 + seg - 0.04
        on = code in active
        fill = BLUE if on else base
        cls = ' class="pl"' if (on and pulse) else ""
        body += f'<path{cls} d="{_arc(c, c, r0, r1, a0, a1)}" fill="{fill}" stroke="{strk if not on else fill}" stroke-width="3"/>'
        am = (a0 + a1) / 2
        rm = (r0 + r1) / 2
        cents[code] = (left + c + rm * math.cos(am), top + c + rm * math.sin(am))
    gon = "GV" in active
    if gon and pulse:
        body += f'<circle class="rg" cx="{c}" cy="{c}" r="{r0 - 10}" fill="none" stroke="{ORANGE}" stroke-width="6"/>'
    body += f'<circle cx="{c}" cy="{c}" r="{r0 - 10}" fill="{ORANGE if gon else base}" stroke="{strk if not gon else ORANGE}" stroke-width="3"/>'
    cents["GV"] = (left + c, top + c)
    i = f' id="{eid}"' if eid else ""
    svg = (f'<svg{i} aria-label="NIST CSF 2.0 wheel" width="{size}" height="{size}" viewBox="0 0 {size} {size}" style="position:absolute;left:{left}px;top:{top}px;width:{size}px;height:{size}px">'
           f'<style>{st}{RM}</style>{body}</svg>')
    return svg, cents


def wheel_labels(cents, size, active=(), dark=False, big=True, names=True):
    out = ""
    fs = 30 if big else 22
    for code, name in [("GV", "Govern")] + FN:
        x, y = cents[code]
        on = code in active
        col = ("#FFFFFF" if code != "GV" else NAVY) if on else (CREAM if dark else NAVY)
        w = 220 if big else 160
        label = name.upper() if names else code
        out += f'<p style="position:absolute;left:{x - w / 2:.0f}px;top:{y - fs * 0.75:.0f}px;width:{w}px;font-size:{fs}px;font-weight:700;letter-spacing:2px;text-align:center;color:{col}">{label}</p>'
    return out


def write_deck(root, title, order_sections, slides, faces=None):
    os.makedirs(os.path.join(root, "project", "slides"), exist_ok=True)
    for sid, html_ in slides:
        open(os.path.join(root, "project", "slides", f"{sid}.html"), "w").write(html_)
    deck = {"v": 4, "createdOnFiles": {"v": 1, "at": "2026-10-21T11:30:00Z"}, "lists": "css", "title": title,
            "order": [s for s, _ in slides], "sections": order_sections,
            "faces": faces or {"source-serif-4": {"family": "Source Serif 4", "href": "https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400..700&display=swap"},
                                "ibm-plex-sans": {"family": "IBM Plex Sans", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap"},
                                "ibm-plex-mono": {"family": "IBM Plex Mono", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&display=swap"}},
            "designSystems": []}
    json.dump(deck, open(os.path.join(root, "project", "deck.json"), "w"), ensure_ascii=False)
    return deck
