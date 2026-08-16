# AGENTS.md — Cold War: Iron Curtain (CWIC)

Instructions for AI coding agents (Codex, Claude Code, Copilot, and others)
working in this repository. Humans are welcome to read it too — it is the
canonical description of how this repo works.

---

## What this repository is

A large total-overhaul mod for **Hearts of Iron IV** (Paradox Interactive),
covering the Cold War from 1949 onward. Target game version: **1.19**.

It is **not** a software project. There is no build, no package manager, no
unit test suite, and no application to run. The deliverable is a folder of
**Paradox script** (PDX script) — a brace-based declarative configuration
language that the game engine loads at startup.

Scale, so you know what you are searching:

| | Count |
|---|---|
| PDX script files (`.txt`/`.gui`/`.gfx`/`.asset`) | ~9,400 |
| Event files | ~460 |
| Focus tree files | ~490 |
| Country history files | ~470 |
| Localisation `.yml` files | ~2,090 |
| Binary art/audio assets | ~60,000 |

Because of that last row, **never run a repo-wide `grep` without
`--include`**, and never read binary assets looking for text.

---

## Layout

```
ColdWarIronCurtain-MKU/
├── Cold War Iron Curtain/     ← the mod itself; nearly all work happens here
│   ├── common/                ← game rules (75 subfolders)
│   │   ├── national_focus/    ← focus trees
│   │   ├── decisions/         ├ ideas/         ├ characters/
│   │   ├── technologies/      ├ on_actions/    ├ scripted_effects/
│   │   ├── scripted_triggers/ └ scripted_localisation/
│   ├── events/                ← one file per country or topic
│   ├── history/
│   │   ├── countries/         ← starting state, `<TAG> - <Name>.txt`
│   │   ├── states/            ← `<id>-<StateName>.txt`
│   │   └── units/             ← starting orders of battle
│   ├── localisation/
│   │   ├── english/           ← required; UTF-8 **with BOM**
│   │   └── french/ japanese/ russian/
│   ├── gfx/ interface/        ← sprites, portraits, GUI layout
│   ├── map/ music/ sound/
│   ├── scenario_tests/        ← in-engine scenario definitions (see Testing)
│   └── descriptor.mod         ← mod metadata + replace_path list
├── tools/                     ← Python helper scripts (see Tooling)
├── docs/SETUP.md              ← human contributor setup
├── .github/                   ← CI, templates, Copilot config
└── CWIC Backup/               ← ARCHIVE — do not modify
```

Other top-level folders (`CWIC +Translate/`, `Reworked MLA/`,
`For yuri from Taiga/`, `ino/`, `LogDocs/`) are working scratch areas and
archives. Leave them alone unless a task names them.

---

## Hard rules

1. **Do not modify `CWIC Backup/`.** It is a historical archive.

2. **Do not touch the `path=` line in `descriptor.mod`.** It holds a
   developer-local absolute path and is intentionally machine-specific. You may
   *add* a `replace_path` entry when the mod takes full ownership of a new
   vanilla folder; never reorder or delete existing ones.

3. **Tabs, not spaces**, for indentation in PDX script. See the note on legacy
   files below before you reformat anything.

4. **Localisation is mandatory for player-visible text.** Every new event
   title/description/option, focus name, decision name, idea name, or character
   name needs a matching key in `localisation/english/`. Missing keys render
   in-game as the raw key string.

5. **Localisation files are UTF-8 with BOM.** Without the BOM the game silently
   fails to load the file. Do not "clean up" the BOM.

6. **No hardcoded absolute paths** anywhere in script. CI enforces this.

7. **Keep changes scoped.** Do not reformat, re-indent, or "tidy" files you were
   not asked to change. See below for why this matters more than usual here.

### The legacy-formatting trap

About **42% of PDX script files in this repo use space indentation**, in
violation of rule 3 — and some files mix tabs and spaces within a single block.
This is pre-existing debt, not a bug to fix.

Do **not** mass-reformat. A whitespace-only sweep would touch thousands of
files, destroy `git blame` for the mod's entire history, and produce a diff no
human can review. CI is deliberately built to tolerate this: it checks only the
lines **you add**, so write new lines with tabs and leave surrounding lines
exactly as they are.

---

## Tooling

