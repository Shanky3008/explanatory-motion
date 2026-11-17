# Examples

Six small pages, no network, no external scripts. The easing code in them is a generated copy of `scripts/easing.mjs`
(`node scripts/sync_easing.mjs` rewrites it, `--check` fails on drift). Open them straight from disk.

| Page | Shows |
|---|---|
| `guided-path/before.html` | a water-cycle picture with every fault the guided-path reference warns about |
| `guided-path/after.html` | the same drawing as five numbered steps: reading order, one highlight, earlier steps dimmed, flow arrows, labels beside parts, reading-time holds, keyboard and reduced-motion support |
| `guided-path-heart/before.html` | a cut-open heart with the common faults: no order, pale colours, labels parked far from their parts with no leaders, a label sitting on a vessel it does not name |
| `guided-path-heart/after.html` | the same drawing as nine numbered steps in the true order of the blood (body, right atrium, right ventricle, pulmonary artery, lungs, pulmonary veins, left atrium, left ventricle, aorta), blue for oxygen-poor and red for oxygen-rich, each boxed label pointing at its own chamber, the loop closed by a dashed return; Previous, Next, Show all and arrow keys |
| `camera-move/before.html` | a camera move that is linear, too fast, aimed at the wrong thing, with no hold and a label that leads the move |
| `camera-move/after.html` | the same move with a hold on the whole scene, a smooth curve, zoom in log space, the subject landing at 62 % of frame height, the label arriving after the camera, and a speed graph |

Useful URL options: `?t=SECONDS` freezes the page at that time, `?t=end` shows the finished state, `?all=1` (guided path)
shows every step at once, `?step=3` (heart page) freezes on a step, `?guides=1` (camera page) draws the safe band and the subject box and the page prints the live
subject fill.
