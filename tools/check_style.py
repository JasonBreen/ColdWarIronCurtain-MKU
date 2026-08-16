#!/usr/bin/env python3
"""CWIC repository style checker.

Enforces the two mechanical conventions that CI can actually verify:

  1. PDX script (.txt/.gui/.gfx/.asset) indents with hard tabs, never spaces.
  2. Localisation .yml files are UTF-8 with BOM (empty files are exempt --
     a zero-byte file cannot carry a BOM).

Modes
-----
--diff <base>   Check only the lines ADDED relative to <base>. This is what CI
                runs on pull requests. Roughly 42% of the PDX files in this repo
                predate the tab convention, so a whole-tree gate would fail on
                every pull request forever and teach everyone to ignore CI.
                Checking added lines holds new work to the standard without
                punishing anyone for touching a legacy file.

--all           Audit the whole tree and report how much legacy debt remains.
                Exits 0 by default so it is safe to run anywhere; pass --strict
                to make it exit non-zero instead.

Usage
-----
    python3 tools/check_style.py --diff origin/development-branch
    python3 tools/check_style.py --all
"""

import argparse
import os
import subprocess
import sys

MOD = "Cold War Iron Curtain"
SCRIPT_EXTS = (".txt", ".gui", ".gfx", ".asset")
LOC_DIR = MOD + "/localisation"

# Archived / vendored trees that are not held to current conventions.
EXCLUDED_PREFIXES = (
    "CWIC Backup/",
    "CWIC +Translate/",
    "Reworked MLA/",
    "For yuri from Taiga/",
)


def _run(cmd):
    """Run a git command, returning stdout (empty string on failure)."""
    try:
        out = subprocess.run(
            cmd, capture_output=True, text=True, errors="replace", check=False
        )
        return out.stdout if out.returncode == 0 else ""
    except OSError:
        return ""


def is_excluded(path):
    return any(path.startswith(p) for p in EXCLUDED_PREFIXES)


def is_script(path):
    return path.endswith(SCRIPT_EXTS) and not is_excluded(path)


def is_loc(path):
    return path.endswith(".yml") and path.startswith(LOC_DIR) and not is_excluded(path)


def added_lines_by_file(base):
    """Map each changed file to a list of (line_no, text) for ADDED lines."""
    diff = _run(["git", "diff", "--unified=0", "--no-color", f"{base}...HEAD"])
    if not diff:
        # Fall back to a two-dot diff when no merge base exists (e.g. a shallow
        # clone or a freshly created branch).
        diff = _run(["git", "diff", "--unified=0", "--no-color", base])

    result = {}
    path = None
    new_ln = 0
    for line in diff.splitlines():
        if line.startswith("+++ "):
            target = line[4:].strip()
            path = None if target == "/dev/null" else target[2:]  # strip "b/"
            continue
        if line.startswith("@@"):
            # @@ -old,cnt +new,cnt @@
            try:
                seg = line.split("+", 1)[1].split("@@", 1)[0].strip()
                new_ln = int(seg.split(",")[0])
            except (IndexError, ValueError):
                new_ln = 0
            continue
        if path and line.startswith("+") and not line.startswith("+++"):
            result.setdefault(path, []).append((new_ln, line[1:]))
            new_ln += 1
    return result


def check_indent_lines(lines):
    """Return added lines that begin with a space."""
    return [(ln, text) for ln, text in lines if text.startswith(" ") and text.strip()]


def has_bom(path):
    try:
        with open(path, "rb") as fh:
            return fh.read(3) == b"\xef\xbb\xbf"
    except OSError:
        return True  # unreadable -> do not fail the build on it


def is_empty(path):
    try:
        return os.path.getsize(path) == 0
    except OSError:
        return False


def mode_diff(base):
    changed = added_lines_by_file(base)
    if not changed:
        print(f"No changed lines against {base}; nothing to check.")
        return 0

    failures = 0

    for path in sorted(changed):
        if not is_script(path):
            continue
        bad = check_indent_lines(changed[path])
        if bad:
            failures += 1
            print(f"\nSPACE INDENT  {path}")
            for ln, text in bad[:10]:
                print(f"    line {ln}: {text[:80].rstrip()}")
            if len(bad) > 10:
                print(f"    ... and {len(bad) - 10} more line(s)")

    for path in sorted(changed):
        if not is_loc(path) or not os.path.exists(path):
            continue
        if is_empty(path):
            continue
        if not has_bom(path):
            failures += 1
            print(f"\nMISSING BOM   {path}")
            print("    Localisation files must be saved as UTF-8 with BOM.")

    if failures:
        print(
            f"\n{failures} file(s) failed. PDX script indents with hard tabs; "
            "localisation .yml files are UTF-8 with BOM."
        )
        return 1

    print(f"Style OK - checked {len(changed)} changed file(s) against {base}.")
    return 0


def mode_all(strict):
    script_total = script_bad = 0
    loc_total = loc_bad = loc_empty = 0
    bad_loc_files = []

    for root, dirs, files in os.walk(".", topdown=True):
        dirs[:] = [d for d in dirs if d != ".git"]
        for name in files:
            rel = os.path.relpath(os.path.join(root, name), ".").replace("\\", "/")
            if is_script(rel):
                script_total += 1
                try:
                    with open(rel, "r", encoding="utf-8", errors="replace") as fh:
                        for line in fh:
                            if line.startswith(" ") and line.strip():
                                script_bad += 1
                                break
                except OSError:
                    pass
            elif is_loc(rel):
                loc_total += 1
                if is_empty(rel):
                    loc_empty += 1
                elif not has_bom(rel):
                    loc_bad += 1
                    bad_loc_files.append(rel)

    pct = (script_bad / script_total * 100) if script_total else 0
    print("Whole-tree audit")
    print(f"  PDX script files      : {script_total}")
    print(f"    with space indent   : {script_bad}  ({pct:.1f}% legacy debt)")
    print(f"  Localisation .yml     : {loc_total}")
    print(f"    missing BOM         : {loc_bad}")
    print(f"    empty (BOM exempt)  : {loc_empty}")
    for f in bad_loc_files[:20]:
        print(f"      - {f}")

    if strict and (script_bad or loc_bad):
        return 1
    return 0


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--diff", metavar="BASE", help="check only lines added vs BASE")
    g.add_argument("--all", action="store_true", help="audit the whole tree")
    ap.add_argument(
        "--strict", action="store_true", help="with --all, exit 1 on any finding"
    )
    args = ap.parse_args()

    if args.diff:
        return mode_diff(args.diff)
    return mode_all(args.strict)


if __name__ == "__main__":
    sys.exit(main())
