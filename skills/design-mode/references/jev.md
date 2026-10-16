# Jev judgments

Jev is TypeSafe's judgment model. It retrieves nothing and writes no prose. It returns typed judgments with probabilities on evidence you already hold. design-mode uses it in four places, always as a check beside your own reading, never as the decision.

## Availability

- Jev is on PATH when the `jev` command resolves (`command -v jev`). The research-team plugin ships it. It needs `TYPESAFE_API_KEY`, or the same line in `~/.config/typesafe/env`.
- No `jev`, no key, or a failed call → skip the Jev step, say so in one line of the reply, and continue with your own judgment. Never block on it.

## Rules for every use

- **Privacy.** Every call sends its text to api.typesafe.ai. Never send URLs, Figma file keys, client or product names, participant data, interview quotes, or anything personal. Handbook text and generic restatements are fine. When the needed text is confidential, skip Jev.
- **English.** Jev reads English best. Restate claims and queries in English.
- **Numbers belong to code.** Jev reads literally and is weak at numbers. Compute ratios, scores, and intervals with the scripts. Let Jev judge only the words.
- **It is a detector.** A Jev verdict is tier 1 evidence, like a lint pass (**principle-prove-it-with-evidence**). It never stands in for users, and it never settles a taste, brand, or product call.

## 1. Routing a task to a playbook

Use it when the task does not obviously match one playbook.

```bash
python3 scripts/route.py --task "<the task in one English sentence, no names or links>"
```

It ranks the intent lines in `references/routes.txt` and returns JSON.

- `pick` set → a clear winner. Confirm it against the playbook list before you open it.
- `ambiguous: true` → the top scores are close. Choose from `top3` yourself, and say in the reply why the pick fit.
- Exit 2 → Jev unavailable. Route by the playbook list. Exit 3 → the task carried a link or an ID. Restate it without them.

Measured on 2026-10-16 over ten sample tasks, the top score was right on nine. The miss ("checkout completion dropped, find out why") pulled toward the deceptive pattern audit on the word "checkout", and the policy returned it as ambiguous, which is the intended behavior. Keep `routes.txt` phrased as user intent, not playbook jargon. When you add a playbook, add its line.

## 2. Checking a claim before the reply

Use it for each load-bearing claim in a reply or a report: a WCAG criterion number or level, a threshold, a sample size, a benchmark, a law's scope, or a license statement (**principle-cite-the-law-in-scope**).

1. Find the passage in `../design-handbook/references/` that carries the claim. That text is local, so nothing about the client leaves the session.
2. Run `jev check "<claim in English>" <reference file> --quote "<short verbatim phrase from that passage>"`.
3. Read the verdict.
   - `verified` with `review: false` → use the claim.
   - `verified` with `review: true` → read the passage yourself before you use it.
   - `contradicted` → use what the reference says.
   - `unsupported` → the reference is silent. Find another source or label the claim unverified.
   - `fabricated` → the quote is not in the file. Fix the quote or drop the claim.
   - `numbers_missing` not empty → a figure in your claim is not in the source. Treat it as unverified, whatever the verdict.

## 3. Ranking critique findings

Use it in the **critique** skill's synthesis when the seats return more findings than you can read with care, roughly more than ten.

1. Write one finding per line, as `<finding ID> | <severity> | <the problem in one sentence>`. Drop screen names, client names, and links from the line.
2. Run `jev rank "<the agreed objectives and users, in one sentence>" < findings.txt`.
3. Read from the top. Jev reorders and never drops. A low score means "read later", not "dismiss". `ERR` means the call failed for that line, not that the finding is weak.
4. The Act on bucket still follows the critique skill's rules. Severity 3 and 4 findings, A or AA failures, and deceptive patterns stay in Act on whatever their rank.

## 4. Triaging sources during research

Use it when a step gathers outside sources, such as discovery's evidence inventory, prior art for a prototype, or refreshing a handbook reference. When the research-team skill is installed, follow it. It applies these same two steps.

1. More than about ten hits → write one per line as `<url> | <title> | <snippet>` and run `jev rank "<the question, in English>" < hits.txt`. Read and fetch from the top down. Public search hits may include their URLs, since they hold no client data.
2. Before you cite a fetched source, save its text to a file and run `jev check` on the claim you take from it, as in section 2.
