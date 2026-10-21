import math
from common import *
from kit import _arc

D = Deck("NIST CSF 2.0 · Core Functions & Profiles · Çorum 2026")
VID = ("/_blob/91df7f517384ac27b06a93d08e3feba4", "/_blob/e07c4d31814f6c8ccfea8a0197065c4b")


def ctext(k, title, body, kc=TEALT):
    return (f'<p style="font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{kc}">{k}</p>'
            f'<h3 style="font-size:32px;font-weight:600;line-height:1.2;color:{NAVY}">{title}</h3>'
            f'<p style="font-size:26px;line-height:1.4;color:{BODY2}">{body}</p>')


# 1 cover — big live wheel on the right
w, c = wheel_svg(620, active=("GV",), pulse=True, left=1160, top=200, dark=True)
cover(D, "cover", "Day 1 · Monday 2 November 2026 · 13:30–14:30",
      ["NIST Cybersecurity", "Framework 2.0"], "Core Functions and Profiles for the research laboratory",
      "Cyberbiosecurity Training Workshop · Hitit University, Çorum",
      w + wheel_labels(c, 620, ("GV",), dark=True, big=False),
      """Welcome back. This morning Prof. Gargılı set out why biological laboratories need cybersecurity. This hour gives that need a structure: the NIST Cybersecurity Framework, version 2.0.

Plan for the hour: why a framework, what changed in 2.0, the six functions with a laboratory example for each, how the Core is built, and then Tiers and Profiles, the part you will use tomorrow afternoon.""")

video(D, "film", VID[0], VID[1], "Opening film: the five CSF 1.1 functions turn into the CSF 2.0 wheel as GOVERN moves into the centre",
      "Opening film, about 14 seconds; it loops while this slide is shown. Advance when it reaches the title card.")

statement(D, "spafford", ["“The only truly secure system is one", "that is powered off, cast in a block of", "concrete and sealed in a lead-lined room", "with armed guards.”", "Our laboratories are powered on."],
          """Let the quote build line by line, then the last line lands in orange.

Our sequencers, freezers, biosafety cabinets and LIMS are all powered on and most are networked. So the question is never how to be perfectly secure. It is how to manage the risk in a way everyone in the building understands.""",
          eyebrow="Gene Spafford · Purdue University", size=72, colors=[CREAM, CREAM, CREAM, CREAM, ORANGE])

# 4 Oxford
body = cards_row([
    ctext("Exposed", "Pumps and pressure controls", "Screenshots shared with Forbes showed live access to instrument interfaces."),
    ctext("Context", "A lab doing COVID-19 research", "Timestamps suggested access as recently as 14 February."),
    ctext("Response", "Contained and reported", "The university notified the NCSC; it said no clinical research or patient data were affected."),
], top=360, accent_cycle=[ORANGE, BLUE, TEAL])
body += lens(720, "Instrument controllers are IT assets. Nobody had them on an inventory, so nobody was protecting them.", label="The lesson", build="rise 4 auto")
body += src("ESET WeLiveSecurity, 26 Feb 2021, reporting Forbes and Hold Security", 880)
content(D, "oxford", "February 2021 · University of Oxford · Structural Biology",
        "Intruders reached the controls of equipment that prepares biochemical samples", body, ill="server",
        notes="""A real case close to home for everyone in this room. In February 2021 Oxford confirmed that attackers had accessed systems in its Structural Biology division, including the controls of machines that purify and prepare biochemical samples.

The point is not that the attackers were sophisticated; reports suggest they were not. The point is that laboratory equipment was reachable, and nobody had treated it as an IT asset.""")

# 5 why
icn = lambda name, col: f'<x-icon name="{name}" style="width:52px;height:52px;color:{col}"></x-icon>'
body = cards_row([
    icn("CheckCircle", BLUE) + ctext("01 · Outcomes", "What to achieve, not how", "The Core lists outcomes. Your lab chooses the controls that reach them."),
    icn("Globe", TEAL) + ctext("02 · Any organization", "Not only critical infrastructure", "Version 2.0 is written for organizations of every size, a core facility included."),
    icn("Book", ORANGE) + ctext("03 · Voluntary", "A map, not a regulation", "It sits beside Law 7545 and KVKK and helps organise how you meet them."),
], top=380, accent_cycle=[BLUE, TEAL, ORANGE], pad="34px 34px")
content(D, "why", "Why a framework", "One vocabulary for the biosafety officer, the IT team and the rector", body, ill="people",
        notes="""Three things to remember about the CSF before we open it. It describes outcomes rather than prescribing products. Since 2.0 it is explicitly for any organization, not just power plants and banks. And it is voluntary: it does not replace national law, but it is an excellent way to organise compliance work.""")

