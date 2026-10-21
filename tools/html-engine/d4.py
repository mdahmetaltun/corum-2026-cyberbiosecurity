from lib import *

FOOT = "Hands-on · Applying NIST CSF 2.0 to a Biotechnology Lab"
S = []

CATS = [("GV.RR", "Roles, responsibilities & authorities", "GV"), ("GV.PO", "Policy", "GV"), ("GV.SC", "Supply chain risk management", "GV"),
        ("ID.AM", "Asset management", "ID"), ("ID.RA", "Risk assessment", "ID"),
        ("PR.AA", "Identity, authentication & access", "PR"), ("PR.AT", "Awareness & training", "PR"), ("PR.DS", "Data security", "PR"), ("PR.PS", "Platform security", "PR"),
        ("DE.CM", "Continuous monitoring", "DE"), ("RS.MA", "Incident management", "RS"), ("RC.RP", "Recovery plan execution", "RC")]

CSS = """
.seg { display:inline-flex; border-radius:10px; overflow:hidden; border:1.5px solid var(--rule); }
.seg button { font: 500 24px var(--mono); width:50px; height:40px; border:0; background:var(--card); color:var(--text); cursor:pointer; border-left:1.5px solid var(--rule); }
.seg button:first-child { border-left:0; }
.seg.cur button.on { background: var(--blue-t); color:#fff; }
.seg.tgt button.on { background: var(--orange); color: var(--ink); }
.seg button:focus-visible { outline: 3px solid var(--orange); outline-offset: -3px; }
.btab { font: 500 24px var(--mono); padding: 10px 18px; border-radius: 10px; border: 1.5px solid var(--rule); background: var(--card); color: var(--text); cursor: pointer; }
.btab.on { background: var(--ink); color: var(--steel); border-color: var(--ink); }
.btn { font: 500 24px var(--mono); padding: 12px 20px; border-radius: 10px; border: 0; cursor: pointer; letter-spacing: .04em; }
.btn.pri { background: var(--orange); color: var(--ink); }
.btn.sec { background: var(--paper-2); color: var(--text); }
.dark .btn.sec { background: var(--ink-3); color: var(--steel); }
.btn:focus-visible, .btab:focus-visible { outline: 3px solid var(--blue); outline-offset: 2px; }
.prow { display:grid; grid-template-columns: 130px 1fr 210px 210px; align-items:center; gap: 14px; padding: 3px 0; border-bottom: 1.5px solid var(--rule); }
.prow .nm { font-size: 24px; line-height: 1.2; }
.gap-item { display:flex; gap:14px; align-items:center; font-size: 26px; }
.ap input { font: 400 25px var(--sans); width: 100%; box-sizing: border-box; padding: 12px 14px; border: 1.5px solid var(--rule); border-radius: 10px; background: var(--card); color: var(--text); }
.ap input:focus { outline: 3px solid var(--blue); outline-offset: 0; }
.ap .r { display:grid; grid-template-columns: 70px 1.6fr 170px 1fr 1fr 150px; gap: 14px; align-items:center; }
.phase { display:grid; grid-template-columns: 70px 1fr 120px; align-items:center; gap: 18px; padding: 16px 22px; border-radius: 12px; }
.phase.now { background: var(--orange); color: var(--ink); }
.phase.done { opacity: .45; }
#copyout { width: 100%; height: 140px; font: 20px var(--mono); }
"""

S.append(lobby("lobby", "Day 2 · Tuesday 3 November", "14:30 – 15:15",
    ["Hands-on Group", "Exercise"], "Applying NIST CSF 2.0 to a biotechnology laboratory",
    """Holding screen while groups sit together. Ideally five or six groups of four to six people, mixing institutions and roles. Press → for the opening film."""))

S.append(video("open", "media/opener.mp4", "media/opener.jpg", "Opening film, about 10 seconds: one laboratory, six functions, twenty-two categories, forty-five minutes. Advances by itself."))

S.append(section("title", f"""<canvas class="fx" data-fx="helix" data-x="1560"></canvas>
<p class="label" data-in="fade">Session 4 · Hands-on</p>
<div class="mega" data-k="stretch" style="font-size:240px" data-wdth="112">APPLY IT.</div>
<p class="lead muted" data-in="up" data-d="700">Build a CSF 2.0 profile for a biotechnology laboratory in 45 minutes</p>
<div class="spacer"></div>
<div class="col" data-in="fade" data-d="900" style="gap:4px"><p class="h3">{SPEAKER}</p><p class="small muted">{AFFIL}</p></div>""",
    "dark", "fade", "grid-bg", foot=EVENT, note="""This is where the two days come together. Each group becomes the cyberbiosecurity working group of a fictional laboratory and produces a small Organizational Profile and a three-item action plan. Group presentations follow at 15:30."""))

