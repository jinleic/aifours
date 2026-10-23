#!/usr/bin/env python3
"""smoke_v3_v1 -- focused stop / small-output smoke for core7_engine_v3 (lane sun-coset7).

A sanity control, never gate evidence. Written under the parent HOLD; it may be executed only after an
explicit parent GO, when the parent's checkers no longer hold the math-1 process slots.
Usage:  python3 code/smoke_v3_v1.py ENGINE_SHA256

Sequential: this harness plus at most ONE engine child at any time; no other helper process.
No timeouts; never SIGKILL; signals only through the owned Popen handle.
Before each child: clock <= 17:29:00 PDT and fresh statvfs >= 12.2e9 + 16 MiB, else the remaining cases
are refused. Cases:
 S1 budget stop    KII, budget 20 s.     Expect rc 0, UNKNOWN, stop_reason 'self-budget 20s exceeded',
                   0 <= profiles_done < profiles_total, profile_in_progress set, the 4 certificate files plus
                   run.json present, outputs < 16 MiB.
 S2 SIGTERM stop   KII, budget 600 s; one SIGTERM through Popen.send_signal 15 s after spawn.
                   Expect rc 0, UNKNOWN, stop_reason 'SIGTERM received (cooperative stop)', sigterm_received
                   true, profile_in_progress set, all files present.
 S3 COMPLETE       MSP45, budget 60 s.   Expect COMPLETE and, against the frozen Stage A v1 outputs
                   (evidence/stageA-MSP45): equal stats (v1 keys), survivors, decompressed vfc_killed,
                   non-empty leaf lines, and the parsed lp_duals object (key set and values).
 S4 COMPLETE       X1, budget 120 s.     The same comparisons against evidence/stageA-X1.
The harness stops after the first case whose child exits non-zero or leaves no readable run.json.
Records: evidence/smoke-v3-<stamp>/ (exclusive): per-case stdout/stderr, summary.json with expectations,
observations and PASS/FAIL per check.
"""
import datetime
import gzip
import hashlib
import json
import os
import signal
import subprocess
import sys
import time

LANE = '/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7'
ENGINE = os.path.join(LANE, 'code', 'core7_engine_v3.py')
LAUNCH_DEADLINE = datetime.datetime.fromisoformat('2026-10-18T17:29:00-07:00').timestamp()
GROWTH = 16 * 1024 * 1024
CERT_FILES = ('leaves.jsonl.gz', 'vfc_killed.json.gz', 'lp_duals.json.gz', 'survivors.json')
CASES = (
    ('S1', 'KII', 20, None, None),
    ('S2', 'KII', 600, 15, None),
    ('S3', 'MSP45', 60, None, 'stageA-MSP45'),
    ('S4', 'X1', 120, None, 'stageA-X1'),
)


def now_local():
    return datetime.datetime.now().astimezone().isoformat(timespec='seconds')


def sha_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def free_bytes():
    st = os.statvfs(LANE)
    return st.f_bavail * st.f_frsize


def load_outputs(d):
    out = {}
    with open(os.path.join(d, 'run.json')) as f:
        out['run'] = json.load(f)
    with open(os.path.join(d, 'survivors.json')) as f:
        out['survivors'] = json.load(f)
    with open(os.path.join(d, 'vfc_killed.json.gz'), 'rb') as f:
        out['vfc'] = json.loads(gzip.decompress(f.read()))
    with open(os.path.join(d, 'lp_duals.json.gz'), 'rb') as f:
        out['duals'] = json.loads(gzip.decompress(f.read()))
    with open(os.path.join(d, 'leaves.jsonl.gz'), 'rb') as f:
        out['leaves'] = [x for x in gzip.decompress(f.read()).decode().split('\n') if x]
    return out


