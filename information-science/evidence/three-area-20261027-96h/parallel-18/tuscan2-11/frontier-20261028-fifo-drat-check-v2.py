#!/usr/bin/env python3
"""Solve a pinned CNF with Kissat and stream its binary DRAT proof through an
owned named FIFO into drat-trim's STANDARD INPUT (-i). No proof bytes are
stored on disk.

v1 passed the FIFO path to drat-trim, which closes and reopens a named proof
file (drat-trim.c lines 1457-1459), so the stream was lost (controls failed).
Here the parent opens the FIFO read end once and hands it to drat-trim as
stdin, and keeps a dummy write end until Kissat has been reaped.

Acceptance (all required): CNF SHA-256 equals the expected pin before and after;
Kissat exits 20 with 's UNSATISFIABLE'; drat-trim exits 0 with 's VERIFIED' and
no 'NOT VERIFIED'/'TIMEOUT'; drat-trim's parsed variable/clause counts equal the
CNF header; solver and checker binary hashes are unchanged. Anything else is
recorded as UNKNOWN or NOT_VERIFIED, never as verified.
Usage: SCRIPT CNF EXPECTED_SHA256 FIFO OUT.json SOLVER_SECONDS CHECK_SECONDS
"""
import fcntl
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

DRAT = Path(__file__).resolve().parent / 'frontier-20261028-drat-trim'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main(argv):
    if len(argv) != 7:
        raise SystemExit('usage: SCRIPT CNF EXPECTED_SHA256 FIFO OUT.json SOLVER_SECONDS CHECK_SECONDS')
    cnf, expected, fifo, out = Path(argv[1]), argv[2], Path(argv[3]), Path(argv[4])
    solver_s, check_s = int(argv[5]), int(argv[6])
    kissat = Path(shutil.which('kissat')).resolve()
    with cnf.open('r', encoding='ascii') as stream:
        header = stream.readline().split()
    record = {'kind': 'fifo_stdin_streamed_drat_check', 'cnf': str(cnf), 'expected_cnf_sha256': expected,
              'runner_sha256': sha(__file__), 'kissat': str(kissat), 'drat_trim': str(DRAT), 'header': header,
              'cnf_sha256_before': sha(cnf), 'kissat_sha256_before': sha(kissat), 'drat_sha256_before': sha(DRAT)}
    if record['cnf_sha256_before'] != expected:
        raise SystemExit('CNF pin mismatch')
    os.mkfifo(fifo, 0o600)
    rfd = os.open(fifo, os.O_RDONLY | os.O_NONBLOCK)
    dummy = os.open(fifo, os.O_WRONLY | os.O_NONBLOCK)
    flags = fcntl.fcntl(rfd, fcntl.F_GETFL)
    fcntl.fcntl(rfd, fcntl.F_SETFL, flags & ~os.O_NONBLOCK)
    t0 = time.monotonic()
    checker = subprocess.Popen([str(DRAT), str(cnf), '-i', '-t', str(check_s)], stdin=rfd,
                               stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    os.close(rfd)
    solver = subprocess.run([str(kissat), f'--time={solver_s}', str(cnf), str(fifo)],
                            capture_output=True, text=True, timeout=solver_s + 120, check=False)
    solve_s = time.monotonic() - t0
    os.close(dummy)
    ctext, _ = checker.communicate(timeout=check_s + 120)
    total_s = time.monotonic() - t0
    m_parse = re.search(r'parsing input formula with (\d+) variables and (\d+) clauses', ctext)
    m_bytes = re.search(r'read (\d+) bytes from proof file', ctext)
    lines = [x.strip() for x in ctext.splitlines()]
    record.update({
        'solver_returncode': solver.returncode,
        'solver_status_line': next((x for x in solver.stdout.splitlines() if x.startswith('s ')), None),
        'solver_proof_lines': [x for x in solver.stdout.splitlines() if 'proof' in x.lower()][:6],
        'solver_stdout_tail': solver.stdout[-1500:], 'solver_seconds': round(solve_s, 3),
        'checker_returncode': checker.returncode, 'checker_output': ctext[-3000:],
        'checker_parsed_variables_clauses': [int(m_parse.group(1)), int(m_parse.group(2))] if m_parse else None,
        'proof_bytes_read': int(m_bytes.group(1)) if m_bytes else None, 'total_seconds': round(total_s, 3),
        'cnf_sha256_after': sha(cnf), 'kissat_sha256_after': sha(kissat), 'drat_sha256_after': sha(DRAT),
        'fifo_node_retained': str(fifo)})
    ok = (record['cnf_sha256_after'] == expected and solver.returncode == 20
          and record['solver_status_line'] == 's UNSATISFIABLE' and checker.returncode == 0
          and 's VERIFIED' in lines and not any('NOT VERIFIED' in x or 'TIMEOUT' in x for x in lines)
          and record['checker_parsed_variables_clauses'] == [int(header[2]), int(header[3])]
          and record['kissat_sha256_after'] == record['kissat_sha256_before']
          and record['drat_sha256_after'] == record['drat_sha256_before'])
    record['verdict'] = 'UNSAT_DRAT_VERIFIED' if ok else ('UNKNOWN' if solver.returncode == 0 else 'NOT_VERIFIED')
    with out.open('x', encoding='utf-8') as stream:
        json.dump(record, stream, indent=2, sort_keys=True)
        stream.write('\n')
    print(json.dumps({k: record[k] for k in ('verdict', 'solver_returncode', 'checker_returncode',
                                              'proof_bytes_read', 'solver_seconds', 'total_seconds')}))


if __name__ == '__main__':
    main(sys.argv)
