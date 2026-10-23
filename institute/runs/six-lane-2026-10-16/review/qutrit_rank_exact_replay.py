"""Parent replay of the worker's four exact sympy checks for the qutrit rank proof, from the pinned copies in
dualunitary-rank-bound-parent-inputs-v3, inside a new sandbox (the scripts write ../evidence/NAME.json next to
themselves). Compares every boolean result with the pinned worker output and requires all_ok.
Usage: python -B qutrit_rank_exact_replay.py NEW_SANDBOX_DIR   (run with an interpreter that has sympy)
"""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time
from zoneinfo import ZoneInfo

PIN = Path(__file__).resolve().parent / 'dualunitary-rank-bound-parent-inputs-v3'
NAMES = ['relations_exact', 'lemma_T_exact', 'case_algebra_exact', 'marginal_identity_exact']


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def bools(d, prefix=''):
    out = {}
    for k, v in d.items():
        if isinstance(v, bool):
            out[prefix + k] = v
        elif isinstance(v, dict):
            out.update(bools(v, prefix + k + '/'))
    return out


def main():
    box = Path(sys.argv[1]).resolve()
    box.mkdir(exist_ok=False)
    (box / 'code').mkdir()
    (box / 'evidence').mkdir()
    manifest = json.loads((PIN / 'manifest.json').read_text())
    result = {'started_at_pt': datetime.now(ZoneInfo('America/Los_Angeles')).isoformat(),
              'interpreter': sys.executable, 'driver_sha256': sha(__file__), 'runs': [], 'status': 'FAILED'}
    try:
        for n in NAMES:
            for f in (n + '.py', n + '.json'):
                if sha(PIN / f) != manifest['files'][f]['sha256']:
                    raise ValueError('pinned file changed: ' + f)
            shutil.copyfile(PIN / (n + '.py'), box / 'code' / (n + '.py'))
            t = time.monotonic()
            p = subprocess.run([sys.executable, '-B', str(box / 'code' / (n + '.py'))], capture_output=True, text=True,
                               timeout=1800, cwd=box / 'code')
            (box / (n + '.stdout.txt')).write_text(p.stdout)
            (box / (n + '.stderr.txt')).write_text(p.stderr)
            new = json.loads((box / 'evidence' / (n + '.json')).read_text())
            old = json.loads((PIN / (n + '.json')).read_text())
            nb, ob = bools(new), bools(old)
            row = {'check': n, 'returncode': p.returncode, 'seconds': round(time.monotonic() - t, 1),
                   'all_ok': new.get('all_ok'), 'boolean_keys': len(nb), 'booleans_equal_pinned': nb == ob,
                   'byte_identical_to_pinned': sha(box / 'evidence' / (n + '.json')) == sha(PIN / (n + '.json'))}
            result['runs'].append(row)
            print(json.dumps(row), flush=True)
            if p.returncode != 0 or new.get('all_ok') is not True or nb != ob:
                raise ValueError('replay mismatch for ' + n)
        result['status'] = 'PARENT_REPLAY_OF_WORKER_EXACT_CHECKS_PASS'
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    result['finished_at_pt'] = datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()
    with (box / 'parent-result.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(result['status'], result.get('error', ''))
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
