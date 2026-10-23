"""Sivas 2026 slide kit — Çorum design grammar (1920×1080, eyebrow + title top-left, illustration top-right,
white cards with a 6px accent strip, callout strip, shimmering progress bar, staged build-ins) re-dressed in the
event identity: Kapsid mark, Canlı palette, Sora display + IBM Plex Sans/Mono."""
import html, json, math, os, re, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "slides-builder"))
import kit as _kit  # noqa: E402  (animated SVG illustrations, recoloured below)

# ── Canlı palette (Kapsid identity) ──
INK, INK0, INK2, INK3 = "#1D2554", "#121838", "#28316B", "#3A4590"
PAPER, PAPER2, WHITE = "#F5F7FF", "#EEF1FF", "#FFFFFF"
TEXT, BODY2, MUTE = "#1D2554", "#3B4374", "#4A5280"
T1, T2, T3, TT = "#8AF5E6", "#19E3C8", "#0FB09C", "#087F72"      # turquoise (TT = text on light)
V1, V2, V3 = "#7C6BFF", "#5B47FF", "#3A2BB8"                       # violet
P1, P2, PT = "#FF7AB0", "#FF3D8B", "#D9136A"                       # pink (PT = text on light)
AMBER, AMBERT = "#FFB627", "#9A5B00"
CREAM, SKY, LINE = "#F2F4FF", "#B4BCEA", "#DCE1F7"
VTINT, TTINT, PTINT, ATINT = "#ECE9FF", "#E2FBF7", "#FFE8F1", "#FFF4DC"

DISPLAY = "'Sora', 'IBM Plex Sans', Arial, sans-serif"
SANS = "'IBM Plex Sans', Arial, sans-serif"
MONO = "'IBM Plex Mono', monospace"
RM = "@media (prefers-reduced-motion:reduce){*{animation:none!important}}"
EMBPAL = dict(a=V2, b=T2, c=P2, d=AMBER, fg=CREAM)

FOOT = "Siber Biyogüvenlik Çalıştayı · Sivas · 16–17 Kasım 2026"
SPEAKER = "Prof. Dr. Ahmet Altun"
AFFIL = "Sivas Cumhuriyet Üniversitesi · Tıp Fakültesi"


def esc(s):
    return html.escape(s, quote=False)


# ── recolour the Çorum illustration library into Canlı ──
_MAP = {"#13294B": INK, "#F7F9FC": PAPER, "#1F2D45": TEXT, "#3A4A63": BODY2, "#5A6A82": MUTE,
        "#1662E8": V2, "#5B9BFF": V1, "#D6E6FF": VTINT, "#E8F0FF": PAPER2, "#00C2B2": T2, "#00968A": TT,
        "#7FD1C9": T1, "#3EDBCB": T2, "#FF7A1A": P2, "#EA5A0C": PT, "#FFB547": AMBER, "#F0C27A": AMBER,
        "#22C55E": T3, "#DCE3EC": LINE, "#F5F3EE": CREAM, "#B9C7DA": SKY}


def recolor(s):
    return re.sub(r"#[0-9A-Fa-f]{6}\b", lambda m: _MAP.get(m.group(0).upper(), m.group(0)), s).replace("rgba(19,41,75,", "rgba(29,37,84,")


def illus(name, **k):
    return recolor(_kit.illus(name, **k))


