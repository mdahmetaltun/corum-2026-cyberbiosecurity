"""v2 decks: vivid per-deck theme + live 3D / kinetic elements. Original generators (d1–d4) are reused untouched;
illustrations are swapped for live embeds where a 3D form fits, kinetic interstitials and count-up numerals are added,
then every original palette colour is mapped to the deck's theme.
usage: python3 build_v2.py <deck: csf|ai|kase|lab> <outroot> <video_still_blob> <video_clip_blob>"""
import importlib, json, re, sys
import kit
from anim import emb

ORIG = {  # role -> original hex
    "ink": "#13294B", "paper": "#F7F9FC", "text": "#1F2D45", "body2": "#3A4A63", "mute": "#5A6A82",
    "primary": "#1662E8", "plight": "#5B9BFF", "pale": "#D6E6FF", "pale2": "#E8F0FF",
    "second": "#00C2B2", "tealt": "#00968A", "mint": "#7FD1C9", "aqua": "#3EDBCB",
    "hot": "#FF7A1A", "hott": "#EA5A0C", "gold": "#FFB547", "sand": "#F0C27A", "green": "#22C55E",
    "grey": "#DCE3EC", "cream": "#F5F3EE", "sky": "#B9C7DA", "ink2": "#1B3866", "ink3": "#36578A",
    "glow": "#24507F", "glowb": "#0E7C7B", "hottint": "#FFF3EA", "ntint": "#EEF2F7", "track": "#2E4A72", "dot": "#E3E8EF",
}
THEMES = {
    "csf": dict(name="Electric Cobalt", ink="#0A1640", paper="#F5F7FF", text="#141F45", body2="#36406A", mute="#5B6690",
                primary="#2F5BF0", plight="#6F8EFF", pale="#D9E2FF", pale2="#E8EDFF", second="#7C5CFF", tealt="#2340C8",
                mint="#C8F53A", aqua="#DDFB7A", hot="#FF5C4D", hott="#C2362B", gold="#C8F53A", sand="#C8F53A", green="#C8F53A",
                grey="#D5DCF7", cream="#F4F6FF", sky="#A9B6E8", ink2="#16286B", ink3="#2E4A9E", glow="#2F5BF0", glowb="#C8F53A",
                hottint="#FFE9E6", ntint="#EDF0FB", track="#2E4A9E", dot="#DDE3F7",
                pal=dict(a="#2F5BF0", b="#6F8EFF", c="#FF5C4D", d="#C8F53A", fg="#F4F6FF")),
    "ai": dict(name="Ultraviolet", ink="#1A0B3D", paper="#FAF7FF", text="#1E1240", body2="#3B2B6B", mute="#625492",
               primary="#7B3DFF", plight="#A27BFF", pale="#E7DCFF", pale2="#F1EBFF", second="#19B8D6", tealt="#5B21D6",
               mint="#19D3F0", aqua="#7CE7F7", hot="#FF2E93", hott="#C2185B", gold="#19D3F0", sand="#19D3F0", green="#19D3F0",
               grey="#E2D8F7", cream="#F7F3FF", sky="#C4B8EC", ink2="#2B1466", ink3="#4A2F8F", glow="#7B3DFF", glowb="#19D3F0",
               hottint="#FFE6F2", ntint="#F0ECF8", track="#4A2F8F", dot="#E6E0F2",
               pal=dict(a="#7B3DFF", b="#A27BFF", c="#FF2E93", d="#19D3F0", fg="#F7F3FF")),
    "kase": dict(name="Signal", ink="#0B2530", paper="#F6F9F9", text="#10262E", body2="#2F4A52", mute="#4A6670",
                 primary="#0E7C86", plight="#3BB5C4", pale="#D3EEF0", pale2="#E6F5F6", second="#12C2B0", tealt="#0A6F66",
                 mint="#FFC233", aqua="#5EDBCF", hot="#FF6A13", hott="#C2410C", gold="#FFC233", sand="#FFC233", green="#12C2B0",
                 grey="#D6E3E3", cream="#F2F7F6", sky="#A9C6C8", ink2="#123A47", ink3="#2A5A66", glow="#FF6A13", glowb="#12C2B0",
                 hottint="#FFEDE3", ntint="#EAF1F1", track="#2A5A66", dot="#DCE6E6",
                 pal=dict(a="#12C2B0", b="#5EDBCF", c="#FF6A13", d="#FFC233", fg="#F2F7F6")),
    "lab": dict(name="Bio Lime", ink="#0D3328", paper="#F7FBF3", text="#12301F", body2="#3D5A4E", mute="#4F6B60",
                primary="#15803D", plight="#4CBF6A", pale="#DDF3D5", pale2="#ECF8E6", second="#2DD4BF", tealt="#166534",
                mint="#A3E635", aqua="#7EEAD8", hot="#FF8A1F", hott="#C2410C", gold="#A3E635", sand="#A3E635", green="#A3E635",
                grey="#DCE9D5", cream="#F3FAF0", sky="#A7C9B8", ink2="#164A3A", ink3="#2C6A55", glow="#2DD4BF", glowb="#A3E635",
                hottint="#FFF0E0", ntint="#EEF5EA", track="#2C6A55", dot="#E1ECDB",
                pal=dict(a="#2DD4BF", b="#7EEAD8", c="#FF8A1F", d="#A3E635", fg="#F3FAF0")),
}
MODS = {"csf": "d1", "ai": "d2", "kase": "d3", "lab": "d4"}
TITLES = {"csf": "CSF 2.0 · Core Functions & Profiles · v2", "ai": "AI RMF · Research Laboratories · v2",
          "kase": "Institutional Cybersecurity Infrastructure · v2", "lab": "HelixLab CSF Exercise · v2"}

