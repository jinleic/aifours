#!/usr/bin/env python3
"""stageC_launch_v3 -- SEQUENTIAL Stage C launcher for lane sun-coset7: K62, then K63. EXPLORATORY.

Written under the parent HOLD of 2026-10-18; it may be executed only after an explicit parent GO.
Usage:  python3 code/stageC_launch_v3.py ENGINE_PATH ENGINE_SHA256 BUDGET_SECONDS

v3 = v2 made sequential for the 2-process cap: this launcher plus at most ONE other process at any time
(one admission check, or one engine child). No ps or other helper is spawned while an engine runs.
Fail closed; never retries; no timeouts; never SIGKILL; never signals a bare PID.
 1. Refuse unless ENGINE_SHA256 matches the engine file, 0 < BUDGET <= 3600, and no output directory exists.
 2. Create the record directory evidence/stageC-launch-v3-<stamp>/ (exclusive).
 3. For U in (K62, K63), strictly in order:
    a. open U's stdout/stderr files exclusively;
    b. clock: now <= 17:29:00 PDT; effective budget = min(BUDGET, 17:57:00 PDT - now - 600 s), refuse if < 300 s;
    c. FRESH admission_v2 for U, projected growth = 16 MiB x (children not yet run, U included); it must
       exit 0 AND its receipt must read PASS;
    d. re-read statvfs (>= 12.2e9 + that growth) and the clock immediately before spawning;
    e. spawn the engine with subprocess.Popen (argument list, no shell, stdin=DEVNULL, own files, TMPDIR in
       the lane);
    f. supervise through the owned handle only: poll() every 10 s (while poll() returns None the child is
       unreaped, so its PID cannot be recycled); a SIGTERM received by this launcher is forwarded ONCE to the
       current child through Popen.send_signal, which re-polls first;
    g. settle: return code, time, the kernel's RUSAGE_CHILDREN peak RSS (max over all reaped children so
       far), and the engine's run.json fields.
    The sequence stops -- no later admission and no later child -- on any refusal in b-d, a non-zero return
    code, a missing or unreadable run.json, a post-hoc peak RSS >= 1 GiB, or a received SIGTERM.
 4. summary.json (exclusive) records every step; supervise.jsonl logs each poll.
The per-process RSS cap (0.9 GiB) and the 12.0e9 in-flight disk floor are enforced cooperatively inside the
v3 engine (20 s checks); this launcher verifies the RSS cap after each child from kernel rusage.
"""
import datetime
import hashlib
import json
import os
import resource
import signal
import subprocess
import sys
import time

LANE = '/Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261016/sun-coset7'
MON = '/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/disk-monitor-v1-20261018T0722-to-1810.jsonl'
ADMISSION = os.path.join(LANE, 'code', 'admission_v2.py')
UNIVERSES = ('K62', 'K63')
OUT_CAP = 16 * 1024 * 1024
RSS_CAP_BYTES = 1024 ** 3
LAUNCH_DEADLINE = datetime.datetime.fromisoformat('2026-10-18T17:29:00-07:00').timestamp()
NATIVE_END = datetime.datetime.fromisoformat('2026-10-18T17:57:00-07:00').timestamp()
MIN_BUDGET = 300
POLL_EVERY = 10
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


def children_peak_rss():
    """Kernel peak RSS over all reaped children of this launcher (ru_maxrss: bytes on macOS, KiB on Linux)."""
    r = resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss
    return r if sys.platform == 'darwin' else r * 1024


def budget_now(budget):
    return min(budget, int(NATIVE_END - time.time() - 600))


