from common import *

D = Deck("Institutional Cybersecurity Infrastructure · Case Study · Çorum 2026")
VID = ("/_blob/0fe0ca6065718d92160418c654701716", "/_blob/e1f833bee17e1b7243afe344e9f80b49")


def navy(sid, notes, ill=None, il_left=1430, il_top=90, transition="fade"):
    """decorator: body(i,n) -> inner html for a navy slide."""
    def wrap(body):
        def f(i, n):
            inner = progress(i, n, True) + bg_network() + (illus(ill, left=il_left, top=il_top) if ill else "")
            inner += body(i, n) + footer(D.foot, i + 1, True)
            return section(sid, inner, True, transition, notes)
        D.add(sid, f)
        return body
    return wrap


def eyebrow(text, top, dark=True, build="fade 1 auto", width=1300):
    return f'<p data-build-in="{build}" style="position:absolute;left:128px;top:{top}px;width:{width}px;font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{MINT if dark else TEALT}">{text}</p>'


def rings_svg(size, left, top, eid="rings", dark=True):
    c = size / 2
    st = (".r{transform-box:fill-box;transform-origin:center;animation:r 3.2s ease-out infinite}.r2{animation-delay:1.06s}.r3{animation-delay:2.13s}"
          "@keyframes r{0%{transform:scale(.35);opacity:.9}100%{transform:scale(1);opacity:0}}"
          ".sp{transform-origin:50% 50%;animation:sp 24s linear infinite}@keyframes sp{to{transform:rotate(360deg)}}" + RM)
    b = ""
    for k, (r, col, dash) in enumerate([(0.48, LBLUE, "14 12"), (0.36, BLUE, ""), (0.24, TEAL, "")]):
        b += f'<circle cx="{c}" cy="{c}" r="{size * r:.0f}" fill="none" stroke="{col}" stroke-width="4" {"stroke-dasharray=" + chr(34) + dash + chr(34) if dash else ""} opacity=".8"/>'
    for k in range(3):
        b += f'<circle class="r r{k + 1}" cx="{c}" cy="{c}" r="{size * 0.48:.0f}" fill="none" stroke="{SAND}" stroke-width="3"/>'
    b += f'<g class="sp"><circle cx="{c}" cy="{c - size * 0.48:.0f}" r="10" fill="{SAND}"/><circle cx="{c + size * 0.36:.0f}" cy="{c}" r="8" fill="{MINT}"/></g>'
    b += f'<circle cx="{c}" cy="{c}" r="{size * 0.12:.0f}" fill="{ORANGE}"/>'
    return (f'<svg id="{eid}" aria-label="Concentric rings around a protected core" width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
            f'style="position:absolute;left:{left}px;top:{top}px;width:{size}px;height:{size}px"><style>{st}</style>{b}</svg>')


# 1 cover
cover(D, "cover", "Day 2 · Tuesday 3 November 2026 · 11:30–12:30",
      ["Institutional", "Cybersecurity", "Infrastructure"], "A practical case study",
      "Cyberbiosecurity Training Workshop · Hitit University, Çorum",
      rings_svg(560, 1200, 230, eid="ringsc"),
      """This session is practical. We take one large real incident to see how infrastructure fails, then walk through a composite case: a university central research laboratory that serves external industry clients, assessed and rebuilt in two phases.

Everything maps back to the CSF functions from yesterday, so this afternoon's exercise will feel familiar.""")
video(D, "film", VID[0], VID[1], "Opening film: the timeline of the 2021 Irish health service ransomware attack",
      "Opening film, about 15 seconds: the 2021 HSE attack, from the first email to detonation eight weeks later. Advance when it reaches the title card.")

# 3 HSE timeline
EV = [("16 Mar 2021", "Malicious email reaches a workstation", BLUE), ("18 Mar", "Opened; an Excel file downloads; foothold gained", BLUE),
      ("31 Mar", "Antivirus detects activity, but it is in monitor mode", ORANGE), ("7–13 May", "Provider reports unhandled threats on 16+ systems", ORANGE),
      ("14 May, 04:00", "Conti ransomware detonates; IT taken offline nationally", ORANGE)]
tl_svg = (f'<svg aria-label="" width="1664" height="20" viewBox="0 0 1664 20" style="position:absolute;left:128px;top:300px;width:1664px;height:20px">'
          f'<style>.l{{stroke-dasharray:1664;stroke-dashoffset:1664;animation:l 2.4s cubic-bezier(.6,0,.2,1) forwards}}@keyframes l{{to{{stroke-dashoffset:0}}}}{RM}</style>'
          f'<line x1="0" y1="10" x2="1664" y2="10" stroke="{GREY}" stroke-width="4"/><line class="l" x1="0" y1="10" x2="1664" y2="10" stroke="{ORANGE}" stroke-width="4"/></svg>')
body = tl_svg
for k, (d, t, col) in enumerate(EV):
    x = 128 + k * 336
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:{x}px;top:296px;width:304px;display:flex;flex-direction:column;gap:12px">'
             f'<div style="width:28px;height:28px;background:{col};border-radius:14px;border:5px solid {PAPER}"></div>'
             f'<p style="font-size:24px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:{ORANGET if col == ORANGE else TEALT}">{d}</p>'
             f'<p style="font-size:28px;line-height:1.32;color:{TEXT}">{t}</p></div>')
