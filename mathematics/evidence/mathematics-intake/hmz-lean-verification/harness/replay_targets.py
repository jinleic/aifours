#!/usr/bin/env python3
"""Replay each target's delivered checks on APFS copies, never rewriting target-owned evidence."""
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

WORKSPACE = Path('/Users/jinleic/jinleic-workspace')
AI4S = WORKSPACE / 'ai4s'
OUT = Path(__file__).resolve().parent / 'replays'
ENVIRONMENT = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OMP_NUM_THREADS='1', OPENBLAS_NUM_THREADS='1')


def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def copy_target(name):
    destination = OUT / name
    if destination.exists():
        raise SystemExit(f'refusing to reuse existing replay copy {destination}')
    subprocess.run(['cp', '-cR', str(AI4S / name), str(destination)], check=True)
    return destination


def plan():
    OUT.mkdir(exist_ok=True)
    kac_output = OUT / 'kac-moody-serre-relations-replay'
    jobs = {
        'kac-moody-serre-relations': (
            [sys.executable, str(AI4S / 'kac-moody-serre-relations/hmz-lean-20261014/reproduce.py'), '--output', str(kac_output)],
            AI4S / 'kac-moody-serre-relations/hmz-lean-20261014'),
    }
    artin = copy_target('artin-group-grobner-shirshov') / 'hmz-lean-20261014'
    jobs['artin-group-grobner-shirshov'] = ([sys.executable, 'reproduce.py'], artin)
    semigroup = copy_target('regular-semigroup-embedding') / 'hmz-lean-20261014'
    jobs['regular-semigroup-embedding'] = ([sys.executable, 'verify.py'], semigroup)
    estimator = copy_target('m-estimator-sample-augmentation') / 'hmz-lean-20261014'
    jobs['m-estimator-sample-augmentation'] = ([sys.executable, 'verify.py'], estimator)
    kirkman = copy_target('kirkman-large-sets-57-87') / 'hmz-lean-20261014'
    jobs['kirkman-large-sets-57-87:partial'] = (['sh', 'reproduce.sh', 'partial'], kirkman)
    jobs['kirkman-large-sets-57-87:audit-joint'] = (['sh', 'reproduce.sh', 'audit-joint'], kirkman)
    return jobs


def main():
    jobs = plan()
    running = {}
    for name, (command, cwd) in jobs.items():
        log = OUT / (name.replace(':', '-') + '.parent-replay.log')
        handle = log.open('w')
        running[name] = (subprocess.Popen(command, cwd=cwd, env=ENVIRONMENT, stdin=subprocess.DEVNULL,
                                          stdout=handle, stderr=subprocess.STDOUT), handle, log, command, cwd, time.monotonic())
    results = {}
    for name, (process, handle, log, command, cwd, started) in running.items():
        try:
            code = process.wait(timeout=3000)
        except subprocess.TimeoutExpired:
            process.terminate()
            code = process.wait()
        handle.close()
        results[name] = {'command': command, 'cwd': str(cwd), 'returncode': code,
                         'seconds': time.monotonic() - started, 'log': str(log),
                         'log_sha256': hashlib.sha256(log.read_bytes()).hexdigest()}
    receipt = {'schema': 'ai4s-math-parent-target-replays/1', 'ended_at_utc': stamp(),
               'isolation': 'APFS copies under verification/replays; Kac-Moody wrapper copies inputs into a new output directory itself.',
               'results': results}
    (OUT / 'replay-summary.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({name: {'returncode': r['returncode'], 'seconds': round(r['seconds'], 1)} for name, r in results.items()}, indent=2))
    raise SystemExit(0 if all(r['returncode'] == 0 for r in results.values()) else 1)


if __name__ == '__main__':
    main()
