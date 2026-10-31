#!/usr/bin/env python3
"""Independent replay of the level-six (2,2,6) two-minor resultant certificate.

No producer code is imported.  Rows come from the independently replayed
ratio-cone certificate.  P2 is checked against own fraction-free determinants
on a SHIFTED unisolvent triangular grid; the factorization by own integer
convolution; H by own modular Sylvester eliminations at 463 points for two
large primes plus exact Sylvester determinants; the linear factors by own
division; and integer-root exclusion by own Hensel lifting at a different prime.
"""
import hashlib
import json
import math
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CERT = ('frontier-20261028-level6-226-ratio-cone-certificate-v1.json',
        'ca05270e600105cd29c6e804033e5569c5fff0e85d035e21b1f0c499b69c764b')
RCERT = ('frontier-20261028-level6-226-generic-irreducibility-certificate-v1.json',
         '5aa67436e478db33b12bdfe3f6ba00b321ca81ebe9a8fa1fca4a6c9efd7d4297')
PROD = ('frontier-20261028-level6-226-two-minor-resultant-v1.json',
        'e410b55d3e4252c1bc7d88db77d16cf85ced36b5069b9bdf47bb51edcda81bba')
PRIMES = (1000000000000000003, 1000000000000000009)


def read(pin):
    raw = (ROOT / pin[0]).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == pin[1], pin[0]
    return json.loads(raw)


