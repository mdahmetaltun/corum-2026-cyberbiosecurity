"""Slide builders shared by the four Sivas decks."""
from skit import *
from sanim import emb

PAL = EMBPAL


def content(d, sid, eyebrow_, title, body, ill=None, notes="", dark=False, transition="fade", illus_html=None, title_id=None):
    def f(i, n):
        inner = progress(i, n, dark)
        if dark:
            inner = progress(i, n, True) + bg_glow(len(sid))
        if illus_html is not None:
            inner += illus_html
        elif ill:
            inner += illus(ill)
        inner += head(eyebrow_, title, dark, eid=title_id) + body + footer(i + 1, dark)
        return section(sid, inner, dark, transition, notes)
    d.add(sid, f)


def cover(d, sid, kicker, title_lines, sub, right_html, notes, tagtext="SİVAS 2026", size=96):
    def f(i, n):
        stp = round(size * 1.08)
        inner = bg_glow(1) + right_html + brand_row(tagtext=tagtext)
        inner += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:236px;width:1080px;font-family:{MONO};font-size:24px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:{T2}">{kicker}</p>'
        for k, (t, c) in enumerate(title_lines):
            inner += (f'<h1 data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{300 + k * stp}px;width:1150px;font-family:{DISPLAY};'
                      f'font-size:{size}px;font-weight:800;letter-spacing:-2.5px;line-height:1.02;color:{c or CREAM}">{t}</h1>')
        y2 = 300 + len(title_lines) * stp + 28
        inner += (f'<svg aria-label="" width="300" height="14" viewBox="0 0 300 14" style="position:absolute;left:128px;top:{y2}px;width:300px;height:14px"><style>.f{{animation:g 5s cubic-bezier(.6,0,.2,1) infinite}}@keyframes g{{0%{{stroke-dashoffset:292}}45%,60%{{stroke-dashoffset:0}}100%{{stroke-dashoffset:-292}}}}{RM}</style>'
                  f'<defs><linearGradient id="ag" x1="0" x2="1"><stop offset="0" stop-color="{T2}"/><stop offset=".5" stop-color="{V1}"/><stop offset="1" stop-color="{P2}"/></linearGradient></defs><line x1="4" y1="7" x2="296" y2="7" stroke="{INK3}" stroke-width="8" stroke-linecap="round"/><line class="f" x1="4" y1="7" x2="296" y2="7" stroke="url(#ag)" stroke-width="8" stroke-linecap="round" stroke-dasharray="292 292" stroke-dashoffset="292"/></svg>')
        inner += f'<p data-build-in="fade {len(title_lines) + 2} auto" style="position:absolute;left:128px;top:{y2 + 40}px;width:1080px;font-size:34px;line-height:1.32;color:{SKY}">{sub}</p>'
        inner += (f'<div data-build-in="fade {len(title_lines) + 3} auto" style="position:absolute;left:128px;top:{max(800, y2 + 150)}px;width:1100px;display:flex;flex-direction:row;gap:22px;align-items:center">'
                  f'<div style="width:6px;height:120px;background:{P2};border-radius:3px"></div><div style="display:flex;flex-direction:column;gap:4px">'
                  f'<p style="font-size:32px;font-weight:600;color:{CREAM}">{SPEAKER}</p><p style="font-size:24px;color:{SKY}">{AFFIL}</p>'
                  f'<p style="font-size:24px;color:{SKY}">Hilton Garden Inn Sivas · 16–17 Kasım 2026</p></div></div>')
        return section(sid, inner, True, "fade", notes)
    d.add(sid, f)


def video(d, sid, still, clip, alt, notes):
    def f(i, n):
        inner = f'<img src="{still}" data-video="{clip}" alt="{alt}" style="position:absolute;left:0px;top:0px;width:1920px;height:1080px;object-fit:cover">'
        return section(sid, inner, True, "fade", notes, bg=INK0)
    d.add(sid, f)


def kinetic(d, sid, eyebrow_, words, notes, size=150, gap=0.55, transition="push"):
    """words: [(text, colour)] — each slams in, then a light sweep."""
    def f(i, n):
        inner = progress(i, n, True) + emb("particles", 0, 0, 1920, 1080, PAL)
        inner += eyebrow(eyebrow_, 150)
        inner += emb("kinetic", 128, 220, 1664, 680, PAL, words=[[w, c or CREAM] for w, c in words], size=size, lh=1.12, gap=gap, weight=900)
        inner += footer(i + 1, True)
        return section(sid, inner, True, transition, notes, bg=INK0)
    d.add(sid, f)


