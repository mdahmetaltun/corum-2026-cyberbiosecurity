import math
from lib import *

FOOT = "NIST AI RMF · Research Laboratories"
S = []


def rmf_svg(sid, active="", small=False):
    """AI RMF core: GOVERN at the centre, MAP → MEASURE → MANAGE around it. Segments carry data-seg for zoom targets
    and data-only/data-on hooks via the outer slide."""
    r0, r1, g = 200, 470, 0.035
    segs = [("MAP", -math.pi / 2 - math.pi / 3), ("MEASURE", -math.pi / 2 + math.pi / 3), ("MANAGE", math.pi / 2 + math.pi / 3 - 0.0)]
    # three equal sectors starting at top-left, going clockwise: MAP (top-right), MEASURE (bottom), MANAGE (top-left)
    starts = [-math.pi / 2, -math.pi / 2 + 2 * math.pi / 3, -math.pi / 2 + 4 * math.pi / 3]
    out = [f'<svg viewBox="-500 -500 1000 1000" role="img" aria-label="AI RMF core: Govern, Map, Measure, Manage" style="width:100%;height:100%;overflow:visible"><defs>']
    paths = []
    for i, name in enumerate(["MAP", "MEASURE", "MANAGE"]):
        a0 = starts[i] + g; a1 = starts[i] + 2 * math.pi / 3 - g
        mid = (a0 + a1) / 2; flip = math.sin(mid) > 0.2
        rm = (r0 + r1) / 2 - 16
        A0, A1 = (a1, a0) if flip else (a0, a1)
        out.append(f'<path id="{sid}-t{i}" d="M{rm*math.cos(A0):.1f},{rm*math.sin(A0):.1f} A{rm},{rm} 0 0 {0 if flip else 1} {rm*math.cos(A1):.1f},{rm*math.sin(A1):.1f}"/>')
        p = lambda r, a: f"{r*math.cos(a):.1f},{r*math.sin(a):.1f}"
        d = f"M{p(r1,a0)} A{r1},{r1} 0 0 1 {p(r1,a1)} L{p(r0,a1)} A{r0},{r0} 0 0 0 {p(r0,a0)} Z"
        on = name in active or active == "ALL"
        paths.append(f'<g class="rseg{" on" if on else ""}" data-seg="{name}" data-rk="{name}"><path d="{d}" stroke-width="3"/><text font-size="{56 if name!="MEASURE" else 52}" text-anchor="middle" dy="{34 if flip else 0}" font-family="Archivo, sans-serif" font-weight="800" letter-spacing="5"><textPath href="#{sid}-t{i}" startOffset="50%">{name}</textPath></text></g>')
        # arrow head at the end of each sector (clockwise flow)
        ae = starts[i] + 2 * math.pi / 3 - g * 0.2
        paths.append(f'<circle cx="{(r1+28)*math.cos(ae):.1f}" cy="{(r1+28)*math.sin(ae):.1f}" r="9" class="rdot"/>')
    out.append("</defs>")
    out += paths
    on = "GOVERN" in active or active == "ALL"
    out.append(f'<g class="rseg gv{" on" if on else ""}" data-seg="GOVERN" data-rk="GOVERN"><circle r="{r0-24}" stroke-width="3"/><text font-size="58" text-anchor="middle" dy="20" font-family="Archivo, sans-serif" font-weight="850" letter-spacing="4">GOVERN</text></g>')
    out.append("</svg>")
    return "".join(out)


CSS = """
.rmf .rseg path, .rmf .rseg circle { transition: fill .45s, stroke .45s; }
.dark .rmf .rseg path, .dark .rmf .rseg circle { fill: var(--ink-2); stroke: rgba(232,236,239,.28); }
.dark .rmf .rseg text { fill: var(--steel); }
.light .rmf .rseg path, .light .rmf .rseg circle { fill: var(--card); stroke: #B9C3CC; }
.light .rmf .rseg text { fill: var(--text); }
.rmf .rseg.on path { fill: #4C7DFF !important; stroke: transparent !important; }
.light .rmf .rseg.on path { fill: #2448C2 !important; }
.rmf .rseg.on text { fill: #fff !important; }
.rmf .rseg.gv.on circle { fill: #FF5B1F !important; stroke: transparent !important; }
.rmf .rseg.gv.on text { fill: #0A1424 !important; }
.rmf .rdot { fill: var(--orange); }
.trust .pillar { display:flex; align-items:flex-end; justify-content:center; text-align:center; padding:22px 14px; border-radius:12px; font-family: var(--display); font-weight: 750; font-size: 32px; line-height:1.12; }
.dark .trust .pillar { background: var(--ink-3); }
#core [data-only].on { opacity: 1 !important; }
.risk12 .card { padding: 16px 22px; gap: 4px; transition: opacity .4s, border-color .4s; }
.risk12.dimmed .card:not(.on) { opacity: .3; }
"""

