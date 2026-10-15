#!/usr/bin/env python3
"""Independent finite exact-arithmetic checks; these are not asymptotic proofs.
Reproduce: python3 work/check_algebra.py
No imports from illustrate.py, and no optimization solver is used.
"""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]


def positive(x):
    return max(Q(0), x)


def loss(x):
    return 10*abs(x)+positive(x-1)


def geometry(a, b, t, v):
    return (2*positive(a-t)+2*positive(-a-t)
            +2*positive(b+v-t)+2*positive(-b+v-t)
            +positive(t)/2+positive(t-v)/2)


def main():
    geometry_count = identity_count = selection_count = 0
    grid = [Q(i, 2) for i in range(-8, 9)]
    for a, b in product(grid, repeat=2):
        optimum_t, optimum_v = abs(a), abs(a)-abs(b)
        target = (abs(a)+abs(b))/2
        assert geometry(a, b, optimum_t, optimum_v) == target
        for t, v in product(grid, repeat=2):
            value = geometry(a, b, t, v)
            assert value >= target
            if value == target:
                assert (t, v) == (optimum_t, optimum_v)
            geometry_count += 1
    for d, linear, error in product((Q(1, 10), Q(1, 100)), grid, (-1, 1)):
        assert abs(d*linear) < 1
        observed = loss(error+d*linear)-loss(Q(error))
        predicted = 10*error*d*linear+(d*positive(linear) if error == 1 else 0)
        assert observed == predicted
        identity_count += 1
    limit_counts = {-1: 0, 0: 0, 1: 0}
    for a, b, ap, bp in product((-1, 1), repeat=4):
        s1 = a if a == ap else 0
        s2 = b if b == bp else 0
        v = abs(s1)-abs(s2)
        limit_counts[v] += 1
        for e, ep, candidate in product((a, b), (ap, bp), grid):
            optimum = e if e == ep else 0
            optimum_value = loss(e-optimum)+loss(ep-optimum)+Q(1, 10)*abs(optimum)
            value = loss(e-candidate)+loss(ep-candidate)+Q(1, 10)*abs(candidate)
            assert value >= optimum_value
            if value == optimum_value:
                assert candidate == optimum
            selection_count += 1
    assert limit_counts == {-1: 4, 0: 8, 1: 4}
    packing = []
    for j in range(1, 7):
        occupied, chosen = set(), []
        powers = [4**k for k in range(1, j+1)]
        for n in range(4**j, 4**(j+1)):
            locations = {n+k for k in powers}
            if locations.isdisjoint(occupied):
                chosen.append(n)
                occupied.update(locations)
        denominator = j*(j-1)+1
        assert len(chosen)*denominator >= 3*4**j
        assert len(occupied) == j*len(chosen)
        packing.append({"j": j, "selected_windows": len(chosen),
                        "lower_bound": str(Q(3*4**j, denominator)),
                        "distinct_error_indices": len(occupied)})
    for e, ep in product((Q(-1, 4), Q(1, 4)), repeat=2):
        lower, upper = max(2*(e-1), 2*(ep-1)), min(2*(e+1), 2*(ep+1))
        assert lower <= Q(-3, 2) < 0 < Q(3, 2) <= upper
    # Independent 2x2 calculation: two close quadratic minima can pool far away.
    quadratic = []
    for delta in (Q(1, 2), Q(1, 10), Q(1, 100)):
        determinant = delta**4
        y = delta**2/(delta**2+delta**4)
        assert determinant > 0
        assert y == 1/(1+delta**2)
        quadratic.append({"half_minimizer_norm": str(delta),
                          "pooled_minimizer_norm": str(y),
                          "half_hessian_determinant": str(determinant)})
    result = {"verdict": "PASS", "scope": "finite exact arithmetic, not an asymptotic proof",
              "geometry_grid_checks": geometry_count,
              "local_loss_identity_checks": identity_count,
              "pooled_coordinate_grid_checks": selection_count,
              "rademacher_limit_counts_out_of_16": limit_counts,
              "disjoint_window_packings": packing,
              "generic_convexity_counterexample": quadratic,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (ROOT/'evidence/exact-checks.json').write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
