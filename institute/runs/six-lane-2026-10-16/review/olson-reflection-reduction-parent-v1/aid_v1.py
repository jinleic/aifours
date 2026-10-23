#!/usr/bin/env python3
"""Parent aid for K0star-r1 / RED-r1 (olson-reflection-reduction-review-v1 snapshot). NOT a proof premise.
Independent re-implementation (no worker code): raw subset DP for identity 2p-subwords in D_2p, compared with
Lemma H0 (00:49-59) on many words with and without empty runs; Spec checks of FUS (both printed forms and the
Codex correction), SL; avoidance checks of TR (both directions), SL (both directions), PM0/FUS (one-way);
K0* conclusion (kappa=0 avoiders of length 4p-2 with rotations in {rho_1, rho_-1} have g=0) on every avoider found.
Usage: /usr/bin/python3 -B aid_v1.py OUT.json"""
import json, random, sys, time, hashlib, platform

def mul(a, b, p):
    return ((a[0] + a[1] * b[0]) % p, a[1] * b[1])

def spec(w, p):
    S = {(0, (0, 1))}
    for x in w:
        S |= {(c + 1, mul(g, x, p)) for (c, g) in S}
    return S

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

def decompose(w, p):
    N = len(w)
    if not any(x[1] == -1 for x in w):
        return None
    s = None
    for i in range(N):
        prev = w[i - 1]
        if prev[1] == -1 and (w[i][1] == 1 or w[i][0] != prev[0]):
            s = i
            break
    if s is None:
        return None
    ww = w[s:] + w[:s]
    runs, blocks = [], []
    a = b = 0
    last_block = False
    for x in ww:
        if x[1] == 1:
            if x[0] == 1:
                a += 1
            elif x[0] == p - 1:
                b += 1
            else:
                raise ValueError('rotation outside {rho_1, rho_-1}')
            last_block = False
        else:
            if last_block and blocks[-1][0] == x[0]:
                blocks[-1][1] += 1
            else:
                runs.append((a, b))
                a = b = 0
                blocks.append([x[0], 1])
            last_block = True
    assert a == 0 and b == 0 and last_block and len(runs) == len(blocks)
    k = len(blocks)
    for i in range(k):
        if runs[i] == (0, 0):
            assert blocks[i - 1][0] != blocks[i][0]
    return runs, [tuple(bl) for bl in blocks]

def compose(runs, blocks, p):
    w = []
    for (a, b), (y, l) in zip(runs, blocks):
        w += [(1, 1)] * a + [(p - 1, 1)] * b + [(y, -1)] * l
    return w

