from lib import *

FOOT = "Institutional Cybersecurity Infrastructure · Case Study"
S = []

CSS = """
.zones text { font-family: var(--sans); }
.zones .zt { font-family: var(--display); font-weight: 800; font-size: 30px; }
.zones .zs { font-size: 22px; }
.ring-lab { font-family: var(--mono); font-size: 24px; letter-spacing: .08em; }
.sevrow { display:grid; grid-template-columns: 120px 1fr 200px; gap: 24px; align-items:center; padding: 16px 0; }
.light .sevrow { border-bottom: 1.5px solid var(--rule); }
.raci td, .raci th { text-align:center; }
.raci td:first-child, .raci th:first-child { text-align:left; }
.raci .R { color:#fff; background: var(--blue-t); border-radius:8px; padding:4px 12px; font-family: var(--mono); font-weight:500; }
.raci .A { color: var(--ink); background: var(--orange); border-radius:8px; padding:4px 12px; font-family: var(--mono); font-weight:500; }
.raci .C, .raci .I { font-family: var(--mono); color: var(--mute-l); }
.tile { display:flex; flex-direction:column; gap:10px; }
"""

S.append(lobby("lobby", "Day 2 · Tuesday 3 November", "11:30 – 12:30",
    ["Institutional", "Cybersecurity Infrastructure"], "A practical case study",
    """Holding screen. Press → to play the opening film; it advances to the title slide by itself."""))

S.append(video("open", "media/opener.mp4", "media/opener.jpg",
    """Opening film, about 15 seconds: the timeline of the 2021 Irish health service ransomware attack, from the first email to detonation eight weeks later."""))

S.append(section("title", f"""<canvas class="fx" data-fx="rings"></canvas>
<p class="label" data-in="fade">Session 3 · A practical case study</p>
<div class="col" style="gap:0">
  <div class="mega" data-k="rise" style="font-size:150px">INSTITUTIONAL</div>
  <div class="mega" data-k="rise" data-d="150" style="font-size:150px">CYBERSECURITY</div>
  <div class="mega b" data-k="rise" data-d="300" style="font-size:150px">INFRASTRUCTURE</div>
</div>
<div class="spacer"></div>
<div class="col" data-in="fade" data-d="900" style="gap:4px"><p class="h3">{SPEAKER}</p><p class="small muted">{AFFIL}</p></div>""",
    "dark", "fade", "grid-bg", foot=EVENT, note="""This session is practical. We take one large real incident to see how infrastructure fails, then walk through a composite case: a university central research laboratory that serves external industry clients, assessed and rebuilt in two phases.

Everything maps back to the CSF functions from yesterday, so this afternoon's exercise will feel familiar."""))

EV = [("16 Mar 2021", "Malicious email reaches a workstation", "b"), ("18 Mar", "Opened; an Excel file downloads; foothold gained", "b"),
      ("31 Mar", "Antivirus detects activity, but it is in monitor mode", "o"), ("7–13 May", "Provider reports unhandled threats on 16+ systems", "o"),
      ("14 May, 04:00", "Conti ransomware detonates; IT taken offline nationally", "o")]
evs = "".join(f"""<div class="col" data-step="{i+1}" style="gap:12px"><div style="width:26px;height:26px;border-radius:13px;background:var(--{'orange' if c=='o' else 'blue'})"></div><p class="label {'o' if c=='o' else 'b'}" style="color:var(--{'orange-t' if c=='o' else 'blue-t'})">{d}</p><p class="body" style="font-size:28px">{t}</p></div>""" for i, (d, t, c) in enumerate(EV))
S.append(section("hse", f"""<p class="label">Health Service Executive, Ireland · 2021</p>
<h2 class="h2" data-k="words">Eight weeks between the first email and the ransomware</h2>
<div style="position:relative;margin-top:30px">
  <div class="rule" style="position:absolute;top:12px;left:0;height:3px" data-in="grow"></div>
  <div class="g5" style="gap:30px;position:relative">{evs}</div>
</div>
<div class="spacer"></div>
<div class="g3" data-step="6" style="gap:24px">
  <div class="card"><p class="k">DWELL TIME</p><p class="num b" style="font-size:80px">≈ 8 wks</p></div>
  <div class="card"><p class="k">IMMEDIATE RESPONSE COST</p><p class="num b" style="font-size:80px">€53 m</p><p class="small muted">HSE figure to the Dáil Public Accounts Committee</p></div>
  <div class="card hot"><p class="k">ROOT FINDING (PwC)</p><p class="body">Fragmented legacy IT, never designed to resist attack, and no single owner of cyber risk.</p></div>
</div>""", "light", "wipe", foot=FOOT, note="""Build the timeline one click per event. The details come from the independent PwC post-incident review published in December 2021.

The orange dots are the moments the organisation could have acted: antivirus saw it on 31 March but was set to monitor only; a week before detonation the security provider reported unhandled threats on at least sixteen systems. The last click shows the cost and the root finding, which is a governance finding, not a technical one."""))

