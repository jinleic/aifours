#!/usr/bin/env python3
"""stageC_launch_v2 -- Stage C launcher for lane sun-coset7 (K62 and K63 only). EXPLORATORY.

Written under the parent HOLD of 2026-10-18; it may be executed only after an explicit parent GO.
Usage:  python3 code/stageC_launch_v2.py ENGINE_PATH ENGINE_SHA256 BUDGET_SECONDS

Fail closed; never retries; no timeouts; never SIGKILL; never signals a bare PID.
 1. Refuse unless ENGINE_SHA256 matches the engine file, 0 < BUDGET <= 3600, now <= 17:29:00 PDT and
    now + BUDGET + 600 s <= 17:57:00 PDT (2026-10-18), and neither output directory exists.
 2. Create the record directory evidence/stageC-launch-v2-<stamp>/ (exclusive) and open every engine
    stdout/stderr file exclusively BEFORE admission.
 3. Run admission_v2 for K62 and then K63; both must exit 0 AND their receipts must read PASS.
    Otherwise write summary.json (REFUSED) and launch nothing.
 4. Immediately before spawning, re-read statvfs (>= 12.2e9 + projected growth) and the clock (<= 17:29).
 5. Spawn both engines with subprocess.Popen (argument list, no shell, stdin=DEVNULL, own files,
    TMPDIR inside the lane). The Popen handles are the only process identities used: while poll() returns
    None the child is unreaped, so its PID cannot be recycled; Popen.send_signal re-polls first.
 6. Every 10 s, for each unsettled child: poll(); if still running, read `ps -ww -o ppid=,rss=,command= -p PID`
    and verify ppid == this launcher and the exact engine argv. A verified RSS >= 1 GiB, or 3 consecutive
    unverifiable samples, sends ONE SIGTERM through the handle (the v3 engine treats it as a cooperative
    stop and writes UNKNOWN with its exact frontier). A SIGTERM received by this launcher is forwarded
    once to both children in the same way. No escalation ever.
 7. Settlement: return code, end time and the engine's run.json fields per child; summary.json (exclusive).
"""
import datetime
import hashlib
import json
import os
import signal
import subprocess
import sys
import time

LANE = '/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7'
MON = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/disk-monitor-v1-20261018T0722-to-1810.jsonl'
ADMISSION = os.path.join(LANE, 'code', 'admission_v2.py')
UNIVERSES = ('K62', 'K63')
GROWTH = 2 * 16 * 1024 * 1024
RSS_CAP_KB = 1024 * 1024
LAUNCH_DEADLINE = datetime.datetime.fromisoformat('2026-10-18T17:29:00-07:00').timestamp()
NATIVE_END = datetime.datetime.fromisoformat('2026-10-18T17:57:00-07:00').timestamp()
SAMPLE_EVERY = 10
TERM_FLAG = [False]


def now_local():
    return datetime.datetime.now().astimezone().isoformat(timespec='seconds')


