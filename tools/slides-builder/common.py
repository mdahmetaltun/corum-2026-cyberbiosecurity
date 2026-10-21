from kit import *

SPEAKER = "Prof. Dr. Ahmet Altun"
AFFIL = "Sivas Cumhuriyet University · Faculty of Medicine"
EVENT = "Cyberbiosecurity Training Workshop · Hitit University · Çorum"


class Deck:
    def __init__(self, foot):
        self.foot = foot
        self.slides = []  # (id, builder) — builders get (i, n)

    def add(self, sid, fn):
        self.slides.append((sid, fn))

    def render(self):
        n = len(self.slides)
        return [(sid, fn(i, n)) for i, (sid, fn) in enumerate(self.slides)]


def content(d, sid, eyebrow, title, body, ill=None, notes="", dark=False, transition="fade", lines=1, foot=None, illus_html=None):
    """Standard content slide. body: html string (pinned children). lines: title lines (for callers' layout)."""
    def f(i, n):
        inner = progress(i, n, dark)
        if illus_html is not None:
            inner += illus_html
        elif ill:
            inner += illus(ill)
        inner += head(eyebrow, title, dark)
        inner += body
        inner += footer(foot or d.foot, i + 1, dark)
        return section(sid, inner, dark, transition, notes)
    d.add(sid, f)


def cover(d, sid, kicker, title_lines, sub, date_line, right_html, notes):
    def f(i, n):
        fs = 104 if len(title_lines) <= 2 else 92
        stp = round(fs * 1.115)
        tl = "".join(f'<h1 data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{330 + k * stp}px;width:1100px;font-family:{SERIF};font-size:{fs}px;font-weight:600;line-height:1.04;color:{CREAM}">{t}</h1>' for k, t in enumerate(title_lines))
        y2 = 330 + len(title_lines) * stp + 30
        inner = bg_network() + right_html
        inner += il_pulse_bar()
        inner += (f'<div data-build-in="fade 1 auto" style="position:absolute;left:128px;top:104px;width:1100px;display:flex;flex-direction:row;gap:18px;align-items:center">'
                  f'<svg aria-label="" viewBox="0 0 56 56" style="width:56px;height:56px"><rect width="56" height="56" rx="14" fill="#0E7C7B"/><path d="M28 10 L44 16 V28 C44 38 37 44 28 48 C19 44 12 38 12 28 V16 Z" fill="none" stroke="#F5F3EE" stroke-width="3.5" stroke-linejoin="round"/><path d="M21 28 L26 33 L36 23" fill="none" stroke="#F5F3EE" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
                  f'<p style="font-size:30px;font-weight:700;letter-spacing:1px;color:{CREAM}">Cyberbiosecurity</p>'
                  f'<p style="padding:6px 16px;font-size:24px;font-weight:600;letter-spacing:2px;color:{NAVY};background:{SAND};border-radius:20px">ÇORUM 2026</p></div>')
        inner += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:236px;width:1000px;font-size:24px;font-weight:600;line-height:1.45;letter-spacing:2px;text-transform:uppercase;color:{MINT}">{kicker}</p>'
        inner += tl
        inner += (f'<svg aria-label="" width="280" height="14" viewBox="0 0 280 14" style="position:absolute;left:128px;top:{y2}px;width:280px;height:14px"><style>.f{{animation:g 5s cubic-bezier(.6,0,.2,1) infinite}}@keyframes g{{0%{{stroke-dashoffset:272}}45%,60%{{stroke-dashoffset:0}}100%{{stroke-dashoffset:-272}}}}{RM}</style>'
                  f'<defs><linearGradient id="ag" x1="0" x2="1"><stop offset="0" stop-color="{MINT}"/><stop offset="1" stop-color="{SAND}"/></linearGradient></defs><line x1="4" y1="7" x2="276" y2="7" stroke="#2E4A72" stroke-width="8" stroke-linecap="round"/><line class="f" x1="4" y1="7" x2="276" y2="7" stroke="url(#ag)" stroke-width="8" stroke-linecap="round" stroke-dasharray="272 272" stroke-dashoffset="272"/></svg>')
        inner += f'<p data-build-in="fade 3 auto" style="position:absolute;left:128px;top:{y2 + 40}px;width:1000px;font-size:34px;line-height:1.32;color:{SKY}">{sub}</p>'
        inner += (f'<div data-build-in="fade 5 auto" style="position:absolute;left:128px;top:{max(772, y2 + 150)}px;width:1000px;display:flex;flex-direction:row;gap:22px;align-items:center">'
                  f'<div style="width:6px;height:132px;background:{SAND};border-radius:3px"></div><div style="display:flex;flex-direction:column;gap:4px">'
                  f'<p style="font-size:32px;font-weight:600;color:{CREAM}">{SPEAKER}</p><p style="font-size:24px;color:{SKY}">{AFFIL}</p><p style="font-size:24px;color:{SKY}">{date_line}</p></div></div>')
        return section(sid, inner, True, "fade", notes)
    d.add(sid, f)


