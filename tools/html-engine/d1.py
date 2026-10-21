from lib import *

FOOT = "NIST CSF 2.0 · Core Functions & Profiles"
S = []

S.append(lobby("lobby", "Day 1 · Monday 2 November", "13:30 – 14:30",
    ["NIST Cybersecurity", "Framework 2.0"], "Core Functions and Profiles for the research laboratory",
    """Holding screen while participants come back from lunch. The helix keeps moving so the room knows the session is about to start.

When you are ready, press the right arrow: the opening video plays and then advances by itself."""))

S.append(video("open", "media/opener.mp4", "media/opener.jpg",
    """Opening film, about 13 seconds. It moves from CSF 1.1's five functions to CSF 2.0, where GOVERN takes the centre. It advances to the title slide on its own when it ends."""))

S.append(section("title", f"""<canvas class="fx" data-fx="helix" data-x="1560"></canvas>
<p class="label" data-in="fade">Session 1 · NIST CSWP 29 · February 2024</p>
<div class="col" style="gap:0">
  <div class="mega" data-k="rise" style="font-size:150px">CORE FUNCTIONS</div>
  <div class="mega b" data-k="rise" data-d="250" style="font-size:150px">&amp; PROFILES</div>
</div>
<p class="lead muted" data-in="up" data-d="600">A common language for securing the biolab</p>
<div class="spacer"></div>
<div class="row" data-in="fade" data-d="900" style="gap:48px;align-items:flex-end">
  <div class="col" style="gap:4px"><p class="h3">{SPEAKER}</p><p class="small muted">{AFFIL}</p></div>
</div>""", "dark", "fade", "grid-bg", foot=EVENT, note="""Welcome back. This morning Prof. Gargılı set out why biological laboratories need cybersecurity. This hour gives that need a structure: the NIST Cybersecurity Framework, version 2.0.

Plan for the hour: why a framework, what changed in 2.0, the six functions with a laboratory example for each, how the Core is built, and then Tiers and Profiles, the part you will use tomorrow afternoon."""))

S.append(section("spafford", """<div class="spacer"></div>
<p class="quote" data-k="words" style="max-width:1640px">“The only truly secure system is one that is powered off, cast in a block of concrete and sealed in a lead-lined room with armed guards.”</p>
<p class="cite muted" data-in="fade" data-d="1500">Gene Spafford · computer security researcher, Purdue University</p>
<div class="spacer"></div>
<div class="h1 o" data-step="1" data-k="slam">Our laboratories are powered on.</div>""", "dark", "iris", "grid-bg", foot=FOOT, note="""Let the quote land. Then click once.

Our sequencers, freezers, biosafety cabinets and LIMS are all powered on and most are networked. So the question is never how to be perfectly secure. It is how to manage the risk in a way everyone in the building understands."""))

S.append(section("oxford", """<canvas class="fx" data-fx="net"></canvas>
<p class="label" data-in="fade">February 2021 · University of Oxford · Division of Structural Biology</p>
<h2 class="h2" data-k="words" style="max-width:1500px">Intruders reached the controls of equipment that purifies and prepares biochemical samples.</h2>
<div class="g3" style="margin-top:12px">
  <div class="card" data-in="up" data-d="900"><p class="k">EXPOSED</p><p class="h3">Pumps and pressure controls</p><p class="body muted">Screenshots shared with Forbes showed live access to the instrument interfaces.</p></div>
  <div class="card" data-in="up" data-d="1050"><p class="k">CONTEXT</p><p class="h3">A lab working on COVID-19 research</p><p class="body muted">Timestamps suggested access as recently as 14 February.</p></div>
  <div class="card" data-in="up" data-d="1200"><p class="k">RESPONSE</p><p class="h3">Contained and reported</p><p class="body muted">The university notified the NCSC; it said clinical research and patient data were not affected.</p></div>
</div>
<div class="spacer"></div>
<p class="src" data-in="fade" data-d="1400">ESET WeLiveSecurity, 26 Feb 2021, reporting Forbes and Hold Security</p>""", "dark", "zoom", "grid-bg", foot=FOOT, note="""A real case, close to home for everyone in this room. In February 2021 Oxford confirmed that attackers had accessed systems in its Structural Biology division, including the controls of machines that prepare biochemical samples.

The point is not that the attackers were sophisticated; reports suggest they were not. The point is that laboratory equipment is now reachable from the internet, and nobody had treated it as an IT asset."""))

