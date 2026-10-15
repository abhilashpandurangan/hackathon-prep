---
name: repo-polish
description: Audits and rewrites the project README for judge scan-reading, generates the architecture diagram from the actual code, and enforces repo hygiene. Use after a hackathon build works but before judging.
---

# Repo Polish

Use this skill when the build works and judging is near. In async judging
the README is the front door: judges scan dozens of projects and decide in
seconds which ones deserve a closer look. It works with any AI agent; adapt
the tool names to whatever your agent provides.

## Rewrite the README for scan-reading

- Restructure the README into this order, top to bottom:
  - Hero block: one-liner, badges, one hero screenshot or GIF, and the live
    demo link above the fold.
  - 30-second pitch: what it is, who it is for, why it matters.
  - Feature gallery: three screenshots maximum, each with a one-line
    caption tied to a demo beat.
  - Architecture: a Mermaid diagram generated from the actual codebase, not
    imagined. Read the imports and the data flow first.
  - Quick start: clone and running in under 5 minutes, copy-paste commands
    only.
  - Tech stack: what the repo actually imports.
  - Known limitations: one honest paragraph. Judges trust transparency more
    than perfection.
  - License.

- Keep it under 500 lines. Move anything longer into linked sub-documents.

- Output a punch list alongside the rewrite: for each existing section,
  mark it keep verbatim, rewrite, delete, or move to a sub-doc. Show the
  list before rewriting so the builder can veto.

## Generate the architecture diagram

- Read the code and draw what is there: components, data flow direction,
  and external services. Never draw aspirational architecture.

- Use Mermaid so it renders natively on GitHub. Keep it to seven boxes or
  fewer; a diagram nobody can parse at a glance is decoration.

- Label every arrow with what actually travels across it: a query, a
  webhook, a file, an API response.

## Run the hygiene audit

- `requirements.txt` exists with pinned versions.
- `.env.example` exists and no real secrets are committed anywhere. Scan
  for API keys, tokens, and private keys in the history you are about to
  push; report anything found before it goes public.
- `.gitignore` excludes secrets, virtual environments, and local data
  stores.
- `LICENSE` exists.
- Screenshots are current: no empty placeholders, no debug HUD, no
  localhost URLs that only work on the builder's machine.

- Present failures as a checklist with fixes, ordered by what a judge would
  notice first.

## External plugins and skills

- If your agent has a plugin marketplace, look for diagram or Mermaid
  plugins when the architecture is complex. For most hackathon projects the
  hand-written Mermaid block this skill produces is enough.

- If your agent can capture screenshots (for example through a browser
  tool), use it to refresh the feature gallery against the running app.
  Otherwise ask the builder for three fresh screenshots and place them.

- Pair with the `devpost-submission` skill in this repo: the polished README
  is what the Devpost repo link points at.