def video(d, sid, still, clip, alt, notes):
    def f(i, n):
        inner = f'<img src="{still}" data-video="{clip}" alt="{alt}" style="position:absolute;left:0px;top:0px;width:1920px;height:1080px;object-fit:cover">'
        return section(sid, inner, True, "fade", notes)
    d.add(sid, f)


def statement(d, sid, lines, notes, eyebrow="", sub="", bg=NAVY, transition="fade", ill_html="", colors=None, size=96, top=None):
    """Big serif lines on navy, each building in."""
    def f(i, n):
        inner = progress(i, n, True) + bg_network() + ill_html
        total = len(lines) * size * 1.12 + (90 if sub else 0)
        y = top or ((1080 - total) / 2 + 10)
        if eyebrow:
            inner += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:{y - 60:.0f}px;width:1400px;font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{MINT}">{eyebrow}</p>'
        cols = colors or [CREAM] * len(lines)
        for k, t in enumerate(lines):
            inner += f'<h2 data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{y + k * size * 1.12:.0f}px;width:1560px;font-family:{SERIF};font-size:{size}px;font-weight:600;line-height:1.08;color:{cols[k]}">{t}</h2>'
        if sub:
            inner += f'<p data-build-in="fade {len(lines) + 2} auto" style="position:absolute;left:128px;top:{y + len(lines) * size * 1.12 + 36:.0f}px;width:1300px;font-size:32px;line-height:1.4;color:{SKY}">{sub}</p>'
        inner += footer(d.foot, i + 1, True)
        return section(sid, inner, True, transition, notes, bg=bg)
    d.add(sid, f)


def refs(d, sid, items, notes="Sources for this session. Every DOI on this slide was checked against Crossref."):
    def f(i, n):
        lis = "".join(f"<li>{t}</li>" for t in items)
        body = f'<div style="width:1400px;display:flex;flex-direction:column"><ol style="font-size:24px;line-height:1.45;color:{BODY2};padding-left:32px">{lis}</ol></div>'
        inner = progress(i, n) + illus("book") + head("Sources", "References and further reading") + body + footer(d.foot, i + 1)
        return section(sid, inner, False, "fade", notes)
    d.add(sid, f)


def thanks(d, sid, sub, notes):
    def f(i, n):
        inner = bg_network() + il_pulse_bar()
        inner += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:250px;width:1000px;font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{MINT}">Questions &amp; discussion</p>'
        inner += f'<h1 data-build-in="rise 2 auto" style="position:absolute;left:128px;top:310px;width:1300px;font-family:{SERIF};font-size:150px;font-weight:600;line-height:1;color:{CREAM}">Thank you.</h1>'
        inner += f'<p data-build-in="fade 3 auto" style="position:absolute;left:128px;top:500px;width:1100px;font-size:34px;line-height:1.35;color:{SKY}">{sub}</p>'
        inner += (f'<div data-build-in="fade 4 auto" style="position:absolute;left:128px;top:700px;width:1300px;display:flex;flex-direction:row;gap:22px;align-items:center">'
                  f'<div style="width:6px;height:120px;background:{SAND};border-radius:3px"></div><div style="display:flex;flex-direction:column;gap:4px">'
                  f'<p style="font-size:32px;font-weight:600;color:{CREAM}">{SPEAKER}</p><p style="font-size:24px;color:{SKY}">{AFFIL}</p>'
                  f'<p style="font-size:24px;color:{SKY}">aaltun@cumhuriyet.edu.tr · ORCID 0000-0003-2056-8683</p></div></div>')
        inner += illus("shield", left=1380, top=300, w=360, h=236)
        return section(sid, inner, True, "fade", notes)
    d.add(sid, f)


def lens(top, text, label="In the lab", build="rise 9 auto"):
    """Navy 'in the lab' strip."""
    return (f'<div data-build-in="{build}" style="position:absolute;left:128px;top:{top}px;width:1664px;display:flex;flex-direction:row;gap:30px;align-items:center;padding:26px 40px;background:{NAVY};border-radius:20px">'
            f'<x-icon name="Lightbulb" style="width:44px;height:44px;color:{SAND}"></x-icon>'
            f'<p style="width:190px;font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{SAND}">{label}</p>'
            f'<p style="flex:1;font-size:28px;line-height:1.38;color:{CREAM}">{text}</p></div>')


def src(text, top=900):
    return f'<p style="position:absolute;left:128px;top:{top}px;width:1500px;font-size:24px;color:{MUTE}">{text}</p>'
