#!/usr/bin/env python3
"""Exact small-prime verification of the Codex consult claims
(review/codex-consult-residual/proof_text.md), against the lane's definitions:

  unit option set  Opt(U) = {(val T, |T|/2 mod p) : T nonempty, even #refl, |T| even}
  depth(U)         = max d with e_const in span{(m(s))_{deg m < d} : s in Opt(U)}
                     (= exists theta = [0] + sum c_s [s] in J^d; tiling.depth_at_least)
  tiling           = partition of the cyclic word into arcs (top-level blocks);
                     it proves the theorem iff sum depth(block) >= 2p-1 (Lemma G).

Sections: A membership of w_p in Res; B direct solution; C max short-block tiling
depth (all partitions into arcs of length <= Lb, exact block depths) with
counter-controls; D lemma checks.  Usage: verify_consult.py [primes...]
"""
import sys, os, json, random, itertools
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tiling import unit_points, depth_at_least
import coverage_all as ca

def depth(unit, p):
    pts = unit_points(tuple(unit), p)
    d = 0
    while d <= len(unit) // 2 and depth_at_least(pts, d + 1, p):
        d += 1
    return d

def R(x): return ('R', x)
def F(y): return ('F', y)

def w_family(p, variant='w'):
    if variant == 'w':      # consult w_p
        runs = [('F', 0, p - 2), ('R', 1, p - 2), ('F', 1, p - 2), ('R', 1, p - 2), ('F', 2, 4), ('R', 1, 3)]
    elif variant == 'short_first_rot':   # counter-control: first rotation run p-3
        runs = [('F', 0, p - 2), ('R', 1, p - 3), ('F', 1, p - 2), ('R', 1, p - 2), ('F', 2, 5), ('R', 1, 3)]
    elif variant == 'even_middle':       # counter-control: middle reflection run even
        runs = [('F', 0, p - 2), ('R', 1, p - 2), ('F', 1, p - 1), ('R', 1, p - 2), ('F', 2, 3), ('R', 1, 3)]
    w = []
    for c, v, l in runs:
        w += [(c, v % p)] * l
    assert len(w) == 4 * p - 1
    return w

def lemmaA_max(word, p):
    """max over all zone-sign patterns of the rotation runs and all k of the CD bound."""
    ys, gaps = ca.gaps_of(word)
    runs = [g for g in gaps if g]
    best = -10**9
    for signs in itertools.product((1, -1), repeat=len(runs)):
        signed = [s * x % p for s, g in zip(signs, runs) for x in g]
        for k in range(1, len(signed) + 1):
            best = max(best, ca.lemmaA_bound(signed, k, p))
    return best

def section_A(p, w):
    ys, gaps = ca.gaps_of(w)
    Rn = sum(1 for c, _ in w if c == 'R')
    # odd reflection runs (cyclic)
    n = len(w); s = next(i for i in range(n) if w[i][0] == 'F' and w[i - 1][0] == 'R')
    ww = w[s:] + w[:s]; lens = []; cur = 0
    for c, _ in ww:
        if c == 'F': cur += 1
        elif cur: lens.append(cur); cur = 0
    if cur: lens.append(cur)
    oF = sum(1 for l in lens if l % 2)
    return {'EGZ': Rn >= 3 * p - 1, 'P': ca.tool_P(ys, gaps, p), 'DBL': ca.tool_DBL(ys, gaps, p),
            'DAV': ca.tool_DAV(ys, gaps, p), 'RIGID': ca.tool_RIGID(w, p), 'RPRIME': ca.tool_RPRIME(w, p),
            'T0(oF<=1)': oF <= 1, 'LemmaA_max_bound': lemmaA_max(w, p), 'LemmaA': lemmaA_max(w, p) >= p}

def section_B(p, w):
    # consult's selection: all initial sigma_0, first sigma_1, second rotation run, final 3 rotations
    idx = list(range(0, p - 2)) + [2 * (p - 2)] + list(range(3 * (p - 2), 4 * (p - 2))) + list(range(4 * p - 4, 4 * p - 1))
    v, e = 0, 1
    for i in idx:
        c, x = w[i]
        v = (v + e * x) % p
        if c == 'F': e = -e
    return {'size': len(idx), 'increasing': idx == sorted(idx), 'product': (v, e), 'dp_exists': ca.has_solution(w, p)}

def max_tiling_depth(w, p, Lb):
    n = len(w)
    cache = {}
    def bd(s, L):
        key = (s, L)
        if key not in cache:
            cache[key] = depth([w[(s + i) % n] for i in range(L)], p)
        return cache[key]
    best = -1
    for cut in range(n):
        dp = [-10**9] * (n + 1); dp[0] = 0
        for i in range(n):
            if dp[i] < 0: continue
            for L in range(1, Lb + 1):
                if i + L > n: break
                val = dp[i] + bd((cut + i) % n, L)
                if val > dp[i + L]: dp[i + L] = val
        best = max(best, dp[n])
    return best

