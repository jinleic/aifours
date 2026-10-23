#!/usr/bin/env python3
"""Snapshot-safe replay entry points: Python/system tools only, no binaries.

Every task has subprocess timeouts totaling below 300 seconds. Restores missing logs
from checksummed staged gzip parts before invoking any checker that needs them.
Imports no producing code. Full-range arithmetic is not silently inferred from
metadata or samples.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import time


TASKS = {
    'main-metadata': ['code/verify_result.py'],
    'main-records': ['code/check.py', 'records', 'logs/main', '--allow-partial'],
    'python-records': ['code/check.py', 'records', 'logs/python-main', '--allow-partial'],
    'comparison': ['code/compare_scans.py'],
    'main-negative': ['code/verify_result.py', '--result', 'evidence/result-broken.json'],
    'comparison-negative': ['code/compare_scans.py', '--python-records', 'evidence/recovery-broken-shared.records.jsonl'],
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('task', choices=TASKS)
    parser.add_argument('--output')
    args = parser.parse_args()
    t0 = time.monotonic()
    # This reconstructs and validates parts on every call, even if raw logs
    # survived the snapshot. The temporary writes are small and sequential.
    recovery = subprocess.run([sys.executable, 'code/recover_logs.py'],
                              capture_output=True, text=True, timeout=30)
    if recovery.returncode:
        sys.stderr.write(recovery.stderr)
        raise SystemExit(recovery.returncode)
    run = subprocess.run([sys.executable]+TASKS[args.task],
                         capture_output=True, text=True, timeout=240)
    record = dict(task=args.task, command=[sys.executable]+TASKS[args.task],
                  returncode=run.returncode, seconds=time.monotonic()-t0,
                  recovery=json.loads(recovery.stdout), stdout=run.stdout,
                  stderr=run.stderr)
    if args.output:
        Path(args.output).write_text(json.dumps(record, indent=2)+'\n')
    sys.stdout.write(run.stdout)
    sys.stderr.write(run.stderr)
    raise SystemExit(run.returncode)


if __name__ == '__main__':
    main()
