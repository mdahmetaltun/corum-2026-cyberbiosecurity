"""Small live 3D / kinetic elements for Slides x-embeds (sandboxed, scripts allowed, no network, system fonts).
Every element: emb(kind, left, top, w, h, pal, **opts) -> '<x-embed ...>page</x-embed>' (kept well under 16 KB)."""
import json

HEAD = ("<!doctype html><html><head><meta charset='utf-8'><style>html,body{margin:0;height:100%;background:transparent;overflow:hidden}"
        "canvas{display:block;width:100%;height:100%}</style></head><body><canvas id='c'></canvas><script>")
BOOT = ("const C=document.getElementById('c'),X=C.getContext('2d');let W,H,D=Math.min(2,window.devicePixelRatio||1);"
        "function fit(){W=C.clientWidth;H=C.clientHeight;C.width=W*D;C.height=H*D;X.setTransform(D,0,0,D,0,0)}fit();addEventListener('resize',fit);"
        "const RM=matchMedia('(prefers-reduced-motion: reduce)').matches;const P=__P__;"
        "function hx(h,a){const n=parseInt(h.slice(1),16);return `rgba(${n>>16},${(n>>8)&255},${n&255},${a})`}"
        "function loop(f){let t0=performance.now();function s(n){f((n-t0)/1000);if(!RM)requestAnimationFrame(s)}requestAnimationFrame(s)}")
TAIL = "</script></body></html>"

JS = {}

# rotating DNA double helix, depth-shaded
JS["helix"] = """loop(t=>{X.setTransform(D,0,0,D,0,0);X.clearRect(0,0,W,H);const vw=P.vert?H:W,vh=P.vert?W:H;if(P.vert)X.setTransform(0,D,-D,0,W*D,0);
const n=P.n||18,R=Math.min(vw*.32,vh*.3),cy=vh/2,sp=(vw*.86)/n,x0=vw*.07;
const pts=[];for(let i=0;i<n;i++){const a=t*1.2+i*.55,y=Math.cos(a),z=Math.sin(a);pts.push([x0+i*sp,cy+R*y,z,cy-R*y,-z])}
for(const p of pts){X.strokeStyle=hx(P.fg,.25+.25*Math.abs(p[2]));X.lineWidth=3;X.beginPath();X.moveTo(p[0],p[1]);X.lineTo(p[0],p[3]);X.stroke()}
const ball=(x,y,z,c)=>{const r=(P.r||5)+4*(z+1);X.fillStyle=hx(c,.45+.55*(z+1)/2);X.beginPath();X.arc(x,y,r,0,7);X.fill()};
const order=[];pts.forEach((p,i)=>{order.push([p[2],()=>ball(p[0],p[1],p[2],i%4==0?P.c:P.a)]);order.push([p[4],()=>ball(p[0],p[3],p[4],i%3==0?P.d:P.b)])});
order.sort((u,v)=>u[0]-v[0]).forEach(o=>o[1]())});"""

