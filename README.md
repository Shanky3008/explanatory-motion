# explanatory-motion

An agent skill (the folder-with-`SKILL.md` format) that teaches a coding agent to make **explanatory motion**: animated
teaching pictures, interactive 3D lessons and short explainer videos that a learner can follow with the sound off.

It is a working method plus references, checklists and small tested scripts. It is not a library and bundles no third-party
code. Status: first public release. Licence: MIT (see `LICENSE`).

## What is in it

| Path | What |
|---|---|
| `SKILL.md` | when to use it, the core loop, three non-negotiables, a decision table, the numbers most often needed |
| `references/` | one file per topic: staging, colour, timing and easing, camera, guided paths, truthfulness, narration sync, exploded and cut-open views, diagrams and maths, interactive versus film, performance budgets, accessibility, film pipeline, recommended tools |
| `checklists/` | a first-sight look rubric with scores, a pre-render check, a "watch it in motion" review, a truth check |
| `scripts/` | `contact_sheet.py`, `frame_strip.py`, `easing.mjs`, `timing_lint.py`, `sync_easing.mjs` and a self-test |
| `examples/` | three small self-contained SVG pages (a water cycle, a camera move, a cut-open heart), each with a wrong version and a right version |

## Install

Copy this repository as a folder named `explanatory-motion` into the skills folder of your agent (for example
`~/.claude/skills/` for all projects, or `.claude/skills/` inside a project). The agent reads `SKILL.md` first and opens the other files only when
the decision table sends it there.

## Check that the scripts work on your machine

    python scripts/selftest.py

Needs Python 3.8+, Node 18+, ffmpeg and ffprobe on the path, and Pillow (`pip install pillow`) for the contact sheet.
The test builds its own tiny synthetic inputs (a four-second test clip, five coloured stills, a toy narration) and removes
them afterwards.

## How to read the numbers

Every rule is tagged: **[E]** a published standard (for example WCAG contrast and flashing limits), **[C]** common practice,
**[H]** a house rule learnt by making and reviewing many pictures, **[M]** a figure measured once in one setup. Treat [H] numbers as starting points and adjust them by looking
at the result; the skill's own advice is to look before claiming anything.

## The three ideas in one paragraph

A picture must stay true (never prettier but wrong; refuse to stage what cannot be shown truthfully). Its first three seconds
decide whether a learner trusts it, so score the first-sight look, not just correctness. And look at the result yourself,
with a contact sheet for stills and a frame strip for motion, before saying it is done.

## Examples

Open `examples/guided-path/after.html`, `examples/guided-path-heart/after.html` and `examples/camera-move/after.html` in a browser, beside their `before.html`. Append
`?t=2.2` to freeze a page at 2.2 seconds, `?t=end` for the finished state; on the camera page `?guides=1` draws the safe band
and the subject box.

## Contributing and licence

MIT License: use it, change it and share it, in private or commercial work, as long as the copyright and licence notice
stay with it. See `LICENSE`. The tools this skill recommends are not bundled and keep their own licences
(`references/tools.md`).

Corrections and additions are welcome: open an issue or a pull request. For a new rule, say where the number comes from
and tag it [E], [C], [H] or [M] as the other rules are tagged; for a script change, run `python scripts/selftest.py` first.