S.append(lobby("lobby", "Day 2 · Tuesday 3 November", "09:15 – 10:15",
    ["NIST AI Risk", "Management Framework"], "Principles and applications for research laboratories",
    """Holding screen for the first session of Day 2. Press → when the room is ready; the opening film plays and advances by itself."""))

S.append(video("open", "media/opener.mp4", "media/opener.jpg",
    """Opening film, about 13 seconds: the 40,000-molecule counter from Urbina et al., then the four AI RMF verbs."""))

S.append(section("title", f"""<canvas class="fx" data-fx="net"></canvas>
<p class="label" data-in="fade">Session 2 · NIST AI 100-1</p>
<div class="col" style="gap:0">
  <div class="mega" data-k="rise" style="font-size:170px">AI RISK</div>
  <div class="mega b" data-k="rise" data-d="200" style="font-size:170px">MANAGEMENT</div>
</div>
<p class="lead muted" data-in="up" data-d="600">Principles and applications for research laboratories</p>
<div class="spacer"></div>
<div class="col" data-in="fade" data-d="900" style="gap:4px"><p class="h3">{SPEAKER}</p><p class="small muted">{AFFIL}</p></div>""",
    "dark", "fade", "grid-bg", foot=EVENT, note="""Good morning. Yesterday we built a shared language for cyber risk. This morning we do the same for a newer kind of risk: AI systems that are now part of research workflows.

Plan: one hard example, why AI risk is different, the AI RMF itself (trustworthiness and the four functions), the Generative AI profile, AI as an attack target, and a worked laboratory case."""))

CSF = ["GV", "ID", "PR", "DE", "RS", "RC"]
AIR = ["GOVERN", "MAP", "MEASURE", "MANAGE"]
S.append(section("bridge", f"""<div class="g2" style="flex:1;gap:80px;align-items:center">
  <div class="col" style="gap:26px">
    <p class="label">Yesterday · CSF 2.0</p>
    <div class="h1" data-k="rise">Six functions for cyber risk</div>
    <div class="row" style="flex-wrap:wrap;gap:14px">{''.join(f'<span class="chip {"o" if c=="GV" else ""}" style="font-size:32px;padding:10px 18px" data-in="pop" data-d="{400+i*70}">{c}</span>' for i,c in enumerate(CSF))}</div>
  </div>
  <div class="col" style="gap:26px">
    <p class="label">Today · AI RMF 1.0</p>
    <div class="h1 b" data-k="rise" data-d="500">Four functions for AI risk</div>
    <div class="row" style="flex-wrap:wrap;gap:14px">{''.join(f'<span class="chip {"o" if c=="GOVERN" else "b"}" style="font-size:32px;padding:10px 18px" data-in="pop" data-d="{900+i*90}">{c}</span>' for i,c in enumerate(AIR))}</div>
  </div>
</div>
<p class="lead muted" data-in="up" data-d="1400">Both put governance first. The habits you learned yesterday transfer.</p>""",
    "dark", "zoom", "grid-bg", foot=FOOT, note="""A deliberate bridge. Both NIST frameworks start from governance. If a lab has done the CSF work, it already has the owners, the inventory habit and the review cycle that AI risk management needs."""))