S.append(section("lesson", """<div class="spacer"></div>
<div class="mega" style="font-size:150px" data-k="rise">The signals were there.</div>
<div class="mega o" style="font-size:150px" data-k="rise" data-d="600">The structure to act on them was not.</div>
<div class="spacer"></div>
<p class="lead muted" data-in="up" data-d="1300">Infrastructure is not only hardware. It is who owns the risk, who watches, and who may decide.</p>""",
    "dark", "zoom", "grid-bg", foot=FOOT, note="""The core message of the session. Technology detected the intrusion; the organisation did not respond. That is why yesterday GOVERN was at the centre of the wheel."""))

S.append(section("layers", """<p class="label">Three layers of every institution</p>
<div class="g3" style="flex:1;gap:30px;align-content:center">
  <div class="card" data-in="up" data-d="200" style="gap:20px;padding:44px"><p class="num b" style="font-size:120px">01</p><p class="h2" style="font-size:60px">Technical</p><p class="body muted">Networks, instrument PCs, accounts, logs, backups</p></div>
  <div class="card hot" data-in="up" data-d="350" style="gap:20px;padding:44px"><p class="num o" style="font-size:120px">02</p><p class="h2" style="font-size:60px">People</p><p class="body muted">Staff, students, client technicians, vendor engineers</p></div>
  <div class="card" data-in="up" data-d="500" style="gap:20px;padding:44px"><p class="num b" style="font-size:120px">03</p><p class="h2" style="font-size:60px">Physical</p><p class="body muted">Doors, freezers, cabinets, sample stores, USB ports</p></div>
</div>
<p class="body muted" data-in="fade" data-d="800">A weakness in any one layer opens the other two.</p>""", "dark", "rise", "grid-bg", foot=FOOT, note="""The same three layers we use in social engineering training. Keep them in mind; every finding in the case belongs to one of them, and the people layer is usually the cheapest to attack."""))

S.append(section("facility", """<p class="label">The case · a composite, not one real institution</p>
<h2 class="h2" data-k="words">A university central research laboratory that also serves industry</h2>
<div class="g4" style="gap:20px;margin-top:10px">
  <div class="card" data-in="up" data-d="400"><p class="num b" style="font-size:96px">40+</p><p class="body">instruments, many with a dedicated control PC</p></div>
  <div class="card" data-in="up" data-d="500"><p class="num b" style="font-size:96px">60</p><p class="body">users: staff, students, visiting client technicians</p></div>
  <div class="card hot" data-in="up" data-d="600"><p class="num o" style="font-size:96px">12</p><p class="body">external industry clients sending samples and data</p></div>
  <div class="card" data-in="up" data-d="700"><p class="num b" style="font-size:96px">8</p><p class="body">vendors with some form of remote support access</p></div>
</div>
<div class="card solid" data-in="up" data-d="900" style="flex-direction:row;align-items:center;gap:30px;padding:28px 34px"><p class="label" style="color:inherit;flex:none;opacity:.8">Why it matters</p><p class="body">Client samples and data make this a supply-chain node: a breach here is a breach for twelve companies. In CSF terms, GV.SC is the centre of gravity.</p></div>""",
    "light", "push", foot=FOOT, note="""A composite built from typical core facilities; the numbers are illustrative. If you wish, relate it to our own work at Sivas Cumhuriyet University's central research centre, where this external-client angle shaped our project design.

The defining feature is the external clients. A university lab that only serves its own researchers has an internal risk; a facility that holds twelve companies' samples and data is part of their supply chain."""))

S.append(section("phases", """<div class="spacer"></div>
<div class="row" style="align-items:stretch;gap:0">
  <div class="card" data-in="left" style="flex:1;border-radius:14px 0 0 14px;padding:48px;gap:18px"><p class="k">PHASE 1 · WEEKS 1–4</p><p class="h1" style="font-size:110px">Assess</p><p class="lead muted">Inventory, network map, interviews, Current Profile</p></div>
  <div style="width:0;height:0;align-self:center;border-top:70px solid transparent;border-bottom:70px solid transparent;border-left:70px solid var(--ink-2)" data-in="fade" data-d="300"></div>
  <div class="card solid" data-in="right" data-d="400" style="flex:1;padding:48px;gap:18px;margin-left:24px"><p class="k" style="color:inherit">PHASE 2 · WEEKS 5–10</p><p class="h1" style="font-size:110px">Build &amp; train</p><p class="lead">Segmentation, identity, logging, backups, plans, people</p></div>
</div>
<div class="spacer"></div>
<p class="body muted" data-in="fade" data-d="900">Assessment first, then targeted investment. Buying tools before the inventory is the most common and most expensive mistake.</p>""",
    "dark", "zoom", "grid-bg", foot=FOOT, note="""Two phases. First assess, then build and train. The order matters: without an inventory and a Current Profile you cannot know which investments close which gaps."""))

