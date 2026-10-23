#!/usr/bin/env python3
"""Exhaustive Walsh classes of six-variable cubics, by cubic part.

Producer for remaining-types-round2, type (2,192).

1. GL(6,2) orbits on cubic forms RM(3,6)/RM(2,6) (2^20 forms), computed by
   label propagation along three generators of GL(6,2).
2. For each orbit representative C, all 2^15 quadratic completions C+q
   (q in the span of the 15 quadratic monomials). Affine terms only permute
   and negate Walsh values, so this enumerates every function with cubic
   part C up to that action. The |W| histogram of each completion is recorded.
3. The cubic part of 1_Z for an 8-point linear zero flat (x0x1x2) is
   treated separately, with all 2^15 completions listed.

The output is a table. The independent audit recomputes it from scratch.
Refuses to overwrite its output.
"""
import json, os, sys, time, hashlib
from collections import Counter
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'results', 'rank2-cubic-classes.json')

def need(cond, label):
    if not cond:
        raise ValueError('check failed: ' + label)

CUBS = [(i, j, k) for i in range(6) for j in range(i + 1, 6) for k in range(j + 1, 6)]
QUADS = [(i, j) for i in range(6) for j in range(i + 1, 6)]
CIDX = {m: n for n, m in enumerate(CUBS)}
BITS = np.array([[(x >> i) & 1 for i in range(6)] for x in range(64)], dtype=np.int64)


def cubic_image(mat):
    """Columns of the induced linear map on cubic forms (mod RM(2,6)).

    mat[i] is the bitmask of the linear form substituted for x_i."""
    cols = []
    for (i, j, k) in CUBS:
        img = 0
        for a in range(6):
            if not (mat[i] >> a) & 1:
                continue
            for b in range(6):
                if not (mat[j] >> b) & 1:
                    continue
                for c in range(6):
                    if not (mat[k] >> c) & 1:
                        continue
                    s = {a, b, c}
                    if len(s) == 3:
                        img ^= 1 << CIDX[tuple(sorted(s))]
        cols.append(img)
    return cols


def apply_cols(cols, states):
    img = np.zeros_like(states)
    for b, col in enumerate(cols):
        img ^= ((states >> b) & 1) * col
    return img


def orbits():
    n = 1 << 20
    states = np.arange(n, dtype=np.int64)
    gens = []
    cyc = [1 << ((i + 1) % 6) for i in range(6)]          # x_i -> x_{i+1}
    swp = [1 << 1, 1 << 0] + [1 << i for i in range(2, 6)]  # swap x0,x1
    trv = [(1 << 0) | (1 << 1)] + [1 << i for i in range(1, 6)]  # x0 -> x0+x1
    for m in (cyc, swp, trv):
        img = apply_cols(cubic_image(m), states)
        need(len(np.unique(img)) == n, 'generator acts bijectively')
        gens.append(img)
    lab = states.copy()
    it = 0
    while True:
        it += 1
        old = lab.copy()
        for img in gens:
            np.minimum.at(lab, img, lab.copy())
            lab = np.minimum(lab, lab[img])
        lab = lab[lab]
        lab = lab[lab]
        if np.array_equal(lab, old):
            break
    reps, counts = np.unique(lab, return_counts=True)
    return [(int(r), int(c)) for r, c in zip(reps, counts)], it


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


def completions(cubic_mask):
    cub = np.zeros(64, dtype=np.int64)
    for n, (i, j, k) in enumerate(CUBS):
        if (cubic_mask >> n) & 1:
            cub ^= BITS[:, i] & BITS[:, j] & BITS[:, k]
    q = np.arange(1 << 15, dtype=np.int64)
    vals = np.zeros((1 << 15, 64), dtype=np.int64)
    for b, (i, j) in enumerate(QUADS):
        vals ^= ((q >> b) & 1)[:, None] * (BITS[:, i] & BITS[:, j])[None, :]
    vals ^= cub[None, :]
    return fwht_rows(1 - 2 * vals)


def affine_check(omega):
    """Is the 0/1 vector omega (indexed by kappa) an affine function?"""
    lin = [omega[1 << i] ^ omega[0] for i in range(6)]
    for k in range(64):
        v = omega[0]
        for i in range(6):
            if (k >> i) & 1:
                v ^= lin[i]
        if v != omega[k]:
            return False
    return True


def hist_key(row):
    return tuple(sorted(Counter(np.abs(row).tolist()).items()))


def main():
    if os.path.exists(OUT):
        print('refusing to overwrite', OUT)
        sys.exit(2)
    t0 = time.time()
    orb, iters = orbits()
    need(sum(c for _, c in orb) == 1 << 20, 'orbit sizes sum to 2^20')
    out = {'orbit_label_propagation_iterations': iters, 'cubic_classes': []}
    for rep, size in orb:
        W = completions(rep)
        p6 = sum(1 for a in range(20) for b in range(a + 1, 20)
                 if (rep >> a) & 1 and (rep >> b) & 1 and not set(CUBS[a]) & set(CUBS[b]))
        res = Counter(int(x) for x in np.unique(W % 8))
        need(len(res) == 1, 'uniform W mod 8 over all completions')
        r8 = next(iter(res))
        need(r8 == (4 * p6) % 8, 'W = 4*P6 mod 8')
        # Lemma B: the second residue bit is affine in kappa for every completion
        aff_ok = True
        for row in W:
            if r8 == 0:
                om = [int((v // 8) % 2) for v in row]
            else:
                om = [int(((v // 4 - p6) // 2) % 2) for v in row]
            if not affine_check(om):
                aff_ok = False
                break
        need(aff_ok, 'second residue bit affine for every completion')
        hists = Counter(hist_key(row) for row in W)
        out['cubic_classes'].append({
            'rep_mask': rep,
            'rep_monomials': [list(CUBS[n]) for n in range(20) if (rep >> n) & 1],
            'orbit_size': size,
            'P6_complementary_pairs': p6,
            'W_mod_8': r8,
            'second_residue_bit_affine_all_completions': aff_ok,
            'completion_abs_walsh_histograms': [
                {'hist': [list(p) for p in k], 'count': v} for k, v in sorted(hists.items())],
        })
    # the zero-flat cubic part x0x1x2 (z = 8): explicit list by completion index
    m012 = 1 << CIDX[(0, 1, 2)]
    W = completions(m012)
    classes = {}
    per_q = []
    for qi, row in enumerate(W):
        k = hist_key(row)
        if k not in classes:
            classes[k] = len(classes)
        per_q.append(classes[k])
    out['zero_flat_cubic'] = {
        'cubic_monomials': [[0, 1, 2]],
        'quadratic_monomial_order': [list(p) for p in QUADS],
        'classes': [{'id': v, 'hist': [list(p) for p in k],
                     'max_abs_W': max(a for a, _ in k),
                     'count': per_q.count(v)} for k, v in classes.items()],
        'class_of_completion_sha256': hashlib.sha256(bytes(per_q)).hexdigest(),
    }
    out['seconds'] = time.time() - t0
    with open(OUT, 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({'classes': len(orb), 'sizes': [c for _, c in orb],
                      'zero_flat': out['zero_flat_cubic']['classes'], 'seconds': out['seconds']}))


if __name__ == '__main__':
    main()