S.append(section("megasyn", """<canvas class="fx" data-fx="net"></canvas>
<p class="label">Collaborations Pharmaceuticals · Spiez Convergence conference</p>
<div class="row" style="align-items:flex-end;gap:40px">
  <div class="num" style="font-size:300px" data-k="count" data-to="40000">40,000</div>
  <p class="h3 muted" style="padding-bottom:40px" data-in="fade" data-d="1200">molecules<br>in under six hours</p>
</div>
<p class="lead" data-k="words" data-d="400" style="max-width:1500px">A generative model built to steer drug candidates <b>away</b> from toxicity was asked to reward toxicity instead. Its output included VX and other known chemical warfare agents.</p>
<div class="spacer"></div>
<div class="row" style="gap:24px;align-items:center" data-step="1"><span class="chip o">Nothing was synthesised.</span><p class="body muted">The authors published to warn the drug-discovery community, not to show how.</p></div>
<p class="src" data-in="fade" data-d="1500">Urbina F, Lentzos F, Invernizzi C, Ekins S. Nat Mach Intell. 2022;4:189–191. doi:10.1038/s42256-022-00465-9</p>""",
    "dark", "iris", "grid-bg", foot=FOOT, note="""Urbina and colleagues, 2022. Their company builds machine-learning models that predict toxicity so that drug candidates avoid it. For a biosecurity conference they inverted one objective. In under six hours the model proposed 40,000 molecules scoring as highly toxic, including VX.

Click: they synthesised nothing, and they deliberately withheld details. The lesson for us is not about chemistry. It is that a capability built for good can be repurposed by changing one line, and that nobody in the lab had thought about it before."""))

USES = [
    ("Structure prediction", "Protein models feed experimental design", "Validity · dual use"),
    ("Image analysis", "Microscopy, viability and pathology scoring", "Drift · bias"),
    ("Language assistants", "Drafting protocols, code, reports and reviews", "Confabulation · data leakage"),
    ("Lab automation", "Liquid handlers and cloud labs driven by scripts", "Safety · security"),
    ("Sequence & molecule design", "Generative models propose candidates", "Dual use · IP"),
    ("Literature mining", "Screening papers and extracting data", "Confabulation · coverage"),
]
S.append(section("uses", f"""<p class="label">AI is already on the bench</p>
<h2 class="h2" data-k="words">Six places AI enters a life-science laboratory</h2>
<div class="g3" style="gap:22px;flex:1;align-content:center">{''.join(f'<div class="card" data-in="up" data-d="{400+i*90}"><p class="h3">{a}</p><p class="body muted">{b}</p><span class="chip" style="align-self:flex-start">{c}</span></div>' for i,(a,b,c) in enumerate(USES))}</div>""",
    "light", "wipe", foot=FOOT, note="""Ask the room: how many of you used one of these last week? Usually most hands go up for language assistants.

Each card names the risks we will meet again in the framework: confabulation, drift, bias, data leakage, dual use."""))

DIFF = ["Data changes; models drift.", "Behaviour is learned, not written.", "Failures are hard to predict.", "Errors scale instantly.", "The same tool can be used both ways."]
S.append(section("different", f"""<p class="label">Why AI risk is different · NIST AI 100-1, Appendix B</p>
<div class="col" style="gap:6px;flex:1;justify-content:center">{''.join(f'<div class="h1 {"o" if i==4 else ""}" style="font-size:96px" data-step="{i+1}" data-k="stretch">{t}</div>' for i,t in enumerate(DIFF))}</div>""",
    "dark", "zoom", "grid-bg", foot=FOOT, note="""Five lines, one click each, summarising NIST's own appendix on how AI risks differ from traditional software.

Traditional software does what its code says. A trained model does what its data taught it, and the data can change under it. That is why we need a framework that keeps measuring after deployment."""))

S.append(section("glance", """<p class="label">The framework at a glance</p>
<div class="row" style="gap:56px;flex:1">
  <div class="col" style="gap:20px;width:760px;flex:none">
    <div class="h1" data-k="rise">AI RMF 1.0</div>
    <p class="lead">NIST AI 100-1, released <b>26 January 2023</b>. Voluntary, rights-preserving, not tied to any sector or use case.</p>
    <div class="g2" style="gap:16px;margin-top:8px">
      <div class="card" data-in="up" data-d="500"><p class="k">PART 1</p><p class="body">Framing AI risk and the characteristics of trustworthy AI</p></div>
      <div class="card" data-in="up" data-d="650"><p class="k">PART 2</p><p class="body">The Core: four functions, and how to build profiles</p></div>
    </div>
  </div>
  <div class="col grow" style="gap:0">
    <div class="sev md" style="padding:16px 0 16px 24px" data-in="right" data-d="400"><p class="label muted" style="color:var(--mute-l)">Jan 2023</p><p class="body"><b>AI RMF 1.0</b> and its companion <b>Playbook</b></p></div>
    <div class="sev md" style="padding:16px 0 16px 24px" data-in="right" data-d="550"><p class="label muted" style="color:var(--mute-l)">Jul 2024</p><p class="body"><b>Generative AI Profile</b>, NIST AI 600-1</p></div>
    <div class="sev md" style="padding:16px 0 16px 24px" data-in="right" data-d="700"><p class="label muted" style="color:var(--mute-l)">Mar 2025</p><p class="body"><b>Adversarial ML taxonomy</b>, NIST AI 100-2 E2025</p></div>
    <div class="sev md" style="padding:16px 0 16px 24px" data-in="right" data-d="850"><p class="label muted" style="color:var(--mute-l)">Dec 2025</p><p class="body"><b>Cyber AI Profile</b>, NIST IR 8596 (preliminary draft)</p></div>
    <div class="sev hi" style="padding:16px 0 16px 24px" data-in="right" data-d="1000"><p class="label">2026</p><p class="body">NIST states AI RMF 1.0 <b>is being revised</b>; a critical-infrastructure profile concept note followed in April.</p></div>
  </div>
</div>""", "light", "push", foot=FOOT, note="""The essentials. Version 1.0 since January 2023, a Playbook with suggested actions for every subcategory, and a growing family of profiles.

Be explicit about status: NIST's page now says version 1.0 is being revised as part of the U.S. AI Action Plan. What you learn today, the functions and the trustworthiness characteristics, is expected to carry over, but check for a new version before you write institutional policy."""))