def bareiss(m):
    a = [row[:] for row in m]
    n = len(a)
    sign, prev = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            swap = next((i for i in range(k + 1, n) if a[i][k]), None)
            if swap is None:
                return 0
            a[k], a[swap] = a[swap], a[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = (a[i][j] * a[k][k] - a[i][k] * a[k][j]) // prev
        prev = a[k][k]
    return sign * a[-1][-1]


def det_mod(m, q):
    a = [[v % q for v in row] for row in m]
    n = len(a)
    d = 1
    for k in range(n):
        piv = next((i for i in range(k, n) if a[i][k]), None)
        if piv is None:
            return 0
        if piv != k:
            a[k], a[piv] = a[piv], a[k]
            d = -d
        d = d * a[k][k] % q
        inv = pow(a[k][k], -1, q)
        for i in range(k + 1, n):
            f = a[i][k] * inv % q
            if f:
                for j in range(k, n):
                    a[i][j] = (a[i][j] - f * a[k][j]) % q
    return d % q


def sylvester(f, g):
    """f,g low-to-high integer coefficient lists with nonzero leading terms."""
    m, n = len(f) - 1, len(g) - 1
    fd, gd = f[::-1], g[::-1]
    size = m + n
    rows = [[0] * i + fd + [0] * (size - i - len(fd)) for i in range(n)]
    rows += [[0] * i + gd + [0] * (size - i - len(gd)) for i in range(m)]
    return rows


def mul(a, b):
    out = {}
    for (i, j), c in a.items():
        for (u, v), d in b.items():
            out[i + u, j + v] = out.get((i + u, j + v), 0) + c * d
    return {k: v for k, v in out.items() if v}


def power(a, e):
    out = {(0, 0): 1}
    for _ in range(e):
        out = mul(out, a)
    return out


def spec(poly, x0, n):
    v = [0] * (n + 1)
    for (i, j), c in poly.items():
        v[j] += c * x0**i
    return v


def evalq(poly, x0, y0):
    return sum(c * x0**i * y0**j for (i, j), c in poly.items())


def main():
    out = ROOT / 'frontier-20261028-level6-226-two-minor-independent-replay-v1.json'
    if out.exists():
        raise FileExistsError(out)
    C, RJ, W = read(CERT), read(RCERT), read(PROD)
    rows = dict(zip(C['target_word_rows'], C['full_target_affine_entries']))
    words = W['second_minor_rows']
    assert len(words) == len(set(words)) == 34 and words[0] == '00601'
    mat = [[[Q(v) for v in e] for e in rows[w]] for w in words]
    scales = [math.lcm(*(v.denominator for e in row for v in e)) for row in mat]
    imat = [[[int(v * s) for v in e] for e in row] for row, s in zip(mat, scales)]
    total_scale = math.prod(scales)
    P2 = {(t['x_power'], t['y_power']): Q(t['coefficient']) for t in W['P2_coefficients']}
    assert max(i + j for i, j in P2) <= 34
    grid = 0
    for i in range(35):
        for j in range(35 - i):
            xv, yv = i - 7, j + 3
            d = bareiss([[a + xv * b + yv * c for a, b, c in row] for row in imat])
            assert Q(d, total_scale) == evalq(P2, xv, yv), (xv, yv)
            grid += 1
    R2 = {(t['x_power'], t['y_power']): int(t['coefficient']) for t in W['R2_coefficients']}
    lin = lambda a, b, c: {k: v for k, v in {(1, 0): a, (0, 1): b, (0, 0): c}.items() if v}
    cof = mul(mul(power(lin(1, 0, 5), 3), power(lin(0, 1, 5), 7)), power(lin(2, 2, 19), 2))
    rebuilt = {k: -3145728 * v for k, v in mul(cof, R2).items()}
    assert rebuilt == {k: int(v) for k, v in P2.items()} and all(v.denominator == 1 for v in P2.values())
    R = {(t['x_power'], t['y_power']): int(t['coefficient']) for t in RJ['R_coefficients']}
    assert R[0, 21] == 2107392 and R2[0, 22] == 44255232
    assert max(i + j for i, j in R) == 21 and max(i + j for i, j in R2) == 22
    H = [int(c) for c in W['H_coefficients_low_to_high']]
    assert len(H) - 1 == 462

    def hmod(x0, q):
        z = 0
        for c in reversed(H):
            z = (z * x0 + c) % q
        return z

    modular = 0
    for q in PRIMES:
        for x0 in range(1000, 1463):
            f = [c % q for c in spec(R, x0, 21)]
            g = [c % q for c in spec(R2, x0, 22)]
            assert det_mod(sylvester(f, g), q) == hmod(x0, q), (q, x0)
            modular += 1
    exact = 0
    for x0 in (-9, -1, 0, 3, 50):
        d = bareiss(sylvester(spec(R, x0, 21), spec(R2, x0, 22)))
        assert d == sum(c * x0**i for i, c in enumerate(H)), x0
        exact += 1
    rest = [Q(c) for c in H]
    for a, b, m in W['explicit_linear_factors_a_x_plus_b_multiplicity']:
        for _ in range(m):
            n = len(rest) - 1
            quo = [Q(0)] * n
            work = rest[:]
            for i in range(n, 0, -1):
                quo[i - 1] = work[i] / a
                work[i - 1] -= quo[i - 1] * b
            assert work[0] == 0
            rest = quo
    assert all(v.denominator == 1 for v in rest)
    H2 = [int(v) for v in rest]
    assert len(H2) - 1 == W['H2_degree'] == 393 and str(H2[-1]) == W['H2_leading_coefficient']
    for a, b, m in W['explicit_linear_factors_a_x_plus_b_multiplicity']:
        assert sum(c * (-b)**i * a**(len(H2) - 1 - i) for i, c in enumerate(H2)) != 0
    lc = abs(H2[-1])
    cauchy = 1 + -(-max(abs(c) for c in H2[:-1]) // lc)
    dH2 = [i * H2[i] for i in range(1, len(H2))]

    def pmod(c, p):
        v = [x % p for x in c]
        while v and v[-1] == 0:
            v.pop()
        return v

    def pgcd(a, b, p):
        a, b = pmod(a, p), pmod(b, p)
        while b:
            inv = pow(b[-1], -1, p)
            while len(a) >= len(b) and a:
                d = len(a) - len(b)
                f = a[-1] * inv % p
                for j, c in enumerate(b):
                    a[j + d] = (a[j + d] - f * c) % p
                while a and a[-1] == 0:
                    a.pop()
            a, b = b, a
        return a

    p = 5000
    while True:
        p += 1
        if all(p % d for d in range(2, math.isqrt(p) + 1)) and H2[-1] % p and len(pgcd(H2, dH2, p)) == 1:
            break

    def ev(c, x0, m):
        z = 0
        for a in reversed(c):
            z = (z * x0 + a) % m
        return z

    roots = [r for r in range(p) if ev(H2, r, p) == 0]
    modulus = p
    while modulus <= 2 * cauchy:
        modulus *= p
    within = []
    for r in roots:
        a = r
        for _ in range(4000):
            if ev(H2, a, modulus) == 0:
                break
            a = (a - ev(H2, a, modulus) * pow(ev(dH2, a, modulus), -1, modulus)) % modulus
        assert ev(H2, a, modulus) == 0
        if a > modulus // 2:
            a -= modulus
        if abs(a) <= cauchy:
            within.append(a)
    assert not any(sum(c * a**i for i, c in enumerate(H2)) == 0 for a in within)
    result = {
        'producer_sha256': PROD[1], 'rows_source_sha256': CERT[1], 'R_source_sha256': RCERT[1],
        'shifted_grid_exact_determinants': grid, 'grid': 'x in [-7,27], y=j+3, i+j<=34 (unisolvent for total degree 34)',
        'P2_factorization_by_integer_convolution': True,
        'modular_sylvester_checks': modular, 'modular_primes': [str(q) for q in PRIMES],
        'exact_sylvester_checks': exact,
        'linear_factor_division_and_multiplicity_exactness': True,
        'H2_degree': len(H2) - 1, 'second_hensel_prime': p, 'H2_roots_mod_p': len(roots),
        'symmetric_lifts_within_cauchy_bound': [str(a) for a in within],
        'status': 'PASS_INDEPENDENT_TWO_MINOR_RESULTANT_NO_INTEGER_FIBRE_COMMON_ZERO',
        'not_formal_or_external_model_review': True,
    }
    out.write_text(json.dumps(result, indent=2) + '\n')
    print('PASS independent: grid', grid, 'modular', modular, 'exact', exact, 'p', p, 'roots', len(roots),
          'within', len(within), out.name, flush=True)


if __name__ == '__main__':
    main()
