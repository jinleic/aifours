"""Replay the pinned gcDCQS producer from recorded KM rows and retained SAT models.
No solver calls: regenerate each colouring CNF, independently check every clause against the retained
assignment, decode/transport all 80 colourings, compare the complete certificate bytes and run the parent checker.
Source packages and outputs are immutable/exclusive-create. The worker separately reran actual solver searches.
Usage: python3 -B gcdcqs20_parent_producer_replay.py
"""
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import subprocess
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
PIN = HERE / 'gcdcqs20-parent-producer-inputs-v1'
CERTS = HERE / 'gcdcqs20-parent-inputs-v1'
OUT = HERE / 'gcdcqs20-parent-producer-replay-v1'
PY = '/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/depolarizing/env/bin/python'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def check_assignment(cnf, log):
    values = {}
    sat_line = False
    for line in Path(log).read_text().split('\n'):
        if line == 's SATISFIABLE':
            sat_line = True
        if line.startswith('v '):
            for token in line.split()[1:]:
                literal = int(token)
                if literal:
                    var, value = abs(literal), literal > 0
                    if var in values and values[var] != value:
                        raise ValueError('contradictory assignment')
                    values[var] = value
    nv = nc = None
    pending, seen = [], 0
    for line in Path(cnf).read_text().split('\n'):
        if not line or line.startswith('c'):
            continue
        if line.startswith('p '):
            _, kind, nvs, ncs = line.split()
            if kind != 'cnf' or nv is not None:
                raise ValueError('bad DIMACS header')
            nv, nc = int(nvs), int(ncs)
            continue
        for token in line.split():
            literal = int(token)
            if literal:
                if nv is None or not 1 <= abs(literal) <= nv:
                    raise ValueError('literal outside header range')
                pending.append(literal)
            else:
                seen += 1
                if not any(values.get(abs(x)) == (x > 0) for x in pending):
                    raise ValueError('unsatisfied or unassigned clause ' + str(seen))
                pending = []
    if not sat_line or pending or seen != nc or set(values) != set(range(1, nv + 1)):
        raise ValueError('incomplete assignment or clause accounting')
    return {'variables': nv, 'assigned_variables': len(values), 'clauses': seen, 'all_clauses_satisfied': True}


def main():
    OUT.mkdir(exist_ok=False)
    env = dict(os.environ, OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1', MKL_NUM_THREADS='1', VECLIB_MAXIMUM_THREADS='1', PYTHONDONTWRITEBYTECODE='1')
    results = []
    for tag, sample in [('e1s1', 1), ('e1s0', 0)]:
        dest = OUT / tag
        command = [PY, '-B', str(PIN / 'code/pipeline2.py'), str(dest), '--group', 'A4xC', '--g', '20', '--res', 'C3',
                   '--avoid', 'R;1;1;1', '--samples', '1', '--workers', '1', '--rows-from', str(PIN / 'original-km-summary.json') + ':' + str(sample),
                   '--strengthen', '--profile', 'P10', '--stop-on-first', '--model-from', str(PIN / (tag + '-kissat.log'))]
        proc = subprocess.run(command, env=env, cwd=OUT, capture_output=True, text=True)
        with (OUT / (tag + '.stdout.txt')).open('x') as f:
            f.write(proc.stdout)
        with (OUT / (tag + '.stderr.txt')).open('x') as f:
            f.write(proc.stderr)
        if proc.returncode:
            raise RuntimeError(tag + ' producer failed: ' + proc.stderr[-1000:])
        rebuilt_cnf = dest / 'col_0_r0_a0.cnf'
        if sha(rebuilt_cnf) != sha(PIN / (tag + '-colour.cnf')):
            raise ValueError('regenerated CNF differs from recorded original')
        assignment = check_assignment(rebuilt_cnf, PIN / (tag + '-kissat.log'))
        cert = dest / 'gcdcqs20_s0.txt'
        original = CERTS / ('gcdcqs20-' + tag + '_p10.txt')
        if sha(cert) != sha(original):
            raise ValueError('regenerated certificate differs from pinned candidate')
        receipt = OUT / (tag + '-parent-check.json')
        chk = subprocess.run(['/usr/bin/python3', '-B', str(HERE / 'check_gcdcqs_parent.py'), str(cert), '80', '4', '20', sha(original), str(receipt)], capture_output=True, text=True)
        if chk.returncode:
            raise ValueError('regenerated certificate fails parent checker')
        results.append({'tag': tag, 'source_KM_sample': sample, 'command': command, 'exit': proc.returncode, 'cnf_sha256': sha(rebuilt_cnf),
                        'model_sha256': sha(PIN / (tag + '-kissat.log')), 'assignment_check': assignment, 'certificate_sha256': sha(cert),
                        'pinned_certificate_sha256': sha(original), 'parent_checker_exit': chk.returncode, 'parent_checker_receipt_sha256': sha(receipt)})
    report = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(timespec='seconds'), 'status': 'PASS',
              'script_sha256': sha(__file__), 'results': results,
              'scope': 'Parent regenerates exact colouring CNFs and certificates, checking every SAT clause independently. Actual solver reruns are the worker\'s separate recorded replays, not parent executions.',
              'header_provenance': 'Both historical certificate comments say KM sample0 because pipeline2 loops once over supplied rows. args.rows_from binds original KM samples1 and0 respectively; pinned comments are retained unchanged.'}
    with (OUT / 'parent-result.json').open('x') as f:
        json.dump(report, f, indent=2)
        f.write('\n')
    print(json.dumps({'status': report['status'], 'results': results}, indent=1))


if __name__ == '__main__':
    main()
