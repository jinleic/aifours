#!/usr/bin/env python3
"""Certifier B: rigorous enclosure of Psi_T by the exact MOMENT route.

Same functional as certifier A (notes/PROOF.md, Sections 1 and 9), but
computed through the moment sequence c_h = E R^h only:

    nu_i  = sum_{h=0}^{i} (-1)^h binom(i,h) c_h^(k-1)          (exact rational)
    M_i   = exp(-lambda (1 - nu_i)),   lambda = k alpha / 2
    mu_j  = sum_{i=0}^{j} (-1)^i binom(j,i) M_i                (explicit binomials)
    -E log(1 - R_1...R_k) = sum_{h>=1} c_h^k / h                (series + tail)
    Psi_T = -sum_{j<=T} mu_j^2/j + (k-1) alpha sum_{h>=1} c_h^k/h.

Algorithmic choices are deliberately different from certifier A: no product
laws are enumerated; nu_i is an exact rational from big-integer moment sums;
exp(-a) is enclosed by the full alternating Taylor series of exp(-a) itself
(no argument reduction, no squaring) on a DECIMAL fixed-point grid; mu_j uses
explicit binomial coefficients with endpoint selection; the clause term uses
moment powers and the bound c_h <= r_max^h for its tail. Rounding is directed.
Gating uses explicit exceptions (no assert), so python -O cannot disable it.

Exit status: 0 certified; 1 rejected; 2 malformed input.
"""
import argparse
import hashlib
import json
import sys
import time
from fractions import Fraction
from math import comb, gcd, log10
from pathlib import Path


class Rejected(Exception):
    pass


class BadInput(Exception):
    pass


def check(cond, msg, exc=Rejected):
    if not cond:
        raise exc(msg)


