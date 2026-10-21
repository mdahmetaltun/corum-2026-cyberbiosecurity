import React from "react";
import {
  AbsoluteFill,
  Easing,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
} from "remotion";
import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";

const LATIN_EXT = "U+0100-02BA, U+02BD-02C5, U+02C7-02CC, U+02CE-02D7, U+02DD-02FF, U+0304, U+0308, U+0329, U+1E00-1E9F, U+20A0-20C0, U+2C60-2C7F, U+A720-A7FF";
const faces: Array<[string, string, string, string?]> = [
  ["Archivo", "archivo-latin-wdth-normal.woff2", "100 900"],
  ["Archivo", "archivo-latin-ext-wdth-normal.woff2", "100 900", LATIN_EXT],
  ["Plex Sans", "ibm-plex-sans-latin-400-normal.woff2", "400"],
  ["Plex Sans", "ibm-plex-sans-latin-500-normal.woff2", "500"],
  ["Plex Sans", "ibm-plex-sans-latin-ext-400-normal.woff2", "400", LATIN_EXT],
  ["Source Serif 4", "source-serif-4-latin-wght-normal.woff2", "200 900"],
  ["Source Serif 4", "source-serif-4-latin-ext-wght-normal.woff2", "200 900", LATIN_EXT],
  ["Plex Mono", "ibm-plex-mono-latin-400-normal.woff2", "400"],
  ["Plex Mono", "ibm-plex-mono-latin-500-normal.woff2", "500"],
  ["Plex Sans", "ibm-plex-sans-latin-ext-500-normal.woff2", "500", LATIN_EXT],
  ["Plex Mono", "ibm-plex-mono-latin-ext-400-normal.woff2", "400", LATIN_EXT],
  ["Plex Mono", "ibm-plex-mono-latin-ext-500-normal.woff2", "500", LATIN_EXT],
];
faces.forEach(([family, file, weight, unicodeRange]) => {
  loadFont({ family, url: staticFile(`fonts/${file}`), weight, format: "woff2", ...(unicodeRange ? { unicodeRange } : {}) } as Parameters<typeof loadFont>[0]);
});

export const F = {
  display: "Archivo, Arial, sans-serif",
  serif: "'Source Serif 4', Georgia, serif",
  mono: "'Plex Mono', monospace",
  sans: "'Plex Sans', Arial, sans-serif",
};

// Base palette; each opener switches it with usePalette() before its children render.
export const C = {
  ink: "#13294B",
  ink2: "#1B3866",
  steel: "#F5F3EE",
  mute: "#B9C7DA",
  line: "rgba(157,184,211,0.13)",
  orange: "#FF7A1A",
  blue: "#5B9BFF",
  teal: "#7FD1C9",
  gold: "#F0C27A",
  glowA: "rgba(36,80,127,0.75)",
  glowB: "rgba(14,124,123,0.35)",
};

/** Vivid per-deck themes (Çorum 2026 colour boards) */
export const PALETTES = {
  csf: { ink: "#0A1640", ink2: "#2340C8", steel: "#F4F6FF", mute: "#A9B6E8", line: "rgba(61,107,255,0.17)", orange: "#FF5C4D", blue: "#2F5BF0", teal: "#C8F53A", gold: "#C8F53A", glowA: "rgba(47,91,240,0.62)", glowB: "rgba(200,245,58,0.16)" },
  ai: { ink: "#1A0B3D", ink2: "#2B1466", steel: "#F7F3FF", mute: "#C4B8EC", line: "rgba(123,61,255,0.18)", orange: "#FF2E93", blue: "#7B3DFF", teal: "#19D3F0", gold: "#19D3F0", glowA: "rgba(123,61,255,0.58)", glowB: "rgba(25,211,240,0.18)" },
  kase: { ink: "#0B2530", ink2: "#123A47", steel: "#F2F7F6", mute: "#A9C6C8", line: "rgba(18,194,176,0.15)", orange: "#FF6A13", blue: "#12C2B0", teal: "#FFC233", gold: "#FFC233", glowA: "rgba(255,106,19,0.30)", glowB: "rgba(18,194,176,0.24)" },
  lab: { ink: "#0D3328", ink2: "#164A3A", steel: "#F3FAF0", mute: "#A7C9B8", line: "rgba(163,230,53,0.15)", orange: "#FF8A1F", blue: "#2DD4BF", teal: "#A3E635", gold: "#A3E635", glowA: "rgba(45,212,191,0.36)", glowB: "rgba(163,230,53,0.20)" },
};
export const usePalette = (k: keyof typeof PALETTES) => { Object.assign(C, PALETTES[k]); };

export const EASE = Easing.bezier(0.16, 1, 0.3, 1);
export const clamp = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

export const ramp = (f: number, a: number, b: number, from = 0, to = 1, easing = EASE) =>
  interpolate(f, [a, b], [from, to], { ...clamp, easing });

/** Ink background with a slowly drifting lab grid and a vignette */
export const Backdrop: React.FC<{ drift?: number }> = ({ drift = 1 }) => {
  const f = useCurrentFrame();
  const off = (f * 0.35 * drift) % 80;
  return (
    <AbsoluteFill style={{ background: C.ink }}>
      <AbsoluteFill
        style={{
          backgroundImage: `linear-gradient(${C.line} 1px, transparent 1px), linear-gradient(90deg, ${C.line} 1px, transparent 1px)`,
          backgroundSize: "80px 80px",
          backgroundPosition: `${off}px ${off}px`,
          opacity: 0.55,
        }}
      />
      <AbsoluteFill
        style={{
          background:
            `radial-gradient(ellipse at 78% 50%, ${C.glowA} 0%, transparent 55%), radial-gradient(ellipse at 0% 100%, ${C.glowB} 0%, transparent 50%)`,
        }}
      />
    </AbsoluteFill>
  );
};

