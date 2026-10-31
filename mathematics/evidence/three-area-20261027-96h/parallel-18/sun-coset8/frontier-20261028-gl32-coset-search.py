#!/usr/bin/env python3
"""Bounded actual-coset Sun8 search in GL(3,2), order168.

Enumerates subgroups from explicit matrix generators, all actual left cosets,
and an exact gcd/disjointness clique. No external packages or float arithmetic.
"""
from collections import Counter, deque
from itertools import product
from math import gcd


def apply(cols, x):
    return (cols[0] if x & 1 else 0) ^ (cols[1] if x & 2 else 0) ^ (cols[2] if x & 4 else 0)


def group():
    mats = [c for c in product(range(1, 8), repeat=3)
            if len({apply(c, x) for x in range(8)}) == 8]
    pos = {m: i for i, m in enumerate(mats)}
    if len(mats) != 168 or mats[0] != (1, 2, 4):
        raise ValueError("invalid GL(3,2) enumeration")
    table = [[pos[tuple(apply(a, v) for v in b)] for b in mats] for a in mats]
    return mats, table


def generated(gens, table):
    seen = 1
    todo = deque([0])
    while todo:
        x = todo.popleft()
        for gen in gens:
            y = table[x][gen]
            if not seen >> y & 1:
                seen |= 1 << y
                todo.append(y)
    return seen


def all_subgroups(table):
    known = {1: ()}
    todo = deque([1])
    while todo:
        h = todo.popleft()
        gens = known[h]
        for g in range(168):
            if h >> g & 1:
                continue
            newgens = gens + (g,)
            k = generated(newgens, table)
            if k not in known:
                known[k] = newgens
                todo.append(k)
    return sorted(known, key=lambda h: (h.bit_count(), h))


def all_cosets(groups, table):
    cs = []
    full = (1 << 168) - 1
    for h in groups:
        H = [i for i in range(168) if h >> i & 1]
        if any(not (h >> table[x][y] & 1) for x in H for y in H):
            raise ValueError("subgroup closure failure")
        remaining = full
        while remaining:
            g = (remaining & -remaining).bit_length() - 1
            c = sum(1 << table[g][x] for x in H)
            if c.bit_count() != len(H) or c & remaining != c:
                raise ValueError("coset partition failure")
            cs.append((h, g, c, 168 // len(H)))
            remaining &= ~c
    return cs


def find_eight(cs):
    adj = [0] * len(cs)
    for i in range(len(cs)):
        ci, ni = cs[i][2:]
        for j in range(i):
            cj, nj = cs[j][2:]
            if gcd(ni, nj) <= 7 and not ci & cj:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    seen = 0

    def color(mask):
        order, bounds = [], []
        k = 0
        while mask:
            k += 1
            avail = mask
            while avail:
                low = avail & -avail
                v = low.bit_length() - 1
                order.append(v)
                bounds.append(k)
                mask &= ~low
                avail &= ~low
                avail &= ~adj[v]
        return order, bounds

    def dfs(chosen, candidates):
        nonlocal seen
        seen += 1
        if len(chosen) == 8:
            return chosen
        order, bounds = color(candidates)
        for j in range(len(order) - 1, -1, -1):
            if len(chosen) + bounds[j] < 8:
                return None
            v = order[j]
            result = dfs(chosen + [v], candidates & adj[v])
            if result is not None:
                return result
            candidates &= ~(1 << v)
        return None

    return dfs([], (1 << len(cs)) - 1), seen


def main():
    mats, table = group()
    print("group_order:", len(mats), flush=True)
    subs = all_subgroups(table)
    print("subgroup_count:", len(subs), flush=True)
    print("subgroups_by_order:", dict(sorted(Counter(x.bit_count() for x in subs).items())), flush=True)
    cs = all_cosets(subs, table)
    print("left_coset_count:", len(cs), flush=True)
    print("cosets_by_index:", dict(sorted(Counter(x[3] for x in cs).items())), flush=True)
    found, seen = find_eight(cs)
    print("clique_search_nodes:", seen, flush=True)
    if found is None:
        print("RESULT: no eight-coset counterconfiguration in GL(3,2)")
    else:
        print("CANDIDATE: requires independent witness checking")
        for j in found:
            h, g, c, n = cs[j]
            print("candidate:", n, mats[g], hex(h), hex(c))


if __name__ == "__main__":
    main()
