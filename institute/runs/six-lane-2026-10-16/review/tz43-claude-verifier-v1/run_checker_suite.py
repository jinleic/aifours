#!/usr/bin/env python3
"""Tz43VerifierDesk parent runner for the prompt-only Claude-authored checker (tz43-claude-verifier-v1).

Runs checker.py sequentially (one child at a time) on every case in cases.json under python3 -B and
python3 -O -B. Native RLIMIT_CPU only; no timeouts, no kills. Per-run stdout/stderr go to new files in
runs/; the aggregate goes to result.json. All files are created exclusively (mode 'x').
Usage: /usr/bin/python3 -B run_checker_suite.py EXPECTED_CHECKER_SHA256
"""
import hashlib
import json
import os
import resource
import subprocess
import sys
import time
from datetime import datetime
from zoneinfo import ZoneInfo

HERE = os.path.dirname(os.path.abspath(__file__))
PY = '/usr/bin/python3'
CHECKER = os.path.join(HERE, 'checker.py')
MODES = {'B': ['-B'], 'OB': ['-O', '-B']}
ENV = {'PATH': '/usr/bin:/bin', 'TMPDIR': os.path.join(HERE, 'tmp'), 'LC_ALL': 'C'}


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def limit():
    resource.setrlimit(resource.RLIMIT_CPU, (120, 130))


def run_one(tag, flags, args):
    out_path = os.path.join(HERE, 'runs', tag + '.stdout.txt')
    err_path = os.path.join(HERE, 'runs', tag + '.stderr.txt')
    argv = [PY] + flags + [CHECKER] + [str(a) for a in args]
    with open(out_path, 'x') as fo, open(err_path, 'x') as fe:
        t0 = time.monotonic()
        proc = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=fo, stderr=fe, cwd=HERE, env=ENV,
                                preexec_fn=limit)
        _, status, ru = os.wait4(proc.pid, 0)
        wall = time.monotonic() - t0
    proc.returncode = os.waitstatus_to_exitcode(status)
    with open(out_path, 'rb') as f:
        out = f.read()
    with open(err_path, 'rb') as f:
        err = f.read()
    text = out.decode('utf-8', 'replace')
    lines = text.split('\n')
    obj = None
    one_line = len(lines) == 2 and lines[1] == '' or len(lines) == 1
    try:
        obj = json.loads(text)
        if not isinstance(obj, dict):
            obj = None
    except ValueError:
        obj = None
    return {'argv': argv[1:], 'exit': proc.returncode, 'signal': -proc.returncode if proc.returncode < 0 else None,
            'stdout_json': obj, 'stdout_one_json_line': bool(obj is not None and one_line),
            'stdout_sha256': hashlib.sha256(out).hexdigest(), 'stderr_bytes': len(err),
            'stderr_tail': err[-1500:].decode('utf-8', 'replace'), 'wall_s': round(wall, 3),
            'user_s': round(ru.ru_utime, 3), 'sys_s': round(ru.ru_stime, 3), 'maxrss_bytes': ru.ru_maxrss}


def main():
    if len(sys.argv) != 2:
        raise SystemExit('usage: run_checker_suite.py EXPECTED_CHECKER_SHA256')
    checker_sha = sha(CHECKER)
    if checker_sha != sys.argv[1]:
        raise SystemExit('checker hash mismatch: ' + checker_sha)
    with open(os.path.join(HERE, 'cases.json')) as f:
        plan = json.load(f)
    started = stamp()
    t0 = time.monotonic()
    results = []
    for case in plan['cases']:
        if case.get('file_sha256_actual_required'):
            actual = sha(case['args'][2])
            if actual != case['file_sha256_actual_required']:
                raise SystemExit('fixture hash mismatch for ' + case['case'])
        for mode in case['modes']:
            r = run_one(case['case'] + '.' + mode, MODES[mode], case['args'])
            j = r['stdout_json'] or {}
            if case['expect'] == 'accept':
                ok = r['exit'] == 0 and j.get('valid') is True and j.get('invariant') is None
            else:
                ok = (r['exit'] == case['expect_exit'] and j.get('valid') is False
                      and j.get('invariant') in case['accepted_invariants'])
            r.update({'case': case['case'], 'group': case['group'], 'mode': mode, 'expect': case['expect'],
                      'intended_category': case.get('intended_category'),
                      'accepted_invariants': case.get('accepted_invariants'),
                      'observed_invariant': j.get('invariant'), 'observed_valid': j.get('valid'),
                      'observed_reason': j.get('reason'), 'ok': bool(ok and r['stdout_one_json_line'] and r['stderr_bytes'] == 0)})
            results.append(r)
            print(json.dumps({'case': r['case'], 'mode': mode, 'exit': r['exit'], 'invariant': r['observed_invariant'],
                              'ok': r['ok'], 'wall_s': r['wall_s']}), flush=True)
    summary = {
        'runner': 'run_checker_suite.py', 'runner_sha256': sha(os.path.abspath(__file__)),
        'checker_sha256': checker_sha, 'cases_json_sha256': sha(os.path.join(HERE, 'cases.json')),
        'python': subprocess.run([PY, '--version'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                 universal_newlines=True).stdout.strip(),
        'started_at_pt': started, 'finished_at_pt': stamp(), 'suite_wall_s': round(time.monotonic() - t0, 3),
        'executions': len(results), 'ok': sum(r['ok'] for r in results),
        'not_ok': [(r['case'], r['mode']) for r in results if not r['ok']],
        'accepted_executions': sum(r['exit'] == 0 for r in results),
        'rejected_executions': sum(r['exit'] != 0 for r in results),
        'max_child_maxrss_bytes': max(r['maxrss_bytes'] for r in results),
        'max_child_wall_s': max(r['wall_s'] for r in results),
        'all_stdout_one_json_line': all(r['stdout_one_json_line'] for r in results),
        'all_stderr_empty': all(r['stderr_bytes'] == 0 for r in results),
        'cases': results,
    }
    with open(os.path.join(HERE, 'suite-raw.json'), 'x') as f:
        json.dump(summary, f, indent=1)
        f.write('\n')
    print(json.dumps({k: v for k, v in summary.items() if k != 'cases'}))
    return 0 if not summary['not_ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
