#!/usr/bin/env python3
"""Summarise HIT lines of kblock_exact_v2 by (F, kappa, weight multiset w.r.t. the most frequent nonzero value g, and the
run-position pattern of non-g elements).  Weight of value v: the odd a in [1, 2p-1] with a*g = v mod p.
Usage: hit_types_v1.py p FILE"""
import collections, sys
p, f = int(sys.argv[1]), sys.argv[2]
c = collections.Counter(); thin = collections.Counter()
for line in open(f):
    if not line.startswith('HIT'):
        continue
    parts = dict(t.split('=', 1) for t in line.split()[1:])
    F = int(parts['F'])
    runs = [[int(x) for x in r.split(',')] for r in parts['runs'].split('|')]
    k = len(runs)
    tot = [sum(r[v] for r in runs) for v in range(p)]
    g = max(range(1, p), key=lambda v: tot[v])
    wt = {v: next(a for a in range(1, 2 * p, 2) if (a * g - v) % p == 0) for v in range(p)}
    ws = collections.Counter()
    for v in range(p):
        if tot[v]:
            ws[wt[v]] += tot[v]
    H = (F - k) // 2
    c[(F, p - 1 - H, tuple(sorted(ws.items())))] += 1
    for r in runs:
        heavy = [wt[v] for v in range(p) if r[v] and wt[v] not in (1, 2 * p - 1)]
        if heavy:
            thin[('heavy_run', tuple(sorted(heavy)), 'g_in_run', r[g], 'minus_in_run', r[(-g) % p])] += 1
for k_, v_ in sorted(c.items()):
    print('type', k_, v_)
for k_, v_ in sorted(thin.items()):
    print('heavy-run', k_, v_)
