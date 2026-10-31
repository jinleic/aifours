#!/usr/bin/env python3
# r165 reviewer-authored control C7: SAMPLED direct test of the level-6 primitive claim on ALL 24
# oriented lowest types at parameter points with min(r,s) >= 5, using the independent model.
# Reasoning used (reviewer's own, written in review-v1.md): for min(r,s) >= 5 no node-3 seed lies at
# level <= 5, so S_5 = L_5; at level 6 the only possible seed modules are the irreducible l-modules of
# the seeds (ad v)^5 u1 (type (1,0), when r=5) and (ad v)^5 u2 (type (0,1), when s=5), so for every other
# type the actual source is the free P.  Hence: actual D3 injective <=> rank(D3|P) = m (free), except
# for the seed type at r=5 / s=5 where P = span(seed) and the actual source is 0.
# rank mod p = m  =>  rank over Q = m.  This is a SAMPLE of parameter points, not a proof for all r,s.
import sys
sys.dont_write_bytecode = True
import json, hashlib, importlib.util, os, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r165model', os.path.join(HERE, 'r165-c2-omega-model.py'))
K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)
CENSUS = json.load(open(os.path.join(HERE, 'r165-c1-character-census.out.json')))
MULT = {(r['a'], r['b']): r['mult'] for r in CENSUS['level6_table']}
p = K.primes_below(2 ** 25, 3)[2]
POINTS = [(6, 6), (6, 9), (9, 6), (7, 13), (13, 7), (31, 6), (6, 31), (5, 5), (5, 7), (7, 5), (5, 50), (50, 5)]

def log(msg):
    print(msg, file=sys.stderr, flush=True)

res = {'start_clock': K.clock(), 'prime': p, 'points': POINTS,
       'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
       'model_sha256': hashlib.sha256(open(os.path.join(HERE, 'r165-c2-omega-model.py'), 'rb').read()).hexdigest(),
       'types': []}
allok = True
for (a, b), m in sorted(MULT.items()):
    t0 = time.time()
    B = K.build_type(6, a, b, want_omega=False, want_d3=True, log=log)
    A = np.vstack([B['F1Y'], B['F2Y']])
    Kp, free, rank = K.rref_kernel_mod(A, p)
    D3K = [K.matmul_mod(B['D3'][c], Kp, p) for c in range(3)]
    ranks, verdict = {}, {}
    for (r, s) in POINTS:
        M = (D3K[0] + r * D3K[1] + s * D3K[2]) % p
        rk = K.rank_mod(M.T.copy(), p)
        ranks[f'{r},{s}'] = rk
        seed_type = ((a, b) == (1, 0) and r == 5) or ((a, b) == (0, 1) and s == 5)
        if seed_type:
            ok = (m == 1 and rk == 0)      # P = span(seed): free D3 kills it; actual source is 0
        else:
            ok = (rk == m)
        verdict[f'{r},{s}'] = 'seed-type actual source 0' if seed_type and ok else ('injective' if ok else 'NOT CERTIFIED')
        allok &= ok
    res['types'].append({'type': [a, b], 'm': m, 'dimP_mod_p': Kp.shape[1], 'NL': B['NL'], 'NL5': B['NL5'],
                         'ranks': ranks, 'verdicts': verdict, 'seconds': round(time.time() - t0, 1)})
    allok &= Kp.shape[1] == m
    log(f'type {(a, b)} m={m} done {K.clock()}')
res['all_sampled_points_certified'] = bool(allok)
res['end_clock'] = K.clock()
print(json.dumps(res, indent=1))
