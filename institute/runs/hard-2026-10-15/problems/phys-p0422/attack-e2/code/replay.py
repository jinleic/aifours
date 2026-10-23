"""Replay the numerical evidence, finite checks, and negative controls.

The universal argument remains a mathematical proof in notes/PROOF.md;
the finite checks do not purport to verify its infinite quantifiers.
All launched commands use this Python interpreter; execution is sequential.
"""
import argparse
import json
from pathlib import Path
import subprocess
import sys
import time


def run(args, filename, expected=0, marker=None):
    command=[sys.executable]+args
    out=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True,timeout=300)
    Path('logs',filename).write_text(out.stdout)
    assert out.returncode==expected, f'{args}: exit {out.returncode}, expected {expected}; see logs/{filename}'
    if marker:
        assert marker in out.stdout, f'Expected marker missing in logs/{filename}'
    print(f"PASS replay ({'expected rejection' if expected else 'success'}): python3 {' '.join(args)}",flush=True)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--skip-small-models',action='store_true')
    args=p.parse_args()
    start=time.monotonic()
    run(['code/certify.py','--output','certificates/results.json'],'certify.txt',marker='PASS k5')
    run(['code/independent_check.py'],'independent.txt',marker='ALTERNATE CHECK PASS k5')
    if not args.skip_small_models:
        run(['code/small_models.py'],'small-models.txt',marker='PASS finite exhaustive check')
    run(['code/baseline.py'],'baseline.txt',marker='PASS baseline k=5')
    run(['code/model_constants.py'],'model-constants.txt',marker='N0=3382400000000')
    run(['code/make_controls.py'],'make-controls.txt')
    for k in (4,5):
        run(['code/independent_check.py','--trials','certificates/negative-controls.json',
             '--name',f'k{k}_zero_warning_control'],f'control-zero-k{k}.txt',1,'certificate REJECTED')
        run(['code/independent_check.py','--trials',f'certificates/k{k}_low_density_control.json'],
            f'control-low-k{k}.txt',1,'certificate REJECTED')
    run(['code/certify.py','--trials','certificates/negative-controls.json'],
        'control-producer-zero.txt',1,'claimed negative margin fails')
    run(['code/small_models.py','--break-comparison'],'control-comparison.txt',1,'FAIL: comparison fails')
    run(['code/small_models.py','--illustrate-noninteger'],'illustration-noninteger.txt',1,'ILLUSTRATIVE COUNTEREXAMPLE: noninteger H')
    run(['code/small_models.py','--illustrate-signed-odd'],'illustration-signed-odd.txt',1,'ILLUSTRATIVE COUNTEREXAMPLE: negative B')
    run(['code/validate_claims.py'],'schema.txt',marker='PASS claims.schema.json')
    print(f'ALL REPLAY CHECKS PASSED in {time.monotonic()-start:.2f} seconds.')


if __name__=='__main__':
    main()
