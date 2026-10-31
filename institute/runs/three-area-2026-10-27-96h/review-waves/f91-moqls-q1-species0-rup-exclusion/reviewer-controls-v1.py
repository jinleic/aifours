#!/usr/bin/env python3
"""Reviewer (f91) tamper controls for reviewer-rup-check-v1.py and diagnostics."""
import hashlib, importlib.util, json, pathlib, subprocess, sys
H = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location('rc', H / 'reviewer-rup-check-v1.py'); rc = importlib.util.module_from_spec(spec); spec.loader.exec_module(rc)
ROOT = pathlib.Path('/Users/jinleic/repos/aifours/physics/evidence/three-area-20261027-96h/parallel-18/moqls8')
C = (ROOT / 'frontier-20261028-q1-support-species0-v1.cnf').read_bytes()
P = (ROOT / 'frontier-20261028-q1-support-species0-proof-v1.drup').read_bytes()
assert hashlib.sha256(C).hexdigest() == '0ddbe3818bba22fb3e040d669f0b81dcfe8f39f3b005db842a6c969db8f00f63'
assert hashlib.sha256(P).hexdigest() == '2d405f676add4fe7967e98722834c536d9545ed1a0038f4546b1721e55b33599'
def run(c, p):
    try: return 'PASS', rc.verify(c, p)
    except (ValueError, UnicodeError) as e: return 'REJECT', str(e)
out = {}
# T1 truncated proof (final empty clause removed)
out['T1_truncated_proof'] = run(C, P.rsplit(b'\n', 2)[0] + b'\n')
# T2 bogus unit lemma prepended
out['T2_bogus_unit_prepended'] = run(C, b'1 0\n' + P)
# T3 satisfiable formula with bogus empty proof
out['T3_sat_formula_empty_proof'] = run(b'p cnf 2 1\n1 2 0\n', b'0\n')
# T4 wrong formula: first 3000 clauses only
lines = C.decode('ascii').splitlines(); hdr = lines[0].split(); body = lines[1:]
wrong = ('p cnf %s 3000\n' % hdr[2] + '\n'.join(body[:3000]) + '\n').encode('ascii')
out['T4_wrong_formula_first_3000_clauses'] = run(wrong, P)
# T5 a middle lemma literal flipped (line 16, the long lemma) -- report whatever happens
pl = P.decode('ascii').splitlines(); l16 = pl[15].split(); l16[0] = str(-int(l16[0])); pl2 = pl[:]; pl2[15] = ' '.join(l16)
out['T5_lemma16_first_literal_flipped'] = run(C, ('\n'.join(pl2) + '\n').encode('ascii'))
# D1 diagnostic: remove the 336-literal nonclassicality clause; does the pinned proof still check?
idx = [i for i, s in enumerate(body) if len(s.split()) == 337]; assert len(idx) == 1
body2 = body[:idx[0]] + body[idx[0] + 1:]
noN = ('p cnf %s %d\n' % (hdr[2], len(body2)) + '\n'.join(body2) + '\n').encode('ascii')
(H / 'controls' / 'species0-without-nonclassical-clause.cnf').open('xb').write(noN)
out['D1_pinned_proof_vs_cnf_without_nonclassical_clause'] = run(noN, P)
out['D1_cnf_without_nonclassical_sha256'] = hashlib.sha256(noN).hexdigest()
# D2 diagnostic: fresh kissat on the CNF without the nonclassicality clause
r = subprocess.run(['kissat', '-q', str(H / 'controls' / 'species0-without-nonclassical-clause.cnf'), str(H / 'controls' / 'species0-without-nonclassical-clause.drup')], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=600)
out['D2_kissat_without_nonclassical'] = {'exit': r.returncode, 'stdout': r.stdout.strip().splitlines()[-1:] , 'stderr': r.stderr.strip()[-200:]}
if r.returncode == 20:
    out['D2_reviewer_rup_check_of_fresh_proof'] = run(noN, (H / 'controls' / 'species0-without-nonclassical-clause.drup').read_bytes())
# R1 fresh kissat replay of the pinned CNF, reviewer-checked
r = subprocess.run(['kissat', '-q', str(ROOT / 'frontier-20261028-q1-support-species0-v1.cnf'), str(H / 'controls' / 'species0-fresh-kissat.drup')], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=600)
out['R1_kissat_fresh_pinned_cnf'] = {'exit': r.returncode, 'stdout': r.stdout.strip().splitlines()[-1:], 'stderr': r.stderr.strip()[-200:],
    'kissat_sha256': hashlib.sha256(pathlib.Path('/opt/homebrew/Cellar/kissat/4.0.4/bin/kissat').read_bytes()).hexdigest()}
fp = (H / 'controls' / 'species0-fresh-kissat.drup').read_bytes()
out['R1_fresh_proof_sha256'] = hashlib.sha256(fp).hexdigest(); out['R1_fresh_proof_bytes'] = len(fp)
out['R1_reviewer_rup_check_of_fresh_proof'] = run(C, fp)
print(json.dumps(out, indent=1, default=str))
