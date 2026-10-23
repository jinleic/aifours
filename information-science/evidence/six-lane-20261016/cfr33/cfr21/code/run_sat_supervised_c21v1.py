#!/usr/bin/env python3
"""One native SAT call with real-clock/RSS/disk supervision, exclusive receipts.
Usage: run_sat_supervised_c21v1.py OUTDIR CNF kissat|cadical SEED SECONDS
       [--proof] [--rss-bytes BYTES]
Native solver limits only; no subprocess.run(timeout), Popen.kill or SIGKILL.
SIGTERM/SIGINT forwards to the one owned child.2.5GiB maximum RSS threshold,
8MiB child-created output/proof cap,12GB shared floor and frozen18:20 PDT stop.
Proof output is OPTIONAL: ordinary search deliberately does not generate proofs.
Exit10 means SAT CLAIM, UNDECODED: stop queue and decode/check the actual model;
exit20 means UNSAT SOLVER CLAIM, UNCERTIFIED. Everything else exits0 UNKNOWN.
The waiting supervisor logs real host clocks every<=300s. Darwin proc_pidinfo
(PROC_PIDTASKINFO=4) supplies current RSS without ps polling/extra native children.
ABI field layout is from SDK MacOSX26.0 sys/proc_info.h:6 uint64 +12 int32.
No unmonitored fallback is permitted if the native memory API is unavailable.
"""
import argparse
import ctypes
import hashlib
import json
import os
from pathlib import Path
import resource
import shutil
import signal
import subprocess
import threading
import time
from datetime import datetime
from zoneinfo import ZoneInfo

ZONE = ZoneInfo('America/Los_Angeles')
STOP_AT = datetime(2026, 10, 18, 18, 20, tzinfo=ZONE)
FLOOR = 12_000_000_000
RSS_MAX = 5 * 1024 ** 3 // 2
FILECAP = 8 * 1024 ** 2


def stamp():
    return datetime.now(ZONE).isoformat()


