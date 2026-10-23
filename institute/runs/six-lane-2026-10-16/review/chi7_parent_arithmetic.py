"""Independent parent exact-rational checks for the chi(G(n,7)) proof; standard library, no worker imports.
The logarithm enclosure is derived from log3=2*sum_{k>=0}(1/2)^(2k+1)/(2k+1), with a positive geometric-tail
bound. This checks arithmetic premises and the degree-eight obstruction, not the probabilistic import chain.
Usage: python3 -B chi7_parent_arithmetic.py NEW_RECEIPT.json
"""
from datetime import datetime
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys
from zoneinfo import ZoneInfo


def det(A):
    B = [list(row) for row in A]
    ans = F(1)
    for i in range(len(B)):
        pivot = next((j for j in range(i, len(B)) if B[j][i]), None)
        if pivot is None:
            return F(0)
        if pivot != i:
            B[i], B[pivot] = B[pivot], B[i]
            ans = -ans
        q = B[i][i]
        ans *= q
        for j in range(i + 1, len(B)):
            t = B[j][i] / q
            for k in range(i + 1, len(B)):
                B[j][k] -= t * B[i][k]
    return ans


def main():
    out = Path(sys.argv[1])
    if out.exists():
        raise SystemExit('Refusing to overwrite receipt')
    z, terms = F(1, 2), 2
    lo = 2 * sum((z ** (2*k + 1) / (2*k + 1) for k in range(terms)), F(0))
    hi = lo + 2 * z ** (2*terms + 1) / ((2*terms + 1) * (1 - z*z))
    c7lo, c7hi = F(3, 8)*lo-F(7, 18), F(3, 8)*hi-F(7, 18)
    critical_lo, critical_hi = F(27, 4)*lo, F(27, 4)*hi
    JI = [[F(1 + (i == j)) for j in range(3)] for i in range(3)]
    H = [[F(3, 10)*JI[i//3][j//3]*JI[i%3][j%3] for j in range(9)] for i in range(9)]
    minors = [det([row[:n] for row in H[:n]]) for n in range(1, 10)]
    M8 = [[F(5, 8) if i == j else F(1, 8) for j in range(4)] for i in range(4)]
    checks = {
        'log3_interval_exactly_13_over12_to11_over10': (lo, hi) == (F(13, 12), F(11, 10)),
        'C7_lower_is_5_over288_positive': c7lo == F(5, 288) and c7lo > 0,
        'C7_upper_is_17_over720': c7hi == F(17, 720),
        'sharpened_degree_threshold_strictly_between7_and8': 7 < critical_lo < critical_hi < 8,
        'original_threshold_between6_and7': 6 < 6*lo < 6*hi < 7,
        'degree6_global_decay_control_positive': F(3, 8)*lo-F(6, 18) > 0,
        'degree8_decay_control_negative': F(3, 8)*hi-F(8, 18) < 0,
        'EY_growth_base_squared_exceeds_one': 16*F(3, 4)**7 == F(2187, 1024) and F(2187, 1024) > 1,
        'non3colourability_degree7_first_moment_base_squared': 9*F(2, 3)**7 == F(128, 243) and F(128, 243) < 1,
        'non3colourability_degree6_control': 9*F(2, 3)**6 == F(64, 81) and F(64, 81) < 1,
        'degree5_first_moment_control_inconclusive': 9*F(2, 3)**5 == F(32, 27) and F(32, 27) > 1,
        'SSC_series_ratio_is_two_thirds_less_than_one': F(6, 9) == F(2, 3) and F(6, 9) < 1,
        'Gaussian_H_positive_by_all_leading_principal_minors': all(x > 0 for x in minors),
        'Gaussian_H_determinant_matches_formula': minors[-1] == 4**6*F(3, 10)**9,
        'degree8_point_is_doubly_stochastic': all(sum(row) == 1 for row in M8) and all(sum(row[j] for row in M8) == 1 for j in range(4)),
        'degree8_point_squared_Frobenius_is_7_over4': sum(x*x for row in M8 for x in row) == F(7, 4),
        'degree8_exact_integer_phi_obstruction_positive': 13**32 > 2**56*3**32*5**5,
        'eta_interior_beats_endpoint': 3**9 < 2**16,
    }
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'driver_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'checks': checks,
              'log3_enclosure': [str(lo), str(hi)], 'C7_enclosure': [str(c7lo), str(c7hi)],
              'Gaussian_H_leading_minors': list(map(str, minors)),
              'status': 'PARENT_EXACT_CHI7_ARITHMETIC_AND_CONTROLS_PASS' if all(checks.values()) else 'FAILED',
              'limits': 'Arithmetic premises only. The log enclosure uses the stated classical atanh-series identity; the global entropy inequality and KPW probabilistic bridge are reviewed written arguments, not established by this script.'}
    with out.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({k: result[k] for k in ['status', 'log3_enclosure', 'C7_enclosure', 'checks']}, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == '__main__':
    raise SystemExit(main())
