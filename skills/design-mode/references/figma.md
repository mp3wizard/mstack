# Reading Figma

How a design-mode step reads a Figma file. Two MCP servers can reach Figma, and they are good at different reads. Use whichever is connected, and both together when one read needs what each holds.

| Route | What it is | Reads best |
|---|---|---|
| **Official** | Figma's own hosted MCP server | One frame or node in depth: screenshot, layout and styles for a spec, the variables a node uses, Code Connect, design-system search |
| **Console** | Figma Console MCP, through its Desktop Bridge plugin in Figma Desktop | The whole file or system: every variable and style, annotations, comments, version history, lint and audits, FigJam contents, the current selection |

When the `anthropic-skills:figma-mcp-router` skill is installed, its Decision Matrix is the authority for routes and fallbacks. Read it first. This file covers only the read-only rows a design playbook needs.

## 1. Check what is connected

- Match tools by name, not by server prefix. Official tools can appear under more than one prefix (a hosted connector and a desktop server). Load them with ToolSearch, for example `get_screenshot`, `get_design_context`, or `figma_get_status`.
- Official is connected when `get_metadata` or `get_screenshot` is in your tool list.
- Console is connected when `figma_get_status` reports the Desktop Bridge as connected. The plugin must be running in Figma Desktop with the target file open. `figma_list_open_files` shows which file it is on.
- Neither connected → use frames or screenshots the user exports, and say so in the reply.

## 2. Parse the link

A Figma URL carries the file key after `/design/` or `/file/`, and the node in `node-id`. The URL writes the node ID with a hyphen (`node-id=12-345`). The API wants a colon (`12:345`). A link without `node-id` points at the whole file, so read its pages with `get_metadata` or `figma_get_file_data` before picking frames.

## 3. Pick the read

| Need | Official | Console |
|---|---|---|
| Screenshot of a frame as evidence | `get_screenshot` | `figma_take_screenshot`, `figma_capture_screenshot` |
| Layer tree, names, sizes, structure | `get_metadata` | `figma_get_file_data` |
| Layout and styles for a spec or code | `get_design_context` | `figma_get_component_for_development` |
| Variables and tokens a node uses | `get_variable_defs` | `figma_get_variables`, `figma_get_token_values`, `figma_browse_tokens` |
| Every style and text style in the file | | `figma_get_styles`, `figma_get_text_styles` |
| Export tokens to a DTCG file in the repo | | `figma_export_tokens` (confirm the active file first) |
| Component spec, variants, and states | `get_design_context` | `figma_get_component_for_development_deep`, `figma_analyze_component_set` |
| Which components already exist | `search_design_system`, `get_libraries` | `figma_search_components`, `figma_get_library_components` |
| Code Connect mapping to the codebase | `get_code_connect_map` | |
| Dev Mode annotations | | `figma_get_annotations` |
| Review comments | | `figma_get_comments` |
| FigJam board (research synthesis, journey maps) | `get_figjam` | `figjam_get_board_contents` |
| Who changed what, version diff | | `figma_get_file_versions`, `figma_diff_versions`, `figma_blame_node` |
| Design lint, accessibility scan, system audit | | `figma_lint_design`, `figma_audit_component_accessibility`, `figma_audit_design_system_report` |
| Design against code parity | | `figma_check_design_parity` |
| What the designer has selected | | `figma_get_selection` |

Default rule. A deep read of a few frames goes to Official. A file-wide or system-wide read goes to Console. Independent reads run in parallel.

Common pairings:

- **Spec a screen.** `get_screenshot` plus `get_design_context` per frame (Official), then `figma_get_annotations` for the designer's notes (Console).
- **Audit a design system.** `figma_get_variables` and `figma_get_styles` for the full token set, then `figma_audit_design_system_report` (Console). `search_design_system` (Official) finds what the libraries already hold.
- **Why was it designed this way.** `figma_get_comments` and `figma_get_file_versions` (Console) beside the decision records.

## 4. When a read fails

1. Retry once.
2. Use the other route's tool from the same table row. If the row has none, use exported frames from the user. Never substitute a different capability.
3. Say which route is active, for example "⚠️ Official MCP unavailable. Switched to Console." Never fail silently.
4. Console bridge down → wait about 15 seconds for it to reconnect, then run `figma_diagnose` or `figma_reconnect`.

## 5. Quota

Official reads count against the seat's quota. View and Collab seats get very few Official calls (6 per month in the figma-mcp-router data of 2026-10-03). On those seats, or after a rate-limit error, send bulk reads to Console. Console's version, diff, and blame tools use the REST API quota, so narrow them to one node or a short version range.

## 6. Reading is not writing

design-mode reads Figma. A Figma file is shared work, so any write is an outward action under the router's Always-pause list. That covers Official `use_figma` and every Console tool that creates, sets, imports, batches, posts a comment, or sets an annotation. Write only when the user asked for it. Load `figma:figma-use` before any `use_figma` call. With several files open, pin the target with `figma_navigate` and `lock: true` before a Console write.

## 7. Evidence

- Save every screenshot to the evidence dir with the file, frame, node ID, state, and viewport in its name.
- Quote token values with the node ID and the variable name they came from.
- A Figma lint or accessibility scan is a detector result (**principle-prove-it-with-evidence**). Compute contrast with `scripts/contrast.py` on the values you read.
- A Figma frame shows intent, not the shipped product. Judge the live UI when one exists, and treat the frame as the spec.
- Never send a file key, frame content, or a client's name to a third-party service.
