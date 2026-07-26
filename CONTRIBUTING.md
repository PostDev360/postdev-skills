# Contributing to PostDev Skills

Thanks for wanting to help. This repo holds Claude Code skills — plain Markdown, no build step, no dependencies. That makes contributing easy, and it also means the bar for clarity is high: the Markdown *is* the product.

By contributing, you agree your contribution is licensed under the [MIT License](LICENSE).

## Ways to contribute

- **Report a problem** — a skill triggers when it shouldn't, doesn't trigger when it should, or gives bad guidance. [Open an issue](https://github.com/PostDev360/postdev-skills/issues/new/choose).
- **Improve an existing skill** — sharper wording, a missing question, a clearer example.
- **Add a translation** — the READMEs live in [`docs/i18n/`](docs/i18n/).
- **Propose a new skill** — please open an issue first so we can agree on scope before you write it.

## Repository layout

```
skills/<skill-name>/
├── SKILL.md          # required — the skill itself
└── references/       # optional — files SKILL.md tells the model to read on demand
docs/i18n/            # translated READMEs
.github/workflows/    # CI: validates every SKILL.md
```

## Skill requirements

Every `skills/<name>/SKILL.md` must have YAML frontmatter with exactly two keys:

```yaml
---
name: my-skill
description: Use this skill when ... It ... Skip this skill if ...
---
```

- `name` — lowercase, hyphen-separated, and **identical to the folder name**.
- `description` — under 1024 characters, written in the third person. It is the *only* thing the model sees when deciding whether to load the skill, so it must state **when to use it**, **what it does**, and **when not to use it**. Include the literal phrases a user would type.
- Body — under ~500 lines. Anything longer or only occasionally needed belongs in `references/`, loaded on demand.

CI enforces the mechanical parts of this. Run it locally before pushing:

```bash
python3 .github/scripts/validate_skills.py
```

## Writing guidance

These skills are read by a model, not compiled. What works:

- **Be imperative.** "Ask in batches of 3–4" beats "it may be helpful to ask a few questions at a time."
- **Show, don't describe.** A Bad/Good example pair is worth a paragraph of explanation.
- **State the boundaries.** When the skill should stop, and what it must never assume.
- **Cut anything the model already knows.** Generic advice dilutes the specific instructions that matter.
- **Keep it self-contained.** No external links the model needs to fetch to follow the skill.

## Pull requests

1. Fork the repo and branch from `main` (`fix/brief-wording`, `feat/skill-name`).
2. Make the change. Keep the diff focused — one skill or one concern per PR.
3. Run the validator.
4. **Test it for real**: copy the skill into `~/.claude/skills/`, start Claude Code, and confirm it triggers and behaves as intended. Describe what you tested in the PR.
5. Open the PR against `main` and fill in the template.

Changes to a skill's behaviour should also update the README section describing it. Translations can lag behind English — an out-of-date translation is not a blocker for merging.

## Code of Conduct

Participation is governed by the [Code of Conduct](CODE_OF_CONDUCT.md).
