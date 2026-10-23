#!/usr/bin/env python3
"""Run a bounded set of local recovery computations on at most three CPUs.

This is visit orchestration, not a claims.json replay entry point. Every
individual claimed replay is a separate Python invocation below 900 seconds.
Each child is terminated at 820 seconds and failures are reported, never
interpreted as nonexistence. No compiled executable or producer import.
"""
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import subprocess
import sys
import time


def jobs(phase):
    if phase.startswith('prefix'):
        Path('evidence/prefix-chunks').mkdir(exist_ok=True)
        for chunk in range(10):
            if phase == 'prefix-produce':
                start = 200000000000+240000000*chunk
                argv = ['code/replay.py', '--start', str(start), '--stop', str(start+240000000),
                        '--step', '24', '--output', 'evidence/prefix-chunks/%02d.json' % chunk]
            else:
                backend = phase.removeprefix('prefix-')
                argv = ['code/check_interval.py', str(chunk), '--backend', backend,
                        '--output', 'evidence/prefix-chunks/%02d.%s.json' % (chunk, backend)]
            yield str(chunk), argv
    else:
        backend = phase.removeprefix('windows-')
        Path('evidence/window-chunks').mkdir(exist_ok=True)
        for group in range(5):
            indices = ','.join(str(i) for i in range(20*group, 20*group+20))
            argv = ['code/check_windows.py', '--indices', indices, '--backend', backend,
                    '--output', 'evidence/window-chunks/%02d.%s.json' % (group, backend)]
            yield str(group), argv


def run_job(item):
    key, argv = item
    begin = time.monotonic()
    try:
        run = subprocess.run([sys.executable]+argv, capture_output=True, text=True, timeout=820)
        row = dict(job=key, command=['python3']+argv, returncode=run.returncode,
                   seconds=time.monotonic()-begin, stdout=run.stdout, stderr=run.stderr)
    except subprocess.TimeoutExpired:
        row = dict(job=key, command=['python3']+argv, returncode=None,
                   seconds=time.monotonic()-begin, timeout=True)
    return row


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('phase', choices=['prefix-produce', 'prefix-pow', 'prefix-manual',
                                   'windows-pow', 'windows-manual'])
    p.add_argument('--workers', type=int, choices=(1, 2, 3), default=2)
    p.add_argument('--first', type=int, default=0)
    args = p.parse_args()
    output = Path('evidence/recovery-'+args.phase+'-runs.json')
    rows = []
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(run_job, item) for item in jobs(args.phase)
                   if int(item[0]) >= args.first]
        for done in as_completed(futures):
            row = done.result()
            rows.append(row)
            output.write_text(json.dumps(sorted(rows, key=lambda r: int(r['job'])), indent=2)+'\n')
            print(json.dumps({k: row[k] for k in ('job', 'returncode', 'seconds')}), flush=True)
    if any(r['returncode'] != 0 for r in rows):
        raise SystemExit(1)


if __name__ == '__main__':
    main()
