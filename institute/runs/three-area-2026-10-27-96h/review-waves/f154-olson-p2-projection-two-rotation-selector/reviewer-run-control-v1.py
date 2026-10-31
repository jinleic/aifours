import hashlib
import json
import pathlib
import resource
import subprocess
import sys
import time

D = pathlib.Path('/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-27-96h/review-waves/f154-olson-p2-projection-two-rotation-selector')
E = pathlib.Path('/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261027-96h/parallel-18/ordered-olson')
EXPECTED = [
    (D / 'manifest-v1.json', '6204853698b308eefb05025d008a21fa6ad229a2e2e14f4a879b22d118d8f374', 2741, 30),
    (E / 'frontier-20261028-olson-actual-block-fatal-correction-v1.json', 'e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e', 9278, 92),
    (E / 'frontier-20261028-olson-p2-band-v1.md', '2b02c24161f4cc2127ee180a0eebd6a03326a3428c6defbe176c80f9619046f1', 13059, 83),
]

def clock():
    return subprocess.check_output(['/bin/date', '+%Y-%m-%dT%H:%M:%S%z %Z'], text=True).strip()

def metadata(p):
    b = p.read_bytes()
    return {'path': str(p), 'sha256': hashlib.sha256(b).hexdigest(), 'bytes': len(b), 'LF': b.count(b'\n')}

def require(b, message):
    if not b:
        raise RuntimeError(message)

mode = sys.argv[1]
require(mode in ('q5', 'p7'), 'mode')
receipt = D / f'reviewer-receipt-{mode}-v1.json'
stdout = D / f'reviewer-stdout-{mode}-v1.json'
stderr = D / f'reviewer-stderr-{mode}-v1.txt'
for p in (receipt, stdout, stderr):
    require(not p.exists(), f'refusing overwrite {p}')
verified = []
for p, sha, size, lf in EXPECTED:
    m = metadata(p)
    require(m['sha256'] == sha and m['bytes'] == size and m['LF'] == lf, f'pin mismatch {m}')
    verified.append(m)
source = D / 'reviewer-exact-control-v1.cpp'
binary = D / 'reviewer-exact-control-v1.bin'
compile_record = None
if mode == 'q5':
    require(not binary.exists(), 'refusing binary overwrite')
    argv = ['/usr/bin/cc', '-x', 'c++', '-std=c++17', '-O2', str(source), '-lc++', '-o', str(binary)]
    started = clock()
    cp = subprocess.run(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    compile_record = {'argv': argv, 'started': started, 'finished': clock(), 'returncode': cp.returncode, 'stdout': cp.stdout, 'stderr': cp.stderr}
    require(cp.returncode == 0, json.dumps(compile_record))
argv = [str(binary), mode]
started = clock()
t0 = time.monotonic()
with stdout.open('x') as out, stderr.open('x') as err:
    proc = subprocess.Popen(argv, stdin=subprocess.DEVNULL, stdout=out, stderr=err)
    rc = proc.wait()
finished = clock()
r = {'kind': 'REVIEWER_BOUNDED_EXACT_CONTROL_RECEIPT', 'argv': argv, 'pid': proc.pid,
     'started': started, 'finished': finished, 'elapsed_seconds': time.monotonic() - t0,
     'returncode': rc, 'complete': rc == 0, 'compile': compile_record, 'verified_inputs_in_order': verified,
     'source': metadata(source), 'binary': metadata(binary), 'runner': metadata(pathlib.Path(__file__)),
     'stdout': metadata(stdout), 'stderr': metadata(stderr),
     'observed_children_ru_maxrss_native': resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss,
     'limits': 'Single CPU child; cooperative 240s deadline; no OS memory enforcement claimed; no author code executed.',
     'observed_clock_immediately_before_receipt_write': clock()}
with receipt.open('x') as f:
    json.dump(r, f, indent=2)
    f.write('\n')
print(json.dumps({'receipt': str(receipt), 'returncode': rc, 'elapsed_seconds': r['elapsed_seconds']}))
if rc:
    sys.exit(rc)
