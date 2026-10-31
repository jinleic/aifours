from itertools import combinations, product
from time import monotonic
start = monotonic()
def require(ok, msg):
  if not ok:
    raise RuntimeError(msg)
def guard():
  require(monotonic() - start < 55, 'cooperative deadline exceeded')
V = tuple(range(1, 5))
pairs = list(combinations(V, 2))
B = (0, 5)
def independent(S):
  return len(S) == 4 and all(len({(w[a], w[b]) for w in S}) == 4 for a, b in combinations(range(3), 2))
triples = list(product(range(2), repeat=3))
good = set()
for S in combinations(triples, 4):
  guard()
  if independent(S):
    good.add(frozenset(S))
expected = {frozenset(w for w in triples if sum(w) % 2 == c) for c in range(2)}
require(good == expected, 'local parity classification')
for c in product(range(2), repeat=4):
  guard()
  C = sum(c) % 2
  v = tuple(x ^ C for x in c)
  require(all((c[i] ^ (sum(v[k] for k in range(4) if k != i) % 2)) == 0 for i in range(4)), 'simultaneous parity normalization')
def eps(p):
  return sum(p[a] > p[b] for a in range(4) for b in range(a + 1, 4)) % 2
def f(i, j, a):
  k, l = [x for x in V if x not in (i, j)]
  return l if a == k else k if a == l else a
def t(i, a, k):
  return int(a not in (i, k))
def proj(w, p):
  return tuple(w[x - 1] for x in p)
M = {(i, j): {(a, f(i, j, a)) for a in V} for i, j in pairs}
R = {p: set(product(V, repeat=2)) - M[p] for p in pairs}
for i, j in pairs:
  k, l = [x for x in V if x not in (i, j)]
  actual = {(a, b) for a, b in product(V, repeat=2) if (t(i, a, k) ^ t(j, b, k)) == 1 and (t(i, a, l) ^ t(j, b, l)) == 1}
  require(actual == M[(i, j)], 'canonical matching characterization')
P = []
for i, j in pairs:
  guard()
  k, l = [x for x in V if x not in (i, j)]
  e = eps((i, j, k, l))
  for a in V:
    w = [None] * 4
    w[i - 1] = a
    w[j - 1] = f(i, j, a)
    w[k - 1] = B[t(i, a, k) ^ e]
    w[l - 1] = B[t(i, a, l) ^ e ^ 1]
    P.append(tuple(w))
def valid_p(Q, rs):
  universe = set(product(range(6), repeat=2))
  return len(Q) == 24 and len(set(Q)) == 24 and all(len({proj(w, p) for w in Q}) == 24 and {proj(w, p) for w in Q} == universe - rs[p] for p in pairs)
require(valid_p(P, R), 'common P and all six complements')
require(all(sum(x in V for x in w) == 2 for w in P), 'P has exactly two internal coordinates')
def compatible(w, rs):
  return all(proj(w, p) in rs[p] for p in pairs)
Cands = set()
for w in product(V, repeat=4):
  guard()
  if compatible(w, R):
    Cands.add(w)
I = V
def swap(i, j):
  w = list(V)
  w[i - 1], w[j - 1] = w[j - 1], w[i - 1]
  return tuple(w)
for i, j in pairs:
  k, l = [x for x in V if x not in (i, j)]
  require({w for w in Cands if proj(w, (i, j)) == (i, j)} == {I, swap(k, l)}, 'forced residual fiber')
T12, T34 = swap(1, 2), swap(3, 4)
F = {I, T12, T34}
D = (2, 1, 4, 3)
require(F <= Cands, 'forced three corners are compatible')
require(proj(D, (1, 3)) in M[(1, 3)], 'fourth corner forbidden in pair13')
def cut_closed(S, p):
  q = tuple(x for x in V if x not in p)
  rows, cols = {}, {}
  for w in S:
    r, c = proj(w, p), proj(w, q)
    rows.setdefault(r, set()).add(c)
    cols.setdefault(c, set()).add(r)
  return bool(S) and all(len(cs) == 2 for cs in rows.values()) and all(len(rs) == 2 for rs in cols.values()) and all(rows[r2] == cs for cs in rows.values() for c in cs for r2 in cols[c])
require(cut_closed(F | {D}, (1, 2)), 'positive complete rectangle control')
H = ((1, 1), (1, -1))
require(all(sum(H[r][c] * H[s][c] for c in range(2)) == (2 if r == s else 0) for r, s in product(range(2), repeat=2)), 'positive exact Hadamard Gram control')
neg = []
def reject(ok, label):
  require(not ok, 'negative control unexpectedly accepted: ' + label)
  neg.append(label)
reject(valid_p(P[:-1] + [P[0]], R), 'duplicate maximal word')
badR = dict(R)
badR[(1, 3)] = set(product(V, repeat=2)) - {(a, a) for a in V}
reject(valid_p(P, badR), 'incorrect missing matching')
badC = Cands - {T34}
reject({w for w in badC if proj(w, (1, 2)) == (1, 2)} == {I, T34}, 'missing forced extension')
reject(compatible(D, R), 'forbidden fourth corner')
reject(cut_closed(F, (1, 2)), 'three-corner nonrectangle')
reject(independent(((0, 0, 0), (0, 0, 1), (1, 1, 0), (1, 1, 1))), 'non-Latin local triples')
require(len(neg) == 6, 'negative control count')
guard()
print('PASS: canonical common P/all six complements; local normal form; forced fibers; forbidden rectangle; P words=', len(P), '; compatible residual words=', len(Cands), '; intended negative controls=', len(neg))
