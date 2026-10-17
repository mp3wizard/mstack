# Handbook map: pstack to mstack

This document answers two questions:

1. If we apply poteto's method to the design process, which handbooks replace pstack's code-centric ones?
2. How does each pstack playbook, principle, and workflow skill map to its design-process equivalent?

It is also the build spec for this plugin. Every skill in `skills/` traces to a row here.

## Method

The research ran on 2026-10-15 through the `research-team` process. Seven parallel angles each used the channel that could reach them, and a completeness critic filled the gaps:

| Angle | Channel |
|---|---|
| SDLC design-process frameworks | wigolo web, anysearch, direct fetch, GitHub API |
| UX laws and heuristics | wigolo web, anysearch, Perplexity scholarly search |
| Accessibility and inclusive design | wigolo web, anysearch (w3.org primary) |
| Design systems, handoff, design QA | wigolo web, anysearch |
| User research, validation, metrics | wigolo web, anysearch, Perplexity scholarly search |
| Existing agent-skill handbooks | `gh` CLI, local filesystem, read-only Codex |
| Community signal | grok X search, verified through the X syndication API |
| Completeness critic | wigolo web, anysearch |

Totals: 148 sources and 197 claims recorded. 182 claims were checked with Jev (`jev check` against the fetched primary text): 163 verified, 12 contradicted, 7 unsupported. The other 15 stayed unchecked and are treated as unverified. The contradicted and unsupported claims that matter are listed in [Corrections](#corrections-the-plugin-must-not-repeat). The raw evidence, with local paths scrubbed, is in [`research/findings.json`](research/findings.json).

## What carries over unchanged

The method layer of pstack is domain-neutral. mstack keeps it as is:

- A router skill (`/design-mode`) matches the task to a playbook and copies the playbook's steps into the todo list verbatim. A skipped step stays in the list with `skip: <reason>`.
- Principles are leaf skills. The reply names each principle that changed a decision, and the specific choice it changed. poteto calls this the durable core of pstack, and it carries over to design as "name the heuristic".
- Every claim carries its evidence or its label (measured, inferred, or guess).
- Delegate subagents get file pointers, not inlined context, and the lead reviews their output instead of passing it through.
- Replies are short declarative sentences framed for the consumer and the maintainer.

## The one real conflict, and how mstack resolves it

pstack's principle `never-block-on-the-human` says: if you can observe the answer by running something, don't ask. Every design-process framework in the research gates on evidence from real users (GOV.UK phases, ISO 9241-210, the Double Diamond, Lean UX). An agent cannot recruit participants, and designers in the community signal keep taste and quality sign-off for themselves.

ISO 9241-210 separates inspection-based evaluation from user-based testing. mstack uses that split to define three evidence tiers:

| Tier | Who produces it | Examples | Can it prove usability? |
|---|---|---|---|
| 1. Inspection | The agent, now | Heuristic review, cognitive walkthrough, WCAG checks, computed contrast, screenshots, state coverage | No. Findings are hypotheses. |
| 2. Existing evidence | Already in the project | Past research, analytics, support tickets, recorded sessions | Partly. Cite it, don't extend it. |
| 3. New user evidence | A human runs it | Usability rounds, interviews, card sorts, experiments | Yes. |

The rules that follow from this:

- **Never fabricate user evidence.** No invented quotes, personas, participants, or findings. Ever.
- **Prepare the study, not the verdict.** When tier 3 is needed, the agent produces a ready-to-run kit (plan, tasks, script, consent, instruments, analysis template), runs tier 1 methods meanwhile, labels their output as unvalidated, and records the missing user evidence as a pending gate. It keeps working.
- **Propose and proceed.** Taste and brand calls go to a human as an evidence pack (screenshots per state and viewport, a recommendation, the alternatives). The agent does not stop to ask a taste question it can answer with a prototype.

## Handbooks to install or reference instead

### Layer 1: agent skills to delegate to

poteto-mode delegates `deslop` and `control-ui` to `cursor-team-kit` instead of re-implementing them. design-mode does the same with these skills. The router names them per playbook step and falls back to its own instructions when one is missing.

| Skill | Status when this plugin was built | License | Use it for | Caveat |
|---|---|---|---|---|
| `impeccable` (pbakaus/impeccable) | Installed (user's fork, 4.5.0) | Apache-2.0 | Critique, polish, anti-slop detector, live iteration | Its detector is evidence, not proof. Inspect the rendered UI too. |
| `design:*` (anthropics/knowledge-work-plugins/design) | Installed (1.2.0) | Apache-2.0 | Critique, handoff template, user-research and synthesis scaffolds, UX copy | Its accessibility-review quick reference labels SC 2.5.5 (44x44) as AA. It is AAA. Cite WCAG directly for levels. |
| `figma:*` (Figma official) | Installed | Unknown | Reading frames, Dev Mode specs, design-to-code, Code Connect, libraries | Delegate the mechanics. Do not copy its text. |
| `frontend-design` (anthropics/skills) | Installed | Apache-2.0 | Avoiding the generic default look when generating UI | The skill was rewritten. Older posts describe a different version. |
| `emil-design-eng`, `improve-animations`, `apple-design` (emilkowalski/skills) | Installed | MIT | Motion review, worst-case content, iOS-style polish | |
| `checklist-design` | Installed | MIT | Component completeness checklists | |
| `uxui-bcif-handoff`, `bcif-figma-rename-ui`, `figma-lint-bindings` | Installed (user's own) | User's own | Team handoff format, layer naming, token binding lint | |
| `design-auditor` | Installed | Unknown (no LICENSE upstream) | Code and Figma audit against 18 rules | Unknown license. Use it, don't vendor it. |
| Vercel `web-design-guidelines` (vercel-labs/agent-skills) | Not installed | MIT | File:line UI review against the Web Interface Guidelines | The only agent-native ruleset with MUST/SHOULD/NEVER rules. Fetches rules fresh. |
| `accessibility-agents` (Community-Access) | Not installed | MIT | WCAG 2.2 audits with specialist agents | Installs an edit-gate hook. Read it before enabling. |
| `web-quality-skills` (addyosmani) | Not installed | MIT | Core Web Vitals, Lighthouse, accessibility checks | |
| `design-review` agent (OneRedOak/claude-code-workflows) | Not installed | MIT | Seven-phase live-browser design review at three viewports | Targets WCAG 2.1. mstack's design-qa playbook adapts it to 2.2. |

Install commands for the missing ones live in the README.

### Layer 2: handbooks as the source of truth

Each principle and playbook cites these. How we may use each one depends on its license, which the research recorded per source.

**Tier A. Adaptable with attribution.** We may adapt the text inside our skills, keeping the attribution line.

| Handbook | License | Grounds |
|---|---|---|
| GOV.UK Service Manual and Service Standard (14 points) | OGL v3 | Lifecycle spine: discovery, alpha, beta, live, with exit criteria. User research, measuring success, accessibility testing, writing for user interfaces. |
| Design Council Framework for Innovation (Double Diamond) and Systemic Design Framework | CC BY 4.0 | Diverge then converge. Four design principles. |
| 18F Methods (now in GitHub `18F/guides`) and USDS Digital Services Playbook (`usds/playbook`) | CC0 / US public domain | Method cards for discover, decide, make, validate. Service-quality questions. |
| U.S. Web Design System, including the component lifecycle | CC0 / US public domain | Component maturity and deprecation. |
| GOV.UK Design System contribution criteria | OGL v3 | Evidence before adding a component. |
| Vercel Web Interface Guidelines | MIT | UI implementation rules. |
| Playwright visual comparisons | Apache-2.0 | Pixel-diff evidence for design QA. |
| ICO Age appropriate design code, UK Analysis Function charts guidance | OGL v3 | Children's privacy defaults. Chart review. |
| Digital.gov plain-language guides | CC0 | Content design. |

**Tier B. Quote with notice, never adapt.** (Carbon's site text is treated as tier C. Its repo is Apache-2.0, but no text is adapted here.) These allow copying with the license notice but no derivatives, or impose ShareAlike on adapted text. Skills cite the criterion or section, paraphrase in our own words, and quote verbatim only in short spans with the source named.

| Handbook | License | Grounds |
|---|---|---|
| WCAG 2.2 and WCAG 3.0 Working Draft (W3C TR) | W3C Document License (no derivatives) | Accessibility gate. Success criterion numbers and levels. |
| Understanding WCAG 2.2, ACT Rules, WAI-ARIA APG, WCAG-EM 2, COGA, W3C Accessibility Maturity Model | Pages link the W3C Software and Document License, but WAI's permission page puts most WAI material under the Document License. Default to cite and paraphrase. | How-to for each criterion, conformance method, component keyboard models, cognitive accessibility. |
| W3C Design Tokens (DTCG) 2025.10 Format module | W3C Community Final Specification Agreement | Token format and validation. |
| W3C Internationalization quick tips and RTL authoring | W3C Document License | i18n and RTL readiness. |
| Inclusive Design Principles | CC BY-SA (version ambiguous between 4.0 and 2.0 UK) | Inclusive critique. ShareAlike would bind adapted text, so we link. |

**Tier C. Link and paraphrase only.** All rights reserved, unknown, or no-derivatives. We cite clause or section names and write the guidance in our own words.

- Nielsen Norman Group: 10 usability heuristics, heuristic evaluation, severity ratings, 5-user and 40-user sample sizes, card-sort sizing, cognitive walkthrough, design critiques, UX maturity, service blueprints, aesthetic-usability effect. The heuristics page allows using the heuristics with credit and a link.
- Laws of UX (Jon Yablonski): CC BY-NC-ND 4.0. Use it as a designer-facing index only, and never repeat its folk versions (see Corrections).
- Dieter Rams' ten principles (Vitsoe): CC BY-NC-ND 4.0.
- Don Norman, *The Design of Everyday Things* (2013): signifiers, mapping, feedback, constraints, conceptual models, gulfs of execution and evaluation, slips vs mistakes.
- Ben Shneiderman's eight golden rules. Bruce Tognazzini's First Principles of Interaction Design (personal-use copies only).
- ISO 9241-210:2019 (human-centred design activities) and ISO 9241-110:2020 (interaction principles). Paywalled. Cite clause names only.
- Apple Human Interface Guidelines. Copyrighted, and Apple's site terms forbid scraping. Material Design 3 guideline text has no license we could find. Fluent 2 site text falls under the Microsoft Terms of Use.
- Atomic Design (Brad Frost), Refactoring UI, Scott Hurff's UI stack, OOUX/ORCA (Sophia Prater).
- Steve Krug's books and test kit (share downloads with the notice intact, never repost), MeasuringU (SUS, SEQ, UX-Lite norms), Google HEART (Rodden et al., CHI 2010), Kohavi et al. on trustworthy experiments, Teresa Torres on continuous discovery, the Christensen Institute on Jobs to Be Done, Strategyn ODI.
- Shape Up, SVPG, GV Design Sprint, Lean UX.
- deceptive.design (all rights reserved), FTC 2022 dark patterns report, EDPB Guidelines 03/2022 v2.0, DSA Article 25.
- Microsoft HAX Toolkit (license unknown) and Google PAIR Guidebook (CC BY-NC-SA) for AI features.
- Microsoft Inclusive Design toolkit (Persona Spectrum). No open license found.

**Tier D. Non-commercial licenses, never blend into MIT text:** IDEO.org Field Guide (CC BY-NC-ND 3.0), Stanford d.school Bootleg (CC BY-NC-SA 4.0), Google PAIR (CC BY-NC-SA 4.0), Mailchimp Content Style Guide (CC BY-NC 4.0). Link to them.

## Mapping: playbooks

Legend. **Replace**: a design playbook takes its slot. **Adapt**: same playbook, design-grounded steps. **Route**: domain-neutral harness work, use pstack's playbook when pstack is installed. **Drop**: no design meaning.

| pstack playbook | Decision | mstack playbook | Grounded in |
|---|---|---|---|
| investigation | Replace | `discovery` (problem framing, evidence inventory, regimes, go or no-go) and `investigation` (read-only "how does this flow work, why was it designed so") | GOV.UK discovery, Double Diamond Discover and Define, 18F, JTBD |
| bug-fix | Replace | `ux-defect-fix`: reproduce on the real surface, classify slip vs mistake, fix the signifier, mapping, or constraint, re-run the same task | Norman ch. 5, NN/g heuristics, ISO 9241-110 |
| perf-issue | Replace | Folded into `ux-defect-fix` (perceived latency) and `metric-hillclimb` | Doherty and Thadhani 1982 (sub-second, not 400 ms), Nielsen H1 |
| hillclimb | Replace | `metric-hillclimb`: one change per round, HEART metric, experiment integrity checks | Rodden et al. 2010, Kohavi et al. 2020 |
| runtime-forensics, trace-forensics | Replace | Folded into `metric-hillclimb` step 1 (funnel and analytics forensics against a HEART plan) | HEART, GOV.UK measuring success |
| feature | Replace | `feature-design`: objects first, flows, state matrix, diverge, converge, spec | OOUX, UI stack, Double Diamond Develop, Carbon |
| refactoring | Replace | `design-system-refactor`: token drift audit, consolidate, deprecate through a lifecycle, pinned visual baseline | DTCG 2025.10, USWDS lifecycle, Playwright |
| prototype | Adapt | `prototype`: test the riskiest assumption at the lowest fidelity that answers it, variants behind a switcher | GOV.UK alpha, Lean UX, GV Sprint |
| visual-parity | Adapt | `design-qa`: live UI at three viewports, pixel diff per state, worst-case content, accessibility | Carbon checklist, Playwright, OneRedOak, Vercel WIG |
| eval | Replace | `usability-test`: study kit for a human to run, then synthesis. Card sort and tree test kits live here too. | Krug, NN/g, GOV.UK, Nielsen and Landauer 1993 |
| opening-a-pr | Replace | `design-handoff`: the spec package, invoked at the end of every design-producing playbook | ISO 9241-210 7.4.5, Carbon, Figma Dev Mode, Shape Up pitch |
| shipping | Replace | Folded into `design-handoff` and `accessibility-audit` (WCAG-EM 2 conformance statement) | WCAG-EM 2 |
| multi-phase-plan | Replace | `design-sprint` for a time-boxed sprint. pstack's multi-phase-plan otherwise. | GV Sprint |
| babysit | Route | Use pstack. Design review rounds run through the `critique` skill. | |
| autonomous-run, orchestrate, autopilot-full, autopilot-stack | Route | Use pstack's playbooks unchanged. | |
| session-pickup, pause-safely | Adapt | `session-pickup` and `pause-safely`: resume notes and decision logs under `.mstack/<slug>/`, Figma read-only, no outward action to pause | pstack |
| authoring-a-skill, worktree-cleanup | Drop | Not design work. | |
| (none) | New | `heuristic-review` | NN/g HE method and severity ratings, ISO 9241-110, Shneiderman, Norman |
| (none) | New | `accessibility-audit` | WCAG 2.2, ACT Rules, APG, WCAG-EM 2, GOV.UK accessibility testing |
| (none) | New | `deceptive-pattern-audit` | deceptive.design, EDPB 03/2022, FTC 2022, DSA Art. 25, ICO code |
| (none) | New | `content-design` | GOV.UK writing for UIs, Digital.gov plain language |
| (none) | New | `design-system-component` | GOV.UK contribution criteria, Carbon checklist, DTCG, APG, USWDS lifecycle |
| (none) | New | `ai-feature-design` | Microsoft HAX, Google PAIR |
| (none) | New | `measure` (metrics plan before build, experiment readout, maturity retro) | HEART, GOV.UK Service Standard point 10, Kohavi, NN/g maturity, W3C AMM |

## Mapping: principles

| pstack principle | Decision | mstack principle |
|---|---|---|
| attack-the-premise | Replace | `principle-frame-the-problem` |
| exhaust-the-design-space | Replace | `principle-diverge-then-converge` |
| sequence-verifiable-units | Replace | `principle-riskiest-assumption-first` (includes the fidelity ladder) |
| laziness-protocol, subtract-before-you-add | Replace | `principle-as-little-design-as-possible` |
| experience-first, outcome-oriented-execution | Replace | `principle-user-outcome-first` |
| model-the-domain, foundational-thinking, redesign-from-first-principles | Replace | `principle-model-the-objects` |
| type-system-discipline | Replace | `principle-design-every-state` |
| boundary-discipline, make-operations-idempotent | Replace | `principle-design-for-error-and-reversal` |
| minimize-reader-load | Replace | `principle-minimize-cognitive-load` |
| (none) | New | `principle-follow-conventions` |
| (none) | New | `principle-signify-and-give-feedback` |
| (none) | New | `principle-accessible-by-default` |
| (none) | New | `principle-honest-design` |
| build-the-lever, encode-lessons-in-structure | Replace | `principle-encode-decisions-in-the-system` |
| migrate-callers-then-delete-legacy-apis | Replace | `principle-deprecate-through-a-lifecycle` |
| prove-it-works | Replace | `principle-prove-it-with-evidence` |
| (none) | New | `principle-never-fabricate-user-evidence` |
| explain-the-number | Replace | `principle-explain-the-metric` |
| (none) | New | `principle-cite-the-law-in-scope` |
| fix-root-causes | Replace | `principle-fix-the-design-cause` |
| test-behavior-not-implementation | Replace | `principle-observe-behavior-over-opinion` |
| never-block-on-the-human | Replace | `principle-propose-and-proceed` |
| guard-the-context-window, separate-before-serializing-shared-state | Keep (domain-neutral) | Stated inline in the router. Not duplicated. |

## Mapping: workflow skills and agents

| pstack | mstack |
|---|---|
| `interrogate` (multi-model adversarial review) | `critique`: independent lens reviewers (heuristics, accessibility, cognition and laws, conventions and system consistency, content, ethics), diverse models including Codex when installed, findings stated as problems against objectives with a heuristic or criterion ID and evidence |
| `arena` | `diverge`: N variants behind one switcher, cross-judge, pick a base, graft |
| `how`, `why`, `teach` | `investigation` playbook |
| `unslop` | Delegate to `impeccable` (anti-slop detector) plus the `ui-slop-sicko` agent |
| `benchmark-checklist` | `principle-explain-the-metric` plus `scripts/sus.py` |
| `show-me-your-work` | `design-log`: the same append-only TSV with an evidence `tier` column, `log.sh`, a transcript audit, and a cross-model trail review. The evidence pack in `design-handoff` links it. |
| `reflect` | `design-reflect`: three reviewers (judgment, process and tooling, divergent) and a synthesizer over the session, edits only after approval |
| `correct` | `measure` playbook, maturity retro step |
| `figure-it-out` | `bespoke-run` playbook |
| `setup-pstack` | `setup-mstack`: per-role models and a budget in `~/.mstack/models.md`, using Claude Code's `Agent` model aliases |
| `poteto-help` | `design-help` |
| `poteto-agent` | `design-agent` |
| `comment-sicko` | `ui-slop-sicko`: an independent hunter that sees only the rendered UI and hunts generic AI-UI tells and visual bugs |
| none | `design-handbook`: reference skill holding the laws, heuristics, standards, numbers, and the license-tagged bibliography |

Levers (scripts a reviewer can rerun): `scripts/contrast.py` computes the WCAG 2.x contrast ratio and checks it against 1.4.3, 1.4.6, and 1.4.11. `scripts/sus.py` scores the System Usability Scale. `scripts/route.py` asks Jev to rank the playbooks for a task. `design-log/scripts/log.sh` appends decision rows with the spreadsheet-formula guard. Each carries a `--self-test`.

## Corrections the plugin must not repeat

These came back contradicted or unsupported against primary sources. Skills must state the corrected form.

| Folk claim | What the primary source says | Source |
|---|---|---|
| Keep menus to 7 ± 2 items (Miller) | Miller 1956 is about absolute judgment and immediate memory span. Current working-memory estimates are about 3 to 5 chunks. Menus use recognition, not recall, so they need no 7-item cap. | Cowan 2010; NN/g short-term memory article |
| The Doherty threshold is 400 ms | The 1982 IBM text argues for sub-second response. 400 ms is a later popularization. Say "aim for sub-second". | Doherty and Thadhani 1982 reproduction (Jev: unsupported) |
| Hick's law limits menu length | Hick 1952 measured choice reaction time to up to 10 stimuli. Menu selection can be scan-bound. | Hick 1952; Landauer and Nachbar 1985 |
| More options always cause choice overload | The meta-analytic mean effect is close to zero, with high variance. | Scheibehenne et al. 2010 |
| Pretty designs are more usable | The aesthetic-usability effect concerns perceived usability. Polished prototypes inflate ratings. | NN/g |
| Be liberal in what you accept (Postel) as a UX rule | Postel's law comes from networking, and RFC 9413 warns that tolerance can harm interoperability. | RFC 9413 |
| 5 users find 85% of problems | 85% is an average that assumes λ ≈ 0.31 and one homogeneous user group. Individual 5-user samples found 55% to 99%. NN/g says about 15 users for full coverage. For qualitative rounds it recommends about 5 for one group, 3 to 4 each for two groups, and at least 3 each for three or more. | Nielsen and Landauer 1993; Faulkner 2003; Spool and Schroeder 2001 |
| NN/g recommends 20 users for quantitative studies | That was 2006. The current figure is 40. | NN/g |
| A SUS of 68 means 68% | 68 is the average, at about the 50th percentile. SUS scores are not percentages. | MeasuringU |
| HEART means tracking all five categories | The paper says to choose the categories explicitly. | Rodden et al. 2010 |
| ODI opportunity = importance − satisfaction | Opportunity = importance + max(0, importance − satisfaction). | Strategyn |
| An expert review can replace usability testing | NN/g says heuristic evaluation complements user research and cannot replace it. A single evaluator finds about 35% of problems, and Nielsen recommends 3 to 5 evaluators. Parallel model passes are not independent evaluators, so never claim a coverage percentage. | NN/g |
| WCAG 2.5.5 (44 × 44) is a AA criterion | 2.5.5 Target Size (Enhanced) is AAA. WCAG 2.2 adds 2.5.8 Target Size (Minimum) at AA: 24 × 24 CSS px, with exceptions. | WCAG 2.2 |
| APCA is the WCAG 3 contrast algorithm | The WCAG 3 Working Draft (10 Sep 2026) leaves the contrast algorithm undetermined. Use WCAG 2.x ratios as the gate. APCA may appear as an advisory column only. | WCAG 3.0 WD |
| WCAG 2.2 dates from October 2023 | It was republished on 12 Dec 2024. Cite that edition. 4.1.1 Parsing is removed in 2.2. | W3C |
| EN 301 549 already requires WCAG 2.2 in the EU | V4.1.1 (Sep 2026) aligns with WCAG 2.2 but is not yet cited in the Official Journal. The legal EU reference is still V3.2.1 (WCAG 2.1 AA). | ETSI, EAA |
| Section 508 tracks current WCAG | Section 508 still incorporates WCAG 2.0 AA. | US Access Board |

## Source status changes found on 2026-10-15

- `methods.18f.gov` and `guides.18f.gov` no longer resolve. 18F Methods live in GitHub `18F/guides`. `18F/methods` was archived on 2024-05-31.
- The USDS playbook repo moved from `whitehouse/playbook` to `usds/playbook`.
- Cagan has retired the term "dual-track agile" in favor of continuous discovery and delivery.
- Lean UX Canvas v2 has been replaced by the Lean Product Canvas and the Lean Strategy Canvas.
- DTCG 2025.10 is the stable token format. An editor's draft dated 2026-09-08 exists.
- WCAG-EM 2 (23 Jul 2026) now covers apps. The W3C Accessibility Maturity Model became a Group Note on 2025-11-04.
- The W3C Web Sustainability Guidelines are a Group Note Draft (2026-09-24). They are advisory, not a gate.
- The US Federal Plain Language Guidelines are no longer on a .gov site.

## Known gaps

The research could not fill these. Skills that touch them say so instead of guessing.

- DesignOps: no open-licensed framework found.
- Service design method libraries: licenses undetermined. NN/g's blueprint definition is the only grounding.
- Forms design depth: GOV.UK question protocol, Adam Silver's Form Design Patterns, and Baymard were not researched.
- RITE method (Medlock et al. 2002), the cleanest hillclimb analog: not fetched.
- ISO 9241-210 clause 7.4.5 body and ISO 9241-11:2018 usability definition: not read (paywalled).
- Australian Digital Service Standard criteria: not retrieved.
- Zeigarnik effect replication status: not researched. Treat it as weak evidence.
- Typography and color theory beyond tokens: no open primary source identified.
- The FTC "click-to-cancel" rule's legal status: not verified. Do not cite it.

## pstack on Claude Code: known gaps

pstack is installed from the Cursor source as `pstack@pstack-local`. `claude plugin details` shows 54 skills and 2 agents registered. It was written for Cursor, so on Claude Code:

- `poteto-agent` looks for its SKILL.md under `~/.cursor/plugins/`. It fails unless the parent passes an absolute path.
- Model slugs such as `grok-4.7-xhigh-fast` and `claude-opus-5-5-xhigh` are not valid values for Claude Code's `Agent` `model` parameter.
- `Task`, `AskQuestion`, `is_background`, and `/setup-pstack` writing a `.cursor/rules` file are Cursor-only.
- `deslop`, `control-ui`, and `control-cli` come from `cursor-team-kit`, which is not installed.
- Plugin agents register under the plugin namespace on Claude Code (`pstack:poteto-agent`). The bare name errors.

`michael-denyer/pstack-claude` (MIT) is a maintained Claude Code port that translates these primitives. Prefer it when you want pstack itself on Claude Code. mstack avoids all of these by using Claude Code primitives directly.
