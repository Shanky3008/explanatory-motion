---
name: explanatory-motion
description: Make explanatory motion: animated teaching pictures, interactive 3D or SVG lessons and short explainer videos that a learner understands with the sound off. Use whenever the user wants to animate a diagram or a process, show how a mechanism works, cut open or explode an object, number the steps of a sequence, add flow arrows, time labels and subtitles to narration, plan a camera move for an explainer, review a contact sheet or frame strip of one, or check that a picture is true to its source, even if they only say "animate this lesson", "make an explainer" or "this lesson looks flat". Not for interface micro-interactions, product-marketing animation, character animation, games or data dashboards. Gives a core loop (say what must be understood, stage, time, render, look, fix), three non-negotiables (truth before beauty, first-sight clarity, look before you claim), numeric references, checklists and tested helper scripts.
---

# Explanatory motion

Motion that teaches is different from motion that decorates. A learner who watches with the sound off must still see
*what* the thing is, *where* to look next, *in what order* things happen, and *which parts are simplified*. This skill
turns that into a loop you can run, numbers you can check, and review steps that catch the faults a correct-looking
result usually hides.

Use it for: animated diagrams, labelled cut-away pictures, interactive lessons in three.js or SVG, short narrated or silent
explainer films, picture sets for books or lessons, and the review of any of these. Do not use it for: product
marketing animation, interface micro-interactions with no teaching content (use a UI motion guide), character animation,
or game design.

## Non-negotiables

1. **Truth before beauty.** A picture must stay true to its source. Never prettier but wrong. Simplify only where you can
   mark the simplification. Refuse to stage what cannot be shown truthfully, and say so. Do not light one spot of a brain
   unless the script names it. When the words say "may", the picture must not look certain.
   (`references/truthfulness.md`, `checklists/truth-check.md`)
2. **First-sight clarity.** Judge the first three seconds, not only correctness: is the thing itself large, lit, in
   meaningful colour, with one path for the eye? Score it with the rubric before polishing anything.
   (`checklists/first-sight-look.md`)
3. **Look before you claim.** Open the result yourself: a contact sheet for stills, a frame strip for motion. A runner's
   "done" means it ran, not that it is good. Say what you did not look at.
   (`checklists/watch-in-motion.md`, `references/film-pipeline.md`)

## The core loop

1. **Say what must be understood.** Write one sentence per shot: "After this, the viewer knows that ___." If the source
   (a script, a text, a lesson) has claims you cannot picture truthfully, list them as "not pictured" now.
2. **Stage.** Choose the shot and the subject size, the palette (one hue, one meaning), the ground and light, the
   camera, and the path of the eye. Make stills first. (`staging-composition`, `colour-clarity`, `camera`, `guided-paths`)
3. **Time.** Set durations from distance and size, curves from the table, holds from the reading-time rule, label onsets
   from word timings. (`timing-easing`, `narration-sync`)
4. **Render.** Interactive: run the page. Film: render in resumable chunks, one headless browser at a time.
   (`film-pipeline`, `performance-budgets`, `interactive-vs-film`)
5. **LOOK.** Contact sheet of stills; frame strip of every shot; run the timing linter; read the result at the size a learner
   will see it. Score the rubric.
