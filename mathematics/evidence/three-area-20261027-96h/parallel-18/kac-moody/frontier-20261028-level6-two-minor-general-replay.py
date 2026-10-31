#!/usr/bin/env python3
"""Independent replay of a general level-six two-minor resultant certificate.

Imports no producer code.  Rebuilds every full target row with the separate
tree-Jacobi engine, rebuilds both minors from the claimed factorizations by own
rational convolution and compares them with own fraction-free determinants on a
SHIFTED unisolvent triangular grid, checks positivity labels, checks every
resultant modulo two 60-bit primes at deg+1 points with own Sylvester
eliminations plus exact integer Sylvester determinants, divides out the claimed
linear factors, certifies the remaining integer roots at a different Hensel
prime, and re-derives the nonnegative-root fibres.
"""
import argparse
import hashlib
import importlib.util
import json
import math
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PRIMES = (1000000000000000003, 1000000000000000009)


def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / file)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ind = load('independent', 'frontier-20261028-levi-critical-independent-replay.py')


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


def poly(entry):
    return {(t['x_power'], t['y_power']): Q(t['coefficient']) for t in entry['coefficients']}


def gcd_modp(a, b, p):
    def trim(v):
        while v and v[-1] == 0:
            v.pop()
        return v
    a, b = trim([v % p for v in a]), trim([v % p for v in b])
    while b:
        inv = pow(b[-1], -1, p)
        while len(a) >= len(b) and a:
            d = len(a) - len(b)
            f = a[-1] * inv % p
            for j, c in enumerate(b):
                a[j + d] = (a[j + d] - f * c) % p
            a = trim(a)
        a, b = b, a
    return a


