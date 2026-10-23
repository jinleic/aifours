#!/usr/bin/env python3
"""rcert_run.py -- [F] c6 driver (task OlsonRunCount5): one process at a time, sequential calls of ./rcert2.
Part X (cross-check of the NEW tool against the FROZEN c5 receipt c5/out/allsing_run.txt, rotation classes, a subset only;
       c5 is not re-run): p = 11, k = 13..18 and p = 13, k = 15..19, every B: words, (H), (Hs0) and seedEmpty must equal
       c5's 'words', 'H', 'Hs', 'seedEmpty'.
Part T1 (target T1 of c6/README.md): the four p = 17 classes (k, B) = (25, 3), (25, 4), (26, 4), (27, 5), dihedral classes,
       MUT 0; native limit TLIM = 9000 s per class (an incomplete class is reported with complete = 0 and is UNKNOWN).
Part M (mutation controls, MUT = 1 seeds widened by one, MUT = 2 windows shrunk by one): p = 11, k = 16..18 (rot) and
       p = 17, (25, 3) (dih); counts must drop for MUT = 2 (plain and/or seeded).
Usage: python3 rcert_run.py PART   (PART in X, T1, M)"""
import subprocess, sys, json, time
def run(args):
    out = subprocess.run(['./rcert2'] + [str(a) for a in args], capture_output=True, text=True, check=True).stdout
    for line in out.splitlines(): print(line, flush=True)
    return [json.loads(l) for l in out.splitlines() if l.startswith('{"summary"')][0]
part = sys.argv[1]
print('== rcert_run.py %s start %s' % (part, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
if part == 'X':
    ref = {}
    for l in open('../c5/out/allsing_run.txt'):
        if '"summary"' in l:
            d = json.loads(l); ref[(d['p'], d['k'], d['B'])] = d
    agree = dis = 0; bad = []
    for p, ks in ((11, range(13, 19)), (13, range(15, 20))):
        for k in ks:
            for B in range(1, k - p):
                if k - p - B < 1: continue
                s = run([p, k, B, 'rot', 3000, 0])
                r = ref.get((p, k, B))
                ok = r is not None and (s['words'], s['H'], s['Hs0'], s['seedEmpty']) == (r['words'], r['H'], r['Hs'], r['seedEmpty'])
                agree += ok; dis += (not ok)
                if not ok: bad.append((p, k, B, s, r))
    print(json.dumps({'crosscheck_classes_agree': agree, 'disagree': dis, 'examples': bad[:3]}), flush=True)
elif part == 'T1':
    for (k, B) in ((25, 3), (25, 4), (26, 4), (27, 5)):
        run([17, k, B, 'dih', 9000, 0])
elif part == 'M':
    for M in (0, 1, 2):
        for k in (16, 17, 18):
            for B in range(1, k - 11):
                if k - 11 - B < 1: continue
                run([11, k, B, 'rot', 3000, M])
        run([17, 25, 3, 'dih', 3000, M])
print('== rcert_run.py %s end %s' % (part, time.strftime('%Y-%m-%dT%H:%M:%S')), flush=True)
