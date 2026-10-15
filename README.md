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
