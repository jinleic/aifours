#!/usr/bin/env python3
"""Certifier A: rigorous outward-rounded enclosure of Psi_T (product-law route).

Psi_T(rho, alpha) = -sum_{j=1}^T mu_j^2 / j - (k-1) alpha E log(1 - R_1...R_k),
mu_j = sum_i (-1)^i binom(j,i) M_i,  M_i = exp(lambda (nu_i - 1)),
nu_i = E (1 - Q)^i,  Q = R_1...R_{k-1},  lambda = k alpha / 2,
for a finitely supported rational warning law rho on [0,1)  (notes/PROOF.md).

Algorithm (deliberately different from certifier B):
  * exact Fraction enumeration of the (k-1)- and k-fold product laws over
    multisets with multinomial masses;
  * nu_i as binary fixed-point intervals from per-atom power recurrences;
  * exp by exact argument reduction x/2^64, an alternating Taylor enclosure,
    then 64 outward-rounded squarings;
  * mu_j by an interval forward-difference table;
  * -log(1-z) per product atom by the power series plus its geometric tail.
Every rounding is directed (floor for lower, ceil for upper endpoints).
Gating uses explicit exceptions; no assert statements are used, so the
checks cannot be disabled with python -O.

Exit status: 0 certified; 1 rejected (rigorous upper bound not <= -epsilon or
finite-y condition fails); 2 malformed input.
"""
import argparse
import hashlib
import json
import sys
import time
from collections import Counter
from fractions import Fraction
from itertools import combinations_with_replacement
from math import factorial
from pathlib import Path

HALVINGS = 64          # exp argument reduction x / 2^HALVINGS
CLAUSE_BITS = 192      # precision of the clause (log) term, absolute


class Rejected(Exception):
    pass


class BadInput(Exception):
    pass


def require(cond, msg, exc=Rejected):
    if not cond:
        raise exc(msg)


def floor_div(a, b):
    return a // b


