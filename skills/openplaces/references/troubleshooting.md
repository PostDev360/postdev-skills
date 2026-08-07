# openplaces — when a call fails

Read this when `openplaces` exits non-zero or returns something unexpected.

## Exit codes

| Code | Family | Retry? | Action |
|---|---|---|---|
| 0 | success | — | — |
| 2 | usage error | no | the command line is malformed; re-read `references/commands.md` |
| 3 | invalid input | no | a value is out of range — fix it |
| 4 | not found | no | the query was valid but matched nothing |
| 5 | network unreachable | yes, once | the host could not be reached at all |
| 6 | upstream error | yes, once, after a pause | the service answered with an error |
| 7 | missing configuration | no | `OPENROUTESERVICE_API_KEY` is unset |

The error text goes to stderr and always starts with `openplaces:`. Read it —
it names the failing host and the reason.

## Exit 6 on `search`: Overpass was busy

By far the most common failure. Public Overpass instances answer `504` whenever
their dispatcher is saturated, and this is frequent at peak hours — during
development, a first attempt failed and the identical query succeeded seconds
later.

The tool already retries with exponential backoff before reporting exit 6. So:

- **Retry once**, after a few seconds.
- If it fails again, tell the user the service is busy and suggest trying
  later. Do not loop.
- Never work around it by increasing `--limit` or widening `--radius-m`; a
  heavier query is more likely to be refused, not less.

## Exit 7: no OpenRouteService key

Only `route` and `isochrone` need it. Everything else keeps working.

Tell the user a free key is available at
`https://openrouteservice.org/dev/#/signup`, and that it goes in the
environment as `OPENROUTESERVICE_API_KEY`. Never write a key into a file in the
repository, into a `SKILL.md`, or into the conversation as a value to be
committed.

## The result is in the wrong town

A known Base Adresse Nationale behaviour, not a bug in the tool. The BAN weights
town names weakly in free-text search: `"8 boulevard du Port Marseille"` returns
`8 Boulevard du Port 95000 Cergy` at score 0.588, because a street of that name
exists in Cergy and "Marseille" barely moves the ranking.

Fix it by constraining rather than rephrasing:

```bash
openplaces --json resolve "8 boulevard du Port" --postcode 13002
```

Check `score` on the result. Above 0.9 is a solid match. Around 0.5 or below,
treat the answer as a suggestion and ask the user to confirm.

## `resolve` returned a French street for a foreign address

Also expected, and already mitigated. The BAN returns *something* for almost
any input rather than an empty list — `"Alexanderplatz Berlin"` comes back as
`Allée de Berlin, Les Pavillons-sous-Bois` at score 0.38. The tool consults
Photon whenever the BAN's best score falls below 0.5 and puts the Photon rows
first, so the correct answer normally leads.

If a foreign address still comes back French, force it:

```bash
openplaces --json resolve "Alexanderplatz Berlin" --country intl
```

## `search` found nothing

In order of likelihood:

1. **The radius is too small.** Default is 2000 m. Rural areas need more.
2. **The category was not recognised** and it fell back to a name search. Run
   `openplaces categories` to check, and use a recognised term.
3. **`--open-now` dropped everything.** It keeps only places whose hours parse
   *and* say open. Re-run without it to see whether the places exist at all.
4. **A `--tag` filter is too narrow.** `wheelchair=yes` is tagged on a minority
   of objects; absence of the tag is not absence of the feature.
5. **The data genuinely is not there.** OpenStreetMap coverage is contributed
   and uneven. Say so rather than trying ten variations.

## `open_now` is `null` everywhere

Normal. `opening_hours` is one of the most frequently missing tags in
OpenStreetMap, and the evaluator deliberately returns `null` rather than
guessing for syntax it does not fully support — public holidays, school
holidays, seasonal rules.

Report it as "opening hours unknown". Do not infer hours from the type of
business.

## Results look stale

Responses are cached for seven days by default. If a user reports that a place
has changed:

```bash
openplaces cache clear
```

Then re-run. Only do this when there is a concrete reason — clearing the cache
sends every subsequent call back over the network, which is exactly what the
cache exists to prevent.

## The tool is not installed

```bash
uv tool install git+https://github.com/PostDev360/openplaces
# or: pipx install git+https://github.com/PostDev360/openplaces
```

Install from git: the package is not on PyPI yet, and the name `openplaces`
there belongs to an unrelated project.

The distribution name is `openplaces-cli`; the command is `openplaces`. Needs
Python 3.10 or newer — `uv` will fetch one, `pipx` will not. If neither `uv`
nor `pipx` is available, say so and stop. Do not answer the location question
from memory.

If the install succeeded but `openplaces` is still not found, the problem is
the PATH: both installers place the command in `~/.local/bin`, which is not
always on the PATH of a service or daemon.
