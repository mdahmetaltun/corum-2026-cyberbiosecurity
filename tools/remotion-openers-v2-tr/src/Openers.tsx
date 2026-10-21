import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig, Sequence, random } from "remotion";
import { Backdrop, C, F, usePalette, RiseText, TypeLine, Slam, Corner, Flash, arcPath, ramp, clamp } from "./kit";

const FOOT_L = "SİBER BİYOGÜVENLİK EĞİTİM ÇALIŞTAYI · ÇORUM";

/* ───────────────────────── 1 · CSF 2.0 ───────────────────────── */
const OLD = ["TANIMLAMA", "KORUMA", "TESPİT", "MÜDAHALE", "KURTARMA"];

const Wheel: React.FC<{ six: number; spin: number; scale: number; hot: number }> = ({ six, spin, scale, hot }) => {
  // six: 0 = five-function ring, 1 = ring opened up around GOVERN core
  const cx = 960, cy = 540;
  const r0 = interpolate(six, [0, 1], [150, 285]);
  const r1 = interpolate(six, [0, 1], [330, 430]);
  const gap = 0.035;
  const seg = (Math.PI * 2) / 5;
  return (
    <svg width={1920} height={1080} style={{ position: "absolute", inset: 0, scale: `${scale}`, rotate: `${spin}deg` }}>
      <defs>
        {OLD.map((_, i) => {
          const a0 = -Math.PI / 2 + i * seg + gap, a1 = a0 + seg - gap * 2;
          const rm = (r0 + r1) / 2;
          return (
            <path key={i} id={`lab${i}`} d={`M${cx + rm * Math.cos(a0)},${cy + rm * Math.sin(a0)} A${rm},${rm} 0 0 1 ${cx + rm * Math.cos(a1)},${cy + rm * Math.sin(a1)}`} />
          );
        })}
      </defs>
      {OLD.map((w, i) => {
        const a0 = -Math.PI / 2 + i * seg + gap, a1 = a0 + seg - gap * 2;
        const flash = interpolate(hot, [i * 0.12, i * 0.12 + 0.2, i * 0.12 + 0.45], [0, 1, 0.15], clamp);
        return (
          <g key={w}>
            <path d={arcPath(cx, cy, r0, r1, a0, a1)} fill={C.ink2} stroke={flash > 0.3 ? C.orange : "rgba(232,236,239,0.35)"} strokeWidth={2} />
            <path d={arcPath(cx, cy, r0, r1, a0, a1)} fill={C.orange} opacity={flash * 0.35} />
            <text fill={C.steel} fontFamily={F.display} fontWeight={800} fontSize={interpolate(six, [0, 1], [34, 30])} letterSpacing="0.12em" dy={11}>
              <textPath href={`#lab${i}`} startOffset="50%" textAnchor="middle">{w}</textPath>
            </text>
          </g>
        );
      })}
    </svg>
  );
};

export const OpenerCSF: React.FC = () => {
  usePalette("csf");
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const ringIn = spring({ frame: f - 70, fps, config: { damping: 200 } });
  const six = spring({ frame: f - 175, fps, config: { damping: 16, stiffness: 90 } });
  const spin = interpolate(f, [70, 330], [-40, 18], clamp);
  const zoom = interpolate(f, [292, 330], [1, 9], { ...clamp, easing: (t) => t * t * t });
  const wheelOut = ramp(f, 312, 330, 1, 0);
  return (
    <AbsoluteFill style={{ background: C.ink, overflow: "hidden" }}>
      <Backdrop />
      {/* 0–70: document id types in */}
      <Sequence from={0} durationInFrames={95} layout="absolute-fill">
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", gap: 28, opacity: ramp(f, 78, 94, 1, 0) }}>
          <TypeLine text="NIST.CSWP.29" start={6} size={44} color={C.steel} />
          <TypeLine text="yayım 26 · 02 · 2024" start={26} size={30} />
        </AbsoluteFill>
      </Sequence>
      {/* wheel */}
      {f >= 70 && f < 332 ? (
        <AbsoluteFill style={{ opacity: Math.min(ringIn, wheelOut), scale: `${zoom}` }}>
          <Wheel six={six} spin={spin} scale={interpolate(ringIn, [0, 1], [0.6, 1])} hot={ramp(f, 112, 160)} />
          <div style={{ position: "absolute", top: 110, width: "100%", textAlign: "center", fontFamily: F.mono, fontSize: 26, letterSpacing: "0.2em", color: C.mute, opacity: ramp(f, 95, 115) * ramp(f, 168, 180, 1, 0) }}>
            CSF 1.1 · BEŞ FONKSİYON
          </div>
          <div style={{ position: "absolute", top: 110, width: "100%", textAlign: "center", fontFamily: F.mono, fontSize: 26, letterSpacing: "0.2em", color: C.orange, opacity: ramp(f, 200, 215) }}>
            CSF 2.0 · ALTI FONKSİYON
          </div>
          <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
            {f >= 178 ? <Slam text="YÖNETİŞİM" start={178} size={80} color={C.orange} stretch /> : null}
          </AbsoluteFill>
        </AbsoluteFill>
      ) : null}
      <Flash at={178} />
      {/* title */}
      {f >= 322 ? (
        <AbsoluteFill style={{ justifyContent: "center", paddingLeft: 140, gap: 6 }}>
          <div style={{ fontFamily: F.mono, fontSize: 30, letterSpacing: "0.22em", color: C.orange, opacity: ramp(f, 326, 345) }}>NIST SİBER GÜVENLİK ÇERÇEVESİ 2.0</div>
          <RiseText text="ÇEKİRDEK" start={332} size={150} />
          <RiseText text="FONKSİYONLAR" start={338} size={150} />
          <RiseText text="VE PROFİLLER" start={344} size={150} color={C.teal} />
          <div style={{ fontFamily: F.sans, fontSize: 38, color: C.mute, marginTop: 24, opacity: ramp(f, 372, 392) }}>Biyolaboratuvarı güvenceye almak için ortak bir dil</div>
        </AbsoluteFill>
      ) : null}
      <Corner left={FOOT_L} right="Prof. Dr. Ahmet Altun" at={380} />
    </AbsoluteFill>
  );
};