def ceil_div(a, b):
    return -((-a) // b)


def fx_floor(q, bits):
    return floor_div(q.numerator << bits, q.denominator)


def fx_ceil(q, bits):
    return ceil_div(q.numerator << bits, q.denominator)


# ---------------------------------------------------------------- input
def parse_trial(trial):
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
    require(k >= 2, 'k must be >= 2', BadInput)
    require(T >= 1, 'T must be >= 1', BadInput)
    require(alpha > 0 and eps > 0 and y > 0, 'alpha, epsilon, y must be positive', BadInput)
    require(len(rates) == len(weights) and len(rates) >= 1, 'rates/weights length mismatch', BadInput)
    require(all(0 <= r < 1 for r in rates), 'every rate must lie in [0,1)', BadInput)
    require(all(w >= 0 for w in weights), 'weights must be nonnegative', BadInput)
    require(sum(weights) == 1, 'weights must sum to exactly 1', BadInput)
    return k, T, alpha, eps, y, rates, weights


def product_law(rates, weights, arity):
    """Exact law of a product of `arity` iid draws, merged by value."""
    law = {}
    m = len(rates)
    for combo in combinations_with_replacement(range(m), arity):
        mass = Fraction(factorial(arity))
        value = Fraction(1)
        for idx, c in Counter(combo).items():
            mass = mass * weights[idx] ** c / factorial(c)
            value *= rates[idx] ** c
        law[value] = law.get(value, Fraction(0)) + mass
    require(sum(law.values()) == 1, f'{arity}-fold product law does not have mass 1', BadInput)
    return sorted(law.items())


# ---------------------------------------------------------------- exp
def exp_enclosure_nonpos(x, out_bits):
    """Return (lo, hi) integers with lo/2^out <= exp(x) <= hi/2^out, x <= 0 rational."""
    require(x <= 0, 'exp_enclosure_nonpos needs x <= 0', BadInput)
    work = out_bits + HALVINGS + 96
    u = x / (1 << HALVINGS)                  # exact; |u| < 2^-40 for |x| < 2^24
    require(-u < Fraction(1, 1 << 20), 'argument too large for the reduced Taylor step', BadInput)
    a = -u                                    # a >= 0, exp(u) = sum (-a)^n / n!
    a_lo, a_hi = fx_floor(a, work), fx_ceil(a, work)
    one = 1 << work
    # magnitudes a^n / n! with directed rounding; terms strictly decrease (a<1)
    m_lo, m_hi = [one], [one]
    n = 0
    while True:
        n += 1
        m_lo.append(floor_div(m_lo[-1] * a_lo, n << work))
        m_hi.append(ceil_div(m_hi[-1] * a_hi, n << work))
        if m_hi[-1] <= 1 and n >= 2:
            break
    N = n - 1                                 # last included index; m_hi[n] bounds the tail
    s_lo = sum(m_lo[i] if i % 2 == 0 else -m_hi[i] for i in range(N + 1)) - m_hi[N + 1]
    s_hi = sum(m_hi[i] if i % 2 == 0 else -m_lo[i] for i in range(N + 1)) + m_hi[N + 1]
    lo, hi = max(0, s_lo), s_hi
    require(lo <= hi, 'internal exp enclosure inverted')
    for _ in range(HALVINGS):
        lo = (lo * lo) >> work
        hi = ceil_div(hi * hi, one)
    shift = work - out_bits
    return lo >> shift, ceil_div(hi, 1 << shift)


# ---------------------------------------------------------------- -log(1-z)
def minus_log1m_enclosure(z, bits):
    """(lo, hi) with lo/2^bits <= -log(1-z) <= hi/2^bits for rational 0 <= z < 1."""
    require(0 <= z < 1, 'log argument outside [0,1)', BadInput)
    if z == 0:
        return 0, 0
    z_lo, z_hi = fx_floor(z, bits), fx_ceil(z, bits)
    one = 1 << bits
    p_lo, p_hi = z_lo, z_hi                   # z^h enclosures
    s_lo, s_hi = 0, 0
    h = 1
    while True:
        s_lo += floor_div(p_lo, h)
        s_hi += ceil_div(p_hi, h)
        p_lo = (p_lo * z_lo) >> bits
        p_hi = ceil_div(p_hi * z_hi, one)
        h += 1
        # tail after the terms already added: sum_{h' >= h} z^h'/h' <= z^h / (h (1-z))
        tail = Fraction(p_hi, one) / (h * (1 - z))
        if tail < Fraction(1, one):
            break
    return s_lo, s_hi + fx_ceil(tail, bits)


# ---------------------------------------------------------------- main computation
def certify(trial, verbose=True):
    t0 = time.monotonic()
    name = trial.get('name', '?')
    k, T, alpha, eps, y, rates, weights = parse_trial(trial)
    lam = Fraction(k) * alpha / 2
    P = T + 192 + 8 * len(rates)
    one = 1 << P

    # nu_i = E (1-Q)^i, Q from the exact (k-1)-fold product law
    qlaw = product_law(rates, weights, k - 1)
    nu_lo = [0] * (T + 1)
    nu_hi = [0] * (T + 1)
    for q, w in qlaw:
        b = 1 - q
        b_lo, b_hi = fx_floor(b, P), fx_ceil(b, P)
        p_lo = p_hi = one
        wn, wd = w.numerator, w.denominator
        for i in range(T + 1):
            nu_lo[i] += floor_div(wn * p_lo, wd)
            nu_hi[i] += ceil_div(wn * p_hi, wd)
            p_lo = (p_lo * b_lo) >> P
            p_hi = ceil_div(p_hi * b_hi, one)
    nu_hi = [min(v, one) for v in nu_hi]       # nu_i <= 1 exactly

    # M_i = exp(lambda (nu_i - 1)), monotone in nu_i
    M_lo, M_hi = [], []
    for i in range(T + 1):
        x_lo = Fraction(nu_lo[i] - one, one) * lam
        x_hi = Fraction(nu_hi[i] - one, one) * lam
        lo, _ = exp_enclosure_nonpos(x_lo, P)
        _, hi = exp_enclosure_nonpos(x_hi, P)
        M_lo.append(lo)
        M_hi.append(min(hi, one))

    # mu_j = (Delta^j M)_0 with Delta u_i = u_i - u_{i+1}; interval difference table
    row_lo, row_hi = M_lo[:], M_hi[:]
    mu = []
    for j in range(1, T + 1):
        row_lo, row_hi = ([row_lo[i] - row_hi[i + 1] for i in range(len(row_lo) - 1)],
                          [row_hi[i] - row_lo[i + 1] for i in range(len(row_hi) - 1)])
        lo, hi = max(0, row_lo[0]), min(one, row_hi[0])   # mu_j = E(1-A)^j in [0,1]
        require(lo <= hi, f'mu_{j} enclosure inverted')
        mu.append((lo, hi))
    width_mu = max(hi - lo for lo, hi in mu)

    # site sum S = sum mu_j^2 / j, in units 2^(-2P)
    S_lo = sum(floor_div(lo * lo, j) for j, (lo, _) in enumerate(mu, start=1))
    S_hi = sum(ceil_div(hi * hi, j) for j, (_, hi) in enumerate(mu, start=1))

    # clause correction C = (k-1) alpha E[-log(1 - R_1...R_k)]
    zlaw = product_law(rates, weights, k)
    C_lo = Fraction(0)
    C_hi = Fraction(0)
    for z, w in zlaw:
        lo, hi = minus_log1m_enclosure(z, CLAUSE_BITS)
        C_lo += w * lo
        C_hi += w * hi
    C_lo = C_lo * (k - 1) * alpha / (1 << CLAUSE_BITS)
    C_hi = C_hi * (k - 1) * alpha / (1 << CLAUSE_BITS)

    psi_lo = -Fraction(S_hi, one * one) + C_lo
    psi_hi = -Fraction(S_lo, one * one) + C_hi

    # finite-y error T exp(-y)
    _, ey_hi = exp_enclosure_nonpos(-y, 128)
    fy = T * Fraction(ey_hi, 1 << 128)

    out = {
        'name': name, 'certifier': 'A (product law, binary grid, reduced Taylor + squaring)',
        'k': k, 'T': T, 'alpha': str(alpha), 'epsilon': str(eps), 'y': str(y),
        'precision_bits': P,
        'psi_enclosure': [dec(psi_lo, False), dec(psi_hi, True)],
        'psi_upper_exact': f'{psi_hi.numerator}/{psi_hi.denominator}' if psi_hi.denominator < 10**4000 else None,
        'site_enclosure': [dec(Fraction(S_lo, one * one), False), dec(Fraction(S_hi, one * one), True)],
        'clause_enclosure': [dec(C_lo, False), dec(C_hi, True)],
        'mu_max_width': dec(Fraction(width_mu, one), True),
        'finite_y_error_upper': dec(fy, True),
        'q_atoms': len(qlaw), 'z_atoms': len(zlaw),
    }
    if verbose:
        print(f'PSI_ENCLOSURE {name} {out["psi_enclosure"][0]} {out["psi_enclosure"][1]}', flush=True)
    margin_ok = psi_hi <= -eps
    fy_ok = fy <= eps / 2
    out['psi_upper_le_minus_epsilon'] = margin_ok
    out['finite_y_ok'] = fy_ok
    out['psi_lower_positive'] = psi_lo > 0
    out['seconds'] = round(time.monotonic() - t0, 2)
    return out


def dec(q, upper, places=20):
    """Outward-rounded decimal string of a Fraction."""
    d = 10 ** places
    n = ceil_div(q.numerator * d, q.denominator) if upper else floor_div(q.numerator * d, q.denominator)
    sign = '-' if n < 0 else ''
    n = abs(n)
    return f'{sign}{n // d}.{n % d:0{places}d}'


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
    results = []
    failures = []
    for t in chosen:
        res = certify(t)
        res['trials_sha256'] = hashlib.sha256(raw).hexdigest()
        results.append(res)
        if res['psi_upper_le_minus_epsilon'] and res['finite_y_ok']:
            print(f"CERTIFIED {res['name']}: Psi_{res['T']} <= {res['psi_enclosure'][1]} <= -{res['epsilon']}; "
                  f"T exp(-y) <= {res['finite_y_error_upper']} <= epsilon/2 ({res['seconds']} s)", flush=True)
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
