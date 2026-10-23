import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { Backdrop, C, clamp, Corner, F, Flash, Kapsid, ramp, RiseText, Slam, TypeLine, EASE } from "./kit";

const W = 1920, H = 1080, S = 0.2;

/* ───────────── zoom levels (each a full 1920×1080 scene) ───────────── */
const rnd = (seed: number) => () => { seed = (seed * 16807) % 2147483647; return seed / 2147483647; };
const r0 = rnd(5);
const NODES = Array.from({ length: 46 }, () => [80 + r0() * 1760, 80 + r0() * 920]);
const A = [[1180, 300], [560, 520], [1240, 220]]; // target top-left in each level (child box = 384×216)

const Level0: React.FC = () => (
  <svg width={W} height={H} style={{ position: "absolute", left: 0, top: 0 }}>
    <rect width={W} height={H} fill={C.ink0} />
    {NODES.map((p, i) => { const q = NODES[(i * 7 + 3) % NODES.length]; return <line key={i} x1={p[0]} y1={p[1]} x2={q[0]} y2={q[1]} stroke={C.t2} strokeOpacity={0.25} strokeWidth={2} />; })}
    {NODES.map((p, i) => <circle key={`n${i}`} cx={p[0]} cy={p[1]} r={i % 6 ? 6 : 10} fill={i % 5 ? C.t1 : C.amber} opacity={0.8} />)}
    <rect x={A[0][0]} y={A[0][1]} width={384} height={216} rx={8} fill={C.ink} stroke={C.p2} strokeWidth={6} />
  </svg>
);
const Level1: React.FC = () => (
  <svg width={W} height={H} style={{ position: "absolute", left: 0, top: 0 }}>
    <rect width={W} height={H} fill={C.ink} />
    <rect x={0} y={500} width={W} height={36} fill={C.v3} opacity={0.5} />
    <rect x={930} y={0} width={36} height={H} fill={C.v3} opacity={0.5} />
    {Array.from({ length: 24 }, (_, i) => { const x = 60 + (i % 6) * 310, y = 70 + Math.floor(i / 6) * 250; return <rect key={i} x={x} y={y} width={240} height={170} rx={14} fill={C.cream} opacity={0.12} />; })}
    <rect x={A[1][0]} y={A[1][1]} width={384} height={216} rx={12} fill={C.ink2} stroke={C.amber} strokeWidth={8} />
  </svg>
);
const Level2: React.FC = () => (
  <svg width={W} height={H} style={{ position: "absolute", left: 0, top: 0 }}>
    <rect width={W} height={H} fill={C.ink2} />
    <rect x={40} y={40} width={W - 80} height={H - 80} rx={20} fill="none" stroke={C.cream} strokeOpacity={0.4} strokeWidth={6} />
    {[0, 1, 2, 3].map((i) => <rect key={i} x={120 + i * 260} y={480} width={180} height={460} rx={14} fill={C.cream} opacity={0.1} />)}
    {[0, 1, 2, 3, 4].map((i) => <circle key={`c${i}`} cx={1240 + (i % 3) * 200} cy={640 + Math.floor(i / 3) * 200} r={60} fill={i === 2 ? C.p2 : C.t2} opacity={0.75} />)}
    <rect x={A[2][0]} y={A[2][1]} width={384} height={216} rx={12} fill="#0E1330" stroke={C.t2} strokeWidth={8} />
  </svg>
);
const FILES = ["kosu_2026-11-03.fastq", "dizi_verisi_v7.fastq", "protokol_taslak.docx", "musteri_numune.xlsx", "ham_spektrum.raw", "yedek_eski.zip"];
const Level3: React.FC<{ hi?: number }> = ({ hi = 0 }) => (
  <AbsoluteFill style={{ background: "#0E1330", padding: 90, display: "flex", flexDirection: "column", gap: 40 }}>
    <div style={{ fontFamily: F.mono, fontSize: 34, color: C.sky, fontWeight: 500 }}>/veri/dizileme/2026-11/</div>
    <div style={{ display: "flex", flexWrap: "wrap", gap: 36 }}>
      {FILES.map((n, i) => (
        <div key={n} style={{ width: 540, height: 230, borderRadius: 22, padding: 34, boxSizing: "border-box", background: i === 1 ? `rgba(255,61,139,${0.18 + 0.4 * hi})` : "rgba(242,244,255,0.07)", border: `4px solid ${i === 1 ? C.p2 : "rgba(242,244,255,0.18)"}`, display: "flex", flexDirection: "column", justifyContent: "space-between" }}>
          <div style={{ width: 70, height: 86, borderRadius: 10, background: i === 1 ? C.p2 : C.v1 }} />
          <div style={{ fontFamily: F.mono, fontSize: 32, color: C.cream, fontWeight: 500 }}>{n}</div>
        </div>
      ))}
    </div>
  </AbsoluteFill>
);

