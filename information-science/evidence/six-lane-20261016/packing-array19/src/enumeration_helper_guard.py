#!/usr/bin/env python3
"""Creation-only owned-child guard for the NEW ms09 enumeration route; proof pipelines are unchanged.
Caller holds all CPU-token/bigmem locks. This function additionally holds the existing helper flock, uses the
frozen stream module's registered spawn/ACTIVE/SPAWNING lifecycle, samples RSS/time/free every<=1s, and SIGTERMs
ONLY its own Popen child on any guard trip. A bounded termination wait is followed by creation-only retained-lock
quarantine until the child exits. Any trip is UNKNOWN even with rc0. No SIGKILL, process discovery or other PID signal.
Production limits: helper1800s, chunk<=10800s with90s shutdown reserve, original run deadline minus90s, sampled5GiB
helper RSS, sampled in-flight free floor12e9. Tiny-child smoke may pass smaller guard values; production wrapper freezes
its exact values. Receipt writes use x-mode and never overwrite. No enumeration or proof-checking algorithm here.
"""
import fcntl
import json
import os
import signal
import subprocess
import time

HELPER_SECONDS = 1800.0
TERM_WAIT = 60.0
SAMPLE_SECONDS = 1.0
SHUTDOWN_RESERVE = 90.0
RSS_CAP_KB = 5 * 1024 * 1024
INFLIGHT_FLOOR_BYTES = 12000000000


def write_json_x(path, value):
    old = signal.pthread_sigmask(signal.SIG_BLOCK, {signal.SIGTERM})
    try:
        with open(path, 'x') as f:
            json.dump(value, f, indent=1)
    finally:
        signal.pthread_sigmask(signal.SIG_SETMASK, old)


def wait_quarantined(S, p, name, receipt_dir, events, interval=1.0):
    started = time.time()
    begin = os.path.join(receipt_dir, 'helper-quarantine-begin-%d-%d.json' % (p.pid, time.time_ns()))
    write_json_x(begin, {'host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'runner_pid': os.getpid(),
                        'child_pid': p.pid, 'child': name, 'reason': 'survived SIGTERM bounded wait',
                        'capacity': 'all caller token/bigmem locks and helper lock retained until owned child exits'})
    while p.poll() is None:
        time.sleep(interval)
    end = os.path.join(receipt_dir, 'helper-quarantine-end-%d-%d.json' % (p.pid, time.time_ns()))
    write_json_x(end, {'host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'child_pid': p.pid,
                      'seconds': round(time.time() - started, 3), 'rc': p.returncode, 'begin': begin})
    events.append({'action': 'quarantine ended', 'pid': p.pid, 'seconds': round(time.time() - started, 3),
                   'begin_receipt': begin, 'end_receipt': end})