/* ───────────────────────── 2 · AI RMF ───────────────────────── */
const Net: React.FC<{ t: number; glow: number }> = ({ t, glow }) => {
  const nodes = new Array(46).fill(0).map((_, i) => {
    const a = random(`a${i}`) * Math.PI * 2;
    const r = 180 + random(`r${i}`) * 620;
    return { x: 960 + Math.cos(a + t * 0.0015 * (i % 2 ? 1 : -1)) * r * 1.25, y: 540 + Math.sin(a + t * 0.0015) * r * 0.62, k: random(`k${i}`) };
  });
  const lines: React.ReactNode[] = [];
  nodes.forEach((p, i) =>
    nodes.forEach((q, j) => {
      if (j <= i) return;
      const d = Math.hypot(p.x - q.x, p.y - q.y);
      if (d < 230) lines.push(<line key={`${i}-${j}`} x1={p.x} y1={p.y} x2={q.x} y2={q.y} stroke={C.blue} strokeOpacity={(1 - d / 230) * 0.45 * glow} strokeWidth={1.5} />);
    }),
  );
  return (
    <svg width={1920} height={1080} style={{ position: "absolute", inset: 0 }}>
      {lines}
      {nodes.map((p, i) => (
        <circle key={i} cx={p.x} cy={p.y} r={3 + p.k * 4} fill={p.k > 0.86 ? C.orange : C.steel} opacity={0.75 * glow} />
      ))}
    </svg>
  );
};

export const OpenerAI: React.FC = () => {
  usePalette("ai");
  const f = useCurrentFrame();
  const count = Math.round(interpolate(f, [18, 92], [0, 40000], { ...clamp, easing: (t) => 1 - Math.pow(1 - t, 3) }));
  const words = ["YÖNETİŞİM", "HARİTALAMA", "ÖLÇME", "YÖNETME"];
  return (
    <AbsoluteFill style={{ background: C.ink, overflow: "hidden" }}>
      <Backdrop drift={0.6} />
      <Net t={f} glow={ramp(f, 150, 190) * ramp(f, 300, 330, 1, 0.25)} />
      {/* scene 1: the counter */}
      {f < 158 ? (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", opacity: ramp(f, 140, 156, 1, 0), scale: `${interpolate(f, [0, 156], [1, 1.12])}` }}>
          <div style={{ fontFamily: F.mono, fontSize: 250, fontWeight: 500, color: C.steel, letterSpacing: "-0.04em", fontVariantNumeric: "tabular-nums" }}>{count.toLocaleString("tr-TR")}</div>
          <div style={{ fontFamily: F.mono, fontSize: 32, letterSpacing: "0.18em", color: C.mute, opacity: ramp(f, 40, 60) }}>ADAY MOLEKÜL · 6 SAATTEN KISA SÜREDE</div>
          <div style={{ marginTop: 56, fontFamily: F.display, fontWeight: 800, fontSize: 66, color: C.orange, opacity: ramp(f, 100, 116), translate: `0px ${ramp(f, 100, 116, 24, 0)}px` }}>Aynı model. Tersine çevrilmiş hedef.</div>
          <div style={{ position: "absolute", bottom: 150, fontFamily: F.sans, fontSize: 24, color: C.mute, opacity: ramp(f, 104, 120) }}>Urbina et al., Nature Machine Intelligence 4, 189–191 (2022)</div>
        </AbsoluteFill>
      ) : null}
      <Flash at={158} color={C.teal} />
      {/* scene 2: the four verbs, one per beat */}
      {words.map((w, i) => {
        const s = 166 + i * 26;
        const vis = f >= s && f < 166 + 4 * 26 + 6;
        return vis ? (
          <AbsoluteFill key={w} style={{ justifyContent: "center", alignItems: "center", opacity: i < 3 ? ramp(f, s + 22, s + 26, 1, 0) : ramp(f, 270, 276, 1, 0) }}>
            <Slam text={w} start={s} size={200} color={i === 0 ? C.orange : C.steel} stretch />
          </AbsoluteFill>
        ) : null;
      })}
      {/* scene 3: title */}
      {f >= 276 ? (
        <AbsoluteFill style={{ justifyContent: "center", paddingLeft: 140, gap: 6 }}>
          <div style={{ fontFamily: F.mono, fontSize: 30, letterSpacing: "0.22em", color: C.orange, opacity: ramp(f, 280, 300) }}>NIST AI 100-1 · AI RMF</div>
          <RiseText text="YAPAY ZEKÂ" start={284} size={190} />
          <RiseText text="RİSK YÖNETİMİ" start={294} size={190} color={C.teal} />
          <div style={{ fontFamily: F.sans, fontSize: 38, color: C.mute, marginTop: 20, opacity: ramp(f, 326, 346) }}>Araştırma laboratuvarları için ilkeler ve uygulamalar</div>
        </AbsoluteFill>
      ) : null}
      <Corner left={FOOT_L} right="Prof. Dr. Ahmet Altun" at={330} />
    </AbsoluteFill>
  );
};

