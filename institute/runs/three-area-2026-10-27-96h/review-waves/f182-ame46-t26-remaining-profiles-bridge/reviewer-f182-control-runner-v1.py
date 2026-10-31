#!/usr/bin/env python3
"""Reviewer-authored runner (ReviewF182AME46T26): executes the reviewer control
reviewer-f182-independent-control-v1.py once per predeclared case as separate one-shot
processes (hard 120 s timeout each), records native clocks, exit codes and SHA-256 hashes,
and checks each case against the expectation declared below BEFORE the runs.
A timeout is recorded as UNKNOWN, never as acceptance.  Exclusive-create outputs only.
"""
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

WAVE = Path(__file__).resolve().parent
CONTROL = WAVE / 'reviewer-f182-independent-control-v1.py'
RECEIPT = WAVE / 'reviewer-f182-control-run-receipt-v1.json'
CAP = 120
SIX = ['2,5,5,5', '3,4,4,5', '3,5,5,5', '4,4,4,5', '4,4,5,5', '4,5,5,5']
EIGHT = SIX + ['3,4,5,5', '5,5,5,5']
AUTHOR_ALL = {'author.v1_all_comparable_leaves_match', 'author.v2_all_comparable_leaves_match'}

# Predeclared expectations: (exit code, ids that MUST fail, ids that MAY additionally fail, extra predicate name)
CASES = [
    ('none', 0, set(), set(), None),
    ('rule-le2', 3, {'triples.zero.' + p for p in EIGHT},
     AUTHOR_ALL | {'pairs-hand.3_5', 'pairs-hand.4_5', 'pairs-hand.5_5', 'pairs-hand.2_5'}, None),
    ('drop-pair-23', 3, {'triples.zero.' + p for p in SIX}, AUTHOR_ALL, None),
    ('wrong-expected-family', 3, {'families.size.r4'}, set(), None),
    ('cylinder-fibre', 3, {'M.global_positive_parity_fibres_satisfy_M_exactly'}, set(), 'cylinder_reasons'),
]


def sha(b):
    return hashlib.sha256(b).hexdigest()


def cylinder_reasons(doc):
    for c in doc['checks']:
        if c['id'] == 'M.global_positive_parity_fibres_satisfy_M_exactly':
            reasons = c['detail']['failure_reasons']
            ok_keys = {'M_12,intra_fibre_hamming1', 'M_13,intra_fibre_hamming1', 'M_23,intra_fibre_hamming1'}
            return c['detail']['ok'] == 0 and set(reasons) <= ok_keys and sum(reasons.values()) == 3000
    return False


def main():
    if RECEIPT.exists():
        raise SystemExit('refusing to overwrite ' + str(RECEIPT))
    control_bytes = CONTROL.read_bytes()
    runs = []
    for mutation, exp_exit, must_fail, may_fail, extra in CASES:
        out = WAVE / ('reviewer-f182-control-out-%s-v1.json' % mutation)
        cmd = [sys.executable, '-B', str(CONTROL), '--out', str(out), '--mutation', mutation]
        rec = {'mutation': mutation, 'command': cmd, 'clock_before': time.strftime('%Y-%m-%dT%H:%M:%S%z')}
        t0 = time.monotonic()
        try:
            cp = subprocess.run(cmd, capture_output=True, timeout=CAP, cwd=str(WAVE))
            rec.update({'exit': cp.returncode, 'stdout': cp.stdout.decode(), 'stderr': cp.stderr.decode(),
                        'stdout_sha256': sha(cp.stdout), 'stderr_sha256': sha(cp.stderr), 'timed_out': False})
        except subprocess.TimeoutExpired:
            rec.update({'exit': None, 'timed_out': True})
        rec['elapsed_s'] = round(time.monotonic() - t0, 3)
        rec['clock_after'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
        if rec['timed_out']:
            rec['verdict'] = 'UNKNOWN_CAP'
            runs.append(rec)
            continue
        if out.exists():
            ob = out.read_bytes()
            doc = json.loads(ob)
            failed = set(doc['checks_failed'])
            rec.update({'output': out.name, 'output_sha256': sha(ob), 'output_bytes': len(ob),
                        'output_LF': ob.count(b'\n'), 'checks_total': doc['checks_total'],
                        'checks_failed': sorted(failed), 'control_sha256_in_output': doc['script_sha256']})
            ok = (rec['exit'] == exp_exit and must_fail <= failed and failed <= (must_fail | may_fail)
                  and doc['script_sha256'] == sha(control_bytes))
            if extra == 'cylinder_reasons':
                rec['cylinder_reasons_exact'] = cylinder_reasons(doc)
                ok = ok and rec['cylinder_reasons_exact']
            if mutation == 'drop-pair-23':
                ok = ok and not ({'triples.zero.3,4,5,5', 'triples.zero.5,5,5,5'} & failed)
        else:
            ok = False
            rec['output'] = None
        rec['expected'] = {'exit': exp_exit, 'must_fail': sorted(must_fail), 'may_fail': sorted(may_fail)}
        rec['verdict'] = 'AS_PREDECLARED' if ok else 'NOT_AS_PREDECLARED'
        runs.append(rec)
    receipt = {
        'kind': 'REVIEWER_CONTROL_RUN_RECEIPT', 'wave': 'f182-ame46-t26-remaining-profiles-bridge',
        'reviewer': 'ReviewF182AME46T26', 'runner_sha256': sha(Path(__file__).resolve().read_bytes()),
        'control': CONTROL.name, 'control_sha256': sha(control_bytes), 'cap_seconds_per_run': CAP,
        'python_executable': sys.executable, 'runs': runs,
        'all_as_predeclared': all(r['verdict'] == 'AS_PREDECLARED' for r in runs),
    }
    blob = json.dumps(receipt, indent=1, sort_keys=True) + '\n'
    with RECEIPT.open('x', encoding='utf-8') as fh:
        fh.write(blob)
    print(json.dumps([{k: r.get(k) for k in ('mutation', 'exit', 'elapsed_s', 'verdict', 'checks_failed', 'output_sha256')}
                      for r in runs], indent=1))
    print('all_as_predeclared', receipt['all_as_predeclared'])
    print('receipt_sha256', sha(blob.encode()))
    sys.exit(0 if receipt['all_as_predeclared'] else 1)


if __name__ == '__main__':
    main()
