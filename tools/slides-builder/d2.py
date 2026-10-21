import math
from common import *
from kit import _arc

D = Deck("NIST AI RMF · Research Laboratories · Çorum 2026")
VID = ("/_blob/d47b9f07c3f685c33102c9d23f10480b", "/_blob/ea6582c1e00ccf78d5532318aa444900")


def ctext(k, title, body, kc=TEALT):
    return (f'<p style="font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{kc}">{k}</p>'
            f'<h3 style="font-size:32px;font-weight:600;line-height:1.2;color:{NAVY}">{title}</h3>'
            f'<p style="font-size:26px;line-height:1.4;color:{BODY2}">{body}</p>')


RMF = ["MAP", "MEASURE", "MANAGE"]


def rmf_svg(size, active=(), left=0, top=0, eid="rmf", dark=False, pulse=True):
    c = size / 2
    r0, r1 = size * 0.23, size * 0.49
    base = "#1B3866" if dark else "#FFFFFF"
    strk = "#36578A" if dark else GREY
    st = (".pl{transform-box:fill-box;transform-origin:center;animation:pl 2.4s ease-in-out infinite}@keyframes pl{50%{transform:scale(1.04)}}"
          ".rg{transform-box:fill-box;transform-origin:center;animation:rg 2.6s ease-out infinite}@keyframes rg{0%{transform:scale(.9);opacity:.6}100%{transform:scale(1.35);opacity:0}}"
          ".fl{stroke-dasharray:8 14;animation:fl 1.4s linear infinite}@keyframes fl{to{stroke-dashoffset:-44}}" + RM)
    b = ""
    cents = {}
    for i, nm in enumerate(RMF):
        a0 = -math.pi / 2 + i * 2 * math.pi / 3 + 0.03
        a1 = a0 + 2 * math.pi / 3 - 0.06
        on = nm in active
        cls = ' class="pl"' if on and pulse else ""
        b += f'<path{cls} d="{_arc(c, c, r0, r1, a0, a1)}" fill="{BLUE if on else base}" stroke="{BLUE if on else strk}" stroke-width="3"/>'
        am = (a0 + a1) / 2
        cents[nm] = (left + c + (r0 + r1) / 2 * math.cos(am), top + c + (r0 + r1) / 2 * math.sin(am))
    # flow ring (the MAP → MEASURE → MANAGE cycle)
    b += f'<circle class="fl" cx="{c}" cy="{c}" r="{r1 + size * 0.02:.1f}" fill="none" stroke="{TEAL}" stroke-width="4"/>'
    gon = "GOVERN" in active
    if gon and pulse:
        b += f'<circle class="rg" cx="{c}" cy="{c}" r="{r0 - 10:.1f}" fill="none" stroke="{ORANGE}" stroke-width="6"/>'
    b += f'<circle cx="{c}" cy="{c}" r="{r0 - 10:.1f}" fill="{ORANGE if gon else base}" stroke="{ORANGE if gon else strk}" stroke-width="3"/>'
    cents["GOVERN"] = (left + c, top + c)
    svg = (f'<svg id="{eid}" aria-label="AI RMF core: Govern at the centre; Map, Measure and Manage around it" width="{size}" height="{size}" viewBox="0 0 {size} {size}" '
           f'style="position:absolute;left:{left}px;top:{top}px;width:{size}px;height:{size}px"><style>{st}</style>{b}</svg>')
    return svg, cents


def rmf_labels(cents, active=(), dark=False, fs=30):
    out = ""
    for nm in ["GOVERN"] + RMF:
        x, y = cents[nm]
        on = nm in active
        col = (NAVY if nm == "GOVERN" else "#FFFFFF") if on else (CREAM if dark else NAVY)
        out += f'<p style="position:absolute;left:{x - 120:.0f}px;top:{y - fs * 0.75:.0f}px;width:240px;font-size:{fs}px;font-weight:700;letter-spacing:2px;text-align:center;color:{col}">{nm}</p>'
    return out


# 1 cover
rs, rc = rmf_svg(620, ("GOVERN", "MAP", "MEASURE", "MANAGE"), left=1160, top=200, dark=True, eid="rmfc")
cover(D, "cover", "Day 2 · Tuesday 3 November 2026 · 09:15–10:15",
      ["NIST AI RMF"], "The AI Risk Management Framework: principles and applications for research laboratories",
      "Cyberbiosecurity Training Workshop · Hitit University, Çorum",
      rs + rmf_labels(rc, ("GOVERN", "MAP", "MEASURE", "MANAGE"), dark=True, fs=24),
      """Good morning. Yesterday we built a shared language for cyber risk. This morning we do the same for a newer kind of risk: AI systems that are now part of research workflows.

Plan: one hard example, why AI risk is different, the AI RMF itself (trustworthiness and the four functions), the Generative AI profile, AI as an attack target, and a worked laboratory case.""")

