#!/usr/bin/env python3
"""Independent Python cross-checks for the parent replay of worker claim C5' (D_10, p = 5, four odd blocks, n = 18).

Written from the definitions only; imports and runs no worker code and shares no code with the C++ replay.
  (1) fact (d) recomputed with itertools.combinations over every expanded rotation multiset, H = 0..7; the survivor
      multisets are compared with the C++ list survivor_multisets.txt;
  (2) closed-form domain counts per H;
  (3) naive D_10 check (own group law, all C(18,10) index subsets) of PC-k2, three avoider classes found by the C++
      enumeration (every l-tuple), a solved one-letter mutation of PC-k2, and PC-k2 / the found avoiders under the
      injected bugs (untwisted law, target length 8, parity-bug filter).
Usage: python3 -B indep_check_v1.py CPP_SURVIVOR_MULTISETS OUTDIR
"""
import itertools
import json
import math
import os
import sys
import time

P, TARGET = 5, 10
E = (0, 1)


def mul(a, b, twisted=True):
    (v, e), (w, f) = a, b
    return ((v + (e * w if twisted else w)) % P, e * f)


def rho(x):
    return (x % P, 1)


def sig(y):
    return (y % P, -1)


def solvable(word, k=TARGET, twisted=True):
    for idx in itertools.combinations(range(len(word)), k):
        g = E
        for i in idx:
            g = mul(g, word[i], twisted)
        if g == E:
            return True
    return False


def filter_d(H, m, parity_bug=False):
    vals = [x for x in range(P) for _ in range(m[x])]
    pairs = H + 4 if parity_bug else H
    for j in range(0, min(pairs, 5) + 1):
        s = TARGET - 2 * j
        if s > len(vals):
            continue
        if any(sum(c) % P == 0 for c in itertools.combinations(vals, s)):
            return True
    return False


def multisets(R):
    for comb in itertools.combinations_with_replacement(range(P), R):
        yield tuple(comb.count(x) for x in range(P))


def rigid(m):
    vals = {x for x in range(P) if m[x]}
    return any(vals <= {c, (-c) % P} for c in range(1, P))


def ltuples(H):
    return [(a1, a2, a3, H - a1 - a2 - a3) for a1 in range(H + 1) for a2 in range(H + 1 - a1)
            for a3 in range(H + 1 - a1 - a2)]


def word_from(runs, ls, ys):
    w = []
    for i in range(4):
        w += [rho(x) for x in sorted(runs[i])]
        w += [sig(ys[i])] * ls[i]
    return w


def parse_class(line):
    f = dict(kv.split('=', 1) for kv in line.strip().split('|'))
    runs = [[] if r == '-' else [int(ch) for ch in r] for r in f['runs'].split('/')]
    return int(f['H']), runs, [int(ch) for ch in f['y']]


