# Copilot Coding Agent – CWIC Rules

You are a coding agent working on the **Cold War Iron Curtain** Hearts of Iron IV mod.
Follow these rules precisely whenever you read or write files in this repository.

## Mandatory rules

1. **Tabs only.** All PDX script files (`.txt`, `.gui`, `.gfx`, `.asset`) use hard tab (`\t`) indentation. Never use spaces for indentation.

2. **descriptor.mod is off-limits for path edits.** You may add `replace_path` lines if a new folder is being fully replaced, but **never change or delete** the `path=` line or existing `replace_path` entries.

3. **Always add localisation.** Any script key visible to the player (event title/desc/option, focus name/desc, decision name/desc, idea name/desc, character name) **must** have a matching entry in `localisation/english/`. Save localisation files as UTF-8 with BOM.

4. **Follow naming conventions.**
   - Events: namespace prefix, e.g. `USA.1`, `USA.2` — namespace declared with `add_namespace = USA` at top of file.
   - Focuses: `<TAG>_<DescriptiveName>`, e.g. `USA_Marshall_Plan`.
   - Decisions: `<tag>_<snake_case_name>`.
   - Ideas/spirits: `<tag>_<snake_case_name>`.

5. **Match existing file naming.** Before creating a new file, check what files already exist in the target folder and match their casing and naming pattern.

6. **Do not modify `CWIC Backup/`.** This folder is an archive and must not be changed.

7. **No hardcoded local paths.** Script files must never reference absolute filesystem paths.

8. **Minimal scope.** Only modify files directly related to the task. Do not refactor or reformat unrelated files.

9. **Test-in-game note.** PDX script has no automated test runner; flag any change that requires an in-game test in your PR description so a human can verify it.

10. **Localisation language coverage.** English is required. If translations exist for the same key in `french/`, `japanese/`, etc., add placeholder entries (copy the English value) so the game does not fall back to key names.