video(D, "film", VID[0], VID[1], "Opening film: a counter rises to 40,000 candidate molecules, then the four AI RMF verbs appear",
      "Opening film, about 13 seconds; it loops while shown. Advance when it reaches the title card.")

# 3 bridge
CSF = ["GV", "ID", "PR", "DE", "RS", "RC"]
body = pin(128, 300, 780, f'<p style="font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{TEALT}">Yesterday · CSF 2.0</p><h2 style="font-family:{SERIF};font-size:72px;font-weight:600;line-height:1.08;color:{NAVY}">Six functions for cyber risk</h2>', build="left 1 auto", style="display:flex;flex-direction:column;gap:10px")
body += pin(1012, 300, 780, f'<p style="font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{ORANGET}">Today · AI RMF 1.0</p><h2 style="font-family:{SERIF};font-size:72px;font-weight:600;line-height:1.08;color:{BLUE}">Four functions for AI risk</h2>', build="right 3 auto", style="display:flex;flex-direction:column;gap:10px")
for k, c2 in enumerate(CSF):
    body += f'<p data-build-in="pop {2} auto" style="position:absolute;left:{128 + k * 124}px;top:560px;width:104px;font-family:{MONO};font-size:30px;font-weight:600;text-align:center;color:{"#FFFFFF" if c2 == "GV" else NAVY};background:{ORANGE if c2 == "GV" else PALE2};padding:12px 0;border-radius:12px">{c2}</p>'
for k, c2 in enumerate(["GOVERN", "MAP", "MEASURE", "MANAGE"]):
    wdt = [180, 110, 170, 170][k]
    xs = [1012, 1208, 1334, 1520][k]
    body += f'<p data-build-in="pop {4} auto" style="position:absolute;left:{xs}px;top:560px;width:{wdt}px;font-family:{MONO};font-size:28px;font-weight:600;text-align:center;color:#FFFFFF;background:{ORANGE if k == 0 else BLUE};padding:14px 0;border-radius:12px">{c2}</p>'
body += callout(740, "Both put governance first. The habits you built yesterday (owners, inventory, review cycle) carry straight over.", label="The bridge", icon="Link", build="rise 5 auto")
content(D, "bridge", "From cyber risk to AI risk", "Same logic, new kind of system", body, ill="neural",
        notes="""A deliberate bridge. Both NIST frameworks start from governance. If a lab has done the CSF work, it already has the owners, the inventory habit and the review cycle that AI risk management needs.""")


# 4 MegaSyn
def megasyn(i, n):
    inner = progress(i, n, True) + bg_network() + illus("molecule", left=1430, top=90)
    inner += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:150px;width:1200px;font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{MINT}">Dual use · drug discovery · 2022</p>'
    inner += f'<p data-build-in="pop 2 auto" style="position:absolute;left:128px;top:200px;width:1100px;font-family:{SERIF};font-size:240px;font-weight:600;line-height:1;color:{CREAM}">40,000</p>'
    inner += f'<p data-build-in="fade 3 auto" style="position:absolute;left:128px;top:450px;width:1200px;font-size:34px;font-weight:600;color:{SAND}">candidate molecules in under six hours</p>'
    inner += f'<p data-build-in="rise 4 auto" style="position:absolute;left:128px;top:530px;width:1400px;font-size:34px;line-height:1.4;color:{SKY}">A model built to steer drug candidates <b style="color:{CREAM}">away</b> from toxicity was asked to reward toxicity instead. Its output included VX and other known chemical warfare agents.</p>'
    inner += f'<p data-build-in="pop 5 auto" style="position:absolute;left:128px;top:730px;width:440px;font-size:28px;font-weight:700;text-align:center;color:{NAVY};background:{SAND};padding:12px 18px;border-radius:14px">Nothing was synthesised.</p>'
    inner += f'<p data-build-in="fade 6 auto" style="position:absolute;left:600px;top:738px;width:1100px;font-size:28px;line-height:1.35;color:{SKY}">The authors published to warn the field, not to show how.</p>'
    inner += f'<p style="position:absolute;left:128px;top:880px;width:1600px;font-size:24px;color:{SKY}">Urbina F, Lentzos F, Invernizzi C, Ekins S. Nat Mach Intell. 2022;4:189–191. doi:10.1038/s42256-022-00465-9</p>'
    inner += footer(D.foot, i + 1, True)
    return section("megasyn", inner, True, "fade", """Urbina and colleagues, 2022. Their company builds machine-learning models that predict toxicity so that drug candidates avoid it. For a biosecurity conference they inverted one objective. In under six hours the model proposed 40,000 molecules scoring as highly toxic, including VX.

They synthesised nothing, and they deliberately withheld details. The lesson for us is not about chemistry: a capability built for good can be repurposed by changing one line, and nobody in the lab had thought about it before.""")
D.add("megasyn", megasyn)

