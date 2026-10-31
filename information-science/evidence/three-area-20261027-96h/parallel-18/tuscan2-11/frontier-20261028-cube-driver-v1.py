#!/usr/bin/env python3
"""Cube-and-conquer over every normalized second row of a channelled T2(n) CNF.

The pinned base CNF normalizes row 0 = 0..n-1 and row r starts with r. Every
normalized solution has some row 1 starting with 1, avoiding row 0's D1/D2
events and ending differently from n-1. This driver enumerates ALL such row-1
strings in lexicographic order (complete cube list), and for a contiguous
index range adds the row-1 unit clauses (x var = 1+(r*n+c)*n+v) and runs
Kissat on stdin. Records exact per-cube status as JSON lines. UNSAT results
are unverified unless separately proof-checked; UNKNOWN cubes are open.
Usage: SCRIPT N CNF SHA256 OUT.jsonl START COUNT SECONDS WORKERS
"""
import hashlib
import json
import subprocess
import sys
import threading
import time
from pathlib import Path


def row1_candidates(n):
    d1 = {(i, i + 1) for i in range(n - 1)}
    d2 = {(i, i + 2) for i in range(n - 2)}
    out = []

    def rec(p, used):
        if len(p) == n:
            if p[-1] != n - 1:
                out.append(tuple(p))
            return
        for v in range(n):
            if used >> v & 1:
                continue
            if p and (p[-1], v) in d1:
                continue
            if len(p) > 1 and (p[-2], v) in d2:
                continue
            p.append(v)
            rec(p, used | 1 << v)
            p.pop()
    rec([1], 1 << 1)
    return out


def main(argv):
    if len(argv) != 9:
        raise ValueError('usage: SCRIPT N CNF SHA256 OUT.jsonl START COUNT SECONDS WORKERS')
    n = int(argv[1]); cnf = Path(argv[2]); expected = argv[3]; out = Path(argv[4])
    start, count, seconds, workers = map(int, argv[5:9])
    raw = cnf.read_bytes()
    if hashlib.sha256(raw).hexdigest() != expected:
        raise ValueError('base CNF hash mismatch')
    lines = raw.decode().splitlines()
    head = lines[0].split()
    nvars, nclauses = int(head[2]), int(head[3])
    body = '\n'.join(lines[1:]) + '\n'
    cubes = row1_candidates(n)
    cube_digest = hashlib.sha256(json.dumps(cubes).encode()).hexdigest()
    indices = list(range(start, min(len(cubes), start + count)))
    lock = threading.Lock()
    queue = list(indices)
    stop = threading.Event()
    with out.open('x', encoding='utf-8') as stream:
        stream.write(json.dumps({'header': True, 'n': n, 'cnf_sha256': expected, 'total_cubes': len(cubes),
                                 'cube_list_sha256': cube_digest,
                                 'driver_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                                 'start': start, 'count': len(indices), 'seconds': seconds, 'workers': workers}) + '\n')
        stream.flush()

        def worker():
            while not stop.is_set():
                with lock:
                    if not queue:
                        return
                    idx = queue.pop(0)
                row = cubes[idx]
                units = ''.join(f'{1 + (1 * n + c) * n + v} 0\n' for c, v in enumerate(row))
                text = f'p cnf {nvars} {nclauses + n}\n' + body + units
                t0 = time.monotonic()
                proc = subprocess.run(['kissat', '-q', f'--time={seconds}'], input=text, capture_output=True,
                                      text=True, timeout=seconds + 60, check=False)
                rc = proc.returncode
                status = ('sat' if rc == 10 and 's SATISFIABLE' in proc.stdout else
                          'unsat_unverified' if rc == 20 and 's UNSATISFIABLE' in proc.stdout else
                          'unknown' if rc == 0 else 'solver_error')
                record = {'cube': idx, 'row1': row, 'status': status, 'returncode': rc,
                          'elapsed_ms': round((time.monotonic() - t0) * 1000)}
                if status == 'sat':
                    assigned = {int(v) for line in proc.stdout.splitlines() if line.startswith('v ')
                                for v in line.split()[1:] if int(v) > 0}
                    rows = [[next(v for v in range(n) if 1 + (r * n + c) * n + v in assigned) for c in range(n)]
                            for r in range(n)]
                    d1 = [(x[i], x[i + 1]) for x in rows for i in range(n - 1)]
                    d2 = [(x[i], x[i + 2]) for x in rows for i in range(n - 2)]
                    record['rows'] = rows
                    record['internal_check_ok'] = (all(sorted(x) == list(range(n)) for x in rows)
                                                   and len(set(d1)) == len(d1) and len(set(d2)) == len(d2))
                with lock:
                    stream.write(json.dumps(record) + '\n')
                    stream.flush()

        threads = [threading.Thread(target=worker) for _ in range(workers)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()
    print(json.dumps({'n': n, 'total_cubes': len(cubes), 'ran': len(indices), 'output': str(out)}))


if __name__ == '__main__':
    main(sys.argv)