S.append(section("trust", """<p class="label">Characteristics of trustworthy AI</p>
<div class="row" style="gap:20px;flex:1;align-items:stretch">
  <div class="col grow" style="gap:20px">
    <div class="g5 trust" style="flex:1;gap:16px">
      <div class="pillar" data-step="2">Safe</div>
      <div class="pillar" data-step="2">Secure &amp; Resilient</div>
      <div class="pillar" data-step="2">Explainable &amp; Interpretable</div>
      <div class="pillar" data-step="2">Privacy-Enhanced</div>
      <div class="pillar" data-step="2">Fair, with Harmful Bias Managed</div>
    </div>
    <div class="card solid" data-step="1" style="align-items:center;padding:30px"><p class="h2" style="font-size:56px">Valid &amp; Reliable</p><p class="small" style="opacity:.8">the base every other characteristic stands on</p></div>
  </div>
  <div class="card" data-step="3" style="width:220px;flex:none;justify-content:center;align-items:center;background:var(--blue);border-color:var(--blue);color:#fff"><p class="h3" style="writing-mode:vertical-rl;transform:rotate(180deg);font-size:46px">Accountable &amp; Transparent</p></div>
</div>
<p class="body muted" data-in="fade" data-d="400">Seven characteristics. Trade-offs between them are expected and must be decided, not ignored.</p>""",
    "dark", "rise", "grid-bg", foot=FOOT, note="""Build the figure in three clicks, as NIST draws it. First the foundation, valid and reliable: a model that is wrong is not made trustworthy by anything else. Then the five pillars. Then accountability and transparency, which run alongside all of them.

Example of a trade-off: privacy enhancement can reduce accuracy, and explainability can cost performance. The framework asks you to make those trade-offs consciously."""))

S.append(section("core", f"""<span data-step="1" hidden></span><span data-step="2" hidden></span><span data-step="3" hidden></span><span data-step="4" hidden></span>
<div class="row" style="flex:1;align-items:center;gap:90px">
  <div class="rmf" id="rmf-core" style="width:760px;height:760px;flex:none">{rmf_svg("rc")}</div>
  <div class="grow" style="position:relative;height:640px">
    <div class="col abs" data-only="0" style="inset:0;gap:18px;justify-content:center;opacity:0;transition:opacity .45s"><p class="label">The AI RMF Core</p><div class="h1">Four functions</div><p class="lead muted">GOVERN runs through everything. MAP, MEASURE and MANAGE repeat across the AI lifecycle.</p></div>
    <div class="col abs" data-only="1" style="inset:0;gap:18px;justify-content:center;opacity:0;transition:opacity .45s"><span class="chip o" style="align-self:flex-start">6 categories</span><div class="h1" style="font-size:104px">GOVERN</div><p class="lead">A culture of risk management is cultivated and present.</p></div>
    <div class="col abs" data-only="2" style="inset:0;gap:18px;justify-content:center;opacity:0;transition:opacity .45s"><span class="chip b" style="align-self:flex-start">5 categories</span><div class="h1" style="font-size:104px">MAP</div><p class="lead">Context is recognized and risks related to context are identified.</p></div>
    <div class="col abs" data-only="3" style="inset:0;gap:18px;justify-content:center;opacity:0;transition:opacity .45s"><span class="chip b" style="align-self:flex-start">4 categories</span><div class="h1" style="font-size:104px">MEASURE</div><p class="lead">Identified risks are assessed, analyzed, or tracked.</p></div>
    <div class="col abs" data-only="4" style="inset:0;gap:18px;justify-content:center;opacity:0;transition:opacity .45s"><span class="chip b" style="align-self:flex-start">4 categories</span><div class="h1" style="font-size:104px">MANAGE</div><p class="lead">Risks are prioritized and acted upon based on a projected impact.</p></div>
  </div>
</div>""", "dark", "morph", "grid-bg", attrs='data-hook="rmfcore"', foot=FOOT, note="""Walk the four functions, one click each, with NIST's one-line definitions. GOVERN is cross-cutting; the other three form a cycle you repeat whenever a system, its data or its use changes.

After MANAGE, the next slides zoom into each function with laboratory questions."""))