# 6 timeline
tl_svg = (f'<svg aria-label="" width="1664" height="40" viewBox="0 0 1664 40" style="position:absolute;left:128px;top:470px;width:1664px;height:40px">'
          f'<style>.ln{{stroke-dasharray:1600;stroke-dashoffset:1600;animation:ln 2.4s ease-out forwards}}@keyframes ln{{to{{stroke-dashoffset:0}}}}.pk{{transform-box:fill-box;transform-origin:center;animation:pk 2s ease-in-out infinite}}@keyframes pk{{50%{{transform:scale(1.25)}}}}{RM}</style>'
          f'<line x1="0" y1="20" x2="1664" y2="20" stroke="{GREY}" stroke-width="6" stroke-linecap="round"/><line class="ln" x1="0" y1="20" x2="1600" y2="20" stroke="{TEAL}" stroke-width="6" stroke-linecap="round"/>'
          f'<circle cx="140" cy="20" r="16" fill="{BLUE}"/><circle cx="700" cy="20" r="16" fill="{BLUE}"/><circle class="pk" cx="1260" cy="20" r="20" fill="{ORANGE}"/></svg>')
yrs = [("2014", "v1.0 · 12 Feb", "Born from U.S. Executive Order 13636, aimed at <b>critical infrastructure</b>.", NAVY, 40),
       ("2018", "v1.1 · 16 Apr", "Adds supply-chain risk, identity and self-assessment. <b>Five functions.</b>", NAVY, 600),
       ("2024", "v2.0 · 26 Feb", "Written for <b>all organizations</b>. A sixth function, <b>GOVERN</b>, at the centre.", ORANGET, 1160)]
body = tl_svg
for k, (y, chipt, txt, col, x) in enumerate(yrs):
    body += pin(128 + x, 330, 440, bignum(y, col, 110), build=f"rise {k * 2 + 1} auto")
    body += pin(128 + x, 540, 440, chip(chipt, bg=ORANGE if k == 2 else PALE2, color="#FFFFFF" if k == 2 else NAVY) + P(txt, 28, BODY2), build=f"rise {k * 2 + 2} auto", style="display:flex;flex-direction:column;gap:16px;align-items:start")
content(D, "timeline", "A decade of the framework", "From critical infrastructure to every organization", body, ill="timeline",
        notes="""Quick history. Version 1.0 came out in 2014 for critical infrastructure. Version 1.1 in 2018 kept the five functions and added supply-chain and identity material.

Version 2.0, published 26 February 2024, is the version we teach today. Two headline changes: the audience is now every organization, and governance became its own function.""")


# 7 five became six (magic-move pair with the next slide)
def five_svg(size, left, top, eid):
    cc = size / 2
    r0, r1 = size * 0.215, size * 0.49
    seg = 2 * math.pi / 5
    b = ""
    cents = {}
    for i2, (code, _) in enumerate(FN):
        a0 = -math.pi / 2 - seg / 2 + i2 * seg + 0.02
        a1 = a0 + seg - 0.04
        b += f'<path d="{_arc(cc, cc, r0, r1, a0, a1)}" fill="#FFFFFF" stroke="{GREY}" stroke-width="3"/>'
        am = (a0 + a1) / 2
        cents[code] = (left + cc + (r0 + r1) / 2 * math.cos(am), top + cc + (r0 + r1) / 2 * math.sin(am))
    st = f".q{{stroke-dasharray:14 12;animation:q 2s linear infinite}}@keyframes q{{to{{stroke-dashoffset:-52}}}}{RM}"
    b += f'<circle class="q" cx="{cc}" cy="{cc}" r="{r0 - 12}" fill="none" stroke="{ORANGE}" stroke-width="5"/>'
    return (f'<svg id="{eid}" aria-label="CSF 1.1 wheel with an empty centre" width="{size}" height="{size}" viewBox="0 0 {size} {size}" style="position:absolute;left:{left}px;top:{top}px;width:{size}px;height:{size}px"><style>{st}</style>{b}</svg>'), cents


fs, fc = five_svg(640, 128, 300, "wheel")
lab5 = "".join(f'<p style="position:absolute;left:{fc[cd][0] - 110:.0f}px;top:{fc[cd][1] - 22:.0f}px;width:220px;font-size:30px;font-weight:700;letter-spacing:2px;text-align:center;color:{NAVY}">{nm.upper()}</p>' for cd, nm in FN)
body = fs + lab5
body += f'<p data-build-in="pop 1 auto" style="position:absolute;left:{128 + 320 - 50}px;top:{300 + 320 - 40}px;width:100px;font-family:{SERIF};font-size:64px;font-weight:600;text-align:center;color:{ORANGE}">?</p>'
body += pin(900, 380, 880, f'<h2 style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1.05;color:{NAVY}">Five functions</h2>', build="rise 2 auto")
body += pin(900, 490, 880, f'<h2 style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1.05;color:{ORANGET}">became six.</h2>', build="rise 3 auto")
body += pin(900, 640, 820, P("The empty centre of the old wheel now holds the function that steers the other five.", 32, BODY2), build="fade 4 auto")
content(D, "fivesix", "CSF 1.1 → CSF 2.0", "", body, transition="magic", illus_html="",
        notes="""This is the CSF 1.1 wheel: Identify, Protect, Detect, Respond, Recover. Notice the empty, pulsing centre. Click: in 2.0 that hole is filled. The next slide morphs the wheel into the 2.0 version.""")