RINGS = [("#2448C2", "dash", "Perimeter", "internet, email, vendors, cloud LIMS"), ("#2448C2", "", "Endpoints & accounts", "PCs, laptops, shared logins"), ("#C23F0B", "", "Lab devices & OT", "instrument PCs, freezer and room monitors")]
RADII = [440, 330, 220]
ring_svg = "".join(f'<circle data-step="{i+1}" cx="460" cy="460" r="{RADII[i]}" fill="none" stroke="{c}" stroke-width="4" stroke-dasharray="{"12 12" if d else "0"}"/>' for i, (c, d, _, _) in enumerate(RINGS))
legend = "".join(f'<div class="row" data-step="{i+1}" style="gap:18px;align-items:center"><span style="width:34px;height:34px;border-radius:17px;border:4px {"dashed" if d else "solid"} {c};flex:none"></span><div class="col" style="gap:2px"><p class="h3" style="font-size:34px">{t}</p><p class="body muted" style="font-size:26px">{x}</p></div></div>' for i, (c, d, t, x) in enumerate(RINGS))
S.append(section("jewels", f"""<div class="row" style="flex:1;gap:70px;align-items:center">
  <svg viewBox="0 0 920 920" style="width:800px;height:800px;flex:none" role="img" aria-label="Attack surface rings around crown jewels">
    {ring_svg}
    <g data-step="4"><circle cx="460" cy="460" r="125" fill="#FF5B1F"/><text x="460" y="450" text-anchor="middle" font-family="Archivo, sans-serif" font-weight="850" font-size="36" fill="#0A1424">CROWN</text><text x="460" y="490" text-anchor="middle" font-family="Archivo, sans-serif" font-weight="850" font-size="36" fill="#0A1424">JEWELS</text></g>
  </svg>
  <div class="col grow" style="gap:22px">
    <p class="label">Phase 1 · ID.AM, ID.RA</p>
    <h2 class="h2" data-k="words" style="font-size:64px">Start from what must never be lost</h2>
    {legend}
    <ul class="clean" data-step="4" style="margin-top:6px"><li>Client samples, results and contracts</li><li>Instrument control and calibration data</li><li>The cold chain: −80 °C storage and its alarms</li><li>Unpublished research data and IP</li></ul>
  </div>
</div>""", "light", "zoom", attrs='data-zoom=".card"', foot=FOOT, note="""Build from the outside in: perimeter, endpoints and accounts, laboratory devices, and finally the crown jewels. Ask the room what their own crown jewels are before revealing the list.

The cold chain is the item people forget: a freezer alarm on Wi-Fi is a cyber asset with a biosafety consequence."""))

FIND = [("High", "Instrument PCs on unsupported Windows versions, cannot be patched", "PR.PS"),
        ("High", "One flat network: office PCs, Wi-Fi and instruments share a segment", "PR.IR"),
        ("High", "Shared logins on instrument PCs; client technicians use staff accounts", "PR.AA"),
        ("High", "Vendor remote-support tools installed and always on", "GV.SC"),
        ("Med", "Results moved by USB stick between instruments and analysis PCs", "PR.DS"),
        ("Med", "No central logging; instrument PC clocks drift by minutes", "DE.CM"),
        ("High", "Backups exist; nobody has ever tested a restore", "RC.RP"),
        ("Med", "No incident plan names the biosafety officer", "RS.MA")]
rows = "".join(f"""<div class="sevrow" data-in="up" data-d="{300+i*90}"><span class="chip {'o' if s=='High' else 'b'}" style="justify-content:center">{s}</span><p class="body" style="font-size:29px">{t}</p><span class="chip" style="justify-self:end">{c}</span></div>""" for i, (s, t, c) in enumerate(FIND))
S.append(section("findings", f"""<p class="label">Phase 1 output · typical findings in a core facility</p>
<div class="col" style="gap:0">{rows}</div>""", "light", "rise", foot=FOOT, note="""Eight findings that appear in almost every assessment of a shared research facility. These are illustrative, not from one audit. Note how each one maps to a CSF subcategory family; that mapping is what turns a list of complaints into a Current Profile.

Ask: how many of these would be true in your own building?"""))

S.append(section("schneier", """<canvas class="fx" data-fx="net"></canvas>
<div class="spacer"></div>
<p class="label">The people layer</p>
<p class="quote" style="font-size:120px" data-k="words">“Amateurs hack systems, professionals hack people.”</p>
<p class="cite muted" data-in="fade" data-d="1200">Bruce Schneier · security technologist</p>
<div class="spacer"></div>""", "dark", "iris", "grid-bg", foot=FOOT, note="""A line I use in every training. Technical controls raise the cost of attacking systems, so attackers go around them, through people."""))

