#!/usr/bin/env python3
"""Parent third exact verifier of the pinned three-member MOQLS(8) witness.

Integer-only arithmetic: every cell is an integer vector v with squared norm
sigma = sum v_k^2 equal to its denominator_squared; squared overlaps are
<v,w>^2/(sigma_v sigma_w). Classical members are label matrices. No author
or reviewer code is imported.
"""
import hashlib
import itertools
import json
import subprocess
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
WITNESS = HERE / 'parent-inputs-v1' / 'witness.json'
PIN = 'a638a5db88a5d76c01625c4857ff50888c06f26cd5a012571a423add53fec413'
OUT = HERE / 'parent-witness-exact-result-v1.json'
N = 8


class Reject(Exception):
    pass


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'],
                          check=True, text=True, capture_output=True).stdout.strip()


def parse(doc):
    nums = doc['quantum_square_numerators']
    dens = doc['quantum_square_denominator_squared']
    if len(nums) != N*N or len(dens) != N*N:
        raise Reject('SHAPE')
    cells = []
    for v, d in zip(nums, dens):
        if len(v) != N or any(type(x) is not int for x in v) or type(d) is not int or d <= 0:
            raise Reject('ENTRY_TYPE')
        if sum(x*x for x in v) != d:
            raise Reject('NORMALIZER_MISMATCH')
        cells.append(tuple(v))
    quantum = [cells[r*N:(r+1)*N] for r in range(N)]
    mates = doc['classical_mates']
    if len(mates) != 2:
        raise Reject('MATE_COUNT')
    classical = []
    for m in mates:
        if len(m) != N or any(len(row) != N or any(type(x) is not int or not 0 <= x < N for x in row) for row in m):
            raise Reject('LABEL_RANGE')
        classical.append([[tuple(1 if k == x else 0 for k in range(N)) for x in row] for row in m])
    return quantum, classical


def dot(v, w):
    return sum(a*b for a, b in zip(v, w))


def norm2(v):
    return dot(v, v)


def is_onb(vectors):
    for i, j in itertools.combinations(range(N), 2):
        if dot(vectors[i], vectors[j]) != 0:
            return False
    return all(norm2(v) > 0 for v in vectors)


def member_checks(square):
    for r in range(N):
        if not is_onb(square[r]):
            raise Reject('ROW_NOT_ONB')
    for c in range(N):
        if not is_onb([square[r][c] for r in range(N)]):
            raise Reject('COLUMN_NOT_ONB')


def pair_orthogonal(a, b):
    # Same-cell product vectors; Gram of tensor products factorizes.
    cells = [(a[r][c], b[r][c]) for r in range(N) for c in range(N)]
    for (v1, w1), (v2, w2) in itertools.combinations(cells, 2):
        if dot(v1, v2) != 0 and dot(w1, w2) != 0:
            return False
    return True


def squared_overlap(v, w):
    return Fraction(dot(v, w)**2, norm2(v)*norm2(w))


def verify(doc):
    quantum, classical = parse(doc)
    members = [quantum] + classical
    for m in members:
        member_checks(m)
    for a, b in itertools.combinations(range(3), 2):
        if not pair_orthogonal(members[a], members[b]):
            raise Reject('PAIR_NOT_ORTHOGONAL:%d,%d' % (a, b))
    mixed = [r*N+c for r in range(N) for c in range(N)
             if sum(1 for x in quantum[r][c] if x) > 1]
    strict = [(i, j) for i, j in itertools.combinations(range(N*N), 2)
              if 0 < squared_overlap(quantum[i//N][i % N], quantum[j//N][j % N]) < 1]
    if not strict:
        raise Reject('NO_NONCLASSICAL_OVERLAP')
    return {'mixed_cells': mixed, 'first_strict_overlap_pair': strict[0],
            'strict_overlap_pair_count': len(strict),
            'sample_strict_overlap': str(squared_overlap(quantum[strict[0][0]//N][strict[0][0] % N],
                                                         quantum[strict[0][1]//N][strict[0][1] % N]))}


def mutate(doc, kind):
    d = json.loads(json.dumps(doc))
    if kind == 'swap_classical_labels':
        d['classical_mates'][0][1][0], d['classical_mates'][0][1][1] = d['classical_mates'][0][1][1], d['classical_mates'][0][1][0]
    elif kind == 'duplicate_label':
        d['classical_mates'][1][2][0] = d['classical_mates'][1][2][1]
    elif kind == 'sign_flip':
        v = d['quantum_square_numerators'][18]
        v[1] = -v[1]
    elif kind == 'bad_normalizer':
        d['quantum_square_denominator_squared'][18] = 3
    elif kind == 'truncate':
        d['quantum_square_numerators'][5] = d['quantum_square_numerators'][5][:7]
    elif kind == 'classicalize':
        d['quantum_square_numerators'][18] = [1, 0, 0, 0, 0, 0, 0, 0]
        d['quantum_square_denominator_squared'][18] = 1
    elif kind == 'transpose_quantum':
        nums = d['quantum_square_numerators']
        d['quantum_square_numerators'] = [nums[c*N+r] for r in range(N) for c in range(N)]
        dens = d['quantum_square_denominator_squared']
        d['quantum_square_denominator_squared'] = [dens[c*N+r] for r in range(N) for c in range(N)]
    return d


def main():
    if OUT.exists():
        raise FileExistsError(OUT)
    started = clock()
    raw = WITNESS.read_bytes()
    if hashlib.sha256(raw).hexdigest() != PIN:
        raise ValueError('WITNESS_HASH_MISMATCH')
    doc = json.loads(raw)
    result = verify(doc)
    controls = {}
    for kind in ('swap_classical_labels', 'duplicate_label', 'sign_flip', 'bad_normalizer',
                 'truncate', 'classicalize', 'transpose_quantum'):
        try:
            verify(mutate(doc, kind))
        except Reject as exc:
            controls[kind] = 'rejected:' + str(exc)
        else:
            if kind == 'classicalize':
                controls[kind] = 'accepted_as_expected_only_if_still_valid'
                raise AssertionError('CLASSICALIZE_UNEXPECTEDLY_VALID')
            raise AssertionError('CONTROL_NOT_REJECTED:' + kind)
    receipt = {'kind': 'PARENT_THIRD_EXACT_WITNESS_VERIFICATION',
               'started_native_clock': started, 'finished_native_clock': clock(),
               'witness_sha256': PIN, 'result': 'VALID_THREE_MEMBER_FAMILY', **result,
               'controls': controls,
               'limits': 'Physical validity of the pinned three-member family only. '
                         'No M(8), source-definition correspondence, priority, '
                         'novelty or four-family claim.'}
    with OUT.open('x', encoding='utf-8') as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write('\n')
    print(json.dumps(receipt, sort_keys=True))


if __name__ == '__main__':
    main()