/* ───────────────────────── 3 · Case study ───────────────────────── */
const EVENTS = [
  { d: "16 MART 2021", t: "Kötü amaçlı bir e-posta bir bilgisayara ulaşır" },
  { d: "18 MART", t: "Açılıyor. Bir Excel dosyası iniyor." },
  { d: "31 MART", t: "Antivirüs görüyor. Ama izleme modunda." },
  { d: "13 MAYIS", t: "16+ sistemde ele alınmamış tehdit bildirildi" },
  { d: "14 MAYIS · 04:00", t: "Patlama. Ulusal sağlık BT'si çöküyor." },
];

export const OpenerCase: React.FC = () => {
  usePalette("kase");
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const beat = 44;
  const idx = Math.min(EVENTS.length - 1, Math.max(0, Math.floor((f - 20) / beat)));
  const detonate = 20 + 4 * beat;
  const shake = f > detonate && f < detonate + 14 ? (random(`s${f}`) - 0.5) * 26 : 0;
  const weeks = spring({ frame: f - (detonate + 30), fps, config: { damping: 200 } });
  return (
    <AbsoluteFill style={{ background: C.ink, overflow: "hidden", translate: `${shake}px ${-shake * 0.6}px` }}>
      <Backdrop />
      {/* progress rail */}
      <div style={{ position: "absolute", left: 140, right: 140, top: 760, height: 3, background: C.line, opacity: ramp(f, 10, 25) * ramp(f, detonate + 70, detonate + 85, 1, 0) }}>
        <div style={{ width: `${ramp(f, 20, detonate, 0, 100, (t) => t)}%`, height: "100%", background: f >= detonate ? C.orange : C.teal }} />
        {EVENTS.map((e, i) => (
          <div key={i} style={{ position: "absolute", left: `${(i / 4) * 100}%`, top: -9, width: 20, height: 20, marginLeft: -10, borderRadius: 10, background: i <= idx && f >= 20 + i * beat ? (i === 4 ? C.orange : C.steel) : C.ink2, border: `2px solid ${C.mute}` }} />
        ))}
      </div>
      {f < detonate + 70 ? (
        <AbsoluteFill style={{ justifyContent: "center", paddingLeft: 140, paddingBottom: 120, opacity: ramp(f, detonate + 58, detonate + 70, 1, 0) }}>
          {EVENTS.map((e, i) => {
            const s = 20 + i * beat;
            if (f < s || (i < 4 && f >= s + beat)) return null;
            return (
              <div key={i}>
                <TypeLine text={e.d} start={s} size={40} color={i === 4 ? C.orange : C.teal} cps={2} caret={false} />
                <RiseText text={e.t} start={s + 6} size={i === 4 ? 92 : 80} stagger={0.5} color={C.steel} weight={i === 4 ? 900 : 800} />
              </div>
            );
          })}
        </AbsoluteFill>
      ) : null}
      <Flash at={detonate} />
      {f >= detonate + 66 && f < detonate + 150 ? (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center", opacity: ramp(f, detonate + 140, detonate + 150, 1, 0) }}>
          <div style={{ fontFamily: F.display, fontWeight: 900, fontSize: 330, color: C.orange, letterSpacing: "-0.05em", scale: `${interpolate(weeks, [0, 1], [0.6, 1])}`, opacity: weeks }}>≈ 8 hafta</div>
          <div style={{ fontFamily: F.mono, fontSize: 32, letterSpacing: "0.18em", color: C.steel, opacity: ramp(f, detonate + 86, detonate + 100) }}>SALDIRGAN ZATEN İÇERİDEYDİ</div>
          <div style={{ position: "absolute", bottom: 150, fontFamily: F.sans, fontSize: 24, color: C.mute, opacity: ramp(f, detonate + 90, detonate + 104) }}>HSE İrlanda, Conti fidye yazılımı · PwC olay sonrası inceleme, Aralık 2021</div>
        </AbsoluteFill>
      ) : null}
      {f >= detonate + 146 ? (
        <AbsoluteFill style={{ justifyContent: "center", paddingLeft: 140, gap: 6 }}>
          <div style={{ fontFamily: F.mono, fontSize: 30, letterSpacing: "0.22em", color: C.orange, opacity: ramp(f, detonate + 150, detonate + 168) }}>UYGULAMALI BİR VAKA ÇALIŞMASI</div>
          <RiseText text="KURUMSAL" start={detonate + 152} size={150} />
          <RiseText text="SİBER GÜVENLİK" start={detonate + 160} size={150} />
          <RiseText text="ALTYAPISI" start={detonate + 168} size={150} color={C.teal} />
        </AbsoluteFill>
      ) : null}
      <Corner left={FOOT_L} right="Prof. Dr. Ahmet Altun" at={detonate + 190} />
    </AbsoluteFill>
  );
};