FN = [
    ("GOVERN", "Function 1 · cross-cutting", "A culture of risk management is cultivated and present.",
     ["Is there a written policy on which AI tools may touch patient, client or genomic data?",
      "Who approves a new AI tool in the lab, and who is accountable when it fails?",
      "Do we keep an inventory of AI systems in use? (GOVERN 1.6 asks for exactly this.)",
      "Are third-party models and services covered by our supplier rules?"],
     "Start with a one-page AI use policy and a register. Most labs have neither.",
     """GOVERN in a laboratory is mostly about ownership and policy. The inventory point is GOVERN 1.6 in the framework: mechanisms to inventory AI systems, resourced according to risk.

A one-page policy plus a register is a realistic first step for any department represented here."""),
    ("MAP", "Function 2", "Context is recognized and risks related to context are identified.",
     ["What exactly is the system for, and what is it not for?",
      "Who uses it, on which data, and who is affected by its outputs?",
      "Could the capability be misused, here or by others?",
      "Which laws, ethics approvals and client contracts apply?"],
     "Write the intended use down before the first run. Misuse is defined against it.",
     """MAP is about context. The single most useful artefact is a short intended-use statement. Without it, you cannot say when a use has gone beyond what was approved.

Dual-use belongs here: the MegaSyn example was a mapping failure, nobody had asked how the model could be turned around."""),
    ("MEASURE", "Function 3", "Identified risks are assessed, analyzed, or tracked.",
     ["Was performance checked on our own samples, not only the vendor’s benchmark?",
      "How do we detect drift when reagents, instruments or staining change?",
      "Has anyone tried to make it fail on purpose (red-teaming)?",
      "Are errors logged and reviewed, with a human able to override?"],
     "Validate locally, then keep measuring. A model validated once is validated for the past.",
     """MEASURE is where scientists feel at home: validation, error rates, controls. The point to stress is that measurement continues after deployment, because data and conditions change.

Red-teaming in a lab can be simple: give the tool deliberately difficult or out-of-scope inputs and record what happens."""),
    ("MANAGE", "Function 4", "Risks are prioritized and acted upon based on a projected impact.",
     ["Deploy, restrict, or do not deploy: who decides, on what evidence?",
      "What is the response plan when the tool produces harmful or wrong output?",
      "How are vendor model updates tested before they reach the bench?",
      "When is a system retired, and what happens to its data?"],
     "Treat a silent model update like a change of reagent lot: test before use.",
     """MANAGE turns measurements into decisions and keeps them current. Vendor updates are a practical risk: a cloud model can change overnight without notice.

The reagent-lot analogy usually lands well with laboratory scientists."""),
]
for i, (name, eye, d, qs, lens, note) in enumerate(FN):
    qhtml = "".join(f'<div class="card" data-in="up" data-d="{450+j*90}" style="padding:24px 28px"><p class="body" style="font-size:29px">{q}</p></div>' for j, q in enumerate(qs))
    S.append(section(f"fn-{name.lower()}", f"""<div class="rmf abs" style="right:112px;top:84px;width:280px;height:280px">{rmf_svg("m" + name.lower(), name)}</div>
<div class="col" style="gap:12px;max-width:1240px">
  <p class="label">{eye}</p>
  <div class="h1" data-k="stretch">{name}</div>
  <p class="lead">{d}</p>
</div>
<p class="label muted" style="color:var(--mute-l)">Questions for a research laboratory</p>
<div class="g2" style="gap:16px">{qhtml}</div>
<div class="spacer"></div>
<div class="card solid" data-in="up" data-d="900" style="flex-direction:row;align-items:center;gap:30px;padding:26px 34px"><p class="label" style="color:inherit;flex:none;opacity:.8">Start here</p><p class="body">{lens}</p></div>""",
        "light", "zoom", attrs=f'data-zoom="[data-seg={name}]"', foot=FOOT, note=note))

