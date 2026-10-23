"""Parent replay of the non-load-bearing fixed AG(2,8) K1 certificates.

Pins the two original encoders and the CNFs/proofs; rebuilds with slopes 1,2,3,4, quantum 1, p4 1;
compares CNFs byte-for-byte; checks both binary DRAT proofs with the parent's drat-trim build.
K1's written analytic proof does not need these certificates. All outputs use exclusive creation.
"""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
LANE = Path('/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16')
DT = HERE.parent / 'moqls7-parent-proofcheck-v1/drat-trim'
EXPECTED_DT = 'a46c0c717f702206a7fe345de5bcdc0b10112bca6bdbf04dd42cd9848ff08e37'


def sha(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def main():
    inputs, regen = HERE / 'inputs', HERE / 'regen'
    inputs.mkdir(exist_ok=False)
    regen.mkdir(exist_ok=False)
    rec = {'started': now(), 'files': {}, 'rows': [], 'drat_trim_sha256': sha(DT)}
    if rec['drat_trim_sha256'] != EXPECTED_DT:
        raise ValueError('Parent checker SHA mismatch')
    files = ['code/enc8_a.py', 'code/enc8_b.py', 'evidence/k1_cert_v1/a_K1.cnf.map.json']
    for enc in ('a', 'b'):
        files += ['evidence/k1_cert_v1/%s_K1.%s' % (enc, suffix) for suffix in ('cnf', 'drat')]
    for rel in files:
        src, dest = LANE / rel, inputs / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        before = sha(src)
        r = subprocess.run(['cp', '-c', str(src), str(dest)], capture_output=True, text=True)
        if r.returncode or sha(dest) != before:
            raise ValueError('Pin mismatch: ' + rel)
        rec['files'][rel] = before
    m = json.loads((inputs / 'evidence/k1_cert_v1/a_K1.cnf.map.json').read_text())
    rec['encoder_a_map_bound'] = m['meta']['script_sha256'] == rec['files']['code/enc8_a.py']
    for enc in ('a', 'b'):
        cnf = regen / ('%s_K1.cnf' % enc)
        argv = ['/usr/bin/python3', '-B', str(inputs / ('code/enc8_%s.py' % enc)), '--mode', 'fixed',
                '--slopes', '1,2,3,4', '--quantum', '1', '--p4', '1', '--cnf', str(cnf)]
        if enc == 'a':
            argv += ['--map', str(cnf) + '.map.json']
        r = subprocess.run(argv, capture_output=True, text=True)
        pinned = inputs / ('evidence/k1_cert_v1/%s_K1.cnf' % enc)
        proof = inputs / ('evidence/k1_cert_v1/%s_K1.drat' % enc)
        row = {'encoder': enc, 'encoder_rc': r.returncode, 'argv': argv,
               'cnf_equal': r.returncode == 0 and sha(cnf) == sha(pinned)}
        d = subprocess.run([str(DT), str(pinned), str(proof), '-t', '600'], capture_output=True)
        lines = [x.strip() for x in d.stdout.decode('utf-8', 'replace').split('\n')]
        row['drat_rc'] = d.returncode
        row['drat_status'] = [x for x in lines if x.startswith('s ')]
        row['output_sha256'] = hashlib.sha256(d.stdout).hexdigest()
        with open(HERE / ('%s.drat-trim.log' % enc), 'xb') as f:
            f.write(d.stdout)
        row['verified'] = d.returncode == 0 and row['drat_status'] == ['s VERIFIED']
        rec['rows'].append(row)
    rec['ended'] = now()
    rec['verdict'] = 'PASS' if rec['encoder_a_map_bound'] and all(
        x['cnf_equal'] and x['verified'] for x in rec['rows']) else 'FAIL'
    with open(HERE / 'result.json', 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps({'verdict': rec['verdict'], 'rows': rec['rows']}))


if __name__ == '__main__':
    main()