def cdiv(a, b):
    return -((-a) // b)


def lcm(a, b):
    return a // gcd(a, b) * b


def read_trial(trial):
    try:
        k = int(trial['k'])
        T = int(trial['T'])
        alpha = Fraction(trial['alpha'])
        eps = Fraction(trial['epsilon'])
        y = Fraction(trial['y'])
        rates = [Fraction(v) for v in trial['rates']]
        weights = [Fraction(v) for v in trial['weights']]
    except (KeyError, ValueError, TypeError, ZeroDivisionError) as exc:
        raise BadInput(f'malformed trial field: {exc!r}')
    check(k >= 2 and T >= 1, 'need k >= 2 and T >= 1', BadInput)
    check(alpha > 0 and eps > 0 and y > 0, 'alpha, epsilon, y must be positive', BadInput)
    check(len(rates) == len(weights) and rates, 'rates/weights mismatch', BadInput)
    check(all(0 <= r < 1 for r in rates), 'rates must lie in [0,1)', BadInput)
    check(all(w >= 0 for w in weights), 'weights must be nonnegative', BadInput)
    check(sum(weights) == 1, 'weights must sum to exactly 1', BadInput)
    return k, T, alpha, eps, y, rates, weights


def exp_neg_decimal(A, scale_in, digits_out):
    """Enclose exp(-a) for a = A/scale_in >= 0 on the grid 10^-digits_out.

    Uses sum_{n<=N} (-a)^n/n! with directed rounding of each magnitude
    a^n/n!; for N+1 > a the remaining alternating tail has decreasing terms
    and is bounded by the first omitted magnitude (Leibniz).
    """
    check(A >= 0, 'exp_neg_decimal needs a >= 0', BadInput)
    a_float_bound = A // scale_in + 1                 # integer upper bound on a
    guard = int(a_float_bound * 0.4343) + 12          # digits lost to e^a cancellation
    D = digits_out + guard
    one = 10 ** D
    lo_mag, hi_mag = one, one                         # a^0/0!
    s_lo, s_hi = one, one
    n = 0
    while True:
        n += 1
        lo_mag = (lo_mag * A) // (n * scale_in)
        hi_mag = cdiv(hi_mag * A, n * scale_in)
        if n > a_float_bound and hi_mag <= 1:
            # n is the first omitted index: tail bounded by hi_mag (+ rounding slack 1)
            break
        if n % 2 == 0:
            s_lo += lo_mag
            s_hi += hi_mag
        else:
            s_lo -= hi_mag
            s_hi -= lo_mag
    s_lo -= hi_mag
    s_hi += hi_mag
    s_lo = max(0, s_lo)
    s_hi = min(one, s_hi)
    shift = 10 ** guard
    return s_lo // shift, cdiv(s_hi, shift)


def certify(trial, verbose=True):
    t0 = time.monotonic()
    name = trial.get('name', '?')
    k, T, alpha, eps, y, rates, weights = read_trial(trial)
    lam = Fraction(k) * alpha / 2
    m = len(rates)

    # integer representation: r_t = a_t / Dr, w_t = b_t / Dw
    Dr = 1
    for r in rates:
        Dr = lcm(Dr, r.denominator)
    Dw = 1
    for w in weights:
        Dw = lcm(Dw, w.denominator)
    a_int = [r.numerator * (Dr // r.denominator) for r in rates]
    b_int = [w.numerator * (Dw // w.denominator) for w in weights]
    check(sum(b_int) == Dw, 'integerised weights do not sum to Dw', BadInput)
    rmax = max(rates)

    # clause tail cutoff H: r_max^(k(H+1)) / ((H+1)(1-r_max^k)) < 10^-60
    H = T
    zmax = rmax ** k
    if zmax > 0:
        while True:
            tail = zmax ** (H + 1) / ((H + 1) * (1 - zmax))
            if tail < Fraction(1, 10 ** 60):
                break
            H += 16
    else:
        tail = Fraction(0)

    # S_h = sum_t b_t a_t^h  (c_h = S_h / (Dw Dr^h)), h = 0..H
    S = []
    pw = list(b_int)
    for h in range(H + 1):
        S.append(sum(pw))
        pw = [p * a for p, a in zip(pw, a_int)]

    # exact nu_i = Num_i / (Dw^(k-1) Dr^(i(k-1)))
    E = [s ** (k - 1) for s in S[: T + 1]]
    Drk = Dr ** (k - 1)
    Dpow = [1]
    for _ in range(T):
        Dpow.append(Dpow[-1] * Drk)
    Dwk = Dw ** (k - 1)
    digits = int((T + 220) * 0.30103) + 10           # target grid for M_i
    scale = 10 ** digits
    M_lo, M_hi = [], []
    for i in range(T + 1):
        num = 0
        for h in range(i + 1):
            term = comb(i, h) * E[h] * Dpow[i - h]
            num += -term if h % 2 else term
        den = Dwk * Dpow[i]
        check(0 <= num <= den, f'nu_{i} outside [0,1]: moment data inconsistent')
        # a_i = lambda (1 - nu_i) = lam.num (den - num) / (lam.den den), exact
        an = lam.numerator * (den - num)
        ad = lam.denominator * den
        A_lo = (an * scale) // ad
        A_hi = cdiv(an * scale, ad)
        lo, _ = exp_neg_decimal(A_hi, scale, digits)   # exp decreasing in a
        _, hi = exp_neg_decimal(A_lo, scale, digits)
        M_lo.append(lo)
        M_hi.append(hi)

    # mu_j with explicit binomials and endpoint selection
    mu = []
    for j in range(1, T + 1):
        lo = hi = 0
        for i in range(j + 1):
            c = comb(j, i)
            if i % 2 == 0:
                lo += c * M_lo[i]
                hi += c * M_hi[i]
            else:
                lo -= c * M_hi[i]
                hi -= c * M_lo[i]
        lo, hi = max(0, lo), min(scale, hi)
        check(lo <= hi, f'mu_{j} enclosure inverted')
        mu.append((lo, hi))
    S2_lo = Fraction(0)
    S2_hi = Fraction(0)
    for j, (lo, hi) in enumerate(mu, start=1):
        S2_lo += Fraction(lo * lo, j)
        S2_hi += Fraction(hi * hi, j)
    S2_lo /= scale * scale
    S2_hi /= scale * scale

    # clause: sum_{h=1}^H c_h^k / h exactly, plus tail <= zmax^(H+1)/((H+1)(1-zmax))
    part = Fraction(0)
    Dwkk = Dw ** k
    for h in range(1, H + 1):
        part += Fraction(S[h] ** k, Dwkk * Dr ** (h * k) * h)
    C_lo = (k - 1) * alpha * part
    C_hi = (k - 1) * alpha * (part + tail)

    psi_lo = -S2_hi + C_lo
    psi_hi = -S2_lo + C_hi

    # finite-y: T exp(-y)
    ys = 10 ** 40
    Y_lo = (y.numerator * ys) // y.denominator
    _, ey_hi = exp_neg_decimal(Y_lo, ys, 60)
    fy = T * Fraction(ey_hi, 10 ** 60)

    out = {
        'name': name, 'certifier': 'B (exact moments, decimal grid, direct alternating Taylor)',
        'k': k, 'T': T, 'alpha': str(alpha), 'epsilon': str(eps), 'y': str(y),
        'decimal_digits': digits, 'clause_terms_H': H,
        'psi_enclosure': [dstr(psi_lo, False), dstr(psi_hi, True)],
        'site_enclosure': [dstr(S2_lo, False), dstr(S2_hi, True)],
        'clause_enclosure': [dstr(C_lo, False), dstr(C_hi, True)],
        'mu_max_width': dstr(Fraction(max(h - l for l, h in mu), scale), True),
        'finite_y_error_upper': dstr(fy, True),
        'psi_upper_le_minus_epsilon': psi_hi <= -eps,
        'finite_y_ok': fy <= eps / 2,
        'psi_lower_positive': psi_lo > 0,
        'seconds': round(time.monotonic() - t0, 2),
    }
    if verbose:
        print(f'PSI_ENCLOSURE {name} {out["psi_enclosure"][0]} {out["psi_enclosure"][1]}', flush=True)
    return out


def dstr(q, upper, places=20):
    d = 10 ** places
    n = cdiv(q.numerator * d, q.denominator) if upper else (q.numerator * d) // q.denominator
    s = '-' if n < 0 else ''
    n = abs(n)
    return f'{s}{n // d}.{n % d:0{places}d}'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--trials', required=True)
    ap.add_argument('--name', default='all')
    ap.add_argument('--output')
    args = ap.parse_args()
    raw = Path(args.trials).read_bytes()
    trials = json.loads(raw)['trials']
    chosen = [t for t in trials if args.name in ('all', t.get('name'))]
    if not chosen:
        raise BadInput(f'no trial named {args.name}')
    results, failures = [], []
    for t in chosen:
        res = certify(t)
        res['trials_sha256'] = hashlib.sha256(raw).hexdigest()
        results.append(res)
        if res['psi_upper_le_minus_epsilon'] and res['finite_y_ok']:
            print(f"B-CERTIFIED {res['name']}: Psi_{res['T']} <= {res['psi_enclosure'][1]} <= -{res['epsilon']}; "
                  f"T exp(-y) <= {res['finite_y_error_upper']} ({res['seconds']} s)", flush=True)
        else:
            why = []
            if not res['psi_upper_le_minus_epsilon']:
                why.append(f"upper bound {res['psi_enclosure'][1]} is not <= -{res['epsilon']}")
            if not res['finite_y_ok']:
                why.append(f"T exp(-y) bound {res['finite_y_error_upper']} exceeds epsilon/2")
            if res['psi_lower_positive']:
                why.append(f"rigorous lower bound {res['psi_enclosure'][0]} > 0")
            failures.append(f"{res['name']}: " + '; '.join(why))
    if args.output:
        Path(args.output).write_text(json.dumps({'results': results}, indent=1) + '\n')
    if failures:
        raise Rejected(' | '.join(failures))


if __name__ == '__main__':
    try:
        main()
    except Rejected as exc:
        print(f'REJECTED: {exc}', file=sys.stderr)
        sys.exit(1)
    except BadInput as exc:
        print(f'BAD INPUT: {exc}', file=sys.stderr)
        sys.exit(2)
