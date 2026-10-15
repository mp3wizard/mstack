---
name: principle-propose-and-proceed
description: "Apply when tempted to ask the human a question on reversible design work. Answer it with a prototype, inspection, or measurement when you can. For taste, brand, or product calls, record an open decision with a labeled default and its evidence pack, and keep going. Always pause before outward or irreversible actions."
disable-model-invocation: true
---

# Propose and Proceed

Do not stop to ask what a prototype, an inspection, or a measurement can answer. Build it, observe it, and let the result decide.

Taste, brand, product strategy, and risk acceptance belong to a human. For those calls:

- **Record an open decision.** Write the default and its reason into the work, marked as the human's call. Attach its evidence pack. It holds screenshots per state and viewport, the alternatives you built, their tradeoffs, and your recommendation.
- **Keep working** through the handoff draft. Never block on the answer.
- **List the open decisions** in the final reply. `AskUserQuestion` blocks the turn, so use it at most once, as the very last action. Never use it under a session override such as "don't stop" or "going to bed".

**Prepare the study, not the verdict.** When a decision needs users, prepare the kit in **Usability test** (../design-mode/playbooks/usability-test.md) for an evaluative question or **Interview study** (../design-mode/playbooks/interview-study.md) for a generative one. Link published kits such as Krug's instead of copying their files. A human recruits and runs the sessions. Record the gap as a pending gate and continue.

**Always pause** before anything outward or irreversible:

- contacting participants, users, or stakeholders,
- publishing a shared library, page, or post,
- deleting or overwriting design files,
- merging, and any legal, compliance, or accessibility sign-off.

**Why:** Reversible design work is cheap to redo, so waiting usually costs more than a wrong default. Designers keep taste and quality sign-off for themselves. An evidence pack respects that without stalling the work.

## Misuse caveats

- A labeled default is not a decision. It stays an open decision until the human confirms it.
- "Which layout works better" is not a taste question when users can be watched doing the task. Prototype both and prepare the test.

## Grounded in

- [@aryanXmahajan](https://x.com/aryanXmahajan/status/2092087317624414561) on X (author's copyright, link only), agents cannot tell when a product feels cheap or confusing, so that judgment stays human.
- [@tangentstorm](https://x.com/tangentstorm/status/2109561963093106727) on X (author's copyright, link only), each change reaches a human-review column with a screenshot of the expected result while agents keep moving.
- [@educalvolpz](https://x.com/educalvolpz/status/2110038211678355706) on X (author's copyright, link only), the designer still checks error states, long text, keyboard use, and the 375 px width personally.
- [Steve Krug's test kit](https://sensible.com/download-files/) (Steve Krug, share with notice intact, never repost), scripts, a consent form, a prep checklist, and an observer handout for a human-run test.
- [GOV.UK Service Manual, user research](https://www.gov.uk/service-manual/user-research) (Crown copyright, OGL v3), planned rounds, recruitment, informed consent, and participant data as first-class steps.
