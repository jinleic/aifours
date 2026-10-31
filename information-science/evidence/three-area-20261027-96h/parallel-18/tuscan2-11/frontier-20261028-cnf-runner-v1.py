#!/usr/bin/env python3
"""Run one bounded solver configuration on a pinned channelled Tuscan-2 CNF.

The channelled encoder allocates x[r][c][v] first: var = 1+(r*n+c)*n+v.
A SAT model is decoded from those variables and directly checked here; an
independent checker must still verify any claimed witness. UNKNOWN proves
nothing; UNSAT remains unverified without a checked proof.
Usage: SCRIPT N CNF EXPECTED_SHA256 OUT.json SOLVER SECONDS SEED [EXTRA_OPTION ...]
"""
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path


def main(argv):
    if len(argv) < 8:
        raise ValueError('usage: SCRIPT N CNF EXPECTED_SHA256 OUT.json SOLVER SECONDS SEED [EXTRA ...]')
    n = int(argv[1]); cnf = Path(argv[2]); expected = argv[3]; out = Path(argv[4])
    solver = argv[5]; seconds = int(argv[6]); seed = int(argv[7]); extra = argv[8:]
    if solver not in ('kissat', 'cadical') or not 1 <= seconds <= 172800:
        raise ValueError('invalid solver or limit')
    digest = hashlib.sha256(cnf.read_bytes()).hexdigest()
    if digest != expected:
        raise ValueError('CNF hash differs from pinned input')
    if solver == 'kissat':
        command = ['kissat', f'--time={seconds}', f'--seed={seed}', *extra, str(cnf)]
    else:
        command = ['cadical', '-t', str(seconds), f'--seed={seed}', *extra, str(cnf)]
    with out.open('x', encoding='utf-8') as stream:
        start = time.monotonic()
        try:
            proc = subprocess.run(command, capture_output=True, text=True, timeout=seconds + 60, check=False)
            rc, so, se, sup = proc.returncode, proc.stdout, proc.stderr, False
        except subprocess.TimeoutExpired as exc:
            rc = None
            so = exc.stdout.decode() if isinstance(exc.stdout, bytes) else (exc.stdout or '')
            se = exc.stderr.decode() if isinstance(exc.stderr, bytes) else (exc.stderr or '')
            sup = True
        status = ('sat' if rc == 10 and 's SATISFIABLE' in so else
                  'unsat_unverified' if rc == 20 and 's UNSATISFIABLE' in so else
                  'unknown' if rc in (0, None) else 'solver_error')
        result = {'kind': 'pinned_channelled_tuscan2_cnf_run', 'n': n, 'cnf': str(cnf), 'cnf_sha256': digest,
                  'runner_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  'command': command, 'returncode': rc, 'status': status, 'supervisory_timeout': sup,
                  'elapsed_ms': round((time.monotonic() - start) * 1000),
                  'solver_stdout_tail': so[-4000:], 'solver_stderr_tail': se[-2000:],
                  'scope': 'Bounded run; UNKNOWN is not nonexistence; UNSAT unverified without checked proof.'}
        if status == 'sat':
            assigned = {int(v) for line in so.splitlines() if line.startswith('v ')
                        for v in line.split()[1:] if int(v) > 0}
            rows = []
            for r in range(n):
                row = []
                for c in range(n):
                    vals = [v for v in range(n) if 1 + (r * n + c) * n + v in assigned]
                    if len(vals) != 1:
                        raise AssertionError('model does not decode uniquely')
                    row.append(vals[0])
                rows.append(row)
            perms = all(sorted(r) == list(range(n)) for r in rows)
            d1 = [(r[i], r[i + 1]) for r in rows for i in range(n - 1)]
            d2 = [(r[i], r[i + 2]) for r in rows for i in range(n - 2)]
            ok = perms and len(set(d1)) == len(d1) and len(set(d2)) == len(d2)
            result.update({'rows': rows, 'internal_check_ok': ok, 'zero_score_claim': ok,
                           'best_pair_collision_score': 0 if ok else None,
                           'd1_pair_collisions': 0 if ok else None, 'd2_pair_collisions': 0 if ok else None,
                           'd1_excess_events': 0 if ok else None, 'd2_excess_events': 0 if ok else None})
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({k: result.get(k) for k in ('n', 'status', 'returncode', 'elapsed_ms', 'internal_check_ok', 'rows')}))


if __name__ == '__main__':
    main(sys.argv)
