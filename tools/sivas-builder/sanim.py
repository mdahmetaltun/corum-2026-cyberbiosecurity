"""Live x-embed scenes for the Sivas decks. Reuses the Çorum library (anim.JS) and adds:
capsid (3D icosahedral capsid), morph (particle typography morph), zoom (powers-of-ten zoom in / out),
scramble (decrypt-style type), exfil (data leaving a lab, then blocked), otp (authenticator code),
keytap (security key + origin check), countdown (live mm:ss timer)."""
import json, os, sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "slides-builder"))
from anim import HEAD, BOOT, TAIL, JS as _JS  # noqa: E402

# Robust sizing: the presenter (full screen, thumbnails, preloaded hidden slides) can resize the iframe without a
# usable resize event, or start it at 0×0. Re-fit on every frame when the canvas size changes and tell listeners.
BOOT = BOOT.replace("function s(n){f(", "function s(n){if(C.clientWidth!==W||C.clientHeight!==H){fit();dispatchEvent(new Event('resize'))}f(")
assert "dispatchEvent" in BOOT

JS = dict(_JS)
JS["counter"] = JS["counter"].replace("toLocaleString('en-US'", "toLocaleString(P.loc||'tr-TR'").replace('const to=P.to', 'const to=P.to,_w=P.weight||800').replace("`600 ${P.size}px ${f}`", "`${_w} ${P.size}px ${f}`").replace('P.font||"Georgia, \'Times New Roman\', serif"', 'P.font||"__FONT__"')
FONT = "'Segoe UI', 'Helvetica Neue', Arial, sans-serif"

# 3D icosahedral capsid: 20 faces, depth shading, spikes on the 12 vertices; optional burst (faces fly out and re-form)
JS["capsid"] = """const g=(1+Math.sqrt(5))/2,V=[[-1,g,0],[1,g,0],[-1,-g,0],[1,-g,0],[0,-1,g],[0,1,g],[0,-1,-g],[0,1,-g],[g,0,-1],[g,0,1],[-g,0,-1],[-g,0,1]].map(v=>{const l=Math.hypot(...v);return v.map(x=>x/l)});
const F=[];for(let i=0;i<12;i++)for(let j=i+1;j<12;j++)for(let k=j+1;k<12;k++){const d=(a,b)=>Math.hypot(V[a][0]-V[b][0],V[a][1]-V[b][1],V[a][2]-V[b][2]);if(d(i,j)<1.1&&d(j,k)<1.1&&d(i,k)<1.1)F.push([i,j,k])}
const CO=P.cols||[P.t1||P.b,P.b,P.a,P.v1||P.a,P.c,P.b,P.a,P.d];
loop(t=>{X.clearRect(0,0,W,H);const R=Math.min(W,H)*(P.scale||.36),cx=W/2,cy=H/2,a=t*(P.spin||.45),b=.35+Math.sin(t*.3)*.25;
const intro=P.intro?Math.min(1,t/1.6):1,ie=1-Math.pow(1-intro,3);const bu=P.burst?Math.max(0,Math.sin(t*.9-1.2))**6:0;
const rot=v=>{let x=v[0]*Math.cos(a)+v[2]*Math.sin(a),z=-v[0]*Math.sin(a)+v[2]*Math.cos(a),y=v[1]*Math.cos(b)-z*Math.sin(b);z=v[1]*Math.sin(b)+z*Math.cos(b);return[x,y,z]};
const pr=(p,s)=>{const k=3.2/(3.2-p[2]);return[cx+p[0]*R*s*k,cy+p[1]*R*s*k,p[2]]};
const Q=V.map(rot),sc=ie*(1+.03*Math.sin(t*2));
X.lineCap='round';
const items=[];
F.forEach((f,fi)=>{const c=[0,1,2].map(m=>(Q[f[0]][m]+Q[f[1]][m]+Q[f[2]][m])/3);const n=Math.hypot(...c);if(bu<.04&&c[2]<-.02)return;const off=1+bu*(.55+.3*Math.sin(fi*7.1));
const pts=f.map(i=>{const q=Q[i];return pr([c[0]*(off-1)+c[0]+(q[0]-c[0])*.88,c[1]*(off-1)+c[1]+(q[1]-c[1])*.88,c[2]*(off-1)+c[2]+(q[2]-c[2])*.88],sc)});
items.push([c[2],()=>{const sh=.35+.65*Math.max(0,(c[2]/n+1)/2);X.fillStyle=hx(CO[fi%CO.length],.25+.75*sh);X.beginPath();pts.forEach((p,k)=>k?X.lineTo(p[0],p[1]):X.moveTo(p[0],p[1]));X.closePath();X.fill();
if(c[2]>.55&&fi%5==0){const m=pts.map((p,k)=>[(p[0]+pts[(k+1)%3][0])/2,(p[1]+pts[(k+1)%3][1])/2]);X.fillStyle=P.d;X.beginPath();m.forEach((p,k)=>k?X.lineTo(p[0],p[1]):X.moveTo(p[0],p[1]));X.closePath();X.fill()}}])});
Q.forEach((q,i)=>{items.push([q[2]+.01,()=>{const p0=pr([q[0]*1.03,q[1]*1.03,q[2]*1.03],sc),p1=pr([q[0]*1.22,q[1]*1.22,q[2]*1.22],sc),al=.35+.65*(q[2]+1)/2;
X.strokeStyle=hx(P.v3||P.a,al);X.lineWidth=Math.max(2,R*.035);X.beginPath();X.moveTo(p0[0],p0[1]);X.lineTo(p1[0],p1[1]);X.stroke();
X.fillStyle=hx(i%2?P.c:P.d,al);X.beginPath();X.arc(p1[0],p1[1],R*.055*(1+.15*Math.sin(t*3+i)),0,7);X.fill()}])});
items.sort((u,v)=>u[0]-v[0]).forEach(o=>o[1]());
if(P.rings){for(let r=0;r<2;r++){const u=(t*.35+r/2)%1;X.strokeStyle=hx(P.b,.4*(1-u));X.lineWidth=2;X.beginPath();X.arc(cx,cy,R*(1.35+u*.6),0,7);X.stroke()}}});"""