PH = [("Research", "Staff names on the website, vendor names in public tender documents, instrument models in published papers"),
      ("Develop", "A friendly call from the “sequencer vendor’s service engineer” who knows the model and the lab head’s name"),
      ("Exploit", "“Please install this remote-support tool before Monday’s firmware update.”")]
S.append(section("se", f"""<p class="label">Social engineering, applied to the case</p>
<h2 class="h2" data-k="words">Three phases, all in plain sight</h2>
<div class="g3" style="gap:26px;margin-top:10px">{''.join(f'<div class="card{" hot" if i==2 else ""}" data-step="{i+1}" style="gap:16px;padding:38px"><p class="num {"o" if i==2 else "b"}" style="font-size:96px">{i+1}</p><p class="h2" style="font-size:56px">{a}</p><p class="body">{b}</p></div>' for i,(a,b) in enumerate(PH))}</div>
<div class="card solid" data-step="4" style="flex-direction:row;align-items:center;gap:30px;padding:26px 34px"><p class="label" style="color:inherit;flex:none;opacity:.8">Countermeasure</p><p class="body">Vendor access only through the jump host, requested by ticket, verified by a call-back to a known number.</p></div>""",
    "light", "push", foot=FOOT, note="""Research, develop, exploit: the three phases from my social engineering module, applied to our facility. Nothing in the research phase is secret; it is all public.

The countermeasure is a process, not a product: a ticket and a call-back to a number you already hold."""))

PR = [("Ego", "Flatters expertise: “You are the only one who really understands this system.”"),
      ("Sympathy", "A new colleague or vendor in trouble: “I will lose my job if this is not fixed today.”"),
      ("Intimidation", "Borrowed authority: “This is the rector’s office / the regulator. Do it now and keep it quiet.”")]
S.append(section("pressures", f"""<p class="label">Three pressures attackers use</p>
<div class="g3" style="flex:1;gap:28px;align-content:center">{''.join(f'<div class="card" data-in="up" data-d="{300+i*180}" style="gap:20px;padding:44px"><div class="h1" style="font-size:76px" data-k="stretch" data-d="{300+i*180}">{a}</div><p class="lead" style="font-size:34px">{b}</p></div>' for i,(a,b) in enumerate(PR))}</div>
<p class="body muted" data-in="fade" data-d="1000">Urgency plus secrecy is the signature. Train people to pause on both, and make reporting easy and blame-free.</p>""",
    "dark", "zoom", "grid-bg", foot=FOOT, note="""Ego, sympathy, intimidation. Every training example in my deck falls into one of these. The practical rule for staff: when a request comes with urgency and secrecy together, stop and verify through a different channel."""))

