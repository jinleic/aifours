#!/usr/bin/env python3
"""Exact search for eight actual disjoint cosets in A5 with gcds <=7.

Enumerates every subgroup by successive closure under an added group element,
then every left coset. The clique search uses an explicit proper-color bound.
No external package, floating point, network, or mutable data input.
"""
from collections import Counter, deque
from itertools import permutations
from math import gcd


def bits(mask):
    while mask:
        low = mask & -mask
        yield low.bit_length() - 1
        mask ^= low


def group():
    perms = []
    for p in permutations(range(5)):
        inv = sum(p[i] > p[j] for i in range(5) for j in range(i + 1, 5))
        if inv % 2 == 0:
            perms.append(p)
    pos = {p: i for i, p in enumerate(perms)}
    table = [[pos[tuple(a[b[i]] for i in range(5))] for b in perms] for a in perms]
    if len(perms) != 60 or perms[0] != tuple(range(5)):
        raise RuntimeError("incorrect permutation group or identity")
    return perms, table


def extend(h, g, table):
    generators = list(bits(h)) + [g]
    seen = 1
    todo = deque([0])
    while todo:
        x = todo.popleft()
        for gen in generators:
            y = table[x][gen]
            if not seen >> y & 1:
                seen |= 1 << y
                todo.append(y)
    return seen


def all_subgroups(table):
    found = {1}
    pending = deque([1])
    while pending:
        h = pending.popleft()
        for g in range(60):
            if h >> g & 1:
                continue
            k = extend(h, g, table)
            if k not in found:
                found.add(k)
                pending.append(k)
    subgroups = sorted(found, key=lambda h: (h.bit_count(), h))
    for h in subgroups:
        members = tuple(bits(h))
        if not (h & 1) or 60 % len(members):
            raise RuntimeError("bad subgroup identity/order")
        if any(not (h >> table[x][y] & 1) for x in members for y in members):
            raise RuntimeError("subgroup is not closed")
    return subgroups


def cosets(subgroups, table):
    result = []
    full = (1 << 60) - 1
    for h in subgroups:
        members = tuple(bits(h))
        remaining = full
        while remaining:
            g = (remaining & -remaining).bit_length() - 1
            c = sum(1 << table[g][x] for x in members)
            if c.bit_count() != len(members) or c & remaining != c:
                raise RuntimeError("bad left-coset partition")
            result.append((h, g, c, 60 // len(members)))
            remaining &= ~c
    return result


def find_eight(coset_list):
    total = len(coset_list)
    adjacency = [0] * total
    for i in range(total):
        ci, ni = coset_list[i][2:]
        for j in range(i):
            cj, nj = coset_list[j][2:]
            if not ci & cj and gcd(ni, nj) <= 7:
                adjacency[i] |= 1 << j
                adjacency[j] |= 1 << i
    visited = 0

    def colors(mask):
        order, bounds = [], []
        color = 0
        while mask:
            color += 1
            available = mask
            while available:
                low = available & -available
                v = low.bit_length() - 1
                order.append(v)
                bounds.append(color)
                mask &= ~low
                available &= ~low
                available &= ~adjacency[v]
        return order, bounds

    def search(chosen, candidates):
        nonlocal visited
        visited += 1
        if len(chosen) == 8:
            return chosen
        order, bound = colors(candidates)
        for k in range(len(order) - 1, -1, -1):
            if len(chosen) + bound[k] < 8:
                return None
            v = order[k]
            answer = search(chosen + [v], candidates & adjacency[v])
            if answer is not None:
                return answer
            candidates &= ~(1 << v)
        return None

    return search([], (1 << total) - 1), visited


def main():
    perms, table = group()
    subs = all_subgroups(table)
    coset_list = cosets(subs, table)
    print("group_order:", len(perms), flush=True)
    print("subgroup_count:", len(subs), flush=True)
    print("subgroups_by_order:", dict(sorted(Counter(h.bit_count() for h in subs).items())), flush=True)
    print("left_coset_count:", len(coset_list), flush=True)
    print("cosets_by_index:", dict(sorted(Counter(c[3] for c in coset_list).items())), flush=True)
    answer, visited = find_eight(coset_list)
    print("clique_search_nodes:", visited)
    if answer is None:
        print("RESULT: no eight-coset counterconfiguration in A5")
    else:
        print("RESULT: candidate requires independent witness validation")
        for i in answer:
            h, g, c, n = coset_list[i]
            print("candidate:", "index", n, "representative", perms[g],
                  "subgroup_mask", hex(h), "coset_mask", hex(c))


if __name__ == "__main__":
    main()
