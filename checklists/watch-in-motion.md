# Watch it in motion (review from a frame strip)

You cannot reliably judge motion from one frame or from one frame per second. Make a strip of 12-16 frames from the window
you want to judge and read it left to right, like comic panels.

    python scripts/frame_strip.py clip.mp4 --t0 12.0 --t1 17.4 --n 16 --cols 4 --out strip_12-17.png

`t0` and `t1` are seconds *into the clip*. The script prints the time of every cell. Make one strip per shot (or per 5-6 s),
plus one denser strip (0.2 s apart) around any event: a tag appearing, a cut, a step change.

## What to look for, panel by panel
**Continuity and form**
- [ ] Does the subject stay in the safe band in every panel?
- [ ] Does the camera pass through a wall, a prop, a person, or end outside the room? (A wall suddenly gone, a surface filling
      the frame.)
- [ ] Do people's feet slide, hands pass through objects, poses stand in mid-air, a limb teleport between panels?
- [ ] Does an action that should look like cycling or swinging actually change between panels? (A held pose gliding along
      is a common fault of slowed actions: legs that hardly cycle.) Compare limbs panel to panel.
- [ ] Pops: objects appearing from nowhere, a sudden change of size or colour between adjacent panels.

**Clarity**
- [ ] Is the thing the sentence names the thing that changes, in the panel where the word is spoken?
- [ ] Does a tag sit on the thing it names? Is it fully legible, and did it appear *with* its word, not earlier? (Look at the
      panel just before the word.)
- [ ] Do two tags or captions overlap? Is anything off the frame edge (a tag running off)?
- [ ] Subtitles: inside the safe area, readable on the lowest-contrast panel, not breaking mid-phrase.
- [ ] Is a small thing too small in the wide panels (a coin, a bead, an oven)? Note it for a closer cut.
- [ ] Is a hand, head or prop covering what is being explained?
- [ ] Does the idea depend on an action that reads only in motion (a stalled slider shivering, blades slowing, a settle to a dimmer
      light, legs that should cycle)? A strip may not show it: take at least three stills across the action, and give the idea a cue
      that survives a still (an arrow, a tag, a trail).

**Pace**
- [ ] Hold: after something new arrives is there a panel or two with no change? If every panel differs the sequence is a blur.
- [ ] Freeze: more than 6 s (about two panels at 3 s spacing) with no change at all?
- [ ] Does the last shot settle and rest for about a second?

**Truth**
- [ ] Anything the picture shows that the narration did not say, or that contradicts it?
- [ ] Arrows, bends, reflections, flows in the right direction at every panel?

**Strobe and flash**
- [ ] Repeating pattern showing steady forward motion, not frozen or backward?
- [ ] Any hard on-off flicker faster than 3 flashes a second, or a large high-contrast area flashing?

## Record
For each strip: file name, window, verdict (OK / CONCERN / WRONG), one-sentence reason. Keep the strip next to the verdict.
Anything you did not open goes in the hand-over note as "not looked at".

## Limits
A strip catches most visible faults. It does not tell you about sync with audio (check by ear and with `timing_lint.py`),
about frame rate smoothness on a slow device (measure frame times), or about parts of the clip you did not sample.
