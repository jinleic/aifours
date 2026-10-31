#!/usr/bin/env python3
"""proof-extra-controls-v2.py -- f122 reviewer-authored supplementary controls.

(v2: v1 asserted that the FIRST reported failure of the nonempty-z control be a
submodularity failure; the checker reports monotonicity first and the mutation
also breaks the tight monotone step BCR->BCRH, so v1 stopped. v2 reports all
failing families and asserts the targeted tight elemental CMI is violated.)

Supplements proof-identity-and-witness-check-v1.py:
 (1) The tight elemental inequalities of the witness are enumerated by name; a
     tight CMI with NONEMPTY conditioning set is selected and the union value
     r(z|a|b) is raised by 1: the full polymatroid check must then fail for a
     submodularity reason (control W4 in the main checker was degenerate, z=empty,
     and tripped the r(empty)=0 guard instead).
 (2) Per-variable balance of the 16-term functional (sum of coefficients over
     all terms containing each variable) -- an observation, not a claim.
 (3) Phi(r) recomputed from the normalised Fraction vector r/scale.
 (4) Elemental inequalities evaluated on the witness: minimum slack and count
     of strictly positive slacks; and the single most-violated elemental
     inequality of a deliberately corrupted vector (mutated r(BCRHPQ) -> r(BCRHP)
     - 1) to show detection is specific.
No author code imported or executed. Receipt JSON to stdout.
"""
import json
import sys
from fractions import Fraction
from itertools import combinations

NAMES = 'BCRHPQ'
SCALE = 6900000
TABLE = [
    0, 3875000, 6900000, 6900000, 3025000, 6900000, 8300000, 8300000,
    2975000, 5650000, 8300000, 8300000, 5675000, 8300000, 8300000, 8300000,
    6598260, 10309011, 11178976, 11178976, 8461329, 11329176, 12075000, 12075000,
    9420084, 12075000, 12075000, 12075000, 10057128, 12075000, 12075000, 12075000,
    3280188, 6928908, 9708504, 9708504, 5950419, 9585546, 10950000, 10950000,
    5682009, 8326158, 10950000, 10950000, 8331852, 10950000, 10950000, 10950000,
    7996200, 10825200, 11466900, 11466900, 9479700, 11577300, 12205200, 12205200,
    9969600, 12205200, 12205200, 12205200, 10549200, 12205200, 12205200, 12205200,
]
TERMS = [('BC', -1), ('BR', -1), ('BCRH', 2),
         ('BCP', 1), ('BRP', 1), ('BCRP', -1), ('BHP', -1), ('BCHP', 1), ('BCRHP', -1),
         ('BQ', -1), ('BCQ', 1), ('BRQ', 1), ('BHQ', 1), ('CHQ', -1), ('CRHQ', 1), ('BCRHQ', -2)]


def mask(s):
    return sum(1 << NAMES.index(ch) for ch in s)


def name(m):
    return ''.join(NAMES[i] for i in range(6) if m >> i & 1) or 'empty'


def full_polymatroid(r):
    """Return (ok, reasons) with ALL failing families listed (first instance each)."""
    reasons = []
    if r[0] != 0:
        reasons.append('r(empty)!=0')
    for S in range(64):
        for i in range(6):
            if r[S | 1 << i] < r[S]:
                reasons.append(f'monotonicity {name(S)} + {NAMES[i]}')
                break
        else:
            continue
        break
    for S in range(64):
        for T in range(64):
            if r[S] + r[T] < r[S | T] + r[S & T]:
                reasons.append(f'submodularity {name(S)},{name(T)}')
                break
        else:
            continue
        break
    return not reasons, '; '.join(reasons)


def elementals(r):
    rows = []
    for i in range(6):
        rows.append((f'H({NAMES[i]}|{name(63 ^ 1 << i)})', r[63] - r[63 ^ 1 << i]))
    for i, j in combinations(range(6), 2):
        a, b = 1 << i, 1 << j
        rest = [k for k in range(6) if k not in (i, j)]
        for bits in range(16):
            z = sum(1 << rest[t] for t in range(4) if bits >> t & 1)
            rows.append((f'I({NAMES[i]};{NAMES[j]}|{name(z)})', r[z | a] + r[z | b] - r[z | a | b] - r[z], (a, b, z)))
    return rows


def main():
    out = {'script': 'proof-extra-controls-v2.py'}
    r = TABLE
    ok, why = full_polymatroid(r)
    assert ok, why
    el = elementals(r)
    tight = [e[0] for e in el if e[1] == 0]
    out['elemental_total'] = len(el)
    out['elemental_tight_count'] = len(tight)
    out['elemental_tight_names'] = tight
    out['elemental_min_positive_slack_scaled'] = min(e[1] for e in el if e[1] > 0)
    # (1) nonempty-z tight pair control
    pick = next(e for e in el if len(e) == 3 and e[1] == 0 and e[2][2] != 0)
    a, b, z = pick[2]
    w = list(r)
    w[z | a | b] += 1
    ok1, why1 = full_polymatroid(w)
    viol = [(e[0], e[1]) for e in elementals(w) if e[1] < 0]
    out['control_tight_nonempty_z'] = {'chosen': pick[0], 'mutation': f'r({name(z | a | b)}) += 1',
                                       'expected': 'REJECT_with_targeted_CMI_violated', 'polymatroid': ok1,
                                       'failing_families': why1, 'violated_elementals': viol}
    assert not ok1 and 'submodularity' in why1 and (pick[0], -1) in viol
    # (2) per-variable balance
    bal = {v: sum(c for s, c in TERMS if v in s) for v in NAMES}
    out['per_variable_coefficient_sums'] = bal
    out['balanced_in_every_variable'] = all(x == 0 for x in bal.values())
    # (3) normalised Fraction evaluation
    rn = [Fraction(x, SCALE) for x in r]
    val = sum(c * rn[mask(s)] for s, c in TERMS)
    out['phi_normalised_fraction'] = f'{val.numerator}/{val.denominator}'
    assert val == Fraction(-12637, 1725000)
    # (4) specific detection on a corrupted vector
    w = list(r)
    w[63] = r[31] - 1
    ok4, why4 = full_polymatroid(w)
    worst = min(((e[0], e[1]) for e in elementals(w)), key=lambda t: t[1])
    out['control_corrupt_r63'] = {'mutation': 'r(BCRHPQ) := r(BCRHP) - 1', 'polymatroid': ok4, 'reason': why4,
                                  'most_violated_elemental': worst}
    assert not ok4
    out['verdict_of_this_script'] = 'ALL_CHECKS_PASSED'
    print(json.dumps(out, indent=1))


if __name__ == '__main__':
    main()
