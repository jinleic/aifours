#!/usr/bin/env python3
"""Sequential retained checker runs, with a lane-resource snapshot before each child.
No timeout wrapper, no signals, no claimant execution. All creates are exclusive.
Usage: python3 -B run_suite.py PLAN.json NEW_OUTPUT_SUBDIR
"""
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import resource
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

LANE = '/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/tz43-gcdcqs18'
ROOT = Path(__file__).resolve().parent
GIB = 1024**3


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exclusive(path, value, is_json=False):
    with Path(path).open('x') as f:
        if is_json:
            json.dump(value, f, indent=2)
            f.write('\n')
        else:
            f.write(value)


def lane_snapshot():
    # cwd identifies relative-argv solver jobs; parent links identify children.
    p = subprocess.run(['/bin/ps', '-Ao', 'pid=,ppid=,pcpu=,rss=,state=,etime=,command='],
                       capture_output=True, text=True)
    if p.returncode:
        raise RuntimeError('Cannot sample ps: ' + p.stderr)
    processes = {}
    for line in p.stdout.splitlines():
        words = line.strip().split(None, 6)
        if len(words) != 7:
            continue
        pid, ppid, cpu, rss, state, elapsed, command = words
        processes[int(pid)] = {'pid': int(pid), 'ppid': int(ppid), 'pcpu': float(cpu),
                               'rss_bytes': int(rss)*1024, 'state': state,
                               'elapsed': elapsed, 'command': command}
    lsof = subprocess.run(['/usr/sbin/lsof', '-nP', '-a', '-d', 'cwd', '-Fpn'],
                          capture_output=True, text=True)
    if lsof.returncode not in (0, 1):
        raise RuntimeError('Cannot sample cwd: ' + lsof.stderr)
    pid, cwd = None, {}
    for line in lsof.stdout.splitlines():
        if line.startswith('p') and line[1:].isdigit():
            pid = int(line[1:])
        elif line.startswith('n') and pid is not None:
            cwd[pid] = line[1:]
    own = {os.getpid()}
    changed = True
    while changed:
        changed = False
        for pid, row in processes.items():
            if row['ppid'] in own and pid not in own:
                own.add(pid)
                changed = True
    lane_pids = set()
    for pid, row in processes.items():
        where, command = cwd.get(pid, ''), row['command']
        if where == LANE or where.startswith(LANE+'/') or LANE in command:
            lane_pids.add(pid)
        elif re.search(r'(?:gcdcqs18|mcdsqs74)', command) and pid not in own:
            lane_pids.add(pid)
    changed = True
    while changed:
        changed = False
        for pid, row in processes.items():
            if row['ppid'] in lane_pids and pid not in lane_pids:
                lane_pids.add(pid)
                changed = True
    rows = []
    for pid in sorted(lane_pids-own):
        row = dict(processes[pid])
        row['cwd'] = cwd.get(pid)
        executable = Path(row['command'].split()[0]).name
        solver = executable in {'kissat', 'cadical', 'minisat', 'glucose', 'z3', 'scip'}
        row['busy'] = not row['state'].startswith('Z') and (row['pcpu'] >= 0.5 or solver or row['state'].startswith('R'))
        rows.append(row)
    busy = sum(row['busy'] for row in rows)
    memory = sum(row['rss_bytes'] for row in rows)
    return {'sampled_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
            'external_lane_processes': rows, 'external_busy_processes': busy,
            'external_total_rss_bytes': memory, 'our_planned_busy_children': 1,
            'planned_child_rss_ceiling_bytes': 512*1024**2,
            'allowed_busy_processes': 4, 'allowed_lane_rss_bytes': 8*GIB,
            'allowed_now': busy+1 <= 4 and memory+512*1024**2 < 8*GIB,
            'method': 'ps CPU/state plus native-solver classification; cwd from lsof; descendants included; waiting wrappers not counted busy'}