def main():
    surv_path, outdir = sys.argv[1], sys.argv[2]
    os.mkdir(outdir)
    t0 = time.time()
    res = {'script': 'indep_check_v1.py'}
    # (1)+(2) filter (d) and counts
    py_surv, per_H = [], []
    for H in range(8):
        R = 14 - 2 * H
        ms = list(multisets(R))
        surv = [m for m in ms if not filter_d(H, m)]
        py_surv += [(H, m) for m in surv]
        nL = math.comb(H + 3, 3)
        assert len(ltuples(H)) == nL
        dists = math.comb(R + 19, 19)
        prod = lambda m: math.prod(math.comb(c + 3, 3) for c in m)
        per_H.append(dict(H=H, R=R, ltuples=nL, multisets=len(ms), multisets_formula=math.comb(R + 4, 4),
                          survivors=len(surv), survivors_rigid=sum(rigid(m) for m in surv), dists=dists,
                          sum_over_M_prod=sum(prod(m) for m in ms), survivor_dists=sum(prod(m) for m in surv),
                          words=nL * 625 * dists, survivor_words=nL * 625 * sum(prod(m) for m in surv),
                          literal_words=nL * 625 * math.comb(R + 3, 3) * 5 ** R))
    cpp = []
    with open(surv_path) as fh:
        for line in fh:
            f = dict(kv.split('=', 1) for kv in line.strip().split('|'))
            cpp.append((int(f['H']), tuple(int(t) for t in f['M'].split(','))))
    sp, sc = set(py_surv), set(cpp)
    res['filter_d'] = dict(python_survivors=len(py_surv), cpp_survivors=len(cpp), identical=sp == sc and len(cpp) == len(sc),
                           only_python=sorted(map(str, sp - sc)), only_cpp=sorted(map(str, sc - sp)))
    res['per_H'] = per_H
    res['totals'] = dict(words_H0_4=sum(d['words'] for d in per_H if d['H'] <= 4),
                         words_H0_7=sum(d['words'] for d in per_H),
                         survivor_words=sum(d['survivor_words'] for d in per_H),
                         literal_words_H0_4=sum(d['literal_words'] for d in per_H if d['H'] <= 4),
                         literal_words_H0_7=sum(d['literal_words'] for d in per_H))
    res['totals']['task_closed_form_1021369625000_matches_H0_4'] = res['totals']['words_H0_4'] == 1021369625000
    # (3) naive checks
    pc = [rho(1)] * 9 + [sig(0)] * 7 + [rho(4)] + [sig(0)]
    mut = [rho(1)] * 9 + [sig(0)] * 7 + [rho(1)] + [sig(0)]
    nc = dict(pc_k2_length=len(pc), pc_k2_avoids=not solvable(pc), pc_k2_untwisted_solvable=solvable(pc, twisted=False),
              pc_k2_target8_solvable=solvable(pc, k=8), pc_k2_filter_d_clean=filter_d(2, (0, 9, 0, 0, 1)),
              pc_k2_filter_d_parity_bug=filter_d(2, (0, 9, 0, 0, 1), parity_bug=True),
              pc_k2_last_rotation_to_rho1_solvable=solvable(mut))
    classes = ['H=2|runs=111111111/-/-/4|y=0000',  # PC-k2 class (6 of its 10 l-tuples spell PC-k2 literally)
               'H=1|runs=4/4/4/111111111|y=0000',  # found avoider A1
               'H=3|runs=-/-/4/4444444|y=0020',    # found avoider A2
               'H=4|runs=4/4/4/444|y=0243']        # found avoider A3
    cls = []
    for line in classes:
        H, runs, ys = parse_class(line)
        m = tuple(sum(r.count(x) for r in runs) for x in range(P))
        rows = []
        for a in ltuples(H):
            ls = [2 * t + 1 for t in a]
            w = word_from(runs, ls, ys)
            assert len(w) == 18
            rows.append(dict(l=ls, avoids=not solvable(w), untwisted_solvable=solvable(w, twisted=False),
                             target8_solvable=solvable(w, k=8)))
        cls.append(dict(cls=line, multiset=m, rigid=rigid(m), filter_d_clean=filter_d(H, m),
                        filter_d_parity_bug=filter_d(H, m, parity_bug=True), ltuples=len(rows),
                        avoid_all=all(r['avoids'] for r in rows),
                        untwisted_solvable=sum(r['untwisted_solvable'] for r in rows),
                        target8_solvable=sum(r['target8_solvable'] for r in rows)))
    nc['classes'] = cls
    res['naive'] = nc
    ok = (res['filter_d']['identical'] and res['totals']['task_closed_form_1021369625000_matches_H0_4']
          and nc['pc_k2_avoids'] and nc['pc_k2_untwisted_solvable'] and nc['pc_k2_target8_solvable']
          and not nc['pc_k2_filter_d_clean'] and nc['pc_k2_filter_d_parity_bug']
          and nc['pc_k2_last_rotation_to_rho1_solvable']
          and all(c['avoid_all'] and c['rigid'] and not c['filter_d_clean'] and c['filter_d_parity_bug']
                  and c['untwisted_solvable'] == c['ltuples'] and c['target8_solvable'] == c['ltuples'] for c in cls))
    res['all_ok'] = ok
    res['elapsed_s'] = round(time.time() - t0, 3)
    with open(os.path.join(outdir, 'indep_check.json'), 'x') as fh:
        json.dump(res, fh, indent=1)
        fh.write('\n')
    print('indep_check all_ok=%s elapsed=%.1fs' % (ok, res['elapsed_s']))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