S.append(section("arch", """<p class="label">Phase 2 · target architecture · PR.IR, PR.AA, DE.CM, RC.RP</p>
<svg class="zones" viewBox="0 0 1664 700" style="width:1664px;height:700px" role="img" aria-label="Segmented network with jump host, logging and offline backup">
  <defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#55606E"/></marker></defs>
  <g data-step="1">
    <rect x="0" y="270" width="220" height="130" rx="14" fill="#E1E6EA"/><text class="zt" x="110" y="330" text-anchor="middle" fill="#0F1B2D">Internet</text><text class="zs" x="110" y="364" text-anchor="middle" fill="#55606E">email · clients · vendors</text>
    <rect x="290" y="270" width="190" height="130" rx="14" fill="#0F1B2D"/><text class="zt" x="385" y="342" text-anchor="middle" fill="#E8ECEF">Firewall</text>
    <line x1="220" y1="335" x2="286" y2="335" stroke="#55606E" stroke-width="3" marker-end="url(#ah)"/>
    <rect x="570" y="30" width="520" height="170" rx="14" fill="#FAFBFC" stroke="#B9C3CC" stroke-width="2"/><text class="zt" x="600" y="90" fill="#0F1B2D">Campus IT zone</text><text class="zs" x="600" y="130" fill="#55606E">email, office PCs, Wi-Fi, student devices</text>
    <rect x="570" y="250" width="520" height="170" rx="14" fill="#FAFBFC" stroke="#2448C2" stroke-width="3"/><text class="zt" x="600" y="310" fill="#2448C2">Lab OT zone (own VLAN)</text><text class="zs" x="600" y="350" fill="#55606E">instrument PCs, freezer and room monitors</text><text class="zs" x="600" y="384" fill="#55606E">no internet by default · named accounts</text>
    <rect x="570" y="470" width="520" height="170" rx="14" fill="#FAFBFC" stroke="#B9C3CC" stroke-width="2"/><text class="zt" x="600" y="530" fill="#0F1B2D">Client data enclave</text><text class="zs" x="600" y="570" fill="#55606E">storage separated per client · access by contract</text>
    <path d="M480,320 C520,320 520,115 566,115" fill="none" stroke="#55606E" stroke-width="3" marker-end="url(#ah)"/>
    <path d="M480,350 C520,350 520,555 566,555" fill="none" stroke="#55606E" stroke-width="3" marker-end="url(#ah)"/>
  </g>
  <g data-step="2">
    <rect x="270" y="500" width="230" height="160" rx="14" fill="#FF5B1F"/><text class="zt" x="385" y="556" text-anchor="middle" fill="#0A1424">Vendor jump host</text><text class="zs" x="385" y="592" text-anchor="middle" fill="#0A1424">MFA · recorded</text><text class="zs" x="385" y="624" text-anchor="middle" fill="#0A1424">time-boxed by ticket</text>
    <path d="M110,400 C110,580 200,580 266,580" fill="none" stroke="#C23F0B" stroke-width="3" stroke-dasharray="8 8" marker-end="url(#ah)"/>
    <path d="M500,560 C540,560 540,400 566,380" fill="none" stroke="#C23F0B" stroke-width="3" marker-end="url(#ah)"/>
  </g>
  <g data-step="3">
    <rect x="1180" y="30" width="230" height="610" rx="14" fill="#0F1B2D"/><text class="zt" x="1295" y="300" text-anchor="middle" fill="#E8ECEF">Central</text><text class="zt" x="1295" y="340" text-anchor="middle" fill="#E8ECEF">logging</text><text class="zs" x="1295" y="384" text-anchor="middle" fill="#8C9AAE">NTP-synced clocks</text><text class="zs" x="1295" y="414" text-anchor="middle" fill="#8C9AAE">defined retention</text>
    <line x1="1090" y1="115" x2="1176" y2="115" stroke="#2448C2" stroke-width="3" stroke-dasharray="6 6" marker-end="url(#ah)"/>
    <line x1="1090" y1="335" x2="1176" y2="335" stroke="#2448C2" stroke-width="3" stroke-dasharray="6 6" marker-end="url(#ah)"/>
    <line x1="1090" y1="555" x2="1176" y2="555" stroke="#2448C2" stroke-width="3" stroke-dasharray="6 6" marker-end="url(#ah)"/>
  </g>
  <g data-step="4">
    <rect x="1460" y="250" width="204" height="390" rx="14" fill="#FAFBFC" stroke="#C23F0B" stroke-width="3" stroke-dasharray="12 8"/><text class="zt" x="1562" y="420" text-anchor="middle" fill="#C23F0B">Offline</text><text class="zt" x="1562" y="460" text-anchor="middle" fill="#C23F0B">backup</text><text class="zs" x="1562" y="500" text-anchor="middle" fill="#55606E">immutable copy</text><text class="zs" x="1562" y="530" text-anchor="middle" fill="#55606E">restore tested</text>
  </g>
</svg>""", "light", "morph", foot=FOOT, note="""Build the target architecture in four clicks. First the zones: campus IT, a separate lab network with no internet by default, and a client data enclave. Second, the vendor jump host: the only way in for remote support, with MFA, session recording and time limits. Third, central logging with synchronised clocks. Fourth, an offline, immutable backup whose restore has been tested.

Each element closes one of the findings two slides back."""))

S.append(section("change", """<p class="label">Identity lesson · Change Healthcare · February 2024</p>
<div class="row" style="align-items:flex-end;gap:36px">
  <div class="num" style="font-size:250px" data-k="count" data-to="192.7" data-dec="1">192.7</div>
  <p class="h2 muted" style="padding-bottom:30px" data-in="fade" data-d="1200">million people</p>
</div>
<p class="lead" data-k="words" data-d="300" style="max-width:1500px">The attackers entered through a remote-access portal that did not require multi-factor authentication.</p>
<div class="spacer"></div>
<div class="card solid" data-step="1" style="flex-direction:row;align-items:center;gap:30px;padding:28px 34px"><p class="label" style="color:inherit;flex:none;opacity:.8">Rule</p><p class="h3" style="font-size:40px">MFA on every remote path, and vendor paths first.</p></div>
<p class="src" data-in="fade" data-d="1400">Figure as reported to the U.S. HHS Office for Civil Rights, July 2025</p>""",
    "dark", "iris", "grid-bg", foot=FOOT, note="""The largest health-data breach on record in the United States: 192.7 million individuals, from one portal without MFA. Click for the rule.

This is PR.AA in practice. For our facility it means the vendor jump host and any VPN or remote desktop path."""))