# point globe with arcs and travelling packets
JS["globe"] = """const N=170,S=[];for(let i=0;i<N;i++){const y=1-2*(i+.5)/N,r=Math.sqrt(1-y*y),f=i*2.39996;S.push([Math.cos(f)*r,y,Math.sin(f)*r])}
const L=[];for(let i=0;i<N;i++)for(let j=i+1;j<N;j++){const d=Math.hypot(S[i][0]-S[j][0],S[i][1]-S[j][1],S[i][2]-S[j][2]);if(d<.33&&Math.random()<.5)L.push([i,j])}
loop(t=>{X.clearRect(0,0,W,H);const R=Math.min(W,H)*.42,cx=W/2,cy=H/2,a=t*.35,ca=Math.cos(a),sa=Math.sin(a),tl=.35,ct=Math.cos(tl),st=Math.sin(tl);
const Q=S.map(p=>{let x=p[0]*ca+p[2]*sa,z=-p[0]*sa+p[2]*ca,y=p[1]*ct-z*st;z=p[1]*st+z*ct;return[cx+x*R,cy+y*R,z]});
X.lineWidth=1.2;for(const[i,j]of L){const z=(Q[i][2]+Q[j][2])/2;X.strokeStyle=hx(P.a,.12+.4*(z+1)/2);X.beginPath();X.moveTo(Q[i][0],Q[i][1]);X.lineTo(Q[j][0],Q[j][1]);X.stroke()}
Q.forEach((q,i)=>{const k=(q[2]+1)/2;X.fillStyle=hx(i%11==0?P.c:P.fg,.2+.75*k);X.beginPath();X.arc(q[0],q[1],1.4+2.6*k,0,7);X.fill()});
for(let k=0;k<(L.length?5:0);k++){const e=L[(k*37)%L.length],u=(t*.6+k*.2)%1,p=Q[e[0]],q=Q[e[1]];X.fillStyle=P.d;X.beginPath();X.arc(p[0]+(q[0]-p[0])*u,p[1]+(q[1]-p[1])*u,4,0,7);X.fill()}
X.strokeStyle=hx(P.b,.35);X.lineWidth=2;X.beginPath();X.ellipse(cx,cy,R*1.12,R*.32,-.3,0,7);X.stroke()});"""

# stack of wireframe server cubes rotating, LEDs blinking
JS["cubes"] = """const V=[[-1,-1,-1],[1,-1,-1],[1,1,-1],[-1,1,-1],[-1,-1,1],[1,-1,1],[1,1,1],[-1,1,1]],E=[[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]],F=[[0,1,2,3],[4,5,6,7],[0,1,5,4],[2,3,7,6],[1,2,6,5],[0,3,7,4]];
loop(t=>{X.clearRect(0,0,W,H);const s=Math.min(W,H)*.15,a=t*.6,ca=Math.cos(a),sa=Math.sin(a),tl=.5,ct=Math.cos(tl),st=Math.sin(tl);
for(let b=0;b<3;b++){const oy=(b-1)*s*1.25;const Q=V.map(v=>{let x=v[0]*1.5,y=v[1]*.5,z=v[2]*1.1;let X1=x*ca+z*sa,Z1=-x*sa+z*ca;let Y1=y*ct-Z1*st,Z2=y*st+Z1*ct;return[W/2+X1*s,H/2+oy+Y1*s,Z2]});
const fs=F.map(f=>[f.reduce((m,i)=>m+Q[i][2],0)/4,f]).sort((u,v)=>u[0]-v[0]);
for(const[z,f]of fs){X.fillStyle=hx(b==1?P.a:P.b,.10+.18*(z+2)/4);X.beginPath();f.forEach((i,k)=>k?X.lineTo(Q[i][0],Q[i][1]):X.moveTo(Q[i][0],Q[i][1]));X.closePath();X.fill()}
X.strokeStyle=hx(P.fg,.75);X.lineWidth=2;for(const[i,j]of E){X.beginPath();X.moveTo(Q[i][0],Q[i][1]);X.lineTo(Q[j][0],Q[j][1]);X.stroke()}
for(let k=0;k<3;k++){const on=Math.sin(t*4+b*2+k*1.3)>0;X.fillStyle=on?(k==2?P.c:P.d):hx(P.fg,.2);const p=Q[0],q=Q[1],u=.2+k*.12;X.beginPath();X.arc(p[0]+(q[0]-p[0])*u,p[1]+(q[1]-p[1])*u-6,4,0,7);X.fill()}}});"""

