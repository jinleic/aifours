#!/usr/bin/env python3
"""INV aid (repr-INV.md A1/A2): single-bracket windows at length N = 4p-2.

For every RGR run datum (k <= KMAX runs, all splits) at N = 4p-2 with at least one
INV violation (an even run, or k > p), classify how Phi <= 2 patterns certify
solvability:
  zero  : 0 in W(empty)                       (pairs)
  full  : some single cyclic interval P has |Ach(P)| >= p   (Cor. GR-W)
  joint : neither, but the pairwise-difference system
          y_a - y_b notin W_ab for all reflection-run pairs is infeasible
  none  : Phi <= 2 patterns do not certify (some theta survives them)
Usage: inv_brackets.py p KMAX
"""
import itertools, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gr_window import ach

def windows(a, b, l, p):
    k = len(a)
    res = {}
    for P in range(1 << k):
        z = [1 if (P >> i) & 1 else -1 for i in range(k)]
        f = [int(z[i] != z[(i + 1) % k]) for i in range(k)]
        if sum(f) > 2:
            continue
        lo, hi = ach(z, a, b, l, p)
        res[P] = (lo, hi)
    return res

def wset(lo, hi, p):
    return set() if lo > hi else {t % p for t in range(lo, hi + 1, 2)}

def classify(a, b, l, p):
    k = len(a)
    W = windows(a, b, l, p)
    lo, hi = W[0]
    if 0 in wset(lo, hi, p):
        return 'zero'
    for P, (lo, hi) in W.items():
        if lo <= hi and (hi - lo) // 2 + 1 >= p:
            return 'full'
    # joint: search theta (sum 0) avoiding all Phi<=2 windows
    sets = {P: wset(lo, hi, p) for P, (lo, hi) in W.items()}
    for th in itertools.product(range(p), repeat=k - 1):
        theta = list(th) + [(-sum(th)) % p]
        ok = True
        for P, S in sets.items():
            s = sum(theta[i] for i in range(k) if (P >> i) & 1) % p
            if s in S:
                ok = False
                break
        if ok:
            return 'none'
    return 'joint'

def main():
    p = int(sys.argv[1]); KMAX = int(sys.argv[2])
    N = 4 * p - 2
    out = {}
    for k in range(1, KMAX + 1):
        st = {}
        for cuts in itertools.combinations(range(1, N), 2 * k - 1):
            bnd = (0,) + cuts + (N,)
            parts = [bnd[i + 1] - bnd[i] for i in range(2 * k)]
            r = parts[0::2]; l = parts[1::2]
            # rotation-canonical: skip if some rotation of (r,l) is lexicographically smaller
            pairs = list(zip(r, l))
            if any(pairs[s:] + pairs[:s] < pairs for s in range(1, k)):
                continue
            evenR = any(x % 2 == 0 for x in r); evenF = any(x % 2 == 0 for x in l)
            if not (evenR or evenF or k > p):
                continue
            for a in itertools.product(*[range(x + 1) for x in r]):
                b = [x - y for x, y in zip(r, a)]
                c = classify(list(a), b, l, p)
                key = ('evenF' if evenF else '') + ('evenR' if evenR else '') + ('k>p' if k > p else '') + ':' + c
                st[key] = st.get(key, 0) + 1
        out[k] = st
        print(k, json.dumps(st), flush=True)
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'evidence', 'inv', f'brackets_p{p}_k{KMAX}.json')
    json.dump(out, open(path, 'w'), indent=1)

if __name__ == '__main__':
    main()
