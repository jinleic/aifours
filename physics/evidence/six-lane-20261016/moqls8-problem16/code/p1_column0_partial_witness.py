"""Exact Q(sqrt2) control for the LOCAL sharpness example in P1 monomial r1.
This is five assignments on row0 UNION column0 (15cells), NOT five full QLS,
NOT a full F_one SAT model and NOT a physical counterexample to Problem16.
No native solver or process-group supervisor is invoked. Two corrupted copies
are retained and must fail for separate unitary/support reasons.
"""
from __future__ import annotations

import copy
import hashlib
import itertools
import json
import resource
import shutil
import subprocess
from datetime import datetime
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'evidence/p1_column0_partial_witness_v1'
PROOF = ROOT / 'review/P1_COLUMN0_MONOMIAL_REDUCTION.r1.md'
PROOF_SHA = '34e90d7358d9a9af018732fa843518b9f84e35e90b4a355e863c48841dc4284a'
Z = (F(0), F(0))
ONE = (F(1), F(0))
H = (F(0), F(1, 2))
HALF = (F(1, 2), F(0))


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def add(x, y):
    return x[0] + y[0], x[1] + y[1]


def mul(x, y):
    return x[0] * y[0] + 2 * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def neg(x):
    return -x[0], -x[1]


def dot(x, y):
    value = Z
    for a, b in zip(x, y):
        value = add(value, mul(a, b))
    return value


def basis(c):
    return [ONE if i == c else Z for i in range(8)]


def build():
    matrices = {s: [[Z for _ in range(8)] for _ in range(8)] for s in range(1, 6)}
    pure = {1: {0: 0, 2: 7, 3: 6, 4: 5, 5: 4},
            2: {0: 0, 1: 4, 2: 1, 3: 3, 4: 2, 7: 7},
            3: {0: 0, 1: 5, 2: 3, 5: 2, 6: 4, 7: 6},
            4: {0: 0, 1: 6, 2: 2, 3: 5, 4: 3, 5: 1, 6: 7, 7: 4},
            5: {0: 0, 1: 7, 3: 2, 5: 3, 6: 1, 7: 5}}
    for s, rows in pure.items():
        for r, c in rows.items():
            matrices[s][r] = basis(c)
    matrices[1][1][1:4] = [H, HALF, HALF]
    matrices[1][6][2:4] = [H, neg(H)]
    matrices[1][7][1:4] = [H, neg(HALF), neg(HALF)]
    for s, rows, cols in ((2, (5, 6), (5, 6)), (3, (3, 4), (1, 7)), (5, (2, 4), (4, 6))):
        r, t = rows
        c, d = cols
        matrices[s][r][c] = matrices[s][r][d] = H
        matrices[s][t][c], matrices[s][t][d] = H, neg(H)
    return matrices


def unitary(matrices):
    checks = 0
    for s, a in matrices.items():
        for kind, vectors in (('row', a), ('column', list(map(list, zip(*a))))):
            for r in range(8):
                for t in range(8):
                    checks += 1
                    if dot(vectors[r], vectors[t]) != (ONE if r == t else Z):
                        raise ValueError('unitary:%s:%s:%s,%s' % (s, kind, r, t))
    return checks


def check(matrices):
    uc = unitary(matrices)
    for r in range(1, 8):
        for c in range(1, 8):
            active = [s for s in range(1, 6) if matrices[s][r][c] != Z]
            if len(active) > 1:
                raise ValueError('support_overlap:%s,%s:%r' % (r, c, active))
    cells = [(0, c) for c in range(8)] + [(r, 0) for r in range(1, 8)]

    def vector(s, cell):
        r, c = cell
        return basis(c) if r == 0 else matrices[s][r]

    norms = pairs = 0
    for s in range(1, 6):
        for cell in cells:
            v = vector(s, cell)
            assert dot(v, v) == ONE
            norms += 1
    for s, t in itertools.combinations(range(1, 6), 2):
        for p, q in itertools.combinations(cells, 2):
            if mul(dot(vector(s, p), vector(s, q)), dot(vector(t, p), vector(t, q))) != Z:
                raise ValueError('partial_tensor_orthogonality:%s,%s:%r,%r' % (s, t, p, q))
            pairs += 1
    supports = {s: [[c for c in range(1, 8) if matrices[s][r][c] != Z] for r in range(1, 8)]
                for s in range(1, 6)}
    monomial = [s for s in range(2, 6) if all(len(row) == 1 for row in supports[s])]
    return {'row_and_column_inner_products': uc, 'specified_cell_norms': norms,
            'partial_tensor_pair_inner_products': pairs, 'supports': supports, 'other_monomial_columns': monomial}


