#!/usr/bin/env python3
"""Random inherited RGR run data with k >= p+1 at N = 4p-2; for those with no full window,
run hwsingle with famM = 1, 2, 3 and report which family certifies (aid only).
Usage: sample_famtest.py p trials seed consttype(0/1) [kmin]"""
import random, subprocess, sys, json, os
HERE = os.path.dirname(os.path.abspath(__file__))
from hw import windows


def inherited(a, b, l, p):
    R = sum(a) + sum(b); F = sum(l); H = sum(x // 2 for x in l)
    fr = sum((x + y) // 2 for x, y in zip(a, b))
    if any(x > p - 1 for x in a) or any(y > p - 1 for y in b):
        return False
    return R <= 3 * p - 2 and F + fr <= 3 * p - 2 and R + H <= 3 * p - 2 and H <= p - 1


def has_full(a, b, l, p):
    W = windows(a, b, l, p)
    return any(hi - lo + 1 >= p for (lo, hi) in W.values())


def run(p, fam, a, b, l, cap=20000):
    k = len(a)
    args = [os.path.join(HERE, 'hwsingle'), str(p), str(fam), str(k)] + [str(x) for x in a + b + l] + ['0', str(cap)]
    out = subprocess.run(args, capture_output=True, text=True, timeout=600).stdout
    if 'full window' in out or 'P=empty' in out:
        return 0
    for line in out.splitlines():
        if line.startswith('feasible_count'):
            return int(line.split()[1])
    raise RuntimeError(out)


def main():
    p = int(sys.argv[1]); T = int(sys.argv[2]); seed = int(sys.argv[3]); const = int(sys.argv[4])
    kmin = int(sys.argv[5]) if len(sys.argv) > 5 else p + 1
    N = 4 * p - 2
    rng = random.Random(seed)
    stats = {}
    tried = 0
    while tried < T:
        k = rng.randint(kmin, 2 * p - 1)
        cuts = sorted(rng.sample(range(1, N), 2 * k - 1))
        parts = [y - x for x, y in zip([0] + cuts, cuts + [N])]
        r = parts[0::2]; l = parts[1::2]
        if const:
            a = list(r); b = [0] * k
        else:
            a = []; b = []
            for ri in r:
                x = rng.randint(0, ri); a.append(x); b.append(ri - x)
        if not inherited(a, b, l, p):
            continue
        if k > 15:
            continue
        if has_full(a, b, l, p):
            stats.setdefault((k, 'full'), 0); stats[(k, 'full')] += 1
            tried += 1
            continue
        tried += 1
        res = []
        for fam in (1, 2, 3):
            c = run(p, fam, a, b, l)
            res.append(c)
            if c == 0:
                break
        key = (k, 'cert_by_m<=%d' % len(res) if res[-1] == 0 else 'UNCERT_m<=3')
        stats[key] = stats.get(key, 0) + 1
        if res[-1] != 0 or len(res) >= 3:
            print(json.dumps({'p': p, 'a': a, 'b': b, 'l': l, 'res': res}), flush=True)
    for kk in sorted(stats):
        print(kk, stats[kk])


if __name__ == '__main__':
    main()
