#!/usr/bin/env python3
"""cplus_half.py -- [F] exact-control smoke for the sharpened hypothesis of Theorem C+ in c6/proof-Cplus-r2.md (review fix C4):
(ii+') 2kB <= p and n_ev,al <= 2(k - kB - 2B) + n_pr - 1, i.e. s0 := (k - kB - 2B) + (n_pr - n_ev,al)/2 >= 1/2.  Uses the frozen
c5/cplus_replay.py (exec'ed read-only): its word generator random_word_block, its literal replay 'procedure' (which asserts every
intermediate claim of the proof, in particular (B1+) |X_o| >= 2 Delta + 1, and checks the final pattern with an independent slow
lambda) and caseB_vector; words are restricted to s0 = 1/2 EXACTLY (the new case, outside r1's (ii+)).  MUT = 1: |S| = Delta (must
break (M) in Case B); MUT = 2: final test against lambda - 1 (must lose kills).  Usage: python3 cplus_half.py MUT NW NV"""
import sys, random, json, time
SRC = open('../c5/cplus_replay.py').read()
GUARD = "if __name__ == '__main__':\n    main()"
assert SRC.count(GUARD) == 1
G = {}
exec(compile(SRC.replace(GUARD, ""), 'c5/cplus_replay.py', 'exec'), G)
def main():
    MUT, NW, NV = (int(v) for v in sys.argv[1:4])
    rnd = random.Random(9009 + MUT)
    tot = {'words': 0, 'vectors': 0, 'kills': 0, 'nokill': 0, 'assert_failures': 0, 'caseA': 0, 'caseB': 0, 'caseB_margin_1': 0,
           'MUT1_M_broken': 0}
    ex = []
    t0 = time.time()
    print('== cplus_half.py MUT=%d NW=%d NV=%d start %s' % (MUT, NW, NV, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    for p in (13, 17, 19, 23):
        made = tries = 0
        while made < NW and tries < 2000000:
            tries += 1
            W = G['random_word_block'](rnd, p)
            s0x2 = 2 * (W.k - W.kB - 2 * W.B) + W.npr - W.nev_al
            if not (2 * W.kB <= p and s0x2 == 1): continue
            made += 1; tot['words'] += 1
            lo, hi = W.single_lo, W.single_hi
            for v in range(NV):
                if v % 3 != 2:
                    x = G['caseB_vector'](W, rnd)
                    if x is None: continue
                else:
                    if sum(lo) > p or sum(hi) < p: continue
                    x = [rnd.randint(lo[t], hi[t]) for t in range(W.k)]
                    diff = p - sum(x)
                    for t in rnd.sample(range(W.k), W.k):
                        if diff > 0: st = min(diff, hi[t] - x[t]); x[t] += st; diff -= st
                        elif diff < 0: st = min(-diff, x[t] - lo[t]); x[t] -= st; diff += st
                stats = {}
                tot['vectors'] += 1
                try:
                    kind, kill = G['procedure'](W, x, MUT, stats)
                    tot['case' + kind] += 1
                    if kill: tot['kills'] += 1
                    else: tot['nokill'] += 1
                    if kind == 'B':
                        cs, mg = G['caseinfo'](W, x)
                        if mg == 1: tot['caseB_margin_1'] += 1
                    tot['MUT1_M_broken'] += stats.get('MUT1_M_broken', 0)
                except AssertionError as e:
                    tot['assert_failures'] += 1
                    if len(ex) < 4: ex.append((p, W.a, W.b, x, str(e)[:80]))
        print('  p=%d words=%d tries=%d (%.1f s)' % (p, made, tries, time.time() - t0), flush=True)
    print(json.dumps({'MUT': MUT, 'totals': tot, 'first_failures': ex}), flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()
