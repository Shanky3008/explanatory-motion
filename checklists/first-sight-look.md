# First-sight look rubric

Purpose: score the first impression, which is what a learner forms in the first three seconds and rarely revises. Correct
but ugly, or correct but unreadable, fails here.

## How to apply
1. Open the still (or the first screen) at a normal size. Do not zoom in. Look for three seconds.
2. Say aloud, before reading any label: "This is a ___ and it shows ___." If you cannot, score Form and Opening 0.
3. Score each line 0, 1 or 2 using the anchors. Judge the picture, not the effort.
4. Write the worst fault in one sentence. That sentence is the fix list.
5. A different person (or a fresh look next day) scores a sample to check your own scoring is not generous.

## Scores (0 bad, 1 passable, 2 good)
| Line | 0 | 1 | 2 |
|---|---|---|---|
| Setting: is the ground right for the subject | one pale box for everything; subject floats | acceptable, generic | ground fits (dark for space, sky for a valley, light plate for a cut-open diagram) |
| Form: recognisable objects, true colour and material | plain blobs; cannot tell what it is | recognisable with the labels | recognisable at once; materials look like themselves |
| Light: gives shape, keeps hue | washed to white, or flat grey | some shape, some bleaching | lit side and shaded side, hues intact, nothing clipped |
| Opening: the thing itself, large, first | under 6 % of the stage, or buried under controls | visible but small or half off screen | fills its stage, first screen shows it before controls |
| Labels: readable, name what they point at | missing, overlapping, or on the wrong thing | readable, a little crowded | readable at the target size, beside parts, leaders end at edges |
| Motion: does it move if the idea is motion (2 if the idea is not motion) | the idea is motion and nothing moves | moves only on demand or only turns | the right thing moves, clearly |
| Consistency: one product | different frame, type or label style | mostly consistent | identical frame, type, colours across the set |
| Path: if the idea is a sequence or a cycle, does the picture number it (2 if the idea is not a sequence) | a sequence or cycle with no numbered or directed path | steps numbered but hard to follow, or no arrows | numbered in the true order, one step lit at a time, arrows in the flowing colour |

Total out of 16.

## Decisions
| Total | Action |
|---|---|
| 14-16 | ship (after the truth check) |
| 10-13 | fix the worst fault, re-score |
| 0-9 | redo the staging; do not polish |

Any 0 in Form or Setting means fix before anything else, whatever the total. A *truth check* failure (see
`truth-check.md`) overrides every score.

## Measured helpers (not a substitute for looking)
- Fraction of the stage covered by the main object (pixels differing from the clear background): under 6 % is "small".
- Share of the stage visible on the first screen at 1366 x 768: under 62 % is "buried".
- Share of the object's brightest pixels above 95 % luminance: most of them means "washed out".
- Number of console errors: must be 0.

## Look as a learner, not as the author
- Squint or reduce the picture to 480 px wide: do the colours still separate? Does one thing stand out?
- Convert to grayscale: does the story survive?
- Look at the thumbnail beside three others in the set: does it look like one product?

## Worked example
A heart lesson opens on a pale grey-teal box with a small whitish heart low in it. Setting 0, Form 1, Light 0, Opening 0,
Labels 1, Motion 0 (it only turns), Consistency 1, Path 0 (the blood's route is a sequence and nothing is numbered): total 3 of 16.
Decision: redo staging. After: light ground, red and blue chambers, cut-open, numbered badges, beating on the stage: all
eight lines 2 = 16. (`examples/guided-path-heart/` shows both states.)
