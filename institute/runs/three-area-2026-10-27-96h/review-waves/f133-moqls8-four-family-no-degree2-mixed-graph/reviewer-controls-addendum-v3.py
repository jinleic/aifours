#!/usr/bin/env python3
"""
reviewer-controls-addendum-v3.py -- review wave f133, reviewer-written adversarial addendum, third attempt.

Addenda v1/v2 produced only vacuous C10/C12 tests (no classical mates at all).  Here a constrained MOLS-pair
backtracking search (MRV cell choice, random restarts) builds a Latin square L of order 8 whose {0,1} cells contain a
row/column cycle of length 2k (k=5: cycle type (5,3); k=6: cycle type (6,2)) TOGETHER WITH an orthogonal mate R
satisfying the cycle condition (R-symbols on the cycle's 0-cells = R-symbols on its 1-cells; after relabeling R these
are the symbols 0..k-1).  Hence the C_2k-mixed Q obtained by rotating the cycle has at least one classical mate.
Then ALL classical mates of Q are enumerated (transversal decompositions of L with the cycle condition) and
orthogonal pairs / triples are counted.

Candidate 3 predicts for n=8:
  k=5: t <= min(4,3) = 3  -> no mutually orthogonal TRIPLE of classical mates  (row bound alone would allow 4 mates)
  k=6: t <= min(5,2) = 2  -> no orthogonal PAIR of classical mates             (row bound alone would allow 5 mates)
A triple (k=5) or a pair (k=6) would refute candidate 3's complement pigeonhole.
"""
import sys, os, json, hashlib, itertools, datetime, time, random, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('rc', os.path.join(HERE, 'reviewer-controls-v1.py'))
rc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rc)

RESULTS = []
def record(name, expected, observed):
    ok = (expected == observed)
    RESULTS.append({'check': name, 'expected': repr(expected), 'observed': repr(observed), 'ok': ok})
    print(('PASS ' if ok else 'FAIL ') + name + ' | expected ' + repr(expected) + ' | observed ' + repr(observed))
    return ok

def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

n = 8
sys.setrecursionlimit(10000)

def mate_from(T, cv):
    R = {}
    for sym, ti in enumerate(cv):
        for x in T[ti]:
            R[x] = rc.unit(n, sym)
    return R

def mols_pair_search(Lfixed, Rfixed, Rdomain, rng, max_nodes):
    L, R = {}, {}
    rowL = [set() for _ in range(n)]; colL = [set() for _ in range(n)]
    rowR = [set() for _ in range(n)]; colR = [set() for _ in range(n)]
    pairs = set()
    cells_all = [(r, c) for r in range(n) for c in range(n)]
    nodes = [0]
    def options(cell):
        r, c = cell
        As = [Lfixed[cell]] if cell in Lfixed else [a for a in range(n) if a not in rowL[r] and a not in colL[c]]
        As = [a for a in As if a not in rowL[r] and a not in colL[c]]
        Bs = [Rfixed[cell]] if cell in Rfixed else list(Rdomain.get(cell, range(n)))
        Bs = [b for b in Bs if b not in rowR[r] and b not in colR[c]]
        return [(a, b) for a in As for b in Bs if (a, b) not in pairs]
    def rec():
        nodes[0] += 1
        if nodes[0] > max_nodes:
            return False
        best, bestopts = None, None
        for cell in cells_all:
            if cell in L:
                continue
            opts = options(cell)
            if not opts:
                return False
            if best is None or len(opts) < len(bestopts):
                best, bestopts = cell, opts
        if best is None:
            return True
        rng.shuffle(bestopts)
        r, c = best
        for a, b in bestopts:
            L[best] = a; R[best] = b
            rowL[r].add(a); colL[c].add(a); rowR[r].add(b); colR[c].add(b); pairs.add((a, b))
            if rec():
                return True
            del L[best]; del R[best]
            rowL[r].discard(a); colL[c].discard(a); rowR[r].discard(b); colR[c].discard(b); pairs.discard((a, b))
        return False
    ok = rec()
    return (L, R, nodes[0]) if ok else (None, None, nodes[0])