/** Kinetic line: characters rise out of a mask with a stagger */
export const RiseText: React.FC<{
  text: string;
  start: number;
  size: number;
  weight?: number;
  color?: string;
  font?: string;
  stagger?: number;
  tracking?: number;
  out?: number;
}> = ({ text, start, size, weight = 600, color = C.steel, font = F.serif, stagger = 1.2, tracking = -0.01, out }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const chars = Array.from(text);
  return (
    <div style={{ display: "flex", overflow: "hidden", fontFamily: font, fontSize: size, fontWeight: weight, color, letterSpacing: `${tracking}em`, lineHeight: 1.02, paddingBottom: size * 0.08 }}>
      {chars.map((ch, i) => {
        const s = spring({ frame: f - start - i * stagger, fps, config: { damping: 18, stiffness: 140, mass: 0.7 } });
        const o = out !== undefined ? ramp(f, out + i * 0.6, out + 10 + i * 0.6, 0, 1) : 0;
        return (
          <span
            key={i}
            style={{
              display: "inline-block",
              whiteSpace: "pre",
              translate: `0px ${(1 - s) * size * 1.1 - o * size * 1.1}px`,
              opacity: Math.min(1, s * 1.4) * (1 - o),
            }}
          >
            {ch}
          </span>
        );
      })}
    </div>
  );
};

/** Typewriter mono line with a blinking caret */
export const TypeLine: React.FC<{ text: string; start: number; cps?: number; size?: number; color?: string; caret?: boolean }> = ({
  text,
  start,
  cps = 1.4,
  size = 30,
  color = C.mute,
  caret = true,
}) => {
  const f = useCurrentFrame();
  const n = Math.max(0, Math.min(text.length, Math.floor((f - start) * cps)));
  const blink = Math.floor(f / 8) % 2 === 0;
  return (
    <div style={{ fontFamily: F.mono, fontSize: size, color, letterSpacing: "0.04em", whiteSpace: "pre" }}>
      {text.slice(0, n)}
      {caret && f >= start ? <span style={{ opacity: blink ? 1 : 0, color: C.orange }}>▌</span> : null}
    </div>
  );
};

/** Word that slams in: big scale-down with motion blur feel */
export const Slam: React.FC<{ text: string; start: number; size: number; color?: string; stretch?: boolean }> = ({ text, start, size, color = C.steel, stretch = false }) => {
  const f = useCurrentFrame();
  const { fps } = useVideoConfig();
  const s = spring({ frame: f - start, fps, config: { damping: 14, stiffness: 180, mass: 0.8 } });
  const wdth = stretch ? interpolate(s, [0, 1], [62, 125], clamp) : 100;
  return (
    <div
      style={{
        fontFamily: F.display,
        fontWeight: 900,
        fontSize: size,
        color,
        letterSpacing: "-0.035em",
        lineHeight: 0.9,
        scale: `${interpolate(s, [0, 1], [2.6, 1], clamp)}`,
        fontVariationSettings: `"wdth" ${wdth}`,
        opacity: interpolate(f - start, [0, 4], [0, 1], clamp),
        filter: `blur(${interpolate(s, [0, 0.7, 1], [18, 2, 0], clamp)}px)`,
        whiteSpace: "nowrap",
      }}
    >
      {text}
    </div>
  );
};

export const Corner: React.FC<{ left: string; right: string; at: number }> = ({ left, right, at }) => {
  const f = useCurrentFrame();
  const o = ramp(f, at, at + 20);
  return (
    <>
      <div style={{ position: "absolute", left: 96, bottom: 72, fontFamily: F.mono, fontSize: 24, color: C.mute, letterSpacing: "0.12em", opacity: o, textTransform: "uppercase" }}>{left}</div>
      <div style={{ position: "absolute", right: 96, bottom: 72, fontFamily: F.mono, fontSize: 24, color: C.mute, letterSpacing: "0.12em", opacity: o, textTransform: "uppercase" }}>{right}</div>
    </>
  );
};

/** Flash frame used on hard cuts */
export const Flash: React.FC<{ at: number; color?: string }> = ({ at, color = C.orange }) => {
  const f = useCurrentFrame();
  const o = interpolate(f, [at, at + 2, at + 9], [0, 0.85, 0], clamp);
  return <AbsoluteFill style={{ background: color, opacity: o, mixBlendMode: "screen", pointerEvents: "none" }} />;
};

export const arcPath = (cx: number, cy: number, r0: number, r1: number, a0: number, a1: number) => {
  const p = (r: number, a: number) => [cx + r * Math.cos(a), cy + r * Math.sin(a)];
  const [x0, y0] = p(r1, a0);
  const [x1, y1] = p(r1, a1);
  const [x2, y2] = p(r0, a1);
  const [x3, y3] = p(r0, a0);
  const large = a1 - a0 > Math.PI ? 1 : 0;
  return `M${x0},${y0} A${r1},${r1} 0 ${large} 1 ${x1},${y1} L${x2},${y2} A${r0},${r0} 0 ${large} 0 ${x3},${y3} Z`;
};
