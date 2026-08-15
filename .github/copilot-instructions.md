# Copilot Instructions – Cold War Iron Curtain (CWIC)

## Project overview
This repository is **Cold War Iron Curtain (CWIC)**, a large overhaul mod for **Hearts of Iron IV** (Paradox Interactive).
The mod covers the Cold War era (roughly 1950–1991) and replaces the vanilla HOI4 start-date and focus trees with historically-grounded Cold War content.
It is authored in **Paradox Script** (PDX script), a brace-based configuration language specific to Paradox games.

Target HOI4 version: **1.19**

## Repository layout

```
ColdWarIronCurtain-MKU/
├── Cold War Iron Curtain/          ← The mod folder (main working area)
│   ├── common/                     ← Game mechanics definitions
│   │   ├── national_focus/         ← Focus trees (one file per country/era)
│   │   ├── decisions/              ← Decision categories and individual decisions
│   │   ├── ideas/                  ← National spirits, laws, ministers
│   │   ├── characters/             ← Country leaders and generals
│   │   ├── technologies/           ← Tech tree files
│   │   ├── scripted_effects/       ← Reusable effect macros
│   │   ├── scripted_triggers/      ← Reusable trigger macros
│   │   ├── scripted_localisation/  ← Dynamic localisation expressions
│   │   └── on_actions/             ← Event hooks
│   ├── events/                     ← Country and news events (one file per country/topic)
│   ├── history/
│   │   ├── countries/              ← Starting state files (.txt per country tag)
│   │   ├── states/                 ← State definition files
│   │   └── units/                  ← Starting OOB files
│   ├── localisation/
│   │   ├── english/                ← Primary localisation (.yml, UTF-8 BOM)
│   │   ├── french/
│   │   └── …                       ← Other languages mirror the english/ structure
│   ├── gfx/                        ← Graphics (sprites, portraits, flags, loading screens)
│   ├── interface/                  ← GUI layout files (.gui, .gfx)
│   └── descriptor.mod              ← Mod metadata and replace_path declarations
├── .github/                        ← GitHub Actions, templates, Copilot config (this file)
├── .vscode/                        ← VS Code workspace settings
├── docs/                           ← Developer documentation
└── tools/                          ← Helper scripts
```

## Coding conventions

### General PDX script style
- **Indentation**: hard tabs (`\t`), not spaces.
- **Braces**: opening brace on the same line as the block name; closing brace on its own line.
- **Event IDs**: `<NAMESPACE>.<number>` — namespace defined at top of file with `add_namespace = <NS>`.
- **Focus IDs**: `<COUNTRY_TAG>_<DescriptiveName>` (e.g. `AFG_The_Royal_Afghanistan_Armed_Forces`).
- **Decision IDs**: snake_case, prefixed with country tag (e.g. `usa_marshall_plan`).
- **Idea/spirit keys**: snake_case, prefixed with country tag.

### Localisation
- Files live in `localisation/<language>/` and **must be saved as UTF-8 with BOM**.
- Every user-visible key added in script **must** have a corresponding entry in at least `localisation/english/`.
- Key naming:
  - Event title: `<NS>.<id>.t`
  - Event description: `<NS>.<id>.d`
  - Event option: `<NS>.<id>.<letter>` (a, b, c, …)
  - Focus name: `<FOCUS_ID>` — tooltip: `<FOCUS_ID>_desc`
  - Decision name: `<decision_id>` — tooltip: `<decision_id>_desc`

### descriptor.mod
- **Never edit the `path=` line** — it contains a developer-local absolute path.
- When a new folder is fully replaced by the mod, add a `replace_path = "…"` entry.

### File naming
- Events: `<CountryOrTopic>_Events.txt` or `<CountryOrTopic>.txt` (match existing casing in the folder).
- Focus trees: `<decade>s_<COUNTRY_TAG>.txt` (e.g. `1950s_AFG.txt`).
- History: `<TAG> - <Country Name>.txt` for countries; numeric state ID `<NNN>-<StateName>.txt` for states.

## Common patterns

### Minimal event skeleton
```pdx
add_namespace = EXAMPLE

country_event = {
	id = EXAMPLE.1
	immediate = { }
	title = EXAMPLE.1.t
	desc = EXAMPLE.1.d
	picture = GFX_some_picture

	is_triggered_only = yes

	option = {
		name = EXAMPLE.1.a
	}
}
```

### Minimal focus skeleton
```pdx
focus = {
	id = TAG_Focus_Name
	icon = GFX_some_icon
	cost = 10
	x = 0
	y = 0
	search_filters = { IC_FILTER }
	completion_reward = {
		# effects here
	}
}
```

### Minimal decision skeleton
```pdx
tag_decision_category = {
	tag_some_decision = {
		icon = generic_political_actions
		cost = political_power
		days_remove = 70
		ai_will_do = { factor = 1 }
		modifier = { }
		complete_effect = { }
		remove_effect = { }
	}
}
```

## What NOT to do
- Do not hard-code absolute paths anywhere in script files.
- Do not remove or rename existing `replace_path` entries in `descriptor.mod`.
- Do not use spaces for indentation in PDX script files.
- Do not add localisation keys without a matching script reference (and vice versa).
- Do not modify files in `CWIC Backup/` — that folder is an archive.
