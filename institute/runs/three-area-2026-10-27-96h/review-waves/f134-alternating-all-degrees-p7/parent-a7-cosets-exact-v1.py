#!/usr/bin/env python3
"""Verify seven disjoint A6 cosets in A7 without importing author code.

This refutes the cited seven-index claim; it does not exhibit eight disjoint
cosets or refute Sun8. Output is exclusively created at the path in argv[1].
"""
import hashlib
import itertools
import json
import math
from pathlib import Path
import subprocess
import sys


def clock():
    return subprocess.check_output(
        ['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True
    ).strip()


def even(p):
    return sum(p[i] > p[j] for i in range(7) for j in range(i + 1, 7)) % 2 == 0


def compose(g, h):
    return tuple(g[h[i]] for i in range(7))


def partition_check(group, cosets):
    if len(cosets) != 7 or any(len(c) != 360 for c in cosets):
        return False
    return sum(map(len, cosets)) == len(group) and set.union(*cosets) == group


def main():
    if len(sys.argv) != 2:
        raise SystemExit('usage: checker.py NEW_OUTPUT.json')
    out = Path(sys.argv[1])
    started = clock()
    group = {p for p in itertools.permutations(range(7)) if even(p)}
    stabilizers = [{p for p in group if p[i] == i} for i in range(7)]
    identity = tuple(range(7))
    if len(group) != 2520 or any(len(h) != 360 or identity not in h for h in stabilizers):
        raise SystemExit('group or stabilizer size/identity mismatch')
    if len({frozenset(h) for h in stabilizers}) != 7:
        raise SystemExit('point stabilizers are not distinct')
    if any(compose(g, h) not in stabilizers[0] for g in stabilizers[0] for h in stabilizers[0]):
        raise SystemExit('point stabilizer is not closed')
    ordered_group = sorted(group)
    reps = [next(p for p in ordered_group if p[i] == 0) for i in range(7)]
    cosets = [{compose(g, h) for h in stabilizers[i]} for i, g in enumerate(reps)]
    fibers = [{p for p in group if p[i] == 0} for i in range(7)]
    if cosets != fibers or not partition_check(group, cosets):
        raise SystemExit('cosets are not the seven disjoint point-preimage fibers')
    if any(math.gcd(len(group) // len(stabilizers[i]), len(group) // len(stabilizers[j])) != 7 for i in range(7) for j in range(i + 1, 7)):
        raise SystemExit('index gcd mismatch')
    bad_cosets = cosets[:-1] + [cosets[0]]
    if partition_check(group, bad_cosets):
        raise SystemExit('duplicate-coset negative control was not rejected')
    result = {
        'kind': 'PARENT_INDEPENDENT_EXACT_A7_COUNTEREXAMPLE',
        'started_native_clock': started,
        'finished_native_clock': clock(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'method': 'Enumerate even permutations on seven labels; compose representatives with seven distinct point stabilizers.',
        'group_order': len(group),
        'stabilizer_orders': list(map(len, stabilizers)),
        'distinct_point_stabilizers': len({frozenset(h) for h in stabilizers}),
        'first_stabilizer_closure_checked': True,
        'indices': [len(group) // len(h) for h in stabilizers],
        'seven_left_coset_sizes': list(map(len, cosets)),
        'cosets_equal_distinct_point_preimage_fibers': True,
        'seven_cosets_partition_group': True,
        'all_21_pairwise_index_gcds_equal_seven': True,
        'duplicate_coset_control_rejected': True,
        'limits': 'Seven index-7 cosets refute the all-A_n seven-index exclusion. They are not eight cosets and do not refute Sun8; no other family case or novelty is established.',
    }
    with out.open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
