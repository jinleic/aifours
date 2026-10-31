#!/usr/bin/env python3
"""Independent exhaustive check of candidate pencil support-mask certificates."""
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys


class CertificateError(ValueError):
    pass


def read_support(path):
    raw = path.read_bytes()
    cells = []
    support = set()
    for number, line in enumerate(raw.decode("utf-8").splitlines(), 1):
        if not line or line.startswith("#"):
            continue
        fields = line.split()
        if len(fields) < 3 or not re.fullmatch(r"[0-5]", fields[0]) or not re.fullmatch(r"[0-5]", fields[1]):
            raise CertificateError(f"bad row at {number}")
        a, b = int(fields[0]), int(fields[1])
        cells.append((a, b))
        for tok in fields[2:]:
            if not re.fullmatch(r"[+\-s][0-5][0-5]", tok):
                raise CertificateError(f"bad token at {number}")
            coord = (a, b, int(tok[1]), int(tok[2]))
            if coord in support:
                raise CertificateError("duplicate support coordinate")
            support.add(coord)
    if cells != list(itertools.product(range(6), repeat=2)) or len(support) != 60:
        raise CertificateError("unexpected cells or support count")
    return support, hashlib.sha256(raw).hexdigest()


def masks_for(support, spectator, level, pencil):
    row, col = [j for j in range(4) if j not in (spectator, pencil)]
    entries = {(p[row], p[col]): p[pencil] for p in support if p[spectator] == level}
    relevant = [p for p in support if p[spectator] == level]
    if len(entries) != len(relevant) or set(entries.values()) != set(range(6)):
        raise CertificateError(f"pencil collision or missing column {(spectator, level, pencil)}")
    masks = []
    for size in range(1, 7):
        for selected in itertools.combinations(range(6), size):
            cells = {cell for cell, variable in entries.items() if variable in selected}
            rows = {r for r, c in cells}
            cols = {c for r, c in cells}
            if cells == set(itertools.product(rows, cols)):
                masks.append(selected)
    return sorted(masks)


def verify(support, candidate):
    total = 0
    for record in candidate["per_slice"]:
        spectator, level = record["spectator"], record["level"]
        for choice in record["choices"]:
            pencil = choice["pencil_axis"]
            observed = masks_for(support, spectator, level, pencil)
            listed = sorted(tuple(x) for x in choice["possible_rectangular_masks"])
            if observed != listed:
                raise CertificateError(f"rectangle-mask mismatch {(spectator,level,pencil)}")
            allowed = sorted({x for mask in observed for x in mask})
            if allowed != choice["allowed_coordinates_for_rank_one"] or 12 - len(allowed) != choice["basis_rank_sum_lower_bound"]:
                raise CertificateError(f"rank-one coordinate bound mismatch {(spectator,level,pencil)}")
            total += 1
    if total != 72:
        raise CertificateError(f"expected 72 matrix pencils, got {total}")
    return total


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("table", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    support, table_sha = read_support(args.table)
    raw = args.candidate.read_bytes()
    candidate = json.loads(raw)
    if candidate["table_sha256"] != table_sha:
        raise CertificateError("candidate binds different table bytes")
    verified = verify(support, candidate)
    mutated = set(support)
    mutated.remove(min(mutated))
    try:
        verify(mutated, candidate)
    except CertificateError as exc:
        if not str(exc).startswith("rectangle-mask mismatch"):
            raise CertificateError(f"mutation rejected for unexpected reason: {exc}") from exc
        negative = str(exc)
    else:
        raise CertificateError("removed coefficient mutation incorrectly accepted")
    result = {"table_sha256": table_sha, "candidate_sha256": hashlib.sha256(raw).hexdigest(),
              "pencils_verified": verified, "all_mask_lists_match": True,
              "one_support_deletion_control": negative,
              "scope": "same-harness independent support parser and rectangle enumeration; mathematical lifting requires the written rank argument"}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result, out, indent=2)
        out.write("\n")
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
