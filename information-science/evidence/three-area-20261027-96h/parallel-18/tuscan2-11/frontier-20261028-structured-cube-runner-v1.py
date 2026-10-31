#!/usr/bin/env python3
"""Cube-and-conquer sampler for a pinned partial-symmetry T2(11) CNF (v2 layout).

Cubes fix positions 1..DEPTH of row 0 (the first block's base row, whose first
symbol is already fixed by the CNF) to every sequence of distinct symbols
different from that first symbol; the union of all cubes covers every model.
X variables are 1 + (r*11 + c)*11 + v (allocated first by the v2 encoder).
Each selected cube is solved by Kissat on stdin under a time limit; SAT models
are decoded and checked for 110 distinct D1 and 99 distinct D2 events. UNSAT is
unverified unless separately proof-checked; UNKNOWN cubes stay open.
Usage: SCRIPT CNF SHA256 FIRST_SYMBOL DEPTH OUT.jsonl START COUNT SECONDS WORKERS
"""
import hashlib
import itertools
import json
import subprocess
import sys
import threading
import time
from pathlib import Path

N = 11


def xvar(r, c, v):
    return 1 + (r * N + c) * N + v


def main(argv):
    if len(argv) != 10:
        raise SystemExit('usage: SCRIPT CNF SHA256 FIRST_SYMBOL DEPTH OUT.jsonl START COUNT SECONDS WORKERS')
    cnf, expected = Path(argv[1]), argv[2]
    first, depth = int(argv[3]), int(argv[4])
    out = Path(argv[5])
    start, count, seconds, workers = map(int, argv[6:10])
    raw = cnf.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise SystemExit('CNF hash mismatch')
    lines = raw.decode().splitlines()
    nvars, nclauses = int(lines[0].split()[2]), int(lines[0].split()[3])
    body = '\n'.join(lines[1:]) + '\n'
    others = [v for v in range(N) if v != first]
    cubes = [list(p) for p in itertools.permutations(others, depth)]
    digest = hashlib.sha256(json.dumps(cubes).encode()).hexdigest()
    queue = list(range(start, min(len(cubes), start + count)))
    lock = threading.Lock()
    with out.open('x', encoding='utf-8') as stream:
        stream.write(json.dumps({'header': True, 'cnf_sha256': expected, 'first_symbol': first, 'depth': depth,
                                 'total_cubes': len(cubes), 'cube_list_sha256': digest,
                                 'runner_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                                 'start': start, 'count': count, 'seconds': seconds, 'workers': workers}) + '\n')
        stream.flush()

        def work():
            while True:
                with lock:
                    if not queue:
                        return
                    idx = queue.pop(0)
                cube = cubes[idx]
                units = ''.join(f'{xvar(0, c + 1, v)} 0\n' for c, v in enumerate(cube))
                text = f'p cnf {nvars} {nclauses + depth}\n' + body + units
                t0 = time.monotonic()
                proc = subprocess.run(['kissat', f'--time={seconds}'], input=text, capture_output=True,
                                      text=True, timeout=seconds + 120, check=False)
                rc, so = proc.returncode, proc.stdout
                status = ('sat' if rc == 10 else 'unsat_unverified' if rc == 20 else
                          'unknown' if rc == 0 else 'solver_error')
                rec = {'cube': idx, 'row0_prefix': [first] + cube, 'status': status, 'returncode': rc,
                       'elapsed_ms': round((time.monotonic() - t0) * 1000)}
                if status == 'sat':
                    assigned = {int(v) for ln in so.splitlines() if ln.startswith('v ')
                                for v in ln.split()[1:] if int(v) > 0}
                    rows = [[next(v for v in range(N) if xvar(r, c, v) in assigned) for c in range(N)]
                            for r in range(N)]
                    d1 = {(x[i], x[i + 1]) for x in rows for i in range(N - 1)}
                    d2 = {(x[i], x[i + 2]) for x in rows for i in range(N - 2)}
                    rec.update({'rows': rows, 'internal_check_ok': all(sorted(x) == list(range(N)) for x in rows)
                                and len(d1) == 110 and len(d2) == 99})
                with lock:
                    stream.write(json.dumps(rec) + '\n')
                    stream.flush()

        threads = [threading.Thread(target=work) for _ in range(workers)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    print(json.dumps({'total_cubes': len(cubes), 'ran': min(count, max(0, len(cubes) - start)), 'output': str(out)}))


if __name__ == '__main__':
    main(sys.argv)
