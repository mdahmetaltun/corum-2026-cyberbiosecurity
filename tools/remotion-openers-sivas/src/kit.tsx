import React from "react";
import { AbsoluteFill, Easing, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { loadFont } from "@remotion/fonts";
import K from "./kapsid.json";

const LATIN_EXT = "U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+20A0-20C0, U+2C60-2C7F, U+A720-A7FF";
const faces: Array<[string, string, string, boolean]> = [];
for (const w of ["600", "700", "800"]) {
  faces.push(["Sora", `sora-latin-${w}-normal.woff2`, w, false], ["Sora", `sora-latin-ext-${w}-normal.woff2`, w, true]);
}
for (const w of ["500", "600"]) {
  faces.push(["Plex Mono", `ibm-plex-mono-latin-${w}-normal.woff2`, w, false], ["Plex Mono", `ibm-plex-mono-latin-ext-${w}-normal.woff2`, w, true]);
}
for (const w of ["400", "500"]) {
  faces.push(["Plex Sans", `ibm-plex-sans-latin-${w}-normal.woff2`, w, false], ["Plex Sans", `ibm-plex-sans-latin-ext-${w}-normal.woff2`, w, true]);
}
faces.forEach(([family, file, weight, ext]) => {
  loadFont({ family, url: staticFile(`fonts/${file}`), weight, format: "woff2", ...(ext ? { unicodeRange: LATIN_EXT } : {}) } as Parameters<typeof loadFont>[0]);
});

export const F = { display: "Sora, Arial, sans-serif", mono: "'Plex Mono', monospace", sans: "'Plex Sans', Arial, sans-serif" };

/** Canlı palette (Kapsid identity) */
export const C = {
  ink: "#1D2554", ink0: "#121838", ink2: "#28316B", cream: "#F2F4FF", sky: "#B4BCEA",
  t1: "#8AF5E6", t2: "#19E3C8", v1: "#7C6BFF", v2: "#5B47FF", v3: "#3A2BB8", p1: "#FF7AB0", p2: "#FF3D8B", amber: "#FFB627",
  line: "rgba(124,107,255,0.16)",
};

export const EASE = Easing.bezier(0.16, 1, 0.3, 1);
export const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
export const ramp = (f: number, a: number, b: number, from = 0, to = 1, easing = EASE) => interpolate(f, [a, b], [from, to], { ...clamp, easing });

export const Backdrop: React.FC<{ glowA?: string; glowB?: string }> = ({ glowA = "rgba(91,71,255,0.55)", glowB = "rgba(25,227,200,0.18)" }) => {
  const f = useCurrentFrame();
  const off = (f * 0.4) % 96;
  return (
    <AbsoluteFill style={{ background: C.ink0 }}>
      <AbsoluteFill style={{ backgroundImage: `linear-gradient(${C.line} 1px, transparent 1px), linear-gradient(90deg, ${C.line} 1px, transparent 1px)`, backgroundSize: "96px 96px", backgroundPosition: `${off}px ${off}px`, opacity: 0.6 }} />
      <AbsoluteFill style={{ background: `radial-gradient(ellipse at 76% 42%, ${glowA} 0%, transparent 56%), radial-gradient(ellipse at 0% 100%, ${glowB} 0%, transparent 52%)` }} />
    </AbsoluteFill>
  );
};

export const RiseText: React.FC<{ text: string; start: number; size: number; color?: string; font?: string; weight?: number; stagger?: number; tracking?: number }> = ({
  text, start, size, color = C.cream, font = F.display, weight = 800, stagger = 1.1, tracking = -0.03,
}) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  return (
    <div style={{ display: "flex", overflow: "hidden", fontFamily: font, fontSize: size, fontWeight: weight, color, letterSpacing: `${tracking}em`, lineHeight: 1.04, paddingBottom: size * 0.1 }}>
      {Array.from(text).map((ch, i) => {
        const s = spring({ frame: f - start - i * stagger, fps, config: { damping: 18, stiffness: 140, mass: 0.7 } });
        return <span key={i} style={{ display: "inline-block", whiteSpace: "pre", translate: `0px ${(1 - s) * size * 1.1}px`, opacity: Math.min(1, s * 1.4) }}>{ch}</span>;
      })}
    </div>
  );
};

