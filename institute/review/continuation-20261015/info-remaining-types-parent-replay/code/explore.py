#!/usr/bin/env python3
"""Producer for the remaining seven residue types (exploratory + witnesses).

z3 is used only to FIND satisfying count vectors (positive witnesses showing a
relaxation cannot exclude a type).  No negative claim relies on a solver.
Independent replay is code/audit.py, which imports neither this file nor z3.
"""
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import time
import z3

ROOT = Path(__file__).resolve().parents[1]
VALS = [2, -6, 10, -14, 18, -22, 26]
TYPES = [(2, 192), (4, 160), (6, 112), (6, 128), (6, 144), (8, 120), (8, 136)]
NF = {(2, 192): [('l', 0), ('l', 1), ('q', 0, 1)],
      (4, 160): [('q', 0, 1), ('l', 0), ('l', 1), ('q', 2, 3)],
      (6, 112): [('q', 0, 1), ('q', 2, 3), ('q', 4, 5)],
      (6, 128): [('q', 0, 1), ('q', 2, 3), ('q', 4, 5), ('l', 6)],
      (6, 144): [('q', 0, 1), ('l', 0), ('l', 1), ('q', 2, 3), ('q', 4, 5)],
      (8, 120): [('q', 0, 1), ('q', 2, 3), ('q', 4, 5), ('q', 6, 7)],
      (8, 136): [('q', 0, 1), ('l', 0), ('l', 1), ('q', 2, 3), ('q', 4, 5), ('q', 6, 7)]}
CUB = [m for m in range(256) if bin(m).count('1') <= 3]
QUAD = [m for m in range(256) if bin(m).count('1') <= 2]