S.append(section("mission", """<canvas class="fx" data-fx="rings"></canvas>
<p class="label">Your mission</p>
<h2 class="h1" data-k="words" style="font-size:100px;max-width:1500px">You are HelixLab’s new cyberbiosecurity working group.</h2>
<div class="g3" style="gap:24px;margin-top:20px;max-width:1500px">
  <div class="card" data-in="up" data-d="700"><p class="k">DELIVER 1</p><p class="h3">Crown jewels and scope</p></div>
  <div class="card" data-in="up" data-d="850"><p class="k">DELIVER 2</p><p class="h3">Current and Target Profile for 12 categories</p></div>
  <div class="card solid" data-in="up" data-d="1000"><p class="k" style="color:inherit">DELIVER 3</p><p class="h3">Top three actions, with owners</p></div>
</div>
<p class="lead muted" data-in="fade" data-d="1200">Presented in three minutes per group at 15:30.</p>""", "dark", "zoom", "grid-bg", foot=FOOT, note="""Read the mission aloud. The three deliverables mirror steps 1 to 4 of NIST's quick-start guide from yesterday: scope, gather, create, analyse and plan."""))

ASSETS = [("NGS sequencer", "Windows 10 control PC; vendor cloud upload; vendor remote support tool"), ("2 × qPCR systems", "Results exported by USB stick to the analysis PC"),
          ("4 × −80 °C freezers", "Wi-Fi alarm module sends SMS to the lab head"), ("LIMS", "Cloud service; one shared admin account"),
          ("Analysis server", "Linux; 18 student accounts; no central logs"), ("AI tools", "Chat assistant for SOP drafts; image classifier for cell counts")]
S.append(section("helix", f"""<p class="label">Fact sheet · HelixLab (fictional)</p>
<h2 class="h2" style="font-size:66px">A university biotechnology laboratory, BSL-2</h2>
<div class="g3" style="gap:18px">
  <div class="card" data-in="up" data-d="200" style="gap:6px;padding:24px 28px"><p class="k">PEOPLE</p><p class="body">6 staff · 18 graduate students · 2 client technicians with badge access</p></div>
  <div class="card hot" data-in="up" data-d="300" style="gap:6px;padding:24px 28px"><p class="k">CLIENTS</p><p class="body">3 biotech companies send samples and receive sequencing data</p></div>
  <div class="card" data-in="up" data-d="400" style="gap:6px;padding:24px 28px"><p class="k">NETWORK</p><p class="body">One campus network for everything; lab Wi-Fi password on the door</p></div>
</div>
<p class="label muted" style="color:var(--mute-l)">Systems</p>
<div class="g3" style="gap:16px">{''.join(f'<div class="card" data-in="up" data-d="{500+i*80}" style="gap:6px;padding:24px 28px"><p class="h3" style="font-size:34px">{a}</p><p class="body muted" style="font-size:27px">{b}</p></div>' for i,(a,b) in enumerate(ASSETS))}</div>""", "light", "wipe", foot=FOOT, note="""The fact sheet is deliberately realistic: every detail is something seen in real laboratories. Give groups two minutes to read it. The three client companies make supply-chain governance relevant, and the AI tools link back to this morning."""))

INJ = [("Friday 18:30", "An email from the “sequencer vendor” asks the lab to install an urgent firmware update via a download link before Monday."),
       ("Last week", "Freezer alarm SMS messages stopped arriving three days ago. Nobody noticed until a sample check."),
       ("Yesterday", "A student pasted a client’s sample sheet, with project codes and donor ages, into a public AI chatbot to reformat it.")]
S.append(section("injects", f"""<p class="label">Three things that happened this month</p>
<div class="g3" style="gap:26px;flex:1;align-content:center">{''.join(f'<div class="card" data-step="{i+1}" style="gap:20px;padding:40px"><p class="num {"o" if i==0 else "b"}" style="font-size:110px">{i+1}</p><p class="label">{d}</p><p class="lead" style="font-size:33px">{t}</p></div>' for i,(d,t) in enumerate(INJ))}</div>
<p class="body muted" data-step="4">Use them as evidence when you rate the Current Profile. Each one points to at least two categories.</p>""",
    "dark", "rise", "grid-bg", foot=FOOT, note="""Reveal the three events one at a time. They are the evidence groups should use. Don't tell them which categories each maps to; that is in the debrief slide."""))

