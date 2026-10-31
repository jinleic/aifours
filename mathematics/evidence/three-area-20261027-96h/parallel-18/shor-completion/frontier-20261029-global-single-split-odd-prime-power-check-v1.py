#!/usr/bin/env python3
"""Integer-only finite controls for the same-named global written proposition.

No prior checker outputs are loaded. All scientific arithmetic here uses
Python integers, math.gcd and math.isqrt. These are finite controls, not an
all-order proof or an independent-model-family verification.
"""
import json
from itertools import combinations
from math import gcd, isqrt

A = (0, 3, 8, 11)
Y = (0, 1, 7, 13, 14)
OUT = {}


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def primes_upto(n):
    return [p for p in range(2, n + 1)
            if all(p % d != 0 for d in range(2, isqrt(p) + 1))]


# Prime-list control uses a separately constructed integer sieve.
sieve = [True] * 201
sieve[0] = sieve[1] = False
for d in range(2, 201):
    if sieve[d]:
        for multiple in range(d * d, 201, d):
            sieve[multiple] = False
assert primes_upto(200) == [p for p in range(201) if sieve[p]]
OUT['integer_prime_lists_agree'] = True

# Universal gcd transport identity: g0=gcd(y,R), g0|h|R implies
# gcd((h/g0)*y,R)=h.  All residues of the named nonsquarefree R are checked.
transport_count = 0
Rs = (45, 105, 165, 225, 315, 495, 825, 1155, 1815, 2145, 5445)
for R in Rs:
    for y in range(R):
        g0 = gcd(y, R)
        for h in divisors(R):
            if h % g0 == 0:
                assert gcd((h // g0) * y, R) == h
                transport_count += 1
OUT['gcd_transport'] = {'R_values': Rs, 'identities': transport_count}

# Stabilizer of any nonempty proper E in a finite cyclic group.
stabilizer_count = 0
for R in (3, 5, 7, 9, 15):
    full = (1 << R) - 1
    for mask in range(1, full):
        def fixes(shift):
            return (((mask << shift) | (mask >> (R - shift))) & full) == mask
        pi = next(s for s in range(1, R + 1) if fixes(s))
        assert R % pi == 0
        for h in divisors(R):
            assert fixes(h) == (h % pi == 0)
        for r in range(R):
            assert bool(mask >> r & 1) == bool(mask >> (r % pi) & 1)
        stabilizer_count += 1
OUT['cyclic_stabilizer_partitions'] = stabilizer_count


def coordinate_groups(R, moduli):
    return [list(range(c, R, m)) for m in moduli for c in range(m)]


def agreement_graph_connected(mask, R, groups):
    """Opposite colours with a shared residue coordinate are adjacent."""
    parent = list(range(R))

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    for members in groups:
        colour = (mask >> members[0]) & 1
        if any(((mask >> r) & 1) != colour for r in members):
            leader = root(members[0])
            for r in members[1:]:
                parent[root(r)] = leader
    return len({root(r) for r in range(R)}) == 1


def lifted_mask(base_mask, period, R):
    return sum(((base_mask >> (r % period)) & 1) << r for r in range(R))


# G1: three-coordinate agreement graph, colouring independent of an entire
# prime-power CRT coordinate. Exhaustive small analogues, not all R of theorem.
g1 = []
for R, free_power, moduli in ((30, 2, (2, 3, 5)),
                              (30, 3, (2, 3, 5)),
                              (30, 5, (2, 3, 5)),
                              (60, 4, (2, 3, 5))):
    base = R // free_power
    assert gcd(base, free_power) == 1
    groups = coordinate_groups(R, moduli)
    count = 0
    for mask in range(1, (1 << base) - 1):
        assert agreement_graph_connected(lifted_mask(mask, base, R), R, groups)
        count += 1
    g1.append({'R': R, 'free_power': free_power, 'partitions': count})
OUT['G1_exhaustive_analogues'] = g1
# Two coordinates do NOT suffice for G1: five disconnected components.
assert not agreement_graph_connected(lifted_mask(1, 3, 15), 15,
                                      coordinate_groups(15, (3, 5)))
OUT['G1_two_coordinate_negative_control'] = 'disconnected as required'

# G2: pi-periodic colour with gcd(pi,w)=1. Add edges for agreement mod w
# and on either of two coprime coordinates dividing pi. Include R>pi*w.
g2 = []
for pi, w, R, base_axes in ((6, 5, 30, (2, 3)),
                            (6, 5, 60, (2, 3)),
                            (15, 7, 105, (3, 5))):
    assert gcd(pi, w) == 1 and R % (pi * w) == 0
    groups = coordinate_groups(R, base_axes + (w,))
    count = 0
    for mask in range(1, (1 << pi) - 1):
        assert agreement_graph_connected(lifted_mask(mask, pi, R), R, groups)
        count += 1
    g2.append({'pi': pi, 'w': w, 'R': R, 'partitions': count})
OUT['G2_exhaustive_analogues'] = g2
assert not agreement_graph_connected(1, 15, coordinate_groups(15, (3, 5, 3)))
OUT['G2_coprimality_negative_control'] = 'disconnected when pi=15,w=3,E={0}'

# General nonsquarefree-R collision arithmetic, independent of graph controls.
collision_count = 0
for R in (165, 495, 825, 1815, 2145):
    for p in (7, 13, 17):
        if R % p == 0:
            continue
        for exponent in (1, 2):
            rho = p ** exponent
            for j in range(1, 2 * R, 2):
                y = rho * j
                g0 = gcd(y, R)
                for h in divisors(R):
                    if h % g0 == 0:
                        t = h // g0
                        assert gcd(t, 2 * p) == 1
                        for K in (1, 3):
                            n = (1 << K) * rho * R
                            assert gcd(t * y, n) == rho * h
                            # h is odd and gcd(h,R)=h; x=h suffices for identity.
                            assert gcd(rho * h, n) == rho * h
                            collision_count += 1
OUT['general_cross_collision_identities'] = collision_count

# Final gcd fact from p0=0 mod pi and rho, with 165|pi|R.
final_count = 0
for R in (165, 495, 825, 1815, 2145):
    for pi in divisors(R):
        if pi % 165:
            continue
        for p in (7, 13, 17):
            if R % p == 0:
                continue
            for exponent in (1, 2):
                rho = p ** exponent
                for j in range(1, 12, 2):
                    p0 = rho * pi * j
                    y = 8 - p0
                    w = gcd(y, R)
                    assert y % 2 == 1 and gcd(y, p) == 1 and gcd(w, pi) == 1
                    final_count += 1
OUT['final_step_coprimality_cases'] = final_count

# Small exhaustive tiling controls of the parity dichotomy. No author data read.
def tiling(S, T, N):
    return len(S) * len(T) == N and len({(s + t) % N for s in S for t in T}) == N


def complements(V, N):
    answers = set()
    def extend(covered, chosen):
        if len(covered) == N:
            answers.add(tuple(sorted(chosen)))
            return
        c = next(x for x in range(N) if x not in covered)
        for v in V:
            p0 = (c - v) % N
            tile = {(p0 + w) % N for w in V}
            if not (tile & covered):
                extend(covered | tile, chosen + (p0,))
    extend(set(V), (0,))
    return sorted(answers)


dichotomy = {}
for K in (1, 2):
    N = 7 * (1 << K)
    count = 0
    for b in range(K + 1):
        for rest in combinations(range(1, N), (1 << b) - 1):
            V = (0,) + rest
            for P in complements(V, N):
                assert tiling(P, V, N)
                V7 = {7 * v % N for v in V}
                assert len(V7) == len(V) and tiling(P, V7, N)
                for gamma in range(7):
                    Pg = {x for x in P if x % 7 == gamma}
                    AP = {x % (1 << K) for x in Pg}
                    BV = {x % (1 << K) for x in V7}
                    assert len(AP) == len(Pg) and len(BV) == len(V7)
                    assert tiling(AP, BV, 1 << K)
                    assert (len({x % 2 for x in Pg}) == 2) != (len({x % 2 for x in V}) == 2)
                count += 1
    dichotomy[N] = count
OUT['dichotomy_exhaustive_small_tilings'] = dichotomy
OUT['result'] = 'PASS'
if __name__ == '__main__':
    print(json.dumps(OUT, indent=1, sort_keys=True))
