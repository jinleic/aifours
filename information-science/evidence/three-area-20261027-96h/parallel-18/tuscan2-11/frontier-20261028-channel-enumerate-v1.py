#!/usr/bin/env python3
"""Enumerate all models of a pinned channelled Tuscan-2 CNF by blocking.

Each model is decoded from x[r][c][v] (var=1+(r*n+c)*n+v), checked directly,
and blocked by the clause excluding its exact array. The CNF plus blocking
clauses is streamed to Kissat on stdin (no extra files). The final UNSAT call
is unverified unless separately proof-checked; any timeout is UNKNOWN.
Usage: SCRIPT N CNF SHA256 OUT.json SECONDS_PER_CALL MAX_SOLUTIONS
"""
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path


def main(argv):
    if len(argv) != 7:
        raise ValueError('usage: SCRIPT N CNF SHA256 OUT.json SECONDS_PER_CALL MAX_SOLUTIONS')
    n = int(argv[1]); cnf = Path(argv[2]); expected = argv[3]; out = Path(argv[4])
    seconds, cap = int(argv[5]), int(argv[6])
    raw = cnf.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('CNF hash mismatch')
    lines = raw.decode().splitlines()
    header = lines[0].split()
    if header[:2] != ['p', 'cnf']:
        raise ValueError('bad header')
    nvars, nclauses = int(header[2]), int(header[3])
    body = '\n'.join(lines[1:]) + '\n'
    blocks, solutions, calls = [], [], []
    status = 'max_solutions'
    with out.open('x', encoding='utf-8') as stream:
        start = time.monotonic()
        while len(solutions) < cap:
            text = f'p cnf {nvars} {nclauses + len(blocks)}\n' + body + ''.join(' '.join(map(str, b)) + ' 0\n' for b in blocks)
            t0 = time.monotonic()
            proc = subprocess.run(['kissat', f'--time={seconds}', '-q'], input=text, capture_output=True,
                                  text=True, timeout=seconds + 60, check=False)
            calls.append({'call': len(calls) + 1, 'returncode': proc.returncode,
                          'elapsed_ms': round((time.monotonic() - t0) * 1000)})
            if proc.returncode == 20 and 's UNSATISFIABLE' in proc.stdout:
                status = 'exhausted_unsat_unverified'
                break
            if proc.returncode != 10 or 's SATISFIABLE' not in proc.stdout:
                status = 'unknown_or_error'
                break
            assigned = {int(v) for line in proc.stdout.splitlines() if line.startswith('v ')
                        for v in line.split()[1:] if int(v) > 0}
            rows = []
            for r in range(n):
                row = []
                for c in range(n):
                    vals = [v for v in range(n) if 1 + (r * n + c) * n + v in assigned]
                    if len(vals) != 1:
                        raise AssertionError('model decode failed')
                    row.append(vals[0])
                rows.append(row)
            d1 = [(r[i], r[i + 1]) for r in rows for i in range(n - 1)]
            d2 = [(r[i], r[i + 2]) for r in rows for i in range(n - 2)]
            if not (all(sorted(r) == list(range(n)) for r in rows) and len(set(d1)) == len(d1) and len(set(d2)) == len(d2)):
                raise AssertionError('decoded model is not a Tuscan-2 square')
            if rows in solutions:
                raise AssertionError('blocking failed: duplicate solution')
            solutions.append(rows)
            blocks.append([-(1 + (r * n + c) * n + rows[r][c]) for r in range(1, n) for c in range(1, n)])
        result = {'kind': 'channelled_tuscan2_model_enumeration', 'n': n, 'cnf': str(cnf), 'cnf_sha256': expected,
                  'enumerator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'status': status, 'solutions_found': len(solutions), 'solutions': solutions, 'calls': calls,
                  'elapsed_ms': round((time.monotonic() - start) * 1000),
                  'scope': 'Count of normalized models of this exact CNF; final UNSAT unverified; timeout UNKNOWN.'}
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({k: result[k] for k in ('n', 'status', 'solutions_found', 'elapsed_ms')}))


if __name__ == '__main__':
    main(sys.argv)