# 5 uses
icn = lambda name, col: f'<x-icon name="{name}" style="width:48px;height:48px;color:{col}"></x-icon>'
USES = [("Search", BLUE, "Structure prediction", "Protein models feed experimental design", "Validity · dual use"),
        ("Activity", TEAL, "Image analysis", "Microscopy, viability and pathology scoring", "Drift · bias"),
        ("Chat", ORANGE, "Language assistants", "Protocols, code, reports and reviews", "Confabulation · leakage"),
        ("Settings", BLUE, "Lab automation", "Liquid handlers and cloud labs run by scripts", "Safety · security"),
        ("Lightning", TEAL, "Molecule & sequence design", "Generative models propose candidates", "Dual use · IP"),
        ("Book", ORANGE, "Literature mining", "Screening papers, extracting data", "Confabulation · coverage")]
items = [icn(ic, col) + f'<h3 style="font-size:30px;font-weight:600;color:{NAVY}">{t}</h3><p style="font-size:26px;line-height:1.35;color:{BODY2}">{b}</p>' + chip(r) for ic, col, t, b, r in USES]
body = cards_row(items[:3], top=300, accent_cycle=[BLUE, TEAL, ORANGE], pad="26px 30px") + cards_row(items[3:], top=600, build_start=4, accent_cycle=[BLUE, TEAL, ORANGE], pad="26px 30px")
content(D, "uses", "AI is already on the bench", "Six places AI enters a life-science laboratory", body, ill="ai",
        notes="""Ask the room: how many of you used one of these last week? Usually most hands go up for language assistants.

Each card names the risks we will meet again in the framework: confabulation, drift, bias, data leakage, dual use.""")

statement(D, "different", ["Data changes; models drift.", "Behaviour is learned, not written.", "Failures are hard to predict.", "Errors scale instantly.", "The same tool can be used both ways."],
          """Five lines, one each, summarising NIST's own appendix on how AI risks differ from traditional software.

Traditional software does what its code says. A trained model does what its data taught it, and the data can change under it. That is why we need a framework that keeps measuring after deployment.""",
          eyebrow="Why AI risk is different · NIST AI 100-1, Appendix B", size=80, colors=[CREAM, CREAM, CREAM, CREAM, SAND], ill_html=illus("neural", left=1430, top=90))

# 7 glance
TL = [("Jan 2023", "AI RMF 1.0 and its companion Playbook", BLUE), ("Jul 2024", "Generative AI Profile, NIST AI 600-1", BLUE),
      ("Mar 2025", "Adversarial ML taxonomy, NIST AI 100-2 E2025", BLUE), ("Dec 2025", "Cyber AI Profile, NIST IR 8596 (preliminary draft)", BLUE),
      ("2026", "NIST states AI RMF 1.0 is being revised; a critical-infrastructure profile concept note followed in April", ORANGE)]
body = pin(128, 290, 700, f'<h2 style="font-family:{SERIF};font-size:110px;font-weight:600;line-height:1;color:{NAVY}">AI RMF 1.0</h2><p style="font-size:30px;line-height:1.4;color:{BODY2}">NIST AI 100-1, released <b>26 January 2023</b>. Voluntary, rights-preserving, not tied to any sector or use case.</p>', build="rise 1 auto", style="display:flex;flex-direction:column;gap:20px")
body += cards_row([ctext("Part 1", "Framing risk", "AI risks and the characteristics of trustworthy AI"), ctext("Part 2", "The Core", "Four functions, and how to build profiles")], top=600, total=700, build_start=2, accent_cycle=[TEAL, ORANGE], pad="24px 26px")
for k, (d, t, col) in enumerate(TL):
    body += (f'<div data-build-in="left {k + 4} auto" style="position:absolute;left:940px;top:{290 + k * 124}px;width:852px;display:flex;flex-direction:row;gap:22px;align-items:center">'
             f'<div style="width:22px;height:22px;background:{col};border-radius:11px"></div><div style="flex:1;display:flex;flex-direction:column;gap:2px"><p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{TEALT if col == BLUE else ORANGET}">{d}</p>'
             f'<p style="font-size:27px;line-height:1.3;color:{TEXT}">{t}</p></div></div>')
