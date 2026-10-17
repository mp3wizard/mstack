#!/usr/bin/env python3
"""Second opinion on which design-mode playbook fits a task, from Jev.

Ranks the intent lines in ../references/routes.txt against the task with
`jev rank` (TypeSafe). Jev only reorders. This script owns the policy: it
names a playbook only when the top score is at least RATIO times the second,
and otherwise returns the top three for the router to decide. The router's
own reading always has the last word.

The task text is sent to api.typesafe.ai, so the script refuses text that
carries URLs, email addresses, or long ID-like strings. Strip client names too.

Usage:
  route.py --task "<one-line task, in English>"
  route.py --self-test
Exit codes: 0 ranked, 2 jev unavailable or failed (route by the router's
rules), 3 task refused for privacy.
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys

ROUTES = pathlib.Path(__file__).resolve().parent.parent / "references" / "routes.txt"
RATIO = 1.5
PRIVATE = re.compile(r"https?://|www\.|figma\.com|[\w.+-]+@[\w-]+\.[\w.]+|\b[A-Za-z0-9]{20,}\b")


def load_routes(text):
    routes = {}
    for line in text.splitlines():
        if " | " in line:
            slug, intent = line.split(" | ", 1)
            routes[slug.strip()] = intent.strip()
    return routes


def parse_rank(output):
    ranked = []
    for line in output.splitlines():
        if "\t" not in line:
            continue
        score, cand = line.split("\t", 1)
        slug = cand.split(" | ", 1)[0].strip()
        try:
            ranked.append((slug, float(score)))
        except ValueError:
            ranked.append((slug, None))
    ok = sorted((r for r in ranked if r[1] is not None), key=lambda r: -r[1])
    return ok, [s for s, v in ranked if v is None]


def decide(ranked, errors=()):
    top3 = [{"slug": s, "score": v} for s, v in ranked[:3]]
    if not ranked:
        return {"pick": None, "ambiguous": True, "top3": top3, "reason": "no scores returned"}
    if len(ranked) == 1 or ranked[1][1] == 0 or ranked[0][1] >= RATIO * ranked[1][1]:
        return {"pick": ranked[0][0], "ambiguous": False, "top3": top3,
                "reason": f"top score clears {RATIO}x the runner-up", "errors": list(errors)}
    return {"pick": None, "ambiguous": True, "top3": top3,
            "reason": f"top two within {RATIO}x, router decides", "errors": list(errors)}


def self_test():
    routes = load_routes(ROUTES.read_text())
    assert len(routes) >= 22, "every playbook has an intent line"
    out = "0.56\tusability-test | x\n0.18\tmeasure | y\nERR\tprototype | z\n"
    ranked, errs = parse_rank(out)
    assert ranked[0] == ("usability-test", 0.56) and errs == ["prototype"], "parse scores and ERR"
    assert decide(ranked)["pick"] == "usability-test", "clear winner is picked"
    close, _ = parse_rank("0.44\tdeceptive-pattern-audit | a\n0.42\tdesign-qa | b\n")
    d = decide(close)
    assert d["pick"] is None and d["ambiguous"], "close scores defer to the router"
    assert decide([])["ambiguous"], "no scores defers to the router"
    assert PRIVATE.search("review https://www.figma.com/design/abc"), "URL refused"
    assert PRIVATE.search("email pat@example.com about it"), "email refused"
    assert not PRIVATE.search("audit the settings page against WCAG 2.2 AA"), "plain task allowed"
    print("route.py self-test: ok")


def main(argv):
    if argv[1:] == ["--self-test"]:
        self_test()
        return 0
    if len(argv) != 3 or argv[1] != "--task":
        print(__doc__.strip(), file=sys.stderr)
        return 2
    task = argv[2]
    if PRIVATE.search(task):
        print(json.dumps({"pick": None, "refused": True,
                          "reason": "task carries a URL, email, or ID. Restate it without them."}))
        return 3
    jev = shutil.which("jev")
    if not jev:
        print(json.dumps({"pick": None, "fallback": "router rules", "reason": "jev not on PATH"}))
        return 2
    try:
        res = subprocess.run([jev, "rank", task], input=ROUTES.read_text(), capture_output=True,
                             text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({"pick": None, "fallback": "router rules", "reason": str(exc)}))
        return 2
    ranked, errs = parse_rank(res.stdout)
    if res.returncode != 0 or not ranked:
        print(json.dumps({"pick": None, "fallback": "router rules",
                          "reason": (res.stderr or "jev returned no scores").strip()[:200]}))
        return 2
    print(json.dumps(decide(ranked, errs)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
