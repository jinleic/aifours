#!/usr/bin/env python3
"""
reviewer-controls-addendum-v5.py -- review wave f133, non-vacuous C10 (k=5) attempt via random MOLS pairs.

Generates random orthogonal pairs (L, R) of Latin squares of order 8 with the unconstrained MRV backtracking search
of addendum v3 (random restarts), then for every symbol pair {s0,s1} of L whose row/column cycles have type (10,6)
builds the C10-mixed Q (rotate the 10-cycle) and enumerates ALL classical mates of Q (transversal decompositions of
L with the cycle condition).  Counts orthogonal pairs / triples of such mates.  Candidate 3 predicts no triple
(t <= min(4,3) = 3); the row bound alone would allow a triple.
"""
import sys, os, json, hashlib, itertools, datetime, time, random, importlib.util

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('a3', os.path.join(HERE, 'reviewer-controls-addendum-v3.py'))
a3 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(a3)
rc = a3.rc

RESULTS = []
def record(name, expected, observed):
    ok = (expected == observed)
    RESULTS.append({'check': name, 'expected': repr(expected), 'observed': repr(observed), 'ok': ok})
    print(('PASS ' if ok else 'FAIL ') + name + ' | expected ' + repr(expected) + ' | observed ' + repr(observed))
    return ok

def utc():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

n = 8

