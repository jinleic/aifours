#!/usr/bin/env python3
"""Compile each discriminating control in controls/ and require the expected rejection.

Results are merged into controls/receipt.json (entries of controls not run are kept), so a subset
can be re-run without re-running the monolithic certificate controls, whose kernel checks peak
at about 12 GB. Wrap each invocation in tools/watch_cmd.py to enforce a memory cap."""
import json
import os
import pathlib
import subprocess
import sys
import time

FORMAL = pathlib.Path(os.environ.get('FORMAL', pathlib.Path(__file__).resolve().parents[1]))
TOOLBIN = FORMAL / 'env' / 'toolchains' / 'lean-4.24.0-darwin_aarch64' / 'bin'
EXPECT = {
    'CertLowDensity4': 'decide',
    'CertLowDensity5': 'decide',
    'CertTooStrong5': 'decide',
    'WrongArity': 'mismatch',
    'WrongDensity': 'mismatch',
    'BadTrialWeights': 'error',
    'CertL4LowDensity': 'decide',
    'CertL5LowDensity': 'decide',
    'CertK3TblLowDensity': 'decide',
    'CertK3TblTooStrong': 'decide',
    'CertK3TblShortEdge': 'decide',
    'CertK3TblTamper': 'decide',
}


def main(names):
    env = dict(os.environ, PATH=f"{TOOLBIN}:{os.environ['PATH']}")
    env.setdefault('LEAN_NUM_THREADS', '4')
    receipt = FORMAL / 'controls' / 'receipt.json'
    out = json.loads(receipt.read_text()) if receipt.exists() else {}
    for name in names:
        t0 = time.time()
        p = subprocess.run(['lake', 'env', 'lean', str(FORMAL / 'controls' / f'{name}.lean')],
                           cwd=FORMAL / 'lean', env=env, capture_output=True, text=True)
        log = p.stdout + p.stderr
        errors = [l for l in log.splitlines() if ': error:' in l or 'error:' in l[:80]]
        ok = p.returncode != 0 and EXPECT[name] in log
        out[name] = {'exit_code': p.returncode, 'rejected_as_expected': ok,
                     'expected_fragment': EXPECT[name], 'seconds': round(time.time() - t0, 1),
                     'first_error': errors[0][:400] if errors else None}
        print(name, json.dumps(out[name]))
    receipt.write_text(json.dumps(out, indent=1))
    return 0 if all(out[n]['rejected_as_expected'] for n in names) else 1


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or list(EXPECT)))
