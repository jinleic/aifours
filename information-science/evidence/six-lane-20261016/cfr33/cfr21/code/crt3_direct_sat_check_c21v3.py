#!/usr/bin/env python3
"""Versioned direct-CNF verifier using CaDiCaL for ONLY unresolved proof cases.
Production formula unchanged from v2; CNF SHA must match the retained original.
No cap is raised. No import/reuse of the Gaussian-elimination solver.

Usage:
  crt3_direct_sat_check_c21v3.py calibrate OUTDIR
  crt3_direct_sat_check_c21v3.py retry REQUEST.json SECONDS OUTDIR
Common family is independently reconstructed from (u1,v1,u2,v2) in lexicographic F7^4:
 beta_i(0,c)=i*c; beta_i(t,c)=i*c+u_t*(i^2-i)+v_t*(i^3-i) mod7.
Every alpha_i(c) in F3 has one-hot variables; row0 and column0 are zero gauges.
Every pair difference has one-hot variables linked to alpha_i-alpha_j, and for
the three columns of each beta residue every difference value occurs exactly
once. No sum equations, nullspace bases, projected inequalities or symmetry
reductions from the primary solver are used.
UNSAT requires a pinned DRAT checker with exact s VERIFIED; SAT is reconstructed
by CRT and checked directly on all row pairs. Native per-case solver/checker
limits, SIGTERM forwarding,8MiB child file-size cap, global deadline and disk
floor apply. Every case directory/file is new/exclusive; proofs are retained.
"""
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import resource
import shutil
import signal
import subprocess
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

LANE = Path(__file__).resolve().parents[1]
STOP = False
CHILD = None
FLOOR = 12_000_000_000
FILECAP = 8 * 1024 * 1024
DATACAP = 3 * 1024 ** 3


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def on_term(signum, frame):
    global STOP
    STOP = True
    if CHILD is not None:
        try:
            CHILD.send_signal(signal.SIGTERM)
        except ProcessLookupError:
            pass


def free_bytes():
    st = os.statvfs(LANE)
    return st.f_bavail * st.f_frsize


def child_limits():
    resource.setrlimit(resource.RLIMIT_FSIZE, (FILECAP, FILECAP))


def execute(cmd, out):
    global CHILD
    if free_bytes() < FLOOR + 64 * 1024 ** 2:
        raise RuntimeError('shared disk floor margin reached')
    begin = time.monotonic()
    with open(out, 'xb') as f:
        CHILD = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT, preexec_fn=child_limits)
        rc = CHILD.wait()
        CHILD = None
    return {'command': cmd, 'rc': rc, 'wall_s': time.monotonic() - begin, 'stdout_sha256': sha(out)}


