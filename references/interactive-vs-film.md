# Motion for interactive lessons versus film

The same idea needs different motion depending on whether the viewer controls it. Decide first. Tags: [E] standard,
[C] common, [H] house rule.

| | Film (a fixed clip) | Interactive lesson |
|---|---|---|
| Who sets the pace | you, from narration | the learner (play, pause, scrub, step) |
| Camera | scripted, always moving a little | user-driven with reset; scripted tours optional |
| Text | subtitles timed to words | persistent labels; reading time not enforced |
| Sound off | must still make sense (the premise of this skill) | must still make sense |
| First impression | the first shot | the first screen, before any interaction |
| Failure modes | too fast, tag early, camera through a wall | model tiny, stage buried under controls, motion hidden in a tab |
| Check by | frame strips, contact sheets | screenshots at several viewports, interaction script |

## 1. When motion belongs in a lesson at all
Motion teaches when the thing to learn is a change over time, a sequence, a rate, or a cause that is only visible in motion
(the order of a cycle, a wave moving, a slow travelling squeeze). It is decoration when the lesson is about shape,
position, structure or comparison at one moment. Do not add motion to a skeleton, a map, a bond angle or a chart. [H]

Check list by idea:
| Idea is motion (animate) | Idea is structure (leave still, offer a turn) |
|---|---|
| heartbeat and valve order, breathing, flow, nerve impulse, cell division, orbits, tectonics, water cycle, waves, engines, collisions | skeleton, anatomy of a joint, map layers, architecture, crystal lattice, orbitals, solids and conics |

## 2. Where the motion lives
- On the stage, not in a hidden tab. A lesson whose only motion is behind a secondary tab shows a still picture to everyone
  who never opens it. Measure: capture three screenshots 1 s apart at load; if 0.00 % of pixels change, nothing moves. [H]
- Starts playing, unless reduced-motion is set (section 4 of `accessibility.md`). Starts at a *named, meaningful still*
  when paused: mid-ejection for a heart, end of breath-in for a lung, start positions for planets. [H]
- Moves existing parts (position, rotation, scale about a pivot, tint). It does not rewrite geometry. [H]
- Pauses itself when the tab is hidden or the stage is off screen. [C]

## 3. Controls for any lesson that moves
- Play/Pause (a button with `aria-pressed`), speed (0.25x, 0.5x, 1x), a scrub slider, Space toggles when focus is in the
  control bar. [H]
- A phase name and one plain sentence under it; a small strip chart if a quantity matters (pressure, volume). [H]
- Reset view; step through the guided path with arrows. [H]
- All controls reachable by keyboard with visible focus, labelled for screen readers. [E]
- Time step capped (50 ms) so a slow device slows, not jumps. [C]

## 4. First screen of an interactive lesson
See `staging-composition.md` section 4. The model is visible, large and lit before the learner scrolls or touches
anything; controls fold behind one button; the stage fills the first screen. A lesson that opens on the back of the object
(the eye viewed from behind) wastes the first impression: open on the view that names the thing. [H]

## 5. Adding a look to many lessons at once
When you improve the look of a whole library, change it by configuration and one injected block, so everything outside the
block is byte-identical and the proof is cheap: strip the block and compare to the original. Never rename or remove a part,
control, label or text. If anything in the kit throws, it switches itself off and the lesson draws as before. [H]
Re-check each changed lesson in the same browser: no console error, same data object, same controls, same parts with the
same labels and sizes, median frame time within 10 % of the original. Feed the checker deliberately broken candidates and
confirm it fails each for the right reason before trusting it. [H]

Audit a library before fixing it: score every lesson with the first-sight rubric, then count faults by class (wrong ground,
washed light, speck-sized model, buried opening, sequence without a numbered path, labels). A typical result is one fault
repeated across hundreds of lessons (one ground, one light rig), which is fixed once in configuration by subject family,
not lesson by lesson. Keep the few lessons that already look right as the reference for the others. [H]

## 6. Additive changes only when others use your library
If other people film from, or build against, your asset library: add, never rename or remove an export, shot name, prop
name, effect name or story name. Optional parameters keep the old result by default. Regenerate the registry. [H]

## 7. Interactive and film from one scene
Write the scene as a pure function of time `scene.at(t)`: the same `t` twice gives the same picture. The interactive page
calls it with the clock; the film renderer calls it with frame times; seeking, scrubbing and caching are free. Idle
animations (blinks, sway) must also be functions of `t` with a fixed seed. [H]
