"""Metadata only: observe authorized run resources; never launch science or signal processes."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import time
from datetime import datetime

ROOT = Path('/Users/jinleic/repos/aifours')
RUN = Path(__file__).resolve().parent.parent
stopped = False


def stop(signum, frame):
    global stopped
    stopped = True


def clock():
    observed = subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z'], text=True).strip()
    return datetime.strptime(observed, '%Y-%m-%dT%H:%M:%S%z').isoformat(timespec='seconds')


def observe():
    stat = os.statvfs(ROOT)
    return {'t': clock(), 'free': stat.f_bavail * stat.f_frsize,
            'floor_bytes': 12000000000, 'scope': 'metadata only; not scientific checkpoint or launch admission'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--once', action='store_true')
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    out = Path(args.output).resolve()
    if not out.is_relative_to(RUN):
        raise SystemExit('Output must be inside the current run')
    contract = json.loads((RUN / 'contract-v1.json').read_text())
    end = datetime.fromisoformat(contract['cutoffs']['owned_compute_settled_by']).timestamp()
    for sig in (signal.SIGTERM, signal.SIGINT):
        signal.signal(sig, stop)
    with out.open('x') as handle:
        start = {'event': 'observer_start', 'at': clock(), 'pid': os.getpid(), 'pgid': os.getpgrp(),
                 'cwd': str(Path.cwd()), 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
        handle.write(json.dumps(start) + '\n')
        while not stopped and time.time() < end:
            record = observe()
            handle.write(json.dumps(record) + '\n')
            handle.flush()
            print(json.dumps(record), flush=True)
            if args.once:
                break
            target = min(time.monotonic() + 10, time.monotonic() + max(0, end - time.time()))
            while not stopped and time.monotonic() < target:
                time.sleep(min(1, max(0, target - time.monotonic())))
        handle.write(json.dumps({'event': 'observer_end', 'at': clock(), 'sigterm_or_sigint': stopped}) + '\n')
        handle.flush()
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
