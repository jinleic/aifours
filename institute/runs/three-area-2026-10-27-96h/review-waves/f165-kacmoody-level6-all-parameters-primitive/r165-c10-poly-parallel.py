#!/usr/bin/env python3
# r165 reviewer-authored control C10: the C5 exact reconstruction, split over worker processes by prime
# (same model, same interpolation, same Cauchy bound), for the largest canonical type.
#   worker a b k W  : primes with index = k (mod W) from the deterministic list; writes residues
#   combine a b W   : CRT + the same analysis/positive+negative controls as C5
# For a type that is self-transposed, OPTIONAL mirror evaluation f(i,j)=f(j,i) halves the determinant work;
# the symmetry is NOT assumed in the final check: combine evaluates direct determinants at random
# asymmetric off-grid points with an unused prime.
import sys
sys.dont_write_bytecode = True
import json, hashlib, importlib.util, os, time, random
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r165model', os.path.join(HERE, 'r165-c2-omega-model.py'))
K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)
spec5 = importlib.util.spec_from_file_location('r165c5', os.path.join(HERE, 'r165-c5-full-polynomial.py'))
C5 = importlib.util.module_from_spec(spec5); spec5.loader.exec_module(C5)
CENSUS = json.load(open(os.path.join(HERE, 'r165-c1-character-census.out.json')))
MULT = {(r['a'], r['b']): r['mult'] for r in CENSUS['level6_table']}

def log(msg):
    print(msg, file=sys.stderr, flush=True)

def poly_mod_p_mirror(M0, Mr, Ms, m, p, shift=6):
    pts = [(shift + i, shift + j) for i in range(m + 1) for j in range(i, m + 1 - i)]
    vals = K.batch_det_mod(M0, Mr, Ms, pts, p)
    V = {}
    for (r, s), v in zip(pts, vals):
        i, j = r - shift, s - shift
        V[(i, j)] = v
        V[(j, i)] = v
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
    S = C5.stirling_matrix(m, p)
    return ((S @ D) % p @ S.T) % p

def plan(a, b):
    m = MULT[(a, b)]
    Nmax = C5.column_norm_bound(a, b)
    bound = Nmax ** m
    primes = K.primes_below(2 ** 25, 400)
    need, mod = [], 1
    for p in primes[:-1]:
        if mod > 4 * bound:
            break
        need.append(p); mod *= p
    return m, Nmax, bound, need, primes[-1]

