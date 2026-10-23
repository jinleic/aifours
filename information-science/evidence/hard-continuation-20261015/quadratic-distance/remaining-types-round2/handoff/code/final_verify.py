#!/usr/bin/env python3
"""Single final verification pass for remaining-types-round2.

1. Runs code/audit.py in place, normally and under python -O; both must PASS.
2. Corruption controls: each copies the directory to a temporary location,
   applies one meaningful corruption and reruns the audit copy, normally and
   under -O. Each run must fail with an explicit AUDIT FAIL / ValueError.
3. Writes results/final-verify.json with return codes, elapsed times and
   SHA-256 of every code/input/result file. Refuses to overwrite it.
"""
import hashlib, json, os, shutil, subprocess, sys, tempfile, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..'))
OUT = os.path.join(ROOT, 'results', 'final-verify.json')


def need(cond, label):
    if not cond:
        raise ValueError('FINAL VERIFY FAIL: ' + label)


def run(root, opt):
    cmd = [sys.executable] + (['-O'] if opt else []) + [os.path.join(root, 'code', 'audit.py')]
    t = time.time()
    p = subprocess.run(cmd, capture_output=True, text=True, cwd=root)
    return {'cmd': ' '.join(['python3'] + (['-O'] if opt else []) + ['code/audit.py']), 'returncode': p.returncode,
            'seconds': round(time.time() - t, 2), 'stdout_tail': p.stdout[-300:], 'stderr_tail': p.stderr[-300:]}


def edit_json(path, fn):
    with open(path) as fh:
        d = json.load(fh)
    fn(d)
    with open(path, 'w') as fh:
        json.dump(d, fh)


def c_minc(d):
    d['single_character_min_c']['c'] = 12


def c_split(d):
    d['z8_classes']['8a'] = 16


def c_valid(d):
    for e in d['classes']:
        if e['hist'] == [[8, 64]]:
            e['ell4']['valid_sets'] += 1


def c_orbit(d):
    d['cubic_classes'][1]['orbit_size'] += 1


def c_newwit(d):
    d['aux']['R1'][0][-1] += 1
    d['aux']['R1'][1][-1] -= 1


def c_fiber(d):
    d['z8_noninvariant_sets'][0]['D1_fibers'] = [13, 23]


CORRUPTIONS = [
    ('results/rank6-144-zero-sets.json', c_minc, 'single-character minimum c claimed 12 instead of 14'),
    ('results/rank4-160-structure.json', c_split, 'z=8 class 8a count claimed 16'),
    ('results/rank2-coset-realizability.json', c_valid, 'bent ell=4 valid subset count +1'),
    ('results/rank2-cubic-classes.json', c_orbit, 'cubic orbit size +1'),
    ('results/rank2-probe2-z8.json', c_newwit, 'new witness R1 counts shifted (marginals broken)'),
    ('results/rank6-144-zero-sets.json', c_fiber, 'one (6,144) fiber pair claimed 13/23'),
    ('inputs/round1-rank2-probe-scross-aux.json', None, 'pinned round-1 witness byte change'),
]


def main():
    if os.path.exists(OUT):
        print('refusing to overwrite', OUT)
        sys.exit(2)
    t0 = time.time()
    rec = {'clean': [run(ROOT, False), run(ROOT, True)], 'corruptions': []}
    for r in rec['clean']:
        need(r['returncode'] == 0 and '"verdict": "PASS"' in r['stdout_tail'], 'clean audit must pass: ' + r['cmd'])
    for rel, fn, label in CORRUPTIONS:
        with tempfile.TemporaryDirectory() as td:
            dst = os.path.join(td, 'r2')
            shutil.copytree(ROOT, dst, ignore=shutil.ignore_patterns('handoff', '*.gz'))
            path = os.path.join(dst, rel)
            if fn is None:
                with open(path, 'ab') as fh:
                    fh.write(b' ')
            else:
                edit_json(path, fn)
            runs = [run(dst, False), run(dst, True)]
            for r in runs:
                need(r['returncode'] != 0 and ('AUDIT FAIL' in r['stderr_tail'] or 'ValueError' in r['stderr_tail']),
                     'corruption must fail explicitly: ' + label)
            rec['corruptions'].append({'file': rel, 'corruption': label, 'runs': runs})
    hashes = {}
    for sub in ('code', 'inputs', 'results'):
        for name in sorted(os.listdir(os.path.join(ROOT, sub))):
            p = os.path.join(ROOT, sub, name)
            if os.path.isfile(p) and name != 'final-verify.json':
                with open(p, 'rb') as fh:
                    hashes[sub + '/' + name] = hashlib.sha256(fh.read()).hexdigest()
    for name in ('PROOF.md',):
        with open(os.path.join(ROOT, name), 'rb') as fh:
            hashes[name] = hashlib.sha256(fh.read()).hexdigest()
    rec['sha256'] = hashes
    rec['seconds'] = round(time.time() - t0, 2)
    rec['verdict'] = 'PASS'
    with open(OUT, 'w') as fh:
        json.dump(rec, fh, indent=1)
    print(json.dumps({'verdict': 'PASS', 'clean': [(r['cmd'], r['returncode'], r['seconds']) for r in rec['clean']],
                      'corruptions_failed_as_required': len(rec['corruptions']), 'seconds': rec['seconds']}))


if __name__ == '__main__':
    main()
