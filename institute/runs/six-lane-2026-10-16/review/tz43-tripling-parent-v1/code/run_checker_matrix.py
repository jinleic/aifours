#!/usr/bin/env python3
"""Tz43TriplingAudit runner: both existing FDGDD checkers on the constructive certificate and its mutations.

Runs, one child at a time, the unchanged parent definition checker (check_fdgdd_format_d.py) and the unchanged
prompt-only Claude-authored checker (checker.py, KIND fdgdd, EXPECTED_V 90, EXPECTED_SHA) under /usr/bin/python3
and /opt/homebrew/bin/python3, each with -B and -O -B. Native RLIMIT_CPU only; no timeouts, no kills.
Every fixture is hash-checked against the build manifest before and after its runs, and the hash each checker
reports or is bound to must equal it. Outputs are new files only (mode 'x').
Usage: /usr/bin/python3 -B run_checker_matrix.py MANIFEST MANIFEST_SHA PARENT_CHECKER_SHA CLAUDE_CHECKER_SHA
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

DESK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REVIEW = os.path.dirname(DESK)
PARENT = os.path.join(REVIEW, 'tz43-fdgdd18-parent-v1', 'code', 'check_fdgdd_format_d.py')
CLAUDE = os.path.join(REVIEW, 'tz43-claude-verifier-v1', 'checker.py')
INTERPRETERS = [('sys39', '/usr/bin/python3'), ('brew', '/opt/homebrew/bin/python3')]
MODES = [('B', ['-B']), ('OB', ['-O', '-B'])]
ENV = {'PATH': '/usr/bin:/bin', 'TMPDIR': os.path.join(DESK, 'tmp'), 'LC_ALL': 'C'}
RUNS = os.path.join(DESK, 'runs')
ORIG_SHA = '3e22f5021631ac82ea5b5fa6f884984bb874f1f9a384fd35bfeff523e731a998'


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def sha_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def limit():
    resource.setrlimit(resource.RLIMIT_CPU, (120, 130))


def run_child(tag, argv):
    out_path = os.path.join(RUNS, tag + '.stdout.txt')
    err_path = os.path.join(RUNS, tag + '.stderr.txt')
    with open(out_path, 'x') as fo, open(err_path, 'x') as fe:
        t0 = time.monotonic()
        proc = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=fo, stderr=fe, cwd=DESK, env=ENV,
                                preexec_fn=limit)
        _, status, ru = os.wait4(proc.pid, 0)
        wall = time.monotonic() - t0
    code = os.waitstatus_to_exitcode(status)
    with open(out_path, 'rb') as f:
        out = f.read()
    with open(err_path, 'rb') as f:
        err = f.read()
    return {'tag': tag, 'argv': argv, 'exit': code, 'stdout': out.decode('utf-8', 'replace'),
            'stdout_sha256': hashlib.sha256(out).hexdigest(), 'stderr_bytes': len(err),
            'stderr_tail': err[-1500:].decode('utf-8', 'replace'), 'wall_s': round(wall, 3),
            'user_s': round(ru.ru_utime, 3), 'maxrss_bytes': ru.ru_maxrss}


def parent_case(name, path, sha, expect_failed, extra=()):
    rows = []
    for iname, py in INTERPRETERS:
        for mname, flags in MODES:
            tag = 'parent__%s__%s__%s' % (name, iname, mname)
            rep_path = os.path.join(RUNS, tag + '.report.json')
            r = run_child(tag, [py] + flags + [PARENT, path, '--out', rep_path] + list(extra))
            rep = None
            if os.path.exists(rep_path):
                with open(rep_path) as f:
                    rep = json.load(f)
            failed = rep.get('failed_checks') if rep else None
            ok = (rep is not None and r['stderr_bytes'] == 0
                  and rep['input']['sha256'] == sha and rep['checker']['sha256'] == PARENT_SHA
                  and rep['python']['optimize_flag'] == (1 if mname == 'OB' else 0))
            if expect_failed:
                ok = ok and r['exit'] == 1 and rep['verdict'] == 'FAIL' and set(failed) == set(expect_failed)
            else:
                ok = ok and r['exit'] == 0 and rep['verdict'] == 'PASS' and failed == [] \
                    and rep.get('definition_core_verdict') == 'PASS' and not rep.get('not_run_checks')
            fexamples = {}
            if rep and failed:
                for c in failed:
                    d = rep['checks'].get(c, {})
                    fexamples[c] = {'violations': d.get('violations'), 'first_example': (d.get('examples') or [None])[0]}
            r.pop('stdout')
            r.update({'checker': 'parent', 'case': name, 'interpreter': iname, 'mode': mname,
                      'report_path': rep_path, 'report_sha256': sha_file(rep_path) if rep else None,
                      'python_version': rep['python']['version'] if rep else None,
                      'verdict': rep.get('verdict') if rep else None, 'failed_checks': failed,
                      'expected_failed_checks': expect_failed, 'failed_check_examples': fexamples,
                      'reported_input_sha256': rep['input']['sha256'] if rep else None,
                      'reported_checker_sha256': rep['checker']['sha256'] if rep else None,
                      'stats_frames_status_hist': (rep.get('stats', {}).get('frames', {}) or {}).get(
                          'class_status_histogram') if rep else None,
                      'ok': bool(ok)})
            rows.append(r)
            print(json.dumps({'tag': tag, 'exit': r['exit'], 'failed': failed, 'ok': r['ok']}), flush=True)
    return rows


def claude_case(name, path, bound_sha, expect_invariant, expected_v='90', actual_sha=None):
    actual_sha = actual_sha or bound_sha
    rows = []
    for iname, py in INTERPRETERS:
        for mname, flags in MODES:
            tag = 'claude__%s__%s__%s' % (name, iname, mname)
            r = run_child(tag, [py] + flags + [CLAUDE, 'fdgdd', expected_v, path, bound_sha])
            text = r.pop('stdout')
            lines = text.split('\n')
            one_line = len(lines) == 2 and lines[1] == ''
            try:
                j = json.loads(text)
            except ValueError:
                j = None
            ok = j is not None and one_line and r['stderr_bytes'] == 0 and j.get('sha256') == actual_sha
            if expect_invariant is None:
                ok = ok and r['exit'] == 0 and j.get('valid') is True and j.get('invariant') is None \
                    and j.get('sha256') == bound_sha
            else:
                ok = ok and r['exit'] == 1 and j.get('valid') is False and j.get('invariant') == expect_invariant
            r.update({'checker': 'claude', 'case': name, 'interpreter': iname, 'mode': mname,
                      'bound_sha256': bound_sha, 'actual_sha256': actual_sha, 'expected_v': expected_v,
                      'valid': j.get('valid') if j else None, 'invariant': j.get('invariant') if j else None,
                      'expected_invariant': expect_invariant, 'reason': j.get('reason') if j else None,
                      'counts': j.get('counts') if j else None, 'stdout_one_json_line': one_line,
                      'ok': bool(ok)})
            rows.append(r)
            print(json.dumps({'tag': tag, 'exit': r['exit'], 'invariant': r['invariant'], 'ok': r['ok']}), flush=True)
    return rows


def main():
    global PARENT_SHA
    if len(sys.argv) != 5:
        raise SystemExit('usage: run_checker_matrix.py MANIFEST MANIFEST_SHA PARENT_CHECKER_SHA CLAUDE_CHECKER_SHA')
    manifest_path, manifest_sha, PARENT_SHA, claude_sha = sys.argv[1:]
    if sha_file(manifest_path) != manifest_sha:
        raise SystemExit('manifest hash mismatch')
    if sha_file(PARENT) != PARENT_SHA or sha_file(CLAUDE) != claude_sha:
        raise SystemExit('checker hash mismatch')
    with open(manifest_path) as f:
        man = json.load(f)
    fixtures = [('positive', man['written']['positive'], man['outputs']['positive']['sha256'], [], None)]
    for name, spec in man['mutations'].items():
        fixtures.append((name, man['written'][name], man['outputs'][name]['sha256'],
                         spec['expected_parent_failed_checks'], spec['expected_claude_invariant']))
    out = {'runner': os.path.abspath(__file__), 'runner_sha256': sha_file(os.path.abspath(__file__)),
           'manifest': os.path.abspath(manifest_path), 'manifest_sha256': manifest_sha,
           'parent_checker': PARENT, 'parent_checker_sha256': PARENT_SHA,
           'claude_checker': CLAUDE, 'claude_checker_sha256': claude_sha,
           'interpreters': dict(INTERPRETERS), 'started_at_pt': stamp(), 'rows': [], 'hash_checks': []}
    t0 = time.monotonic()
    for name, path, sha, exp_failed, exp_inv in fixtures:
        before = sha_file(path)
        if before != sha:
            raise SystemExit('fixture hash mismatch before runs: ' + name)
        out['rows'] += parent_case(name, path, sha, exp_failed)
        out['rows'] += claude_case(name, path, sha, exp_inv)
        after = sha_file(path)
        out['hash_checks'].append({'case': name, 'path': path, 'expected': sha, 'before': before, 'after': after,
                                   'ok': before == after == sha})
    pos_path, pos_sha = fixtures[0][1], fixtures[0][2]
    out['rows'] += parent_case('control_wrong_target_m6', pos_path, pos_sha, ['C01_HEADER'], ['--k', '5', '--m', '6'])
    out['rows'] += claude_case('control_wrong_expected_sha', pos_path, ORIG_SHA, 'sha256', actual_sha=pos_sha)
    out['rows'] += claude_case('control_wrong_expected_v89', pos_path, pos_sha, 'order', expected_v='89')
    out['hash_checks'].append({'case': 'positive-after-controls', 'path': pos_path, 'expected': pos_sha,
                               'after': sha_file(pos_path), 'ok': sha_file(pos_path) == pos_sha})
    rows = out['rows']
    out['summary'] = {
        'executions': len(rows), 'ok': sum(r['ok'] for r in rows),
        'not_ok': [r['tag'] for r in rows if not r['ok']],
        'positive_executions_ok': sum(r['ok'] for r in rows if r['case'] == 'positive'),
        'positive_executions': sum(1 for r in rows if r['case'] == 'positive'),
        'rejection_executions_ok': sum(r['ok'] for r in rows if r['case'] != 'positive'),
        'rejection_executions': sum(1 for r in rows if r['case'] != 'positive'),
        'all_hash_checks_ok': all(h['ok'] for h in out['hash_checks']),
        'all_stderr_empty': all(r['stderr_bytes'] == 0 for r in rows),
        'max_child_maxrss_bytes': max(r['maxrss_bytes'] for r in rows),
        'max_child_wall_s': max(r['wall_s'] for r in rows), 'suite_wall_s': round(time.monotonic() - t0, 3)}
    out['finished_at_pt'] = stamp()
    with open(os.path.join(DESK, 'checker-matrix-v1.json'), 'x') as f:
        json.dump(out, f, indent=1)
        f.write('\n')
    print(json.dumps(out['summary']))
    return 0 if not out['summary']['not_ok'] and out['summary']['all_hash_checks_ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
