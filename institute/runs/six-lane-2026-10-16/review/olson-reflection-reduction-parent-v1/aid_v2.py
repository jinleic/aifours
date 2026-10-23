#!/usr/bin/env python3
"""Parent aid v2 for Theorem K0* (not a proof premise): targeted search among G-words of length 4p-2 with
kappa = 0 (sum floor(l_i/2) = p - 1) and all rotations rho_1 (B = 0, forced by (Z0) after normalisation), built from
block/run shapes that include genuine empty runs. Raw subset DP decides avoidance. A kappa=0 avoider with an empty run
would contradict K0*. Local moves keep kappa, B and every block length: recolour a block, move one rho_1 between runs.
Usage: /usr/bin/python3 -B aid_v2.py OUT.json"""
import json, random, sys, time, hashlib

def mul(a, b, p):
    return ((a[0] + a[1] * b[0]) % p, a[1] * b[1])

def count_id(w, p):
    T = 2 * p
    cnt = [dict() for _ in range(T + 1)]
    cnt[0][(0, 1)] = 1
    for x in w:
        for c in range(T - 1, -1, -1):
            if cnt[c]:
                nxt = cnt[c + 1]
                for g, n in cnt[c].items():
                    h = mul(g, x, p)
                    nxt[h] = nxt.get(h, 0) + n
    return cnt[T].get((0, 1), 0)

def compose(runs, blocks):
    w = []
    for r, (y, l) in zip(runs, blocks):
        w += [(1, 1)] * r + [(y, -1)] * l
    return w

def valid(runs, blocks):
    k = len(blocks)
    return all(runs[i] > 0 or blocks[i - 1][0] != blocks[i][0] for i in range(k)) and sum(runs) >= 1

def random_shape(p, rng):
    while True:
        oF = rng.randint(1, p + 2)
        H = p - 1
        # blocks: oF odd blocks and some even blocks; distribute H pairs
        eF = rng.randint(0, 3)
        k = oF + eF
        if k < 2:
            continue
        pairs = [0] * k
        for _ in range(H):
            pairs[rng.randrange(k)] += 1
        par = [1] * oF + [0] * eF
        rng.shuffle(par)
        ls = []
        ok = True
        for i in range(k):
            l = 2 * pairs[i] + par[i]
            if l == 0:
                ok = False
                break
            ls.append(l)
        if not ok:
            continue
        R = 2 * p - oF
        if R < 1:
            continue
        g = rng.randint(1, min(3, k - 1))
        empties = set(rng.sample(range(k), g))
        nonempty = [i for i in range(k) if i not in empties]
        if R < len(nonempty):
            continue
        runs = [0] * k
        for i in nonempty:
            runs[i] = 1
        for _ in range(R - len(nonempty)):
            runs[rng.choice(nonempty)] += 1
        ys = [rng.randrange(p) for _ in range(k)]
        blocks = [(ys[i], ls[i]) for i in range(k)]
        if valid(runs, blocks):
            return runs, blocks

def main():
    out = sys.argv[1]
    t0 = time.time()
    rng = random.Random(4181018)
    res = {'schema': 'olson-k0star-parent-aid-v2', 'seed': 4181018, 'by_p': {}}
    bad = []
    for p, starts, steps in ((5, 3000, 40), (7, 700, 40)):
        st = {'words_checked': 0, 'kappa0_avoiders': 0, 'kappa0_avoiders_with_empty_run': 0, 'min_count_seen': None}
        seen = set()
        for _ in range(starts):
            runs, blocks = random_shape(p, rng)
            w = compose(runs, blocks)
            assert len(w) == 4 * p - 2 and sum(l // 2 for _, l in blocks) == p - 1
            c = count_id(w, p)
            for _s in range(steps):
                key = (tuple(runs), tuple(blocks))
                if key not in seen:
                    seen.add(key)
                    st['words_checked'] += 1
                    st['min_count_seen'] = c if st['min_count_seen'] is None else min(st['min_count_seen'], c)
                    if c == 0:
                        st['kappa0_avoiders'] += 1
                        if any(r == 0 for r in runs):
                            st['kappa0_avoiders_with_empty_run'] += 1
                            if len(bad) < 10:
                                bad.append({'p': p, 'runs': runs, 'blocks': blocks})
                k = len(blocks)
                r2, b2 = list(runs), list(blocks)
                if rng.random() < 0.5:
                    i = rng.randrange(k)
                    b2[i] = (rng.randrange(p), b2[i][1])
                else:
                    src = [i for i in range(k) if r2[i] >= 1]
                    i = rng.choice(src)
                    j = rng.randrange(k)
                    r2[i] -= 1
                    r2[j] += 1
                if not valid(r2, b2):
                    continue
                c2 = count_id(compose(r2, b2), p)
                if c2 <= c or rng.random() < 0.05:
                    runs, blocks, c = r2, b2, c2
        res['by_p'][str(p)] = st
    res['kappa0_avoiders_with_empty_run_examples'] = bad
    res['status'] = 'PASS' if not bad else 'FAIL'
    res['seconds'] = round(time.time() - t0, 1)
    res['script_sha256'] = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
    with open(out, 'x') as f:
        json.dump(res, f, indent=1)
        f.write('\n')
    print(json.dumps({'status': res['status'], 'seconds': res['seconds'], 'by_p': res['by_p']}))

if __name__ == '__main__':
    main()
