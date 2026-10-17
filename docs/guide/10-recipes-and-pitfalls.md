# Recipes and pitfalls

## Recipes

Copyable prompts by task are in `skills/design-help/references/recipes.md`. Three to start with:

```
/mstack:design-mode audit [url] against WCAG 2.2 AA. per-criterion evidence, computed contrast, and keyboard walk. report only.
```

```
/mstack:critique [figma link]. objectives: new admins invite a teammate in under a minute. rate every finding 0 to 4.
```

```
/mstack:design-mode prepare a usability test for the new checkout. i'll run the sessions and send you the raw answers.
```

## Pitfalls

| What happens | Why | What to do |
|---|---|---|
| You get a description of screenshots | The proof step was skipped | Ask for the screenshot paths per state and viewport (prove-it-with-evidence). |
| A report quotes users nobody interviewed | An invented user claim | Say "label the evidence tier". Only a human-run study is tier 3. |
| The agent asks you which layout is better | It forgot that a prototype can answer | Say "prototype it and let the result decide" (propose-and-proceed). |
| A critique "agrees" on everything | Every seat ran on one model family | Install codex-bridge for seat G, or read the agreement as corroboration, not confirmation. |
| A contrast pass looks guessed | The ratio was not computed | Ask for `contrast.py` output. |
| A Figma link is ignored | No Figma server is connected | Connect the Figma MCP or Figma Console MCP, or attach exported frames. |
| An overnight run moved but finished nothing | `/loop` got a duration, not a check | Give it a predicate that can pass or fail. |
| A restart lost the thread | No trail was kept | Ask for Session pickup now, and for design-log before the next long run. |
| Runs cost more than expected | Panels and variants spawn many agents | Lower the budget in setup-mstack, use fewer variants, or merge critique to three seats. |

For a quick routing answer at any point, type `/mstack:design-help` with the question.