/** Powers-of-ten dive through nested levels; p runs 0→3 */
const Dive: React.FC<{ p: number; hi: number }> = ({ p, hi }) => {
  const k = Math.min(2, Math.floor(p));
  const e = Math.min(1, p - k);
  const v = Math.pow(S, e);
  let ox = 0, oy = 0;
  for (let j = 0; j < k; j++) { ox += A[j][0] * Math.pow(S, j); oy += A[j][1] * Math.pow(S, j); }
  const sk = Math.pow(S, k);
  const vx = ox + A[k][0] * sk * (1 - v) / (1 - S), vy = oy + A[k][1] * sk * (1 - v) / (1 - S);
  const vw = W * sk * v;
  const z = W / vw;
  const box = (child: React.ReactNode, a: number[]) => (
    <div style={{ position: "absolute", left: a[0], top: a[1], width: W, height: H, transform: `scale(${S})`, transformOrigin: "0 0", overflow: "hidden" }}>{child}</div>
  );
  return (
    <AbsoluteFill style={{ overflow: "hidden" }}>
      <div style={{ position: "absolute", left: 0, top: 0, width: W, height: H, transformOrigin: "0 0", transform: `translate(${-vx * z}px, ${-vy * z}px) scale(${z})` }}>
        <Level0 />
        {box(<><Level1 />{box(<><Level2 />{box(<Level3 hi={hi} />, A[2])}</>, A[1])}</>, A[0])}
      </div>
    </AbsoluteFill>
  );
};

const LABELS = ["BÖLGE AĞI", "KAMPÜS", "LABORATUVAR", "CİHAZ BİLGİSAYARI"];