# 8 six functions with definitions building one by one
DEFS = [("GV", "Govern", "Strategy, expectations and policy are established, communicated and monitored.", ORANGE),
        ("ID", "Identify", "The organization’s current cybersecurity risks are understood.", BLUE),
        ("PR", "Protect", "Safeguards to manage cybersecurity risks are used.", BLUE),
        ("DE", "Detect", "Possible attacks and compromises are found and analyzed.", BLUE),
        ("RS", "Respond", "Actions regarding a detected incident are taken.", BLUE),
        ("RC", "Recover", "Affected assets and operations are restored.", BLUE)]
ws, wc = wheel_svg(640, active=("GV", "ID", "PR", "DE", "RS", "RC"), pulse=True, left=128, top=300, eid="wheel")
body = ws + wheel_labels(wc, 640, ("GV", "ID", "PR", "DE", "RS", "RC"))
for k, (cd, nm, df, col) in enumerate(DEFS):
    y = 290 + k * 104
    body += (f'<div data-build-in="left {k + 1} auto" style="position:absolute;left:880px;top:{y}px;width:912px;display:flex;flex-direction:row;gap:22px;align-items:center;background:#FFFFFF;padding:16px 24px;border-radius:16px;box-shadow:0 8px 24px rgba(19,41,75,0.07)">'
             f'<p style="font-family:{MONO};font-size:26px;font-weight:600;color:#FFFFFF;background:{col};padding:6px 12px;border-radius:10px">{cd}</p>'
             f'<div style="flex:1;display:flex;flex-direction:column;gap:2px"><p style="font-size:28px;font-weight:700;color:{NAVY}">{nm}</p><p style="font-size:24px;line-height:1.3;color:{BODY2}">{df}</p></div></div>')
content(D, "six", "NIST CSF 2.0 · the Core", "Six functions, working at the same time", body, transition="magic", ill="shield",
        notes="""The wheel morphs: GOVERN appears in the centre and every function lights up. Each click brings in one function with NIST's own one-line definition (paraphrased very slightly for length). Read them aloud; they are short on purpose.

Stress the title: all six run concurrently; they are not a checklist in order. The next slides zoom into one function at a time, and the wheel follows to the corner.""")

