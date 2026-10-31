#!/usr/bin/env python3
"""Independent finite checks of the pinned circular Tuscan candidate."""
from collections import Counter
from itertools import combinations, permutations

class Group:
    def __init__(self, elements, product):
        self.el = list(elements)
        self.index = {x: i for i, x in enumerate(self.el)}
        self.n = len(self.el)
        self.mul = [[self.index[product(x, y)] for y in self.el] for x in self.el]
        self.inv = [next(j for j in range(self.n)
                         if self.mul[i][j] == 0 and self.mul[j][i] == 0)
                    for i in range(self.n)]
        assert all(self.mul[0][a] == a and self.mul[a][0] == a for a in range(self.n))
        assert all(self.mul[self.mul[a][b]][c] == self.mul[a][self.mul[b][c]]
                   for a in range(self.n) for b in range(self.n) for c in range(self.n))

    def diff(self, a, b):
        return self.mul[self.inv[a]][b]

    def conj(self, g, p):
        return self.mul[self.mul[g][p]][self.inv[g]]

    def powers(self, g):
        powers = [0]
        cur = self.mul[0][g]
        while cur != 0:
            assert cur not in powers
            powers.append(cur)
            cur = self.mul[cur][g]
        return powers


def regular_row_orbits(group, phi):
    n = group.n
    def norm(row):
        i = row.index(0)
        return row[i:] + row[:i]
    def translate(row, g):
        return norm(tuple(group.mul[g][x] for x in row))
    unseen = {(0,) + p for p in permutations(range(1, n))}
    result = []
    while unseen:
        row = min(unseen)
        orbit = {translate(row, g) for g in range(n)}
        assert orbit <= unseen
        unseen -= orbit
        s = len(orbit)
        delta = [group.diff(row[i], row[(i+1) % n]) for i in range(n)]
        epsilon = [group.diff(row[i], row[(i+2) % n]) for i in range(n)]
        assert all(delta[i] == delta[i % s] and epsilon[i] == epsilon[i % s]
                   for i in range(n))
        assert all(epsilon[i] == group.mul[delta[i]][delta[(i+1) % n]]
                   for i in range(n))
        for step, period in ((1, delta[:s]), (2, epsilon[:s])):
            arcs = Counter((r[i], r[(i+step) % n]) for r in orbit for i in range(n))
            multiplicities = Counter(period)
            assert all(a != b for (a, b) in arcs)
            assert all(arcs[(a, b)] == multiplicities[group.diff(a, b)]
                       for a in range(n) for b in range(n) if a != b)
        mod = max(phi) + 1
        assert sum(phi[e] for e in epsilon[:s]) % mod == (2 * sum(phi[d] for d in delta[:s])) % mod
        result.append((row, s, delta[:s], epsilon[:s]))
    return result


