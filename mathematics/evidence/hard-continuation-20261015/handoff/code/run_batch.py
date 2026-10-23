#!/usr/bin/env python3
"""Resumable driver: run certify.py over consecutive block chunks.

Each chunk is one separate `certify.py run` command with a hard per-command
timeout below 300 s.  A chunk whose valid receipt already exists is skipped,
so an interrupted batch resumes where it stopped.  At most --workers commands
run at once (default 4, the lane limit).  Creating the file named by --stop
lets running commands finish and starts no new one.  This driver executes a
finite plan and exits; it installs nothing and never reschedules itself.
"""
import argparse
import hashlib
import json
import os
import subprocess
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE.parent
CERTIFY = HERE / 'certify.py'
SCHEMA = 'math-p0039-cert-receipt/2'


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def receipt_path(task, first, last):
    return BASE / 'receipts' / task / ('%s-%05d-%05d.json' % (task, first, last))


def valid_receipt(path, task, first, last, checker):
    try:
        r = json.loads(path.read_text())
    except (OSError, ValueError):
        return False
    blocks = r.get('blocks', [])
    resolved = all(len(b.get('resolutions', [])) == len(b['survivors']) for b in blocks)
    return (r.get('schema') == SCHEMA and r.get('task') == task
            and r.get('first') == first and r.get('last') == last
            and r.get('checker_sha256') == checker
            and [b['id'] for b in blocks] == list(range(first, last + 1))
            and resolved and (task == 'low' or not r.get('survivors')))


def main():
    p = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    p.add_argument('--plan', action='append', required=True,
                   help='task:first:last:chunk (inclusive block ids); repeatable, run in order')
    p.add_argument('--workers', type=int, default=4)
    p.add_argument('--timeout', type=float, default=295.0)
    p.add_argument('--stop', default=str(BASE / 'STOP'))
    p.add_argument('--log', default=str(BASE / 'evidence' / 'batch-log.jsonl'))
    p.add_argument('--logs', help='directory of preserved C block logs passed to certify.py (default: its own)')
    args = p.parse_args()
    if not 1 <= args.workers <= 4 or not 0 < args.timeout < 300:
        sys.exit('workers must be 1..4 and timeout below 300 s')
    checker = sha256_file(CERTIFY)
    jobs = []
    for item in args.plan:
        task, first, last, chunk = item.split(':')
        first, last, chunk = int(first), int(last), int(chunk)
        if chunk < 1:
            sys.exit('chunk must be positive')
        a = first
        while a <= last:
            b = min(last, (a // chunk + 1) * chunk - 1)
            jobs.append((task, a, b))
            a = b + 1
    todo = [j for j in jobs if not valid_receipt(receipt_path(*j), *j, checker)]
    lock = threading.Lock()
    env = dict(os.environ, OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1',
               VECLIB_MAXIMUM_THREADS='1', PYTHONHASHSEED='0')

    def log(entry):
        with lock, open(args.log, 'a') as f:
            f.write(json.dumps(entry, separators=(',', ':')) + '\n')
            f.flush()
            os.fsync(f.fileno())

    def work(job):
        task, a, b = job
        if Path(args.stop).exists():
            return 'stopped'
        if sha256_file(CERTIFY) != checker:
            return 'stopped'  # never mix checker versions inside one batch
        path = receipt_path(task, a, b)
        path.parent.mkdir(parents=True, exist_ok=True)
        cmd = [sys.executable, str(CERTIFY), 'run', '--task', task, '--first', str(a),
               '--last', str(b), '--receipt', str(path)] + (['--logs', args.logs] if args.logs else [])
        began = time.monotonic()
        try:
            done = subprocess.run(cmd, capture_output=True, text=True, timeout=args.timeout, env=env)
            rc, err = done.returncode, done.stderr[-2000:]
        except subprocess.TimeoutExpired:
            rc, err = 'timeout', ''
        ok = rc == 0 and valid_receipt(path, task, a, b, checker)
        log(dict(task=task, first=a, last=b, returncode=rc, ok=ok,
                 seconds=round(time.monotonic() - began, 3), stderr_tail=err,
                 finished_utc=datetime.now(timezone.utc).isoformat()))
        return 'ok' if ok else 'failed'

    log(dict(event='start', checker_sha256=checker, planned_chunks=len(jobs), todo=len(todo),
             workers=args.workers, timeout=args.timeout, plan=args.plan,
             at=datetime.now(timezone.utc).isoformat()))
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        results = list(pool.map(work, todo))
    summary = dict(event='end', ok=results.count('ok'), failed=results.count('failed'),
                   stopped=results.count('stopped'), at=datetime.now(timezone.utc).isoformat())
    log(summary)
    print(json.dumps(summary))
    sys.exit(0 if summary['failed'] == 0 and summary['stopped'] == 0 else 1)


if __name__ == '__main__':
    main()