content(D, "glance", "The framework at a glance", "A voluntary framework, still evolving", body, ill="timeline",
        notes="""The essentials. Version 1.0 since January 2023, a Playbook with suggested actions for every subcategory, and a growing family of profiles.

Be explicit about status: NIST's page now says version 1.0 is being revised as part of the U.S. AI Action Plan. What you learn today, the functions and the trustworthiness characteristics, is expected to carry over, but check for a new version before you write institutional policy.""")

# 8 trustworthiness
PIL = ["Safe", "Secure &amp; Resilient", "Explainable &amp; Interpretable", "Privacy-Enhanced", "Fair, with Harmful Bias Managed"]
pcol = [BLUE, TEAL, LBLUE, BLUE, TEAL]
body = ""
for k, t in enumerate(PIL):
    body += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:{128 + k * 280}px;top:300px;width:256px;height:380px;display:flex;flex-direction:column;justify-content:end;background:{pcol[k]};padding:24px;border-radius:18px 18px 6px 6px">'
             f'<p style="font-size:30px;font-weight:700;line-height:1.2;text-align:center;color:#FFFFFF">{t}</p></div>')
body += f'<div data-build-in="rise 1 auto" style="position:absolute;left:128px;top:700px;width:1376px;display:flex;flex-direction:column;gap:4px;align-items:center;background:{NAVY};padding:26px;border-radius:18px"><p style="font-family:{SERIF};font-size:52px;font-weight:600;color:{SAND}">Valid &amp; Reliable</p><p style="font-size:24px;color:{SKY}">the base every other characteristic stands on</p></div>'
body += f'<div data-build-in="left 7 auto" style="position:absolute;left:1536px;top:300px;width:256px;height:556px;display:flex;flex-direction:column;justify-content:center;background:{ORANGE};padding:24px;border-radius:18px"><p style="font-size:34px;font-weight:700;line-height:1.2;text-align:center;color:{NAVY}">Accountable &amp; Transparent</p><p style="font-size:24px;text-align:center;color:{NAVY}">runs alongside all of them</p></div>'
content(D, "trust", "Characteristics of trustworthy AI", "Seven characteristics, and their trade-offs", body, illus_html="",
        notes="""The figure builds as NIST draws it. First the foundation, valid and reliable: a model that is wrong is not made trustworthy by anything else. Then the five pillars. Then accountability and transparency, which run alongside all of them.

Example of a trade-off: privacy enhancement can reduce accuracy, and explainability can cost performance. The framework asks you to make those trade-offs consciously.""")

# 9 core (magic source)
DEFS = [("GOVERN", "A culture of risk management is cultivated and present.", ORANGE, "6 categories"),
        ("MAP", "Context is recognized and risks related to context are identified.", BLUE, "5 categories"),
        ("MEASURE", "Identified risks are assessed, analyzed, or tracked.", BLUE, "4 categories"),
        ("MANAGE", "Risks are prioritized and acted upon based on a projected impact.", BLUE, "4 categories")]
rs, rc = rmf_svg(640, ("GOVERN", "MAP", "MEASURE", "MANAGE"), left=128, top=300, eid="rmf")
body = rs + rmf_labels(rc, ("GOVERN", "MAP", "MEASURE", "MANAGE"))
for k, (nm, df, col, cats) in enumerate(DEFS):
    body += (f'<div data-build-in="left {k + 1} auto" style="position:absolute;left:880px;top:{300 + k * 150}px;width:912px;display:flex;flex-direction:row;gap:24px;align-items:center;background:#FFFFFF;padding:22px 26px;border-radius:18px;border-left:8px solid {col};box-shadow:0 8px 24px rgba(19,41,75,0.07)">'
             f'<div style="flex:1;display:flex;flex-direction:column;gap:4px"><p style="font-size:30px;font-weight:700;letter-spacing:2px;color:{NAVY}">{nm}</p><p style="font-size:26px;line-height:1.3;color:{BODY2}">{df}</p></div>'
             f'<p style="font-family:{MONO};font-size:24px;font-weight:600;color:{NAVY};background:{PALE2};padding:6px 12px;border-radius:10px;white-space:nowrap">{cats}</p></div>')
content(D, "core", "The AI RMF Core", "Four functions; GOVERN runs through all", body, transition="magic", illus_html="",
        notes="""Walk the four functions, one row per click, with NIST's one-line definitions. GOVERN is cross-cutting; the other three form a cycle you repeat whenever a system, its data or its use changes. The dashed teal ring is that cycle.

The next slides zoom into each function with laboratory questions; the ring follows into the corner.""")