# illustration name -> live element (others keep their animated SVG)
LIVE = {"csf": {"shield": "shield", "radar": "radar", "backup": "cubes", "network": "globe", "molecule": "molecule", "helix": "helix", "layers": "cubes"},
        "ai": {"neural": "globe", "ai": "orbit", "molecule": "molecule", "network": "globe", "lock": "shield", "shield": "shield"},
        "kase": {"server": "cubes", "layers": "cubes", "radar": "radar", "lock": "shield", "shield": "shield", "backup": "cubes", "network": "globe"},
        "lab": {"helix": "helix", "target": "radar", "people": "orbit", "shield": "shield", "scan": "radar"}}

# kinetic interstitials: deck -> (insert before id, slide id, eyebrow, [(word, role or None)], notes)
KINETIC = {
    "csf": ("fivesix", "k-six", "CSF 1.1 → CSF 2.0", [("IDENTIFY · PROTECT", None), ("DETECT · RESPOND", None), ("RECOVER", None), ("+ GOVERN", "hot")],
            "Kinetic interstitial. Let the five old functions land, then GOVERN arrives as the sixth. Advance to the wheel."),
    "ai": ("core", "k-core", "The AI RMF Core", [("GOVERN.", "hot"), ("MAP.", None), ("MEASURE.", None), ("MANAGE.", "mint")],
           "Kinetic interstitial: the four verbs, one per beat. Then the full Core with definitions."),
    "kase": ("arch", "k-build", "Phase 2", [("ASSESS.", None), ("BUILD.", "mint"), ("TRAIN.", None), ("REHEARSE.", "hot")],
             "Kinetic interstitial into Phase 2. Assessment is done; now build, train and rehearse."),
    "lab": ("clock", "k-go", "The exercise", [("1 LAB.", None), ("6 SEATS.", None), ("45 MINUTES.", "mint"), ("GO.", "hot")],
            "Kinetic interstitial before the clock starts. Read it aloud, then start the timer."),
}


def recolor(s, th):
    m = {ORIG[k].upper(): th[k] for k in ORIG}
    s = re.sub(r"#[0-9A-Fa-f]{6}\b", lambda x: m.get(x.group(0).upper(), x.group(0)), s)
    r, g, b = (int(th["ink"][i:i + 2], 16) for i in (1, 3, 5))
    return s.replace("rgba(19,41,75,", f"rgba({r},{g},{b},")


