#!/usr/bin/env python3
"""rv163 machine-generated receipt: re-hashes the frozen inputs, the manifest, every rv163 artifact and
review-v1.md, with native /bin/date clocks.  Writes rv163-receipts-v1.json (not itself hashed inside)."""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/rqls10')


def clock():
    return subprocess.run(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], capture_output=True, text=True,
                          check=True).stdout.strip()


def rec(p):
    b = p.read_bytes()
    return {'path': str(p), 'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b), 'LF': b.count(b'\n'),
            'CR': b.count(b'\r')}


start = clock()
manifest = json.loads((HERE / 'manifest-v1.json').read_text())
inputs = []
for item in manifest['inputs_in_read_order']:
    r = rec(Path(item['path']))
    r['matches_manifest'] = (r['sha256'] == item['sha256'] and r['bytes'] == item['bytes'] and r['LF'] == item['LF'])
    inputs.append(r)
own = [rec(HERE / n) for n in ('manifest-v1.json', 'rv163-exact-cert-check-v1.py', 'rv163-exact-cert-check-v1.json',
                               'rv163-flat-torus-parity-v1.py', 'rv163-flat-torus-parity-v1.json',
                               'rv163-thmA-numeric-v1.py', 'rv163-thmA-numeric-v1.json', 'rv163-receipt-v1.py',
                               'review-v1.md')]
out = {'native_clock_start': start, 'inputs': inputs, 'review_dir_files': own,
       'directory_listing': sorted(p.name for p in HERE.iterdir()), 'native_clock_finish': clock()}
(HERE / 'rv163-receipts-v1.json').write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps(out, indent=1))
