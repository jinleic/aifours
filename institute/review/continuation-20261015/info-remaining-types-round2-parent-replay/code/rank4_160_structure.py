#!/usr/bin/env python3
"""Type (4,160): coset-affine structure, z = 8 classification and slice witnesses.

Normal form: D = a0a1+a0+a1+a2a3, u = a0..a3, k = a4..a7, K = span(e4..e7).
Computes:
  * D0 = q4^{-1}(0) spans F_2^4 affinely (premise of Lemma 4.2);
  * every 3-dimensional linear subspace Z of D^{-1}(0) that passes the
    E-extension criterion, classified by dim pi(Z) (8a: 0, 8b: 1). For each
    class it counts the D1 cosets on which E restricted to the coset cannot
    be affine. The quadratic-in-k ANF coefficients are affine in u, so
    their values on D0 determine them;
  * the lone-slice table: every ternary eps in {0,+-1}^16 with (H eps)(u1)=12
    and (H eps)(v)=0 on the other nine D1 cosets, for each u1 in D1, with
    the minimum energy outside u1;
  * two aggregate slice witnesses (case 8a, z = 8). One has c = 4. The other
    has c = 16 and pairwise distinct characters. Both satisfy every slice
    constraint proved in PROOF.md.
Refuses to overwrite its output.
"""
import itertools, json, os, sys, time
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, '..', 'results', 'rank4-160-structure.json')


def need(cond, label):
    if not cond:
        raise ValueError('check failed: ' + label)


def bit(x, i):
    return (x >> i) & 1


def q4(u):
    return (bit(u, 0) & bit(u, 1)) ^ bit(u, 0) ^ bit(u, 1) ^ (bit(u, 2) & bit(u, 3))


Q0 = [u for u in range(16) if q4(u) == 0]
Q1 = [u for u in range(16) if q4(u) == 1]
D0B = [a for a in range(256) if q4(a & 15) == 0]
CUB8 = [m for m in range(256) if bin(m).count('1') <= 3]
PFMASK = 0b1111


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
PFVEC = sum(1 << i for i, a in enumerate(D0B) if (a & PFMASK) == PFMASK)


def ext_ok(Z):
    zs = set(Z)
    return in_span(PIV3, sum(1 << i for i, a in enumerate(D0B) if a not in zs) ^ PFVEC)


def anf16(vals):
    a = list(vals)
    for i in range(4):
        for x in range(16):
            if x >> i & 1:
                a[x] ^= a[x ^ (1 << i)]
    return a


def hadamard16(v):
    return [sum(v[x] * (1 - 2 * (bin(x & u).count('1') & 1)) for x in range(16)) for u in range(16)]


