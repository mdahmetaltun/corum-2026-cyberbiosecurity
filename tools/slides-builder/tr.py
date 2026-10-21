"""Turkish localisation of the v2 Slides decks without touching layout/animation.

extract <src_project> <out.json>     -> list of unique translatable strings
apply   <src_project> <dst_project> <dict.json>  -> copies project with strings replaced
Only text nodes, aria-labels, <title>, kinetic words, terminal lines and deck.json
title/section descriptions are changed. Markup, styles, scripts are byte-identical otherwise.
"""
import json, os, re, shutil, sys, html

EMB = re.compile(r"(<x-embed\b[^>]*>)(.*?)(</x-embed>)", re.S)
PJS = re.compile(r"const P=(\{.*?\});function hx", re.S)
SKIP = re.compile(r"(<style\b.*?</style>|<script\b.*?</script>)", re.S)
TXT = re.compile(r">([^<>]+)<")
ARIA = re.compile(r'(aria-label|alt|title)="([^"]+)"')
LET = re.compile(r"[A-Za-z]{2,}")


def want(s):
    s = s.strip()
    if not LET.search(s):
        return False
    if re.fullmatch(r"(ID|PR|DE|RS|RC|GV)(\.[A-Z]{2})?(-\d+)?", s):
        return False
    if s.startswith("http") or re.fullmatch(r"(doi:|https?://)\S+", s):
        return False
    return True


def walk_plain(seg, fn):
    """apply fn to text nodes + attrs in a non-embed segment, skipping style/script."""
    parts = SKIP.split(seg)
    out = []
    for i, p in enumerate(parts):
        if i % 2 == 1:
            out.append(p)
            continue
        p = TXT.sub(lambda m: ">" + fn(m.group(1)) + "<", p)
        p = ARIA.sub(lambda m: f'{m.group(1)}="{fn(m.group(2))}"', p)
        out.append(p)
    return "".join(out)


def walk_embed(page, fn):
    m = PJS.search(page)
    if not m:
        return page
    P = json.loads(m.group(1))
    ch = False
    if "words" in P:
        P["words"] = [[fn(w), c] for w, c in P["words"]]; ch = True
    if "lines" in P:
        P["lines"] = [fn(l) if isinstance(l, str) else [fn(l[0])] + l[1:] for l in P["lines"]]; ch = True
    for k in ("label", "suffix", "prefix", "text", "pre", "suf"):
        if isinstance(P.get(k), str):
            P[k] = fn(P[k]); ch = True
    if not ch:
        return page
    return page[:m.start(1)] + json.dumps(P, ensure_ascii=False) + page[m.end(1):]


def process(s, fn):
    out, last = [], 0
    for m in EMB.finditer(s):
        out.append(walk_plain(s[last:m.start()], fn))
        out.append(m.group(1) + walk_embed(m.group(2), fn) + m.group(3))
        last = m.end()
    out.append(walk_plain(s[last:], fn))
    return "".join(out)


def strings(proj):
    seen = []
    def fn(t):
        core = html.unescape(t).strip()
        if want(core) and core not in seen:
            seen.append(core)
        return t
    for f in sorted(os.listdir(f"{proj}/slides")):
        process(open(f"{proj}/slides/{f}").read(), fn)
    d = json.load(open(f"{proj}/deck.json"))
    for v in [d["title"]] + [x["description"] for x in d.get("sections", {}).values()]:
        if v not in seen:
            seen.append(v)
    return seen


def apply(src, dst, tr, ov=None):
    miss = []
    def fn(t):
        core = html.unescape(t).strip()
        if not want(core):
            return t
        if core not in tr:
            miss.append(core); return t
        lead = t[:len(t) - len(t.lstrip())]; trail = t[len(t.rstrip()):]
        val = tr[core]
        esc = html.escape(val, quote=True) if ("&" in t or "<" in val or '"' in val) else val
        return lead + esc + trail
    if os.path.exists(dst):
        shutil.rmtree(dst)
    shutil.copytree(src, dst)
    for f in os.listdir(f"{dst}/slides"):
        p = f"{dst}/slides/{f}"
        new = process(open(p).read(), fn).replace("<section ", '<section lang="tr" ', 1).replace("toLocaleString('en-US'", "toLocaleString('tr-TR'")
        for o, n in (ov or {}).get(f[:-5], []):
            assert o in new, (f, o); new = new.replace(o, n)
        open(p, "w").write(new)
    d = json.load(open(f"{dst}/deck.json"))
    d["title"] = tr.get(d["title"], d["title"])
    for x in d.get("sections", {}).values():
        x["description"] = tr.get(x["description"], x["description"])
    json.dump(d, open(f"{dst}/deck.json", "w"), ensure_ascii=False)
    return sorted(set(miss))


def load(p):
    if p.endswith(".py"):
        g = {}; exec(open(p).read(), g)
        return {k: v.replace("'", "\u2019") for k, v in g["T"].items()}, g.get("OV")
    return json.load(open(p)), None


if __name__ == "__main__":
    if sys.argv[1] == "extract":
        pass
    if sys.argv[1] == "extract":
        json.dump(strings(sys.argv[2]), open(sys.argv[3], "w"), ensure_ascii=False, indent=0)
        print(len(json.load(open(sys.argv[3]))))
    else:
        m = apply(sys.argv[2], sys.argv[3], *load(sys.argv[4]))
        print("missing", len(m)); [print(" ", x) for x in m]
