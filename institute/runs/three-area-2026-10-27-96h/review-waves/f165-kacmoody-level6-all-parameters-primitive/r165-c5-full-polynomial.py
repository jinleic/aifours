#!/usr/bin/env python3
# r165 reviewer-authored control C5: EXACT bivariate determinant polynomial for ONE canonical type,
#   f(x,y) = det( 24*Omega(r=6+x, s=6+y) | P_(a,b) ),  P = f1/f2-lowest space of L_6(M) at degree (a,b),
# reconstructed rigorously:
#   * entries of Omega on P are affine in (r,s)  =>  total degree of f <= m = dim P;
#   * values mod p on the unisolvent triangle {(i,j): i+j<=m} -> Newton forward differences -> monomials mod p;
#   * Cauchy bound |coef| <= max_{|x|=|y|=1}|f| <= Nmax^m with Nmax the max word-column 1-norm of the
#     word-space operator (which restricts to 24*Omega on Lie elements), so CRT over primes with
#     product > 2*bound gives the exact integer coefficients.
# Then: sign census of coefficients, independent-prime off-grid evaluation check (positive control),
# a perturbed-coefficient negative control, and re-expansion on the fifth rays r=5 / s=5 (informative).
# Usage: r165-c5-full-polynomial.py a b
import sys
sys.dont_write_bytecode = True
import json, hashlib, importlib.util, os, time, random
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r165model', os.path.join(HERE, 'r165-c2-omega-model.py'))
K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)
CENSUS = json.load(open(os.path.join(HERE, 'r165-c1-character-census.out.json')))
MULT = {(r['a'], r['b']): r['mult'] for r in CENSUS['level6_table']}

def log(msg):
    print(msg, file=sys.stderr, flush=True)

def column_norm_bound(a, b, shift=6):
    """max over words w of sum_terms |c0+shift*cr+shift*cs| + |cr| + |cs| for the full word image of w."""
    n = 6
    ws = K.words_of_degree(n, a, b)
    best = 0
    for w in ws:
        Fj = {}
        for j in range(8):
            d = {}
            K.F_pencil(j, w, n, d)
            Fj[j] = d
        o = {}
        for (i, j), kw in K.KW.items():
            for y, (c0, cr, cs) in Fj[j].items():
                for key, sg in (((i << (3 * (n - 1))) | y, kw), ((y << 3) | i, -kw)):
                    e = o.get(key)
                    if e is None:
                        o[key] = [sg * c0, sg * cr, sg * cs]
                    else:
                        e[0] += sg * c0; e[1] += sg * cr; e[2] += sg * cs
        tot = sum(abs(c0 + shift * cr + shift * cs) + abs(cr) + abs(cs) for (c0, cr, cs) in o.values())
        best = max(best, tot)
    return best

def restricted_pencil(B, p):
    A = np.vstack([B['F1Y'], B['F2Y']])
    Kp, free, rank = K.rref_kernel_mod(A, p)
    Mc = []
    for c in range(3):
        Y = K.matmul_mod(B['R'][c], Kp, p)
        Z = K.lower_unit_solve_mod(B['T'], Y, p)
        Mc.append(Z[free, :] % p)
    return Kp.shape[1], Mc

def stirling_matrix(m, p):
    # S[a][i] = s(i,a) / i!  (signed Stirling numbers of the first kind), mod p
    s = [[0] * (m + 1) for _ in range(m + 1)]
    s[0][0] = 1
    for i in range(m):
        for a in range(i + 2):
            v = (s[i][a - 1] if a >= 1 else 0) - i * s[i][a]
            s[i + 1][a] = v % p
    fact = 1
    S = np.zeros((m + 1, m + 1), dtype=np.int64)
    for i in range(m + 1):
        if i:
            fact = fact * i % p
        inv = pow(fact, p - 2, p)
        for a in range(i + 1):
            S[a, i] = s[i][a] * inv % p
    return S