def guarded_run(plan, case, optimized, directory):
    label = case['case'] + ('.optimized' if optimized else '.normal')
    # The lane owner has reserved one checker slot. Independently sample before
    # every execution; do not launch if the sampled total would exceed the cap.
    samples = []
    for attempt in range(300):
        snapshot = lane_snapshot()
        samples.append(snapshot)
        if snapshot['allowed_now']:
            break
        time.sleep(2)
    if not samples[-1]['allowed_now']:
        exclusive(directory/(label+'.resources.json'), samples, True)
        return {'case': case['case'], 'optimized': optimized, 'outcome': 'UNKNOWN_RESOURCE_CAP',
                'expectation_met': False, 'resource_samples': samples}
    exclusive(directory/(label+'.resources.json'), samples, True)
    if sha(plan['checker']) != plan['checker_sha256']:
        raise RuntimeError('Checker pin changed before execution')
    if sha(case['input']) != case['actual_input_sha256']:
        raise RuntimeError('Input pin changed before execution')
    receipt = directory/(label+'.json')
    python = [sys.executable] + (['-O'] if optimized else []) + ['-B']
    if plan['kind'] == 'gcdcqs18':
        checker_args = [case['input'], case['expected_input_sha256'], str(receipt)]
    else:
        checker_args = [case['input'], str(case.get('expected_v', 74)), case['expected_input_sha256'], str(receipt)]
    command = ['/usr/bin/time', '-l'] + python + [plan['checker']] + checker_args
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    started = time.perf_counter()
    child = subprocess.run(command, capture_output=True, text=True, cwd=str(ROOT), env=env)
    elapsed = time.perf_counter()-started
    exclusive(directory/(label+'.stdout.txt'), child.stdout)
    exclusive(directory/(label+'.time-stderr.txt'), child.stderr)
    measurement = re.search(r'^\s*(\d+)\s+maximum resident set size\s*$', child.stderr, re.M)
    peak = int(measurement.group(1)) if measurement else None
    result = json.loads(receipt.read_text()) if receipt.exists() else {'status': 'NO_RECEIPT'}
    expected = case['expected']
    if expected['type'] == 'positive':
        success_status = 'PASS' if plan['kind'] == 'gcdcqs18' else 'VALID_MCDSQS'
        matched = child.returncode == 0 and result.get('status') == success_status
    else:
        invalid_status = 'FAIL' if plan['kind'] == 'gcdcqs18' else 'INVALID'
        matched = child.returncode == 1 and result.get('status') == invalid_status
        matched = matched and result.get('error_type') == 'CertificateError'
        matched = matched and result.get('reason') == expected['reason']
        if plan['kind'] == 'gcdcqs18':
            matched = matched and result.get('category') == expected['category']
    row = {'case': case['case'], 'optimized': optimized, 'input': case['input'],
           'input_sha256': case['actual_input_sha256'], 'expected_input_sha256': case['expected_input_sha256'],
           'expected': expected, 'returncode': child.returncode, 'status': result.get('status'),
           'error_type': result.get('error_type'), 'reason': result.get('reason'),
           'category': result.get('category'), 'details': result.get('details'),
           'expectation_met': bool(matched), 'runtime_seconds': elapsed,
           'peak_rss_bytes': peak, 'runtime_measurement': 'supervisor perf_counter around /usr/bin/time -l; Darwin ru_maxrss in bytes',
           'command': command, 'receipt': str(receipt), 'receipt_sha256': sha(receipt) if receipt.exists() else None,
           'stdout': str(directory/(label+'.stdout.txt')),
           'time_stderr': str(directory/(label+'.time-stderr.txt')),
           'resource_sample': str(directory/(label+'.resources.json')),
           'external_busy_processes_before_launch': snapshot['external_busy_processes'],
           'external_lane_rss_before_launch': snapshot['external_total_rss_bytes']}
    if expected['type'] == 'negative' and matched and plan['kind'] == 'mcdsqs74':
        row['observed_category_from_exact_reason'] = expected['category']
    if expected['type'] == 'positive':
        row['checker_result'] = result
    print(json.dumps({'case': label, 'status': result.get('status'), 'reason': result.get('reason'),
                      'expectation_met': bool(matched), 'seconds': elapsed, 'peak_rss_bytes': peak}), flush=True)
    return row


def main():
    if len(sys.argv) != 3:
        raise SystemExit('Usage: PLAN.json NEW_OUTPUT_SUBDIR')
    plan_path, destination = map(Path, sys.argv[1:])
    plan = json.loads(plan_path.read_text())
    destination.mkdir(exist_ok=False)
    started = time.perf_counter()
    rows = []
    for case in plan['cases']:
        for optimized in (False, True):
            rows.append(guarded_run(plan, case, optimized, destination))
    all_matched = all(row['expectation_met'] for row in rows)
    rss_values = [row['peak_rss_bytes'] for row in rows if row.get('peak_rss_bytes') is not None]
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'kind': plan['kind'], 'status': 'ALL_EXPECTATIONS_MET' if all_matched else 'EXPECTATION_MISMATCH',
              'checker': plan['checker'], 'checker_sha256': plan['checker_sha256'],
              'supervisor_sha256': sha(__file__), 'plan_sha256': sha(plan_path),
              'cases': len(plan['cases']), 'executions': len(rows), 'outcomes': rows,
              'total_runtime_seconds': time.perf_counter()-started,
              'max_child_peak_rss_bytes': max(rss_values) if rss_values else None,
              'max_sampled_external_busy_processes': max((row.get('external_busy_processes_before_launch',0) for row in rows), default=0),
              'one_child_at_a_time': True,
              'no_timeout_or_signal_used': True}
    exclusive(destination/'suite-result.json', result, True)
    print(json.dumps({'status': result['status'], 'executions': len(rows),
                      'runtime_seconds': result['total_runtime_seconds'],
                      'mismatches': [row['case'] for row in rows if not row['expectation_met']]}), flush=True)
    return 0 if all_matched else 1


if __name__ == '__main__':
    raise SystemExit(main())