def classical_adversary(L, good_filter):
    T = rc.transversals(L, n)
    masks = [sum(1 << (r*n + c) for r, c in t) for t in T]
    good = [i for i, t in enumerate(T) if good_filter(t)]
    covers = rc.exact_covers(masks, n, allowed=good)
    index = {cv: i for i, cv in enumerate(covers)}
    def meets_once(i, cv):
        return all(bin(masks[i] & masks[j]).count('1') == 1 for j in cv)
    pairs, triples, first_pair = 0, 0, None
    for i, cv1 in enumerate(covers):
        cand = [t for t in good if meets_once(t, cv1)]
        for cv2 in rc.exact_covers(masks, n, allowed=cand):
            j = index[cv2]
            if j <= i:
                continue
            pairs += 1
            if first_pair is None:
                first_pair = (cv1, cv2)
            cand2 = [t for t in cand if meets_once(t, cv2)]
            for cv3 in rc.exact_covers(masks, n, allowed=cand2):
                if index[cv3] > j:
                    triples += 1
    return dict(T=T, masks=masks, good=good, covers=covers, pairs=pairs, triples=triples, first_pair=first_pair)

def run_k(k, pi, seeds, max_nodes, want_instances):
    print('\n=== C_%d-mixed Q (k=%d) in n=8 via constrained MOLS-pair search; candidate 3 bound t <= %d ===' % (2*k, k, min(k-1, n-k)))
    cyc_rows = list(range(k))                   # pi's long cycle is on rows 0..k-1
    Lfixed = {}
    for r in range(n):
        Lfixed[(r, r)] = 0
        Lfixed[(r, pi[r])] = 1
    Rfixed = {(r, r): r for r in cyc_rows}      # WLOG relabeling of R: cycle 0-cells carry symbols 0..k-1
    Rdomain = {(r, pi[r]): list(range(k)) for r in cyc_rows}   # cycle 1-cells must reuse those symbols
    found = 0
    tot_mates = tot_pairs = tot_triples = 0
    with_pairs = 0
    structure_done = False
    t0 = time.time()
    squares_seen = set()
    for seed in range(seeds):
        rng = random.Random(seed)
        L, R, nodes = mols_pair_search(Lfixed, Rfixed, Rdomain, rng, max_nodes)
        if L is None:
            continue
        key = tuple(L[(r, c)] for r in range(n) for c in range(n))
        if key in squares_seen:
            continue
        squares_seen.add(key)
        assert rc.is_latin(L, n) and rc.is_latin(R, n)
        comps = rc.two_symbol_components(L, n, 0, 1)
        cyc = next(c for c in comps if len(c) == 2*k)
        found += 1
        Q = rc.rotate(L, n, set(cyc), 0, 1)
        r0 = next(r for r in range(n) if r not in {x[0] for x in cyc})
        A = rc.mixed_analysis(Q, n, r0)
        assert rc.qls_violation(Q, n) is None
        assert len(A['comps']) == 1 and rc.is_single_cycle(A['comps'][0], k)
        Rq = rc.classical(R, n)
        assert rc.pair_violation(Q, Rq, n) is None, 'search output must be a mate of Q'
        c0 = {x for x in cyc if L[x] == 0}
        c1 = {x for x in cyc if L[x] == 1}
        flt = lambda t: (bool(set(t) & c0) == bool(set(t) & c1))
        res = classical_adversary(L, flt)
        assert len(res['covers']) >= 1
        tot_mates += len(res['covers']); tot_pairs += res['pairs']; tot_triples += res['triples']
        if res['pairs']:
            with_pairs += 1
        print('   k=%d seed %d: search nodes %d, transversals %d, cycle-condition %d, classical mates %d, orthogonal pairs %d, triples %d'
              % (k, seed, nodes, len(res['T']), len(res['good']), len(res['covers']), res['pairs'], res['triples']))
        if not structure_done and (res['pairs'] or k == 6):
            T = res['T']
            ok = sum(1 for cv in res['covers'] if rc.pair_violation(Q, mate_from(T, cv), n) is None)
            record('k=%d seed %d: ALL %d cycle-condition decompositions are classical mates of Q' % (k, seed, len(res['covers'])), len(res['covers']), ok)
            X = A['mixed']
            a, b = A['comps'][0]['supports'][0]
            if res['pairs']:
                cv1, cv2 = res['first_pair']
                R1, S1 = mate_from(T, cv1), mate_from(T, cv2)
                record('k=%d: R (x) S ONB' % k, None, rc.pair_violation(R1, S1, n))
                FR = rc.forced_structure(Q, R1, n, r0, X, a, b, 'k=%d/R(a,b)' % k)
                FS = rc.forced_structure(Q, S1, n, r0, X, a, b, 'k=%d/S(a,b)' % k)
                rc.cross_mate_checks(FR, FS, 'k=%d/R,S(a,b)' % k)
                FRb = rc.forced_structure(Q, R1, n, r0, X, b, a, 'k=%d/R(b,a)' % k)
                FSb = rc.forced_structure(Q, S1, n, r0, X, b, a, 'k=%d/S(b,a)' % k)
                rc.cross_mate_checks(FRb, FSb, 'k=%d/R,S(b,a)' % k)
                print('   k=%d: U^R = %s' % (k, FR['U']))
                print('   k=%d: U^S = %s' % (k, FS['U']))
                off = [y for y in FR['Ea'] if y != (r0, a)]
                print('   k=%d: e_b-overlap cells R %s S %s among off-first-row light e_a cells %s' % (k, sorted(FR['B']), sorted(FS['B']), off))
                record('k=%d: n-k-1 == %d off-first-row light e_a cells' % (k, n-k-1), n-k-1, len(off))
            else:
                FR = rc.forced_structure(Q, Rq, n, r0, X, a, b, 'k=%d/R(a,b)' % k)
                print('   k=%d: U^R = %s' % (k, FR['U']))
                off = [y for y in FR['Ea'] if y != (r0, a)]
                record('k=%d: n-k-1 == %d off-first-row light e_a cells' % (k, n-k-1), n-k-1, len(off))
            structure_done = True
        if found >= want_instances:
            break
    print('   k=%d: distinct squares with >=1 classical mate found %d (of %d seeds), with orthogonal mate pairs %d; total mates %d, pairs %d, triples %d (%.1fs)'
          % (k, found, seeds, with_pairs, tot_mates, tot_pairs, tot_triples, time.time()-t0))
    return dict(found=found, with_pairs=with_pairs, mates=tot_mates, pairs=tot_pairs, triples=tot_triples)

