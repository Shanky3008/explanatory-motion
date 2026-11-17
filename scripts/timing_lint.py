#!/usr/bin/env python3
"""Lint tag and subtitle timing against word-level narration timings. Standard library only.

usage:
  python timing_lint.py CUES.json WORDS.json [--audience mixed|adult|learner|<wps>] [--tag-lead 0.1]
                        [--tag-late 0.4] [--min-tag 1.5] [--cps 20] [--max-line 42]
                        [--portrait] [--young] [--json]

Presets: --portrait sets the line limit to 32 characters (portrait 9:16 video; the default 42 is for wide video).
         --young sets 17 characters per second and the "learner" reading speed (2.0 words per second) for children or
         second-language readers (the defaults, 20 and "mixed", are for adults and unknown audiences).
         A preset replaces --max-line / --cps; --young also replaces --audience when that is left at "mixed".

WORDS.json   a list [{"word": "fat", "start": 12.40, "end": 12.71}, ...], or {"words": [...]}, or an aligner's
             {"segments": [{"words": [...]}]}. Words the aligner could not time (no start) are skipped.
CUES.json    a list (or {"cues": [...]}) of
               {"id": "t1", "kind": "tag", "text": "fat", "start": 12.3, "end": 14.0}
                   optional "word" (the spoken word(s), default = text) and "occurrence" (1 = first mention)
               {"id": "s1", "kind": "subtitle", "text": "Fat floats\\non the milk", "start": 12.3, "end": 15.0}
                   (a real newline or the two characters \\n both count as a line break)

Checks (ERROR fails the run with exit code 1; WARN is for a person to review):
  tag       word not found (ERROR); onset earlier than its word by more than --tag-lead (ERROR);
            onset later than --tag-late after the word (WARN); on screen under --min-tag seconds (ERROR) or under the
            reading time (WARN); anchored to a later mention than the first (WARN); more than two tags at once (ERROR)
  subtitle  starts before its first word by more than --tag-lead (ERROR); on screen under the reading time (ERROR);
            character rate above --cps (ERROR); more than two lines (ERROR); a line longer than --max-line (WARN);
            ends before its last word ends (WARN); lingers more than 0.8 s after its last word (WARN);
            text not found in the words (WARN, timing not checked)
The reading time is 0.6 + words / wps, minimum 1.2 s (references/timing-easing.md section 3).
"""
import argparse, json, re, sys, unicodedata

WPS = {"adult": 3.0, "mixed": 2.5, "learner": 2.0}


def norm(w):
    """Lower-case and keep letters, digits, combining marks and apostrophes in any script (accents, Devanagari, ...)."""
    s = unicodedata.normalize("NFC", str(w)).lower().replace("’", "'")
    return "".join(ch for ch in s if ch == "'" or unicodedata.category(ch)[0] in "LNM")


def tokens(text):
    return [t for t in (norm(x) for x in re.split(r"\s+", str(text).replace("\\n", " "))) if t]


def reading_seconds(n_words, wps):
    return max(1.2, 0.6 + n_words / wps)


def load_json(path, what):
    try:
        with open(path, encoding="utf-8-sig") as f:
            return json.load(f)
    except FileNotFoundError:
        sys.exit(f"{what} file not found: {path}")
    except json.JSONDecodeError as e:
        sys.exit(f"{what} file {path} is empty or not valid JSON: {e}")


def load_words(path):
    data = load_json(path, "words")
    if isinstance(data, dict):
        if "segments" in data:
            data = [w for s in data["segments"] for w in s.get("words", [])]
        else:
            data = data.get("words", [])
    out = []
    for w in data:
        if w.get("start") is None or w.get("end") is None:
            continue
        t = norm(w.get("word", ""))
        if t:
            out.append({"t": t, "start": float(w["start"]), "end": float(w["end"])})
    for i, w in enumerate(out):
        if w["end"] < w["start"]:
            sys.exit(f"word timings invalid: '{w['t']}' ends ({w['end']}) before it starts ({w['start']})")
        if i and w["start"] < out[i - 1]["start"] - 1e-6:
            sys.exit(f"word timings out of order: '{w['t']}' starts at {w['start']} after "
                     f"'{out[i - 1]['t']}' at {out[i - 1]['start']}; sort or re-align first")
    return out


def find_seq(words, toks, from_idx=0):
    n = len(toks)
    for i in range(from_idx, len(words) - n + 1):
        if all(words[i + k]["t"] == toks[k] for k in range(n)):
            return i
    return -1


def find_all(words, toks):
    n = len(toks)
    return [i for i in range(len(words) - n + 1) if all(words[i + k]["t"] == toks[k] for k in range(n))]


