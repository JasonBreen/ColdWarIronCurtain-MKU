# CONTINUE.md - Project Guide for Cold War Iron Curtain (CWIC)

## 1. Project Overview
**Cold War Iron Curtain (CWIC)** is a comprehensive mod for **Hearts of Iron IV (HOI4)** focused on the geopolitical landscape of the Cold War era. It simulates the tension between superpowers and the struggle for independence of various nations across several decades.

- **Key Technologies**: Paradox Scripting (PDX script), GitHub Actions (CI/CD), CWTools (validation).
- **High-level Architecture**: Data-driven modding structure with a heavy emphasis on complex mechanics (DEFCON, MAD, UN, Economic Systems, and Tech Trees).

## 2. Getting Started
### Prerequisites
- **VS Code** is the recommended IDE.
- **Required Extensions**:
  - `tboby.cwtools-vscode` (CWTools): For syntax highlighting and validation.
  - `nacl.hoi4-mod-utilities`: For focus tree previews and localization help.
  - `redhat.vscode-yaml`: For YAML support.
  - `eamodio.gitlens`: For Git history.
  - `gruntfuggly.todo-tree`: For tracking TODOs.

### Installation & Setup
1. Open the workspace file: `ColdWarIronCurtain-MKU.code-workspace`.
2. Install the recommended extensions listed above.
3. **Critical Step**: Update your local configuration in `.vscode/settings.json` to point `hoi4ModUtilities.modFile` to your local HOI4 mod installation path.

### Running Tests
- Verify logic and syntax using **CWTools**.
- Check game logs in the HOI4 error log after running the mod to catch runtime issues.

## 3. Project Structure
- `common/`: The core data directory.
  - `characters/`: Leader and commander definitions.
  - `ideas/`: Mechanic definitions (e.g., `Defcon.txt`).
  - `ai_templates/` & `ai_strategy_plans/`: AI behavior and scenario-specific strategies.
  - `abilities/`: Leader and region abilities.
- `events/`: Definitions for game events.
- `localisation/`: All text for UI and events. Stored in `.yml` files (e.g., `defcon_l_english.yml`).
- `interface/`: GUI and icon definitions.
- `gfx/`: Visual assets (DDS, TGA, etc.).
- `map/`: Map data including provinces, terrain, and strategic regions.
- `docs/`: Essential documentation (see `docs/SETUP.md`).
- `tools/`: Python-based utility scripts (e.g., `strip_hoi4_logs.py`).

## 4. Development Workflow
- **Coding Standards**: Follow PDX Script syntax (curly braces `{ }`, key-value `=` , strings in `"..."`).
- **Validation**: Always validate changes using **CWTools** before merging.
- **Localization**: Every new text element must have a corresponding localization key in the appropriate `.yml` file within `localisation/`.
- **Release Process**: 
  1. Merge all changes to `main`.
  2. Increment version in `Cold War Iron Curtain/descriptor.mod`.
  3. Tag the release (e.g., `git tag v1.20`).
  4. Push the tag. GitHub Actions (`release.yml`) will handle zipping and Discord notification.

## 5. Key Concepts
- **DEFCON/MAD System**: A strategic tension mechanic implemented via `common/ideas/`.
- **UN Mechanic**: A system simulating international political dynamics.
- **Economic System**: Includes money, policies, edicts, and loan/bond mechanics.
- **Strategic Regions**: Highly detailed map subdivisions for strategic gameplay.

## 6. Common Tasks
- **Adding a New Idea**: Define the logic in `common/ideas/[name].txt` and add the text in `localisation/[lang]/[name]_l_[lang].yml`.
- **Adding an Event**: Define the triggers/effects in `events/[name].txt` and add localization.
- **Release a Mod**: Refer to `docs/SETUP.md` for the complete automated release procedure.

## 7. Troubleshooting
- **Syntax Errors**: Use the **CWTools** extension to highlight errors immediately.
- **Missing Text**: If a UI element shows "Missing Key", search `localisation/` for the key name.
- **CI/CD Failures**: Check the "Actions" tab on GitHub for details on `validate.yml` or `release.yml` failures.

## 8. References
- **Setup Guide**: `docs/SETUP.md`
- **Main Project Info**: `README.md`
- **Environment Setup**: `ColdWarIronCurtain-MKU.code-workspace`