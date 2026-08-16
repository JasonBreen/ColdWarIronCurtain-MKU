# CLAUDE.md

## Read AGENTS.md first

**[AGENTS.md](AGENTS.md) is the canonical guide for this repository** — layout,
hard rules, naming conventions, tooling, and git workflow all live there. Read
it before making changes. It is kept as the single source of truth so that
Claude Code, Codex, and Copilot all follow the same rules; this file adds only
the parts specific to working through Claude Code.

## The 60-second version

This is **Cold War: Iron Curtain**, a total-overhaul Hearts of Iron IV mod
written in Paradox script. No build, no package manager, no unit tests, no app
to run. ~9,400 script files, ~2,090 localisation files, ~60,000 binary assets.

Five rules that cause the most damage when missed:

1. `CWIC Backup/` is an archive — never modify it.
2. Never touch the `path=` line in `Cold War Iron Curtain/descriptor.mod`.
3. New PDX script lines indent with **tabs**. ~42% of existing files use spaces
   — that is known debt; **do not mass-reformat it**.
4. Localisation `.yml` files are **UTF-8 with BOM**. Dropping the BOM makes the
   game silently skip the file.
5. Player-visible text needs a `localisation/english/` key, or it renders in
   game as the raw key string.

## Before you finish a change

```bash
python3 tools/check_style.py --diff origin/development-branch
python3 tools/loc_audit.py --check
```

Both are dependency-free and are exactly what CI runs.

## Searching this repo efficiently

The binary assets (~60,000 `.dds`/`.png`/`.tga`/`.wav` files) will drown any
naive search and waste a large amount of context.

- Always scope Grep with `--include`/`glob`, e.g. `glob: "**/*.txt"`.
- Prefer targeting a specific subtree (`Cold War Iron Curtain/events/`) over the
  repo root.
- Exclude `CWIC Backup/` from searches unless you are specifically archaeology-
  hunting; it duplicates much of the mod and will produce confusing double hits.
- When looking for an event definition rather than an event *call*, search for
  the localisation key (`ADR.1.t`) rather than the ID (`ADR.1`).

## Verification honesty

There is **no automated way to test gameplay** in this repo. CI checks syntax
and conventions only — it cannot tell you whether a focus is reachable or an
event fires.

When reporting on a change, say what you changed and state explicitly that it
needs in-game verification, including the country and start date to load. Do not
describe a gameplay change as "working," "verified," or "tested." That claim
requires a human loading HOI4.

## Scope discipline

Files here are large and old, and a great deal of the content is
hand-maintained by many contributors over years. Change only what the task
requires. In particular, resist the urge to normalise whitespace, reorder
`replace_path` entries, or tidy neighbouring script — those produce enormous,
unreviewable diffs and destroy `git blame`.
