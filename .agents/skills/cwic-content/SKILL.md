---
name: cwic-content
description: Create or modify Cold War Iron Curtain PDX gameplay content such as events, focuses, decisions, ideas, AI, or history.
---

# CWIC Content

Work inside `Cold War Iron Curtain/`. Before editing, inspect adjacent files and follow their identifier, filename, and scope conventions rather than introducing a new pattern.

Use hard tabs in PDX files. Keep braces and comments consistent with the target file. Declare an event namespace and use `<NAMESPACE>.<number>` IDs; use `<TAG>_<DescriptiveName>` for focuses and `<tag>_<snake_case_name>` for decisions and ideas.

For every player-visible key, add or update English localisation in `localisation/english/`, saved as UTF-8 with BOM. Do not hard-code local paths, edit `descriptor.mod`'s `path=` line, or modify `CWIC Backup/`.

Make the smallest coherent change. After implementation, use `$cwic-validate` and identify the exact in-game scenario needed to verify triggers, effects, and UI.
