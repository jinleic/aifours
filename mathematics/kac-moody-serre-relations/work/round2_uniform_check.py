#!/usr/bin/env python3
"""Independent tensor/FLINT checker for the round-two candidate subset.

No producer import. Exact determinant identities and complete cell ledgers
are checked, but a partial ledger is never promoted to uniform equality.
The prior checked height-six theorem and written coefficient-one theorem
are explicit prerequisites, not silently re-proved by this program.
"""
import argparse
import copy
import gzip
import hashlib
import itertools
import json
import math
import time
from fractions import Fraction as Q
from pathlib import Path

import flint
from flint import fmpz_mpoly_ctx
from check_certificate import TensorCoordinates, ExactSpan, tensor, comm, word_lowering
from check_interior_minor import bareiss

EDGES = ((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1))
GOOD = {'POSITIVE_MINOR_CANDIDATE', 'ZERO_QUOTIENT_CANDIDATE', 'POSITIVE_WEIGHT_REDUCTION'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def key(values):
    return ''.join(map(str, values))


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_cover(data, alpha):
    require(data['degree'] == list(alpha), 'coverage degree mismatch')
    require(list(map(tuple, data['edge_order'])) == list(EDGES), 'edge order mismatch')
    expected = set(itertools.product(*(range(1, alpha[i]+1) for i, j in EDGES)))
    rows = data['cover']
    require(len(rows) == len(expected) == data['cell_count'], 'wrong complete cell count')
    require({tuple(row['cell']) for row in rows} == expected, 'omitted or duplicated parameter cell')
    edge_index = {edge: i for i, edge in enumerate(EDGES)}
    for row in rows:
        p = row['permutation']
        require(sorted(p) == [0, 1, 2], 'invalid permutation')
        require(all(alpha[i] == alpha[p[i]] for i in range(3)), 'permutation does not stabilize degree')
        renamed = [0]*6
        for magnitude, (i, j) in zip(row['cell'], EDGES):
            renamed[edge_index[p[i], p[j]]] = magnitude
        require(renamed == row['representative'], 'incorrect cell permutation')
    representatives = sorted({key(row['representative']) for row in rows})
    require(representatives == data['representatives'], 'representative inventory mismatch')
    require(all(tuple(map(int, label)) in expected for label in representatives), 'representative outside parameter partition')
    return representatives


def cell_matrix(alpha, cell):
    require(len(cell) == 6 and all(isinstance(m, int) and 1 <= m <= alpha[i]
                                 for m, (i, j) in zip(cell, EDGES)), 'invalid cell category')
    matrix = [[2 if i == j else 0 for j in range(3)] for i in range(3)]
    variables = []
    for magnitude, (i, j) in zip(cell, EDGES):
        matrix[i][j] = -magnitude
        if magnitude == alpha[i]:
            variables.append((i, j))
    return matrix, variables


def ideals_in_box(matrix, alpha, basis):
    spaces = {}
    for degree in basis.ordered:
        if any(a > b for a, b in zip(degree, alpha)):
            continue
        generated = []
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                exponent = 1-matrix[i][j]
                source_degree = tuple(exponent if k == i else 1 if k == j else 0 for k in range(3))
                if degree == source_degree:
                    polynomial = {(j,): Q(1)}
                    for _ in range(exponent):
                        polynomial = comm({(i,): Q(1)}, polynomial)
                    generated.append(basis.solve(polynomial, degree))
            previous = tuple(a-int(k == i) for k, a in enumerate(degree))
            if previous in spaces:
                generated.extend(basis.raise_row(i, previous, row) for row in spaces[previous].pivots.values())
        spaces[degree] = ExactSpan(generated)
    return spaces


def content_determinant(matrix, ring, arity):
    """Recompute a hard determinant by exact Schur steps and row division.

    For current size m, det(B)=det(p*D-c*r)/p**(m-2).
    This rational-function identity, followed by checked exact row divisions
    and checked polynomial factorizations, yields an exact polynomial identity.
    No producer state, scalar factors, or elimination transcript is trusted.
    """
    current = [row[:] for row in matrix]
    scalar = Q(1)
    raw_factors = []
    divisions = 0
    while len(current) > 1:
        size = len(current)
        choice = next((r for r in range(size) if current[r][0].to_dict().get((0,)*arity)), None)
        require(choice is not None, 'no nonzero constant Schur pivot')
        if choice != 0:
            current[0], current[choice] = current[choice], current[0]
            scalar = -scalar
        pivot = current[0][0]
        raw_factors.append((pivot, 2-size))
        following = []
        for row in current[1:]:
            numerators = [pivot*entry-row[0]*top for entry, top in zip(row[1:], current[0][1:])]
            divisor = ring.constant(0)
            for entry in numerators:
                divisor = divisor.gcd(entry)
            require(divisor != 0, 'zero Schur row')
            raw_factors.append((divisor, 1))
            reduced = []
            for numerator in numerators:
                quotient, remainder = divmod(numerator, divisor)
                require(remainder == 0, 'Schur row division not exact')
                reduced.append(quotient)
                divisions += 1
            following.append(reduced)
        current = following
    raw_factors.append((current[0][0], 1))
    collection = {}
    for polynomial, weight in raw_factors:
        if weight == 0:
            continue
        unit, factorization = polynomial.factor()
        checked = ring.constant(int(unit))
        scalar *= Q(int(unit))**weight
        for factor, multiplicity in factorization:
            checked *= factor**multiplicity
            identity = tuple(sorted((tuple(map(int, powers)), int(value))
                                    for powers, value in factor.to_dict().items()))
            if identity not in collection:
                collection[identity] = [factor, 0]
            collection[identity][1] += weight*int(multiplicity)
        require(checked == polynomial, 'local factorization identity failed')
    require(all(exponent >= 0 for factor, exponent in collection.values()), 'uncancelled determinant denominator')
    answer = ring.constant(scalar.numerator)
    for factor, exponent in collection.values():
        answer *= factor**exponent
    answer, remainder = divmod(answer, ring.constant(scalar.denominator))
    require(remainder == 0, 'final determinant not integral after denominator clearing')
    return answer, divisions


def verify_representative(directory, alpha, label, basis, replacement=None):
    record_path = directory / f'cell-{label}.json'
    data = json.loads(record_path.read_text())
    cell = tuple(map(int, label))
    require(data['degree'] == list(alpha) and data['cell'] == list(cell) and data['cell_key'] == label,
            'cell record scope mismatch')
    matrix, variables = cell_matrix(alpha, cell)
    producer_status = data['status']
    if replacement:
        require(producer_status == 'NO_POSITIVE_MINOR_FOUND', 'replacement does not refer to an attempted gap')
    status = 'POSITIVE_MINOR_CANDIDATE' if replacement else producer_status
    result = {'cell': list(cell), 'status': status, 'producer_status': producer_status,
              'record_sha256': digest(record_path)}
    if status not in GOOD:
        # Failed or deadline-skipped cells remain explicit scope gaps.
        return result
    require(data['baseline_matrix'] == matrix, 'incorrect baseline Cartan matrix')
    if status == 'POSITIVE_WEIGHT_REDUCTION':
        rows = [i for i in range(3)
                if all(cell[k] < alpha[i] for k, edge in enumerate(EDGES) if edge[0] == i)
                and sum(matrix[i][j]*alpha[j] for j in range(3)) > 0]
        require(rows and rows == data['positive_rows'], 'cell is not excluded by a fixed positive weight')
        result['positive_rows'] = rows
        return result
    ideals = ideals_in_box(matrix, alpha, basis)
    columns = [i for i in range(len(basis.words[alpha])) if i not in ideals[alpha].pivots]
    n = len(columns)
    require(n == data['quotient_dimension'], 'wrong Serre quotient dimension')
    require(data['ideal_dimensions'] == {key(a): space.rank() for a, space in ideals.items()},
            'Serre box dimension ledger mismatch')
    result['dimension'] = n
    if status == 'ZERO_QUOTIENT_CANDIDATE':
        require(n == 0, 'nonzero quotient mislabeled as zero')
        return result
    require(n > 0, 'positive-minor certificate with empty source')
    targets = []
    for i in range(3):
        previous = tuple(a-int(i == k) for k, a in enumerate(alpha))
        targets.extend((i, j) for j in range(len(basis.words[previous])) if j not in ideals[previous].pivots)
    require(data['target_dimension'] == len(targets), 'wrong target quotient dimension')
    require(list(map(tuple, data['variable_edges'])) == variables, 'record variable dictionary mismatch')
    certificate_path = replacement if replacement else directory / data['certificate']
    if not replacement:
        require(certificate_path.parent == directory and certificate_path.name.startswith(f'cell-{label}-'),
                'invalid certificate path')
    certificate = json.loads(gzip.decompress(certificate_path.read_bytes()))
    require(certificate['status'] == 'POSITIVE_MINOR_CANDIDATE' and certificate['degree'] == list(alpha)
            and certificate['cell'] == list(cell), 'certificate scope mismatch')
    require(certificate['baseline_matrix'] == matrix and list(map(tuple, certificate['variable_edges'])) == variables,
            'certificate parameter dictionary mismatch')
    require(certificate['quotient_dimension'] == n and certificate['source_columns'] == columns
            and list(map(tuple, certificate['target_coordinates'])) == targets, 'quotient bases mismatch')

    def numbers(cartan):
        out = [[Q(0)]*n for _ in targets]
        target_index = {item: k for k, item in enumerate(targets)}
        for c, column in enumerate(columns):
            polynomial = tensor(basis.words[alpha][column])
            for i in range(3):
                previous = tuple(a-int(i == k) for k, a in enumerate(alpha))
                raw = basis.solve(word_lowering(polynomial, i, cartan), previous)
                for j, value in ideals[previous].remainder(raw).items():
                    out[target_index[i, j]][c] = value
        return out

    baseline = numbers(matrix)
    slopes = []
    for i, j in variables:
        shifted = [row[:] for row in matrix]
        shifted[i][j] -= 1
        values = numbers(shifted)
        slopes.append([[values[r][c]-baseline[r][c] for c in range(n)] for r in range(len(targets))])
    rows = certificate['chosen_rows']
    require(len(rows) == n and len(set(rows)) == n and all(isinstance(r, int) and 0 <= r < len(targets) for r in rows),
            'invalid maximal-minor row selection')
    entries = [[(baseline[r][c],)+tuple(slope[r][c] for slope in slopes) for c in range(n)] for r in rows]
    encoded = certificate['minor_affine']
    require(len(encoded) == n and all(len(row) == n for row in encoded), 'wrong minor shape')
    require(all(tuple(map(Q, encoded[r][c])) == entries[r][c] for r in range(n) for c in range(n)),
            'saved minor differs from independent tensor lowering')
    denominator = math.lcm(*(v.denominator for row in entries for entry in row for v in entry))
    require(denominator > 0 and denominator == certificate['denominator'], 'incorrect denominator clearing')
    arity = max(1, len(variables))
    ring = fmpz_mpoly_ctx.get(tuple('x'+str(i) for i in range(arity)))
    gens = ring.gens()
    scaled = [[ring.constant(int(entry[0]*denominator)) +
               sum((gens[k]*int(entry[k+1]*denominator) for k in range(len(variables))), ring.constant(0))
               for entry in row] for row in entries]
    if certificate.get('determinant_algorithm') == 'row-content elimination and checked factorization identities':
        value, divisions = content_determinant(scaled, ring, arity)
    else:
        value, divisions = bareiss(scaled, ring)
    orientation = certificate['orientation']
    require(orientation in (-1, 1), 'invalid determinant orientation')
    terms = {}
    for powers, coefficient in certificate['polynomial_terms']:
        require(len(powers) == len(variables) and all(isinstance(p, int) and p >= 0 for p in powers), 'invalid exponents')
        powers = tuple(powers) if variables else (0,)
        require(powers not in terms, 'duplicate determinant monomial')
        require(isinstance(coefficient, str) and str(int(coefficient)) == coefficient, 'nonintegral determinant coefficient')
        coefficient = int(coefficient)
        require(coefficient > 0, 'nonpositive polynomial coefficient')
        terms[powers] = coefficient
    require(len(terms) == certificate['monomials'] and certificate['negative_coefficients'] == 0, 'term statistics mismatch')
    constant = int(certificate['constant'])
    require(constant > 0 and terms.get((0,)*arity) == constant, 'nonpositive or incorrect constant')
    require(ring.from_dict(terms) == orientation*value, 'exact determinant identity failed')
    changed = dict(terms)
    changed[(0,)*arity] += 1
    require(ring.from_dict(changed) != orientation*value, 'tampered constant accepted')
    result.update(certificate_sha256=digest(certificate_path), monomials=len(terms),
                  variables=len(variables), positive_constant=str(constant),
                  exact_divisions=divisions, altered_constant_rejected=True)
    return result


def canonical_lower_cell(beta, cell):
    """The finer current cell lies wholly in this lower-degree cell."""
    canonical = tuple(sorted(beta, reverse=True))
    p = min(p for p in itertools.permutations(range(3)) if all(beta[i] == canonical[p[i]] for i in range(3)))
    edge_index = {edge: k for k, edge in enumerate(EDGES)}
    renamed = [0]*6
    for magnitude, (i, j) in zip(cell, EDGES):
        renamed[edge_index[p[i], p[j]]] = min(magnitude, beta[i])
    return key(canonical), key(renamed)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('directory', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--extra-certificates', nargs='*', type=Path, default=[])
    args = parser.parse_args()
    require(not args.output.exists(), 'refusing to overwrite an independent-check receipt')
    started = time.monotonic()
    flint.ctx.threads = 1
    spec_path = args.directory / 'input-322-422-332.json'
    spec = json.loads(spec_path.read_text())
    prior = Path('evidence/symbolic-222/all-cells-independent-check.json')
    require(digest(prior) == spec['prior_height6_receipt_sha256'], 'prior height-six receipt changed')
    prior_data = json.loads(prior.read_text())
    replacements = {}
    for path in args.extra_certificates:
        certificate = json.loads(gzip.decompress(path.read_bytes()))
        require(certificate['status'] == 'POSITIVE_MINOR_CANDIDATE', 'supplement is not a positive-minor candidate')
        identity = (key(certificate['degree']), key(certificate['cell']))
        require(identity not in replacements, 'duplicate replacement certificate')
        replacements[identity] = path
    used_replacements = set()
    require(prior_data['status'] == 'PASS' and prior_data['cell_count'] == 64, 'prior uniform height-six prerequisite absent')
    basis = TensorCoordinates(8)
    degrees = [(3, 2, 2), (4, 2, 2), (3, 3, 2)]
    equality = {}
    summaries = []
    for alpha in degrees:
        directory = args.directory / ('degree-'+key(alpha))
        coverage_path = directory / 'cover.json'
        coverage = json.loads(coverage_path.read_text())
        representatives = verify_cover(coverage, alpha)
        damaged = copy.deepcopy(coverage)
        damaged['cover'].pop()
        try:
            verify_cover(damaged, alpha)
        except ValueError:
            omitted_cell_rejected = True
        else:
            raise AssertionError('incomplete coverage accepted')
        records = {}
        for label in representatives:
            replacement = replacements.get((key(alpha), label))
            record = verify_representative(directory, alpha, label, basis, replacement)
            if replacement:
                used_replacements.add((key(alpha), label))
            records[label] = record
            print(json.dumps({'degree': alpha, 'checked_cell': label, 'status': record['status'],
                              'dimension': record.get('dimension'), 'monomials': record.get('monomials')}), flush=True)
        local_good, equality_good, dependency_gaps = [], [], []
        equality[key(alpha)] = {}
        for row in coverage['cover']:
            cell = tuple(row['cell'])
            status = records[key(row['representative'])]['status']
            good = status in GOOD
            dependencies = []
            if sum(alpha) > 7:
                for i in range(3):
                    beta = tuple(a-int(i == j) for j, a in enumerate(alpha))
                    if min(beta) >= 2 and sum(beta) > 6:
                        degree_key, lower_key = canonical_lower_cell(beta, cell)
                        if not equality.get(degree_key, {}).get(lower_key, False):
                            dependencies.append({'degree': degree_key, 'cell': lower_key})
            equal = good and (status == 'ZERO_QUOTIENT_CANDIDATE' or not dependencies)
            equality[key(alpha)][key(cell)] = equal
            if good:
                local_good.append(list(cell))
            if equal:
                equality_good.append(list(cell))
            if good and not equal:
                dependency_gaps.append({'cell': list(cell), 'unsettled_lower_cells': dependencies})
        produced = json.loads((directory/'summary.json').read_text())
        original_good = [row['cell'] for row in coverage['cover']
                         if records[key(row['representative'])]['producer_status'] in GOOD]
        require(produced['candidate_covered_cells'] == original_good, 'producer candidate-coverage ledger mismatch')
        require(produced['uncovered_cells'] == [row['cell'] for row in coverage['cover'] if row['cell'] not in original_good],
                'producer gap ledger mismatch')
        require(produced['all_cells_candidate_covered'] == (len(original_good) == coverage['cell_count']), 'false uniform candidate flag')
        summaries.append({'degree': list(alpha), 'cell_count': coverage['cell_count'],
                          'representative_count': len(records), 'records': list(records.values()),
                          'local_candidate_verified_cells': local_good, 'equality_cells': equality_good,
                          'uncovered_local_cells': [row['cell'] for row in coverage['cover'] if row['cell'] not in local_good],
                          'lower_degree_dependency_gaps': dependency_gaps,
                          'all_cells_equal': len(equality_good) == coverage['cell_count'],
                          'coverage_sha256': digest(coverage_path), 'omitted_cell_rejected': omitted_cell_rejected})
    require(used_replacements == set(replacements), 'unconsumed replacement outside the checked scope')
    height7 = summaries[0]['all_cells_equal']
    height8 = height7 and all(summary['all_cells_equal'] for summary in summaries[1:])
    source_paths = [Path(__file__), Path('work/check_certificate.py'), Path('work/check_interior_minor.py')]
    result = {'status': 'PASS_EXACT_REPORTED_SUBSET', 'uniform_height7': height7, 'uniform_height8': height8,
              'degrees': summaries, 'field': 'Q; exact integer polynomial determinants after positive denominator clearing',
              'threads': 1, 'python_flint_version': flint.__version__,
              'prerequisite_height6_receipt_sha256': digest(prior), 'producer_input_sha256': digest(spec_path),
              'source_sha256': {str(path): digest(path) for path in source_paths},
              'elapsed_seconds': round(time.monotonic()-started, 3),
              'logical_scope': 'Listed equality cells only, conditional on the written coefficient-one/Serre/descent/sl2 reductions and the prior accepted uniform height-six certificate. Missing-edge rank-three matrices are symmetrizable. No all-height claim.'}
    args.output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'degrees'}, indent=2))


if __name__ == '__main__':
    main()