# particle typography morph: words are sampled into dot clouds; dots fly from word to word
JS["morph"] = """const WS=P.words,N=P.n||1600,FN=P.font||"__FONT__",per=P.per||3.2,tr=P.tr||1.15;const O=document.createElement('canvas'),OC=O.getContext('2d');let T=[],px=new Float32Array(N),py=new Float32Array(N),sx=new Float32Array(N),sy=new Float32Array(N),R0=2;
let SW=0,SH=0;function samp(){if(!W||!H)return;SW=W;SH=H;try{O.width=W;O.height=H;T=WS.map(w=>{OC.clearRect(0,0,W,H);let sz=P.size;OC.font=`${P.weight||800} ${sz}px ${FN}`;const m=OC.measureText(w[0]).width;if(m>W*.95){sz=sz*W*.95/m;OC.font=`${P.weight||800} ${sz}px ${FN}`}
OC.fillStyle='#fff';OC.textAlign=P.align=='left'?'left':'center';OC.textBaseline='middle';OC.fillText(w[0],P.align=='left'?4:W/2,H/2);const d=OC.getImageData(0,0,W,H).data,st=Math.max(2,Math.round(sz/34)),pts=[];R0=st*.42;
for(let y=0;y<H;y+=st)for(let x=0;x<W;x+=st)if(d[(y*W+x)*4+3]>140)pts.push([x,y]);for(let i=pts.length-1;i>0;i--){const j=(i*7919)%(i+1);[pts[i],pts[j]]=[pts[j],pts[i]]}return pts})}catch(e){T=[]}
for(let i=0;i<N;i++){sx[i]=Math.random()*W;sy[i]=Math.random()*H}}samp();addEventListener('resize',samp);
const ez=u=>u<.5?4*u*u*u:1-Math.pow(-2*u+2,3)/2;
loop(t=>{X.clearRect(0,0,W,H);if(W&&H&&(W!==SW||H!==SH||!T.length||!T[0].length))samp();if(!T.length||!T[0].length){if(!W||!H)return;const n=WS.length,tq=Math.max(0,t),k=Math.floor(tq/per)%n,u=(tq%per)/per,w=WS[k];let sz=P.size;X.font=`${P.weight||800} ${sz}px ${FN}`;const m=X.measureText(w[0]).width;if(m>W*.95){sz=sz*W*.95/m;X.font=`${P.weight||800} ${sz}px ${FN}`}X.globalAlpha=Math.min(1,u*6,(1-u)*6);X.fillStyle=w[1]||P.fg;X.textAlign='center';X.textBaseline='middle';X.fillText(w[0],W/2,H/2);X.globalAlpha=1;return}const n=WS.length,tt=t+per-tr,k=Math.floor(tt/per)%n,pk=(k+n-1)%n,u=Math.min(1,(tt%per)/tr),e=ez(u),first=t<tr;
const A=T[pk],B=T[k],ca=WS[pk][1]||P.fg,cb=WS[k][1]||P.fg;X.fillStyle=u<1?cb:cb;
for(let i=0;i<N;i++){const a=first?[sx[i],sy[i]]:A[i%A.length],b=B[i%B.length],sw=Math.sin(u*Math.PI)*(30+40*((i*13)%7)/7),an=i*2.4;
const x=a[0]+(b[0]-a[0])*e+Math.cos(an)*sw,y=a[1]+(b[1]-a[1])*e+Math.sin(an)*sw;X.globalAlpha=i<B.length||u<1?1:0;X.fillStyle=(i%17==0)?(P.d||cb):(u<.5?ca:cb);X.fillRect(x-R0,y-R0,R0*2,R0*2)}X.globalAlpha=1});""".replace("__FONT__", FONT)

