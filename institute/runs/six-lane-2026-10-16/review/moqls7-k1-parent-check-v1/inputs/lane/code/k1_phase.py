#!/usr/bin/env python3
"""k1_phase.py: exact phase system for the equianharmonic K1 weight-4 pattern. Lane moqls7-maximum.

Under the weight-4 pattern every row transition is a unitary whose support is exactly a circulant (7,4,2)
difference-set pattern, so (lemma: log-magnitude system has nullity 1) every pattern coefficient has modulus 1/2.
Write psi_p = (1/2) sum_{k in A(p)} exp(2 pi i theta[p,k]) e_k. Orthogonality of two collinear points p, q whose
supports share s coordinates is a vanishing sum of s unit complex numbers u_k = exp(2 pi i (theta[q,k]-theta[p,k])):
  s = 2: u_{k2} = -u_{k1}             (theta-relation with constant 1/2);
  s = 3: {u_k} = u * {1, w, w^2}      (two branches sigma in {1,2}: d_{k2}-d_{k1} = sigma/3, d_{k3}-d_{k1} = 2sigma/3).
This module builds the integer relation matrix (rows over unknowns theta[p,k]) and the rational right-hand sides.
"""
import collections
import itertools
import json
from fractions import Fraction


def load(classfile, idx, models, mi):
    net = [tuple(q) for q in json.load(open(classfile))["classes"][idx]["net"]]
    model = json.load(open(models))["models"][mi]
    S = collections.defaultdict(set)
    for s in model:
        p, k = map(int, s.split(":"))
        S[p].add(k)
    return net, S


def relations(net, S):
    lines = [[q for q in range(49) if net[q][c] == b] for c in range(4) for b in range(7)]
    row0 = set(lines[0])
    var = {}
    for p in sorted(S):
        if p in row0:
            continue
        for k in sorted(S[p]):
            var[(p, k)] = len(var)
    two, three = [], []
    for l in lines:
        for p, q in itertools.combinations(l, 2):
            if p in row0 or q in row0:
                continue
            ov = sorted(S[p] & S[q])
            if len(ov) == 2:
                k1, k2 = ov
                # d_k = theta[q,k] - theta[p,k];  d_k2 - d_k1 = 1/2
                two.append(({var[(q, k2)]: 1, var[(p, k2)]: -1, var[(q, k1)]: -1, var[(p, k1)]: 1}, Fraction(1, 2)))
            elif len(ov) == 3:
                k1, k2, k3 = ov
                r1 = {var[(q, k2)]: 1, var[(p, k2)]: -1, var[(q, k1)]: -1, var[(p, k1)]: 1}
                r2 = {var[(q, k3)]: 1, var[(p, k3)]: -1, var[(q, k1)]: -1, var[(p, k1)]: 1}
                three.append((r1, r2, (p, q, ov)))
            elif len(ov) == 0:
                continue
            else:
                raise ValueError("unexpected overlap %d" % len(ov))
    return var, two, three


class Eq:
    """sum coef[v]*theta[v] == half/2 + (sum_t sig[t]*sigma_t)/3  (mod 1); half in Z/2, sig[t] in Z/3."""
    __slots__ = ("coef", "half", "sig")

    def __init__(self, coef, half, sig):
        self.coef = {v: c for v, c in coef.items() if c}
        self.half = half % 2
        self.sig = {t: s % 3 for t, s in sig.items() if s % 3}

    def axpy(self, m, other):
        """self + m*other (m integer)."""
        coef = dict(self.coef)
        for v, c in other.coef.items():
            coef[v] = coef.get(v, 0) + m * c
        sig = dict(self.sig)
        for t, s in other.sig.items():
            sig[t] = sig.get(t, 0) + m * s
        return Eq(coef, self.half + m * other.half, sig)


def build_equations(two, three):
    eqs = []
    for coef, rhs in two:
        assert rhs == Fraction(1, 2)
        eqs.append(Eq(coef, 1, {}))
    for t, (r1, r2, _) in enumerate(three):
        eqs.append(Eq(r1, 0, {t: 1}))      # d_k2 - d_k1 = sigma_t/3
        eqs.append(Eq(r2, 0, {t: 2}))      # d_k3 - d_k1 = 2 sigma_t/3
    return eqs


def eliminate(eqs):
    """Unimodular elimination with unit pivots. Returns (conditions, leftover, pivots):
    conditions = equations with no theta left (each says half == 0 mod 2 and sig.sigma == 0 mod 3);
    leftover = equations still containing theta but without unit coefficients (empty if fully eliminated)."""
    active = list(eqs)
    conditions, pivots = [], []
    occ = collections.defaultdict(set)
    for i, e in enumerate(active):
        for v in e.coef:
            occ[v].add(i)
    alive = set(range(len(active)))
    while True:
        best = None
        for i in alive:
            e = active[i]
            if not e.coef:
                continue
            for v, c in e.coef.items():
                if abs(c) == 1:
                    cost = (len(occ[v]), len(e.coef))
                    if best is None or cost < best[0]:
                        best = (cost, i, v)
        if best is None:
            break
        _, i, v = best
        piv = active[i]
        c = piv.coef[v]
        alive.discard(i)
        for v2 in piv.coef:
            occ[v2].discard(i)
        pivots.append((v, piv))
        for j in list(occ[v]):
            e = active[j]
            m = -e.coef[v] * c          # c = +-1 so c*c = 1
            new = e.axpy(m, piv)
            for v2 in e.coef:
                occ[v2].discard(j)
            active[j] = new
            for v2 in new.coef:
                occ[v2].add(j)
            assert v not in new.coef
    leftover = []
    for i in sorted(alive):
        e = active[i]
        if e.coef:
            leftover.append(e)
        else:
            conditions.append(e)
    return conditions, leftover, pivots
