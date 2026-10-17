# Make it yours

## Pick your models

`/mstack:setup-mstack` writes `~/.mstack/models.md` with one line per role: delegates, judgment, mechanical, the six critique seats, the diverge variants, and the reflect tooling seat, plus a budget. Re-run it to change them. design-mode reads the file once per session, so a new choice applies from the next chat.

## Retro after a session

`/mstack:design-reflect` runs three reviewers over the session transcript and the decision trail (judgment, process and tooling, and a divergent seat on codex-bridge when installed), then a synthesizer that sorts their findings into Accepted, Rejected, and Backlog. It proposes edits only to skills and playbooks the session used, prefers a mechanism such as a checker rule over more prose, and applies nothing until you approve each row.

It reads only the current project's transcripts under `~/.claude/projects/`, never another project's.

## Edit the plugin

Clone the repo, add the clone as the marketplace (see the README), and edit the skills. After every change run:

```bash
python3 scripts/check-plugin.py
```

It fails when the router and the playbook or principle files disagree, when a path does not resolve, when a skill cites a URL from outside the research evidence, or when a skill repeats a known UX myth. A new playbook needs three things: the file, its line in the router's Playbooks section, and an intent line in `skills/design-mode/references/routes.txt`.

The scripts each have a self-test:

```bash
python3 skills/design-mode/scripts/contrast.py --self-test
```

```bash
skills/design-log/scripts/log.sh --self-test
```

Next: [Recipes and pitfalls](10-recipes-and-pitfalls.md).