/* ───────────── F2 · Cybertheft opener (15 s) ───────────── */
export const FilmCybertheft: React.FC = () => {
  const f = useCurrentFrame();
  const p = interpolate(f, [70, 120, 130, 170, 180, 222], [0, 1, 1, 2, 2, 3], { ...clamp, easing: EASE });
  const diveO = ramp(f, 58, 72) * (1 - ramp(f, 296, 302));
  const lab = Math.min(3, Math.round(p));
  const prog = ramp(f, 240, 292, 0, 100);
  return (
    <AbsoluteFill style={{ background: C.ink0 }}>
      {/* intrusion log */}
      <AbsoluteFill style={{ padding: "300px 160px", display: "flex", flexDirection: "column", gap: 22, opacity: 1 - ramp(f, 56, 68) }}>
        <TypeLine text="03:12:44  oturum açıldı · lab-ws-07" start={4} cps={1.6} size={40} color={C.sky} caret={false} />
        <TypeLine text="03:12:51  yetki: araştırmacı (paylaşılan hesap)" start={22} cps={1.8} size={40} color={C.sky} caret={false} />
        <TypeLine text="03:13:02  hedef bulundu: /veri/dizileme/2026-11/" start={42} cps={2.2} size={40} color={C.p1} />
      </AbsoluteFill>
      <AbsoluteFill style={{ opacity: diveO }}>
        <Dive p={p} hi={ramp(f, 226, 240)} />
        <AbsoluteFill style={{ background: "radial-gradient(ellipse at center, transparent 55%, rgba(18,24,56,0.9) 100%)" }} />
        <div style={{ position: "absolute", left: 96, bottom: 150, fontFamily: F.display, fontWeight: 800, fontSize: 72, color: C.cream, letterSpacing: "-0.02em", textShadow: "0 4px 30px rgba(0,0,0,0.6)" }}>{LABELS[lab]}</div>
        <div style={{ position: "absolute", right: 96, bottom: 158, fontFamily: F.mono, fontWeight: 600, fontSize: 40, color: C.t2 }}>×{Math.round(Math.pow(1 / S, p)).toLocaleString("tr-TR")}</div>
        {/* copy progress */}
        <div style={{ position: "absolute", left: 560, top: 720, width: 800, opacity: ramp(f, 236, 246), display: "flex", flexDirection: "column", gap: 14 }}>
          <div style={{ fontFamily: F.mono, fontSize: 32, color: C.p1, fontWeight: 600 }}>kopyalanıyor → bilinmeyen sunucu · %{Math.round(prog)}</div>
          <div style={{ height: 16, borderRadius: 8, background: "rgba(242,244,255,0.15)" }}><div style={{ width: `${prog}%`, height: 16, borderRadius: 8, background: C.p2 }} /></div>
        </div>
      </AbsoluteFill>
      <Flash at={300} />
      {/* slam words */}
      <AbsoluteFill style={{ padding: "180px 160px", display: "flex", flexDirection: "column", gap: 6, opacity: 1 - ramp(f, 352, 362) }}>
        <Slam text="VERİ." start={304} size={190} />
        <Slam text="FİKİR." start={318} size={190} color={C.t2} />
        <Slam text="ZAMAN." start={332} size={190} color={C.p2} />
      </AbsoluteFill>
      {/* title card */}
      <AbsoluteFill style={{ opacity: ramp(f, 356, 370) }}>
        <Backdrop glowA="rgba(255,61,139,0.38)" />
        <div style={{ position: "absolute", right: 150, top: 230, opacity: f > 358 ? 1 : 0 }}><Kapsid start={360} size={560} /></div>
        <div style={{ position: "absolute", left: 140, top: 300, display: "flex", flexDirection: "column", gap: 0 }}>
          <div style={{ fontFamily: F.mono, fontSize: 30, letterSpacing: "0.18em", color: C.t2, fontWeight: 600, opacity: ramp(f, 364, 380), marginBottom: 26 }}>SİBER BİYOGÜVENLİK ÇALIŞTAYI</div>
          <RiseText text="BİYOTEKNOLOJİYİ" start={368} size={104} />
          <RiseText text="SİBER HIRSIZLIKTAN" start={378} size={104} color={C.p2} />
          <RiseText text="KORUMAK" start={388} size={104} />
        </div>
        <Corner left="1. GÜN · 14:45" right="SİVAS · 16 KASIM 2026" at={392} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};

/* ───────────── F1 · Workshop opener (12 s) ───────────── */
export const FilmWorkshop: React.FC = () => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const mv = spring({ frame: f - 96, fps, config: { damping: 20, stiffness: 70 } });
  const x = interpolate(mv, [0, 1], [W / 2 - 260, 150]);
  const y = interpolate(mv, [0, 1], [H / 2 - 270, 210]);
  const sz = interpolate(mv, [0, 1], [520, 300]);
  return (
    <AbsoluteFill>
      <Backdrop />
      <div style={{ position: "absolute", left: x, top: y }}><Kapsid start={6} size={sz} spin={0} /></div>
      <div style={{ position: "absolute", left: 500, top: 250, display: "flex", flexDirection: "row", gap: 30, alignItems: "baseline" }}>
        <Slam text="SİBER" start={118} size={150} />
        <Slam text="BİYO" start={132} size={150} color={C.p2} />
      </div>
      <div style={{ position: "absolute", left: 500, top: 410 }}><Slam text="GÜVENLİK" start={146} size={150} color={C.t2} /></div>
      <div style={{ position: "absolute", left: 160, top: 640 }}><TypeLine text="> laboratuvarınız artık bir ağ." start={186} cps={1.2} size={52} color={C.cream} /></div>
      <div style={{ position: "absolute", left: 160, top: 760, display: "flex", flexDirection: "row", gap: 24, opacity: ramp(f, 240, 262) }}>
        {["ÇALIŞTAY", "16–17 KASIM 2026", "SİVAS"].map((t, i) => (
          <div key={t} style={{ fontFamily: F.mono, fontWeight: 600, fontSize: 34, letterSpacing: "0.12em", color: C.ink0, background: [C.t2, C.amber, C.p1][i], padding: "10px 24px", borderRadius: 40, translate: `0px ${(1 - ramp(f, 240 + i * 6, 262 + i * 6)) * 40}px` }}>{t}</div>
        ))}
      </div>
      <Flash at={116} color={C.v1} />
      <Corner left="HEALTH SECURITY PARTNERS · SİVAS CUMHURİYET ÜNİVERSİTESİ" right="HILTON GARDEN INN SİVAS" at={270} />
    </AbsoluteFill>
  );
};

