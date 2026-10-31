#!/usr/bin/env python3
# r165 receipts: SHA-256 / bytes / LF of every r165-* artifact in this review directory, the manifest and the
# four frozen inputs (re-hashed), presence check for __pycache__, and the native /bin/date clock.
import sys
sys.dont_write_bytecode = True
import hashlib, json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = '/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/kac-moody/'
INPUTS = ['frontier-20261029-invariant-target-multiplicity-erratum-v1.json',
          'frontier-20261028-level6-inventory-scope-addendum-v1.json',
          'frontier-20261029-quotient-stable-contraction-descent-v1.md',
          'frontier-20261029-level6-all-parameters-primitive-candidate-v1.md']

def rec(path):
    b = open(path, 'rb').read()
    return {'path': path, 'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b), 'LF': b.count(b'\n')}

out = {'clock_before': subprocess.run(['/bin/date'], capture_output=True, text=True).stdout.strip()}
out['manifest'] = rec(os.path.join(HERE, 'manifest-v1.json'))
out['inputs'] = [rec(SRC + f) for f in INPUTS]
out['artifacts'] = [rec(os.path.join(HERE, f)) for f in sorted(os.listdir(HERE))
                    if f.startswith('r165-') and f != 'r165-c9-receipts.out.json']
out['pycache_present'] = any(f == '__pycache__' for f in os.listdir(HERE))
out['non_r165_entries'] = sorted(f for f in os.listdir(HERE) if not f.startswith('r165-'))
out['clock_after'] = subprocess.run(['/bin/date'], capture_output=True, text=True).stdout.strip()
print(json.dumps(out, indent=1))