# shield that turns in 3D, scan line and pulse rings
JS["shield"] = """loop(t=>{X.clearRect(0,0,W,H);const s=Math.min(W,H)*.36,cx=W/2,cy=H/2,k=Math.cos(t*.9),sx=Math.max(.08,Math.abs(k));
for(let r=0;r<3;r++){const u=((t*.5+r/3)%1);X.strokeStyle=hx(P.b,.5*(1-u));X.lineWidth=3;X.beginPath();X.arc(cx,cy,s*(.9+u*.9),0,7);X.stroke()}
X.save();X.translate(cx,cy);X.scale(sx,1);const g=X.createLinearGradient(-s,0,s,0);g.addColorStop(0,k>0?P.a:P.c);g.addColorStop(1,hx(k>0?P.a:P.c,.6));X.fillStyle=g;
X.beginPath();X.moveTo(0,-s);X.lineTo(s*.82,-s*.66);X.lineTo(s*.82,s*.05);X.quadraticCurveTo(s*.78,s*.72,0,s);X.quadraticCurveTo(-s*.78,s*.72,-s*.82,s*.05);X.lineTo(-s*.82,-s*.66);X.closePath();X.fill();
X.strokeStyle=P.fg;X.lineWidth=6/sx*sx;X.lineCap='round';X.lineJoin='round';X.beginPath();X.moveTo(-s*.32,0);X.lineTo(-s*.06,s*.26);X.lineTo(s*.38,-s*.22);X.stroke();X.restore();
const yy=cy-s+((t*.8)%1)*2*s;X.strokeStyle=hx(P.d,.8);X.lineWidth=3;X.beginPath();X.moveTo(cx-s*sx*.85,yy);X.lineTo(cx+s*sx*.85,yy);X.stroke()});"""

# radar sweep with blips
JS["radar"] = """const B=[];for(let i=0;i<9;i++)B.push([Math.random()*6.28,.25+Math.random()*.7,i%4==0]);
loop(t=>{X.clearRect(0,0,W,H);const R=Math.min(W,H)*.45,cx=W/2,cy=H/2,a=(t*1.4)%6.283;
X.strokeStyle=hx(P.b,.35);X.lineWidth=1.5;for(let i=1;i<=4;i++){X.beginPath();X.arc(cx,cy,R*i/4,0,7);X.stroke()}
X.beginPath();X.moveTo(cx-R,cy);X.lineTo(cx+R,cy);X.moveTo(cx,cy-R);X.lineTo(cx,cy+R);X.stroke();
for(let i=0;i<40;i++){X.fillStyle=hx(P.b,.22*(1-i/40));X.beginPath();X.moveTo(cx,cy);X.arc(cx,cy,R,a-i*.025-.025,a-i*.025);X.fill()}
X.strokeStyle=P.b;X.lineWidth=3;X.beginPath();X.moveTo(cx,cy);X.lineTo(cx+R*Math.cos(a),cy+R*Math.sin(a));X.stroke();
for(const b of B){let d=(a-b[0]+6.283)%6.283,al=Math.max(0,1-d/3);X.fillStyle=hx(b[2]?P.c:P.d,al);X.beginPath();X.arc(cx+R*b[1]*Math.cos(b[0]),cy+R*b[1]*Math.sin(b[0]),5+5*al,0,7);X.fill()}});"""

# atom: core with three tilted 3D orbits
JS["orbit"] = """loop(t=>{X.clearRect(0,0,W,H);const R=Math.min(W,H)*.42,cx=W/2,cy=H/2,tilt=[0,1.05,-1.05],col=[P.a,P.b,P.d];
const items=[];for(let o=0;o<3;o++){const tl=tilt[o];for(let i=0;i<=64;i++){}
const u=t*(1+o*.35)+o*2;const x=Math.cos(u),y=Math.sin(u)*.32;const xr=x*Math.cos(tl)-y*Math.sin(tl),yr=x*Math.sin(tl)+y*Math.cos(tl);items.push([Math.sin(u),cx+xr*R,cy+yr*R,col[o]]);
X.strokeStyle=hx(col[o],.55);X.lineWidth=2.5;X.beginPath();X.ellipse(cx,cy,R,R*.32,tl,0,7);X.stroke()}
const g=X.createRadialGradient(cx-8,cy-8,4,cx,cy,R*.26);g.addColorStop(0,P.fg);g.addColorStop(1,P.c);X.fillStyle=g;X.beginPath();X.arc(cx,cy,R*.22*(1+.05*Math.sin(t*3)),0,7);X.fill();
items.sort((p,q)=>p[0]-q[0]).forEach(p=>{X.fillStyle=p[3];X.beginPath();X.arc(p[1],p[2],7+4*p[0],0,7);X.fill()})});"""

