#!/usr/bin/env python3
"""
reviewer-controls-addendum-v2.py -- review wave f133, reviewer-written adversarial addendum, second attempt.

Addendum v1's controls F/G were vacuous: random Latin-square completions with a prescribed 10-/12-cycle had no
classical mates at all.  Here the base squares are single cycle switches of the four non-cyclic group tables of
order 8 (Z2^3, Z4xZ2, D4, Q8): swapping two symbols along one of their row/column cycles keeps the square Latin,
keeps many transversals, and changes the cycle structure of other symbol pairs, which produces 10- and 12-cycles.

For every resulting (square, symbol pair, cycle of length 2k with k in {5,6}) the C_2k-mixed Q is built, every
classical mate of Q is enumerated (= transversal decompositions with the cycle condition), and the numbers of
mutually orthogonal mate pairs and triples are counted.  Candidate 3 predicts:
  k=5 (C10): t <= min(4,3) = 3  -> no TRIPLE of mutually orthogonal classical mates (the row bound alone allows 4);
  k=6 (C12): t <= min(5,2) = 2  -> no PAIR of orthogonal classical mates (the row bound alone allows 5).
A found triple (k=5) or pair (k=6) would refute candidate 3's complement pigeonhole.
"""
import sys, os, json, hashlib, itertools, datetime, time, importlib.util
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

def group_tables():
    out = {}
    els = [(a, b) for a in range(2) for b in range(4)]
    out['Z2xZ4'] = rc.group_table(els, lambda x, y: ((x[0]+y[0]) % 2, (x[1]+y[1]) % 4))[0]
    els = list(itertools.product(range(2), repeat=3))
    out['Z2^3'] = rc.group_table(els, lambda x, y: tuple((a+b) % 2 for a, b in zip(x, y)))[0]
    els = [(r, s) for s in range(2) for r in range(4)]
    out['D4'] = rc.group_table(els, lambda x, y: ((x[0] + (y[0] if x[1] == 0 else -y[0])) % 4, (x[1]+y[1]) % 2))[0]
    # Q8 as pairs (sign, unit) with unit in {1,i,j,k}; multiplication table of units
    units = ['1', 'i', 'j', 'k']
    mul = {('1', u): (1, u) for u in units}
    mul.update({(u, '1'): (1, u) for u in units})
    mul.update({('i', 'i'): (-1, '1'), ('j', 'j'): (-1, '1'), ('k', 'k'): (-1, '1'),
                ('i', 'j'): (1, 'k'), ('j', 'k'): (1, 'i'), ('k', 'i'): (1, 'j'),
                ('j', 'i'): (-1, 'k'), ('k', 'j'): (-1, 'i'), ('i', 'k'): (-1, 'j')})
    els = [(s, u) for s in (1, -1) for u in units]
    def qmul(x, y):
        s, u = mul[(x[1], y[1])]
        return (x[0]*y[0]*s, u)
    out['Q8'] = rc.group_table(els, qmul)[0]
    for name, L in out.items():
        assert rc.is_latin(L, n), name
    return out

def cycle_switches(L):
    """All Latin squares obtained from L by swapping two symbols along one of their row/column cycles."""
    out = []
    for sa, sb in itertools.combinations(range(n), 2):
        for cyc in rc.two_symbol_components(L, n, sa, sb):
            L2 = dict(L)
            for x in cyc:
                L2[x] = sb if L[x] == sa else sa
            out.append(L2)
    return out

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

