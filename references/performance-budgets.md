# Performance budgets

Aim: a lesson that runs smoothly on a school laptop with integrated graphics and a mid-range phone. Tags: [C] common
practice, [M] measured once in one setup (treat as an example of scale and re-measure on your target), [H] house rule.

## 1. Budgets (starting points)
| Quantity | Budget | Notes |
|---|---|---|
| Frame time, interactive, integrated graphics | 16.7 ms for 60 fps, never over 33 ms (30 fps) | measure on the weakest target, not your own machine [C] |
| Script time while a motion plays | under 10 ms per second of animation for a simple lesson | one setup measured 1-9 ms/s for small anatomical models [M] |
| Draw calls per frame | under about 150 on integrated graphics, under 80 on low-end phones | merge static parts, instance repeated ones [C] |
| Triangles | under 150k integrated, under 60k low-end phone | [C] |
| Separate meshes (parts) | a few dozen is comfortable; past about 90, measure frame cost | an 89-part model needed checking [M] |
| Instanced particles | cap at 300 | beads, dust, flow [H] |
| Device pixel ratio | cap at 1.5 on integrated graphics and phones; 2 at most | `renderer.setPixelRatio(Math.min(devicePixelRatio, 1.5))` [C] |
| Shadow map | one light, 1024-2048 squared | [C] |
| Textures | power-of-two where possible, compress, reuse, under about 2 MB each for a lesson | [C] |
| Page weight added by a motion or look layer | under 10 % of the page's compressed size | [H] |
| First model frame | within 10 % of the page without the layer | [H] |
| Time to first interactive frame | under 3 s on the target laptop | [H] |
| Console errors | 0 | [H] |
| Network | none for a self-contained lesson (no CDN scripts) | [H] |

## 2. Tactics
- **Animate transforms, opacity and tint, not layout.** In SVG and CSS use `transform` and `opacity`; avoid animating
  width, height, top, left or filters on large areas. [C]
- **Instance and merge.** Identical small things (beads, tiles) are one instanced mesh; static background pieces are merged
  into one geometry. [C]
- **One light with shadows.** More shadow lights multiply cost. [C]
- **Post-processing is expensive.** Bloom and depth of field cost full-screen passes; use them only in film renders or on
  desktop-class devices, and half the resolution for bloom. Give each a switch; a lesson must look right with them off. [H]
- **Render on demand.** If nothing is moving, do not redraw. For static views draw once per input. [C]
- **Pause off screen and when hidden.** [C]
- **Cap the time step.** 50 ms. [C]
- **Avoid allocating each frame** (new vectors, new materials). Reuse. [C]
- **Level of detail.** A close view may use a detailed mesh; the establishing view a simplified one. [C]
- **Lazy-load** heavy, rarely used parts (a second model) after the first frame. [H]

## 3. Measuring
- Run a 3-second sampler: record frame intervals, report median and 95th percentile; run it at the weakest viewport
  and device pixel ratio you support. [H]
- Compare "with the layer" against "without" back to back, ten pairs, and use the median ratio; a single run on a busy
  machine lies. [H]
- Count what the renderer says it drew (`renderer.info.render.calls`, `.triangles`) and record it with the result. [C]
- Headless software rendering can run at 0.3-2 frames per second; in that case check motion by *stepping the clock and taking
  pictures*, not by watching, and say so in your report. [M]

## 4. Film render budgets (offline)
- Offline frame rendering of 1080 x 1920 in a headless browser ran at about 2-3.5 frames per second end to end on an
  integrated-graphics laptop (about 9-14 minutes for a 60 s clip), and 30-45 fps for draw-and-capture alone. Plan batches by
  those numbers and measure your own. [M]
- Disk: a 60 s portrait clip of JPEG frames is about 0.25 GB per copy; keep one copy of frames and delete caches once the
  clip is finished and copied out, unless re-timing is still likely. [M]
- Run one headless browser at a time; see `film-pipeline.md`. [H]

## 5. Budget the work, not only the frames
Estimate before starting. A labelled flat diagram is quick; a scene with several effects takes much longer; a whole machine
or building takes longer still. Say so to the person asking before you begin the expensive ones, and put the first rough
stills on screen early so you can look at the whole before polishing any part. [H]
