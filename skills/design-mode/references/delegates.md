# Delegates

Skills and agents design-mode hands a step to when they are installed. Check your available skills and agents before routing. Fall back to the playbook's own steps when a delegate is missing, and say so in the reply. You own the delegate's output. Verify it like your own.

This table names third-party skills and their known defects, so it goes stale. Check it when a delegate behaves differently from what it says.

| Need | Delegate when installed | Caveat |
|---|---|---|
| Critique, polish, anti-slop detection, live iteration | `impeccable:impeccable` | A detector pass is evidence, not proof. |
| Critique template, research plan and synthesis scaffolds, UX copy, handoff template | `design:design-critique`, `design:user-research`, `design:research-synthesis`, `design:ux-copy`, `design:design-handoff`, `design:design-system` | `design:accessibility-review` labels SC 2.5.5 as AA. It is AAA. Cite WCAG directly for levels. |
| Read or write Figma, Dev Mode specs, design to code, libraries, Code Connect | `figma:figma-use`, `figma:figma-spec`, `figma:figma-design-to-code`, `figma:figma-generate-library`, `figma:figma-code-connect` | Load `figma:figma-use` before any Figma write. |
| Avoid the generic default look when generating UI | `frontend-design:frontend-design` | |
| Code and Figma audit | `anthropic-skills:design-auditor` | License unknown. Use it, do not copy it. |
| Token binding lint, layer naming, team handoff format | `anthropic-skills:figma-lint-bindings`, `anthropic-skills:bcif-figma-rename-ui`, `uxui-bcif-handoff:uxui-bcif-handoff` | |
| Component completeness, motion review, charts | `checklist-design:checklist-design`, `emil-design-eng`, `improve-animations`, `dataviz` | |
| UI implementation rules by file and line | Vercel `web-design-guidelines` | Not bundled. Install from `vercel-labs/agent-skills`. |
| WCAG 2.2 audits by specialist agents | Community-Access `accessibility-agents` | Not bundled. It installs an edit-gate hook. |
| Screenshots and live interaction | The built-in browser, the Playwright MCP, or the `run` skill | Use one fixed environment for every screenshot you compare. |
| A different model family's opinion | The `codex-bridge:codex-second-opinion` agent | Agreement across families is high signal. |