S.append(section("synnovis", """<p class="label">Supply-chain lesson · Synnovis pathology · June 2024</p>
<h2 class="h2" data-k="words">One laboratory services provider. Two hospital trusts. Months of disruption.</h2>
<div class="g3" style="gap:26px;margin-top:16px">
  <div class="card" data-in="up" data-d="500"><p class="num b" style="font-size:110px" data-k="count" data-to="10146" data-d="500">10,146</p><p class="body">outpatient appointments postponed</p></div>
  <div class="card" data-in="up" data-d="650"><p class="num b" style="font-size:110px" data-k="count" data-to="1705" data-d="650">1,705</p><p class="body">elective procedures postponed</p></div>
  <div class="card hot" data-in="up" data-d="800"><p class="num o" style="font-size:110px">2025</p><p class="body">King’s College Hospital confirmed the attack was one contributing factor in a patient’s death</p></div>
</div>
<div class="spacer"></div>
<div class="card solid" data-step="1" style="flex-direction:row;align-items:center;gap:30px;padding:26px 34px"><p class="label" style="color:inherit;flex:none;opacity:.8">For a facility with clients</p><p class="body">Contracts with security and notification clauses, per-client data separation, and a plan for telling every client within hours.</p></div>""",
    "light", "wipe", foot=FOOT, note="""Synnovis provided pathology services to King's College Hospital and Guy's and St Thomas'. NHS England's cumulative figures to mid-September 2024: 10,146 outpatient appointments and 1,705 elective procedures postponed. In June 2025 King's confirmed that the attack was one contributing factor in a patient's death.

Turn it around: our facility is someone else's Synnovis. GV.SC applies in both directions."""))

S.append(section("telemetry", """<p class="label">DE.CM · you cannot fight what you cannot see</p>
<div class="row" style="flex:1;gap:60px;align-items:center">
  <div class="col" style="gap:20px;width:760px;flex:none">
    <h2 class="h2" data-k="words">Six log sources cover most of a laboratory</h2>
    <div class="g2" style="gap:14px">
      <span class="chip" style="font-size:28px;padding:12px 16px" data-in="pop" data-d="300">Firewall</span><span class="chip" style="font-size:28px;padding:12px 16px" data-in="pop" data-d="380">Identity / directory</span>
      <span class="chip" style="font-size:28px;padding:12px 16px" data-in="pop" data-d="460">Jump host sessions</span><span class="chip" style="font-size:28px;padding:12px 16px" data-in="pop" data-d="540">Instrument PC events</span>
      <span class="chip" style="font-size:28px;padding:12px 16px" data-in="pop" data-d="620">LIMS audit trail</span><span class="chip o" style="font-size:28px;padding:12px 16px" data-in="pop" data-d="700">Freezer &amp; room alarms</span>
    </div>
  </div>
  <div class="col grow" style="gap:18px">
    <div class="card sev md" data-step="1"><p class="h3">Synchronise every clock</p><p class="body muted">Without NTP, a timeline across instruments cannot be rebuilt.</p></div>
    <div class="card sev md" data-step="2"><p class="h3">Collect centrally</p><p class="body muted">Logs on the compromised machine are the first thing an attacker deletes.</p></div>
    <div class="card sev hi" data-step="3"><p class="h3">Decide retention in advance</p><p class="body muted">The HSE intruder was inside for eight weeks. Keep at least that much.</p></div>
  </div>
</div>""", "light", "push", foot=FOOT, note="""Six log sources, three rules. The freezer alarm is in orange on purpose: it is both a security signal and a biosafety signal.

The retention point links back to the opening case: if you keep two weeks of logs, an eight-week intrusion is invisible."""))

TAX = [("Event", "Observable occurrence", "A failed login on the LIMS", "b", 30), ("Incident", "Violates policy or threatens operations", "Malware found on an instrument PC", "b", 55), ("Breach", "Confirmed loss of data", "Client results copied out", "o", 78), ("Crisis", "Threatens safety or the institution", "Freezers or containment affected", "o", 100)]
S.append(section("taxonomy", f"""<p class="label">Definitions and thresholds</p>
<h2 class="h2" data-k="words">Name the level before you choose the response</h2>
<div class="col" style="gap:16px;margin-top:10px">{''.join(f'<div class="row" style="align-items:center;gap:28px" data-step="{i+1}"><div style="width:{w*9}px;max-width:900px;flex:none;background:var(--{"orange" if c=="o" else "blue"});color:{"#0A1424" if c=="o" else "#fff"};border-radius:12px;padding:22px 28px"><p class="h3" style="font-size:44px">{a}</p></div><div class="col" style="gap:4px"><p class="body"><b>{b}</b></p><p class="body muted">{e}</p></div></div>' for i,(a,b,e,c,w) in enumerate(TAX))}</div>""",
    "light", "rise", foot=FOOT, note="""Four levels, one click each. Most alerts are events. Calling every event a crisis exhausts the team; calling a crisis an event delays the response. Write the thresholds down before you need them.

In a laboratory, anything that touches containment or sample viability goes straight to the top level."""))

RACI = [("Declare an incident", "A", "R", "C", "C", "I", "I"),
        ("Isolate the lab network", "A", "R", "C", "C", "I", "I"),
        ("Decide on samples and containment", "C", "C", "A", "R", "I", "I"),
        ("Report under Law 7545 / KVKK", "A", "C", "I", "I", "R", "C"),
        ("Inform clients and the public", "A", "I", "C", "C", "C", "R")]
