#!/usr/bin/env python3
"""Reviewer-authored positive and intended-reason negative controls for f180.
Uses only the reviewer engine (reviewer-f180-lib/defs/replay); the certificate is
parsed in full and modified IN MEMORY only.  Each control prints its expected and
observed outcome and the reason string; exit 0 iff every control behaves as intended."""
import sys, os, json, hashlib, time, importlib.util
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
L = _load('rlib', 'reviewer-f180-lib.py'); RD = _load('rdefs', 'reviewer-f180-defs.py'); R = _load('rrep', 'reviewer-f180-replay.py')
CERT = R.CERT_DEFAULT
T0 = time.time(); Z3 = Fr(83, 100)
raw = open(CERT, 'rb').read(); cert = json.loads(raw.decode('utf-8'))
print('cert sha256', hashlib.sha256(raw).hexdigest())
nb, mc, aux = RD.selector_polys(Z3)
Qpol, Hpol = RD.compact_polys(Z3); rp = RD.residual_polys(Z3)
results = []
def record(name, expected_fail, observed_fail, reason):
    good = expected_fail == observed_fail
    results.append(good)
    print('%-4s %-70s expected=%s observed=%s | %s' % ('OK' if good else 'BAD', name, 'FAIL' if expected_fail else 'PASS',
                                                     'FAIL' if observed_fail else 'PASS', reason))

def sorted_signs(P, box, paths):
    Pi, _ = L.integerize(P); Ps = R.affine_to_s(Pi, box[0], box[1], 6)
    degs = [L.deg_in(Ps, i) for i in range(6)]; out = {}; mats = {}
    def matfn(ax, iv):
        k = (degs[ax], iv)
        if k not in mats: mats[k] = np.array(L.leaf_matrix(degs[ax], iv[0], iv[1]), dtype=object)
        return mats[k]
    def leaffn(it, T):
        mn = T.min(); out[it[0]] = (mn > 0) - (mn < 0)
    R.trie(R.tensor(Ps, degs), [(p, L.path_intervals(p, 6)) for p in paths], 6, matfn, leaffn)
    return out

def compact_pos(P, paths):
    Pi, _ = L.integerize(P); out = {}; mats = {}
    def matfn(ax, iv):
        if iv not in mats: mats[iv] = np.array(L.compact_axis_matrix(iv[0], iv[1]), dtype=object)
        return mats[iv]
    def leaffn(it, T):
        p, ivs = it; good = len(p) >= 6 and T.min() >= 0; nc = 0
        for corner in L.itertools.product((0, 1), repeat=6):
            co = [Fr(ivs[j][0] + corner[j], 1 << ivs[j][1]) for j in range(6)]
            if all(0 < c < 1 for c in co):
                nc += 1; good = good and T[tuple(2 * c for c in corner)] > 0
        out[p] = good and nc > 0
    R.trie(R.tensor(Pi, [2] * 6), [(p, L.path_intervals(p, 6)) for p in paths], 6, matfn, leaffn)
    return out

def inside(cube, p):
    return all(cube[0] <= Fr(n, 1 << l) and Fr(n + 1, 1 << l) <= cube[1] for n, l in L.path_intervals(p, 6))

def resid_max_sign(P, paths):
    Pi, _ = L.integerize(P); degs = [L.deg_in(Pi, i) for i in range(3)]; out = {}; mats = {}
    def matfn(ax, iv):
        k = (ax, iv)
        if k not in mats:
            mats[k] = np.array(L.leaf_matrix(degs[1], iv[0], iv[1]) if ax == 1 else R.compact_general_matrix(degs[ax], iv[0], iv[1]), dtype=object)
        return mats[k]
    def leaffn(it, T):
        mx = T.max(); out[it[0]] = (mx > 0) - (mx < 0)
    R.trie(R.tensor(Pi, degs), [(p, L.path_intervals(p, 3)) for p in paths], 3, matfn, leaffn)
    return out

def by_label(cov, lab, k):
    return [p for p, l in cert[cov]['leaves'] if l == lab][:k]

