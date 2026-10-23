#!/usr/bin/env python3
"""Refresh exact Git exclusions for large generated files and native executables.

Keeps every local file. Does not stage, commit, push, or rewrite historical records.
Run from any directory; the repository root is derived from this script's location.
"""

from pathlib import Path
import os
import subprocess

ROOT = Path(__file__).resolve().parents[2]
START = "# BEGIN generated publication exclusions (maintenance/publication-2026-10-22)"
END = "# END generated publication exclusions"
SOURCE_SUFFIXES = {
    ".py", ".sh", ".bash", ".zsh", ".c", ".cc", ".cpp", ".h", ".hpp",
    ".lean", ".md", ".toml", ".yaml", ".yml", ".rs", ".js", ".ts",
}
MAGICS = {b"\x7fELF", b"\xcf\xfa\xed\xfe", b"\xfe\xed\xfa\xcf", b"\xca\xfe\xba\xbe"}


def main():
    os.chdir(ROOT)
    ignore = ROOT / ".gitignore"
    original = ignore.read_text()
    # Include the previously generated paths so refreshes are idempotent.
    old_paths = []
    if START in original:
        before, rest = original.split(START, 1)
        block, after = rest.split(END, 1)
        old_paths = [line[1:] for line in block.splitlines() if line.startswith("/")]
        original = before.rstrip() + after
    raw = subprocess.check_output([
        "git", "ls-files", "-c", "-o", "--exclude-standard", "-z",
    ])
    paths = set(os.fsdecode(p) for p in raw.split(b"\0") if p)
    paths.update(old_paths)
    selected = []
    for name in sorted(paths):
        path = ROOT / name
        if path.is_symlink() or not path.is_file() or path.suffix in SOURCE_SUFFIXES:
            continue
        size = path.stat().st_size
        if size > 5 * 1024 * 1024:
            selected.append((name, size, "generated file over 5 MiB"))
        elif size > 1024 * 1024 and any(
            part in {"mutations", "construction_mutations", "controls", "ablations", "reversed", "orderings"}
            for part in path.relative_to(ROOT).parts
        ):
            selected.append((name, size, "large generated control or duplicate enumeration"))
        elif size >= 4:
            with path.open("rb") as stream:
                magic = stream.read(4)
            if magic in MAGICS:
                selected.append((name, size, "compiled native executable"))
    # Escape metacharacters in Git wildmatch paths, preserving directory slashes.
    def pattern(name):
        for char in ("\\", "*", "?", "[", "]"):
            name = name.replace(char, "\\" + char)
        return "/" + name
    lines = [START, "# Exact generated payloads; sources and small witnesses remain versioned."]
    lines.extend(pattern(name) for name, _, _ in selected)
    lines.append(END)
    ignore.write_text(original.rstrip() + "\n\n" + "\n".join(lines) + "\n")
    manifest = Path(__file__).with_name("exact-exclusions.tsv")
    manifest.write_text("bytes\treason\tpath\n" + "".join(
        f"{size}\t{reason}\t{name}\n" for name, size, reason in selected
    ))
    print(f"Exact exclusions: {len(selected)} files, {sum(s for _, s, _ in selected) / 2**20:.2f} MiB; local files preserved")


if __name__ == "__main__":
    main()
