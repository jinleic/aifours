"""Exact outward-rounded certification of the finite energetic functional.

Only Python standard-library integer/Fraction arithmetic enters inequalities.
The input gives a rational law for R. The proof of the analytic bound is in
notes/PROOF.md. This implementation uses repeated squaring for exponentials
and the positive power series for -log(1-z). An algorithmically distinct
implementation of the same formula uses a Taylor/reciprocal exponential and
an atanh logarithm instead. Both were written by the same producer.
"""
import argparse
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
import json
from math import comb
from pathlib import Path
import sys
import time


BITS = 384
SCALE = 1 << BITS
EXP_HALVINGS = 220
LOG_TERMS = 160


def floor_grid(x):
    return x.numerator * SCALE // x.denominator


def ceil_grid(x):
    return -((-x.numerator * SCALE) // x.denominator)


def product_law(rates, weights, arity):
    ans = defaultdict(F)
    for indices in product(range(len(rates)), repeat=arity):
        r, w = F(1), F(1)
        for i in indices:
            r *= rates[i]
            w *= weights[i]
        ans[r] += w
    assert sum(ans.values()) == 1
    return sorted(ans.items())


def exp_interval_nonpositive(x):
    """Enclose exp(x) for x <= 0 with integer endpoints divided by SCALE.

    At u=x/2^s, max(0,1+u) <= exp(u) <= 1/(1-u). Squaring
    nonnegative intervals s times with outward rounding is rigorous.
    """
    assert x <= 0
    u = x / (1 << EXP_HALVINGS)
    lo = max(0, floor_grid(1 + u))
    hi = ceil_grid(1 / (1 - u))
    for _ in range(EXP_HALVINGS):
        lo = lo * lo // SCALE
        hi = -((-hi * hi) // SCALE)
    assert 0 <= lo <= hi <= SCALE
    return lo, hi


def minus_log_bounds(z):
    """S_N <= -log(1-z) <= S_N+z^(N+1)/((N+1)(1-z))."""
    assert 0 <= z < 1
    power, lower = z, F(0)
    for j in range(1, LOG_TERMS + 1):
        lower += power / j
        power *= z
    return lower, lower + power / ((LOG_TERMS + 1) * (1 - z))


def decimal_outward(x, places=18, upper=False):
    d = 10 ** places
    n = -((-x.numerator * d) // x.denominator) if upper else x.numerator * d // x.denominator
    sign = '-' if n < 0 else ''
    n = abs(n)
    return f"{sign}{n // d}.{n % d:0{places}d}"


def certify(trial):
    name = trial['name']
    k, alpha, T = int(trial['k']), F(trial['alpha']), int(trial['T'])
    rates, weights = list(map(F, trial['rates'])), list(map(F, trial['weights']))
    epsilon, y = F(trial['epsilon']), int(trial['y'])
    assert k >= 2 and alpha > 0 and T >= 1 and epsilon > 0 and y > 0
    assert len(rates) == len(weights) and rates
    assert all(0 <= x < 1 for x in rates)
    assert all(w >= 0 for w in weights) and sum(weights) == 1
    degree_law = product_law(rates, weights, k - 1)
    correction_law = product_law(rates, weights, k)
    lam = k * alpha / 2
    moments = []
    # Recursively generated powers are exact rational numbers.
    powers = [F(1)] * len(degree_law)
    for i in range(T + 1):
        nu = sum((w * p for (_, w), p in zip(degree_law, powers)), F(0))
        moments.append(exp_interval_nonpositive(lam * (nu - 1)))
        powers = [p * (1 - z) for p, (z, _) in zip(powers, degree_law)]
    site_upper = F(0)
    site_lower = F(0)
    mu_bounds = []
    for j in range(1, T + 1):
        low, high = 0, 0
        for i in range(j + 1):
            c = (-1) ** i * comb(j, i)
            l, u = moments[i]
            low += c * (l if c >= 0 else u)
            high += c * (u if c >= 0 else l)
        low, high = max(0, low), min(SCALE, high)
        assert low <= high
        mu_bounds.append((low, high))
        site_upper -= F(low * low, j * SCALE * SCALE)
        site_lower -= F(high * high, j * SCALE * SCALE)
    correction_lower, correction_upper = F(0), F(0)
    for z, w in correction_law:
        l, u = minus_log_bounds(z)
        correction_lower += (k - 1) * alpha * w * l
        correction_upper += (k - 1) * alpha * w * u
    lower = site_lower + correction_lower
    upper = site_upper + correction_upper
    _, exp_minus_y_upper = exp_interval_nonpositive(F(-y))
    finite_y_error = T * F(exp_minus_y_upper, SCALE)
    assert upper <= -epsilon, f"{name}: claimed negative margin fails: upper={float(upper):.9g}"
    assert finite_y_error <= epsilon / 2, f"{name}: finite-y error too large"
    result = {
        'name': name,
        'k': k,
        'alpha': str(alpha),
        'T': T,
        'epsilon': str(epsilon),
        'y': y,
        'bits': BITS,
        'exponential_halvings': EXP_HALVINGS,
        'log_terms': LOG_TERMS,
        'functional_lower': str(lower),
        'functional_upper': str(upper),
        'functional_decimal_enclosure': [decimal_outward(lower), decimal_outward(upper, upper=True)],
        'site_decimal_enclosure': [decimal_outward(site_lower), decimal_outward(site_upper, upper=True)],
        'correction_decimal_enclosure': [decimal_outward(correction_lower), decimal_outward(correction_upper, upper=True)],
        'finite_y_error_upper': str(finite_y_error),
        'poisson_energy_per_variable_lower': str(epsilon / (2 * y)),
        'eventual_fixed_model_energy_per_variable_lower': str(epsilon / (4 * y)),
        'moment_intervals_numerators': moments,
        'mu_intervals_numerators': mu_bounds,
    }
    print(f"PASS {name}: Psi_{T} in [{result['functional_decimal_enclosure'][0]}, {result['functional_decimal_enclosure'][1]}] <= -{epsilon}", flush=True)
    print(f"  finite-y error < {decimal_outward(finite_y_error, upper=True)}; E ground/n >= {epsilon/(2*y)} in Poisson/repeated model", flush=True)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--trials', default='certificates/trials.json')
    parser.add_argument('--name', default='all')
    parser.add_argument('--output')
    args = parser.parse_args()
    trials = json.loads(Path(args.trials).read_text())['trials']
    selected = [t for t in trials if args.name in ('all', t['name'])]
    assert selected, 'No trial selected'
    start = time.monotonic()
    results = [certify(t) for t in selected]
    if args.output:
        Path(args.output).write_text(json.dumps({'certificates': results}, indent=2) + '\n')
    print(f"Certified {len(results)} trial(s) in {time.monotonic()-start:.2f} seconds.")


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, ValueError, KeyError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