items = [f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{TEALT}">Dwell time</p>' + bignum("≈ 8 weeks", BLUE, 72),
         f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{TEALT}">Immediate response cost</p>' + bignum("€53 m", BLUE, 72) + P("HSE figure to the Dáil Public Accounts Committee", 24, MUTE),
         f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{ORANGET}">Root finding (PwC)</p>' + P("Fragmented legacy IT, never designed to resist attack, and no single owner of cyber risk.", 28, TEXT, lh=1.35)]
body += cards_row(items, top=600, build_start=6, accent_cycle=[BLUE, BLUE, ORANGE], pad="26px 30px")
content(D, "hse", "Health Service Executive, Ireland · 2021", "Eight weeks from first email to ransomware", body, ill="timeline",
        notes="""Build the timeline one click per event. The details come from the independent PwC post-incident review published in December 2021.

The orange dots are the moments the organisation could have acted: antivirus saw it on 31 March but was set to monitor only; a week before detonation the security provider reported unhandled threats on at least sixteen systems. The last cards show the cost and the root finding, which is a governance finding, not a technical one.""")

statement(D, "lesson", ["The signals were there.", "The structure to act", "on them was not."],
          """The core message of the session. Technology detected the intrusion; the organisation did not respond. That is why yesterday GOVERN was at the centre of the wheel.""",
          sub="Infrastructure is not only hardware. It is who owns the risk, who watches, and who may decide.",
          size=110, colors=[CREAM, SAND, SAND], ill_html=illus("bell", left=1430, top=90))

# 5 three layers
LY = [("01", "Technical", "Networks, instrument PCs, accounts, logs, backups", BLUE, "Settings"),
      ("02", "People", "Staff, students, client technicians, vendor engineers", ORANGE, "Users"),
      ("03", "Physical", "Doors, freezers, cabinets, sample stores, USB ports", TEAL, "Lock")]
items = [f'<x-icon name="{ic}" style="width:56px;height:56px;color:{col}"></x-icon>' + bignum(nm, col, 110) + f'<h3 style="font-family:{SERIF};font-size:60px;font-weight:600;color:{NAVY}">{t}</h3>' + P(b, 28, BODY2)
         for nm, t, b, col, ic in LY]
body = cards_row(items, top=290, accent_cycle=[BLUE, ORANGE, TEAL], pad="36px 40px", height=470)
body += callout(800, "A weakness in any one layer opens the other two. The people layer is usually the cheapest to attack.", label="Remember", icon="Warning", build="rise 4 auto")
content(D, "layers", "Three layers of every institution", "Technical, people, physical", body, ill="layers",
        notes="""The same three layers we use in social engineering training. Keep them in mind; every finding in the case belongs to one of them, and the people layer is usually the cheapest to attack.""")

# 6 facility
FAC = [("40+", "instruments, many with a dedicated control PC", BLUE), ("60", "users: staff, students, visiting client technicians", BLUE),
       ("12", "external industry clients sending samples and data", ORANGE), ("8", "vendors with some form of remote support access", BLUE)]
items = [bignum(a, col, 110) + P(b, 28, BODY2, lh=1.35) for a, b, col in FAC]
body = cards_row(items, top=300, accent_cycle=[BLUE, BLUE, ORANGE, BLUE], pad="30px 32px", height=330)
body += lens(700, "Client samples and data make this a supply-chain node: a breach here is a breach for twelve companies. In CSF terms, GV.SC is the centre of gravity.", label="Why it matters", build="rise 5 auto")
content(D, "facility", "The case · a composite, not one real institution", "A core lab that also serves industry", body, ill="server",
        notes="""A composite built from typical core facilities; the numbers are illustrative. If you wish, relate it to our own work at Sivas Cumhuriyet University's central research centre, where this external-client angle shaped our project design.

The defining feature is the external clients. A university lab that only serves its own researchers has an internal risk; a facility that holds twelve companies' samples and data is part of their supply chain.""")


# 7 phases (navy)
@navy("phases", """Two phases. First assess, then build and train. The order matters: without an inventory and a Current Profile you cannot know which investments close which gaps.""", ill="stairs")
def _(i, n):
    h = eyebrow("Two phases · ten weeks", 200)
    h += (f'<div id="ph1" data-build-in="left 2 auto" style="position:absolute;left:128px;top:300px;width:760px;height:440px;display:flex;flex-direction:column;gap:18px;justify-content:center;background:#1B3866;padding:48px;border-radius:24px">'
          f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{MINT}">Phase 1 · weeks 1–4</p>'
          f'<h2 style="font-family:{SERIF};font-size:120px;font-weight:600;line-height:1;color:{CREAM}">Assess</h2><p style="font-size:30px;line-height:1.4;color:{SKY}">Inventory, network map, interviews, Current Profile</p></div>')
    h += (f'<svg aria-label="" data-build-in="fade 3 auto" width="120" height="120" viewBox="0 0 120 120" style="position:absolute;left:900px;top:460px;width:120px;height:120px">'
          f'<style>.a{{animation:a 1.4s ease-in-out infinite}}@keyframes a{{50%{{transform:translateX(14px)}}}}{RM}</style><path class="a" d="M20 30 L70 60 L20 90" fill="none" stroke="{SAND}" stroke-width="12" stroke-linecap="round" stroke-linejoin="round"/></svg>')
    h += (f'<div data-build-in="right 4 auto" style="position:absolute;left:1032px;top:300px;width:760px;height:440px;display:flex;flex-direction:column;gap:18px;justify-content:center;background:{SAND};padding:48px;border-radius:24px">'
          f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{NAVY}">Phase 2 · weeks 5–10</p>'
          f'<h2 style="font-family:{SERIF};font-size:120px;font-weight:600;line-height:1;color:{NAVY}">Build &amp; train</h2><p style="font-size:30px;line-height:1.4;color:{NAVY}">Segmentation, identity, logging, backups, plans, people</p></div>')
    h += f'<p data-build-in="fade 5 auto" style="position:absolute;left:128px;top:800px;width:1600px;font-size:30px;line-height:1.4;color:{SKY}">Assessment first, then targeted investment. Buying tools before the inventory is the most common and most expensive mistake.</p>'
    return h


# 8 crown jewels
def jewels_svg():
    s = 760
    c = s / 2
    st = (".p{transform-box:fill-box;transform-origin:center;animation:p 2.4s ease-in-out infinite}@keyframes p{50%{transform:scale(1.06)}}"
          ".sw{transform-origin:380px 380px;animation:sw 6s linear infinite}@keyframes sw{to{transform:rotate(360deg)}}"
          ".d{stroke-dasharray:14 12;animation:d 3s linear infinite}@keyframes d{to{stroke-dashoffset:-52}}" + RM)
    b = f'<defs><linearGradient id="swg" x1="0" x2="1"><stop offset="0" stop-color="{ORANGE}" stop-opacity="0"/><stop offset="1" stop-color="{ORANGE}" stop-opacity=".35"/></linearGradient></defs>'
    b += f'<circle class="d" cx="{c}" cy="{c}" r="360" fill="#FFFFFF" stroke="{BLUE}" stroke-width="5"/>'
    b += f'<circle cx="{c}" cy="{c}" r="270" fill="{PALE}" stroke="{BLUE}" stroke-width="5"/>'
    b += f'<circle cx="{c}" cy="{c}" r="180" fill="#FFF3EA" stroke="{ORANGET}" stroke-width="5"/>'
    b += f'<g class="sw"><path d="M{c} {c} L{c + 360} {c} A360 360 0 0 0 {c + 360 * math.cos(-0.6):.1f} {c + 360 * math.sin(-0.6):.1f} Z" fill="url(#swg)"/></g>'
    b += f'<circle class="p" cx="{c}" cy="{c}" r="96" fill="{ORANGE}"/>'
    return f'<svg aria-label="Attack surface rings around the crown jewels" width="{s}" height="{s}" viewBox="0 0 {s} {s}" style="position:absolute;left:128px;top:250px;width:640px;height:640px"><style>{st}</style>{b}</svg>'


import math
RG = [("Perimeter", "internet, email, vendors, cloud LIMS", BLUE, 268), ("Endpoints &amp; accounts", "PCs, laptops, shared logins", BLUE, 326), ("Lab devices &amp; OT", "instrument PCs, freezer and room monitors", ORANGET, 400)]
body = jewels_svg()
body += f'<p style="position:absolute;left:298px;top:536px;width:300px;font-size:24px;font-weight:700;letter-spacing:2px;text-align:center;line-height:1.15;color:{NAVY}">CROWN<br>JEWELS</p>'
for k, (t, x, col, _) in enumerate(RG):
    body += (f'<div data-build-in="left {k + 1} auto" style="position:absolute;left:860px;top:{290 + k * 110}px;width:932px;display:flex;flex-direction:row;gap:22px;align-items:center">'
             f'<div style="width:34px;height:34px;border-radius:17px;border:5px solid {col}"></div><div style="display:flex;flex-direction:column;gap:2px"><h3 style="font-size:32px;font-weight:600;color:{NAVY}">{t}</h3><p style="font-size:26px;color:{BODY2}">{x}</p></div></div>')
JW = ["Client samples, results and contracts", "Instrument control and calibration data", "The cold chain: −80 °C storage and its alarms", "Unpublished research data and IP"]
body += (f'<div data-build-in="rise 4 auto" style="position:absolute;left:860px;top:640px;width:932px;display:flex;flex-direction:column;gap:10px;background:{NAVY};padding:28px 36px;border-radius:20px">'
         f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{SAND}">The crown jewels</p>'
         + "".join(f'<p style="font-size:28px;line-height:1.3;color:{CREAM}">· {j}</p>' for j in JW) + "</div>")
content(D, "jewels", "Phase 1 · ID.AM, ID.RA", "Start from what must never be lost", body, illus_html="",
        notes="""Build from the outside in: perimeter, endpoints and accounts, laboratory devices, and finally the crown jewels. Ask the room what their own crown jewels are before revealing the list.

The cold chain is the item people forget: a freezer alarm on Wi-Fi is a cyber asset with a biosafety consequence.""")

# 9 findings
FIND = [("High", "Instrument PCs on unsupported Windows versions, cannot be patched", "PR.PS"),
        ("High", "One flat network: office PCs, Wi-Fi and instruments share a segment", "PR.IR"),
        ("High", "Shared logins on instrument PCs; client technicians use staff accounts", "PR.AA"),
        ("High", "Vendor remote-support tools installed and always on", "GV.SC"),
        ("Med", "Results moved by USB stick between instruments and analysis PCs", "PR.DS"),
        ("Med", "No central logging; instrument PC clocks drift by minutes", "DE.CM"),
        ("High", "Backups exist; nobody has ever tested a restore", "RC.RP"),
        ("Med", "No incident plan names the biosafety officer", "RS.MA")]
body = ""
for k, (s, t, c) in enumerate(FIND):
    r, cc = k % 4, k // 4
    hot = s == "High"
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:{128 + cc * 844}px;top:{290 + r * 140}px;width:820px;height:120px;display:flex;flex-direction:row;gap:20px;align-items:center;background:#FFFFFF;padding:18px 24px;border-radius:16px;border-left:8px solid {ORANGE if hot else BLUE};box-shadow:0 8px 24px rgba(19,41,75,0.07)">'
             f'<p style="width:90px;font-size:24px;font-weight:700;text-align:center;color:{"#FFFFFF" if hot else NAVY};background:{ORANGET if hot else PALE2};padding:6px 0;border-radius:10px">{s}</p>'
             f'<p style="flex:1;font-size:26px;line-height:1.3;color:{TEXT}">{t}</p>{chip(c)}</div>')
