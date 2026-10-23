import sys, subprocess, time, collections
sys.path.insert(0, '.')
import large_t_e0 as lte, large_t_gen as ltg, large_t_lex as v2, phase_cert as pcert, phase_check as pc
prof = lte.profiles(12)[0]
S = ltg.SmallGen(prof); S.build_gen(0, 12)
for g in v2.generators(S): v2.add_lex_leader(S, g)
blocks = []; t0 = time.time(); R = collections.Counter(); sizes = collections.Counter()
while time.time() - t0 < 90:
    p = subprocess.run(['cadical', '-q', '-t', '60'], input=v2.dimacs(S.nv, S.cl + blocks), capture_output=True, text=True)
    if p.returncode != 10: print('status', p.returncode); break
    m = {int(v) for l in p.stdout.splitlines() if l.startswith('v ') for v in l.split()[1:] if int(v) > 0}
    N = [x for x in S.points if S.var[x] in m]; blocks.append([-S.var[x] for x in N])
    okc, why = ltg.component_checks(N)
    if not okc: R['components'] += 1; continue
    mc = ltg.moduli_certificate(N)
    if mc is not None and mc['verified']: R['moduli'] += 1; continue
    c = pcert.extract_certificate(N)
    if c is not None: R['phase'] += 1; sizes[len(c)] += 1; continue
    R['OPEN'] += 1
print(len(blocks), dict(R), 'cert sizes', dict(sizes))
