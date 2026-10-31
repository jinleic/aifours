#!/usr/bin/env python3
"""Reviewer control of the trie bookkeeping in reviewer-f180-replay.py: for every
(cover, polynomial) output file of the main batch, re-derive the recorded verdict of
up to 25 randomly chosen leaves WITHOUT the trie (global tensor -> per-axis leaf
matrices applied one leaf at a time) and require identical sign data; also checks
that a deliberately mis-assigned box (the leaf's sibling) changes at least one
verdict-relevant number somewhere (negative case)."""
import sys, os, json, random, time, importlib.util
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
L = _load('rlib', 'reviewer-f180-lib.py'); RD = _load('rdefs', 'reviewer-f180-defs.py'); R = _load('rrep', 'reviewer-f180-replay.py')
T0 = time.time(); Z3 = Fr(83, 100); rng = random.Random(77)
rec = json.load(open(os.path.join(HERE, 'reviewer-f180-receipts-main.json')))
nb, mc, aux = RD.selector_polys(Z3); Qpol, Hpol = RD.compact_polys(Z3); rp = RD.residual_polys(Z3)

def direct(T00, ivs, matfn):
    T = T00
    for ax in range(T.ndim):
        T = R.apply_axis(T, matfn(ax, ivs[ax]), ax)
    return T

def sib(p):
    return p[:-1] + ('1' if p[-1] == '0' else '0')

agree = 0; total = 0; sibdiff = 0; sibtot = 0
for j in rec['jobs']:
    o = json.load(open(os.path.join(HERE, j['out_file'])))
    cov, poly = o['cover'], o['poly']
    keys = sorted(o['results']); sample = rng.sample(keys, min(25, len(keys)))
    if not sample:
        continue
    if cov in ('NB', 'MC'):
        P, _ = L.integerize((nb if cov == 'NB' else mc)[poly]); box = R.N_BOX if cov == 'NB' else R.M_BOX
        Ps = R.affine_to_s(P, box[0], box[1], 6); degs = [L.deg_in(Ps, i) for i in range(6)]; T00 = R.tensor(Ps, degs)
        matfn = lambda ax, iv: np.array(L.leaf_matrix(degs[ax], iv[0], iv[1]), dtype=object)
        def verdict(p):
            T = direct(T00, L.path_intervals(p, 6), matfn); mn = T.min()
            return [poly, (mn > 0) - (mn < 0), int(mn).bit_length()]
    elif cov in ('QO', 'HO'):
        P, _ = L.integerize(Qpol if cov == 'QO' else Hpol); T00 = R.tensor(P, [2] * 6)
        matfn = lambda ax, iv: np.array(L.compact_axis_matrix(iv[0], iv[1]), dtype=object)
        def verdict(p):
            if o['results'][p][0] == 'R':
                return o['results'][p]
            ivs = L.path_intervals(p, 6); T = direct(T00, ivs, matfn); ok = len(p) >= 6 and T.min() >= 0; nc = 0
            if ok:
                for corner in L.itertools.product((0, 1), repeat=6):
                    co = [Fr(ivs[k][0] + corner[k], 1 << ivs[k][1]) for k in range(6)]
                    if all(0 < c < 1 for c in co):
                        nc += 1
                        if not T[tuple(2 * c for c in corner)] > 0:
                            ok = False; break
                ok = ok and nc > 0
            return ['pos', bool(ok), 'corners=%d' % nc]
    else:
        def verdict(p):
            nm = o['results'][p][0]; P, _ = L.integerize(rp[nm]); degs = [L.deg_in(P, i) for i in range(3)]
            mf = lambda ax, iv: np.array(L.leaf_matrix(degs[1], iv[0], iv[1]) if ax == 1 else R.compact_general_matrix(degs[ax], iv[0], iv[1]), dtype=object)
            T = direct(R.tensor(P, degs), L.path_intervals(p, 3), mf); mx = T.max()
            ok = (mx <= 0) if nm in ('Abar', 'Dbar') else (mx < 0)
            return [nm, bool(ok), (mx > 0) - (mx < 0)]
    for p in sample:
        total += 1; agree += verdict(p) == o['results'][p]
    if cov in ('NB', 'MC'):
        for p in sample[:5]:
            sibtot += 1; sibdiff += verdict(sib(p)) != o['results'][p]
print('trie verdicts reproduced without trie: %d/%d sampled leaves' % (agree, total))
print('negative: sibling box gives a different (sign, bit-length) record for %d/%d sampled NB/MC leaves' % (sibdiff, sibtot))
print('seconds', round(time.time() - T0, 1))
sys.exit(0 if agree == total and sibdiff > 0 else 1)