def sha(path):
    with open(path, 'rb') as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()


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
            raise RuntimeError('Darwin RSS API self-control failed; no child launched')

    def read(self, pid):
        info = ProcTaskInfo()
        count = self.fn(pid, 4, 0, ctypes.byref(info), ctypes.sizeof(info))
        if count == 0:
            return None
        if count != ctypes.sizeof(info):
            raise RuntimeError('Darwin task-info ABI size mismatch')
        return info.resident_size


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('outdir'); p.add_argument('cnf'); p.add_argument('solver', choices=['kissat', 'cadical'])
    p.add_argument('seed', type=int); p.add_argument('seconds', type=int)
    p.add_argument('--proof', action='store_true')
    p.add_argument('--rss-bytes', type=int, default=RSS_MAX)
    args = p.parse_args()
    if not 1 <= args.seconds <= 10800 or not 1 <= args.rss_bytes <= RSS_MAX:
        raise ValueError('native time/RSS cap cannot be raised')
    out = Path(args.outdir)
    os.mkdir(out)
    monitor = ResidentSize()
    solver = shutil.which(args.solver)
    if not solver:
        raise RuntimeError('native solver missing')
    st = os.statvfs(out)
    if st.f_bavail * st.f_frsize < FLOOR + 64 * 1024 ** 2:
        raise RuntimeError('shared disk-floor margin reached before launch')
    # Reserve120s before the frozen stop time; no long new child near deadline.
    remaining = int((STOP_AT - datetime.now(ZONE)).total_seconds()) - 120
    seconds = min(args.seconds, remaining)
    if seconds < 1:
        raise RuntimeError('no native time window remains before frozen stop')
    cmd = [solver, '--seed=%d' % args.seed]
    cmd += ['--time=%d' % seconds] if args.solver == 'kissat' else ['-t', str(seconds)]
    cmd.append(args.cnf)
    if args.proof:
        cmd.append(str(out / 'proof.drat'))
    state = {'child': None, 'stop_reason': None, 'peak_sampled_rss': 0, 'rss_samples': 0}
    done = threading.Event()
    start_clock, begin = stamp(), time.monotonic()

    def stop(reason):
        if state['stop_reason'] is None:
            state['stop_reason'] = reason
        child = state['child']
        if child is not None:
            try:
                child.send_signal(signal.SIGTERM)
            except ProcessLookupError:
                pass

    def forward(signum, frame):
        stop('owned signal%d' % signum)

    signal.signal(signal.SIGTERM, forward)
    signal.signal(signal.SIGINT, forward)
    start = {'clock': start_clock, 'runner_pid': os.getpid(), 'command': cmd,
             'native_seconds_requested': args.seconds, 'native_seconds_actual': seconds,
             'seed': args.seed, 'rss_stop_bytes': args.rss_bytes, 'child_file_cap_bytes': FILECAP,
             'cnf_sha256': sha(args.cnf), 'solver_sha256': sha(solver),
             'runner_sha256': sha(__file__), 'proof_requested': args.proof,
             'rss_api_self_control_bytes': monitor.read(os.getpid()), 'stop_at': STOP_AT.isoformat()}
    with open(out / 'start.json', 'x') as f:
        json.dump(start, f, indent=1)

    def watch():
        last = 0.0
        with open(out / 'heartbeat.jsonl', 'x') as log:
            while not done.is_set():
                child = state['child']
                if child is not None:
                    try:
                        rss = monitor.read(child.pid)
                        if rss is None:
                            # A reaped/zombie child may disappear just before wait returns.
                            if not done.wait(0.05):
                                stop('RSS API unavailable for owned live child')
                        else:
                            state['rss_samples'] += 1
                            state['peak_sampled_rss'] = max(state['peak_sampled_rss'], rss)
                            if rss > args.rss_bytes:
                                stop('native child RSS stop threshold')
                    except Exception as error:
                        stop('RSS monitor error: ' + repr(error))
                st = os.statvfs(out)
                free = st.f_bavail * st.f_frsize
                if free < FLOOR:
                    stop('shared disk floor')
                if datetime.now(ZONE) >= STOP_AT:
                    stop('frozen worker stop deadline')
                if time.monotonic() - begin >= seconds + 30:
                    stop('native limit overrun guard')
                if time.monotonic() - last >= 300:
                    last = time.monotonic()
                    log.write(json.dumps({'clock': stamp(), 'child_pid': child.pid if child else None,
                                          'free_bytes': free, **{k: v for k, v in state.items() if k != 'child'}}) + '\n')
                    log.flush()
                done.wait(0.5)

    def child_limits():
        resource.setrlimit(resource.RLIMIT_FSIZE, (FILECAP, FILECAP))

    with open(out / 'solver.out', 'xb') as f:
        state['child'] = subprocess.Popen(cmd, stdout=f, stderr=subprocess.STDOUT, preexec_fn=child_limits)
        thread = threading.Thread(target=watch, name='owned-native-sat-resource-watch', daemon=True)
        thread.start()
        if state['stop_reason'] is not None:
            stop(state['stop_reason'])
        rc = state['child'].wait()
        done.set()
        thread.join()
    ru = resource.getrusage(resource.RUSAGE_CHILDREN)
    statuses = [line.strip() for line in (out / 'solver.out').read_text().splitlines() if line.startswith('s ')]
    if rc == 10 and statuses == ['s SATISFIABLE']:
        verdict, result = 'SAT-CLAIM-UNDECODED', 10
    elif rc == 20 and statuses == ['s UNSATISFIABLE'] and state['stop_reason'] is None:
        verdict, result = 'UNSAT-SOLVER-CLAIM-UNCERTIFIED', 20
    else:
        verdict, result = 'UNKNOWN', 0
    rec = {**start, 'end_clock': stamp(), 'wall_s': time.monotonic() - begin, 'exit_code': rc,
           'verdict': verdict, 'status_lines': statuses, 'stop_reason': state['stop_reason'],
           'peak_sampled_rss': state['peak_sampled_rss'], 'rss_samples': state['rss_samples'],
           'child_maxrss_bytes_macOS': ru.ru_maxrss, 'solver_out_sha256': sha(out / 'solver.out')}
    if (out / 'proof.drat').exists():
        rec.update(proof_sha256=sha(out / 'proof.drat'), proof_bytes=(out / 'proof.drat').stat().st_size)
    with open(out / 'record.json', 'x') as f:
        json.dump(rec, f, indent=1)
    print(json.dumps(rec), flush=True)
    raise SystemExit(result)


if __name__ == '__main__':
    main()