def run_helper(S, cmd, receipt_dir, chunk_guard_monotonic, run_guard_wall,
               helper_seconds=HELPER_SECONDS, term_wait=TERM_WAIT, sample_seconds=SAMPLE_SECONDS,
               rss_cap_kb=RSS_CAP_KB, inflight_floor_bytes=INFLIGHT_FLOOR_BYTES):
    """Return rc, output, info; caller treats any guard_tripped as UNKNOWN regardless of rc."""
    reason = S.admitted_reason()
    if reason:
        raise S.AdmissionDenied(reason)
    if time.monotonic() >= chunk_guard_monotonic or time.time() >= run_guard_wall:
        raise S.AdmissionDenied('enumeration chunk/run deadline before helper-lock wait')
    fd = os.open(S.HELPER_LOCK, os.O_CREAT | os.O_RDWR)
    fcntl.flock(fd, fcntl.LOCK_EX)
    p = None
    out_thread = None
    info = {'cmd': ' '.join(cmd)[:300], 'guard_tripped': False, 'guard_reasons': [], 'events': [],
            'peak_rss_kb': 0, 'minimum_sampled_free_bytes': None, 'helper_seconds': helper_seconds,
            'chunk_guard_monotonic': chunk_guard_monotonic, 'run_guard_wall': run_guard_wall,
            'sample_seconds': sample_seconds, 'rss_cap_kb': rss_cap_kb, 'inflight_floor_bytes': inflight_floor_bytes}
    try:
        reason = S.admitted_reason()
        if reason:
            raise S.AdmissionDenied(reason)
        if time.monotonic() >= chunk_guard_monotonic or time.time() >= run_guard_wall:
            raise S.AdmissionDenied('enumeration chunk/run deadline after helper-lock wait')
        lane_rss = S.lane_rss_kb()
        info['lane_rss_kb_at_start'] = lane_rss
        if lane_rss + rss_cap_kb > S.LANE_RSS_LIMIT_KB:
            raise S.AdmissionDenied('lane RSS headroom before guarded enumeration')
        # S.spawn may be the outer post-all-lock growth hook; it rechecks its gates/deadlines before Popen.
        p, output, out_thread = S._start(cmd)
        started = time.monotonic()
        info['pid'] = p.pid
        info['spawn_clock'] = time.strftime('%Y-%m-%dT%H:%M:%S%z')
        while p.poll() is None:
            elapsed = time.monotonic() - started
            rss = S._rss_kb(p.pid)
            free = S.disk_free_bytes()
            info['peak_rss_kb'] = max(info['peak_rss_kb'], rss)
            info['minimum_sampled_free_bytes'] = free if info['minimum_sampled_free_bytes'] is None else min(info['minimum_sampled_free_bytes'], free)
            reasons = []
            if S.ABORT[0]:
                reasons.append('runner abort')
            if rss > rss_cap_kb:
                reasons.append('helper RSS cap')
            if free < inflight_floor_bytes:
                reasons.append('in-flight free-space floor')
            if elapsed >= helper_seconds:
                reasons.append('helper elapsed limit')
            if time.monotonic() >= chunk_guard_monotonic:
                reasons.append('chunk deadline')
            if time.time() >= run_guard_wall:
                reasons.append('run deadline')
            if reasons:
                info['guard_tripped'] = True
                info['guard_reasons'] = reasons
                info['events'].append({'action': 'SIGTERM owned helper', 'pid': p.pid, 'reasons': reasons,
                                       'host_clock': time.strftime('%Y-%m-%dT%H:%M:%S%z')})
                try:
                    p.terminate()
                except OSError as exc:
                    info['events'].append({'terminate_error': str(exc)})
                try:
                    p.wait(timeout=term_wait)
                    info['stop'] = 'term'
                except subprocess.TimeoutExpired:
                    info['stop'] = 'quarantined'
                    wait_quarantined(S, p, 'enumeration helper', receipt_dir, info['events'], min(1.0, sample_seconds))
                break
            time.sleep(min(1.0, sample_seconds))
        if p.poll() is not None:
            S.unregister(p)
        out_thread.join(timeout=10)
        if out_thread.is_alive():
            info['guard_tripped'] = True
            info['guard_reasons'].append('output collection did not finish')
        if S.ABORT[0]:
            info['guard_tripped'] = True
            if 'runner abort' not in info['guard_reasons']:
                info['guard_reasons'].append('runner abort')
        post_reasons = []
        if time.monotonic() - started >= helper_seconds:
            post_reasons.append('helper elapsed limit')
        if time.monotonic() >= chunk_guard_monotonic:
            post_reasons.append('chunk deadline')
        if time.time() >= run_guard_wall:
            post_reasons.append('run deadline')
        for observed in post_reasons:
            info['guard_tripped'] = True
            if observed not in info['guard_reasons']:
                info['guard_reasons'].append(observed)
        info['seconds'] = round(time.monotonic() - started, 3)
        info['rc'] = p.returncode
        info.setdefault('stop', 'self')
        return p.returncode, b''.join(output).decode(errors='replace'), info
    finally:
        if p is not None:
            if p.poll() is None:
                wait_quarantined(S, p, 'owned helper before lock release', receipt_dir, info['events'], min(1.0, sample_seconds))
            S.unregister(p)
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)
