#!/usr/bin/env python3
"""Genuinely new grade8 complete primitive maps on the free region r,s>=8.

Producer: whole f1/f2 kernel in the full Lyndon root space, canonical affine
endomorphism, complete bivariate determinant interpolation. Replay: separate
literal string-Lyndon/tree-Jacobi source/actions/contraction, every affine
matrix and the entire determinant on a DIFFERENT unisolvent triangle.
No actual-parameter claim below8, no whole-level8 or B8 result.
"""
SOURCE_INPUT = None
import argparse
import hashlib
import importlib.util
import json
import math
from collections import Counter
from fractions import Fraction as Q
from pathlib import Path
ROOT = Path(__file__).resolve().parent

def load(name, file):
    spec = importlib.util.spec_from_file_location(name, ROOT / file)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m

def pin(name, sha):
    assert Path(name).name == name
    raw = (ROOT / name).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == sha
    return json.loads(raw)

def publish(name, record):
    with (ROOT / name).open('x') as stream:
        json.dump(record, stream, indent=2)
        stream.write('\n')
    return hashlib.sha256((ROOT / name).read_bytes()).hexdigest()

def mobius(d):
    count = 0
    p = 2
    while p * p <= d:
        if d % p == 0:
            d //= p
            count += 1
            if d % p == 0:
                return 0
        p += 1
    return (-1) ** (count + int(d > 1))

