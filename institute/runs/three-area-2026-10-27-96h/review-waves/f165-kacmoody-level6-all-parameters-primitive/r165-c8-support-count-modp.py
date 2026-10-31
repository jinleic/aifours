#!/usr/bin/env python3
# r165 reviewer-authored control C8: coefficient SUPPORT of f(x,y)=det(24*Omega(6+x,6+y)|P_(a,b)) modulo
# two independent primes (same interpolation as C5, no CRT).  A coefficient nonzero mod p is nonzero over Z,
# so the union count is a RIGOROUS LOWER BOUND on the number of nonzero integer coefficients; equality of the
# two per-prime supports is (probabilistic) evidence that the bound is attained.  Signs are NOT available mod p.
# Usage: r165-c8-support-count-modp.py a b [a b ...]
import sys
sys.dont_write_bytecode = True
import json, hashlib, importlib.util, os, time

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('r165model', os.path.join(HERE, 'r165-c2-omega-model.py'))
K = importlib.util.module_from_spec(spec); spec.loader.exec_module(K)
spec5 = importlib.util.spec_from_file_location('r165c5', os.path.join(HERE, 'r165-c5-full-polynomial.py'))
C5 = importlib.util.module_from_spec(spec5); spec5.loader.exec_module(C5)
CENSUS = json.load(open(os.path.join(HERE, 'r165-c1-character-census.out.json')))
MULT = {(r['a'], r['b']): r['mult'] for r in CENSUS['level6_table']}

def log(msg):
    print(msg, file=sys.stderr, flush=True)

if __name__ == '__main__':
    args = list(map(int, sys.argv[1:]))
    types = [(args[i], args[i + 1]) for i in range(0, len(args), 2)]
    primes = K.primes_below(2 ** 25, 60)[-2:]      # disjoint from the first primes used by C5
    res = {'start_clock': K.clock(), 'primes': primes,
           'script_sha256': hashlib.sha256(open(__file__, 'rb').read()).hexdigest(),
           'model_sha256': hashlib.sha256(open(os.path.join(HERE, 'r165-c2-omega-model.py'), 'rb').read()).hexdigest(),
           'c5_sha256': hashlib.sha256(open(os.path.join(HERE, 'r165-c5-full-polynomial.py'), 'rb').read()).hexdigest(),
           'types': []}
    for (a, b) in types:
        t0 = time.time()
        m = MULT[(a, b)]
        B = K.build_type(6, a, b, want_d3=False, log=log)
        supports = []
        for p in primes:
            mp, Mc = C5.restricted_pencil(B, p)
            assert mp == m, (mp, m)
            C = C5.poly_mod_p(Mc[0], Mc[1], Mc[2], m, p)
            supp = {(i, j) for i in range(m + 1) for j in range(m + 1 - i) if int(C[i, j]) != 0}
            supports.append(supp)
            log(f'type {(a, b)} prime {p}: support {len(supp)} at {K.clock()}')
        union = supports[0] | supports[1]
        res['types'].append({'type': [a, b], 'm': m, 'monomials': (m + 1) * (m + 2) // 2,
                             'support_per_prime': [len(s) for s in supports],
                             'supports_equal': supports[0] == supports[1],
                             'rigorous_lower_bound_nonzero': len(union),
                             'constant_term_nonzero': (0, 0) in union,
                             'seconds': round(time.time() - t0, 1)})
    res['end_clock'] = K.clock()
    print(json.dumps(res, indent=1))