FNS = [
    ("GOVERN", "Function 1 · cross-cutting", "A culture of risk management is cultivated and present.",
     ["Is there a written policy on which AI tools may touch patient, client or genomic data?", "Who approves a new AI tool in the lab, and who is accountable when it fails?",
      "Do we keep an inventory of AI systems in use? (GOVERN 1.6 asks for exactly this.)", "Are third-party models and services covered by our supplier rules?"],
     "Start with a one-page AI use policy and a register. Most labs have neither.",
     """GOVERN in a laboratory is mostly about ownership and policy. The inventory point is GOVERN 1.6 in the framework: mechanisms to inventory AI systems, resourced according to risk.

A one-page policy plus a register is a realistic first step for any department represented here."""),
    ("MAP", "Function 2", "Context is recognized and risks related to context are identified.",
     ["What exactly is the system for, and what is it not for?", "Who uses it, on which data, and who is affected by its outputs?",
      "Could the capability be misused, here or by others?", "Which laws, ethics approvals and client contracts apply?"],
     "Write the intended use down before the first run. Misuse is defined against it.",
     """MAP is about context. The single most useful artefact is a short intended-use statement. Without it, you cannot say when a use has gone beyond what was approved.

Dual use belongs here: the MegaSyn example was a mapping failure; nobody had asked how the model could be turned around."""),
    ("MEASURE", "Function 3", "Identified risks are assessed, analyzed, or tracked.",
     ["Was performance checked on our own samples, not only the vendor’s benchmark?", "How do we detect drift when reagents, instruments or staining change?",
      "Has anyone tried to make it fail on purpose (red-teaming)?", "Are errors logged and reviewed, with a human able to override?"],
     "Validate locally, then keep measuring. A model validated once is validated for the past.",
     """MEASURE is where scientists feel at home: validation, error rates, controls. The point to stress is that measurement continues after deployment, because data and conditions change.

Red-teaming in a lab can be simple: give the tool deliberately difficult or out-of-scope inputs and record what happens."""),
    ("MANAGE", "Function 4", "Risks are prioritized and acted upon based on a projected impact.",
     ["Deploy, restrict, or do not deploy: who decides, on what evidence?", "What is the response plan when the tool produces harmful or wrong output?",
      "How are vendor model updates tested before they reach the bench?", "When is a system retired, and what happens to its data?"],
     "Treat a silent model update like a change of reagent lot: test before use.",
     """MANAGE turns measurements into decisions and keeps them current. Vendor updates are a practical risk: a cloud model can change overnight without notice.

The reagent-lot analogy usually lands well with laboratory scientists."""),
]
for k, (nm, eb, df, qs, start, note) in enumerate(FNS):
    rs, rc = rmf_svg(260, (nm,), left=1532, top=40, eid="rmf")
    body = rs + pin(128, 270, 1300, P(df, 36, BODY2, lh=1.32), build="fade 1 auto")
    body += f'<p data-build-in="fade 2 auto" style="position:absolute;left:128px;top:356px;width:1000px;font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{TEALT}">Questions for a research laboratory</p>'
    for j, q in enumerate(qs):
        r, c2 = divmod(j, 2)
        body += (f'<div data-build-in="rise {j + 3} auto" style="position:absolute;left:{128 + c2 * 844}px;top:{410 + r * 160}px;width:820px;height:136px;display:flex;flex-direction:row;gap:20px;align-items:center;background:#FFFFFF;padding:22px 28px;border-radius:18px;border-top:6px solid {ORANGE if nm == "GOVERN" else BLUE};box-shadow:0 10px 32px rgba(19,41,75,0.08)">'
                 f'<p style="font-family:{SERIF};font-size:48px;font-weight:600;color:{ORANGE if nm == "GOVERN" else BLUE}">{j + 1}</p><p style="flex:1;font-size:28px;line-height:1.32;color:{TEXT}">{q}</p></div>')
    body += lens(760, start, label="Start here", build="rise 8 auto")
    content(D, f"fn-{nm.lower()}", eb, nm.capitalize(), body, transition="magic", illus_html="", notes=note)

# 14 GenAI profile
RISKS = [("CBRN Information or Capabilities", 1), ("Confabulation", 1), ("Dangerous, Violent, or Hateful Content", 0), ("Data Privacy", 1),
         ("Environmental Impacts", 0), ("Harmful Bias and Homogenization", 0), ("Human-AI Configuration", 1), ("Information Integrity", 1),
         ("Information Security", 1), ("Intellectual Property", 1), ("Obscene, Degrading, and/or Abusive Content", 0), ("Value Chain and Component Integration", 1)]