6. **Fix.** Fix the *worst* fault first (the rubric's one-sentence "worst fault"). Re-render only what changed, then look at
   what changed. Repeat until the rubric total is at least 14 of 16 and the truth check is clean.

Start small: one page or one shot, look at it, then scale to the batch. Before a large build, propose a few contrasting ways to picture the idea and let the user choose. Announce expensive builds before starting them.

## Decision table: what to read

| If you are about to... | Read |
|---|---|
| place the subject, choose frame size, lay out a first screen | `references/staging-composition.md` |
| choose colours, grounds, light, outlines, contrast, colour-blind safety | `references/colour-clarity.md` |
| set a duration, easing curve, stagger, hold, reading time, avoid strobing | `references/timing-easing.md` |
| choose a shot, move the camera, keep it out of walls | `references/camera.md` |
| number steps, draw flow arrows, light a sentence at a time, place labels | `references/guided-paths.md` |
| decide what you may simplify, how to mark it, when to refuse | `references/truthfulness.md` |
| align narration, labels and subtitles; safe areas | `references/narration-sync.md` |
| show the inside of something or how parts fit | `references/exploded-cutaway.md` |
| animate a graph, equation, geometry, chemistry, rays | `references/diagrams-maths-motion.md` |
| decide between an interactive lesson and a film; controls; first screen | `references/interactive-vs-film.md` |
| budget triangles, draw calls, pixel ratio, frame time, render time | `references/performance-budgets.md` |
| reduced motion, flashing, contrast, keyboard, captions | `references/accessibility.md` |
| render frames, encode, avoid piling up browsers, cache, hand over | `references/film-pipeline.md` |
| pick a library or tool and check its licence | `references/tools.md` |

Checklists (use them, tick them): `checklists/first-sight-look.md` (score), `checklists/pre-render-check.md`,
`checklists/watch-in-motion.md`, `checklists/truth-check.md`.

## The numbers most often needed

Full tables with reasons are in the references. Tag meanings: [E] published standard (named in the reference), [C] common
practice, [M] measured once in one setup (re-measure), [H] house rule to tune.

| What | Value |
|---|---|
| Subject in an establishing shot / close-up | 35-55 % of frame height / 55-70 % of frame width [H] |
| Model covers less than this of its stage = "a speck" | 6 % [H] |
| One shot lasts | 2.2-5.5 s [H] |
| Duration of a move | `lo + (hi - lo) * f^0.6` (f = travel / reference span); ui 0.15-0.6 s, scene 0.4-2.0 s, camera 0.4-2.4 s [H] |
| Exit versus entrance duration | 60-70 % [C] |
| Easing | spatial moves never linear; camera uses the symmetric `smooth` curve (peak 1.5 x average speed) [H] |
| Camera peak speed | under 1 frame width per second [H] |
| Quick cut with camera motion (a whip) | 0.2-0.3 s, then hold [H] |
| Reading time on screen | `0.6 + words / wps` s, minimum 1.2 s; wps 3.0 adult, 2.5 mixed, 2.0 children or second language [H] |
| Hold after something new arrives | at least max(0.5 s, reading time); the final shot rests about 1 s [H] |
| Tag (name label) | onset no earlier than its word (tolerance 0.1 s), visible 1.5 s or more, at most two at once [H] |
| Subtitles, wide | two lines or fewer; 42 characters per line; at most 20 characters per second for adults, 17 for children [C] (streaming timed-text style guides) |
| Subtitles, portrait | two lines or fewer; 28-32 characters per line [H] |
| Steps in one guided picture | 3 to 9; one highlight at a time; previous steps dimmed to 35-60 %, not hidden [H] |
| Meaning hues in one piece | five or fewer plus neutrals and one highlight [H] |
| Text contrast | 4.5 : 1 normal, 3 : 1 large text and meaningful graphics [E] (WCAG 1.4.3, 1.4.11) |
| Flashing | at most three flashes in any second [E] (WCAG 2.3.1) |
| Click and touch targets | at least 24 x 24 CSS px [E] (WCAG 2.5.8, AA); 44 x 44 where you can [E] (2.5.5, AAA) |
| Wide-frame text and key detail | inside the central 90 % [E] (EBU R 95 graphics-safe); portrait margins in `narration-sync.md` [C] |
| Device pixel ratio cap on integrated graphics and phones | 1.5 [C] |
| First-sight rubric to ship | 14 of 16, truth check clean [H] |
| Frame time | 16.7 ms at 60 fps, never over 33 ms on the weakest target [C] |
| Headless browsers at once | one, behind a lock; count before and after [H] |

## What to deliver

For a picture or lesson: the page or images, the contact sheet, the rubric score with the worst fault, the truth-check
result, and a **hand-over note** with three lists: what it shows, what it deliberately does not show (and why), and what you
did not look at.
For a film: the clip, the frame strips you reviewed with a verdict per strip, the linter output, ffprobe values, the same note.
Anything a viewer sees must carry no tool, model, voice, file or template wording.

## Scripts (small, dependency-light, tested)

Run `python scripts/selftest.py` to confirm they work on your machine (needs python, node, ffmpeg, and Pillow for the
contact sheet). Each prints `--help`.

| Script | Does |
|---|---|
| `scripts/contact_sheet.py` | contact sheet from a folder of stills, labelled by file name |
| `scripts/frame_strip.py` | N evenly spaced frames from a time window of a clip, tiled, with the time of each cell |
| `scripts/easing.mjs` (+ `easing.test.mjs`) | curves, duration-from-distance, reading time, peak-speed ratio, strobing check, camera path clearance and keep-in |
| `scripts/sync_easing.mjs` | keeps the easing code inlined in the example pages identical to `easing.mjs` (`--check` fails on drift) |
| `scripts/timing_lint.py` | checks tag and subtitle cues against word timings: tag before its word, too short, too fast, too many at once |

Examples (open in a browser, no network): `examples/guided-path/{before,after}.html`, `examples/guided-path-heart/{before,after}.html`
(a nine-step cut-open heart, the quality bar for a guided picture) and `examples/camera-move/{before,after}.html`. Add `?t=2.2` to freeze a page at a time, `?t=end` for the finished state,
on the camera page `?guides=1` to draw the safe band and subject box, and on the heart page `?step=3` to freeze on a step.

## Habits that prevent most failures

- Prefer a *small number of clear things* to a rich scene. If a part is not needed by the sentence, remove it.
- Make the scene a pure function of time (same `t`, same picture) so you can seek, cache, scrub and render the same way.
- Compute geometry from the rule (refraction, reflection, sums, trajectories) instead of placing it by hand; then a reviewer
  can recompute it.
- Name every shot and every part; never refer to a shot by number.
- Change libraries additively when others use them: add, never rename or remove.
- One headless browser at a time; test one page before a batch; keep jobs resumable; remove only your own processes.
- When a check passes, ask whether the check could have failed. Feed it a deliberately broken input once.
- Be honest about opinion: the numbers tagged [H] are starting points that worked in practice, not laws. Adjust them by looking.

## When the brief conflicts with a rule

If the user asks for something the rules advise against (a spinning logo, a pretty but wrong ray), say what the rule is and
why, offer the truthful alternative, and do what they decide unless it would mislead a learner about facts. Misleading a
learner is the one thing not to do on request.