if __name__ == '__main__':
    mode, a, b = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    mirror = (a == b)
    if mode == 'worker':
        k, W = int(sys.argv[4]), int(sys.argv[5])
        m, Nmax, bound, need, _ = plan(a, b)
        B = K.build_type(6, a, b, want_d3=False, log=log)
        out = {'start_clock': K.clock(), 'type': [a, b], 'k': k, 'W': W, 'mirror': mirror, 'residues': {}}
        for idx, p in enumerate(need):
            if idx % W != k:
                continue
            mp, Mc = C5.restricted_pencil(B, p)
            if mp != m:
                out['residues'][str(p)] = None
                continue
            C = (poly_mod_p_mirror if mirror else C5.poly_mod_p)(Mc[0], Mc[1], Mc[2], m, p)
            out['residues'][str(p)] = [int(C[i, j]) for i in range(m + 1) for j in range(m + 1 - i)]
            log(f'worker {k}: prime {p} done at {K.clock()}')
        out['end_clock'] = K.clock()
        with open(os.path.join(HERE, f'r165-c10-residues-{a}{b}-{k}of{W}.json'), 'w') as fh:
            json.dump(out, fh)
    elif mode == 'combine':
        W = int(sys.argv[4])
        m, Nmax, bound, need, check_prime = plan(a, b)
        res = {'start_clock': K.clock(), 'type': [a, b], 'm': m, 'Nmax_column_norm': Nmax,
               'coef_bound_bits': bound.bit_length(), 'mirror_evaluation_used': mirror,
               'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
               'model_sha256': hashlib.sha256(open(os.path.join(HERE, 'r165-c2-omega-model.py'), 'rb').read()).hexdigest()}
        keys = [(i, j) for i in range(m + 1) for j in range(m + 1 - i)]
        resid, files = {}, []
        for k in range(W):
            fn = os.path.join(HERE, f'r165-c10-residues-{a}{b}-{k}of{W}.json')
            files.append({'file': os.path.basename(fn), 'sha256': hashlib.sha256(open(fn, 'rb').read()).hexdigest()})
            d = json.load(open(fn))
            for p, v in d['residues'].items():
                assert v is not None, f'kernel dimension mismatch at prime {p}'
                resid[int(p)] = v
        assert sorted(resid) == sorted(need), 'missing primes'
        res['residue_files'] = files
        crt = [0] * len(keys); modulus = 1
        for p in need:
            v = resid[p]
            if modulus == 1:
                crt = list(v); modulus = p
            else:
                crt = [C5.crt_pair(x, modulus, y, p)[0] for x, y in zip(crt, v)]
                modulus *= p
        coef = {}
        for key, v in zip(keys, crt):
            if v > modulus // 2:
                v -= modulus
            if v:
                coef[key] = v
        res['primes_used'] = len(need)
        res['modulus_bits'] = modulus.bit_length()
        B = K.build_type(6, a, b, want_d3=False, log=log)
        mp, Mc = C5.restricted_pencil(B, check_prime)
        random.seed(16544)
        test_pts = [(6, 6), (5, 5), (1, 1), (6 + 137, 6 + 251), (6 + 251, 6 + 137), (6 + 999, 6 + 3), (2, 9)] + \
                   [(random.randint(1, 10 ** 6), random.randint(1, 10 ** 6)) for _ in range(6)]
        direct = [K.det_mod((Mc[0] + r * Mc[1] + s * Mc[2]) % check_prime, check_prime) for (r, s) in test_pts]
        recon = [C5.eval_poly(coef, r - 6, s - 6) % check_prime for (r, s) in test_pts]
        res['check_prime'] = check_prime
        res['offgrid_check_points'] = test_pts
        res['offgrid_check_pass'] = direct == recon and mp == m
        bad = dict(coef)
        key0 = max(bad, key=lambda kk: (kk[0] + kk[1], kk))
        bad[key0] += 1
        res['NEG_perturbed_coefficient_passes_check'] = [C5.eval_poly(bad, r - 6, s - 6) % check_prime for (r, s) in test_pts] == direct
        vals = list(coef.values())
        res['nonzero_coefficients'] = len(vals)
        res['monomials_total_degree_le_m'] = len(keys)
        res['positive_coefficients'] = sum(1 for v in vals if v > 0)
        res['negative_coefficients'] = sum(1 for v in vals if v < 0)
        res['constant_term_sign'] = (coef.get((0, 0), 0) > 0) - (coef.get((0, 0), 0) < 0)
        res['max_total_degree_present'] = max(i + j for (i, j) in coef)
        res['coef_bits_max'] = max(abs(v).bit_length() for v in vals)
        res['symmetric_in_x_y'] = all(coef.get((i, j)) == coef.get((j, i)) for (i, j) in coef)
        res['exact_sign_at_small_points'] = {f'{r},{s}': ((lambda v: (v > 0) - (v < 0))(C5.eval_poly(coef, r - 6, s - 6)))
                                             for r in range(1, 7) for s in range(1, 7)}
        g5 = C5.shift_poly(coef, -1, -1)
        res['shift5_negative_coefficients'] = sum(1 for v in g5.values() if v < 0)
        res['shift5_nonzero_coefficients'] = len(g5)
        res['ray_r5_negative_coeffs'] = sum(1 for (i, j), v in g5.items() if i == 0 and v < 0)
        res['ray_s5_negative_coeffs'] = sum(1 for (i, j), v in g5.items() if j == 0 and v < 0)
        res['corner_5_5_value_sign'] = (lambda v: (v > 0) - (v < 0))(g5.get((0, 0), 0))
        blob = json.dumps(sorted([[i, j, str(v)] for (i, j), v in coef.items()]), separators=(',', ':')).encode()
        res['coefficient_list_sha256'] = hashlib.sha256(blob).hexdigest()
        with open(os.path.join(HERE, f'r165-c10-poly-{a}{b}-coefficients.json'), 'wb') as fh:
            fh.write(blob + b'\n')
        res['end_clock'] = K.clock()
        print(json.dumps(res, indent=1))
