"""Addendum for hostile-review findings m2/m3: bind every parent check output and the worker verifier to the
pinned CDF witnesses, and exercise the parent checker's CLI rejections (SHA, v, k).

Writes cdf-receipt-binding-addendum-v1/ and refuses to overwrite it. Reads only pinned copies under review/.
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
OUT = HERE / 'cdf-receipt-binding-addendum-v1'
WORKER_VERIFIER = ROOT / 'information-science/evidence/six-lane-20261016/cdf-k5/code/verify_cdf.py'
PARENT_CHECKER = HERE / 'check_cdf_independent.py'
WITNESSES = [
    (321, 'cdf321-parent-inputs-v1/cdf_321.txt', 'cdf321-parent-verification-cdf_321-v1.json'),
    (321, 'cdf321-parent-inputs-v1/cdf_321_alt_seed2.txt', 'cdf321-parent-verification-cdf_321_alt_seed2-v1.json'),
    (321, 'cdf321-parent-inputs-v1/cdf_321_alt_seed3.txt', 'cdf321-parent-verification-cdf_321_alt_seed3-v1.json'),
    (501, 'cdf501-parent-inputs-v1/cdf_501.txt', 'cdf501-parent-verification-v1.json'),
    (501, 'cdf501-parent-inputs-v1/cdf_501_alt_seed2.txt', 'cdf501-alt-parent-verification-v1.json'),
    (621, 'cdf621-parent-inputs-v1/cdf_621.txt', 'cdf621-cdf_621-parent-check-v1.json'),
    (681, 'cdf681-parent-inputs-v1/cdf_681.txt', 'cdf681-parent-verification-cdf_681-v1.json'),
    (801, 'cdf801-parent-inputs-v1/cdf_801.txt', 'cdf801-cdf_801-parent-check-v1.json'),
    (901, 'cdf901-parent-inputs-v1/cdf_901.txt', 'cdf901-cdf_901-parent-check-v1.json'),
]


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def main():
    OUT.mkdir(exist_ok=False)
    verifier_copy = OUT / 'verify_cdf.worker-copy.py'
    shutil.copyfile(WORKER_VERIFIER, verifier_copy)
    result = {'recorded_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'script_sha256': sha(__file__), 'parent_checker_sha256': sha(PARENT_CHECKER),
              'worker_verifier_source': str(WORKER_VERIFIER), 'worker_verifier_sha256': sha(verifier_copy),
              'witnesses': [], 'cli_controls': []}
    failures = []
    for v, rel, parent_json in WITNESSES:
        cert = HERE / rel
        cert_sha = sha(cert)
        parent_out = HERE / parent_json
        parent = json.loads(parent_out.read_text())
        proc = subprocess.run([sys.executable, '-B', str(verifier_copy), str(cert)], capture_output=True, text=True, timeout=600)
        worker = json.loads(proc.stdout)
        row = {'v': v, 'certificate': rel, 'certificate_sha256': cert_sha,
               'parent_output': parent_json, 'parent_output_sha256': sha(parent_out),
               'parent_status': parent.get('status'), 'parent_certificate_sha256': parent.get('certificate_sha256'),
               'parent_v': parent.get('v'), 'parent_k': parent.get('k'),
               'worker_verifier_rc': proc.returncode, 'worker_report': worker}
        ok = (parent.get('status') == 'VALID' and parent.get('certificate_sha256') == cert_sha and parent.get('v') == v
              and parent.get('k') == 5 and proc.returncode == 0 and worker.get('verdict') == 'ACCEPT'
              and worker.get('sha256') == cert_sha and worker.get('v') == v and worker.get('k') == 5)
        row['bound'] = ok
        if not ok:
            failures.append(rel)
        result['witnesses'].append(row)
    # Parent checker CLI branches that the earlier controls did not exercise.
    base = HERE / 'cdf321-parent-inputs-v1/cdf_321.txt'
    base_sha = sha(base)
    k6 = OUT / 'fixture-header-k6.txt'
    text = base.read_text().replace('CDF 321 5', 'CDF 321 6', 1)
    with k6.open('x') as stream:
        stream.write(text)
    controls = [('wrong_sha', [str(base), '321', '0' * 64], 'SHA-256 mismatch'),
                ('wrong_v', [str(base), '501', base_sha], 'Unexpected parameters'),
                ('header_k6', [str(k6), '321', sha(k6)], 'Unexpected parameters')]
    for name, args, reason in controls:
        out_path = OUT / f'control-{name}-must-not-exist.json'
        proc = subprocess.run([sys.executable, '-B', str(PARENT_CHECKER)] + args + [str(out_path)],
                              capture_output=True, text=True, timeout=120)
        intended = proc.returncode != 0 and reason in (proc.stderr + proc.stdout) and not out_path.exists()
        result['cli_controls'].append({'control': name, 'returncode': proc.returncode, 'stderr': proc.stderr.strip()[-300:],
                                       'expected_reason': reason, 'intended_rejection': intended})
        if not intended:
            failures.append(name)
    result['status'] = 'BINDING_AND_CLI_CONTROLS_PASS' if not failures else 'FAIL'
    result['failures'] = failures
    result['scope'] = ('Binds existing parent checker outputs and a parent-executed run of the worker verifier to the pinned bytes; '
                       'the worker verifier itself takes no expected v/k/SHA, so binding is enforced here by comparing its report.')
    with (OUT / 'result.json').open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps({k: result[k] for k in ('status', 'failures', 'cli_controls')}, indent=2))
    return 0 if not failures else 1


if __name__ == '__main__':
    raise SystemExit(main())
