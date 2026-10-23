#!/usr/bin/env python3
"""Compute Aut(G) by brute force on a generating set, and its orbits on G.

Input: table file written by groups.py.  Output JSON: automorphism count,
orbits (list of lists, ordered by min element), orbit index per element,
and the full list of automorphisms (as permutations of element indices).
Every automorphism is checked to be a bijective homomorphism on the WHOLE
table (not only on generators).
"""
import itertools
import json
import sys


def read_table(path):
    with open(path) as f:
        n = int(f.readline())
        tab = [list(map(int, f.readline().split())) for _ in range(n)]
    return n, tab


def element_orders(n, tab):
    ords = []
    for g in range(n):
        x, k = g, 1
        while x != 0:
            x, k = tab[x][g], k + 1
        ords.append(k)
    return ords


def gen_closure(n, tab, gens):
    seen = {0}
    frontier = [0]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = tab[x][g]
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    return seen


def small_generating_set(n, tab):
    # greedy: add the element enlarging the generated subgroup most
    gens = []
    cur = {0}
    while len(cur) < n:
        best = max(range(n), key=lambda g: len(gen_closure(n, tab, gens + [g])))
        gens.append(best)
        cur = gen_closure(n, tab, gens)
    # try to find a 2-generator set if greedy gave more
    if len(gens) > 2:
        for a, b in itertools.combinations(range(1, n), 2):
            if len(gen_closure(n, tab, [a, b])) == n:
                return [a, b]
    return gens


def words_for_all(n, tab, gens):
    """For every element, a word (list of generator positions) expressing it."""
    word = {0: []}
    frontier = [0]
    while frontier:
        nxt = []
        for x in frontier:
            for gi, g in enumerate(gens):
                y = tab[x][g]
                if y not in word:
                    word[y] = word[x] + [gi]
                    nxt.append(y)
        frontier = nxt
    return word


def automorphisms(n, tab):
    ords = element_orders(n, tab)
    gens = small_generating_set(n, tab)
    word = words_for_all(n, tab, gens)
    cands = [[h for h in range(n) if ords[h] == ords[g]] for g in gens]
    auts = []
    for imgs in itertools.product(*cands):
        phi = [None] * n
        ok = True
        for x in range(n):
            y = 0
            for gi in word[x]:
                y = tab[y][imgs[gi]]
            phi[x] = y
        if len(set(phi)) != n:
            continue
        for a in range(n):
            pa = phi[a]
            ra = tab[a]
            for b in range(n):
                if phi[ra[b]] != tab[pa][phi[b]]:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            auts.append(phi)
    return gens, auts


def main():
    path, out = sys.argv[1], sys.argv[2]
    n, tab = read_table(path)
    gens, auts = automorphisms(n, tab)
    orbit_of = [-1] * n
    orbits = []
    for g in range(n):
        if orbit_of[g] >= 0:
            continue
        orb = sorted({phi[g] for phi in auts})
        for h in orb:
            orbit_of[h] = len(orbits)
        orbits.append(orb)
    inv = [next(h for h in range(n) if tab[g][h] == 0) for g in range(n)]
    res = {'n': n, 'generators': gens, 'aut_order': len(auts), 'orbits': orbits,
           'orbit_of': orbit_of, 'inverse': inv, 'element_orders': element_orders(n, tab),
           'automorphisms': auts}
    with open(out, 'w') as f:
        json.dump(res, f)
    print(f"n={n} |Aut|={len(auts)} orbits={len(orbits)} sizes={[len(o) for o in orbits]}")


if __name__ == '__main__':
    main()
