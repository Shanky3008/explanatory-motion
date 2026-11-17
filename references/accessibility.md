# Accessibility

Tags: [E] published standard (WCAG 2.x unless noted), [C] common practice, [H] house rule.

Where each [E] number comes from (W3C Web Content Accessibility Guidelines, checked on 16 November 2026):

| Rule here | Success criterion | Level |
|---|---|---|
| text 4.5 : 1, large text 3 : 1 | 1.4.3 Contrast (Minimum) | AA |
| graphics that carry meaning 3 : 1 | 1.4.11 Non-text Contrast | AA |
| text can be enlarged to 200 % | 1.4.4 Resize Text | AA |
| no more than three flashes in any second | 2.3.1 Three Flashes or Below Threshold | A |
| pause, stop or hide moving content over 5 s | 2.2.2 Pause, Stop, Hide | A |
| motion from interaction can be switched off | 2.3.3 Animation from Interactions | AAA |
| pointer targets at least 24 x 24 CSS px | 2.5.8 Target Size (Minimum) | AA |
| pointer targets at least 44 x 44 CSS px | 2.5.5 Target Size (Enhanced) | AAA |
| captions for recorded narration | 1.2.2 Captions (Prerecorded) | A |
| audio description or text alternative for visual-only content | 1.2.3 / 1.2.5 | A / AA |
| visible focus; name, role and state of controls | 2.4.7 / 4.1.2 | AA / A |

The `prefers-reduced-motion` setting is defined by the W3C Media Queries specification, not by WCAG.

## 1. Understand it with the sound off, and without colour alone
- Every piece must make sense muted: subtitles or on-screen text carry the narration's content, and the picture alone shows
  the sequence. Test by watching a strip of frames with the audio off. [H]
- Do not carry meaning by colour alone: add number, shape, label, line style. See `colour-clarity.md` section 6. [E]

## 2. Text contrast and size
- Text 4.5 : 1 against its background, large text and meaningful graphics 3 : 1. [E]
- Minimum text height on a phone: about 4 % of the screen height for subtitles, 2.5 % for tags and labels (at 1920 high:
  about 77 px and 48 px). [H]
- Do not put text on a busy part of the picture without a dark edge or a translucent box. [H]
- Let users enlarge text (relative units); do not lock text into an image if the lesson is interactive. [E]

## 3. Flashing and strobing
- No more than three flashes in any one second, and no large area flashing at high contrast (the guideline's area test: a flash
  covering more than about a quarter of a 10-degree field of view, roughly 341 x 256 px on a 1024 x 768 screen). Fading glows are
  fine; a hard on-off faster than 3 Hz is not. [E] (WCAG 2.3.1)
- Avoid large, high-contrast, repeating stripes moving at the stroboscopic speeds in `timing-easing.md` section 8. [C]
- A heartbeat or a pulse is a slow glow (0.3-0.6 s up), not a blink. [H]

## 4. Reduced motion
- Read the user's setting (`prefers-reduced-motion: reduce`) and also react when it changes while the page is open. [E]
- With it set: do not auto-play; start paused at the named, meaningful still; show a one-line notice ("Motion is paused
  because your device asks for less movement. Press Play to watch it."); the Play button still works. [H]
- Replace big camera moves, parallax and spin with cuts or fades. Keep essential motion (the thing the lesson is about) only
  on demand. [C]
- Auto-rotating turntables stop under reduced-motion and stop when the learner touches the model. [H]

## 5. Pause, stop, hide
Anything that moves automatically for more than 5 seconds needs a way to pause, stop or hide it. [E] (WCAG 2.2.2)

## 6. Keyboard, focus, screen readers
- Controls are real buttons, keyboard reachable in reading order, with a visible focus ring. [E]
- Play/Pause has an accessible name and a pressed state. [E]
- The scene has a text alternative: a short description of what it shows and what it does *not* show (the
  "not to scale" line). [E]
- The current step or phase is announced politely (`aria-live="polite"`), not on every frame. [C]
- Click targets at least 24 x 24 CSS px [E] (2.5.8, AA); aim for 44 x 44 [E] (2.5.5, AAA, the enhanced level; 44 is also the usual touch-screen guideline).

## 7. Captions and audio descriptions
- Provide captions for narration (a text track or burned-in subtitles). For burned-in subtitles also supply the transcript
  text separately. [E]
- If important information is only visual and the audience may not see it, narrate it. [E]

## 8. Cognitive load
- One idea per shot; at most two tags at once; at most two things moving at once beyond the camera's drift. [H]
- Plain words for the audience's reading level; unfamiliar terms explained when first shown. [H]
