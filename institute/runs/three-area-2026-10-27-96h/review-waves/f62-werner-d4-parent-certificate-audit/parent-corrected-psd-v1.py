#!/usr/bin/env python3
"""Independent standard-library strict-PD check of the saved d=4 multipliers.

This checks only the corrected matrix data, not orbit identities, source-map
semantics, the physical bridge, or the full Werner theorem.
"""
import collections
import hashlib
import json
import lzma
import sys
from fractions import Fraction
from pathlib import Path

DATA = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/werner3-ququart/frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz')
EXPECTED = 'c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94'
SOURCE = '0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f'
OUTPUT = Path(__file__).with_name('parent-corrected-psd-result-v1.json')


def positive_definite(values, n):
    if type(n) is not int or n < 1 or len(values) != n * n:
        raise ValueError('SHAPE')
    rows = []
    for i in range(n):
        row = []
        for j in range(n):
            num, den = values[i * n + j]
            num, den = int(num), int(den)
            if den <= 0:
                raise ValueError('DENOMINATOR')
            row.append(Fraction(num, den))
        rows.append(row)
    if any(rows[i][j] != rows[j][i] for i in range(n) for j in range(i)):
        raise ValueError('SYMMETRY')
    # Symmetric Gaussian elimination without pivoting. All strictly positive
    # pivots are equivalent to positive definiteness by Schur complements.
    for k in range(n):
        pivot = rows[k][k]
        if pivot <= 0:
            raise ValueError('NONPOSITIVE_PIVOT')
        for i in range(k + 1, n):
            coefficient = rows[k][i] / pivot
            for j in range(i, n):
                rows[i][j] -= coefficient * rows[k][j]
    return n


def rejected(values, n, reason):
    try:
        positive_definite(values, n)
    except ValueError as exc:
        return str(exc) == reason
    return False


def main():
    sys.set_int_max_str_digits(0)
    if OUTPUT.exists():
        raise FileExistsError(OUTPUT)
    raw = DATA.read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED:
        raise ValueError('INPUT_HASH')
    obj = json.loads(lzma.decompress(raw, memlimit=256 * 1024 * 1024))
    if (obj['dimension'], obj['copies'], obj['source_member_sha256']) != (4, 3, SOURCE):
        raise ValueError('SOURCE_TARGET')
    mats, eqs = obj['matrices'], obj['equality_coefficients']
    if len(mats) != 1237 or len(eqs) != 329:
        raise ValueError('COUNT')
    controls = {
        'negative_pivot': rejected([(1, 1), (2, 1), (2, 1), (1, 1)], 2, 'NONPOSITIVE_PIVOT'),
        'singular_pivot': rejected([(1, 1), (1, 1), (1, 1), (1, 1)], 2, 'NONPOSITIVE_PIVOT'),
        'nonsymmetric': rejected([(1, 1), (0, 1), (1, 1), (1, 1)], 2, 'SYMMETRY'),
        'bad_denominator': rejected([(1, 0)], 1, 'DENOMINATOR'),
    }
    if not all(controls.values()):
        raise ValueError('CONTROL')
    pivots = sum(positive_definite(m['values'], m['r']) for m in mats)
    if pivots != 4149:
        raise ValueError('PIVOT_COUNT')
    result = {
        'verdict': 'PASS',
        'corrected_data_sha256': digest,
        'source_member_sha256': SOURCE,
        'dimension': 4,
        'copies': 3,
        'matrices_checked': len(mats),
        'all_strictly_positive': True,
        'strict_positive_pivots': pivots,
        'matrix_size_histogram': dict(sorted(collections.Counter(m['r'] for m in mats).items())),
        'equality_entries_counted_not_verified_here': len(eqs),
        'negative_controls': controls,
        'method': 'Standard-library Fraction upper-triangular Schur elimination and exact symmetry; no author or reviewer checker imported.',
        'scope': 'Positive definiteness of these saved corrected real rational matrices only. Certificate identity and physical map are separate obligations.'
    }
    text = json.dumps(result, indent=2, sort_keys=True) + '\n'
    with OUTPUT.open('x', encoding='utf-8') as f:
        f.write(text)
    print(text, end='')


if __name__ == '__main__':
    main()
