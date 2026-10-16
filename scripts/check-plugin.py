#!/usr/bin/env python3
"""Structural checks for the mstack plugin.

Fails (exit 1) when:
  - the router and the playbook/principle files disagree,
  - a skill names a principle-* or playbooks/*.md that does not exist,
  - a SKILL.md frontmatter name does not match its directory,
  - a skill cites a URL whose domain never appeared in the research evidence,
  - a playbooks/*.md or scripts/*.py path does not resolve from the file that names it
    (files under skills/design-mode/ resolve from skills/design-mode/),
  - a skill repeats one of the folk claims encoded in FOLK below (a subset of the
    Corrections table in docs/handbook-map.md; add a row here when you add one there).

Warns when a cited URL is on a known domain but not an exact match.

Usage:
  scripts/check-plugin.py                 check the whole plugin
  scripts/check-plugin.py --files a.md b.md   URL and folk-claim checks on some files
  scripts/check-plugin.py --self-test
"""
import json
import pathlib
import re
import sys
from urllib.parse import urlsplit

ROOT = pathlib.Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
ROUTER = SKILLS / "design-mode" / "SKILL.md"
PLAYBOOKS = SKILLS / "design-mode" / "playbooks"
EVIDENCE = [ROOT / "docs" / "research" / "findings.json", ROOT / "docs" / "research" / "validation.json", ROOT / "docs" / "sources.md"]

PATH_RE = re.compile(r"(?<![\w/.-])((?:\.\./)*(?:design-mode/)?(?:playbooks/[a-z0-9-]+\.md|scripts/[a-z0-9-]+\.py))")
URL_RE = re.compile(r"https?://[^\s)>\]\"'`]+")

FOLK = [
    ("Miller 7±2 as a design rule",
     re.compile(r"7\s*(±|\+/-|\+-|plus or minus)\s*2", re.I),
     re.compile(r"\b(not|folk|misquot|myth|caveat|cowan|don't|never)\b", re.I)),
    ("Doherty 400 ms threshold",
     re.compile(r"\b400\s*ms\b", re.I),
     re.compile(r"sub-second|populari[sz]", re.I)),
    ("WCAG 2.5.5 labelled AA",
     re.compile(r"2\.5\.5[^\n]{0,60}\bAA\b(?!A)|\bAA\b(?!A)[^\n]{0,60}2\.5\.5"),
     re.compile(r"\bAAA\b")),
    ("5 users find 85%",
     re.compile(r"\b85\s*%"),
     re.compile(r"λ|lambda|average|55", re.I)),
    ("SUS 68 as a percentage",
     re.compile(r"\b68\s*%"),
     re.compile(r"\bnot\b", re.I)),
    ("APCA as a gate",
     re.compile(r"\bAPCA\b"),
     re.compile(r"advisory|\bnot\b|draft|undetermined|never", re.I)),
    ("ODI opportunity as plain difference",
     re.compile(r"importance\s*[-−]\s*satisfaction", re.I),
     re.compile(r"max\s*\(", re.I)),
    ("Hick's law as a menu-length cap",
     re.compile(r"\bHick[^\n]{0,60}\b(caps?|limits?|maximum|max)\b", re.I),
     re.compile(r"\b(not|never|reaction|scope|scan)", re.I)),
    ("choice overload as universal",
     re.compile(r"choice overload", re.I),
     re.compile(r"meta-analy|close to zero|near zero|variance|\bnot\b|weak|never", re.I)),
    ("aesthetic-usability as real usability",
     re.compile(r"aesthetic[^\n]{0,60}more usable", re.I),
     re.compile(r"perceived", re.I)),
    ("Postel's law as blanket leniency",
     re.compile(r"\bPostel", re.I),
     re.compile(r"RFC 9413|caveat|\bnot\b|never|harm|silently", re.I)),
    ("HEART needs all five categories",
     re.compile(r"HEART[^\n]{0,80}all five|all five[^\n]{0,80}HEART", re.I),
     re.compile(r"\bnot\b|choose|never", re.I)),
    ("expert review replaces user testing",
     re.compile(r"(heuristic|expert)[^\n]{0,60}(replace|instead of)[^\n]{0,30}(test|research)", re.I),
     re.compile(r"\b(not|cannot|never|can't)\b", re.I)),
    ("WCAG 2.2 dated October 2023 only",
     re.compile(r"WCAG 2\.2[^\n]{0,40}(October|Oct\.?) 2023", re.I),
     re.compile(r"republish|12 Dec|December 2024", re.I)),
    ("Section 508 tracks WCAG 2.1 or 2.2",
     re.compile(r"Section 508[^\n]{0,40}WCAG 2\.[12]\b", re.I),
     re.compile(r"\bnot\b|2\.0", re.I)),
    ("EN 301 549 already requires WCAG 2.2",
     re.compile(r"EN 301 549[^\n]{0,60}(requires|mandates)[^\n]{0,30}2\.2", re.I),
     re.compile(r"not yet|V4|4\.1\.1", re.I)),
    ("NN/g 20 users for quantitative",
     re.compile(r"\b20\s+(users|participants)\b[^\n]{0,60}quantitative", re.I),
     re.compile(r"2006|outdated|was\b", re.I)),
]