# ---- N1/N2: coverage negatives (dropped, duplicated, overlapping leaf) + positive ----
for cov in ('QO', 'HO', 'NB', 'MC', 'residual'):
    paths = [p for p, _ in cert[cov]['leaves']]
    okc, info = L.coverage_proof(paths)
    record('P  coverage %s (unmodified)' % cov, False, not okc, info)
    for idx in (0, len(paths) // 2, len(paths) - 1):
        okc, info = L.coverage_proof(paths[:idx] + paths[idx + 1:])
        record('N1 %s drop leaf #%d' % (cov, idx), True, not okc, info)
    okc, info = L.coverage_proof(paths + [paths[len(paths) // 3]])
    record('N2 %s duplicate leaf' % cov, True, not okc, info)
    okc, info = L.coverage_proof(paths + [paths[len(paths) // 3] + '0'])
    record('N2 %s add overlapping child of a leaf' % cov, True, not okc, info)

# ---- P/N3/N4 on NB ----
qs = by_label('NB', 'Q', 40); ts = by_label('NB', 'Y2tan', 40); us = by_label('NB', 'unsorted', 40); es = by_label('NB', 'E4v6', 40)
NBOX = R.N_BOX; MBOX = R.M_BOX
s = sorted_signs(nb['Q'], NBOX, qs); record('P  NB 40 Q leaves as Q', False, any(v <= 0 for v in s.values()), 'min Q coefficient >0 on all')
s = sorted_signs(nb['A'], NBOX, qs); nf = sum(v <= 0 for v in s.values())
record('N3 NB 40 Q leaves relabelled A (need A>0)', True, nf > 0, '%d/40 leaves have a Bernstein coefficient of A <= 0' % nf)
def unsorted_box(p):
    ivs = L.path_intervals(p, 6); lo = [Fr(n, 1 << l) for n, l in ivs]; hi = [Fr(n + 1, 1 << l) for n, l in ivs]
    return any(lo[i] > hi[j] for i in range(6) for j in range(i + 1, 6))
nf = sum(not unsorted_box(p) for p in qs)
record('N3 NB 40 Q leaves relabelled unsorted', True, nf > 0, '%d/40 boxes contain sorted points (no lo_i>hi_j)' % nf)
nf = sum(not unsorted_box(p) for p in us)
record('P  NB 40 unsorted leaves as unsorted', False, nf > 0, '%d/40 not unsorted' % nf)
ss = {k: sorted_signs(nb[k], NBOX, ts) for k in ('mA', 'Fm', 'mGq', 'T2')}
bad = sum(any(ss[k][p] <= 0 for k in ss) for p in ts)
record('P  NB 40 Y2tan leaves as Y2tan', False, bad > 0, '%d/40 fail' % bad)
sd = sorted_signs(nb['mDl'], NBOX, ts); nf = sum(sd[p] <= 0 for p in ts)
record('N3 NB 40 Y2tan leaves relabelled Disc (need -disc>0)', True, nf > 0, '%d/40 have a coefficient of -disc <= 0' % nf)
sn = sorted_signs(L.pscale(nb['T2'], -1), NBOX, ts); nf = sum(sn[p] <= 0 for p in ts)
record('N4 NB wrong-sign polynomial -T2 on 40 Y2tan leaves', True, nf > 0, '%d/40 have min coefficient <= 0' % nf)
sn = sorted_signs(L.pscale(nb['mE46'], -1), NBOX, es); nf = sum(sn[p] <= 0 for p in es)
record('N4 NB wrong-sign polynomial +E4(v6) on 40 E4v6 leaves', True, nf > 0, '%d/40 have min coefficient <= 0' % nf)
# ---- MC ----
hs = by_label('MC', 'H', 40); ys = by_label('MC', 'Y1end', 40)
sm = {k: sorted_signs(mc[k], MBOX, ys) for k in ('A', 'mD', 'c2', 'mendL', 'mendH')}
bad = sum(any(sm[k][p] <= 0 for k in sm) for p in ys)
record('P  MC 40 Y1end leaves as Y1end', False, bad > 0, '%d/40 fail' % bad)
sh = {k: sorted_signs(mc[k], MBOX, hs) for k in ('A', 'mD', 'c2', 'mendL', 'mendH')}
nf = sum(any(sh[k][p] <= 0 for k in sh) for p in hs)
record('N3 MC 40 H leaves relabelled Y1end', True, nf > 0, '%d/40 fail some Y1end tensor' % nf)
sn = sorted_signs(L.pscale(mc['mendH'], -1), MBOX, ys); nf = sum(sn[p] <= 0 for p in ys)
record('N4 MC wrong-sign polynomial +D^2 Y1+(-E/D) on 40 Y1end leaves', True, nf > 0, '%d/40 have min coefficient <= 0' % nf)
# ---- QO/HO ----
pq = by_label('QO', 'pos', 40); rq = by_label('QO', 'R', 40)
cp = compact_pos(Qpol, pq); record('P  QO 40 pos leaves', False, not all(cp.values()), 'corner/nonneg rule')
nf = sum(not inside(R.N_CUBE, p) for p in pq)
record('N3 QO 40 pos leaves relabelled R', True, nf > 0, '%d/40 boxes not inside [11/32,37/64]^6' % nf)
nf = sum(not inside(R.N_CUBE, p) for p in rq)
record('P  QO 40 R leaves inside cube', False, nf > 0, '%d/40 outside' % nf)
cn = compact_pos(L.pscale(Qpol, -1), pq); nf = sum(not v for v in cn.values())
record('N4 QO wrong-sign polynomial -Qpol on 40 pos leaves', True, nf > 0, '%d/40 fail' % nf)
rh = by_label('HO', 'R', 40); ch = compact_pos(Hpol, rh); nf = sum(not v for v in ch.values())
record('N3 HO 40 R leaves relabelled pos', True, nf > 0, '%d/40 fail the positivity rule (Hpol not certified inside M^6)' % nf)
# ---- residual ----
ab = [p for p, l in cert['residual']['leaves'] if l == 'Abar<=0'][:40]; db = [p for p, l in cert['residual']['leaves'] if l == 'Dbar<=0'][:40]
sA = resid_max_sign(rp['Abar'], ab); record('P  residual 40 Abar<=0 leaves', False, any(v > 0 for v in sA.values()), 'max coefficient <= 0')
sD = resid_max_sign(rp['Abar'], db); nf = sum(v > 0 for v in sD.values())
record('N3 residual 40 Dbar<=0 leaves relabelled Abar<=0', True, nf > 0, '%d/40 have a positive Abar coefficient' % nf)
sN = resid_max_sign(L.pscale(rp['Abar'], -1), ab); nf = sum(v > 0 for v in sN.values())
record('N4 residual wrong-sign polynomial -Abar on 40 Abar<=0 leaves', True, nf > 0, '%d/40 have a positive coefficient' % nf)
print('controls behaving as intended: %d/%d' % (sum(results), len(results)), round(time.time() - T0, 1), 's')
sys.exit(0 if all(results) else 1)
