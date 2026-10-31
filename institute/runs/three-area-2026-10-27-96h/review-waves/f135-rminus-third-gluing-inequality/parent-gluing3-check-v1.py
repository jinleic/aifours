#!/usr/bin/env python3
"""Exact, nonblind parent check of the L3 identity and a nine-variable witness.

The 18 entropy terms and 12 CMI rows are transcribed from the candidate. No
producer or reviewer code is imported. The data point is not an entropic law.
"""
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import subprocess
import sys


SOURCE = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus/frontier-20261028-nine-variable-gluing-separation-check-result.json')
SOURCE_SHA = '486fe82f61fe70bef56027897f08422f8812115265bd5443c75cb524b6aea60c'
ORDER = 'bdefgijDF'
TERMS = [
    (-1, 'abcehi'), (-1, 'acefghi'), (2, 'abcdefghij'),
    (1, 'abcefhiD'), (1, 'acefghiD'), (-1, 'acefhijD'),
    (1, 'abcefhijD'), (-2, 'abcdefghijD'), (1, 'abcehiF'),
    (-1, 'acefhiF'), (1, 'acefghiF'), (-1, 'abcefghiF'),
    (-1, 'abcdfhjF'), (1, 'abcdfghjF'), (1, 'acefhijF'),
    (-1, 'abcefhijF'), (1, 'abcdefhijF'), (-1, 'abcdefghijF'),
]
ROWS = [
    ('b', 'g', 'acefhiDF'), ('b', 'F', 'acefhijD'),
    ('d', 'D', 'abcefhijF'), ('d', 'D', 'abcefghiF'),
    ('e', 'g', 'abcdfhjDF'), ('f', 'F', 'abcehiD'),
    ('g', 'i', 'abcdefhjDF'), ('g', 'D', 'abcdfhjF'),
    ('j', 'D', 'abcdefghiF'), ('j', 'D', 'acefhiF'),
    ('D', 'F', 'acefghi'), ('D', 'F', 'abcehi'),
]


def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def add_entropy(out, weight, variables):
    require(len(set(variables)) == len(variables), 'DUPLICATE_VARIABLE')
    out[frozenset(variables)] += weight


def cmi(out, weight, a, b, given):
    require(a != b and a not in given and b not in given, 'BAD_CMI')
    for sign, part in ((1, given + a), (1, given + b), (-1, given + a + b), (-1, given)):
        add_entropy(out, weight * sign, part)


def normalize(counter):
    return {key: value for key, value in counter.items() if value}


def entropy_identity(terms, rows):
    literal, expanded = Counter(), Counter()
    for coefficient, variables in terms:
        add_entropy(literal, coefficient, variables)
    for a, b, given in rows:
        cmi(expanded, 1, a, b, given)
    cmi(expanded, -2, 'D', 'F', 'abcdefghij')
    return normalize(literal) == normalize(expanded)


def mask(variables):
    return sum(1 << ORDER.index(x) for x in set(variables) if x in ORDER)


def contracted_terms():
    result = Counter()
    for coefficient, variables in TERMS:
        result[mask(variables)] += coefficient
    return {k: v for k, v in result.items() if v}


def elemental_violations(values):
    require(len(values) == 512 and values[0] == 0, 'WITNESS_SHAPE_OR_EMPTY')
    full = 511
    violations = []
    checked = 0
    for i in range(9):
        checked += 1
        if values[full] - values[full ^ (1 << i)] < 0:
            violations.append(('MONOTONICITY', i))
    for i, j in itertools.combinations(range(9), 2):
        remaining = [k for k in range(9) if k not in (i, j)]
        for subset in range(1 << 7):
            base = sum(1 << k for bit, k in enumerate(remaining) if subset & (1 << bit))
            slack = values[base | (1 << i)] + values[base | (1 << j)] - values[base] - values[base | (1 << i) | (1 << j)]
            checked += 1
            if slack < 0:
                violations.append(('CMI', i, j, base))
    require(checked == 4617, 'ELEMENTAL_COVERAGE')
    return violations


def main():
    require(len(sys.argv) == 2, 'EXPECTED_NEW_OUTPUT_PATH')
    started = clock()
    data = SOURCE.read_bytes()
    require(hashlib.sha256(data).hexdigest() == SOURCE_SHA, 'WITNESS_HASH')
    doc = json.loads(data)
    require(doc['nine_variable_order'] == ['B=b', 'R=d', 'E=e', 'T=f', 'G=g', 'I=i', 'J=j', "P=g'2", "Q=f'3"], 'VARIABLE_ORDER')
    values = [Fraction(s) for s in doc['nine_variable_primal_values']]
    require(entropy_identity(TERMS, ROWS), 'IDENTITY')
    altered_terms = [(-TERMS[0][0], TERMS[0][1])] + TERMS[1:]
    require(not entropy_identity(altered_terms, ROWS), 'IDENTITY_MUTATION_UNDETECTED')
    require(not entropy_identity(TERMS, ROWS[:-1]), 'REMOVED_CMI_UNDETECTED')
    for _, variables in TERMS:
        require(not ('D' in variables and 'F' in variables), 'MIXED_TERM')
    require(sum(c for c, _ in TERMS) == 0, 'COEFFICIENT_SUM')
    contracted = contracted_terms()
    require(len(contracted) == 18, 'CONTRACTION_TERM_COUNT')
    require(not elemental_violations(values), 'ELEMENTAL_VIOLATION')
    value = sum(Fraction(coefficient) * values[k] for k, coefficient in contracted.items())
    require(value == Fraction(-7123, 3450000), 'WITNESS_VALUE')
    modular = [Fraction(m.bit_count()) for m in range(512)]
    require(not elemental_violations(modular), 'MODULAR_POSITIVE_CONTROL')
    require(sum(Fraction(c) * modular[k] for k, c in contracted.items()) == 0, 'MODULAR_L3')
    broken = values.copy()
    broken[-1] -= 100
    require(any(x[0] == 'MONOTONICITY' for x in elemental_violations(broken)), 'MUTATION_NOT_REJECTED')
    result = {
        'kind': 'PARENT_EXACT_L3_IDENTITY_AND_SHANNON_WITNESS_CONTROL',
        'started_native_clock': started,
        'observed_native_clock_after_checks': clock(),
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'input_sha256': SOURCE_SHA,
        'identity_18_terms_12_cmi_minus_2_conditional_independence': True,
        'no_DF_mixed_entropy_terms': True,
        'contracted_variable_order': list(ORDER),
        'contracted_coefficients': sorted(contracted.items()),
        'elemental_inequalities_checked': 4617,
        'witness_violations': 0,
        'witness_L3': str(value),
        'modular_positive_control': 'PASS',
        'negative_controls': ['altered_entropy_term_rejected', 'removed_CMI_rejected', 'lowered_full_entropy_breaks_monotonicity'],
        'limits': 'Exact checks on the stated identity and nine-variable Shannon-cone point; gluing validity is a written argument. No entropic witness, original R-minus bound, novelty, human, independent-family or formal proof.',
    }
    with Path(sys.argv[1]).open('x', encoding='utf-8') as f:
        json.dump(result, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