export const TypeLine: React.FC<{ text: string; start: number; cps?: number; size?: number; color?: string; caret?: boolean }> = ({ text, start, cps = 1.4, size = 30, color = C.sky, caret = true }) => {
  const f = useCurrentFrame();
  const n = Math.max(0, Math.min(text.length, Math.floor((f - start) * cps)));
  const blink = Math.floor(f / 8) % 2 === 0;
  if (f < start) return null;
  return (
    <div style={{ fontFamily: F.mono, fontSize: size, color, letterSpacing: "0.03em", whiteSpace: "pre", fontWeight: 500 }}>
      {text.slice(0, n)}
      {caret ? <span style={{ opacity: blink ? 1 : 0, color: C.t2 }}>▌</span> : null}
    </div>
  );
};

export const Slam: React.FC<{ text: string; start: number; size: number; color?: string }> = ({ text, start, size, color = C.cream }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: f - start, fps, config: { damping: 14, stiffness: 180, mass: 0.8 } });
  if (f < start) return null;
  return (
    <div style={{ fontFamily: F.display, fontWeight: 800, fontSize: size, color, letterSpacing: "-0.04em", lineHeight: 0.95, scale: `${interpolate(s, [0, 1], [2.6, 1], clamp)}`, opacity: interpolate(f - start, [0, 4], [0, 1], clamp), filter: `blur(${interpolate(s, [0, 0.7, 1], [18, 2, 0], clamp)}px)`, whiteSpace: "nowrap" }}>
      {text}
    </div>
  );
};

export const Corner: React.FC<{ left: string; right: string; at: number }> = ({ left, right, at }) => {
  const f = useCurrentFrame();
  const o = ramp(f, at, at + 20);
  const st: React.CSSProperties = { position: "absolute", bottom: 72, fontFamily: F.mono, fontWeight: 500, fontSize: 24, color: C.sky, letterSpacing: "0.12em", opacity: o };
  return (<><div style={{ ...st, left: 96 }}>{left}</div><div style={{ ...st, right: 96 }}>{right}</div></>);
};

export const Flash: React.FC<{ at: number; color?: string }> = ({ at, color = C.p2 }) => {
  const f = useCurrentFrame();
  const o = interpolate(f, [at, at + 2, at + 10], [0, 0.85, 0], clamp);
  return <AbsoluteFill style={{ background: color, opacity: o, mixBlendMode: "screen", pointerEvents: "none" }} />;
};

/** Kapsid mark that assembles: every facet flies in from a scattered position, spikes grow, the core lights up. */
export const Kapsid: React.FC<{ start: number; size: number; spin?: number; glow?: boolean }> = ({ start, size, spin = 0, glow = true }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = f - start;
  return (
    <svg viewBox="0 0 256 256" width={size} height={size} style={{ overflow: "visible", rotate: `${spin * t}deg` }}>
      {glow ? <circle cx={128} cy={130} r={110} fill="none" stroke={C.t2} strokeWidth={2} opacity={ramp(t, 40, 70, 0, 0.5)} strokeDasharray="4 12" /> : null}
      {K.faces.map((fc, i) => {
        const s = spring({ frame: t - i * 2.2, fps, config: { damping: 15, stiffness: 90, mass: 0.9 } });
        const ang = i * 2.39996;
        const dist = 260 + (i % 4) * 70;
        const dx = (1 - s) * Math.cos(ang) * dist, dy = (1 - s) * Math.sin(ang) * dist;
        const core = fc.core && glow ? 0.65 + 0.35 * Math.sin(t / 6) : 1;
        return (
          <g key={i} style={{ transform: `translate(${dx}px, ${dy}px) rotate(${(1 - s) * 140}deg)`, transformOrigin: `${fc.cx}px ${fc.cy}px`, opacity: Math.min(1, s * 1.5) }}>
            <path d={fc.d} fill={fc.fill} opacity={core} />
          </g>
        );
      })}
      {K.spikes.map((sp, i) => {
        const g = ramp(t, 30 + i * 3, 46 + i * 3);
        const x2 = sp.x1 + (sp.x2 - sp.x1) * g, y2 = sp.y1 + (sp.y2 - sp.y1) * g;
        return (
          <g key={`s${i}`} opacity={g}>
            <line x1={sp.x1} y1={sp.y1} x2={x2} y2={y2} stroke={K.stroke} strokeWidth={5} strokeLinecap="round" />
            <circle cx={x2} cy={y2} r={6 * g} fill={sp.dot} />
          </g>
        );
      })}
    </svg>
  );
};