def morph(d, sid, eyebrow_, words, notes, size=230, sub="", per=3.2, transition="push"):
    """Particle typography morph through words [(text, colour)]."""
    def f(i, n):
        inner = progress(i, n, True) + bg_glow(9, a=V3, b=P2)
        inner += eyebrow(eyebrow_, 160)
        inner += emb("morph", 96, 250, 1728, 470, PAL, words=[[w, c or CREAM] for w, c in words], size=size, per=per, n=1900, weight=800)
        if sub:
            inner += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:770px;width:1664px;font-size:34px;line-height:1.35;color:{SKY};text-align:center">{sub}</p>'
        inner += footer(i + 1, True)
        return section(sid, inner, True, transition, notes, bg=INK0)
    d.add(sid, f)


def statement(d, sid, lines, notes, eyebrow_="", sub="", right_html="", size=88, top=None, transition="fade", width=1560):
    """Big display lines on ink, building one by one. lines: [(text, colour)]."""
    def f(i, n):
        inner = progress(i, n, True) + bg_glow(len(sid) + 4) + right_html
        total = len(lines) * size * 1.1 + (110 if sub else 0)
        y = top or ((1080 - total) / 2)
        if eyebrow_:
            inner += eyebrow(eyebrow_, round(y - 64))
        for k, (t, c) in enumerate(lines):
            inner += (f'<h2 data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{y + k * size * 1.1:.0f}px;width:{width}px;font-family:{DISPLAY};'
                      f'font-size:{size}px;font-weight:800;letter-spacing:-2px;line-height:1.06;color:{c or CREAM}">{t}</h2>')
        if sub:
            inner += f'<p data-build-in="fade {len(lines) + 2} auto" style="position:absolute;left:128px;top:{y + len(lines) * size * 1.1 + 40:.0f}px;width:{min(width, 1400)}px;font-size:32px;line-height:1.4;color:{SKY}">{sub}</p>'
        inner += footer(i + 1, True)
        return section(sid, inner, True, transition, notes)
    d.add(sid, f)


def refs(d, sid, items, notes="Bu oturumun kaynakları. DOI'li her kaynak Crossref'te doğrulandı; DOI'si olmayan resmî belgeler kurum ve tarihle verildi.", size=24):
    def f(i, n):
        lis = "".join(f"<li>{t}</li>" for t in items)
        body = f'<div style="width:1664px;display:flex;flex-direction:column"><ol style="font-size:{size}px;line-height:1.42;color:{BODY2};padding-left:32px">{lis}</ol></div>'
        inner = progress(i, n) + illus("book") + head("Kaynaklar", "Kaynaklar ve ileri okuma") + body + footer(i + 1)
        return section(sid, inner, False, "fade", notes)
    d.add(sid, f)


def thanks(d, sid, sub, notes, title="Teşekkürler.", tsize=140):
    def f(i, n):
        inner = bg_glow(2) + emb("capsid", 1220, 170, 600, 600, PAL, rings=True, spin=.35, t1=T1, v1=V1, v3=V3)
        inner += eyebrow("Sorular ve tartışma", 250)
        inner += f'<h1 data-build-in="rise 2 auto" style="position:absolute;left:128px;top:310px;width:1100px;font-family:{DISPLAY};font-size:{tsize}px;font-weight:800;letter-spacing:-4px;line-height:1;white-space:nowrap;color:{CREAM}">{title}</h1>'
        inner += f'<p data-build-in="fade 3 auto" style="position:absolute;left:128px;top:490px;width:1050px;font-size:34px;line-height:1.35;color:{SKY}">{sub}</p>'
        inner += (f'<div data-build-in="fade 4 auto" style="position:absolute;left:128px;top:720px;width:1300px;display:flex;flex-direction:row;gap:22px;align-items:center">'
                  f'<div style="width:6px;height:120px;background:{P2};border-radius:3px"></div><div style="display:flex;flex-direction:column;gap:4px">'
                  f'<p style="font-size:32px;font-weight:600;color:{CREAM}">{SPEAKER}</p><p style="font-size:24px;color:{SKY}">{AFFIL}</p>'
                  f'<p style="font-family:{MONO};font-size:24px;color:{SKY}">aaltun@cumhuriyet.edu.tr · ORCID 0000-0003-2056-8683</p></div></div>')
        return section(sid, inner, True, "fade", notes)
    d.add(sid, f)


def numcard(num, title, text, color=V2, numsize=64):
    return (f'<p style="font-family:{DISPLAY};font-size:{numsize}px;font-weight:800;letter-spacing:-2px;line-height:1;color:{color}">{num}</p>'
            + H(title, 32) + P(text, 26, BODY2, lh=1.38))
