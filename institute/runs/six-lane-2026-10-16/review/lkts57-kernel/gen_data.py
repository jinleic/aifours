#!/usr/bin/env python3
"""Generate a Lean data module from a raw LKTS(v) certificate (LKTS/KTS/CLASS text format).

The raw file is read byte-exactly and its SHA-256 must equal --expect-sha256.  Every row is
emitted in raw order (system, class, row) without sorting, deduplication or repair, as a
Lean triple (a, b, c) of natural numbers.  This script only parses syntax; the Lean kernel
checks every mathematical condition (Lean module LktsKernel.Generic).

Usage:
  python3 gen_data.py RAW OUT.lean --v 57 --name data57 --expect-sha256 HEX --label TEXT
"""
import argparse
import hashlib
import pathlib
import sys


def parse(text, v):
    systems = []
    header_seen = False
    for lineno, line in enumerate(text.split("\n"), 1):
        tok = line.split()
        if not tok or tok[0].startswith("#"):
            continue
        if tok[0] == "LKTS":
            if tok != ["LKTS", str(v)] or header_seen:
                raise SystemExit(f"line {lineno}: unexpected header {line!r}")
            header_seen = True
        elif tok[0] == "KTS":
            if len(tok) != 2 or int(tok[1]) != len(systems):
                raise SystemExit(f"line {lineno}: unexpected system label {line!r}")
            systems.append([])
        elif tok[0] == "CLASS":
            if not systems or len(tok) != 2 or int(tok[1]) != len(systems[-1]):
                raise SystemExit(f"line {lineno}: unexpected class label {line!r}")
            systems[-1].append([])
        else:
            if not systems or not systems[-1] or len(tok) != 3:
                raise SystemExit(f"line {lineno}: unexpected row {line!r}")
            systems[-1][-1].append(tuple(int(t) for t in tok))
    if not header_seen:
        raise SystemExit("missing LKTS header")
    return systems


def render(systems, sha, label, name, v):
    out = [
        "/-",
        "GENERATED FILE - do not edit.  Produced by gen_data.py from the raw certificate",
        f"{label}",
        f"(LKTS({v}) text format), SHA-256 {sha}.",
        f"Rows are copied verbatim in raw order: {name}Sys i = KTS i, and its entry [c][r] = (a, b, c)",
        "is row r of CLASS c.  Nothing is assumed about these numbers here; LktsKernel.Generic",
        "states the checker and its soundness theorem, and the certificate module runs the",
        "checker in the Lean kernel.  Each system is a separate definition only to keep each",
        "elaboration unit small.",
        "-/",
        "namespace Kirkman.KernelCert",
        "",
        "/-- Raw certificate SHA-256 recorded by gen_data.py at generation time. -/",
        f'def {name}RawSha256 : String := "{sha}"',
        "",
    ]
    for i, sysm in enumerate(systems):
        out.append("set_option maxRecDepth 4096 in")
        out.append(f"/-- KTS {i} of the raw LKTS({v}) certificate: its classes, each a list of rows. -/")
        out.append(f"def {name}Sys{i} : List (List (Nat × Nat × Nat)) := [")
        for c, cls in enumerate(sysm):
            rows = ", ".join(f"({a}, {b}, {d})" for (a, b, d) in cls)
            sep = "," if c + 1 < len(sysm) else ""
            out.append(f"  [{rows}]{sep} -- CLASS {c}")
        out.append("]")
        out.append("")
    out.append(f"/-- The raw LKTS({v}) certificate: the list of its systems KTS 0, KTS 1, ... in raw order. -/")
    out.append(f"def {name} : List (List (List (Nat × Nat × Nat))) := [")
    names = [f"{name}Sys{i}" for i in range(len(systems))]
    for j in range(0, len(names), 8):
        chunk = ", ".join(names[j:j + 8])
        sep = "," if j + 8 < len(names) else ""
        out.append(f"  {chunk}{sep}")
    out += ["]", "", "end Kirkman.KernelCert", ""]
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raw")
    ap.add_argument("out")
    ap.add_argument("--v", type=int, required=True)
    ap.add_argument("--name", required=True)
    ap.add_argument("--expect-sha256", required=True)
    ap.add_argument("--label", required=True)
    args = ap.parse_args()
    raw = pathlib.Path(args.raw).read_bytes()
    sha = hashlib.sha256(raw).hexdigest()
    if sha != args.expect_sha256:
        raise SystemExit(f"SHA-256 mismatch: {sha} != {args.expect_sha256}")
    systems = parse(raw.decode("ascii"), args.v)
    text = render(systems, sha, args.label, args.name, args.v)
    pathlib.Path(args.out).write_text(text)
    nrows = sum(len(cls) for s in systems for cls in s)
    print(f"v={args.v} systems={len(systems)} classes={sum(len(s) for s in systems)} rows={nrows} "
          f"raw_sha256={sha} out_sha256={hashlib.sha256(text.encode()).hexdigest()}")


if __name__ == "__main__":
    sys.exit(main())
