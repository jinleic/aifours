#!/usr/bin/env python3
"""Aid only: Depth Lemma witness search (proof-RUNS.md Sec. 10 plan).
For run data (constant rho_1, all reflection runs odd, regime B) and each run t, search a
pattern P (t notin P, P cup {t} has m(P)+1 intervals) such that, with U_Q = g_Q(E+), L_Q = g_Q(E-):
  windows of P, P+t, {t} nonempty and not full;
  (A') U_P + U_t + L_{P+t} >= -2 ;  (B') L_P + L_t + U_{P+t} >= p - 2 ;
  derived bound  r_t - 2*(U_{P+t} + L_P + 2 - p) <= 2p - R - 1.
Reports runs t with no witness (would leave the Depth Lemma open for that t).
"""
import random, sys
from collections import Counter
from scl_closure import tables
from sample_famtest import inherited, has_full


def comps(P, k):
    z = [(P >> i) & 1 for i in range(k)]
    return sum(1 for j in range(k) if z[j] and not z[j - 1])


def witness(a, l, p, t, U, L):
    k = len(a); R = sum(a); full = (1 << k) - 1
    T = 1 << t
    nb = T | (1 << ((t - 1) % k)) | (1 << ((t + 1) % k))
    best = None
    def getUL(Q):
        if Q == 0 or Q == full:
            return None
        return U[Q], L[Q]
    Ut, Lt = U[T], L[T]
    if Ut + Lt < 0 or Ut + Lt + 1 >= p:
        return None
    for P in range(1, full + 1):
        if P & nb:
            continue
        if (P | T) == full:
            continue
        UP, LP = U[P], L[P]; UQ, LQ = U[P | T], L[P | T]
        if UP + LP < 0 or UQ + LQ < 0 or UP + LP + 1 >= p or UQ + LQ + 1 >= p:
            continue
        if UP + Ut + LQ < -2 or LP + Lt + UQ < p - 2:
            continue
        bound = a[t] - 2 * (UQ + LP + 2 - p)
        if best is None or bound < best:
            best = bound
            if best <= 2 * p - R - 1:
                return best
    return best


KMAX = int(sys.argv[4]) if len(sys.argv) > 4 else 13
def main():
    p = int(sys.argv[1]); T = int(sys.argv[2]); seed = int(sys.argv[3])
    rng = random.Random(seed); N = 4 * p - 2
    st = Counter(); ex = []
    done = 0
    while done < T:
        k = rng.randint(p + 1, min(2 * p - 3, KMAX)); R = rng.randint(k, 2 * p - 3); F = N - R
        if F < k or (F - k) % 2:
            continue
        c = sorted(rng.sample(range(1, R), k - 1)); r = [y - x for x, y in zip([0] + c, c + [R])]
        l = [1] * k
        for _ in range((F - k) // 2):
            l[rng.randrange(k)] += 2
        a = list(r); b = [0] * k
        if not inherited(a, b, l, p) or has_full(a, b, l, p):
            continue
        done += 1
        U, L = tables(a, b, l, p)
        H = sum(v // 2 for v in l); kappa = p - 1 - H
        for t in range(k):
            w = witness(a, l, p, t, U, L)
            ok = (w is not None and w <= 2 * p - R - 1)
            st['ok' if ok else 'nowit'] += 1
            st['hi_kappa' if R + 2 * k > 4 * p + 3 else 'lo_kappa'] += 1
            if not ok and len(ex) < 6:
                ex.append((a, l, t, w, 'kappa', kappa, 'R+2k', R + 2 * k))
    print(dict(st))
    for e in ex:
        print(e)


if __name__ == '__main__':
    main()