RISKS = [("CBRN Information or Capabilities", 1), ("Confabulation", 1), ("Dangerous, Violent, or Hateful Content", 0), ("Data Privacy", 1),
         ("Environmental Impacts", 0), ("Harmful Bias and Homogenization", 0), ("Human-AI Configuration", 1), ("Information Integrity", 1),
         ("Information Security", 1), ("Intellectual Property", 1), ("Obscene, Degrading, and/or Abusive Content", 0), ("Value Chain and Component Integration", 1)]
S.append(section("genai", f"""<p class="label">Generative AI Profile · NIST AI 600-1 · July 2024</p>
<h2 class="h2" data-k="words">Twelve risks unique to or worsened by generative AI</h2>
<div class="g4 risk12" style="gap:14px" data-hook-target>{''.join(f'<div class="card{" hot" if hot else ""}" data-in="pop" data-d="{300+i*50}" {"data-on=1" if hot else ""}><p class="k">{i+1:02d}</p><p class="body" style="font-size:28px;line-height:1.25">{n}</p></div>' for i,(n,hot) in enumerate(RISKS))}</div>
<p class="body muted" data-step="1">Highlighted: the eight that matter most in a research laboratory.</p>""",
    "light", "rise", attrs='data-hook="genai"', foot=FOOT, note="""The Generative AI Profile lists twelve risks. Click once to highlight the eight most relevant to us: CBRN information, confabulation, data privacy, human-AI configuration (over-reliance), information integrity, information security, intellectual property, and the value chain, meaning the third-party models and plug-ins you build on.

The first one, CBRN information or capabilities, is the one this workshop exists for."""))

S.append(section("confab", """<div class="spacer"></div>
<p class="label">Confabulation</p>
<div class="mega" style="font-size:150px" data-k="rise">A fluent answer</div>
<div class="mega o" style="font-size:150px" data-k="rise" data-d="400">is not a verified one.</div>
<div class="g3" style="margin-top:48px">
  <div class="card" data-step="1"><p class="k">REFERENCES</p><p class="body">Plausible citations with invented authors, journals or DOIs</p></div>
  <div class="card" data-step="2"><p class="k">PROTOCOLS</p><p class="body">Concentrations, incubation times or biosafety levels stated with confidence and no source</p></div>
  <div class="card solid" data-step="3"><p class="k" style="color:inherit">LAB RULE</p><p class="body">Every AI-assisted citation is DOI-checked; every protocol step is checked against the SOP or the primary source.</p></div>
</div>
<div class="spacer"></div>""", "dark", "iris", "grid-bg", foot=FOOT, note="""Confabulation is NIST's term for what people call hallucination. In research it shows up as fake references and as invented protocol parameters.

The lab rule on the last card is simple and enforceable. It also protects research integrity, which is a cyberbiosecurity outcome in its own right."""))

ATT = [("Data poisoning", "Corrupt the training or reference data so the model learns the wrong thing"),
       ("Prompt injection", "Hide instructions in a document or web page the assistant reads"),
       ("Supply chain", "Tampered model weights, packages or plug-ins from third parties"),
       ("Privacy attacks", "Infer or extract sensitive training data, such as patient records")]
S.append(section("target", f"""<p class="label">AI as the target · NIST AI 100-2 E2025, adversarial ML taxonomy</p>
<h2 class="h2" data-k="words">The model is also an asset that can be attacked</h2>
<div class="g4" style="gap:20px">{''.join(f'<div class="card" data-in="up" data-d="{400+i*120}" style="min-height:300px"><p class="num {"o" if i==1 else "b"}" style="font-size:96px">{i+1}</p><p class="h3">{a}</p><p class="body muted">{b}</p></div>' for i,(a,b) in enumerate(ATT))}</div>
<p class="body muted" data-in="fade" data-d="1000">These map straight back to yesterday’s CSF functions: PR.DS for data, GV.SC for the supply chain, DE.AE for spotting abuse.</p>""",
    "light", "push", foot=FOOT, note="""So far the AI was the source of risk. Here it is the target. NIST's adversarial machine learning taxonomy names the classes of attack; four are enough for a lab audience.

Prompt injection deserves a minute: an assistant that reads a supplier's PDF or a web page can be instructed by text hidden inside it. Anyone connecting an assistant to email or files should know this."""))

