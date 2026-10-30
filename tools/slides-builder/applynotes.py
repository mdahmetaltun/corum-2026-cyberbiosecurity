import re,sys,html,json
root,mod=sys.argv[1],sys.argv[2]
g={};exec(open(mod).read(),g);N=g["N"]
order=json.load(open(f"{root}/project/deck.json"))["order"]
miss=[i for i in order if i not in N]; extra=[k for k in N if k not in order]
assert not miss and not extra,(miss,extra)
for sid in order:
    p=f"{root}/project/slides/{sid}.html"; s=open(p).read()
    t=N[sid].strip().replace("'","’")
    assert len(t)<=4000,(sid,len(t))
    new,n=re.subn(r"<aside>.*?</aside>",lambda m:"<aside>"+html.escape(t,quote=False)+"</aside>",s,flags=re.S)
    assert n==1,(sid,n); open(p,"w").write(new)
print("ok",len(order),"max",max(len(N[k]) for k in N),"words",sum(len(N[k].split()) for k in N))
