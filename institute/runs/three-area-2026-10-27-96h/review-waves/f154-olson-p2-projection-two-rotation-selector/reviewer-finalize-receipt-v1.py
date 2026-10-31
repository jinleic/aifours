import hashlib
import json
import pathlib
import subprocess

D = pathlib.Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f154-olson-p2-projection-two-rotation-selector')
NAMES = ['manifest-v1.json', 'review-v1.md', 'reviewer-control-plan-v1.json', 'reviewer-exact-control-v1.cpp', 'reviewer-exact-control-v1.bin', 'reviewer-run-control-v1.py', 'reviewer-receipt-q5-v1.json', 'reviewer-stdout-q5-v1.json', 'reviewer-stderr-q5-v1.txt', 'reviewer-receipt-p7-v1.json', 'reviewer-stdout-p7-v1.json', 'reviewer-stderr-p7-v1.txt', 'reviewer-piece-control-v1.py', 'reviewer-piece-control-results-v1.json', 'reviewer-sector-control-v1.py', 'reviewer-sector-control-results-v1.json', 'reviewer-finalize-receipt-v1.py']

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

clock_after_report = clock()
artifacts = []
for name in NAMES:
    b = (D / name).read_bytes()
    artifacts.append({'path': str(D / name), 'bytes': len(b), 'LF': b.count(b'\n'), 'sha256': hashlib.sha256(b).hexdigest()})
for mode in ('q5', 'p7'):
    r = json.loads((D / f'reviewer-receipt-{mode}-v1.json').read_text())
    if r['returncode'] != 0 or not r['complete']:
        raise RuntimeError('incomplete exact control')
for mode in ('piece', 'sector'):
    r = json.loads((D / f'reviewer-{mode}-control-results-v1.json').read_text())
    if r['status'] != 'COMPLETE':
        raise RuntimeError('incomplete supplemental control')
r = {'kind': 'F154_REVIEWER_FINAL_ARTIFACT_RECEIPT', 'status': 'COMPLETE', 'verdict': 'NO_SUBSTANTIVE_DEFECT_FOUND', 'FATAL': 0, 'MAJOR': 0, 'MINOR': 0, 'overall_correctness': 'correct', 'confidence': 0.97, 'first_finalizer_clock_after_report_write_upper_bound_only': clock_after_report, 'artifacts': artifacts, 'scope_boundary': 'Theorem P2 only; no floor/L_RES/actual-block premise; correction is mandatory nontransfer constraint; no ordered-Olson/novelty/formal/independent-family claim.', 'observed_clock_immediately_before_receipt_write': clock()}
p = D / 'reviewer-artifact-receipt-v1.json'
with p.open('x') as f:
    json.dump(r, f, indent=2)
    f.write('\n')
report = next(a for a in artifacts if a['path'].endswith('/review-v1.md'))
print(json.dumps({'review': report, 'receipt': str(p), 'status': r['status'], 'verdict':r['verdict']}))
