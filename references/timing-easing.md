# Timing and easing

Three separate tables follow because interface elements, objects in a scene and the camera behave differently. The code
for every curve and rule here is in `scripts/easing.mjs` (run `node scripts/easing.test.mjs` to see it pass).
Tags: [E] standard, [C] common practice, [H] house rule. The cubic-bezier curves in section 2 are the widely published
standard set used by the Material Design and CSS easing guidance; the names here are this skill's own.

## 1. How long should a move take
Duration grows with distance, but well under proportionally: a move twice as far should take noticeably less than twice
as long, because the eye needs a floor of time to register any move at all. The helper uses

    seconds = lo + (hi - lo) * f^0.6        f = travel / reference span, clamped to 0..1

Reference span: the viewport diagonal for interface moves, the frame width for scene moves and the camera. [H]

| Kind | lo | hi | Typical results |
|---|---|---|---|
| Interface element | 0.15 s | 0.60 s | 10 % of the screen: 0.26 s; 50 %: 0.45 s; full screen: 0.60 s |
| Object in a scene | 0.40 s | 2.00 s | quarter frame width: 1.1 s; full width: 2.0 s |
| Camera re-frame | 0.40 s | 2.40 s | quarter width: 1.3 s; one width: 2.4 s |

A leaving thing should not hold the viewer up, so give an exit less time than the matching entrance: about two thirds of it
(0.5-0.8 is fine). [C] Interface design guidance generally gives exits slightly less time than entrances; the exact ratio
is a house choice.

## 2. Curves
Anything that travels across the picture eases in and out, because a constant-speed move starts and stops dead and looks
mechanical. Reserve constant speed for what really is uniform: a wheel at a steady rate, a conveyor, a gauge filling evenly.

| Name here | Use for | cubic-bezier |
|---|---|---|
| glide | a label or object moving from one place to another on screen | (0.4, 0, 0.2, 1) |
| arrive | entrance: starts fast, lands softly | (0, 0, 0.2, 1) |
| leave | exit: starts gently, accelerates away | (0.4, 0, 1, 1) |
| settle | a strong landing for emphasis | (0.2, 0, 0, 1) |
| smooth | symmetric ease, simple to compute | smoothstep 3t^2 - 2t^3 |

Overshoot (going past the target and coming back) suggests elasticity. In a teaching picture that is a claim: do not give a
rigid part, a pointer or an organ an overshoot unless the real thing springs. Allowed: a few percent on labels and badges;
more only in playful, clearly non-physical interface chrome. [H]

Peak speed matters as much as duration. Peak speed = ratio x (distance / duration). Measured with `peakSpeedRatio`:
smooth 1.5, leave 1.7, glide 2.7, settle 4.1, arrive 4.8. So a gentle symmetric curve (smooth) suits the camera, and the
punchy curves (glide, arrive, settle) suit short moves of labels and objects. Keep the peak of any camera move under 1 frame
width per second and the peak of a followed object under about 0.8 frame widths per second, or the eye loses it. Example: a
camera move of 0.6 frame widths in 1.4 s with smooth peaks at 1.5 x 0.43 = 0.64 frame widths per second (fine); with glide
it would peak at 2.7 x 0.43 = 1.16 (too fast, lengthen it). [H]

## 3. Reading time (the rule for how long text and labels stay)

    seconds_on_screen >= 0.6 + words / wps

| Audience | wps (words per second) |
|---|---|
| fluent adult readers | 3.0 |
| mixed or unknown audience (default) | 2.5 |
| children or readers in a second language | 2.0 |

Minimum for any text: 1.2 s. A single formula or symbol group: 1.5 s plus 0.5 s per extra term. A name tag of 1-3 words:
at least 1.5 s. [H] (adult fluent reading is roughly 3.3-4 words per second on paper; text next to moving pictures is
read more slowly because attention is split, so the table is deliberately lower.)

