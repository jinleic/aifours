#!/usr/bin/env python3
"""replayG2.py -- [F] literal replay of c6/proof-SEEDG.md, Part 1 (as replayG.py) + Part 2 (deep), with mutation controls.
Usage: python3 replayG2.py MUT NV
The functions of c6/replayG.py are exec'ed read-only (its main() is not run).  Part 1 = replayG.py's run (full proof, explicit
seed arcs checked).  Part 2 (deep): vectors drawn inside the seed boxes [max(lambda({t}), s_lo), min(U({t}), s_hi)] with sum p; the
explicit seed arcs are NOT checked (the conclusion of Lemma GS is asserted instead), then the pin chain of {a}^c with the seed
ranges, X_[k] = p, the Theorem C+ procedure and the final removal chain, as in Part 1.  RA2 words have no Part 2 (their boxes
admit no vector with sum p: sum x = -2).  MUT as in replayG.py: 1 canonical ranges in the certification steps; 2 kill re-check
against lambda - 1; 3 |S| = Delta in the C+ procedure.
"""
import sys, random, time, json
SRCG = open('replayG.py').read()
GUARD = "if __name__ == '__main__':\n    main()"
assert SRCG.count(GUARD) == 1
NS = {'__name__': 'replayG_lib'}
exec(compile(SRCG.replace(GUARD, ''), 'c6/replayG.py', 'exec'), NS)
Kill, verify_kill, seeds_of, certify_chain, procedure = NS['Kill'], NS['verify_kill'], NS['seeds_of'], NS['certify_chain'], NS['procedure']
lam_set, U_set, in_arc = NS['lam_set'], NS['U_set'], NS['in_arc']
def run_deep(W, SD, x, MUT, stats):
    p, k = W.p, W.k
    u = [xi % p for xi in x]
    rng = {}
    for t in range(k):
        if not in_arc(W, {t}, u): raise Kill(frozenset([t]), 'singleton')
        L1, U1 = lam_set(W, {t}), U_set(W, {t})
        assert L1 <= x[t] <= U1
        Q, slo, shi = SD[t]
        assert slo <= x[t] <= shi
        rng[t] = (max(L1, slo), min(U1, shi)) if MUT != 1 else (L1, U1)
    certify_chain(W, set(range(1, k)), x, u, rng, 'pin')
    assert sum(x) == p
    kind2, kill, Qf = procedure(W, x, 1 if MUT == 3 else 0, stats)
    if MUT == 3 and not kill: return 'MUT3-M-broken'
    assert kill, 'procedure pattern does not violate (0.2)'
    certify_chain(W, set(Qf), x, u, rng, 'final-' + kind2)
    raise AssertionError('violated pattern certified without a kill')
def deep_vectors(W, SD, rnd, NV):
    p, k = W.p, W.k
    box = [(max(W.single_lo[t], SD[t][1]), min(W.single_hi[t], SD[t][2])) for t in range(k)]
    if sum(lo for lo, hi in box) > p or sum(hi for lo, hi in box) < p: return []
    out = []
    for i in range(NV):
        mode = i % 4
        if mode == 0: x = [rnd.randint(lo, hi) for lo, hi in box]
        elif mode == 1: x = [lo for lo, hi in box]
        elif mode == 2: x = [hi for lo, hi in box]
        else: x = [min(max((1 if W.d[t] > 0 else (-1 if W.d[t] < 0 else 0)), lo), hi) for t, (lo, hi) in enumerate(box)]
        diff = p - sum(x); guard = 0
        while diff != 0 and guard < 400000:
            guard += 1
            t = rnd.randrange(k); lo, hi = box[t]
            if diff > 0 and x[t] < hi: x[t] += 1; diff -= 1
            elif diff < 0 and x[t] > lo: x[t] -= 1; diff += 1
        if diff == 0: out.append(('deep%d' % mode, x))
    return out
def main():
    MUT = int(sys.argv[1]); NV = int(sys.argv[2])
    rnd = random.Random(9009 + MUT)
    t0 = time.time()
    print('== replayG2.py MUT=%d NV=%d start %s' % (MUT, NV, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
    # Part 1: replayG.py's main with this MUT/NV (its own seeds)
    sys_argv = sys.argv
    sys.argv = ['replayG.py', str(MUT), str(NV)]
    NS['main']()
    sys.argv = sys_argv
    # Part 2: deep vectors on fresh words of the same kinds
    jobs = []
    for p in (13, 17, 19): jobs.append(('RA3', p, p - 6, 3, (p - 3) // 2))
    for p in (11, 13, 17, 19): jobs.append(('RA3', p, p - 7, 3, (p - 5) // 2))
    for p in (17, 19, 23, 29):
        for fam, reg in (('SA', NS['region_SA']), ('PA', NS['region_PA'])):
            pool = []
            for (k, kappa, B) in NS['classes'](p):
                if 2 * p - k + 2 * kappa == k: continue
                W0 = NS['make_excess_word'](p, k, kappa, B, rnd)
                if W0 is None: continue
                if fam == 'PA' and NS['region_SA'](W0) is not None: continue
                if reg(W0) is not None: pool.append((k, kappa, B))
                if len(pool) >= 40: break
            for (k, kappa, B) in rnd.sample(pool, min(3, len(pool))): jobs.append((fam, p, k, kappa, B))
    tot = {}; fails = []; nwords = 0; nodeep = 0
    for job in jobs:
        if job[0] == 'RA3':
            kind, p, kB, B, m = job
            words = [NS['make_allsingle'](p, kB, B, lay, rnd) for lay in ('block', 'spread', 'random')]
        else:
            kind, p, k, kappa, B = job
            words = [w for w in (NS['make_excess_word'](p, k, kappa, B, rnd) for _ in range(3)) if w is not None]
        for W in words:
            if kind in ('SA', 'PA'): m = NS['region_SA'](W) if kind == 'SA' else NS['region_PA'](W)
            nwords += 1
            SD = seeds_of(W, kind, m)
            vs = deep_vectors(W, SD, rnd, NV)
            if not vs: nodeep += 1
            for (tag, x) in vs:
                stats = {}
                try:
                    out = run_deep(W, SD, x, MUT, stats)
                except Kill as K:
                    out = K.stage if verify_kill(W, K.P, [xi % W.p for xi in x], MUT) else 'NOKILL-' + K.stage
                except AssertionError as e:
                    out = 'ASSERT:' + str(e)[:45]
                key = 'P2:%s:%s' % (kind, out)
                tot[key] = tot.get(key, 0) + 1
                if (out.startswith('NOKILL') or out.startswith('ASSERT')) and len(fails) < 8: fails.append((job, tag, out))
        print('  deep job %s done %.1f s' % (str(job), time.time() - t0), flush=True)
    print(json.dumps({'MUT': MUT, 'part': 2, 'jobs': jobs, 'words': nwords, 'words_without_deep_vectors': nodeep,
                      'outcomes': sorted(tot.items()), 'first_failures': fails}), flush=True)
    print('== end %.1f s' % (time.time() - t0), flush=True)
if __name__ == '__main__':
    main()