S.append(section("why", """<p class="label">Why a framework</p>
<h2 class="h2" data-k="words">The biosafety officer, the IT team and the rector need one shared vocabulary.</h2>
<div class="g3" style="margin-top:20px">
  <div class="card" data-in="up" data-d="500"><p class="k">01 · OUTCOMES</p><p class="h3">What to achieve, not how</p><p class="body muted">The Core lists outcomes. Your lab chooses the controls that reach them.</p></div>
  <div class="card" data-in="up" data-d="650"><p class="k">02 · ANY ORGANIZATION</p><p class="h3">Not only critical infrastructure</p><p class="body muted">Version 2.0 is written for organizations of every size and sector, a university core facility included.</p></div>
  <div class="card" data-in="up" data-d="800"><p class="k">03 · VOLUNTARY</p><p class="h3">A map, not a regulation</p><p class="body muted">It sits beside legal duties such as Türkiye's Law 7545 and KVKK, and helps you organise how you meet them.</p></div>
</div>""", "light", "wipe", foot=FOOT, note="""Three things to remember about the CSF before we open it.

It describes outcomes rather than prescribing products. Since 2.0 it is explicitly for any organization, not just power plants and banks. And it is voluntary: it does not replace national law, but it is an excellent way to organise compliance work."""))

S.append(section("timeline", """<p class="label">A decade of the framework</p>
<div class="spacer"></div>
<div style="position:relative;height:420px">
  <div class="rule" style="position:absolute;top:96px;left:0" data-in="grow"></div>
  <div class="g3" style="position:absolute;inset:0">
    <div class="col" data-in="up" data-d="300"><p class="num" style="font-size:96px" data-m="y14">2014</p><span class="chip" style="align-self:flex-start">v1.0 · 12 Feb</span><p class="body">Born from U.S. Executive Order 13636, aimed at <b>critical infrastructure</b>.</p></div>
    <div class="col" data-in="up" data-d="500"><p class="num" style="font-size:96px">2018</p><span class="chip" style="align-self:flex-start">v1.1 · 16 Apr</span><p class="body">Adds supply-chain risk, identity and self-assessment. <b>Five functions.</b></p></div>
    <div class="col" data-in="up" data-d="700"><p class="num o" style="font-size:96px" data-m="y24">2024</p><span class="chip o" style="align-self:flex-start">v2.0 · 26 Feb</span><p class="body">Written for <b>all organizations</b>. A sixth function, <b>GOVERN</b>, at the centre.</p></div>
  </div>
</div>
<div class="spacer"></div>""", "light", "morph", foot=FOOT, note="""Quick history. Version 1.0 came out in 2014 for critical infrastructure. Version 1.1 in 2018 kept the five functions and added supply-chain and identity material.

Version 2.0, published 26 February 2024, is the version we teach today. Two headline changes: the audience is now every organization, and governance became its own function."""))

S.append(section("fivesix", """<div class="row" style="flex:1;align-items:center;gap:80px">
  <div class="wheel" id="w5" data-wheel data-mode="five" data-m="wheel" style="width:640px;height:640px;flex:none"></div>
  <div class="col grow" style="gap:18px">
    <p class="label">CSF 1.1 → CSF 2.0</p>
    <div class="h1" data-k="rise">Five functions</div>
    <div class="h1 o" data-k="rise" data-d="350">became six.</div>
    <p class="lead muted" data-in="up" data-d="800">The empty centre of the old wheel now holds the function that steers the other five.</p>
  </div>
</div>""", "dark", "zoom", "grid-bg", foot=FOOT, note="""This is the old wheel: Identify, Protect, Detect, Respond, Recover. Notice the hole in the middle.

In 2.0 that hole is filled. Next slide."""))

