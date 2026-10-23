"""Parent replay of the frozen r2 polynomial and central certificates, with failure controls."""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
SNAP = HERE / 'colour-complete-claim-snapshot-r2'
OUT = HERE / 'colour-final-r2-parent-replay-v1'
PY = '/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/random5reg-colour/.venv/bin/python'


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def run(name, path, args, expected_rc, expected_verdict=None, optimize=False, reason=None):
    command = [PY] + (['-O'] if optimize else []) + ['-B', str(SNAP / path)] + args
    t = time.monotonic()
    p = subprocess.run(command, capture_output=True, text=True, timeout=900)
    (OUT / (name + '.stdout')).write_text(p.stdout)
    (OUT / (name + '.stderr')).write_text(p.stderr)
    parsed = json.loads(p.stdout) if p.stdout.strip() else None
    match = p.returncode == expected_rc
    if expected_verdict is not None:
        match = match and parsed is not None and parsed.get('verdict', 'PASS' if parsed.get('PASS') else 'FAIL') == expected_verdict
    if reason is not None:
        match = match and reason in (p.stdout + p.stderr)
    if not match:
        raise ValueError((name, p.returncode, expected_rc, p.stdout[-500:], p.stderr[-500:]))
    return {'name': name, 'command': command, 'returncode': p.returncode, 'expected_returncode': expected_rc,
            'wall_seconds': round(time.monotonic() - t, 3), 'matches': match, 'result': parsed}


def main():
    OUT.mkdir(exist_ok=False)
    result = {'status': 'FAILED', 'started_at_pt': stamp(), 'driver_sha256': sha(__file__)}
    try:
        pins = {}
        for line in (SNAP / 'MANIFEST-r2.sha256').read_text().splitlines():
            h, rest = line.split('  ', 1)
            rel = rest.split('  # ', 1)[0]
            if (SNAP / rel).is_file():
                if sha(SNAP / rel) != h:
                    raise ValueError('snapshot pin ' + rel)
                pins[rel] = h
        result['snapshot_file_hashes'] = pins
        version_cmd = [PY, '-B', '-c',
                       'import sys,json,os,flint,mpmath;print(json.dumps({"python":sys.version,"optimize":sys.flags.optimize,"flint":flint.__version__,"mpmath":mpmath.__version__,"PYTHONOPTIMIZE_set":bool(os.environ.get("PYTHONOPTIMIZE"))}))']
        version = subprocess.run(version_cmd, capture_output=True, text=True, check=True)
        result['runtime'] = json.loads(version.stdout)
        if result['runtime']['optimize'] != 0:
            raise ValueError('optimised interpreter')
        poly_cmd = [PY, '-B', str(SNAP / 'code/slice_poly_dump_r2.py'), '--stdout',
                    '--compare', str(SNAP / 'evidence/slice_minors_rainbow.json')]
        polynomial = subprocess.run(poly_cmd, capture_output=True, timeout=300)
        (OUT / 'polynomial.json').write_bytes(polynomial.stdout)
        (OUT / 'polynomial.stderr').write_bytes(polynomial.stderr)
        if polynomial.returncode != 0 or sha(OUT / 'polynomial.json') != pins['evidence/slice_minors_rainbow.json']:
            raise ValueError('coefficient regeneration differs')
        result['polynomial'] = {'command': poly_cmd, 'returncode': polynomial.returncode,
                                'sha256': sha(OUT / 'polynomial.json'), 'byte_identical': True}
        a = 'code/cert_ldc3_r2.py'
        b = 'checkerB/code/central_iv_r2.py'
        trials = [
            run('A-positive', a, ['1/10000', '3/20', '12', '4'], 0, 'PASS'),
            run('A-zero-eps', a, ['1/10000', '0', '4', '2'], 1, 'FAIL'),
            run('A-zero-grid', a, ['1/10000', '3/20', '0', '0'], 1, reason='positive integers'),
            run('A-negative-grid', a, ['1/10000', '3/20', '-1', '-1'], 1, reason='positive integers'),
            run('A-optimized', a, ['1/10000', '3/20', '12', '4'], 1, optimize=True, reason='refusing'),
            run('B-positive', b, ['--nc', '8', '--eps', '3/20'], 0, 'PASS'),
            run('B-zero-eps', b, ['--nc', '4', '--eps', '0'], 1, 'FAIL'),
            run('B-zero-grid', b, ['--nc', '0'], 2, 'FAIL'),
            run('B-negative-grid', b, ['--nc', '-1'], 2, 'FAIL'),
            run('B-optimized', b, ['--nc', '8'], 3, 'REFUSED', optimize=True),
        ]
        ap, bp = trials[0]['result'], trials[5]['result']
        if ap['Q_check']['boxes'] != 1728 or ap['C_check']['boxes'] != 256:
            raise ValueError('A coverage totals')
        if bp['Q']['subboxes_checked'] != 512 or bp['C']['vertices_checked'] != 16:
            raise ValueError('B coverage totals')
        result['trials'] = trials
        result['status'] = 'PARENT_R2_COEFFICIENT_CENTRAL_AND_FAILURE_CONTROLS_PASS'
        result['outer_evidence'] = ['colour-parent-replay-v1/parent-replay-result.json',
                                    'colour-codex-checker-v1/parent-result.json']
        result['scope'] = 'New r2 polynomial and central code re-executed. Outer trees and outer checkers are unchanged from the parent A/C full replays; their hashes remain bound by both manifests.'
    except Exception as exc:
        result['error'] = type(exc).__name__ + ': ' + str(exc)
    result['finished_at_pt'] = stamp()
    with (OUT / 'parent-result.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({k: result.get(k) for k in ['status', 'error', 'runtime']}, indent=2))
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