FUNCS = [
    ("GV", "Govern", "The core · GV", "Cybersecurity risk management strategy, expectations and policy are established, communicated and monitored.",
     [("GV.OC", "Organizational Context"), ("GV.RM", "Risk Management Strategy"), ("GV.RR", "Roles, Responsibilities & Authorities"), ("GV.PO", "Policy"), ("GV.OV", "Oversight"), ("GV.SC", "Supply Chain Risk Management")],
     "GV.SC", "Who owns the risk of a networked −80 °C freezer: the lab head, the biosafety officer, or IT? GOVERN makes someone answer, in writing.",
     """GOVERN is new in 2.0, and it is where cyberbiosecurity starts. Six categories. Spend a moment on GV.RR: roles and authorities. In most labs nobody has formally been given the cyber risk of laboratory equipment.

Highlight GV.SC, supply-chain risk: instrument vendors with remote access, cloud LIMS providers, and for core facilities the external clients whose samples and data you hold."""),
    ("ID", "Identify", "Function · ID", "The organization’s current cybersecurity risks are understood.",
     [("ID.AM", "Asset Management"), ("ID.RA", "Risk Assessment"), ("ID.IM", "Improvement")],
     "ID.AM", "The sequencer PC on an unsupported OS, the Wi-Fi freezer alarm, the shared analysis server: if it is not on the inventory, it is not protected.",
     """IDENTIFY is about knowing what you have and what could go wrong. Asset management is the foundation of everything else.

Link forward: at 15:30 today Prof. Merey runs the laboratory asset-mapping exercise. That exercise is ID.AM in practice."""),
    ("PR", "Protect", "Function · PR", "Safeguards to manage the organization’s cybersecurity risks are used.",
     [("PR.AA", "Identity, Authentication & Access"), ("PR.AT", "Awareness & Training"), ("PR.DS", "Data Security"), ("PR.PS", "Platform Security"), ("PR.IR", "Infrastructure Resilience")],
     "PR.AT", "Named accounts on instrument PCs, MFA on every remote session, a separate network for lab equipment, and staff who recognise a fake “vendor engineer” call.",
     """Five categories. In laboratories the weak points are usually PR.AA, shared logins on instrument PCs, and PR.AT, people.

Most intrusions still begin with a person being persuaded to do something. Awareness training is a Protect outcome, not an optional extra."""),
    ("DE", "Detect", "Function · DE", "Possible cybersecurity attacks and compromises are found and analyzed.",
     [("DE.CM", "Continuous Monitoring"), ("DE.AE", "Adverse Event Analysis")],
     "DE.AE", "In the 2021 Irish health service attack, antivirus detected the intruder on 31 March but was in monitor mode. Detection without analysis is only a log entry.",
     """Two categories. Monitoring collects signals; adverse event analysis decides what they mean.

The HSE case is the reminder: the signal was there seven weeks before the ransomware went off. We open that case fully tomorrow at 11:30."""),
    ("RS", "Respond", "Function · RS", "Actions regarding a detected cybersecurity incident are taken.",
     [("RS.MA", "Incident Management"), ("RS.AN", "Incident Analysis"), ("RS.CO", "Reporting & Communication"), ("RS.MI", "Incident Mitigation")],
     "RS.MI", "Contain without causing a biosafety incident: isolate the instrument network, not the freezer’s power. The biosafety officer belongs at the response table.",
     """Four categories. The laboratory twist is in mitigation: the fastest containment move can destroy samples or break containment.

So response plans in a lab must be written jointly by IT and biosafety. RS.CO also covers reporting: in Türkiye, Law 7545 requires reporting to the Cyber Security Presidency without delay."""),
    ("RC", "Recover", "Function · RC", "Assets and operations affected by a cybersecurity incident are restored.",
     [("RC.RP", "Recovery Plan Execution"), ("RC.CO", "Recovery Communication")],
     "RC.RP", "After the June 2024 ransomware attack on Synnovis, a London pathology provider, 10,146 outpatient appointments and 1,705 elective procedures were postponed.",
     """Two categories. Recovery is not only restoring servers; it is restoring the service the lab provides.

Synnovis is a supply-chain story too: one pathology contractor, two major hospital trusts disrupted for months. Figures are NHS England's cumulative numbers to mid-September 2024."""),
]
for k, (cd, nm, eb, df, cats, hot, lab, note) in enumerate(FUNCS):
    ws, wc = wheel_svg(260, active=(cd,), pulse=True, left=1532, top=40, eid="wheel")
    body = ws
    body += pin(128, 270, 1300, P(df, 36, BODY2, lh=1.32), build="fade 1 auto")
    ncol = 3 if len(cats) in (3, 5, 6) else 2
    gw = (1664 - 24 * (ncol - 1)) / ncol
    for j, (code, name) in enumerate(cats):
        r, cc = divmod(j, ncol)
        acc = ORANGE if code == hot else BLUE
        body += (f'<div data-build-in="rise {j + 2} auto" style="position:absolute;left:{128 + cc * (gw + 24):.0f}px;top:{410 + r * 150}px;width:{gw:.0f}px;height:126px;display:flex;flex-direction:row;gap:20px;align-items:center;background:#FFFFFF;padding:22px 26px;border-radius:18px;border-top:6px solid {acc};box-shadow:0 10px 32px rgba(19,41,75,0.08)">'
                 f'<p style="font-family:{MONO};font-size:26px;font-weight:600;color:{"#FFFFFF" if code == hot else NAVY};background:{ORANGE if code == hot else PALE2};padding:6px 12px;border-radius:10px;white-space:nowrap">{code}</p>'
                 f'<p style="flex:1;font-size:28px;line-height:1.25;font-weight:600;color:{NAVY}">{name}</p></div>')
    rows = (len(cats) + ncol - 1) // ncol
    if rows == 1:
        body += illus({"ID": "scan", "DE": "radar", "RC": "backup"}.get(cd, "shield"), left=1432, top=566)
        body += pin(128, 600, 1200, f'<p style="font-family:{SERIF};font-size:44px;font-weight:600;line-height:1.2;color:{NAVY}">{len(cats)} categories · {", ".join(c2 for c2, _ in cats)}</p>', build=f"fade {len(cats) + 2} auto")
    body += lens(800 if rows == 1 else 410 + rows * 150 + 40, lab, build=f"rise {len(cats) + 3} auto")
    content(D, f"f-{cd}", eb, nm, body, transition="magic", illus_html="", notes=note)

