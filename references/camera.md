# Camera

A camera move in an explainer is a pointer: it tells the viewer where to look next. Move it only when the next
sentence is about somewhere else. Tags: [E] standard, [C] common practice, [H] house rule.

## 1. Shot types
Name every shot (`"overview"`, `"valve-close"`), never refer to shots by number: inserting a shot shifts the numbers
and silently re-points every later rule. [H]

| Shot | Size | Seconds | Subject takes | Use |
|---|---|---|---|---|
| establish | wide | 3.5-5 | 35-55 % of frame height (group) | where are we; slow sideways drift |
| low wide | wide | 3.5-5 | as above, camera near ground, sky fills top half | scale, awe, weather |
| medium | medium | 3-4.5 | head to knees, or one object with support | an action |
| push in | medium to close | 3-5 | ends 10-15 % tighter | the question, the face, "look closely" |
| close-up | close | 2.5-4.5 | 55-70 % of frame width | one object or face |
| cut-in (detail insert) | close | 2.2-3.5 | about 60 % of frame width, locked with 2 % push | a hand, a rim, one valve |
| low angle | medium | 3-5 | looking up | danger, climbing, power |
| top-down | overhead | 3.5-5 | camera 65-90 degrees above, slow 5 degree turn | layouts, flows, who stands where |
| orbit | medium | 4-5.5 | subject centred, camera arcs 20-40 degrees | show 3D form once |
| track | medium | 3-5 | subject held one third in from the edge while it travels | following |
| pull back | wide | 4-5.5 | starts close, ends 1.6-2.5 times farther and higher | the answer, the ending |
| dive in / rise out | close | 1.0-1.4 | push until the subject fills the frame; next shot starts inside it | enter or leave an object or body |
| over the shoulder | medium | 3-5 | a dark head in a lower corner, subject in the upper half | looking at what someone looks at |
| split focus | medium | 3-5 | near thing large one side, subject small other side | comparing near and far |

Over-the-shoulder is the easiest shot to get wrong: it puts a head in the corner and hides small things on a worktop. Use
it only when the subject is large and clear above the head. [H]

## 2. Move speeds
| Move | Rule |
|---|---|
| continuous push or pull | 5-15 % change of distance over the shot, i.e. 1-5 % per second |
| drift (never a frozen frame) | about 2 % of frame width over the shot |
| orbit | 20-40 degrees over 4-5.5 s, i.e. 5-9 degrees per second |
| re-frame to a new subject | duration from the camera row of `timing-easing.md`; peak under 1 frame width per second |
| whip or fast cut | 0.2-0.3 s with motion blur, then the picture holds: a whip is a cut with motion, not a slow pan [C] film convention |
| final shot | comes to rest and holds at least 1 s, longer if its last caption needs its reading time |

A held shot should not be a frozen image: a slow creep of a couple of percent keeps it alive, and only the closing shot rests.
A very slow drift beats a frozen frame; a visible move that starts and stops abruptly is worse than either. Ease both ends;
prefer the symmetric `smooth` curve for the camera (peak only 1.5 times the average speed). [H]

## 3. Establishing, then close
Order a sequence wide, medium, close, and return wide for the conclusion. A close shot with no earlier wide shot leaves
the viewer without a place. When the next sentence introduces a new thing, go *wider first* and then in. Vary the size
from one sentence to the next. [H]

## 4. The camera must never pass through geometry
Four faults seen again and again: the camera ends outside a room's shell (the room vanishes), a push-in on a person who
faces furniture puts the camera inside the furniture, a camera tracking beside a road passes through a post, and an
orbit around a prop clips a wall.

Rules:
- Clamp the camera inside the set (a keep-in box smaller than the walls by about 0.3 m or 10 %). `pathInside` in
  `scripts/easing.mjs` tests a whole path against that box; a room that has lost a wall in one frame fails it. [H]
- Clamp it above the floor (`minY`). [H]
- Sample the whole path every 100 ms (10 Hz) and test a sphere of the camera's near radius plus a margin of about
  0.2 m against every solid box in the scene. `pathClearance` in `scripts/easing.mjs` does this on boxes. A per-shot
  numeric test beats looking; but *also* look at a strip, because a test only knows the boxes you gave it. [H]
- When a person is in the way at a cut, move the person onto open floor at that cut and move them back afterwards. [H]
- For vehicles or rooms with a window, keep the camera's side of the scene empty (about 12 m for a road passing a
  car), or the camera passes through the scenery that slides by. [H]
- Keep the camera in the set's open side: if the set is a three-walled room, the missing wall faces the camera. [H]

## 5. Subject position
- The subject box (projected bounding box) sits inside a safe band: not above the top overlay, not below the subtitle
  zone. In portrait 1080 x 1920 the band is roughly y = 22 %-70 % of the height; in wide 16:9 it is roughly 8 %-82 %
  (5 % title-safe margin on top, a subtitle zone of about 13 % at the bottom). [H] A medium subject (50-70 % of frame
  height) is taller than the portrait band: keep its key detail (the face, the valve, the label target) inside the band
  and let the rest run under the overlays.
- Subject centre about 44 % from the top is a good default in portrait; 50 % in wide. [H]
- A subject that is a *function of time* (a runner crossing the frame) is given to the camera as time since the cut, not
  the global time: otherwise the shot starts mid-way. [H]
- Check that the subject box stays in the band for every sampled frame, not only the first and last. `pathClearance`
  does not project; pull 8 frames with `scripts/frame_strip.py` and look.

## 6. Interactive cameras
In an interactive lesson the user drives the camera. Rules: smooth damping on drag (a typical damping factor is 0.08-0.15, a starting value to tune by feel); a "reset
view" button; auto-rotation only while idle and only if the idea is shape (stop it as soon as the lesson is about
something that moves, and always stop under reduced-motion); limits on zoom so the user cannot enter the object by accident
(`minDistance` at least 1.2 times the object's radius); clipping planes that never cut the thing being explained. [H]