DEFS = [
    ("GV", "GOVERN", "The organization’s cybersecurity risk management strategy, expectations, and policy are established, communicated, and monitored."),
    ("ID", "IDENTIFY", "The organization’s current cybersecurity risks are understood."),
    ("PR", "PROTECT", "Safeguards to manage the organization’s cybersecurity risks are used."),
    ("DE", "DETECT", "Possible cybersecurity attacks and compromises are found and analyzed."),
    ("RS", "RESPOND", "Actions regarding a detected cybersecurity incident are taken."),
    ("RC", "RECOVER", "Assets and operations affected by a cybersecurity incident are restored."),
]
defs = "".join(f"""<div class="col abs" data-only="{i+1}" style="inset:0;gap:20px;justify-content:center;opacity:0;transition:opacity .45s" ><span class="chip {'o' if c=='GV' else 'b'}" style="align-self:flex-start">{c}</span><div class="h1" style="font-size:104px">{n}</div><p class="lead">{d}</p></div>""" for i, (c, n, d) in enumerate(DEFS))
S.append(section("wheel", f"""<style>#wheel [data-only].on{{opacity:1 !important}}</style>
<span data-step="1" hidden></span><span data-step="2" hidden></span><span data-step="3" hidden></span><span data-step="4" hidden></span><span data-step="5" hidden></span><span data-step="6" hidden></span><span data-step="7" hidden></span>
<div class="row" style="flex:1;align-items:center;gap:90px">
  <div class="wheel" id="w6" data-wheel data-m="wheel" data-active="GV" data-steps="GV,ID,PR,DE,RS,RC,ALL" style="width:760px;height:760px;flex:none"></div>
  <div class="grow" style="position:relative;height:640px">
    <div class="col abs" data-only="0" style="inset:0;gap:18px;justify-content:center;opacity:0;transition:opacity .45s"><p class="label">NIST CSF 2.0 · the Core</p><div class="h1">Six functions</div><p class="lead muted">GOVERN informs how the other five are carried out. Press → to walk the wheel.</p></div>
    {defs}
    <div class="col abs" data-only="7" style="inset:0;gap:18px;justify-content:center;opacity:0;transition:opacity .45s"><p class="label">Read them together</p><div class="h1" style="font-size:104px">Concurrent, not sequential</div><p class="lead muted">All six run at once. Each slide that follows zooms into one segment.</p></div>
  </div>
</div>""", "dark", "morph", "grid-bg", attrs='data-hook="wheelzero"', foot=FOOT, note="""The wheel morphs: GOVERN appears in the centre. Each click lights one function and shows NIST's own one-line definition. Read the definitions aloud; they are short on purpose.

After RECOVER, one more click lights the whole wheel: the functions act at the same time, not as a checklist in order."""))