hdr = ["Activity", "Incident lead", "IT / network", "Biosafety officer", "Lab head", "Legal / DPO", "Comms"]
S.append(section("raci", f"""<p class="label">Command structure · RS.MA, RS.CO</p>
<h2 class="h2" data-k="words">Who decides, who acts, who is told</h2>
<table class="t raci" style="font-size:28px"><tr>{''.join(f'<th>{h}</th>' for h in hdr)}</tr>
{''.join(f'<tr data-step="{i+1}"><td>{r[0]}</td>' + ''.join(f'<td><span class="{x}">{x}</span></td>' for x in r[1:]) + '</tr>' for i,r in enumerate(RACI))}
</table>
<p class="body muted" data-in="fade" data-d="600"><b>R</b> responsible · <b>A</b> accountable · <b>C</b> consulted · <b>I</b> informed. One A per row.</p>""",
    "light", "morph", foot=FOOT, note="""A RACI matrix adapted from my incident response deck, with one change for laboratories: the biosafety officer is accountable for decisions about samples and containment. IT must not cut power to a freezer room on its own authority.

Five rows, one click each. The reporting row reminds us of Law 7545 and KVKK."""))

S.append(section("golden", """<p class="label">When priorities collide</p>
<div class="col" style="gap:6px;flex:1;justify-content:center">
  <div class="mega o" style="font-size:130px" data-step="1" data-k="stretch">1 · Human safety</div>
  <div class="mega" style="font-size:130px" data-step="2" data-k="stretch">2 · Service continuity</div>
  <div class="mega" style="font-size:130px" data-step="3" data-k="stretch">3 · Data integrity</div>
  <div class="mega muted" style="font-size:130px" data-step="4" data-k="stretch">4 · Reputation</div>
</div>
<p class="body muted" data-step="5">Even under pressure, preserve timestamps and chain of custody. Evidence you destroyed in a hurry cannot be recovered.</p>""",
    "dark", "zoom", "grid-bg", foot=FOOT, note="""The golden rule from my incident response material, one click per line. In a laboratory, human safety includes biosafety: containment comes before getting the sequencer back online.

The last click adds the balance: containment speed versus forensic fidelity. Move fast, but keep the evidence."""))

S.append(section("backup", """<p class="label">RC.RP · recovery</p>
<div class="row" style="gap:40px;align-items:center;margin-top:10px">
  <div class="col" style="align-items:center;gap:8px;flex:1" data-in="pop" data-d="200"><p class="num b" style="font-size:240px">3</p><p class="h3">copies of the data</p></div>
  <div class="col" style="align-items:center;gap:8px;flex:1" data-in="pop" data-d="400"><p class="num b" style="font-size:240px">2</p><p class="h3">different media</p></div>
  <div class="col" style="align-items:center;gap:8px;flex:1" data-in="pop" data-d="600"><p class="num o" style="font-size:240px">1</p><p class="h3">offline or immutable</p></div>
</div>
<div class="spacer"></div>
<div class="card solid" data-step="1" style="padding:36px 40px"><p class="h2" style="font-size:60px">A backup is a hypothesis. A tested restore is evidence.</p></div>""",
    "light", "rise", foot=FOOT, note="""The 3-2-1 rule. Ransomware groups look for backups first, so the offline or immutable copy is the one that saves you.

Click for the line from my incident response deck. Ask: when did your group last restore something from backup on purpose?"""))

LV = [("Level 1 · Basic", "Antivirus alert; manual isolation; sparse local logs", "Panic and delay", "o"),
      ("Level 2 · Intermediate", "EDR alert; fast search for indicators; central logs", "Controlled containment", "b"),
      ("Level 3 · Advanced", "Automated containment; threat hunting; segmented network", "Neutralised in minutes", "b")]
S.append(section("maturity", f"""<p class="label">Same event, three outcomes</p>
<h2 class="h2" data-k="words">Suspicious PowerShell on an instrument PC, with an outbound connection</h2>
<div class="g3" style="gap:26px;margin-top:10px">{''.join(f'<div class="card{" hot" if i==1 else ""}" data-step="{i+1}" style="gap:18px;padding:36px"><p class="k">{a}</p><p class="body">{b}</p><div class="rule"></div><p class="h3 {c}">{o}</p></div>' for i,(a,b,o,c) in enumerate(LV))}</div>
<p class="body muted" data-step="4">Where is your organization on this ladder today? Level 2 is a realistic one-year target for most facilities.</p>""",
    "light", "push", foot=FOOT, note="""One scenario, three maturity levels, from my April incident response workshop. One click per level, then the question to the room.

Level 2 does not require a large security team; it requires central logs and a practised playbook."""))

WK = [("Week 1", "Inventory & roles", "Asset list, crown jewels, name the incident lead and deputies"),
      ("Week 2", "Starter kit", "A master plan and three playbooks: ransomware, vendor compromise, data leak"),
      ("Week 3", "Telemetry audit", "Clocks synced, log sources connected, retention set"),
      ("Week 4", "Tabletop", "A 60-minute exercise with IT, biosafety, lab heads and legal")]