body += src("Illustrative findings typical of shared research facilities; not from a single audit", 860)
content(D, "findings", "Phase 1 output · typical findings", "Eight findings, eight CSF subcategories", body, ill="scan",
        notes="""Eight findings that appear in almost every assessment of a shared research facility. These are illustrative, not from one audit. Note how each one maps to a CSF subcategory family; that mapping is what turns a list of complaints into a Current Profile.

Ask: how many of these would be true in your own building?""")


# 10 Schneier
@navy("schneier", """A line I use in every training. Technical controls raise the cost of attacking systems, so attackers go around them, through people.""", ill="people", transition="fade")
def _(i, n):
    h = eyebrow("The people layer", 260)
    h += f'<h2 data-build-in="rise 2 auto" style="position:absolute;left:128px;top:330px;width:1600px;font-family:{SERIF};font-size:120px;font-weight:600;line-height:1.08;color:{CREAM}">“Amateurs hack systems,</h2>'
    h += f'<h2 data-build-in="rise 3 auto" style="position:absolute;left:128px;top:470px;width:1600px;font-family:{SERIF};font-size:120px;font-weight:600;line-height:1.08;color:{SAND}">professionals hack people.”</h2>'
    h += f'<p data-build-in="fade 4 auto" style="position:absolute;left:128px;top:680px;width:1200px;font-size:30px;color:{SKY}">Bruce Schneier · security technologist</p>'
    return h


