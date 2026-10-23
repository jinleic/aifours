#!/usr/bin/env python3
"""Constructive check of the RIGID-CASE argument for D_2p (left convention).

Rigid word: cyclic word over {rho_1, rho_-1, sigma_0}.  Claimed proof:
  (a) F >= 2p: select 2p reflections (sigma_0^{2p} = 1);
  (b) some rotation-run contains >= p copies of rho_1 or of rho_-1: Doubling
      Lemma applies (p equal rotations in one gap sum to 0) -- not constructed
      here, only flagged;
  (c) otherwise all run nets |d_i| <= p-1 and F <= 2p-1; take the natural
      flip pattern z* (flip at odd sigma-runs; one forced mismatch at the
      closure if the number of odd sigma-runs is odd), then, by the discrete
      intermediate value step, toggle the flips at sigma-run k and sigma-run j'
      to get |D| + delta <= 2p-1; then build an explicit selection:
      choose c_i sigma's per run (parity f_i), A eff+ and A eff- rotations with
      2A + sum c_i = 2p.
The constructed selection is multiplied out in the group and must be the identity.
"""
import random
import sys


def mul_word(p, letters):
    v, e = 0, 1
    for (x, f) in letters:
        v = (v + e * x) % p
        e *= f
    return v, e


def construct(p, word):
    N = len(word)
    a = sum(1 for x, e in word if e == 1 and x == 1)
    b = sum(1 for x, e in word if e == 1 and x == p - 1)
    F = N - a - b
    idx_F = [i for i, (x, e) in enumerate(word) if e == -1]
    if F >= 2 * p:
        return ('F', idx_F[:2 * p])
    if F == 0:
        return ('noF', None)
    # rotate to start with an R-run (after a sigma-run)
    starts = [i for i in range(N) if word[i][1] == 1 and word[i - 1][1] == -1]
    if not starts:
        return ('noRrun', None)
    s0 = starts[0]
    order = [(s0 + j) % N for j in range(N)]
    runs = []  # list of (type, [indices])
    for i in order:
        tp = 'R' if word[i][1] == 1 else 'S'
        if runs and runs[-1][0] == tp:
            runs[-1][1].append(i)
        else:
            runs.append([tp, [i]])
    Rr = [r[1] for r in runs if r[0] == 'R']
    Sr = [r[1] for r in runs if r[0] == 'S']
    k = len(Rr)
    for r in Rr:
        if sum(1 for i in r if word[i][0] == 1) >= p or sum(1 for i in r if word[i][0] == p - 1) >= p:
            return ('doubling', None)
    d = [sum(1 if word[i][0] == 1 else -1 for i in r) for r in Rr]
    ell = [len(s) for s in Sr]
    e = [l % 2 for l in ell]
    # natural flips with closure fix
    f = e[:]
    if sum(f) % 2:
        f[k - 1] ^= 1
    def zpat(fl):
        z = [1] * k
        for i in range(k - 1):
            z[i + 1] = z[i] * (-1 if fl[i] else 1)
        return z
    def cost(fl):
        z = zpat(fl)
        D = sum(z[i] * d[i] for i in range(k))
        delta = sum(1 for i in range(k) if fl[i] != e[i])
        return abs(D) + delta, z, D, delta
    best = cost(f)
    # IVT deviations: toggle flips at sigma-run k-1 (closure) and sigma-run j
    for j in range(k - 1):
        g = f[:]
        g[k - 1] ^= 1
        g[j] ^= 1
        c = cost(g)
        if c[0] < best[0]:
            best = c
            f_best = g
    fl = f if best == cost(f) else f_best
    Phi, z, D, delta = cost(fl)
    if Phi > 2 * p - 1:
        return ('FAIL', (Phi, d, ell))
    # build selection: c_i sigma's with parity fl[i]
    Cmin = sum(fl)
    Cmax = sum(ell[i] if ell[i] % 2 == fl[i] else ell[i] - 1 for i in range(k))
    R = a + b
    Ep = sum((sum(1 for i in Rr[t] if word[i][0] == 1) if z[t] == 1 else sum(1 for i in Rr[t] if word[i][0] == p - 1)) for t in range(k))
    Em = R - Ep
    lo = (2 * p - Cmax) // 2 if (2 * p - Cmax) % 2 == 0 else None
    A = None
    for cand in range(min(Ep, Em), -1, -1):
        C = 2 * p - 2 * cand
        if Cmin <= C <= Cmax and (C - Cmin) % 2 == 0:
            A = cand
            break
    if A is None:
        return ('NOALLOC', (Phi, Ep, Em, Cmin, Cmax))
    C = 2 * p - 2 * A
    c = list(fl)
    extra = C - Cmin
    for i in range(k):
        cap = (ell[i] if ell[i] % 2 == fl[i] else ell[i] - 1) - c[i]
        add = min(cap, extra)
        add -= add % 2
        c[i] += add
        extra -= add
    assert extra == 0
    sel = []
    for i in range(k):
        sel += Sr[i][:c[i]]
    # eff+ / eff- rotations
    plus, minus = [], []
    for t in range(k):
        for i in Rr[t]:
            eff = (1 if word[i][0] == 1 else -1) * z[t]
            (plus if eff == 1 else minus).append(i)
    sel += plus[:A] + minus[:A]
    sel.sort()
    return ('OK', sel)


def main():
    rng = random.Random(int(sys.argv[2]) if len(sys.argv) > 2 else 0)
    p = int(sys.argv[1])
    trials = int(sys.argv[3]) if len(sys.argv) > 3 else 20000
    N = 4 * p - 1
    st = {}
    for _ in range(trials):
        word = []
        while len(word) < N:
            if rng.random() < 0.5:
                word += [(rng.choice([1, p - 1]), 1) for _ in range(rng.choice((1, 2, 3, p - 1, p + 1)))]
            else:
                word += [(0, -1)] * rng.choice((1, 2, 3, 5))
        word = word[:N]
        kind, data = construct(p, word)
        st[kind] = st.get(kind, 0) + 1
        if kind in ('F', 'OK'):
            sel = data
            assert len(sel) == 2 * p and len(set(sel)) == 2 * p
            v, e = mul_word(p, [word[i] for i in sel])
            assert (v, e) == (0, 1), ('not identity', word, sel, v, e)
        if kind in ('FAIL', 'NOALLOC'):
            print(kind, data, word)
    print('p', p, st)


if __name__ == '__main__':
    main()
