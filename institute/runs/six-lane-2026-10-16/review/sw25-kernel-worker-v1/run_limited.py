#!/usr/bin/env python3
"""Run one command under host-native resource guards with live RSS sampling (stdlib only).

Guards (no SIGKILL, ever):
  * resident set size of the whole process tree (the child plus its descendants), sampled with
    `ps -A -o pid=,ppid=,rss=` every SAMPLE_S seconds;
  * wall time.
If a cap is exceeded the child receives SIGTERM, followed by a bounded wait of TERM_WAIT_S seconds.
stdout/stderr go to NEW files (O_EXCL: an existing file is never overwritten).
The child is reaped with os.wait4, which yields its own exact ru_maxrss (bytes on macOS) and CPU times.

Script usage:
  python3 -B run_limited.py RECEIPT.json STDOUT STDERR RSS_CAP_BYTES WALL_CAP_S CWD -- CMD [ARGS...]
The receipt (JSON, created exclusively) is also printed.  The child's environment is inherited.
"""
import json
import os
import signal
import subprocess
import sys
import time

SAMPLE_S = 0.25
TERM_WAIT_S = 60.0
KEEP_EVERY_S = 2.0


def host_time():
    return subprocess.run(['date', '+%Y-%m-%d %H:%M:%S %Z'], capture_output=True, text=True).stdout.strip()


def tree_rss_bytes(root):
    out = subprocess.run(['ps', '-A', '-o', 'pid=,ppid=,rss='], capture_output=True, text=True).stdout
    kids, rss = {}, {}
    for line in out.splitlines():
        parts = line.split()
        if len(parts) != 3:
            continue
        try:
            pid, ppid, kib = int(parts[0]), int(parts[1]), int(parts[2])
        except ValueError:
            continue
        kids.setdefault(ppid, []).append(pid)
        rss[pid] = kib * 1024
    total, stack, seen = 0, [root], set()
    while stack:
        p = stack.pop()
        if p in seen:
            continue
        seen.add(p)
        total += rss.get(p, 0)
        stack.extend(kids.get(p, []))
    return total, len(seen)


def run(argv, cwd, stdout_path, stderr_path, rss_cap, wall_cap, env=None):
    """Run argv; return a receipt dict.  Never raises on child failure."""
    out_f = open(stdout_path, 'x')
    err_f = open(stderr_path, 'x')
    started = host_time()
    t0 = time.monotonic()
    proc = subprocess.Popen(argv, cwd=cwd, env=env, stdin=subprocess.DEVNULL, stdout=out_f, stderr=err_f)
    out_f.close()
    err_f.close()
    peak, peak_procs, nsamples, kept = 0, 0, 0, []
    term_reason, term_at, last_keep = None, None, -KEEP_EVERY_S
    status, ru, abandoned = None, None, False
    while True:
        wpid, wstatus, wru = os.wait4(proc.pid, os.WNOHANG)
        if wpid == proc.pid:
            status, ru = wstatus, wru
            break
        elapsed = time.monotonic() - t0
        rss, nprocs = tree_rss_bytes(proc.pid)
        nsamples += 1
        if rss > peak:
            peak, peak_procs = rss, nprocs
        if elapsed - last_keep >= KEEP_EVERY_S:
            kept.append([round(elapsed, 2), rss])
            last_keep = elapsed
        if term_reason is None and (rss > rss_cap or elapsed > wall_cap):
            term_reason = 'rss_cap' if rss > rss_cap else 'wall_cap'
            term_at = time.monotonic()
            os.kill(proc.pid, signal.SIGTERM)
        elif term_reason is not None and time.monotonic() - term_at > TERM_WAIT_S:
            abandoned = True  # bounded wait expired; no SIGKILL by policy
            break
        time.sleep(SAMPLE_S)
    wall = time.monotonic() - t0
    rec = {
        'argv': argv, 'cwd': str(cwd), 'started_at': started, 'finished_at': host_time(),
        'wall_seconds': round(wall, 3), 'rss_cap_bytes': rss_cap, 'wall_cap_seconds': wall_cap,
        'sample_interval_seconds': SAMPLE_S, 'samples': nsamples,
        'sampled_peak_tree_rss_bytes': peak, 'processes_in_tree_at_peak': peak_procs,
        'kept_samples_elapsed_rss': kept, 'terminated_by_guard': term_reason,
        'abandoned_after_bounded_wait': abandoned,
        'stdout': str(stdout_path), 'stderr': str(stderr_path),
    }
    if status is not None:
        proc.returncode = os.waitstatus_to_exitcode(status)
        rec.update({
            'exit_code': proc.returncode,
            'ru_maxrss_bytes': ru.ru_maxrss,
            'user_cpu_seconds': round(ru.ru_utime, 3), 'system_cpu_seconds': round(ru.ru_stime, 3),
            'cpu_seconds_per_wall_second': round((ru.ru_utime + ru.ru_stime) / wall, 3) if wall > 0 else None,
        })
    else:
        rec['exit_code'] = None
    return rec


def main(argv):
    if len(argv) < 9 or argv[7] != '--':
        raise SystemExit(__doc__)
    receipt, out, err, cap, wall, cwd = argv[1], argv[2], argv[3], int(argv[4]), float(argv[5]), argv[6]
    rec = run(argv[8:], cwd, out, err, cap, wall)
    with open(receipt, 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps({k: v for k, v in rec.items() if k != 'kept_samples_elapsed_rss'}, indent=1))
    return 0 if rec['exit_code'] == 0 else 1


if __name__ == '__main__':
    raise SystemExit(main(sys.argv))