# 11 SE phases
PH = [("Research", "Staff names on the website, vendor names in public tender documents, instrument models in published papers", BLUE),
      ("Develop", "A friendly call from the “sequencer vendor’s service engineer” who knows the model and the lab head’s name", BLUE),
      ("Exploit", "“Please install this remote-support tool before Monday’s firmware update.”", ORANGE)]
items = [bignum(str(k + 1), col, 96) + f'<h3 style="font-family:{SERIF};font-size:52px;font-weight:600;color:{NAVY}">{a}</h3>' + P(b, 28, BODY2, lh=1.38) for k, (a, b, col) in enumerate(PH)]
body = cards_row(items, top=290, accent_cycle=[BLUE, BLUE, ORANGE], pad="30px 34px", height=420)
body += lens(760, "Vendor access only through the jump host, requested by ticket, verified by a call-back to a known number.", label="Defence", build="rise 4 auto")
content(D, "se", "Social engineering, applied to the case", "Three phases, all in plain sight", body, ill="phish",
        notes="""Research, develop, exploit: the three phases from my social engineering module, applied to our facility. Nothing in the research phase is secret; it is all public.

The countermeasure is a process, not a product: a ticket and a call-back to a number you already hold.""")


# 12 pressures (navy)
@navy("pressures", """Ego, sympathy, intimidation. Every training example in my deck falls into one of these. The practical rule for staff: when a request comes with urgency and secrecy together, stop and verify through a different channel.""", ill="chat")
def _(i, n):
    h = eyebrow("Three pressures attackers use", 180)
    PR = [("Ego", "“You are the only one who really understands this system.”", MINT),
          ("Sympathy", "“I will lose my job if this is not fixed today.”", SKY),
          ("Intimidation", "“This is the rector’s office / the regulator. Do it now and keep it quiet.”", SAND)]
    for k, (a, b, col) in enumerate(PR):
        h += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:{128 + k * 563}px;top:330px;width:539px;height:420px;display:flex;flex-direction:column;gap:22px;background:#1B3866;padding:40px 38px;border-radius:22px;border-top:8px solid {col}">'
              f'<h2 style="font-family:{SERIF};font-size:64px;font-weight:600;color:{col}">{a}</h2><p style="font-size:32px;line-height:1.38;color:{CREAM}">{b}</p></div>')
    h += f'<p data-build-in="fade 5 auto" style="position:absolute;left:128px;top:800px;width:1600px;font-size:30px;line-height:1.4;color:{SKY}"><b style="color:{SAND}">Urgency plus secrecy</b> is the signature. Train people to pause on both, and make reporting easy and blame-free.</p>'
    return h


# 13 target architecture
def zone(x, y, w, h, title, sub, build, bg="#FFFFFF", border=GREY, tc=NAVY, sc=BODY2, eid=None, dash=False):
    idt = f' id="{eid}"' if eid else ""
    return (f'<div{idt} data-build-in="{build}" style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;display:flex;flex-direction:column;gap:6px;justify-content:center;background:{bg};padding:18px 24px;border-radius:16px;border:{4 if border != GREY else 2}px {"dashed" if dash else "solid"} {border}">'
            f'<p style="font-size:30px;font-weight:700;color:{tc}">{title}</p>' + "".join(f'<p style="font-size:24px;line-height:1.3;color:{sc}">{s}</p>' for s in sub) + "</div>")


flow = (f'<svg aria-label="" width="1664" height="620" viewBox="0 0 1664 620" style="position:absolute;left:128px;top:270px;width:1664px;height:620px">'
        f'<style>.f{{stroke-dasharray:10 10;animation:f 1.2s linear infinite}}@keyframes f{{to{{stroke-dashoffset:-40}}}}{RM}</style>'
        f'<g fill="none" stroke-width="4">'
        f'<path class="f" d="M210 310 L270 310" stroke="{MUTE}"/>'
        f'<path class="f" d="M460 290 C510 290 500 95 560 95" stroke="{MUTE}"/>'
        f'<path class="f" d="M460 330 C510 330 500 525 560 525" stroke="{MUTE}"/>'
        f'<path class="f" d="M105 380 C105 560 180 560 262 560" stroke="{ORANGET}"/>'
        f'<path class="f" d="M480 540 C530 540 520 330 560 320" stroke="{ORANGET}"/>'
        f'<path class="f" d="M1080 95 L1170 95" stroke="{BLUE}"/><path class="f" d="M1080 310 L1170 310" stroke="{BLUE}"/><path class="f" d="M1080 525 L1170 525" stroke="{BLUE}"/>'
        f'<path class="f" d="M1400 310 L1450 310" stroke="{ORANGET}"/></g></svg>')