# ── chrome ──
def progress(i, n, dark=False):
    w = max(60, round(1920 * (i + 1) / n))
    track = "#FFFFFF" if dark else INK
    return (f'<svg aria-label="" width="1920" height="8" viewBox="0 0 1920 8" style="position:absolute;left:0px;top:0px;width:1920px;height:8px">'
            f'<style>.sh{{animation:sh 3.2s ease-in-out infinite}}@keyframes sh{{from{{transform:translateX(-240px)}}to{{transform:translateX({w}px)}}}}{RM}</style>'
            f'<defs><linearGradient id="pg" x1="0" x2="1"><stop offset="0" stop-color="{T2}"/><stop offset=".45" stop-color="{V2}"/><stop offset=".8" stop-color="{P2}"/><stop offset="1" stop-color="{AMBER}"/></linearGradient>'
            f'<linearGradient id="sg" x1="0" x2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset=".5" stop-color="#FFFFFF" stop-opacity=".8"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient>'
            f'<clipPath id="pc"><rect width="{w}" height="8"/></clipPath></defs><rect width="1920" height="8" fill="{track}" fill-opacity=".07"/>'
            f'<rect width="{w}" height="8" fill="url(#pg)"/><g clip-path="url(#pc)"><rect class="sh" width="240" height="8" fill="url(#sg)"/></g></svg>')


def footer(num, dark=False, left=FOOT):
    c = SKY if dark else MUTE
    return (f'<p style="position:absolute;left:128px;bottom:64px;width:1300px;font-size:24px;color:{c}">{left}</p>'
            f'<p style="position:absolute;right:128px;bottom:64px;width:120px;font-size:24px;color:{c};text-align:right">{num}</p>')


def mark_tiny(dark=False):
    """Small Kapsid mark beside the footer number (static)."""
    return kapsid_svg(40, 1652, 1004, small=True)


def head(eyebrow, title, dark=False, width=1300, eid=None):
    eb = T2 if dark else TT
    tc = CREAM if dark else INK
    i = f' id="{eid}"' if eid else ""
    return (f'<div style="width:{width}px;display:flex;flex-direction:column;gap:14px">'
            f'<p style="font-family:{MONO};font-size:24px;letter-spacing:3px;text-transform:uppercase;font-weight:600;color:{eb}">{eyebrow}</p>'
            f'<h2{i} style="font-family:{DISPLAY};font-size:56px;font-weight:700;letter-spacing:-1px;line-height:1.1;color:{tc}">{title}</h2></div>')


# Slides runtime accepts only these x-icon names; every other name used in the scripts maps onto one of them.
ICONS_OK = set("Activity Book Chart Chat Check CheckCircle Clock Cloud Code Database Globe GraduationCap Home Key Lightbulb Lightning Link Lock PaperPlane Play Search Settings Star ThumbsUp Tool Trust Users Verified Warning Wrench".split())
ICONMAP = {"FlaskConical": "Lightbulb", "Cable": "Link", "Scale": "Trust", "Gem": "Star", "DoorOpen": "Home", "Network": "Globe",
           "Handshake": "Users", "KeyRound": "Key", "FileWarning": "Warning", "UserX": "Users", "Triangle": "Activity", "TriangleAlert": "Warning",
           "Dna": "Activity", "ShieldCheck": "Verified", "Moon": "Clock", "CloudUpload": "Cloud", "UserMinus": "Users", "Repeat": "Link",
           "Smartphone": "Lock", "ClipboardList": "Check", "HardDrive": "Database", "PhoneCall": "Chat", "Laptop": "Code", "Fingerprint": "Lock",
           "MessageCircleQuestion": "Chat", "Award": "GraduationCap", "ShieldAlert": "Warning", "ListChecks": "CheckCircle", "Timer": "Clock",
           "UserRoundX": "Users", "Smile": "ThumbsUp", "Brain": "Lightbulb", "Layers": "Activity", "Hand": "Users", "BatteryCharging": "Lightning",
           "AtSign": "Chat", "Wifi": "Globe", "Printer": "Book", "Ban": "Warning", "RefreshCw": "Settings", "Copy": "Database", "QrCode": "Search",
           "House": "Home", "Nfc": "Key", "AppWindow": "Code", "SmartphoneNfc": "Key", "Siren": "Warning", "KeySquare": "Key", "HandMetal": "Users",
           "FileCheck": "CheckCircle", "SquareCheckBig": "CheckCircle", "Mail": "PaperPlane", "Unlink": "Link", "CircleHelp": "Chat",
           "MessageSquareText": "Chat", "BookOpen": "Book", "CalendarSync": "Clock", "Radar": "Activity", "CalendarDays": "Clock", "Camera": "Star",
           "Eye": "Search"}