def run_k(k, max_instances):
    print('\n=== C_%d-mixed Q (k=%d) in n=8 from cycle-switched group tables; candidate 3 bound t <= %d ===' % (2*k, k, min(k-1, n-k)))
    seen = set()
    inst = 0
    with_decomp = 0
    with_pairs = 0
    tot_pairs = tot_triples = tot_mates = 0
    structure_done = False
    t0 = time.time()
    for gname, L0 in group_tables().items():
        for L in cycle_switches(L0):
            key = tuple(L[(r, c)] for r in range(n) for c in range(n))
            for s0, s1 in itertools.combinations(range(n), 2):
                comps = rc.two_symbol_components(L, n, s0, s1)
                for cyc in comps:
                    if len(cyc) != 2*k:
                        continue
                    k2 = (key, s0, s1, tuple(cyc))
                    if k2 in seen:
                        continue
                    seen.add(k2)
                    inst += 1
                    Q = rc.rotate(L, n, set(cyc), s0, s1)
                    assert rc.qls_violation(Q, n) is None
                    r0 = next(r for r in range(n) if r not in {x[0] for x in cyc})
                    A = rc.mixed_analysis(Q, n, r0)
                    assert len(A['comps']) == 1 and rc.is_single_cycle(A['comps'][0], k)
                    c0 = {x for x in cyc if L[x] == s0}
                    c1 = {x for x in cyc if L[x] == s1}
                    flt = lambda t: (bool(set(t) & c0) == bool(set(t) & c1))
                    res = classical_adversary(L, flt)
                    tot_mates += len(res['covers'])
                    if res['covers']:
                        with_decomp += 1
                    tot_pairs += res['pairs']
                    tot_triples += res['triples']
                    if res['pairs']:
                        with_pairs += 1
                    if res['covers'] and (res['pairs'] or k == 6) and not structure_done:
                        # verify Q (x) R for every classical mate of this instance, and the forced structure on one mate / pair
                        T = res['T']
                        ok = sum(1 for cv in res['covers'] if rc.pair_violation(Q, mate_from(T, cv), n) is None)
                        record('k=%d (%s switch): ALL %d cycle-condition decompositions are classical mates of Q' % (k, gname, len(res['covers'])), len(res['covers']), ok)
                        X = A['mixed']
                        a, b = A['comps'][0]['supports'][0]
                        if res['pairs']:
                            cv1, cv2 = res['first_pair']
                            R, S = mate_from(T, cv1), mate_from(T, cv2)
                            record('k=%d: R (x) S ONB' % k, None, rc.pair_violation(R, S, n))
                            FR = rc.forced_structure(Q, R, n, r0, X, a, b, 'k=%d/R(a,b)' % k)
                            FS = rc.forced_structure(Q, S, n, r0, X, a, b, 'k=%d/S(a,b)' % k)
                            rc.cross_mate_checks(FR, FS, 'k=%d/R,S(a,b)' % k)
                            FRb = rc.forced_structure(Q, R, n, r0, X, b, a, 'k=%d/R(b,a)' % k)
                            FSb = rc.forced_structure(Q, S, n, r0, X, b, a, 'k=%d/S(b,a)' % k)
                            rc.cross_mate_checks(FRb, FSb, 'k=%d/R,S(b,a)' % k)
                            print('   k=%d: U^R = %s' % (k, FR['U']))
                            print('   k=%d: U^S = %s' % (k, FS['U']))
                            print('   k=%d: e_b-overlap cells R %s S %s among off-first-row light e_a cells %s'
                                  % (k, sorted(FR['B']), sorted(FS['B']), [y for y in FR['Ea'] if y != (r0, a)]))
                            record('k=%d: n-k-1 off-first-row light e_a cells' % k, n-k-1, len([y for y in FR['Ea'] if y != (r0, a)]))
                        else:
                            R = mate_from(T, res['covers'][0])
                            FR = rc.forced_structure(Q, R, n, r0, X, a, b, 'k=%d/R(a,b)' % k)
                            print('   k=%d: U^R = %s' % (k, FR['U']))
                            record('k=%d: n-k-1 off-first-row light e_a cells' % k, n-k-1, len([y for y in FR['Ea'] if y != (r0, a)]))
                        structure_done = True
                    if inst >= max_instances:
                        break
                if inst >= max_instances:
                    break
            if inst >= max_instances:
                break
        if inst >= max_instances:
            break
    print('   k=%d: instances %d (distinct square/symbol-pair/cycle), with >=1 classical mate %d, with orthogonal mate pairs %d;'
          ' total mates %d, pairs %d, triples %d (%.1fs)' % (k, inst, with_decomp, with_pairs, tot_mates, tot_pairs, tot_triples, time.time()-t0))
    return dict(inst=inst, with_decomp=with_decomp, with_pairs=with_pairs, pairs=tot_pairs, triples=tot_triples, mates=tot_mates)

def main():
    start = utc()
    print('reviewer-controls-addendum-v2.py start (UTC):', start)
    src = os.path.abspath(__file__)
    with open(src, 'rb') as f:
        print('script sha256:', hashlib.sha256(f.read()).hexdigest())
    with open(os.path.join(HERE, 'reviewer-controls-v1.py'), 'rb') as f:
        print('helper (reviewer-controls-v1.py) sha256:', hashlib.sha256(f.read()).hexdigest())
    r5 = run_k(5, max_instances=400)
    record('k=5 (C10): instances with at least one classical mate exist (non-vacuous test)', True, r5['with_decomp'] >= 1)
    record('k=5 (C10)-adversarial: mutually orthogonal classical mate TRIPLES (candidate 3 predicts 0; row bound alone would allow them)', 0, r5['triples'])
    r6 = run_k(6, max_instances=400)
    record('k=6 (C12): instances with at least one classical mate exist (non-vacuous test)', True, r6['with_decomp'] >= 1)
    record('k=6 (C12)-adversarial: orthogonal classical mate PAIRS (candidate 3 predicts 0; row bound alone would allow 4 mates)', 0, r6['pairs'])
    end = utc()
    allres = RESULTS + [r for r in rc.RESULTS if 'check' in r]
    npass = sum(1 for r in allres if r['ok'])
    nfail = len(allres) - npass
    print('\nSUMMARY: %d checks, %d PASS, %d FAIL; start %s end %s' % (len(allres), npass, nfail, start, end))
    outpath = os.path.join(HERE, 'reviewer-controls-addendum-result-v2.json')
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
