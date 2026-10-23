#!/usr/bin/env python3
"""Regenerate a row-cycle CNF in ONE RAM buffer; run one native SAT child safely.

Usage: run_sat_supervised_c21v2.py OUTDIR N K SEED SECONDS (--mu MU|--base)
       [--cycle 2|3] [--fixed F] [--canonical-columns] [--unit-anchor]
       [--plant DMRAW] [--solver kissat|cadical] [--rss-bytes B]
       [--stop-wait-seconds S]

No CNF or proof files are created. The complete bounded CNF is built before the
child exists, hashed by its encoder, and fed from one read-only buffer to stdin.
Retained growth is at most16MiB/chunk (native stdout8MiB plus small metadata/logs
and a candidate). The frozen12GB floor+64MiB margin is checked just before launch.
No model CLIs, subprocess timeout, Popen.kill, SIGKILL or automatic recovery.

Resource supervision is in the MAIN thread, not a daemon watcher: any RSS/disk/
heartbeat failure requests one SIGTERM and follows a bounded<=120s stop path.
If the child remains alive, write UNKNOWN-UNREAPED-CHILD with its detached PID,
exit70 for parent intervention, and run NO further model. The caller must reserve
that child's CPU/RSS until the parent has dealt with it. Do not queue this behind
a driver which would silently continue after70. The native time window reserves
120s before the frozen18:20 PDT stop.

A separate daemon does only bounded-buffer stdin writing; its failures are
observed by the main loop. SAT is decoded with full DM/action checks before
exit10. UNSAT exit20 is only an UNCERTIFIED solver claim; no proof is retained.
All outputs are exclusive creates; old v1 is preserved but never used here.
"""
import argparse
import ctypes
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import resource
import shutil
import signal
import subprocess
import sys
import threading
import time
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
ENCODER = ROOT / 'code/fixed_rowcycle_cnf_c21v1.py'
ZONE = ZoneInfo('America/Los_Angeles')
STOP_AT = datetime(2026, 10, 18, 18, 20, tzinfo=ZONE)
STOP_REQUEST_AT = STOP_AT - timedelta(seconds=125)  #120s stop plus5s receipt margin
FLOOR = 12_000_000_000
MARGIN = 64 * 1024 ** 2
RETAINED_BOUND = 16 * 1024 ** 2
RSS_MAX = 5 * 1024 ** 3 // 2
FILECAP = 8 * 1024 ** 2


def stamp():
    return datetime.now(ZONE).isoformat()


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


def free_bytes(path):
    st = os.statvfs(path)
    return st.f_bavail * st.f_frsize


class ProcTaskInfo(ctypes.Structure):
    _fields_ = [(name, ctypes.c_uint64) for name in (
        'virtual_size', 'resident_size', 'total_user', 'total_system', 'threads_user', 'threads_system')]
    _fields_ += [(name, ctypes.c_int32) for name in (
        'policy', 'faults', 'pageins', 'cow_faults', 'messages_sent', 'messages_received',
        'syscalls_mach', 'syscalls_unix', 'csw', 'threadnum', 'numrunning', 'priority')]