# powers-of-ten zoom: region network -> campus -> laboratory -> instrument workstation -> data; loops; rev:true zooms out
JS["zoom"] = """const S=.16,TG=[[.46,-.22],[.34,.26],[-.42,.30],[.06,-.16],[.10,.06]],LB=P.labels,n=5,per=P.per||3.2;
function rnd(s){return()=>{s=(s*16807)%2147483647;return s/2147483647}}
const r0=rnd(7),NODES=[];for(let i=0;i<34;i++)NODES.push([r0()*1.9-.95,r0()*1.9-.95]);NODES.push(TG[0]);
const B=[];const r1=rnd(11);for(let i=0;i<5;i++)for(let j=0;j<5;j++)if((i+j)%3)B.push([-.9+i*.38,-.9+j*.38,.28+r1()*.06,.22+r1()*.1]);
const BASES='ACGTTGCAGTCCATGGACTTAGCGATCAAGTCGGATCCTAGCTAGGCATTCGA';
function pan(c,a){X.fillStyle=c;X.globalAlpha=a;X.beginPath();X.roundRect?X.roundRect(-1,-1,2,2,.08):X.rect(-1,-1,2,2);X.fill();X.globalAlpha=1}
const LV=[(t,u)=>{pan(P.bg||'#121838',1);X.strokeStyle=hx(P.b,.35);X.lineWidth=.006;NODES.forEach((p,i)=>{const q=NODES[(i*7+3)%NODES.length],r=NODES[(i*5+1)%NODES.length];X.beginPath();X.moveTo(p[0],p[1]);X.lineTo(q[0],q[1]);X.lineTo(r[0],r[1]);X.stroke()});
NODES.forEach((p,i)=>{X.fillStyle=i==NODES.length-1?P.c:hx(i%5?P.b:P.d,.85);X.beginPath();X.arc(p[0],p[1],i==NODES.length-1?.05+.01*Math.sin(t*4):.022,0,7);X.fill()})},
(t,u)=>{pan('#1F2A63',1);X.fillStyle=hx(P.b,.18);X.fillRect(-.95,-.05,1.9,.08);X.fillRect(-.07,-.95,.08,1.9);B.forEach(b=>{X.fillStyle=hx(P.fg,.16);X.fillRect(b[0],b[1],b[2],b[3])});
X.fillStyle=hx(P.a,.9);X.fillRect(TG[1][0]-.17,TG[1][1]-.13,.34,.26);X.strokeStyle=P.d;X.lineWidth=.012;X.strokeRect(TG[1][0]-.19,TG[1][1]-.15,.38,.3)},
(t,u)=>{pan('#26306B',1);X.strokeStyle=hx(P.fg,.5);X.lineWidth=.01;X.strokeRect(-.92,-.92,1.84,1.84);for(let i=0;i<4;i++){X.fillStyle=hx(P.fg,.14);X.fillRect(-.8+i*.42,-.75,.3,.62)}
for(let i=0;i<5;i++){X.fillStyle=i==2?P.c:hx(P.b,.7);X.beginPath();X.arc(-.75+i*.37,.62,.07,0,7);X.fill()}X.fillStyle=P.d;X.fillRect(TG[2][0]-.16,TG[2][1]-.12,.32,.24);X.fillStyle=hx(P.b,.9);X.fillRect(TG[2][0]-.12,TG[2][1]-.09,.24,.13)},
(t,u)=>{pan('#2E3A7E',1);X.fillStyle='#0E1330';X.fillRect(-.82,-.7,1.64,1.06);X.fillStyle=hx(P.b,.12);X.fillRect(-.78,-.66,1.56,.98);X.fillStyle=hx(P.fg,.5);X.fillRect(-.12,.36,.24,.12);X.fillRect(-.36,.48,.72,.05);
for(let i=0;i<6;i++){const x=-.66+(i%3)*.4,y=-.52+Math.floor(i/3)*.38;X.fillStyle=i==4?P.d:hx(P.fg,.55);X.fillRect(x,y,.16,.2);X.fillStyle=hx(P.a,.8);X.fillRect(x,y,.16,.05)}
X.fillStyle=P.c;X.fillRect(.68,.56,.2,.07);X.fillStyle=hx(P.fg,.7);X.fillRect(.62,.565,.06,.06)},
(t,u)=>{pan('#121838',1)}];
function txt4(t,k2,m){if(k2!=4)return;}
loop(t=>{X.setTransform(D,0,0,D,0,0);X.clearRect(0,0,W,H);const L=n*per;let tt=t%L;if(P.rev)tt=L-tt;let k=Math.min(n-1,Math.floor(tt/per)),p=(tt%per)/per;const e0=Math.max(0,(p-.28)/.72),e=e0<.5?4*e0*e0*e0:1-Math.pow(-2*e0+2,3)/2;
const v=Math.pow(S,e),cx=TG[k][0]*(1-v)/(1-S),cy=TG[k][1]*(1-v)/(1-S),R=Math.min(W,H)*.5,sc=R/v;
const set=(ox,oy,s)=>X.setTransform(D*sc*s,0,0,D*sc*s,D*(W/2+(ox-cx)*sc),D*(H/2+(oy-cy)*sc));
const pk=(k+n-1)%n;set(-TG[pk][0]/S,-TG[pk][1]/S,1/S);LV[pk](t,e);
set(0,0,1);LV[k](t,e);
set(TG[k][0],TG[k][1],S);X.globalAlpha=.55+.45*e;LV[(k+1)%n](t,e);X.globalAlpha=1;
const dna=(ox,oy,s,al)=>{const cell=.11*s;for(let r=0;r<15;r++)for(let c=0;c<15;c++){const x=ox+(-.8+c*.115)*s,y=oy+(-.8+r*.115)*s,ch=BASES[(r*15+c)%BASES.length],hi=r==8&&c>=7&&c<=9;
const qx=W/2+(x-cx)*sc,qy=H/2+(y-cy)*sc,ps=cell*sc;if(qx<-40||qx>W+40||qy<-40||qy>H+40)continue;X.setTransform(D,0,0,D,0,0);X.globalAlpha=al;
X.fillStyle=hi?P.c:{A:P.b,C:P.a,G:P.d,T:P.fg}[ch];if(ps>9){X.font=`700 ${ps*.8}px Menlo, Consolas, monospace`;X.textAlign='center';X.textBaseline='middle';X.fillText(ch,qx,qy)}else X.fillRect(qx-ps*.3,qy-ps*.3,ps*.6,ps*.6)}X.globalAlpha=1};
if(k==4)dna(0,0,1,1);if(k==3)dna(TG[3][0],TG[3][1],S,.55+.45*e);
X.setTransform(D,0,0,D,0,0);const grd=X.createRadialGradient(W/2,H/2,Math.min(W,H)*.35,W/2,H/2,Math.max(W,H)*.75);grd.addColorStop(0,'rgba(18,24,56,0)');grd.addColorStop(1,P.bg||'#121838');X.fillStyle=grd;X.fillRect(0,0,W,H);
const lab=(s,al)=>{X.globalAlpha=al;X.font=`800 ${Math.round(H*.07)}px __FONT__`;X.textAlign='left';X.textBaseline='alphabetic';X.fillStyle=P.fg;X.fillText(s,H*.06,H*.92);X.globalAlpha=1};
lab(LB[k],1-Math.min(1,e*2));lab(LB[(k+1)%n],Math.max(0,e*2-1));
X.font=`600 ${Math.round(H*.035)}px Menlo, Consolas, monospace`;X.textAlign='right';X.fillStyle=P.b;X.fillText('×'+Math.round(Math.pow(1/S,k+e)).toLocaleString('tr-TR'),W-H*.06,H*.92)});""".replace("__FONT__", FONT)

