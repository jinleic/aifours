#!/usr/bin/env python3
"""Obligation S (sharpness / falsification), rotation slice, 2026-10-18.

Question S(p, N): is there a word of length N over D_(2p) with no identity 2p-subword whose rotation letters are
NOT contained in one {rho_x, rho_-x}, x != 0 ("non-rigid")?  N = 4p-2 is ROT(p) itself (a hit would be a ROT
counterexample, to be re-verified independently); N = 4p-3 asks whether ROT is sharp in the length.
Method: stochastic local search minimising the EXACT number of identity 2p-subwords (counting raw ordered-product
DP, states (size, sign, value) with integer counts; no window formula), restricted to non-rigid words.
A miss is UNKNOWN (never evidence of absence).  Every hit is re-checked by rawdp.witness (bitmask DP) and the
unchanged olson/code/was_verify.py dp_has before being printed as a JSON line.
Controls (mode 'control'): the same search WITHOUT the non-rigid restriction must find avoiders (positive control
of the search), and the count DP must be > 0 on words mutated to contain an explicit identity subword.
Usage: sharp_search_v1.py MODE p N seed iters restarts
"""
import json, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OLSON = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, HERE)
sys.path.insert(1, os.path.join(OLSON, 'code'))
import rawdp  # noqa: E402
import was_verify  # noqa: E402


def count_identity(word, p):
    size = 2 * p
    # cnt[c][ei][v]
    cnt = [[[0] * p for _ in range(2)] for _ in range(size + 1)]
    cnt[0][0][0] = 1
    for kind, val in word:
        for c in range(size - 1, -1, -1):
            for ei in (0, 1):
                row = cnt[c][ei]
                if not any(row):
                    continue
                e = 1 if ei == 0 else -1
                tei = ei if kind == 'r' else 1 - ei
                tgt = cnt[c + 1][tei]
                sh = (e * val) % p
                for v in range(p):
                    if row[v]:
                        tgt[(v + sh) % p] += row[v]
    return cnt[size][0][0]


def nonrigid(word, p):
    vals = {v % p for k, v in word if k == 'r'}
    if 0 in vals:
        return True
    if not vals:
        return False
    x = next(iter(vals))
    return not vals <= {x, (-x) % p}


def search(p, N, rng, iters, need_nonrigid):
    letters = [(k, v) for k in 'rs' for v in range(p)]
    while True:
        w = [rng.choice(letters) for _ in range(N)]
        if not need_nonrigid or nonrigid(w, p):
            break
    cur = count_identity(w, p)
    for it in range(iters):
        if cur == 0:
            return w, it
        w2 = list(w)
        j = rng.randrange(N)
        if rng.random() < 0.2 and N >= 2:
            # move a letter (keeps the multiset)
            i = rng.randrange(N)
            x = w2.pop(i)
            w2.insert(j, x)
        else:
            w2[j] = rng.choice(letters)
        if need_nonrigid and not nonrigid(w2, p):
            continue
        c2 = count_identity(w2, p)
        if c2 <= cur or rng.random() < 0.01:
            w, cur = w2, c2
    return None, iters


def verify(w, p):
    a = rawdp.witness(w, p, 2 * p) is None
    b = not was_verify.dp_has([('R' if k == 'r' else 'F', v) for k, v in w], p)
    return a and b


def main():
    mode, p, N, seed, iters, restarts = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), \
        int(sys.argv[5]), int(sys.argv[6])
    rng = random.Random(seed)
    hits = 0
    found_rigid = 0
    for r in range(restarts):
        w, it = search(p, N, rng, iters, need_nonrigid=(mode == 'search'))
        if w is None:
            continue
        ok = verify(w, p)
        nr = nonrigid(w, p)
        hits += 1
        found_rigid += (not nr)
        print(json.dumps({'mode': mode, 'p': p, 'N': N, 'restart': r, 'iters': it, 'verified_avoider': ok,
                          'nonrigid': nr, 'word': rawdp.fmt(w)}), flush=True)
    neg_ok = None
    if mode == 'control':
        # negative control: force an explicit identity 2p-subword into random words; count must be > 0
        neg_ok = 0
        for _ in range(50):
            w = [(rng.choice('rs'), rng.randrange(p)) for _ in range(N)]
            idx = sorted(rng.sample(range(N), 2 * p))
            v, e = rawdp.product(w, idx[:-1], p)
            w[idx[-1]] = ('r' if e == 1 else 's', (-e * v) % p)
            assert rawdp.product(w, idx, p) == (0, 1)
            neg_ok += count_identity(w, p) > 0
    print(json.dumps({'summary': 1, 'mode': mode, 'p': p, 'N': N, 'seed': seed, 'iters': iters,
                      'restarts': restarts, 'hits': hits, 'rigid_hits': found_rigid, 'neg_controls_ok_of_50': neg_ok}),
          flush=True)


if __name__ == '__main__':
    main()