body = ""
for k, (nm, hot) in enumerate(RISKS):
    r, c2 = divmod(k, 4)
    body += (f'<div data-build-in="pop {k + 1} auto" style="position:absolute;left:{128 + c2 * 422}px;top:{300 + r * 166}px;width:398px;height:146px;display:flex;flex-direction:column;gap:6px;background:{"#FFFFFF" if hot else "#EEF2F7"};padding:20px 24px;border-radius:16px;border-top:6px solid {ORANGE if hot else GREY};{"box-shadow:0 10px 28px rgba(19,41,75,0.08)" if hot else ""}">'
             f'<p style="font-family:{MONO};font-size:24px;font-weight:600;color:{ORANGET if hot else MUTE}">{k + 1:02d}</p><p style="font-size:27px;line-height:1.25;font-weight:{600 if hot else 400};color:{NAVY if hot else MUTE}">{nm}</p></div>')
body += f'<div data-build-in="fade 13 auto" style="position:absolute;left:128px;top:812px;width:1664px;display:flex;flex-direction:row;gap:16px;align-items:center"><div style="width:40px;height:8px;background:{ORANGE};border-radius:4px"></div><p style="font-size:26px;color:{BODY2}">Highlighted: the eight that matter most in a research laboratory</p></div>'
content(D, "genai", "Generative AI Profile · NIST AI 600-1 · July 2024", "Twelve risks made worse by generative AI", body, ill="chat",
        notes="""The Generative AI Profile lists twelve risks; they pop in one by one. The eight with orange tops matter most to us: CBRN information, confabulation, data privacy, human-AI configuration (over-reliance), information integrity, information security, intellectual property, and the value chain, meaning the third-party models and plug-ins you build on.

The first one, CBRN information or capabilities, is the one this workshop exists for.""")


