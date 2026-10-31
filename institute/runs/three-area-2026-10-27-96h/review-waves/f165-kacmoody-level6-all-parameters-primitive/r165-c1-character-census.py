#!/usr/bin/env python3
# r165 reviewer-authored control C1 (independent of author code).
# Exact census of f1/f2-lowest multiplicities in the free Lie algebra L(M) on the
# 8-dimensional level-one sl3-adjoint module M, by the multigraded Witt formula and the
# finite-A2 Weyl alternating formula.  Pure Python integers only.
# Also parses the two mandatory JSON inputs completely and compares their stated numbers.
import json, sys, hashlib, subprocess
from collections import defaultdict
from math import gcd

def clock():
    return subprocess.run(['/bin/date'], capture_output=True, text=True).stdout.strip()

START = clock()
# Letter degrees (alpha1, alpha2) of u0..u7 = v, Xv, Yv, Zv, XYv, ZXv, ZYv, Z^2v (each at level 1).
LET = [(0, 0), (1, 0), (0, 1), (1, 1), (1, 1), (2, 1), (1, 2), (2, 2)]
NMAX = 7

Tw = {0: {(0, 0): 1}}           # number of words of length n and degree (a,b)
for n in range(1, NMAX + 1):
    d = defaultdict(int)
    for (a, b), c in Tw[n - 1].items():
        for (x, y) in LET:
            d[(a + x, b + y)] += c
    Tw[n] = dict(d)

def mobius(n):
    res, m, p = 1, n, 2
    while p * p <= m:
        if m % p == 0:
            m //= p
            if m % p == 0:
                return 0
            res = -res
        p += 1
    if m > 1:
        res = -res
    return res

