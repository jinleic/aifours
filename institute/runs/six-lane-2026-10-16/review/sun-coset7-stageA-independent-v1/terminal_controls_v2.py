#!/usr/bin/env python3
"""Deterministic terminal-handling controls for the sun-coset7 Stage A checker (stdlib only).

one      --label v1|v2 --checker C --checker-sha S --control X --input-dir D --outdir O
         One control in ONE process: exclusive outdir, fresh admission gate (statvfs free >=
         12.2e9 + 16 MiB, else exit 90 without running), the verified checker bytes executed as a
         module, one injection installed by monkeypatching from outside (the checker source is not
         modified), then checker main() for `verify --universe MSP45 --input-dir D`.  stdout and
         stderr of the process go to files in O; injections are logged on stderr.
record   --outdir O --rc N                      postrun record with the shell-observed status
evaluate --dir D --v1-sha A --v2-sha B --out F  compare every control with the frozen expectations
compare  --a A --b B --rc N --out F             v1 versus v2 positive results (timing removed)

Consumer rule applied to every run: a result is accepted only if the process exited normally with
status 0, result.json parses with exit_code 0 and overall COMPLETE_VALID, and no
result.json.CANCELLED.json exists.
"""
import argparse
import errno
import hashlib
import json
import os
import signal
import sys
import time
import types

ADMISSION_FREE = 12_200_000_000 + 16 * 1024 * 1024
NOT_STARTED_RC = 90
UNIVERSE = 'MSP45'
RUN_FILES = ('run.json', 'survivors.json', 'vfc_killed.json.gz', 'lp_duals.json.gz', 'leaves.jsonl.gz')
THRESHOLD = 2048          # result bytes written before the in-serialisation injections fire
MARKER_SUFFIX = '.CANCELLED.json'

CONTROLS = {
    'H0': 'no injection (harness neutrality)',
    'C1': 'terminal resource stop: statvfs reads 12e9-1 B (below the in-flight floor) after the universe completed',
    'C2': 'SIGTERM delivered after the universe completed and before the terminal decision (handler path)',
    'C3': 'SIGTERM sent at the first resource sample after the universe completed (v2: inside the blocked decision window)',
    'C4': 'SIGTERM sent during result serialisation, after %d bytes' % THRESHOLD,
    'C5': 'SIGTERM sent right after the summary line is printed',
    'C6': 'SIGTERM sent at the final SIGTERM unblock, after the last check (v2 only)',
    'C7': 'resource stop after publication: statvfs reads 12e9-1 B once result.json is closed (v2 only; v1 never samples after publication)',
    'C8': 'publication error: OSError(ENOSPC) raised during result serialisation after %d bytes' % THRESHOLD,
}
V2_ONLY = {'C6', 'C7'}