def tr_upper(t):
    """Turkish-aware upper case that leaves HTML entities alone."""
    return re.sub(r"(&[a-zA-Z#0-9]+;)|([^&]+)", lambda m: m.group(1) or m.group(2).replace("i", "İ").replace("ı", "I").upper(), t)


def fix_upper(h):
    """Bake text-transform:uppercase into the text (the runtime may not honour lang="tr", so İ/I come out right)."""
    return re.sub(r'(<p [^>]*?)text-transform:uppercase;?([^>]*>)([^<]*)(</p>)', lambda m: m.group(1) + m.group(2) + tr_upper(m.group(3)) + m.group(4), h)


def fix_icons(h):
    def rep(m):
        n = ICONMAP.get(m.group(1), m.group(1))
        assert n in ICONS_OK, n
        return f'<x-icon name="{n}"'
    return re.sub(r'<x-icon name="([A-Za-z]+)"', rep, h)


def section(sid, inner, dark=False, transition="fade", notes="", bg=None, lang="tr"):
    bgc = bg or (INK if dark else PAPER)
    col = CREAM if dark else TEXT
    n = f"<aside>{esc(notes.strip())}</aside>" if notes else ""
    return fix_upper(fix_icons(f'<section id="{sid}" lang="{lang}" data-transition="{transition}" style="background:{bgc};color:{col};font-family:{SANS};'
                     f'padding:128px 128px 160px;display:flex;flex-direction:column;gap:12px">\n{inner}\n{n}\n</section>\n'))


def pin(left, top, width, inner, build=None, height=None, style="", tag="div", eid=None):
    b = f' data-build-in="{build}"' if build else ""
    h = f"height:{height}px;" if height else ""
    i = f' id="{eid}"' if eid else ""
    return f'<{tag}{i}{b} style="position:absolute;left:{left}px;top:{top}px;width:{width}px;{h}{style}">{inner}</{tag}>'


def P(text, size=28, color=None, weight=None, lh=1.4, extra="", font=None):
    c = f"color:{color};" if color else ""
    w = f"font-weight:{weight};" if weight else ""
    f = f"font-family:{font};" if font else ""
    return f'<p style="font-size:{size}px;line-height:{lh};{f}{c}{w}{extra}">{text}</p>'


def H(text, size=36, color=INK, lh=1.15, extra=""):
    return f'<p style="font-family:{DISPLAY};font-size:{size}px;font-weight:700;letter-spacing:-0.5px;line-height:{lh};color:{color};{extra}">{text}</p>'


def tag(text, bg=VTINT, color=V3, size=24):
    return f'<p style="font-family:{MONO};font-size:{size}px;font-weight:600;letter-spacing:1px;color:{color};background:{bg};padding:6px 14px;border-radius:10px">{text}</p>'


def card_style(accent=V2, bg=WHITE, pad="30px 32px", gap=12, shadow=True, radius=22, top_border=True, extra=""):
    sh = "box-shadow:0 12px 34px rgba(29,37,84,0.09);" if shadow else ""
    bt = f"border-top:6px solid {accent};" if top_border and accent else ""
    return f'display:flex;flex-direction:column;gap:{gap}px;background:{bg};padding:{pad};border-radius:{radius}px;{bt}{sh}{extra}'


ACC = [V2, T2, P2, AMBER, V1, T3]