def norm(url):
    url = url.rstrip(".,;:")
    parts = urlsplit(url)
    return f"{parts.scheme}://{parts.netloc.lower()}{parts.path.rstrip('/')}"


def known_urls():
    exact, domains = set(), set()
    for path in EVIDENCE:
        if path.exists():
            for u in URL_RE.findall(path.read_text()):
                exact.add(norm(u))
                domains.add(urlsplit(u).netloc.lower().removeprefix("www."))
    return exact, domains


def check_text(path, text, exact, domains, errors, warnings):
    in_code = False
    for n, line in enumerate(text.splitlines(), 1):
        if line.strip().startswith("```"):
            in_code = not in_code
        for u in URL_RE.findall(line):
            nu = norm(u)
            dom = urlsplit(nu).netloc.removeprefix("www.")
            if nu in exact:
                continue
            if dom in domains:
                warnings.append(f"{path}:{n}: URL not in evidence, domain known: {u}")
            else:
                errors.append(f"{path}:{n}: URL domain never seen in research: {u}")
        if in_code or line.lstrip().startswith("#"):
            continue
        for label, bad, ok in FOLK:
            if bad.search(line) and not ok.search(line):
                errors.append(f"{path}:{n}: folk claim ({label}): {line.strip()[:120]}")


def frontmatter(text):
    m = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not m:
        return {}
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            k, v = line.split(":", 1)
            fields[k.strip()] = v.strip().strip('"')
    return fields


