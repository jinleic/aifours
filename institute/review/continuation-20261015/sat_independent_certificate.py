#!/usr/bin/env python3
"""Parent-written rigorous checker for the finite warning-law criterion.

The producer's checkers are not imported or consulted. Exponentials use dyadic
alternating Taylor brackets after integer/fractional argument reduction.
Logarithm upper bounds are certified by checking exp(-L) <= 1-W exactly.
"""
import argparse
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import time

import mpmath

PRECISION = 768
ONE = 1 << PRECISION


class CertificateError(RuntimeError):
    pass


def floor_scaled(value):
    value = Fraction(value)
    return (value.numerator * ONE) // value.denominator


def ceil_scaled(value):
    value = Fraction(value)
    return -((-value.numerator * ONE) // value.denominator)


def decimal_upper(value, digits):
    """Render the exact rational ceiling on a decimal grid, with no float step."""
    units = math.ceil(value * 10**digits)
    whole, remainder = divmod(abs(units), 10**digits)
    return f"{'-' if units < 0 else ''}{whole}.{remainder:0{digits}d}"


def mul_lo(a, b):
    return (a * b) >> PRECISION


def mul_hi(a, b):
    return -((-(a * b)) >> PRECISION)


def exp_neg_fraction_part(scaled, upper):
    """Bracket exp(-f), 0<=f<=1, by alternating Taylor partial sums.

    Terms are nonincreasing, so every odd partial sum is a lower bound and every
    even partial sum an upper bound. Even terms are rounded down in the lower
    bound, odd terms up; the upper bound uses the opposite directions.
    """
    if not 0 <= scaled <= ONE:
        raise CertificateError("fractional exponent out of range")
    lo_term = hi_term = ONE
    lower_partial = upper_partial = ONE
    n = 0
    while True:
        n += 1
        lo_term = (lo_term * scaled) // (n * ONE)
        hi_term = -((-(hi_term * scaled)) // (n * ONE))
        previous_upper = upper_partial
        if n % 2:
            lower_partial -= hi_term
            upper_partial -= lo_term
        else:
            lower_partial += lo_term
            upper_partial += hi_term
        if n % 2 and n > 20 and hi_term < 4:
            # S_n (odd) is below exp(-f); S_{n-1} (even) is above it.
            return previous_upper + 2 if upper else lower_partial - 2


def exp_minus_one_bounds():
    """S_399 <= exp(-1) <= S_400 for the alternating Taylor partial sums."""
    partial = Fraction(0)
    fact = 1
    lower = None
    for n in range(0, 401):
        if n:
            fact *= n
        partial += Fraction((-1) ** n, fact)
        if n == 399:
            lower = partial
    return floor_scaled(lower), ceil_scaled(partial)


EXP_MINUS_ONE = exp_minus_one_bounds()


def set_precision(bits):
    """Use 2^-bits dyadic grids. Alternating sums amplify errors by about 2^j;
    use bits comfortably above the cutoff T. The recorded T=512 checks use
    768 bits, while the T=1024 checks use 1536 bits."""
    global PRECISION, ONE, EXP_MINUS_ONE
    if bits < 640:
        raise CertificateError("precision below the logarithm-certification margin")
    PRECISION, ONE = bits, 1 << bits
    EXP_MINUS_ONE = exp_minus_one_bounds()


def exp_neg_scaled(scaled, upper):
    """Directed bound for exp(-t), with t=scaled/2^P >= 0."""
    if scaled < 0:
        raise CertificateError("negative exponent passed to exp_neg_scaled")
    whole, fractional = divmod(scaled, ONE)
    result = exp_neg_fraction_part(fractional, upper)
    base = EXP_MINUS_ONE[1] if upper else EXP_MINUS_ONE[0]
    for _ in range(whole):
        result = mul_hi(result, base) if upper else mul_lo(result, base)
    if result < 0:
        result = 0
    return result


def exp_interval_nonpositive(value):
    """Enclose exp(value) for an exact rational value <= 0."""
    value = Fraction(value)
    if value > 0:
        raise CertificateError("exponent must be nonpositive")
    t_lo, t_hi = floor_scaled(-value), ceil_scaled(-value)
    return exp_neg_scaled(t_hi, upper=False), exp_neg_scaled(t_lo, upper=True)


def certified_neg_log_upper(one_minus_w):
    """Return dyadic L with exp(-L) <= 1-W, hence -log(1-W) <= L."""
    one_minus_w = Fraction(one_minus_w)
    if not 0 < one_minus_w <= 1:
        raise CertificateError("1-W must lie in (0,1]")
    if one_minus_w == 1:
        return Fraction(0)
    with mpmath.workdps(260):
        estimate = -mpmath.log(mpmath.mpf(one_minus_w.numerator) / one_minus_w.denominator)
        scaled = int(mpmath.ceil(estimate * ONE)) + (1 << (PRECISION - 600))
    for _ in range(8):
        if exp_neg_scaled(scaled, upper=True) * one_minus_w.denominator <= one_minus_w.numerator * ONE:
            return Fraction(scaled, ONE)
        scaled += 1 << (PRECISION - 500)
    raise CertificateError("failed to certify logarithm bound")


def law_product(rates, weights, arity):
    law = {}
    for indices in itertools.product(range(len(rates)), repeat=arity):
        value = Fraction(1)
        weight = Fraction(1)
        for index in indices:
            value *= rates[index]
            weight *= weights[index]
        law[value] = law.get(value, Fraction(0)) + weight
    return law


def certify(trial):
    started = time.monotonic()
    k = int(trial["k"])
    alpha = Fraction(trial["alpha"])
    rates = [Fraction(x) for x in trial["rates"]]
    weights = [Fraction(x) for x in trial["weights"]]
    T = int(trial["T"])
    epsilon = Fraction(trial["epsilon"])
    y = int(trial["y"])
    if k < 2 or T < 1 or alpha <= 0 or epsilon <= 0 or y <= 0:
        raise CertificateError("invalid scalar parameter")
    if len(rates) != len(weights) or not rates or sum(weights) != 1:
        raise CertificateError("weights must define a probability law")
    if any(not 0 <= r < 1 for r in rates) or any(w < 0 for w in weights):
        raise CertificateError("rates must lie in [0,1) and weights be nonnegative")
    lam = Fraction(k, 2) * alpha
    q_law = law_product(rates, weights, k - 1)
    complement = [(1 - value, weight) for value, weight in q_law.items()]
    moments_lo, moments_hi = [], []
    powers = [Fraction(1)] * len(complement)
    for i in range(T + 1):
        nu = sum(weight * power for (_, weight), power in zip(complement, powers))
        lo, hi = exp_interval_nonpositive(lam * (nu - 1))
        moments_lo.append(lo)
        moments_hi.append(hi)
        powers = [power * base for power, (base, _) in zip(powers, complement)]
    site_lower = Fraction(0)
    mu_rows = []
    for j in range(1, T + 1):
        lo = hi = 0
        for i in range(j + 1):
            coefficient = math.comb(j, i)
            if i % 2:
                lo -= coefficient * moments_hi[i]
                hi -= coefficient * moments_lo[i]
            else:
                lo += coefficient * moments_lo[i]
                hi += coefficient * moments_hi[i]
        lo, hi = max(lo, 0), min(hi, ONE)
        if lo > hi:
            raise CertificateError(f"empty mu enclosure at j={j}")
        site_lower += Fraction(lo * lo, ONE * ONE * j)
        if j in (1, 2, 4, 8, 16, 32, 64, 128):
            mu_rows.append({"j": j, "lower_decimal": decimal_upper(-Fraction(lo, ONE), 24).removeprefix("-"),
                            "upper_decimal": decimal_upper(Fraction(hi, ONE), 24)})
    w_law = law_product(rates, weights, k)
    log_upper = sum(weight * certified_neg_log_upper(1 - value) for value, weight in w_law.items())
    correction_upper = (k - 1) * alpha * log_upper
    psi_upper = correction_upper - site_lower
    tail_upper = Fraction(exp_neg_scaled(y * ONE, upper=True), ONE) * T
    passed = psi_upper <= -epsilon and tail_upper <= epsilon / 2
    return {
        "name": trial.get("name"), "k": k, "alpha": str(alpha), "T": T, "y": y, "epsilon": str(epsilon),
        "psi_upper_fraction_sha256": hashlib.sha256(f"{psi_upper.numerator}/{psi_upper.denominator}".encode()).hexdigest(),
        "psi_upper_decimal_outward": decimal_upper(psi_upper, 18),
        "tail_upper_decimal_outward": decimal_upper(tail_upper, 30),
        "criterion_passed": passed, "mu_samples": mu_rows,
        "seconds": round(time.monotonic() - started, 3),
    }




def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("trials", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--require", choices=("pass", "reject", "report"), default="pass")
    parser.add_argument("--names", nargs="*")
    parser.add_argument("--precision-bits", type=int, default=PRECISION)
    args = parser.parse_args()
    set_precision(args.precision_bits)
    data = json.loads(args.trials.read_text())
    trials = data.get("trials", data if isinstance(data, list) else [])
    if args.names:
        trials = [t for t in trials if t.get("name") in set(args.names)]
    if not trials:
        raise CertificateError("no trials selected")
    results = [certify(trial) for trial in trials]
    report = {"checker": Path(__file__).name, "precision_bits": PRECISION,
              "input": str(args.trials), "input_sha256": hashlib.sha256(args.trials.read_bytes()).hexdigest(),
              "requirement": args.require, "results": results}
    if args.output:
        args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    outcomes = [r["criterion_passed"] for r in results]
    if args.require == "pass" and not all(outcomes):
        raise SystemExit(1)
    if args.require == "reject" and any(outcomes):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
