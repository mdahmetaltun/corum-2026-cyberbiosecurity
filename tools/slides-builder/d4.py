import math
from common import *

D = Deck("Hands-on · Applying NIST CSF 2.0 to a Biotechnology Lab · Çorum 2026")
VID = ("/_blob/340cf16a8f338ef05833eca63432cbcb", "/_blob/3bff7d93a8ab44c9bf97aaf11ff98b01")
TOOL = "https://claude.ai/artifact/1LZkxgu56oodvpnb2BBqLr"

CATS = [("GV.RR", "Roles, responsibilities &amp; authorities", "GV"), ("GV.PO", "Policy", "GV"), ("GV.SC", "Supply chain risk management", "GV"),
        ("ID.AM", "Asset management", "ID"), ("ID.RA", "Risk assessment", "ID"),
        ("PR.AA", "Identity, authentication &amp; access", "PR"), ("PR.AT", "Awareness &amp; training", "PR"), ("PR.DS", "Data security", "PR"), ("PR.PS", "Platform security", "PR"),
        ("DE.CM", "Continuous monitoring", "DE"), ("RS.MA", "Incident management", "RS"), ("RC.RP", "Recovery plan execution", "RC")]


def navy(sid, notes, ill=None, transition="fade"):
    def wrap(body):
        def f(i, n):
            inner = progress(i, n, True) + bg_network() + (illus(ill, left=1430, top=90) if ill else "")
            inner += body(i, n) + footer(D.foot, i + 1, True)
            return section(sid, inner, True, transition, notes)
        D.add(sid, f)
        return body
    return wrap


def eyebrow(text, top, build="fade 1 auto"):
    return f'<p data-build-in="{build}" style="position:absolute;left:128px;top:{top}px;width:1300px;font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{MINT}">{text}</p>'


def helix_big(left, top, w=520, h=640):
    st = (".s{animation:s 3s ease-in-out infinite}.s2{animation-delay:-1.5s}@keyframes s{50%{transform:translateX(0);opacity:1}}"
          ".b{transform-box:fill-box;transform-origin:center;animation:b 3s ease-in-out infinite}@keyframes b{0%,100%{transform:scaleX(1)}50%{transform:scaleX(-1)}}" + RM)
    b = ""
    for k in range(12):
        y = 30 + k * 50
        dl = -k * 0.25
        col = [BLUE, TEAL, SAND, ORANGE][k % 4]
        b += (f'<g class="b" style="animation-delay:{dl:.2f}s"><line x1="{w * 0.18:.0f}" y1="{y}" x2="{w * 0.82:.0f}" y2="{y}" stroke="{col}" stroke-width="5" stroke-linecap="round" opacity=".85"/>'
              f'<circle cx="{w * 0.18:.0f}" cy="{y}" r="12" fill="{MINT}"/><circle cx="{w * 0.82:.0f}" cy="{y}" r="12" fill="{SKY}"/></g>')
    return (f'<svg aria-label="Animated DNA helix" width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{h}px"><style>{st}</style>{b}</svg>')


# 1 cover
cover(D, "cover", "Day 2 · Tuesday 3 November 2026 · 14:30–15:15",
      ["Hands-on:", "Apply it."], "Build a CSF 2.0 profile for a biotechnology laboratory in 45 minutes",
      "Cyberbiosecurity Training Workshop · Hitit University, Çorum",
      helix_big(1240, 200),
      """This is where the two days come together. Each group becomes the cyberbiosecurity working group of a fictional laboratory and produces a small Organizational Profile and a three-item action plan. Group presentations follow at 15:30.

Ideally five or six groups of four to six people, mixing institutions and roles.""")
video(D, "film", VID[0], VID[1], "Opening film: one laboratory, six functions, twenty-two categories, forty-five minutes",
      "Opening film, about 10 seconds. Advance when it reaches the title card.")


