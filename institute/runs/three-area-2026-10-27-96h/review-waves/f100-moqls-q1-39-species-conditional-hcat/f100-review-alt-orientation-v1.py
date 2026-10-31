#!/usr/bin/env python3
"""f100 review: independent corroboration in a different orientation.  For every species, the reviewer's
encoder builds the necessary-support CNF with row class 2, column class 3, anchor symbol 5 (the author used
row class 0/column class 1/anchor 0 for 0-37 and 1/0/0 for 38).  kissat runs with the pure-RUP flag set and a
bounded wall time; each proof is verified by the reviewer's checker.  Files are retained under
alt-orientation-r2c3a5/.  A timeout or unverified proof is reported as such, never as a PASS."""
import hashlib, importlib.util, json, pathlib, subprocess, time

HERE = pathlib.Path(__file__).resolve().parent
def load(name):
    spec = importlib.util.spec_from_file_location(name[:-3].replace('-', '_'), HERE / name)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
enc = load('f100-review-encoder-v1.py'); rup = load('f100-review-rup-check-v1.py')
SOLVER = '/opt/homebrew/bin/kissat'
R, C, S = 2, 3, 5

def main():
    out = HERE / 'f100-review-alt-orientation-receipt-v1.json'
    sub = HERE / 'alt-orientation-r2c3a5'
    if out.exists() or sub.exists():
        raise SystemExit('refusing to overwrite')
    sub.mkdir()
    triples = enc.load_triples()
    solver_sha = hashlib.sha256(pathlib.Path(SOLVER).read_bytes()).hexdigest()
    cases = []
    t0 = time.monotonic()
    for sp in range(39):
        clauses, numbering, stats, A, lines = enc.build(triples[sp], R, C, S)
        data = ('p cnf %d %d\n' % (len(numbering), len(clauses)) +
                ''.join(' '.join(str(numbering[n] * sg) for n, sg in cl) + ' 0\n' for cl in clauses)).encode('ascii')
        cnf = sub / f's{sp:02d}-r{R}c{C}a{S}.cnf'; proof = sub / f's{sp:02d}-r{R}c{C}a{S}.drup'
        with cnf.open('xb') as h:
            h.write(data)
        args = [SOLVER, '--quiet', '--plain', '--no-binary', '--no-preprocess', '--no-eliminate', '--no-substitute', '--no-factor',
                '--no-probe', '--no-sweep', '--no-vivify', '--no-transitive', '--time=60', str(cnf), str(proof)]
        t1 = time.monotonic()
        p = subprocess.run(args, stdin=subprocess.DEVNULL, capture_output=True)
        wall = time.monotonic() - t1
        s_lines = [x.rstrip('\r') for x in p.stdout.decode().split('\n') if x.startswith('s ')]
        rec = {'species': sp, 'orientation': [R, C, S], 'variables': stats['variables'], 'clauses': stats['clauses'], 'triangles': stats['triangles'],
               'cnf_sha256': hashlib.sha256(data).hexdigest(), 'cnf_bytes': len(data), 'returncode': p.returncode, 's_lines': s_lines,
               'stderr_empty': p.stderr == b'', 'solver_wall_seconds': wall, 'status': 'UNKNOWN'}
        if proof.exists():
            pb = proof.read_bytes()
            rec['proof_sha256'] = hashlib.sha256(pb).hexdigest(); rec['proof_bytes'] = len(pb)
            if p.returncode == 20 and s_lines == ['s UNSATISFIABLE']:
                try:
                    r = rup.check(data, pb)
                    rec['reviewer_rup'] = {k: r[k] for k in ('verdict', 'additions', 'deletions', 'rup_verified', 'empty_clause_verified', 'lines_after_empty')}
                    rec['status'] = 'REVIEWER_RUP_VERIFIED' if r['verdict'] == 'VERIFIED' else 'PROOF_NOT_VERIFIED'
                except rup.CheckError as e:
                    rec['reviewer_rup'] = {'verdict': 'NOT_VERIFIED', 'parse_error': str(e)}; rec['status'] = 'PROOF_NOT_VERIFIED'
            elif p.returncode == 10:
                rec['status'] = 'SOLVER_SAT_SUPPORT_RELAXATION_WOULD_NEED_INSPECTION'
        cases.append(rec)
        print(json.dumps({k: rec[k] for k in ('species', 'variables', 'clauses', 'returncode', 'status', 'solver_wall_seconds')} | ({'additions': rec['reviewer_rup']['additions']} if 'reviewer_rup' in rec and 'additions' in rec['reviewer_rup'] else {})), flush=True)
    receipt = {'kind': 'F100_REVIEW_ALTERNATIVE_ORIENTATION_REFUTATIONS', 'orientation': [R, C, S], 'solver': SOLVER, 'solver_sha256_before': solver_sha,
               'solver_sha256_after': hashlib.sha256(pathlib.Path(SOLVER).read_bytes()).hexdigest(),
               'encoder_sha256': hashlib.sha256((HERE / 'f100-review-encoder-v1.py').read_bytes()).hexdigest(),
               'checker_sha256': hashlib.sha256((HERE / 'f100-review-rup-check-v1.py').read_bytes()).hexdigest(),
               'all_reviewer_rup_verified': all(c['status'] == 'REVIEWER_RUP_VERIFIED' for c in cases),
               'total_additions': sum(c['reviewer_rup']['additions'] for c in cases if 'reviewer_rup' in c and 'additions' in c['reviewer_rup']),
               'elapsed_seconds': time.monotonic() - t0, 'cases': cases,
               'limits': 'Same-harness local computation; sound-CNF argument in review-v1.md; Hcat untouched.'}
    with out.open('x', encoding='utf-8') as h:
        json.dump(receipt, h, indent=1); h.write('\n')
    print('ALL_ALT_VERIFIED', receipt['all_reviewer_rup_verified'], 'TOTAL_ADDITIONS', receipt['total_additions'])

if __name__ == '__main__':
    main()