FUNCS = [
    ("GV", "GOVERN", "The core", "Strategy, expectations and policy are established, communicated and monitored.",
     [("GV.OC", "Organizational Context"), ("GV.RM", "Risk Management Strategy"), ("GV.RR", "Roles, Responsibilities, and Authorities"), ("GV.PO", "Policy"), ("GV.OV", "Oversight"), ("GV.SC", "Cybersecurity Supply Chain Risk Management")],
     "Who owns the risk of a networked −80 °C freezer: the lab head, the biosafety officer, or IT? GOVERN makes someone answer, in writing.",
     "GV.SC", """GOVERN is new in 2.0, and it is where cyberbiosecurity starts. Six categories. Spend a moment on GV.RR: roles and authorities. In most labs nobody has formally been given the cyber risk of laboratory equipment.

Highlight GV.SC, supply-chain risk: instrument vendors with remote access, cloud LIMS providers, and for core facilities the external clients whose samples and data you hold."""),
    ("ID", "IDENTIFY", "Function 2", "Current cybersecurity risks are understood.",
     [("ID.AM", "Asset Management"), ("ID.RA", "Risk Assessment"), ("ID.IM", "Improvement")],
     "The sequencer PC on an unsupported operating system, the Wi-Fi freezer alarm, the shared analysis server: if it is not on the inventory, it is not protected.",
     "ID.AM", """IDENTIFY is about knowing what you have and what could go wrong. Asset management is the foundation of everything else.

Link forward: at 15:30 today Prof. Merey runs the laboratory asset-mapping exercise. That exercise is ID.AM in practice."""),
    ("PR", "PROTECT", "Function 3", "Safeguards to manage cybersecurity risks are used.",
     [("PR.AA", "Identity Management, Authentication, and Access Control"), ("PR.AT", "Awareness and Training"), ("PR.DS", "Data Security"), ("PR.PS", "Platform Security"), ("PR.IR", "Technology Infrastructure Resilience")],
     "Named accounts on instrument PCs, MFA on every remote session, a separate network for lab equipment, and staff who can recognise a fake “vendor engineer” call.",
     "PR.AT", """Five categories. In laboratories the weak points are usually PR.AA, shared logins on instrument PCs, and PR.AT, people.

Most intrusions still begin with a person being persuaded to do something. Awareness training is a Protect outcome, not an optional extra."""),
    ("DE", "DETECT", "Function 4", "Possible attacks and compromises are found and analyzed.",
     [("DE.CM", "Continuous Monitoring"), ("DE.AE", "Adverse Event Analysis")],
     "In the Irish health service attack of 2021, antivirus detected the intruder on 31 March, but it was set to monitor mode. Detection without analysis and action is only a log entry.",
     "DE.AE", """Two categories. Monitoring collects signals; adverse event analysis decides what they mean.

The HSE case is the reminder: the signal was there seven weeks before the ransomware went off. We will open that case fully tomorrow at 11:30."""),
    ("RS", "RESPOND", "Function 5", "Actions regarding a detected incident are taken.",
     [("RS.MA", "Incident Management"), ("RS.AN", "Incident Analysis"), ("RS.CO", "Incident Response Reporting and Communication"), ("RS.MI", "Incident Mitigation")],
     "Contain without causing a biosafety incident: isolate the instrument network, not the freezer’s power. The biosafety officer belongs at the response table.",
     "RS.MI", """Four categories. The laboratory twist is in mitigation: the fastest containment move can destroy samples or break containment.

So response plans in a lab must be written jointly by IT and biosafety. RS.CO also covers reporting: in Türkiye, Law 7545 requires reporting to the Cyber Security Presidency without delay."""),
    ("RC", "RECOVER", "Function 6", "Affected assets and operations are restored.",
     [("RC.RP", "Incident Recovery Plan Execution"), ("RC.CO", "Incident Recovery Communication")],
     "After the June 2024 ransomware attack on Synnovis, a pathology provider in London, 10,146 outpatient appointments and 1,705 elective procedures were postponed.",
     "RC.RP", """Two categories. Recovery is not only restoring servers; it is restoring the service the lab provides.

Synnovis is a supply-chain story too: one pathology contractor, two major hospital trusts disrupted for months. Figures are NHS England's cumulative numbers to mid-September 2024."""),
]
for i, (c, n, eyebrow, d, cats, lens, hot, note) in enumerate(FUNCS):
    cols = "g3" if len(cats) in (3, 6, 5) else "g2"
    if len(cats) == 4: cols = "g2"
    cards = "".join(f"""<div class="card{' hot' if code == hot else ''}" data-in="up" data-d="{450 + j * 80}" style="padding:30px 30px;flex-direction:row;align-items:center;gap:20px"><span class="chip{' o' if code == hot else ''}">{code}</span><p class="body" style="font-size:31px;line-height:1.25">{nm}</p></div>""" for j, (code, nm) in enumerate(cats))
    prev = "GV" if i == 0 else FUNCS[i - 1][0]
    zoom_sel = f"[data-seg={c}]"
    S.append(section(f"f-{c}", f"""<div class="wheel abs" id="mw-{c}" data-wheel data-active="{c}" style="right:112px;top:84px;width:280px;height:280px"></div>
<div class="col" style="gap:12px;max-width:1240px">
  <p class="label">{eyebrow} · {c}</p>
  <div class="h1" data-k="stretch">{n}</div>
  <p class="lead">{d}</p>
</div>
<div class="{cols}" style="gap:16px">{cards}</div>
<div class="spacer"></div>
<div class="card solid" data-in="up" data-d="900" style="flex-direction:row;align-items:center;gap:30px;padding:28px 34px"><p class="label" style="color:inherit;flex:none;opacity:.8">In the lab</p><p class="body" style="font-size:30px">{lens}</p></div>""",
        "light", "zoom", attrs=f'data-zoom="{zoom_sel}"', foot=FOOT, note=note))

