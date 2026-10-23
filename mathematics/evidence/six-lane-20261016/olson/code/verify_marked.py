#!/usr/bin/env python3
"""Independent checks of the 'marked linearisation' used in Theorem P (D_2p).

Group D_2p = {(v,e)}: (v,e)(v',e') = (v + e v', e e')  [left convention].
Word: rotations (x,+1), reflections (y,-1).  Cyclic word rotated to END with a
reflection: X_1 f_1 X_2 f_2 ... X_F f_F (X_t = rotations before f_t).
Colouring u_t in {0,1} of gaps t=1..F with u_1 = 0; reflection f_t selected iff
u_t != u_{t+1} (u_{F+1} := u_1).  Marks m_i for rotations; rotation i selected
iff m_i XOR u_{gap(i)}.

Claims checked here by brute force:
 (1) bijection: every selection with an even number of reflections arises from
     exactly one (u with u_1=0, m);
 (2) the ordered product of the selection is (V, +1) with
       V = sum_{t>=2} beta_t u_t + sum_i x_i m_i,
       beta_t = y_{t-1} - y_t - (sum of rotations in X_t);
 (3) size = sum_t [u_t != u_{t+1}] + sum_i (m_i XOR u_gap(i));
 (4) Chevalley-Warning congruence: sum over patterns with V = 0 and size = 0
     (mod p) of (p-1)^{#ones} is 0 mod p, provided deg budget 3(p-1) < #vars
     (checked numerically for small instances, also beyond the budget to see
     where it can fail).
"""
import itertools
import random
import sys


def product(p, letters):
    v, e = 0, 1
    for (x, f) in letters:
        v = (v + e * x) % p
        e *= f
    return v, e


def check_instance(p, word, rng, full=True):
    # word: list of (val, eps) ending with a reflection
    assert word[-1][1] == -1
    F = sum(1 for (_, e) in word if e == -1)
    gap_of = []
    t = 1
    for (x, e) in word:
        if e == 1:
            gap_of.append(t)
        else:
            gap_of.append(None)
            t += 1
    refl_pos = [i for i, (_, e) in enumerate(word) if e == -1]
    rot_pos = [i for i, (_, e) in enumerate(word) if e == 1]
    ys = [word[i][0] for i in refl_pos]  # y_1..y_F
    Xsum = [0] * (F + 2)
    for i in rot_pos:
        Xsum[gap_of[i]] = (Xsum[gap_of[i]] + word[i][0]) % p
    beta = {t: (ys[t - 2] - ys[t - 1] - Xsum[t]) % p for t in range(2, F + 1)}
    nvars = (F - 1) + len(rot_pos)
    seen_sel = {}
    cw_sum = 0
    for bits in itertools.product((0, 1), repeat=nvars):
        u = [None, 0] + list(bits[:F - 1])  # u[1..F]
        m = bits[F - 1:]
        sel = []
        for j, i in enumerate(refl_pos):
            t = j + 1
            un = u[t + 1] if t < F else u[1]
            if u[t] != un:
                sel.append(i)
        for k, i in enumerate(rot_pos):
            if m[k] ^ u[gap_of[i]]:
                sel.append(i)
        sel.sort()
        key = tuple(sel)
        assert key not in seen_sel, 'not injective'
        seen_sel[key] = bits
        val, eps = product(p, [word[i] for i in sel])
        assert eps == 1, 'parity'
        V = (sum(beta[t] * u[t] for t in range(2, F + 1)) + sum(word[i][0] * m[k] for k, i in enumerate(rot_pos))) % p
        assert V == val, ('value formula', V, val)
        size = sum(1 for t in range(1, F + 1) if u[t] != (u[t + 1] if t < F else u[1])) + sum(m[k] ^ u[gap_of[i]] for k, i in enumerate(rot_pos))
        assert size == len(sel), 'size formula'
        if V == 0 and size % p == 0:
            cw_sum += pow(p - 1, sum(bits), p)
    # every even-reflection selection reached?
    n = len(word)
    cnt_even = sum(1 for r in range(n + 1) for S in itertools.combinations(range(n), r)
                   if sum(1 for i in S if word[i][1] == -1) % 2 == 0) if full else None
    if full:
        assert cnt_even == len(seen_sel), ('surjectivity', cnt_even, len(seen_sel))
    return nvars, cw_sum % p


def main():
    rng = random.Random(int(sys.argv[1]) if len(sys.argv) > 1 else 0)
    fails = 0
    for trial in range(300):
        p = rng.choice((3, 5))
        n = rng.randint(3, 10)
        word = [(rng.randrange(p), rng.choice((1, -1))) for _ in range(n - 1)] + [(rng.randrange(p), -1)]
        nvars, cw = check_instance(p, word, rng, full=(n <= 10))
        if 3 * (p - 1) < nvars and cw != 0:
            fails += 1
            print('CW congruence FAILED within budget', p, word, cw)
    print('formula/bijection checks passed; CW-congruence failures within budget:', fails)


if __name__ == '__main__':
    main()
