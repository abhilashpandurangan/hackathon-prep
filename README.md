# hackathon-prep

Reusable skills for hackathons. Each skill is a self-contained playbook in
`skills/<name>/` that an AI assistant can follow to do hackathon work well:
preparing, building, demoing, and pitching.

## Skills

| Skill | What it does |
|---|---|
| `hackathon-playbook` | The full arc: researching the event, picking a winning build, pre-event prep, a build-day runbook, the demo, and follow-up. |
| `pitch-deck` | Automatically generates a hackathon pitch deck from your project facts: 5 slides, speaker notes, and a demo script. |

## Install a skill

Copy the skill folder into your assistant's custom skills directory:

```bash
cp -r skills/hackathon-playbook ~/workspace/custom-skills/
```

Each skill has a `SKILL.md` (the instructions) and a `skill.yaml` (its
metadata). No dependencies, no build step.

## Add a new skill

1. Create `skills/<skill-name>/SKILL.md` following the existing style:
   second person, one idea per bullet, sections named for what they do.
2. Add `skills/<skill-name>/skill.yaml` with name, title, description,
   category, and `include_in_prompt`.
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
