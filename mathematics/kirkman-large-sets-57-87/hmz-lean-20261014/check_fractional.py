#!/usr/bin/env python3
"""Exact fractional feasibility witness; never asserts an integral LKTS exists."""
import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE.parent
PACKING = TARGET / 'evidence/c19-17-staged.frozen-packing.json'
VERIFIER = TARGET / 'work/c19_verify.py'
EXPECTED_PACKING_SHA256 = '6515e4041991d0c857df9c5d5752613f8d958d4ee76296cbbc24c024b807d714'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists():
        raise SystemExit('Refusing to overwrite existing evidence')
    if sha(PACKING) != EXPECTED_PACKING_SHA256:
        raise ValueError('Frozen packing identity differs')
    spec = importlib.util.spec_from_file_location('existing_c19_verifier', VERIFIER)
    verifier = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verifier)
    packing = json.loads(PACKING.read_text())
    if len(packing) != 17:
        raise ValueError('Expected17 fixed constituents')
    occupied = set()
    kept16 = set()
    for index, candidate in enumerate(packing):
        orbits = verifier.check_fixed(candidate)
        if len(orbits) != 28 or occupied & orbits:
            raise ValueError('Invalid or overlapping fixed constituents')
        if index == 16:
            kept16 = occupied.copy()
            released = orbits
        occupied.update(orbits)
    universe = list(itertools.combinations(range(57), 3))
    by_orbit = {}
    for block in universe:
        by_orbit.setdefault(verifier.key(block), []).append(block)
    if len(by_orbit) != 1540 or {len(blocks) for blocks in by_orbit.values()} != {19}:
        raise ValueError('Unexpected triple-orbit inventory')
    residual17 = set(by_orbit) - occupied
    residual16 = set(by_orbit) - kept16
    if len(residual17) != 1064 or len(residual16) != 1092 or residual16 != residual17 | released:
        raise ValueError('Released-system complement mismatch')
    remaining = [block for orbit in sorted(residual17) for block in by_orbit[orbit]]
    pairs = Counter(pair for block in remaining for pair in itertools.combinations(block, 2))
    points = Counter(point for block in remaining for point in block)
    if len(remaining) != 20216 or set(pairs) != set(itertools.combinations(range(57), 2)):
        raise ValueError('Wrong concrete complement')
    if set(pairs.values()) != {38} or points != Counter({point: 1064 for point in range(57)}):
        raise ValueError('Wrong residual pair/point degree')
    pair_weight, class_weight = Fraction(1, 38), Fraction(1, 1064)
    checks = {
        'pair_model_orbit': 2 * 19 * pair_weight,
        'pair_model_pair': 38 * pair_weight,
        'class_model_orbit': 2 * 19 * 28 * class_weight,
        'class_model_pair': 38 * 28 * class_weight,
        'class_model_point': 1064 * class_weight,
    }
    if any(value != 1 for value in checks.values()):
        raise ValueError('Fractional witness violates exact-one constraints')
    wrong = Fraction(1, 37)
    rejected = 2 * 19 * wrong != 1 and 38 * wrong != 1
    if not rejected:
        raise ValueError('Wrong-denominator control was not rejected')
    receipt = {
        'verdict': 'PASS_EXACT_FRACTIONAL_WITNESS_ONLY',
        'full_goal_solved': False, 'target57_certificate': False, 'target87_certificate': False,
        'source_sha256': sha(Path(__file__).resolve()), 'packing_sha256': sha(PACKING),
        'existing_verifier_sha256': sha(VERIFIER),
        'fixed_systems_checked': 17, 'retained_systems': 16, 'released_system': 16,
        'released_orbits': len(released), 'joint_orbit_universe': len(residual16),
        'frozen_completion_orbits': len(residual17), 'remaining_concrete_triples': len(remaining),
        'residual_pair_degree': 38, 'residual_point_degree': 1064,
        'unnormalized_pair_placement_rows': len(residual17) * 19 * 2,
        'unnormalized_class_placement_rows': len(residual17) * 19 * 2 * 28,
        'pair_weight': str(pair_weight), 'class_weight': str(class_weight),
        'exact_constraint_sums': {name: str(value) for name, value in checks.items()},
        'negative_control': {'changed_pair_denominator': 37, 'rejected': rejected,
                             'orbit_and_pair_sum': str(38 * wrong)},
        'scope': 'Unnormalized continuous relaxation only; no integral construction or infeasibility claim.'
    }
    args.output.write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps(receipt, indent=2))


if __name__ == '__main__':
    main()