def main():
    start = utc()
    print('reviewer-controls-addendum-v3.py start (UTC):', start)
    src = os.path.abspath(__file__)
    with open(src, 'rb') as f:
        print('script sha256:', hashlib.sha256(f.read()).hexdigest())
    with open(os.path.join(HERE, 'reviewer-controls-v1.py'), 'rb') as f:
        print('helper (reviewer-controls-v1.py) sha256:', hashlib.sha256(f.read()).hexdigest())
    pi5 = {0: 1, 1: 2, 2: 3, 3: 4, 4: 0, 5: 6, 6: 7, 7: 5}          # cycle type (5,3): 10-cycle + 6-cycle
    r5 = run_k(5, pi5, seeds=40, max_nodes=200000, want_instances=12)
    record('k=5 (C10): squares with >=1 classical mate were found (non-vacuous)', True, r5['found'] >= 1)
    record('k=5 (C10)-adversarial: mutually orthogonal classical mate TRIPLES over all found squares (candidate 3 predicts 0)', 0, r5['triples'])
    pi6 = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 0, 6: 7, 7: 6}          # cycle type (6,2): 12-cycle + 4-cycle
    r6 = run_k(6, pi6, seeds=40, max_nodes=200000, want_instances=12)
    record('k=6 (C12): squares with >=1 classical mate were found (non-vacuous)', True, r6['found'] >= 1)
    record('k=6 (C12)-adversarial: orthogonal classical mate PAIRS over all found squares (candidate 3 predicts 0)', 0, r6['pairs'])
    end = utc()
    allres = RESULTS + [r for r in rc.RESULTS if 'check' in r]
    npass = sum(1 for r in allres if r['ok'])
    nfail = len(allres) - npass
    print('\nSUMMARY: %d checks, %d PASS, %d FAIL; start %s end %s' % (len(allres), npass, nfail, start, end))
    outpath = os.path.join(HERE, 'reviewer-controls-addendum-result-v3.json')
    if os.path.exists(outpath):
        print('refusing to overwrite', outpath)
        sys.exit(2)
    with open(outpath, 'w') as f:
        json.dump({'start_utc': start, 'end_utc': end, 'checks': len(allres), 'pass': npass, 'fail': nfail,
                   'k5': r5, 'k6': r6, 'results': allres}, f, indent=1)
    print('wrote', outpath)
    sys.exit(0 if nfail == 0 else 1)

if __name__ == '__main__':
    main()