ROLES = [("Lab head", "Chairs; owns the final decisions"), ("Biosafety officer", "Samples, containment, cold chain"), ("IT / network", "Systems, accounts, logs, backups"),
         ("Data steward", "Client data, KVKK, AI tool use"), ("Vendor manager", "Contracts, remote access, procurement"), ("Rapporteur", "Records ratings; presents at 15:30")]
S.append(section("roles", f"""<p class="label">Take a role</p>
<h2 class="h2" data-k="words">Six seats at the table. Argue from yours.</h2>
<div class="g3" style="gap:20px;margin-top:10px">{''.join(f'<div class="card{" hot" if i==5 else ""}" data-in="up" data-d="{300+i*80}" style="gap:10px"><p class="h3" style="font-size:40px">{a}</p><p class="body muted">{b}</p></div>' for i,(a,b) in enumerate(ROLES))}</div>""",
    "light", "push", foot=FOOT, note="""Ask each group to assign roles now; with fewer than six people, combine vendor manager with data steward. Role-play creates productive disagreement, especially between IT and the biosafety officer."""))

PHASES = [("Scope & crown jewels", 8), ("Rate the Current Profile", 12), ("Set Target & find gaps", 10), ("Top-3 action plan", 10), ("Prepare the 3-minute pitch", 5)]
plist = "".join(f'<div class="phase" data-ph="{i}"><p class="num" style="font-size:56px">{i+1}</p><p class="h3" style="font-size:36px">{a}</p><p class="mono tab" style="font-size:30px;text-align:right">{m} min</p></div>' for i, (a, m) in enumerate(PHASES))
S.append(section("clock", f"""<p class="label">45 minutes · five phases</p>
<div class="row" style="flex:1;gap:50px;align-items:center" data-interactive>
  <div class="col" style="gap:8px;width:820px;flex:none" id="phlist">{plist}</div>
  <div class="col grow" style="align-items:center;gap:26px">
    <div style="position:relative;width:520px;height:520px">
      <svg viewBox="0 0 520 520" style="width:520px;height:520px" aria-hidden="true"><circle cx="260" cy="260" r="236" fill="none" stroke="rgba(232,236,239,.12)" stroke-width="22"/><circle id="tring" cx="260" cy="260" r="236" fill="none" stroke="#FF5B1F" stroke-width="22" stroke-linecap="round" transform="rotate(-90 260 260)" stroke-dasharray="1482.8" stroke-dashoffset="0"/></svg>
      <div class="col" style="position:absolute;inset:0;align-items:center;justify-content:center;gap:6px"><p class="num tab" id="tclock" style="font-size:150px">08:00</p><p class="label" id="tphase">Phase 1 of 5</p></div>
    </div>
    <div class="row" style="gap:14px"><button class="btn pri" id="tstart">Start</button><button class="btn sec" id="tnext">Next phase</button><button class="btn sec" id="treset">Reset</button></div>
  </div>
</div>""", "dark", "zoom", "grid-bg", attrs='data-hook="timer"', foot=FOOT, note="""The facilitation timer. Press Start; it counts down each phase and moves on automatically, highlighting the current phase on the left. Next phase skips ahead; Reset returns to the start.

The timer keeps running if you move to other slides, so you can show the rating guide or the builder and come back."""))

S.append(section("scope", """<p class="label">Phase 1 · 8 minutes · GV.OC, ID.AM</p>
<h2 class="h2" data-k="words">Scope it, then name the crown jewels</h2>
<div class="g2" style="gap:30px;margin-top:10px">
  <div class="card" data-in="up" data-d="300" style="gap:16px"><p class="k">ANSWER TOGETHER</p><ul class="clean"><li>Which systems are in scope? Which are not?</li><li>Which laws and contracts apply? (Law 7545, KVKK, client contracts)</li><li>Who would be harmed if HelixLab were down for two weeks?</li></ul></div>
  <div class="card hot" data-in="up" data-d="450" style="gap:16px"><p class="k">CROWN JEWELS · PICK THREE</p><ul class="clean"><li>What must never be lost?</li><li>What must never leak?</li><li>What must never be altered without anyone noticing?</li></ul></div>
</div>""", "light", "push", foot=FOOT, note="""Eight minutes. Lost, leaked, altered: those three questions map to availability, confidentiality and integrity, the CIA triad from yesterday's introduction. Good answers usually include the client data, the freezer contents and the sequencing results."""))

