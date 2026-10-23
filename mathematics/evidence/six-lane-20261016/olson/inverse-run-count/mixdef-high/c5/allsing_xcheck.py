#!/usr/bin/env python3
"""allsing_xcheck.py -- [F] cross-check of the (H) part of the exploratory tool allsing.cpp (c5 README Sec. 7).
Re-computes, for every all-singleton item-(iii) class (p, k, B) with p = 11, k <= 16 and p = 13, k <= 16, the number of
words (one per rotation class, the same canonical form as allsing.cpp: lexicographically maximal 0/1 rotation) that satisfy
(H), with the INDEPENDENT routine `analyse` of the frozen c3/hcheck.py (its source is read and exec'ed; c3 is not modified),
and compares with the per-class counts "H" of out/allsing_run.txt.  Mutation control: MUT = 1 in hcheck's condition (B)
(p + 2 instead of p + 1) must lower some counts.
"""
import json, re, sys, time
src = open('../c3/hcheck.py').read()
start = src.index('def analyse'); end = src.index('n = agree = skipped = 0')
ns = {'itertools': __import__('itertools')}
def get_analyse(MUT):
    g = {'itertools': __import__('itertools'), 'MUT': MUT}
    exec(src[start:end], g)
    return g['analyse']
def rotmax(s):
    k = len(s)
    for r in range(1, k):
        for i in range(k):
            a, b = s[i], s[(i + r) % k]
            if a != b:
                if b > a: return False
                break
    return True
def words(k, B):
    from itertools import combinations
    for rest in combinations(range(1, k), B - 1):
        pos = (0,) + rest
        s = [0] * k
        for x in pos: s[x] = 1
        if rotmax(s): yield pos
summ = {}
for l in open('out/allsing_run.txt'):
    if '"summary"' in l:
        d = json.loads(l); summ[(d['p'], d['k'], d['B'])] = d
print('== allsing_xcheck.py start', time.strftime('%Y-%m-%dT%H:%M:%S'), flush=True)
an0, an1 = get_analyse(0), get_analyse(1)
agree = dis = 0; mutchanged = 0
for (p, kmax) in ((11, 16), (13, 16)):
    for k in range(p + 2, kmax + 1):
        kappa = k - p
        for B in range(1, kappa):
            kB = kappa - B
            n = h0 = h1 = 0
            for pos in words(k, B):
                d = [1] * k
                for x in pos: d[x] = -1
                a0 = an0(p, kB, B, d); a1 = an1(p, kB, B, d)
                n += 1; h0 += (a0[0] and a0[1]); h1 += (a1[0] and a1[1])
            ref = summ.get((p, k, B))
            ok = ref is not None and ref['words'] == n and ref['H'] == h0
            agree += ok; dis += (not ok)
            mutchanged += (h1 != h0)
            print(json.dumps({'p': p, 'k': k, 'B': B, 'kB': kB, 'words': n, 'H_hcheck': h0, 'H_hcheck_MUT1': h1,
                              'allsing_words': ref['words'] if ref else None, 'allsing_H': ref['H'] if ref else None, 'agree': ok}), flush=True)
print(json.dumps({'classes_agree': agree, 'classes_disagree': dis, 'classes_changed_by_MUT1': mutchanged}), flush=True)
print('== allsing_xcheck.py end', time.strftime('%Y-%m-%dT%H:%M:%S'), flush=True)
