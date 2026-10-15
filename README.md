# hackathon-prep

Reusable, agent-agnostic skills for hackathons. Each skill is a
self-contained playbook in `skills/<name>/` that any AI agent can follow:
Claude Code, Cursor, Copilot, ChatGPT, Muse, or anything else that reads
markdown instructions.

Skills follow the open `SKILL.md` convention: a single markdown file with
`name` and `description` frontmatter, no vendor lock-in, no special tools
required.

## Skills

| Skill | What it does |
|---|---|
| `hackathon-playbook` | The full arc: researching the event, picking a winning build, pre-event prep, a build-day runbook, the demo, and follow-up. |
| `pitch-deck` | Automatically generates a hackathon pitch deck from your project facts: 5 slides, speaker notes, and a demo script. |
| `agent-starter` | Generates a minimal working starter for an agentic app: ADK, LangGraph, or RAG, each with a simple chat UI. |
| `devpost-submission` | Generates a complete, paste-ready Devpost submission packet from the project repo, plus a pre-submit audit against the event's rules. |
| `demo-video` | Generates a timed, shot-by-shot demo video script with spoken voiceover lines, a recording checklist, and export and upload specs. |
| `repo-polish` | Audits and rewrites the project README for judge scan-reading, generates the architecture diagram from the actual code, and enforces repo hygiene. |
| `judge-qa` | Generates a judge Q&A bank from the event rubric and the project, with drafted answers and backup-slide content for the hard questions. |
| `sponsor-tracks` | Maps the event's sponsor tracks, prizes, and APIs into a prize matrix and shows which sponsor bounties the build qualifies for. |

## Starter templates

Runnable starting points in `templates/`, each with its own README:

- `templates/adk-starter/` — Google ADK agent + Streamlit chat UI
- `templates/langgraph-starter/` — LangGraph ReAct agent + Streamlit chat UI
- `templates/rag-starter/` — local ChromaDB RAG + Streamlit UI (works with no API key; generated answers when `OPENAI_API_KEY` is set)

## Install a skill

Point your agent at `skills/<name>/SKILL.md`, or copy the folder into your
agent's skills directory. Examples:

```bash
# Claude Code
cp -r skills/hackathon-playbook ~/.claude/skills/

# Cursor (~/.cursor/skills) or your agent's equivalent
cp -r skills/pitch-deck <your-agent-skills-dir>/
```

No dependencies, no build step. If your agent auto-discovers skills, drop
the folder in and mention the skill by name.

## Add a new skill

1. Create `skills/<skill-name>/SKILL.md` with `name` and `description`
   frontmatter, following the existing style: plain second person, one idea
   per bullet, sections named for what they do.
2. Keep it agent-agnostic: describe capabilities ("use web search", "open the
   page in your browser tool"), never name one vendor's tools or paths.
3. List it in the table above.

## Inspiration

Patterns in these skills are borrowed from real hackathon builds:

- `DEMO_SCRIPT.md` checked into the repo and a cached demo fallback that
  runs without API keys (EarningsPulse, Money Talks 1)
- No-invention guards that reject model-generated figures not grounded in
  real data, plus human approval gates before anything touches money
  (Paceline, PayPal AI Hackathon)
- Red-team scripts that prove the agent refuses attacks live: prompt
  injection, duplicate invoices, bank-detail swaps (GlassLedger, DivHacks)
- Published failure logs as a credibility move (Lease Lens)
- Quantified pitches: time saved, cost per case, test counts
  (C:DIR Agentic Regulator Hackathon winners)
