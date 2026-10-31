#!/usr/bin/env python3
"""
reviewer-controls-addendum-v4.py -- review wave f133, exhaustiveness diagnostic for addendum v3.

Re-runs the constrained MOLS-pair search of addendum v3 (same WLOG normal form: L has 0 on the diagonal and 1 at
(r, pi(r)); R carries symbols 0..k-1 on the long cycle's 0-cells, in order, and reuses them on its 1-cells) with a
large node budget and reports whether the search EXHAUSTED the space (proof of non-existence of a classical mate
for every C_2k-mixed Q of this normal form) or merely hit the budget.

WLOG justification (reviewer): any Latin square of order 8 whose {0,1} cells contain a row/column cycle of length
2k has, after a row permutation and a column permutation, its 0-cells on the diagonal and its 1-cells at a
permutation pi' of cycle type (k, 8-k); a simultaneous row/column conjugation (which fixes the diagonal) maps pi'
to the fixed pi.  Relabeling R's symbols is a unitary on R.  Both operations preserve every orthogonality relation.
"""
import sys, os, json, hashlib, datetime, time, random, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('a3', os.path.join(HERE, 'reviewer-controls-addendum-v3.py'))
a3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a3)

def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

n = 8
RES = []

def run(k, pi, max_nodes, seed=0):
    Lfixed = {}
    for r in range(n):
        Lfixed[(r, r)] = 0
        Lfixed[(r, pi[r])] = 1
    Rfixed = {(r, r): r for r in range(k)}
    Rdomain = {(r, pi[r]): list(range(k)) for r in range(k)}
    t0 = time.time()
    L, R, nodes = a3.mols_pair_search(Lfixed, Rfixed, Rdomain, random.Random(seed), max_nodes)
    dt = time.time() - t0
    status = 'FOUND' if L is not None else ('EXHAUSTED' if nodes <= max_nodes else 'BUDGET_HIT')
    print('k=%d seed %d: status %s, nodes %d (budget %d), %.1fs' % (k, seed, status, nodes, max_nodes, dt))
    RES.append({'k': k, 'seed': seed, 'status': status, 'nodes': nodes, 'budget': max_nodes, 'seconds': round(dt, 1)})
    return status

def main():
    start = utc()
    print('reviewer-controls-addendum-v4.py start (UTC):', start)
    with open(os.path.abspath(__file__), 'rb') as f:
        print('script sha256:', hashlib.sha256(f.read()).hexdigest())
    pi6 = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 0, 6: 7, 7: 6}
    s6 = run(6, pi6, max_nodes=50_000_000, seed=0)
    s6b = run(6, pi6, max_nodes=50_000_000, seed=1)
    pi5 = {0: 1, 1: 2, 2: 3, 3: 4, 4: 0, 5: 6, 6: 7, 7: 5}
    s5 = run(5, pi5, max_nodes=int(sys.argv[1]) if len(sys.argv) > 1 else 6_000_000, seed=0)
    end = utc()
    print('SUMMARY: k=6 -> %s / %s ; k=5 -> %s ; start %s end %s' % (s6, s6b, s5, start, end))
    outpath = os.path.join(HERE, 'reviewer-controls-addendum-result-v4.json')
    if os.path.exists(outpath):
        print('refusing to overwrite', outpath)
        sys.exit(2)
    with open(outpath, 'w') as f:
        json.dump({'start_utc': start, 'end_utc': end, 'runs': RES}, f, indent=1)
    print('wrote', outpath)

if __name__ == '__main__':
    main()
