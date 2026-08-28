# Repository Guidelines

## Project Structure & Module Organization

`Cold War Iron Curtain/` is the shipped Hearts of Iron IV mod. Make gameplay changes there: `common/` contains mechanics (focuses, decisions, ideas, AI, and scripted content), `events/` contains event chains, `history/` contains country/state/OOB setup, and `localisation/english/` is the required source for player-facing text. Visual assets live in `GFX/`, `portraits/`, `interface/`, `sound/`, and `music/`. Keep helper scripts in `tools/` and setup notes in `docs/`. Treat `CWIC Backup/` as read-only archive material.

## Development & Validation

Open `ColdWarIronCurtain-MKU.code-workspace` in VS Code and install the recommended CWTools and HOI4 extensions described in `docs/SETUP.md`.

Run the targeted localisation audit when changing Southeast Asia event/localisation content:

```powershell
py -3 tools/loc_audit.py --check
py -3 tools/loc_audit.py --summary
```

The first command reports missing or malformed audited localisation; the second reports coverage without writing CSVs. CI also checks every localisation `.yml` for UTF-8 BOM and PDX `.txt`, `.gui`, and `.gfx` files for space indentation. CWTools CLI validation is not yet configured, so load a new game or relevant save in HOI4 for gameplay, UI, and event-flow changes.

## Coding Style & Naming

Use hard tabs for indentation in PDX script files; place opening braces on the declaration line and closing braces on their own lines. Declare event namespaces and use IDs such as `USA.1`. Name focuses `<TAG>_<DescriptiveName>` (for example, `AFG_The_Royal_Afghanistan_Armed_Forces`) and country-scoped decisions/ideas `<tag>_<snake_case_name>`.

Save localisation as UTF-8 with BOM. Add English keys for every visible script key: event `.t`, `.d`, and option suffixes, plus focus or decision `_desc` keys. Match the casing and filename pattern already used in the target directory. Never hard-code absolute paths or change `descriptor.mod`'s developer-local `path=` line.

## Testing Guidelines

Keep changes narrow and test the affected country tag, start date, triggers, effects, localisation, and GUI/assets in-game. Record manual test steps and outcomes in the PR; include screenshots or a short clip when UI, portraits, or graphics change.

## Commits & Pull Requests

Use concise, imperative commit subjects that name the affected content, such as `Add ENG MIO` or `Rework French Indochina command isolation`. Avoid unrelated formatting or archive changes. Fill out every section of `.github/PULL_REQUEST_TEMPLATE.md`: explain why, check affected areas, list country tags, confirm localisation and tab rules, and state in-game testing. Link the relevant issue when one exists.