# 15 anatomy (statement-style on navy with three numbers)
def anatomy(i, n):
    inner = progress(i, n, True) + bg_network()
    inner += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:150px;width:1400px;font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{MINT}">How the Core is built</p>'
    nums = [("6", "Functions", CREAM), ("22", "Categories", MINT), ("106", "Subcategories", SAND)]
    for k, (nmb, lab, col) in enumerate(nums):
        x = 128 + k * 580
        inner += f'<p data-build-in="pop {k * 2 + 2} auto" style="position:absolute;left:{x}px;top:300px;width:460px;font-family:{SERIF};font-size:230px;font-weight:600;line-height:1;text-align:center;color:{col}">{nmb}</p>'
        inner += f'<p data-build-in="fade {k * 2 + 3} auto" style="position:absolute;left:{x}px;top:560px;width:460px;font-size:34px;font-weight:600;text-align:center;color:{CREAM}">{lab}</p>'
        if k < 2:
            inner += f'<x-shape kind="arrow-right" data-build-in="fade {k * 2 + 3} auto" style="position:absolute;left:{x + 470}px;top:400px;width:90px;height:44px;background:#36578A"></x-shape>'
    inner += f'<p data-build-in="fade 8 auto" style="position:absolute;left:128px;top:720px;width:1664px;font-size:32px;line-height:1.4;text-align:center;color:{SKY}">Each subcategory links to <b>Implementation Examples</b> and <b>Informative References</b>, published online so they can change without a new framework.</p>'
    inner += footer(D.foot, i + 1, True)
    return section("anatomy", inner, True, "fade", """Zoom out from the functions to the structure. Six functions, twenty-two categories, one hundred and six subcategories.

In 2.0 the examples and the mappings to other standards such as ISO 27001 moved online, so they can be updated without a new framework version. Next slide: one thread from function down to an actual task.""")
D.add("anatomy", anatomy)

# 16 drill-down
body = ""
chain = [("IDENTIFY", BLUE, "#FFFFFF"), ("ID.AM · Asset Management", PALE2, NAVY), ("ID.AM-01", ORANGE, "#FFFFFF")]
x = 128
for k, (t, bg, fg) in enumerate(chain):
    wdt = 60 + len(t) * 19
    body += f'<p data-build-in="left {k + 1} auto" style="position:absolute;left:{x}px;top:280px;width:{wdt}px;font-family:{MONO};font-size:30px;font-weight:600;text-align:center;color:{fg};background:{bg};padding:12px 18px;border-radius:12px">{t}</p>'
    x += wdt + 20
    if k < 2:
        body += f'<x-shape kind="arrow-right" data-build-in="fade {k + 1} auto" style="position:absolute;left:{x}px;top:296px;width:48px;height:28px;background:{SKY}"></x-shape>'
        x += 68
body += pin(128, 380, 1400, f'<p style="font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{TEALT}">Subcategory</p><h2 style="font-family:{SERIF};font-size:56px;font-weight:600;line-height:1.12;color:{NAVY}">“Inventories of hardware managed by the organization are maintained.”</h2>', build="rise 4 auto", style="display:flex;flex-direction:column;gap:10px")
body += cards_row([
    ctext("NIST implementation example", "All types of hardware", "Maintain inventories for all types of hardware, including IT, IoT, OT, and mobile devices."),
    ctext("In a biotech lab this means", "Bench-level inventory", "Instrument control PCs and their OS versions · freezer, incubator and cabinet controllers · data loggers, tablets, USB sticks"),
], top=600, build_start=5, accent_cycle=[BLUE, ORANGE])
content(D, "drill", "One thread through the Core", "From a function to a task on the bench", body, ill="scan",
        notes="""Build this slide one click at a time. Function, category, subcategory: ID.AM-01. Then NIST's own implementation example, then what it means on our bench.

This one line, an up-to-date hardware inventory that includes OT and IoT, is where most laboratories fail first. It is also the first step of the exercise this afternoon.""")

# 17 tiers
TIERS = [("1", "Partial", "Managed ad hoc; limited awareness across the organization.", PALE, NAVY),
         ("2", "Risk Informed", "Approved by management, not yet organization-wide policy.", LBLUE, NAVY),
         ("3", "Repeatable", "Formally approved, expressed as policy, regularly updated.", BLUE, "#FFFFFF"),
         ("4", "Adaptive", "Adapts from lessons learned and predictive indicators.", NAVY, "#FFFFFF")]
body = ""
for k, (nmb, nm, ds, bg, fg) in enumerate(TIERS):
    h = 250 + k * 110
    top = 900 - h
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:{128 + k * 422}px;top:{top}px;width:398px;height:{h}px;display:flex;flex-direction:column;gap:10px;justify-content:end;background:{bg};padding:28px 30px;border-radius:20px 20px 6px 6px{";border:4px solid " + ORANGE if nmb == "3" else ""}">'
             f'<p style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1;color:{fg}">{nmb}</p><p style="font-size:32px;font-weight:700;color:{fg}">{nm}</p><p style="font-size:24px;line-height:1.35;color:{fg}">{ds}</p></div>')
