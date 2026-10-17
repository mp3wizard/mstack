---
name: setup-mstack
description: "Configure which model mstack uses per role (delegates, judgment, mechanical sweeps, critique seats, diverge variants, reflect reviewers) and at what reasoning budget. Writes ~/.mstack/models.md, which design-mode, critique, diverge, and design-reflect read before their defaults. Use for /setup-mstack, 'configure mstack models', 'mstack budget', or changing mstack's model choices."
disable-model-invocation: true
---

# Setup mstack

Write `~/.mstack/models.md`, a small file of role lines that mstack's skills read before their own defaults. Without the file, every skill keeps its defaults, so this setup is optional.

## 1. Know the valid values

The Agent tool's `model` parameter accepts the aliases it advertises in this session, such as `opus`, `sonnet`, `haiku`, and `fable`. Read the advertised list from the Agent tool's schema. Never write a value it does not advertise. `inherit` is always valid and means the role runs on the parent session's model, so the Agent call omits `model`.

A role that names another plugin's agent, such as the critique skill's seat G on **codex-bridge:codex-second-opinion**, keeps that agent's own model. This file does not change it.

## 2. Load the current state

If `~/.mstack/models.md` exists, read it and treat its `budget` line and role lines as the current choices. Otherwise start from the defaults in step 5. Drop a line whose role is not in step 5, and list it as dropped.

## 3. Ask for a budget

Ask once with AskUserQuestion. Name the current budget when the file records one, and say that `standard` matches the skill defaults.

- `max`: every role at `effort: max`.
- `high`: every role at `effort: high`.
- `standard`: no `effort` set, so each call uses the model's own default. This matches the skill defaults.
- `lean`: judgment roles stay as they are, and delegate and mechanical roles drop to `haiku` where the user agrees.

The skills pass the budget as the Agent tool's `effort` parameter. Because this file is the user's own instruction for these calls, setting `effort` from it is allowed.

## 4. Show the roles and confirm

Show every role with its value. Ask whether to accept them or change specific roles, offering the advertised aliases plus `inherit`. Ask with AskUserQuestion, at most twice in this skill, and never under a session override. Two roles hold lists. `critique seats` is a fixed mapping of exactly six entries, one per seat A to F. `diverge variants` is a rotation: the diverge skill cycles through it for however many variants the task needs, so its length does not set the count.

## 5. Write the file

Overwrite the whole file so a re-run stays idempotent. Create `~/.mstack/` if it is missing. Shape and defaults:

```
# mstack model configuration. One line per role. Delete a line to fall back to the skill default.
# Values: an Agent tool model alias, or `inherit` for the parent session's model.
budget: standard
delegates: sonnet
judgment: opus
mechanical: haiku
critique seats: opus, sonnet, opus, sonnet, sonnet, opus
diverge variants: opus, sonnet
reflect tooling: sonnet
```

What each role controls:

- **delegates.** `mstack:design-agent` calls inside playbook steps: variants, kits, specs.
- **judgment.** The design-mode judgment default, the diverge judge's fallback model, and design-reflect's judgment seat, divergent fallback, and synthesizer.
- **mechanical.** Screenshot sweeps and other mechanical batches.
- **critique seats.** Seats A to F of the critique skill, in order. Seat G is not in the list.
- **diverge variants.** The models the diverge skill cycles through for its N variants.
- **reflect tooling.** design-reflect's process and tooling seat.

## 6. Validate and confirm

Read the file back. Every role value must be an advertised alias or `inherit`, the budget must be `max`, `high`, `standard`, or `lean`, and `critique seats` must hold six entries. Then tell the user the file path, the budget, and any role that differs from the defaults. design-mode reads the file once per session, so the new choices apply from the next chat. Re-running this skill updates it.

Adapted from pstack's setup-pstack skill (see NOTICE.md).
