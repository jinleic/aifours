#!/usr/bin/env python3
"""Definition-first parent checker for a circular Florentine rectangle or cyclic difference matrix.
CFR(r,n): r permutations of 0..n-1; each (cyclic displacement d, ordered distinct pair a,b) occurs at most once.
DM(k,n;1) over CYCLIC Z_n: for each row pair, entrywise differences contain every residue exactly once.
No claimant imports. Raw format: exactly r or k numeric lines, n canonical space-separated integers each.
Usage: check_cfr_dm_parent.py cfr|dm FILE ROWS N EXPECTED_SHA256 NEW_RECEIPT.json
"""
from collections import Counter
from datetime import datetime
import hashlib
import json
from pathlib import Path
import re
import sys
from zoneinfo import ZoneInfo


class Invalid(Exception):
    pass


def need(condition, category, detail):
    if not condition:
        raise Invalid(category + ': ' + detail)


def parse(raw, rows, n):
    need(rows >= 1 and n >= 2, 'PARAMS', 'positive row count and n>=2 required')
    need(raw.endswith(b'\n') and b'\r' not in raw, 'FORMAT', 'canonical final LF required; no CR')
    try:
        text = raw.decode('ascii')
    except UnicodeDecodeError:
        raise Invalid('FORMAT: non-ASCII input')
    lines = text.split('\n')[:-1]
    need(len(lines) == rows, 'ROW_COUNT', f'{len(lines)} rows, expected {rows}')
    matrix = []
    for i, line in enumerate(lines):
        need(re.fullmatch(r'(0|[1-9][0-9]*)( (0|[1-9][0-9]*))*', line) is not None,
             'FORMAT', f'line {i+1}: noncanonical integer row')
        row = list(map(int, line.split(' ')))
        need(len(row) == n, 'ROW_WIDTH', f'line {i+1}: {len(row)} entries, expected {n}')
        need(all(0 <= x < n for x in row), 'POINT_RANGE', f'line {i+1}: entry outside 0..{n-1}')
        matrix.append(row)
    return matrix


def cfr(matrix, n):
    r = len(matrix)
    need(r <= n - 1, 'PARAMS', 'more than n-1 rows cannot have distinct pair distances')
    for i, row in enumerate(matrix):
        need(sorted(row) == list(range(n)), 'ROW_PERMUTATION', f'row {i} is not a permutation')
    seen = {}
    for i, row in enumerate(matrix):
        for d in range(1, n):
            for start in range(n):
                a, b = row[start], row[(start + d) % n]
                event = (d, a, b)
                need(event not in seen, 'EVENT_COLLISION',
                     f'd={d}, a={a}, b={b} occurs at row/start {seen.get(event)} and {(i,start)}')
                seen[event] = (i, start)
    need(len(seen) == r * n * (n - 1), 'EVENT_COUNT', 'incomplete event accounting')
    return {'rows': r, 'order': n, 'events_checked': len(seen),
            'events_per_nonzero_displacement': {str(d): sum(e[0] == d for e in seen) for d in range(1, n)},
            'row_permutations': True, 'all_cyclic_ordered_pair_events_distinct': True}


def dm(matrix, n):
    pairs = []
    for i in range(len(matrix)):
        for j in range(i):
            differences = [(matrix[i][c] - matrix[j][c]) % n for c in range(n)]
            counts = Counter(differences)
            need(counts == Counter(range(n)), 'DM_PAIR', f'rows {j},{i}: differences not every Z_{n} residue once')
            pairs.append({'rows': [j, i], 'differences_sorted': sorted(differences)})
    return {'rows': len(matrix), 'order': n, 'group': f'CYCLIC Z_{n}',
            'row_pairs_checked': len(pairs), 'pair_checks': pairs}


def check(kind, path, rows, n, expected_sha):
    raw = Path(path).read_bytes()
    digest = hashlib.sha256(raw).hexdigest()
    need(digest == expected_sha, 'INPUT_SHA256', 'pinned input digest mismatch')
    matrix = parse(raw, rows, n)
    need(kind in ('cfr', 'dm'), 'PARAMS', 'kind must be cfr or dm')
    structure = cfr(matrix, n) if kind == 'cfr' else dm(matrix, n)
    return {'status': 'PASS', 'kind': kind, 'sha256': digest, 'bytes': len(raw), 'structure': structure}


def main():
    if len(sys.argv) != 7:
        raise SystemExit('Usage: cfr|dm FILE ROWS N EXPECTED_SHA256 NEW_RECEIPT.json')
    kind, path, rows, n, expected_sha, out = sys.argv[1:]
    try:
        result = check(kind, path, int(rows), int(n), expected_sha)
        rc = 0
    except (Invalid, OSError) as exc:
        result = {'status': 'FAIL', 'error_type': type(exc).__name__, 'reason': str(exc)}
        rc = 1
    result.update(recorded_at_pt=datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
                  checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), input=str(Path(path).resolve()))
    with Path(out).open('x') as f:
        json.dump(result, f, indent=1)
        f.write('\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'structure'}, indent=1))
    return rc


if __name__ == '__main__':
    sys.exit(main())