S.append(section("anatomy", """<p class="label">How the Core is built</p>
<div class="row" style="flex:1;align-items:center;gap:40px">
  <div class="col grow" style="align-items:center;gap:10px" data-in="up"><div class="num" style="font-size:300px" data-k="count" data-to="6">6</div><p class="h3">Functions</p></div>
  <div class="h1 muted" data-in="fade" data-d="400">›</div>
  <div class="col grow" style="align-items:center;gap:10px" data-in="up" data-d="300"><div class="num b" style="font-size:300px" data-k="count" data-to="22" data-d="300">22</div><p class="h3">Categories</p></div>
  <div class="h1 muted" data-in="fade" data-d="700">›</div>
  <div class="col grow" style="align-items:center;gap:10px" data-in="up" data-d="600"><div class="num o" style="font-size:260px" data-k="count" data-to="106" data-d="600">106</div><p class="h3">Subcategories</p></div>
</div>
<p class="lead muted" data-in="up" data-d="1300" style="text-align:center;max-width:none">Each subcategory links to <b style="color:var(--steel)">Implementation Examples</b> and <b style="color:var(--steel)">Informative References</b> published online.</p>""", "dark", "zoom", "grid-bg", foot=FOOT, note="""Zoom out from the functions to the structure. Six functions, twenty-two categories, one hundred and six subcategories.

In 2.0 the examples and the mappings to other standards such as ISO 27001 moved online, so they can be updated without a new framework version. Next slide: one thread from function down to an actual task."""))

S.append(section("drill", """<p class="label">One thread through the Core</p>
<div class="row" style="gap:18px;align-items:center;flex-wrap:wrap">
  <span class="chip b" style="font-size:30px;padding:10px 18px" data-in="left">IDENTIFY</span><span class="h3 muted">›</span>
  <span class="chip" style="font-size:30px;padding:10px 18px" data-step="1" data-in="left">ID.AM · Asset Management</span><span class="h3 muted" data-step="1">›</span>
  <span class="chip o" style="font-size:30px;padding:10px 18px" data-step="2" data-in="left">ID.AM-01</span>
</div>
<div class="col" data-step="2" style="gap:10px"><p class="label muted" style="color:var(--mute-l)">Subcategory</p><p class="h2" style="font-size:64px">Inventories of hardware managed by the organization are maintained.</p></div>
<div class="g2" style="gap:28px">
  <div class="card" data-step="3"><p class="k">NIST IMPLEMENTATION EXAMPLE</p><p class="body">Maintain inventories for all types of hardware, including IT, IoT, OT, and mobile devices.</p></div>
  <div class="card hot" data-step="4"><p class="k">IN A BIOTECH LAB THIS MEANS</p><ul class="clean"><li>Instrument control PCs and their OS versions</li><li>Freezer, incubator and cabinet controllers on the network</li><li>Data loggers, tablets, USB sticks used for transfer</li></ul></div>
</div>""", "light", "morph", foot=FOOT, note="""Build this slide one click at a time. Function, category, subcategory: ID.AM-01. Then NIST's own implementation example, then what it means on our bench.

This one line, an up-to-date hardware inventory that includes OT and IoT, is where most laboratories fail first. It is also the first step of the exercise this afternoon."""))