def ev(c, t, m=None):
    z = 0
    for a in reversed(c):
        z = z * t + a
        if m:
            z %= m
    return z


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--certificate', required=True)
    ap.add_argument('--certificate-sha256', required=True)
    args = ap.parse_args()
    raw = (ROOT / args.certificate).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == args.certificate_sha256
    W = json.loads(raw)
    degree = tuple(W['degree'])
    out = ROOT / args.certificate.replace('-certificate-v1.json', '-independent-replay-v1.json')
    if out.exists():
        raise FileExistsError(out)
    praw = (ROOT / W['pencil']).read_bytes()
    assert hashlib.sha256(praw).hexdigest() == W['pencil_sha256']
    P = json.loads(praw)
    words = P['source_words']
    assert tuple(words) == ind.lyndon_words(degree)
    basis = [ind.ind.standard_bracket(w) for w in words]
    hor = []
    for v in basis:
        col = {}
        for g, prefix in (('f1', '1:'), ('f2', '2:')):
            col.update({prefix + w: q for w, q in ind.act(v, g, 6, 6).items()})
        hor.append(col)
    k = P['joint_horizontal_kernel_dim']
    assert len(words) - len(ind.ind.ReducedSpace(hor)) == k == W['columns']
    coeffs = P['horizontal_kernel_coefficients']
    assert len(ind.ind.ReducedSpace([{int(i): Q(q) for i, q in c.items()} for c in coeffs])) == k
    vectors = [ind.combine(basis, c) for c in coeffs]
    for v in vectors:
        for g in ('f1', 'f2'):
            assert not ind.act(v, g, 6, 6)
    aa = [ind.d3(v, degree, 6, 6) for v in vectors]
    xx = [ind.d3(v, degree, 7, 6) for v in vectors]
    yy = [ind.d3(v, degree, 6, 7) for v in vectors]
    target = sorted(set(w for z in aa + xx + yy for w in z))
    assert len(target) == W['full_target_rows']
    rows = {w: [[Q(aa[j].get(w, 0)), Q(xx[j].get(w, 0)) - Q(aa[j].get(w, 0)), Q(yy[j].get(w, 0)) - Q(aa[j].get(w, 0))]
                for j in range(k)] for w in target}
    report = {}
    for key, wordlist in (('P1', W['selected_rows']), ('P2', W['second_minor_rows'])):
        assert len(wordlist) == len(set(wordlist)) == k
        F = W['minor_factorizations'][key]
        total = {(0, 0): Q(F['content'])}
        for entry in F['factors']:
            g = poly(entry)
            vals = list(g.values())
            positive = g.get((0, 0), 0) != 0 and (all(c > 0 for c in vals) or all(c < 0 for c in vals))
            assert positive == entry['strictly_positive_on_quadrant']
            for _ in range(entry['multiplicity']):
                total = mul(total, g)
        mat = [[rows[w][j] for j in range(k)] for w in wordlist]
        scales = [math.lcm(*(v.denominator for e in row for v in e)) for row in mat]
        imat = [[[int(v * s) for v in e] for e in row] for row, s in zip(mat, scales)]
        sc = math.prod(scales)
        count = 0
        for i in range(k + 1):
            for j in range(k + 1 - i):
                xv, yv = i - 5, j + 2
                d = bareiss([[a + xv * b + yv * c for a, b, c in row] for row in imat])
                assert Q(d, sc) == sum(c * xv**u * yv**v for (u, v), c in total.items()), (key, xv, yv)
                count += 1
        report[key] = {'grid_determinants': count, 'factor_count': len(F['factors'])}
    badP1 = [poly(e) for e in W['minor_factorizations']['P1']['factors'] if not e['strictly_positive_on_quadrant']]
    badP2 = [poly(e) for e in W['minor_factorizations']['P2']['factors'] if not e['strictly_positive_on_quadrant']]
    assert len(W['bad_pairs']) == len(badP1) * len(badP2)
    pair_reports = []
    index = 0
    for B in badP1:
        for C in badP2:
            pr = W['bad_pairs'][index]
            index += 1
            var = 0 if pr['eliminated_variable'] == 'x' else 1
            def spec(d, t0):
                n = max(m[var] for m in d)
                v = [Q(0)] * (n + 1)
                for m, c in d.items():
                    v[m[var]] += c * t0**m[1 - var]
                assert all(c.denominator == 1 for c in v)
                return [int(c) for c in v]
            for d in (B, C):
                n = max(m[var] for m in d)
                assert all(m[1 - var] == 0 for m in d if m[var] == n)
            H = [int(c) for c in pr['resultant_coefficients_low_to_high']]
            deg = len(H) - 1
            checks = 0
            for q in PRIMES:
                for t0 in range(2000, 2001 + deg):
                    assert det_mod(sylvester([c % q for c in spec(B, t0)], [c % q for c in spec(C, t0)]), q) == ev(H, t0, q)
                    checks += 1
            for t0 in (-3, 0, 7):
                assert bareiss(sylvester(spec(B, t0), spec(C, t0))) == ev(H, t0)
            rest = [Q(c) for c in H]
            for a, b, m in pr['repeated_part_linear_factors_a_t_plus_b_mult_in_H']:
                for _ in range(m):
                    n = len(rest) - 1
                    quo = [Q(0)] * n
                    work = rest[:]
                    for i in range(n, 0, -1):
                        quo[i - 1] = work[i] / a
                        work[i - 1] -= quo[i - 1] * b
                    assert work[0] == 0
                    rest = quo
            assert all(c.denominator == 1 for c in rest)
            Wc = [int(c) for c in rest]
            for a, b, m in pr['repeated_part_linear_factors_a_t_plus_b_mult_in_H']:
                assert ev(Wc, Q(-b, a)) != 0
            dW = [i * Wc[i] for i in range(1, len(Wc))]
            cauchy = 1 + -(-max(abs(c) for c in Wc[:-1]) // abs(Wc[-1]))
            p = 5000
            while True:
                p += 1
                if all(p % d for d in range(2, math.isqrt(p) + 1)) and Wc[-1] % p and len(gcd_modp(Wc, dW, p)) == 1:
                    break
            modulus = p
            while modulus <= 2 * cauchy:
                modulus *= p
            found = []
            for r in [r for r in range(p) if ev(Wc, r, p) == 0]:
                a = r
                for _ in range(64):
                    if ev(Wc, a, modulus) == 0:
                        break
                    a = (a - ev(Wc, a, modulus) * pow(ev(dW, a, modulus), -1, modulus)) % modulus
                assert ev(Wc, a, modulus) == 0
                if a > modulus // 2:
                    a -= modulus
                if abs(a) <= cauchy and ev(Wc, a) == 0:
                    found.append(a)
            linear_roots = [-b // a for a, b, m in pr['repeated_part_linear_factors_a_t_plus_b_mult_in_H'] if b % a == 0]
            all_roots = sorted(set(found) | set(linear_roots))
            assert all_roots == sorted(pr['squarefree_part_integer_roots'])
            nonneg = [r for r in all_roots if r >= 0]
            assert nonneg == [f['fixed_' + ('y' if var == 0 else 'x')] for f in pr['nonnegative_integer_root_fibres']]
            pair_reports.append({'modular_sylvester_checks': checks, 'exact_checks': 3, 'second_hensel_prime': p,
                                 'integer_roots': all_roots, 'nonnegative_integer_roots': nonneg})
    result = {'certificate': args.certificate, 'certificate_sha256': args.certificate_sha256,
              'degree': list(degree), 'independent_full_target_rows': len(target), 'minors': report,
              'pairs': pair_reports, 'producer_status': W['status'],
              'status': 'PASS_INDEPENDENT_GENERAL_TWO_MINOR_REPLAY', 'not_formal_or_external_model_review': True}
    out.write_text(json.dumps(result, indent=2) + '\n')
    print('PASS independent', degree, 'grid', [r['grid_determinants'] for r in report.values()],
          'pairs', len(pair_reports), 'nonneg roots', [p['nonnegative_integer_roots'] for p in pair_reports], out.name, flush=True)


if __name__ == '__main__':
    main()
