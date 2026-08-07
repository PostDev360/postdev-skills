# openplaces — command and output reference

Read this when composing a call whose flags are not in `SKILL.md`, or when
parsing an output field you have not seen before.

## Global flags

Placed **before** the subcommand.

| Flag | Effect |
|---|---|
| `--json` | flat JSON records — use this whenever you parse the result |
| `--geojson` | GeoJSON `FeatureCollection`; for mapping tools, not for parsing |
| `--version` | print the version |

`--json` and `--geojson` are mutually exclusive. `--geojson` is not available
for `route`, which has no geometry to emit.

## `search` — places of a kind around a point

```
openplaces search <query> [--near <place> | --lat <f> --lng <f>]
                          [--radius-m <int>] [--limit <int>] [--open-now]
                          [--tag KEY=VALUE ...] [--country auto|fr|intl]
```

- `<query>` is a category term (see `openplaces categories`) or a name. An
  unrecognised term becomes a case-insensitive name search.
- `--radius-m` defaults to 2000, maximum 50000.
- `--limit` defaults to 10, maximum 100.
- `--tag` is repeatable and ANDs with the category, e.g.
  `--tag wheelchair=yes --tag outdoor_seating=yes`.
- One of `--near` or the `--lat`/`--lng` pair is required. `--lat` without
  `--lng` is an error, not a partial hint.

Result records:

```json
{
  "id": "node/1250893403",
  "name": "La Panetteria",
  "lat": 43.2949, "lng": 5.3718,
  "address": "12 rue de la République 13002 Marseille",
  "phone": "+33 4 91 00 00 00",
  "website": "https://…",
  "opening_hours": "Mo-Fr 06:30-19:30; Sa 08:00-19:30",
  "open_now": true,
  "wheelchair": "yes",
  "distance_m": 175,
  "osm_url": "https://www.openstreetmap.org/node/1250893403"
}
```

Sorted nearest first. `open_now` is `true`, `false` or `null`. Every string
field may be `""`.

## `resolve` — address to coordinates

```
openplaces resolve <query> [--limit <int>] [--country auto|fr|intl]
                           [--postcode <str>] [--citycode <str>]
```

- `--postcode` and `--citycode` (INSEE code) are BAN-only filters, and are the
  reliable way to pin a town when free text is ambiguous.
- `--country fr` uses the BAN alone; `--country intl` uses Photon alone. Both
  are binding — an empty result stays empty.

Result records:

```json
{
  "name": "8 Quai du port 13002 Marseille",
  "lat": 43.296415, "lng": 5.373379,
  "type": "housenumber",
  "postcode": "13002", "city": "Marseille",
  "context": "13, Bouches-du-Rhône, Provence-Alpes-Côte d'Azur",
  "score": 0.971,
  "source": "BAN"
}
```

`score` is 0–1 for BAN rows and `null` for Photon rows, which carry no
relevance score. A `null` score is not a low score.

## `reverse` — coordinates to address

```
openplaces reverse --lat <f> --lng <f> [--country auto|fr|intl]
```

Same record shape as `resolve`, plus `distance_m` — how far the returned
address is from the point asked about. Results are nearest first; the first row
is the answer, the rest are context.

## `details` — one specific OSM object

```
openplaces details <type>/<id>
```

`<type>` is `node`, `way` or `relation`; the id comes from a `search` result's
`id` field. Returns the search record shape plus a full `tags` object holding
every OpenStreetMap tag on the object — useful for cuisine, operator, opening
hours variants, accessibility details.

## `route` — distance and duration

```
openplaces route --from <place> --to <place> [--profile <profile>]
```

Requires `OPENROUTESERVICE_API_KEY`. Both endpoints are geocoded first, so they
can be free text.

```json
{"profile": "driving-car", "distance_km": 12.4, "duration_min": 38,
 "from": "Marseille", "to": "Aix-en-Provence"}
```

This is **not** turn-by-turn navigation. There is no manoeuvre list.

Profiles: `driving-car`, `driving-hgv`, `cycling-regular`, `cycling-electric`,
`cycling-mountain`, `cycling-road`, `foot-walking`, `foot-hiking`, `wheelchair`.

## `isochrone` — reachable area

```
openplaces isochrone [--near <place> | --lat <f> --lng <f>]
                     [--minutes <int>] [--profile <profile>]
```

Requires the same key. `--minutes` defaults to 15, maximum 60.

Returns a GeoJSON `FeatureCollection` whose polygon is the reachable area, plus
a `summary` object:

```json
{"profile": "driving-car", "minutes": 20,
 "area_km2": 312.5, "reachable_population": 480000}
```

For an agent this is usually the more useful question than a point-to-point
route: "what is within twenty minutes of here" is what actually drives a
decision about where to put something or where to meet.

## `categories` — the recognised terms

```
openplaces categories [--json]
```

Prints every canonical category and the OSM tags it maps to.

## `cache`

```
openplaces cache info
openplaces cache clear
```

`info` reports the path, size, entry count and how many entries are still
fresh. Only clear the cache if the user asks, or if stale data is provably the
problem — clearing it means every subsequent call goes back over the network.
