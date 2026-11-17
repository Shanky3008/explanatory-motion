// Self-test for easing.mjs on tiny synthetic inputs. Run: node scripts/easing.test.mjs
import assert from 'node:assert/strict';
import * as E from './easing.mjs';

const near = (a, b, eps = 1e-3) => assert.ok(Math.abs(a - b) < eps, `${a} is not within ${eps} of ${b}`);

// every curve starts at 0, ends at 1
for (const [name, fn] of Object.entries(E.EASE)) { near(fn(0), 0); near(fn(1), 1); }
near(E.easeInOutCubic(0.5), 0.5); near(E.smoothstep(0.5), 0.5);
// glide is slower than linear at the start and monotonic
assert.ok(E.EASE.glide(0.1) < 0.1); assert.ok(E.EASE.arrive(0.1) > 0.1);
let prev = -1; for (let i = 0; i <= 100; i++) { const v = E.EASE.glide(i / 100); assert.ok(v >= prev - 1e-9); prev = v; }
// cubicBezier(0.25,0.25,0.75,0.75) is the identity
const id = E.cubicBezier(0.25, 0.25, 0.75, 0.75); near(id(0.3), 0.3, 1e-4);

// peak speed: smoothstep 1.5, linear 1
near(E.peakSpeedRatio(E.smoothstep), 1.5, 0.01); near(E.peakSpeedRatio(E.linear), 1, 0.01);
near(E.peakSpeedRatio(E.EASE.glide), 2.73, 0.1); assert.ok(E.peakSpeedRatio(E.EASE.arrive) > 4);

// travel duration: documented examples
near(E.travelSeconds(0.1, 'ui'), 0.263, 0.005);
near(E.travelSeconds(0.5, 'ui'), 0.447, 0.005);
near(E.travelSeconds(1, 'ui'), 0.6, 1e-9);
near(E.travelSeconds(0.25, 'scene'), 1.096, 0.005);
near(E.travelSeconds(0.25, 'camera'), 1.27, 0.01);
near(E.travelSeconds(1, 'camera'), 2.4, 1e-9);
assert.ok(E.travelSeconds(0.5, 'ui') > E.travelSeconds(0.25, 'ui'));
// doubling the distance adds less than double the time
assert.ok(E.travelSeconds(0.4, 'camera') < 2 * E.travelSeconds(0.2, 'camera'));
near(E.exitSeconds(1), 0.65);

// reading time: worked example from the reference (6 words, mixed audience = 3.0 s)
near(E.readingSeconds(6, 'mixed'), 3.0, 1e-9);
near(E.readingSeconds(1, 'adult'), 1.2, 1e-9);       // minimum of 1.2 s
near(E.readingSeconds(10, 'learner'), 5.6, 1e-9);
assert.equal(E.countWords('  the warm  water rises '), 4);

// aliasing: documented examples (spacing 0.5 m, 30 fps)
assert.equal(E.aliasStep(18, 0.5).ok, true);   near(E.aliasStep(18, 0.5).fraction, 0.2, 1e-6);
assert.equal(E.aliasStep(15, 0.5).ok, false);  assert.match(E.aliasStep(15, 0.5).verdict, /frozen/);
assert.equal(E.aliasStep(16.25, 0.5).ok, true);
assert.equal(E.aliasStep(22.5, 0.5).ok, false); assert.match(E.aliasStep(22.5, 0.5).verdict, /flicker/);
assert.equal(E.aliasStep(3, 0.5).ok, true);    // slow: 0.2 spacing per frame

// camera clearance: a path from x=-5 to x=5 through a wall at x=0 fails; a path that goes around passes
const wall = [{ min: [-0.1, 0, -2], max: [0.1, 3, 2] }];
const through = (t) => [-5 + 10 * t, 1.5, 0];
const r1 = E.pathClearance(through, wall, { duration: 1, hz: 50, radius: 0.1, margin: 0.2 });
assert.equal(r1.ok, false); assert.ok(r1.hits.length > 0);
const around = (t) => [-5 + 10 * t, 1.5, t < 0.5 ? 6 * (t * 2) : 6 * (2 - t * 2)];   // swings out to z=6 and back
const wall2 = [{ min: [-0.1, 0, -2], max: [0.1, 3, 2] }];
const r2 = E.pathClearance(around, wall2, { duration: 1, hz: 50 });
assert.equal(r2.ok, true, JSON.stringify(r2.hits.slice(0, 2)));


// keep-in: a path that ends outside the room fails; one that stays inside passes
const room = { min: [-5, 0, -4], max: [5, 3, 4] };
const leaves = (t) => [-4 + 12 * t, 1.5, 0];                       // ends at x = 8, outside the shell
const r3 = E.pathInside(leaves, room, { duration: 1, hz: 50 });
assert.equal(r3.ok, false); assert.equal(r3.hits[0].axis, 'x');
const stays = (t) => [-4 + 8 * t, 1.5, 0];
assert.equal(E.pathInside(stays, room, { duration: 1, hz: 50 }).ok, true);
assert.equal(E.pathInside((t) => [0, -0.2, 0], room).ok, false);   // under the floor

// tween
const tw = E.tween(10, 20, 2); near(tw(0), 10); near(tw(2), 20); near(tw(5), 20);
console.log('easing.test.mjs: all checks passed');