# 3 mission
@navy("mission", """Read the mission aloud. The three deliverables mirror steps 1 to 4 of NIST's quick-start guide from yesterday: scope, gather, create, analyse and plan.""", ill="target")
def _(i, n):
    h = eyebrow("Your mission", 190)
    h += f'<h2 data-build-in="rise 2 auto" style="position:absolute;left:128px;top:240px;width:1250px;font-family:{SERIF};font-size:76px;font-weight:600;line-height:1.08;color:{CREAM}">You are HelixLab’s new <span style="color:{SAND}">cyberbiosecurity working group.</span></h2>'
    DL = [("Deliver 1", "Crown jewels and scope", MINT), ("Deliver 2", "Current and Target Profile for 12 categories", SKY), ("Deliver 3", "Top three actions, with owners", SAND)]
    for k, (a, b, col) in enumerate(DL):
        h += (f'<div data-build-in="rise {k + 3} auto" style="position:absolute;left:{128 + k * 563}px;top:560px;width:539px;height:230px;display:flex;flex-direction:column;gap:14px;background:{"#1B3866" if k < 2 else SAND};padding:32px 34px;border-radius:22px;border-top:8px solid {col}">'
              f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{col if k < 2 else NAVY}">{a}</p><h3 style="font-family:{SERIF};font-size:38px;font-weight:600;line-height:1.15;color:{CREAM if k < 2 else NAVY}">{b}</h3></div>')
    h += f'<p data-build-in="fade 6 auto" style="position:absolute;left:128px;top:820px;width:1600px;font-size:30px;color:{SKY}">Presented in <b style="color:{SAND}">three minutes per group</b> at 15:30.</p>'
    return h


# 4 fact sheet
FACTS = [("Users", "People", "6 staff · 18 graduate students · 2 client technicians with badge access", BLUE),
         ("Link", "Clients", "3 biotech companies send samples and receive sequencing data", ORANGE),
         ("Globe", "Network", "One campus network for everything; lab Wi-Fi password on the door", BLUE)]
items = [f'<div style="display:flex;flex-direction:row;gap:14px;align-items:center"><x-icon name="{ic}" style="width:40px;height:40px;color:{col}"></x-icon><p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{TEALT if col == BLUE else ORANGET}">{a}</p></div>' + P(b, 27, TEXT, lh=1.35) for ic, a, b, col in FACTS]
body = cards_row(items, top=270, accent_cycle=[BLUE, ORANGE, BLUE], pad="22px 28px", height=190)
ASSETS = [("NGS sequencer", "Windows 10 control PC; vendor cloud upload; vendor remote support tool"), ("2 × qPCR systems", "Results exported by USB stick to the analysis PC"),
          ("4 × −80 °C freezers", "Wi-Fi alarm module sends SMS to the lab head"), ("LIMS", "Cloud service; one shared admin account"),
          ("Analysis server", "Linux; 18 student accounts; no central logs"), ("AI tools", "Chat assistant for SOP drafts; image classifier for cell counts")]
body += f'<p data-build-in="fade 4 auto" style="position:absolute;left:128px;top:490px;width:600px;font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{MUTE}">Systems</p>'
for k, (a, b) in enumerate(ASSETS):
    r, c = divmod(k, 3)
    body += (f'<div data-build-in="rise {k + 5} auto" style="position:absolute;left:{128 + c * 563}px;top:{540 + r * 175}px;width:539px;height:155px;display:flex;flex-direction:column;gap:6px;background:#FFFFFF;padding:20px 26px;border-radius:16px;border-left:6px solid {TEAL};box-shadow:0 8px 24px rgba(19,41,75,0.07)">'
             f'<h3 style="font-size:30px;font-weight:600;color:{NAVY}">{a}</h3><p style="font-size:25px;line-height:1.32;color:{BODY2}">{b}</p></div>')
content(D, "helix", "Fact sheet · HelixLab (fictional)", "A university biotechnology laboratory, BSL-2", body, ill="helix",
        notes="""The fact sheet is deliberately realistic: every detail is something seen in real laboratories. Give groups two minutes to read it. The three client companies make supply-chain governance relevant, and the AI tools link back to this morning.""")


# 5 injects (navy)
@navy("injects", """Reveal the three events one at a time. They are the evidence groups should use. Don't tell them which categories each maps to; that is in the debrief slide.""", ill="bell")
def _(i, n):
    h = eyebrow("Three things that happened this month", 190)
    INJ = [("Friday 18:30", "An email from the “sequencer vendor” asks the lab to install an urgent firmware update via a download link before Monday.", "PaperPlane", SAND),
           ("Last week", "Freezer alarm SMS messages stopped arriving three days ago. Nobody noticed until a sample check.", "Warning", MINT),
           ("Yesterday", "A student pasted a client’s sample sheet, with project codes and donor ages, into a public AI chatbot to reformat it.", "Chat", SKY)]
    for k, (d, t, ic, col) in enumerate(INJ):
        h += (f'<div data-build-in="rise {k + 2} auto" style="position:absolute;left:{128 + k * 563}px;top:260px;width:539px;height:500px;display:flex;flex-direction:column;gap:18px;background:#1B3866;padding:36px 36px;border-radius:22px;border-top:8px solid {col}">'
              f'<div style="display:flex;flex-direction:row;gap:18px;align-items:center"><p style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1;color:{col}">{k + 1}</p><x-icon name="{ic}" style="width:52px;height:52px;color:{col}"></x-icon></div>'
              f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{col}">{d}</p><p style="font-size:31px;line-height:1.38;color:{CREAM}">{t}</p></div>')
    h += f'<p data-build-in="fade 5 auto" style="position:absolute;left:128px;top:810px;width:1600px;font-size:30px;line-height:1.4;color:{SKY}">Use them as evidence when you rate the Current Profile. <b style="color:{SAND}">Each one points to at least two categories.</b></p>'
    return h


# 6 roles
ROLES = [("Lab head", "Chairs; owns the final decisions", "Star"), ("Biosafety officer", "Samples, containment, cold chain", "Warning"), ("IT / network", "Systems, accounts, logs, backups", "Settings"),
         ("Data steward", "Client data, KVKK, AI tool use", "Database"), ("Vendor manager", "Contracts, remote access, procurement", "Link"), ("Rapporteur", "Records ratings; presents at 15:30", "Chat")]
items = [f'<x-icon name="{ic}" style="width:48px;height:48px;color:{ORANGET if k == 5 else BLUE}"></x-icon><h3 style="font-family:{SERIF};font-size:44px;font-weight:600;color:{NAVY}">{a}</h3>' + P(b, 28, BODY2) for k, (a, b, ic) in enumerate(ROLES)]
body = cards_row(items[:3], top=290, accent_cycle=[BLUE, TEAL, BLUE], pad="28px 32px", height=270) + cards_row(items[3:], top=590, build_start=4, accent_cycle=[TEAL, BLUE, ORANGE], pad="28px 32px", height=270)
content(D, "roles", "Take a role", "Six seats at the table. Argue from yours.", body, ill="people",
        notes="""Ask each group to assign roles now; with fewer than six people, combine vendor manager with data steward. Role-play creates productive disagreement, especially between IT and the biosafety officer.""")


# 7 phases / clock
PHASES = [("Scope &amp; crown jewels", 8), ("Rate the Current Profile", 12), ("Set Target &amp; find gaps", 10), ("Top-3 action plan", 10), ("Prepare the 3-minute pitch", 5)]


def phase_ring(left, top, size=560):
    c = size / 2
    r = size * 0.42
    circ = 2 * math.pi * r
    segs = ""
    acc = 0
    cols = [MINT, SKY, BLUE, SAND, ORANGE]
    for k, (_, m) in enumerate(PHASES):
        ln = circ * m / 45
        segs += f'<circle cx="{c}" cy="{c}" r="{r:.1f}" fill="none" stroke="{cols[k]}" stroke-width="26" stroke-dasharray="{ln - 8:.1f} {circ:.1f}" stroke-dashoffset="{-acc:.1f}" transform="rotate(-90 {c} {c})"/>'
        acc += ln
    st = (f".h{{transform-origin:{c}px {c}px;animation:h 12s linear infinite}}@keyframes h{{to{{transform:rotate(360deg)}}}}"
          f".g{{transform-box:fill-box;transform-origin:center;animation:g 2s ease-in-out infinite}}@keyframes g{{50%{{transform:scale(1.15)}}}}" + RM)
    hand = f'<g class="h"><line x1="{c}" y1="{c}" x2="{c}" y2="{c - r + 30:.0f}" stroke="{CREAM}" stroke-width="6" stroke-linecap="round"/><circle class="g" cx="{c}" cy="{c - r:.0f}" r="16" fill="{CREAM}"/></g>'
    return (f'<svg aria-label="Forty-five minutes divided into five phases" width="{size}" height="{size}" viewBox="0 0 {size} {size}" style="position:absolute;left:{left}px;top:{top}px;width:{size}px;height:{size}px"><style>{st}</style>'
            f'<circle cx="{c}" cy="{c}" r="{r:.1f}" fill="none" stroke="#2E4A72" stroke-width="26"/>{segs}{hand}<circle cx="{c}" cy="{c}" r="14" fill="{CREAM}"/></svg>')


@navy("clock", f"""Five phases, 45 minutes. The ring shows the share of time per phase.

For a live countdown, open the interactive tool ({TOOL}) on a second tab: its timer slide counts each phase down and moves on automatically.""")
def _(i, n):
    h = eyebrow("45 minutes · five phases", 190)
    cols = [MINT, SKY, BLUE, SAND, ORANGE]
    for k, (a, m) in enumerate(PHASES):
        h += (f'<div data-build-in="left {k + 2} auto" style="position:absolute;left:128px;top:{250 + k * 118}px;width:900px;height:100px;display:flex;flex-direction:row;gap:26px;align-items:center;background:#1B3866;padding:14px 28px;border-radius:16px;border-left:10px solid {cols[k]}">'
              f'<p style="width:60px;font-family:{SERIF};font-size:56px;font-weight:600;color:{cols[k]}">{k + 1}</p><p style="flex:1;font-size:34px;font-weight:600;color:{CREAM}">{a}</p>'
              f'<p style="font-family:{MONO};font-size:32px;font-weight:600;color:{cols[k]}">{m} min</p></div>')
    h += phase_ring(1180, 250)
    h += f'<p style="position:absolute;left:1260px;top:490px;width:400px;font-family:{SERIF};font-size:96px;font-weight:600;text-align:center;color:{CREAM}">45′</p>'
    return h


# 8 scope
L1 = ["Which systems are in scope? Which are not?", "Which laws and contracts apply? (Law 7545, KVKK, client contracts)", "Who would be harmed if HelixLab were down for two weeks?"]
L2 = [("Lost", "What must never be lost?", "Availability"), ("Leaked", "What must never leak?", "Confidentiality"), ("Altered", "What must never be altered without anyone noticing?", "Integrity")]
body = (f'<div data-build-in="rise 1 auto" style="position:absolute;left:128px;top:290px;width:820px;height:560px;display:flex;flex-direction:column;gap:22px;background:#FFFFFF;padding:36px 40px;border-radius:20px;border-top:8px solid {BLUE};box-shadow:0 10px 32px rgba(19,41,75,0.08)">'
        f'<p style="font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{TEALT}">Answer together</p>'
        + "".join(f'<div style="display:flex;flex-direction:row;gap:18px;align-items:start"><x-icon name="CheckCircle" style="width:36px;height:36px;color:{BLUE}"></x-icon><p style="flex:1;font-size:30px;line-height:1.35;color:{TEXT}">{t}</p></div>' for t in L1) + "</div>")
body += f'<p data-build-in="fade 2 auto" style="position:absolute;left:1000px;top:290px;width:792px;font-size:24px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:{ORANGET}">Crown jewels · pick three</p>'
for k, (a, b, c) in enumerate(L2):
    body += (f'<div data-build-in="left {k + 3} auto" style="position:absolute;left:1000px;top:{340 + k * 172}px;width:792px;height:150px;display:flex;flex-direction:row;gap:24px;align-items:center;background:{NAVY};padding:20px 30px;border-radius:18px">'
             f'<p style="width:170px;font-family:{SERIF};font-size:48px;font-weight:600;color:{SAND}">{a}</p><div style="flex:1;display:flex;flex-direction:column;gap:4px"><p style="font-size:28px;line-height:1.3;color:{CREAM}">{b}</p><p style="font-size:24px;color:{MINT}">{c}</p></div></div>')
content(D, "scope", "Phase 1 · 8 minutes · GV.OC, ID.AM", "Scope it, then name the crown jewels", body, ill="target",
        notes="""Eight minutes. Lost, leaked, altered: those three questions map to availability, confidentiality and integrity, the CIA triad from yesterday's introduction. Good answers usually include the client data, the freezer contents and the sequencing results.""")

# 9 rating guide
TG = [("1", "Partial", "Nobody owns it; it happens if someone remembers", ORANGET), ("2", "Risk informed", "People know it matters; it is not written policy", GOLD),
      ("3", "Repeatable", "Written, approved, done the same way every time", BLUE), ("4", "Adaptive", "Measured and improved from lessons learned", TEALT)]
body = ""
for k, (nm, a, b, col) in enumerate(TG):
    hgt = 280 + k * 35
    body += (f'<div data-build-in="rise {k + 1} auto" style="position:absolute;left:{128 + k * 422}px;top:{660 - hgt}px;width:398px;height:{hgt}px;display:flex;flex-direction:column;gap:8px;justify-content:end;background:#FFFFFF;padding:24px 28px;border-radius:18px;border-top:8px solid {col};box-shadow:0 10px 32px rgba(19,41,75,0.08)">'
             f'<p style="font-family:{SERIF};font-size:80px;font-weight:600;line-height:1;color:{col}">{nm}</p><h3 style="font-size:32px;font-weight:600;color:{NAVY}">{a}</h3><p style="font-size:25px;line-height:1.32;color:{BODY2}">{b}</p></div>')
for k, (c, _, f) in enumerate(CATS):
    body += f'<p data-build-in="pop 5 auto" style="position:absolute;left:{128 + k * 139}px;top:690px;width:127px;font-family:{MONO};font-size:24px;font-weight:600;text-align:center;color:{NAVY};background:{PALE2};padding:8px 0;border-radius:10px">{c}</p>'
body += pin(128, 770, 1664, P("Twelve categories chosen from the 22 for this lab. <b>Be honest about Current; be realistic about Target.</b> Most targets land on 2 or 3.", 28, BODY2), build="fade 6 auto")
content(D, "rate", "Phases 2–3 · rating guide", "Rate each category from 1 to 4", body, illus_html="",
        notes="""A plain-language version of the CSF tiers for rating categories. Remind groups: tier 4 everywhere is not a sensible target for a teaching-and-research lab. Most targets land on 2 or 3.

Twelve categories keeps it achievable in the time; they are the ones the fact sheet and the three events give evidence for.""")


# 10 worksheet (example profile + radar)
exec(open("/tmp/claude-0/-home-claude/6c3aefa0-5919-57de-a397-a857f2da152f/scratchpad/radar_fn.py").read())
EXC = {'GV.RR': 1, 'GV.PO': 1, 'GV.SC': 1, 'ID.AM': 2, 'ID.RA': 1, 'PR.AA': 1, 'PR.AT': 2, 'PR.DS': 1, 'PR.PS': 1, 'DE.CM': 1, 'RS.MA': 1, 'RC.RP': 2}
EXT = {'GV.RR': 3, 'GV.PO': 3, 'GV.SC': 3, 'ID.AM': 3, 'ID.RA': 3, 'PR.AA': 3, 'PR.AT': 3, 'PR.DS': 3, 'PR.PS': 2, 'DE.CM': 3, 'RS.MA': 3, 'RC.RP': 3}


def dots(v, col):
    return "".join(f'<div style="width:26px;height:26px;border-radius:13px;background:{col if j < v else "#E3E8EF"}"></div>' for j in range(4))


body = (f'<div data-build-in="fade 1 auto" style="position:absolute;left:128px;top:270px;width:1000px;display:flex;flex-direction:row;gap:14px;align-items:center;padding:0 14px">'
        f'<p style="width:120px;font-size:24px;font-weight:700;color:{MUTE}">Code</p><p style="flex:1;font-size:24px;font-weight:700;color:{MUTE}">Category</p>'
        f'<p style="width:150px;font-size:24px;font-weight:700;color:{BLUE}">Current</p><p style="width:150px;font-size:24px;font-weight:700;color:{ORANGET}">Target</p></div>')
for k, (c, nm, f) in enumerate(CATS):
    body += (f'<div data-build-in="left {2 + k // 4} auto" style="position:absolute;left:128px;top:{316 + k * 50}px;width:1000px;height:44px;display:flex;flex-direction:row;gap:14px;align-items:center;padding:0 14px;background:{"#FFFFFF" if k % 2 == 0 else "#EEF2F7"};border-radius:8px">'
             f'<p style="width:120px;font-family:{MONO};font-size:24px;font-weight:600;color:{NAVY}">{c}</p><p style="flex:1;font-size:24px;color:{TEXT}">{nm}</p>'
             f'<div style="width:150px;display:flex;flex-direction:row;gap:8px">{dots(EXC[c], BLUE)}</div><div style="width:150px;display:flex;flex-direction:row;gap:8px">{dots(EXT[c], ORANGE)}</div></div>')
FN = ["GV", "ID", "PR", "DE", "RS", "RC"]
avg = lambda d, fn: sum(d[c] for c, _, f in CATS if f == fn) / sum(1 for c, _, f in CATS if f == fn)
body += radar_svg(1190, 250, 560, [avg(EXC, f) for f in FN], [avg(EXT, f) for f in FN])
body += f'<div data-build-in="fade 6 auto" style="position:absolute;left:1240px;top:830px;width:500px;display:flex;flex-direction:row;gap:22px;align-items:center"><div style="width:30px;height:8px;background:{BLUE};border-radius:4px"></div><p style="font-size:24px;color:{BODY2}">Current</p><div style="width:30px;height:8px;background:{ORANGE};border-radius:4px"></div><p style="font-size:24px;color:{BODY2}">Target</p></div>'
content(D, "worksheet", "Example worksheet · HelixLab", "One row per category, one radar per group", body, illus_html="",
        notes=f"""An example of a finished worksheet, so groups see the target format. The radar averages categories per function.

For live rating during the session, the interactive profile builder with group tabs and automatic gap ranking is in the HTML tool: {TOOL}""")


# 11 interactive tool link (navy)
@navy("tool", f"""This slide points to the interactive companion: {TOOL}

It has the live 45-minute phase timer, the profile builder with Example and Group 1–6 tabs (click tiers; the radar and the top-three gaps update), and the action-plan form. Ratings stay in the browser it is opened in, so use one laptop for the whole session.""", ill="gauge")
def _(i, n):
    h = eyebrow("Interactive companion", 190)
    h += f'<h2 data-build-in="rise 2 auto" style="position:absolute;left:128px;top:240px;width:1250px;font-family:{SERIF};font-size:84px;font-weight:600;line-height:1.08;color:{CREAM}">Rate live, compare groups, <span style="color:{SAND}">keep the clock.</span></h2>'
    FT = [("Clock", "Phase timer", "Counts down each of the five phases and moves on by itself"), ("Chart", "Profile builder", "Example and Group 1–6 tabs; click tiers; radar and top-three gaps update"),
          ("CheckCircle", "Action plan", "Three rows: action, CSF code, owner, date, cost")]
    for k, (ic, a, b) in enumerate(FT):
        h += (f'<div data-build-in="rise {k + 3} auto" style="position:absolute;left:{128 + k * 563}px;top:470px;width:539px;height:260px;display:flex;flex-direction:column;gap:14px;background:#1B3866;padding:32px 34px;border-radius:22px">'
              f'<x-icon name="{ic}" style="width:52px;height:52px;color:{MINT}"></x-icon><h3 style="font-size:36px;font-weight:600;color:{CREAM}">{a}</h3><p style="font-size:27px;line-height:1.35;color:{SKY}">{b}</p></div>')
    h += (f'<div data-build-in="fade 6 auto" style="position:absolute;left:128px;top:780px;width:1664px;display:flex;flex-direction:row;gap:24px;align-items:center;background:{SAND};padding:24px 34px;border-radius:18px">'
          f'<x-icon name="Link" style="width:44px;height:44px;color:{NAVY}"></x-icon><p style="font-family:{MONO};font-size:30px;font-weight:600;color:{NAVY}">claude.ai/artifact/1LZkxgu56oodvpnb2BBqLr</p>'
          f'<p style="flex:1;font-size:26px;text-align:right;color:{NAVY}">open on a second tab</p></div>')
    return h


# 12 action plan
HD = ["#", "Action", "CSF", "Owner", "By when", "Cost"]
CW = [80, 760, 200, 260, 200, 164]
body = (f'<div data-build-in="fade 1 auto" style="position:absolute;left:128px;top:280px;width:1664px;height:70px;display:flex;flex-direction:row;align-items:center;background:{NAVY};border-radius:14px">'
        + "".join(f'<p style="width:{CW[k]}px;padding:0 18px;font-size:24px;font-weight:600;color:#FFFFFF">{h}</p>' for k, h in enumerate(HD)) + "</div>")
EXR = ["Route all vendor remote support through one jump host with MFA and a ticket", "PR.AA · GV.SC", "IT / network", "6 weeks", "M"]
body += (f'<div data-build-in="left 2 auto" style="position:absolute;left:128px;top:366px;width:1664px;height:110px;display:flex;flex-direction:row;align-items:center;background:#FFF3EA;border-radius:14px;border-left:8px solid {ORANGE}">'
         f'<p style="width:72px;padding:0 18px;font-family:{SERIF};font-size:30px;font-weight:600;color:{ORANGET}">e.g.</p>'
         + "".join(f'<p style="width:{CW[k + 1]}px;padding:0 18px;font-size:26px;line-height:1.3;color:{TEXT}">{v}</p>' for k, v in enumerate(EXR)) + "</div>")
for r in range(3):
    body += (f'<div data-build-in="left {r + 3} auto" style="position:absolute;left:128px;top:{492 + r * 110}px;width:1664px;height:96px;display:flex;flex-direction:row;align-items:center;background:#FFFFFF;border-radius:14px;box-shadow:0 6px 18px rgba(19,41,75,0.06)">'
             f'<p style="width:80px;padding:0 18px;font-family:{SERIF};font-size:52px;font-weight:600;color:{BLUE}">{r + 1}</p>'
             + "".join(f'<div style="width:{CW[k]}px;padding:0 18px"><div style="height:3px;background:#DCE3EC"></div></div>' for k in range(1, 6)) + "</div>")
body += callout(838, "Push back on vague actions. “Improve awareness” of what, for whom, by when?", label="Facilitator", icon="Warning", build="rise 6 auto")
content(D, "plan", "Phase 4 · 10 minutes · the action plan", "Three actions. Each closes a named gap.", body, ill="checklist",
        notes="""Groups fill this on paper or in the interactive tool. A good action names the gap it closes, an owner by role, a date and a rough cost. Vague actions such as "improve awareness" should be pushed back: awareness of what, for whom, by when?""")


# 13 pitch
@navy("pitch", """The pitch format. Three minutes total, strictly timed. The question for the room at the end is often the best part of the presentations.""", ill="chat")
def _(i, n):
    h = eyebrow("15:30 · three minutes per group", 190)
    h += f'<h2 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:240px;width:1250px;font-family:{SERIF};font-size:80px;font-weight:600;color:{CREAM}">The 180-second pitch</h2>'
    PT = [("30″", "Our crown jewels", 30, MINT), ("45″", "Our biggest gap, and the evidence", 45, SKY), ("75″", "Our three actions and owners", 75, SAND), ("30″", "One question for the room", 30, MINT)]
    x = 128
    for k, (t, a, s, col) in enumerate(PT):
        w = 1664 * s / 180 - 16
        h += (f'<div data-build-in="left {k + 2} auto" style="position:absolute;left:{x:.0f}px;top:420px;width:{w:.0f}px;height:340px;display:flex;flex-direction:column;gap:14px;justify-content:end;background:{"#1B3866" if col != SAND else SAND};padding:28px 26px;border-radius:20px;border-top:8px solid {col}">'
              f'<p style="font-family:{SERIF};font-size:80px;font-weight:600;line-height:1;color:{col if col != SAND else NAVY}">{t}</p><p style="font-size:28px;line-height:1.3;font-weight:600;color:{CREAM if col != SAND else NAVY}">{a}</p></div>')
        x += w + 16
    h += f'<p data-build-in="fade 6 auto" style="position:absolute;left:128px;top:810px;width:1600px;font-size:30px;color:{SKY}">Bar widths are to scale. The action plan gets the most time.</p>'
    return h


# 14 debrief
DEB = [("Fake vendor email", ["GV.SC", "PR.AT", "PR.AA"], ORANGE), ("Freezer alarm went silent", ["DE.CM", "ID.AM", "RS.MA"], BLUE), ("Client data in a public chatbot", ["PR.DS", "GV.PO", "PR.AT"], TEAL)]
body = ""
for k, (t, cs, col) in enumerate(DEB):
    body += (f'<div data-build-in="left {k + 1} auto" style="position:absolute;left:128px;top:{290 + k * 160}px;width:1664px;height:136px;display:flex;flex-direction:row;gap:30px;align-items:center;background:#FFFFFF;padding:20px 34px;border-radius:18px;border-left:10px solid {col};box-shadow:0 10px 28px rgba(19,41,75,0.08)">'
             f'<p style="width:70px;font-family:{SERIF};font-size:72px;font-weight:600;color:{col}">{k + 1}</p><h3 style="flex:1;font-family:{SERIF};font-size:44px;font-weight:600;color:{NAVY}">{t}</h3>'
             + "".join(chip(c, bg=ORANGE if j == 0 else PALE2, size=28) for j, c in enumerate(cs)) + "</div>")
body += lens(790, "Most groups find their largest gap in GV.SC or DE.CM. Neither needs a big budget; both need an owner.", label="Pattern", build="rise 4 auto")
content(D, "debrief", "Facilitator debrief · after the presentations", "What the three events were pointing at", body, ill="scan",
        notes="""Use after the 15:30 group presentations. Reveal one event at a time and ask which groups caught which categories.

Closing point: the two most common big gaps, supply chain and monitoring, are mainly governance work. That brings us back to GOVERN at the centre of the wheel.""")


# 15 close
@navy("close", """Close the exercise. Encourage every participant to repeat the profile for their own laboratory within the month, starting with the inventory. Then move to the group presentations.""")
def _(i, n):
    h = helix_big(1360, 200)
    h += f'<h2 data-build-in="rise 1 auto" style="position:absolute;left:128px;top:330px;width:1250px;font-family:{SERIF};font-size:100px;font-weight:600;line-height:1.08;color:{CREAM}">Your profile is a draft.</h2>'
    h += f'<h2 data-build-in="rise 2 auto" style="position:absolute;left:128px;top:460px;width:1250px;font-family:{SERIF};font-size:100px;font-weight:600;line-height:1.08;color:{SAND}">Your lab is real.</h2>'
    for k, (t, bg, fc, w) in enumerate([("15:30 · Group presentations &amp; discussion", "#1B3866", CREAM, 640), ("Closing · evaluation · certificates", SAND, NAVY, 560)]):
        h += f'<p data-build-in="fade 3 auto" style="position:absolute;left:{128 + k * 680}px;top:720px;width:{w}px;font-size:26px;font-weight:600;color:{fc};background:{bg};padding:16px 24px;border-radius:14px">{t}</p>'
    return h


refs(D, "refs", [
    "National Institute of Standards and Technology. <i>The NIST Cybersecurity Framework (CSF) 2.0</i>. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
    "National Institute of Standards and Technology. <i>NIST Cybersecurity Framework 2.0: Organizational Profiles Quick-Start Guide</i>. NIST SP 1301; 2024. doi:10.6028/NIST.SP.1301",
    "NIST. <i>CSF 2.0 Organizational Profile Template</i>; 2024. csrc.nist.gov",
    "7545 sayılı Siber Güvenlik Kanunu. Resmî Gazete 32846; 19 Mar 2025. · 6698 sayılı Kişisel Verilerin Korunması Kanunu.",
    "HelixLab is a fictional teaching scenario written for this workshop.",
])
thanks(D, "thanks", "Group presentations follow at 15:30", "Thank the groups and move to the presentations.")

SECTIONS = {"s1": {"description": "Mission and scenario", "start": "cover"},
            "s2": {"description": "Running the exercise", "start": "clock"},
            "s3": {"description": "Presenting and debrief", "start": "pitch"}}

if __name__ == "__main__":
    import sys
    write_deck(sys.argv[1], "HelixLab CSF Exercise", SECTIONS, D.render())
    print("ok", len(D.slides))
