#!/usr/bin/env python3
"""Parent re-execution of the phys-2 checker A (outer cones) and the central-box certificate.
Verifies every input hash first; writes only into this directory; refuses to overwrite."""
import hashlib, json, subprocess, sys, time, os
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
HERE = Path(__file__).resolve().parent
LANE = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/random5reg-colour')
PY = str(LANE / '.venv/bin/python')
def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''): h.update(b)
    return h.hexdigest()
sums = {}
for line in (LANE / 'outer/evidence/SHA256SUMS').read_text().splitlines():
    h, _, p = line.partition('  '); sums[p.strip()] = h
out = HERE / 'parent-replay-result.json'
if out.exists(): sys.exit('refusing to overwrite ' + str(out))
code_sha = sha(HERE / 'cert_cells.py')
assert code_sha == sums['code/cert_cells.py'], 'checker copy differs from lane SHA256SUMS'
ldc_sha = sha(HERE / 'cert_ldc3.py')
assert ldc_sha.startswith('376400f8') and ldc_sha.endswith('d3f5a'), ldc_sha
cones = ['00', '01', '02', '10', '11', '12', '20', '21', '22']
def run_cone(c):
    cert = LANE / f'outer/evidence/cone{c}.json'
    h = sha(cert); assert h == sums[f'evidence/cone{c}.json'], (c, h)
    res = HERE / f'cone{c}.parent-check.json'
    if res.exists(): raise SystemExit('exists ' + str(res))
    t0 = time.time()
    p = subprocess.run(['/usr/bin/time', '-l', PY, str(HERE / 'cert_cells.py'), str(cert), str(res), '--require-r0', '1/10000'], capture_output=True, text=True)
    (HERE / f'cone{c}.stdout').write_text(p.stdout); (HERE / f'cone{c}.stderr').write_text(p.stderr)
    r = json.loads(res.read_text()) if res.exists() else None
    return {'cone': c, 'cert_sha256': h, 'returncode': p.returncode, 'wall_s': round(time.time() - t0, 1), 'result': r}
started = time.strftime('%Y-%m-%dT%H:%M:%S%z')
with ThreadPoolExecutor(3) as ex:
    cone_results = list(ex.map(run_cone, cones))
t0 = time.time()
p = subprocess.run(['/usr/bin/time', '-l', PY, str(HERE / 'cert_ldc3.py'), '1/10000', '3/20', '12', '4'], capture_output=True, text=True)
(HERE / 'central.stdout').write_text(p.stdout); (HERE / 'central.stderr').write_text(p.stderr)
central = {'returncode': p.returncode, 'wall_s': round(time.time() - t0, 1), 'code_sha256': ldc_sha}
try:
    central['json'] = json.loads(p.stdout.strip().splitlines()[-1])
except Exception as e:
    central['parse_error'] = repr(e)
summary = {'started_pt': started, 'finished_pt': time.strftime('%Y-%m-%dT%H:%M:%S%z'), 'python': PY, 'checker_sha256': code_sha,
           'sha256sums_file_sha256': sha(LANE / 'outer/evidence/SHA256SUMS'), 'cones': cone_results, 'central': central}
out.write_text(json.dumps(summary, indent=1, default=str) + '\n')
print(json.dumps({'cones': [(c['cone'], c['returncode'], (c['result'] or {}).get('verdict'), (c['result'] or {}).get('dual_leaves'), (c['result'] or {}).get('central_leaves'), (c['result'] or {}).get('failed')) for c in cone_results], 'central_rc': p.returncode}, default=str))
