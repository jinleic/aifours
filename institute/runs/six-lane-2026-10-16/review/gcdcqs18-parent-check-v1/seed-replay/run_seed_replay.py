#!/usr/bin/env python3
"""Sequential seed-replay executions; a disk-floor check and a lane-resource sample precede every child.
No timeout wrapper or signal; one child at a time; exclusive creates only.
Usage: python3 -B run_seed_replay.py NEW_OUTPUT_SUBDIR
"""
from datetime import datetime
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
LANE = '/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/tz43-gcdcqs18'
FLOOR_BYTES = 12_200_000_000
PINS = {
    'resource_sampler': (PARENT / 'run_suite.py', '23647fc9c4fac74053bb2c108140635db35ae269cf4649811a066cedd05833d4'),
    'replay': (HERE / 'replay_seed.py', 'ab3a90ce1aa60ab040fde8bc6d8c88a9bf28ef7b74fb989d7d23a181e25b4f1a'),
    'certificate': (PARENT / 'input/gcdcqs18_4_2_z8z3z3.txt', '1382d572f8024c9b93ff6f5cf8aff942a9538119e8462ba54b02b6f160da282e'),
    'seed': (HERE / 'input/seed-v1.json', '1831510f69d8610bf5496ecaed166ac86f8df768fd7c8a996a4c31cde59475f4'),
    'wrong_seed': (HERE / 'fixtures/seed-v1.t8-fixes-stems.json', 'd1bc2d758d9116816d997ff2f92824b7a60560f7ee5514f65db8e9a66badcdb6'),
}
CERT_ARGS = [str(PINS['certificate'][0]), PINS['certificate'][1]]
CASES = [
    {'case': 'positive', 'args': CERT_ARGS + [str(PINS['seed'][0]), PINS['seed'][1]], 'flags': [],
     'expected': {'type': 'positive'}},
    {'case': 'wrong-described-t8-fixes-stems', 'args': CERT_ARGS + [str(PINS['seed'][0]), PINS['seed'][1]],
     'flags': ['--wrong-t8-fixes-stems'],
     'expected': {'type': 'negative', 'condition': 'action_description', 'category': 'action.block_invariance',
                  'generator': 't8', 'passed_before': ['pin', 'parse', 'seed', 'group_description']}},
    {'case': 'wrong-seed-t8-fixes-stems', 'args': CERT_ARGS + [str(PINS['wrong_seed'][0]), PINS['wrong_seed'][1]],
     'flags': [],
     'expected': {'type': 'negative', 'condition': 'action_seed', 'category': 'action.block_invariance',
                  'generator': 't8', 'passed_before': ['pin', 'parse', 'seed', 'group_description',
                                                       'action_description', 'group_seed']}},
]


def now():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def exclusive(path, value):
    with Path(path).open('x') as f:
        if isinstance(value, str):
            f.write(value)
        else:
            json.dump(value, f, indent=2)
            f.write('\n')


def disk():
    free = {}
    for path in (str(HERE), LANE):
        st = os.statvfs(path)
        free[path] = st.f_bavail * st.f_frsize
    return {'sampled_at_pt': now(), 'free_bytes': free, 'floor_bytes': FLOOR_BYTES,
            'ok': all(v >= FLOOR_BYTES for v in free.values())}


def check_pins():
    observed = {name: sha(path) for name, (path, _) in PINS.items()}
    if any(observed[name] != expected for name, (_, expected) in PINS.items()):
        raise RuntimeError('Pin mismatch: %s' % observed)
    return observed


