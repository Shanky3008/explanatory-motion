# Guided paths: numbered steps, flow arrows, sentence focus

A learner looking at a rich picture does not know where to start. A guided path gives the eye one route. The quality
bar this file encodes is a clean printed plate: light ground, saturated meaning colours, a cut-open view with outlines,
flow arrows, numbered badges, boxed labels, and exactly one path through them. Tags: [C] common, [H] house rule.

## 1. Anatomy of a guided picture
1. **Numbered badges** in reading order, 1 to N. Circles about 4-5 % of the shorter frame side across, filled with the
   colour of what they name, white numeral. [H]
2. **Boxed labels** next to each badge: rounded rectangle, light fill, dark ink, 1-3 words, uppercase or small caps for
   scan-ability. Thin leader line (1-2 px at 1080 wide) to the part, ending at the *edge* of the part, with a small
   arrowhead pointing at it. Keep the label off its part: in a box beside it, joined by the leader, so the part stays fully
   visible. [H]
3. **Flow arrows** along the route the stuff takes, drawn in the colour of what flows, with a visible head. Where flow
   is the lesson, add moving beads on top of the arrow. [H]
4. **One path**: the numbers must be followable without lifting your eye more than one hop. If the route loops (out and
   back), the loop is closed visually and the number sequence continues around it. The numbers follow the true order of the
   process, not the position on the screen, so the numbers need not rise steadily down the page (in the heart example step 6 is
   low on the right, step 7 sits above step 8, step 9 is at the top) and that is correct. Check the order by hand against the
   source. [H]
5. **Count**: 3 to 9 steps in one picture. More than nine: split into two pictures, or group (for example "steps 4-6" share
   one badge colour). Fewer than three is not a path. [H]

Worked example, water cycle, five steps: 1 sun warms the sea (amber badge), 2 vapour rises (pale blue, dashed
arrow, because vapour is not liquid water), 3 vapour cools into a cloud (grey-blue), 4 rain falls (blue, solid arrow),
5 water runs back to the sea (blue, solid). The arrow from 5 returns to the sea and the viewer sees the loop close.
See `examples/guided-path/after.html`, and `examples/guided-path-heart/after.html` for a nine-step cut-open example.

## 2. Revealing the sequence in order
- Reveal steps in the order of the numbers and of the narration, one at a time. Never show all badges at once and ask
  the viewer to find "step 1". [H]
- The current step is at full strength: badge, label and arrow all visible, its part highlighted (one highlight only).
  Previous steps stay on screen but dim to 35-60 % opacity: they remain as context and the route stays visible. Not hidden,
  not equal. [H]
- Next steps do not appear until their turn, except as a faint 10-15 % ghost if the viewer needs to see where the path will
  go. [H]
- Step timing: badge pop 0.25 s, arrow draw 0.8-1.2 s (constant speed), label fade 0.2 s starting as the word is spoken,
  then hold for the reading time of the label or caption (`timing-easing.md` section 3). A five-step path with 6-word
  captions takes about 5 x (1.0 + 3.0) = 20 s. [H]
- In an interactive version: Next/Previous buttons and keyboard arrows step through; a "show all" toggle displays the
  full dim-plus-current state; under reduced-motion the steps change without arrows drawing themselves. [H]

## 3. Sentence-by-sentence focus
For text beside a picture (books, lessons), each sentence should light the thing it talks about, and the change must be
*visible*:
- Between two sentences at least one part must change opacity by 30 points or more, or gain/lose the highlight. A change
  smaller than that is not noticed. [H]
- In six sentence taps in a section, no two consecutive states should look identical. Count distinct states
  automatically if you can (hash the opacity/filter of each part) and look at the ones that did not change. [H]
- A sentence with no pictured referent (a transition, a date, an etymology) keeps the previous state: it does not light
  something arbitrary. [H]
- Light the right part, not just a part. Check each sentence-to-part mapping once by reading them side by side. [H]
- The thing the text uses as its example is the thing drawn (the text says 12 = 3 x 4: draw 3 x 4, not 2 x 6). [H]
- A looped reveal (grid cells appearing row by row, then restarting) can be caught empty by a screenshot. Make the loop
  rest on the complete state for a moment, and capture stills at several times. [H]

## 4. Labels
- 1 to 3 tags per short film; at most two visible at once; each stays at least 1.5 s; inside one shot. [H]
- A tag names a thing the *first* time the narration says its word. If the first mention falls within 1.2 s of a cut, tag the
  next mention, or start the tag earlier in the same shot, or declare the word untagged. [H]
- Two labels never overlap; a label never sits on a line it does not name; no label runs off the frame. Automate the
  overlap check on label boxes: two rectangles overlap when `a.x < b.x + b.w && b.x < a.x + a.w && a.y < b.y + b.h && b.y < a.y + a.h`
  (take the boxes from `getBoundingClientRect` or `getBBox`, grown by 4 px so near-touching counts). [H]
- Nothing is lettered that the narration does not say; no stray template words ("Later example:", "category") and no
  raw code in a caption. [H]
- Label spelling follows the text it illustrates (one spelling per word across the piece). [H]

## 5. Diagrams that go wrong
- An unlabelled mark (a box, a bar) is either named or removed. [H]
- A connector line that runs into a digit, a label printed over a symbol, side numbers sitting on the lines they
  measure: move them beside. [H]
- A tree or flow where the line stops at the edge of the number, not through it. [H]
- Two sections that show the same picture, because the same drawing was reused with new labels. Redraw or merge. [H]

- Each label points at its own part. Read every label aloud with the part its leader ends on: "left ventricle ... the left
  ventricle". A swapped pair (two labels each pointing at the other's chamber) passes every automatic check and is wrong. [H]
- **Reference pictures can be wrong.** A picture you were given as the quality bar sets the look and the layout, not the
  facts. Check each label, arrow and colour in it against the source before copying its structure; correct it, do not inherit
  it. [H]

## 6. Interactive picture, quick checklist
badges numbered; reading order followed; path shown one step at a time; previous dimmed; flow arrows directed; one
highlight; labels beside parts; contrast 4.5 : 1; works with keyboard; reduced-motion shows the complete path statically.