_TERM_C = {'stop_latched_at_decision': True, 'overall_before_terminal_decision': 'COMPLETE_VALID'}
EXPECT = {
    'v2': {
        'H0': {'rc': 0, 'marker': False, 'result': 'parse', 'overall': 'COMPLETE_VALID', 'exit_code': 0, 'accept': True,
               'terminal': {'stop_latched_at_decision': False, 'sigterm_pending_at_decision': False}},
        'C1': {'rc': 3, 'marker': False, 'result': 'parse', 'overall': 'UNKNOWN', 'exit_code': 3, 'accept': False,
               'terminal': dict(_TERM_C, sigterm_pending_at_decision=False), 'stop_reason_prefix': 'statvfs free'},
        'C2': {'rc': 3, 'marker': False, 'result': 'parse', 'overall': 'UNKNOWN', 'exit_code': 3, 'accept': False,
               'terminal': dict(_TERM_C, sigterm_pending_at_decision=False), 'stop_reason_exact': 'SIGTERM'},
        'C3': {'rc': 3, 'marker': False, 'result': 'parse', 'overall': 'UNKNOWN', 'exit_code': 3, 'accept': False,
               'terminal': dict(_TERM_C, sigterm_pending_at_decision=True),
               'stop_reason_exact': 'SIGTERM pending at terminal decision'},
        'C4': {'rc': 3, 'marker': True, 'marker_reason_exact': 'SIGTERM received during or after serialisation',
               'result': 'parse', 'overall': 'COMPLETE_VALID', 'exit_code': 0, 'accept': False},
        'C5': {'rc': 3, 'marker': True, 'marker_reason_exact': 'SIGTERM received during or after serialisation',
               'result': 'parse', 'overall': 'COMPLETE_VALID', 'exit_code': 0, 'accept': False},
        'C6': {'rc': 128 + 15, 'marker': False, 'result': 'parse', 'overall': 'COMPLETE_VALID', 'exit_code': 0,
               'accept': False},
        'C7': {'rc': 3, 'marker': True, 'marker_reason_prefix': 'stop latched after the decision: statvfs free',
               'result': 'parse', 'overall': 'COMPLETE_VALID', 'exit_code': 0, 'accept': False},
        'C8': {'rc': 5, 'marker': True, 'marker_reason_prefix': 'publication error: OSError', 'result': 'unparseable',
               'accept': False},
    },
    # Predictions for v1 read off its source (S00:1944-1971); they show whether each control is sensitive.
    'v1': {
        'H0': {'rc': 0, 'marker': False, 'result': 'parse', 'overall': 'COMPLETE_VALID', 'exit_code': 0, 'accept': True,
               'resources_stop_exact': None},
        'C1': {'rc': 0, 'marker': False, 'result': 'parse', 'overall': 'COMPLETE_VALID', 'exit_code': 0, 'accept': True,
               'resources_stop_prefix': 'statvfs free'},
        'C2': {'rc': 0, 'marker': False, 'result': 'parse', 'overall': 'COMPLETE_VALID', 'exit_code': 0, 'accept': True,
               'resources_stop_exact': 'SIGTERM'},
        'C3': {'rc': 0, 'marker': False, 'result': 'parse', 'overall': 'COMPLETE_VALID', 'exit_code': 0, 'accept': True,
               'resources_stop_exact': 'SIGTERM'},
        'C4': {'rc': 0, 'marker': False, 'result': 'parse', 'overall': 'COMPLETE_VALID', 'exit_code': 0, 'accept': True,
               'resources_stop_exact': None},
        'C5': {'rc': 0, 'marker': False, 'result': 'parse', 'overall': 'COMPLETE_VALID', 'exit_code': 0, 'accept': True,
               'resources_stop_exact': None},
        'C8': {'rc': 1, 'marker': False, 'result': 'unparseable', 'accept': False},
    },
}

STATE = {'post': False, 'published': False, 'fired': set()}


def sha(b):
    return hashlib.sha256(b).hexdigest()


def rd(p):
    with open(p, 'rb') as f:
        return f.read()


def wx(p, obj):
    with open(p, 'x') as f:
        json.dump(obj, f, indent=1, default=str)
        f.write('\n')
        f.flush()
        os.fsync(f.fileno())


def now():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z')


def log(msg):
    os.write(2, ('%s t=%.6f %s\n' % (now(), time.monotonic(), msg)).encode())


def fire(tag, kill):
    STATE['fired'].add(tag)
    log('INJECT %s: %s%s' % (tag, CONTROLS[tag], ' (os.kill SIGTERM to self)' if kill else ''))
    if kill:
        os.kill(os.getpid(), signal.SIGTERM)


