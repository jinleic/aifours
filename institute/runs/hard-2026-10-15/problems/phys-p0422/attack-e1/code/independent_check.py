"""Independent exact replay: no imports from the producer or its results.

Reads only rational trial data. Uses multinomial compositions, a positive
Taylor enclosure followed by reciprocation, decimal fixed-point arithmetic,
and the atanh expansion of the logarithm. These differ from the producer's
ordered tuples, repeated-squaring elementary bounds, binary grid, and log
power series. No numerical approximation is used in an assertion.
"""
import argparse
from fractions import Fraction
import json
from math import comb, factorial
from pathlib import Path
import sys
import time


D = 10 ** 150
TAYLOR_N = 160
ATANH_N = 160
REDUCE = 128


def updiv(a, b):
    assert b > 0
    return -((-a) // b)


def compositions(total, size):
    if size == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, size - 1):
                yield (first,) + rest


def weighted_products(rates, weights, arity):
    out = []
    for counts in compositions(arity, len(rates)):
        value, mass = Fraction(1), Fraction(factorial(arity))
        for r, w, c in zip(rates, weights, counts):
            value *= r ** c
            mass *= w ** c / factorial(c)
        out.append((value, mass))
    assert sum(mass for _, mass in out) == 1
    return out


def exp_negative(a):
    """Enclose exp(-a), a>=0, on the grid 1/D using positive Taylor.

    e^(a/128) lies between its positive Taylor polynomial and that
    polynomial plus a geometric upper bound on its positive tail.
    Reciprocate the interval and square seven times to get exp(-a).
    """
    assert a >= 0
    t = a / REDUCE
    lo_t = t.numerator * D // t.denominator
    hi_t = updiv(t.numerator * D, t.denominator)
    assert hi_t < D  # t < 1 suffices for the tail estimate below.
    low_term = high_term = D
    low_sum = high_sum = D
    for j in range(1, TAYLOR_N + 1):
        low_term = low_term * lo_t // (D * j)
        high_term = updiv(high_term * hi_t, D * j)
        low_sum += low_term
        high_sum += high_term
    next_term = updiv(high_term * hi_t, D * (TAYLOR_N + 1))
    # Later Taylor-term ratios are at most hi_t/(D*(N+2)).
    tail = updiv(next_term * D * (TAYLOR_N + 2), D * (TAYLOR_N + 2) - hi_t)
    high_sum += tail
    lo = D * D // high_sum
    hi = updiv(D * D, low_sum)
    for _ in range(7):
        lo, hi = lo * lo // D, updiv(hi * hi, D)
    assert 0 <= lo <= hi <= D
    return lo, hi


def minus_log(z):
    assert 0 <= z < 1
    u = z / (2 - z)
    term, lo = u, Fraction(0)
    for j in range(ATANH_N):
        lo += 2 * term / (2 * j + 1)
        term *= u * u
    hi = lo + 2 * term / ((2 * ATANH_N + 1) * (1 - u * u))
    return lo, hi


def check(trial):
    k = int(trial['k'])
    alpha = Fraction(trial['alpha'])
    epsilon = Fraction(trial['epsilon'])
    nterms = int(trial['T'])
    y = int(trial['y'])
    rs = [Fraction(v) for v in trial['rates']]
    ws = [Fraction(v) for v in trial['weights']]
    assert len(rs) == len(ws) and rs
    assert k >= 2 and alpha > 0 and epsilon > 0 and nterms >= 1 and y > 0
    assert all(0 <= r < 1 for r in rs)
    assert all(w >= 0 for w in ws) and sum(ws) == 1
    law = weighted_products(rs, ws, k - 1)
    M = []
    for power in range(nterms + 1):
        # Recompute exact powers independently instead of using the producer's
        # recursive power table or any supplied moment/interval table.
        nu = sum((mass * (1 - p) ** power for p, mass in law), Fraction(0))
        M.append(exp_negative(k * alpha * (1 - nu) / 2))
    variable_upper = Fraction(0)
    variable_lower = Fraction(0)
    for j in range(1, nterms + 1):
        low, high = 0, 0
        for i in range(j + 1):
            c = comb(j, i)
            if i % 2 == 0:
                low += c * M[i][0]
                high += c * M[i][1]
            else:
                low -= c * M[i][1]
                high -= c * M[i][0]
        low, high = max(0, low), min(D, high)
        assert low <= high
        variable_upper -= Fraction(low * low, D * D * j)
        variable_lower -= Fraction(high * high, D * D * j)
    clause_upper = clause_lower = Fraction(0)
    for p, mass in weighted_products(rs, ws, k):
        lower_log, upper_log = minus_log(p)
        clause_upper += (k - 1) * alpha * mass * upper_log
        clause_lower += (k - 1) * alpha * mass * lower_log
    low_total = variable_lower + clause_lower
    high_total = variable_upper + clause_upper
    _, error_exp_hi = exp_negative(Fraction(y))
    error_upper = nterms * Fraction(error_exp_hi, D)
    assert high_total <= -epsilon, f"{trial['name']}: negative-margin certificate REJECTED"
    assert error_upper <= epsilon / 2, f"{trial['name']}: finite-y margin REJECTED"
    # These displays are rounded integer bounds; floats are not needed even
    # for the output used by the report.
    scale = 10 ** 18
    out_lo = low_total.numerator * scale // low_total.denominator
    out_hi = updiv(high_total.numerator * scale, high_total.denominator)
    print(f"INDEPENDENT PASS {trial['name']}: {out_lo}/10^18 <= Psi <= {out_hi}/10^18 <= -{epsilon}", flush=True)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--trials', default='certificates/trials.json')
    p.add_argument('--name', default='all')
    args = p.parse_args()
    trials = json.loads(Path(args.trials).read_text())['trials']
    chosen = [t for t in trials if args.name in ('all', t['name'])]
    assert chosen, 'No trial selected'
    begin = time.monotonic()
    for trial in chosen:
        check(trial)
    print(f"Independent checks completed in {time.monotonic()-begin:.2f} seconds.")


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, ValueError, KeyError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        sys.exit(1)
