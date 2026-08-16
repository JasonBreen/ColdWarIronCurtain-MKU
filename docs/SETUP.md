# CWIC Developer Setup Guide

This document describes the one-time setup steps required to get the full GitHub automation working for the **Cold War Iron Curtain** mod.

---

## 1. VS Code extensions

Open the workspace file `ColdWarIronCurtain-MKU.code-workspace` in VS Code.
When prompted, install the recommended extensions:

| Extension | Purpose |
|-----------|---------|
| **CWTools** (`tboby.cwtools-vscode`) | PDX script syntax highlighting, validation, hover docs |
| **HOI4 Mod Utilities** (`nacl.hoi4-mod-utilities`) | Focus tree previewer, localisation helper |
| **YAML** (`redhat.vscode-yaml`) | Localisation file support |
| **GitLens** (`eamodio.gitlens`) | Git history and blame |
| **TODO Tree** (`gruntfuggly.todo-tree`) | Track TODO/FIXME in code |

After installing CWTools, point the HOI4 Mod Utilities extension at your local
mod install. **Do not put this in `.vscode/settings.json`** — that file is
tracked, so your local path would overwrite everyone else's.

Put it in your own User settings (`Ctrl+Shift+P` → *Preferences: Open User
Settings (JSON)*), or in `.vscode/settings.local.json`, which is gitignored:

```json
"hoi4ModUtilities.modFile": "C:/Users/<YourName>/Documents/Paradox Interactive/Hearts of Iron IV/mod/ColdWarIronCurtain/Cold War Iron Curtain/descriptor.mod"
```

The `.editorconfig` at the repo root handles tab indentation and the
localisation UTF-8 BOM automatically, provided you have the
`editorconfig.editorconfig` extension installed.

---

## 2. GitHub repository secrets

Go to **Settings → Secrets and variables → Actions** in the GitHub repository and add the following secrets:

### Required for Discord release notifications

| Secret name | Value |
|-------------|-------|
| `DISCORD_WEBHOOK_URL` | The full webhook URL from your Discord server channel settings. Create one under **Server Settings → Integrations → Webhooks**. |

### Optional – automated Steam Workshop upload

If you want GitHub Actions to push releases to the Steam Workshop automatically:

| Secret name | Value |
|-------------|-------|
| `STEAM_USERNAME` | Your Steam account username (dedicated bot account recommended) |
| `STEAM_PASSWORD` | The Steam account password |

> ⚠️ Use a **dedicated Steam account** for automation, not your personal account. Steam Guard must be disabled or configured for CI on that account.
>
> The release workflow currently only zips and attaches the mod to the GitHub Release. To add steamcmd upload, extend `.github/workflows/release.yml` with a steamcmd step using these secrets.

---

## 3. GitHub labels

The `pr-checks.yml` workflow uses [`actions/labeler`](https://github.com/actions/labeler) to auto-label PRs.
The labels must exist in the repository before they can be applied.

Create the following labels at <https://github.com/JasonBreen/ColdWarIronCurtain-MKU/labels>:

| Label | Suggested colour |
|-------|-----------------|
| `events` | `#e4e669` |
| `focus-trees` | `#0075ca` |
| `decisions` | `#cfd3d7` |
| `ideas` | `#a2eeef` |
| `localisation` | `#d93f0b` |
| `gfx` | `#e99695` |
| `history` | `#c5def5` |
| `ai` | `#bfd4f2` |
| `technologies` | `#0e8a16` |
| `characters` | `#f9d0c4` |
| `ci` | `#000000` |

---

## 4. Creating a release

1. Merge all changes for the release into `development-branch` (the default branch).
2. Update the `version` field in `Cold War Iron Curtain/descriptor.mod`.
3. Create and push a tag:
   ```bash
   git tag v1.20
   git push origin v1.20
   ```
4. The `release.yml` workflow will automatically:
   - Zip the mod folder.
   - Create a GitHub Release with auto-generated release notes.
   - Attach the zip as a downloadable asset.
   - Post a Discord notification (if `DISCORD_WEBHOOK_URL` is set).

---

## 5. What CI actually checks

`.github/workflows/validate.yml` runs three jobs on every push and PR. All are
plain Python 3 with no dependencies, so you can run them locally first:

```bash
python3 tools/check_style.py --diff origin/development-branch   # tabs + loc BOM
python3 tools/check_style.py --all                              # debt report
python3 tools/loc_audit.py --check                              # SEA loc audit
```

| Job | What it does |
|-----|--------------|
| **Style** | Checks that lines *you added* use tab indentation, and that any localisation file you touched keeps its UTF-8 BOM. |
| **Localisation audit** | Runs `loc_audit.py --check`, resolving every SEA event key against `localisation/english/`. |
| **Repository hygiene** | Fails if a script file gains a hardcoded absolute path (`C:\Users\…`). |

### Why the style check is incremental

About **42%** of the PDX script files in this repo use space indentation,
predating the tabs convention. A whole-tree gate would fail on every pull
request forever, so the check only looks at added lines. Run
`python3 tools/check_style.py --all` to see the remaining debt.

Do **not** try to fix it with a mass reformat — that would touch thousands of
files and destroy `git blame` for the mod's history.

### Adding CWTools CLI (optional, future)

Full PDX semantic validation would need [CWTools CLI](https://github.com/cwtools/cwtools-vscode):
install the .NET runtime on the runner, fetch the CWTools binary, and add a step
running `dotnet cwtools validate --game hoi4 "Cold War Iron Curtain"`.
