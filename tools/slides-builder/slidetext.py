import json,re,sys,html
sys.path.insert(0,'.')
import tr
root=sys.argv[1]
d=json.load(open(f"{root}/project/deck.json"))
for i,sid in enumerate(d["order"],1):
    s=open(f"{root}/project/slides/{sid}.html").read()
    notes=re.search(r"<aside>(.*?)</aside>",s,re.S)
    s2=re.sub(r"<aside>.*?</aside>","",s,flags=re.S)
    items=[]
    def fn(t):
        c=html.unescape(t).strip()
        if tr.want(c): items.append(c)
        return t
    tr.process(s2,fn)
    builds=len(re.findall(r'data-build-in=',s2))
    print(f"### {i}. {sid}  (build adımı: {builds}, geçiş: {re.search(r'data-transition=\"(\w+)\"',s).group(1)})")
    print(" | ".join(items))
    print("NOT:", (notes.group(1) if notes else "").replace("\n"," ")[:400])
    print()
