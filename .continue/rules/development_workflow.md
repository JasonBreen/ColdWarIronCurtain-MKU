# Development Workflow & Best Practices

## Code Changes
- **Testing**: Always verify changes within the HOI4 mod environment if possible.
- **Validation**: Use CWTools for syntax and logic validation. Check for errors in the HOI4 log after running the mod.
- **Localization**: When adding new text, ensure a corresponding localization key is added to the appropriate `.yml` file in `localisation/`.

## Git & Version Control
- **Branching**: Work on feature branches for significant changes.
- **Commits**: Use descriptive commit messages.
- **Releases**: Follow the process outlined in `docs/SETUP.md` for creating a release (update `descriptor.mod`, tag, and push).

## File Organization
- `common/`: Primary data files (characters, buildings, ai, etc.).
- `events/`: Game events.
- `localisation/`: All text for UI and events (in `.yml` format).
- `interface/`: GUI and icon definitions.
- `gfx/`: All visual assets (textures, models).
- `map/`: Map-related data.

## Automation
- **GitHub Actions**: 
  - `validate.yml`: Runs CI checks (including CWTools if configured).
  - `release.yml`: Handles mod zipping and GitHub releases.

## Important Files
- `Cold War Iron Curtain/descriptor.mod`: Contains mod version and metadata.
- `docs/SETUP.md`: Detailed instructions for developers.
