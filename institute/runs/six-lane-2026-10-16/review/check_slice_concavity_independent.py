"""Parent re-derivation of the polynomial part of the phys-2 slice-concavity lemma.

Independent of the lane's python-flint and sympy code: plain integer dictionaries only.
Variables mu = (x, y, z, w) index the 2x2 spectrum cells (-1,-1), (-1,1), (1,-1), (1,1).
S = 2x2 nonnegative integer matrices with entry sum 5 and no zero row or column (|S| = 36);
Phi = sum_s 5!/prod(s!) mu^s, m_k = sum_s w_s s_k mu^s, S2_kl = sum_s w_s s_k s_l mu^s,
M = 5 Phi (2 diag(m) - S2) + 3 m m^T.

Checks: |S| = 36; Phi equals the inclusion-exclusion closed form; M 1 = 0 exactly; for every dropped
index, the three leading principal minors of the remaining 3x3 block have only strictly positive
coefficients. This checks only the polynomial positivity step, not the Hessian bridge from psi to M.
"""
from datetime import datetime
from itertools import product
from math import factorial
import hashlib
import json
from pathlib import Path
import sys
import time
from zoneinfo import ZoneInfo

OUT = Path(__file__).resolve().parent / 'slice-concavity-parent-check-v1.json'


def add(p, q, scale=1):
    r = dict(p)
    for mono, c in q.items():
        v = r.get(mono, 0) + scale * c
        if v:
            r[mono] = v
        else:
            r.pop(mono, None)
    return r


def mul(p, q):
    r = {}
    for a, ca in p.items():
        for b, cb in q.items():
            mono = (a[0] + b[0], a[1] + b[1], a[2] + b[2], a[3] + b[3])
            r[mono] = r.get(mono, 0) + ca * cb
    return {k: v for k, v in r.items() if v}


def const(c):
    return {(0, 0, 0, 0): c} if c else {}


def power_of_sum(indices, n):
    """(sum_{i in indices} mu_i)^n by the multinomial theorem."""
    r = {}
    k = len(indices)
    def rec(pos, left, exps):
        if pos == k - 1:
            exps = exps + [left]
            mono = [0, 0, 0, 0]
            coeff = factorial(n)
            for i, e in zip(indices, exps):
                mono[i] = e
                coeff //= factorial(e)
            r[tuple(mono)] = r.get(tuple(mono), 0) + coeff
            return
        for e in range(left + 1):
            rec(pos + 1, left - e, exps + [e])
    rec(0, n, [])
    return r


def main():
    if OUT.exists():
        raise SystemExit('refusing to overwrite prior evidence')
    started = time.monotonic()
    spectra = [s for s in product(range(6), repeat=4) if sum(s) == 5
               and s[0] + s[1] > 0 and s[2] + s[3] > 0 and s[0] + s[2] > 0 and s[1] + s[3] > 0]
    weight = {s: factorial(5) // (factorial(s[0]) * factorial(s[1]) * factorial(s[2]) * factorial(s[3])) for s in spectra}
    phi = {s: weight[s] for s in spectra}
    closed = power_of_sum([0, 1, 2, 3], 5)
    for rowcol in ([0, 1], [2, 3], [0, 2], [1, 3]):
        closed = add(closed, power_of_sum(rowcol, 5), -1)
    for i in range(4):
        closed = add(closed, power_of_sum([i], 5), 1)
    m = [{s: weight[s] * s[k] for s in spectra if s[k]} for k in range(4)]
    s2 = [[{s: weight[s] * s[k] * s[l] for s in spectra if s[k] * s[l]} for l in range(4)] for k in range(4)]
    M = [[None] * 4 for _ in range(4)]
    for k in range(4):
        for l in range(4):
            inner = add(const(0), s2[k][l], -1)
            if k == l:
                inner = add(inner, m[k], 2)
            M[k][l] = add(mul(mul(const(5), phi), inner), mul(mul(const(3), m[k]), m[l]))
    kernel_ok = all(not add(add(add(M[k][0], M[k][1]), M[k][2]), M[k][3]) for k in range(4))
    symmetric = all(M[k][l] == M[l][k] for k in range(4) for l in range(4))
    minors = {}
    for drop in range(4):
        keep = [i for i in range(4) if i != drop]
        A = [[M[i][j] for j in keep] for i in keep]
        p1 = A[0][0]
        p2 = add(mul(A[0][0], A[1][1]), mul(A[0][1], A[1][0]), -1)
        p3 = {}
        for (i, j, k), sign in (((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                                 ((0, 2, 1), -1), ((1, 0, 2), -1), ((2, 1, 0), -1)):
            p3 = add(p3, mul(mul(A[0][i], A[1][j]), A[2][k]), sign)
        record = {}
        for name, poly, degree in (('P1', p1, 10), ('P2', p2, 20), ('P3', p3, 30)):
            coeffs = list(poly.values())
            record[name] = {'terms': len(poly), 'min_coeff': min(coeffs), 'negative_or_zero_terms': sum(c <= 0 for c in coeffs),
                            'homogeneous_degree_ok': all(sum(mono) == degree for mono in poly)}
        minors[str(drop)] = record
    p3_drop3_text = repr(sorted(p3.items()))
    ok = (len(spectra) == 36 and phi == closed and kernel_ok and symmetric and
          all(r[n]['negative_or_zero_terms'] == 0 and r[n]['homogeneous_degree_ok'] for r in minors.values() for n in r))
    result = {'status': 'POLYNOMIAL_POSITIVITY_PASS' if ok else 'FAIL',
              'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'python': sys.version.split()[0], 'spectra': len(spectra), 'phi_equals_closed_form': phi == closed,
              'M_times_ones_zero': kernel_ok, 'M_symmetric': symmetric, 'minors': minors,
              'last_computed_P3_sha256': hashlib.sha256(p3_drop3_text.encode()).hexdigest(),
              'duration_seconds': time.monotonic() - started,
              'scope': 'Polynomial positivity of Sylvester minors of M only. The Hessian identity relating psi to M, the slice/closure argument and every use in the certificate are not checked here.'}
    with OUT.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps(result, indent=2))
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