Both scripts are plain Python 3 with no dependencies. Run them from the repo
root. CI runs both, so running them locally first is the fastest way to know
your change is clean.

```bash
# Style: tabs + localisation BOM, checked on the lines you ADDED
python3 tools/check_style.py --diff origin/development-branch

# Whole-tree debt report (never fails; informational)
python3 tools/check_style.py --all

# Localisation audit for the Southeast Asia theatres
python3 tools/loc_audit.py --check      # lint, exit 1 on failure
python3 tools/loc_audit.py --summary    # counts only, writes nothing
python3 tools/loc_audit.py             # regenerate the audit CSVs
```

`loc_audit.py` resolves every event title/desc/option key in the SEA theatres
against `localisation/english/`. Its plain invocation rewrites CSVs in the repo
— use `--check` or `--summary` unless you specifically intend to regenerate.

---

## Testing

**There is no automated way to verify gameplay.** PDX script has no test
runner; correctness is established by loading the mod in HOI4. This is the
single most important thing to understand about working here.

Consequences for an agent:

- CI passing means *syntax and conventions* are fine. It says nothing about
  whether your focus tree is reachable, your event fires, or your effect works.
- **Always state plainly in your PR description what still needs in-game
  testing**, and which country/date/start to load to see it. A human has to do
  that step.
- Never claim a gameplay change "works" or is "verified." Say what you changed
  and what you could not check.

`Cold War Iron Curtain/scenario_tests/` holds in-engine scenario definitions
that the game itself can run. They are not part of CI.

---

## Conventions

### Naming

| Thing | Pattern | Example |
|---|---|---|
| Event ID | `<NAMESPACE>.<n>` | `ADR.1` |
| Namespace | declared at top of file | `add_namespace = ADR` |
| Focus ID | `<TAG>_<DescriptiveName>` | `USA_Marshall_Plan` |
| Decision ID | `<tag>_<snake_case>` | `usa_marshall_plan` |
| Idea / spirit | `<tag>_<snake_case>` | `sov_five_year_plan` |
| Country history | `<TAG> - <Country Name>.txt` | `SOV - Soviet union.txt` |
| State history | `<id>-<StateName>.txt` | `845-Jawa Timur.txt` |

Event and focus **file** names are inconsistent across the repo (`ADR.txt`,
`ARG50s_Events.txt`, `1950s_Afghanistan.txt`, `1950s_BUL.txt` all coexist).
**Match the neighbouring files in the folder you are editing** rather than
following a single global rule.

### Localisation keys

```
<NS>.<id>.t     event title
<NS>.<id>.d     event description
<NS>.<id>.a     event option (a, b, c, …)
<FOCUS_ID>      focus name
<FOCUS_ID>_desc focus tooltip
<decision_id>          decision name
<decision_id>_desc     decision tooltip
```

### Skeletons

```pdx
add_namespace = EXAMPLE

country_event = {
	id = EXAMPLE.1
	title = EXAMPLE.1.t
	desc = EXAMPLE.1.d
	picture = GFX_some_picture

	is_triggered_only = yes

	option = {
		name = EXAMPLE.1.a
	}
}
```

```pdx
focus = {
	id = TAG_Focus_Name
	icon = GFX_some_icon
	cost = 10
	x = 0
	y = 0
	completion_reward = {
	}
}
```

Note: `country_event = { ... }` also appears as an *effect* that fires an event.
A definition carries `title`/`desc`/`option`; a bare `country_event = { id = X
days = 2 }` is a call. Do not confuse the two when searching.

---

## Git workflow

- Default branch: **`development-branch`**.
- Branch from it, commit with descriptive messages, open a PR against it.
- Fill in `.github/PULL_REQUEST_TEMPLATE.md` — CI rejects PR bodies under 20
  characters, and the template's in-game-testing checklist is the mechanism by
  which a human knows what to verify.
- Never commit `.psd` sources, HOI4 log dumps, or `__pycache__/`.

---

## When you are unsure

PDX script fails **silently**. A misspelled effect, a missing localisation key,
or a malformed trigger usually produces no error — the content simply never
appears in game. There is no compiler to catch you.

So: prefer copying the shape of an existing, working example in the same folder
over inventing syntax from memory. If no local precedent exists for what you are
about to write, say so rather than guessing.
