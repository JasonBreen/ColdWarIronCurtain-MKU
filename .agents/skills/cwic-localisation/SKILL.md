---
name: cwic-localisation
description: Add, repair, or review Cold War Iron Curtain localisation while preserving HOI4 encoding and key conventions.
---

# CWIC Localisation

Locate the PDX references before changing text, then update the matching file under `Cold War Iron Curtain/localisation/english/`. English is required for every player-visible event, focus, decision, idea, character, GUI, or tooltip key.

Save `.yml` files as UTF-8 with BOM. Preserve the target file's `l_english:` header, quoting style, key casing, and ordering conventions. Use event keys `<NAMESPACE>.<id>.t`, `.d`, and option suffixes; use `_desc` for focus and decision descriptions.

When the same key family is present in another language directory, add a matching placeholder using the English text so it does not display the raw key. Do not change unrelated keys, mass-reformat localisation, or edit archived `CWIC Backup/` files.

For Southeast Asia localisation or event work, run `py -3 tools/loc_audit.py --check`. Otherwise, use `$cwic-validate` for repository-wide encoding and indentation checks.
