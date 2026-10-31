#!/usr/bin/env python3
"""Reviewer-authored per-leaf DIRECT exact replay for the f180 certificate.

usage: reviewer-f180-replay.py COVER POLY SHARD NSHARDS [ZNUM ZDEN] [CERTPATH]

COVER in {QO, HO, NB, MC, residual}; POLY a selector polynomial name (NB/MC),
or 'ALL' (QO/HO/residual).  For every leaf whose label needs POLY (rules
written from the packet text, NOT read from the certificate), the Bernstein
coefficients of POLY on that leaf's box are computed directly from the
monomial form: per axis an integer matrix (blossom / Taylor shift +
monomial->Bernstein conversion, positive scalings only) is applied to the
global coefficient tensor; leaves sharing per-axis intervals share partial
mode products (trie over axes 0..5), but no parent-box Bernstein tensor or
de Casteljau subdivision of the author is used.  Exact integers only.
Writes reviewer-f180-out-<COVER>-<POLY>-<SHARD>of<NSHARDS>[-z..].json.
"""
import sys, os, json, time, hashlib, importlib.util
from fractions import Fraction as Fr
sys.dont_write_bytecode = True
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
def _load(name, fn):
    spec = importlib.util.spec_from_file_location(name, os.path.join(HERE, fn))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
L = _load('rlib', 'reviewer-f180-lib.py')
RD = _load('rdefs', 'reviewer-f180-defs.py')
CERT_DEFAULT = '/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/phase-type/frontier-20261029-ph7-threshold-z3-certificate-v1.json'

# rules written from the packet text (Lemma C3 / addendum section 6)
NB_RULES = {'unsorted': (), 'F': ('F',), 'A': ('A',), 'Q': ('Q',), 'E4v6': ('mA', 'mE46'),
            'Y2v6': ('mA', 'mG6', 'mD6'), 'Y2tan': ('mA', 'Fm', 'mGq', 'T2'),
            'Y2E': ('mA', 'mGE', 'mDE'), 'Disc': ('mA', 'mDl')}
NB_NONSTRICT = {('Y2v6', 'mD6'), ('Y2E', 'mDE')}
MC_RULES = {'unsorted': (), 'mA': ('mA',), 'D': ('D',), 'H': ('H',), 'Y1end': ('A', 'mD', 'c2', 'mendL', 'mendH')}
N_BOX = (Fr(11, 21), Fr(37, 27)); M_BOX = (Fr(7, 9), Fr(5, 3))
N_CUBE = (Fr(11, 32), Fr(37, 64)); M_CUBE = (Fr(7, 16), Fr(5, 8))

def tensor(P, degs):
    arr = np.zeros([d + 1 for d in degs], dtype=object)
    for k, v in P.items():
        arr[k] = int(v)
    return arr

def apply_axis(T, M, axis):
    R = np.tensordot(M, T, axes=([1], [axis]))
    return np.moveaxis(R, 0, axis)

def trie(T0, items, naxes, matfn, leaffn):
    """items: list of (path, intervals); every leaf gets the tensor obtained by applying
    matfn(axis, interval) on every axis to T0."""
    def rec(level, T, group):
        if level == naxes:
            assert len(group) == 1, 'two leaves with one box'
            leaffn(group[0], T); return
        buckets = {}
        for it in group:
            buckets.setdefault(it[1][level], []).append(it)
        for iv in sorted(buckets):
            rec(level + 1, apply_axis(T, matfn(level, iv), level), buckets[iv])
    rec(0, T0, items)

def affine_to_s(P, lo, hi, nv):
    W = hi - lo
    T = {k: Fr(v) for k, v in P.items()}
    for ax in range(nv):
        NT = {}
        for key, val in T.items():
            kk = key[ax]
            for j in range(kk + 1):
                nk = key[:ax] + (j,) + key[ax + 1:]
                NT[nk] = NT.get(nk, 0) + val * L.math.comb(kk, j) * lo ** (kk - j) * W ** j
        T = L.clean(NT)
    Ti, _ = L.integerize(T)
    return Ti

def compact_general_matrix(d, n, l):
    """compactified axis of degree d: column i = s^i (1-s)^(d-i) in monomial form, then
    shift+convert to the dyadic interval (positive scaling)."""
    G = [[((-1) ** (m - i)) * L.math.comb(d - i, m - i) if m >= i else 0 for i in range(d + 1)] for m in range(d + 1)]
    return L.matmul(L.leaf_matrix(d, n, l), G)

def shard_items(items, shard, nshards):
    """distribute axis-0 buckets greedily (largest first) over shards"""
    buckets = {}
    for it in items:
        buckets.setdefault(it[1][0], []).append(it)
    loads = [0] * nshards; assign = {}
    for key in sorted(buckets, key=lambda k: (-len(buckets[k]), k)):
        s = min(range(nshards), key=lambda i: (loads[i], i)); assign[key] = s; loads[s] += len(buckets[key])
    return [it for it in items if assign[it[1][0]] == shard]

