#!/usr/bin/python3
"""Parent exact-rational constants/count certificate for chi(G_{n,12})=5, independent of worker code.
Reuses the mathematical procedure of chi8_parent_rational_check.py: atanh series for logarithms and positive
exponential Taylor series with geometric remainder. No FLINT, SymPy, NumPy or decimal arithmetic.
Usage: python3 -B chi12_parent_rational_check.py NEW.json (refuses overwrite).
"""
from fractions import Fraction as Q
import hashlib
import json
from math import factorial
from pathlib import Path
import subprocess
import sys


def logs(z, n=200):
    x = Q(z - 1, z + 1)
    lo = 2 * sum((x**(2*i+1) / (2*i+1) for i in range(n)), Q(0))
    hi = lo + 2 * x**(2*n+1) / ((2*n+1) * (1-x*x))
    scale = 10**45
    return Q(lo.numerator * scale // lo.denominator, scale), Q(-((-hi.numerator * scale) // hi.denominator), scale)


def exps(lo, hi, n=90):
    lower = sum((lo**i / factorial(i) for i in range(n+1)), Q(0))
    upper = sum((hi**i / factorial(i) for i in range(n+1)), Q(0))
    ratio = hi / (n+2)
    if not 0 <= ratio < 1:
        raise ValueError('Taylor-tail condition failed')
    upper += (hi**(n+1) / factorial(n+1)) / (1-ratio)
    return lower, upper


def outward(lo, hi, digits=24):
    scale = 10**digits
    return {'lower_numerator': lo.numerator * scale // lo.denominator,
            'upper_numerator': -((-hi.numerator * scale) // hi.denominator), 'denominator': scale}


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    l4,u4 = logs(4)
    l5,u5 = logs(5)
    l11,u11 = logs(11)
    elo,ehi = exps(Q(5,6)*l4*l11, Q(5,6)*u4*u11)
    dlo,dhi = 1/ehi-Q(1,16), 1/elo-Q(1,16)
    e5lo,e5hi = exps(Q(11,6)*l5, Q(11,6)*u5)
    klo,khi = Q(121,18)*dlo, Q(121,18)*dhi
    C_lo,C_hi = Q(121,600)*dlo*e5lo, Q(121,600)*dhi*e5hi
    s22 = sum((Q(12**j, factorial(j)) for j in range(22)), Q(0))
    D1,D2,tail = Q(38400,17),Q(2400,17),Q(9,50)
    preimages = [factorial(12*r)//factorial(12)**r for r in range(1,5)]
    checks = {
        'log11_upper_below_12_over_5': u11 < Q(12,5),
        '22_term_exact_certificate': s22-11**5 == Q(545861266838,761674375) > 0,
        '21_terms_insufficient': s22-Q(12**21,factorial(21)) < 11**5,
        'delta_strictly_positive': dlo > 0,
        'C12_outward_interval': Q(586620539754832511083,10**24) < C_lo < C_hi < Q(586620539754832511084,10**24),
        'variance_factor': Q(40*121,5*144) == Q(121,18),
        'first_epsilon_bound': Q(3,1600)/D1 == Q(17,20480000),
        'second_epsilon_bound': tail/D2 == Q(51,40000),
        'first_implies_second': Q(17,20480000) < Q(51,40000),
        'H1': 25-10-12+2 == 5,
        'SSC_ratio': Q(11,16) < 1,
        'EY_growth': 5*Q(4,5)**6 == Q(4096,3125) > 1,
        'Molloy_Reed': 4*Q(3,4)**6 == Q(729,1024) < 1,
        'S2_S1_polynomial_degree': 25+Q(25,2)+Q(401,2)+4 == 242,
        'residue_preimages': preimages == [1,2704156,3384731762521200,235809301462142612780721600]
    }
    record = {'recorded_at_pt': subprocess.check_output(['date','+%Y-%m-%d %H:%M:%S %Z'], text=True).strip(),
              'script_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'method': {'atanh_terms':200,'rational_log_grid_digits':45,'exp_degree':90},
              'log11':outward(l11,u11),'a_squared_minus_1_over_16':outward(dlo,dhi),
              'kappa':outward(klo,khi),'E0':outward(200/e5hi,200/e5lo),'C12':outward(C_lo,C_hi),
              'e12_partial_sum_minus_11_power5':str(s22-11**5),'preimages':preimages,'checks':checks,
              'all_ok':all(checks.values()),
              'scope':'Independent exact constants/counts only; not the universal matrix inequality or probabilistic transfer.'}
    with open(sys.argv[1], 'x') as f:
        json.dump(record,f,indent=2)
        f.write('\n')
    print(json.dumps({'all_ok':record['all_ok'],'checks':len(checks),'C12':record['C12']}))
    return 0 if record['all_ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