body = flow
body += zone(128, 520, 210, 120, "Internet", ["email · clients · vendors"], "fade 1 auto", bg=PALE2, border=PALE2)
body += zone(398, 520, 190, 120, "Firewall", [], "fade 1 auto", bg=NAVY, border=NAVY, tc=CREAM)
body += zone(688, 270, 520, 180, "Campus IT zone", ["email, office PCs, Wi-Fi, students"], "rise 1 auto")
body += zone(688, 485, 520, 200, "Lab OT zone · own VLAN", ["instrument PCs, freezer monitors", "no internet by default · named accounts"], "rise 1 auto", border=BLUE, tc=BLUE)
body += zone(688, 720, 520, 170, "Client data enclave", ["separated per client · access by contract"], "rise 1 auto")
body += zone(350, 730, 300, 160, "Jump host", ["vendor access only", "MFA · recorded · ticketed"], "pop 2 auto", bg=ORANGE, border=ORANGE, sc=NAVY)
body += zone(1298, 270, 230, 620, "Central logging", ["NTP-synced clocks", "defined retention"], "left 3 auto", bg=NAVY, border=NAVY, tc=CREAM, sc=SKY)
body += zone(1578, 485, 214, 405, "Offline backup", ["immutable copy", "restore tested"], "pop 4 auto", bg="#FFF3EA", border=ORANGET, tc=ORANGET, dash=True)
content(D, "arch", "Phase 2 · target architecture · PR.IR, PR.AA, DE.CM, RC.RP", "Segment, gate, watch, keep a copy", body, illus_html="",
        notes="""Build the target architecture in four clicks. First the zones: campus IT, a separate lab network with no internet by default, and a client data enclave. Second, the vendor jump host: the only way in for remote support, with MFA, session recording and time limits. Third, central logging with synchronised clocks. Fourth, an offline, immutable backup whose restore has been tested.

Each element closes one of the findings a few slides back.""")


