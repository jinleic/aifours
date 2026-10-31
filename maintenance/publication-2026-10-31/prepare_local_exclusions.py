#!/usr/bin/env python3
"""Inventory publication exclusions without removing local files or staging Git.

Default is a dry run. --apply refreshes only this publication's ignore block and
inventory. Existing tracked artifacts are reported separately and never untracked.
"""

import argparse
import os
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
START = "# BEGIN publication exclusions (2026-10-31)"
END = "# END publication exclusions (2026-10-31)"
LIMIT = 1024 * 1024
SOURCE_SUFFIXES = {".py", ".sh", ".c", ".cc", ".cpp", ".h", ".hpp", ".lean", ".md", ".toml", ".yaml", ".yml", ".rs", ".js", ".ts"}
MAGICS = {b"\x7fELF", b"\xcf\xfa\xed\xfe", b"\xfe\xed\xfa\xcf", b"\xca\xfe\xba\xbe"}
# Each pattern is also emitted as a Git rule. Ordinary * never spans a slash.
RULES = [
    ("*.drup", "solver proof stream"),
    ("*.drup.gz", "solver proof stream"),
    ("*.drup.xz", "solver proof stream"),
    ("*.cnf.body*", "generated CNF body"),
    ("**/*-localdeps/**", "vendored Python dependency"),
    ("**/*-python-deps/**", "vendored Python dependency"),
    ("**/three-area-20261027-96h/**/*.html", "downloaded third-party source page"),
    ("**/three-area-20261027-96h/**/*.zip", "downloaded or duplicate input archive"),
    ("**/three-area-20261027-96h/**/*.tar.gz", "downloaded source archive"),
    ("**/three-area-20261027-96h/**/*-stdout.txt", "raw process output"),
    ("**/three-area-20261027-96h/**/*-stderr.txt", "raw process output"),
    ("**/three-area-20261027-96h/**/stdout.txt", "raw process output"),
    ("**/three-area-20261027-96h/**/stderr.txt", "raw process output"),
    ("**/three-area-20261027-96h/**/*public-source.jpg", "third-party page render"),
    ("**/three-area-20261027-96h/**/*source*.png", "third-party page render"),
    ("**/three-area-20261027-96h/**/*-public-browser-source.txt", "third-party source text copy"),
    ("institute/runs/three-area-2026-10-27-96h/public-sources/*.html", "downloaded third-party source page"),
    ("institute/runs/three-area-2026-10-27-96h/source-screens/**/*.png", "third-party page render"),
    ("institute/runs/three-area-2026-10-27-96h/source-screens/**/source-tomar-text-*.txt", "third-party source text copy"),
    ("institute/runs/three-area-2026-10-27-96h/source-screens/**/superseded*text*.txt", "third-party source text copy"),
    ("institute/runs/three-area-2026-10-27-96h/review-waves/*/literal-packet*.md", "duplicate review input packet"),
    ("institute/runs/three-area-2026-10-27-96h/review-waves/*/packet-part-*.md", "duplicate review input packet"),
    ("institute/runs/three-area-2026-10-27-96h/review-waves/*/documentary-snapshot-part*.md", "duplicate review input packet"),
    ("institute/runs/three-area-2026-10-27-96h/review-waves/*/*extracted-text*.txt", "third-party source text copy"),
]


def git_paths(*args):
    return {os.fsdecode(p) for p in subprocess.check_output(
        ["git", "-C", str(ROOT), "ls-files", *args, "-z"]
    ).split(b"\0") if p}


def reason_for(name, size):
    for pattern, reason in RULES:
        if "/" not in pattern:
            pattern = "**/" + pattern
        expression = re.escape(pattern).replace(r"\*\*/", "(?:.*/)?").replace(r"\*\*", ".*").replace(r"\*", "[^/]*")
        if re.fullmatch(expression, name):
            return reason
    path = ROOT / name
    if path.suffix not in SOURCE_SUFFIXES and size > LIMIT:
        return "generated payload over 1 MiB"
    if path.suffix not in SOURCE_SUFFIXES and size >= 4:
        with path.open("rb") as stream:
            if stream.read(4) in MAGICS:
                return "compiled native executable"
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    tracked = git_paths("-c")
    candidates = git_paths("-o", "--exclude-standard")
    # Find future files already hidden by our generic rules, too. Deliberately
    # omit --exclude-standard here so the current .gitignore cannot hide them
    # from the inventory. Matches may overlap older cache/source exclusions.
    candidates.update(git_paths("-o", "-i", *["--exclude=" + pattern for pattern, _ in RULES]))
    inventory = HERE / "additional-exclusions.tsv"
    if inventory.exists():
        candidates.update(line.split("\t", 2)[2] for line in inventory.read_text().splitlines()[1:])
    rows = []
    for name in sorted(candidates - tracked):
        if name.startswith(HERE.relative_to(ROOT).as_posix() + "/"):
            continue
        path = ROOT / name
        if path.is_symlink() or not path.is_file():
            continue
        size = path.stat().st_size
        reason = reason_for(name, size)
        if reason:
            rows.append((size, reason, name))
    lines = [START, "# Payloads stay on disk. Proof sources, compact witnesses, reviews and pins remain eligible."]
    lines += [pattern for pattern, _ in RULES]
    for _, reason, name in rows:
        if reason not in {"generated payload over 1 MiB", "compiled native executable"}:
            continue
        for char in ("\\", "*", "?", "[", "]"):
            name = name.replace(char, "\\" + char)
        lines.append("/" + name)
    lines.append(END)
    ignore = ROOT / ".gitignore"
    original = ignore.read_text()
    if START in original:
        before, rest = original.split(START, 1)
        _, after = rest.split(END, 1)
        original = before.rstrip() + after
    if args.apply:
        ignore.write_text(original.rstrip() + "\n\n" + "\n".join(lines) + "\n")
        inventory.write_text("bytes\treason\tpath\n" + "".join(
            f"{size}\t{reason}\t{name}\n" for size, reason, name in rows
        ))
    print(f"{'Applied' if args.apply else 'Dry run'}: {len(rows)} publication exclusions, {sum(row[0] for row in rows)} bytes; local files preserved")


if __name__ == "__main__":
    main()