def cards_row(items, top, n=None, gap=24, left=128, total=1664, build_start=1, kind="rise", height=None, accents=None,
              pad="30px 32px", bg=WHITE, ids=None, row_gap=None):
    n = n or len(items)
    w = (total - gap * (n - 1)) / n
    out = []
    acc = accents or ACC
    for k, inner in enumerate(items):
        r, c = divmod(k, n)
        st = card_style(acc[k % len(acc)], bg, pad)
        h = f"height:{height}px;" if height else ""
        y = top + r * ((height or 0) + (row_gap if row_gap is not None else gap))
        i = f' id="{ids[k]}"' if ids else ""
        b = f' data-build-in="{kind} {build_start + k} auto"' if kind else ""
        out.append(f'<div{i}{b} style="position:absolute;left:{left + c * (w + gap):.0f}px;top:{y}px;width:{w:.0f}px;{h}{st}">{inner}</div>')
    return "".join(out)


def callout(top, text, label="Laboratuvarda", icon="FlaskConical", build="rise 9 auto", dark_strip=True, left=128, width=1664):
    bg, tc, lc = (INK, CREAM, AMBER) if dark_strip else (VTINT, TEXT, V3)
    return (f'<div data-build-in="{build}" style="position:absolute;left:{left}px;top:{top}px;width:{width}px;display:flex;flex-direction:row;gap:28px;align-items:center;padding:24px 40px;background:{bg};border-radius:22px">'
            f'<x-icon name="{icon}" style="width:44px;height:44px;color:{lc}"></x-icon>'
            f'<p style="width:240px;font-family:{MONO};font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{lc}">{label}</p>'
            f'<p style="flex:1;font-size:28px;line-height:1.36;color:{tc}">{text}</p></div>')


def src(text, top=900, dark=False):
    return f'<p style="position:absolute;left:128px;top:{top}px;width:1560px;font-size:24px;color:{SKY if dark else MUTE}">{text}</p>'


def eyebrow(text, top, dark=True, build="fade 1 auto", width=1400, left=128):
    return (f'<p data-build-in="{build}" style="position:absolute;left:{left}px;top:{top}px;width:{width}px;font-family:{MONO};font-size:24px;'
            f'letter-spacing:3px;text-transform:uppercase;font-weight:600;color:{T2 if dark else TT}">{text}</p>')


def icon(name, size=48, color=V2):
    return f'<x-icon name="{name}" style="width:{size}px;height:{size}px;color:{color}"></x-icon>'


# ── Kapsid mark (exact geometry of the approved logo; 256 grid) ──
PAL = dict(t1=T1, t2=T2, t3=T3, v1=V1, v2=V2, v3=V3, p=P2, p2=P1, a=AMBER)


def _pol(cx, cy, r, deg):
    a = math.radians(deg)
    return (cx + r * math.cos(a), cy + r * math.sin(a))


def _inset(pts, gap):
    from shapely.geometry import Polygon
    g = Polygon(pts).buffer(-gap, join_style=2, mitre_limit=10)
    c = list(g.exterior.coords)[:-1]
    return "M" + " L".join(f"{x:.2f} {y:.2f}" for x, y in c) + " Z"