def main():
    engine_sha = sys.argv[1]
    t0 = time.time()
    summary = {'harness': 'smoke_v3_v1', 'harness_sha256': sha_file(os.path.abspath(__file__)), 'started': now_local(),
               'engine': ENGINE, 'engine_sha256_expected': engine_sha, 'engine_sha256_actual': sha_file(ENGINE),
               'exploratory_control': True, 'cases': {}, 'stopped_because': None}
    rec = os.path.join(LANE, 'evidence', 'smoke-v3-%s' % datetime.datetime.fromtimestamp(t0).strftime('%Y%m%dT%H%M%S'))
    os.mkdir(rec)
    if summary['engine_sha256_actual'] != engine_sha:
        summary['stopped_because'] = 'engine sha256 mismatch'
    for name, univ, budget, term_after, ref in CASES:
        if summary['stopped_because']:
            break
        case = {'universe': univ, 'budget_s': budget, 'sigterm_after_s': term_after, 'reference': ref, 'checks': {}}
        summary['cases'][name] = case
        f_now = free_bytes()
        case['pre_spawn'] = {'free_bytes': f_now, 'at': now_local()}
        if time.time() > LAUNCH_DEADLINE or f_now < 12.2e9 + GROWTH:
            case['refused'] = 'clock past 17:29:00 PDT or statvfs below 12.2e9 + 16 MiB'
            summary['stopped_because'] = 'refusal before %s' % name
            break
        outdir = os.path.join(rec, name + '-' + univ)
        fo = open(os.path.join(rec, name + '.stdout'), 'x')
        fe = open(os.path.join(rec, name + '.stderr'), 'x')
        argv = [sys.executable, ENGINE, univ, outdir, str(budget)]
        env = dict(os.environ)
        env['TMPDIR'] = os.path.join(LANE, 'tmp')
        h = subprocess.Popen(argv, cwd=LANE, stdin=subprocess.DEVNULL, stdout=fo, stderr=fe, env=env, close_fds=True)
        t_spawn = time.time()
        case.update({'argv': argv, 'pid': h.pid, 'spawned': now_local()})
        signalled = False
        while True:
            rc = h.poll()
            if rc is not None:
                break
            if term_after is not None and not signalled and time.time() - t_spawn >= term_after:
                signalled = True
                if h.poll() is None:
                    h.send_signal(signal.SIGTERM)
                    case['sigterm_sent'] = now_local()
            time.sleep(1)
        fo.close()
        fe.close()
        case['returncode'], case['settled'] = rc, now_local()
        try:
            got = load_outputs(outdir)
        except Exception as e:
            case['load_error'] = repr(e)
            summary['stopped_because'] = 'outputs of %s unreadable' % name
            break
        run = got['run']
        st = run.get('stats', {})
        case['observed'] = {k: run.get(k) for k in ('status', 'stop_reason', 'engine_sha256', 'sigterm_received', 'note',
                                                   'peak_rss_bytes_at_write', 'output_sha256')}
        case['observed'].update({'profiles_total': run.get('profiles_total'), 'profiles_done': st.get('profiles_done'),
                                 'profile_in_progress': st.get('profile_in_progress')})
        size = sum(os.path.getsize(os.path.join(outdir, x)) for x in os.listdir(outdir))
        c = case['checks']
        c['rc0'] = rc == 0
        c['engine_sha_recorded'] = run.get('engine_sha256') == engine_sha
        c['all_files_present'] = all(os.path.exists(os.path.join(outdir, x)) for x in CERT_FILES + ('run.json',))
        c['outputs_lt_16MiB'] = size < GROWTH
        if name == 'S1':
            c['unknown'] = run.get('status') == 'UNKNOWN'
            c['reason_budget'] = run.get('stop_reason') == 'self-budget 20s exceeded'
            c['frontier'] = (isinstance(st.get('profiles_done'), int) and 0 <= st['profiles_done'] < run.get('profiles_total', 0)
                             and st.get('profile_in_progress') is not None)
        elif name == 'S2':
            c['signal_sent'] = 'sigterm_sent' in case
            c['unknown'] = run.get('status') == 'UNKNOWN'
            c['reason_sigterm'] = run.get('stop_reason') == 'SIGTERM received (cooperative stop)'
            c['flag_recorded'] = run.get('sigterm_received') is True
            c['frontier'] = (isinstance(st.get('profiles_done'), int) and 0 <= st['profiles_done'] < run.get('profiles_total', 0)
                             and st.get('profile_in_progress') is not None)
        else:
            refd = load_outputs(os.path.join(LANE, 'evidence', ref))
            c['complete'] = run.get('status') == 'COMPLETE' and st.get('profile_in_progress') is None
            c['stats_equal_v1'] = all(st.get(k) == v for k, v in refd['run']['stats'].items())
            c['survivors_equal_v1'] = got['survivors'] == refd['survivors']
            c['vfc_killed_equal_v1'] = got['vfc'] == refd['vfc']
            c['leaf_lines_equal_v1'] = got['leaves'] == refd['leaves']
            c['lp_duals_equal_v1'] = got['duals'] == refd['duals']
        case['pass'] = all(c.values())
        if rc != 0:
            summary['stopped_because'] = 'child %s returned %s' % (name, rc)
    summary['all_pass'] = bool(summary['cases']) and all(x.get('pass') for x in summary['cases'].values()) and \
        len(summary['cases']) == len(CASES) and not summary['stopped_because']
    summary['finished'] = now_local()
    with open(os.path.join(rec, 'summary.json'), 'x') as f:
        json.dump(summary, f, indent=1, default=str)
    print(json.dumps({'record': rec, 'all_pass': summary['all_pass'], 'stopped_because': summary['stopped_because'],
                      'cases': {k: {'pass': v.get('pass'), 'checks': v.get('checks')} for k, v in summary['cases'].items()}}))


if __name__ == '__main__':
    main()