TIERS = [
    ("1", "Partial", "Risk is managed ad hoc; limited awareness across the organization."),
    ("2", "Risk Informed", "Management approves practices, but they are not yet organization-wide policy."),
    ("3", "Repeatable", "Practices are formally approved, expressed as policy and regularly updated."),
    ("4", "Adaptive", "Practices adapt from lessons learned and predictive indicators."),
]
tiers = "".join(f"""<div class="card{' hot' if n=='3' else ''}" data-in="up" data-d="{300 + int(n)*150}" style="justify-content:flex-end;height:{200 + int(n)*55}px;padding:26px 28px"><p class="num {'o' if n=='3' else 'b'}" style="font-size:120px">{n}</p><p class="h3">{t}</p><p class="body muted" style="font-size:26px">{d}</p></div>""" for n, t, d in TIERS)
S.append(section("tiers", f"""<p class="label">Tiers</p>
<h2 class="h2" data-k="words">How rigorous are our governance and management practices?</h2>
<div class="g4" style="align-items:end;flex:1">{tiers}</div>
<p class="body muted" data-in="fade" data-d="1100">Tiers are not a score to maximise. Choose the tier your risk justifies; a teaching lab and a BSL-3 core facility need different targets.</p>""", "light", "rise", foot=FOOT, note="""Tiers describe the rigour of your practices, from ad hoc to adaptive. They apply to governance and to management of risk.

Stress the last line: higher is not automatically better. Tier 3 is a sensible target for many research facilities; Tier 4 costs real money and staff."""))

S.append(section("profiles", """<div class="spacer"></div>
<div class="row" style="align-items:center;gap:56px">
  <div class="col" style="gap:10px;flex:1" data-in="left"><p class="label">Where we are</p><div class="h1 b" data-k="rise">Current Profile</div></div>
  <div class="h1 o" data-k="slam" data-d="500">→</div>
  <div class="col" style="gap:10px;flex:1" data-in="right" data-d="300"><p class="label">Where we must be</p><div class="h1 o" data-k="rise" data-d="300">Target Profile</div></div>
</div>
<div class="g3" style="margin-top:56px">
  <div class="card" data-step="1"><p class="k">THE GAP</p><p class="body">The difference between the two profiles, outcome by outcome.</p></div>
  <div class="card" data-step="2"><p class="k">THE ACTION PLAN</p><p class="body">Prioritised work to close the gap, with owners, budget and dates.</p></div>
  <div class="card solid" data-step="3"><p class="k" style="color:inherit">THE CYCLE</p><p class="body">Implement, then update the Current Profile. Repeat.</p></div>
</div>
<div class="spacer"></div>""", "dark", "iris", "grid-bg", foot=FOOT, note="""A Profile is the CSF applied to you. The Current Profile says which outcomes you achieve today; the Target Profile says which you need, given your risks and obligations.

Click three times: the gap, the action plan, the cycle. This is exactly what each group will build tomorrow at 14:30."""))

S.append(section("radar", """<div class="row" style="flex:1;gap:56px;align-items:stretch">
  <div class="col" style="gap:14px;width:720px;flex:none">
    <p class="label">Worked example · illustrative values</p>
    <h2 class="h2" style="font-size:64px">A university core facility serving industry clients</h2>
    <p class="body muted">Tiers 1–4 per function. Blue: today. Orange, dashed: the target the facility’s board agreed.</p>
    <div class="col" style="gap:14px;margin-top:10px">
      <div class="card sev hi" data-step="2" style="padding:20px 26px"><p class="body"><b>GV.SC</b> · client samples and data arrive from outside; vendors log in remotely</p></div>
      <div class="card sev hi" data-step="2" style="padding:20px 26px"><p class="body"><b>DE.CM</b> · no central logging from instrument PCs</p></div>
      <div class="card sev md" data-step="2" style="padding:20px 26px"><p class="body"><b>RC.RP</b> · backups exist; a restore has never been tested</p></div>
    </div>
  </div>
  <div class="grow" style="display:grid;place-items:center"><div data-radar data-axes="GV,ID,PR,DE,RS,RC" data-a="1,2,2,1,1,1" data-b="3,3,3,3,3,2" data-b-at="1" style="width:820px;height:800px"></div></div>
</div>""", "light", "morph", foot=FOOT, note="""An illustrative profile; the numbers are an example, not data from a real facility. Blue is today. Click once: the orange target appears. Click again: the three biggest gaps.

For a facility that receives clients' samples and data, supply-chain governance, GV.SC, is usually the largest gap and the most specific to our sector."""))

