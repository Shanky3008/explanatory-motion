# Pre-render check

Run before spending render time or shipping a page. Fix, tick, and note what you could not check.

## A. Idea and truth
- [ ] One sentence of what the viewer must understand is written down.
- [ ] Every claim in the narration/text has a picture or is marked "not pictured" with a reason.
- [ ] `truth-check.md` passed.
- [ ] Each convention (colours, scale, speed, exaggeration) is stated on screen or in text.

## B. Script and timing
- [ ] Narration exists; word times come from an aligner, not an estimate.
- [ ] `python scripts/timing_lint.py cues.json words.json` reports no ERROR.
- [ ] Every tag: first mention, onset not before its word, at least 1.5 s, inside one shot, at most two at once.
- [ ] Subtitles: two lines or fewer, line length within the limit, reading time met, breaks at phrase edges.
- [ ] Audio file is not silent in the first seconds; length matches the planned video length.

## C. Staging (stills)
- [ ] One still per shot; contact sheet made (`scripts/contact_sheet.py`) and looked at.
- [ ] Subject size per `staging-composition.md` table; nothing important outside the safe area.
- [ ] No head in a corner, no label on a face, no ring across a head.
- [ ] Camera is outside no wall, inside no object: `pathClearance` clean or looked at in a strip.
- [ ] Moving things have a still reference line.
- [ ] First-sight rubric total at least 14 of 16.

## D. Colour and text
- [ ] Palette table written, one hue one meaning, five or fewer meaning hues.
- [ ] Contrast 4.5 : 1 for text on the worst frame; grayscale test passed.
- [ ] No tool, model, voice, file or template words anywhere visible.
- [ ] Spelling follows the source text.

## E. Motion
- [ ] Durations from `timing-easing.md`; nothing linear that travels; no overshoot on rigid things.
- [ ] Holds met; the final shot rests for about a second.
- [ ] Strobing check done for repeating patterns (`aliasStep`).
- [ ] Flashing: at most three flashes in any second, and no large high-contrast area flashing.

## F. Machine
- [ ] Browser lock free or acquired; browsers counted before (n = ___).
- [ ] Tested one shot/page first and looked at it.
- [ ] Enough disk (about 0.5 GB per 60 s portrait clip in flight) and memory (about 3 GB).
- [ ] Scene is a pure function of time (same t gives same frame).

## G. After the render (do not skip)
- [ ] Browsers counted after (n = ___; same as before).
- [ ] `watch-in-motion.md` done with a frame strip of every shot.
- [ ] Audio present and in sync; ffprobe values as expected.
- [ ] Hand-over note lists what was not looked at.
