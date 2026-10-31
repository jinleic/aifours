#!/usr/bin/env python3
"""proofF159pa boundary probe (reviewer ReviewF159ProofAttack). Exact, standard library only.

Question: the main candidate (Section 2) describes the imported girth-four certificate as
"Qpol>0, Hpol>0 on all six NONNEGATIVE rates", while the certificate's own argument (parent
disposition) only covers POSITIVE rates (open cube). This probe replays every girth-four leaf
exactly and inspects the vertex Bernstein coefficients at leaf vertices whose coordinates are all
< 1 (finite rates, zero allowed). If all such vertex values are > 0, positivity extends to
[0,inf)^6 by choosing, for each coordinate, the touched endpoint or the lower endpoint (< 1).
Otherwise the zero vertices are reported as points with nonnegative rates where Q or H vanish.
Not used by the main proof (Lemma 1 gives strictly positive rates); documentation of wording scope.
"""
import hashlib, json, math, time
from fractions import Fraction as Fr

P = ('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/'
     'frontier-20261028-ph7-girth4-critical-bernstein-certificate.json')
OUT = ('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/'
       'f159-ph7-eight-ninths-impossibility/proofF159pa-boundary-probe-v1-result.json')
raw = open(P, 'rb').read()
assert hashlib.sha256(raw).hexdigest() == 'b2674b8221205230df969c205c0975486c2079202c896f6d4e37f4c6269e87d8'
C = json.loads(raw)
n = 6


def padd(*ps):
    o = {}
    for p in ps:
        for k, v in p.items():
            o[k] = o.get(k, 0) + v
    return {k: v for k, v in o.items() if v != 0}


def psc(p, c):
    return {k: v * c for k, v in p.items() if v * c != 0}


def pmul(p, q):
    o = {}
    for k1, v1 in p.items():
        for k2, v2 in q.items():
            k = tuple(a + b for a, b in zip(k1, k2))
            o[k] = o.get(k, 0) + v1 * v2
    return {k: v for k, v in o.items() if v != 0}


def var(i):
    e = [0] * n
    e[i] = 1
    return {tuple(e): Fr(1)}


def cst(c):
    return {(0,) * n: Fr(c)}


def esym(vs, k):
    E = [cst(1)] + [{} for _ in range(k)]
    for v in vs:
        for j in range(k, 0, -1):
            E[j] = padd(E[j], pmul(E[j - 1], v))
    return E[k]


u = [var(i) for i in range(n)]
f = [esym(u, k) for k in range(5)]
A = padd(f[2], psc(f[1], -4), cst(Fr(74, 9)))
B = padd(f[3], psc(f[2], -4), psc(f[1], Fr(74, 9)), cst(Fr(-28, 3)))
h0 = padd(f[4], psc(f[2], Fr(-70, 9)), psc(f[1], Fr(212, 9)), cst(Fr(-1007, 27)))
h1 = padd(f[3], psc(f[1], Fr(-70, 9)), cst(Fr(212, 9)))
Q = psc(padd(pmul(A, A), psc(pmul(padd(f[1], cst(-4)), B), -1)), 81)
H = psc(padd(pmul(h0, A), psc(pmul(h1, B), -1)), -243)


def flat(m):
    return sum(a * 3 ** i for i, a in enumerate(m))


def init(Pp):
    T = [0] * 729
    for k, v in Pp.items():
        T[flat(k)] = int(v * 64 / 2 ** sum(1 for a in k if a == 1))
        assert Fr(v * 64, 2 ** sum(1 for a in k if a == 1)).denominator == 1
    return T


BASES = [[b for b in range(729) if (b // 3 ** ax) % 3 == 0] for ax in range(n)]


def split(T, ax):
    st = 3 ** ax
    L = list(T)
    Rr = list(T)
    for b in BASES[ax]:
        b0, b1, b2 = T[b], T[b + st], T[b + 2 * st]
        m = b0 + 2 * b1 + b2
        L[b], L[b + st], L[b + 2 * st] = 4 * b0, 2 * (b0 + b1), m
        Rr[b], Rr[b + st], Rr[b + 2 * st] = m, 2 * (b1 + b2), 4 * b2
    return L, Rr


CORNERS = []
for c in range(64):
    bits = [(c >> i) & 1 for i in range(n)]
    CORNERS.append((bits, flat([2 * x for x in bits])))
out = {}
t0 = time.time()
for name, Pp, key in (('Q', Q, 'Q_positive_compactified_binary_leaf_paths'), ('H', H, 'H_positive_compactified_binary_leaf_paths')):
    leaves = set(C[key])
    pre = {p[:i] for p in leaves for i in range(len(p))}
    stack = [('', init(Pp), [(0, 0)] * n)]
    finite_vertices = 0
    zero_finite = []
    while stack:
        path, T, box = stack.pop()
        if path in leaves:
            assert min(T) >= 0
            for bits, vi in CORNERS:
                # vertex coordinate < 1 for every axis (finite rates; zero rates allowed)
                if all((b == 0) or (k + 1 < 2 ** m) for b, (k, m) in zip(bits, box)):
                    finite_vertices += 1
                    if T[vi] <= 0:
                        coords = [Fr(k + b, 2 ** m) for b, (k, m) in zip(bits, box)]
                        zero_finite.append({'leaf': path, 'x': [str(x) for x in coords],
                                            'rates': [str(x / (1 - x)) for x in coords], 'value': T[vi]})
            continue
        assert path in pre, ('uncovered', path)
        ax = len(path) % n
        L, Rr = split(T, ax)
        k, m = box[ax]
        bl, br = list(box), list(box)
        bl[ax] = (2 * k, m + 1)
        br[ax] = (2 * k + 1, m + 1)
        stack.append((path + '1', Rr, br))
        stack.append((path + '0', L, bl))
    out[name] = {'finite_vertices_checked': finite_vertices, 'nonpositive_finite_vertices': len(zero_finite),
                 'examples': zero_finite[:8]}
    print(name, out[name]['finite_vertices_checked'], out[name]['nonpositive_finite_vertices'], zero_finite[:2], flush=True)
out['interpretation'] = ('if nonpositive_finite_vertices == 0 for Q and H, the leaves also certify strict positivity on '
                         '[0,inf)^6; otherwise the listed points are nonnegative-rate zeros (wording overstatement)')
out['seconds'] = round(time.time() - t0, 2)
open(OUT, 'w').write(json.dumps(out, indent=1, sort_keys=True) + '\n')
print('wrote', OUT)
