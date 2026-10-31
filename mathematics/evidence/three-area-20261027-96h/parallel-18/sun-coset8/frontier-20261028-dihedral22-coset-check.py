#!/usr/bin/env python3
"""Exhaustive actual left-coset check in C11 semidirect C2.

Independent, finite arithmetic only. Not an unrestricted Sun8 proof.
"""
from collections import Counter, deque
from math import gcd

P = 11
G = [(a, b) for b in range(2) for a in range(P)]
POS = {x: i for i, x in enumerate(G)}
MUL = [[POS[((a + ((-1)**b)*c) % P, (b+d) % 2)] for c, d in G] for a, b in G]
FULL = (1 << len(G)) - 1


def members(mask):
    return [i for i in range(len(G)) if mask & (1 << i)]


def generated(h, g):
    gens = members(h) + [g]
    seen = 1
    queue = deque([0])
    while queue:
        x = queue.popleft()
        for y in gens:
            z = MUL[x][y]
            if not seen & (1 << z):
                seen |= 1 << z
                queue.append(z)
    return seen


def subgroups():
    found, queue = {1}, deque([1])
    while queue:
        h = queue.popleft()
        for g in range(len(G)):
            if h & (1 << g):
                continue
            k = generated(h, g)
            if k not in found:
                found.add(k)
                queue.append(k)
    return sorted(found, key=lambda x: (x.bit_count(), x))


def all_cosets(hs):
    out = []
    for h in hs:
        H = members(h)
        if any(not h & (1 << MUL[x][y]) for x in H for y in H):
            raise ValueError("nonclosed subgroup")
        remaining = FULL
        while remaining:
            g = (remaining & -remaining).bit_length() - 1
            c = sum(1 << MUL[g][x] for x in H)
            if c.bit_count() != len(H) or c & remaining != c:
                raise ValueError("cosets not a partition")
            out.append((h, g, c, len(G) // len(H)))
            remaining &= ~c
    return out


def search(cs):
    adj = [0] * len(cs)
    for i in range(len(cs)):
        for j in range(i):
            if not cs[i][2] & cs[j][2] and gcd(cs[i][3], cs[j][3]) <= 7:
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    visits = 0

    def go(selected, candidates):
        nonlocal visits
        visits += 1
        if len(selected) == 8:
            return selected
        if len(selected) + candidates.bit_count() < 8:
            return None
        while candidates:
            low = candidates & -candidates
            i = low.bit_length() - 1
            candidates ^= low
            r = go(selected + [i], candidates & adj[i])
            if r is not None:
                return r
            if len(selected) + candidates.bit_count() < 8:
                break
        return None

    return go([], (1 << len(cs)) - 1), visits


def main():
    hs = subgroups()
    cs = all_cosets(hs)
    print("group_order:", len(G))
    print("subgroup_count:", len(hs))
    print("subgroups_by_order:", dict(sorted(Counter(h.bit_count() for h in hs).items())))
    print("left_coset_count:", len(cs))
    print("cosets_by_index:", dict(sorted(Counter(c[3] for c in cs).items())))
    answer, visits = search(cs)
    print("search_nodes:", visits)
    if answer is not None:
        print("CANDIDATE: independently verify", [cs[i] for i in answer])
        raise SystemExit(1)
    print("RESULT: no eight-coset counterconfiguration in D22")


if __name__ == "__main__":
    main()
