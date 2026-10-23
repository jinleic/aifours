#!/usr/bin/env python3
"""Check final delivery consistency and the remaining small claim commands.

This does not re-prove arithmetic outside the recorded subsets. It checks that
the named finite replay results are complete and successful, that packaging
checks and negative controls passed, and that the final claim scopes agree.
"""
import hashlib
import json
from pathlib import Path
import shlex
import subprocess
import sys
import time

from check import schema_validate


def load(path):
    return json.loads(Path(path).read_text())


def main():
    claims = load('claims.json')
    schema_validate(claims, load('claims.schema.json'))
    assert claims['outcome'] == 'partial'
    assert len({c['cid'] for c in claims['claims']}) == len(claims['claims'])
    assert all(c['scope'] != 'headline' for c in claims['claims'])
    for c in claims['claims']:
        for filename in c['evidence']:
            assert Path(filename).is_file(), 'missing evidence '+filename
        for field in ('verify_command', 'check_command', 'control_command'):
            if c[field]:
                tokens = shlex.split(c[field])
                assert tokens[0] == 'python3' and '--all' not in tokens
    result = load('evidence/recovery-result.json')
    assert result['phase'] == 'complete' and result['headline_resolved'] is False
    assert result['independent_exhaustive_main_range'] is False
    assert result['main_end'] == 10341223092224
    assert result['fresh_exact_prefix_end'] == 202400000000
    assert [r['chunk'] for r in result['fresh_exact_prefix_chunks']] == list(range(10))
    assert result['rechecked_window_groups'] == list(range(5))
    quick = load('evidence/recovery-quick-checks.json')
    assert len(quick) == 21 and all(r['passed'] for r in quick)
    assert sum(r['expected'] == 'success' for r in quick) == 11
    assert sum(r['expected'] == 'nonzero' for r in quick) == 10
    assert all((r['returncode'] == 0) == (r['expected'] == 'success') for r in quick)
    snapshot = load('evidence/recovery-snapshot-test.json')
    assert snapshot['returncode'] == 0 and snapshot['recovered_files'] == 3
    main_records = load('evidence/recovery-main-records-run.json')
    assert main_records['returncode'] == 0
    arithmetic = json.loads(main_records['stdout'])
    assert arithmetic['audit_records'] == 251526
    assert arithmetic['audit_sha256'] == result['main_audit_sha256']
    assert arithmetic['audit_unsieved_records'] == 34515
    recorded_times = [main_records['seconds']]
    for chunk in range(10):
        produced = load('evidence/prefix-chunks/%02d.json' % chunk)
        assert not produced['base_two_hits'] and not produced['unresolved']
        for backend in ('pow', 'manual'):
            row = load('evidence/prefix-chunks/%02d.%s.json' % (chunk, backend))
            assert row['count'] == 10000000
            assert row['every_n_decision_full_residue_sha256'] == produced['every_n_decision_full_residue_sha256']
            recorded_times.append(row['seconds'])
    for group in range(5):
        for backend in ('pow', 'manual'):
            row = load('evidence/window-chunks/%02d.%s.json' % (group, backend))
            assert row['verified_windows'] == list(range(20*group, 20*group+20))
            assert row['total_members'] == 20971520
            recorded_times.append(row['seconds'])
    assert max(recorded_times) < 900, 'a recorded individual replay exceeded the limit'
    windows = [json.loads(line) for line in Path('logs/python-windows.jsonl').read_text().splitlines()]
    inside = [w for w in windows if 200000000000 <= w['start'] and w['end'] <= result['main_end']]
    assert len(inside) == 99 and windows[-1]['start'] == 10404842295296 > result['main_end']
    parts = load('selection-inputs/first-attempt-logs/MANIFEST.json')
    assert sum(len(s['parts']) for s in parts['sources']) == 33
    assert all(p['compressed_bytes'] < 5000000 for s in parts['sources'] for p in s['parts'])
    build = load('evidence/build.json')
    assert hashlib.sha256(Path('code/scan.c').read_bytes()).hexdigest() == build['source_sha256']
    # Exercise the two small replay commands not already recorded by the
    # arithmetic campaigns/quick checks. Execute argument arrays, not a shell.
    by_cid = {c['cid']: c for c in claims['claims']}
    auxiliary = []
    for cid, field in [('isolated-controls', 'verify_command'), ('power-two-family', 'check_command')]:
        command = by_cid[cid][field]
        argv = shlex.split(command)
        assert argv[0] == 'python3'
        begin = time.monotonic()
        run = subprocess.run([sys.executable]+argv[1:], capture_output=True, text=True, timeout=830)
        assert run.returncode == 0, run.stderr
        auxiliary.append(dict(command=command, returncode=run.returncode,
                              seconds=time.monotonic()-begin, stdout=run.stdout, stderr=run.stderr))
    output = dict(outcome='partial', consistency_checks_passed=True, claim_count=len(claims['claims']),
                  positive_quick_checks=11, negative_controls=10,
                  main_record_checks=251526, shared_arithmetic_checks=6032,
                  fresh_contiguous_prefix_members=100000000,
                  separated_window_members=104857600,
                  separated_windows_inside_main=99, separated_windows_outside_main=[99],
                  longest_recorded_individual_replay_seconds=max(recorded_times),
                  auxiliary_commands=auxiliary,
                  scope='Delivery consistency and named finite replay results only. No exhaustive independent certification of the main range; no all-orders resolution.')
    Path('evidence/recovery-final-checks.json').write_text(json.dumps(output, indent=2)+'\n')
    print(json.dumps({k: v for k, v in output.items() if k != 'auxiliary_commands'}, indent=2))


if __name__ == '__main__':
    main()