def install(mod, control, out):
    real_vu = mod.verify_universe

    def verify_universe(*a, **k):
        r = real_vu(*a, **k)
        STATE['post'] = True
        log('UNIVERSE_DONE status=%s' % r.get('status'))
        if control == 'C2':
            fire('C2', True)
        return r

    mod.verify_universe = verify_universe

    if control in ('C1', 'C7'):
        real_free = mod.Guard.free
        low = mod.INFLIGHT_FLOOR - 1

        def free(self):
            if (control == 'C1' and STATE['post']) or (control == 'C7' and STATE['published']):
                if control not in STATE['fired']:
                    fire(control, False)
                return low
            return real_free(self)

        mod.Guard.free = free

    if control == 'C3':
        real_sample = mod.Guard.sample

        def sample(self):
            if STATE['post'] and 'C3' not in STATE['fired']:
                fire('C3', True)
            return real_sample(self)

        mod.Guard.sample = sample

    if control in ('C4', 'C7', 'C8'):
        import builtins
        real_open = builtins.open

        class ResultFile:
            def __init__(self, f):
                self._f = f
                self._n = 0

            def write(self, s):
                if control == 'C8' and self._n + len(s) >= THRESHOLD and 'C8' not in STATE['fired']:
                    fire('C8', False)
                    raise OSError(errno.ENOSPC, 'injected: no space left on device')
                r = self._f.write(s)
                self._n += len(s)
                if control == 'C4' and self._n >= THRESHOLD and 'C4' not in STATE['fired']:
                    fire('C4', True)
                return r

            def flush(self):
                return self._f.flush()

            def fileno(self):
                return self._f.fileno()

            def close(self):
                r = self._f.close()
                STATE['published'] = True
                log('RESULT_CLOSED bytes=%d' % self._n)
                return r

            def __getattr__(self, name):
                return getattr(self._f, name)

        def opener(file, mode='r', *a, **k):
            f = real_open(file, mode, *a, **k)
            if mode == 'x' and os.path.abspath(str(file)) == out:
                return ResultFile(f)
            return f

        mod.open = opener

    if control == 'C5':
        import builtins
        real_print = builtins.print

        def printer(*a, **k):
            r = real_print(*a, **k)
            if 'C5' not in STATE['fired']:
                fire('C5', True)
            return r

        mod.print = printer

    if control == 'C6':
        real_mask = signal.pthread_sigmask

        def mask(how, sigs):
            if how == signal.SIG_UNBLOCK and signal.SIGTERM in set(sigs) and 'C6' not in STATE['fired']:
                fire('C6', True)
            return real_mask(how, sigs)

        signal.pthread_sigmask = mask