S.append(section("sprint", f"""<canvas class="fx" data-fx="helix" data-x="1640"></canvas>
<p class="label">Start tomorrow · a 30-day sprint</p>
<div class="g4" style="gap:22px;flex:1;align-content:center;max-width:1480px">{''.join(f'<div class="card" data-in="up" data-d="{300+i*150}" style="gap:16px;padding:34px"><p class="label">{w}</p><p class="h2" style="font-size:54px">{a}</p><p class="body muted">{b}</p></div>' for i,(w,a,b) in enumerate(WK))}</div>
<p class="lead muted" data-in="fade" data-d="1000">Complexity is the enemy of execution. Start with the basics, but start.</p>""",
    "dark", "zoom", "grid-bg", foot=FOOT, note="""The 30-day sprint from my incident response material. It is deliberately modest: inventory and roles, a starter kit of plans, a telemetry audit, and a tabletop exercise.

Any institution represented here can do this before the end of the year."""))

MET = [("MTTD", "Mean time to detect", "b"), ("MTTR", "Mean time to respond", "b"), ("MFA %", "Remote paths with MFA", "o"), ("Assets %", "Devices on the inventory", "b"), ("Restore", "Last successful test", "o"), ("Reports", "Phishing reports by staff", "b")]
S.append(section("metrics", f"""<p class="label">Metrics that matter</p>
<h2 class="h2" data-k="words">You cannot manage what you do not measure</h2>
<div class="g3" style="gap:22px;margin-top:10px">{''.join(f'<div class="card tile" data-in="up" data-d="{300+i*90}" style="padding:30px 34px"><p class="num {c}" style="font-size:80px">{a}</p><p class="body">{b}</p></div>' for i,(a,b,c) in enumerate(MET))}</div>
<p class="body muted" data-in="fade" data-d="1000">Report them to leadership every quarter. Metrics are what turn security from a cost into a budget line.</p>""",
    "light", "wipe", foot=FOOT, note="""Six metrics a facility can actually collect. Rising phishing reports are good news: they mean people are noticing.

These numbers are also how you justify the budget for phase two."""))

S.append(section("takeaways", """<canvas class="fx" data-fx="rings"></canvas>
<p class="label">Three things to keep</p>
<div class="col" style="gap:8px;flex:1;justify-content:center">
  <div class="mega" style="font-size:108px" data-step="1" data-k="stretch">Inventory before investment.</div>
  <div class="mega b" style="font-size:108px" data-step="2" data-k="stretch">MFA on every remote path.</div>
  <div class="mega o" style="font-size:108px" data-step="3" data-k="stretch">Rehearse with biosafety.</div>
</div>
<div class="row" style="gap:24px" data-step="4"><span class="chip">13:30 · Laboratory cyberbiosecurity policies & SOPs · Prof. Dr. Gökçe Merey</span><span class="chip o">14:30 · Hands-on: apply CSF 2.0</span></div>""",
    "dark", "zoom", "grid-bg", foot=FOOT, note="""Three lines, one click each, then the afternoon programme. Prof. Merey's session on policies and SOPs follows lunch; it builds directly on the RACI and playbooks we saw here."""))

S.append(sources("refs", [
    "PwC. <i>Conti cyber attack on the HSE: independent post incident review</i>. Commissioned by the HSE Board; published 10 Dec 2021.",
    "NHS England (London). Update on cyber incident clinical impact in south east London; 19 Sep 2024.",
    "Infosecurity Magazine. Patient death linked to NHS cyber-attack (King’s College Hospital statement); 26 Jun 2025.",
    "CyberInsider. Change Healthcare revises breach impact to 192.7 million individuals (HHS OCR filing of 31 Jul 2025); 15 Aug 2025.",
    "Nelson A, Rekhi S, Souppaya M, Scarfone K. <i>Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile</i>. NIST SP 800-61r3; 2025. doi:10.6028/NIST.SP.800-61r3",
    "National Institute of Standards and Technology. <i>The NIST Cybersecurity Framework (CSF) 2.0</i>. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
    "Altun A. <i>Incident Response: Best Practices, Tools, and Resources</i>; and <i>Personnel-Related Vulnerabilities and Cybersecurity</i>. Workshop materials, 2026.",
    "7545 sayılı Siber Güvenlik Kanunu. Resmî Gazete 32846; 19 Mar 2025. · 6698 sayılı Kişisel Verilerin Korunması Kanunu.",
], FOOT))

S.append(thanks("thanks", "Thank you.", "Questions on building the infrastructure", "Take questions, then release for lunch. Remind everyone that the 14:30 exercise uses everything from this session.", FOOT))

if __name__ == "__main__":
    n = build("/home/claude/corum/dist/d3/index.html", "Institutional Cyber Infrastructure", 60, FOOT, S, extra_css=CSS)
    print("slides", n)
