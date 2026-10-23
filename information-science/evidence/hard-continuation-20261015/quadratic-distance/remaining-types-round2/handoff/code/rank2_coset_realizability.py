#!/usr/bin/env python3
"""Exact per-coset (h, Lambda) realizability for type (2,192) at z = 8.

A D=1 coset function is E_c = x0x1x2 + q + (affine). Here x0x1x2 is the cubic
part of 1_Z for the linear zero 3-flat Z = {x0=x1=x2=0}. L_c is any ell-subset.
Then Lambda(kappa) = sum_{k in L_c} (-1)^{E_c(k)+kappa.k} and
h = (-3 W_{E_c} + 4 Lambda)/16, which must be an integer with |h| <= 4.

Proved-complete parametrization:
  * the affine stabilizer of the cubic form x0x1x2 acts on the 2^15 quadratic
    parts. Label propagation shows it has exactly six orbits, one per Walsh
    class;
  * affine terms of E_c and the stabilizer action change (h, Lambda) only by
    a kappa-permutation and a joint sign (h, Lambda) -> (-h, -Lambda) per kappa,
    so the sign-normalized histogram is invariant;
  * for one representative per orbit, every ell-subset of F_2^6 (ell = 2, 4)
    is enumerated.
Refuses to overwrite its output.
"""
import itertools, json, os, sys, time
from collections import Counter
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'results', 'rank2-coset-realizability.json')


def need(cond, label):
    if not cond:
        raise ValueError('check failed: ' + label)


BITS = np.array([[(x >> i) & 1 for i in range(6)] for x in range(64)], dtype=np.int64)
QUADS = [(i, j) for i in range(6) for j in range(i + 1, 6)]


def anf(tt):
    a = tt.copy()
    for i in range(6):
        s = 1 << i
        a = a.reshape(a.shape[:-1] + (-1, 2, s))
        a[..., 1, :] ^= a[..., 0, :]
        a = a.reshape(a.shape[:-3] + (64,))
    return a


def tt_of_q(q):
    q = np.asarray(q, dtype=np.int64)
    vals = np.zeros((len(q), 64), dtype=np.int64)
    for b, (i, j) in enumerate(QUADS):
        vals ^= ((q >> b) & 1)[:, None] * (BITS[:, i] & BITS[:, j])[None, :]
    return vals ^ (BITS[:, 0] & BITS[:, 1] & BITS[:, 2])[None, :]


def fwht_rows(signs):
    W = signs.copy()
    h = 1
    while h < 64:
        W = W.reshape(W.shape[0], -1, 2 * h)
        a = W[:, :, :h].copy()
        b = W[:, :, h:].copy()
        W[:, :, :h] = a + b
        W[:, :, h:] = a - b
        W = W.reshape(W.shape[0], 64)
        h *= 2
    return W


def main():
    if os.path.exists(OUT):
        print('refusing to overwrite', OUT)
        sys.exit(2)
    t0 = time.time()
    allq = np.arange(1 << 15)
    TT = tt_of_q(allq)
    I = [1 << i for i in range(6)]

    def sub(i, v):
        r = I.copy()
        r[i] = v
        return r
    G = [([1 << 1, 1 << 0] + I[2:], 0), ([1 << 1, 1 << 2, 1 << 0] + I[3:], 0),
         (I[:3] + [1 << 4, 1 << 3] + I[5:], 0), (I[:3] + [1 << 4, 1 << 5, 1 << 3], 0),
         (sub(0, 3), 0), (sub(3, (1 << 3) | (1 << 4)), 0), (sub(3, (1 << 3) | 1), 0)]
    G += [(I, 1 << i) for i in range(6)]
    imgs = []
    for rows, t in G:
        y = np.zeros(64, dtype=np.int64)
        for i in range(6):
            y |= ((np.array([bin(x & rows[i]).count('1') & 1 for x in range(64)]) ^ ((t >> i) & 1)) << i)
        co = anf(TT[:, y])
        need(np.all(co[:, 7] == 1), 'cubic part keeps x0x1x2')
        need(np.all(co[:, [m for m in range(64) if bin(m).count('1') >= 3 and m != 7]] == 0), 'no other cubic/quartic')
        qp = np.zeros(1 << 15, dtype=np.int64)
        for b, (i, j) in enumerate(QUADS):
            qp |= co[:, (1 << i) | (1 << j)] << b
        imgs.append(qp)
    lab = np.arange(1 << 15)
    while True:
        old = lab.copy()
        for img in imgs:
            np.minimum.at(lab, img, lab.copy())
            lab = np.minimum(lab, lab[img])
        lab = lab[lab]
        if np.array_equal(lab, old):
            break
    reps, cnt = np.unique(lab, return_counts=True)
    W = fwht_rows(1 - 2 * TT)
    hk = [tuple(sorted(Counter(np.abs(r).tolist()).items())) for r in W]
    need(len(reps) == 6, 'six orbits')
    for r in reps:
        members = np.nonzero(lab == r)[0]
        need(len({hk[m] for m in members}) == 1, 'orbit has one Walsh class')
    need(len({hk[r] for r in reps}) == 6, 'distinct classes per orbit')
    KAP = np.array([[1 - 2 * (bin(k & kap).count('1') & 1) for kap in range(64)] for k in range(64)], dtype=np.int64)
    combos = {ell: np.array(list(itertools.combinations(range(64), ell)), dtype=np.int64) for ell in (2, 4)}
    classes = []
    for r, c in zip(reps, cnt):
        E = TT[r]
        w = W[r]
        C = KAP * (1 - 2 * E)[:, None]
        entry = {'rep_q': int(r), 'orbit_size': int(c), 'hist': [list(p) for p in hk[r]]}
        for ell in (2, 4):
            found = Counter()
            nvalid = 0
            cb = combos[ell]
            for s in range(0, len(cb), 50000):
                ch = cb[s:s + 50000]
                Lam = C[ch].sum(1)
                num = -3 * w[None, :] + 4 * Lam
                ok = np.all(num % 16 == 0, axis=1) & np.all(np.abs(num) <= 64, axis=1)
                if not ok.any():
                    continue
                Hs = num[ok] // 16
                Ls = Lam[ok]
                nvalid += int(ok.sum())
                neg = (Hs < 0) | ((Hs == 0) & (Ls < 0))
                Hn = np.where(neg, -Hs, Hs)
                Ln = np.where(neg, -Ls, Ls)
                for hh, ll in zip(Hn, Ln):
                    found[tuple(sorted(Counter(zip(hh.tolist(), ll.tolist())).items()))] += 1
            entry['ell%d' % ell] = {'valid_sets': nvalid,
                                    'hists': [{'hist': [[list(p), n] for p, n in k], 'count': v} for k, v in sorted(found.items())]}
        classes.append(entry)
    out = {'classes': classes, 'seconds': time.time() - t0}
    with open(OUT, 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps([(e['hist'], e['ell2']['valid_sets'], e['ell4']['valid_sets'], len(e['ell4']['hists'])) for e in classes]))


if __name__ == '__main__':
    main()
