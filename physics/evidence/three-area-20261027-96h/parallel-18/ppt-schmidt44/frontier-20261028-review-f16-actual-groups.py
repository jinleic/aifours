#!/usr/bin/env python3
"""Independently enumerate actual A5 and D22 subgroups/cosets, then 8-cliques.

Search uses exact integer bitsets and a proper greedy coloring upper bound.
This verifies only these two finite examples, not arbitrary-group theorems.
"""
from collections import Counter, deque
from itertools import permutations
from math import gcd
import json


def parity(p):
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def a5():
    elements = [p for p in permutations(range(5)) if parity(p) == 0]
    index = {p: i for i, p in enumerate(elements)}
    table = [[index[tuple(a[b[i]] for i in range(5))] for b in elements] for a in elements]
    return table, index[tuple(range(5))]


def d22():
    elements = [(r, s) for s in range(2) for r in range(11)]
    index = {x: i for i, x in enumerate(elements)}
    table = [[index[((r + (-1 if s else 1) * t) % 11, s ^ u)]
              for t, u in elements] for r, s in elements]
    return table, index[(0, 0)]


def indices(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def generated(gens, table, identity):
    found = 1 << identity
    todo = [identity]
    while todo:
        x = todo.pop()
        for g in gens:
            y = table[x][g]
            bit = 1 << y
            if not found & bit:
                found |= bit
                todo.append(y)
    return found


def subgroups(table, identity):
    n = len(table)
    seen = {1 << identity: ()}
    todo = deque([1 << identity])
    while todo:
        h = todo.popleft()
        generators = seen[h]
        for x in range(n):
            if h & (1 << x):
                continue
            newgens = generators + (x,)
            extension = generated(newgens, table, identity)
            if extension not in seen:
                seen[extension] = newgens
                todo.append(extension)
    for h in seen:
        members = list(indices(h))
        if identity not in members or any(not (h & (1 << table[a][b])) for a in members for b in members):
            raise AssertionError("invalid subgroup")
    return list(seen)


def cosets(table, subgroups_):
    n = len(table)
    out = []
    for h in subgroups_:
        members = list(indices(h))
        remaining = (1 << n) - 1
        found = []
        while remaining:
            bit = remaining & -remaining
            x = bit.bit_length() - 1
            c = sum(1 << table[x][g] for g in members)
            if c.bit_count() != len(members) or c & ~remaining:
                raise AssertionError("cosets do not partition")
            remaining ^= c
            found.append(c)
            out.append((n // len(members), c))
        if len(found) != n // len(members):
            raise AssertionError("wrong coset index")
    return out


def find_eight(cosets_):
    n = len(cosets_)
    neighbors = [0] * n
    for i, (ai, ci) in enumerate(cosets_):
        for j in range(i + 1, n):
            aj, cj = cosets_[j]
            if not (ci & cj) and gcd(ai, aj) <= 7:
                neighbors[i] |= 1 << j
                neighbors[j] |= 1 << i
    nodes = 0

    def enough_colors(remaining, needed):
        # Partition the candidate graph into independent color classes.
        colors = 0
        while remaining:
            colors += 1
            if colors >= needed:
                return True  # no pruning from this partial coloring
            available = remaining
            while available:
                bit = available & -available
                v = bit.bit_length() - 1
                remaining ^= bit
                available &= ~bit
                available &= ~neighbors[v]
        return False

    def search(candidates, chosen):
        nonlocal nodes
        nodes += 1
        if len(chosen) == 8:
            return chosen
        needed = 8 - len(chosen)
        if candidates.bit_count() < needed or not enough_colors(candidates, needed):
            return None
        while candidates.bit_count() >= needed:
            bit = candidates & -candidates
            v = bit.bit_length() - 1
            candidates ^= bit
            got = search(candidates & neighbors[v], chosen + (v,))
            if got is not None:
                return got
        return None

    witness = search((1 << n) - 1, ())
    if witness:
        if any(cosets_[i][1] & cosets_[j][1] or gcd(cosets_[i][0], cosets_[j][0]) > 7
               for pos, i in enumerate(witness) for j in witness[pos + 1:]):
            raise AssertionError("bad output witness")
    return nodes, witness


def check(name, group):
    table, identity = group()
    h = subgroups(table, identity)
    c = cosets(table, h)
    nodes, witness = find_eight(c)
    return {"group": name, "order": len(table), "subgroup_count": len(h),
            "subgroups_by_order": dict(sorted(Counter(x.bit_count() for x in h).items())),
            "coset_count": len(c), "cosets_by_index": dict(sorted(Counter(i for i, _ in c).items())),
            "search_nodes": nodes, "counterexample_found": witness is not None}


print(json.dumps([check("D22", d22), check("A5", a5)], indent=2))
