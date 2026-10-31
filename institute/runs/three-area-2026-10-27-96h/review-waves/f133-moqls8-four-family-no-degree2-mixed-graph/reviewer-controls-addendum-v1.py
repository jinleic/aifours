#!/usr/bin/env python3
"""
reviewer-controls-addendum-v1.py -- review wave f133, reviewer-written adversarial addendum.

Loads helper functions from reviewer-controls-v1.py (the reviewer's own file; no author code).  Adds:
  B'  exhaustive (all 832, not sampled) Q (x) R check for the C8 control of control B
  A'  exhaustive classical third-mate search for the two-C4 Q of control A (all classical mates up to relabeling
      are transversal decompositions of the base square with the symbol-pairing condition)
  F   C10-mixed Q in n=8 (k=5): only the complement bound n-k=3 is binding (row bound alone allows t<=4).
      Exhaustive classical-mate search over several completions of a partial Latin square whose {s0,s1} cells
      form a 10-cycle plus a 6-cycle.  Candidate 3 predicts: no mutually orthogonal TRIPLE of classical mates.
      If a pair exists, the k=5 forced structure (3 available transition positions per row, n-k-1=2 off-first-row
      light e_a cells, disjoint e_b-overlap sets) is verified exactly.
  G   C12-mixed Q in n=8 (k=6): bound min(5,2)=2.  Candidate 3 predicts: no orthogonal PAIR of classical mates.
"""
import sys, os, json, hashlib, itertools, datetime, time, random, importlib.util
from collections import Counter

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

def mate_from(T, cv):
    R = {}
    for sym, ti in enumerate(cv):
        for x in T[ti]:
            R[x] = rc.unit(n, sym)
    return R

def classical_adversary(L, good_filter, label, want_pairs=None, want_triples=0, sample_pairs=None):
    """All decompositions of L into 8 disjoint transversals passing good_filter; count orthogonal pairs/triples."""
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
    print('   %s: transversals %d, condition-passing %d, decompositions %d, orthogonal pairs %d, triples %d'
          % (label, len(T), len(good), len(covers), pairs, triples))
    return dict(T=T, masks=masks, covers=covers, pairs=pairs, triples=triples, first_pair=first_pair)

# ---------------------------------------------------------------------------------------------------------------
def control_Bprime():
    print('\n=== B\': exhaustive Q (x) R over all cycle-condition decompositions (C8 control) ===')
    els = [(a, b) for a in range(4) for b in range(2)]
    L, gi = rc.group_table(els, lambda x, y: ((x[0]+y[0]) % 4, (x[1]+y[1]) % 2))
    s0, s1 = gi[(0, 0)], gi[(1, 0)]
    cyc = next(c for c in rc.two_symbol_components(L, n, s0, s1) if (0, 0) in c)
    Q = rc.rotate(L, n, set(cyc), s0, s1)
    c0 = {x for x in cyc if L[x] == s0}
    c1 = {x for x in cyc if L[x] == s1}
    flt = lambda t: (bool(set(t) & c0) == bool(set(t) & c1))
    T = rc.transversals(L, n)
    masks = [sum(1 << (r*n + c) for r, c in t) for t in T]
    good = [i for i, t in enumerate(T) if flt(t)]
    covers = rc.exact_covers(masks, n, allowed=good)
    t0 = time.time()
    ok = sum(1 for cv in covers if rc.pair_violation(Q, mate_from(T, cv), n) is None)
    record('B\': ALL cycle-condition decompositions give classical mates of the C8-mixed Q', len(covers), ok)
    print('   B\': %d decompositions checked in %.1fs' % (len(covers), time.time()-t0))

