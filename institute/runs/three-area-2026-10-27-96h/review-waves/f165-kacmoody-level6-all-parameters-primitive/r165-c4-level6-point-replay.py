#!/usr/bin/env python3
# r165 reviewer-authored control C4: level-6 point replays for the five canonical types (and the
# transposes of the two asymmetric ones) with the independent model r165-c2-omega-model.py.
#  - dim of the f1/f2-lowest space P mod p versus the exact character census (C1);
#  - Omega (canonical contraction, x24) preserves P mod p;
#  - det(24*Omega|P) mod p at sample parameter points (nonzero mod p => nonzero over Q);
#  - direct rank of the free D3 on P mod p at the same points (rank m => injective over Q);
#  - node-exchange consistency det_(b,a)(r,s) / det_(a,b)(s,r) constant.
# Usage: r165-c4-level6-point-replay.py a b [a b ...]
import sys
sys.dont_write_bytecode = True
import json, hashlib, importlib.util, os, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r165model', os.path.join(HERE, 'r165-c2-omega-model.py'))
K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)
CENSUS = json.load(open(os.path.join(HERE, 'r165-c1-character-census.out.json')))
MULT = {(r['a'], r['b']): r['mult'] for r in CENSUS['level6_table']}

P1 = K.primes_below(2 ** 25, 1)[0]
POINTS = [(6, 6), (6, 7), (7, 6), (8, 11), (11, 8), (6, 40), (40, 6), (123, 77),
          (5, 5), (5, 6), (6, 5), (5, 12), (12, 5), (5, 100), (100, 5)]
INFO_POINTS = [(1, 1), (1, 2), (2, 1), (2, 3), (3, 2), (4, 4), (4, 7), (7, 4), (3, 3)]

def log(msg):
    print(msg, file=sys.stderr, flush=True)

def run_type(a, b, p):
    t0 = time.time()
    B = K.build_type(6, a, b, log=log)
    m_exp = MULT[(a, b)]
    A = np.vstack([B['F1Y'], B['F2Y']])
    Kp, free, rank = K.rref_kernel_mod(A, p)
    m = Kp.shape[1]
    Z = []
    for c in range(3):
        Y = K.matmul_mod(B['R'][c], Kp, p)
        Z.append(K.lower_unit_solve_mod(B['T'], Y, p))
    Mc = [Zc[free, :] % p for Zc in Z]
    invariant = all(np.array_equal(Z[c] % p, K.matmul_mod(Kp, Mc[c], p)) for c in range(3))
    dets = {}
    for (r, s) in POINTS + INFO_POINTS:
        M = (Mc[0] + r * Mc[1] + s * Mc[2]) % p
        dets[f'{r},{s}'] = K.det_mod(M, p)
    D3K = [K.matmul_mod(B['D3'][c], Kp, p) for c in range(3)]
    ranks = {}
    for (r, s) in POINTS + INFO_POINTS:
        M = (D3K[0] + r * D3K[1] + s * D3K[2]) % p
        ranks[f'{r},{s}'] = K.rank_mod(M.T.copy(), p)
    return {'type': [a, b], 'NW': B['NW'], 'NL': B['NL'], 'NL5': B['NL5'], 'rows_f1f2': int(A.shape[0]),
            'prime': p, 'dim_P_mod_p': m, 'census_mult': m_exp, 'dim_matches': m == m_exp,
            'omega_preserves_P_mod_p': bool(invariant),
            'det24Omega_mod_p': dets,
            'det_nonzero_on_claim_points': all(dets[f'{r},{s}'] != 0 for (r, s) in POINTS),
            'D3_rank_mod_p': ranks,
            'D3_injective_on_claim_points': all(ranks[f'{r},{s}'] == m for (r, s) in POINTS),
            'seconds': round(time.time() - t0, 1)}

if __name__ == '__main__':
    start = K.clock()
    args = list(map(int, sys.argv[1:]))
    types = [(args[i], args[i + 1]) for i in range(0, len(args), 2)]
    res = {'start_clock': start,
           'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
           'model_sha256': hashlib.sha256(open(os.path.join(HERE, 'r165-c2-omega-model.py'), 'rb').read()).hexdigest(),
           'census_out_sha256': hashlib.sha256(open(os.path.join(HERE, 'r165-c1-character-census.out.json'), 'rb').read()).hexdigest(),
           'claim_points': POINTS, 'informative_points': INFO_POINTS, 'results': []}
    for (a, b) in types:
        log(f'type {(a, b)} start {K.clock()}')
        res['results'].append(run_type(a, b, P1))
        log(f'type {(a, b)} done {K.clock()}')
    # node-exchange consistency for available transposed pairs
    byt = {tuple(r['type']): r for r in res['results']}
    nx = []
    for (a, b) in list(byt):
        if a > b and (b, a) in byt:
            d1, d2 = byt[(a, b)]['det24Omega_mod_p'], byt[(b, a)]['det24Omega_mod_p']
            ratios = set()
            for key in d1:
                r, s = map(int, key.split(','))
                v1, v2 = d1[key], d2.get(f'{s},{r}')
                if v2 is None or v1 == 0 or v2 == 0:
                    continue
                ratios.add(v2 * pow(v1, P1 - 2, P1) % P1)
            nx.append({'pair': [[a, b], [b, a]], 'distinct_ratios': sorted(ratios), 'constant': len(ratios) == 1})
    res['node_exchange'] = nx
    res['end_clock'] = K.clock()
    print(json.dumps(res, indent=1))
