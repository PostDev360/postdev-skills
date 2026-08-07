---
name: openplaces
description: Use this skill for any question about real-world places, addresses or travel — "where is the nearest pharmacy", "geocode this address", "what are the coordinates of X", "what's the address at these coordinates", "how far / how long from A to B", "what can I reach in 20 minutes", "find bakeries open now near Y", "list charging stations around Z". It drives the `openplaces` CLI, which answers from OpenStreetMap, the Base Adresse Nationale and OpenRouteService — free, no paid API key, and no address data leaving the EU, which matters when the addresses belong to clients or patients. Also use it when a user explicitly asks for a Google Maps or Google Places alternative. Skip it for driving directions turn by turn (it returns distance and duration, not a manoeuvre list), and skip it for ratings or reviews, which OpenStreetMap does not hold.
allowed-tools: Bash
license: MIT
---

# openplaces

## What this is

A command-line tool that answers place, address and travel questions from open
data. It replaces Google Places for the queries below, at zero cost and without
sending addresses outside the EU.

Read `references/commands.md` for the full flag and output reference. Read
`references/troubleshooting.md` when a command fails.

## Before the first call

Check the tool is installed:

```bash
openplaces --version
```

If that fails, install it and say so — do not silently fall back to guessing
coordinates from memory:

```bash
uv tool install git+https://github.com/PostDev360/openplaces
# or: pipx install git+https://github.com/PostDev360/openplaces
```

Needs Python 3.10 or newer; `uv` fetches one itself if none is suitable. The
distribution is `openplaces-cli` and the installed command is `openplaces` —
`uv tool list` shows the former, `which openplaces` the latter.

Install from git, not from PyPI: the package is not published there yet, so
`uv tool install openplaces-cli` resolves to an unrelated project.

## Core rule: never invent a location

If `openplaces` is unavailable or returns nothing, **say so**. Do not supply
coordinates, addresses, distances or opening hours from memory. A plausible
wrong address is worse than no answer here, because the user cannot tell the
difference — that is the whole reason to shell out to real data.

The one exception is well-known city-level coordinates used as a `--near`
argument, which the tool will itself resolve properly.

## Choosing a command

| The user wants | Command |
|---|---|
| places of a kind, near somewhere | `search` |
| an address turned into coordinates | `resolve` |
| coordinates turned into an address | `reverse` |
| everything known about one specific place | `details` |
| distance and duration between two places | `route` |
| the area reachable within N minutes | `isochrone` |

Always pass `--json` when you need to read the result yourself. The default
output is shaped for a human reading a terminal; `--json` is stable and
documented. Use `--geojson` only when the user wants a file for a mapping tool.

## Typical calls

```bash
openplaces --json search "pharmacy" --near "Marseille 2e" --radius-m 1500 --limit 5
openplaces --json search "bakery" --near "Lyon" --open-now
openplaces --json search "pharmacy" --near "Lyon" --tag wheelchair=yes
openplaces --json resolve "8 quai du Port, Marseille"
openplaces --json reverse --lat 43.2965 --lng 5.3698
openplaces --json details node/1941628376
openplaces --json route --from "Marseille" --to "Aix-en-Provence" --profile foot-walking
openplaces --json isochrone --near "Aix-en-Provence" --minutes 20
```

## Reading the results

### `open_now` has three values, not two

`true`, `false`, and **`null`** — meaning the opening-hours syntax was not
recognised, so nothing is claimed. Report `null` as "opening hours unknown".
Never round it to "closed" or to "open".

`--open-now` filters to `true` only, so it silently drops places whose hours are
unparseable. When a user asks "what's open near me", mention that the list may
be shorter than reality for that reason.

### Empty fields are normal

`phone`, `website`, `opening_hours` and `address` are frequently `""` in
OpenStreetMap. That is missing data, not an error, and not a reason to retry.
Report what is there and stay quiet about the rest.

### There are no ratings or reviews

OpenStreetMap does not hold them. If the user asks for "the best-rated
restaurant nearby", say plainly that this source has no ratings, give the list
by distance, and let them decide. Do not substitute your own impressions of
named businesses as if they were data.

### Attribution

If results are reproduced anywhere public — a document, a page, a post — they
must carry "© OpenStreetMap contributors" (ODbL). Mention this when the user is
clearly producing something public.

## Handling failures

Exit codes are distinct per failure family. Act on them rather than retrying
blindly:

| Code | Meaning | What to do |
|---|---|---|
| 3 | invalid input | fix the argument; do not retry as-is |
| 4 | not found | tell the user; try a broader query |
| 5 | network unreachable | report it; the tool already retried |
| 6 | upstream error | wait a few seconds, retry **once** |
| 7 | missing `OPENROUTESERVICE_API_KEY` | only affects `route`/`isochrone` — tell the user a free key is needed |

Exit 6 usually means a public Overpass instance was busy. One retry is
reasonable; a loop of retries is not, and will get the user's IP banned.

## Getting geocoding right

`resolve` answers from the Base Adresse Nationale for France and Photon
elsewhere, choosing automatically. Two things to know:

- The BAN weights town names weakly in free text. `"8 boulevard du Port
  Marseille"` returns the Cergy street of that name. When a user names a town
  and the result contradicts it, retry with `--postcode` or `--citycode`.
- Always check the `score` field on BAN results. Above 0.9 is a solid match;
  around 0.5 means the tool was unsure enough to also consult Photon. If the
  best score is low and the user's intent was specific, ask them to disambiguate
  rather than picking the first row.

Use `--country fr` or `--country intl` when the user has been explicit about
where they mean. Both are binding — no silent fallback to the other provider.

## Being a good citizen

The tool caches responses and spaces its calls, but that only helps if you do
not defeat it:

- One call per question. Do not sweep a city by issuing dozens of `search`
  calls at different coordinates.
- Prefer a larger `--radius-m` over many small searches.
- `--limit` costs nothing extra up to 100; ask for what you need in one call.
- Never put `openplaces` in a shell loop over a list of addresses without
  telling the user how many calls that will make.

## Categories

`search` maps common French and English terms to OpenStreetMap tags. An
unrecognised term falls back to a name search, which is how brands like
"Monoprix" are found. To see the recognised terms:

```bash
openplaces categories
```

If a user's term is missing and would be generally useful, it belongs in the
tool's `categories.json`, not in a workaround here — mention that they can
contribute it.
