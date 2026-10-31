#!/usr/bin/env python3
"""Reviewer control of the reviewer per-leaf engine itself (exact rationals):
for sampled leaves, the Bernstein form built from the engine's per-leaf tensor,
evaluated at random rational points t of the unit box, must equal ONE POSITIVE
constant times the polynomial evaluated directly at the mapped point (u=x/(1-x)
compactified with the prod(1-x)^deg factor; v=lo+(hi-lo)s affine).  Negative
case: the same test against a perturbed polynomial must fail."""
import sys, os, json, random, time, math, importlib.util, itertools
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
L = _load('rlib', 'reviewer-f180-lib.py'); RD = _load('rdefs', 'reviewer-f180-defs.py'); R = _load('rrep', 'reviewer-f180-replay.py')
T0 = time.time(); Z3 = Fr(83, 100); rng = random.Random(4242)
cert = json.loads(open(R.CERT_DEFAULT, 'rb').read().decode('utf-8'))
nb, mc, aux = RD.selector_polys(Z3); Qpol, Hpol = RD.compact_polys(Z3); rp = RD.residual_polys(Z3)

def ev(P, pt):
    s = Fr(0)
    for k, v in P.items():
        t = Fr(v)
        for e, a in zip(k, pt):
            if e: t *= a ** e
        s += t
    return s

def bern_eval(T, t):
    n = T.ndim; tot = Fr(0)
    for idx in itertools.product(*[range(s) for s in T.shape]):
        c = T[idx]
        if c == 0: continue
        b = Fr(1)
        for j in range(n):
            d = T.shape[j] - 1
            b *= math.comb(d, idx[j]) * t[j] ** idx[j] * (1 - t[j]) ** (d - idx[j])
        tot += c * b
    return tot

def leaf_tensor(T0_, ivs, matfn):
    T = T0_
    for ax in range(T.ndim):
        T = R.apply_axis(T, matfn(ax, ivs[ax]), ax)
    return T

def run_case(name, P, paths, kind, box=None, perturb=False, npts=3):
    Pi, _ = L.integerize(P); nv = 3 if kind == 'resid' else 6
    Ptest = L.padd(Pi, L.const(1, nv)) if perturb else Pi      # perturbed polynomial for the negative case
    if kind == 'affine':
        Ps = R.affine_to_s(Pi, box[0], box[1], 6); degs = [L.deg_in(Ps, i) for i in range(6)]
        mat = lambda ax, iv: np.array(L.leaf_matrix(degs[ax], iv[0], iv[1]), dtype=object); T00 = R.tensor(Ps, degs)
    elif kind == 'compact':
        degs = [2] * 6; mat = lambda ax, iv: np.array(L.compact_axis_matrix(iv[0], iv[1]), dtype=object); T00 = R.tensor(Pi, degs)
    else:
        degs = [L.deg_in(Pi, i) for i in range(3)]
        mat = lambda ax, iv: np.array(L.leaf_matrix(degs[1], iv[0], iv[1]) if ax == 1 else R.compact_general_matrix(degs[ax], iv[0], iv[1]), dtype=object)
        T00 = R.tensor(Pi, degs)
    good = True
    for p in paths:
        ivs = L.path_intervals(p, nv); T = leaf_tensor(T00, ivs, mat); ratios = []
        for _ in range(npts):
            t = [Fr(rng.randint(1, 996), 997) for _ in range(nv)]                      # strictly inside (0,1)
            g = [Fr(ivs[j][0], 1 << ivs[j][1]) + t[j] / (1 << ivs[j][1]) for j in range(nv)]   # global unit-cube coordinate
            if kind == 'affine':
                val = ev(Ptest, [box[0] + (box[1] - box[0]) * gj for gj in g])
            elif kind == 'compact':
                if any(gj >= 1 for gj in g): continue
                val = ev(Ptest, [gj / (1 - gj) for gj in g]) * math.prod((1 - gj) ** 2 for gj in g)
            else:
                if g[0] >= 1 or g[2] >= 1: continue
                val = ev(Ptest, [g[0] / (1 - g[0]), g[1], g[2] / (1 - g[2])]) * (1 - g[0]) ** degs[0] * (1 - g[2]) ** degs[2]
            bv = bern_eval(T, t)
            if val == 0:
                good &= bv == 0; continue
            ratios.append(bv / val)
        good &= len(ratios) > 0 and len(set(ratios)) == 1 and ratios[0] > 0
    return good

res = []
def rec(name, expect_ok, got_ok):
    res.append(expect_ok == got_ok)
    print('%-3s %-62s expected=%s observed=%s' % ('OK' if expect_ok == got_ok else 'BAD', name, 'consistent' if expect_ok else 'inconsistent', 'consistent' if got_ok else 'inconsistent'))
pick = lambda cov, lab, k: rng.sample([p for p, l in cert[cov]['leaves'] if l == lab], k)
cases = [('QO pos leaves, Qpol', Qpol, pick('QO', 'pos', 12), 'compact', None),
         ('HO pos leaves, Hpol', Hpol, pick('HO', 'pos', 12), 'compact', None),
         ('NB Q leaves, Q', nb['Q'], pick('NB', 'Q', 10), 'affine', R.N_BOX),
         ('NB Y2tan leaves, T2', nb['T2'], pick('NB', 'Y2tan', 4), 'affine', R.N_BOX),
         ('NB Y2v6 leaves, mG6', nb['mG6'], pick('NB', 'Y2v6', 6), 'affine', R.N_BOX),
         ('MC Y1end leaves, mendH', mc['mendH'], pick('MC', 'Y1end', 2), 'affine', R.M_BOX),
         ('residual Dbar leaves, Dbar', rp['Dbar'], pick('residual', 'Dbar<=0', 12), 'resid', None),
         ('residual Abar leaves, Abar', rp['Abar'], pick('residual', 'Abar<=0', 12), 'resid', None)]
for name, P, paths, kind, box in cases:
    rec('P ' + name, True, run_case(name, P, paths, kind, box))
    rec('N ' + name + ' vs P+1', False, run_case(name, P, paths[:2], kind, box, perturb=True))
print('engine consistency controls as intended: %d/%d' % (sum(res), len(res)), round(time.time() - T0, 1), 's')
sys.exit(0 if all(res) else 1)
