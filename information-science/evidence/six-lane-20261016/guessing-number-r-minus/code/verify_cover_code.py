"""Brute-force verification of the fractional clique cover strategy on R^- with alphabet s=8 (=F_2^3).

Vertex v holds one bit per cover clique containing it (each vertex lies in exactly 3 of the 10 BCDRV
cliques).  Winning set C = {assignments: XOR of the three bits of every cover clique is 0}, |C| = 2^20.
Check: (i) |C| = 2^20 by enumeration of free bits; (ii) for every codeword and every vertex v, the
strategy 'my bit for clique K = XOR of the K-bits of the other two members' (all seen by v) returns the
true value; (iii) FD form: no two codewords agree on N(v) and differ at v.  Hence gn(R^-,8) >= log_8 2^20 = 20/3.
"""
import sys, os, json
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from graphs import R_MINUS_EDGES, adjacency

cover = [(1,2,3),(1,4,5),(1,6,7),(2,3,9),(2,7,10),(3,8,9),(4,5,10),(4,8,10),(5,6,9),(6,7,8)]
nb = adjacency(R_MINUS_EDGES)
for K in cover:
    for a in K:
        for b in K:
            assert a == b or b in nb[a]
slots = {}  # (vertex, clique index) -> bit position
for ki, K in enumerate(cover):
    for v in K:
        slots[(v, ki)] = len(slots)
assert len(slots) == 30 and all(sum(1 for (v, k) in slots if v == u) == 3 for u in range(1, 11))
# free bits: for each clique, its first two members' bits are free; the third is their XOR
free = [(K[0], ki) for ki, K in enumerate(cover)] + [(K[1], ki) for ki, K in enumerate(cover)]
M = 1 << 20
idx = np.arange(M, dtype=np.int64)
bits = np.zeros((M, 30), dtype=np.uint8)
for j, s in enumerate(free):
    bits[:, slots[s]] = (idx >> j) & 1
for ki, K in enumerate(cover):
    bits[:, slots[(K[2], ki)]] = bits[:, slots[(K[0], ki)]] ^ bits[:, slots[(K[1], ki)]]
# vertex symbols in {0..7}: bits ordered by clique index
vals = np.zeros((M, 10), dtype=np.int64)
for v in range(1, 11):
    ks = sorted(k for (u, k) in slots if u == v)
    for t, k in enumerate(ks):
        vals[:, v - 1] |= bits[:, slots[(v, k)]].astype(np.int64) << t
assert len(np.unique(vals @ (8 ** np.arange(10)))) == M  # distinct codewords
ok_strategy = True
for v in range(1, 11):
    ks = sorted(k for (u, k) in slots if u == v)
    guess = np.zeros(M, dtype=np.int64)
    for t, k in enumerate(ks):
        others = [u for u in cover[k] if u != v]
        g = bits[:, slots[(others[0], k)]] ^ bits[:, slots[(others[1], k)]]
        guess |= g.astype(np.int64) << t
    ok_strategy &= bool(np.array_equal(guess, vals[:, v - 1]))
ok_fd = True
for v in range(1, 11):
    nbr = sorted(nb[v])
    key = np.zeros(M, dtype=np.int64)
    for u in nbr: key = key * 8 + vals[:, u - 1]
    order = np.argsort(key, kind="stable")
    ks, xs = key[order], vals[order, v - 1]
    same = ks[1:] == ks[:-1]
    ok_fd &= not bool(np.any(same & (xs[1:] != xs[:-1])))
out = dict(alphabet=8, codewords=M, strategy_correct_on_all=ok_strategy, functional_dependency_ok=ok_fd,
           implied_lower_bound="gn(R^-,8) >= log_8(2^20) = 20/3")
print(json.dumps(out))
if not (ok_strategy and ok_fd): sys.exit(1)
