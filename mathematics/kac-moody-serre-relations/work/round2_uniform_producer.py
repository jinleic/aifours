#!/usr/bin/env python3
"""Bounded exact rank-three cell-minor research; never an independent checker.

Only new round2-uniform outputs are written. A cell digit m<alpha_i fixes
-a_ij=m; the digit alpha_i means -a_ij=alpha_i+x, x>=0. Stabilizers, not
all of S3, identify cells at a fixed nonconstant multidegree.
"""
import argparse
import gzip
import hashlib
import itertools
import json
import math
import signal
import sys
import time
from fractions import Fraction as Q
from pathlib import Path

import flint
from flint import fmpz_mpoly_ctx
from graded_lie import Field, FreeLie, RowSpace, bracket, descend_factory

EDGES = ((0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1))


def save(path, data):
    if path.exists():
        raise FileExistsError(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.suffix == '.gz':
        with gzip.open(path, 'wt') as stream:
            json.dump(data, stream, sort_keys=True)
    else:
        path.write_text(json.dumps(data, indent=2) + '\n')


def key(cell):
    return ''.join(map(str, cell))


def cover(alpha):
    cells = list(itertools.product(*(range(1, alpha[i] + 1) for i, j in EDGES)))
    permutations = [p for p in itertools.permutations(range(3))
                    if all(alpha[p[i]] == alpha[i] for i in range(3))]
    edge_index = {edge: k for k, edge in enumerate(EDGES)}
    rows = []
    for cell in cells:
        orbit = []
        for p in permutations:
            renamed = [0] * 6
            for k, (i, j) in enumerate(EDGES):
                renamed[edge_index[p[i], p[j]]] = cell[k]
            orbit.append((tuple(renamed), p))
        representative, permutation = min(orbit)
        rows.append({'cell': list(cell), 'representative': list(representative),
                     'permutation': list(permutation)})
    return {'degree': list(alpha), 'edge_order': EDGES,
            'cell_count': len(cells), 'cover': rows,
            'representatives': sorted({key(row['representative']) for row in rows})}


def serre_spaces(matrix, alpha, free):
    original = {}
    for i, j in EDGES:
        exponent = 1 - matrix[i][j]
        degree = tuple(exponent if k == i else 1 if k == j else 0 for k in range(3))
        if all(a <= b for a, b in zip(degree, alpha)):
            polynomial = {(j,): 1}
            for _ in range(exponent):
                polynomial = bracket({(i,): 1}, polynomial)
            original.setdefault(degree, []).append(free.coordinates(polynomial, degree))
    ideals = {}
    for degree in sorted(free.words, key=lambda a: (sum(a), a)):
        if not all(a <= b for a, b in zip(degree, alpha)):
            continue
        space = RowSpace(Field(), original.get(degree, ()))
        for i in range(3):
            previous = tuple(a - int(i == k) for k, a in enumerate(degree))
            if previous in ideals:
                for row in ideals[previous].basis():
                    space.add(free.ad_generator(i, previous, row))
        ideals[degree] = space
    return ideals


def raw_lowerings(alpha, free):
    """Cache affine coefficient arrays once, before any ideal projection."""
    diagonal = tuple(tuple(2 if i == j else 0 for j in range(3)) for i in range(3))
    lower = descend_factory(diagonal)
    raw = {}
    for i in range(3):
        previous = tuple(a - int(i == k) for k, a in enumerate(alpha))
        raw[i, -1] = [free.coordinates(lower(i, word), previous) for word in free.words[alpha]]
        for edge, (u, v) in enumerate(EDGES):
            if u != i:
                continue
            shifted = [list(row) for row in diagonal]
            shifted[u][v] = -1
            slope = descend_factory(tuple(map(tuple, shifted)))
            values = []
            for column, word in enumerate(free.words[alpha]):
                value = free.coordinates(slope(i, word), previous)
                for j, coefficient in raw[i, -1][column].items():
                    value[j] = value.get(j, 0) - coefficient
                    if not value[j]:
                        del value[j]
                values.append(value)
            raw[i, edge] = values
    return raw


def affine_matrix(alpha, cell, ideals, free, raw):
    columns = [j for j in range(len(free.words[alpha])) if j not in ideals[alpha].rows]
    targets = []
    variables = [k for k, (i, j) in enumerate(EDGES) if cell[k] == alpha[i]]
    for i in range(3):
        previous = tuple(a - int(i == k) for k, a in enumerate(alpha))
        targets.extend((i, j) for j in range(len(free.words[previous])) if j not in ideals[previous].rows)
    target_index = {item: k for k, item in enumerate(targets)}
    entries = [[[Q(0)] * (1 + len(variables)) for _ in columns] for _ in targets]
    for c, column in enumerate(columns):
        for i in range(3):
            previous = tuple(a - int(i == k) for k, a in enumerate(alpha))
            baseline = dict(raw[i, -1][column])
            for edge, (u, v) in enumerate(EDGES):
                if u == i:
                    for j, coefficient in raw[i, edge][column].items():
                        baseline[j] = baseline.get(j, 0) + cell[edge] * coefficient
            for j, coefficient in ideals[previous].reduce(baseline).items():
                entries[target_index[i, j]][c][0] = coefficient
            for v, edge in enumerate(variables, 1):
                if EDGES[edge][0] == i:
                    for j, coefficient in ideals[previous].reduce(raw[i, edge][column]).items():
                        entries[target_index[i, j]][c][v] = coefficient
    return columns, targets, variables, entries


def select_rows(entries, order):
    span = RowSpace(Field())
    chosen = []
    for r in order:
        if span.add({j: entry[0] for j, entry in enumerate(entries[r]) if entry[0]}):
            chosen.append(r)
    return chosen


def determinant(matrix, ring, term_limit, event):
    """Producer Bareiss implementation, with explicit exact-division checks."""
    values = [row[:] for row in matrix]
    previous, sign = ring.constant(1), 1
    for k in range(len(values) - 1):
        pivot_row = next((i for i in range(k, len(values)) if values[i][k]), None)
        if pivot_row is None:
            return ring.constant(0)
        if pivot_row != k:
            values[k], values[pivot_row] = values[pivot_row], values[k]
            sign = -sign
        pivot = values[k][k]
        largest = 0
        for i in range(k + 1, len(values)):
            for j in range(k + 1, len(values)):
                numerator = values[i][j] * pivot - values[i][k] * values[k][j]
                quotient, remainder = divmod(numerator, previous)
                if remainder:
                    raise ArithmeticError('nonexact producer Bareiss division')
                values[i][j] = quotient
                largest = max(largest, len(quotient))
                if largest > term_limit:
                    raise OverflowError(f'intermediate entry exceeds {term_limit} monomials at pivot {k}')
            values[i][k] = ring.constant(0)
        previous = pivot
        event({'pivot': k, 'largest_entry_terms': largest})
    return sign * values[-1][-1]


def expired(signum, frame):
    raise TimeoutError('per-minor mathematical computation deadline')


def run_degree(alpha, free, args, log):
    output = args.output / ('degree-' + key(alpha))
    output.mkdir(parents=True, exist_ok=True)
    coverage = cover(alpha)
    save(output / 'cover.json', coverage)
    raw = raw_lowerings(alpha, free)
    start = time.monotonic()
    results = []
    def event(data):
        log.write(json.dumps({'degree': alpha, 'elapsed': round(time.monotonic() - start, 3), **data}) + '\n')
        log.flush()
    for label in coverage['representatives']:
        cell = tuple(map(int, label))
        record = {'degree': alpha, 'cell': cell, 'cell_key': label, 'attempts': []}
        if time.monotonic() - start >= args.seconds_per_degree:
            record['status'] = 'NOT_ATTEMPTED_DEGREE_DEADLINE'
            save(output / f'cell-{label}.json', record)
            results.append(record)
            continue
        begin = time.monotonic()
        event({'cell': label, 'phase': 'start'})
        matrix = [[2 if i == j else 0 for j in range(3)] for i in range(3)]
        for magnitude, (i, j) in zip(cell, EDGES):
            matrix[i][j] = -magnitude
        record['baseline_matrix'] = matrix
        # If a whole cell has a strictly positive row weight, the first-relation
        # cone criterion excludes this degree once its lower degrees are equal.
        fixed_positive = [i for i in range(3)
                          if all(cell[k] < alpha[i] for k, edge in enumerate(EDGES) if edge[0] == i)
                          and sum(matrix[i][j] * alpha[j] for j in range(3)) > 0]
        if fixed_positive:
            record.update(status='POSITIVE_WEIGHT_REDUCTION', positive_rows=fixed_positive)
        else:
            ideals = serre_spaces(matrix, alpha, free)
            columns, targets, variables, entries = affine_matrix(alpha, cell, ideals, free, raw)
            n = len(columns)
            record.update(quotient_dimension=n, target_dimension=len(targets),
                          variable_edges=[EDGES[k] for k in variables],
                          ideal_dimensions={key(a): len(space) for a, space in ideals.items()})
            if not n:
                record['status'] = 'ZERO_QUOTIENT_CANDIDATE'
            else:
                orders = [list(range(len(targets))), list(reversed(range(len(targets)))),
                          sorted(range(len(targets)), key=lambda r: (sum(any(e) for e in entries[r]), r))]
                used = set()
                record['status'] = 'NO_POSITIVE_MINOR_FOUND'
                for attempt, order in enumerate(orders[:args.attempts]):
                    rows = select_rows(entries, order)
                    if len(rows) != n:
                        record['status'] = 'BASELINE_RANK_DEFECT_REQUIRES_AUDIT'
                        record['baseline_rank'] = len(rows)
                        break
                    if tuple(sorted(rows)) in used:
                        continue
                    used.add(tuple(sorted(rows)))
                    selected = [[entries[r][c] for c in range(n)] for r in rows]
                    denominator = math.lcm(*(v.denominator for row in selected for entry in row for v in entry))
                    candidate = {'degree': alpha, 'cell': cell, 'baseline_matrix': matrix,
                                 'variable_edges': [EDGES[k] for k in variables],
                                 'quotient_dimension': n, 'source_columns': columns,
                                 'target_coordinates': targets, 'chosen_rows': rows,
                                 'denominator': denominator,
                                 'minor_affine': [[[str(v) for v in entry] for entry in row] for row in selected]}
                    prefix = f'cell-{label}-attempt-{attempt}'
                    save(output / (prefix + '-input.json.gz'), candidate)
                    attempt_start = time.monotonic()
                    event({'cell': label, 'attempt': attempt, 'phase': 'determinant', 'dimension': n, 'variables': len(variables)})
                    try:
                        signal.setitimer(signal.ITIMER_REAL, min(args.seconds_per_minor,
                            max(0.01, args.seconds_per_degree - (time.monotonic() - start))))
                        arity = max(1, len(variables))
                        ring = fmpz_mpoly_ctx.get(tuple('x' + str(i) for i in range(arity)))
                        gens = ring.gens()
                        polynomial_matrix = [[ring.constant(int(entry[0] * denominator)) +
                            sum((gens[k] * int(entry[k+1] * denominator) for k in range(len(variables))), ring.constant(0))
                            for entry in row] for row in selected]
                        value = determinant(polynomial_matrix, ring, args.term_limit,
                            lambda detail: event({'cell': label, 'attempt': attempt, **detail}))
                        terms = value.to_dict()
                        constant = int(terms.get((0,) * arity, 0))
                        if not constant:
                            raise ArithmeticError('selected full-rank baseline minor has zero constant')
                        orientation = 1 if constant > 0 else -1
                        normalized = sorted((tuple(map(int, powers)), orientation * int(coefficient)) for powers, coefficient in terms.items())
                        negatives = sum(coefficient < 0 for powers, coefficient in normalized)
                        candidate.update(status='POSITIVE_MINOR_CANDIDATE' if not negatives else 'SIGN_TEST_INCONCLUSIVE',
                                         orientation=orientation, constant=str(abs(constant)),
                                         monomials=len(normalized), negative_coefficients=negatives,
                                         polynomial_terms=[[list(powers) if variables else [], str(coefficient)] for powers, coefficient in normalized])
                    except (TimeoutError, OverflowError, ArithmeticError) as error:
                        candidate.update(status=type(error).__name__.upper(), error=str(error))
                    finally:
                        signal.setitimer(signal.ITIMER_REAL, 0)
                    candidate['elapsed_seconds'] = round(time.monotonic() - attempt_start, 3)
                    path = output / (prefix + '.json.gz')
                    save(path, candidate)
                    attempt_record = {'path': path.name, 'status': candidate['status'],
                                      'seconds': candidate['elapsed_seconds'],
                                      'monomials': candidate.get('monomials'),
                                      'negative_coefficients': candidate.get('negative_coefficients')}
                    record['attempts'].append(attempt_record)
                    event({'cell': label, 'attempt': attempt, **attempt_record})
                    if candidate['status'] == 'POSITIVE_MINOR_CANDIDATE':
                        record['status'] = candidate['status']
                        record['certificate'] = path.name
                        break
        record['elapsed_seconds'] = round(time.monotonic() - begin, 3)
        save(output / f'cell-{label}.json', record)
        results.append(record)
        event({'cell': label, 'phase': 'complete', 'status': record['status'], 'seconds': record['elapsed_seconds']})
        print(json.dumps({'degree': alpha, 'cell': label, 'status': record['status'], 'dimension': record.get('quotient_dimension'), 'seconds': record['elapsed_seconds']}), flush=True)
    good = {'POSITIVE_MINOR_CANDIDATE', 'ZERO_QUOTIENT_CANDIDATE', 'POSITIVE_WEIGHT_REDUCTION'}
    by_key = {record['cell_key']: record for record in results}
    covered = [row['cell'] for row in coverage['cover'] if by_key[key(row['representative'])]['status'] in good]
    summary = {'degree': alpha, 'cell_count': coverage['cell_count'], 'representative_count': len(results),
               'candidate_covered_cells': covered,
               'uncovered_cells': [row['cell'] for row in coverage['cover'] if row['cell'] not in covered],
               'all_cells_candidate_covered': len(covered) == coverage['cell_count'],
               'elapsed_seconds': round(time.monotonic() - start, 3), 'results': results,
               'scope': 'Exact producer candidates and written cone reductions; independent checker NOT run. Equality requires equality in all immediately lower degrees.'}
    save(output / 'summary.json', summary)
    return {k: v for k, v in summary.items() if k != 'results'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--degrees', nargs='+', choices=['322', '422', '332'], required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--seconds-per-minor', type=float, default=30)
    parser.add_argument('--seconds-per-degree', type=float, default=1200)
    parser.add_argument('--term-limit', type=int, default=250000)
    parser.add_argument('--attempts', type=int, choices=[1, 2, 3], default=3)
    args = parser.parse_args()
    flint.ctx.threads = 1
    signal.signal(signal.SIGALRM, expired)
    args.output.mkdir(parents=True, exist_ok=True)
    run_label = '-'.join(args.degrees)
    spec = {'date': '2026-10-14', 'argv': sys.argv, 'degrees': args.degrees,
            'seconds_per_minor': args.seconds_per_minor, 'seconds_per_degree': args.seconds_per_degree,
            'term_limit': args.term_limit, 'attempts': args.attempts,
            'processes': 1, 'threads': 1, 'python_flint_version': flint.__version__,
            'producer_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'graded_lie_sha256': hashlib.sha256(Path('work/graded_lie.py').read_bytes()).hexdigest(),
            'prerequisites': ['proof.md Sections 3,4,7,8', 'proof.md Section 9 and evidence/symbolic-222/all-cells-independent-check.json'],
            'prior_height6_receipt_sha256': hashlib.sha256(Path('evidence/symbolic-222/all-cells-independent-check.json').read_bytes()).hexdigest()}
    save(args.output / f'input-{run_label}.json', spec)
    started = time.monotonic()
    free = FreeLie(3, max(sum(map(int, degree)) for degree in args.degrees))
    with (args.output / f'execution-{run_label}.jsonl').open('x') as log:
        summaries = [run_degree(tuple(map(int, degree)), free, args, log) for degree in args.degrees]
    save(args.output / f'run-{run_label}.json', {'summaries': summaries, 'elapsed_seconds': round(time.monotonic() - started, 3)})


if __name__ == '__main__':
    main()
