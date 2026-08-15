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

After installing **HOI4 Mod Utilities**, verify `.vscode/settings.json` has the correct `hoi4ModUtilities.modFile` path for your setup:

```json
"hoi4ModUtilities.modFile": "${workspaceFolder}/Cold War Iron Curtain/descriptor.mod"
```

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

1. Merge all changes for the release into `main`.
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

## 5. CWTools CLI validation (future)

The `validate.yml` workflow has a placeholder step for [CWTools CLI](https://github.com/cwtools/cwtools-vscode).
To enable full validation:

1. Install the .NET runtime on your CI runner (or use a Docker image).
2. Download the CWTools CLI release binary.
3. Replace the placeholder step in `.github/workflows/validate.yml` with:
   ```yaml
   - name: Run CWTools validation
     run: dotnet cwtools validate --game hoi4 "Cold War Iron Curtain"
   ```