def encode(matrices):
    return {s: [[[str(a), str(b)] for a, b in row] for row in m] for s, m in matrices.items()}


def new_json(path, obj):
    raw = json.dumps(obj, indent=1).encode()
    with path.open('xb') as f:
        f.write(raw)
    return sha(raw)


def main():
    free = shutil.disk_usage(ROOT).free
    used = int(subprocess.run(['du', '-sk', str(ROOT)], capture_output=True, text=True, check=True).stdout.split()[0]) * 1024
    if free - 200000 < 12200000000 or used + 200000 > 10200547328:
        raise SystemExit('DEFERRED exact local checker: fresh disk/lane gate')
    assert sha(PROOF.read_bytes()) == PROOF_SHA
    assert mul(H, H) == HALF
    matrices = build()
    good = check(matrices)
    assert good['other_monomial_columns'] == [4]
    assert sum(len(x) for x in good['supports'][1]) == 12
    assert good['row_and_column_inner_products'] == 640
    assert good['specified_cell_norms'] == 75 and good['partial_tensor_pair_inner_products'] == 1050
    OUT.mkdir()
    witness_sha = new_json(OUT / 'WITNESS.json', {'field': 'a+b*sqrt2; coefficients are rational strings',
                                                'matrices': encode(matrices), 'scope': '15specifiedcells only;49unspecified',
                                                'construction': 'manual P1-B1 local sharpness seed'})
    controls = []
    bad = copy.deepcopy(matrices)
    bad[3][4] = list(bad[3][3])
    new_json(OUT / 'MUTATION_duplicate_Q3_row4.json', {'matrices': encode(bad), 'fixture': 'duplicateQ3row3into4'})
    reason = None
    try:
        check(bad)
    except ValueError as ex:
        reason = str(ex)
    assert reason == 'unitary:3:row:3,4'
    controls.append({'mutation': 'duplicateQ3row3into4', 'rejected': True, 'reason': reason})
    bad = copy.deepcopy(matrices)
    bad[4][2], bad[4][3] = bad[4][3], bad[4][2]
    assert unitary(bad) == 640
    new_json(OUT / 'MUTATION_swap_Q4_rows2_3.json', {'matrices': encode(bad), 'fixture': 'swapQ4rows2and3;unitaritypreserved'})
    reason = None
    try:
        check(bad)
    except ValueError as ex:
        reason = str(ex)
    assert reason == 'support_overlap:3,2:[4, 5]'
    controls.append({'mutation': 'swapQ4rows2and3', 'rejected': True, 'unitarity_preserved': True, 'reason': reason})
    result = {'host': datetime.now().astimezone().isoformat(), 'status': 'VERIFIED_FINITE_EXACT_LOCAL_PARTIAL_CONFIGURATION',
              'code_sha256': sha(Path(__file__).read_bytes()), 'proof_note_sha256': PROOF_SHA,
              'witness_sha256': witness_sha, 'arithmetic': 'exact rational pairs for Q(sqrt2); no numerical tolerance',
              'positive_checks': good, 'mutation_controls': controls,
              'Q2_Aprofile_row2_little_endian': [1, 0, 0], 'Q2_Aprofile_row3_little_endian': [0, 0, 1],
              'fits_frozen_signed_cube': 'P1-B1.L1.001.L2.004',
              'full_F_one_CNF_model_checked': False, 'remaining49cells': 'UNSPECIFIED',
              'original_Problem16_counterexample': False, 'universal_lemma_independently_reviewed': False,
              'new_CNF_or_native_solver_run': False, 'novelty_or_priority_claim': False,
              'fresh_free_bytes': free, 'fresh_lane_bytes': used,
              'max_RSS_bytes_Darwin': resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    rh = new_json(OUT / 'RESULT.json', result)
    print(json.dumps({'RESULT_sha256': rh, 'witness_sha256': witness_sha, 'positive_checks':
                      {k: good[k] for k in ('row_and_column_inner_products', 'specified_cell_norms',
                                           'partial_tensor_pair_inner_products', 'other_monomial_columns')},
                      'mutation_controls': controls, 'native_run': False}), flush=True)


if __name__ == '__main__':
    main()