def main(deck, outroot, still, clip):
    th = THEMES[deck]
    pal = th["pal"]
    # live illustrations
    orig_illus = dict(kit.ILLUS)
    for nm, kind in LIVE[deck].items():
        def mk(kind=kind, nm=nm):
            def f(left=1480, top=48, w=360, h=236, **k):
                return emb(kind, left, top, w, h, pal, n=12, r=3)
            return f
        kit.ILLUS[nm] = mk()
    mod = importlib.import_module(MODS[deck])
    D = mod.D
    # kinetic interstitial slide
    before, sid, eyebrow, words, notes = KINETIC[deck]

    def kin(i, n, sid=sid, eyebrow=eyebrow, words=words, notes=notes):
        ws = [[w, th[r] if r else th["cream"]] for w, r in words]
        inner = kit.progress(i, n, True)
        inner += emb("particles", 0, 0, 1920, 1080, pal)
        inner += f'<p data-build-in="fade 1 auto" style="position:absolute;left:128px;top:150px;width:1400px;font-size:24px;letter-spacing:2px;text-transform:uppercase;font-weight:600;color:{kit.MINT}">{eyebrow}</p>'
        inner += emb("kinetic", 128, 220, 1664, 680, pal, words=ws, size=150, lh=1.12, gap=0.55, weight=900)
        inner += kit.footer(D.foot, i + 1, True)
        return kit.section(sid, inner, True, "push", notes)
    idx = [s for s, _ in D.slides].index(before)
    D.slides.insert(idx, (sid, kin))
    slides = D.render()
    kit.ILLUS.clear(); kit.ILLUS.update(orig_illus)

    out = []
    for s_id, h in slides:
        light = f"background:{kit.PAPER}" in h[:400]
        # count-up numerals
        if deck == "ai" and s_id == "megasyn":
            h = re.sub(r'<p data-build-in="pop 2 auto" style="[^"]*font-size:240px[^"]*">40,000</p>',
                       emb("counter", 128, 200, 1150, 250, pal, to=40000, size=230, fg=th["cream"]), h)
        if deck == "kase" and s_id == "change":
            h = re.sub(r'<p data-build-in="pop 2 auto" style="[^"]*font-size:250px[^"]*">192\.7</p>',
                       emb("counter", 128, 220, 700, 270, pal, to=192.7, dec=1, size=250, fg=th["cream"]), h)
        if deck == "csf" and s_id == "anatomy":
            for k, (v, role) in enumerate([(6, "cream"), (22, "mint"), (106, "sand")]):
                h = re.sub(rf'<p data-build-in="pop {k * 2 + 2} auto" style="[^"]*font-size:230px[^"]*">{v}</p>',
                           emb("counter", 128 + k * 580, 290, 460, 250, pal, to=v, size=230, align="center", fg=th[role], dur=1.2 + k * 0.4), h)
        if deck == "kase" and s_id == "telemetry":
            term = emb("terminal", 128, 740, 736, 170, pal, bg=th["ink"], fg="#FFFFFF", lines=[
                ["$ tail -f /var/log/lab-ot.log", th["sky"]], ["04:00:02 ntp   offset +0.003 s    OK", None],
                ["04:00:07 jump  vendor-seq  MFA   OK", th["mint"]], ["04:00:12 frz-3 temp -71 C      ALERT", th["hot"]]])
            h = h.replace("\n<aside>", "\n" + term + "\n<aside>", 1) if "\n<aside>" in h else h.replace("\n</section>", "\n" + term + "\n</section>")
        if deck == "kase" and s_id == "cover":
            h = re.sub(r'<svg id="ringsc".*?</svg>', emb("orbit", 1200, 230, 560, 560, pal), h, flags=re.S)
        if deck == "lab" and s_id in ("cover", "close"):
            h = re.sub(r'<svg aria-label="Animated DNA helix".*?</svg>',
                       emb("helix", 1228 if s_id == "cover" else 1360, 180 if s_id == "cover" else 200, 520, 640, pal, vert=True, n=13, r=6), h, flags=re.S)
        if s_id == "film":
            h = re.sub(r'src="/_blob/[0-9a-f]+" data-video="/_blob/[0-9a-f]+"', f'src="{still}" data-video="{clip}"', h)
        if light:  # embeds on light slides draw with the ink colour instead of the near-white
            h = h.replace(f'"fg": "{pal["fg"]}"', f'"fg": "{th["ink"]}"')
        out.append((s_id, recolor(h, th)))
    secs = {k: dict(v) for k, v in mod.SECTIONS.items()}
    kit.write_deck(outroot, TITLES[deck], secs, out)
    print("ok", deck, len(out))


if __name__ == "__main__":
    main(*sys.argv[1:5])
