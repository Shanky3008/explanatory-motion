# Film pipeline and render hygiene

How to turn a scene into a finished clip without losing work, hanging a machine or shipping something you never saw.
Tags: [C] common, [H] house rule.

## 1. The stages
1. **Script and timings**: narration audio, aligned word times (`narration-sync.md`).
2. **Shot list**: one row per sentence: shot name, size, subject, what changes, tag word, seconds.
3. **Scene**: a pure function of time (`interactive-vs-film.md` section 7).
4. **Stills first**: one frame per shot (the middle of the shot and its last frame). Make a contact sheet and LOOK
   (`checklists/first-sight-look.md`).
5. **Render frames** in chunks (for example 450 frames), each written to disk as it finishes, with a manifest. Checkpoint
   every 90 frames so a crash redoes at most that much.
6. **Finish**: subtitles, tags, narration mux, end card, watermark if wanted.
7. **Check**: duration, audio present and in sync, then a frame strip of every shot and LOOK
   (`checklists/watch-in-motion.md`).
8. **Hand over** with a list of what was not looked at.

## 2. Encoding with ffmpeg
Frames to video (image sequence named `frame_%05d.jpg`, 30 fps, narration `voice.wav`):

    ffmpeg -framerate 30 -i frame_%05d.jpg -i voice.wav -c:v libx264 -pix_fmt yuv420p -crf 18 -preset medium \
           -c:a aac -b:a 160k -movflags +faststart -shortest out.mp4

`yuv420p` is needed for broad playback; `+faststart` lets it play while loading. Verify:
`ffprobe -v error -show_entries stream=codec_name,width,height,r_frame_rate,duration out.mp4`. The video and audio
durations should agree within 0.05 s. Test the first 55 seconds for silence with
`ffmpeg -i out.mp4 -af silencedetect=n=-55dB:d=2 -f null -`. [C]

Motion blur: let the number of blended sub-frames follow how far the picture moves in one frame. A few pixels need none; a
whip or a quick explode needs several (8-16 was enough in one test). Check one whip frame at full size. [H]

FFmpeg's licence is LGPL with GPL parts: if you redistribute a build, read `references/tools.md`.

## 3. One headless browser at a time
Headless browsers eat memory and can pile up. Rules that came from real incidents (hundreds of hidden browsers once
launched by a batch):
- **Use a lock file, created atomically.** Create it only if it does not exist (exclusive create, e.g. shell `set -o noclobber`
  or `open(path, 'x')`), never by overwriting: an overwrite silently takes another job's lock. Write `{who, started, pid}`;
  wait; read it back after about 2 s to confirm it is still yours; only then start. Check for a browser already running
  as well as for the file. Delete it when finished. A lock older than about 20 minutes with no browser running is stale:
  remove it and note that you did. Never remove a fresh foreign lock. [H]
- **Count browsers before and after** your run; if the count is higher after, find and close your own. Close only the
  browser you started, never kill by name. [H]
- Check free memory first (about 3 GB free for a 1080 x 1920 render). [H]
- **Test one page or one story before a batch**, look at it, then batch. [H]
- Keep jobs resumable: per-item state file, "STOP" file honoured at the next safe point, hash-checked results so finished work
  is kept. [H]
- Do not wait forever: a bounded wait (60 minutes per attempt is plenty), then report that the slot was busy rather than
  forcing it. [H]

## 4. Caches and disk
- Cache frames under a hash of (scene version, shot list, size). A changed script must not reuse stale frames. [H]
- Keep the finished clip, its manifest, and its checks. Delete frame folders after copy-out and review, unless a re-time to new
  narration is likely. [H]
- Do the clean-up in batches of ten, after the contact sheets have been looked at, not before. [H]

## 5. Look at the result yourself
A success status from the runner means "it ran". It does not mean "it is good". Always:
- For stills: build a contact sheet (`scripts/contact_sheet.py`) and look at every cell at a size where labels are readable.
- For motion: pull a frame strip from the clip (`scripts/frame_strip.py`), 16 frames per window around each change, and
  look for the faults in `checklists/watch-in-motion.md`. A one-frame-per-second sheet cannot show a tag that appears
  a second early or a limb that does not move between samples.
- Look at what changed *after* your last edit. A re-render that nobody opened is unverified.
- State in your hand-over what you did not look at (clips never opened, angles not staged, tags a still did not catch).

## 6. Things the viewer must never see
Names of tools, models, libraries, voices, file names, licence text inserted by tooling, debug overlays, placeholder
labels, "TODO", or template wording. Scan subtitles, tags, captions and the poster for these before release. [H]

## 7. Patching files by script
When a script edits source files: write the script to a file (not a shell here-document that may eat backslashes); never put a
line comment in the middle of a one-line statement you patch, since it swallows the rest of the line; preserve whitespace
unless you mean to change it. [H]