# decrypt-style type: glyphs flicker, then lock left to right; optional loop
JS["scramble"] = """const LN=P.lines,G='ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ0123456789#$%&@<>/';
loop(t=>{X.clearRect(0,0,W,H);const tt=P.loop?t%P.loop:t;X.textBaseline='middle';LN.forEach((l,i)=>{const s=l[0],sz=l[2]||P.size,st=(P.delay||.2)+i*(P.gap||.5);X.font=`${P.weight||800} ${sz}px __FONT__`;let x=0;const y=(i+.5)*sz*(P.lh||1.12);
for(let c=0;c<s.length;c++){const lock=st+c*.045+.35,ch=s[c];let out=ch;if(tt<st)break;if(tt<lock&&ch!=' ')out=G[Math.floor((tt*30+c*7)%G.length)];X.fillStyle=tt<lock?hx(P.b,.85):(l[1]||P.fg);X.fillText(out,x,y);x+=X.measureText(ch).width}})});""".replace("__FONT__", FONT)

# data leaving a lab; second half a guard intercepts the flow
JS["exfil"] = """const LB=P.labels||['LAB','?'],per=P.per||10;
loop(t=>{X.clearRect(0,0,W,H);const tt=t%per,guard=tt>per/2,ax=W*.17,ay=H*.55,bx=W*.85,by=H*.4,mx=W*.53;
X.fillStyle=hx(P.fg,.08);X.strokeStyle=hx(P.fg,.55);X.lineWidth=3;X.beginPath();X.roundRect?X.roundRect(ax-W*.12,ay-H*.28,W*.24,H*.5,14):X.rect(ax-W*.12,ay-H*.28,W*.24,H*.5);X.fill();X.stroke();
for(let i=0;i<6;i++){X.fillStyle=hx(i==3?P.d:P.b,.7);X.fillRect(ax-W*.09+(i%3)*W*.065,ay-H*.18+Math.floor(i/3)*H*.16,W*.04,H*.08)}
X.fillStyle=guard?hx(P.fg,.25):P.c;X.beginPath();X.arc(bx,by,H*.09,0,7);X.fill();X.strokeStyle=hx(P.fg,.5);X.stroke();
X.font=`700 ${Math.round(H*.07)}px __FONT__`;X.textAlign='center';X.fillStyle=P.fg;X.fillText(LB[0],ax,ay+H*.33);X.fillText(LB[1],bx,by+H*.2);
const path=u=>{const x=(1-u)*(1-u)*(ax+W*.12)+2*(1-u)*u*mx+u*u*bx,y=(1-u)*(1-u)*ay+2*(1-u)*u*(H*.08)+u*u*by;return[x,y]};
X.setLineDash([8,10]);X.strokeStyle=hx(P.fg,.25);X.beginPath();for(let u=0;u<=1;u+=.02){const p=path(u);u?X.lineTo(p[0],p[1]):X.moveTo(p[0],p[1])}X.stroke();X.setLineDash([]);
for(let k=0;k<9;k++){let u=((t*.32+k/9)%1);let col=P.c;if(guard&&u>.42){u=.42-(u-.42)*.6;col=P.b}const p=path(Math.max(0,u));X.fillStyle=col;X.fillRect(p[0]-7,p[1]-7,14,14)}
if(guard){const p=path(.45),s=H*.11;X.save();X.translate(p[0],p[1]);X.fillStyle=P.b;X.beginPath();X.moveTo(0,-s);X.lineTo(s*.8,-s*.6);X.lineTo(s*.8,s*.05);X.quadraticCurveTo(s*.75,s*.7,0,s);X.quadraticCurveTo(-s*.75,s*.7,-s*.8,s*.05);X.lineTo(-s*.8,-s*.6);X.closePath();X.fill();
X.strokeStyle='#121838';X.lineWidth=6;X.lineCap='round';X.beginPath();X.moveTo(-s*.32,0);X.lineTo(-s*.06,s*.26);X.lineTo(s*.36,-s*.22);X.stroke();X.restore()}
X.font=`600 ${Math.round(H*.05)}px Menlo, Consolas, monospace`;X.textAlign='left';X.fillStyle=guard?P.b:P.c;X.fillText(guard?(P.on||'ENGELLENDİ'):(P.off||'SIZDIRILIYOR')+' '+Math.floor(tt*137)+' MB',W*.03,H*.08)});""".replace("__FONT__", FONT)