TG = [("1", "Partial", "Nobody owns it; it happens if someone remembers"), ("2", "Risk informed", "People know it matters; it is not written policy"), ("3", "Repeatable", "Written, approved, done the same way every time"), ("4", "Adaptive", "Measured and improved from lessons learned")]
S.append(section("rate", f"""<p class="label">Phase 2–3 · rating guide</p>
<h2 class="h2" data-k="words">Rate each category from 1 to 4</h2>
<div class="g4" style="gap:20px">{''.join(f'<div class="card{" hot" if n=="3" else ""}" data-in="up" data-d="{300+i*100}" style="gap:10px"><p class="num {"o" if n=="3" else "b"}" style="font-size:96px">{n}</p><p class="h3">{a}</p><p class="body muted">{b}</p></div>' for i,(n,a,b) in enumerate(TG))}</div>
<div class="row" style="flex-wrap:wrap;gap:12px" data-in="fade" data-d="800">{''.join(f'<span class="chip">{c}</span>' for c,_,_ in CATS)}</div>
<p class="body muted" data-in="fade" data-d="900">Twelve categories chosen from the 22 for this lab. Be honest about Current; be realistic about Target.</p>""",
    "light", "rise", foot=FOOT, note="""A plain-language version of the CSF tiers for rating categories. Remind groups: tier 4 everywhere is not a sensible target for a teaching-and-research lab. Most targets land on 2 or 3.

Twelve categories keeps it achievable in the time; they are the ones the fact sheet and the three events give evidence for."""))

rows = "".join(f"""<div class="prow" data-cat="{c}"><span class="chip">{c}</span><span class="nm">{n}</span>
<span class="seg cur" role="group" aria-label="{c} current tier">{''.join(f'<button data-v="{v}" aria-label="Current {v}">{v}</button>' for v in range(1,5))}</span>
<span class="seg tgt" role="group" aria-label="{c} target tier">{''.join(f'<button data-v="{v}" aria-label="Target {v}">{v}</button>' for v in range(1,5))}</span></div>""" for c, n, _ in CATS)
tabs = '<button class="btab" data-g="EX">Example</button>' + "".join(f'<button class="btab" data-g="G{i}">Group {i}</button>' for i in range(1, 7))
S.append(section("builder", f"""<div class="row" style="justify-content:space-between;align-items:center" data-interactive>
  <div class="col" style="gap:6px"><p class="label">Profile builder · live</p><p class="h3" id="bnote" style="font-size:34px">Example ratings for HelixLab</p></div>
  <div class="row" style="gap:10px">{tabs}</div>
</div>
<div class="row" style="flex:1;gap:44px;min-height:0" data-interactive>
  <div class="col" style="width:1000px;flex:none;gap:0">
    <div class="prow" style="border-bottom:2px solid var(--text)"><span class="label muted" style="color:var(--mute-l)">Code</span><span class="label muted" style="color:var(--mute-l)">Category</span><span class="label b" style="color:var(--blue-t)">Current</span><span class="label">Target</span></div>
    {rows}
  </div>
  <div class="col grow" style="gap:12px;min-width:0">
    <div id="bradar" data-axes="GV,ID,PR,DE,RS,RC" data-a="1,1,1,1,1,1" data-b="1,1,1,1,1,1" style="width:480px;height:440px;align-self:center"></div>
    <p class="label">Largest gaps</p>
    <div class="col" id="bgaps" style="gap:8px"></div>
    <div class="row" style="gap:10px;margin-top:6px"><button class="btn pri" id="bcopy">Copy summary</button><button class="btn sec" id="bclear">Clear group</button></div>
    <textarea id="copyout" hidden readonly aria-label="Summary text"></textarea>
  </div>
</div>""", "light", "morph", attrs='data-hook="builder"', foot=FOOT, note="""The live profile builder. Pick a group tab and click tiers: blue for Current, orange for Target. The radar averages categories per function, and the three largest gaps are listed automatically.

The Example tab is pre-filled to show how it works; groups 1 to 6 start empty. Ratings are kept in this browser only. During the 15:30 presentations, enter each group's numbers on its tab and compare. Copy summary puts a text version on the clipboard."""))