def encode(q, beta, path, planted_alpha=None):
    n, k = 3 * q, len(beta)
    if q < 1 or math.gcd(q, 3) != 1 or k < 2:
        raise ValueError('bad q/k')
    if any(len(row) != n or any(type(v) is not int or not 0 <= v < q for v in row) for row in beta):
        raise ValueError('bad beta dimensions/residues')
    norm = [[(beta[i][c] - beta[0][c]) % q for c in range(n)] for i in range(k)]
    grouped = []
    for i in range(k):
        for j in range(i):
            by = [[] for _ in range(q)]
            for c in range(n):
                by[(norm[i][c] - norm[j][c]) % q].append(c)
            if any(len(x) != 3 for x in by):
                raise ValueError('beta pair multiplicity is not3')
            grouped.append((i, j, by))
    avars, dvars = {}, {}
    nv = 0
    for i in range(1, k):
        for c in range(1, n):
            for u in range(3):
                nv += 1
                avars[i, c, u] = nv
    for i in range(1, k):
        for j in range(1, i):
            for c in range(1, n):
                for d in range(3):
                    nv += 1
                    dvars[i, j, c, d] = nv
    clauses = set()

    def A(i, c, u):
        return (u == 0) if i == 0 or c == 0 else avars[i, c, u]

    def D(i, j, c, d):
        if c == 0:
            return d == 0
        if j == 0:
            return A(i, c, d)
        return dvars[i, j, c, d]

    def neg(v):
        return not v if type(v) is bool else -v

    def add(vs):
        if any(type(v) is bool and v for v in vs):
            return
        vs = {v for v in vs if type(v) is not bool}
        if any(-v in vs for v in vs):
            return
        clauses.add(tuple(sorted(vs, key=lambda x: (abs(x), x))))

    def one(vs):
        add(vs)
        for a in range(len(vs)):
            for b in range(a):
                add([neg(vs[a]), neg(vs[b])])

    for i in range(1, k):
        for c in range(1, n):
            one([A(i, c, u) for u in range(3)])
    for i in range(1, k):
        for j in range(1, i):
            for c in range(1, n):
                one([D(i, j, c, d) for d in range(3)])
                for u in range(3):
                    for v in range(3):
                        add([neg(A(i, c, u)), neg(A(j, c, v)), D(i, j, c, (u - v) % 3)])
    for i, j, by in grouped:
        for cols in by:
            for d in range(3):
                one([D(i, j, c, d) for c in cols])
    if planted_alpha is not None:
        if len(planted_alpha) != k or any(len(row) != n or any(v not in (0, 1, 2) for v in row) for row in planted_alpha):
            raise ValueError('bad planted alpha')
        if any(planted_alpha[0]) or any(row[0] for row in planted_alpha):
            raise ValueError('planted alpha violates gauges')
        for i in range(1, k):
            for c in range(1, n):
                add([A(i, c, planted_alpha[i][c])])
    text = 'p cnf %d %d\n' % (nv, len(clauses))
    text += ''.join(' '.join(map(str, clause)) + (' ' if clause else '') + '0\n' for clause in sorted(clauses))
    with open(path, 'x') as f:
        f.write(text)
    return {'n': n, 'k': k, 'q': q, 'variables': nv, 'clauses': len(clauses), 'cnf_sha256': sha(path)}, avars, norm


def decode_alpha(stdout, avars, k, n):
    true = set()
    for line in Path(stdout).read_text().splitlines():
        if line.startswith('v '):
            true.update(int(t) for t in line.split()[1:] if int(t) > 0)
    alpha = [[0] * n for _ in range(k)]
    for i in range(1, k):
        for c in range(1, n):
            values = [u for u in range(3) if avars[i, c, u] in true]
            if len(values) != 1:
                raise AssertionError('one-hot alpha decode failed')
            alpha[i][c] = values[0]
    return alpha


def dm_from_alpha(q, norm, alpha):
    n, k = 3 * q, len(norm)
    cbeta = 3 * pow(3, -1, q) if q > 1 else 0
    calpha = q * pow(q, -1, 3)
    dm = [[(cbeta * b + calpha * a) % n for b, a in zip(row, ar)] for row, ar in zip(norm, alpha)]
    for i in range(k):
        for j in range(i):
            if len({(dm[i][c] - dm[j][c]) % n for c in range(n)}) != n:
                raise AssertionError('SAT model fails direct DM definition')
    return dm