# authenticator app: 6-digit code, countdown ring; period P.per seconds (demo speed)
JS["otp"] = """const per=P.per||8,acc=P.acc||'kullanici@kurum.edu.tr';function code(k){let s=(k*2654435761+97)%1000000;s=Math.abs(s|0)%1000000;return String(s).padStart(6,'0')}
loop(t=>{X.clearRect(0,0,W,H);const k=Math.floor(t/per),u=(t%per)/per,cw=W*.86,ch=H*.5,x0=(W-cw)/2,y0=H*.28;
X.fillStyle=hx(P.fg,.96);X.beginPath();X.roundRect?X.roundRect(x0,y0,cw,ch,24):X.rect(x0,y0,cw,ch);X.fill();
X.fillStyle=P.ink||'#1D2554';X.font=`600 ${Math.round(H*.045)}px __FONT__`;X.textAlign='left';X.textBaseline='middle';X.fillText(acc,x0+cw*.06,y0+ch*.2);
const c=code(k),sz=Math.round(Math.min(H*.17,cw*.11));X.font=`700 ${sz}px Menlo, Consolas, monospace`;X.fillStyle=u>.8?P.c:(P.ink||'#1D2554');X.fillText(c.slice(0,3)+' '+c.slice(3),x0+cw*.06,y0+ch*.6);
const rx=x0+cw*.86,ry=y0+ch*.58,rr=ch*.18;X.lineWidth=rr*.28;X.strokeStyle=hx(P.a,.18);X.beginPath();X.arc(rx,ry,rr,0,7);X.stroke();X.strokeStyle=u>.8?P.c:P.a;X.beginPath();X.arc(rx,ry,rr,-Math.PI/2,-Math.PI/2+Math.PI*2*(1-u));X.stroke();
X.font=`700 ${Math.round(rr*.8)}px __FONT__`;X.textAlign='center';X.fillStyle=P.ink||'#1D2554';X.fillText(String(Math.ceil((1-u)*30)),rx,ry);
X.fillStyle=P.fg;X.textAlign='center';X.font=`600 ${Math.round(H*.05)}px __FONT__`;X.fillText(P.cap||'Kod her 30 saniyede değişir',W/2,H*.9)});""".replace("__FONT__", FONT)

