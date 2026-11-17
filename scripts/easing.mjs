// easing.mjs - curves, duration rules, strobing check and camera clearance check.
// Plain ES module, no dependencies. Import in node or in a browser page served over http.
// Rules and reasons: references/timing-easing.md and references/camera.md.

export const clamp = (x, lo = 0, hi = 1) => Math.min(hi, Math.max(lo, x));

// ---- curves: each maps t in [0,1] to progress in [0,1] -------------------
export const linear = (t) => t;
export const smoothstep = (t) => { t = clamp(t); return t * t * (3 - 2 * t); };
export const smootherstep = (t) => { t = clamp(t); return t * t * t * (t * (6 * t - 15) + 10); };
export const easeInOutCubic = (t) => { t = clamp(t); return t < 0.5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2; };

// CSS-style cubic-bezier(x1, y1, x2, y2), solved for x by Newton steps with a bisection fallback.
export function cubicBezier(x1, y1, x2, y2) {
  const cx = 3 * x1, bx = 3 * (x2 - x1) - cx, ax = 1 - cx - bx;
  const cy = 3 * y1, by = 3 * (y2 - y1) - cy, ay = 1 - cy - by;
  const X = (s) => ((ax * s + bx) * s + cx) * s;
  const Y = (s) => ((ay * s + by) * s + cy) * s;
  const dX = (s) => (3 * ax * s + 2 * bx) * s + cx;
  return (t) => {
    t = clamp(t);
    let s = t;
    for (let i = 0; i < 8; i++) {
      const err = X(s) - t;
      if (Math.abs(err) < 1e-7) return Y(s);
      const d = dX(s);
      if (Math.abs(d) < 1e-6) break;
      s -= err / d;
    }
    let lo = 0, hi = 1; s = t;
    for (let i = 0; i < 40; i++) { const e = X(s) - t; if (Math.abs(e) < 1e-7) break; if (e > 0) hi = s; else lo = s; s = (lo + hi) / 2; }
    return Y(s);
  };
}

// Named curves used by this skill (see the table in timing-easing.md).
export const EASE = {
  glide: cubicBezier(0.4, 0, 0.2, 1),   // on-screen move from A to B
  arrive: cubicBezier(0, 0, 0.2, 1),    // entrance
  leave: cubicBezier(0.4, 0, 1, 1),     // exit
  settle: cubicBezier(0.2, 0, 0, 1),    // strong landing
  smooth: smoothstep,
  linear,
};

// ---- how long: duration from travel ---------------------------------------
const KINDS = { ui: [0.15, 0.60], scene: [0.40, 2.00], camera: [0.40, 2.40] };
// travel fraction f = distance / reference span (viewport diagonal for ui, frame width for scene and camera).
export function travelSeconds(f, kind = 'ui') {
  const [lo, hi] = KINDS[kind] || KINDS.ui;
  return lo + (hi - lo) * Math.pow(clamp(f), 0.6);
}
export const exitSeconds = (enterSeconds) => enterSeconds * 0.65;

// ---- how long text stays ----------------------------------------------------
const WPS = { adult: 3.0, mixed: 2.5, learner: 2.0 };
export function readingSeconds(words, audience = 'mixed') {
  const wps = typeof audience === 'number' ? audience : (WPS[audience] || WPS.mixed);
  return Math.max(1.2, 0.6 + words / wps);
}
export const countWords = (s) => (String(s).trim().match(/\S+/g) || []).length;

// ---- peak speed of a curve relative to its average speed -------------------
export function peakSpeedRatio(fn, n = 2000) {
  let m = 0;
  for (let i = 0; i < n; i++) m = Math.max(m, (fn((i + 1) / n) - fn(i / n)) * n);
  return m;
}

// ---- strobing of repeating patterns ----------------------------------------
// speed and spacing in the same length unit, speed per second.
export function aliasStep(speed, spacing, fps = 30) {
  const perFrame = speed / (fps * spacing);
  const frac = Math.round((perFrame - Math.floor(perFrame)) * 1e6) / 1e6;
  let verdict;
  if (perFrame < 1 / 3) verdict = 'ok: slow enough to follow';
  else if (frac < 0.05 || frac > 0.95) verdict = 'bad: pattern looks frozen';
  else if (frac >= 0.7) verdict = 'bad: pattern may look as if it runs backward';
  else if (frac > 0.3) verdict = 'bad: flicker (fraction near one half)';
  else verdict = 'ok: drifts slowly forward';
  return { perFrame, fraction: frac, verdict, ok: verdict.startsWith('ok') };
}

// ---- camera clearance --------------------------------------------------------
// pathFn(t) -> [x, y, z] for t in [0, duration]; boxes: [{min:[x,y,z], max:[x,y,z]}] (solid things, walls as thin boxes).
// Samples at hz; fails when the camera sphere (radius + margin) touches a box.
export function pathClearance(pathFn, boxes, { duration = 1, hz = 10, radius = 0.1, margin = 0.2 } = {}) {
  const hits = []; let minDistance = Infinity;
  const n = Math.max(1, Math.ceil(duration * hz));
  for (let i = 0; i <= n; i++) {
    const t = (i / n) * duration; const p = pathFn(t);
    boxes.forEach((b, k) => {
      let d2 = 0;
      for (let a = 0; a < 3; a++) { const v = p[a]; const d = v < b.min[a] ? b.min[a] - v : v > b.max[a] ? v - b.max[a] : 0; d2 += d * d; }
      const d = Math.sqrt(d2); minDistance = Math.min(minDistance, d);
      if (d < radius + margin) hits.push({ t: Math.round(t * 1000) / 1000, box: k, distance: Math.round(d * 1000) / 1000 });
    });
  }
  return { ok: hits.length === 0, hits, minDistance };
}

// Convenience: interpolate a value along a move with a curve.
export const lerp = (a, b, u) => a + (b - a) * u;
export function tween(from, to, seconds, curve = EASE.glide) {
  return (t) => lerp(from, to, curve(clamp(t / seconds)));
}

// ---- camera keep-in -----------------------------------------------------------
// pathFn(t) -> [x, y, z]; box: {min:[x,y,z], max:[x,y,z]} is the set the camera must stay inside (a room's shell, shrunk by
// the margin you want). Fails when the camera sphere (radius) leaves the box at any sample: the "camera outside the room" fault.
export function pathInside(pathFn, box, { duration = 1, hz = 10, radius = 0.1 } = {}) {
  const hits = [];
  const n = Math.max(1, Math.ceil(duration * hz));
  for (let i = 0; i <= n; i++) {
    const t = (i / n) * duration; const p = pathFn(t);
    for (let a = 0; a < 3; a++) {
      if (p[a] - radius < box.min[a] || p[a] + radius > box.max[a]) { hits.push({ t: Math.round(t * 1000) / 1000, axis: 'xyz'[a] }); break; }
    }
  }
  return { ok: hits.length === 0, hits };
}
