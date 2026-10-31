#!/usr/bin/env python3
"""Exact, fixed-object completion filter; no diagonal-ansatz classification.

Read the phase literals printed in the pinned f163 MINOR-fix addendum. For
its Q00/Q01/Q10 core, enumerate every orthogonal perfect matching in the
three K_5,5 edge classes. Then certify that each missing row/column
orthogonal-complement intersection is exactly one-dimensional, using an
exact cyclotomic upper bound and nonzero 9x9 minors modulo 41.

This script does not repeat the adopted full-array transversal census and
does not certify an arbitrary-core or universal 1-RQLS(10) no-go.
"""
import ast
import hashlib
import itertools
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'frontier-20261029-fixed-core-completion-certificate-v1.json'
SOURCE = ROOT / 'frontier-20261029-quantum-mann-dichotomy-addendum-1.md'
EXPECTED = 'caba356039f35b823d469f11956e771d04b55ca82ed69095e7ea158c0c4f5375'
if OUT.exists():
    raise FileExistsError(OUT)
raw = SOURCE.read_bytes()
assert hashlib.sha256(raw).hexdigest() == EXPECTED
text = raw.decode('utf-8')
T = ast.literal_eval(re.search(r'Characters: T = (\[[^\n]*?\])', text).group(1))
PH = []
for q in ('Q00', 'Q01', 'Q10', 'Q11'):
    pat = re.escape('PHI2[' + q + ']') + r'\s*=\s*(\([^\n]*\))'
    PH.append(ast.literal_eval(re.search(pat, text).group(1)))
assert len(T) == 10 and all(len(p) == 10 for p in PH)

def exponents(q, s, t):
    return tuple((4 * ((a * s + b * t) % 5) + PH[q][j]) % 20
                 for j, (a, b) in enumerate(T))

def zero_inner(u, v):
    coeff = [0] * 20
    for a, b in zip(u, v):
        coeff[(b - a) % 20] += 1
    # z^10 = -1, then Phi20 = z^8-z^6+z^4-z^2+1.
    reduced = [coeff[i] - coeff[i + 10] for i in range(10)]
    for k in (9, 8):
        a = reduced[k]
        reduced[k] = 0
        reduced[k - 2] += a
        reduced[k - 4] -= a
        reduced[k - 6] += a
        reduced[k - 8] -= a
    return not any(reduced)

def edge_vector(q, a, b):
    # q=0: AB edge (a,b); q=1: AC edge (a,b); q=2: BC edge (a,b).
    if q == 0:
        return exponents(q, a, b)
    if q == 1:
        return exponents(q, a, (b - a) % 5)
    return exponents(q, (b - a) % 5, a)

matching_results = {}
for q, name in enumerate(('AB', 'AC', 'BC')):
    good = []
    for perm in itertools.permutations(range(5)):
        vv = [edge_vector(q, a, perm[a]) for a in range(5)]
        if all(zero_inner(vv[i], vv[j]) for i in range(5) for j in range(i + 1, 5)):
            good.append(perm)
    expected = {tuple((k - a) % 5 for a in range(5)) for k in range(5)} if q == 0 else {
        tuple((a + k) % 5 for a in range(5)) for k in range(5)}
    assert set(good) == expected
    assert all(len({perm[a] for perm in good}) == 5 for a in range(5))
    matching_results[name] = {
        'all_permutations_tested': 120,
        'orthogonal_perfect_matchings': [list(p) for p in good],
        'one_factorizations_up_to_class_order': 1,
    }

P = 41
Z = 2
assert pow(Z, 20, P) == 1
assert all(pow(Z, k, P) != 1 for k in (1, 2, 4, 5, 10))
assert (pow(Z, 8, P) - pow(Z, 6, P) + pow(Z, 4, P) - pow(Z, 2, P) + 1) % P == 0

def pivots_mod(matrix):
    a = [[x % P for x in row] for row in matrix]
    nr, nc = len(a), len(a[0])
    row = 0
    pivots = []
    for col in range(nc):
        pivot = next((r for r in range(row, nr) if a[r][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = pow(a[row][col], -1, P)
        a[row] = [(x * scale) % P for x in a[row]]
        for r in range(nr):
            if r != row and a[r][col]:
                factor = a[r][col]
                a[r] = [(x - factor * y) % P for x, y in zip(a[r], a[row])]
        pivots.append(col)
        row += 1
        if row == nr:
            break
    return pivots

def determinant_mod(matrix):
    a = [[x % P for x in row] for row in matrix]
    det = 1
    for col in range(len(a)):
        pivot = next((r for r in range(col, len(a)) if a[r][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            det = -det
        value = a[col][col]
        det = det * value % P
        inverse = pow(value, -1, P)
        for r in range(col + 1, len(a)):
            factor = a[r][col] * inverse % P
            for c in range(col + 1, len(a)):
                a[r][c] = (a[r][c] - factor * a[col][c]) % P
            a[r][col] = 0
    return det % P

rank_witnesses = []
for r, c in itertools.product(range(5), repeat=2):
    # The selected BC matching is row r in Q10; AC matching is column c in Q01.
    columns = [exponents(2, r, t) for t in range(5)] + [exponents(1, s, c) for s in range(5)]
    forced = exponents(3, r, c)
    assert all(zero_inner(v, forced) for v in columns)
    matrix = [[pow(Z, v[j], P) for v in columns] for j in range(10)]
    pc = pivots_mod(matrix)
    assert len(pc) == 9
    selected = [[row[k] for k in pc] for row in matrix]
    pr = pivots_mod(list(map(list, zip(*selected))))
    assert len(pr) == 9
    minor = [[matrix[i][j] for j in pc] for i in pr]
    det = determinant_mod(minor)
    assert det
    rank_witnesses.append({
        'missing_cell': [5 + r, 5 + c],
        'minor_rows_zero_based': pr,
        'minor_columns_zero_based': pc,
        'minor_determinant_mod_41': det,
        'exact_orthogonal_nonzero_vector': list(forced),
        'span_rank_over_Q_zeta20': 9,
        'orthogonal_complement_dimension': 1,
    })

output = {
    'status': 'EXACT_FIXED_OBJECT_FILTER_PASS_NOT_A_UNIVERSAL_NO_GO',
    'native_clock': subprocess.check_output(['/bin/date'], text=True).rstrip('\n'),
    'source_packet_sha256': EXPECTED,
    'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    'arithmetic': 'Integers; reduction modulo Phi20; rank lower bounds in F41 via zeta20 -> 2.',
    'matchings': matching_results,
    'rank_witnesses': rank_witnesses,
    'scope': 'The Q00/Q01/Q10 core of the adopted five-transversal QLS10 only; no non-diagonal core produced.',
    'noncompletion_dependency': 'Written deduction additionally uses the adopted exact five-transversal census, not repeated here.',
}
with OUT.open('x', encoding='utf-8') as f:
    json.dump(output, f, indent=2)
    f.write('\n')
print(json.dumps({
    'status': output['status'],
    'orthogonal_matchings_per_pair': {k: len(v['orthogonal_perfect_matchings']) for k, v in matching_results.items()},
    'one_dimensional_missing_cell_spaces': len(rank_witnesses),
    'native_clock': output['native_clock'],
}, indent=2))