aprow = lambda i: f"""<div class="r"><p class="num o" style="font-size:56px">{i}</p><input id="ap{i}a" placeholder="Action" aria-label="Action {i}"><input id="ap{i}c" placeholder="CSF code" aria-label="CSF code {i}"><input id="ap{i}o" placeholder="Owner (role)" aria-label="Owner {i}"><input id="ap{i}w" placeholder="By when" aria-label="By when {i}"><input id="ap{i}k" placeholder="Cost L/M/H" aria-label="Cost {i}"></div>"""
S.append(section("plan", f"""<p class="label">Phase 4 · 10 minutes · the action plan</p>
<h2 class="h2" data-k="words">Three actions. Each closes a named gap.</h2>
<div class="ap col" style="gap:16px" data-interactive>
  <div class="r"><span></span><span class="label muted" style="color:var(--mute-l)">Action</span><span class="label muted" style="color:var(--mute-l)">CSF</span><span class="label muted" style="color:var(--mute-l)">Owner</span><span class="label muted" style="color:var(--mute-l)">By when</span><span class="label muted" style="color:var(--mute-l)">Cost</span></div>
  {aprow(1)}{aprow(2)}{aprow(3)}
</div>
<div class="card" data-in="up" data-d="600" style="flex-direction:row;gap:26px;align-items:center"><p class="label" style="flex:none">Example</p><p class="body">Route all vendor remote support through one jump host with MFA and a ticket · <b>PR.AA, GV.SC</b> · IT / network · 6 weeks · <b>M</b></p></div>""",
    "light", "push", attrs='data-hook="plan"', foot=FOOT, note="""Groups fill this on paper or here. A good action names the gap it closes, an owner by role, a date and a rough cost. Vague actions such as "improve awareness" should be pushed back: awareness of what, for whom, by when?

The fields on this slide are saved in this browser for the active group tab of the builder."""))

S.append(section("pitch", """<canvas class="fx" data-fx="net"></canvas>
<p class="label">15:30 · three minutes per group</p>
<div class="g4" style="gap:22px;flex:1;align-content:center">
  <div class="card" data-in="up" data-d="200" style="gap:14px;padding:38px"><p class="num b" style="font-size:100px">30″</p><p class="h3">Our crown jewels</p></div>
  <div class="card" data-in="up" data-d="350" style="gap:14px;padding:38px"><p class="num b" style="font-size:100px">45″</p><p class="h3">Our biggest gap, and the evidence</p></div>
  <div class="card hot" data-in="up" data-d="500" style="gap:14px;padding:38px"><p class="num o" style="font-size:100px">75″</p><p class="h3">Our three actions and owners</p></div>
  <div class="card" data-in="up" data-d="650" style="gap:14px;padding:38px"><p class="num b" style="font-size:100px">30″</p><p class="h3">One question for the room</p></div>
</div>""", "dark", "zoom", "grid-bg", foot=FOOT, note="""The pitch format. Three minutes total, strictly timed. The question for the room at the end is often the best part of the presentations."""))

DEB = [("Fake vendor email", ["GV.SC", "PR.AT", "PR.AA"]), ("Freezer alarm went silent", ["DE.CM", "ID.AM", "RS.MA"]), ("Client data in a public chatbot", ["PR.DS", "GV.PO", "PR.AT"])]
S.append(section("debrief", f"""<p class="label">Facilitator debrief · show after the presentations</p>
<h2 class="h2" data-k="words">What the three events were pointing at</h2>
<div class="col" style="gap:18px;margin-top:10px">{''.join(f'<div class="row card" data-step="{i+1}" style="flex-direction:row;align-items:center;gap:30px;padding:26px 32px"><p class="num {"o" if i==0 else "b"}" style="font-size:72px;width:70px">{i+1}</p><p class="h3 grow">{t}</p><div class="row" style="gap:10px">{"".join(f"<span class=\'chip {"o" if j==0 else ""}\'>{c}</span>" for j,c in enumerate(cs))}</div></div>' for i,(t,cs) in enumerate(DEB))}</div>
<p class="body muted" data-step="4">Most groups find their largest gap in GV.SC or DE.CM. Neither needs a big budget; both need an owner.</p>""",
    "light", "rise", foot=FOOT, note="""Use after the 15:30 group presentations. Reveal one event at a time and ask which groups caught which categories.

Closing point: the two most common big gaps, supply chain and monitoring, are mainly governance work. That brings us back to GOVERN at the centre of the wheel."""))

