/* Çorum deck engine — stage scaling, morph (FLIP), zoom, iris, kinetic type, steps, overview, notes, timer */
(() => {
  "use strict";
  const W = 1920, H = 1080;
  const RM = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const EASE = "cubic-bezier(.16,1,.3,1)", EASE_IN = "cubic-bezier(.7,0,.84,0)", EASE_IO = "cubic-bezier(.65,0,.35,1)", POP = "cubic-bezier(.34,1.56,.64,1)";
  const stage = document.getElementById("stage");
  const slides = [...stage.querySelectorAll(":scope > section.slide")];
  const body = document.body;
  const CFG = window.DECK || {};
  const TITLE = CFG.title || document.title;
  const MINUTES = +CFG.minutes || 60;
  let idx = 0, step = 0, scale = 1, overview = false, anims = [], timerStart = 0, timerOn = false;
  const hooks = (window.DeckHooks = window.DeckHooks || {});

  /* ── helpers ── */
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const anim = (el, kf, o) => { if (!el || !el.animate) return null; const a = el.animate(kf, o); anims.push(a); return a; };
  const done = (a) => (a ? a.finished.catch(() => {}) : Promise.resolve());
  const rectIn = (el) => { const s = stage.getBoundingClientRect(), r = el.getBoundingClientRect(); return { x: (r.left - s.left) / scale, y: (r.top - s.top) / scale, w: r.width / scale, h: r.height / scale }; };
  const isDark = (s) => s.classList.contains("dark");
  const maxStep = (s) => $$("[data-step]", s).reduce((m, e) => Math.max(m, +e.dataset.step || 0), 0);
  const pad2 = (n) => String(n).padStart(2, "0");

  /* ── fit the 1920×1080 stage to the window ── */
  function fit() {
    scale = Math.min(innerWidth / W, innerHeight / H);
    stage.style.position = "absolute";
    stage.style.left = "50%"; stage.style.top = "50%";
    stage.style.transform = `translate(-50%,-50%) scale(${scale})`;
  }

  /* ── footers ── */
  slides.forEach((s, i) => {
    if (s.hasAttribute("data-nofoot")) return;
    const f = document.createElement("div");
    f.className = "foot";
    f.innerHTML = `<span>${s.dataset.foot || TITLE}</span><span class="tab">${pad2(i + 1)} / ${pad2(slides.length)}</span>`;
    s.appendChild(f);
  });

  /* ── kinetic text: split into words / masked chars ── */
  function split(el, chars) {
    if (el.__split) return; el.__split = true;
    const walk = (node) => {
      [...node.childNodes].forEach((n) => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach((tok) => {
            if (!tok) return;
            if (/^\s+$/.test(tok)) { frag.appendChild(document.createTextNode(" ")); return; }
            const w = document.createElement("span"); w.className = "kw";
            if (chars) {
              for (const ch of tok) {
                const m = document.createElement("span"); m.className = "kmask";
                const c = document.createElement("span"); c.className = "kc"; c.textContent = ch;
                m.appendChild(c); w.appendChild(m);
              }
            } else w.textContent = tok;
            frag.appendChild(w);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1 && !n.classList.contains("kw") && n.tagName !== "BR") walk(n);
      });
    };
    walk(el);
  }
  $$("[data-k='rise'],[data-k='rise-fast']").forEach((e) => split(e, true));
  $$("[data-k='words']").forEach((e) => split(e, false));

  const GLYPHS = "ABCDEFGHJKLMNPQRSTUVWXYZ0123456789#%&/<>=+";
  function scramble(el, delay) {
    const orig = el.__orig || (el.__orig = el.textContent);
    const start = performance.now() + delay, dur = Math.max(700, orig.length * 38);
    el.textContent = orig.replace(/\S/g, () => GLYPHS[(Math.random() * GLYPHS.length) | 0]);
    const tick = (t) => {
      if (!el.isConnected) return;
      const p = (t - start) / dur;
      if (p < 0) { requestAnimationFrame(tick); return; }
      const k = Math.floor(Math.min(1, p) * orig.length);
      el.textContent = orig.slice(0, k) + orig.slice(k).replace(/\S/g, () => GLYPHS[(Math.random() * GLYPHS.length) | 0]);
      if (p < 1) requestAnimationFrame(tick); else el.textContent = orig;
    };
    requestAnimationFrame(tick);
  }
  function countUp(el, delay) {
    const to = parseFloat(el.dataset.to), dec = +el.dataset.dec || 0, pre = el.dataset.pre || "", suf = el.dataset.suf || "";
    const fmt = (v) => pre + v.toLocaleString("en-US", { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf;
    const dur = +el.dataset.dur || 1600, start = performance.now() + delay;
    el.textContent = fmt(0);
    const tick = (t) => {
      const p = Math.min(1, Math.max(0, (t - start) / dur)), e = 1 - Math.pow(1 - p, 3);
      el.textContent = fmt(to * e);
      if (p < 1) requestAnimationFrame(tick);
    };
    requestAnimationFrame(tick);
  }
  function typeOut(el, delay) {
    const orig = el.__orig || (el.__orig = el.textContent);
    el.textContent = "";
    let i = 0;
    const t0 = setTimeout(function next() { i++; el.textContent = orig.slice(0, i); if (i < orig.length) setTimeout(next, 26); }, delay);
    el.__t = t0;
  }

  /* run one element's entrance; d = delay in ms */
  function play(el, d) {
    const k = el.dataset.k, inn = el.dataset.in;
    const delay = d + (+el.dataset.d || 0);
    if (RM) { if (k === "count") el.textContent = (el.dataset.pre || "") + (+el.dataset.to).toLocaleString("en-US") + (el.dataset.suf || ""); return; }
    if (k === "rise" || k === "rise-fast") {
      const cs = $$(".kc", el), st = Math.min(k === "rise-fast" ? 14 : 30, 700 / Math.max(1, cs.length));
      cs.forEach((c, i) => anim(c, [{ transform: "translateY(115%)" }, { transform: "none" }], { duration: 760, delay: delay + i * st, easing: EASE, fill: "backwards" }));
    } else if (k === "words") {
      $$(".kw", el).forEach((w, i) => anim(w, [{ transform: "translateY(36px)", opacity: 0, filter: "blur(6px)" }, { transform: "none", opacity: 1, filter: "blur(0)" }], { duration: 650, delay: delay + i * 70, easing: EASE, fill: "backwards" }));
    } else if (k === "stretch") {
      const fin = el.dataset.wdth || 100;
      anim(el, [
        { fontVariationSettings: '"wdth" 62', letterSpacing: "0.12em", opacity: 0, transform: "scale(1.25)" },
        { fontVariationSettings: '"wdth" 125', letterSpacing: "-0.02em", opacity: 1, transform: "scale(1)", offset: 0.62 },
        { fontVariationSettings: `"wdth" ${fin}`, letterSpacing: getComputedStyle(el).letterSpacing, opacity: 1, transform: "none" },
      ], { duration: 1300, delay, easing: EASE_IO, fill: "backwards" });
    } else if (k === "slam") {
      anim(el, [{ transform: "scale(2.4)", opacity: 0, filter: "blur(14px)" }, { transform: "scale(.97)", opacity: 1, filter: "blur(0)", offset: 0.7 }, { transform: "none", opacity: 1 }], { duration: 650, delay, easing: EASE, fill: "backwards" });
    } else if (k === "scramble") scramble(el, delay);
    else if (k === "count") countUp(el, delay);
    else if (k === "type") typeOut(el, delay);
    else if (k === "draw") {
      $$("path,line,polyline,circle,rect", el).forEach((p, i) => {
        if (!p.getTotalLength) return;
        let L = 0; try { L = p.getTotalLength(); } catch (e) { return; }
        p.style.strokeDasharray = L;
        anim(p, [{ strokeDashoffset: L }, { strokeDashoffset: 0 }], { duration: 1100, delay: delay + i * 60, easing: EASE_IO, fill: "backwards" });
      });
    }
    if (inn) {
      const kf = {
        up: [{ transform: "translateY(48px)", opacity: 0 }, { transform: "none", opacity: 1 }],
        down: [{ transform: "translateY(-48px)", opacity: 0 }, { transform: "none", opacity: 1 }],
        left: [{ transform: "translateX(-80px)", opacity: 0 }, { transform: "none", opacity: 1 }],
        right: [{ transform: "translateX(80px)", opacity: 0 }, { transform: "none", opacity: 1 }],
        fade: [{ opacity: 0 }, { opacity: 1 }],
        pop: [{ transform: "scale(.5)", opacity: 0 }, { transform: "none", opacity: 1 }],
        zoom: [{ transform: "scale(1.6)", opacity: 0, filter: "blur(10px)" }, { transform: "none", opacity: 1, filter: "blur(0)" }],
        grow: [{ transform: "scaleX(0)", transformOrigin: "0 50%" }, { transform: "none", transformOrigin: "0 50%" }],
      }[inn] || [{ opacity: 0 }, { opacity: 1 }];
      anim(el, kf, { duration: inn === "pop" ? 620 : 760, delay, easing: inn === "pop" ? POP : EASE, fill: "backwards" });
    }
  }
  const animatable = (root) => $$("[data-k],[data-in]", root).filter((e) => !e.closest("[data-step]:not(.shown)") || e.closest("[data-step]") === e);

  function enter(s, base) {
    animatable(s).filter((e) => !e.closest("[data-step]")).forEach((e) => play(e, base));
    $$("video[data-auto]", s).forEach((v) => { try { v.currentTime = 0; const p = v.play(); if (p) p.catch(() => {}); } catch (e) {} });
    startFx(s);
    if (s.dataset.hook && hooks[s.dataset.hook]) hooks[s.dataset.hook](s, step, "enter");
  }
  function leave(s) {
    $$("video", s).forEach((v) => { try { v.pause(); } catch (e) {} });
    stopFx(s);
    if (s.dataset.hook && hooks[s.dataset.hook]) hooks[s.dataset.hook](s, step, "leave");
  }

  /* ── steps ── */
  function applySteps(s, animate) {
    $$("[data-step]", s).forEach((e) => {
      const want = step >= +e.dataset.step;
      if (want && !e.classList.contains("shown")) {
        e.classList.add("shown");
        if (animate && !RM) {
          if (!e.dataset.in && !e.dataset.k) anim(e, [{ opacity: 0, transform: "translateY(36px)" }, { opacity: 1, transform: "none" }], { duration: 700, easing: EASE, fill: "backwards" });
          else play(e, 0);
          $$("[data-k],[data-in]", e).forEach((c) => play(c, 120));
        }
      } else if (!want) e.classList.remove("shown");
    });
    $$("[data-on]", s).forEach((e) => e.classList.toggle("on", step >= +e.dataset.on));
    $$("[data-only]", s).forEach((e) => e.classList.toggle("on", String(e.dataset.only).split(",").includes(String(step))));
    s.classList.toggle("dimming", s.hasAttribute("data-dim") && step > 0);
    $$("[data-wheel][data-steps]", s).forEach((w) => { const list = w.dataset.steps.split(","); setWheel(w, step > 0 ? list[Math.min(step, list.length) - 1] : w.dataset.active || ""); });
    $$("[data-radar]", s).forEach((r) => drawRadar(r, animate));
    if (s.dataset.hook && hooks[s.dataset.hook]) hooks[s.dataset.hook](s, step, "step");
  }

  /* ── transitions ── */
  function originOf(sel, inSlide) {
    const t = sel && inSlide.querySelector(sel);
    if (!t) return null;
    const vis = inSlide.style.visibility; inSlide.style.visibility = "visible";
    const r = rectIn(t); inSlide.style.visibility = vis;
    return { x: r.x + r.w / 2, y: r.y + r.h / 2, r };
  }
  const T = {
    cut: () => Promise.resolve(),
    fade(a, b) { anim(a, [{ opacity: 1 }, { opacity: 0 }], { duration: 420, easing: "ease" }); return done(anim(b, [{ opacity: 0 }, { opacity: 1 }], { duration: 520, easing: "ease" })); },
    push(a, b, fwd) {
      const d = fwd ? 1 : -1;
      anim(a, [{ transform: "none" }, { transform: `translateX(${-d * 35}%) scale(.92)`, opacity: 0.2 }], { duration: 800, easing: EASE_IO });
      return done(anim(b, [{ transform: `translateX(${d * 100}%)` }, { transform: "none" }], { duration: 800, easing: EASE_IO }));
    },
    rise(a, b, fwd) {
      anim(a, [{ transform: "none", opacity: 1 }, { transform: `translateY(${fwd ? -12 : 12}%) scale(.96)`, opacity: 0 }], { duration: 700, easing: EASE_IO });
      return done(anim(b, [{ transform: `translateY(${fwd ? 100 : -100}%)` }, { transform: "none" }], { duration: 800, easing: EASE_IO }));
    },
    zoom(a, b, fwd) {
      // forward: dive into the element named by b.dataset.zoom inside slide a. backward: pull back out of it.
      const sel = fwd ? b.dataset.zoom : a.dataset.zoom;
      const o = fwd ? originOf(sel, a) : originOf(sel, b);
      const ox = o ? o.x : W / 2, oy = o ? o.y : H / 2, org = `${ox}px ${oy}px`;
      const deep = o ? Math.min(14, Math.max(4, (W / Math.max(40, o.r.w)) * 0.9)) : 1.35;
      if (fwd) {
        anim(a, [{ transform: "none", transformOrigin: org, opacity: 1, filter: "blur(0)" }, { transform: `scale(${deep})`, transformOrigin: org, opacity: 0, filter: "blur(6px)" }], { duration: 900, easing: EASE_IN });
        return done(anim(b, [{ transform: `scale(${o ? 1 / deep : 0.7})`, transformOrigin: org, opacity: 0 }, { transform: "none", transformOrigin: org, opacity: 1 }], { duration: 900, delay: 260, easing: EASE, fill: "backwards" }));
      }
      anim(a, [{ transform: "none", transformOrigin: org, opacity: 1 }, { transform: `scale(${o ? 1 / deep : 0.7})`, transformOrigin: org, opacity: 0 }], { duration: 700, easing: EASE_IN });
      return done(anim(b, [{ transform: `scale(${deep})`, transformOrigin: org, opacity: 0, filter: "blur(6px)" }, { transform: "none", transformOrigin: org, opacity: 1, filter: "blur(0)" }], { duration: 950, delay: 200, easing: EASE, fill: "backwards" }));
    },
    iris(a, b, fwd) {
      const sel = fwd ? b.dataset.zoom : null, o = sel ? originOf(sel, a) : null;
      const x = o ? o.x : W / 2, y = o ? o.y : H / 2;
      return done(anim(b, [{ clipPath: `circle(0px at ${x}px ${y}px)` }, { clipPath: `circle(2300px at ${x}px ${y}px)` }], { duration: 1050, easing: EASE_IO }));
    },
    wipe(a, b, fwd) {
      return done(anim(b, [{ clipPath: fwd ? "inset(0 0 0 100%)" : "inset(0 100% 0 0)" }, { clipPath: "inset(0 0 0 0)" }], { duration: 900, easing: EASE_IO }));
    },
    morph(a, b) {
      // Magic-move: elements sharing data-m glide from their old box to their new one; the rest fades up.
      const pairs = [];
      $$("[data-m]", b).forEach((nb) => {
        const na = a.querySelector(`[data-m="${CSS.escape(nb.dataset.m)}"]`);
        if (na) pairs.push([na, nb]);
      });
      a.style.visibility = "visible";
      const ra = pairs.map(([na]) => ({ r: rectIn(na), cs: getComputedStyle(na) }));
      const rb = pairs.map(([, nb]) => rectIn(nb));
      const bgA = getComputedStyle(a).backgroundColor, bgB = getComputedStyle(b).backgroundColor;
      if (bgA !== bgB) anim(b, [{ backgroundColor: bgA }, { backgroundColor: bgB }], { duration: 900, easing: EASE_IO });
      const morphed = new Set(pairs.map((p) => p[1]));
      pairs.forEach(([na, nb], i) => {
        const A = ra[i].r, B = rb[i];
        const sx = A.w / Math.max(1, B.w), sy = A.h / Math.max(1, B.h);
        const uni = nb.hasAttribute("data-mu");
        const S = uni ? `scale(${sy})` : `scale(${sx},${sy})`;
        const csB = getComputedStyle(nb);
        const kf0 = { transform: `translate(${A.x - B.x}px,${A.y - B.y}px) ${S}`, transformOrigin: "0 0" };
        const kf1 = { transform: "none", transformOrigin: "0 0" };
        if (ra[i].cs.color !== csB.color) { kf0.color = ra[i].cs.color; kf1.color = csB.color; }
        if (ra[i].cs.backgroundColor !== csB.backgroundColor) { kf0.backgroundColor = ra[i].cs.backgroundColor; kf1.backgroundColor = csB.backgroundColor; }
        if (ra[i].cs.opacity !== csB.opacity) { kf0.opacity = ra[i].cs.opacity; kf1.opacity = csB.opacity; }
        anim(nb, [kf0, kf1], { duration: 1000, easing: EASE_IO });
      });
      // non-morphing content of b: smallest blocks that hold no morph element
      const rest = [];
      const collect = (el) => [...el.children].forEach((c) => {
        if (c.classList.contains("foot") || c.classList.contains("notes") || c.classList.contains("fx")) return;
        if (morphed.has(c)) return;
        if ([...morphed].some((m) => c.contains(m))) collect(c); else rest.push(c);
      });
      collect(b);
      rest.forEach((c, i) => { if (!c.dataset.in && !c.dataset.k) anim(c, [{ opacity: 0, transform: "translateY(24px)" }, { opacity: 1, transform: "none" }], { duration: 650, delay: 380 + Math.min(i, 10) * 45, easing: EASE, fill: "backwards" }); });
      return new Promise((r) => setTimeout(r, 1000));
    },
  };

  function go(n, opts = {}) {
    if (n < 0 || n >= slides.length) return;
    if (overview) { exitOverview(n); return; }
    if (n === idx && !opts.force) return;
    anims.forEach((a) => { try { a.finish(); } catch (e) {} }); anims = [];
    const a = slides[idx], b = slides[n], fwd = n > idx;
    leave(a);
    slides.forEach((s) => s.classList.remove("leaving"));
    a.classList.remove("current"); a.classList.add("leaving");
    idx = n;
    step = opts.toEnd ? maxStep(b) : 0;
    $$("[data-step]", b).forEach((e) => e.classList.remove("shown"));
    b.classList.add("current");
    applySteps(b, false);
    const kind = RM ? "fade" : (fwd ? b.dataset.t : a.dataset.t) || "fade";
    const tr = (T[kind] || T.fade)(a, b, fwd);
    const base = { zoom: fwd ? 650 : 500, morph: 300, iris: 350, push: 450, rise: 450, wipe: 400 }[kind] ?? 200;
    enter(b, base);
    tr.then(() => { if (slides[idx] !== a) { a.classList.remove("leaving"); a.style.visibility = ""; } });
    if (!timerOn && idx > 0) startTimer();
    sync();
  }
  function next() {
    if (overview) return;
    const s = slides[idx];
    if (step < maxStep(s)) { step++; applySteps(s, true); sync(); }
    else go(idx + 1);
  }
  function prev() {
    if (overview) return;
    const s = slides[idx];
    if (step > 0) { step--; applySteps(s, false); sync(); }
    else go(idx - 1, { toEnd: true });
  }

  /* ── overview: contact sheet zoom-out ── */
  function enterOverview() {
    overview = true; stage.classList.add("overview");
    const n = slides.length, cols = Math.ceil(Math.sqrt(n * 1.25)), rows = Math.ceil(n / cols), gap = 28, padX = 70, padY = 60;
    const s = Math.min((W - padX * 2 - gap * (cols - 1)) / cols / W, (H - padY * 2 - gap * (rows - 1)) / rows / H);
    const offX = (W - (cols * W * s + gap * (cols - 1))) / 2, offY = (H - (rows * H * s + gap * (rows - 1))) / 2;
    slides.forEach((sl, i) => {
      const c = i % cols, r = Math.floor(i / cols);
      sl.style.transformOrigin = "0 0";
      sl.style.transform = `translate(${offX + c * (W * s + gap)}px,${offY + r * (H * s + gap)}px) scale(${s})`;
    });
    $$("[data-step]").forEach((e) => e.classList.add("shown"));
    sync();
  }
  function exitOverview(n) {
    overview = false;
    const target = n ?? idx;
    slides.forEach((sl) => { sl.style.transform = ""; });
    setTimeout(() => {
      stage.classList.remove("overview");
      slides.forEach((sl) => { sl.style.transformOrigin = ""; });
      if (target !== idx) go(target, { force: true }); else { $$("[data-step]", slides[idx]).forEach((e) => e.classList.remove("shown")); step = 0; applySteps(slides[idx], false); enter(slides[idx], 0); }
      sync();
    }, RM ? 0 : 700);
  }

  /* ── ambient canvases (helix / net / rings) ── */
  const fxRuns = new Map();
  function startFx(s) {
    $$("canvas.fx", s).forEach((cv) => {
      if (fxRuns.has(cv)) return;
      const ctx = cv.getContext("2d"); cv.width = W; cv.height = H;
      const kind = cv.dataset.fx, rnd = mulberry(7);
      const pts = Array.from({ length: 70 }, () => ({ x: rnd() * W, y: rnd() * H, vx: (rnd() - 0.5) * 0.35, vy: (rnd() - 0.5) * 0.35, hot: rnd() > 0.9 }));
      let t0 = performance.now(), live = true;
      const draw = (t) => {
        if (!live) return;
        const T = Math.max(0, (t - t0) / 1000);
        ctx.clearRect(0, 0, W, H);
        if (kind === "helix") helix(ctx, T, cv.dataset.x ? +cv.dataset.x : 1450);
        else if (kind === "net") net(ctx, pts);
        else if (kind === "rings") rings(ctx, T);
        if (!RM) requestAnimationFrame(draw);
      };
      requestAnimationFrame(draw);
      fxRuns.set(cv, () => { live = false; });
    });
  }
  function stopFx(s) { $$("canvas.fx", s).forEach((cv) => { const k = fxRuns.get(cv); if (k) { k(); fxRuns.delete(cv); } }); }
  function mulberry(a) { return () => { a |= 0; a = (a + 0x6d2b79f5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a); t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296; }; }
  function helix(ctx, T, cx) {
    const turns = 34, amp = 190, top = -60, span = H + 120;
    for (let i = 0; i < turns; i++) {
      const y = top + (i / turns) * span, ph = i * 0.42 + T * 0.7;
      const x1 = cx + Math.sin(ph) * amp, x2 = cx + Math.sin(ph + Math.PI) * amp, z1 = Math.cos(ph), z2 = Math.cos(ph + Math.PI);
      ctx.strokeStyle = `rgba(232,236,239,${0.06 + 0.06 * (1 + Math.min(z1, z2))})`; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.moveTo(x1, y); ctx.lineTo(x2, y); ctx.stroke();
      [[x1, z1, i % 7 === 0], [x2, z2, false]].forEach(([x, z, hot]) => {
        ctx.fillStyle = hot ? `rgba(255,91,31,${0.55 + 0.35 * z})` : `rgba(76,125,255,${0.35 + 0.35 * z})`;
        ctx.beginPath(); ctx.arc(x, y, 5 + 3 * z, 0, Math.PI * 2); ctx.fill();
      });
    }
  }
  function net(ctx, pts) {
    pts.forEach((p) => { p.x += p.vx; p.y += p.vy; if (p.x < 0 || p.x > W) p.vx *= -1; if (p.y < 0 || p.y > H) p.vy *= -1; });
    for (let i = 0; i < pts.length; i++) for (let j = i + 1; j < pts.length; j++) {
      const d = Math.hypot(pts[i].x - pts[j].x, pts[i].y - pts[j].y);
      if (d < 210) { ctx.strokeStyle = `rgba(76,125,255,${(1 - d / 210) * 0.32})`; ctx.lineWidth = 1.4; ctx.beginPath(); ctx.moveTo(pts[i].x, pts[i].y); ctx.lineTo(pts[j].x, pts[j].y); ctx.stroke(); }
    }
    pts.forEach((p) => { ctx.fillStyle = p.hot ? "rgba(255,91,31,.85)" : "rgba(232,236,239,.5)"; ctx.beginPath(); ctx.arc(p.x, p.y, p.hot ? 5 : 3.2, 0, Math.PI * 2); ctx.fill(); });
  }
  function rings(ctx, T) {
    const cx = W * 0.72, cy = H * 0.5;
    for (let k = 0; k < 7; k++) {
      const r = ((T * 90 + k * 160) % 1120);
      ctx.strokeStyle = `rgba(255,91,31,${0.28 * (1 - r / 1120)})`; ctx.lineWidth = 2;
      ctx.beginPath(); ctx.arc(cx, cy, r, 0, Math.PI * 2); ctx.stroke();
    }
    ctx.strokeStyle = "rgba(232,236,239,.12)"; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(cx, cy); ctx.lineTo(cx + Math.cos(T * 1.2) * 1100, cy + Math.sin(T * 1.2) * 1100); ctx.stroke();
  }

  /* ── CSF 2.0 wheel (Govern at the core, five functions around it) ── */
  const FUNCS = [["ID", "IDENTIFY"], ["PR", "PROTECT"], ["DE", "DETECT"], ["RS", "RESPOND"], ["RC", "RECOVER"]];
  function arc(cx, cy, r0, r1, a0, a1) {
    const p = (r, a) => `${(cx + r * Math.cos(a)).toFixed(1)},${(cy + r * Math.sin(a)).toFixed(1)}`;
    const L = a1 - a0 > Math.PI ? 1 : 0;
    return `M${p(r1, a0)} A${r1},${r1} 0 ${L} 1 ${p(r1, a1)} L${p(r0, a1)} A${r0},${r0} 0 ${L} 0 ${p(r0, a0)} Z`;
  }
  function buildWheel(el) {
    const dark = !!el.closest(".dark"), five = el.dataset.mode === "five";
    const r0 = five ? 150 : 200, r1 = 470, seg = (Math.PI * 2) / 5, g = 0.03;
    let s = `<svg viewBox="-500 -500 1000 1000" role="img" aria-label="NIST CSF 2.0 functions wheel"><defs>`;
    FUNCS.forEach(([c], i) => {
      const a0 = -Math.PI / 2 - seg / 2 + i * seg + g, a1 = a0 + seg - 2 * g, rm = (r0 + r1) / 2 - 14;
      const flip = Math.sin((a0 + a1) / 2) > 0.2;
      const A0 = flip ? a1 : a0, A1 = flip ? a0 : a1;
      s += `<path id="${el.id || "w"}-${c}" d="M${rm * Math.cos(A0)},${rm * Math.sin(A0)} A${rm},${rm} 0 0 ${flip ? 0 : 1} ${rm * Math.cos(A1)},${rm * Math.sin(A1)}"/>`;
    });
    s += `</defs>`;
    FUNCS.forEach(([c, name], i) => {
      const a0 = -Math.PI / 2 - seg / 2 + i * seg + g, a1 = a0 + seg - 2 * g;
      const flip = Math.sin((a0 + a1) / 2) > 0.2;
      s += `<g class="seg" data-seg="${c}"><path d="${arc(0, 0, r0, r1, a0, a1)}" stroke-width="3"/>` +
        `<text font-size="44" text-anchor="middle" dy="${flip ? 30 : 0}"><textPath href="#${el.id || "w"}-${c}" startOffset="50%">${name}</textPath></text>` +
        `<text class="code" font-size="30" font-family="Plex Mono, monospace" text-anchor="middle" x="${((r0 + r1) / 2 + 70) * Math.cos((a0 + a1) / 2)}" y="${((r0 + r1) / 2 + 70) * Math.sin((a0 + a1) / 2) + 10}" style="letter-spacing:.05em;font-weight:500">${c}</text></g>`;
    });
    if (!five) s += `<g class="seg" data-seg="GV"><circle r="${r0 - 22}" stroke-width="3"/><text font-size="${r0 > 180 ? 56 : 40}" text-anchor="middle" dy="18">GOVERN</text><text class="code" font-size="30" text-anchor="middle" dy="66" font-family="Plex Mono, monospace" style="font-weight:500">GV</text></g>`;
    else s += `<circle r="${r0 - 22}" fill="none" stroke="${dark ? "rgba(232,236,239,.25)" : "#CBD3DA"}" stroke-width="3" stroke-dasharray="10 12"/>`;
    s += `</svg>`;
    el.innerHTML = s;
    el.__dark = dark;
    setWheel(el, el.dataset.active || "");
  }
  function setWheel(el, active) {
    const dark = el.__dark, act = String(active).split("+");
    $$(".seg", el).forEach((gp) => {
      const on = act.includes(gp.dataset.seg) || act.includes("ALL");
      const shape = gp.querySelector("path,circle");
      shape.setAttribute("fill", on ? (gp.dataset.seg === "GV" ? "#FF5B1F" : dark ? "#4C7DFF" : "#2448C2") : dark ? "#101E33" : "#FAFBFC");
      shape.setAttribute("stroke", on ? "transparent" : dark ? "rgba(232,236,239,.28)" : "#B9C3CC");
      $$("text", gp).forEach((t) => t.setAttribute("fill", on ? (gp.dataset.seg === "GV" ? "#0A1424" : "#FFFFFF") : dark ? "#E8ECEF" : "#0F1B2D"));
    });
  }
  $$("[data-wheel]").forEach(buildWheel);

  /* ── radar (tiers 1–4) ── */
  function drawRadar(el, animate) {
    const axes = el.dataset.axes.split(","), n = axes.length, R = 300, cx = 400, cy = 380;
    const sets = [["a", "#4C7DFF", "Current"], ["b", "#FF5B1F", "Target"]].filter(([k]) => el.dataset[k]).map(([k, col, lab]) => ({ k, col, lab, v: el.dataset[k].split(",").map(Number), at: +(el.dataset[k + "At"] || 0) }));
    const pt = (i, v) => { const a = -Math.PI / 2 + (i / n) * Math.PI * 2; return [cx + Math.cos(a) * R * (v / 4), cy + Math.sin(a) * R * (v / 4)]; };
    const dark = !!el.closest(".dark"), ln = dark ? "rgba(232,236,239,.18)" : "#CBD3DA", tx = dark ? "#E8ECEF" : "#0F1B2D", mt = dark ? "#8C9AAE" : "#55606E";
    let s = `<svg viewBox="0 0 800 780" role="img" aria-label="Profile radar: tiers by function">`;
    for (let t = 1; t <= 4; t++) s += `<polygon points="${axes.map((_, i) => pt(i, t).join(",")).join(" ")}" fill="none" stroke="${ln}" stroke-width="2"/><text x="${cx + 8}" y="${cy - (R * t) / 4 + 26}" fill="${mt}" font-size="22" font-family="Plex Mono, monospace">T${t}</text>`;
    axes.forEach((a, i) => { const [x, y] = pt(i, 4); const [lx, ly] = pt(i, 4.62); s += `<line x1="${cx}" y1="${cy}" x2="${x}" y2="${y}" stroke="${ln}" stroke-width="2"/><text x="${lx}" y="${ly + 10}" text-anchor="middle" fill="${tx}" font-size="30" font-family="Plex Mono, monospace" font-weight="500">${a}</text>`; });
    sets.forEach((st) => {
      const vis = step >= st.at;
      s += `<g class="rs" data-k="${st.k}" style="opacity:${vis ? 1 : 0};transform-origin:${cx}px ${cy}px"><polygon points="${st.v.map((v, i) => pt(i, v).join(",")).join(" ")}" fill="${st.col}" fill-opacity="${st.k === "a" ? 0.28 : 0.1}" stroke="${st.col}" stroke-width="5" ${st.k === "b" ? 'stroke-dasharray="14 10"' : ""}/>` +
        st.v.map((v, i) => `<circle cx="${pt(i, v)[0]}" cy="${pt(i, v)[1]}" r="9" fill="${st.col}"/>`).join("") + `</g>`;
    });
    s += `</svg>`;
    const prevVis = el.__vis || {};
    el.innerHTML = s;
    if (animate !== false) $$(".rs", el).forEach((g) => { const k = g.dataset.k, vis = g.style.opacity === "1"; if (vis && !prevVis[k] && !RM) g.animate([{ transform: "scale(0)", opacity: 0 }, { transform: "none", opacity: 1 }], { duration: 900, easing: POP }); });
    el.__vis = Object.fromEntries($$(".rs", el).map((g) => [g.dataset.k, g.style.opacity === "1"]));
  }
  window.Deck = { drawRadar, setWheel, buildWheel, go: (n) => go(n), next, prev, get index() { return idx; } };

  /* ── chrome ── */
  const hud = document.createElement("div"); hud.id = "hud";
  hud.innerHTML = `<button id="b-prev" aria-label="Previous">◀</button><span class="count tab" id="b-count"></span><button id="b-next" aria-label="Next">▶</button><button id="b-ov" aria-label="Overview">GRID</button><button id="b-notes" aria-label="Speaker notes">NOTES</button><button id="b-timer" aria-label="Timer">TIMER</button><button id="b-fs" aria-label="Fullscreen">FULL</button><button id="b-help" aria-label="Keyboard shortcuts">?</button>`;
  document.body.appendChild(hud);
  const prog = document.createElement("div"); prog.id = "progress"; document.body.appendChild(prog);
  const notes = document.createElement("div"); notes.id = "notes"; notes.hidden = true; document.body.appendChild(notes);
  const timer = document.createElement("div"); timer.id = "timer"; timer.hidden = true; document.body.appendChild(timer);
  const help = document.createElement("div"); help.id = "help"; help.hidden = true;
  help.innerHTML = `<div class="box"><div><kbd>→ / Space / click</kbd>next build or slide</div><div><kbd>←</kbd>back</div><div><kbd>G</kbd>or <kbd>Esc</kbd>grid overview (click a slide to zoom in)</div><div><kbd>N</kbd>speaker notes</div><div><kbd>T</kbd>session timer (${MINUTES} min)</div><div><kbd>F</kbd>fullscreen</div><div><kbd>B</kbd>black screen</div><div><kbd>Home / End</kbd>first / last slide</div><div><kbd>12 ⏎</kbd>jump to slide 12</div></div>`;
  document.body.appendChild(help);
  const black = document.createElement("div"); black.id = "blackout"; black.hidden = true; document.body.appendChild(black);

  function heading(s) { const h = s.querySelector(".h1,.h2,.mega,.quote,h1,h2"); return h ? (h.__orig || h.textContent).replace(/\s+/g, " ").trim().slice(0, 70) : ""; }
  function sync() {
    document.getElementById("b-count").textContent = `${pad2(idx + 1)} / ${pad2(slides.length)}`;
    prog.style.width = `${((idx + (maxStep(slides[idx]) ? step / (maxStep(slides[idx]) + 1) : 0)) / (slides.length - 1)) * 100}%`;
    if (!notes.hidden) {
      const n = slides[idx].querySelector(".notes"), nx = slides[idx + 1];
      notes.innerHTML = `<h4>Slide ${idx + 1}${maxStep(slides[idx]) ? ` · build ${step}/${maxStep(slides[idx])}` : ""}</h4>${n ? n.innerHTML : "<p>No notes.</p>"}${nx ? `<h4>Next · ${heading(nx) || "slide " + (idx + 2)}</h4>` : ""}`;
    }
    try { history.replaceState(null, "", `#s${idx + 1}`); } catch (e) {}
  }
  function startTimer() { timerOn = true; timerStart = performance.now(); }
  setInterval(() => {
    if (timer.hidden) return;
    const el = timerOn ? (performance.now() - timerStart) / 1000 : 0, left = MINUTES * 60 - el;
    const f = (x) => `${pad2(Math.floor(Math.abs(x) / 60))}:${pad2(Math.floor(Math.abs(x) % 60))}`;
    timer.innerHTML = `${f(el)}<span class="left">${left < 0 ? "+" : "−"}${f(left)}</span>`;
  }, 500);

  const toggle = (el) => { el.hidden = !el.hidden; sync(); };
  const fs = () => { try { if (!document.fullscreenElement) document.documentElement.requestFullscreen().catch(() => {}); else document.exitFullscreen(); } catch (e) {} };
  document.getElementById("b-prev").onclick = (e) => { e.stopPropagation(); prev(); };
  document.getElementById("b-next").onclick = (e) => { e.stopPropagation(); next(); };
  document.getElementById("b-ov").onclick = (e) => { e.stopPropagation(); overview ? exitOverview() : enterOverview(); };
  document.getElementById("b-notes").onclick = (e) => { e.stopPropagation(); toggle(notes); };
  document.getElementById("b-timer").onclick = (e) => { e.stopPropagation(); toggle(timer); };
  document.getElementById("b-fs").onclick = (e) => { e.stopPropagation(); fs(); };
  document.getElementById("b-help").onclick = (e) => { e.stopPropagation(); toggle(help); };
  help.onclick = () => toggle(help);
  black.onclick = () => (black.hidden = true);

  let numBuf = "";
  addEventListener("keydown", (e) => {
    if (e.target.closest && e.target.closest("input,textarea,select,[contenteditable]")) return;
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    const k = e.key;
    if (/^[0-9]$/.test(k)) { numBuf += k; return; }
    if (k === "Enter" && numBuf) { go(Math.min(slides.length, +numBuf) - 1); numBuf = ""; return; }
    numBuf = "";
    if (["ArrowRight", "ArrowDown", " ", "PageDown", "Enter"].includes(k)) { e.preventDefault(); next(); }
    else if (["ArrowLeft", "ArrowUp", "PageUp", "Backspace"].includes(k)) { e.preventDefault(); prev(); }
    else if (k === "Home") go(0);
    else if (k === "End") go(slides.length - 1);
    else if (k === "g" || k === "G" || k === "o" || k === "O") overview ? exitOverview() : enterOverview();
    else if (k === "Escape") { if (!help.hidden) help.hidden = true; else overview ? exitOverview() : enterOverview(); }
    else if (k === "n" || k === "N") toggle(notes);
    else if (k === "t" || k === "T") toggle(timer);
    else if (k === "f" || k === "F") fs();
    else if (k === "b" || k === "B" || k === ".") black.hidden = !black.hidden;
    else if (k === "?") toggle(help);
  });
  stage.addEventListener("click", (e) => {
    if (e.target.closest("input,button,select,textarea,a,label,[data-interactive]")) return;
    if (overview) { const s = e.target.closest(".slide"); if (s) exitOverview(slides.indexOf(s)); return; }
    const x = e.clientX / innerWidth;
    x < 0.22 ? prev() : next();
  });
  let tx = null;
  addEventListener("touchstart", (e) => { tx = e.touches[0].clientX; }, { passive: true });
  addEventListener("touchend", (e) => { if (tx == null) return; const d = e.changedTouches[0].clientX - tx; if (Math.abs(d) > 50) (d < 0 ? next : prev)(); tx = null; });
  let hudT = 0;
  addEventListener("mousemove", () => { body.classList.add("hud-on"); clearTimeout(hudT); hudT = setTimeout(() => body.classList.remove("hud-on"), 2600); });
  $$("video[data-next]").forEach((v) => v.addEventListener("ended", () => { if (slides[idx].contains(v)) next(); }));
  addEventListener("resize", fit);

  /* ── boot ── */
  fit();
  const m = /^#s(\d+)$/.exec(location.hash || "");
  idx = m ? Math.min(slides.length - 1, Math.max(0, +m[1] - 1)) : 0;
  slides[idx].classList.add("current");
  applySteps(slides[idx], false);
  enter(slides[idx], 200);
  sync();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => $$("[data-wheel]").forEach((w) => setWheel(w, w.dataset.active || "")));
})();