# ---------------------------------------------------------------------------------------------------------------
def control_Aprime():
    print('\n=== A\': exhaustive classical third-mate search for the two-C4 Q of control A ===')
    s0, s1 = 0, 1
    squares = {lam: rc.gf8_linear_square(lam) for lam in range(1, 8)}
    # reproduce control A's first solution deterministically
    sol = None
    for lam in range(1, 8):
        L = squares[lam]
        ints = rc.intercalates_on(L, n, s0, s1)
        for I1, I2 in itertools.combinations(ints, 2):
            if set(I1[0]) & set(I2[0]) or set(I1[1]) & set(I2[1]):
                continue
            trade = {(r, c) for I in (I1, I2) for r in I[0] for c in I[1]}
            zero = [x for x in trade if L[x] == s0]
            one = [x for x in trade if L[x] == s1]
            for mu1, mu2 in itertools.combinations([m for m in range(1, 8) if m != lam], 2):
                if all({squares[mu][x] for x in zero} == {squares[mu][x] for x in one} for mu in (mu1, mu2)):
                    sol = (lam, I1, I2, mu1, mu2)
                    break
            if sol:
                break
        if sol:
            break
    lam, I1, I2, mu1, mu2 = sol
    L = squares[lam]
    trade = {(r, c) for I in (I1, I2) for r in I[0] for c in I[1]}
    zero = {x for x in trade if L[x] == s0}
    one = {x for x in trade if L[x] == s1}
    Q = rc.rotate(L, n, trade, s0, s1)
    # a classical mate R of Q (a Latin square L_R with Q (x) R an ONB) is, by the same argument as for a cycle,
    # an orthogonal mate of L whose symbol classes (transversals) meet a trade s0-cell iff they meet a trade s1-cell.
    flt = lambda t: (bool(set(t) & zero) == bool(set(t) & one))
    res = classical_adversary(L, flt, 'A\'')
    T, covers = res['T'], res['covers']
    t0 = time.time()
    ok = sum(1 for cv in covers if rc.pair_violation(Q, mate_from(T, cv), n) is None)
    record('A\': ALL pairing-condition decompositions give classical mates of the two-C4 Q', len(covers), ok)
    print('   A\': %d decompositions checked in %.1fs' % (len(covers), time.time()-t0))
    record('A\': orthogonal classical mate PAIRS exist (t=3 realised)', True, res['pairs'] >= 1)
    record('A\'-adversarial: mutually orthogonal classical mate TRIPLES (classical four-family extensions)', 0, res['triples'])
    # negative sanity: decompositions failing the pairing condition are not mates (sample)
    masks = res['masks']
    sample = [cv for cv in rc.exact_covers(masks, n, limit=300) if not all(flt(T[i]) for i in cv)][:100]
    bad = sum(1 for cv in sample if rc.pair_violation(Q, mate_from(T, cv), n) is not None)
    record('A\'-neg: sampled decompositions violating the pairing condition all fail Q (x) R (sample %d)' % len(sample), len(sample), bad)

# ---------------------------------------------------------------------------------------------------------------
def complete_latin(partial, n, rng):
    """Randomised backtracking completion of a partial Latin square (dict cell->symbol)."""
    L = dict(partial)
    cells = [(r, c) for r in range(n) for c in range(n) if (r, c) not in L]
    rowused = [set(L[(r, c)] for c in range(n) if (r, c) in L) for r in range(n)]
    colused = [set(L[(r, c)] for r in range(n) if (r, c) in L) for c in range(n)]
    sys.setrecursionlimit(10000)
    def rec(i):
        if i == len(cells):
            return True
        r, c = cells[i]
        opts = [s for s in range(n) if s not in rowused[r] and s not in colused[c]]
        rng.shuffle(opts)
        for s in opts:
            L[(r, c)] = s
            rowused[r].add(s); colused[c].add(s)
            if rec(i+1):
                return True
            rowused[r].discard(s); colused[c].discard(s)
            del L[(r, c)]
        return False
    assert rec(0)
    return L

def cycle_square(pi, n, rng):
    """Latin square with s0=0 on the diagonal and s1=1 at (r, pi(r)); the {0,1} cycles have lengths 2*|orbits of pi|."""
    partial = {}
    for r in range(n):
        partial[(r, r)] = 0
        partial[(r, pi[r])] = 1
    return complete_latin(partial, n, rng)