def section_D(p, rng):
    out = {}
    # four-letter classification, exhaustive up to translation (a=0) and scaling
    def norm_iter(k):
        for vals in itertools.product(range(p), repeat=k):
            nz = [v for v in vals if v]
            if nz and nz[0] != 1: continue
            yield vals
    bad = Counter4 = {'frrf': 0, 'rfrf': 0, 'frfr': 0, 'fixed_shapes_nonfull': 0}
    for C, x, z in norm_iter(3):
        S = (x + z) % p
        for shape, unit, pred in [
            ('frrf', [F(0), R(x), R(z), F(-C)], C == S and C != 0),
            ('rfrf', [R(x), F(0), R(z), F(-C)], C == S and z != 0),
            ('frfr', [F(0), R(x), F(-C), R(z)], C == S and x != 0)]:
            nonfull = depth(unit, p) < 2
            if nonfull != pred: bad[shape] += 1
    for vals in itertools.product(range(p), repeat=4) if p <= 7 else [tuple(rng.randrange(p) for _ in range(4)) for _ in range(3000)]:
        a, b, c, d = vals
        for unit in ([R(a), R(b), R(c), R(d)], [F(a), F(b), F(c), F(d)], [R(a), R(b), F(c), F(d)],
                     [F(a), F(b), R(c), R(d)], [R(a), F(b), F(c), R(d)]):
            if depth(unit, p) < 2: bad['fixed_shapes_nonfull'] += 1
    out['four_letter_mismatches'] = bad
    # constant-rotation bracket formula
    mism = 0; checked = 0
    for n_ in range(1, min(2 * p - 2, 12) + 1):
        m = n_ // 2
        for x in (0, 1):
            for C in range(p):
                unit = [F(0)] + [R(x)] * n_ + [F(-C)]
                full = depth(unit, p) >= m + 1
                pred = (x == 0) or (C % p not in {((4 * j - 2) * x) % p for j in range(1, m + 1)})
                checked += 1; mism += (full != pred)
    out['constant_bracket'] = {'checked': checked, 'mismatches': mism}
    # four arbitrary rotations between reflections
    mism = 0; checked = 0
    for C in range(p):
        for xs in itertools.combinations_with_replacement(range(p), 4):
            if p > 7 and rng.random() > 0.15: continue
            unit = [F(0)] + [R(x) for x in xs] + [F(-C)]
            full = depth(unit, p) >= 3
            allx = len(set(xs)) == 1 and xs[0] != 0
            pred = not (allx and C % p in {(2 * xs[0]) % p, (6 * xs[0]) % p})
            checked += 1; mism += (full != pred)
    out['four_rotation_bracket'] = {'checked': checked, 'mismatches': mism}
    # six-letter universal shapes
    shapes = {'FRRFFF': 'FRRFFF', 'FFFRRF': 'FFFRRF', 'FRFFRF': 'FRFFRF'}
    res6 = {}
    for name, sh in shapes.items():
        nonfull = 0; tot = 0
        it = itertools.product(range(p), repeat=6) if p <= 5 else (tuple(rng.randrange(p) for _ in range(6)) for _ in range(4000))
        for vals in it:
            unit = [(c, v) for c, v in zip(sh, vals)]
            tot += 1; nonfull += depth(unit, p) < 3
        res6[name] = {'tested': tot, 'nonfull': nonfull, 'exhaustive': p <= 5}
    out['six_letter'] = res6
    # eight-letter degenerate unit
    out['sigma0_rho1^4_sigma-6^3_depth'] = depth([F(0)] + [R(1)] * 4 + [F(-6)] * 3, p)
    # insertion lemma
    viol = 0
    for _ in range(300):
        L = rng.randrange(2, 7)
        U = [(rng.choice('RF'), rng.randrange(p)) for _ in range(L)]
        d0 = depth(U, p)
        pos = rng.randrange(0, L + 1)
        if rng.random() < 0.5:
            v = rng.randrange(p); ins = [R(v), R(-v % p)]
        else:
            y = rng.randrange(p); ins = [F(y), F(y)]
        if depth(U[:pos] + ins + U[pos:], p) < d0 + 1: viol += 1
    out['insertion_violations_of_300'] = viol
    return out

def main():
    primes = [int(a) for a in sys.argv[1:]] or [5, 7, 11, 13]
    rng = random.Random(20261017)
    report = {}
    for p in primes:
        r = {}
        w = w_family(p)
        r['A_membership_tools_true'] = section_A(p, w)
        r['B_direct_solution'] = section_B(p, w)
        r['C_max_depth_blocks_lt_p'] = max_tiling_depth(w, p, p - 1)
        r['C_target'] = 2 * p - 1
        r['C_max_depth_blocks_le_p'] = max_tiling_depth(w, p, p)
        for var in ('short_first_rot', 'even_middle'):
            wv = w_family(p, var)
            r['C_counter_' + var + '_blocks_lt_p'] = max_tiling_depth(wv, p, p - 1)
        if p <= 11:
            r['D_lemmas'] = section_D(p, rng)
        report[p] = r
        print(p, json.dumps(r), flush=True)
    json.dump(report, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'evidence', 'consult_verification.json'), 'w'), indent=1)

if __name__ == '__main__':
    main()
