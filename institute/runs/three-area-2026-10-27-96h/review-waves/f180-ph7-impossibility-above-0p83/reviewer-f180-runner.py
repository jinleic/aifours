#!/usr/bin/env python3
"""Run a batch of reviewer replay jobs (each a one-shot process capped at 120 s),
recording a receipt per job: argv, start/end clock, exit code, stdout, SHA-256 of
its output file.  usage: reviewer-f180-runner.py BATCHNAME JOBFILE MAXPAR"""
import sys, os, json, time, subprocess, hashlib
from concurrent.futures import ThreadPoolExecutor
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))

def stamp():
    return time.strftime('%Y-%m-%dT%H:%M:%S%z', time.localtime())

def run(args):
    t0 = time.time(); s = stamp()
    try:
        cp = subprocess.run([sys.executable, '-B', os.path.join(HERE, 'reviewer-f180-replay.py')] + args,
                            capture_output=True, text=True, timeout=120, cwd=HERE)
        rc, so, se = cp.returncode, cp.stdout, cp.stderr[-2000:]
    except subprocess.TimeoutExpired:
        rc, so, se = 'TIMEOUT(120s)=UNKNOWN', '', ''
    e = stamp()
    fn = None
    for tok in so.split():
        if tok.startswith('reviewer-f180-out-'):
            fn = tok
    h = hashlib.sha256(open(os.path.join(HERE, fn), 'rb').read()).hexdigest() if fn and os.path.exists(os.path.join(HERE, fn)) else None
    return {'argv': args, 'start': s, 'end': e, 'wall_s': round(time.time() - t0, 2), 'exit': rc,
            'stdout': so.strip(), 'stderr_tail': se.strip(), 'out_file': fn, 'out_sha256': h}

def main():
    batch, jobfile, maxpar = sys.argv[1], sys.argv[2], int(sys.argv[3])
    jobs = [line.split() for line in open(os.path.join(HERE, jobfile)) if line.strip() and not line.startswith('#')]
    b0 = stamp()
    with ThreadPoolExecutor(maxpar) as ex:
        receipts = list(ex.map(run, jobs))
    rec = {'batch': batch, 'jobfile': jobfile, 'python': sys.version, 'batch_start': b0, 'batch_end': stamp(),
           'jobs': receipts}
    fn = os.path.join(HERE, 'reviewer-f180-receipts-%s.json' % batch)
    with open(fn, 'w') as fh:
        json.dump(rec, fh, indent=1)
    for r in receipts:
        print(r['exit'], r['wall_s'], ' '.join(r['argv']), '|', r['stdout'][-160:])
    print('receipts', os.path.basename(fn))

if __name__ == '__main__':
    main()
