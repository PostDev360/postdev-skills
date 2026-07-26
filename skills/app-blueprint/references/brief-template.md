# Project Brief template

Fill this in from the interview answers and save it as `PROJECT_BRIEF.md` at the root of the project directory. Write it in the user's language.

## Formatting rules

- One line per bullet. If a bullet needs two lines, it is two bullets.
- Use the user's own words wherever possible. Do not upgrade their vocabulary into jargon.
- No invented content. Anything the user did not say goes under **Open questions**, never into a section as a guess.
- Do not add sections for topics the interview did not cover (no tech-stack, timeline, or cost sections unless the user gave those answers).
- Keep the whole brief under roughly one screen. It is a decision record, not a specification.

## Sections, in this order

```markdown
# Project Brief — <project name>

_Last updated: <YYYY-MM-DD> — confirmed by <user> / awaiting confirmation_

## Problem & audience
- The problem this solves, in one line.
- Who it is for.
- Comparable existing tool, if the user named one.

## Users & access
- Accounts or no accounts.
- The kinds of users, and what each is allowed to do.

## Data
- What the app remembers between visits.
- Anything sensitive, flagged explicitly.

## Platforms
- Web / phone / desktop, and which comes first.
- Offline requirement, yes or no.

## Must-have scope (v1)
- The 2–3 things it cannot ship without.

## Later (v2+)
- Explicitly deferred features, so they stay out of v1.

## Constraints
- Budget, hosting, deadline.
- Expected number of users and how often.

## Integrations & look
- External services it must connect to.
- Existing visual identity, or open.

## Open questions
- Anything still unresolved. Empty means ready to build.
```

## After writing it

Show the brief to the user and ask them to confirm or correct it. Only once **Open questions** is empty and the user has confirmed does architecture or code work begin.

When the brief changes later, update the `_Last updated_` line in the same edit.
