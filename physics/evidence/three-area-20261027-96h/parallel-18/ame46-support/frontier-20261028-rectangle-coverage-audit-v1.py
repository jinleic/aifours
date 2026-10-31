#!/usr/bin/env python3
"""Check complete slice/pencil coverage and aggregation of a rank-mask receipt."""
import argparse
import collections
import copy
import hashlib
import itertools
import json
from pathlib import Path
import sys


class CoverageError(ValueError):
    pass


def audit(data):
    records = data["per_slice"]
    expected_slices = set(itertools.product(range(4), range(6)))
    observed_slices = [(r["spectator"], r["level"]) for r in records]
    if len(observed_slices) != 24 or set(observed_slices) != expected_slices:
        raise CoverageError("duplicate or missing spectator-level slice")
    totals = collections.Counter()
    rank_one_dims = collections.Counter()
    masks = collections.Counter()
    pencils = set()
    for rec in records:
        spectator, level = rec["spectator"], rec["level"]
        choices = rec["choices"]
        if len(choices) != 3 or {c["pencil_axis"] for c in choices} != set(range(4)) - {spectator}:
            raise CoverageError("duplicate or missing active pencil")
        bounds = []
        for choice in choices:
            key = (spectator, level, choice["pencil_axis"])
            if key in pencils:
                raise CoverageError("duplicate pencil")
            pencils.add(key)
            allowed = set(choice["allowed_coordinates_for_rank_one"])
            mask_items = choice["possible_rectangular_masks"]
            if {i for mask in mask_items for i in mask} != allowed:
                raise CoverageError("rank-one coordinate union mismatch")
            if choice["basis_rank_sum_lower_bound"] != 12 - len(allowed):
                raise CoverageError("pencil rank-sum bound mismatch")
            rank_one_dims[len(allowed)] += 1
            for mask in mask_items:
                masks[len(mask)] += 1
            bounds.append(choice["basis_rank_sum_lower_bound"])
        if rec["best_bound"] != max(bounds):
            raise CoverageError("slice maximum mismatch")
        totals[spectator] += rec["best_bound"]
    expected_pencils = {(s, l, p) for s in range(4) for l in range(6) for p in range(4) if p != s}
    if pencils != expected_pencils:
        raise CoverageError("pencil universe mismatch")
    claimed = {r["spectator"]: r["support_lower_bound"] for r in data["totals_by_spectator"]}
    if len(data["totals_by_spectator"]) != 4 or claimed != dict(totals):
        raise CoverageError("spectator total mismatch")
    return {"slices": len(records), "pencils": len(pencils),
            "rank_one_subspace_dimension_histogram": dict(sorted(rank_one_dims.items())),
            "rectangular_mask_size_histogram": dict(sorted(masks.items())),
            "totals_by_spectator": dict(sorted(totals.items()))}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("candidate", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    raw = args.candidate.read_bytes()
    candidate = json.loads(raw)
    summary = audit(candidate)
    mutant = copy.deepcopy(candidate)
    mutant["per_slice"][0] = copy.deepcopy(mutant["per_slice"][1])
    try:
        audit(mutant)
    except CoverageError as exc:
        if str(exc) != "duplicate or missing spectator-level slice":
            raise
        rejection = str(exc)
    else:
        raise CoverageError("duplicate-slice mutation incorrectly accepted")
    result = {"candidate_sha256": hashlib.sha256(raw).hexdigest(), "coverage": summary,
              "duplicate_slice_control": rejection,
              "scope": "Aggregation/coverage audit only; independent support-mask verifier is separate."}
    with args.output.open("x", encoding="utf-8") as out:
        json.dump(result, out, indent=2)
        out.write("\n")
    json.dump(result, sys.stdout, indent=2)
    print()


if __name__ == "__main__":
    main()
