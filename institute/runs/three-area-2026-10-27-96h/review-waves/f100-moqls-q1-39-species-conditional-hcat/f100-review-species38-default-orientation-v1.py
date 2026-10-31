#!/usr/bin/env python3
"""f100 review side check: species 38 in the default orientation (row class 0, column class 1, anchor 0),
CNF produced by the reviewer's encoder, solved by the local kissat with a bounded wall time, proof verified
by the reviewer's checker.  Informational: any orientation yields a sound necessary CNF."""
import hashlib, importlib.util, json, pathlib, subprocess, time

HERE = pathlib.Path(__file__).resolve().parent
def load(name):
    spec = importlib.util.spec_from_file_location(name[:-3].replace('-', '_'), HERE / name)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
enc = load('f100-review-encoder-v1.py'); rup = load('f100-review-rup-check-v1.py')
SOLVER = '/opt/homebrew/bin/kissat'

def main():
    out = HERE / 'f100-review-species38-default-orientation-receipt-v1.json'
    cnf = HERE / 'f100-review-species38-r0c1a0-v1.cnf'; proof = HERE / 'f100-review-species38-r0c1a0-v1.drup'
    for p in (out, cnf, proof):
        if p.exists():
            raise SystemExit('refusing to overwrite ' + str(p))
    triples = enc.load_triples()
    clauses, numbering, stats, A, lines = enc.build(triples[38], 0, 1, 0)
    data = ('p cnf %d %d\n' % (len(numbering), len(clauses)) +
            ''.join(' '.join(str(numbering[n] * sg) for n, sg in cl) + ' 0\n' for cl in clauses)).encode('ascii')
    with cnf.open('xb') as h:
        h.write(data)
    solver_sha = hashlib.sha256(pathlib.Path(SOLVER).read_bytes()).hexdigest()
    args = [SOLVER, '--quiet', '--no-binary', '--time=60', str(cnf), str(proof)]
    t0 = time.monotonic()
    p = subprocess.run(args, stdin=subprocess.DEVNULL, capture_output=True)   # bounded by kissat's own --time; no external kill
    wall = time.monotonic() - t0
    s_lines = [x.rstrip('\r') for x in p.stdout.decode().split('\n') if x.startswith('s ')]
    rec = {'orientation': [0, 1, 0], 'stats': stats, 'cnf_sha256': hashlib.sha256(data).hexdigest(), 'cnf_bytes': len(data),
           'solver': SOLVER, 'solver_sha256_before': solver_sha, 'solver_sha256_after': hashlib.sha256(pathlib.Path(SOLVER).read_bytes()).hexdigest(),
           'args': args[1:], 'returncode': p.returncode, 's_lines': s_lines, 'stderr': p.stderr.decode(), 'wall_seconds': wall}
    if proof.exists():
        pb = proof.read_bytes()
        rec['proof_sha256'] = hashlib.sha256(pb).hexdigest(); rec['proof_bytes'] = len(pb)
        if p.returncode == 20 and s_lines == ['s UNSATISFIABLE']:
            r = rup.check(data, pb)
            rec['reviewer_rup'] = {k: r[k] for k in ('verdict', 'additions', 'deletions', 'rup_verified', 'empty_clause_verified', 'lines_after_empty')}
    with out.open('x', encoding='utf-8') as h:
        json.dump(rec, h, indent=1); h.write('\n')
    print(json.dumps({k: rec[k] for k in rec if k not in ('stats', 'args')}, indent=1))

if __name__ == '__main__':
    main()