def poly_mod_p(M0, Mr, Ms, m, p, shift=6):
    pts = [(shift + i, shift + j) for i in range(m + 1) for j in range(m + 1 - i)]
    vals = K.batch_det_mod(M0, Mr, Ms, pts, p)
    V = {}
    for (r, s), v in zip(pts, vals):
        V[(r - shift, s - shift)] = v
    # forward differences: first in y for each x, then in x
    DY = {}
    for i in range(m + 1):
        seq = [V[(i, j)] for j in range(m + 1 - i)]
        for j in range(m + 1 - i):
            DY[(i, j)] = seq[0]
            seq = [(seq[t + 1] - seq[t]) % p for t in range(len(seq) - 1)]
    D = np.zeros((m + 1, m + 1), dtype=np.int64)
    for j in range(m + 1):
        seq = [DY[(i, j)] for i in range(m + 1 - j)]
        for i in range(m + 1 - j):
            D[i, j] = seq[0]
            seq = [(seq[t + 1] - seq[t]) % p for t in range(len(seq) - 1)]
    S = stirling_matrix(m, p)
    C = (S @ D) % p
    C = (C @ S.T) % p
    return C

def crt_pair(a1, m1, a2, m2):
    t = ((a2 - a1) * pow(m1, -1, m2)) % m2
    return a1 + m1 * t, m1 * m2

def eval_poly(coef, x, y):
    tot = 0
    for (i, j), c in coef.items():
        tot += c * x ** i * y ** j
    return tot

def shift_poly(coef, dx, dy):
    """coefficients of g(X,Y) = f(X+dx, Y+dy)."""
    from math import comb
    out = {}
    for (i, j), c in coef.items():
        for a in range(i + 1):
            ca = c * comb(i, a) * dx ** (i - a)
            for b in range(j + 1):
                v = ca * comb(j, b) * dy ** (j - b)
                if v:
                    out[(a, b)] = out.get((a, b), 0) + v
    return {k: v for k, v in out.items() if v}