body += f'<p data-build-in="fade 5 auto" style="position:absolute;left:128px;top:280px;width:820px;font-size:28px;line-height:1.4;color:{BODY2}">Tiers are not a score to maximise. Choose the tier your risk justifies; a teaching lab and a BSL-3 core facility need different targets.</p>'
content(D, "tiers", "Tiers", "How rigorous are our practices?", body, ill="stairs",
        notes="""Tiers describe the rigour of your practices, from ad hoc to adaptive. They apply to governance and to management of risk.

Stress the sentence at the top: higher is not automatically better. Tier 3, outlined in orange, is a sensible target for many research facilities; Tier 4 costs real money and staff.""")

# 18 profiles
body = (pin(128, 300, 700, f'<p style="font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{TEALT}">Where we are</p><h2 style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1.05;color:{BLUE}">Current Profile</h2>', build="left 1 auto", style="display:flex;flex-direction:column;gap:8px")
        + f'<x-shape kind="arrow-right" data-build-in="pop 2 auto" style="position:absolute;left:880px;top:390px;width:150px;height:72px;background:{ORANGE}"></x-shape>'
        + pin(1092, 300, 700, f'<p style="font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{ORANGET}">Where we must be</p><h2 style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1.05;color:{ORANGET}">Target Profile</h2>', build="right 3 auto", style="display:flex;flex-direction:column;gap:8px"))
body += cards_row([ctext("The gap", "Outcome by outcome", "The difference between the two profiles."),
                   ctext("The action plan", "Owners, budget, dates", "Prioritised work that closes the gap."),
                   ctext("The cycle", "Implement, then update", "Re-rate the Current Profile. Repeat.")], top=600, build_start=4, accent_cycle=[BLUE, TEAL, ORANGE])
content(D, "profiles", "Profiles", "The CSF applied to your own laboratory", body, ill="profile",
        notes="""A Profile is the CSF applied to you. The Current Profile says which outcomes you achieve today; the Target Profile says which you need, given your risks and obligations.

The three cards build in turn: the gap, the action plan, the cycle. This is exactly what each group will build tomorrow at 14:30.""")


# 19 radar example
def radar_svg(left, top, size, cur, tgt):
    axes = 6
    cx = cy = size / 2
    R = size * 0.38
    pt = lambda i2, v: (cx + math.cos(-math.pi / 2 + i2 * math.pi / 3) * R * v / 4, cy + math.sin(-math.pi / 2 + i2 * math.pi / 3) * R * v / 4)
    rings = "".join(f'<polygon points="{" ".join(f"{pt(i2, t)[0]:.1f},{pt(i2, t)[1]:.1f}" for i2 in range(axes))}" fill="none" stroke="{GREY}" stroke-width="2"/>' for t in (1, 2, 3, 4))
    spokes = "".join(f'<line x1="{cx}" y1="{cy}" x2="{pt(i2, 4)[0]:.1f}" y2="{pt(i2, 4)[1]:.1f}" stroke="{GREY}" stroke-width="2"/>' for i2 in range(axes))
    poly = lambda v: " ".join(f"{pt(i2, x)[0]:.1f},{pt(i2, x)[1]:.1f}" for i2, x in enumerate(v))
    st = (f".cu{{transform-origin:{cx}px {cy}px;animation:cu 3s ease-in-out infinite}}@keyframes cu{{50%{{transform:scale(1.04)}}}}"
          f".tg{{stroke-dasharray:16 10;animation:tg 2s linear infinite}}@keyframes tg{{to{{stroke-dashoffset:-52}}}}{RM}")
    dots = "".join(f'<circle cx="{pt(i2, x)[0]:.1f}" cy="{pt(i2, x)[1]:.1f}" r="8" fill="{BLUE}"/>' for i2, x in enumerate(cur))
    svg = (f'<svg aria-label="Radar of current versus target tiers by function" width="{size}" height="{size}" viewBox="0 0 {size} {size}" style="position:absolute;left:{left}px;top:{top}px;width:{size}px;height:{size}px"><style>{st}</style>'
           f'{rings}{spokes}<polygon class="tg" points="{poly(tgt)}" fill="{ORANGE}" fill-opacity=".08" stroke="{ORANGE}" stroke-width="5"/>'
           f'<g class="cu"><polygon points="{poly(cur)}" fill="{BLUE}" fill-opacity=".25" stroke="{BLUE}" stroke-width="6"/>{dots}</g></svg>')
    labs = ""
    for i2, a in enumerate(["GV", "ID", "PR", "DE", "RS", "RC"]):
        x, y = pt(i2, 4.75)
        labs += f'<p style="position:absolute;left:{left + x - 40:.0f}px;top:{top + y - 20:.0f}px;width:80px;font-family:{MONO};font-size:28px;font-weight:600;text-align:center;color:{NAVY}">{a}</p>'
    return svg + labs