/* ───────────────────────── 4 · Hands-on ───────────────────────── */
const BEATS = [
  { n: "1", w: "LABORATUVAR" },
  { n: "6", w: "FONKSİYON" },
  { n: "22", w: "KATEGORİ" },
  { n: "45", w: "DAKİKA" },
];

export const OpenerLab: React.FC = () => {
  usePalette("lab");
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const beat = 34;
  const end = 16 + BEATS.length * beat;
  const ring = ramp(f, end, end + 90, 0, 1, (t) => t);
  const titleIn = spring({ frame: f - (end + 20), fps, config: { damping: 200 } });
  return (
    <AbsoluteFill style={{ background: C.ink, overflow: "hidden" }}>
      <Backdrop drift={1.4} />
      {BEATS.map((b, i) => {
        const s = 16 + i * beat;
        if (f < s || f >= s + beat + (i === 3 ? 8 : 0)) return null;
        return (
          <AbsoluteFill key={i} style={{ justifyContent: "center", alignItems: "center", flexDirection: "row", gap: 48 }}>
            <Slam text={b.n} start={s} size={420} color={i === 3 ? C.orange : C.teal} />
            <div style={{ opacity: ramp(f, s + 6, s + 14) }}>
              <RiseText text={b.w} start={s + 5} size={130} stagger={0.8} />
            </div>
          </AbsoluteFill>
        );
      })}
      <Flash at={end} color={C.teal} />
      {f >= end ? (
        <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
          <svg width={760} height={760} style={{ position: "absolute", opacity: titleIn * 0.9 }}>
            <circle cx={380} cy={380} r={340} fill="none" stroke={C.line} strokeWidth={14} />
            <circle cx={380} cy={380} r={340} fill="none" stroke={C.orange} strokeWidth={14} strokeDasharray={2 * Math.PI * 340} strokeDashoffset={2 * Math.PI * 340 * ring} transform="rotate(-90 380 380)" strokeLinecap="round" />
          </svg>
          <div style={{ textAlign: "center", scale: `${interpolate(titleIn, [0, 1], [0.8, 1])}`, opacity: titleIn }}>
            <div style={{ fontFamily: F.mono, fontSize: 28, letterSpacing: "0.22em", color: C.orange }}>UYGULAMALI GRUP ALIŞTIRMASI</div>
            <div style={{ fontFamily: F.display, fontWeight: 900, fontSize: 210, color: C.steel, letterSpacing: "-0.04em", lineHeight: 0.95 }}>UYGULAYIN.</div>
            <div style={{ fontFamily: F.sans, fontSize: 34, color: C.mute, marginTop: 18 }}>Bir biyoteknoloji laboratuvarında NIST CSF 2.0</div>
          </div>
        </AbsoluteFill>
      ) : null}
      <Corner left={FOOT_L} right="Prof. Dr. Ahmet Altun" at={end + 40} />
    </AbsoluteFill>
  );
};