def transfer_check(group, generator):
    pows = group.powers(generator)
    P = set(pows)
    q = len(P)
    assert q >= 2 and q & (q - 1) == 0 and group.n % q == 0 and (group.n // q) % 2 == 1
    normalizer = [g for g in range(group.n) if {group.conj(g, p) for p in P} == P]
    centralizer = [g for g in range(group.n)
                   if all(group.mul[g][p] == group.mul[p][g] for p in P)]
    assert normalizer == centralizer
    reps, representative = [], {}
    for t in range(group.n):
        if t not in representative:
            coset = {group.mul[p][t] for p in P}
            assert not coset.intersection(representative)
            reps.append(t)
            representative.update((v, t) for v in coset)
    assert len(reps) == group.n // q
    transfer = []
    for g in range(group.n):
        acc = 0
        for t in reps:
            tg = group.mul[t][g]
            factor = group.mul[tg][group.inv[representative[tg]]]
            assert factor in P
            acc = group.mul[acc][factor]
        transfer.append(acc)
    assert all(transfer[group.mul[a][b]] == group.mul[transfer[a]][transfer[b]]
               for a in range(group.n) for b in range(group.n))
    assert set(transfer) == P
    assert len([g for g in range(group.n) if transfer[g] == 0]) == group.n // q
    exponent = {v: i for i, v in enumerate(pows)}
    assert exponent[transfer[generator]] % 2 == 1
    phi = [exponent[t] for t in transfer]
    assert all(phi[group.mul[a][b]] == (phi[a] + phi[b]) % q
               for a in range(group.n) for b in range(group.n))
    return phi, len(normalizer), group.n // q

# Literal n=1 edge case: distinct-pair condition, including the distance-2 test.
r = (0, 1)
for step in (1, 2):
    pairs = Counter((r[i], r[(i+step) % 2]) for i in range(2))
    assert all(pairs[(a, b)] <= 1 for a in range(2) for b in range(2) if a != b)
    print('n=1, step', step, 'pairs', sorted(pairs.items()))
shifted = tuple((x + 1) % 2 for x in r)
assert shifted == r[1:] + r[:1]
print('n=1 nontrivial C2 translation is rotation:', shifted)

# C4: enumerate every directed cyclic row, all regular row orbits, and their arc covers.
C4 = Group(range(4), lambda a, b: (a+b) % 4)
phi4, normalizer4, kernel4 = transfer_check(C4, 1)
orbits4 = regular_row_orbits(C4, phi4)
print('C4 row orbits, representatives, sizes, period D1, period D2:')
for row, s, ds, es in orbits4:
    print(' ', row, s, ds, es, 'sums', sum(phi4[d] for d in ds) % 4,
          sum(phi4[e] for e in es) % 4)
assert Counter(s for _, s, _, _ in orbits4) == Counter({1: 2, 4: 1})
three_row_unions = [subset for k in range(len(orbits4)+1)
                    for subset in combinations(orbits4, k)
                    if sum(x[1] for x in subset) == 3]
assert not three_row_unions
s1 = sum(phi4[h] for h in range(1, 4)) % 4
assert s1 == 2 and (2*s1) % 4 == 0
print('C4 hypothetical D1 all-nonidentity sum:', s1,
      'D2 forced sum:', (2*s1) % 4, 'required D2 sum:', s1)
print('C4 invariant 3-row orbit unions:', len(three_row_unions))

# S3: exact nonabelian row orbit and transfer checks; p=3 counterexample to the stated import.
e = (0, 1, 2)
perms = [e] + [x for x in permutations(range(3)) if x != e]
S3 = Group(perms, lambda a, b: tuple(a[b[i]] for i in range(3)))
transposition = next(i for i in range(1, 6) if len(S3.powers(i)) == 2)
phiS3, normalizerS3, kernelS3 = transfer_check(S3, transposition)
orbitsS3 = regular_row_orbits(S3, phiS3)
print('S3 exact row orbit-size frequencies:', sorted(Counter(s for _, s, _, _ in orbitsS3).items()))
print('S3 checked every orbit for D2=D1*shift(D1), full arcs, and projected sums:', len(orbitsS3))
p3 = next(i for i in range(1, 6) if len(S3.powers(i)) == 3)
P3 = set(S3.powers(p3))
N3 = [g for g in range(6) if {S3.conj(g, p) for p in P3} == P3]
assert len(N3) == 6 and any(S3.mul[a][b] != S3.mul[b][a] for a in N3 for b in N3)
subgroups2 = [set(S3.powers(g)) for g in range(1, 6) if len(S3.powers(g)) == 2]
assert len(subgroups2) == 3
assert all(any({S3.conj(g, x) for x in Q} != Q for g in range(6)) for Q in subgroups2)
print('S3 at p=3: cyclic P3, normalizer size', len(N3),
      'nonabelian; normal order-2 subgroups:', 0)

# The group C2 x (C7 semidirect C3) has cyclic Sylow 2 and a nonabelian normalizer.
H42 = Group(((u, a, b) for u in range(2) for a in range(7) for b in range(3)),
            lambda x, y: ((x[0]+y[0]) % 2, (x[1]+(2**x[2])*y[1]) % 7, (x[2]+y[2]) % 3))
z = H42.index[(1, 0, 0)]
_, normalizer42, kernel42 = transfer_check(H42, z)
a, b = H42.index[(0, 1, 0)], H42.index[(0, 0, 1)]
assert H42.mul[a][b] != H42.mul[b][a] and normalizer42 == 42 and kernel42 == 21
print('C2 x (C7 semidirect C3): normalizer size', normalizer42,
      'noncommuting products', H42.el[H42.mul[a][b]], H42.el[H42.mul[b][a]],
      'transfer kernel size', kernel42)

# Dicyclic group Dic_3, order 12, has Sylow C4 and a normal C3 transfer kernel.
Dic3 = Group(((a, b) for a in range(6) for b in range(2)),
             lambda x, y: ((x[0]+((-1)**x[1])*y[0]+3*x[1]*y[1]) % 6, (x[1]+y[1]) % 2))
x = Dic3.index[(0, 1)]
phi12, normalizer12, kernel12 = transfer_check(Dic3, x)
assert len(Dic3.powers(x)) == 4 and kernel12 == 3
sum12 = sum(phi12[h] for h in range(1, 12)) % 4
assert sum12 == 2 and 2*sum12 % 4 == 0
print('Dic3 order 12: Sylow C4, normalizer size', normalizer12,
      'transfer kernel size', kernel12, 'all-nonidentity projected sum', sum12)
print('All exact independent checks passed.')