def check_structure(errors):
    if not ROUTER.exists():
        errors.append(f"missing router {ROUTER}")
        return
    router = ROUTER.read_text()
    playbook_files = {p.stem for p in PLAYBOOKS.glob("*.md")}
    principle_dirs = {p.name.removeprefix("principle-") for p in SKILLS.glob("principle-*") if p.is_dir()}
    router_playbooks = set(re.findall(r"playbooks/([a-z0-9-]+)\.md", router))
    router_principles = set(re.findall(r"\bprinciple-([a-z0-9]+(?:-[a-z0-9]+)*)", router))
    for s in sorted(playbook_files - router_playbooks):
        errors.append(f"router never names playbooks/{s}.md")
    for s in sorted(router_playbooks - playbook_files):
        errors.append(f"router names missing playbooks/{s}.md")
    for s in sorted(principle_dirs - router_principles):
        errors.append(f"router never names principle-{s}")
    for s in sorted(router_principles - principle_dirs):
        errors.append(f"router names missing principle-{s}")

    skill_dirs = {p.name for p in SKILLS.iterdir() if p.is_dir()}
    for md in sorted(list(SKILLS.rglob("*.md")) + list((ROOT / "agents").glob("*.md"))):
        text = md.read_text()
        rel = md.relative_to(ROOT)
        for s in set(re.findall(r"\bprinciple-([a-z0-9]+(?:-[a-z0-9]+)*)", text)):
            if s not in principle_dirs:
                errors.append(f"{rel}: names missing principle-{s}")
        for s in set(re.findall(r"playbooks/([a-z0-9-]+)\.md", text)):
            if s not in playbook_files:
                errors.append(f"{rel}: names missing playbooks/{s}.md")
        base = SKILLS / "design-mode" if (SKILLS / "design-mode") in md.parents else md.parent
        for ref in set(PATH_RE.findall(text)):
            if not (base / ref).resolve().exists():
                errors.append(f"{rel}: path {ref} does not resolve from {base.relative_to(ROOT)}")
        if md.name == "SKILL.md":
            fm = frontmatter(text)
            if fm.get("name") != md.parent.name:
                errors.append(f"{rel}: frontmatter name {fm.get('name')!r} != directory {md.parent.name!r}")
            if not fm.get("description"):
                errors.append(f"{rel}: missing description")
    for md in sorted((ROOT / "agents").glob("*.md")):
        fm = frontmatter(md.read_text())
        if fm.get("name") != md.stem or not fm.get("description"):
            errors.append(f"agents/{md.name}: frontmatter name must equal filename and have a description")
    routes = SKILLS / "design-mode" / "references" / "routes.txt"
    if routes.exists():
        route_slugs = {l.split(" | ", 1)[0].strip() for l in routes.read_text().splitlines() if " | " in l}
        for s in sorted(playbook_files - route_slugs):
            errors.append(f"routes.txt has no intent line for playbooks/{s}.md")
        for s in sorted(route_slugs - playbook_files):
            errors.append(f"routes.txt names missing playbook {s}")
    if not skill_dirs:
        errors.append("no skills found")


def run(files=None):
    errors, warnings = [], []
    exact, domains = known_urls()
    if files is None:
        check_structure(errors)
        files = sorted(list(SKILLS.rglob("*.md")) + list((ROOT / "agents").glob("*.md")))
    for f in files:
        p = pathlib.Path(f)
        check_text(p, p.read_text(), exact, domains, errors, warnings)
    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    print(f"check-plugin: {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


def self_test():
    exact = {norm("https://www.w3.org/TR/WCAG22")}
    domains = {"w3.org"}
    cases = [
        ("Keep menus to 7±2 items.", 1),
        ("Miller's 7±2 is not a menu rule.", 0),
        ("Respond within 400 ms.", 1),
        ("Aim for sub-second; 400 ms is a later popularization.", 0),
        ("SC 2.5.5 Target Size is AA.", 1),
        ("SC 2.5.5 Target Size (Enhanced) is AAA.", 0),
        ("Five users find 85% of problems.", 1),
        ("85% is an average that assumes λ ≈ 0.31.", 0),
        ("A SUS of 68% is fine.", 1),
        ("Use APCA as the contrast gate.", 1),
        ("APCA is advisory only.", 0),
        ("See https://www.w3.org/TR/WCAG22/#target-size-minimum.", 0),
        ("See https://example.invalid/page.", 1),
        ("Hick's law caps menus at seven.", 1),
        ("Hick's law measures choice reaction time, not menu caps.", 0),
        ("Choice overload means fewer options always win.", 1),
        ("Section 508 requires WCAG 2.1 AA.", 1),
        ("Section 508 still incorporates WCAG 2.0 AA.", 0),
    ]
    for text, want in cases:
        errs, warns = [], []
        check_text("t", text, exact, domains, errs, warns)
        assert len(errs) == want, f"{text!r}: want {want} errors, got {errs}"
    w = []
    check_text("t", "https://www.w3.org/WAI/other", exact, domains, [], w)
    assert len(w) == 1, "known domain, unknown page warns"
    print("check-plugin.py self-test: ok")


if __name__ == "__main__":
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        sys.exit(0)
    if sys.argv[1:2] == ["--files"]:
        sys.exit(run(sys.argv[2:]))
    sys.exit(run())