# 15 confabulation (navy)
def confab(i, n):
    inner = progress(i, n, True) + bg_network() + illus("chat", left=1430, top=90)
    inner += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:170px;width:1000px;font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{MINT}">Confabulation</p>'
    inner += f'<h2 data-build-in="rise 2 auto" style="position:absolute;left:128px;top:220px;width:1300px;font-family:{SERIF};font-size:110px;font-weight:600;line-height:1.05;color:{CREAM}">A fluent answer</h2>'
    inner += f'<h2 data-build-in="rise 3 auto" style="position:absolute;left:128px;top:345px;width:1400px;font-family:{SERIF};font-size:110px;font-weight:600;line-height:1.05;color:{SAND}">is not a verified one.</h2>'
    cards = [("References", "Plausible citations with invented authors, journals or DOIs"), ("Protocols", "Concentrations, incubation times or biosafety levels stated with confidence and no source"),
             ("Lab rule", "Every AI-assisted citation is DOI-checked; every protocol step is checked against the SOP or primary source")]
    for k, (t, b) in enumerate(cards):
        hot = k == 2
        inner += (f'<div data-build-in="rise {k + 4} auto" style="position:absolute;left:{128 + k * 563}px;top:580px;width:539px;display:flex;flex-direction:column;gap:12px;background:{SAND if hot else "#1B3866"};padding:30px 32px;border-radius:20px">'
                  f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{NAVY if hot else MINT}">{t}</p><p style="font-size:28px;line-height:1.38;color:{NAVY if hot else CREAM}">{b}</p></div>')
    inner += footer(D.foot, i + 1, True)
    return section("confab", inner, True, "fade", """Confabulation is NIST's term for what people call hallucination. In research it shows up as fake references and as invented protocol parameters.

The lab rule on the last card is simple and enforceable. It also protects research integrity, which is a cyberbiosecurity outcome in its own right.""")
D.add("confab", confab)

# 16 AI as target
ATT = [("1", "Data poisoning", "Corrupt the training or reference data so the model learns the wrong thing", BLUE),
       ("2", "Prompt injection", "Hide instructions in a document or web page the assistant reads", ORANGE),
       ("3", "Supply chain", "Tampered model weights, packages or plug-ins from third parties", TEAL),
       ("4", "Privacy attacks", "Infer or extract sensitive training data, such as patient records", BLUE)]
items = [f'<p style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1;color:{col}">{nmb}</p><h3 style="font-size:32px;font-weight:600;color:{NAVY}">{t}</h3><p style="font-size:27px;line-height:1.38;color:{BODY2}">{b}</p>' for nmb, t, b, col in ATT]
body = cards_row(items, top=300, accent_cycle=[BLUE, ORANGE, TEAL, BLUE], pad="30px 30px")
body += callout(720, "These map back to yesterday’s CSF functions: PR.DS for data, GV.SC for the supply chain, DE.AE for spotting abuse.", label="Link to CSF", icon="Link", build="rise 6 auto")
content(D, "target", "AI as the target · NIST AI 100-2 E2025", "The model is also an asset to attack", body, ill="lock",
        notes="""So far the AI was the source of risk. Here it is the target. NIST's adversarial machine learning taxonomy names the classes of attack; four are enough for a lab audience.

Prompt injection deserves a minute: an assistant that reads a supplier's PDF or a web page can be instructed by text hidden inside it. Anyone connecting an assistant to email or files should know this.""")

# 17 Cyber AI profile
SDT = [("S", "Secure", "Securing AI system components", BLUE), ("D", "Defend", "Using AI to strengthen cyber defence", TEAL), ("T", "Thwart", "Countering AI-enabled attacks", ORANGE)]
items = [f'<p style="font-family:{SERIF};font-size:130px;font-weight:600;line-height:1;color:{col}">{l}</p><h3 style="font-size:36px;font-weight:600;color:{NAVY}">{t}</h3><p style="font-size:28px;line-height:1.38;color:{BODY2}">{b}</p>' for l, t, b, col in SDT]
body = cards_row(items, top=300, accent_cycle=[BLUE, TEAL, ORANGE], pad="34px 36px")
body += callout(720, "Preliminary draft, 16 Dec 2025; comments closed 30 Jan 2026. You do not need a separate AI security programme: extend the CSF programme you already have.", label="Status", icon="Clock", build="rise 4 auto")
content(D, "cyberai", "Where the two frameworks meet · NIST IR 8596", "The Cyber AI Profile applies CSF 2.0 to AI", body, ill="network",
        notes="""This is the bridge we promised yesterday. The Cyber AI Profile is a CSF 2.0 community profile for AI, with three focus areas: secure, defend, thwart.

It is a preliminary draft, so cite it as such. For an institution, the practical message is that you extend the CSF programme you already have.""")

# 18 worked case
ROWS = [("GOVERN", "Owner named; tool added to the AI register; use limited to research images, no patient identifiers", ORANGE),
        ("MAP", "Intended use: viability scoring of MTT and live/dead images; not for regulatory submissions", BLUE),
        ("MEASURE", "Compared with two blinded human scorers on 300 local images; re-checked when stain lot or microscope changes", BLUE),
        ("MANAGE", "Low-confidence scores go to a human; vendor updates tested on a frozen image set before use", BLUE)]
body = ""
for k, (f, t, col) in enumerate(ROWS):
    body += (f'<div data-build-in="left {k + 1} auto" style="position:absolute;left:128px;top:{310 + k * 140}px;width:1664px;height:118px;display:flex;flex-direction:row;gap:30px;align-items:center;background:#FFFFFF;padding:20px 30px;border-radius:18px;box-shadow:0 8px 24px rgba(19,41,75,0.07)">'
             f'<p style="width:200px;font-family:{MONO};font-size:28px;font-weight:600;text-align:center;color:#FFFFFF;background:{col};padding:10px 0;border-radius:12px">{f}</p><p style="flex:1;font-size:29px;line-height:1.35;color:{TEXT}">{t}</p></div>')
body += src("Illustrative design for a pharmacology laboratory; not data from a real study", 880)
content(D, "case", "Worked case · illustrative", "A cytotoxicity lab adopts an AI classifier", body, ill="eye",
        notes="""An illustrative case from our own kind of work: a pharmacology lab that scores cell viability images with an AI classifier. One row per function.

Note how concrete each line is. That is the test of a good AI RMF implementation: each function produces a decision or a record someone can check. The numbers here are an example design, not a real study.""")

# 19 register (table)
REG = [("Image classifier", "Viability scoring", "Microscopy images", "Lab head", "Medium", "Low-confidence cases", "Each lot change"),
       ("LLM assistant", "Drafting SOP text", "No client or patient data", "Biosafety officer", "Medium", "Every step vs. source", "Quarterly"),
       ("Sequence screening", "Order checks", "Synthetic DNA orders", "Core facility manager", "High", "All flagged hits", "Monthly")]
hdr = ["System", "Use", "Data", "Owner", "Risk", "Human check", "Review"]
wd = [16, 14, 16, 16, 9, 16, 13]
tbl = (f'<table data-build-in="rise 1 auto" style="position:absolute;left:128px;top:320px;width:1664px;font-size:26px;color:{TEXT};background:#FFFFFF;border-radius:16px">'
       + "<tr>" + "".join(f'<th style="width:{wd[k]}%;background:{NAVY};color:#FFFFFF;padding:16px 18px">{h}</th>' for k, h in enumerate(hdr)) + "</tr>"
       + "".join("<tr>" + "".join(f'<td style="{"color:" + ORANGET + ";font-weight:700" if c == "High" else ""}">{c}</td>' for c in r) + "</tr>" for r in REG) + "</table>")
body = tbl + callout(720, "Seven columns, one row per AI system. Start it this week; refine it at the next lab meeting.", label="Example rows", icon="CheckCircle", build="rise 2 auto")
content(D, "register", "A minimal AI register", "One table makes GOVERN real", body, ill="checklist",
        notes="""Example rows only. The register is the smallest artefact that makes GOVERN real: it names the system, its purpose, its data, its owner, a risk level, where a human checks, and when it is reviewed.

Encourage participants to start one for their own group this week.""")

statement(D, "five", ["Who owns it?", "What data does it see?", "What happens when it is wrong?", "Could it be turned around?", "How will we know it changed?"],
          """Five questions, one per click. They map to the functions: ownership is GOVERN, data and misuse are MAP, being wrong and changing are MEASURE and MANAGE.

If participants remember only one slide from this session, this should be it.""",
          eyebrow="Before any AI tool enters the lab", size=84, colors=[CREAM, CREAM, CREAM, SAND, CREAM], ill_html=illus("ai", left=1430, top=90))

# 21 next
NX = [("10:30", "Artificial Intelligence in Life Sciences", "Opportunities, risks and responsible use · Prof. Dr. Gökçe Merey", BLUE),
      ("11:30", "Institutional Cybersecurity Infrastructure", "A practical case study", BLUE),
      ("14:30", "Hands-on: apply CSF 2.0 to a biotechnology lab", "Your lab’s AI tools belong in that profile too", ORANGE)]
body = ""
for k, (t, h, s, col) in enumerate(NX):
    body += (f'<div data-build-in="left {k + 1} auto" style="position:absolute;left:128px;top:{300 + k * 180}px;width:1664px;height:152px;display:flex;flex-direction:row;gap:40px;align-items:center;background:#FFFFFF;padding:24px 36px;border-radius:20px;border-left:10px solid {col};box-shadow:0 10px 32px rgba(19,41,75,0.08)">'
             f'<p style="width:220px;font-family:{SERIF};font-size:72px;font-weight:600;color:{col}">{t}</p><div style="flex:1;display:flex;flex-direction:column;gap:6px"><h3 style="font-size:34px;font-weight:600;color:{NAVY}">{h}</h3><p style="font-size:26px;color:{BODY2}">{s}</p></div></div>')
content(D, "next", "Where this goes next today", "The rest of Day 2", body, ill="clock",
        notes="""Hand over to Prof. Merey's session on AI in the life sciences, which takes the applications side. Remind groups that the afternoon exercise includes AI tools in the scenario.""")

refs(D, "refs", [
    "Tabassi E. <i>Artificial Intelligence Risk Management Framework (AI RMF 1.0)</i>. NIST AI 100-1; 2023. doi:10.6028/NIST.AI.100-1",
    "NIST. <i>AI RMF: Generative Artificial Intelligence Profile</i>. NIST AI 600-1; 2024. doi:10.6028/NIST.AI.600-1",
    "Vassilev A, et al. <i>Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations</i>. NIST AI 100-2 E2025; 2025. doi:10.6028/NIST.AI.100-2e2025",
    "NIST. <i>Cybersecurity Framework Profile for Artificial Intelligence</i>. NIST IR 8596, initial preliminary draft; 16 Dec 2025.",
    "Urbina F, Lentzos F, Invernizzi C, Ekins S. Dual use of artificial-intelligence-powered drug discovery. <i>Nat Mach Intell</i>. 2022;4(3):189–191. doi:10.1038/s42256-022-00465-9",
    "NIST. AI Risk Management Framework (status of revision and profiles); accessed 21 Oct 2026.",
    "National Institute of Standards and Technology. <i>The NIST Cybersecurity Framework (CSF) 2.0</i>. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
])
thanks(D, "thanks", "Questions on AI risk in the laboratory", "Take questions. If someone asks whether a specific AI tool is allowed, route it to the five questions and the register.")

SECTIONS = {"s1": {"description": "Why AI risk in laboratories needs its own framework", "start": "cover"},
            "s2": {"description": "AI RMF: trustworthiness and the four functions", "start": "glance"},
            "s3": {"description": "Generative AI risks, AI as a target, and the Cyber AI Profile", "start": "genai"},
            "s4": {"description": "Applying it in a laboratory", "start": "case"}}

if __name__ == "__main__":
    import sys
    write_deck(sys.argv[1], "AI RMF · Research Laboratories", SECTIONS, D.render())
    print("ok", len(D.slides))
