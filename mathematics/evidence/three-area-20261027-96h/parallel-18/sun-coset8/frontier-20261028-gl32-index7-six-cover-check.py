#!/usr/bin/env python3
"""Check whether six disjoint index-7 GL(3,2) cosets leave another such coset.

This reuses the first GL32 enumeration, so it is not an independent second
implementation; each resulting set relation is checked exactly by bit masks.
"""
import importlib.util
from pathlib import Path

path = Path(__file__).with_name("frontier-20261028-gl32-coset-search.py")
spec = importlib.util.spec_from_file_location("gl32_cosets", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
_, table = module.group()
subgroups = module.all_subgroups(table)
cs = [c[2] for c in module.all_cosets(subgroups, table) if c[3] == 7]
full = (1 << 168) - 1
if len(cs) != len(set(cs)):
    raise SystemExit("FAIL: duplicate index-seven cosets")
coset_set = set(cs)
adj = [0] * len(cs)
for i, a in enumerate(cs):
    for j in range(i):
        if not a & cs[j]:
            adj[i] |= 1 << j
            adj[j] |= 1 << i
counts = [0, 0]
first_bad = None


def visit(chosen, remaining, union):
    global first_bad
    if len(chosen) == 6:
        counts[0] += 1
        if full ^ union not in coset_set:
            counts[1] += 1
            if first_bad is None:
                first_bad = tuple(chosen)
        return
    while remaining:
        bit = remaining & -remaining
        remaining ^= bit
        i = bit.bit_length() - 1
        visit(chosen + [i], remaining & adj[i], union | cs[i])


visit([], (1 << len(cs)) - 1, 0)
print("index_seven_coset_count:", len(cs))
print("six_disjoint_coset_sets:", counts[0])
print("noncoset_complement_sets:", counts[1])
if first_bad is not None:
    print("first_bad_coset_indices:", first_bad)
    raise SystemExit("FAIL: six-coset completion claim is false")
print("PASS: each six-set has index-seven coset as exact complement")
