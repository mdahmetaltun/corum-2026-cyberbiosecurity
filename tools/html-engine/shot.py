import asyncio, sys, os
from playwright.async_api import async_playwright
deck = sys.argv[1]; only = sys.argv[2:] 
def s_is_video(i): return False
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1920,"height":1080})
        errs=[]
        pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
        html = open(f"/home/claude/corum/dist/{deck}/index.html").read()
        wrapped = "<!doctype html><html><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'></head><body>"+html+"</body></html>"
        open(f"/home/claude/corum/dist/{deck}/_test.html","w").write(wrapped)
        await pg.goto(f"file:///home/claude/corum/dist/{deck}/_test.html")
        await pg.wait_for_timeout(800)
        n = await pg.evaluate("document.querySelectorAll('#stage > section').length")
        os.makedirs(f"/home/claude/corum/shots/{deck}", exist_ok=True)
        rng = [int(x) for x in only] if only else range(n)
        for i in rng:
            await pg.evaluate(f"Deck.go({i})")
            await pg.wait_for_timeout(1700)
            ms = await pg.evaluate("Math.max(0,...[...document.querySelectorAll('#stage > section')[Deck.index].querySelectorAll('[data-step]')].map(e=>+e.dataset.step))")
            for k in range(ms):
                await pg.evaluate("Deck.next()"); await pg.wait_for_timeout(900)
            await pg.wait_for_timeout(1200)
            ov = await pg.evaluate("""(()=>{const s=document.querySelectorAll('#stage > section')[Deck.index];const st=document.getElementById('stage').getBoundingClientRect();const sc=st.width/1920;const bad=[];s.querySelectorAll('*').forEach(e=>{if(e.closest('.foot,.fx,.notes,svg,.abs')||e.closest('[hidden]'))return;const r=e.getBoundingClientRect();if(!r.height)return;const b=(r.bottom-st.top)/sc, rt=(r.right-st.left)/sc;if(b>1000||rt>1800)bad.push((e.className||e.tagName)+':'+Math.round(b)+'/'+Math.round(rt))});return bad.slice(0,3)})()""")
            if ov and not s_is_video(i): print("OVERFLOW", i, ov)
            await pg.screenshot(path=f"/home/claude/corum/shots/{deck}/{i:02d}.jpg", type="jpeg", quality=70)
        print("errors:", errs[:10]); print("n", n)
        await b.close()
asyncio.run(main())
