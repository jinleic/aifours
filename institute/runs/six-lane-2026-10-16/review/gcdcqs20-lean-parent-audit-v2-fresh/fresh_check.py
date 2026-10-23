#!/usr/bin/python3
"""Fresh-kernel step for the parent gcDCQS replay v2 (whose builds, binding, negatives and axioms passed but whose
leanchecker step failed because PATH lacked the toolchain's `lean`). Uses v2's parent-built oleans read-only.
Refuses to overwrite its receipt; no timeouts or kills."""
import hashlib, json, os, subprocess, time
from pathlib import Path
HERE = Path(__file__).resolve().parent
V2 = HERE.parent / 'gcdcqs20-lean-parent-audit-v2'
OUT = HERE / 'parent-result.json'
if OUT.exists():
    raise SystemExit('refusing existing receipt')
TC = Path('/Users/jinleic/.elan/toolchains/leanprover--lean4---v4.34.1')
CACHE = Path('/private/tmp/seymour-lean-20261014-68365/.lake/packages')
lp = str(V2 / 'build') + ''.join(':' + str(CACHE / p / '.lake/build/lib/lean') for p in
     ['mathlib', 'batteries', 'aesop', 'Qq', 'proofwidgets', 'plausible', 'LeanSearchClient', 'importGraph'])
env = dict(os.environ, LEAN_PATH=lp, PATH=str(TC / 'bin') + ':' + os.environ.get('PATH', ''))
now = lambda: subprocess.check_output(['date', '+%Y-%m-%d %H:%M:%S %Z'], text=True).strip()
v2 = json.loads((V2 / 'parent-result.json').read_text())
res = {'started_at_pt': now(), 'v2_receipt_sha256': hashlib.sha256((V2 / 'parent-result.json').read_bytes()).hexdigest(),
       'v2_prior_steps_ok': all(s['exit_code'] == 0 for s in v2['steps'] if s['name'].startswith(('regenerate', 'build-')) and 'Neg' not in s['name']),
       'v2_negatives_ok': all(v['exit_code'] != 0 and v['type_mismatch_reported'] and not v['olean_written'] for v in v2['negatives'].values()),
       'v2_axioms_ok': v2['axioms_ok'], 'v2_failure_cause': 'leanchecker could not execute external process lean (PATH)',
       'parent_audit_olean_sha256': hashlib.sha256((V2 / 'build' / 'ParentAudit.olean').read_bytes()).hexdigest()}
t0 = time.monotonic()
p = subprocess.run(['/usr/bin/time', '-l', str(TC / 'bin/leanchecker'), '--fresh', '-v', 'ParentAudit'],
                   cwd=V2 / 'src', env=env, capture_output=True, text=True)
res['fresh'] = {'exit_code': p.returncode, 'wall_seconds': round(time.monotonic() - t0, 3),
                'output_tail': (p.stdout + p.stderr)[-2500:]}
ok = p.returncode == 0 and 'replaying ParentAudit with --fresh' in p.stdout + p.stderr
res['status'] = ('PARENT_GC80_BINDING_REBUILD_AND_FRESH_KERNEL_PASS' if ok and res['v2_prior_steps_ok']
                 and res['v2_negatives_ok'] and res['v2_axioms_ok'] else 'FAIL')
res['finished_at_pt'] = now()
with OUT.open('x') as f:
    json.dump(res, f, indent=2); f.write('\n')
print(res['status'])
raise SystemExit(0 if res['status'].endswith('PASS') else 1)
