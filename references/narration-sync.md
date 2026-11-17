# Narration and text sync

Tags: [E] standard, [C] common practice, [H] house rule.

## 1. The principle
Pictures lead the eye, narration leads the mind, and the two must arrive together. A label that shows up *before* its word
points at something the viewer cannot yet name; a label late by more than half a second is read as a different thing.
The rule: **nothing the voice names appears on screen earlier than the voice says it, and nothing stays after it has
stopped mattering.**

## 2. Get real word timings
- Record or synthesise the narration first, then align the *script text* to the audio with a forced aligner that
  returns word-level start and end times (WhisperX is one such tool; see `references/tools.md`). Time the film to
  those words, not to an estimate. [H]
- An energy-based or words-per-minute estimate is only a fallback for rough scratch cuts. In one test an energy-based clock
  had a median error of 0.3-0.8 s and a worst case of about 2.8 s: unusable for tags. [M]
- Normalise the script and the aligned words the same way before matching: lower case, strip punctuation, join acronyms the
  aligner spells letter by letter (G P S becomes GPS), split compound spellings the voice says as two pieces ("Wi-Fi" is
  "wi fi"). Refuse the piece and report the first differing word if the script and audio disagree. [H]
- Keep timings in a small JSON next to the audio: `[{"word": "fat", "start": 12.40, "end": 12.71}, ...]` (a list, or
  `{"segments":[{"words":[...]}]}` as aligners write it). `scripts/timing_lint.py` reads both.
- Check the audio file itself: it must not be silent for the first seconds (`ffmpeg -af silencedetect=n=-55dB:d=2`),
  and its length must equal the video's within 0.05 s. A beautiful silent film shipped as "narrated" is a classic failure.
- Level the voice to a consistent loudness before muxing; about -16 to -17 LUFS integrated is a common target for phone
  viewing. [C]

## 3. Tags and pointers (short names on things)
A tag is a 1-3 word label with a leader to a thing, appearing when its word is spoken.
- onset (start of the fade-in) between 0.1 s before the word's start and 0.4 s after it. A tag that leads the voice by
  more than 0.1 s is a fault a viewer can notice; 0.75-1.2 s early was clearly visible in review. [H]
- Visible at least 1.5 s; in one shot only; at most two at once; 1-3 per short film. [H]
- Name the thing at its *first* spoken mention. A tag anchored to a later mention is a warning to review. [H]
- If the word falls within about 1.2 s of a cut, tag the next mention, or begin the tag earlier in the same shot, or declare the
  word untagged with a reason. [H]
- A tag anchored to something that is off-screen at that moment is omitted, not forced; a wrong anchor is worse than none.
- Tag near a frame edge opens toward the middle. [H]
- It sits on the thing it names: check a frame at the tag's midpoint.

## 4. Subtitles
- At most two lines. Wide (16:9): 42 characters per line at most, at most 20 characters per second for adults and 17 for
  children. [C] These three figures are the published limits of streaming-service timed-text style guides, not a standard.
  Portrait (9:16): 28-32 characters per line, scaled down from 42 to keep the text height similar on a narrow frame. [H]
- Break at phrase boundaries: never inside a name, never after a preposition (the break "stay closer to / the wall" is a
  fault). [C]
- Appear no earlier than the first word of the line (tolerance 0.1 s); disappear within about 0.4 s after the last word,
  or at the next subtitle. Stay on screen at least the reading time of section 3 of `timing-easing.md`. [H]
- Light text with a dark edge or translucent box; check on the lowest-contrast frame (a mid-tone floor is typical). [H]
- Safe areas: keep text and key detail inside these margins.

| Format | Left/right | Top | Bottom | Notes |
|---|---|---|---|---|
| Wide (16:9) | 5 % | 5 % | 5 % | broadcast graphics-safe area is 90 % of the frame (EBU R 95; action-safe is 93 %) [E] |
| Portrait (9:16, 1080 x 1920) | 5-6 % (60 px) | 12-14 % (about 250 px) | 20-24 % (about 400 px) | platform controls overlay both ends [C] |
| Square (1:1) | 5 % | 8 % | 12 % | [H] |

- A poster or thumbnail should come from a frame *before* the first subtitle appears, or the subtitle text is baked into the
  poster. [H]

## 5. Narration timing against motion
- A step's visual change begins about 0.1-0.3 s before the word that explains it *finishes*, never before it starts
  (the verb lands as the action lands). [H]
- Pauses in narration are for the eye: leave a 0.3-0.5 s silence after a new picture appears before talking about its
  details. [H]
- When a phrase runs long, change the picture instead of holding it: after about 6 s with nothing changing the shot reads as
  frozen. Cut to a closer view or move the highlight to the next part. [H]
- Two-thirds of a film's runtime should have something changing on screen at least every 3-4 s (a camera drift counts only
  if the subject is in motion too). [H]

## 6. Checks
Run `python scripts/timing_lint.py cues.json words.json` (see the script's `--help`). It flags tags that precede their
word, tags shown less than 1.5 s or less than their reading time, subtitles shown less than the reading time, subtitles
that start before their first word, too-fast character rate, more than two tags overlapping, and tags whose word is missing
or is not its first mention. Then look at frames: the linter does not know whether the tag sits on the right thing.
