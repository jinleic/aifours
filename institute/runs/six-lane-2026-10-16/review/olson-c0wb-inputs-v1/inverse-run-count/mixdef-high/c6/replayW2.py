#!/usr/bin/env python3
"""replayW2.py -- [F] Case-B-biased literal replay of Lemma C0B (c6/proof-C0WB.md), task OlsonRunCount5.  Usage: python3 replayW2.py MUT NV
replayW.py produced only Case A instances for C0B.  Here the vectors are built so that the defects are anti runs with c <= 0
(x = -ceil(b/2)) and every other run is a non-defect at its least x (bh = 1 or 2), then raised (aligned runs, bh += 2, within
U({t})) until sum x = p; so Phi(Z) is small and Case B occurs.  Words: classes with k >= kB + 3B and 2kB <= p (p = 17, 19, 23, 29, 31)
whose word violates Theorem C+'s count (n_ev,al > 4 and n_ev,al > 2(k - kB - 2B) + n_pr - 1).  The construction is c5's procedure
(Theorem C+, exec'ed read-only via replayW.py's loader); its assertion '(B1+) fails' is the count Lemma C0B proves; in Case B also
n_ev,al <= B + n_an - 2 is asserted.  Every final pattern is re-checked with slow_lambda.  MUT 1: kill re-check against lambda - 1.
"""
import sys, random, time, json
SRCW = open('replayW.py').read()
GUARD = "if __name__ == '__main__':\n    main()"
assert SRCW.count(GUARD) == 1
NS = {'__name__': 'replayW_lib'}
exec(compile(SRCW.replace(GUARD, ''), 'c6/replayW.py', 'exec'), NS)
procedure, lam_set, make_word, classes = NS['procedure'], NS['lam_set'], NS['make_word'], NS['classes']
def caseB_vector(W, rnd):
    p, k = W.p, W.k
    x = [None] * k
    for t in range(k):
        a, b = W.a[t], W.b[t]
        if a == 0: x[t] = -((b + 1) // 2)                     # anti defect, c = -floor(b/2) <= 0
        elif b == 0: x[t] = (a + 1) // 2 if a % 2 == 1 else a // 2 + 1
        else: x[t] = 1                                         # pair, bh = 2
        x[t] = max(x[t], W.single_lo[t])
    diff = p - sum(x); guard = 0
    al = [t for t in range(k) if W.b[t] == 0]
    while diff != 0 and guard < 200000:
        guard += 1
        t = rnd.choice(al) if diff > 0 else rnd.randrange(k)
        if diff > 0 and x[t] < W.single_hi[t]: x[t] += 1; diff -= 1
        elif diff < 0 and x[t] > W.single_lo[t]: x[t] -= 1; diff += 1
    return x if diff == 0 else None
def main():
    MUT = int(sys.argv[1]); NV = int(sys.argv[2])
    rnd = random.Random(12012 + MUT)
    t0 = time.time()
    print('== replayW2.py MUT=%d NV=%d start %s' % (MUT, NV, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    tot = {}; fails = []; words = 0
    for p in (17, 19, 23, 29, 31):
        pool = [(k, ka, B) for (k, ka, B) in classes(p) if k >= (ka - B) + 3 * B and 2 * (ka - B) <= p and 2 * p - k + 2 * ka - k >= 6]
        done = 0
        for (k, ka, B) in rnd.sample(pool, len(pool)):
            if done >= 8: break
            W = None
            for _ in range(30):
                W0 = make_word(p, k, ka, B, rnd, prefer_even=True)
                if W0 is not None and W0.nev_al > 4 and W0.nev_al > 2 * (W0.k - W0.kB - 2 * W0.B) + W0.npr - 1 and len(W0.anti) >= 1:
                    W = W0; break
            if W is None: continue
            done += 1; words += 1
            for _ in range(NV):
                x = caseB_vector(W, rnd)
                if x is None: tot['novector'] = tot.get('novector', 0) + 1; continue
                stats = {}
                try:
                    kind, kill, Q = procedure(W, x, 0, stats)
                    if kind == 'B':
                        assert W.nev_al <= W.B + len(W.anti) - 2, 'n_ev,al bound'
                    lamQ = lam_set(W, Q) - (1 if MUT == 1 else 0)
                    res = 'kill-' + kind if sum(x[u] for u in Q) < lamQ else 'NOKILL-' + kind
                except AssertionError as e:
                    res = 'ASSERT:' + str(e)[:40]
                tot[res] = tot.get(res, 0) + 1
                if ('NOKILL' in res or 'ASSERT' in res) and len(fails) < 8: fails.append((p, k, ka, B, W.nev_al, res))
        print('  p = %d done %.1f s' % (p, time.time() - t0), flush=True)
    print(json.dumps({'MUT': MUT, 'words': words, 'outcomes': sorted(tot.items()), 'first_failures': fails}), flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()