def main():
    if len(sys.argv) != 2:
        raise SystemExit(__doc__)
    out = Path(sys.argv[1])
    check_pins()
    spec = importlib.util.spec_from_file_location('parent_run_suite', PINS['resource_sampler'][0])
    sampler = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(sampler)
    out.mkdir(exist_ok=False)
    started = time.perf_counter()
    rows, aborted = [], None
    for case in CASES:
        for optimized in (False, True):
            label = case['case'] + ('.optimized' if optimized else '.normal')
            floor = disk()
            if not floor['ok']:
                exclusive(out / (label + '.disk.json'), floor)
                aborted = {'case': label, 'reason': 'free disk below floor', 'disk': floor}
                break
            samples = []
            for _ in range(300):
                samples.append(sampler.lane_snapshot())
                if samples[-1]['allowed_now']:
                    break
                time.sleep(2)
            exclusive(out / (label + '.resources.json'), {'disk': floor, 'lane_samples': samples})
            if not samples[-1]['allowed_now']:
                rows.append({'case': case['case'], 'optimized': optimized, 'outcome': 'UNKNOWN_RESOURCE_CAP',
                             'expectation_met': False})
                continue
            check_pins()
            receipt = out / (label + '.json')
            command = (['/usr/bin/time', '-l', sys.executable] + (['-O'] if optimized else []) + ['-B']
                       + [str(PINS['replay'][0])] + case['args'] + [str(receipt)] + case['flags'])
            t0 = time.perf_counter()
            child = subprocess.run(command, capture_output=True, text=True, cwd=str(HERE),
                                   env=dict(os.environ, PYTHONDONTWRITEBYTECODE='1'))
            elapsed = time.perf_counter() - t0
            exclusive(out / (label + '.stdout.txt'), child.stdout)
            exclusive(out / (label + '.time-stderr.txt'), child.stderr)
            peak = re.search(r'^\s*(\d+)\s+maximum resident set size\s*$', child.stderr, re.M)
            data = json.loads(receipt.read_text()) if receipt.exists() else {'status': 'NO_RECEIPT'}
            expected = case['expected']
            if expected['type'] == 'positive':
                met = (child.returncode == 0 and data.get('status') == 'PASS'
                       and all(c.get('status') == 'PASS' for c in data['conditions'].values()))
            else:
                met = (child.returncode == 1 and data.get('status') == 'FAIL'
                       and data.get('error_type') == 'ReplayError'
                       and data.get('condition') == expected['condition']
                       and data.get('category') == expected['category']
                       and data.get('details', {}).get('generator') == expected['generator']
                       and all(data['conditions'][c].get('status') == 'PASS' for c in expected['passed_before']))
            row = {'case': case['case'], 'optimized': optimized, 'command': command,
                   'returncode': child.returncode, 'status': data.get('status'),
                   'condition': data.get('condition'), 'category': data.get('category'),
                   'reason': data.get('reason'), 'details': data.get('details'), 'expected': expected,
                   'expectation_met': bool(met), 'supervisor_wall_seconds': elapsed,
                   'in_process_runtime_seconds': data.get('runtime_seconds'),
                   'phase_seconds': data.get('phase_seconds'),
                   'peak_rss_bytes_time_l': int(peak.group(1)) if peak else None,
                   'peak_rss_bytes_in_process': data.get('peak_rss_bytes'),
                   'receipt': str(receipt), 'receipt_sha256': sha(receipt) if receipt.exists() else None,
                   'external_busy_before_launch': samples[-1]['external_busy_processes'],
                   'external_lane_rss_before_launch': samples[-1]['external_total_rss_bytes'],
                   'free_disk_bytes_before_launch': floor['free_bytes']}
            rows.append(row)
            print(json.dumps({'case': label, 'status': row['status'], 'condition': row['condition'],
                              'category': row['category'], 'expectation_met': row['expectation_met'],
                              'seconds': elapsed, 'peak_rss_bytes': row['peak_rss_bytes_time_l']}), flush=True)
        if aborted:
            break
    ok = not aborted and len(rows) == 2 * len(CASES) and all(r['expectation_met'] for r in rows)
    result = {'recorded_at_pt': now(), 'status': 'ALL_EXPECTATIONS_MET' if ok else 'EXPECTATION_MISMATCH_OR_ABORTED',
              'aborted': aborted, 'pins': check_pins(), 'supervisor_sha256': sha(__file__), 'executions': len(rows),
              'outcomes': rows, 'total_wall_seconds': time.perf_counter() - started,
              'max_peak_rss_bytes': max((r.get('peak_rss_bytes_time_l') or 0) for r in rows) if rows else None,
              'max_external_busy_before_launch': max((r.get('external_busy_before_launch') or 0) for r in rows) if rows else None,
              'min_free_disk_bytes_before_launch': min(min(r['free_disk_bytes_before_launch'].values()) for r in rows if 'free_disk_bytes_before_launch' in r) if rows else None,
              'one_child_at_a_time': True, 'no_timeout_or_signal_used': True}
    exclusive(out / 'suite-result.json', result)
    print(json.dumps({'status': result['status'], 'executions': len(rows), 'wall_seconds': result['total_wall_seconds'],
                      'mismatches': [r['case'] for r in rows if not r['expectation_met']]}), flush=True)
    return 0 if ok else 1


if __name__ == '__main__':
    raise SystemExit(main())
