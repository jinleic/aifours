#!/usr/bin/env python3
"""Verify the proposed one-copy inequality without importing producer code.

The verifier checks actual conditional-mutual-information rows, the two types
of valid conditional-copy equalities, exact elimination of the copied variable,
the 36 written target coefficients and the point value. It does not establish
that the point is entropic or feasible in the complete source LP.
"""
from collections import Counter
from fractions import Fraction
from hashlib import sha256
from pathlib import Path
import copy
import json

ROOT = Path('/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/guessing-rminus')
CERT = ROOT / 'frontier-20261028-branch1-farkas-cut-result.json'
POINT = ROOT / 'frontier-20261028-source-closure-primal-frozen.json'
EXPECTED_CERT_SHA = 'ae9d207260ef0855f84c9ab3ab6f7d62128562db5ad051a0337bf9ccac6e6498'
EXPECTED_POINT_SHA = '97e38946440c30bd2d16e349c2c8e22d69ac133e1831e7f2d6ff913bfd2f2bec'

# Independent literal transcription from the candidate's displayed inequality.
TARGET = {579:-1, 706:-1, 728:-1, 729:-1, 730:2, 731:1, 733:1,
          737:-1, 739:3, 746:-1, 762:1, 763:-1, 764:-1, 835:1,
          962:-1, 965:-1, 966:1, 975:1, 976:-1, 978:1, 980:1,
          982:-1, 991:-1, 1000:-1, 1002:1, 1003:-1, 1004:1,
          1010:-1, 1011:1, 1013:-1, 1014:1, 1017:5, 1019:-4,
          1020:1, 1021:-1, 1022:-1}
B = 1 << 1
C = 1 << 2
COPY = 1 << 10
ORIGINAL = COPY - 1
Y = ORIGINAL ^ B ^ C


class InvalidCertificate(ValueError):
    pass


def require(condition, reason):
    if not condition:
        raise InvalidCertificate(reason)


def canonical(terms):
    result = Counter()
    for mask, coefficient in terms:
        require(isinstance(mask, int) and 0 <= mask < 2 * COPY,
                'entropy mask outside eleven variables')
        require(isinstance(coefficient, int), 'noninteger row coefficient')
        if mask:  # H(empty)=0
            result[mask] += coefficient
    return {mask: coefficient for mask, coefficient in result.items() if coefficient}


def negate(vector):
    return {mask: -value for mask, value in vector.items()}


def valid_copy_equalities():
    result = []
    for subset in range(COPY):
        if subset & ~Y:
            continue
        # Matching the conditional law of b and its copy given Y.
        result.append(canonical([(subset | B, 1), (subset | COPY, -1)]))
    # b' is conditionally independent of (b,c) given Y.
    result.append(canonical([(Y | COPY, 1), (ORIGINAL, 1),
                             (Y, -1), (ORIGINAL | COPY, -1)]))
    return result


def verify_rows(rows):
    require(isinstance(rows, list) and len(rows) == 48, 'expected 48 certificate rows')
    valid_equalities = valid_copy_equalities()
    total = Counter()
    kinds = Counter()
    for row in rows:
        weight = Fraction(row['weight'])
        actual = canonical(row['terms'])
        metadata = row['metadata']
        if row['equality']:
            require(metadata['kind'] == 'copy_equality', 'bad copy equality kind')
            require(any(actual == e or actual == negate(e) for e in valid_equalities),
                    'invalid conditional-copy equality')
            kinds['copy_equalities'] += 1
        else:
            require(weight >= 0, 'negative CMI weight')
            require(metadata['kind'] == 'CMI', 'non-CMI inequality')
            i, j, z = metadata['i'], metadata['j'], metadata['z']
            require(isinstance(i, int) and isinstance(j, int) and 0 <= i < 11 and 0 <= j < 11 and i != j,
                    'bad CMI variables')
            require(isinstance(z, int) and 0 <= z < 2 * COPY and not z & ((1 << i) | (1 << j)),
                    'bad CMI conditioning set')
            expected = canonical([(z | (1 << i), 1), (z | (1 << j), 1),
                                  (z, -1), (z | (1 << i) | (1 << j), -1)])
            require(actual == expected, 'invalid CMI terms')
            kinds['CMIs'] += 1
        for mask, coefficient in actual.items():
            total[mask] += weight * coefficient
    require(kinds == {'CMIs': 33, 'copy_equalities': 15}, 'unexpected row types')
    result = {mask: value for mask, value in total.items() if value}
    require(all(mask < COPY for mask in result), 'copied-variable entropy did not cancel')
    require(result == {mask: Fraction(value * 276) for mask, value in TARGET.items()},
            'weighted sum does not equal the written target')
    return kinds


def base_values(point):
    values = {}
    for item in point['primal_values']:
        names = item['entropy_variables']
        if not all(isinstance(s, str) and len(s) == 1 and 'a' <= s <= 'j' for s in names):
            continue
        require(len(set(names)) == len(names), 'duplicate variable in entropy coordinate')
        mask = sum(1 << (ord(s) - ord('a')) for s in names)
        require(mask and mask not in values, 'duplicate or empty original entropy coordinate')
        values[mask] = Fraction(item['value'])
    require(set(values) == set(range(1, COPY)), 'incomplete ten-variable entropy coordinates')
    return values


def rejected(rows, expected):
    try:
        verify_rows(rows)
    except InvalidCertificate as exc:
        require(str(exc) == expected, f'control rejected for wrong reason: {exc}')
        return str(exc)
    raise InvalidCertificate(f'mutation was not rejected: {expected}')


def main():
    cb, pb = CERT.read_bytes(), POINT.read_bytes()
    require(sha256(cb).hexdigest() == EXPECTED_CERT_SHA, 'certificate hash mismatch')
    require(sha256(pb).hexdigest() == EXPECTED_POINT_SHA, 'point hash mismatch')
    cert, point = json.loads(cb), json.loads(pb)
    rows = cert['exact_separator']['selected_rows']
    counts = verify_rows(rows)
    values = base_values(point)
    score = sum((Fraction(coefficient) * values[mask] for mask, coefficient in TARGET.items()), Fraction(0))
    require(score == Fraction(-1, 276), 'point value is not -1/276')

    cmi_index = next(i for i, row in enumerate(rows) if not row['equality'])
    copy_index = next(i for i, row in enumerate(rows) if row['equality'] and len(row['terms']) == 2)
    negative = copy.deepcopy(rows)
    negative[cmi_index]['weight'] = '-1'
    altered_cmi = copy.deepcopy(rows)
    altered_cmi[cmi_index]['terms'][0][1] *= -1
    altered_copy = copy.deepcopy(rows)
    altered_copy[copy_index]['terms'][0][0] ^= C
    controls = {
        'negative_CMI_weight': rejected(negative, 'negative CMI weight'),
        'altered_CMI_term': rejected(altered_cmi, 'invalid CMI terms'),
        'altered_copy_identity': rejected(altered_copy, 'invalid conditional-copy equality'),
    }
    print(json.dumps({'result':'PASS', 'certificate_sha256':EXPECTED_CERT_SHA,
                      'point_sha256':EXPECTED_POINT_SHA, 'row_counts':dict(counts),
                      'written_target_terms':len(TARGET),
                      'auxiliary_entropy_coefficients':'all zero',
                      'target_scale':276, 'original_entropy_coordinates':len(values),
                      'exact_L_at_point':str(score), 'negative_controls':controls,
                      'limit':'Universal inequality from exact CMI/copy certificate; point is not claimed entropic or full-source-LP feasible; no improved guessing-number bound.'}, indent=2))


if __name__ == '__main__':
    main()
