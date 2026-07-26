# PostDev Skills

Open-source [Claude Code](https://claude.com/claude-code) skills, built for people shipping real products.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-1-green.svg)](#skills)
[![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![ko-fi](https://img.shields.io/badge/support-ko--fi-ff5e5b.svg)](https://ko-fi.com/postdev360)

**Read this in other languages:** [Français](docs/i18n/README.fr.md) · [中文](docs/i18n/README.zh.md) · [Español](docs/i18n/README.es.md)

---

## Skills

| Skill | What it does |
| --- | --- |
| [**app-blueprint**](skills/app-blueprint/) | Runs a short, plain-language discovery interview *before* any code or architecture is proposed for a new app, product, or feature — then writes a `PROJECT_BRIEF.md` you confirm. |

## Install

Each skill is a self-contained folder. Copy the ones you want into your skills directory.

**For a single project** — the skill is available in that project only, and can be committed alongside it:

```bash
mkdir -p .claude/skills
git clone --depth 1 https://github.com/PostDev360/postdev-skills.git /tmp/postdev-skills
cp -r /tmp/postdev-skills/skills/app-blueprint .claude/skills/
rm -rf /tmp/postdev-skills
```

**For every project on your machine** — the skill is available everywhere:

```bash
mkdir -p ~/.claude/skills
git clone --depth 1 https://github.com/PostDev360/postdev-skills.git /tmp/postdev-skills
cp -r /tmp/postdev-skills/skills/app-blueprint ~/.claude/skills/
rm -rf /tmp/postdev-skills
```

Then start Claude Code and run `/skills` to confirm it is loaded. Skills trigger automatically when your request matches their description — you can also invoke one by name.

## app-blueprint

### Why it exists

Non-technical founders and early-stage builders often ask an AI assistant to "build my app" without realizing how many decisions get made silently along the way — whether to add user accounts, whether data persists, which platforms to target, what the true v1 scope is. App Blueprint forces those decisions into the open first, as a conversation, so the person who owns the product owns the trade-offs — not the AI.

### When it triggers

Automatically, whenever you want to start a new app/product/feature and the requirements aren't yet clear ("I want to build an app", "help me create a project", "I have an idea for a tool"), or when you jump straight to asking for code with no defined scope. It steps aside if you already provided a clear spec, or explicitly ask to skip discovery.

### How it works

1. Asks questions in plain language, translating technical trade-offs into real-world consequences — e.g. *"if someone closes the app and comes back tomorrow, should their information still be there?"* instead of *"do you need persistent storage?"*
2. Asks in small batches of 3–4 related questions, never one long questionnaire, using multiple-choice prompts where the answers are concrete.
3. Covers seven categories in order: purpose & audience, people & access, information & memory, where/how it's used, scope & priority, practical constraints, integrations & look — skipping a category only if you already answered it unambiguously.
4. Writes a **Project Brief** to `PROJECT_BRIEF.md` and asks you to confirm or correct it before any architecture or code is written.
5. Runs in whichever language you write in.

### After the brief is confirmed

Two principles carry forward into the build itself:

- **Concise reporting** — status updates and summaries stay short throughout the build, to keep token usage down over a long project.
- **Modular, block-based construction** — the app is structured as independent, loosely-coupled modules so adding or removing a feature later touches only its own block, not the whole codebase.

### Output

A confirmed, written Project Brief that becomes the source of truth for all following implementation work.

## Contributing

Contributions are welcome — new skills, improvements to existing ones, translations, and bug reports alike. Start with [CONTRIBUTING.md](CONTRIBUTING.md), and see the [Code of Conduct](CODE_OF_CONDUCT.md).

## License

[MIT](LICENSE) © PostDev360

## Support

If these skills save you time, you can support their development on [Ko-fi](https://ko-fi.com/postdev360).
