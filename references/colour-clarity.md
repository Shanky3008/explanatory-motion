# Colour and clarity

Colour in an explanation is a vocabulary. Pretty comes second. Tags: [E] standard, [C] common practice, [H] house rule.

## 1. One hue, one meaning
Write a palette table before drawing anything, and never break it inside one piece.

| Meaning | Hue family | Notes |
|---|---|---|
| carrier A (for example oxygen-rich blood, hot, forward) | warm red-orange | saturated, mid-light |
| carrier B (oxygen-poor blood, cold, return) | cool blue | saturated, mid-dark |
| something being added or acted on | one accent (amber or green) | at most one accent at a time |
| structure, background parts | desaturated tint of one neutral | keep below 35 % saturation |
| a signal travelling | small bright beads (gold) | beads, not glow over a whole region |

Rules [H]:
- Five or fewer meaning hues in one piece, plus neutrals and one highlight.
- The same hue means the same thing in the picture, the arrows, the labels and the badges.
- Colour that names a convention must follow the audience's convention (wire colours, chart signs, element colours).
  State the convention on the page when it is regional.
- Light one thing only. When two things glow the eye has no target, and neither is the point.

## 2. Grounds
- Light ground (off-white, L* above 90) suits cut-away diagrams with outlines: colours keep full strength and the
  outline carries the form. This is the look of a good printed plate.
- A dark studio ground suits glowing, self-lit or space subjects (a star, a working muscle, a screen). Tint the dark
  toward the subject's family; keep it above pure black so edges do not crush.
- Do not use one pale grey-teal box for every subject. A single stage for everything makes metal look like plastic,
  planets look like cream balls and glass vanish. Choose the ground from the subject (space dark, a valley under a sky,
  apparatus on a bench). [H]

## 3. Light
- One key light that gives shape (lit side, shaded side), a soft fill (about a quarter to a third of the key), a weak
  rim. Use near-white light so hues survive. [H]
- Exposure and tone-mapping must not push main surfaces to white. Test: sample the main object's brightest 5 % of
  pixels; if most are above 95 % luminance the scene is over-lit and meaning colours have bleached. [H]
- Reflections come from a map that matches the ground (soft boxes in a studio, a sky outdoors) so metal reads as
  metal and nothing mirrors a pale wall. [H]
- A light source in the scene (a sun, a bulb) should actually be the light, with other lights off. [H]
- Units of light intensity depend on the renderer and its colour-management mode; copy the *ratios* (key : fill : rim),
  then check by looking.

## 4. Outline and form
- Cut-away diagrams: a dark outline 0.3-0.8 % of the shorter frame side (3-8 px at 1080) around each major region, about
  half that for inner structure. Outline colour is a dark tint of the fill, not pure black, except on light grounds where
  near-black is fine. [H] Without an outline, pale and white parts vanish on a light ground (an eye, a strand of DNA, water,
  glass): outline every part whose fill is within about 15 % lightness of the ground.
- Cut faces (where the slice goes through) get a different tone from outside surfaces: lighter flesh tone, or a hatch.
- Three to five tone steps (lit, mid, shade, plus a cast shadow) are enough to read a solid. Smooth gradients add little at small size. [C]

## 5. Contrast [E]
- Normal text against its background: contrast ratio at least 4.5 : 1; large text (about 24 px or 19 px bold) and
  graphical marks that carry meaning: at least 3 : 1 (WCAG 2.x AA).
- Subtitles over moving pictures: light text with a dark edge (stroke of about 6-8 % of the text height) or a dark
  translucent box of 50-70 % opacity. A plain light text over a mid-brown floor is the weakest case; check there.
- Check on the lightest and the darkest part of the picture the text ever crosses, not on the average.

## 6. Colour-blind safety
About 1 man in 12 (8 %) and 1 woman in 200 has a red-green deficiency. [C]
- Never carry a two-way meaning with red versus green alone. Blue versus orange survives all common types.
- Pair colour with a second cue: number, shape, label, position, line style (solid versus dashed), arrowhead.
- Red versus blue (as in a circulation picture) works because the lightness also differs (blue darker). Check by
  converting a frame to grayscale: the two must still differ clearly, and labels must tell them apart anyway.
- A cheap test: desaturate the frame (ffmpeg `hue=s=0`) and see whether the story is still readable. [H]

## 7. Hue fidelity beats prettiness
A named material has a recognisable colour (keep its hue within about 20 degrees of the familiar one, on a hue wheel): gold is yellow-brown, not cream; the Sun is warm and self-lit; water is
blue-green with highlights. A reader who knows the subject will distrust the rest if the colour is wrong. If you stylise,
stylise consistently and say so. [H]

## 8. Worked example
Brief: show blood going round the body. Palette: blue (return), red (out), pale pink tissue, gold beads for the
"pump" signal, amber highlight for the active chamber. Ground: off-white. Outlines: dark tint of each fill. Labels:
cream boxes with dark ink, thin leader line to the part. Numbers 1-9 in badges coloured by the vessel they name.
Check: grayscale frame still shows blue-return darker than red-out; badges readable at 480 px wide.