if __name__ == '__main__':
    a, b = int(sys.argv[1]), int(sys.argv[2])
    res = {'start_clock': K.clock(), 'type': [a, b],
           'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
           'model_sha256': hashlib.sha256(open(os.path.join(HERE, 'r165-c2-omega-model.py'), 'rb').read()).hexdigest()}
    m = MULT[(a, b)]
    B = K.build_type(6, a, b, want_d3=False, log=log)
    Nmax = column_norm_bound(a, b)
    bound = Nmax ** m
    res.update({'m': m, 'NL': B['NL'], 'NW': B['NW'], 'Nmax_column_norm': Nmax,
                'coef_bound_bits': bound.bit_length()})
    log(f'm={m} Nmax={Nmax} bound bits={bound.bit_length()} at {K.clock()}')
    primes = K.primes_below(2 ** 25, 400)
    check_prime = primes[-1]
    used, modulus, crt = [], 1, None
    idx = 0
    t0 = time.time()
    while modulus <= 4 * bound:
        p = primes[idx]; idx += 1
        mp, Mc = restricted_pencil(B, p)
        if mp != m:
            log(f'prime {p}: kernel dim {mp} != {m}; skipped')
            continue
        C = poly_mod_p(Mc[0], Mc[1], Mc[2], m, p)
        if crt is None:
            crt = {(i, j): int(C[i, j]) for i in range(m + 1) for j in range(m + 1 - i)}
            modulus = p
        else:
            for key in crt:
                crt[key], _ = crt_pair(crt[key], modulus, int(C[key]), p)
            modulus *= p
        used.append(p)
        log(f'prime #{len(used)} {p} done; modulus bits {modulus.bit_length()} elapsed {time.time() - t0:.0f}s at {K.clock()}')
    coef = {}
    for key, v in crt.items():
        if v > modulus // 2:
            v -= modulus
        if v:
            coef[key] = v
    res['primes_used'] = used
    res['modulus_bits'] = modulus.bit_length()
    # positive control: independent prime, off-grid points, direct determinant vs reconstructed polynomial
    mp, Mc = restricted_pencil(B, check_prime)
    random.seed(16545)
    test_pts = [(6, 6), (5, 5), (1, 1), (6 + 137, 6 + 251), (6 + 999, 6 + 3), (2, 9)] + \
               [(random.randint(1, 10 ** 6), random.randint(1, 10 ** 6)) for _ in range(6)]
    direct = [K.det_mod((Mc[0] + r * Mc[1] + s * Mc[2]) % check_prime, check_prime) for (r, s) in test_pts]
    direct_batch = K.batch_det_mod(Mc[0], Mc[1], Mc[2], test_pts, check_prime)
    recon = [eval_poly(coef, r - 6, s - 6) % check_prime for (r, s) in test_pts]
    res['check_prime'] = check_prime
    res['offgrid_check_points'] = test_pts
    res['batch_det_equals_single_det'] = direct == direct_batch
    res['offgrid_check_pass'] = direct == recon and mp == m
    # negative control: perturb one coefficient by +1 -> mismatch expected at generic points
    bad = dict(coef)
    key0 = max(bad, key=lambda k: (k[0] + k[1], k))
    bad[key0] = bad[key0] + 1
    recon_bad = [eval_poly(bad, r - 6, s - 6) % check_prime for (r, s) in test_pts]
    res['NEG_perturbed_coefficient_passes_check'] = recon_bad == direct
    vals = list(coef.values())
    res['nonzero_coefficients'] = len(vals)
    res['monomials_total_degree_le_m'] = (m + 1) * (m + 2) // 2
    res['positive_coefficients'] = sum(1 for v in vals if v > 0)
    res['negative_coefficients'] = sum(1 for v in vals if v < 0)
    res['constant_term_sign'] = (coef.get((0, 0), 0) > 0) - (coef.get((0, 0), 0) < 0)
    res['max_total_degree_present'] = max(i + j for (i, j) in coef)
    res['zero_coefficient_monomials'] = sorted([list(k) for k in crt if k not in coef])[:60]
    res['coef_bits_max'] = max(abs(v).bit_length() for v in vals)
    res['constant_term_bits'] = abs(coef.get((0, 0), 0)).bit_length()
    sym = all(coef.get((i, j)) == coef.get((j, i)) for (i, j) in coef)
    res['symmetric_in_x_y'] = sym
    # informative: exact values at small parameters and the fifth rays / shift-5 re-expansion
    res['exact_sign_at_small_points'] = {f'{r},{s}': ((lambda v: (v > 0) - (v < 0))(eval_poly(coef, r - 6, s - 6)))
                                         for r in range(1, 7) for s in range(1, 7)}
    g5 = shift_poly(coef, -1, -1)
    res['shift5_negative_coefficients'] = sum(1 for v in g5.values() if v < 0)
    res['shift5_nonzero_coefficients'] = len(g5)
    rayr5 = {}
    for (i, j), v in g5.items():
        if i == 0:
            rayr5[j] = v
    rays5 = {}
    for (i, j), v in g5.items():
        if j == 0:
            rays5[i] = v
    res['ray_r5_s5plus_t_negative_coeffs'] = sum(1 for v in rayr5.values() if v < 0)
    res['ray_r5_degree'] = max(rayr5) if rayr5 else None
    res['ray_s5_r5plus_t_negative_coeffs'] = sum(1 for v in rays5.values() if v < 0)
    res['ray_s5_degree'] = max(rays5) if rays5 else None
    res['corner_5_5_value_sign'] = (lambda v: (v > 0) - (v < 0))(g5.get((0, 0), 0))
    blob = json.dumps(sorted([[i, j, str(v)] for (i, j), v in coef.items()]), separators=(',', ':')).encode()
    res['coefficient_list_sha256'] = hashlib.sha256(blob).hexdigest()
    with open(os.path.join(HERE, f'r165-c5-poly-{a}{b}-coefficients.json'), 'wb') as fh:
        fh.write(blob + b'\n')
    res['end_clock'] = K.clock()
    print(json.dumps(res, indent=1))