def main():
    start = utc()
    print('reviewer-controls-addendum-v5.py start (UTC):', start)
    with open(os.path.abspath(__file__), 'rb') as f:
        print('script sha256:', hashlib.sha256(f.read()).hexdigest())
    npairs = int(sys.argv[1]) if len(sys.argv) > 1 else 150
    budget = int(sys.argv[2]) if len(sys.argv) > 2 else 300000
    t0 = time.time()
    squares = []
    tried = 0
    for seed in range(npairs):
        tried += 1
        L, R, nodes = a3.mols_pair_search({}, {}, {}, random.Random(1000 + seed), budget)
        if L is None:
            continue
        assert rc.is_latin(L, n) and rc.is_latin(R, n)
        assert rc.pair_violation(rc.classical(L, n), rc.classical(R, n), n) is None
        squares.append(L)
    print('   random MOLS pairs found: %d of %d attempts (%.1fs)' % (len(squares), tried, time.time()-t0))
    record('v5: at least one random MOLS(8) pair was generated', True, len(squares) >= 1)
    inst = with_mates = with_pairs = 0
    tot_mates = tot_pairs = tot_triples = 0
    cycle_type_hist = {}
    structure_done = False
    for L in squares:
        for s0, s1 in itertools.combinations(range(n), 2):
            comps = rc.two_symbol_components(L, n, s0, s1)
            ct = tuple(sorted(len(c) for c in comps))
            cycle_type_hist[ct] = cycle_type_hist.get(ct, 0) + 1
            if 10 not in ct:
                continue
            cyc = next(c for c in comps if len(c) == 10)
            inst += 1
            Q = rc.rotate(L, n, set(cyc), s0, s1)
            r0 = next(r for r in range(n) if r not in {x[0] for x in cyc})
            A = rc.mixed_analysis(Q, n, r0)
            assert rc.qls_violation(Q, n) is None and len(A['comps']) == 1 and rc.is_single_cycle(A['comps'][0], 5)
            c0 = {x for x in cyc if L[x] == s0}
            c1 = {x for x in cyc if L[x] == s1}
            flt = lambda t: (bool(set(t) & c0) == bool(set(t) & c1))
            res = a3.classical_adversary(L, flt)
            if res['covers']:
                with_mates += 1
            tot_mates += len(res['covers']); tot_pairs += res['pairs']; tot_triples += res['triples']
            if res['pairs']:
                with_pairs += 1
            if res['covers'] and not structure_done:
                T = res['T']
                ok = sum(1 for cv in res['covers'] if rc.pair_violation(Q, a3.mate_from(T, cv), n) is None)
                record('v5 k=5: ALL %d cycle-condition decompositions are classical mates of this C10-mixed Q' % len(res['covers']), len(res['covers']), ok)
                X = A['mixed']
                a, b = A['comps'][0]['supports'][0]
                if res['pairs']:
                    cv1, cv2 = res['first_pair']
                    R1, S1 = a3.mate_from(T, cv1), a3.mate_from(T, cv2)
                    record('v5 k=5: R (x) S ONB', None, rc.pair_violation(R1, S1, n))
                    FR = rc.forced_structure(Q, R1, n, r0, X, a, b, 'v5 k=5/R(a,b)')
                    FS = rc.forced_structure(Q, S1, n, r0, X, a, b, 'v5 k=5/S(a,b)')
                    rc.cross_mate_checks(FR, FS, 'v5 k=5/R,S(a,b)')
                    FRb = rc.forced_structure(Q, R1, n, r0, X, b, a, 'v5 k=5/R(b,a)')
                    FSb = rc.forced_structure(Q, S1, n, r0, X, b, a, 'v5 k=5/S(b,a)')
                    rc.cross_mate_checks(FRb, FSb, 'v5 k=5/R,S(b,a)')
                    print('   v5 k=5: U^R = %s' % FR['U'])
                    print('   v5 k=5: U^S = %s' % FS['U'])
                    off = [y for y in FR['Ea'] if y != (r0, a)]
                    print('   v5 k=5: e_b-overlap cells R %s S %s among off-first-row light e_a cells %s' % (sorted(FR['B']), sorted(FS['B']), off))
                    record('v5 k=5: n-k-1 == 2 off-first-row light e_a cells', 2, len(off))
                else:
                    R1 = a3.mate_from(T, res['covers'][0])
                    FR = rc.forced_structure(Q, R1, n, r0, X, a, b, 'v5 k=5/R(a,b)')
                    print('   v5 k=5: U^R = %s' % FR['U'])
                    off = [y for y in FR['Ea'] if y != (r0, a)]
                    record('v5 k=5: n-k-1 == 2 off-first-row light e_a cells', 2, len(off))
                structure_done = True
    print('   cycle-type histogram over (square, symbol pair): %s' % dict(sorted(cycle_type_hist.items())))
    print('   C10 instances %d, with >=1 classical mate %d, with orthogonal mate pairs %d; total mates %d, pairs %d, triples %d (%.1fs)'
          % (inst, with_mates, with_pairs, tot_mates, tot_pairs, tot_triples, time.time()-t0))
    record('v5 k=5: C10 instances with at least one classical mate exist (non-vacuous test)', True, with_mates >= 1)
    record('v5 k=5-adversarial: mutually orthogonal classical mate TRIPLES (candidate 3 predicts 0)', 0, tot_triples)
    end = utc()
    allres = RESULTS + [r for r in rc.RESULTS if 'check' in r]
    npass = sum(1 for r in allres if r['ok']); nfail = len(allres) - npass
    print('\nSUMMARY: %d checks, %d PASS, %d FAIL; start %s end %s' % (len(allres), npass, nfail, start, end))
    outpath = os.path.join(HERE, 'reviewer-controls-addendum-result-v5.json')
    if os.path.exists(outpath):
        print('refusing to overwrite', outpath); sys.exit(2)
    with open(outpath, 'w') as f:
        json.dump({'start_utc': start, 'end_utc': end, 'checks': len(allres), 'pass': npass, 'fail': nfail,
                   'pairs_generated': len(squares), 'c10_instances': inst, 'with_mates': with_mates, 'with_pairs': with_pairs,
                   'mates': tot_mates, 'pairs': tot_pairs, 'triples': tot_triples,
                   'cycle_type_hist': {str(k): v for k, v in cycle_type_hist.items()}, 'results': allres}, f, indent=1)
    print('wrote', outpath)
    sys.exit(0 if nfail == 0 else 1)

if __name__ == '__main__':
    main()