S.append(section("community", """<p class="label">Two kinds of profile</p>
<div class="g2" style="flex:1;gap:36px">
  <div class="card" data-in="up" style="gap:20px"><p class="k">ORGANIZATIONAL PROFILE</p><p class="h2" style="font-size:60px">Yours</p><p class="body">Current and Target for one organization or one facility. NIST publishes a Quick-Start Guide and a fillable template.</p></div>
  <div class="card" data-in="up" data-d="200" style="gap:20px"><p class="k">COMMUNITY PROFILE</p><p class="h2" style="font-size:60px">Shared by a sector or a topic</p>
    <ul class="clean"><li><b>SP 800-61 Rev. 3</b> (April 2025): incident response, organised by CSF 2.0 functions</li><li><b>Cyber AI Profile</b>, NIST IR 8596 (preliminary draft, Dec 2025): Secure, Defend, Thwart</li></ul>
    <span class="chip o" style="align-self:flex-start">→ Tomorrow 09:15 · AI RMF</span></div>
</div>""", "light", "push", foot=FOOT, note="""Organizational Profiles are what you build for your own unit. Community Profiles are written for a whole sector or topic and you can start from them.

Two that matter for this workshop: the new incident response guidance, SP 800-61 Revision 3, which is itself a CSF 2.0 community profile, and the preliminary Cyber AI Profile. That one leads into tomorrow morning's session on the AI Risk Management Framework."""))

STEPS5 = [("Scope", "Which unit, which systems, which risks?"), ("Gather", "Policies, inventories, risk registers, legal duties"), ("Create", "Rate Current and Target, outcome by outcome"), ("Analyze", "Gaps → a prioritised action plan"), ("Implement", "Act, then update the profile")]
st5 = "".join(f"""<div class="col" data-in="up" data-d="{300 + i*160}" style="gap:14px"><p class="num {'o' if i==3 else 'b'}" style="font-size:150px">{i+1}</p><div class="rule"></div><p class="h3">{a}</p><p class="body muted">{b}</p></div>""" for i, (a, b) in enumerate(STEPS5))
S.append(section("fivesteps", f"""<p class="label">NIST Quick-Start Guide · Organizational Profiles</p>
<h2 class="h2" data-k="words">Five steps from framework to action plan</h2>
<div class="g5" style="flex:1;align-items:center;gap:36px">{st5}</div>""", "light", "rise", foot=FOOT, note="""NIST's quick-start guide gives five steps: scope, gather, create, analyze gaps and plan, implement and update.

Tomorrow's exercise compresses steps one to four into forty-five minutes for a fictional biotech lab."""))