# ball-and-stick molecule rotating
JS["molecule"] = """const A=[[0,0,0],[1.2,.3,.2],[-1.1,.5,-.3],[.2,-1.2,.4],[.3,1.3,-.6],[2.2,-.4,.6],[-2.1,-.2,.5],[-.6,-2.1,-.3],[1.1,2.2,.3],[2.6,.9,-.5]],K=[[0,1],[0,2],[0,3],[0,4],[1,5],[2,6],[3,7],[4,8],[1,9]];
loop(t=>{X.clearRect(0,0,W,H);const s=Math.min(W,H)*.17,a=t*.7,b=t*.31;const Q=A.map(p=>{let x=p[0]*Math.cos(a)+p[2]*Math.sin(a),z=-p[0]*Math.sin(a)+p[2]*Math.cos(a),y=p[1]*Math.cos(b)-z*Math.sin(b);z=p[1]*Math.sin(b)+z*Math.cos(b);return[W/2+x*s,H/2+y*s,z]});
X.lineWidth=6;for(const[i,j]of K){X.strokeStyle=hx(P.fg,.35+.15*(Q[i][2]+Q[j][2]));X.beginPath();X.moveTo(Q[i][0],Q[i][1]);X.lineTo(Q[j][0],Q[j][1]);X.stroke()}
Q.map((q,i)=>[q,i]).sort((u,v)=>u[0][2]-v[0][2]).forEach(([q,i])=>{const r=(i==0?20:i<5?15:11)*(1+.12*q[2]);const g=X.createRadialGradient(q[0]-r/3,q[1]-r/3,1,q[0],q[1],r);g.addColorStop(0,P.fg);g.addColorStop(1,i==0?P.c:i<5?P.a:P.b);X.fillStyle=g;X.beginPath();X.arc(q[0],q[1],r,0,7);X.fill()})});"""

# drifting particle field with links (full-bleed backdrop)
JS["particles"] = """const N=60,S=[];for(let i=0;i<N;i++)S.push([Math.random(),Math.random(),(Math.random()-.5)*.02,(Math.random()-.5)*.02,Math.random()]);
loop(t=>{X.clearRect(0,0,W,H);const dt=.016;for(const p of S){p[0]=(p[0]+p[2]*dt+1)%1;p[1]=(p[1]+p[3]*dt+1)%1}
X.lineWidth=1;for(let i=0;i<N;i++)for(let j=i+1;j<N;j++){const dx=(S[i][0]-S[j][0])*W,dy=(S[i][1]-S[j][1])*H,d=Math.hypot(dx,dy);if(d<170){X.strokeStyle=hx(P.b,.18*(1-d/170));X.beginPath();X.moveTo(S[i][0]*W,S[i][1]*H);X.lineTo(S[j][0]*W,S[j][1]*H);X.stroke()}}
S.forEach((p,i)=>{X.fillStyle=hx(i%9==0?P.d:P.b,.25+.35*Math.abs(Math.sin(t+p[4]*6)));X.beginPath();X.arc(p[0]*W,p[1]*H,i%9==0?3.5:2.2,0,7);X.fill()})});"""

