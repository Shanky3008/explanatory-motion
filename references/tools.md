# Tools this skill recommends (none are bundled)

Licence lines below were read from each project's own page on 16 November 2026. Licences change: check the page again
before you redistribute anything.

| Tool | Use it for | Licence as its page states it |
|---|---|---|
| three.js | 3D scenes in the browser; post-processing passes (bloom, depth of field) come with its examples | MIT license |
| GSAP | timelines, sequencing, easing on SVG, DOM and canvas | the "Standard 'No Charge' GSAP License" (see below) |
| WhisperX | word-level timing by aligning a script to audio | BSD-2-Clause license |
| ffmpeg | encoding, frame extraction, silence detection, contact sheets | primarily LGPL 2.1 or later; optional parts GPL 2 or later (see below) |
| Manim (Community edition) | maths animation in Python | MIT license |
| Tweakpane | a small panel of sliders to tune durations, colours, camera numbers by eye | MIT License |

## GSAP, exactly as its licence page gives it
Its page says that GSAP "is now free for everyone, thanks to Webflow's support!" and that "Commercial usage is covered
under the standard license"; plugins such as SplitText and MorphSVG "can be used in commercial projects at no charge". The
page's effective date is 30 April 2025 and its last-modified date 30 May 2025. It restricts "Prohibited Uses": using GSAP in a
tool that lets users build visual animations without code and that "competes with Webflow" needs "prior written consent". Its FAQ
says AI-generated code "is not a 'Prohibited Use'". Read the full page before relying on this summary.
Alternatives with no such wording: plain `requestAnimationFrame` plus `scripts/easing.mjs`, or the Web Animations API.

## ffmpeg
Its legal page says FFmpeg is primarily LGPL 2.1 or later, that optional parts and optimisations are GPL 2 or later (using them makes
the GPL apply to all of it), and that it is not available under other terms. Calling an installed ffmpeg from a script, as this
skill does, does not bundle it.

## When to pick which
- Interactive lesson on the web: three.js for 3D, plain SVG for 2D, your own tweening (`scripts/easing.mjs`) or GSAP.
- Maths film: Manim; or SVG plus the timeline rules in `diagrams-maths-motion.md`.
- Timing: WhisperX; check the output with `scripts/timing_lint.py`.
- Tuning: Tweakpane on the page while you adjust; then write the chosen numbers into the scene file. Remove the panel in
  production.
- Post-processing (bloom, depth of field): film renders and desktop; keep a switch; the lesson must look right with it off.