body = radar_svg(1080, 250, 640, [1, 2, 2, 1, 1, 1], [3, 3, 3, 3, 3, 2])
body += f'<div data-build-in="fade 1 auto" style="position:absolute;left:1180px;top:880px;width:440px;display:flex;flex-direction:row;gap:28px;align-items:center"><div style="width:30px;height:8px;background:{BLUE};border-radius:4px"></div><p style="font-size:24px;color:{BODY2}">Today</p><div style="width:30px;height:8px;background:{ORANGE};border-radius:4px"></div><p style="font-size:24px;color:{BODY2}">Agreed target</p></div>'
body += pin(128, 300, 860, P("Illustrative values for a university core facility that serves external industry clients. Tiers 1–4 per function.", 28, BODY2), build="fade 1 auto")
gaps = [("GV.SC", "Client samples and data arrive from outside; vendors log in remotely", ORANGE), ("DE.CM", "No central logging from instrument PCs", ORANGE), ("RC.RP", "Backups exist; a restore has never been tested", BLUE)]
for k, (cd, t, col) in enumerate(gaps):
    body += (f'<div data-build-in="left {k + 2} auto" style="position:absolute;left:128px;top:{440 + k * 140}px;width:860px;display:flex;flex-direction:row;gap:22px;align-items:center;background:#FFFFFF;padding:22px 26px;border-radius:16px;border-left:8px solid {col};box-shadow:0 8px 24px rgba(19,41,75,0.07)">'
             f'<p style="font-family:{MONO};font-size:26px;font-weight:600;color:{NAVY};background:{PALE2};padding:6px 12px;border-radius:10px">{cd}</p><p style="flex:1;font-size:27px;line-height:1.3;color:{TEXT}">{t}</p></div>')
content(D, "radar", "Worked example · illustrative", "A core facility’s profile and its gaps", body, illus_html="",
        notes="""An illustrative profile; the numbers are an example, not data from a real facility. Blue is today, the dashed orange line is the target the facility's board agreed. The three biggest gaps build in on the left.

For a facility that receives clients' samples and data, supply-chain governance, GV.SC, is usually the largest gap and the most specific to our sector.""")

# 20 organizational vs community
body = cards_row([
    ctext("Organizational profile", "Yours", "Current and Target for one organization or facility. NIST publishes a Quick-Start Guide and a fillable template.") ,
    ctext("Community profile", "Shared by a sector or a topic", "<b>SP 800-61 Rev. 3</b> (April 2025): incident response organised by CSF 2.0 functions.<br><b>Cyber AI Profile</b>, NIST IR 8596 (preliminary draft, Dec 2025): Secure, Defend, Thwart."),
], top=310, accent_cycle=[BLUE, ORANGE], pad="38px 40px")
body += callout(720, "The Cyber AI Profile is where tomorrow morning starts: <b>09:15 · NIST AI Risk Management Framework</b>.", label="Tomorrow", icon="Lightning", build="rise 3 auto")
content(D, "kinds", "Two kinds of profile", "Build your own, or start from a shared one", body, ill="layers",
        notes="""Organizational Profiles are what you build for your own unit. Community Profiles are written for a whole sector or topic and you can start from them.

Two that matter for this workshop: the new incident response guidance, SP 800-61 Revision 3, which is itself a CSF 2.0 community profile, and the preliminary Cyber AI Profile, which leads into tomorrow morning.""")

# 21 five steps
STEPS = [("Scope", "Which unit, systems and risks?"), ("Gather", "Policies, inventories, legal duties"), ("Create", "Rate Current and Target"), ("Analyze", "Gaps → prioritised action plan"), ("Implement", "Act, then update the profile")]
st_svg = (f'<svg aria-label="" width="1664" height="160" viewBox="0 0 1664 160" style="position:absolute;left:128px;top:340px;width:1664px;height:160px"><style>.ln{{stroke-dasharray:10 12;animation:ln 1.6s linear infinite}}@keyframes ln{{to{{stroke-dashoffset:-44}}}}{RM}</style>'
          f'<line class="ln" x1="166" y1="80" x2="1498" y2="80" stroke="{TEAL}" stroke-width="6"/>'
          + "".join(f'<circle cx="{166 + k * 333}" cy="80" r="70" fill="{ORANGE if k == 3 else NAVY}"/>' for k in range(5)) + '</svg>')
body = st_svg
for k, (a, b) in enumerate(STEPS):
    cx = 128 + 166 + k * 333
    body += f'<p data-build-in="pop {k + 1} auto" style="position:absolute;left:{cx - 70}px;top:372px;width:140px;font-family:{SERIF};font-size:80px;font-weight:600;line-height:1;text-align:center;color:#FFFFFF">{k + 1}</p>'
    body += pin(cx - 150, 540, 300, f'<p style="font-size:34px;font-weight:700;text-align:center;color:{NAVY}">{a}</p><p style="font-size:26px;line-height:1.35;text-align:center;color:{BODY2}">{b}</p>', build=f"rise {k + 1} auto", style="display:flex;flex-direction:column;gap:8px")
