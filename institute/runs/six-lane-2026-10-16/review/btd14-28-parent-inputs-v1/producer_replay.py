"""Parent producer replay for the BTD(14,28) witness (explanatory reproducibility, not validity evidence).
Clones the generator, regenerates the restricted Z3-r4-c8 CNF, solves with kissat's native time limit, decodes
with a parent-written decoder from the generator's variable map, checks with the parent checker, and checks the
pinned witness's invariance under the declared row/column permutations.
"""
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
LANE = Path('/Users/jinleic/repos/aifours/information-science/evidence/six-lane-20261016/btd14-28')
OUT = HERE / 'producer-replay'


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def now():
    return subprocess.run(['date', '+%Y-%m-%dT%H:%M:%S%z'], capture_output=True, text=True).stdout.strip()


def main():
    OUT.mkdir(exist_ok=False)
    (OUT / 'code').mkdir()
    pins = {}
    for rel in ('code/inv_cnf_v2.py', 'code/btd_cnf_a.py', 'runs/zp-v1/Z3-r4-c8.cnf', 'runs/zp-v1/Z3-r4-c8.cnf.map.json'):
        dst = OUT / ('code/' + Path(rel).name if rel.startswith('code/') else 'worker-' + Path(rel).name)
        r = subprocess.run(['cp', '-c', str(LANE / rel), str(dst)], capture_output=True, text=True)
        if r.returncode:
            raise ValueError('pin ' + rel)
        pins[rel] = sha(dst)
    cnf = OUT / 'Z3-r4-c8.cnf'
    r = subprocess.run(['/usr/bin/python3', '-B', str(OUT / 'code/inv_cnf_v2.py'), 'Z3-r4-c8', str(cnf)],
                       capture_output=True, text=True, cwd=OUT / 'code')
    rec = {'started': now(), 'pins': pins, 'generator_rc': r.returncode, 'cnf_sha256': sha(cnf),
           'worker_cnf_sha256': pins['runs/zp-v1/Z3-r4-c8.cnf']}
    rec['cnf_equal'] = rec['cnf_sha256'] == rec['worker_cnf_sha256']
    m = json.loads((Path(str(cnf) + '.map.json')).read_text())
    with open(OUT / 'kissat.stdout', 'xb') as so:
        s = subprocess.run(['/opt/homebrew/bin/kissat', '-q', '--time=600', '--seed=0', str(cnf)], stdout=so,
                           stderr=subprocess.STDOUT)
    rec['kissat_rc'] = s.returncode
    model = set()
    for line in (OUT / 'kissat.stdout').read_text().split('\n'):
        if line.startswith('v '):
            model.update(int(t) for t in line.split()[1:] if t != '0')
    if s.returncode == 10:
        M = [[int(m['a'][i][j] in model) + int(m['b'][i][j] in model) for j in range(28)] for i in range(14)]
        bad_b_without_a = sum(1 for i in range(14) for j in range(28) if m['b'][i][j] in model and m['a'][i][j] not in model)
        rec['b_without_a'] = bad_b_without_a
        raw = ('BTD 14 28 8 3 14 7 6\n' + '\n'.join(' '.join(map(str, row)) for row in M) + '\n').encode()
        with open(OUT / 'decoded.btd', 'xb') as f:
            f.write(raw)
        rec['decoded_sha256'] = hashlib.sha256(raw).hexdigest()
        c = subprocess.run(['/usr/bin/python3', '-B', str(HERE / 'check_btd_parent.py'), str(OUT / 'decoded.btd'),
                            '14', '28', '8', '3', '14', '7', '6', rec['decoded_sha256'], str(OUT / 'decoded-check.json')],
                           capture_output=True, text=True)
        rec['decoded_check'] = json.loads((OUT / 'decoded-check.json').read_text())['result']
        rec['decoded_equals_witness'] = raw == (HERE / 'btd14-28-witness-v1.btd').read_bytes()
    W = [list(map(int, l.split())) for l in (HERE / 'btd14-28-witness-v1.btd').read_text().split('\n')[1:-1]]
    g, h = m['row_perm'], m['col_perm']
    rec['row_perm'] = g
    rec['col_perm'] = h
    rec['witness_invariant'] = all(W[g[i]][h[j]] == W[i][j] for i in range(14) for j in range(28))
    rec['row_perm_order3'] = all(g[g[g[i]]] == i for i in range(14)) and any(g[i] != i for i in range(14))
    rec['col_perm_order3'] = all(h[h[h[j]]] == j for j in range(28)) and any(h[j] != j for j in range(28))
    rec['ended'] = now()
    rec['verdict'] = 'PASS' if (r.returncode == 0 and rec['cnf_equal'] and s.returncode == 10
                                and rec.get('decoded_check') == 'VALID' and rec.get('b_without_a') == 0
                                and rec['witness_invariant'] and rec['row_perm_order3'] and rec['col_perm_order3']) else 'FAIL'
    with open(HERE / 'producer-replay-result.json', 'x') as f:
        json.dump(rec, f, indent=1)
        f.write('\n')
    print(json.dumps({k: rec.get(k) for k in ('cnf_equal', 'kissat_rc', 'decoded_check', 'decoded_equals_witness',
                                              'witness_invariant', 'verdict')}))


if __name__ == '__main__':
    main()
