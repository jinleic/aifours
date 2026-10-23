#!/usr/bin/env python3
"""Independent exact audit for remaining-types/PROOF.md; imports no producer code and no solver.

All acceptance checks raise explicit exceptions (active under python -O).
"""
import argparse
from collections import Counter
import gzip
import hashlib
import itertools
import json
from pathlib import Path
import time

ROOT = Path(__file__).resolve().parents[1]
PIN = '200a4997f0a1bcc5c63eaf53f2602118395950ddb951b5bee43c23c92f32cf6d'
VALS = [2, -6, 10, -14, 18, -22, 26]
TYPES = [(2, 192), (4, 160), (6, 112), (6, 128), (6, 144), (8, 120), (8, 136)]
FORMS = {  # independent spelling: list of monomial masks (ANF) for each normal form
    (2, 192): [1, 2, 3], (4, 160): [3, 1, 2, 12], (6, 112): [3, 12, 48], (6, 128): [3, 12, 48, 64],
    (6, 144): [3, 1, 2, 12, 48], (8, 120): [3, 12, 48, 192], (8, 136): [3, 1, 2, 12, 48, 192]}


def need(cond, label):
    if not cond:
        raise ValueError(label)


def anf_eval(monos, a):
    return sum(1 for m in monos if a & m == m) & 1


def gf2_rank_low(vectors):
    basis = {}
    for v in vectors:
        while v:
            p = (v & -v).bit_length() - 1
            if p in basis:
                v ^= basis[p]
            else:
                basis[p] = v
                break
    return len(basis)


def null_dim_low(rows, ncols):
    return ncols - gf2_rank_low(rows)