Worked example: caption "The warm water rises as vapour" (6 words), mixed audience: 0.6 + 6/2.5 = 3.0 s on screen. If
narration reads it in 2.2 s, the text still stays 3.0 s, but never starts before the narrated word (see `narration-sync.md`).

Subtitles also obey a rate cap: no more than about 17 characters per second for children, 20 for adults, two lines at most,
and a line break never inside a name or between a preposition and its noun. [C]

## 4. Holds
After something new has finished arriving, leave it unchanged for max(0.5 s, reading time of whatever it carries)
before the next change begins. A viewer needs roughly 0.4-0.7 s just to find a new object. A sequence that never holds
reads as a blur, however correct each step is. Let the final shot settle and rest for about a second so the last idea has
time to land. [H]

## 5. Stagger and how much moves at once
- Items entering one after another: 30-80 ms between starts, and let a whole interface list finish in about half a second
  so it never drags. For scene steps tied to narration, the narration sets the gaps instead. [C]
- Beyond the camera's own drift, at most two things should be in motion at the same moment; a third pulls the eye away
  from the one that matters. [H]
- A move longer than about half the frame needs a visible intermediate cue (a trail, a change of tone, a cut) so the eye
  can follow it. [H]
- Ambient motion (a faint drift, a slow shimmer) must be slower and fainter than the main motion, never competing. [C]
- Change at most two properties of one element at a time (for example position and tint); more than that reads as noise. [H]

## 6. Interface elements (labels, badges, panels, controls)
| Element | Duration | Notes |
|---|---|---|
| response to a pointer or key | starts within 100 ms | later than that is felt as lag [C] |
| control settling after a press | 150-250 ms | |
| tag or label fade in | 120-250 ms | fully visible when its word is spoken, not before |
| numbered badge appearing | 200-300 ms | scale 0.85 to 1, arrive curve |
| panel or drawer | 250-450 ms | glide |
| change of view | 400-700 ms | |
| previous-step dimming | 250-350 ms | to 35-60 % opacity, not to invisible |

## 7. Objects in a scene
| Thing | Rule |
|---|---|
| Arrow or line drawing itself along a path | grow from the tail at constant speed; length of 0.3 frame widths takes 0.6-1.0 s |
| Beads or particles following a flow | 0.15-0.4 frame widths per second; the eye must be able to follow one bead |
| Number of simultaneous flow particles | 14-300; fewer, larger, slower beats many tiny ones; cap and instance |
| Colour or glow change on a part | 0.3-0.6 s up, a little longer down |
| Cut-open or explode | 1.0-1.6 s with glide; outer parts lead |
| Rotating machine part | at most 1 turn per second on screen; show faster real speeds slowed, with a readout |
| A periodic real process (a heartbeat 75 per minute) | show at 0.25-0.5 of real speed with a speed control; label the speed |
| Slow motion | the same action with longer times, never a second hand-made animation |

## 8. Temporal aliasing (strobing)
Repeating patterns (road bumps, wheel spokes, escalator steps) strobe or appear to run backwards when their per-frame
step is wrong. Let `s` be the spacing of the pattern and `v` the speed; the per-frame step is `v / (fps * s)` in
spacings. Keep it under one third of a spacing, or just above a whole number (fraction 0.1-0.25, so the pattern drifts
slowly forward). Avoid fractions near 0.5. `aliasStep` in the helper reports it. Example: stripes 0.5 m apart at 30 fps:
a speed of 18 m/s gives 1.2 spacings per frame, fraction 0.2: reads as steady forward motion. At 15 m/s it is exactly
1.0 and the stripes look frozen; at 16.25 m/s it is 1.083 and slowly forward; at 22.5 m/s it is 1.5 and flickers. [H]

## 9. Frame rate
24-30 fps for explanatory video is enough; use 30 for text and diagrams. Constant frame rate. For interactive pages use
the display rate but make every animation a function of elapsed time, with the time step capped (50 ms) so a slow device
slows the motion instead of jumping it. [C]