class ResidentSize:
    def __init__(self):
        self.lib = ctypes.CDLL('/usr/lib/libproc.dylib', use_errno=True)
        self.fn = self.lib.proc_pidinfo
        self.fn.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_uint64, ctypes.c_void_p, ctypes.c_int]
        self.fn.restype = ctypes.c_int
        if ctypes.sizeof(ProcTaskInfo) != 96 or not self.read(os.getpid()):
            raise RuntimeError('Darwin RSS ABI self-control failed before child launch')

    def read(self, pid):
        info = ProcTaskInfo()
        count = self.fn(pid, 4, 0, ctypes.byref(info), ctypes.sizeof(info))
        if count == 0:
            return None
        if count != ctypes.sizeof(info):
            raise RuntimeError('Darwin task-info size mismatch')
        return info.resident_size


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('outdir'); p.add_argument('n', type=int); p.add_argument('k', type=int)
    p.add_argument('seed', type=int); p.add_argument('seconds', type=int)
    mode = p.add_mutually_exclusive_group(required=True)
    mode.add_argument('--mu', type=int); mode.add_argument('--base', action='store_true')
    p.add_argument('--cycle', type=int, choices=[2, 3], default=2)
    p.add_argument('--fixed', type=int); p.add_argument('--canonical-columns', action='store_true')
    p.add_argument('--unit-anchor', action='store_true'); p.add_argument('--plant')
    p.add_argument('--solver', choices=['kissat', 'cadical'], default='cadical')
    p.add_argument('--rss-bytes', type=int, default=RSS_MAX)
    p.add_argument('--stop-wait-seconds', type=float, default=120.0)
    args = p.parse_args()
    if not 1 <= args.seconds <= 10800 or not 1 <= args.rss_bytes <= RSS_MAX or not 0.1 <= args.stop_wait_seconds <= 120:
        raise ValueError('native time/RSS/stop bounds cannot be raised')
    out = Path(args.outdir).resolve()
    if ROOT not in out.parents:
        raise ValueError('output must be a new directory inside this lane')
    os.mkdir(out)
    begin, start_clock = time.monotonic(), stamp()
    state = {'child': None, 'stop_reason': None, 'term_at': None, 'peak_rss': 0,
             'rss_samples': 0, 'input_bytes_written': 0, 'writer_error': None}

    def write_record(name, rec):
        try:
            with open(out / name, 'x') as f:
                json.dump(rec, f, indent=1)
        except Exception as error:
            print(json.dumps({'record_write_failed': name, 'error': repr(error), 'receipt': rec}), flush=True)
            return False
        return True

    def request_stop(reason):
        if state['stop_reason'] is None:
            state['stop_reason'] = reason
        child = state['child']
        if child is not None and state['term_at'] is None:
            state['term_at'] = time.monotonic()
            try:
                child.send_signal(signal.SIGTERM)
            except ProcessLookupError:
                pass

    def forward(signum, frame):
        request_stop('owned signal%d' % signum)

    signal.signal(signal.SIGTERM, forward)
    signal.signal(signal.SIGINT, forward)
    # All launch-critical files/APIs are opened/checked BEFORE a child exists.
    monitor = ResidentSize()
    if free_bytes(out) < FLOOR + MARGIN:
        rec = {'clock': stamp(), 'verdict': 'UNKNOWN-DEFERRED-DISK-FLOOR', 'free_bytes': free_bytes(out),
               'floor_bytes': FLOOR, 'margin_bytes': MARGIN, 'child_launched': False,
               'projected_retained_bytes': RETAINED_BOUND}
        write_record('record.json', rec); print(json.dumps(rec), flush=True)
        return 75
    spec = importlib.util.spec_from_file_location('c21_frozen_rowcycle_encoder_for_memory_input', ENCODER)
    encoder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(encoder)
    cnf, metadata = encoder._encode_in_memory(args)
    metadata['cnf_storage'] = 'single read-only RAM buffer; no retained CNF/proof'
    metadata['supervisor_source_sha256'] = sha(__file__)
    if not write_record('model.json', metadata):
        return 74
    native = shutil.which(args.solver)
    if not native:
        raise RuntimeError('native solver missing before launch')
    remaining = int((STOP_REQUEST_AT - datetime.now(ZONE)).total_seconds())
    seconds = min(args.seconds, remaining)
    if seconds < 1:
        write_record('record.json', {'clock': stamp(), 'verdict': 'UNKNOWN-DEFERRED-STOP-WINDOW', 'child_launched': False})
        return 75
    cmd = [native, '--seed=%d' % args.seed]
    cmd += ['--time=%d' % seconds] if args.solver == 'kissat' else ['-t', str(seconds)]
    cmd += ['-']  # native solvers read this complete regenerated CNF from stdin
    start = {'clock': start_clock, 'runner_pid': os.getpid(), 'command': cmd,
             'n': args.n, 'k': args.k, 'seed': args.seed, 'native_seconds_requested': args.seconds,
             'native_seconds_actual': seconds, 'rss_stop_bytes': args.rss_bytes,
             'stop_wait_seconds': args.stop_wait_seconds, 'child_file_cap_bytes': FILECAP,
             'cnf_sha256': metadata['cnf_sha256'], 'cnf_bytes': len(cnf),
             'encoder_source_sha256': metadata['encoder_source_sha256'],
             'supervisor_source_sha256': sha(__file__), 'solver_sha256': sha(native),
             'projected_retained_bytes': RETAINED_BOUND, 'proof_retained': False, 'cnf_retained': False,
             'stop_request_at': STOP_REQUEST_AT.isoformat(), 'stop_at': STOP_AT.isoformat(),
             'child_core_limit_bytes': 0}
    if not write_record('start.json', start):
        return 74
    writer_done = threading.Event()
    pause = threading.Event()

    def child_limits():
        resource.setrlimit(resource.RLIMIT_FSIZE, (FILECAP, FILECAP))
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))

    def feed():
        try:
            fd, offset = state['child'].stdin.fileno(), 0
            while offset < len(cnf):
                offset += os.write(fd, cnf[offset:offset + 65536])
                state['input_bytes_written'] = offset
        except Exception as error:
            state['writer_error'] = repr(error)
        finally:
            try:
                state['child'].stdin.close()
            except Exception as error:
                if state['writer_error'] is None:
                    state['writer_error'] = repr(error)
            writer_done.set()

    unreaped, rc, last_heartbeat = False, None, 0.0
    writer = threading.Thread(target=feed, name='bounded-CNF-stdin-feed', daemon=True)
    writer_started = False
    with open(out / 'solver.out', 'xb') as solver_log, open(out / 'heartbeat.jsonl', 'x') as heartbeat:
        # This is the final, immediately-before-Popen shared-floor check.
        available = free_bytes(out)
        if available < FLOOR + MARGIN or state['stop_reason'] is not None:
            rec = {**start, 'clock': stamp(), 'verdict': 'UNKNOWN-DEFERRED-DISK-OR-SIGNAL',
                   'free_bytes': available, 'child_launched': False, 'stop_reason': state['stop_reason']}
            write_record('record.json', rec); print(json.dumps(rec), flush=True)
            return 75
        env = dict(os.environ); env['TMPDIR'] = str(ROOT / 'tmp-cc')
        state['child'] = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=solver_log, stderr=subprocess.STDOUT,
                                          bufsize=0, preexec_fn=child_limits, start_new_session=True, env=env)
        child = state['child']
        if not write_record('child.json', {'clock': stamp(), 'pid': child.pid, 'command': cmd,
                                           'launch_free_bytes': available, 'detached': True}):
            request_stop('owned child registration record failed')
        try:
            writer.start()
            writer_started = True
        except Exception as error:
            state['writer_error'] = repr(error)
            request_stop('CNF feed thread start failed: ' + repr(error))
            child.stdin.close()
        if state['stop_reason'] is not None:
            request_stop(state['stop_reason'])
        while True:
            rc = child.poll()
            if rc is not None:
                break
            try:
                rss = monitor.read(child.pid)
                if rss is None:
                    if child.poll() is None:
                        request_stop('RSS unavailable for owned live child')
                else:
                    state['rss_samples'] += 1
                    state['peak_rss'] = max(state['peak_rss'], rss)
                    if rss > args.rss_bytes:
                        request_stop('native child RSS stop threshold')
                available = free_bytes(out)
                if available < FLOOR:
                    request_stop('shared disk floor')
                if datetime.now(ZONE) >= STOP_REQUEST_AT:
                    request_stop('reserved shutdown window before frozen deadline')
                if time.monotonic() - begin >= seconds + 30:
                    request_stop('native time-limit overrun guard')
                if state['writer_error'] is not None and child.poll() is None:
                    request_stop('CNF input writer failed: ' + state['writer_error'])
                if time.monotonic() - last_heartbeat >= 300:
                    last_heartbeat = time.monotonic()
                    heartbeat.write(json.dumps({'clock': stamp(), 'child_pid': child.pid, 'free_bytes': available,
                                                **{k: v for k, v in state.items() if k != 'child'}}) + '\n')
                    heartbeat.flush()
            except Exception as error:
                request_stop('resource/log supervision failed: ' + repr(error))
            if state['term_at'] is not None and time.monotonic() - state['term_at'] >= args.stop_wait_seconds:
                if child.poll() is None:
                    unreaped = True
                    break
            pause.wait(0.1)
        if not unreaped and writer_started:
            writer.join(5)
            if writer.is_alive():
                request_stop('input writer did not finish after child exit')
    ru = resource.getrusage(resource.RUSAGE_CHILDREN)
    rec = {**start, 'end_clock': stamp(), 'wall_s': time.monotonic() - begin,
           'child_pid': state['child'].pid, 'child_launched': True, 'exit_code': rc,
           'stop_reason': state['stop_reason'], 'sigterm_sent': state['term_at'] is not None,
           'peak_sampled_rss': state['peak_rss'], 'rss_samples': state['rss_samples'],
           'input_bytes_written': state['input_bytes_written'], 'writer_error': state['writer_error'],
           'child_maxrss_bytes_macOS': ru.ru_maxrss, 'solver_out_sha256': sha(out / 'solver.out')}
    rec['cnf_fully_written'] = state['input_bytes_written'] == len(cnf)
    if unreaped:
        rec['solver_out_sha256_at_guard_snapshot'] = rec.pop('solver_out_sha256')
        rec['solver_output_mutable_until_child_stops'] = True
        rec.update(verdict='UNKNOWN-UNREAPED-CHILD', queue_must_not_continue=True,
                   parent_intervention_required=True, reserved_busy_slots=1,
                   warning='Do not automatically retry/recover or treat the detached PID as stopped.')
        write_record('unreaped-child.json', rec); write_record('record.json', rec)
        print(json.dumps(rec), flush=True)
        return 70
    statuses = [line.strip() for line in (out / 'solver.out').read_text().splitlines() if line.startswith('s ')]
    rec['status_lines'] = statuses
    result = 0
    if rc == 10 and statuses == ['s SATISFIABLE']:
        # The decoder checks all semantics, not merely the CNF assignment.
        target = out / 'candidate.dmraw'
        try:
            encoder.decode(argparse.Namespace(meta=str(out / 'model.json'), solver_output=str(out / 'solver.out'), dm=str(target)))
        except Exception as error:
            rec.update(verdict='UNKNOWN-DECODE-REJECTED', decode_error=repr(error))
        else:
            rec.update(verdict='SAT-DM-DIRECTLY-VERIFIED', dmraw_sha256=sha(target), dmraw=str(target))
            result = 10
    elif rc == 20 and statuses == ['s UNSATISFIABLE'] and state['stop_reason'] is None:
        rec['verdict'] = 'UNSAT-SOLVER-CLAIM-UNCERTIFIED-NO-PROOF-RETAINED'
        result = 20
    else:
        rec['verdict'] = 'UNKNOWN'
    write_record('record.json', rec)
    print(json.dumps(rec), flush=True)
    return result


if __name__ == '__main__':
    raise SystemExit(main())