def cmd_one(a):
    if a.label not in EXPECT or a.control not in CONTROLS or (a.label == 'v1' and a.control in V2_ONLY):
        print('REFUSED: unknown or inapplicable control %s-%s' % (a.label, a.control))
        return 2
    os.mkdir(a.outdir)
    outdir = os.path.abspath(a.outdir)
    ck = os.path.abspath(a.checker)
    src = rd(ck)
    st = os.statvfs(outdir)
    free = st.f_bavail * st.f_frsize
    inputs = {fn: sha(rd(os.path.join(a.input_dir, fn))) for fn in RUN_FILES}
    ok_sha = sha(src) == a.checker_sha
    pre = {'label': a.label, 'control': a.control, 'description': CONTROLS[a.control],
           'checker': {'path': ck, 'sha256': sha(src), 'expected_sha256': a.checker_sha, 'match': ok_sha},
           'harness': {'path': os.path.abspath(__file__), 'sha256': sha(rd(os.path.abspath(__file__)))},
           'input_dir': os.path.abspath(a.input_dir), 'input_sha256': inputs, 'universe': UNIVERSE,
           'admission': {'statvfs_free_bytes': free, 'required_bytes': ADMISSION_FREE, 'ok': free >= ADMISSION_FREE},
           'python': sys.version, 'executable': sys.executable, 'pid': os.getpid(), 'host_clock': now(),
           'tmpdir_env': os.environ.get('TMPDIR')}
    pre['status'] = 'STARTED' if ok_sha and free >= ADMISSION_FREE else 'NOT_STARTED'
    wx(os.path.join(outdir, 'prerun.json'), pre)
    print('%s %s-%s free=%d' % (pre['status'], a.label, a.control, free), flush=True)
    if pre['status'] != 'STARTED':
        return NOT_STARTED_RC
    so = os.open(os.path.join(outdir, 'stdout.txt'), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    se = os.open(os.path.join(outdir, 'stderr.txt'), os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
    sys.stdout.flush()
    sys.stderr.flush()
    os.dup2(so, 1)
    os.dup2(se, 2)
    mod = types.ModuleType('checker_under_test')
    mod.__file__ = ck
    exec(compile(src, ck, 'exec'), mod.__dict__)
    out = os.path.join(outdir, 'result.json')
    install(mod, a.control, out)
    sys.argv = [ck, 'verify', '--universe', UNIVERSE, '--input-dir', os.path.abspath(a.input_dir), '--out', out]
    log('MAIN_START control=%s' % a.control)
    rc = mod.main()
    log('MAIN_RETURNED rc=%s fired=%s' % (rc, sorted(STATE['fired'])))
    return rc


def cmd_record(a):
    outdir = os.path.abspath(a.outdir)
    files = {}
    for fn in sorted(os.listdir(outdir)):
        p = os.path.join(outdir, fn)
        if os.path.isfile(p):
            b = rd(p)
            files[fn] = {'sha256': sha(b), 'bytes': len(b)}
    rec = {'rc_shell': a.rc, 'terminated_by_signal': (a.rc - 128) if a.rc > 128 else None,
           'host_clock': now(), 'files_before_this_record': files}
    wx(os.path.join(outdir, 'postrun.json'), rec)
    print('recorded rc=%d %s' % (a.rc, outdir))
    return 0


def jload(p):
    try:
        return json.loads(rd(p))
    except (OSError, ValueError):
        return None


def consumer_accepts(rc, result, marker_exists):
    return (rc == 0 and result is not None and result.get('exit_code') == 0
            and result.get('overall') == 'COMPLETE_VALID' and not marker_exists)


def evaluate_row(label, control, d, pins):
    exp = EXPECT[label][control]
    row = {'label': label, 'control': control, 'description': CONTROLS[control]}
    pre = jload(os.path.join(d, 'prerun.json'))
    post = jload(os.path.join(d, 'postrun.json'))
    if pre is None or pre.get('status') != 'STARTED':
        row.update(run=False, as_expected=False, reasons=['not started'])
        return row
    reasons = []
    if post is None:
        reasons.append('postrun record missing')
        rc = None
    else:
        rc = post['rc_shell']
    rpath = os.path.join(d, 'result.json')
    result = jload(rpath)
    mpath = rpath + MARKER_SUFFIX
    marker_exists = os.path.exists(mpath)
    marker = jload(mpath) if marker_exists else None
    try:
        err = rd(os.path.join(d, 'stderr.txt')).decode('utf-8', 'replace')
    except OSError:
        err = ''
    injected = [l for l in err.splitlines() if ' INJECT ' in l]
    row.update(run=True, rc_shell=rc, result_parses=result is not None, marker=marker_exists,
               injections=injected, stderr_traceback='Traceback' in err)
    if rc != exp['rc']:
        reasons.append('rc %r != expected %r' % (rc, exp['rc']))
    if marker_exists != exp['marker']:
        reasons.append('marker %r != expected %r' % (marker_exists, exp['marker']))
    if exp['result'] == 'parse' and result is None:
        reasons.append('result.json does not parse')
    if exp['result'] == 'unparseable' and result is not None:
        reasons.append('result.json unexpectedly parses')
    if result is not None:
        row.update(overall=result.get('overall'), exit_code=result.get('exit_code'),
                   checker_sha256=result.get('checker_sha256'), terminal=result.get('terminal'),
                   resources_stop=(result.get('resources') or {}).get('stop'))
        if result.get('checker_sha256') != pins[label]:
            reasons.append('result checker_sha256 is not the %s pin' % label)
        for f in ('overall', 'exit_code'):
            if f in exp and result.get(f) != exp[f]:
                reasons.append('%s %r != expected %r' % (f, result.get(f), exp[f]))
        term = result.get('terminal') or {}
        for k, v in exp.get('terminal', {}).items():
            if term.get(k) != v:
                reasons.append('terminal.%s %r != expected %r' % (k, term.get(k), v))
        why = term.get('stop_reason_at_decision')
        if 'stop_reason_exact' in exp and why != exp['stop_reason_exact']:
            reasons.append('stop reason %r != %r' % (why, exp['stop_reason_exact']))
        if 'stop_reason_prefix' in exp and not str(why).startswith(exp['stop_reason_prefix']):
            reasons.append('stop reason %r lacks prefix %r' % (why, exp['stop_reason_prefix']))
        rs = (result.get('resources') or {}).get('stop')
        if 'resources_stop_exact' in exp and rs != exp['resources_stop_exact']:
            reasons.append('resources.stop %r != %r' % (rs, exp['resources_stop_exact']))
        if 'resources_stop_prefix' in exp and not str(rs).startswith(exp['resources_stop_prefix']):
            reasons.append('resources.stop %r lacks prefix %r' % (rs, exp['resources_stop_prefix']))
    if marker_exists:
        row['marker_content'] = marker
        if marker is None:
            reasons.append('marker does not parse')
        else:
            mr = marker.get('reason', '')
            if 'marker_reason_exact' in exp and mr != exp['marker_reason_exact']:
                reasons.append('marker reason %r != %r' % (mr, exp['marker_reason_exact']))
            if 'marker_reason_prefix' in exp and not mr.startswith(exp['marker_reason_prefix']):
                reasons.append('marker reason %r lacks prefix %r' % (mr, exp['marker_reason_prefix']))
            if marker.get('process_exit_code') != rc:
                reasons.append('marker process_exit_code %r != shell rc %r' % (marker.get('process_exit_code'), rc))
    acc = consumer_accepts(rc, result, marker_exists)
    row['consumer_accepts'] = acc
    if acc != exp['accept']:
        reasons.append('consumer acceptance %r != expected %r' % (acc, exp['accept']))
    if control == 'H0' and injected:
        reasons.append('H0 logged an injection')
    if control != 'H0' and not any((' INJECT %s:' % control) in l for l in injected):
        reasons.append('injection %s did not fire' % control)
    row['as_expected'] = not reasons
    row['reasons'] = reasons
    return row


def cmd_evaluate(a):
    pins = {'v1': a.v1_sha, 'v2': a.v2_sha}
    rows = []
    for label in ('v2', 'v1'):
        for control in sorted(EXPECT[label]):
            d = os.path.join(a.dir, '%s-%s' % (label, control))
            if os.path.isdir(d):
                rows.append(evaluate_row(label, control, d, pins))
            else:
                rows.append({'label': label, 'control': control, 'run': False, 'as_expected': False,
                             'reasons': ['directory missing']})
    v2 = [r for r in rows if r['label'] == 'v2']
    v1 = [r for r in rows if r['label'] == 'v1']
    v2_ok = all(r['as_expected'] for r in v2)
    out = {'evaluated_host_clock': now(), 'harness_sha256': sha(rd(os.path.abspath(__file__))),
           'pins': pins, 'consumer_rule': 'accept iff normal exit 0, result exit_code 0 and COMPLETE_VALID, no marker',
           'v2_all_controls_as_expected': v2_ok,
           'v2_controls_run': [r['control'] for r in v2 if r.get('run')],
           'v1_predictions_matched': [r['control'] for r in v1 if r['as_expected']],
           'v1_injected_runs_accepted_as_complete': [r['control'] for r in v1
                                                      if r.get('run') and r['control'] != 'H0' and r.get('consumer_accepts')],
           'v2_injected_runs_accepted_as_complete': [r['control'] for r in v2
                                                      if r.get('run') and r['control'] != 'H0' and r.get('consumer_accepts')],
           'rows': rows}
    out['status'] = 'PASS' if v2_ok else ('INCOMPLETE' if any(not r.get('run') for r in v2) else 'FAIL')
    wx(a.out, out)
    print(json.dumps({k: out[k] for k in ('status', 'v2_all_controls_as_expected', 'v2_controls_run',
                                          'v1_predictions_matched', 'v1_injected_runs_accepted_as_complete',
                                          'v2_injected_runs_accepted_as_complete')}))
    return 0 if v2_ok else 1


VOLATILE = {'seconds', 'walk_seconds'}
SECTIONS = ('frozen_texts', 'receipt_audit', 'top_issues', 'universes', 'controls', 'overall', 'exit_code')


def strip(o):
    if isinstance(o, dict):
        return {k: strip(v) for k, v in o.items() if k not in VOLATILE}
    if isinstance(o, list):
        return [strip(v) for v in o]
    return o


def cmd_compare(a):
    A, B = jload(a.a), jload(a.b)
    out = {'compared_host_clock': now(), 'harness_sha256': sha(rd(os.path.abspath(__file__))),
           'a': {'path': os.path.abspath(a.a), 'sha256': sha(rd(a.a))},
           'b': {'path': os.path.abspath(a.b), 'sha256': sha(rd(a.b))}, 'b_rc_shell': a.rc,
           'volatile_keys_removed': sorted(VOLATILE)}
    eq = {s: strip(A.get(s)) == strip(B.get(s)) for s in SECTIONS}
    udiff = {}
    for U in sorted(set(A.get('universes') or {}) | set(B.get('universes') or {})):
        ua, ub = (A.get('universes') or {}).get(U, {}), (B.get('universes') or {}).get(U, {})
        udiff[U] = sorted(k for k in set(ua) | set(ub)
                          if k not in VOLATILE and strip(ua.get(k)) != strip(ub.get(k)))
    marker_b = os.path.exists(a.b + MARKER_SUFFIX)
    term = B.get('terminal') or {}
    out.update(section_equal=eq, universe_keys_differing=udiff, keys_only_in_b=sorted(set(B) - set(A)),
               keys_only_in_a=sorted(set(A) - set(B)), b_terminal=term, b_marker=marker_b,
               b_overall=B.get('overall'), b_exit_code=B.get('exit_code'),
               b_universe_status={U: r.get('status') for U, r in (B.get('universes') or {}).items()},
               b_controls_status=(B.get('controls') or {}).get('status'),
               b_consumer_accepts=consumer_accepts(a.rc, B, marker_b))
    out['equal_modulo_timing'] = all(eq.values()) and not any(udiff.values())
    out['status'] = 'PASS' if (out['equal_modulo_timing'] and out['b_consumer_accepts']
                               and term.get('stop_latched_at_decision') is False
                               and term.get('sigterm_pending_at_decision') is False) else 'FAIL'
    wx(a.out, out)
    print(json.dumps({k: out[k] for k in ('status', 'equal_modulo_timing', 'section_equal', 'universe_keys_differing',
                                          'keys_only_in_b', 'b_overall', 'b_exit_code', 'b_marker',
                                          'b_consumer_accepts')}))
    return 0 if out['status'] == 'PASS' else 1


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    o = sub.add_parser('one')
    o.add_argument('--label', required=True)
    o.add_argument('--checker', required=True)
    o.add_argument('--checker-sha', required=True)
    o.add_argument('--control', required=True)
    o.add_argument('--input-dir', required=True)
    o.add_argument('--outdir', required=True)
    r = sub.add_parser('record')
    r.add_argument('--outdir', required=True)
    r.add_argument('--rc', required=True, type=int)
    e = sub.add_parser('evaluate')
    e.add_argument('--dir', required=True)
    e.add_argument('--v1-sha', required=True)
    e.add_argument('--v2-sha', required=True)
    e.add_argument('--out', required=True)
    c = sub.add_parser('compare')
    c.add_argument('--a', required=True)
    c.add_argument('--b', required=True)
    c.add_argument('--rc', required=True, type=int)
    c.add_argument('--out', required=True)
    args = ap.parse_args()
    return {'one': cmd_one, 'record': cmd_record, 'evaluate': cmd_evaluate, 'compare': cmd_compare}[args.cmd](args)


if __name__ == '__main__':
    sys.exit(main())
