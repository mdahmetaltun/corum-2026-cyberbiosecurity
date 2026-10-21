"""Render EN and TR versions; flag slides where any text element got taller/wider or escapes its parent box."""
import asyncio, json, os, sys
from playwright.async_api import async_playwright
import preview
JS = """(()=>{const o=[];document.querySelectorAll('.sl p,.sl h1,.sl h2,.sl h3,.sl li,.sl span,.sl b').forEach(e=>{const r=e.getBoundingClientRect();if(!r.height)return;
let par=e.parentElement,pr=par.getBoundingClientRect();
const esc=(r.right>pr.right+3||r.bottom>pr.bottom+3)&&par.className!=='sl'?1:0;
const clip=e.scrollWidth>e.clientWidth+3||e.scrollHeight>e.clientHeight+3?1:0;
o.push([Math.round(r.height),Math.round(r.width),esc,clip,(e.textContent||'').trim().slice(0,50),Math.round(r.right),Math.round(r.bottom)])});return o})()"""
async def grab(root, order):
    res = {}
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width":1920,"height":1080})
        for sid in order:
            sec = open(f"{root}/project/slides/{sid}.html").read()
            html = f"<!doctype html><html><head><meta charset='utf-8'><style>{preview.FONT_CSS} body{{margin:0}} p,h1,h2,h3,ul,ol{{margin:0}} ul,ol{{padding-left:1.2em}} .sl{{font-size:32px}} .sl *{{box-sizing:border-box}}</style></head><body>{preview.convert(sec)}</body></html>"
            await pg.set_content(html); await pg.wait_for_timeout(150)
            res[sid] = await pg.evaluate(JS)
        await b.close()
    return res
async def main(en, tr):
    order = json.load(open(f"{tr}/project/deck.json"))["order"]
    A = await grab(en, order); B = await grab(tr, order)
    for i, sid in enumerate(order):
        a, b = A[sid], B[sid]; issues = []
        for k, y in enumerate(b):
            x = a[k] if k < len(a) else None
            if y[2] and not (x and x[2]): issues.append("ESC " + y[4])
            if y[3] and not (x and x[3]): issues.append("CLIP " + y[4])
            if x and y[0] > x[0] + 6: issues.append(f"TALL {x[0]}->{y[0]} " + y[4])
            if y[5] > 1860 or y[6] > 1075: issues.append(f"EDGE {y[5]},{y[6]} " + y[4])
        print(sid, len(a), len(b)) if i<2 else None
        if issues: print(i + 1, sid, *issues[:6], sep="\n   ")
asyncio.run(main(sys.argv[1], sys.argv[2]))
