# Project Context: Cold War Iron Curtain (CWIC)

## Overview
Cold War Iron Curtain (CWIC) is a mod for the game **Hearts of Iron IV (HOI4)**. It focuses on the geopolitical landscape of the Cold War era.

## Codebase Structure
The project follows the standard Paradox Interactive modding structure, organized within the `Cold War Iron Curtain/` directory:

- `common/characters/`: Contains `.txt` files defining country leaders, corps commanders, and field marshals. Includes various leader types (e.g., `_Naval_Leaders`, `_Generals`, `_RYU`).
- `common/buildings/`: Contains definitions for societal and landmark buildings.
- `common/autonomous_states/`: Defines types of subordinate states (e.g., `puppet`, `satellite`, `protectorate`, `reichskommissariat`, `republic`, `un_trust_territory`).
- `common/ai_templates/`: Provides template files for AI behavior for various major nations (e.g., `templates_USA`, `templates_SOV`).
- `common/ai_strategy_plans/`: Contains scenario-specific AI strategy plans (e.g., `CHI_historical_strategy_plan.txt`).
- `common/ai_strategy/`: Contains high-level AI strategy and doctrine files.
- `common/ai_focuses/`: Defines AI focus trees for different nations.
- `common/ai_navy/`: Contains AI navy configurations, including taskforce and fleet templates, and goals.
- `common/abilities/`: Defines leader and strategic region abilities.
- `common/bookmarks/`: Contains historical/scenario bookmarks (e.g., `1980.txt`).

## Coding Standards & Tools
- **Language**: Paradox Scripting (PDX script).
- **Validation**: The project is designed to be validated using **CWTools**.
- **Localization**: Localisation files are typically stored in `.yml` files (referenced in `docs/SETUP.md`).
- **Data Format**: Many configuration files use a brace-based syntax (`{ ... }`) characteristic of Paradox scripting.

## Development Workflow
- Use the `.code-workspace` file to ensure all necessary VS Code extensions (CWTools, HOI4 Mod Utilities) are active.
- Always check `.github/workflows/` for CI/CD processes, including validation and release automation.
```