def lie(n, a, b, witt=True):
    if a < 0 or b < 0:
        return 0
    if not witt:                 # deliberately wrong formula for the negative control
        return Tw[n].get((a, b), 0) / n
    g = gcd(gcd(n, a), b)
    tot = 0
    for d in range(1, g + 1):
        if g % d == 0:
            tot += mobius(d) * Tw[n // d].get((a // d, b // d), 0)
    assert tot % n == 0, (n, a, b, tot)
    return tot // n

SHIFTS = [((0, 0), 1), ((1, 0), -1), ((0, 1), -1), ((2, 1), 1), ((1, 2), 1), ((2, 2), -1)]

def terms(n, a, b, witt=True):
    return [lie(n, a - x, b - y, witt) for (x, y), _ in SHIFTS]

def lowest(n, a, b, witt=True):
    return sum(s * t for ((_, s), t) in zip(SHIFTS, terms(n, a, b, witt)))

def weight(n, a, b):
    return (2 * a - b - n, -a + 2 * b - n)

def dim_from_lowest(mu):
    l1, l2 = -mu[1], -mu[0]
    return (l1 + 1) * (l2 + 1) * (l1 + l2 + 2) // 2

def census(n):
    rows = []
    total = 0
    for (a, b) in sorted(Tw[n]):
        w = weight(n, a, b)
        if w[0] <= 0 and w[1] <= 0:
            m = lowest(n, a, b)
            assert m >= 0, (n, a, b, m)
            if m > 0:
                dv = dim_from_lowest(w)
                rows.append({'a': a, 'b': b, 'weight': list(w), 'highest': [-w[1], -w[0]],
                             'mult': m, 'irrdim': dv})
                total += m * dv
    witt_dim = sum(lie(n, a, b) for (a, b) in Tw[n])
    return rows, total, witt_dim

out = {'start_clock': START, 'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest()}
checks = []
def check(name, cond, detail=None):
    checks.append({'name': name, 'pass': bool(cond), 'detail': detail})

# Witt dimension formula sanity
for n in range(1, NMAX + 1):
    w = sum(lie(n, a, b) for (a, b) in Tw[n])
    ref = sum(mobius(d) * 8 ** (n // d) for d in range(1, n + 1) if n % d == 0) // n
    check(f'witt_total_level{n}', w == ref, [w, ref])

rows6, tot6, witt6 = census(6)
check('level6_sum_mult_times_dim_equals_witt_43596', tot6 == witt6 == 43596, [tot6, witt6])
oriented = [(r['a'], r['b']) for r in rows6]
reps = sorted({tuple(sorted(t)) for t in oriented})
check('level6_oriented_types_24', len(oriented) == 24, len(oriented))
check('level6_reps_up_to_transpose_15', len(reps) == 15, reps)
cand_reps = [(0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3), (2, 2), (3, 2), (2, 4), (3, 3), (4, 3), (4, 4), (4, 5), (5, 5), (6, 6)]
check('candidate_15_representatives_match_census', sorted(tuple(sorted(t)) for t in cand_reps) == reps,
      [sorted(tuple(sorted(t)) for t in cand_reps), reps])
check('transpose_symmetry_of_multiplicities', all(lowest(6, a, b) == lowest(6, b, a) for (a, b) in oriented))
mult6 = {(r['a'], r['b']): r['mult'] for r in rows6}

# Erratum and addendum numbers
err_raw = open('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody/frontier-20261029-invariant-target-multiplicity-erratum-v1.json', 'rb').read()
add_raw = open('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody/frontier-20261028-level6-inventory-scope-addendum-v1.json', 'rb').read()
out['erratum_sha256'] = hashlib.sha256(err_raw).hexdigest()
out['addendum_sha256'] = hashlib.sha256(add_raw).hexdigest()
err = json.loads(err_raw.decode('utf-8'))
add = json.loads(add_raw.decode('utf-8'))
def walk(o, acc, path=''):
    if isinstance(o, dict):
        for k, v in o.items():
            walk(v, acc, path + '/' + k)
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, acc, path + f'[{i}]')
    else:
        acc.append((path, o))
eleaves, aleaves = [], []
walk(err, eleaves); walk(add, aleaves)
out['erratum_leaf_count'] = len(eleaves)
out['addendum_leaf_count'] = len(aleaves)
ex = err['exact_recalculation']
check('erratum_letter_degrees_match', [tuple(x) for x in ex['adjoint_letter_degrees']] == LET)
check('erratum_level6_adjoint_terms', terms(6, 5, 5) == ex['level6_adjoint_terms'], terms(6, 5, 5))
check('erratum_level6_adjoint_signs', [s for _, s in SHIFTS] == ex['level6_adjoint_signs'])
check('erratum_level6_adjoint_mult_118', lowest(6, 5, 5) == ex['level6_adjoint_multiplicity'] == 118, lowest(6, 5, 5))
check('erratum_level6_highest22_terms', terms(6, 4, 4) == ex['level6_highest22_terms'], terms(6, 4, 4))
check('erratum_level6_highest22_mult_162', lowest(6, 4, 4) == ex['level6_highest22_multiplicity'] == 162, lowest(6, 4, 4))
check('erratum_level7_invariant_terms', terms(7, 7, 7) == ex['level7_invariant_terms'], terms(7, 7, 7))
check('erratum_level7_invariant_mult_100', lowest(7, 7, 7) == ex['level7_invariant_multiplicity'] == 100, lowest(7, 7, 7))
check('erratum_adjoint_is_(5,5,6)_highest(1,1)', weight(6, 5, 5) == (-1, -1))
check('erratum_(4,4,6)_is_highest(2,2)_dim27', weight(6, 4, 4) == (-2, -2) and dim_from_lowest((-2, -2)) == 27)
check('erratum_(7,7,7)_is_invariant', weight(7, 7, 7) == (0, 0))
check('addendum_(2,4,6)_mult_24', mult6.get((2, 4)) == 24 == mult6.get((4, 2)), mult6.get((2, 4)))
check('addendum_(4,5,6)_mult_90', mult6.get((4, 5)) == 90 == mult6.get((5, 4)), mult6.get((4, 5)))

# Five canonical types and verification-point arithmetic stated in the candidate
five = [(3, 3), (4, 3), (4, 4), (4, 5), (5, 5)]
ms = {t: mult6[t] for t in five}
tri = sum((m + 1) * (m + 2) // 2 for m in ms.values())
ray = sum(2 * (m + 1) for m in ms.values())
out['five_canonical_multiplicities'] = {str(k): v for k, v in ms.items()}
out['sum_triangular_grid_sizes'] = tri
out['sum_two_rays_m_plus_1'] = ray
check('candidate_36683_equals_sum_(m+1)(m+2)/2_over_five_types', tri == 36683, tri)
check('candidate_1182_equals_sum_2(m+1)_over_five_types', ray == 1182, ray)

# Negative controls (must FAIL for the intended reason)
neg = []
neg.append({'name': 'NEG_adjoint_multiplicity_is_162', 'holds': lowest(6, 5, 5) == 162,
            'intended_reason': '162 is the (4,4,6) V(2,2) multiplicity, not the adjoint (5,5,6)'})
bad = [lie(6, 6 - x, 6 - y, witt=False) for (x, y), _ in SHIFTS] + [lie(6, 4 - x, 4 - y, witt=False) for (x, y), _ in SHIFTS]
badtot = sum(lie(6, a, b, witt=False) for (a, b) in Tw[6])
neg.append({'name': 'NEG_no_mobius_witt_gives_integer_lie_dims_and_total_43596',
            'holds': all(float(v).is_integer() for v in bad) and badtot == 43596,
            'values': [str(v) for v in bad] + [str(badtot)],
            'intended_reason': 'dropping the Mobius divisor terms breaks integrality at gcd>1 degrees and the Witt total'})
neg.append({'name': 'NEG_selected_seven_is_complete_inventory', 'holds': len(oriented) == 7 or len(reps) == 7,
            'intended_reason': 'full census has 24 oriented / 15 representative types'})
out['level6_table'] = rows6
out['level6_sum'] = tot6
out['checks'] = checks
out['negative_controls'] = neg
out['all_positive_checks_pass'] = all(c['pass'] for c in checks)
out['all_negative_controls_fail'] = not any(n['holds'] for n in neg)
out['end_clock'] = clock()
print(json.dumps(out, indent=1, default=str))
