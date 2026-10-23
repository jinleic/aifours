"""Parent execution of independently authored checker C; pins inputs and saves controls."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import hashlib
import json
from pathlib import Path
import subprocess
import time
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
LANE = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/random5reg-colour')
PY = str(LANE / '.venv/bin/python')
CHECKER = HERE / 'checker_c.py'


def sha(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def stamp():
    return datetime.now(ZoneInfo('America/Los_Angeles')).isoformat()


def run(name, args, expected=0, reason=None):
    t = time.monotonic()
    p = subprocess.run([PY, '-B', str(CHECKER)] + args,
                       capture_output=True, text=True, timeout=1800)
    for suffix, text in [('stdout', p.stdout), ('stderr', p.stderr)]:
        with (HERE / (name + '.' + suffix)).open('x') as f:
            f.write(text)
    r = json.loads(p.stdout)
    ok = p.returncode == expected and r['verdict'] == ('PASS' if expected == 0 else 'FAIL')
    if reason is not None:
        ok = ok and reason in json.dumps(r['first_failures'])
    return {'name': name, 'returncode': p.returncode, 'expected_returncode': expected,
            'intended_reason': reason, 'matches': ok,
            'wall_seconds': round(time.monotonic() - t, 3), 'result': r}


def main():
    out = HERE / 'parent-result.json'
    if out.exists():
        raise ValueError('refusing overwrite')
    assert sha(CHECKER) == 'e4c055dab0bdcecddd5373db42e9c5e8db1ae3f53abd6722e31ac526ce3ea217'
    result = {'started_at_pt': stamp(), 'checker_sha256': sha(CHECKER),
              'driver_sha256': sha(__file__), 'independence':
              'Codex wrote this checker from the mathematical specification and JSON format; '
              'the prompt barred access to worker checker implementations. It uses Arb like A; '
              'worker checker B uses mpmath.iv. Authorship and arithmetic-library independence differ.'}
    result['selftests'] = [run('selftest' + str(bits), ['--selftest', '--prec', str(bits)])
                           for bits in (128, 200)]
    pins = {}
    for line in (LANE / 'outer/evidence/SHA256SUMS').read_text().splitlines():
        h, _, rel = line.partition('  ')
        pins[rel.strip()] = h
    cones = ['00', '01', '02', '10', '11', '12', '20', '21', '22']

    def cone(c):
        cert = LANE / ('outer/evidence/cone' + c + '.json')
        assert sha(cert) == pins['evidence/cone' + c + '.json']
        return run('cone' + c, [str(cert), '--expect-facet', c[0], c[1]])

    with ThreadPoolExecutor(max_workers=3) as pool:
        result['cones'] = list(pool.map(cone, cones))
    base = LANE / 'outer/evidence/mutations/base_cone00_r1_1over20.json'
    assert sha(base) == pins['evidence/mutations/base_cone00_r1_1over20.json']
    result['positive_base'] = run('positive-base', [str(base), '--allow-r0', '1/20'])
    fixtures = HERE / 'controls'
    fixtures.mkdir(exist_ok=False)
    original = base.read_bytes()
    mutations = [
        ('wrong-facet', 'facet does not match'),
        ('zero-mu', 'strictly positive'),
        ('bad-hex', 'hexadecimal literal'),
        ('zero-dual', 'not rigorously positive'),
        ('relabel-central', 'outside the closed central box'),
        ('drop-last-node', 'truncated preorder'),
        ('append-node', 'trailing nodes'),
        ('changed-radius', 'r0 must equal'),
    ]
    result['controls'] = []
    for name, reason in mutations:
        doc = json.loads(original)
        first = next(i for i, n in enumerate(doc['tree']) if n[0] == 'D')
        node = doc['tree'][first]
        flags = ['--allow-r0', '1/20']
        if name == 'wrong-facet':
            flags += ['--expect-facet', '0', '1']
        elif name == 'zero-mu':
            node[2][0][0] = '0x0.0p+0'
        elif name == 'bad-hex':
            node[1][0] = 'not-a-rational'
        elif name == 'zero-dual':
            node[1] = ['0x0.0p+0'] * 18
            node[2] = [['0x1.0p+0'] * 4 for _ in range(9)]
        elif name == 'relabel-central':
            doc['tree'][first] = ['C']
        elif name == 'drop-last-node':
            doc['tree'] = doc['tree'][:-1]
        elif name == 'append-node':
            doc['tree'].append(['C'])
        elif name == 'changed-radius':
            doc['r0'] = '1/5000'
            flags = []
        path = fixtures / (name + '.json')
        with path.open('x') as f:
            json.dump(doc, f, separators=(',', ':'))
        trial = run('control-' + name, [str(path)] + flags, expected=1, reason=reason)
        trial['fixture_sha256'] = sha(path)
        result['controls'].append(trial)
    checks = result['selftests'] + result['cones'] + [result['positive_base']] + result['controls']
    result['status'] = 'PARENT_INDEPENDENT_CHECKER_AND_CONTROLS_PASS' if all(r['matches'] for r in checks) else 'FAIL'
    result['totals'] = {k: sum(c['result'][k] for c in result['cones'])
                        for k in ['nodes', 'splits', 'dual_leaves', 'central_leaves', 'failed_leaves']}
    result['finished_at_pt'] = stamp()
    with out.open('x') as f:
        json.dump(result, f, indent=2)
        f.write('\n')
    print(json.dumps({'status': result['status'], 'totals': result['totals'],
                      'controls': [(x['name'], x['matches']) for x in result['controls']]}), flush=True)
    return 0 if result['status'].endswith('PASS') else 1


if __name__ == '__main__':
    raise SystemExit(main())