def lint(cues, words, wps, a):
    issues = []

    def add(level, cue, msg):
        issues.append({"level": level, "id": cue.get("id", "?"), "kind": cue.get("kind"), "message": msg})

    ptr = 0
    tags = []
    for c in cues:
        kind = c.get("kind", "subtitle")
        try:
            s, e = float(c["start"]), float(c["end"])
        except (KeyError, TypeError, ValueError):
            add("ERROR", c, "cue has no numeric start and end")
            continue
        dwell = e - s
        if e <= s:
            add("ERROR", c, f"end {e} is not after start {s}")
            continue
        if kind == "tag":
            toks = tokens(c.get("word", c.get("text", "")))
            idxs = find_all(words, toks) if toks else []
            if not idxs:
                add("ERROR", c, f"spoken word '{c.get('word', c.get('text'))}' not found in the timings")
                continue
            occ = int(c.get("occurrence", 0))
            if occ:
                if occ > len(idxs):
                    add("ERROR", c, f"occurrence {occ} requested but the word is spoken {len(idxs)} time(s)")
                    continue
                k = occ - 1
            else:
                k = min(range(len(idxs)), key=lambda j: abs(words[idxs[j]]["start"] - s))
            anchor = words[idxs[k]]["start"]
            if s < anchor - a.tag_lead:
                add("ERROR", c, f"tag appears {anchor - s:.2f} s before its word (word starts {anchor:.2f}, tag at {s:.2f})")
            elif s > anchor + a.tag_late:
                add("WARN", c, f"tag appears {s - anchor:.2f} s after its word")
            if k > 0:
                add("WARN", c, f"anchored to mention {k + 1}; the first mention is at {words[idxs[0]]['start']:.2f} s")
            if dwell < a.min_tag:
                add("ERROR", c, f"on screen {dwell:.2f} s, under the {a.min_tag} s minimum for a tag")
            need = reading_seconds(len(tokens(c.get("text", ""))), wps)
            if dwell < need:
                add("WARN", c, f"on screen {dwell:.2f} s, reading time is {need:.2f} s")
            tags.append((s, e, c))
        else:
            toks = tokens(c.get("text", ""))
            if not toks:
                add("WARN", c, "empty subtitle text")
                continue
            i = find_seq(words, toks, ptr)
            if i < 0:
                i = find_seq(words, toks, 0)
            raw = str(c.get("text", "")).replace("\\n", "\n")
            lines = raw.split("\n")
            if len(lines) > 2:
                add("ERROR", c, f"{len(lines)} lines (maximum 2)")
            longest = max(len(x) for x in lines)
            if longest > a.max_line:
                add("WARN", c, f"longest line is {longest} characters (limit {a.max_line})")
            chars = len(raw.replace("\n", " "))
            need = reading_seconds(len(toks), wps)
            if dwell < need:
                add("ERROR", c, f"on screen {dwell:.2f} s, reading time is {need:.2f} s for {len(toks)} words")
            if chars / dwell > a.cps:
                add("ERROR", c, f"{chars / dwell:.1f} characters per second (limit {a.cps})")
            if i < 0:
                add("WARN", c, "text not found in the word timings; start and end not checked")
                continue
            ptr = i + len(toks)
            first, last = words[i], words[i + len(toks) - 1]
            if s < first["start"] - a.tag_lead:
                add("ERROR", c, f"subtitle appears {first['start'] - s:.2f} s before its first word")
            if e < last["end"] - 0.05:
                add("WARN", c, f"subtitle ends {last['end'] - e:.2f} s before its last word finishes")
            if e - last["end"] > 0.8:
                add("WARN", c, f"subtitle lingers {e - last['end']:.2f} s after its last word")
    # more than two tags at once
    events = sorted([(s, 1, c) for s, e, c in tags] + [(e, -1, c) for s, e, c in tags], key=lambda x: (x[0], x[1]))
    live = 0
    for t, d, c in events:
        live += d
        if live > 2 and d == 1:
            add("ERROR", c, f"more than two tags on screen at {t:.2f} s")
    return issues


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cues"); ap.add_argument("words")
    ap.add_argument("--audience", default="mixed")
    ap.add_argument("--tag-lead", type=float, default=0.1)
    ap.add_argument("--tag-late", type=float, default=0.4)
    ap.add_argument("--min-tag", type=float, default=1.5)
    ap.add_argument("--cps", type=float, default=20.0)
    ap.add_argument("--max-line", type=int, default=42)
    ap.add_argument("--portrait", action="store_true", help="portrait video: line limit 32 characters")
    ap.add_argument("--young", action="store_true", help="children or second-language readers: audience learner (2.0 words/s), 17 characters/s")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.portrait:
        a.max_line = 32
    if a.young:
        a.cps = 17.0
        if a.audience == "mixed":
            a.audience = "learner"
    try:
        wps = float(a.audience)
    except ValueError:
        wps = WPS.get(a.audience)
        if wps is None:
            sys.exit("audience must be mixed, adult, learner or a number of words per second")
    cues = load_json(a.cues, "cues")
    if isinstance(cues, dict):
        cues = cues.get("cues", [])
    if not isinstance(cues, list) or not cues:
        sys.exit("no cues found (expected a non-empty list, or {\"cues\": [...]})")
    words = load_words(a.words)
    if not words:
        sys.exit("no timed words found")
    issues = lint(cues, words, wps, a)
    if a.json:
        print(json.dumps(issues, indent=2))
    else:
        for i in issues:
            print(f"{i['level']:5} {i['kind'] or '':8} {i['id']}: {i['message']}")
        errs = sum(1 for i in issues if i["level"] == "ERROR")
        print(f"{len(cues)} cues, {errs} error(s), {len(issues) - errs} warning(s)")
    sys.exit(1 if any(i["level"] == "ERROR" for i in issues) else 0)


if __name__ == "__main__":
    main()