# 14 Change Healthcare (navy)
@navy("change", """The largest health-data breach on record in the United States: 192.7 million individuals, from one portal without MFA.

This is PR.AA in practice. For our facility it means the vendor jump host and any VPN or remote desktop path.""", ill="key" if False else "lock")
def _(i, n):
    h = eyebrow("Identity lesson · Change Healthcare · February 2024", 170)
    h += f'<p data-build-in="pop 2 auto" style="position:absolute;left:128px;top:220px;width:1000px;font-family:{SERIF};font-size:250px;font-weight:600;line-height:1;color:{CREAM}">192.7</p>'
    h += f'<p data-build-in="fade 3 auto" style="position:absolute;left:840px;top:390px;width:600px;font-size:44px;font-weight:600;color:{SAND}">million people</p>'
    h += f'<p data-build-in="rise 4 auto" style="position:absolute;left:128px;top:510px;width:1500px;font-size:38px;line-height:1.38;color:{SKY}">The attackers entered through a remote-access portal that <b style="color:{CREAM}">did not require multi-factor authentication</b>.</p>'
    h += (f'<div data-build-in="rise 5 auto" style="position:absolute;left:128px;top:690px;width:1664px;display:flex;flex-direction:row;gap:30px;align-items:center;background:{SAND};padding:28px 40px;border-radius:20px">'
          f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{NAVY}">Rule</p><p style="font-family:{SERIF};font-size:44px;font-weight:600;color:{NAVY}">MFA on every remote path, and vendor paths first.</p></div>')
    h += f'<p style="position:absolute;left:128px;top:880px;width:1500px;font-size:24px;color:{SKY}">Figure as reported to the U.S. HHS Office for Civil Rights, July 2025</p>'
    return h


# 15 Synnovis
items = [bignum("10,146", BLUE, 96) + P("outpatient appointments postponed", 28, BODY2), bignum("1,705", BLUE, 96) + P("elective procedures postponed", 28, BODY2),
         bignum("2025", ORANGET, 96) + P("King’s College Hospital confirmed the attack was one contributing factor in a patient’s death", 27, BODY2, lh=1.35)]
body = pin(128, 270, 1300, P("One laboratory services provider. Two hospital trusts. Months of disruption.", 34, BODY2, lh=1.32), build="fade 1 auto")
body += cards_row(items, top=360, build_start=2, accent_cycle=[BLUE, BLUE, ORANGE], pad="30px 34px", height=300)
body += lens(720, "Turn it around: we are someone else’s Synnovis. Contracts with security and notification clauses, per-client separation, and a plan to tell every client within hours.", label="For a facility", build="rise 5 auto")
content(D, "synnovis", "Supply-chain lesson · Synnovis pathology · June 2024", "When the lab is the supplier", body, ill="chain",
        notes="""Synnovis provided pathology services to King's College Hospital and Guy's and St Thomas'. NHS England's cumulative figures to mid-September 2024: 10,146 outpatient appointments and 1,705 elective procedures postponed. In June 2025 King's confirmed that the attack was one contributing factor in a patient's death.

Turn it around: our facility is someone else's Synnovis. GV.SC applies in both directions.""")

# 16 telemetry
LOGS = ["Firewall", "Identity / directory", "Jump host sessions", "Instrument PC events", "LIMS audit trail", "Freezer &amp; room alarms"]
body = ""
for k, l in enumerate(LOGS):
    r, c = divmod(k, 2)
    hot = k == 5
    body += f'<p data-build-in="pop {1} auto" style="position:absolute;left:{128 + c * 380}px;top:{300 + r * 100}px;width:356px;font-size:28px;font-weight:600;text-align:center;color:{"#FFFFFF" if hot else NAVY};background:{ORANGET if hot else PALE2};padding:20px 12px;border-radius:14px">{l}</p>'
RU = [("Synchronise every clock", "Without NTP, a timeline across instruments cannot be rebuilt.", BLUE),
      ("Collect centrally", "Logs on the compromised machine are the first thing an attacker deletes.", BLUE),
      ("Decide retention in advance", "The HSE intruder was inside for eight weeks. Keep at least that much.", ORANGE)]
for k, (t, b, col) in enumerate(RU):
    body += (f'<div data-build-in="left {k + 2} auto" style="position:absolute;left:940px;top:{300 + k * 180}px;width:852px;height:160px;display:flex;flex-direction:column;gap:8px;justify-content:center;background:#FFFFFF;padding:22px 30px;border-radius:18px;border-left:8px solid {col};box-shadow:0 8px 24px rgba(19,41,75,0.07)">'
             f'<h3 style="font-size:32px;font-weight:600;color:{NAVY}">{t}</h3><p style="font-size:26px;line-height:1.35;color:{BODY2}">{b}</p></div>')
body += pin(128, 640, 736, P("The freezer alarm is both a security signal and a biosafety signal.", 28, ORANGET, weight=600, lh=1.35), build="fade 5 auto")
content(D, "telemetry", "DE.CM · you cannot fight what you cannot see", "Six log sources, three rules", body, ill="radar",
        notes="""Six log sources, three rules. The freezer alarm is in orange on purpose: it is both a security signal and a biosafety signal.

The retention point links back to the opening case: if you keep two weeks of logs, an eight-week intrusion is invisible.""")

# 17 taxonomy
TAX = [("Event", "Observable occurrence", "A failed login on the LIMS", BLUE, 360), ("Incident", "Violates policy or threatens operations", "Malware found on an instrument PC", BLUE, 560),
       ("Breach", "Confirmed loss of data", "Client results copied out", ORANGE, 760), ("Crisis", "Threatens safety or the institution", "Freezers or containment affected", ORANGET, 960)]
body = ""
for k, (a, b, e, col, w) in enumerate(TAX):
    y = 290 + k * 150
    body += (f'<div data-build-in="left {k + 1} auto" style="position:absolute;left:128px;top:{y}px;width:{w}px;height:126px;display:flex;flex-direction:column;justify-content:center;background:{col};padding:20px 30px;border-radius:16px">'
             f'<h3 style="font-family:{SERIF};font-size:48px;font-weight:600;color:{"#FFFFFF" if col != ORANGE else NAVY}">{a}</h3></div>')
    body += (f'<div data-build-in="fade {k + 1} auto" style="position:absolute;left:{128 + w + 36}px;top:{y + 14}px;width:{1664 - w - 36}px;display:flex;flex-direction:column;gap:4px">'
             f'<p style="font-size:28px;font-weight:600;color:{NAVY}">{b}</p><p style="font-size:26px;color:{BODY2}">{e}</p></div>')
content(D, "taxonomy", "Definitions and thresholds", "Name the level before you respond", body, ill="gauge",
        notes="""Four levels, one click each. Most alerts are events. Calling every event a crisis exhausts the team; calling a crisis an event delays the response. Write the thresholds down before you need them.

In a laboratory, anything that touches containment or sample viability goes straight to the top level.""")

# 18 RACI
RACI = [("Declare an incident", "A", "R", "C", "C", "I", "I"),
        ("Isolate the lab network", "A", "R", "C", "C", "I", "I"),
        ("Decide on samples and containment", "C", "C", "A", "R", "I", "I"),
        ("Report under Law 7545 / KVKK", "A", "C", "I", "I", "R", "C"),
        ("Inform clients and the public", "A", "I", "C", "C", "C", "R")]
HDR = ["Activity", "Incident lead", "IT / network", "Biosafety officer", "Lab head", "Legal / DPO", "Comms"]
cw = [452, 202, 202, 202, 202, 202, 202]


def badge(x):
    if x == "A":
        return f'<p style="width:64px;font-family:{MONO};font-size:28px;font-weight:600;text-align:center;color:{NAVY};background:{ORANGE};padding:6px 0;border-radius:10px">A</p>'
    if x == "R":
        return f'<p style="width:64px;font-family:{MONO};font-size:28px;font-weight:600;text-align:center;color:#FFFFFF;background:{BLUE};padding:6px 0;border-radius:10px">R</p>'
    return f'<p style="width:64px;font-family:{MONO};font-size:28px;text-align:center;color:{MUTE}">{x}</p>'


body = (f'<div data-build-in="fade 1 auto" style="position:absolute;left:128px;top:280px;width:1664px;height:84px;display:flex;flex-direction:row;align-items:center;background:{NAVY};border-radius:14px">'
        + "".join(f'<p style="width:{cw[k]}px;padding:0 20px;font-size:24px;font-weight:600;{"text-align:center;" if k else ""}color:{"#FFFFFF" if k != 3 else SAND}">{h}</p>' for k, h in enumerate(HDR)) + "</div>")
for r, row in enumerate(RACI):
    body += (f'<div data-build-in="left {r + 2} auto" style="position:absolute;left:128px;top:{380 + r * 96}px;width:1664px;height:84px;display:flex;flex-direction:row;align-items:center;background:{"#FFF3EA" if r == 2 else "#FFFFFF"};border-radius:14px;box-shadow:0 6px 18px rgba(19,41,75,0.06)">'
             f'<p style="width:{cw[0]}px;padding:0 20px;font-size:27px;font-weight:600;color:{NAVY}">{row[0]}</p>'
             + "".join(f'<div style="width:{cw[k + 1]}px;display:flex;flex-direction:row;justify-content:center">{badge(x)}</div>' for k, x in enumerate(row[1:])) + "</div>")
body += pin(128, 870, 1600, P("<b>R</b> responsible · <b>A</b> accountable · <b>C</b> consulted · <b>I</b> informed. One A per row.", 24, BODY2), build="fade 7 auto")
content(D, "raci", "Command structure · RS.MA, RS.CO", "Who decides, who acts, who is told", body, ill="people",
        notes="""A RACI matrix adapted from my incident response deck, with one change for laboratories: the biosafety officer is accountable for decisions about samples and containment. IT must not cut power to a freezer room on its own authority.

Five rows, one click each. The reporting row reminds us of Law 7545 and KVKK.""")

statement(D, "golden", ["1 · Human safety", "2 · Service continuity", "3 · Data integrity", "4 · Reputation"],
          """The golden rule from my incident response material, one click per line. In a laboratory, human safety includes biosafety: containment comes before getting the sequencer back online.

The last line adds the balance: containment speed versus forensic fidelity. Move fast, but keep the evidence.""",
          eyebrow="When priorities collide", sub="Even under pressure, preserve timestamps and chain of custody.",
          size=104, colors=[SAND, CREAM, CREAM, SKY], ill_html=illus("flag", left=1430, top=90))

# 20 backup 3-2-1
NUM = [("3", "copies of the data", BLUE), ("2", "different media", BLUE), ("1", "offline or immutable", ORANGET)]
body = ""
for k, (a, b, col) in enumerate(NUM):
    body += (f'<div data-build-in="pop {k + 1} auto" style="position:absolute;left:{128 + k * 563}px;top:280px;width:539px;display:flex;flex-direction:column;gap:6px;align-items:center">'
             f'<p style="font-family:{SERIF};font-size:260px;font-weight:600;line-height:1;color:{col}">{a}</p><h3 style="font-size:34px;font-weight:600;color:{NAVY}">{b}</h3></div>')
body += (f'<div data-build-in="rise 4 auto" style="position:absolute;left:128px;top:700px;width:1664px;display:flex;flex-direction:row;gap:30px;align-items:center;background:{NAVY};padding:36px 44px;border-radius:22px">'
         f'<x-icon name="Verified" style="width:56px;height:56px;color:{SAND}"></x-icon><p style="font-family:{SERIF};font-size:52px;font-weight:600;color:{CREAM}">A backup is a hypothesis. <span style="color:{SAND}">A tested restore is evidence.</span></p></div>')
content(D, "backup", "RC.RP · recovery", "The 3-2-1 rule", body, ill="backup",
        notes="""The 3-2-1 rule. Ransomware groups look for backups first, so the offline or immutable copy is the one that saves you.

Ask: when did your group last restore something from backup on purpose?""")

# 21 maturity
LV = [("Level 1 · Basic", "Antivirus alert; manual isolation; sparse local logs", "Panic and delay", ORANGET),
      ("Level 2 · Intermediate", "EDR alert; fast search for indicators; central logs", "Controlled containment", BLUE),
      ("Level 3 · Advanced", "Automated containment; threat hunting; segmented network", "Neutralised in minutes", TEALT)]
body = pin(128, 270, 1300, P("Suspicious PowerShell on an instrument PC, with an outbound connection.", 34, BODY2, lh=1.32), build="fade 1 auto")
for k, (a, b, o, col) in enumerate(LV):
    hgt = 300 + k * 70
    body += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:{128 + k * 563}px;top:{730 - hgt}px;width:539px;height:{hgt}px;display:flex;flex-direction:column;gap:14px;justify-content:end;background:#FFFFFF;padding:28px 32px;border-radius:20px;border-top:8px solid {col};box-shadow:0 10px 32px rgba(19,41,75,0.08)">'
             f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{col}">{a}</p><p style="font-size:27px;line-height:1.35;color:{BODY2}">{b}</p>'
             f'<h3 style="font-family:{SERIF};font-size:40px;font-weight:600;color:{col}">{o}</h3></div>')
