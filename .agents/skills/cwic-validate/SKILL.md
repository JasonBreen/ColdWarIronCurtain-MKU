---
name: cwic-validate
description: Validate scoped Cold War Iron Curtain changes with the available local audits and CI-equivalent checks.
---

# CWIC Validate

First inspect the changed paths and select only checks that apply. Run `git diff --check` for every change. For Southeast Asia event or English-localisation changes, run:

```powershell
py -3 tools/loc_audit.py --check
```

Check modified PDX `.txt`, `.gui`, and `.gfx` files for leading spaces; PDX indentation must use hard tabs. Confirm modified localisation `.yml` files start with the UTF-8 BOM bytes `EF BB BF`.

The repository's GitHub workflow checks BOM encoding and PDX indentation. Its CWTools CLI step is presently a placeholder, so do not claim full syntax validation from CI or local checks. For gameplay, UI, event-flow, map, or asset changes, state the exact HOI4 in-game test still required or completed.
