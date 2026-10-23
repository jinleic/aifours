#!/usr/bin/env python3
"""Bounded single CaDiCaL visit; preserve UNKNOWNs and every proof byte."""
from pathlib import Path
import argparse
import gzip
import hashlib
import json
import os
import signal
import subprocess
import time

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seconds', type=int, default=300)
    ap.add_argument('--proof-mb', type=int, default=256)
    args = ap.parse_args()
    prefix = ROOT / 'results/3-dsbf-snonzero'
    log = ROOT / 'results/exact-solver.log'
    proof = prefix.with_suffix('.lrat.gz')
    command = ['cadical', '-t', str(args.seconds), '--lrat', '--no-binary', str(prefix.with_suffix('.cnf')), str(proof)]
    start = time.monotonic()
    reason = None
    with log.open('w') as fh:
        proc = subprocess.Popen(command, stdout=fh, stderr=subprocess.STDOUT, start_new_session=True)
        while proc.poll() is None:
            if time.monotonic() - start > args.seconds + 10:
                reason = 'outer wall limit'
            if proof.exists() and proof.stat().st_size > args.proof_mb * 1024 ** 2:
                reason = 'compressed proof-size cap'
            if reason:
                os.killpg(proc.pid, signal.SIGTERM)
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    os.killpg(proc.pid, signal.SIGKILL)
                    proc.wait()
                break
            time.sleep(0.25)
    text = log.read_text()
    solver_status = 'SAT' if proc.returncode == 10 and 's SATISFIABLE' in text else 'UNSAT' if proc.returncode == 20 and 's UNSATISFIABLE' in text else 'UNKNOWN'
    result = {'solver_status': solver_status, 'certified_class_status': 'UNKNOWN',
              'scope': '3-DSBF104 orbit variables, all weight parities, nonzero support XOR, all Walsh magnitudes<=28; harmless f(0)=0 normalization.',
              'command': command, 'return_code': proc.returncode, 'elapsed_seconds': time.monotonic() - start,
              'stop_reason': reason, 'seconds_limit': args.seconds, 'proof_cap_mb': args.proof_mb,
              'cnf_sha256': hashlib.sha256(prefix.with_suffix('.cnf').read_bytes()).hexdigest(),
              'solver_log_sha256': hashlib.sha256(log.read_bytes()).hexdigest(),
              'negative_claim': False,
              'certification_rule': 'Only a complete independently checked empty-clause proof plus the universal encoding audit can certify UNSAT. SAT requires independent full-table direct/FWHT checks.'}
    if proof.exists():
        result['retained_proof_bytes'] = proof.stat().st_size
        result['retained_proof_sha256'] = hashlib.sha256(proof.read_bytes()).hexdigest()
        result['proof_is_partial_if_unknown'] = solver_status == 'UNKNOWN'
    if solver_status == 'SAT':
        model = {}
        for line in text.splitlines():
            if line.startswith('v '):
                for lit in map(int, line.split()[1:]):
                    if lit: model[abs(lit)] = int(lit > 0)
        raw = json.loads(gzip.decompress((ROOT / 'inputs/orbits.json.gz').read_bytes()))
        orbits = raw['classes']['3-dsbf']['orbits']
        bits = [None] * 512
        for j, orbit in enumerate(orbits):
            assert j + 1 in model
            for x in orbit: bits[x] = model[j + 1]
        result['candidate_bits'] = ''.join(map(str, bits))
    (ROOT / 'results/exact-run.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ['solver_status', 'certified_class_status', 'return_code', 'elapsed_seconds', 'stop_reason']}, sort_keys=True))


if __name__ == '__main__':
    main()