def main():
    engine, engine_sha, budget = os.path.abspath(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    t_start = time.time()
    summary = {'launcher': 'stageC_launch_v3', 'launcher_sha256': sha_file(os.path.abspath(__file__)),
               'started': now_local(), 'python': sys.executable, 'engine': engine, 'engine_sha256_expected': engine_sha,
               'budget_requested_s': budget, 'universes': list(UNIVERSES), 'mode': 'sequential',
               'result': None, 'stopped_because': None, 'refusal': [], 'steps': {}}
    refusal = summary['refusal']
    summary['engine_sha256_actual'] = sha_file(engine)
    if summary['engine_sha256_actual'] != engine_sha:
        refusal.append('engine sha256 mismatch')
    if not 0 < budget <= 3600:
        refusal.append('budget outside (0, 3600]')
    outdirs = {u: os.path.join(LANE, 'evidence', 'stageC-%s' % u) for u in UNIVERSES}
    for u, d in outdirs.items():
        if os.path.exists(d):
            refusal.append('output directory exists: %s' % d)
    stamp = datetime.datetime.fromtimestamp(t_start).strftime('%Y%m%dT%H%M%S')
    rec = os.path.join(LANE, 'evidence', 'stageC-launch-v3-%s' % stamp)
    os.mkdir(rec)
    summary_path = os.path.join(rec, 'summary.json')
    if refusal:
        summary['result'], summary['stopped_because'] = 'REFUSED', 'pre-checks'
        write_json_x(summary_path, summary)
        print(json.dumps({'result': 'REFUSED', 'refusal': refusal, 'record': rec}))
        return
    signal.signal(signal.SIGTERM, lambda s, f: TERM_FLAG.__setitem__(0, True))
    log = open(os.path.join(rec, 'supervise.jsonl'), 'x')
    env = dict(os.environ)
    env['TMPDIR'] = os.path.join(LANE, 'tmp')
    spawned = 0
    for idx, u in enumerate(UNIVERSES):
        step = {'universe': u, 'refusal': []}
        summary['steps'][u] = step
        if TERM_FLAG[0]:
            step['refusal'].append('launcher received SIGTERM before this child')
            summary['stopped_because'] = 'SIGTERM'
            break
        fo = open(os.path.join(rec, '%s.stdout' % u), 'x')
        fe = open(os.path.join(rec, '%s.stderr' % u), 'x')
        eff = budget_now(budget)
        growth = OUT_CAP * (len(UNIVERSES) - idx)
        step.update({'budget_effective_s': eff, 'projected_growth_bytes': growth, 'clock_check_at': now_local()})
        if time.time() > LAUNCH_DEADLINE:
            step['refusal'].append('after 17:29:00 PDT launch deadline')
        if eff < MIN_BUDGET:
            step['refusal'].append('effective budget %d s < %d s' % (eff, MIN_BUDGET))
        if not step['refusal']:
            rpath = os.path.join(rec, 'admission-%s.json' % u)
            r = subprocess.run([sys.executable, ADMISSION, MON, rpath, str(growth)], stdin=subprocess.DEVNULL,
                               capture_output=True, text=True)
            result = None
            if os.path.exists(rpath):
                try:
                    with open(rpath) as f:
                        result = json.load(f).get('result')
                except Exception:
                    result = None
            step['admission'] = {'exit': r.returncode, 'receipt': rpath, 'result': result,
                                 'receipt_sha256': sha_file(rpath) if os.path.exists(rpath) else None,
                                 'stdout': r.stdout[-2000:], 'stderr': r.stderr[-2000:]}
            if r.returncode != 0 or result != 'PASS':
                step['refusal'].append('admission did not PASS (exit %d, result %s)' % (r.returncode, result))
        if not step['refusal']:
            f_now = free_bytes()
            eff = min(eff, budget_now(budget))
            step['pre_spawn'] = {'free_bytes': f_now, 'at': now_local(), 'budget_effective_s': eff}
            if f_now < 12.2e9 + growth:
                step['refusal'].append('pre-spawn statvfs %d < 12.2e9 + growth' % f_now)
            if time.time() > LAUNCH_DEADLINE or eff < MIN_BUDGET:
                step['refusal'].append('pre-spawn clock outside the launch window')
            if TERM_FLAG[0]:
                step['refusal'].append('launcher received SIGTERM before spawning')
        if step['refusal']:
            fo.close()
            fe.close()
            summary['stopped_because'] = 'refusal before %s' % u
            break
        argv = [sys.executable, engine, u, outdirs[u], str(eff)]
        h = subprocess.Popen(argv, cwd=LANE, stdin=subprocess.DEVNULL, stdout=fo, stderr=fe, env=env, close_fds=True)
        spawned += 1
        step.update({'argv': argv, 'pid': h.pid, 'spawned': now_local(), 'signals': []})
        forwarded = False
        while True:
            rc = h.poll()
            if rc is not None:
                break
            if TERM_FLAG[0] and not forwarded:
                forwarded = True
                if h.poll() is None:
                    h.send_signal(signal.SIGTERM)
                    step['signals'].append({'sig': 'SIGTERM', 'why': 'launcher received SIGTERM', 'at': now_local()})
            log.write(json.dumps({'at': now_local(), 'u': u, 'pid': h.pid, 'running': True,
                                  'free_bytes': free_bytes()}) + '\n')
            log.flush()
            time.sleep(POLL_EVERY)
        fo.close()
        fe.close()
        step['settled'], step['returncode'] = now_local(), rc
        step['children_peak_rss_bytes'] = children_peak_rss()
        rj = os.path.join(outdirs[u], 'run.json')
        run_ok = False
        if os.path.exists(rj):
            try:
                with open(rj) as f:
                    run = json.load(f)
                step['run_json'] = {'sha256': sha_file(rj), 'status': run.get('status'),
                                    'stop_reason': run.get('stop_reason'), 'engine_sha256': run.get('engine_sha256'),
                                    'profiles_total': run.get('profiles_total'),
                                    'profiles_done': run.get('stats', {}).get('profiles_done'),
                                    'profile_in_progress': run.get('stats', {}).get('profile_in_progress'),
                                    'survivor_count': run.get('survivor_count'), 'note': run.get('note')}
                run_ok = True
            except Exception as e:
                step['run_json'] = {'error': repr(e)}
        log.write(json.dumps({'at': now_local(), 'u': u, 'event': 'settled', 'returncode': rc}) + '\n')
        log.flush()
        if rc != 0:
            summary['stopped_because'] = 'child %s returned %s' % (u, rc)
        elif not run_ok:
            summary['stopped_because'] = 'child %s left no readable run.json' % u
        elif step['children_peak_rss_bytes'] >= RSS_CAP_BYTES:
            summary['stopped_because'] = 'post-hoc kernel peak RSS >= 1 GiB after %s' % u
        elif TERM_FLAG[0]:
            summary['stopped_because'] = 'SIGTERM'
        if summary['stopped_because']:
            break
    log.close()
    summary['result'] = 'REFUSED' if spawned == 0 else 'FINISHED'
    summary['finished'] = now_local()
    write_json_x(summary_path, summary)
    print(json.dumps({'result': summary['result'], 'stopped_because': summary['stopped_because'], 'record': rec,
                      'steps': {u: {k: s.get(k) for k in ('refusal', 'returncode', 'run_json', 'children_peak_rss_bytes')}
                                for u, s in summary['steps'].items()}}, default=str))


if __name__ == '__main__':
    main()