def control_cycle(label, pi, k, expect_pairs_zero, max_seeds, max_squares_with_mates):
    print('\n=== %s: single C_%d-mixed Q in n=8 (k=%d); candidate 3 bound t <= min(k-1, n-k) = %d ===' % (label, 2*k, k, min(k-1, n-k)))
    squares_tried, squares_with_decomp, squares_with_pairs = 0, 0, 0
    total_pairs, total_triples = 0, 0
    verified_structure = False
    for seed in range(max_seeds):
        rng = random.Random(seed)
        L = cycle_square(pi, n, rng)
        assert rc.is_latin(L, n)
        comps = rc.two_symbol_components(L, n, 0, 1)
        cyc = next(c for c in comps if len(c) == 2*k)
        squares_tried += 1
        Q = rc.rotate(L, n, set(cyc), 0, 1)
        r0 = next(r for r in range(n) if r not in {x[0] for x in cyc})
        A = rc.mixed_analysis(Q, n, r0)
        if seed == 0:
            record('%s: cycle lengths of the {0,1} cells' % label, sorted([2*k, 2*(n-k)]), sorted(len(c) for c in comps))
            record('%s: Q is a QLS' % label, None, rc.qls_violation(Q, n))
            record('%s: single mixed component which is a simple C_%d with one support and alternating parts' % (label, 2*k), True,
                   len(A['comps']) == 1 and rc.is_single_cycle(A['comps'][0], k))
        c0 = {x for x in cyc if L[x] == 0}
        c1 = {x for x in cyc if L[x] == 1}
        flt = lambda t: (bool(set(t) & c0) == bool(set(t) & c1))
        res = classical_adversary(L, flt, '%s seed %d' % (label, seed))
        if res['covers']:
            squares_with_decomp += 1
        total_pairs += res['pairs']
        total_triples += res['triples']
        if res['pairs']:
            squares_with_pairs += 1
            if not verified_structure:
                T = res['T']
                cv1, cv2 = res['first_pair']
                R, S = mate_from(T, cv1), mate_from(T, cv2)
                record('%s: Q (x) R ONB' % label, None, rc.pair_violation(Q, R, n))
                record('%s: Q (x) S ONB' % label, None, rc.pair_violation(Q, S, n))
                record('%s: R (x) S ONB' % label, None, rc.pair_violation(R, S, n))
                X = A['mixed']
                a, b = A['comps'][0]['supports'][0]
                FR = rc.forced_structure(Q, R, n, r0, X, a, b, label + '/R(a,b)')
                FS = rc.forced_structure(Q, S, n, r0, X, a, b, label + '/S(a,b)')
                rc.cross_mate_checks(FR, FS, label + '/R,S(a,b)')
                FRb = rc.forced_structure(Q, R, n, r0, X, b, a, label + '/R(b,a)')
                FSb = rc.forced_structure(Q, S, n, r0, X, b, a, label + '/S(b,a)')
                rc.cross_mate_checks(FRb, FSb, label + '/R,S(b,a)')
                print('   %s: U^R = %s' % (label, FR['U']))
                print('   %s: U^S = %s' % (label, FS['U']))
                print('   %s: e_b-overlap cells R %s S %s among off-first-row light e_a cells %s'
                      % (label, sorted(FR['B']), sorted(FS['B']), [y for y in FR['Ea'] if y != (r0, a)]))
                verified_structure = True
        if squares_with_pairs >= max_squares_with_mates:
            break
    print('   %s: squares tried %d, with >=1 cycle-condition decomposition %d, with orthogonal pairs %d; pairs %d, triples %d'
          % (label, squares_tried, squares_with_decomp, squares_with_pairs, total_pairs, total_triples))
    rc.RESULTS.extend([])  # keep rc results separate
    if expect_pairs_zero:
        record('%s-adversarial: orthogonal classical mate PAIRS over all tried squares (bound t<=2 predicts 0)' % label, 0, total_pairs)
    else:
        record('%s-adversarial: mutually orthogonal classical mate TRIPLES over all tried squares (bound t<=3 predicts 0)' % label, 0, total_triples)
        record('%s: at least one square with an orthogonal mate PAIR was found (t=3 realised for a C_%d-mixed member)' % (label, 2*k), True, squares_with_pairs >= 1)

def main():
    start = utc()
    print('reviewer-controls-addendum-v1.py start (UTC):', start)
    src = os.path.abspath(__file__)
    with open(src, 'rb') as f:
        print('script sha256:', hashlib.sha256(f.read()).hexdigest())
    with open(os.path.join(HERE, 'reviewer-controls-v1.py'), 'rb') as f:
        print('helper (reviewer-controls-v1.py) sha256:', hashlib.sha256(f.read()).hexdigest())
    control_Bprime()
    control_Aprime()
    # F: pi of cycle type (5,3): 10-cycle + 6-cycle
    pi_F = {0: 1, 1: 2, 2: 3, 3: 4, 4: 0, 5: 6, 6: 7, 7: 5}
    control_cycle('F', pi_F, 5, expect_pairs_zero=False, max_seeds=60, max_squares_with_mates=3)
    # G: pi of cycle type (6,2): 12-cycle + 4-cycle
    pi_G = {0: 1, 1: 2, 2: 3, 3: 4, 4: 5, 5: 0, 6: 7, 7: 6}
    control_cycle('G', pi_G, 6, expect_pairs_zero=True, max_seeds=60, max_squares_with_mates=10**9)
    end = utc()
    allres = RESULTS + [r for r in rc.RESULTS if 'check' in r]
    npass = sum(1 for r in allres if r['ok'])
    nfail = len(allres) - npass
    print('\nSUMMARY: %d checks, %d PASS, %d FAIL; start %s end %s' % (len(allres), npass, nfail, start, end))
    outpath = os.path.join(HERE, 'reviewer-controls-addendum-result-v1.json')
    if os.path.exists(outpath):
        print('refusing to overwrite', outpath)
        sys.exit(2)
    with open(outpath, 'w') as f:
        json.dump({'start_utc': start, 'end_utc': end, 'checks': len(allres), 'pass': npass, 'fail': nfail,
                   'results': allres}, f, indent=1)
    print('wrote', outpath)
    sys.exit(0 if nfail == 0 else 1)

if __name__ == '__main__':
    main()