def Jres(k):
    return ((k * k - 4) // 32) % 2


def walsh8(signs):
    return [sum(v * (1 if (a & x).bit_count() % 2 == 0 else -1) for x, v in enumerate(signs)) for a in range(len(signs))]


def fwht(vals):
    v = list(vals)
    h = 1
    while h < len(v):
        for i in range(0, len(v), 2 * h):
            for j in range(i, i + h):
                v[j], v[j + h] = v[j] + v[j + h], v[j] - v[j + h]
        h *= 2
    return v


def degree(truth, n):
    c = list(truth)
    for i in range(n):
        for x in range(1 << n):
            if x >> i & 1:
                c[x] ^= c[x ^ (1 << i)]
    return max((x.bit_count() for x in range(1 << n) if c[x]), default=-1), c


def quad_ranks(w):
    out = set()
    if w in (0, 256):
        out.add(0)
    if w == 128:
        out |= {0, 1, 2, 3}
    for t in range(1, 5):
        if w in (128 - 2 ** (7 - t), 128 + 2 ** (7 - t)):
            out.add(t)
    return out


def zero_table(r2, d, z):
    if z % 2 or z < 1:
        return False
    if r2 <= 4:
        return z >= 8 and z != 10
    if r2 == 6:
        return z >= 4 and z != 6 and (d != 128 or z >= 8)
    return z >= 10 and (d != 136 or z >= 12)


def structure_audit(produced, corrupt_threshold=False):
    out = {}
    for ty in TYPES:
        monos = FORMS[ty]
        Dt = [anf_eval(monos, a) for a in range(256)]
        need(sum(Dt) == ty[1] and Dt[0] == 0, 'normal form weight/origin')
        # polar form from values, independent of the term list
        B = [[Dt[(1 << i) ^ (1 << j)] ^ Dt[1 << i] ^ Dt[1 << j] if i != j else 0 for j in range(8)] for i in range(8)]
        rows = [sum(B[i][j] << j for j in range(8)) for i in range(8)]
        r2 = gf2_rank_low(rows)
        need(r2 == ty[0], 'polar rank')
        rad = [a for a in range(256) if all(((rows[i] & a).bit_count() & 1) == 0 for i in range(8))]
        K = [a for a in rad if Dt[a] == 0]
        tau = len(K).bit_length() - 1
        need(len(K) == 1 << tau, 'K is a subspace')
        Kbasis = []
        for a in sorted(K):
            if a and gf2_rank_low(Kbasis + [a]) > len(Kbasis):
                Kbasis.append(a)
        quart = [I for I in itertools.combinations(range(8), 4)
                 if (B[I[0]][I[1]] * B[I[2]][I[3]] + B[I[0]][I[2]] * B[I[1]][I[3]] + B[I[0]][I[3]] * B[I[1]][I[2]]) % 2]
        D0 = [a for a in range(256) if Dt[a] == 0]
        D1 = [a for a in range(256) if Dt[a] == 1]
        cubics = [m for m in range(256) if m.bit_count() <= 3]
        quads = [m for m in range(256) if m.bit_count() <= 2]
        # transpose orientation vs producer: columns are points
        cols3 = [sum(1 << j for j, m in enumerate(cubics) if a & m == m) for a in D0]
        r3 = gf2_rank_low(cols3)
        cols2 = [sum(1 << j for j, m in enumerate(quads) if a & m == m) for a in D0]
        r2q = gf2_rank_low(cols2)
        p = produced['structures'][str(ty)]
        need(p['tau'] == tau and p['polar_rank'] == r2 and p['RM3_restriction_rank_on_D0'] == r3 and p['RM3_kernel_dim'] == 93 - r3, 'structure mismatch')
        need(len(p['pfaffian_quartic_supports']) == len(quart), 'pfaffian quartic mismatch')
        need(len(p['RM2_kernel_on_D0_truth_hex']) == 37 - r2q, 'quadratic kernel dimension mismatch')
        # kernel words supplied by producer must vanish on D0 and be quadratic
        for hx in p['RM2_kernel_on_D0_truth_hex']:
            w = int(hx, 16)
            need(all(not (w >> a & 1) for a in D0), 'quadratic kernel word does not vanish on D0')
            need(degree([(w >> a) & 1 for a in range(256)], 8)[0] <= 2, 'quadratic kernel word degree')
        slice_bound = 2 ** (12 - tau)
        threshold_violable = 9 * ty[1] > slice_bound
        if corrupt_threshold and ty == (6, 112):
            threshold_violable = True
        expected_violable = ty in ((2, 192), (4, 160), (6, 144))
        need(threshold_violable == expected_violable, 'projection threshold classification')
        rec = {'tau': tau, 'radical_dim': len(rad).bit_length() - 1, 'pfaffian_quartics': len(quart),
               'quartic_supports_avoid_K_coordinates': all(not any(Kv >> i & 1 for Kv in Kbasis for i in I) for I in quart),
               'RM3_restriction_rank': r3, 'RM2_kernel_dim_on_D0': 37 - r2q,
               'slice_bound': slice_bound, 'nine_d': 9 * ty[1], 'threshold_violable': threshold_violable}
        if expected_violable:
            num = 9 * ty[1] - slice_bound
            rec['min_c_for_lever'] = num // 24 + 1  # smallest c with 9d-24c <= slice_bound
        out[str(ty)] = rec
    # Theorem 4.1 ingredients for (6,144)
    t = out[str((6, 144))]
    need(t['RM2_kernel_dim_on_D0'] == 1 and t['quartic_supports_avoid_K_coordinates'], 'Theorem 4.1 ingredients')
    need(t['min_c_for_lever'] == 12, 'Theorem 4.1 threshold')
    need(out[str((4, 160))]['RM2_kernel_dim_on_D0'] > 1, '(4,160) obstruction ingredient')
    return out


def scalar_witness_audit(produced, corrupt=False):
    pairs = [(k, l) for k in VALS for l in VALS if abs(k) + abs(l) <= 28]
    need(len(pairs) == 28 and [tuple(p) for p in produced['canonical_pairs']] == pairs, 'canonical pairs')
    out = {}
    for ty in TYPES:
        rec = produced['scalar_witnesses'][str(ty)]
        need(rec['status'] == 'sat', 'missing scalar witness')
        N = Counter({(k, l): n for k, l, n in rec['counts']})
        if corrupt and ty == (4, 160):
            first = next(iter(N))
            N[first] += 1
        need(all(n >= 0 for n in N.values()) and set(N) <= set(pairs), 'witness support')
        need(sum(N.values()) == 256, 'witness size')
        D = lambda kl: Jres(kl[0]) ^ Jres(kl[1])
        need(sum(n for kl, n in N.items() if D(kl)) == ty[1], 'witness D weight')
        need(sum(kl[0] ** 2 * n for kl, n in N.items()) == 65536 and sum(kl[1] ** 2 * n for kl, n in N.items()) == 65536, 'witness Parseval')
        need(abs(sum(kl[0] * n for kl, n in N.items())) == 256 and abs(sum(kl[1] * n for kl, n in N.items())) == 256, 'witness canonical means')
        z = sum(n for kl, n in N.items() if kl[0] == kl[1])
        c = sum(n for kl, n in N.items() if abs(kl[0] - kl[1]) == 8)
        a = sum(n for kl, n in N.items() if abs(kl[0] + kl[1]) in (4, 12))
        need(zero_table(ty[0], ty[1], z), 'witness zero table')
        p2 = sum(((kl[0] - kl[1]) // 8) ** 2 * n for kl, n in N.items())
        need(p2 % 32 == 0, 'witness |A_R| even integer')
        wR = p2 // 16
        need(wR == 64 + (5 * ty[1] - 4 * z - 8 * c) // 16 and (5 * ty[1] - 4 * z - 8 * c) % 16 == 0, 'witness w_R formula')

        def dual_ok(Q, tq):
            GS = sum((-1) ** Q(kl) * (kl[0] + kl[1]) * n for kl, n in N.items())
            GR = sum((-1) ** Q(kl) * (kl[0] - kl[1]) * n for kl, n in N.items())
            unit = 2 ** (9 - tq)
            if GS % unit or GR % unit:
                return False
            for NS in range(0, 2 ** (2 * tq) + 1):
                NR = 2 ** (2 * tq) - NS
                if NS > 256 - wR or NR > wR:
                    continue
                if abs(GS) <= unit * NS and abs(GR) <= unit * NR and (GS // unit - NS) % 2 == 0 and (GR // unit - NR) % 2 == 0:
                    return True
            return False
        need(dual_ok(D, ty[0] // 2), 'witness dual correlation for D')
        for idx in (0, 1):
            Q = lambda kl, i=idx: Jres(kl[i])
            w = sum(n for kl, n in N.items() if Q(kl))
            need(any(dual_ok(Q, tq) for tq in quad_ranks(w)), 'witness dual correlation for J')
        GD = sum((-1) ** D(kl) * (kl[0] + kl[1]) * n for kl, n in N.items())
        need(GD == 40 * ty[1] - 6656 - 64 * (a + c) - 32 * z, 'reviewed slack identity on witness')
        out[str(ty)] = {'z': z, 'c': c, 'a': a, 'w_R': wR, 'Gamma': GD}
    return out


def representation_audit():
    for k in VALS:
        for l in VALS:
            if abs(k) + abs(l) > 28:
                continue
            D = Jres(k) ^ Jres(l)
            S, R = k + l, k - l
            need(R % 8 == 0, 'R divisible by 8')
            p = R // 8
            E = ((p - D) // 2) % 2
            J1 = int(abs(S) in (12, 20))
            A = int(abs(S) in (4, 12))
            X = J1 ^ D
            need(S == 4 * (2 * D - 1) + 8 * (-1) ** X * (-3 + 4 * A), 'S representation')
            if D:
                need(p == (-1) ** E * (-3 + 4 * int(abs(p) == 1)), 'p representation')
            need(J1 == (((-1) ** D * S - 4) // 16) % 2, 'J1 general definition')
    return True


def genuine_pair_audit(corrupt=False):
    raw = (ROOT / 'inputs/slice-screen.json.gz').read_bytes()
    need(hashlib.sha256(raw).hexdigest() == PIN, 'input pin')
    data = json.loads(gzip.decompress(raw))
    tested = []
    for source in data['sources'][:6]:
        bits = [int(b) for b in source['bits']]
        s = source['support_xor']
        normal = next(v for v in range(1, 512) if (v & s).bit_count() % 2)
        piv = (normal & -normal).bit_length() - 1
        coords = [j for j in range(9) if j != piv]
        pts = []
        for y in range(256):
            x = sum(((y >> i) & 1) << j for i, j in enumerate(coords))
            x |= ((x & normal).bit_count() & 1) << piv
            pts.append(x)
        g = [bits[x] for x in pts]
        h = [bits[x ^ s] for x in pts]
        need(sum(g) % 2 == 1 and sum(h) % 2 == 1, 'odd halves')
        G, Hs = fwht([1 - 2 * b for b in g]), fwht([1 - 2 * b for b in h])
        canon = lambda m: m if m % 8 == 2 else -m
        Kg = [canon(abs(v)) for v in G]
        Kh = [canon(abs(v)) for v in Hs]
        need(all(abs(v) in (256,) for v in fwht(Kg)) and all(abs(v) == 256 for v in fwht(Kh)), 'canonical transform alphabet')
        S = [x + y for x, y in zip(Kg, Kh)]
        R = [x - y for x, y in zip(Kg, Kh)]
        hS, hR = fwht(S), fwht(R)
        need(all((u != 0) != (v != 0) and abs(u + v) == 512 for u, v in zip(hS, hR)), 'Lemma 1.1 partition on genuine pair')
        Dfun = [Jres(x) ^ Jres(y) for x, y in zip(Kg, Kh)]
        p = [r // 8 for r in R]
        E = [((pi - di) // 2) % 2 for pi, di in zip(p, Dfun)]
        J1 = [((((-1) ** di) * si - 4) // 16) % 2 for si, di in zip(S, Dfun)]
        if corrupt:
            E[37] ^= 1
        deg_sum, _ = degree([x ^ y for x, y in zip(J1, E)], 8)
        need(deg_sum <= 3, 'Lemma 2.2 coupling on genuine pair')
        dE, cE = degree(E, 8)
        dJ, cJ = degree(J1, 8)
        need(dE <= 4 and dJ <= 4 and [m for m in range(256) if m.bit_count() == 4 and cE[m]] == [m for m in range(256) if m.bit_count() == 4 and cJ[m]], 'shared quartic part')
        # Lemma 3.1 on this pair's own K = rad(B_D) ∩ D^{-1}(0)
        Bm = [[Dfun[(1 << i) ^ (1 << j)] ^ Dfun[1 << i] ^ Dfun[1 << j] ^ Dfun[0] if i != j else 0 for j in range(8)] for i in range(8)]
        rows = [sum(Bm[i][j] << j for j in range(8)) for i in range(8)]
        rad = [a for a in range(256) if all(((rows[i] & a).bit_count() & 1) == 0 for i in range(8))]
        K = [a for a in rad if Dfun[a] == Dfun[0]]
        tau = len(K).bit_length() - 1
        energy_ok = True
        if tau >= 1:
            Kset = set(K)
            reps, seen = [], set()
            for a in range(256):
                if a not in seen:
                    reps.append(a)
                    seen |= {a ^ k for k in K}
            for kap in range(256):
                # characters of K given by x restricted to K
                tot = 0
                for u in reps:
                    hp = sum(p[u ^ k] * (-1) ** ((kap & k).bit_count() % 2) for k in K)
                    hs = sum(S[u ^ k] * (-1) ** ((kap & k).bit_count() % 2) for k in K)
                    tot += hs * hs + 64 * hp * hp
                energy_ok &= tot == 2 ** 18
        need(energy_ok, 'Lemma 3.1 coset energy identity on genuine pair')
        tested.append({'source_sha256_ascii_bits': source['sha256_ascii_bits'], 'normal': normal, 'peak': max(map(abs, S + R)),
                       'D_weight': sum(Dfun), 'tau_K': tau, 'J1_plus_E_degree': deg_sum})
    return tested


H4 = [[(-1) ** ((c & x).bit_count() % 2) for x in range(4)] for c in range(4)]


def rank2_pattern_audit():
    pats = {}
    for v in itertools.product((-1, 0, 1), repeat=4):
        hv = tuple(sum(H4[c][x] * v[x] for x in range(4)) for c in range(4))
        k = sum(1 for t in v if t)
        need(all(e % 2 == k % 2 for e in hv), 'Lemma 6.3 parity')
        if any(abs(e) == 3 for e in hv):
            need(k == 3 and sorted(map(abs, hv)) == [1, 1, 1, 3], 'Lemma 6.5 pattern shape')
        pats[hv] = k
    need(len(pats) == 81, 'pattern count')
    # joint (u,w) 2-variable patterns: S- and R-side vectors share the parity k mod 2
    for ub in itertools.product((0, 1), repeat=4):
        for wb in itertools.product((0, 1), repeat=4):
            Wu = [sum((-1) ** (ub[x] ^ ((c & x).bit_count() % 2)) for x in range(4)) for c in range(4)]
            Ww = [sum((-1) ** (wb[x] ^ ((c & x).bit_count() % 2)) for x in range(4)) for c in range(4)]
            k = sum(1 for x in range(4) if ub[x] != wb[x])
            need(all(((Wu[c] - Ww[c]) // 2) % 2 == k % 2 and ((Wu[c] + Ww[c]) // 2) % 2 == k % 2 for c in range(4)), 'Lemma 6.3 joint parity')
    return len(pats)

def enumerate_profiles(feats, total, targets):
    """Exact set of achievable odd-entry counts: nonneg integer counts n_i over
    feature tuples (f1,f2,f3,f4,odd) with f1,f2,f3 >= 0, sum n_i = total and
    sum n_i*f_j = targets[j]. Exhaustive memoized recursion with sound pruning."""
    from functools import lru_cache
    feats = list(feats)
    need(all(f[0] >= 0 and f[1] >= 0 and f[2] >= 0 for f in feats), 'nonnegative features')

    @lru_cache(maxsize=None)
    def rec(i, rem, t1, t2, t3, t4):
        if t1 < 0 or t2 < 0 or t3 < 0:
            return frozenset()
        if i == len(feats):
            return frozenset([0]) if rem == 0 and t1 == 0 and t2 == 0 and t3 == 0 and t4 == 0 else frozenset()
        f = feats[i]
        out = set()
        for n in range(rem + 1):
            a1, a2, a3 = t1 - n * f[0], t2 - n * f[1], t3 - n * f[2]
            if a1 < 0 or a2 < 0 or a3 < 0:
                break
            for v in rec(i + 1, rem - n, a1, a2, a3, t4 - n * f[3]):
                out.add(v + (n if f[4] else 0))
        return frozenset(out)
    return sorted(rec(0, total, *targets))


def parity_weight_audit(corrupt=False):
    results = {}
    # R side, D=1 coset, ell in {0,1}: per-kappa types (h, Lambda) with W=(4Lambda-16h)/3 integral
    for ell in (0, 1, 2, 3):
        types = []
        for h in range(-4, 5):
            for Lam in range(-ell, ell + 1):
                if (Lam - ell) % 2 or (4 * Lam - 16 * h) % 3:
                    continue
                types.append((h, Lam, (4 * Lam - 16 * h) // 3))
        feats = sorted({(h * h, W * W, Lam * Lam, Lam * h, h % 2) for h, Lam, W in types})
        results['R_D1_ell%d' % ell] = enumerate_profiles(feats, 64, (144 - 2 * ell, 4096, 64 * ell, 4 * ell))
    # S side, a in {0,1}, both coset kinds; kappa=0 carries the delta term
    for Dc in (0, 1):
        sgn = 2 * Dc - 1
        for a in (0, 1):
            types, zero_types = [], []
            for sv in range(-4, 5):
                for Lam in range(-a, a + 1):
                    if (Lam - a) % 2:
                        continue
                    if (4 * Lam - 16 * sv) % 3 == 0:
                        types.append((sv, Lam, (4 * Lam - 16 * sv) // 3))
                    if (sgn * 32 + 4 * Lam - 16 * sv) % 3 == 0:
                        zero_types.append((sv, Lam, (sgn * 32 + 4 * Lam - 16 * sv) // 3))
            feats = sorted({(s * s, W * W, L * L, L * s, s % 2) for s, L, W in types})
            ws = set()
            for s0, L0, W0 in zero_types:
                tgt = (140 - 2 * a + sgn * 4 * s0 - s0 * s0, 4096 - W0 * W0, 64 * a - L0 * L0,
                       4 * a + sgn * 2 * L0 - L0 * s0)
                if tgt[0] < 0 or tgt[1] < 0 or tgt[2] < 0:
                    continue
                for v in enumerate_profiles(feats, 63, tgt):
                    ws.add(v + (s0 % 2))
            results['S_D%d_a%d' % (Dc, a)] = sorted(ws)
    expected = {'R_D1_ell0': [16], 'R_D1_ell1': [42], 'S_D0_a0': [12, 16], 'S_D0_a1': [42, 46],
                'S_D1_a0': [12, 16], 'S_D1_a1': [42, 46]}
    if corrupt:
        expected['R_D1_ell1'] = [16]
    need({k: v for k, v in results.items() if k in expected} == expected, 'Lemma 6.4 parity-weight table')
    need(results['R_D1_ell2'] == [12, 16, 20, 24, 28] and results['R_D1_ell3'] == list(range(30, 59, 4)), 'Lemma 6.8 audited tables')
    # Lemma 6.8 congruence classes: wt(pi) = 2*ell (mod 4) and 2*a (mod 4)
    need(all(w % 4 == (2 * ell) % 4 for ell in range(4) for w in results['R_D1_ell%d' % ell]), 'Lemma 6.8 R class')
    need(all(w % 4 == (2 * a) % 4 for Dc in (0, 1) for a in (0, 1) for w in results['S_D%d_a%d' % (Dc, a)]), 'Lemma 6.8 S class')
    # Corollary 6.6 logic: parameters <=1 combinations consistent with shared wt(pi)
    allowed = []
    for ells in itertools.product((0, 1), repeat=3):
        if sum(1 for e in ells if e == 0) > 1:
            continue  # Lemma 6.5
        for avec in itertools.product((0, 1), repeat=4):
            sets = [set(results['R_D1_ell%d' % e]) for e in ells] + [set(results['S_D%d_a%d' % (0 if i == 0 else 1, av)]) for i, av in enumerate(avec)]
            common = set.intersection(*sets)
            if not common:
                continue
            c, atot = sum(ells), sum(avec)
            for z in range(8, 65, 2):
                if z == 10 or (z + 2 * c) % 8 or atot % 4 or 2 * (atot + c) + z > 64:
                    continue
                if min(common) > 64 - z:
                    continue
                allowed.append((ells, avec, z, sorted(common)))
    need(all(al[0] == (1, 1, 1) and al[1] == (1, 1, 1, 1) and al[2] == 18 for al in allowed) and allowed, 'Corollary 6.6')
    return results, allowed


def relaxation_audit(rel):
    """Verify one SAT relaxation witness, checking exactly the constraint families it claims."""
    need(rel['status'] == 'sat' and 'aux' in rel, 'relaxation witness absent')
    amod4, s_energy, s_cross = rel.get('amod4', True), rel.get('s_energy', True), rel.get('s_cross', True)
    def walsh2(bits):
        return [sum((-1) ** (bits[x] ^ ((c & x).bit_count() % 2)) for x in range(4)) for c in range(4)]
    pats = []
    for rec in rel['pattern_counts']:
        Wu, Ww = walsh2(rec['u']), walsh2(rec['w'])
        h = [(Wu[c] - Ww[c]) // 2 for c in range(4)]
        s = [(Wu[c] + Ww[c]) // 2 for c in range(4)]
        k = sum(1 for x in range(4) if rec['u'][x] != rec['w'][x])
        pats.append((h, s, k, rec['count']))
    z, ell, a = rel['z'], rel['ell'], rel['a']
    c, atot = sum(ell), sum(a)
    need(sum(n for *_, n in pats) == 64, 'relaxation kappa count')
    need(z >= 8 and z % 2 == 0 and z != 10 and 2 * (atot + c) + z <= 64 and (z + 2 * c) % 8 == 0, 'relaxation scalars')
    if amod4:
        need(atot % 4 == 0, 'relaxation a mod 4')
    need(sum(h[0] ** 2 * n for h, s, k, n in pats) == 64 - z and sum(h[0] * n for h, s, k, n in pats) == 0, 'relaxation D0 coset')
    need(4 * sum(k * n for h, s, k, n in pats) == 496 - z - 2 * c, 'relaxation w_R')
    aux = rel['aux']
    for ci, cc in enumerate((1, 2, 3)):
        ys = aux['R%d' % cc]
        marg = Counter()
        for h, L, n in ys:
            need(abs(L) <= ell[ci] and (ell[ci] - L) % 2 == 0 and (4 * L - 16 * h) % 3 == 0, 'R aux type')
            marg[h] += n
        pm = Counter()
        for h, s, k, n in pats:
            pm[h[cc]] += n
        need(+marg == +pm, 'R aux marginal')
        W = lambda h, L: (4 * L - 16 * h) // 3
        need(sum(W(h, L) ** 2 * n for h, L, n in ys) == 4096, 'R Parseval')
        need(sum(h * h * n for h, L, n in ys) == 144 - 2 * ell[ci], 'R h energy')
        need(sum(L * L * n for h, L, n in ys) == 64 * ell[ci], 'R Lambda energy')
        need(sum(L * h * n for h, L, n in ys) == 4 * ell[ci], 'R Lambda-h')
    k0 = rel['kappa0_pattern']
    Wu, Ww = walsh2(k0['u']), walsh2(k0['w'])
    s_k0 = [(Wu[c] + Ww[c]) // 2 for c in range(4)]
    need(any(r['u'] == k0['u'] and r['w'] == k0['w'] for r in rel['pattern_counts']), 'kappa0 pattern present')
    for cc in range(4):
        sgn = -1 if cc == 0 else 1
        ys = aux['S%d' % cc]
        marg = Counter()
        zeros = []
        for sv, L, d0, n in ys:
            need(abs(L) <= a[cc] and (a[cc] - L) % 2 == 0 and (sgn * 32 * d0 + 4 * L - 16 * sv) % 3 == 0, 'S aux type')
            marg[sv] += n
            if d0:
                zeros.append((sv, L, n))
        pm = Counter()
        for h, s, k, n in pats:
            pm[s[cc]] += n
        need(+marg == +pm, 'S aux marginal')
        need(len(zeros) == 1 and zeros[0][2] == 1 and zeros[0][0] == s_k0[cc], 'S kappa0 bookkeeping')
        s0, L0 = zeros[0][0], zeros[0][1]
        W = lambda sv, L, d0: (sgn * 32 * d0 + 4 * L - 16 * sv) // 3
        need(sum(W(sv, L, d0) ** 2 * n for sv, L, d0, n in ys) == 4096, 'S Parseval')
        need(sum(L * L * n for sv, L, d0, n in ys) == 64 * a[cc], 'S Lambda energy')
        if s_energy:
            need(sum(sv * sv * n for sv, L, d0, n in ys) == 140 - 2 * a[cc] + 4 * sgn * s0, 'S s energy')
        if s_cross:
            need(sum(sv * L * n for sv, L, d0, n in ys) == 4 * a[cc] + 2 * sgn * L0, 'S Lambda-s')
    return {'z': z, 'ell': ell, 'a': a, 'distinct_patterns': len(pats),
            'constraint_families': {'a_mod_4': amod4, 'S_energy': s_energy, 'S_cross': s_cross}}


def probe_audit():
    verified, recorded = {}, {}
    for path in sorted((ROOT / 'results').glob('rank2-probe-*.json')):
        rec = json.loads(path.read_text())
        recorded[path.name] = {'status': rec['status'], 'seconds': rec['seconds'], 'limit': rec['limit'],
                               'a_mod_4': rec['amod4'], 'S_energy': rec['s_energy'], 'S_cross': rec['s_cross']}
        need(rec['status'] in ('sat', 'unknown', 'unsat'), 'probe status')
        if rec['status'] == 'sat' and 'aux' in rec:
            verified[path.name] = relaxation_audit(rec)
            full = dict(rec, amod4=True, s_energy=True, s_cross=True)
            try:
                relaxation_audit(full)
                verified[path.name]['satisfies_full_family'] = True
            except ValueError:
                verified[path.name]['satisfies_full_family'] = False
    need(verified, 'no verified relaxation witness')
    need(any(v['satisfies_full_family'] for v in verified.values()), 'no full-family relaxation witness')
    # No UNKNOWN or solver UNSAT is promoted: only SAT witnesses carry a claim.
    return verified, recorded


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--corrupt-witness', action='store_true')
    ap.add_argument('--corrupt-threshold', action='store_true')
    ap.add_argument('--corrupt-parity-table', action='store_true')
    ap.add_argument('--corrupt-coupling', action='store_true')
    args = ap.parse_args()
    started = time.monotonic()
    raw = (ROOT / 'results/explore.json.gz').read_bytes()
    produced = json.loads(gzip.decompress(raw))
    need(produced['input_sha256'] == PIN, 'producer input pin')
    structures = structure_audit(produced, args.corrupt_threshold)
    scalars = scalar_witness_audit(produced, args.corrupt_witness)
    representation_audit()
    genuine = genuine_pair_audit(args.corrupt_coupling)
    npat = rank2_pattern_audit()
    parity, allowed = parity_weight_audit(args.corrupt_parity_table)
    relax, probe_status = probe_audit()
    need(produced['rank2_joint_relaxation_witness']['status'] in ('sat', 'unknown'), 'producer relaxation status')
    out = {'status': 'PASS', 'scope': 'Independent exact audit; no exclusion of any remaining type is claimed.',
           'structures': structures, 'scalar_witness_stats': scalars, 'representations_all_28_pairs': True,
           'genuine_cap32_pairs_checked': genuine, 'rank2_patterns_checked': npat,
           'parity_weight_table': parity, 'corollary_6_6_surviving_low_parameter_cases': [list(map(list, x[:2])) + [x[2], x[3]] for x in allowed],
           'rank2_relaxation_witnesses_verified': relax, 'rank2_probe_statuses_no_claim_unless_sat': probe_status,
           'producer_full_relaxation_status': produced['rank2_joint_relaxation_witness']['status'],
           'producer_output_sha256': hashlib.sha256(raw).hexdigest(),
           'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
           'elapsed_seconds': time.monotonic() - started}
    (ROOT / 'results/audit.json').write_text(json.dumps(out, indent=2) + '\n')
    print(json.dumps({'status': 'PASS', 'elapsed_seconds': out['elapsed_seconds'], 'relaxation': relax,
                      'parity': parity}, sort_keys=True))


if __name__ == '__main__':
    main()