def sha_file(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def free_bytes():
    st = os.statvfs(LANE)
    return st.f_bavail * st.f_frsize


def write_json_x(path, obj):
    with open(path, 'x') as f:
        json.dump(obj, f, indent=1, default=str)


def ps_sample(pid):
    """Returns (ppid, rss_kb, command) or None if ps fails or its output is malformed."""
    r = subprocess.run(['/bin/ps', '-ww', '-o', 'ppid=,rss=,command=', '-p', str(pid)],
                       stdin=subprocess.DEVNULL, capture_output=True, text=True)
    if r.returncode != 0:
        return None
    lines = [x for x in r.stdout.splitlines() if x.strip()]
    if len(lines) != 1:
        return None
    parts = lines[0].split(None, 2)
    if len(parts) != 3 or not parts[0].isdigit() or not parts[1].isdigit():
        return None
    return int(parts[0]), int(parts[1]), parts[2]


def main():
    engine, engine_sha, budget = os.path.abspath(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    t_start = time.time()
    summary = {'launcher': 'stageC_launch_v2', 'launcher_sha256': sha_file(os.path.abspath(__file__)),
               'started': now_local(), 'python': sys.executable, 'engine': engine, 'engine_sha256_expected': engine_sha,
               'budget_s': budget, 'universes': list(UNIVERSES), 'projected_growth_bytes': GROWTH,
               'rss_cap_kb': RSS_CAP_KB, 'result': None, 'refusal': [], 'admission': {}, 'children': {}}
    refusal = summary['refusal']
    actual_sha = sha_file(engine)
    summary['engine_sha256_actual'] = actual_sha
    if actual_sha != engine_sha:
        refusal.append('engine sha256 mismatch')
    if not 0 < budget <= 3600:
        refusal.append('budget outside (0, 3600]')
    if t_start > LAUNCH_DEADLINE:
        refusal.append('after 17:29:00 PDT launch deadline')
    if t_start + budget + 600 > NATIVE_END:
        refusal.append('budget + 600 s would pass 17:57:00 PDT')
    outdirs = {u: os.path.join(LANE, 'evidence', 'stageC-%s' % u) for u in UNIVERSES}
    for u, d in outdirs.items():
        if os.path.exists(d):
            refusal.append('output directory exists: %s' % d)
    stamp = datetime.datetime.fromtimestamp(t_start).strftime('%Y%m%dT%H%M%S')
    rec = os.path.join(LANE, 'evidence', 'stageC-launch-v2-%s' % stamp)
    os.mkdir(rec)
    summary_path = os.path.join(rec, 'summary.json')
    if refusal:
        summary['result'] = 'REFUSED'
        write_json_x(summary_path, summary)
        print(json.dumps({'result': 'REFUSED', 'refusal': refusal, 'record': rec}))
        return
    files = {}
    for u in UNIVERSES:
        files[u] = (open(os.path.join(rec, '%s.stdout' % u), 'x'), open(os.path.join(rec, '%s.stderr' % u), 'x'))
    log = open(os.path.join(rec, 'supervise.jsonl'), 'x')
    # admission (both, back to back)
    for u in UNIVERSES:
        rpath = os.path.join(rec, 'admission-%s.json' % u)
        r = subprocess.run([sys.executable, ADMISSION, MON, rpath, str(GROWTH)], stdin=subprocess.DEVNULL,
                           capture_output=True, text=True)
        result = None
        if os.path.exists(rpath):
            try:
                with open(rpath) as f:
                    result = json.load(f).get('result')
            except Exception:
                result = None
        summary['admission'][u] = {'exit': r.returncode, 'receipt': rpath, 'result': result,
                                   'receipt_sha256': sha_file(rpath) if os.path.exists(rpath) else None,
                                   'stdout': r.stdout[-2000:], 'stderr': r.stderr[-2000:]}
        if r.returncode != 0 or result != 'PASS':
            refusal.append('admission %s did not PASS (exit %d, result %s)' % (u, r.returncode, result))
    if not refusal:
        f_now, t_now = free_bytes(), time.time()
        summary['pre_spawn'] = {'free_bytes': f_now, 'at': now_local()}
        if f_now < 12.2e9 + GROWTH:
            refusal.append('pre-spawn statvfs %d < 12.2e9 + growth' % f_now)
        if t_now > LAUNCH_DEADLINE or t_now + budget + 600 > NATIVE_END:
            refusal.append('pre-spawn clock past the launch window')
    if refusal:
        summary['result'] = 'REFUSED'
        for fo, fe in files.values():
            fo.close()
            fe.close()
        log.close()
        write_json_x(summary_path, summary)
        print(json.dumps({'result': 'REFUSED', 'refusal': refusal, 'record': rec}))
        return
    signal.signal(signal.SIGTERM, lambda s, f: TERM_FLAG.__setitem__(0, True))
    env = dict(os.environ)
    env['TMPDIR'] = os.path.join(LANE, 'tmp')
    handles = {}
    for u in UNIVERSES:
        argv = [sys.executable, engine, u, outdirs[u], str(budget)]
        h = subprocess.Popen(argv, cwd=LANE, stdin=subprocess.DEVNULL, stdout=files[u][0], stderr=files[u][1],
                             env=env, close_fds=True)
        handles[u] = h
        ident = ps_sample(h.pid)
        summary['children'][u] = {'argv': argv, 'pid': h.pid, 'spawned': now_local(), 'spawn_epoch': time.time(),
                                  'spawn_ps': list(ident) if ident else None, 'signals': [], 'bad_samples': 0,
                                  'max_rss_kb': 0, 'settled': None, 'returncode': None, 'run_json': None}
    summary['result'] = 'LAUNCHED'
    forwarded = False
    while True:
        open_children = [u for u in UNIVERSES if summary['children'][u]['settled'] is None]
        if not open_children:
            break
        if TERM_FLAG[0] and not forwarded:
            forwarded = True
            for u in open_children:
                if handles[u].poll() is None:
                    handles[u].send_signal(signal.SIGTERM)
                    summary['children'][u]['signals'].append({'sig': 'SIGTERM', 'why': 'launcher received SIGTERM',
                                                              'at': now_local(), 'epoch': time.time()})
        for u in open_children:
            c, h = summary['children'][u], handles[u]
            rc = h.poll()
            if rc is not None:
                c['settled'], c['returncode'] = now_local(), rc
                rj = os.path.join(outdirs[u], 'run.json')
                if os.path.exists(rj):
                    try:
                        with open(rj) as f:
                            run = json.load(f)
                        c['run_json'] = {'sha256': sha_file(rj), 'status': run.get('status'),
                                         'stop_reason': run.get('stop_reason'),
                                         'profiles_total': run.get('profiles_total'),
                                         'profiles_done': run.get('stats', {}).get('profiles_done'),
                                         'profile_in_progress': run.get('stats', {}).get('profile_in_progress'),
                                         'survivor_count': run.get('survivor_count')}
                    except Exception as e:
                        c['run_json'] = {'error': repr(e)}
                log.write(json.dumps({'at': now_local(), 'u': u, 'event': 'settled', 'returncode': rc}) + '\n')
                log.flush()
                continue
            s = ps_sample(h.pid)
            expected = ' '.join(c['argv'][1:])
            ok = s is not None and s[0] == os.getpid() and expected in s[2]
            entry = {'at': now_local(), 'u': u, 'pid': h.pid, 'verified': ok, 'rss_kb': s[1] if s else None,
                     'free_bytes': free_bytes()}
            sent = [x['why'] for x in c['signals']]
            if ok:
                c['bad_samples'] = 0
                c['max_rss_kb'] = max(c['max_rss_kb'], s[1])
                if s[1] >= RSS_CAP_KB and not sent:
                    if h.poll() is None:
                        h.send_signal(signal.SIGTERM)
                        c['signals'].append({'sig': 'SIGTERM', 'why': 'RSS %d KiB >= 1 GiB' % s[1],
                                             'at': now_local(), 'epoch': time.time()})
            else:
                c['bad_samples'] += 1
                if c['bad_samples'] >= 3 and not sent:
                    if h.poll() is None:
                        h.send_signal(signal.SIGTERM)
                        c['signals'].append({'sig': 'SIGTERM', 'why': '3 consecutive unverifiable RSS samples',
                                             'at': now_local(), 'epoch': time.time()})
            if c['signals'] and time.time() - c['signals'][0]['epoch'] > 300 and not c.get('late_noted'):
                c['late_noted'] = now_local()
                entry['note'] = 'not settled 300 s after SIGTERM; no further signal (never SIGKILL)'
            log.write(json.dumps(entry) + '\n')
            log.flush()
        time.sleep(SAMPLE_EVERY)
    for fo, fe in files.values():
        fo.close()
        fe.close()
    log.close()
    summary['finished'] = now_local()
    write_json_x(summary_path, summary)
    print(json.dumps({'result': summary['result'], 'record': rec,
                      'children': {u: {k: summary['children'][u][k] for k in ('returncode', 'run_json', 'signals', 'max_rss_kb')}
                                   for u in UNIVERSES}}, default=str))


if __name__ == '__main__':
    main()