def kapsid_paths(c=PAL, mono=None, small=False, cls=True):
    cx, cy, R = 128, 130, 92
    r = R / 2
    Hh = [_pol(cx, cy, R, a) for a in (-90, -30, 30, 90, 150, 210)]
    I = [_pol(cx, cy, r, a) for a in (-90, 30, 150)]
    col = (lambda k: mono) if mono else (lambda k: c[k])
    faces = [((I[0], Hh[5], Hh[0]), "t1"), ((I[0], Hh[0], Hh[1]), "t2"), ((I[0], I[1], Hh[1]), "v1"),
             ((I[1], Hh[1], Hh[2]), "t3"), ((I[1], Hh[2], Hh[3]), "v2"), ((I[1], I[2], Hh[3]), "p"),
             ((I[2], Hh[3], Hh[4]), "v3"), ((I[2], Hh[4], Hh[5]), "v2"), ((I[2], I[0], Hh[5]), "t2")]
    gap = 4.0 if small else 2.4
    out = []
    for k, (pts, key) in enumerate(faces):
        cl = f' class="f f{k}"' if cls else ""
        out.append(f'<path{cl} fill="{col(key)}" d="{_inset(pts, gap)}"/>')
    m = lambda p, q: ((p[0] + q[0]) / 2, (p[1] + q[1]) / 2)
    m01, m12, m20 = m(I[0], I[1]), m(I[1], I[2]), m(I[2], I[0])
    if small:
        out.append(f'<path fill="{col("t1")}" d="{_inset((I[0], I[1], I[2]), gap)}"/>')
        if not mono:
            out.append(f'<path fill="{c["a"]}" d="{_inset((m01, m12, m20), 0.5)}"/>')
    else:
        for pts, key in [((I[0], m01, m20), "t1"), ((m01, I[1], m12), "p2"), ((m20, m12, I[2]), "v1")]:
            out.append(f'<path fill="{col(key)}" d="{_inset(pts, gap)}"/>')
        out.append(f'<path{" class=" + chr(34) + "core" + chr(34) if cls else ""} fill="{mono or c["a"]}" d="{_inset((m01, m12, m20), gap)}"/>')
        for k, (x, y) in enumerate(Hh):
            ang = math.atan2(y - cy, x - cx)
            x1, y1 = x + 7 * math.cos(ang), y + 7 * math.sin(ang)
            x2, y2 = x + 17 * math.cos(ang), y + 17 * math.sin(ang)
            sc = f' class="sp sp{k}"' if cls else ""
            out.append(f'<g{sc}><line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x2:.2f}" y2="{y2:.2f}" stroke="{mono or c["v3"]}" stroke-width="5" stroke-linecap="round"/>'
                       f'<circle cx="{x2:.2f}" cy="{y2:.2f}" r="6" fill="{mono or (c["a"] if k % 2 == 0 else c["p"])}"/></g>')
    return "".join(out)


def kapsid_svg(size, left, top, eid=None, animate=False, small=False, label="Kapsid logosu", build=None, mono=None):
    """Static or gently animated Kapsid mark. animate: facets breathe, spikes pulse, core glows."""
    st = ""
    if animate:
        st = (".f{transform-box:fill-box;transform-origin:center;animation:fb 4.2s ease-in-out infinite}"
              + "".join(f".f{k}{{animation-delay:-{k * .42:.2f}s}}" for k in range(9))
              + "@keyframes fb{0%,100%{transform:scale(1)}50%{transform:scale(.94)}}"
              ".sp{transform-box:view-box;transform-origin:128px 130px;animation:sp 2.4s ease-in-out infinite}"
              + "".join(f".sp{k}{{animation-delay:-{k * .4:.1f}s}}" for k in range(6))
              + "@keyframes sp{0%,100%{transform:scale(1)}50%{transform:scale(1.045)}}"
              ".core{transform-box:fill-box;transform-origin:center;animation:cg 2.4s ease-in-out infinite}@keyframes cg{0%,100%{opacity:1}50%{opacity:.55}}" + RM)
    i = f' id="{eid}"' if eid else ""
    b = f' data-build-in="{build}"' if build else ""
    return (f'<svg{i}{b} aria-label="{label}" width="{size}" height="{size}" viewBox="0 0 256 256" style="position:absolute;left:{left}px;top:{top}px;width:{size}px;height:{size}px">'
            + (f"<style>{st}</style>" if st else "") + kapsid_paths(small=small, cls=animate, mono=mono) + "</svg>")


def brand_row(top=104, left=128, tagtext="SİVAS 2026", dark=True, build="fade 1 auto"):
    """Kapsid + SİBER BİYOGÜVENLİK wordmark row used on covers."""
    wc = "#FFFFFF" if dark else INK
    ac = P2 if dark else PT
    return (f'<div data-build-in="{build}" style="position:absolute;left:{left}px;top:{top}px;width:1200px;height:64px;display:flex;flex-direction:row;gap:18px;align-items:center">'
            f'<svg aria-label="Kapsid" viewBox="0 0 256 256" style="width:64px;height:64px">{kapsid_paths(small=True, cls=False)}</svg>'
            f'<p style="font-family:{DISPLAY};font-size:30px;font-weight:800;letter-spacing:-0.5px;color:{wc}">SİBER <span style="color:{ac}">BİYO</span>GÜVENLİK</p>'
            f'<p style="font-family:{MONO};padding:6px 16px;font-size:24px;font-weight:600;letter-spacing:2px;color:{INK};background:{T2};border-radius:20px">{tagtext}</p></div>')