S.append(section("close", """<canvas class="fx" data-fx="helix" data-x="1560"></canvas>
<div class="spacer"></div>
<div class="mega" style="font-size:150px" data-k="rise">Your profile is a draft.</div>
<div class="mega o" style="font-size:150px" data-k="rise" data-d="500">Your lab is real.</div>
<div class="spacer"></div>
<div class="row" style="gap:20px" data-in="fade" data-d="1200"><span class="chip">15:30 · Group presentations &amp; discussion</span><span class="chip o">Closing · evaluation · certificates</span></div>""",
    "dark", "iris", "grid-bg", foot=FOOT, note="""Close the exercise. Encourage every participant to repeat the profile for their own laboratory within the month, starting with the inventory. Then move to the group presentations."""))

JS = r"""
(function(){
  const CATS = %CATS%;
  const FN = ['GV','ID','PR','DE','RS','RC'];
  const EX = {cur:{'GV.RR':1,'GV.PO':1,'GV.SC':1,'ID.AM':2,'ID.RA':1,'PR.AA':1,'PR.AT':2,'PR.DS':1,'PR.PS':1,'DE.CM':1,'RS.MA':1,'RC.RP':2},
              tgt:{'GV.RR':3,'GV.PO':3,'GV.SC':3,'ID.AM':3,'ID.RA':3,'PR.AA':3,'PR.AT':3,'PR.DS':3,'PR.PS':2,'DE.CM':3,'RS.MA':3,'RC.RP':3}};
  const KEY = 'corum-csf-profiles-v1';
  let store = {}; try { store = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch(e) { store = {}; }
  const save = () => { try { localStorage.setItem(KEY, JSON.stringify(store)); } catch(e) {} };
  let g = 'EX';
  const data = (k) => { if (k === 'EX') return { cur: {...EX.cur}, tgt: {...EX.tgt}, plan: store.EXplan || {} }; return store[k] || (store[k] = { cur:{}, tgt:{}, plan:{} }); };
  let D = data('EX');
  const $ = (s, r=document) => r.querySelector(s), $$ = (s, r=document) => [...r.querySelectorAll(s)];
  function avg(side, f) { const v = CATS.filter(c => c[2]===f).map(c => D[side][c[0]]).filter(Boolean); return v.length ? v.reduce((a,b)=>a+b,0)/v.length : 0; }
  function render() {
    const b = $('#builder'); if (!b) return;
    $$('.btab', b).forEach(t => t.classList.toggle('on', t.dataset.g === g));
    $('#bnote').textContent = g === 'EX' ? 'Example ratings for HelixLab' : 'Group ' + g.slice(1) + ' · click tiers to rate';
    $$('.prow[data-cat]', b).forEach(r => { const c = r.dataset.cat;
      $$('.cur button', r).forEach(x => x.classList.toggle('on', +x.dataset.v === D.cur[c]));
      $$('.tgt button', r).forEach(x => x.classList.toggle('on', +x.dataset.v === D.tgt[c])); });
    const rd = $('#bradar');
    rd.dataset.a = FN.map(f => avg('cur', f).toFixed(2)).join(','); rd.dataset.b = FN.map(f => avg('tgt', f).toFixed(2)).join(',');
    if (window.Deck) Deck.drawRadar(rd, false);
    const gaps = CATS.map(c => [c, (D.tgt[c[0]]||0) - (D.cur[c[0]]||0)]).filter(x => x[1] > 0 && D.cur[x[0][0]]).sort((a,b) => b[1]-a[1]).slice(0,3);
    $('#bgaps').innerHTML = gaps.length ? gaps.map(([c, d]) => `<div class="gap-item"><span class="chip o">+${d}</span><span class="chip">${c[0]}</span><span>${c[1]}</span></div>`).join('') : '<p class="body muted">Rate Current and Target to see gaps.</p>';
    $$('#plan input').forEach(i => { i.value = (D.plan||{})[i.id] || ''; });
  }
  function summary() {
    const lines = [`HelixLab CSF 2.0 profile — ${g === 'EX' ? 'Example' : 'Group ' + g.slice(1)}`, 'Category\tCurrent\tTarget\tGap'];
    CATS.forEach(c => lines.push(`${c[0]} ${c[1]}\t${D.cur[c[0]]||'-'}\t${D.tgt[c[0]]||'-'}\t${(D.tgt[c[0]]&&D.cur[c[0]]) ? D.tgt[c[0]]-D.cur[c[0]] : '-'}`));
    lines.push('', 'Action plan');
    [1,2,3].forEach(i => { const p = D.plan||{}; const a = p['ap'+i+'a']; if (a) lines.push(`${i}. ${a} | ${p['ap'+i+'c']||''} | ${p['ap'+i+'o']||''} | ${p['ap'+i+'w']||''} | ${p['ap'+i+'k']||''}`); });
    return lines.join('\n');
  }
  document.addEventListener('click', (e) => {
    const t = e.target.closest('.btab'); if (t) { g = t.dataset.g; D = data(g); render(); return; }
    const bt = e.target.closest('.seg button');
    if (bt) { if (g === 'EX') { g = 'G1'; D = data('G1'); } const side = bt.parentElement.classList.contains('cur') ? 'cur' : 'tgt'; const c = bt.closest('.prow').dataset.cat; const v = +bt.dataset.v; D[side][c] = D[side][c] === v ? undefined : v; save(); render(); return; }
    if (e.target.id === 'bclear' && g !== 'EX') { store[g] = { cur:{}, tgt:{}, plan:{} }; D = store[g]; save(); render(); return; }
    if (e.target.id === 'bcopy') { const txt = summary(), out = $('#copyout');
      const fallback = () => { out.hidden = false; out.value = txt; out.select(); e.target.textContent = 'Select and copy'; };
      try { navigator.clipboard.writeText(txt).then(() => { e.target.textContent = 'Copied'; out.hidden = true; setTimeout(() => e.target.textContent = 'Copy summary', 1800); }, fallback); } catch(err) { fallback(); } }
  });
  document.addEventListener('input', (e) => { if (e.target.closest && e.target.closest('#plan')) { if (g === 'EX') { store.EXplan = store.EXplan || {}; store.EXplan[e.target.id] = e.target.value; D.plan = store.EXplan; } else { D.plan = D.plan || {}; D.plan[e.target.id] = e.target.value; } save(); } });

  /* phase timer */
  const PH = %PHASES%;
  let ph = 0, left = PH[0][1]*60, running = false, last = 0;
  function tdraw() {
    const c = $('#tclock'); if (!c) return;
    c.textContent = `${String(Math.floor(left/60)).padStart(2,'0')}:${String(Math.floor(left%60)).padStart(2,'0')}`;
    $('#tphase').textContent = ph >= PH.length ? 'Time — present at 15:30' : `Phase ${ph+1} of ${PH.length}`;
    $('#tstart').textContent = running ? 'Pause' : 'Start';
    const total = (PH[Math.min(ph, PH.length-1)][1])*60;
    $('#tring').setAttribute('stroke-dashoffset', String(1482.8 * (1 - Math.max(0,left)/total)));
    $$('#phlist .phase').forEach((p,i) => { p.classList.toggle('now', i === ph); p.classList.toggle('done', i < ph); });
  }
  setInterval(() => { const now = performance.now(); if (running) { left -= (now - last)/1000; if (left <= 0) { ph++; if (ph >= PH.length) { running = false; left = 0; ph = PH.length; } else left = PH[ph][1]*60; } } last = now; tdraw(); }, 250);
  document.addEventListener('click', (e) => {
    if (e.target.id === 'tstart') { running = !running; last = performance.now(); tdraw(); }
    if (e.target.id === 'tnext') { if (ph < PH.length-1) { ph++; left = PH[ph][1]*60; } tdraw(); }
    if (e.target.id === 'treset') { ph = 0; left = PH[0][1]*60; running = false; tdraw(); }
  });
  window.DeckHooks = { builder(s, step, ev) { if (ev === 'enter') render(); }, timer() { tdraw(); }, plan(s, step, ev) { if (ev === 'enter') render(); } };
  document.addEventListener('DOMContentLoaded', render);
  setTimeout(render, 50);
})();
"""
JS = JS.replace("%CATS%", str([list(c) for c in CATS]).replace("'", '"')).replace("%PHASES%", str([list(p) for p in PHASES]).replace("'", '"'))

if __name__ == "__main__":
    n = build("/home/claude/corum/dist/d4/index.html", "HelixLab CSF Exercise", 45, FOOT, S, extra_css=CSS, extra_js=JS)
    print("slides", n)
