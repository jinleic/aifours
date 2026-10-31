#!/usr/bin/env python3
"""f62 reviewer: exact (height-bounded CRT) proof of the corrected d=4 certificate orbit identity with the
f62 independent evaluator (numpy int64 modular backend, own maps/entry rule/orbits/objective; no FLINT,
no author code, no first-reviewer code). Every integer residual R_(f,o) = D*(c - blocks - equalities)(o)
is bounded by an explicitly recomputed B; residues are computed modulo distinct 20-bit primes whose
product P exceeds 2B; all-zero residues then force every R_(f,o) = 0 exactly. Writes only here."""
import importlib.util, json, math, sys, time
from pathlib import Path
import numpy as np
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('f62mod', HERE / 'f62-independent-modular-identity-check.py')
M = importlib.util.module_from_spec(spec); spec.loader.exec_module(M)
OUT = HERE / 'f62-independent-crt-identity-proof-results.json'


def main():
    t0 = time.monotonic()
    pkg, corr = M.load()
    ev = M.Evaluator(pkg)
    types = pkg['types']
    Zq = [[(int(a), int(b)) for a, b in m['values']] for m in corr['matrices']]
    eqc = [(e['group'], tuple(e['index']), int(e['numerator']), int(e['denominator'])) for e in corr['equality_coefficients']]
    # common denominator D
    D = 8 * (2 * 4 ** 3) ** 4
    for Mq in Zq:
        for _, b in Mq: D = D * b // math.gcd(D, b)
    for *_, b in eqc: D = D * b // math.gcd(D, b)
    Zint = [[a * (D // b) for a, b in Mq] for Mq in Zq]
    Lint = [a * (D // b) for *_, a, b in eqc]
    Zmax = max(abs(v) for Mq in Zint for v in Mq); Lmax = max(abs(v) for v in Lint)
    Wmax = max(abs(x) for t in types for row in t['W'] for x in row)
    # own local-map and equality-map maxima (all combinations actually used by this evaluator)
    Amax = 0; Cblock = 0
    rules = {}
    for ti, t in enumerate(types):
        d = ev.dims[ti]; n = math.prod(d); k = len(t['rows'])
        Cblock += k * k * t['r'] ** 2 * n * n
        for r in range(k):
            for s in range(k):
                fam, kpos, lpos = M.entry_rule(t['rows'][r], t['rows'][s])
                for l in range(4):
                    Amax = max(Amax, int(np.abs(ev.local(t['modules'][l], l == 3, kpos, lpos)).max()))
    Emax = 0; Ceq = 0
    parts_of = {name: len(g['parts']) for name, g in pkg['eq_groups'].items()}
    for name, g in pkg['eq_groups'].items():
        for part in g['parts']:
            for s in part['local']: Emax = max(Emax, int(np.abs(ev.eq_rows(s)).max()))
    for g, *_ in eqc: Ceq += parts_of[g]
    obj = M.objective(); Cobj = int(np.abs(obj).max())
    orbits = {f: M.orbit_labels(letters) for f, letters in M.LETTERS.items()}
    maxorbit = max(int(np.bincount(o[0]).max()) for o in orbits.values())
    B = (24 ** 4) * (Cblock * Zmax * Wmax ** 2 * Amax ** 4 + Ceq * Lmax * Emax ** 4 + Cobj * (D // (8 * (2 * 4 ** 3) ** 4)))
    # primes: descending from 2^20 until product > 2B, skipping divisors of D
    primes, P, q = [], 1, 2 ** 20
    while P <= 2 * B:
        q -= 1
        if M.is_prime(q) and D % q:
            primes.append(q); P *= q
    print('D bits', D.bit_length(), 'B bits', B.bit_length(), 'primes', len(primes), 'P bits', P.bit_length(), flush=True)
    nonzero_primes, per = [], []
    for pi_, p in enumerate(primes):
        tp = time.monotonic()
        Zmod = [np.array([v % p for v in Mq], dtype=np.int64).reshape(t['r'], t['r']) for Mq, t in zip(Zint, types)]
        lam = [(g, idx, v % p) for (g, idx, *_), v in zip(eqc, Lint)]
        acc = {f: np.zeros((24,) * 4, dtype=np.int64) for f in M.LETTERS}
        for ti, t in enumerate(types):
            for r in range(len(t['rows'])):
                for s in range(len(t['rows'])):
                    fam, X = ev.block_tensor(ti, r, s, Zmod[ti], p); acc[fam] -= X
            if ti % 100 == 0:
                for f in acc: np.mod(acc[f], p, out=acc[f])
        acc['31'] += (obj % p) * ((D // (8 * (2 * 4 ** 3) ** 4)) % p) % p
        for name, group in pkg['eq_groups'].items():
            coeffs = [(idx, v) for g, idx, v in lam if g == name]
            for part in group['parts']: acc[part['family']] -= int(part['sign']) * ev.eq_tensor(part, coeffs, p)
        counts = {}
        for f, (oid, norb, _) in orbits.items():
            osum = np.zeros(norb, dtype=np.int64); np.add.at(osum, oid, (acc[f] % p).ravel()); counts[f] = int(np.count_nonzero(osum % p))
        if any(counts.values()): nonzero_primes.append({'prime': p, 'counts': counts})
        per.append(round(time.monotonic() - tp, 2))
        if pi_ % 25 == 0 or any(counts.values()): print('prime', pi_ + 1, '/', len(primes), p, counts, per[-1], 's', flush=True)
        if nonzero_primes: break
    ok = not nonzero_primes and P > 2 * B
    res = {'kind': 'f62_independent_crt_exact_d4_certificate_orbit_identity', 'inputs_sha256': M.EXPECTED,
           'common_denominator_bits': D.bit_length(), 'residual_bound_B_bits': B.bit_length(), 'prime_product_bits': P.bit_length(),
           'P_greater_than_2B': P > 2 * B, 'prime_count': len(primes), 'primes_min_max': [min(primes), max(primes)],
           'bound_ingredients': {'Zmax_bits': Zmax.bit_length(), 'Lmax_bits': Lmax.bit_length(), 'Wmax': Wmax, 'Amax': Amax, 'Emax': Emax,
                                 'Cblock': Cblock, 'Ceq': Ceq, 'Cobj': Cobj, 'orbit_size_factor_used': 24 ** 4, 'actual_max_orbit_size': maxorbit},
           'orbit_counts': {f: o[1] for f, o in orbits.items()}, 'primes_with_nonzero_residues': nonzero_primes,
           'mean_seconds_per_prime': round(sum(per) / len(per), 3), 'elapsed_seconds': round(time.monotonic() - t0, 3),
           'numpy_version': np.__version__,
           'scope': 'Exact zero of all 4675 scaled integer orbit residuals via explicit height bound and CRT, with the f62 evaluator; conditional on numpy/Python runtime and this code. Identity only: PSD, physical bridge and commutant span are separate predicates.',
           'verdict': 'PASS' if ok else 'FAIL'}
    res['primes'] = primes; res['D_decimal_sha256'] = M.sha256(str(D).encode()); res['B_decimal'] = str(B)
    OUT.write_text(json.dumps(res, indent=2, sort_keys=True) + '\n')
    print(json.dumps({k: v for k, v in res.items() if k not in ('primes', 'B_decimal')}, indent=2, sort_keys=True), flush=True)
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
