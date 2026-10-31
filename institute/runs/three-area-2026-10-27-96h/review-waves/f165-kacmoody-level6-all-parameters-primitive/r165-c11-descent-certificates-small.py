#!/usr/bin/env python3
# r165 reviewer-authored control C11: where can the (reviewed) descent lemma INDEPENDENTLY certify the
# ACTUAL level-6 map in the small-parameter branches (min(r,s) <= 4), using only FREE data?
# For every one of the 24 oriented level-6 types and sampled (r,s) with min(r,s) <= 4:
#   det(24*Omega|P) mod p != 0  ==>  det != 0 over Q  ==>  (descent lemma) actual D3 injective on Pbar.
# det == 0 mod p gives NO conclusion (the lemma has no converse; the candidate's literal quotient
# certificates, not replayed here, would be needed).  This is a SAMPLE of parameter points.
import sys
sys.dont_write_bytecode = True
import json, hashlib, importlib.util, os, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r165model', os.path.join(HERE, 'r165-c2-omega-model.py'))
K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)
CENSUS = json.load(open(os.path.join(HERE, 'r165-c1-character-census.out.json')))
MULT = {(r['a'], r['b']): r['mult'] for r in CENSUS['level6_table']}
p = K.primes_below(2 ** 25, 5)[4]
POINTS = [(r, s) for r in range(1, 5) for s in range(1, 5)] + \
         [(4, 9), (9, 4), (4, 23), (23, 4), (3, 8), (8, 3), (3, 31), (31, 3), (2, 7), (7, 2), (2, 40), (40, 2), (1, 6), (6, 1), (1, 50), (50, 1)]

def log(msg):
    print(msg, file=sys.stderr, flush=True)

res = {'start_clock': K.clock(), 'prime': p, 'points': POINTS,
       'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
       'model_sha256': hashlib.sha256(open(os.path.join(HERE, 'r165-c2-omega-model.py'), 'rb').read()).hexdigest(),
       'types': []}
tot_cert, tot = 0, 0
per_point = {f'{r},{s}': 0 for (r, s) in POINTS}
for (a, b), m in sorted(MULT.items()):
    B = K.build_type(6, a, b, want_d3=False, log=log)
    A = np.vstack([B['F1Y'], B['F2Y']])
    Kp, free, rank = K.rref_kernel_mod(A, p)
    assert Kp.shape[1] == m
    Mc = []
    for c in range(3):
        Y = K.matmul_mod(B['R'][c], Kp, p)
        Z = K.lower_unit_solve_mod(B['T'], Y, p)
        assert np.array_equal(Z % p, K.matmul_mod(Kp, Z[free, :] % p, p))
        Mc.append(Z[free, :] % p)
    cert = {}
    for (r, s) in POINTS:
        d = K.det_mod((Mc[0] + r * Mc[1] + s * Mc[2]) % p, p)
        cert[f'{r},{s}'] = d != 0
        tot += 1
        if d:
            tot_cert += 1
            per_point[f'{r},{s}'] += 1
    res['types'].append({'type': [a, b], 'm': m, 'certified_points': [k for k, v in cert.items() if v],
                         'no_conclusion_points': [k for k, v in cert.items() if not v]})
    log(f'type {(a, b)} done {K.clock()}')
res['pairs_total'] = tot
res['pairs_certified_by_descent_lemma'] = tot_cert
res['types_certified_per_point_out_of_24'] = per_point
res['end_clock'] = K.clock()
print(json.dumps(res, indent=1))
