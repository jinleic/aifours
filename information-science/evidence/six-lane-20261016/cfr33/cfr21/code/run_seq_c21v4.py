#!/usr/bin/env python3
"""Main-thread, fail-closed queue runner with host clocks and bounded stops.
Usage: run_seq_c21v4.py JOBS.json OUTDIR [--calibration-continue]
Default: exit10 stops the queue immediately. Explicit calibration mode continues
past known-positive controls. Guard exits70/74/75 ALWAYS halt, in either mode.
Every Popen has a fresh12GB+64MiB floor check; no automatic recovery/retry.
Heartbeat/disk errors send one SIGTERM and use a<=120s wait, never SIGKILL.
An unreaped child is recorded with PID and an UNKNOWN receipt, exit70, and
must still count against the lane budget. No later job is launched.
Native child time limits remain required; a10675s queue guard reserves shutdown
before a3h chunk and before the frozen18:20 PDT worker stop.
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
import resource
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

ZONE = ZoneInfo('America/Los_Angeles')
STOP_AT = datetime(2026, 10, 18, 18, 20, 0, tzinfo=ZONE)
FLOOR = 12_000_000_000
STOP_REQUEST_AT = STOP_AT - timedelta(seconds=125)


def clock():
    return datetime.now(ZONE)


def digest(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    calibration = len(sys.argv) == 4 and sys.argv[3] == '--calibration-continue'
    if len(sys.argv) not in (3, 4) or (len(sys.argv) == 4 and not calibration):
        raise SystemExit('usage: run_seq_c21v4.py JOBS OUTDIR [--calibration-continue]')
    jobs = json.loads(Path(sys.argv[1]).read_text())
    out = Path(sys.argv[2])
    os.mkdir(out)
    interval = float(os.environ.get('C21_HEARTBEAT_SECONDS', '300'))
    if not 0.1 <= interval <= 300:
        raise SystemExit('heartbeat interval must be0.1..300s')
    state = {'child': None, 'job': None, 'stop': False, 'reason': None, 'term_at': None}
    pause = threading.Event()
    heartbeat = open(out / 'heartbeat.jsonl', 'x')
    records = open(out / 'records.jsonl', 'x')

    def free_bytes():
        s = os.statvfs(out)
        return s.f_bavail * s.f_frsize

    def request_stop(reason):
        state['stop'] = True
        if state['reason'] is None:
            state['reason'] = reason
        child = state['child']
        if child is not None and state['term_at'] is None:
            state['term_at'] = time.monotonic()
            try:
                child.send_signal(signal.SIGTERM)
            except ProcessLookupError:
                pass

    def log_heartbeat(event):
        try:
            child = state['child']
            available = free_bytes()
            if child is not None and available < FLOOR:
                request_stop('shared disk floor')
            rec = {'clock': clock().isoformat(), 'event': event, 'job': state['job'],
                   'child_pid': child.pid if child is not None else None,
                   'stop': state['stop'], 'reason': state['reason'], 'free_bytes': available}
            heartbeat.write(json.dumps(rec) + '\n')
            heartbeat.flush()
            return True
        except Exception as error:
            request_stop('heartbeat/disk supervision failed: ' + repr(error))
            print('SUPERVISION FAILURE', repr(error), flush=True)
            return False

    def fwd(signum, frame):
        request_stop('owned SIGTERM/SIGINT forwarding')

    def limits():
        resource.setrlimit(resource.RLIMIT_FSIZE, (8 * 1024 ** 2, 8 * 1024 ** 2))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))

    signal.signal(signal.SIGTERM, fwd)
    signal.signal(signal.SIGINT, fwd)
    with open(out / 'start.json', 'x') as f:
        json.dump({'clock': clock().isoformat(), 'runner_pid': os.getpid(),
                   'runner_sha256': digest(__file__), 'jobs_sha256': digest(sys.argv[1]),
                   'heartbeat_seconds': interval, 'stop_at': STOP_AT.isoformat(),
                   'stop_request_at': STOP_REQUEST_AT.isoformat(),
                   'calibration_continue': calibration}, f, indent=1)
    result = 0
    try:
        for job in jobs:
            state['job'] = job['name']
            available = free_bytes()
            if clock() >= STOP_REQUEST_AT:
                request_stop('reserved shutdown window before frozen stop')
            if available < FLOOR + 64 * 1024 ** 2:
                request_stop('pre-launch disk floor margin')
            if state['stop']:
                with open(out / 'deferred-job.json', 'x') as f:
                    json.dump({'clock': clock().isoformat(), 'verdict': 'UNKNOWN-DEFERRED',
                               'job': job, 'free_bytes': available, 'reason': state['reason'],
                               'child_launched': False}, f, indent=1)
                result = 75
                break
            cmd = job['cmd']
            exe_sha = digest(cmd[0]) if Path(cmd[0]).is_file() else None
            path = out / (job['name'] + '.out')
            h0, t0 = clock().isoformat(), time.monotonic()
            unreaped, rc = False, None
            with open(path, 'xb') as f:
                # Fresh check immediately before every native child, not just queue start.
                if free_bytes() < FLOOR + 64 * 1024 ** 2:
                    request_stop('immediate pre-launch disk floor margin')
                    result = 75
                    break
                state['child'] = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT,
                                                   preexec_fn=limits, start_new_session=True)
                child = state['child']
                if state['stop']:
                    request_stop(state['reason'])
                log_heartbeat('child-start')
                last = time.monotonic()
                while True:
                    rc = child.poll()
                    if rc is not None:
                        break
                    if clock() >= STOP_REQUEST_AT:
                        request_stop('reserved shutdown window before frozen stop')
                    if time.monotonic() - t0 >= 10675:
                        request_stop('native chunk guard reserves bounded shutdown')
                    if time.monotonic() - last >= interval:
                        last = time.monotonic()
                        log_heartbeat('heartbeat')
                    if state['term_at'] is not None and time.monotonic() - state['term_at'] >= 120:
                        if child.poll() is None:
                            unreaped = True
                            break
                    pause.wait(0.1)
            rec = {'name': job['name'], 'cmd': cmd, 'exe_sha256': exe_sha,
                   'child_pid': child.pid, 'host_time_start': h0, 'host_time_end': clock().isoformat(),
                   'wall_s': time.monotonic() - t0, 'exit_code': rc,
                   'stopped': state['stop'], 'stop_reason': state['reason']}
            if unreaped:
                rec.update(verdict='UNKNOWN-UNREAPED-CHILD', reserved_busy_slots=1,
                           parent_intervention_required=True, queue_must_not_continue=True,
                           out_sha256_at_guard_snapshot=digest(path))
            else:
                rec['out_sha256'] = digest(path)
            records.write(json.dumps(rec) + '\n')
            records.flush()
            if unreaped:
                with open(out / 'unreaped-child.json', 'x') as f:
                    json.dump(rec, f, indent=1)
                print('UNREAPED: queue halted', json.dumps(rec), flush=True)
                result = 70
                break
            state['child'] = None
            log_heartbeat('child-end')
            if rc in (70, 74, 75):
                with open(out / 'guard-halted.json', 'x') as f:
                    json.dump(rec, f, indent=1)
                print('GUARD: queue halted', json.dumps(rec), flush=True)
                result = rc
                break
            if rc == 10 and not calibration:
                with open(out / 'candidate-found.json', 'x') as f:
                    json.dump(rec, f, indent=1)
                print('CANDIDATE: stopping queue', json.dumps(rec), flush=True)
                result = 10
                break
    finally:
        log_heartbeat('runner-end')
        heartbeat.close()
        records.close()
    if state['stop'] and result == 0:
        result = 75
    print(json.dumps({'clock': clock().isoformat(), 'queue_exit': result,
                      'calibration_continue': calibration, 'reason': state['reason']}), flush=True)
    raise SystemExit(result)


if __name__ == '__main__':
    main()