body += callout(770, "Where is your organisation on this ladder today? Level 2 is a realistic one-year target for most facilities.", label="Ask the room", icon="Chat", build="rise 5 auto")
content(D, "maturity", "Same event, three outcomes", "A maturity ladder for response", body, ill="stairs",
        notes="""One scenario, three maturity levels, from my April incident response workshop. One click per level, then the question to the room.

Level 2 does not require a large security team; it requires central logs and a practised playbook.""")


# 22 sprint (navy)
@navy("sprint", """The 30-day sprint from my incident response material. It is deliberately modest: inventory and roles, a starter kit of plans, a telemetry audit, and a tabletop exercise.

Any institution represented here can do this before the end of the year.""", ill="clock")
def _(i, n):
    h = eyebrow("Start tomorrow · a 30-day sprint", 170)
    h += f'<h2 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:215px;width:1300px;font-family:{SERIF};font-size:72px;font-weight:600;color:{CREAM}">Four weeks, four deliverables</h2>'
    WK = [("Week 1", "Inventory &amp; roles", "Asset list, crown jewels, the incident lead and deputies"),
          ("Week 2", "Starter kit", "A master plan and three playbooks: ransomware, vendor compromise, data leak"),
          ("Week 3", "Telemetry audit", "Clocks synced, log sources connected, retention set"),
          ("Week 4", "Tabletop", "A 60-minute exercise with IT, biosafety, lab heads and legal")]
    cols = [MINT, SKY, MINT, SAND]
    for k, (w, a, b) in enumerate(WK):
        h += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:{128 + k * 422}px;top:370px;width:398px;height:400px;display:flex;flex-direction:column;gap:16px;background:#1B3866;padding:34px 32px;border-radius:22px;border-top:8px solid {cols[k]}">'
              f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{cols[k]}">{w}</p><h3 style="font-family:{SERIF};font-size:46px;font-weight:600;line-height:1.1;color:{CREAM}">{a}</h3>'
              f'<p style="font-size:27px;line-height:1.38;color:{SKY}">{b}</p></div>')
    h += f'<p data-build-in="fade 6 auto" style="position:absolute;left:128px;top:820px;width:1600px;font-size:30px;color:{SKY}">Complexity is the enemy of execution. <b style="color:{SAND}">Start with the basics, but start.</b></p>'
    return h


