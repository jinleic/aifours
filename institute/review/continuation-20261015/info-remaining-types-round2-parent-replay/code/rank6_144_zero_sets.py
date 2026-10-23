#!/usr/bin/env python3
"""Type (6,144): zero sets that are not K-invariant.

Normal form: D = a0a1+a0+a1+a2a3+a4a5, u = a0..a5, k = (a6,a7), K = span(e6,e7).
Computes:
  * the weight enumerator of RM(2,6) restricted to D0 = q6^{-1}(0) (28 points);
  * |D0 cap {l=1}| for every non-constant affine l (odd-slice counts);
  * every z = 8 zero set Z with e67 = 0 that is not K-invariant and passes
    the reviewed moment identities and the E-extension criterion. There are
    no others at z = 8: a nonempty slice set T2 has weight >= 4, and e67 != 0
    forces z >= 12. For each set, the D1 character fibers of E are computed;
  * the exact minimum of c for K-invariant Z (single character):
    minimise sum(l_u) subject to sum (12-4 l_u)^2 <= 4096 over 36 cosets.
Refuses to overwrite its output.
"""
import itertools, json, os, sys, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'results', 'rank6-144-zero-sets.json')


def need(cond, label):
    if not cond:
        raise ValueError('check failed: ' + label)


def bit(x, i):
    return (x >> i) & 1


def q6(u):
    return (bit(u, 0) & bit(u, 1)) ^ bit(u, 0) ^ bit(u, 1) ^ (bit(u, 2) & bit(u, 3)) ^ (bit(u, 4) & bit(u, 5))


U0 = [u for u in range(64) if q6(u) == 0]
U1 = [u for u in range(64) if q6(u) == 1]
QM6 = [m for m in range(64) if bin(m).count('1') <= 2]
CUB8 = [m for m in range(256) if bin(m).count('1') <= 3]
D0B = [a for a in range(256) if q6(a & 63) == 0]
PF = [0b001111, 0b110011, 0b111100]


def basis_with_preimage(rows):
    piv = {}
    for j, r in enumerate(rows):
        x, c = r, 1 << j
        for p in sorted(piv, reverse=True):
            if x >> p & 1:
                x ^= piv[p][0]
                c ^= piv[p][1]
        if x:
            piv[x.bit_length() - 1] = (x, c)
    return list(piv.values())


def span_piv(rows):
    piv = {}
    for r in rows:
        x = r
        while x:
            p = x.bit_length() - 1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p] = x
                break
    return piv


def in_span(piv, x):
    while x:
        p = x.bit_length() - 1
        if p not in piv:
            return False
        x ^= piv[p]
    return True


PIV3 = span_piv([sum(1 << i for i, a in enumerate(D0B) if (a & m) == m) for m in CUB8])
PFVEC = sum(1 << i for i, a in enumerate(D0B) if sum(1 for m in PF if (a & m) == m) & 1)


def ext_ok(Z):
    zs = set(Z)
    t = sum(1 << i for i, a in enumerate(D0B) if a not in zs) ^ PFVEC
    return in_span(PIV3, t)


def moments_ok(Z):
    if len(Z) % 2:
        return False
    x = 0
    for a in Z:
        x ^= a
    if x:
        return False
    for i in range(8):
        for j in range(i + 1, 8):
            want = 1 if (i, j) == (6, 7) else 0
            if sum(1 for a in Z if bit(a, i) and bit(a, j)) % 2 != want:
                return False
    return True


def qvals(coeffs):
    return [sum(1 for j, m in enumerate(QM6) if (coeffs >> j) & 1 and (u & m) == m) & 1 for u in range(64)]


def main():
    if os.path.exists(OUT):
        print('refusing to overwrite', OUT)
        sys.exit(2)
    t0 = time.time()
    need(len(U0) == 28 and len(U1) == 36, 'q6 weight 36')
    need(len(PIV3) == 76, 'RM(3,8) restricted to D0 has rank 76')
    B = basis_with_preimage([sum(1 << i for i, u in enumerate(U0) if (u & m) == m) for m in QM6])
    need(len(B) == 21, 'RM(2,6)|D0 has dimension 21')
    wt = Counter()
    w4 = []
    x = cc = 0
    wt[0] += 1
    for i in range(1, 1 << len(B)):
        j = (i & -i).bit_length() - 1
        x ^= B[j][0]
        cc ^= B[j][1]
        w = bin(x).count('1')
        wt[w] += 1
        if w == 4:
            w4.append((x, cc))
    odd = Counter()
    for l in range(1, 64):
        for b in (0, 1):
            odd[sum(1 for u in U0 if (bin(u & l).count('1') + b) & 1)] += 1
    supp = lambda v: [U0[i] for i in range(28) if v >> i & 1]
    adm = []
    for v, cc in w4:
        T2 = supp(v)
        if 0 not in T2:
            continue
        for chi in ((1, 0), (0, 1), (1, 1)):
            line = {b: [k for k in range(4) if ((chi[0] * (k & 1)) ^ (chi[1] * (k >> 1))) == b] for b in (0, 1)}
            others = [u for u in T2 if u]
            for bs in itertools.product((0, 1), repeat=3):
                off = {0: 0}
                off.update(dict(zip(others, bs)))
                Z = sorted(u | (k << 6) for u in T2 for k in line[off[u]])
                if moments_ok(Z) and ext_ok(Z):
                    g = qvals(cc)
                    need(all(g[u] == (1 if u in T2 else 0) for u in U0), 'quadratic preimage restricts to T2')
                    m = sum(g[u] for u in U1)
                    T2x = 0
                    for u in T2:
                        T2x ^= u
                    adm.append({'Z': Z, 'T2': T2, 'chi_star': list(chi),
                                'T2_xor': T2x, 'T2_totally_singular': all(q6(a ^ b) == 0 for a in T2 for b in T2),
                                'D1_fibers': sorted([m, 36 - m])})
    need(all(a['T2_xor'] == 0 and a['T2_totally_singular'] for a in adm), 'T2 is a totally singular plane')
    fib = Counter(tuple(a['D1_fibers']) for a in adm)
    # exact single-character minimum of c (K-invariant Z): costs (12-4l)^2, l in 0..3
    best = None
    for n1 in range(37):
        for n2 in range(37 - n1):
            for n3 in range(37 - n1 - n2):
                n0 = 36 - n1 - n2 - n3
                if 144 * n0 + 64 * n1 + 16 * n2 <= 4096:
                    c = n1 + 2 * n2 + 3 * n3
                    if best is None or c < best[0]:
                        best = (c, n0, n1, n2, n3)
    out = {
        'rm2_restricted_weight_enumerator': sorted(wt.items()),
        'odd_slice_counts_nonconstant_affine': sorted(odd.items()),
        'z8_noninvariant_admissible_count': len(adm),
        'z8_noninvariant_D1_fiber_histogram': [[list(k), v] for k, v in fib.items()],
        'z8_noninvariant_sets': adm,
        'single_character_min_c': {'c': best[0], 'n_ell0': best[1], 'n_ell1': best[2], 'n_ell2': best[3], 'n_ell3': best[4]},
        'seconds': time.time() - t0,
    }
    with open(OUT, 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: out[k] for k in ('rm2_restricted_weight_enumerator', 'odd_slice_counts_nonconstant_affine',
                                          'z8_noninvariant_admissible_count', 'z8_noninvariant_D1_fiber_histogram',
                                          'single_character_min_c', 'seconds')}))


if __name__ == '__main__':
    main()