body += callout(760, "Tomorrow’s exercise compresses steps 1–4 into 45 minutes for a fictional biotech lab.", label="Tomorrow 14:30", icon="Clock", build="rise 7 auto")
content(D, "steps", "NIST Quick-Start Guide · Organizational Profiles", "Five steps from framework to action plan", body, ill="flag",
        notes="""NIST's quick-start guide gives five steps: scope, gather, create, analyze gaps and plan, implement and update. The numbers pop in one by one.

Tomorrow's exercise compresses steps one to four into forty-five minutes for a fictional biotech lab.""")

# 22 Türkiye
body = cards_row([
    ctext("Law No. 7545 · RG 19 March 2025", "Cybersecurity Law", "Covered entities report detected vulnerabilities and incidents to the Cyber Security Presidency <b>without delay</b>.") + chip("maps to RS.CO · GV.OC"),
    ctext("Law No. 6698 · KVKK", "Personal data protection", "Personal data breaches go to the KVKK Board within <b>72 hours</b> (Board Decision 2019/10).") + chip("maps to RS.CO · PR.DS"),
], top=320, accent_cycle=[ORANGE, BLUE], pad="38px 40px")
body += callout(700, "The CSF does not replace these duties. It is where you show how you meet them. Confirm with your institution’s legal office which apply.", label="In practice", icon="Verified", build="rise 3 auto")
content(D, "turkiye", "In Türkiye", "Voluntary framework, binding duties", body, ill="scale",
        notes="""Bring it home. Law 7545, published in the Official Gazette on 19 March 2025, created reporting duties to the Cyber Security Presidency. KVKK sets 72 hours for notifying personal data breaches.

The CSF does not replace these laws, but outcomes such as GV.OC, legal requirements are understood, and RS.CO, reporting, are where you show you meet them.""")

statement(D, "keep", ["Govern first.", "Know what you run.", "Profile, then act."],
          """Three lines, one per click. Govern first: someone must own the risk. Know what you run: inventory, including OT. Profile, then act: compare where you are with where you must be.

Then point to where these ideas continue: Prof. Merey's asset-mapping exercise at 15:30 and tomorrow's hands-on session.""",
          eyebrow="Three things to keep", sub="Today 15:30 · Laboratory asset mapping (Prof. Dr. Gökçe Merey) · Tomorrow 14:30 · Build your lab’s profile",
          colors=[CREAM, MINT, SAND], size=110, ill_html=illus("flag", left=1430, top=640))

refs(D, "refs", [
    "National Institute of Standards and Technology. <i>The NIST Cybersecurity Framework (CSF) 2.0</i>. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
    "Nelson A, Rekhi S, Souppaya M, Scarfone K. <i>Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile</i>. NIST SP 800-61r3; 2025. doi:10.6028/NIST.SP.800-61r3",
    "NIST. <i>Cybersecurity Framework Profile for Artificial Intelligence</i>. NIST IR 8596, initial preliminary draft; 16 Dec 2025.",
    "Murch RS, So WK, Buchholz WG, Raman S, Peccoud J. Cyberbiosecurity: an emerging new discipline to help safeguard the bioeconomy. <i>Front Bioeng Biotechnol</i>. 2018;6:39. doi:10.3389/fbioe.2018.00039",
    "Peccoud J, Gallegos JE, Murch R, Buchholz WG, Raman S. Cyberbiosecurity: from naive trust to risk awareness. <i>Trends Biotechnol</i>. 2018;36(1):4–7. doi:10.1016/j.tibtech.2017.10.012",
    "NHS England (London). Update on cyber incident clinical impact in south east London; 19 Sep 2024.",
    "ESET WeLiveSecurity. Oxford University lab studying COVID-19 hit by cyberattack; 26 Feb 2021.",
    "7545 sayılı Siber Güvenlik Kanunu, Resmî Gazete 32846, 19 Mar 2025 · 6698 sayılı KVKK; KVK Kurulu Kararı 2019/10.",
])
thanks(D, "thanks", "Questions on the framework, the functions or profiles", "Open the floor. If time is short, take one or two questions and point people to the afternoon exercise.")

SECTIONS = {"s1": {"description": "Why laboratories need a shared cybersecurity framework", "start": "cover"},
            "s2": {"description": "CSF 2.0 and its six functions, each with a laboratory example", "start": "fivesix"},
            "s3": {"description": "How the Core is built, Tiers and Profiles", "start": "anatomy"},
            "s4": {"description": "Duties in Türkiye, takeaways and sources", "start": "turkiye"}}

if __name__ == "__main__":
    import sys
    root = sys.argv[1]
    write_deck(root, "CSF 2.0 · Core Functions & Profiles", SECTIONS, D.render())
    print("ok", len(D.slides))
