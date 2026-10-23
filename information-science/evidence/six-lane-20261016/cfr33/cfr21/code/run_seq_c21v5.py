#!/usr/bin/env python3
"""Version5 lane runner: v3 heartbeat/stop protocol plus a fresh per-launch disk gate.
Usage: run_seq_c21v5.py JOBS.json OUTDIR [--calibration-continue]
Immediately before EVERY child launch require free>=12.2e9 PLUS that job's
'growth_bytes' (default16MiB). If not, write deferred-job.json, launch nothing
further and exit75 (UNKNOWN-DEFERRED); the caller reports once and waits.
Default: child exit10 (candidate) stops the queue. --calibration-continue
continues past exit10 for KNOWN calibration positives only. Child guard exits
70/74/75 always halt the queue. Heartbeats at most300s apart; SIGTERM at the
frozen18:20 PDT stop time or below the12GB physical floor. No Python child
timeout, Popen.kill, SIGKILL, cron/launchd, or automatic recovery. Each search
child carries its own native limit, at most10800s.
"""
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime
from zoneinfo import ZoneInfo

ZONE = ZoneInfo('America/Los_Angeles')
STOP_AT = datetime(2026, 10, 18, 18, 20, 0, tzinfo=ZONE)
FLOOR = 12_000_000_000
LAUNCH_MIN = 12_200_000_000
DEFAULT_GROWTH = 16 * 1024 ** 2


def clock():
    return datetime.now(ZONE)


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    calibration = sys.argv[3:] == ['--calibration-continue']
    if len(sys.argv) not in (3, 4) or (len(sys.argv) == 4 and not calibration):
        raise SystemExit('usage: run_seq_c21v5.py JOBS OUTDIR [--calibration-continue]')
    jobs = json.loads(Path(sys.argv[1]).read_text())
    out = Path(sys.argv[2])
    os.mkdir(out)
    interval = float(os.environ.get('C21_HEARTBEAT_SECONDS', '300'))
    if not 0.1 <= interval <= 300:
        raise SystemExit('heartbeat interval must be0.1..300s')
    state = {'child': None, 'job': None, 'stop': False, 'reason': None}
    end = threading.Event()
    heartbeat = open(out / 'heartbeat.jsonl', 'x')
    write_lock = threading.Lock()

    def free_bytes():
        s = os.statvfs(out)
        return s.f_bavail * s.f_frsize

    def log_heartbeat(event):
        child = state['child']
        rec = {'clock': clock().isoformat(), 'event': event, 'job': state['job'],
               'child_pid': child.pid if child is not None else None,
               'stop': state['stop'], 'reason': state['reason'], 'free_bytes': free_bytes()}
        with write_lock:
            heartbeat.write(json.dumps(rec) + '\n')
            heartbeat.flush()

    def request_stop(reason):
        state['stop'] = True
        state['reason'] = reason
        child = state['child']
        if child is not None:
            try:
                child.send_signal(signal.SIGTERM)
            except ProcessLookupError:
                pass

    def fwd(signum, frame):
        request_stop('owned SIGTERM/SIGINT forwarding')

    def beat():
        while not end.is_set():
            now = clock()
            if now >= STOP_AT:
                request_stop('frozen lane stop deadline')
            elif free_bytes() < FLOOR:
                request_stop('shared disk floor')
            log_heartbeat('heartbeat')
            remaining = max(0.1, (STOP_AT - now).total_seconds())
            end.wait(min(interval, remaining))

    signal.signal(signal.SIGTERM, fwd)
    signal.signal(signal.SIGINT, fwd)
    with open(out / 'start.json', 'x') as f:
        json.dump({'clock': clock().isoformat(), 'runner_pid': os.getpid(),
                   'runner_sha256': digest(__file__), 'jobs_sha256': digest(sys.argv[1]),
                   'heartbeat_seconds': interval, 'stop_at': STOP_AT.isoformat()}, f, indent=1)
    thread = threading.Thread(target=beat, name='lane-host-clock-checkpoint', daemon=True)
    thread.start()
    candidate, deferred, guard = False, False, 0
    try:
        for job in jobs:
            if clock() >= STOP_AT:
                request_stop('frozen lane stop deadline')
            growth = int(job.get('growth_bytes', DEFAULT_GROWTH))
            available = free_bytes()
            if available < LAUNCH_MIN + growth and not state['stop']:
                with open(out / 'deferred-job.json', 'x') as f:
                    json.dump({'clock': clock().isoformat(), 'verdict': 'UNKNOWN-DEFERRED-DISK-GATE',
                               'job': job, 'free_bytes': available, 'required_free_bytes': LAUNCH_MIN + growth,
                               'child_launched': False}, f, indent=1)
                deferred = True
                break
            if state['stop']:
                break
            state['job'] = job['name']
            cmd = job['cmd']
            exe_sha = digest(cmd[0]) if Path(cmd[0]).is_file() else None
            h0, t0 = clock().isoformat(), time.monotonic()
            path = out / (job['name'] + '.out')
            with open(path, 'xb') as f:
                state['child'] = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT)
                if state['stop']:
                    request_stop(state['reason'])
                log_heartbeat('child-start')
                rc = state['child'].wait()
                state['child'] = None
            rec = {'name': job['name'], 'cmd': cmd, 'exe_sha256': exe_sha,
                   'host_time_start': h0, 'host_time_end': clock().isoformat(),
                   'wall_s': time.monotonic() - t0, 'exit_code': rc,
                   'out_sha256': digest(path), 'stopped': state['stop'], 'stop_reason': state['reason']}
            with open(out / 'records.jsonl', 'a') as f:
                f.write(json.dumps(rec) + '\n')
            log_heartbeat('child-end')
            if rc in (70, 74, 75):
                with open(out / 'guard-halted.json', 'x') as f:
                    json.dump(rec, f, indent=1)
                print('GUARD EXIT: queue halted', json.dumps(rec), flush=True)
                guard = rc
                break
            if rc == 10 and not calibration:
                with open(out / 'candidate-found.json', 'x') as f:
                    json.dump(rec, f, indent=1)
                print('CANDIDATE: stopping queue', json.dumps(rec), flush=True)
                candidate = True
                break
    finally:
        end.set()
        thread.join()
        log_heartbeat('runner-end')
        heartbeat.close()
    result = guard if guard else 10 if candidate else 75 if deferred else 0
    print(json.dumps({'clock': clock().isoformat(), 'queue_exit': result, 'calibration_continue': calibration,
                      'deferred': deferred, 'stop_reason': state['reason']}), flush=True)
    raise SystemExit(result)


if __name__ == '__main__':
    main()