# ── backdrops ──
def bg_glow(seed=3, a=V2, b=T2):
    """Dark backdrop: two radial glows + a sparse drifting lattice of capsid-like hexagons (inline SVG)."""
    import random
    rnd = random.Random(seed)
    hexes = ""
    for k in range(16):
        x, y, r = rnd.randint(60, 1860), rnd.randint(60, 1020), rnd.choice([18, 26, 34])
        pts = " ".join(f"{x + r * math.cos(math.radians(-90 + 60 * j)):.0f},{y + r * math.sin(math.radians(-90 + 60 * j)):.0f}" for j in range(6))
        hexes += f'<polygon class="hx" style="animation-delay:-{k * .7:.1f}s" points="{pts}"/>'
    st = (f".g1{{animation:dr 28s ease-in-out infinite alternate}}.hx{{fill:none;stroke:{T1};stroke-opacity:.14;stroke-width:2;animation:tw 6s ease-in-out infinite}}"
          "@keyframes tw{0%,100%{stroke-opacity:.06}50%{stroke-opacity:.28}}@keyframes dr{from{transform:translate(0,0)}to{transform:translate(22px,-14px)}}")
    body = (f'<defs><radialGradient id="ga" cx="1520" cy="420" r="900" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{a}" stop-opacity=".42"/><stop offset="1" stop-color="{INK}" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="gb" cx="80" cy="1080" r="900" gradientUnits="userSpaceOnUse"><stop offset="0" stop-color="{b}" stop-opacity=".2"/><stop offset="1" stop-color="{INK}" stop-opacity="0"/></radialGradient></defs>'
            f'<rect width="1920" height="1080" fill="url(#ga)"/><rect width="1920" height="1080" fill="url(#gb)"/><g class="g1">{hexes}</g>')
    return (f'<svg aria-label="" width="1920" height="1080" viewBox="0 0 1920 1080" style="position:absolute;left:0px;top:0px;width:1920px;height:1080px">'
            f'<style>{st}{RM}</style>{body}</svg>')


def write_deck(root, title, sections, slides):
    os.makedirs(os.path.join(root, "project", "slides"), exist_ok=True)
    for f in os.listdir(os.path.join(root, "project", "slides")):
        os.remove(os.path.join(root, "project", "slides", f))
    for sid, h in slides:
        with open(os.path.join(root, "project", "slides", f"{sid}.html"), "w", encoding="utf-8") as fh:
            fh.write(h)
    deck = {"v": 4, "createdOnFiles": {"v": 1, "at": "2026-10-23T09:00:00Z"}, "lists": "css", "title": title,
            "order": [s for s, _ in slides], "sections": sections,
            "faces": {"sora": {"family": "Sora", "href": "https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700;800&display=swap"},
                      "ibm-plex-sans": {"family": "IBM Plex Sans", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&display=swap"},
                      "ibm-plex-mono": {"family": "IBM Plex Mono", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&display=swap"}},
            "designSystems": []}
    with open(os.path.join(root, "project", "deck.json"), "w", encoding="utf-8") as fh:
        json.dump(deck, fh, ensure_ascii=False)
    return deck


class Deck:
    def __init__(self, title):
        self.title = title
        self.slides = []

    def add(self, sid, fn):
        self.slides.append((sid, fn))

    def render(self):
        n = len(self.slides)
        return [(sid, fn(i, n)) for i, (sid, fn) in enumerate(self.slides)]