# 23 metrics
MET = [("MTTD", "Mean time to detect", BLUE, "Clock"), ("MTTR", "Mean time to respond", BLUE, "Lightning"), ("MFA %", "Remote paths with MFA", ORANGET, "Lock"),
       ("Assets %", "Devices on the inventory", BLUE, "Database"), ("Restore", "Last successful test", ORANGET, "Verified"), ("Reports", "Phishing reports by staff", TEALT, "ThumbsUp")]
items = [f'<x-icon name="{ic}" style="width:44px;height:44px;color:{col}"></x-icon>' + bignum(a, col, 76) + P(b, 28, BODY2) for a, b, col, ic in MET]
body = cards_row(items[:3], top=290, accent_cycle=[BLUE, BLUE, ORANGE], pad="26px 32px", height=250) + cards_row(items[3:], top=560, build_start=4, accent_cycle=[BLUE, ORANGE, TEAL], pad="26px 32px", height=250)
body += pin(128, 840, 1600, P("Report them to leadership every quarter. Metrics turn security from a cost into a budget line.", 28, BODY2), build="fade 7 auto")
content(D, "metrics", "Metrics that matter", "You cannot manage what you do not measure", body, ill="gauge",
        notes="""Six metrics a facility can actually collect. Rising phishing reports are good news: they mean people are noticing.

These numbers are also how you justify the budget for phase two.""")


# 24 takeaways (navy)
@navy("takeaways", """Three lines, one click each, then the afternoon programme. Prof. Merey's session on policies and SOPs follows lunch; it builds directly on the RACI and playbooks we saw here.""", ill="shield")
def _(i, n):
    h = eyebrow("Three things to keep", 200)
    for k, (t, col) in enumerate([("Inventory before investment.", CREAM), ("MFA on every remote path.", SKY), ("Rehearse with biosafety.", SAND)]):
        h += f'<h2 data-build-in="rise {k + 2} auto" style="position:absolute;left:128px;top:{290 + k * 120}px;width:1600px;font-family:{SERIF};font-size:92px;font-weight:600;line-height:1.08;color:{col}">{t}</h2>'
    for k, (t, bg, fc) in enumerate([("13:30 · Laboratory cyberbiosecurity policies &amp; SOPs · Prof. Dr. Gökçe Merey", "#1B3866", CREAM), ("14:30 · Hands-on: apply CSF 2.0", SAND, NAVY)]):
        h += f'<p data-build-in="fade 5 auto" style="position:absolute;left:{128 + k * 1080}px;top:720px;width:{1040 if k == 0 else 584}px;font-size:26px;font-weight:600;color:{fc};background:{bg};padding:16px 24px;border-radius:14px">{t}</p>'
    return h


refs(D, "refs", [
    "PwC. <i>Conti cyber attack on the HSE: independent post incident review</i>. Commissioned by the HSE Board; published 10 Dec 2021.",
    "NHS England (London). Update on cyber incident clinical impact in south east London; 19 Sep 2024.",
    "Infosecurity Magazine. Patient death linked to NHS cyber-attack (King’s College Hospital statement); 26 Jun 2025.",
    "CyberInsider. Change Healthcare revises breach impact to 192.7 million individuals (HHS OCR filing of 31 Jul 2025); 15 Aug 2025.",
    "Nelson A, Rekhi S, Souppaya M, Scarfone K. <i>Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile</i>. NIST SP 800-61r3; 2025. doi:10.6028/NIST.SP.800-61r3",
    "National Institute of Standards and Technology. <i>The NIST Cybersecurity Framework (CSF) 2.0</i>. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
    "Altun A. <i>Incident Response: Best Practices, Tools, and Resources</i>; and <i>Personnel-Related Vulnerabilities and Cybersecurity</i>. Workshop materials, 2026.",
    "7545 sayılı Siber Güvenlik Kanunu. Resmî Gazete 32846; 19 Mar 2025. · 6698 sayılı Kişisel Verilerin Korunması Kanunu.",
])
thanks(D, "thanks", "Questions on building the infrastructure", "Take questions, then release for lunch. Remind everyone that the 14:30 exercise uses everything from this session.")

SECTIONS = {"s1": {"description": "A real incident and the lesson", "start": "cover"},
            "s2": {"description": "Phase 1: assess the facility", "start": "facility"},
            "s3": {"description": "Phase 2: build, respond and recover", "start": "arch"},
            "s4": {"description": "Start tomorrow", "start": "maturity"}}

if __name__ == "__main__":
    import sys
    write_deck(sys.argv[1], "Institutional Cybersecurity Infrastructure", SECTIONS, D.render())
    print("ok", len(D.slides))
