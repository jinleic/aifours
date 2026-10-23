#!/usr/bin/env python3
"""Sample words, keep those uncovered by proved tools (coverage_all.classify),
and print run-structure statistics for them.
Usage: residual_stats.py p nwords seed mode"""
import sys, random, json
from collections import Counter
sys.path.insert(0, __import__('os').path.dirname(__file__))
import coverage_all as ca

def runs(word):
    # cyclic runs, rotated to start at an R-run following an F-run
    n = len(word)
    idx = [i for i in range(n) if word[i][0] == 'F' and word[(i + 1) % n][0] == 'R']
    if not idx:
        return None
    s = (idx[0] + 1) % n
    w = word[s:] + word[:s]
    out = []
    cur = [w[0]]
    for c, v in w[1:]:
        if c == cur[-1][0]:
            cur.append((c, v))
        else:
            out.append(cur); cur = [(c, v)]
    out.append(cur)
    return out

def main():
    p = int(sys.argv[1]); nw = int(sys.argv[2]); seed = int(sys.argv[3]); mode = sys.argv[4]
    rng = random.Random(seed)
    N = 4 * p - 1
    # reuse generator from coverage_all.main by monkeypatching: replicate modes
    gen = ca.__dict__
    shown = 0
    for it in range(nw):
        word = make(mode, p, N, rng)
        res = ca.classify(word, p)
        if any(res.values()):
            continue
        rr = runs(word)
        Rr = [r for r in rr if r[0][0] == 'R']
        Fr = [r for r in rr if r[0][0] == 'F']
        k = len(Rr)
        F = sum(len(r) for r in Fr); R = sum(len(r) for r in Rr)
        lens = [len(r) for r in Fr]
        rsz = [len(r) for r in Rr]
        nets = [sum(1 if v == 1 else (-1 if v == p - 1 else 99) for _, v in r) for r in Rr]
        fconst = all(len(set(v for _, v in r)) == 1 for r in Fr)
        print(json.dumps({'F': F, 'R': R, 'k': k, 'kodd': sum(1 for s in rsz if s % 2), 'Flens': lens,
                          'Rsz': rsz, 'nets': nets, 'Fconst': fconst,
                          'Fvals': [[v for _, v in r] for r in Fr]}))
        shown += 1
    print('shown', shown)

def make(mode, p, N, rng):
    if mode == 'rotrigid':
        pr = rng.uniform(0.25, 0.6)
        return [('R', rng.choice([1, p - 1])) if rng.random() < pr else ('F', rng.randrange(p)) for _ in range(N)]
    if mode == 'twoval':
        c = rng.randrange(1, p)
        pr = rng.uniform(0.25, 0.6)
        return [('R', rng.choice([1, p - 1])) if rng.random() < pr else ('F', rng.choice([0, c])) for _ in range(N)]
    if mode == 'gr':
        pr = rng.uniform(0.25, 0.6)
        word, prevF, cur = [], False, 0
        for _ in range(N):
            if rng.random() < pr:
                word.append(('R', rng.choice([1, p - 1]))); prevF = False
            else:
                if not prevF:
                    cur = rng.randrange(p) if rng.random() < 0.5 else 0
                word.append(('F', cur)); prevF = True
        return word
    raise SystemExit('mode?')

if __name__ == '__main__':
    main()