S.append(section("turkiye", """<canvas class="fx" data-fx="rings"></canvas>
<p class="label">In Türkiye</p>
<h2 class="h2" data-k="words" style="max-width:1150px">The framework is voluntary. These duties are not.</h2>
<div class="col" style="gap:22px;max-width:1120px;margin-top:10px">
  <div class="card" data-in="left" data-d="500"><p class="k">LAW NO. 7545 · CYBERSECURITY LAW · RG 19 MARCH 2025</p><p class="body">Covered entities report detected vulnerabilities and cyber incidents to the Cyber Security Presidency <b>without delay</b>, and share information it requests.</p><span class="chip b" style="align-self:flex-start">maps to RS.CO · GV.OC</span></div>
  <div class="card" data-in="left" data-d="700"><p class="k">LAW NO. 6698 · KVKK · PERSONAL DATA</p><p class="body">Personal data breaches are notified to the KVKK Board, within <b>72 hours</b> under Board Decision 2019/10.</p><span class="chip b" style="align-self:flex-start">maps to RS.CO · PR.DS</span></div>
</div>""", "dark", "wipe", "grid-bg", foot=FOOT, note="""Bring it home. Law 7545, published in the Official Gazette on 19 March 2025, created reporting duties to the Cyber Security Presidency. KVKK sets 72 hours for notifying personal data breaches.

The CSF does not replace these laws, but outcomes such as GV.OC, legal requirements are understood, and RS.CO, reporting, are where you show you meet them. Advise participants to confirm with their institution's legal office which duties apply to them."""))

S.append(section("takeaways", """<canvas class="fx" data-fx="helix" data-x="1560"></canvas>
<p class="label">Three things to keep</p>
<div class="col" style="gap:8px;margin-top:10px">
  <div class="mega" style="font-size:150px" data-step="1" data-k="stretch">Govern first.</div>
  <div class="mega b" style="font-size:150px" data-step="2" data-k="stretch">Know what you run.</div>
  <div class="mega o" style="font-size:150px" data-step="3" data-k="stretch">Profile, then act.</div>
</div>
<div class="spacer"></div>
<div class="row" style="gap:28px" data-step="4">
  <span class="chip">Today 15:30 · Laboratory asset mapping · Prof. Dr. Gökçe Merey</span>
  <span class="chip o">Tomorrow 14:30 · Build your lab's profile</span>
</div>""", "dark", "zoom", "grid-bg", foot=FOOT, note="""Three lines, one per click. Govern first: someone must own the risk. Know what you run: inventory, including OT. Profile, then act: compare where you are with where you must be.

Final click shows where these ideas continue in the programme."""))

S.append(sources("refs", [
    "National Institute of Standards and Technology. <i>The NIST Cybersecurity Framework (CSF) 2.0</i>. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
    "Nelson A, Rekhi S, Souppaya M, Scarfone K. <i>Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile</i>. NIST SP 800-61r3; 2025. doi:10.6028/NIST.SP.800-61r3",
    "NIST. <i>Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile)</i>. NIST IR 8596, initial preliminary draft; 16 Dec 2025.",
    "Murch RS, So WK, Buchholz WG, Raman S, Peccoud J. Cyberbiosecurity: an emerging new discipline to help safeguard the bioeconomy. <i>Front Bioeng Biotechnol</i>. 2018;6:39. doi:10.3389/fbioe.2018.00039",
    "Peccoud J, Gallegos JE, Murch R, Buchholz WG, Raman S. Cyberbiosecurity: from naive trust to risk awareness. <i>Trends Biotechnol</i>. 2018;36(1):4–7. doi:10.1016/j.tibtech.2017.10.012",
    "NHS England (London). Update on cyber incident clinical impact in south east London; 19 Sep 2024.",
    "ESET WeLiveSecurity. Oxford University lab studying COVID-19 hit by cyberattack; 26 Feb 2021.",
    "7545 sayılı Siber Güvenlik Kanunu. Resmî Gazete 32846; 19 Mar 2025. · 6698 sayılı Kişisel Verilerin Korunması Kanunu; KVK Kurulu Kararı 2019/10.",
], FOOT))

S.append(thanks("thanks", "Thank you.", "Questions on the framework, the functions or profiles", "Open the floor. If time is short, take one or two questions and point people to the afternoon exercise.", FOOT))

HOOKS = """window.DeckHooks = { wheelzero(s, step) { s.querySelectorAll('[data-only]').forEach(e => e.classList.toggle('on', String(e.dataset.only) === String(step))); } };"""

if __name__ == "__main__":
    n = build("/home/claude/corum/dist/d1/index.html", "CSF 2.0 Core Functions", 60, FOOT, S, extra_js=HOOKS)
    print("slides", n)