S.append(section("cyberai", """<canvas class="fx" data-fx="rings"></canvas>
<p class="label">Where the two frameworks meet · NIST IR 8596 · preliminary draft, Dec 2025</p>
<h2 class="h2" data-k="words" style="max-width:1300px">The Cyber AI Profile applies CSF 2.0 outcomes to AI</h2>
<div class="g3" style="gap:26px;max-width:1500px;margin-top:20px">
  <div class="card" data-step="1"><p class="num b" style="font-size:110px">S</p><p class="h3">Secure</p><p class="body muted">Securing AI system components</p></div>
  <div class="card" data-step="2"><p class="num b" style="font-size:110px">D</p><p class="h3">Defend</p><p class="body muted">Using AI to strengthen cyber defence</p></div>
  <div class="card" data-step="3"><p class="num o" style="font-size:110px">T</p><p class="h3">Thwart</p><p class="body muted">Countering AI-enabled attacks</p></div>
</div>
<p class="body muted" data-in="fade" data-d="800">Comments closed 30 January 2026; an initial public draft is expected next.</p>""", "dark", "zoom", "grid-bg", foot=FOOT, note="""This is the bridge we promised yesterday. The Cyber AI Profile is a CSF 2.0 community profile for AI, with three focus areas: secure, defend, thwart.

It is a preliminary draft, so cite it as such. For an institution, the practical message is that you do not need a separate AI security programme; you extend the CSF programme you already have."""))

ROWS = [("GOVERN", "Owner named; tool added to the AI register; use limited to research images, no patient identifiers"),
        ("MAP", "Intended use: viability scoring of fixed-time MTT and live/dead images; not for regulatory submissions"),
        ("MEASURE", "Compared with two blinded human scorers on 300 local images; re-checked whenever stain lot or microscope changes"),
        ("MANAGE", "Scores below a confidence threshold go to a human; vendor updates tested on a frozen image set before use")]
S.append(section("case", f"""<p class="label">Worked case · illustrative</p>
<h2 class="h2" data-k="words">A cytotoxicity lab adopts an AI image classifier</h2>
<table class="t" style="margin-top:8px"><tr><th style="width:260px">Function</th><th>What the lab actually does</th></tr>
{''.join(f'<tr data-step="{i+1}"><td><span class="chip {"o" if f=="GOVERN" else "b"}">{f}</span></td><td style="font-size:30px">{t}</td></tr>' for i,(f,t) in enumerate(ROWS))}
</table>""", "light", "wipe", foot=FOOT, note="""An illustrative case from our own kind of work: a pharmacology lab that scores cell viability images with an AI classifier. One click per function.

Note how concrete each line is. That is the test of a good AI RMF implementation: each function produces a decision or a record someone can check. The numbers here are an example design, not a real study."""))

REG = [("Image classifier", "Viability scoring", "Microscopy images", "Lab head", "Medium", "Low-confidence cases", "Each lot change"),
       ("LLM assistant", "Drafting SOP text", "No client or patient data", "Biosafety officer", "Medium", "Every step vs. source", "Quarterly"),
       ("Sequence screening", "Order checks", "Synthetic DNA orders", "Core facility manager", "High", "All flagged hits", "Monthly")]
S.append(section("register", f"""<p class="label">A minimal AI register · example rows</p>
<h2 class="h2" data-k="words">One table makes GOVERN real</h2>
<table class="t" style="font-size:26px"><tr><th>System</th><th>Use</th><th>Data</th><th>Owner</th><th>Risk</th><th>Human check</th><th>Review</th></tr>
{''.join(f'<tr data-in="up" data-d="{400+i*150}">' + ''.join(f'<td>{c if k!=4 else f"<span class=chip>{c}</span>" if c!="High" else f"<span class=\'chip o\'>{c}</span>"}</td>' for k,c in enumerate(r)) + '</tr>' for i,r in enumerate(REG))}
</table>
<p class="body muted" data-in="fade" data-d="1000">Seven columns, one row per AI system. Start it this week; refine it at the next lab meeting.</p>""", "light", "morph", foot=FOOT, note="""Example rows only. The register is the smallest artefact that makes GOVERN real: it names the system, its purpose, its data, its owner, a risk level, where a human checks, and when it is reviewed.

Encourage participants to start one for their own group this week."""))