def main():
    t_start = time.time()
    cover, poly, shard, nshards = sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4])
    zval = Fr(83, 100); ztag = ''
    if len(sys.argv) >= 7:
        zval = Fr(int(sys.argv[5]), int(sys.argv[6])); ztag = '-z%sover%s' % (sys.argv[5], sys.argv[6])
    certpath = sys.argv[7] if len(sys.argv) >= 8 else CERT_DEFAULT
    raw = open(certpath, 'rb').read()
    cert = json.loads(raw.decode('utf-8'))
    out = {'cover': cover, 'poly': poly, 'shard': shard, 'nshards': nshards, 'z': str(zval),
           'cert_sha256': hashlib.sha256(raw).hexdigest(), 'results': {}}
    leaves = cert[cover]['leaves']
    if cover in ('QO', 'HO'):
        Qpol, Hpol = RD.compact_polys(zval)
        P, _ = L.integerize(Qpol if cover == 'QO' else Hpol)
        cube = N_CUBE if cover == 'QO' else M_CUBE
        degs = [2] * 6
        items = [(p, L.path_intervals(p, 6), lab) for p, lab in leaves]
        items = shard_items(items, shard, nshards)
        res = out['results']
        posit = []
        for p, ivs, lab in items:
            if lab == 'R':
                inside = all(cube[0] <= Fr(n, 1 << l) and Fr(n + 1, 1 << l) <= cube[1] for (n, l) in ivs)
                res[p] = ['R', inside, '']
            elif lab == 'pos':
                posit.append((p, ivs))
            else:
                res[p] = [lab, False, 'unknown label']
        mats = {}
        def matfn(ax, iv):
            if iv not in mats:
                mats[iv] = np.array(L.compact_axis_matrix(iv[0], iv[1]), dtype=object)
            return mats[iv]
        def leaffn(it, T):
            p, ivs = it
            ok = len(p) >= 6 and T.min() >= 0
            ncorner = 0
            if ok:
                for corner in L.itertools.product((0, 1), repeat=6):
                    coords = [Fr(ivs[j][0] + corner[j], 1 << ivs[j][1]) for j in range(6)]
                    if all(0 < c < 1 for c in coords):
                        ncorner += 1
                        if not T[tuple(2 * c for c in corner)] > 0:
                            ok = False; break
                ok = ok and ncorner > 0
            res[p] = ['pos', bool(ok), 'corners=%d' % ncorner]
        trie(tensor(P, degs), posit, 6, matfn, leaffn)
    elif cover in ('NB', 'MC'):
        nb, mc, _ = RD.selector_polys(zval)
        polys = nb if cover == 'NB' else mc
        rules = NB_RULES if cover == 'NB' else MC_RULES
        lo, hi = N_BOX if cover == 'NB' else M_BOX
        P, _ = L.integerize(polys[poly])
        Ps = affine_to_s(P, lo, hi, 6)
        degs = [L.deg_in(Ps, i) for i in range(6)]
        need = [(p, L.path_intervals(p, 6)) for p, lab in leaves if poly in rules[lab]]
        items = shard_items(need, shard, nshards)
        mats = {}
        def matfn(ax, iv):
            key = (degs[ax], iv)
            if key not in mats:
                mats[key] = np.array(L.leaf_matrix(degs[ax], iv[0], iv[1]), dtype=object)
            return mats[key]
        res = out['results']
        def leaffn(it, T):
            mn = T.min()
            res[it[0]] = [poly, (mn > 0) - (mn < 0), int(mn).bit_length()]
        trie(tensor(Ps, degs), items, 6, matfn, leaffn)
        out['degs'] = degs
    elif cover == 'residual':
        rp = RD.residual_polys(zval)
        res = out['results']
        items_all = [(p, L.path_intervals(p, 3), lab) for p, lab in leaves]
        items_all = shard_items(items_all, shard, nshards)
        name_of = {'Abar<=0': 'Abar', 'Dbar<=0': 'Dbar', 'f1-4<0': 'f1minus4'}
        for nm in ('Abar', 'Dbar', 'f1minus4'):
            P, _ = L.integerize(rp[nm])
            degs = [L.deg_in(P, i) for i in range(3)]
            mats = {}
            def matfn(ax, iv, degs=degs, mats=mats):
                key = (ax, iv)
                if key not in mats:
                    if ax == 1:
                        M = L.leaf_matrix(degs[1], iv[0], iv[1])          # tau: ordinary Bernstein
                    else:
                        M = compact_general_matrix(degs[ax], iv[0], iv[1])  # y, gam compactified
                    mats[key] = np.array(M, dtype=object)
                return mats[key]
            items = [(p, ivs) for p, ivs, lab in items_all if name_of.get(lab) == nm]
            def leaffn(it, T, nm=nm):
                mx = T.max()
                ok = (mx <= 0) if nm in ('Abar', 'Dbar') else (mx < 0)
                res[it[0]] = [nm, bool(ok), (mx > 0) - (mx < 0)]
            trie(tensor(P, degs), items, 3, matfn, leaffn)
        for p, ivs, lab in items_all:
            if lab not in name_of:
                res[p] = [lab, False, 'unknown label']
    else:
        raise SystemExit('unknown cover')
    out['n_results'] = len(out['results'])
    out['seconds'] = round(time.time() - t_start, 2)
    fn = os.path.join(HERE, 'reviewer-f180-out-%s-%s-%dof%d%s.json' % (cover, poly, shard, nshards, ztag))
    if len(sys.argv) >= 8:
        fn = fn[:-5] + '-altcert.json'
    with open(fn, 'w') as fh:
        json.dump(out, fh, separators=(',', ':'), sort_keys=True)
    bad = [p for p, r in out['results'].items() if (r[1] is False) or (r[1] in (-1,))]
    print('cover', cover, 'poly', poly, 'shard', shard, '/', nshards, 'z', zval, 'checked', out['n_results'],
          'seconds', out['seconds'], 'nonpositive/failed (pre-merge)', len(bad), 'out', os.path.basename(fn))

if __name__ == '__main__':
    main()
