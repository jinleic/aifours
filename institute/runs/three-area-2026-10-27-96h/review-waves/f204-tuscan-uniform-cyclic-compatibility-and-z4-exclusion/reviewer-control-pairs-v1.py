#!/usr/bin/env python3
"""Bounded, independent positive/negative two-cycle-orbit diagnostics."""
from collections import defaultdict
from itertools import combinations, permutations


def shift(x, q, r, t):
    return ((x // r + t) % q) * r + x % r


def canon(c):
    i = c.index(0)
    return c[i:] + c[:i]


def actual_events(cycles):
    triples = []
    for c in cycles:
        n = len(c)
        triples += [(c[j], c[(j+1)%n], c[(j+2)%n]) for j in range(n)]
    return triples


def cut_ok(triples, u):
    pairs = [(x, z) for x, y, z in triples if u not in (x, y, z)]
    return len(pairs) == len(set(pairs))


def local_ok(records, q, r):
    groups = defaultdict(list)
    O = {t*r for t in range(q)}
    for kind, mid in records:
        groups[kind].append(mid)
    for (a,b,d), mids in groups.items():
        for (h,c), (j,e) in combinations(mids, 2):
            if not O <= {a,d*r+b,h*r+c,j*r+e}:
                return False
    return True


def run(n, q):
    r = n//q
    orbits = []
    for perm in permutations(range(1,n)):
        c = (0,)+perm
        images = sorted({canon(tuple(shift(x,q,r,t) for x in c)) for t in range(q)})
        if c != images[0]:
            continue
        L = n // (q//len(images))
        d1 = [(c[j]%r, c[(j+1)%n]%r,
               (c[(j+1)%n]//r-c[j]//r)%q) for j in range(L)]
        if len(d1) != len(set(d1)):
            continue
        d2 = [((c[j]%r,c[(j+2)%n]%r,
                (c[(j+2)%n]//r-c[j]//r)%q),
               ((c[(j+1)%n]//r-c[j]//r)%q,c[(j+1)%n]%r))
              for j in range(L)]
        orbits.append((c, set(d1), d2, images))
    counts = {True: 0, False: 0}
    witnesses = {}
    pairs_scanned = 0
    for left, right in combinations(orbits, 2):
        pairs_scanned += 1
        if left[1] & right[1]:
            continue
        records = left[2]+right[2]
        events = actual_events(left[3]+right[3])
        arcs = [(x,y) for x,y,z in events]
        if len(arcs) != len(set(arcs)):
            raise AssertionError('disjoint type sets yet repeated concrete D1 arc')
        if len(records) != len(set(records)):
            raise AssertionError('disjoint D1 sets yet repeated aligned triple')
        local = local_ok(records,q,r)
        direct = [cut_ok(events,t*r) for t in range(q)]
        if any(v != local for v in direct):
            raise AssertionError('two-orbit cut/compatibility disagreement')
        counts[local] += 1
        witnesses.setdefault(local,(left[0],right[0]))
        if min(counts.values()) >= 25:
            break
    if min(counts.values()) < 25:
        raise AssertionError(f'insufficient positive/negative pairs q={q}: {counts}')
    print(f'PAIR n={n} q={q} valid_orbits={len(orbits)} pairs_scanned={pairs_scanned} '
          f'disjoint_positive={counts[True]} disjoint_negative={counts[False]} '
          f'positive_witness={witnesses[True]} negative_witness={witnesses[False]}')


for n,q in ((8,2),(9,3),(8,4)):
    run(n,q)
print('PAIR CONTROL COMPLETED')