def main():
    if os.path.exists(OUT):
        print('refusing to overwrite', OUT)
        sys.exit(2)
    t0 = time.time()
    need(len(Q0) == 6 and len(Q1) == 10, 'q4 has weight 10')
    diffs = [u ^ Q0[0] for u in Q0[1:]]
    need(len(span_piv(diffs)) == 4, 'D0 spans F_2^4 affinely')
    need(len(PIV3) == 64, 'RM(3,8)|D0 rank 64')
    # all 3-dim linear subspaces inside D^{-1}(0)
    pts = [a for a in D0B if a]
    seen = set()
    for a, b, c in itertools.combinations(pts, 3):
        S = sorted({0, a, b, c, a ^ b, a ^ c, b ^ c, a ^ b ^ c})
        if len(S) == 8 and all(q4(x & 15) == 0 for x in S):
            seen.add(tuple(S))
    classes = Counter()
    nonaffine = Counter()
    ext_pass = 0
    for S in seen:
        if not ext_ok(S):
            continue
        ext_pass += 1
        proj = sorted({x & 15 for x in S})
        kind = '8a' if proj == [0] else '8b'
        need(len(proj) in (1, 2), 'projection is totally singular (dim <= 1)')
        classes[kind] += 1
        # quadratic-in-k ANF coefficients on D0 cosets from E_u = 1 + 1_{Z_u}
        coef = {}
        for u in Q0:
            vals = [1 ^ (1 if (u | (k << 4)) in S else 0) for k in range(16)]
            an = anf16(vals)
            coef[u] = {m: an[m] for m in range(16) if bin(m).count('1') >= 2}
        need(all(coef[u][m] == 0 for u in Q0 for m in coef[u] if bin(m).count('1') >= 3), 'slices have degree <= 2')
        # affine extension in u of each quadratic-in-k coefficient (unique since D0 spans affinely)
        bad = 0
        for u1 in Q1:
            nonaff = False
            for m in [m for m in range(16) if bin(m).count('1') == 2]:
                found = None
                for lin in range(16):
                    for cst in (0, 1):
                        f = lambda u: (bin(u & lin).count('1') + cst) & 1
                        if all(f(u) == coef[u][m] for u in Q0):
                            need(found is None, 'unique affine extension')
                            found = f(u1)
                need(found is not None, 'affine extension exists')
                if found:
                    nonaff = True
            bad += nonaff
        nonaffine[(kind, bad)] += 1
    # lone-slice table
    lone = {}
    for u1 in Q1:
        best = None
        cnt = 0
        # enumerate eps with sum eps*(-1)^{x.u1} = 12: multiply by character, then eps' has sum 12
        for npos, nneg in ((12, 0), (13, 1), (14, 2)):
            for P in itertools.combinations(range(16), npos):
                rest = [x for x in range(16) if x not in P]
                for N in itertools.combinations(rest, nneg):
                    e = [0] * 16
                    for x in P:
                        e[x] = 1 - 2 * (bin(x & u1).count('1') & 1)
                    for x in N:
                        e[x] = -(1 - 2 * (bin(x & u1).count('1') & 1))
                    Y = hadamard16(e)
                    need(Y[u1] == 12, 'centered value 12')
                    if any(Y[v] for v in Q1 if v != u1):
                        continue
                    cnt += 1
                    outside = sum(Y[v] ** 2 for v in range(16) if v != u1)
                    supD0 = sorted(v for v in Q0 if Y[v])
                    if best is None or outside < best[0]:
                        best = (outside, supD0, [Y[v] for v in supD0])
        lone[u1] = {'solutions': cnt, 'min_outside_energy': best[0], 'support_at_min': best[1], 'values_at_min': best[2]}
    need(all(v['min_outside_energy'] == 48 for v in lone.values()), 'lone slice needs 48 outside')
    trip = {}
    for t in itertools.combinations([u for u in Q0 if u], 3):
        trip[t[0] ^ t[1] ^ t[2]] = list(t)
    need(sorted(trip) == Q1, 'triples of D0 minus 0 biject onto D1')
    # aggregate slice witnesses for case 8a (z = 8): energies in Y = phat/4 units
    def check_witness(name, ell, slices, z):
        c = sum(ell)
        need((z + 2 * c) % 8 == 0, name + ': z+2c = 0 mod 8')
        need(2 * c + z <= 56, name + ': slack bound')
        par = {l % 2 for l in ell}
        need(len(par) == 1, name + ': uniform ell parity')
        total = 1824 - 4 * z - 8 * c
        need(sum(E for _, E in slices) == total, name + ': total slice energy')
        used = [u for A, _ in slices for u in A]
        need(sorted(used) == list(range(len(ell))), name + ': each D1 coset in one slice')
        other = 0
        for A, E in slices:
            need(E % 16 == 0 and 0 <= E <= 256, name + ': slice energy range')
            need((E // 16) % 2 == next(iter(par)), name + ': support parity equals the uniform ell parity')
            own = sum((12 - ell[u]) ** 2 for u in A)
            need(E >= own, name + ': own energy fits')
            if A:
                need(E >= 16 * max(12 - ell[u] for u in A), name + ': uncertainty bound')
            other += E - own
        avail = 4 * (96 - z) + sum(l * (16 - l) for l in ell)
        need(other == avail, name + ': outside energy equals D0 energy plus spreads')
        return {'ell': ell, 'c': c, 'z': z, 'slices': [[A, E] for A, E in slices], 'outside_energy': other}
    w4 = check_witness('c4', [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
                       [([0], 192), ([1], 192), ([2], 192), ([3], 192), ([4], 192), ([5], 192),
                        ([6, 8], 256), ([7, 9], 256), ([], 32), ([], 32), ([], 32)] + [([], 0)] * 5, 8)
    w16 = check_witness('c16inj', [2, 2, 2, 2, 2, 2, 2, 2, 0, 0],
                        [([u], 192 if u >= 8 else 160) for u in range(10)] + [([], 0)] * 6, 8)
    out = {
        'D0': Q0, 'D1': Q1,
        'z8_linear_subspaces_in_D0': len(seen), 'z8_ext_pass': ext_pass,
        'z8_classes': dict(classes),
        'z8_nonaffine_D1_cosets': [[list(k), v] for k, v in nonaffine.items()],
        'lone_slice': {str(k): v for k, v in lone.items()},
        'triple_bijection': {str(k): v for k, v in trip.items()},
        'slice_witness_c4': w4, 'slice_witness_c16_injective': w16,
        'seconds': time.time() - t0,
    }
    with open(OUT, 'w') as fh:
        json.dump(out, fh, indent=1)
    print(json.dumps({k: out[k] for k in ('z8_linear_subspaces_in_D0', 'z8_ext_pass', 'z8_classes',
                                          'z8_nonaffine_D1_cosets', 'seconds')}))
    print('lone', {k: (v['solutions'], v['min_outside_energy'], v['support_at_min']) for k, v in lone.items()})


if __name__ == '__main__':
    main()