# security key: tap ripple, then origin check (legit passes, look-alike is refused)
JS["keytap"] = """const OK=P.good||'giris.kurum.edu.tr',BAD=P.bad||'giris-kurum.edu-tr.com',per=P.per||7;
loop(t=>{X.clearRect(0,0,W,H);const k=Math.floor(t/per)%2,u=(t%per)/per,cx=W*.3,cy=H*.5,kw=W*.17,kh=H*.62;
X.fillStyle=P.ink||'#1D2554';X.strokeStyle=hx(P.fg,.6);X.lineWidth=3;X.beginPath();X.roundRect?X.roundRect(cx-kw/2,cy-kh/2,kw,kh,kw*.3):X.rect(cx-kw/2,cy-kh/2,kw,kh);X.fill();X.stroke();
X.fillStyle=hx(P.fg,.2);X.fillRect(cx-kw*.28,cy+kh*.5,kw*.56,kh*.22);X.beginPath();X.arc(cx,cy+kh*.06,kw*.23,0,7);X.fillStyle=P.d;X.fill();
if(u>.12&&u<.55){for(let r=0;r<3;r++){const v=((u-.12)*3+r/3)%1;X.strokeStyle=hx(P.d,.8*(1-v));X.lineWidth=4;X.beginPath();X.arc(cx,cy+kh*.06,kw*(.25+v*.6),0,7);X.stroke()}}
X.font=`700 ${Math.round(H*.055)}px __FONT__`;X.fillStyle=P.fg;X.textAlign='center';X.textBaseline='middle';X.fillText(P.tap||'DOKUN',cx,cy-kh*.32);
const bx=W*.5,bw=W*.47,by=H*.32,bh=H*.36,good=k==0;X.fillStyle=hx(P.fg,.96);X.beginPath();X.roundRect?X.roundRect(bx,by,bw,bh,18):X.rect(bx,by,bw,bh);X.fill();
X.font=`600 ${Math.round(Math.min(H*.065,bw*.065))}px Menlo, Consolas, monospace`;X.textAlign='left';X.fillStyle=P.ink||'#1D2554';X.fillText((good?OK:BAD),bx+bw*.06,by+bh*.32);
if(u>.55){const ok=good;X.fillStyle=ok?P.b:P.c;X.beginPath();X.arc(bx+bw*.12,by+bh*.72,bh*.16,0,7);X.fill();X.strokeStyle=P.ink||'#1D2554';X.lineWidth=7;X.lineCap='round';X.beginPath();
const ox=bx+bw*.12,oy=by+bh*.72,s=bh*.08;if(ok){X.moveTo(ox-s,oy);X.lineTo(ox-s*.2,oy+s*.8);X.lineTo(ox+s,oy-s*.7)}else{X.moveTo(ox-s,oy-s);X.lineTo(ox+s,oy+s);X.moveTo(ox+s,oy-s);X.lineTo(ox-s,oy+s)}X.stroke();
X.font=`700 ${Math.round(Math.min(H*.06,bw*.06))}px __FONT__`;X.fillStyle=P.ink||'#1D2554';X.fillText(ok?(P.oktxt||'Anahtar imzaladı'):(P.badtxt||'Anahtar reddetti'),bx+bw*.24,by+bh*.72)}});""".replace("__FONT__", FONT)

