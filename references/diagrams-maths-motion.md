# Diagrams and maths in motion

For 2D diagrams, graphs, equations and geometry. Manim (maths animation, Python) is a good tool; SVG with a timeline is
enough for most pictures. Tags: [C] common, [H] house rule.

## 1. Order of appearance is the argument
- Draw in the order the sentence is read: axes before the curve, the premise before the conclusion, the known before the
  unknown. [H]
- Things that are the *same object* move between states (a term slides across the equals sign and changes sign); do not
  fade one equation out and another in. Motion shows identity. [C]
- Each step holds for the reading time of what it adds (`timing-easing.md` section 3), plus 0.5 s. [H]
- One highlight at a time, in a fixed accent colour, and the same colour for the same quantity throughout (the radius is
  always amber). [H]

## 2. Graphs
- Axes and tick labels appear first (0.6-1.0 s), then the curve draws left to right at constant speed (not eased in the
  middle, because x is time-like), eased only at the first and last 10 %. [H]
- A moving point rides the curve and a live readout (x, y) follows it; the readout is computed from the same function, not
  typed. [H]
- Mark what the lesson cares about (a maximum, a root, an intercept) with a dot plus a label that appears when the
  narration reaches it. [H]
- Draw to scale. A triangle called "right-angled" must have a right angle at the printed size; a picture of "x = 3" must
  put the point where 3 is. [H]
- Keep the axis range stable while a curve is drawn; re-scaling mid-way destroys comparison. [H]

## 3. Geometry
- Construct from the rule: a bisector with its arcs, a tangent at one point, a reflection across a line. Show the
  construction steps as numbered steps (see `guided-paths.md`). [H]
- Auxiliary lines are dashed and lighter than the figure; the answer is solid and strong. [H]
- Side lengths and angle labels sit beside the sides, not on them; an angle arc has a radius of about 12 % of the shorter
  side. [H]
- When a figure is built up, every new element appears *where* it belongs, drawn from a point already on the figure. [H]

## 4. Equations and notation
- Typeset exponents and indices as real superscripts and subscripts, never `x**2`, `x^2` in a caption or `2*x`. A
  multiplication of a number and a letter is written `2x`, not `2 x x`. [C]
- **Baseline fault** (found in practice): after a superscript or subscript, the *rest of the line* stayed raised or lowered,
  so `ax^2 + bx + c` printed with `+ bx + c` floating high and `C2H6` lost its second H. In SVG, a `tspan` with `baseline-shift`
  or `dy` stays shifted for what follows it. An empty `tspan` to reset it moves nothing, because it has no glyphs. Reset
  on the *next visible glyphs* (give those glyphs the opposite shift) or close the shifted span and open a fresh `tspan`
  with its own absolute `dy`. Test with a line that has raised text in the middle and plain text after.
- A root sign over a single digit has no brackets: write sqrt(2) as the root sign and 2.
- Chemistry: use state symbols (s), (l), (g), (aq) where the text names states; subscripts on formulas; charges as
  superscripts; balance both sides and recompute the count of every element in code. Use one spelling per word, the
  source text's (sulfate or sulphate, not both).
- Units: a number with a unit takes a thin space and the unit upright. [C]
- Keep typefaces to one for text and one for maths. Maths: at least 24-42 px measured on a 1080-wide frame (shrink only to
  fit; check by looking at the phone-size crop). [H]

## 5. Chemistry and structure pictures
- Atoms: element colours follow a common convention (state the convention if unusual); size roughly with atomic radius (keep the order of sizes, ratios within about 30 % of the real ones) in
  a *relative* sense. [C]
- Bonds: lines for shared pairs; dots only where electrons matter; do not leave a stray dot (a lone electron) where the
  molecule has none. [H]
- Reactions: show the state change (a precipitate settling as a white solid) as well as the equation. [H]
- Show the shape claim only if you can show the shape (a flat drawing of a three-dimensional molecule is fine if marked). [H]

## 6. Rays and fields
- Lines drawn from a rule (see `truthfulness.md`), thick enough to read at phone size (3-4 px at 1080 wide for a ray, 5 px
  for a principal ray), and in saturated, *different* colours for different rays (incident, reflected, transmitted,
  shadow). [H]
- Never bend a ray in air. Never let a reflected ray leave from the unlit side. Draw the normal as a dashed line where the
  angle is measured. [H]
- A spectrum is shown as a fan from red to violet landing on a screen, violet bent most, not a grey band. [H]
- Magnetic and electric field lines start and end on the poles or charges and never cross; they do not appear to
  originate from the middle of a magnet. Add arrows. [H]

## 7. Data pictures
- Axis labels with units; zero baseline for bars; one accent for the series the lesson is about, neutrals for the rest. [C]
- Redraw rather than reuse a generic template with changed labels. [H]