def run_case(q, beta, outdir, seconds, solver, checker, planted_alpha=None, expected_cnf_sha=None):
    os.mkdir(outdir)
    start = time.monotonic()
    cnf = outdir + '/model.cnf'
    proof = outdir + '/proof.drat'
    rec, avars, norm = encode(q, beta, cnf, planted_alpha)
    rec['planted_control'] = planted_alpha is not None
    if expected_cnf_sha is not None and rec['cnf_sha256'] != expected_cnf_sha:
        raise AssertionError('retry CNF differs from the retained original')
    secs = max(1, int(seconds))
    cmd = [solver, '--seed=1', '-t', str(secs), cnf, proof]
    solver_out = outdir + '/solver.out'
    run = execute(cmd, solver_out)
    rec['solver'] = run
    lines = [l.strip() for l in Path(solver_out).read_text().splitlines()]
    if run['rc'] == 10 and 's SATISFIABLE' in lines:
        alpha = decode_alpha(solver_out, avars, rec['k'], rec['n'])
        dm = dm_from_alpha(q, norm, alpha)
        text = ''.join(' '.join(map(str, r)) + '\n' for r in dm)
        with open(outdir + '/candidate.dmraw', 'x') as f:
            f.write(text)
        rec.update(status='SAT-DIRECT-DM-VERIFIED', dmraw_sha256=sha(outdir + '/candidate.dmraw'))
    elif run['rc'] == 20 and 's UNSATISFIABLE' in lines and not STOP:
        check = execute([checker, cnf, proof, '-t', str(secs)], outdir + '/checker.out')
        rec['checker'] = check
        check_lines = [l.strip() for l in Path(outdir + '/checker.out').read_text().splitlines()]
        rec['status'] = 'DRAT-VERIFIED-UNSAT' if check['rc'] == 0 and 's VERIFIED' in check_lines else 'UNKNOWN-PROOF-CHECK-FAILED'
    else:
        rec['status'] = 'UNKNOWN-NATIVE-LIMIT-OR-SIGNAL'
    rec.update(clock=stamp(), wall_s=time.monotonic() - start)
    if os.path.exists(proof):
        rec.update(proof_sha256=sha(proof), proof_bytes=os.stat(proof).st_size)
    with open(outdir + '/receipt.json', 'x') as f:
        json.dump(rec, f, indent=1)
    return rec


def get_tools():
    solver = shutil.which('cadical')
    checker = str(LANE / 'bin/drat-trim_c21v1')
    if not solver or not Path(checker).is_file():
        raise RuntimeError('pinned native tools missing')
    return solver, checker


def calibrate(out):
    os.mkdir(out)
    solver, checker = get_tools()
    p21 = LANE.parent / 'cfr27/controls/dm-orbit-v1/P21-mu1-5cycle.dmraw'
    dm21 = [[int(t) for t in line.split()] for line in p21.read_text().splitlines()]
    rec21 = run_case(7, [[v % 7 for v in row] for row in dm21], out + '/sage21k6', 30, solver, checker)
    if rec21['status'] != 'SAT-DIRECT-DM-VERIFIED':
        raise AssertionError('new prover positive21 control failed')
    receipts = [{'name': 'sage21k6', 'source_sha256': sha(p21), 'receipt': rec21}]
    p = LANE.parent / 'prior-art/sage-dm-33-6-1.dmraw'
    dm = [[int(t) for t in line.split()] for line in p.read_text().splitlines()]
    q, n = 11, 33
    beta = [[x % q for x in row] for row in dm]
    shifted = [[(dm[i][c] - dm[0][c]) % 3 for c in range(n)] for i in range(len(dm))]
    known_alpha = [[(v - row[0]) % 3 for v in row] for row in shifted]
    rec = run_case(q, beta, out + '/sage33k6-planted', 30, solver, checker, known_alpha)
    if rec['status'] != 'SAT-DIRECT-DM-VERIFIED':
        raise AssertionError('planted positive CRT control failed')
    receipts.append({'name': 'sage33k6-planted', 'source_sha256': sha(p), 'receipt': rec})
    neg = run_case(1, [[0] * 3 for _ in range(4)], out + '/z3k4', 30, solver, checker)
    if neg['status'] != 'DRAT-VERIFIED-UNSAT':
        raise AssertionError('known negative failed')
    # Checker-specific negative control on the SAT21 CNF, separate from solver controls.
    empty = out + '/invalid-empty.drat'
    with open(empty, 'x') as f:
        f.write('0\n')
    control = execute([checker, out + '/sage21k6/model.cnf', empty, '-t', '10'], out + '/sat-empty-control.out')
    ctrl_lines = [l.strip() for l in Path(out + '/sat-empty-control.out').read_text().splitlines()]
    if control['rc'] == 0 or 's NOT VERIFIED' not in ctrl_lines:
        raise AssertionError('invalid proof accepted on SAT control')
    summary = {'clock': stamp(), 'all_as_expected': True, 'positives': receipts, 'negative': neg,
               'checker_sat_empty_control': control, 'solver_sha256': sha(solver), 'checker_sha256': sha(checker),
               'source_sha256': sha(__file__)}
    with open(out + '/controls.json', 'x') as f:
        json.dump(summary, f, indent=1)
    print('DIRECT CRT CNF CALIBRATION PASS', flush=True)