QS = ["Who owns it?", "What data does it see?", "What happens when it is wrong?", "Could it be turned around?", "How will we know it changed?"]
S.append(section("five", f"""<canvas class="fx" data-fx="helix" data-x="1600"></canvas>
<p class="label">Before any AI tool enters the lab</p>
<div class="col" style="gap:4px;flex:1;justify-content:center">{''.join(f'<div class="h1 {"o" if i==3 else ""}" style="font-size:100px" data-step="{i+1}" data-k="rise">{q}</div>' for i,q in enumerate(QS))}</div>""",
    "dark", "zoom", "grid-bg", foot=FOOT, note="""Five questions, one per click. They map to the functions: ownership is GOVERN, data and misuse are MAP, being wrong and changing are MEASURE and MANAGE.

If participants remember only one slide from this session, this should be it."""))

S.append(section("next", """<p class="label">Where this goes next today</p>
<div class="col" style="gap:20px;margin-top:20px">
  <div class="row card" data-in="left" data-d="200" style="flex-direction:row;align-items:center;gap:40px"><p class="num b tab" style="font-size:72px;width:260px">10:30</p><div class="col" style="gap:6px"><p class="h3">Artificial Intelligence in Life Sciences</p><p class="body muted">Opportunities, risks and responsible use · Prof. Dr. Gökçe Merey</p></div></div>
  <div class="row card" data-in="left" data-d="350" style="flex-direction:row;align-items:center;gap:40px"><p class="num b tab" style="font-size:72px;width:260px">11:30</p><div class="col" style="gap:6px"><p class="h3">Institutional Cybersecurity Infrastructure</p><p class="body muted">A practical case study</p></div></div>
  <div class="row card hot" data-in="left" data-d="500" style="flex-direction:row;align-items:center;gap:40px"><p class="num o tab" style="font-size:72px;width:260px">14:30</p><div class="col" style="gap:6px"><p class="h3">Hands-on: apply CSF 2.0 to a biotechnology lab</p><p class="body muted">Your lab’s AI tools belong in that profile too</p></div></div>
</div>""", "light", "rise", foot=FOOT, note="""Hand over to Prof. Merey's session on AI in the life sciences, which takes the applications side. Remind groups that the afternoon exercise includes AI tools in the scenario."""))

S.append(sources("refs", [
    "Tabassi E. <i>Artificial Intelligence Risk Management Framework (AI RMF 1.0)</i>. NIST AI 100-1; 2023. doi:10.6028/NIST.AI.100-1",
    "NIST. <i>Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile</i>. NIST AI 600-1; 2024. doi:10.6028/NIST.AI.600-1",
    "Vassilev A, et al. <i>Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations</i>. NIST AI 100-2 E2025; 2025. doi:10.6028/NIST.AI.100-2e2025",
    "NIST. <i>Cybersecurity Framework Profile for Artificial Intelligence (Cyber AI Profile)</i>. NIST IR 8596, initial preliminary draft; 16 Dec 2025.",
    "Urbina F, Lentzos F, Invernizzi C, Ekins S. Dual use of artificial-intelligence-powered drug discovery. <i>Nat Mach Intell</i>. 2022;4(3):189–191. doi:10.1038/s42256-022-00465-9",
    "NIST. AI Risk Management Framework (web page, status of revision and profiles); accessed 21 Oct 2026. nist.gov/itl/ai-risk-management-framework",
    "National Institute of Standards and Technology. <i>The NIST Cybersecurity Framework (CSF) 2.0</i>. NIST CSWP 29; 2024. doi:10.6028/NIST.CSWP.29",
], FOOT))

S.append(thanks("thanks", "Thank you.", "Questions on AI risk in the laboratory", "Take questions. If someone asks whether a specific AI tool is allowed, route it to the five questions slide and the register.", FOOT))

HOOKS = """window.DeckHooks = {
  rmfcore(s, step) {
    const map = {1:'GOVERN',2:'MAP',3:'MEASURE',4:'MANAGE'};
    s.querySelectorAll('.rseg').forEach(g => g.classList.toggle('on', step >= 5 ? false : map[step] === g.dataset.rk));
  },
  genai(s, step) { const g = s.querySelector('.risk12'); if (g) g.classList.toggle('dimmed', step >= 1); }
};"""

if __name__ == "__main__":
    n = build("/home/claude/corum/dist/d2/index.html", "AI RMF for Laboratories", 60, FOOT, S, extra_css=CSS, extra_js=HOOKS)
    print("slides", n)