def dimensions(weights, a, b):
    chars = [Counter({(0, 0): 1})]
    for n in range(1, 9):
        following = Counter()
        for (u, v), c in chars[-1].items():
            for x, y in weights:
                following[u + x, v + y] += c
        chars.append(following)

    def lie(x, y):
        if x < 0 or y < 0:
            return 0
        value = sum((mobius(d) * chars[8 // d][x // d, y // d] for d in (1, 2, 4, 8) if x % d == 0 and y % d == 0))
        assert value % 8 == 0
        return value // 8
    multiplicity = lie(a, b) - lie(a - 1, b) - lie(a, b - 1) + lie(a - 2, b - 1) + lie(a - 1, b - 2) - lie(a - 2, b - 2)
    return (lie(a, b), multiplicity)

def signed_stirling(m):
    rows = [[1]]
    for n in range(1, m + 1):
        row = [0] * (n + 1)
        for j, c in enumerate(rows[-1]):
            row[j] -= (n - 1) * c
            row[j + 1] += c
        rows.append(row)
    return rows

def polynomial(triples, F):
    k = len(triples)
    scales = [math.lcm(*(c.denominator for e in row for c in e)) for row in triples]
    data = [[[int(c * s) for c in e] for e in row] for row, s in zip(triples, scales)]
    scale = math.prod(scales)
    MA, MB, MC = [F.fmpz_mat([[e[t] for e in row] for row in data]) for t in range(3)]
    values = {}
    for i in range(k + 1):
        current = MA + MB * i
        for j in range(k + 1 - i):
            values[i, j] = int(current.det())
            current = current + MC
    dx = {}
    dxy = {}
    for j in range(k + 1):
        work = [values[i, j] for i in range(k + 1 - j)]
        for i in range(k + 1 - j):
            dx[i, j] = work[0]
            work = [b - a for a, b in zip(work, work[1:])]
    for i in range(k + 1):
        work = [dx[i, j] for j in range(k + 1 - i)]
        for j in range(k + 1 - i):
            dxy[i, j] = work[0]
            work = [b - a for a, b in zip(work, work[1:])]
    st = signed_stirling(k)
    factorials = [math.factorial(i) for i in range(k + 1)]
    NF = factorials[k]
    mixed = [[0] * (k + 1) for _ in range(k + 1)]
    for (i, j), d in dxy.items():
        if d:
            multiplier = d * (NF // factorials[j])
            for v, c in enumerate(st[j]):
                if c:
                    mixed[i][v] += multiplier * c
    nums = {}
    for v in range(k + 1):
        for u in range(k + 1 - v):
            c = sum((st[i][u] * (NF // factorials[i]) * mixed[i][v] for i in range(u, k + 1) if st[i][u] and mixed[i][v]))
            if c:
                nums[u, v] = c
    for i in range(k + 1):
        powers = [i ** u for u in range(k + 1)]
        columns = [0] * (k + 1)
        for (u, v), c in nums.items():
            columns[v] += c * powers[u]
        for j in range(k + 1 - i):
            z = 0
            for c in reversed(columns):
                z = z * j + c
            assert z == values[i, j] * NF * NF
    terms = {m: Q(c, NF * NF * scale) for m, c in nums.items()}
    return (triples, terms, len(values))

def produce(a, b):
    A = load('grade8_exact_canonical_tools', 'frontier-20261029-level6-canonical-contraction.py')
    dimension, k = dimensions(A.levi.WEIGHTS, a, b)
    assert 0 < k <= 300 and dimension <= 1200, 'bounded additional grade8 free-region types'
    basis = A.levi.lie_basis((a, b, 8))
    assert len(basis) == dimension
    assert SOURCE_INPUT is not None
    source_packet = pin(SOURCE_INPUT[0], SOURCE_INPUT[1])
    assert source_packet['degree'] == [a, b, 8]
    assert source_packet['complete_free_weight_dimension'] == dimension and source_packet['entire_lowest_dimension'] == k
    assert source_packet['source_words'] == [''.join(map(str, w)) for w, _ in basis]
    assert source_packet['all_full_word_F1_F2_integer_products_zero'] and source_packet['RREF_identity_on_all_pivot_coordinates']
    coefficients = [{int(j): Q(c) for j, c in co.items()} for co in source_packet['source_coefficients']]
    detectors = source_packet['detector_Lyndon_indices']
    assert len(coefficients) == k
    assert len(set(detectors)) == k
    assert all((co.get(j, 0) == int(i == q) for i, co in enumerate(coefficients) for q, j in enumerate(detectors)))
    primitive = A.qmatrix([[co.get(j, 0) for co in coefficients] for j in range(dimension)])
    matrices = []
    for r, s in ((8, 8), (9, 8), (8, 9)):
        all_images = []
        selected = []
        for co in coefficients:
            den = math.lcm(*(Q(c).denominator for c in co.values()))
            vector = {}
            for j, c in co.items():
                A.plus(vector, A.standard(basis[j][0]), int(c * den))
            assert vector and (not A.action2(vector, 'f1')) and (not A.action2(vector, 'f2'))
            output = A.canonical_96(A.suffix_d3_2(vector, r, s))
            assert not A.action2(output, 'f1') and (not A.action2(output, 'f2'))
            image = A.decompose_integer(output)
            normalization = den * 192
            all_images.append({w: Q(c, normalization) for w, c in image.items()})
            selected.append([Q(image.get(basis[j][0], 0), normalization) for j in detectors])
        M = [list(row) for row in zip(*selected)]
        assert primitive * A.qmatrix(M) == A.qmatrix([[co.get(w, Q(0)) for co in all_images] for w, _ in basis])
        matrices.append(M)
    triples = [[[matrices[0][i][j], matrices[1][i][j] - matrices[0][i][j], matrices[2][i][j] - matrices[0][i][j]] for j in range(k)] for i in range(k)]
    pencil_name = f'frontier-20261029-level8-{a}{b}-native-primitive-pencil-v1.json'
    pencil = {
        'owner': 'MathKacMoody-2', 'degree': [a, b, 8],
        'variable_meaning': 'x=r-8,y=s-8',
        'complete_free_weight_dimension': dimension,
        'entire_primitive_dimension': k,
        'source_words': [''.join(map(str, w)) for w, _ in basis],
        'source_coefficients': [{str(j): str(c) for j, c in sorted(co.items())} for co in coefficients],
        'detector_Lyndon_indices': detectors,
        'matrix': [[[str(c) for c in e] for e in row] for row in triples],
        'modular_source': {'file': SOURCE_INPUT[0], 'sha256': SOURCE_INPUT[1]},
        'all_source_membership_independence_character_checks': True,
        'all_three_entire_source_matrix_identities': True,
        'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'status': 'COMPLETE_SOURCE_AND_AFFINE_PENCIL_NO_RANK',
        'limits': 'Resumable exact free-source/pencil stage only; no determinant, actual-source/seed/PBW/D3/parent/formal/novelty adoption.'
    }
    pencil_sha = publish(pencil_name, pencil)
    print('RESUMABLE whole source/pencil', (a, b, 8), pencil_name, pencil_sha, flush=True)
    triples, terms, points = polynomial(triples, A.flint)
    name = f'frontier-20261029-level8-{a}{b}-native-primitive-candidate-v1.json'
    result = {'owner': 'MathKacMoody-2', 'degree': [a, b, 8], 'variables': 'x=r-8,y=s-8', 'source_words': [''.join(map(str, w)) for w, _ in basis], 'source_coefficients': [{str(j): str(c) for j, c in sorted(co.items())} for co in coefficients], 'complete_free_weight_dimension': dimension, 'entire_lowest_dimension': k, 'detector_Lyndon_indices': detectors, 'matrix': [[[str(c) for c in e] for e in row] for row in triples], 'polynomial': [{'x_power': u, 'y_power': v, 'coefficient': str(c)} for (u, v), c in sorted(terms.items())], 'full_triangular_grid_points': points, 'positive_coefficients': sum((c > 0 for c in terms.values())), 'negative_coefficients': sum((c < 0 for c in terms.values())), 'positive_constant': terms.get((0, 0), Q(0)) > 0, 'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'canonical_helper': {'file': 'frontier-20261029-level6-canonical-contraction.py', 'sha256': hashlib.sha256((ROOT / 'frontier-20261029-level6-canonical-contraction.py').read_bytes()).hexdigest()}, 'status': 'PRODUCER_ENTIRE_GRADE8_FREE_REGION_SMALL_MAP_CANDIDATE', 'limits': 'Exact candidate source/pencil/polynomial only; alternate reconstruction and actual-source/classical/contraction review required. Claimed parameter region r,s>=8 only if all coefficients positive with positive constant. No small rows, whole grade8/B8, f173 actual-source transfer, parent/formal/kernel/configured-family/human/native-library/novelty acceptance.'}
    result['source_and_pencil_checkpoint'] = {'file': pencil_name, 'sha256': pencil_sha}
    result['modular_source'] = {'file': SOURCE_INPUT[0], 'sha256': SOURCE_INPUT[1]}
    result['replacement_scope'] = 'NEW modular RREF plus exact whole-word kernel lift, developed after the direct type32 free-source/pencil/polynomial run returned no certificate within1800s; that failed stage is unknown. No outcome of another direct run is inferred. Full source/matrices/positive-parameter scope is unchanged.'
    sha = publish(name, result)
    print('WROTE new grade8', (a, b, 8), 'free', dimension, 'lowest', k, 'positive', result['positive_coefficients'], 'negative', result['negative_coefficients'], 'constant', result['positive_constant'], name, sha, flush=True)

def replay(a, b, sha):
    A = load('grade8_literal_old_replay', 'frontier-20261029-level7-canonical-independent-replay.py')
    name = f'frontier-20261029-level8-{a}{b}-native-primitive-candidate-v1.json'
    C = pin(name, sha)
    words = C['source_words']
    assert tuple(words) == A.ind.lyndon_words((a, b, 8))
    dim, k = dimensions(A.ind.WEIGHTS, a, b)
    assert (dim, k) == (len(words), C['entire_lowest_dimension'])
    coefs = [{int(j): Q(c) for j, c in row.items()} for row in C['source_coefficients']]
    free = C['detector_Lyndon_indices']
    assert len(coefs) == len(free) == k
    assert all((co.get(j, 0) == int(i == q) for i, co in enumerate(coefs) for q, j in enumerate(free)))
    for co in coefs:
        vector = A.ind.combine([A.ind.ind.standard_bracket(w) for w in words], co)
        assert not A.ind.act(vector, 'f1', 8, 8) and (not A.ind.act(vector, 'f2', 8, 8))
    primitive = A.qmatrix([[co.get(j, Q(0)) for co in coefs] for j in range(dim)])
    G = [[sum((A.ind.BASIS[i][u][v] * A.ind.BASIS[j][u][v] for u in range(3) for v in range(3))) for j in range(8)] for i in range(8)]
    inverse = A.qmatrix(G).inv()
    GI = [[Q(str(inverse[i, j])) for j in range(8)] for i in range(8)]
    matrices = []
    for r, s in ((8, 8), (9, 8), (8, 9)):
        all_images = []
        selected = []
        for co in coefs:
            d = A.full_tree_d3(co, words, r, s)
            out, den = A.independent_contraction(d, GI)
            assert set(out) <= set(words)
            all_images.append({w: Q(c, den) for w, c in out.items()})
            selected.append([Q(out.get(words[j], 0), den) for j in free])
        M = [list(row) for row in zip(*selected)]
        assert primitive * A.qmatrix(M) == A.qmatrix([[co.get(w, Q(0)) for co in all_images] for w in words])
        matrices.append(M)
    triples = [[[matrices[0][i][j], matrices[1][i][j] - matrices[0][i][j], matrices[2][i][j] - matrices[0][i][j]] for j in range(k)] for i in range(k)]
    assert [[[str(c) for c in e] for e in row] for row in triples] == C['matrix']
    terms = {(t['x_power'], t['y_power']): Q(t['coefficient']) for t in C['polynomial']}
    assert len(terms) == len(C['polynomial']) and all((u + v <= k and min(u, v) >= 0 for u, v in terms))
    assert terms.get((0, 0), Q(0)) > 0 and all((c > 0 for c in terms.values()))
    checked = 0
    termden = math.lcm(*(c.denominator for c in terms.values()))
    termints = {m: int(c * termden) for m, c in terms.items()}
    scales = [math.lcm(*(c.denominator for e in row for c in e)) for row in triples]
    scale = math.prod(scales)
    data = [[[int(c * s) for c in e] for e in row] for row, s in zip(triples, scales)]
    MA, MB, MC = [A.flint.fmpz_mat([[e[t] for e in row] for row in data]) for t in range(3)]
    for i in range(k + 1):
        x = i - 2
        powers = [x ** u for u in range(k + 1)]
        columns = [0] * (k + 1)
        for (u, v), c in termints.items():
            columns[v] += c * powers[u]
        for j in range(k + 1 - i):
            y = j + 3
            value = 0
            for c in reversed(columns):
                value = value * y + c
            assert int((MA + MB * x + MC * y).det()) * termden == value * scale
            checked += 1
    assert checked == (k + 1) * (k + 2) // 2
    output = f'frontier-20261029-level8-{a}{b}-small-primitive-replay-v1.json'
    result = {'owner': 'MathKacMoody-2', 'input_file': name, 'input_sha256': sha, 'degree': [a, b, 8], 'complete_free_weight_dimension': dim, 'entire_lowest_dimension': k, 'whole_source_membership_independence_and_Witt_Weyl_completeness': True, 'all3_entire_source_matrix_identities': True, 'positive_polynomial_terms': len(terms), 'shifted_full_matrix_determinants': checked, 'grid': 'x=i-2,y=j+3;i,j>=0;i+j<=lowest dimension', 'program_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'literal_algebra': {'file': 'frontier-20261029-level7-canonical-independent-replay.py', 'sha256': hashlib.sha256((ROOT / 'frontier-20261029-level7-canonical-independent-replay.py').read_bytes()).hexdigest()}, 'status': 'PASS_ALTERNATE_ENTIRE_GRADE8_SMALL_MAP_FREE_REGION', 'limits': 'Separate literal actions/tree-Jacobi/cyclic-negative replay, same owner and FLINT; shared scalar Witt character method. Actual-source/PBW/classical/contraction inputs UNREVIEWED, f173 conditional only. Region r,s>=8 only; no small parameters, whole grade8/B8, parent/formal/kernel/configured-family/human/native-library/status/novelty acceptance.'}
    print('PASS new grade8 replay', (a, b, 8), 'lowest', k, 'grid', checked, output, publish(output, result), flush=True)

def main():
    if not __debug__:
        raise RuntimeError('assertions disabled')
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', type=int, required=True)
    ap.add_argument('--b', type=int, required=True)
    ap.add_argument('--replay-sha256')
    ap.add_argument('--source-packet')
    ap.add_argument('--source-sha256')
    args = ap.parse_args()
    global SOURCE_INPUT
    SOURCE_INPUT = (args.source_packet, args.source_sha256) if args.source_packet and args.source_sha256 else None
    if args.replay_sha256:
        replay(args.a, args.b, args.replay_sha256)
    else:
        produce(args.a, args.b)
if __name__ == '__main__':
    main()
