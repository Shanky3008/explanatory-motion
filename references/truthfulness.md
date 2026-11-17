# Truthfulness

A picture that is prettier but wrong is worse than no picture, because the learner trusts it. Explanatory motion carries
claims; this file says which claims you may simplify, which you may not, and when to refuse.

## 1. The three-way test for every thing in the frame
For each object, motion, colour and label ask:
1. **True** to the source (the text, the data, the physics)? Keep.
2. **Simplified** but not misleading? Keep, and *mark it* (section 4).
3. **Invented** (a stand-in made up on the spot) or **wrong**? Remove, redraw, or refuse.

## 2. May simplify (and mark)
- Scale: sizes compressed so everything fits (a far thing drawn only three times as far as the near one). Say "not to
  scale".
- Number of items: 14 particles standing for countless ones. Say "a few of the many".
- Geometry: a flat drawing of a solid shape; a circular orbit for a slightly oval one; bending drawn at one surface
  when the real thing bends at two. Say it.
- Speed: a heartbeat at half speed, a collision slowed. Show the speed on screen.
- Colour: conventional colours (blue and red for blood, false colour for energy). Add a legend line if the convention is
  not universal.
- Size of a change: a squash far larger than the real one to make it visible. Say "exaggerated".
- Stand-in shapes: a plain block for a muscle, a ball for a molecule. Fine if they are not mistaken for anatomy.

## 3. May not
- **Prettier but wrong.** A light ray bends only at a boundary between materials (never in mid-air); a reflection leaves from
  the face the light actually hit; an opaque block stops the ray; a ray hitting a mirror obeys angle in = angle out; a lens
  puts the image where the lens rule puts it.
- **Hand-placing what a rule gives.** Compute bends, image positions, trajectories, sums and areas from the rule and show
  the result; do not eyeball them. A reviewer can then recompute it. (Refraction by Snell's law, mirror images by
  reflecting the point, lens positions by the thin-lens rule, totals by the arithmetic.) In a worked-maths picture every
  printed line is recomputed by code.
- **Localising what the source does not localise.** If the text says "the brain", light the whole brain softly; do not
  light one spot unless the text names that part. If the text says a signal "may" reach somewhere, the picture must not look
  certain.
- **Certainty from hedged words.** "May", "can", "usually", "not completely": stage the weaker case as well (the eye half
  open), or show both outcomes, or use a visibly uncertain style (dashed, half intensity).
- **A different example from the text's.** If the text works through a die, draw the die; if it uses (1,2) and (4,6),
  use those points.
- **Mirrored sides.** Left and right of a body or a machine are its own, not the viewer's: in a front view of a heart, its right
  atrium is on the viewer's left. Label by the object's side, and check each label against the part its leader ends on.
- **A route more definite than the source.** If the text says "signals", a drawn path (brain, cord, muscle) is a claim the
  source did not make. Draw it only as far as the text names it, keep it faint and small, and mark it as ours. [H]
- **Wrong direction or sign.** Arrows for force, current, field, flow follow the convention and the physics; recompute
  directions (left-hand rule, current vs electron flow) and say which convention you use.
- **Invented mechanisms.** If the source does not give a mechanism, do not draw one. A claim like "felt time slows" cannot be
  pictured truthfully; show what can be shown (two ways of sitting through the same clock) or refuse.
- **Fake data.** A chart axis, a readout, a number that is invented. A number on screen is computed from the same data that
  produces the motion, not typed in separately.
- **Wrong spelling of the source's term**, or notation faults that change meaning (a subscript that drops the rest of the
  line, `x**2` printed as code).

## 4. How to mark "not to scale", "simplified", "exaggerated"
- One short plain line under the picture or in the corner at 60-70 % of the label size: "Not to scale. Colours show
  oxygen content." In a film, show it for at least its reading time when the picture first appears, or put it in the
  narration; always in the accessible text of an interactive lesson.
- State *what* is compressed, not just that something is: "the far goal is drawn three times as far as the ball".
- Put the same note into the file's metadata (a `shows` and a `does_not_show` field) so a reviewer sees both lists. [H]

## 5. When to refuse
Refuse (say so, do not stage) when:
- the claim cannot be pictured without inventing something the source does not say;
- the picture would have to localise or quantify what is unknown;
- the only way to make it look good is wrong geometry or wrong direction;
- the claim is a school simplification that is itself false (for example "the brain flips the image"): do not draw
  the false mechanism; mention in notes that the sentence is left undrawn and why.

A refusal is a deliverable: record the sentence, the reason, and what would be needed (a better source, a different
framing). "Not pictured" lists per piece are good practice and the reviewer reads them first.

## 6. Check once per piece
Run `checklists/truth-check.md`. A single failed item blocks release; it is not a score to average.

## 7. Worked example: a ray entering a glass block
Source says: light slows in glass and bends toward the normal. Staged: ray straight in air, kink exactly at the
entry face, shallower angle inside, kink again at the exit face, parallel to the original. Computed with Snell's law
(n = 1.5). Faults avoided: a kink before the face, a ray leaving from the wrong face, a bend with no normal drawn. Noted:
"angles drawn to the rule; block thickness exaggerated".
