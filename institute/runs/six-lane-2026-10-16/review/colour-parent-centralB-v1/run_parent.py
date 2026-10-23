"""Parent replay of independently written mpmath.iv central checker and its negative control."""
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
PY = '/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/random5reg-colour/.venv/bin/python'
PINS = {'central_iv.py': 'cca710e9efeeb98358ae4407457505856927b10210d7d884a9a350f1bc99f9e0',
        'cb_common.py': '9d3ad5abb52c3ac9ad1bc1027ae9618040d01b3f7e6266f48651ca91ba183726'}


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def main():
    if (HERE / 'parent-result.json').exists():
        raise ValueError('refusing overwrite')
    for name, expected in PINS.items():
        if hashlib.sha256((HERE / name).read_bytes()).hexdigest() != expected:
            raise ValueError('source pin ' + name)
    result = {'started_at_pt': stamp(), 'pins': PINS, 'trials': []}
    for name, nc, eps, expected in [('positive', '8', '3/20', 0), ('zero-eps-negative', '4', '0/1', 1)]:
        output = HERE / (name + '.json')
        if output.exists():
            raise ValueError('refusing overwrite ' + name)
        cmd = [PY, '-B', str(HERE / 'central_iv.py'), '--nc', nc, '--eps', eps, '--out', str(output)]
        t = time.monotonic()
        p = subprocess.run(cmd, cwd=HERE, capture_output=True, text=True, timeout=600)
        for suffix, text in [('stdout', p.stdout), ('stderr', p.stderr)]:
            with (HERE / (name + '.' + suffix)).open('x') as f:
                f.write(text)
        evidence = json.loads(output.read_text())
        matched = p.returncode == expected and evidence['PASS'] == (expected == 0)
        result['trials'].append({'name': name, 'command': cmd, 'returncode': p.returncode,
                                 'expected_returncode': expected, 'matches': matched,
                                 'wall_seconds': round(time.monotonic() - t, 3), 'result': evidence})
    result['status'] = 'PARENT_CENTRAL_IV_AND_NEGATIVE_CONTROL_PASS' if all(t['matches'] for t in result['trials']) else 'FAIL'
    result['finished_at_pt'] = stamp()
    with (HERE / 'parent-result.json').open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({'status': result['status'], 'trials':
                      [(t['name'], t['returncode'], t['matches']) for t in result['trials']]}))
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