/* ───────────── F3 · MFA exercise opener (9 s) ───────────── */
const Key: React.FC<{ start: number }> = ({ start }) => {
  const f = useCurrentFrame();
  const t = f - start;
  const s = ramp(t, 0, 18);
  return (
    <svg width={520} height={520} viewBox="0 0 520 520" style={{ overflow: "visible", scale: `${0.6 + 0.4 * s}`, opacity: s }}>
      {[0, 1, 2].map((r) => { const v = ((t - 24) / 30 + r / 3) % 1; return t > 24 ? <circle key={r} cx={260} cy={290} r={80 + v * 200} fill="none" stroke={C.amber} strokeWidth={6} opacity={0.8 * (1 - v)} /> : null; })}
      <rect x={160} y={60} width={200} height={400} rx={60} fill={C.ink2} stroke={C.cream} strokeOpacity={0.6} strokeWidth={6} />
      <rect x={200} y={440} width={120} height={70} rx={8} fill={C.sky} opacity={0.5} />
      <circle cx={260} cy={290} r={58} fill={C.amber} />
      <circle cx={260} cy={150} r={22} fill="none" stroke={C.cream} strokeWidth={8} opacity={0.7} />
    </svg>
  );
};

export const FilmMFA: React.FC = () => {
  const f = useCurrentFrame();
  const dots = Math.max(0, Math.min(12, Math.floor((f - 10) / 2.5)));
  const shake = f > 50 && f < 70 ? Math.sin(f * 2.2) * 16 * (1 - (f - 50) / 20) : 0;
  return (
    <AbsoluteFill>
      <Backdrop glowA="rgba(255,182,39,0.28)" />
      <AbsoluteFill style={{ opacity: 1 - ramp(f, 92, 104) }}>
        <div style={{ position: "absolute", left: 460, top: 330, width: 1000, translate: `${shake}px 0px` }}>
          <div style={{ fontFamily: F.mono, fontSize: 32, color: C.sky, fontWeight: 500, marginBottom: 18 }}>Parola</div>
          <div style={{ height: 130, borderRadius: 24, background: "rgba(242,244,255,0.08)", border: `4px solid ${f > 48 ? C.p2 : "rgba(242,244,255,0.3)"}`, display: "flex", alignItems: "center", padding: "0 40px", fontFamily: F.mono, fontSize: 80, color: C.cream, letterSpacing: "0.2em" }}>{"•".repeat(dots)}</div>
          <div style={{ marginTop: 26, fontFamily: F.sans, fontWeight: 500, fontSize: 40, color: C.p1, opacity: ramp(f, 50, 60) }}>Bu parola sızdırılmış bir listede de var.</div>
        </div>
      </AbsoluteFill>
      <AbsoluteFill style={{ padding: "250px 160px", display: "flex", flexDirection: "column", gap: 0, opacity: (1 - ramp(f, 150, 160)) }}>
        <Slam text="ŞİFRE" start={104} size={220} />
        <Slam text="YETMEZ." start={118} size={220} color={C.p2} />
      </AbsoluteFill>
      <div style={{ position: "absolute", right: 110, top: 250, opacity: f > 150 ? 1 : 0 }}><Key start={152} /></div>
      <AbsoluteFill style={{ opacity: ramp(f, 158, 170) }}>
        <div style={{ position: "absolute", left: 150, top: 300, display: "flex", flexDirection: "column" }}>
          <div style={{ fontFamily: F.mono, fontSize: 30, letterSpacing: "0.18em", color: C.amber, fontWeight: 600, marginBottom: 26 }}>ALIŞTIRMA 3 · UYGULAMALI</div>
          <RiseText text="ÇOK FAKTÖRLÜ" start={170} size={92} />
          <RiseText text="DOĞRULAMA VE" start={178} size={92} />
          <RiseText text="DONANIM ANAHTARI" start={186} size={92} color={C.amber} />
        </div>
        <Corner left="2. GÜN · 13:00" right="SİVAS · 17 KASIM 2026" at={196} />
      </AbsoluteFill>
    </AbsoluteFill>
  );
};