def h0_avoids(runs, blocks, p):
    k = len(blocks)
    A = sum(r[0] for r in runs)
    B = sum(r[1] for r in runs)
    H = sum(l // 2 for _, l in blocks)
    kappa = p - 1 - H
    inv2 = (p + 1) // 2
    theta = [(blocks[i - 1][0] - blocks[i][0]) % p for i in range(k)]
    d = [r[0] - r[1] for r in runs]
    even = [l % 2 == 0 for _, l in blocks]

    def inI(u, lo, hi):
        if hi < lo:
            return False
        if hi - lo + 1 >= p:
            return True
        return lo + ((u - lo) % p) <= hi

    if inI(0, -min(p, A - kappa - 1, A // 2), min(p, B - kappa - 1, B // 2)):
        return False
    full = (1 << k) - 1
    lam = {}

    def lam_of(mask):
        if mask not in lam:
            inP = [(mask >> i) & 1 for i in range(k)]
            m = sum(1 for i in range(k) if inP[i] and not inP[i - 1])
            beta = sum(1 for j in range(k) if inP[j] != inP[(j + 1) % k] and even[j])
            DP = sum(d[i] for i in range(k) if inP[i])
            lam[mask] = min(p - m + 1, DP + B - kappa + m - beta, (DP + B) // 2 + 1)
        return lam[mask]

    for mask in range(1, full):
        u = (inv2 * sum(theta[i] for i in range(k) if (mask >> i) & 1)) % p
        if inI(u, 1 - lam_of(full ^ mask), lam_of(mask) - 1):
            return False
    return True

def letters(p, refl_vals):
    return [(1, 1), (p - 1, 1)] + [(y, -1) for y in refl_vals]

def main():
    out = sys.argv[1]
    t0 = time.time()
    rng = random.Random(20261018)
    res = {'schema': 'olson-reflection-parent-aid-v1', 'python': platform.python_version(), 'seed': 20261018}
    # ---------------- Spec lemmas
    fus = {'first_form_checked': 0, 'first_form_fail': [], 'printed_second_checked': 0, 'printed_second_fail_examples': [],
           'printed_second_fail_count': 0, 'corrected_second_checked': 0, 'corrected_second_fail': []}
    sl = {'checked': 0, 'fail': [], 'class_checked': 0, 'class_fail': []}
    for p in (5, 7):
        for u in range(p):
            for v in range(p):
                if u == v:
                    continue
                su, sv = (u, -1), (v, -1)
                for l in range(1, 8):
                    for lp in (2, 4, 6):
                        big = spec([su] * (l + lp), p)
                        if not big <= spec([su] * l + [sv] * lp, p):
                            fus['first_form_fail'].append([p, u, v, l, lp])
                        fus['first_form_checked'] += 1
                        if not spec([sv] * (lp + l), p) <= spec([sv] * lp + [su] * l, p):
                            fus['printed_second_fail_count'] += 1
                            if len(fus['printed_second_fail_examples']) < 5:
                                fus['printed_second_fail_examples'].append([p, u, v, l, lp])
                        fus['printed_second_checked'] += 1
                        if not spec([su] * (lp + l), p) <= spec([sv] * lp + [su] * l, p):
                            fus['corrected_second_fail'].append([p, u, v, l, lp])
                        fus['corrected_second_checked'] += 1
                classes = {}
                for a in range(1, 9):
                    for b in range(1, 9):
                        S = frozenset(spec([su] * a + [sv] * b, p))
                        key = (a // 2 + b // 2, a % 2, b % 2)
                        if key in classes and classes[key] != S:
                            sl['class_fail'].append([p, u, v, a, b])
                        classes.setdefault(key, S)
                        sl['class_checked'] += 1
                        if a >= 3:
                            if S != frozenset(spec([su] * (a - 2) + [sv] * (b + 2), p)):
                                sl['fail'].append([p, u, v, a, b])
                            sl['checked'] += 1
    res['FUS'] = fus
    res['SL'] = sl
    # ---------------- H0 vs raw DP, moves, K0*
    h0 = {'compared': 0, 'mismatch': [], 'avoiders': 0, 'avoiders_with_empty_runs': 0, 'by_p': {}}
    k0 = {'kappa0_avoiders_len_4p_2': 0, 'kappa0_with_empty_run': [], 'kappa_hist_avoiders_with_empty_runs': {}}
    mv = {'TR_checked': 0, 'TR_fail': [], 'SLword_checked': 0, 'SLword_fail': [], 'PM0_checked': 0, 'PM0_fail': [],
          'FUS_checked': 0, 'FUS_fail': [], 'FUS_double_odd_seen': 0}
    seen = set()

    def examine(w, p):
        key = (p, tuple(w))
        if key in seen:
            return None
        seen.add(key)
        dec = decompose(w, p)
        if dec is None:
            return None
        runs, blocks = dec
        if len(blocks) > 11:
            return None
        avoid = count_id(w, p) == 0
        pred = h0_avoids(runs, blocks, p)
        h0['compared'] += 1
        bp = h0['by_p'].setdefault(str(p), {'compared': 0, 'avoiders': 0})
        bp['compared'] += 1
        if pred != avoid and len(h0['mismatch']) < 20:
            h0['mismatch'].append({'p': p, 'w': w, 'dp_avoid': avoid, 'h0_avoid': pred})
        g = sum(1 for r in runs if r == (0, 0))
        if avoid:
            h0['avoiders'] += 1
            bp['avoiders'] += 1
            if g:
                h0['avoiders_with_empty_runs'] += 1
            if len(w) == 4 * p - 2:
                kappa = p - 1 - sum(l // 2 for _, l in blocks)
                if kappa == 0:
                    k0['kappa0_avoiders_len_4p_2'] += 1
                    if g and len(k0['kappa0_with_empty_run']) < 20:
                        k0['kappa0_with_empty_run'].append({'p': p, 'w': w})
                if g:
                    kh = k0['kappa_hist_avoiders_with_empty_runs']
                    kh[str((p, kappa))] = kh.get(str((p, kappa)), 0) + 1
        return runs, blocks, avoid, g

    def moves(runs, blocks, avoid, p):
        k = len(blocks)
        # TR: exact both ways
        srcs = [i for i in range(k) if runs[i][0] >= 1 and runs[i][1] >= 1]
        if srcs and k >= 2:
            s = rng.choice(srcs)
            t = rng.choice([i for i in range(k) if i != s])
            r2 = list(runs)
            r2[s] = (runs[s][0] - 1, runs[s][1] - 1)
            r2[t] = (runs[t][0] + 1, runs[t][1] + 1)
            a2 = count_id(compose(r2, blocks, p), p) == 0
            mv['TR_checked'] += 1
            if a2 != avoid:
                mv['TR_fail'].append({'p': p, 'runs': runs, 'blocks': blocks, 's': s, 't': t})
        # SL on a pair of blocks separated by an empty run: (a,b) -> (a-2,b+2), exact both ways
        for j in range(k):
            jn = (j + 1) % k
            if k >= 2 and runs[jn] == (0, 0) and blocks[j][1] >= 3:
                b2 = list(blocks)
                b2[j] = (blocks[j][0], blocks[j][1] - 2)
                b2[jn] = (blocks[jn][0], blocks[jn][1] + 2)
                a2 = count_id(compose(runs, b2, p), p) == 0
                mv['SLword_checked'] += 1
                if a2 != avoid:
                    mv['SLword_fail'].append({'p': p, 'runs': runs, 'blocks': blocks, 'j': j})
                break
        if not avoid:
            return
        # PM0 across an even block whose neighbouring runs are both nonempty (one-way)
        for j in range(k):
            jn = (j + 1) % k
            if k >= 2 and blocks[j][1] % 2 == 0:
                r2, b2 = [], []
                merged = (runs[j][0] + runs[jn][0], runs[j][1] + runs[jn][1])
                for i in range(k):
                    if i == j:
                        continue
                    if i == jn:
                        r2.append(merged)
                        b2.append((blocks[jn][0], blocks[jn][1] + blocks[j][1]))
                    else:
                        r2.append(runs[i])
                        b2.append(blocks[i])
                if jn == 0:  # merged run moved to the front is fine cyclically
                    pass
                w2 = compose(r2, b2, p)
                mv['PM0_checked'] += 1
                if count_id(w2, p) != 0:
                    mv['PM0_fail'].append({'p': p, 'runs': runs, 'blocks': blocks, 'j': j})
                break
        # FUS at a genuine empty run next to an even block (one-way)
        for t in range(k):
            if runs[t] != (0, 0) or k < 2:
                continue
            left, right = (t - 1) % k, t
            for ev, other in ((left, right), (right, left)):
                if blocks[ev][1] % 2 == 0:
                    b2 = list(blocks)
                    b2[ev] = (blocks[other][0], blocks[ev][1])
                    w2 = compose(runs, b2, p)
                    mv['FUS_checked'] += 1
                    if count_id(w2, p) != 0:
                        mv['FUS_fail'].append({'p': p, 'runs': runs, 'blocks': blocks, 'even': ev, 'other': other})
                    d2 = decompose(w2, p)
                    if d2 and sum(l // 2 for _, l in d2[1]) > sum(l // 2 for _, l in blocks):
                        mv['FUS_double_odd_seen'] += 1
                    return
            return

    for p, N_list, budget in ((5, (18, 14, 16, 20), 5200), (7, (26, 22), 900)):
        for it in range(budget):
            N = rng.choice(N_list)
            nv = rng.choice((2, 2, 3, p))
            vals = rng.sample(range(p), nv)
            L = letters(p, vals)
            q = rng.random()
            w = [(1, 1) if rng.random() < q * 0.7 else ((p - 1, 1) if rng.random() < 0.15 else (rng.choice(vals), -1))
                 for _ in range(N)]
            if not any(x[1] == -1 for x in w):
                w[0] = (vals[0], -1)
            c = count_id(w, p)
            steps = 0
            while steps < 60:
                info = examine(w, p)
                if info is not None:
                    moves(info[0], info[1], info[2], p)
                if c == 0 and rng.random() < 0.5:
                    break
                i = rng.randrange(N)
                x = rng.choice(L)
                if x == w[i]:
                    steps += 1
                    continue
                w2 = w[:i] + [x] + w[i + 1:]
                if not any(y[1] == -1 for y in w2):
                    steps += 1
                    continue
                c2 = count_id(w2, p)
                if c2 <= c or rng.random() < 0.05:
                    w, c = w2, c2
                steps += 1
    res['H0'] = h0
    res['K0star'] = k0
    res['moves'] = mv
    res['seconds'] = round(time.time() - t0, 1)
    ok = (not fus['first_form_fail'] and fus['printed_second_fail_count'] > 0 and not fus['corrected_second_fail']
          and not sl['fail'] and not sl['class_fail'] and not h0['mismatch'] and not k0['kappa0_with_empty_run']
          and not mv['TR_fail'] and not mv['SLword_fail'] and not mv['PM0_fail'] and not mv['FUS_fail'])
    res['status'] = 'PASS' if ok else 'FAIL'
    res['script_sha256'] = hashlib.sha256(open(__file__, 'rb').read()).hexdigest()
    with open(out, 'x') as f:
        json.dump(res, f, indent=1, default=list)
        f.write('\n')
    print(json.dumps({'status': res['status'], 'seconds': res['seconds'], 'compared': h0['compared'],
                      'avoiders': h0['avoiders'], 'avoiders_empty': h0['avoiders_with_empty_runs'],
                      'kappa0': k0['kappa0_avoiders_len_4p_2'], 'printed_second_fail_count': fus['printed_second_fail_count'],
                      'TR': mv['TR_checked'], 'SL': mv['SLword_checked'], 'PM0': mv['PM0_checked'], 'FUS': mv['FUS_checked']}))

if __name__ == '__main__':
    main()