# count-up number (kinetic numeral), then a slow glow
JS["counter"] = """const to=P.to,dec=P.dec||0,f=P.font||"Georgia, 'Times New Roman', serif";
loop(t=>{X.clearRect(0,0,W,H);const u=Math.min(1,t/(P.dur||1.8)),e=1-Math.pow(1-u,3),v=to*e;
let s=v.toLocaleString('en-US',{minimumFractionDigits:dec,maximumFractionDigits:dec});s=(P.pre||'')+s+(P.suf||'');
X.font=`600 ${P.size}px ${f}`;X.textBaseline='middle';X.textAlign=P.align||'left';const x=P.align=='center'?W/2:0;
X.shadowColor=hx(P.d,.35+.25*Math.sin(t*2));X.shadowBlur=u<1?0:18;X.fillStyle=P.fg;X.fillText(s,x,H/2);
if(u<1){X.fillStyle=hx(P.d,.9);X.fillRect(0,H-6,W*e,6)}});"""

# kinetic words: each word slams in (scale+blur), stagger, then a light sweep across the line
JS["kinetic"] = """const WS=P.words,f=P.font||"'Helvetica Neue', Arial, sans-serif";
let SZ=P.size;function fitz(){X.font=`${P.weight||900} ${SZ}px ${f}`;const m=Math.max(...WS.map(w=>X.measureText(w[0]).width));if(W>0&&m>W*.98)SZ=Math.floor(SZ*W*.98/m)}fitz();addEventListener('resize',()=>{SZ=P.size;fitz()});
loop(t=>{X.clearRect(0,0,W,H);X.textBaseline='middle';const P2=Object.assign({},P,{size:SZ});let y=H/2-(WS.length-1)*SZ*P.lh/2;
WS.forEach((w,i)=>{const st=.25+i*P.gap,u=Math.max(0,Math.min(1,(t-st)/.45)),e=1-Math.pow(1-u,3);if(u<=0)return;
X.save();const yy=y+i*SZ*P.lh;X.translate(P.align=='center'?W/2:0,yy);const sc=2.2-1.2*e;X.scale(sc,sc);X.globalAlpha=Math.min(1,u*2);
X.font=`${P.weight||900} ${SZ}px ${f}`;X.textAlign=P.align||'left';X.fillStyle=w[1]||P.fg;if(u<1){X.filter=`blur(${(1-e)*8}px)`}X.fillText(w[0],0,0);X.restore();
const sw=((t-st-1)%4)/1.2;if(t>st+1&&sw>=0&&sw<=1){X.save();X.globalCompositeOperation='source-atop';const tw=W,gx=sw*tw*1.4-tw*.2;const g=X.createLinearGradient(gx-120,0,gx+120,0);g.addColorStop(0,'rgba(255,255,255,0)');g.addColorStop(.5,'rgba(255,255,255,.55)');g.addColorStop(1,'rgba(255,255,255,0)');X.fillStyle=g;X.fillRect(0,yy-SZ*.6,W,SZ*1.2);X.restore()}})});"""

# terminal: typed log lines, looping
JS["terminal"] = """const Lw=P.lines;X.font="24px Menlo, Consolas, 'Courier New', monospace";
loop(t=>{X.clearRect(0,0,W,H);X.fillStyle=hx(P.bg||'#000000',.94);X.fillRect(0,0,W,H);X.font="24px Menlo, Consolas, 'Courier New', monospace";X.textBaseline='top';
const cyc=Lw.length*1.6+2,tt=t%cyc;let shown=0;Lw.forEach((l,i)=>{const st=i*1.6;if(tt<st)return;const n=Math.min(l[0].length,Math.floor((tt-st)*38));X.fillStyle=l[1]||P.fg;X.fillText(l[0].slice(0,n),20,18+i*36);shown=i});
if(Math.floor(t*2)%2==0){X.fillStyle=P.d;X.fillRect(20,18+(shown+1)*36,14,26)}});"""


def emb(kind, left, top, w, h, pal, build=None, **opts):
    p = dict(pal)
    p.update(opts)
    page = HEAD + BOOT.replace("__P__", json.dumps(p, ensure_ascii=False)) + JS[kind] + TAIL
    assert len(page.encode()) < 15500, (kind, len(page))
    b = f' data-build-in="{build}"' if build else ""
    return f'<x-embed{b} style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{h}px">{page}</x-embed>'