def J(k):
    return ((k * k - 4) // 32) % 2


PAIRS = [(k, l) for k in VALS for l in VALS if abs(k) + abs(l) <= 28]


def dval(terms, a):
    v = 0
    for t in terms:
        v ^= ((a >> t[1]) & 1) if t[0] == 'l' else (((a >> t[1]) & 1) & ((a >> t[2]) & 1))
    return v


def rank(rows):
    piv = {}
    for r in rows:
        while r:
            p = r.bit_length() - 1
            if p in piv:
                r ^= piv[p]
            else:
                piv[p] = r
                break
    return len(piv)


def nullspace_words(points, monos):
    rows = [sum((1 if a & m == m else 0) << j for j, m in enumerate(monos)) for a in points]
    R, piv, used = list(rows), [], 0
    for col in range(len(monos)):
        idx = next((i for i in range(used, len(R)) if R[i] >> col & 1), None)
        if idx is None:
            continue
        R[used], R[idx] = R[idx], R[used]
        for i in range(len(R)):
            if i != used and R[i] >> col & 1:
                R[i] ^= R[used]
        piv.append(col)
        used += 1
    out = []
    for f in range(len(monos)):
        if f in piv:
            continue
        v = 1 << f
        for i, p in enumerate(piv):
            if R[i] >> f & 1:
                v |= 1 << p
        w = 0
        for a in range(256):
            w |= (sum(1 for j, m in enumerate(monos) if v >> j & 1 and a & m == m) & 1) << a
        out.append(w)
    return used, out


def structure(ty):
    terms = NF[ty]
    Dt = [dval(terms, a) for a in range(256)]
    B = [[0] * 8 for _ in range(8)]
    for t in terms:
        if t[0] == 'q':
            B[t[1]][t[2]] = B[t[2]][t[1]] = 1
    rows = [sum(B[i][j] << j for j in range(8)) for i in range(8)]
    rad = [a for a in range(256) if all(bin(rows[i] & a).count('1') % 2 == 0 for i in range(8))]
    K = [a for a in rad if Dt[a] == 0]
    Kb = []
    for a in K:
        if a and rank(Kb + [a]) > len(Kb):
            Kb.append(a)
    tau = len(Kb)
    quart = [list(I) for I in itertools.combinations(range(8), 4)
             if (B[I[0]][I[1]] & B[I[2]][I[3]]) ^ (B[I[0]][I[2]] & B[I[1]][I[3]]) ^ (B[I[0]][I[3]] & B[I[1]][I[2]])]
    D0 = [a for a in range(256) if Dt[a] == 0]
    D1 = [a for a in range(256) if Dt[a] == 1]
    r3, kern3 = nullspace_words(D0, CUB)
    nonconst = sum(1 for w in kern3 if any(len({((w >> a) ^ (w >> (a ^ k))) & 1 for a in D1}) > 1 for k in Kb))
    r2, kern2 = nullspace_words(D0, QUAD)
    d = ty[1]
    slice_bound = 2 ** (12 - tau)
    return {'type': list(ty), 'normal_form_terms': terms, 'weight': sum(Dt), 'D0_at_origin': Dt[0],
            'polar_rank': rank(rows), 'radical_dim': len(rad).bit_length() - 1,
            'D_on_radical': 'zero' if all(Dt[a] == 0 for a in rad) else 'nonzero linear',
            'K_basis': Kb, 'tau': tau, 'pfaffian_quartic_supports': quart,
            'RM3_restriction_rank_on_D0': r3, 'RM3_kernel_dim': len(kern3),
            'RM3_kernel_basis_words_with_nonconstant_K_derivative_on_D1': nonconst,
            'RM2_kernel_on_D0_truth_hex': [hex(w) for w in kern2],
            'single_character_slice_bound': slice_bound, 'nine_d': 9 * d,
            'c_threshold_rational': [9 * d - slice_bound, 24]}


def qweight_ranks(w):
    out = set()
    if w in (0, 256):
        out.add(0)
    if w == 128:
        out |= {0, 1, 2, 3}
    for t in range(1, 5):
        if w in (128 - 2 ** (7 - t), 128 + 2 ** (7 - t)):
            out.add(t)
    return sorted(out)


def zero_ok(r2, d, z):
    if z % 2:
        return False
    if r2 <= 4:
        return z >= 8 and z != 10
    if r2 == 6:
        return z >= 4 and z != 6 and (z >= 8 if d == 128 else True)
    return z >= 10 and (z >= 12 if d == 136 else True)


def scalar_model(ty, timeout=120000):
    r2, d = ty
    t = r2 // 2
    s = z3.Solver()
    s.set(timeout=timeout)
    N = {pq: z3.Int('N_%d_%d' % pq) for pq in PAIRS}
    for v in N.values():
        s.add(v >= 0)
    s.add(z3.Sum(list(N.values())) == 256)
    s.add(z3.Sum([N[(k, l)] for (k, l) in PAIRS if J(k) ^ J(l)]) == d)
    s.add(z3.Sum([k * k * N[(k, l)] for (k, l) in PAIRS]) == 65536)
    s.add(z3.Sum([l * l * N[(k, l)] for (k, l) in PAIRS]) == 65536)
    sg = z3.Sum([k * N[(k, l)] for (k, l) in PAIRS])
    sh = z3.Sum([l * N[(k, l)] for (k, l) in PAIRS])
    s.add(z3.Or(sg == 256, sg == -256), z3.Or(sh == 256, sh == -256))
    z = z3.Sum([N[(k, l)] for (k, l) in PAIRS if k == l])
    zv = z3.Int('z')
    s.add(zv == z, z3.Or([zv == zz for zz in range(257) if zero_ok(r2, d, zz)]))
    wR = z3.Int('wR')
    s.add(16 * wR == z3.Sum([((k - l) // 8) ** 2 * N[(k, l)] for (k, l) in PAIRS]), wR % 2 == 0)

    def corr(Q, tt, tag):
        G1 = z3.Sum([(-1) ** Q(pq) * (pq[0] + pq[1]) * N[pq] for pq in PAIRS])
        G2 = z3.Sum([(-1) ** Q(pq) * (pq[0] - pq[1]) * N[pq] for pq in PAIRS])
        N1, N2, q1, q2 = (z3.Int(n + tag) for n in ('NS', 'NR', 'qS', 'qR'))
        u = 2 ** (9 - tt)
        return z3.And(N1 >= 0, N2 >= 0, N1 + N2 == 2 ** (2 * tt), N1 <= 256 - wR, N2 <= wR,
                      G1 == u * q1, G2 == u * q2, q1 <= N1, -q1 <= N1, q2 <= N2, -q2 <= N2,
                      (q1 - N1) % 2 == 0, (q2 - N2) % 2 == 0)
    s.add(corr(lambda pq: J(pq[0]) ^ J(pq[1]), t, 'D'))
    for idx, side in ((0, 'g'), (1, 'h')):
        Jw = z3.Sum([N[pq] for pq in PAIRS if J(pq[idx])])
        s.add(z3.Or([z3.And(Jw == w, corr(lambda pq, i=idx: J(pq[i]), tt, '%s%d_%d' % (side, w, tt)))
                     for w in range(257) for tt in qweight_ranks(w)]))
    return s, N


H4 = [[(-1) ** bin(c & x).count('1') for x in range(4)] for c in range(4)]


def walsh2(bits):
    return tuple(sum((-1) ** (bits[x] ^ (bin(c & x).count('1') % 2)) for x in range(4)) for c in range(4))


def joint_patterns():
    out = []
    for ub in itertools.product((0, 1), repeat=4):
        for wb in itertools.product((0, 1), repeat=4):
            Wu, Ww = walsh2(ub), walsh2(wb)
            out.append({'u': list(ub), 'w': list(wb), 'h': [(Wu[c] - Ww[c]) // 2 for c in range(4)],
                        's': [(Wu[c] + Ww[c]) // 2 for c in range(4)], 'k': sum(1 for x in range(4) if ub[x] != wb[x])})
    return out


def rank2_relaxation(timeout=600000, Lmax=28, Amax=40):
    pats = joint_patterns()
    s = z3.Solver()
    s.set(timeout=timeout)
    x = [z3.Int('x%d' % i) for i in range(len(pats))]
    for v in x:
        s.add(v >= 0)
    s.add(z3.Sum(x) == 64)
    z = z3.Int('z')
    s.add(z >= 8, z <= 64, z % 2 == 0, z != 10)
    s.add(z3.Sum([x[i] * p['h'][0] ** 2 for i, p in enumerate(pats)]) == 64 - z)
    s.add(z3.Sum([x[i] * p['h'][0] for i, p in enumerate(pats)]) == 0)
    ell = [z3.Int('ell%d' % c) for c in (1, 2, 3)]
    acnt = [z3.Int('a%d' % c) for c in range(4)]
    for v in ell:
        s.add(v >= 0, v <= Lmax)
    for v in acnt:
        s.add(v >= 0, v <= Amax)
    ctot, atot = z3.Sum(ell), z3.Sum(acnt)
    s.add(2 * (atot + ctot) + z <= 64, (z + 2 * ctot) % 8 == 0, atot % 4 == 0)
    s.add(4 * z3.Sum([x[i] * p['k'] for i, p in enumerate(pats)]) == 496 - z - 2 * ctot)
    k0 = [z3.Bool('k0_%d' % i) for i in range(len(pats))]
    s.add(z3.PbEq([(b, 1) for b in k0], 1))
    for i in range(len(pats)):
        s.add(z3.Implies(k0[i], x[i] >= 1))
    aux = {}
    for ci, c in enumerate((1, 2, 3)):
        l = ell[ci]
        ys = {}
        for h in range(-4, 5):
            terms = []
            for Lam in range(-Lmax, Lmax + 1):
                if (4 * Lam - 16 * h) % 3:
                    continue
                y = z3.Int('yR%d_%d_%d' % (c, h, Lam))
                ys[(h, Lam)] = y
                s.add(y >= 0, z3.Implies(y > 0, z3.And(Lam <= l, -Lam <= l, (l - Lam) % 2 == 0)))
                terms.append(y)
            s.add(z3.Sum(terms) == z3.Sum([x[i] for i, p in enumerate(pats) if p['h'][c] == h]))
        W = lambda h, L: (4 * L - 16 * h) // 3
        s.add(z3.Sum([y * W(h, L) ** 2 for (h, L), y in ys.items()]) == 4096)
        s.add(z3.Sum([y * h * h for (h, L), y in ys.items()]) == 144 - 2 * l)
        s.add(z3.Sum([y * L * L for (h, L), y in ys.items()]) == 64 * l)
        s.add(z3.Sum([y * L * h for (h, L), y in ys.items()]) == 4 * l)
        aux['R%d' % c] = ys
    for c in range(4):
        av = acnt[c]
        sgn = -1 if c == 0 else 1
        ys = {}
        for sv in range(-4, 5):
            terms = []
            for Lam in range(-Amax, Amax + 1):
                for d0 in (0, 1):
                    if (sgn * 32 * d0 + 4 * Lam - 16 * sv) % 3:
                        continue
                    y = z3.Int('yS%d_%d_%d_%d' % (c, sv, Lam, d0))
                    ys[(sv, Lam, d0)] = y
                    s.add(y >= 0, z3.Implies(y > 0, z3.And(Lam <= av, -Lam <= av, (av - Lam) % 2 == 0)))
                    terms.append(y)
            s.add(z3.Sum(terms) == z3.Sum([x[i] for i, p in enumerate(pats) if p['s'][c] == sv]))
        s.add(z3.Sum([y for k, y in ys.items() if k[2] == 1]) == 1)
        for sv in range(-4, 5):
            s.add(z3.Implies(z3.Sum([y for k, y in ys.items() if k[2] == 1 and k[0] == sv]) == 1,
                             z3.Or([k0[i] for i, p in enumerate(pats) if p['s'][c] == sv])))
        W = lambda sv, L, d0: (sgn * 32 * d0 + 4 * L - 16 * sv) // 3
        s.add(z3.Sum([y * W(*k) ** 2 for k, y in ys.items()]) == 4096)
        s.add(z3.Sum([y * k[1] ** 2 for k, y in ys.items()]) == 64 * av)
        s0 = z3.Sum([y * k[0] for k, y in ys.items() if k[2] == 1])
        L0 = z3.Sum([y * k[1] for k, y in ys.items() if k[2] == 1])
        s.add(z3.Sum([y * k[0] ** 2 for k, y in ys.items()]) == 140 - 2 * av + 4 * sgn * s0)
        s.add(z3.Sum([y * k[0] * k[1] for k, y in ys.items()]) == 4 * av + 2 * sgn * L0)
        aux['S%d' % c] = ys
    r = s.check()
    out = {'status': str(r)}
    if r == z3.sat:
        m = s.model()
        out['z'] = m[z].as_long()
        out['ell'] = [m[v].as_long() for v in ell]
        out['a'] = [m[v].as_long() for v in acnt]
        out['pattern_counts'] = [{'u': p['u'], 'w': p['w'], 'count': m[x[i]].as_long()} for i, p in enumerate(pats) if m[x[i]].as_long()]
        out['kappa0_pattern'] = next({'u': p['u'], 'w': p['w']} for i, p in enumerate(pats) if z3.is_true(m[k0[i]]))
        out['aux'] = {name: [list(k) + [m[y].as_long()] for k, y in ys.items() if m[y].as_long()] for name, ys in aux.items()}
    return out


def main():
    start = time.monotonic()
    raw = (ROOT / 'inputs/slice-screen.json.gz').read_bytes()
    assert hashlib.sha256(raw).hexdigest() == '200a4997f0a1bcc5c63eaf53f2602118395950ddb951b5bee43c23c92f32cf6d'
    structures = {str(ty): structure(ty) for ty in TYPES}
    witnesses = {}
    for ty in TYPES:
        s, N = scalar_model(ty)
        r = s.check()
        rec = {'status': str(r)}
        if r == z3.sat:
            m = s.model()
            rec['counts'] = [[k, l, m.eval(N[(k, l)]).as_long()] for (k, l) in PAIRS if m.eval(N[(k, l)]).as_long()]
        witnesses[str(ty)] = rec
        print(ty, r, flush=True)
    rel = rank2_relaxation()
    print('rank2 relaxation', rel['status'], rel.get('z'), rel.get('ell'), rel.get('a'), flush=True)
    out = {'scope': 'Exploratory producer; z3 used only to find positive count witnesses. Audit replays without z3.',
           'z3_version': z3.get_version_string(), 'input_sha256': hashlib.sha256(raw).hexdigest(),
           'canonical_pairs': PAIRS, 'structures': structures, 'scalar_witnesses': witnesses,
           'rank2_joint_relaxation_witness': rel, 'elapsed_seconds': time.monotonic() - start}
    path = ROOT / 'results/explore.json.gz'
    if path.exists():
        raise SystemExit('Preserve existing producer output')
    path.write_bytes(gzip.compress((json.dumps(out, separators=(',', ':')) + '\n').encode(), mtime=0))
    print('elapsed', out['elapsed_seconds'])


if __name__ == '__main__':
    main()