def retry(indices_path, seconds, out):
    request = json.loads(Path(indices_path).read_text())
    indices = request['indices']
    expected = {row['index']: row['cnf_sha256'] for row in request['origins']}
    if indices != sorted(set(indices)) or any(type(i) is not int or not 0 <= i < 2401 for i in indices):
        raise ValueError('invalid retry index list')
    if set(expected) != set(indices) or len(request['origins']) != len(indices):
        raise ValueError('every retry needs exactly one original CNF hash')
    os.mkdir(out)
    solver, checker = get_tools()
    begin = last = time.monotonic()
    meta = {'clock': stamp(), 'requested_indices': indices, 'seconds': seconds,
            'request_path': indices_path, 'request_sha256': sha(indices_path),
            'solver_sha256': sha(solver), 'checker_sha256': sha(checker), 'source_sha256': sha(__file__)}
    with open(out + '/start.json', 'x') as f:
        json.dump(meta, f, indent=1)
    choices = list(itertools.product(range(7), repeat=4))
    done, certified, unknown, used_bytes = 0, 0, [], 0
    attempted = []
    candidate = False
    with open(out + '/cases.jsonl', 'x') as log:
        for index in indices:
            remaining = seconds - (time.monotonic() - begin)
            if STOP or remaining < 2 or used_bytes > DATACAP or free_bytes() < FLOOR + 64 * 1024 ** 2:
                break
            u1, v1, u2, v2 = choices[index]
            beta = []
            for row in range(7):
                line = []
                for block in range(3):
                    u, v = (0, 0) if block == 0 else (u1, v1) if block == 1 else (u2, v2)
                    offset = (u * (row ** 2 - row) + v * (row ** 3 - row)) % 7
                    line.extend((row * c + offset) % 7 for c in range(7))
                beta.append(line)
            case = out + '/case-%04d' % index
            rec = run_case(7, beta, case, min(20, int(remaining / 2)), solver, checker,
                           expected_cnf_sha=expected[index])
            rec.update(index=index, coefficients=[u1, v1, u2, v2])
            log.write(json.dumps(rec) + '\n')
            log.flush()
            done += 1
            attempted.append(index)
            used_bytes += sum(p.stat().st_size for p in Path(case).iterdir() if p.is_file())
            if rec['status'] == 'DRAT-VERIFIED-UNSAT':
                certified += 1
            elif rec['status'] == 'SAT-DIRECT-DM-VERIFIED':
                candidate = True
                with open(out + '/candidate.json', 'x') as f:
                    json.dump({'case': index, 'path': case, 'receipt': rec}, f, indent=1)
                break
            else:
                unknown.append(index)
            if time.monotonic() - last > 30:
                print(json.dumps({'clock': stamp(), 'done': done, 'certified': certified,
                                  'unknown': len(unknown), 'data_bytes': used_bytes}), flush=True)
                last = time.monotonic()
    status = ('CANDIDATE' if candidate else 'RETRY-SUBSET-CERTIFIED-UNSAT'
              if done == len(indices) and not unknown else 'UNKNOWN-INCOMPLETE')
    rec = {**meta, 'end_clock': stamp(), 'wall_s': time.monotonic() - begin, 'done': done, 'certified': certified,
           'attempted_indices': attempted, 'unknown_indices': unknown, 'last_index': attempted[-1] if attempted else None,
           'new_data_bytes': used_bytes, 'status': status, 'signal': STOP}
    with open(out + '/record.json', 'x') as f:
        json.dump(rec, f, indent=1)
    print(json.dumps(rec), flush=True)
    raise SystemExit(10 if candidate else 0)


def main():
    signal.signal(signal.SIGTERM, on_term)
    signal.signal(signal.SIGINT, on_term)
    if sys.argv[1] == 'calibrate':
        calibrate(sys.argv[2])
    elif sys.argv[1] == 'retry':
        retry(sys.argv[2], float(sys.argv[3]), sys.argv[4])
    else:
        raise SystemExit('expected calibrate or retry')


if __name__ == '__main__':
    main()