# live countdown mm:ss with a ring; last minute turns hot
JS["countdown"] = """const tot=(P.min||10)*60;loop(t=>{X.clearRect(0,0,W,H);const left=Math.max(0,tot-t),m=Math.floor(left/60),s=Math.floor(left%60),u=left/tot,cx=W/2,cy=H/2,R=Math.min(W,H)*.44,hot=left<60;
X.lineWidth=R*.08;X.strokeStyle=hx(P.fg,.12);X.beginPath();X.arc(cx,cy,R,0,7);X.stroke();X.strokeStyle=hot?P.c:P.b;X.lineCap='round';X.beginPath();X.arc(cx,cy,R,-Math.PI/2,-Math.PI/2+Math.PI*2*u);X.stroke();
X.font=`700 ${Math.round(R*.62)}px Menlo, Consolas, monospace`;X.textAlign='center';X.textBaseline='middle';X.fillStyle=hot?P.c:P.fg;X.fillText(String(m).padStart(2,'0')+':'+String(s).padStart(2,'0'),cx,cy);
X.font=`600 ${Math.round(R*.12)}px __FONT__`;X.fillStyle=hx(P.fg,.7);X.fillText(left>0?(P.cap||'kalan süre'):(P.done||'süre doldu'),cx,cy+R*.45)});""".replace("__FONT__", FONT)


JS["counter"] = JS["counter"].replace("__FONT__", FONT)


def emb(kind, left, top, w, h, pal, build=None, eid=None, **opts):
    p = dict(pal)
    p.update(opts)
    page = HEAD + BOOT.replace("__P__", json.dumps(p, ensure_ascii=False)) + JS[kind] + TAIL
    assert len(page.encode()) < 15500, (kind, len(page.encode()))
    b = f' data-build-in="{build}"' if build else ""
    i = f' id="{eid}"' if eid else ""
    return f'<x-embed{i}{b} style="position:absolute;left:{left}px;top:{top}px;width:{w}px;height:{h}px">{page}</x-embed>'
