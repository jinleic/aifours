"""Independent cross-check of the R* census (c2): works in the theta domain with Lemma GR's
Ach (../../../code/gr_window.py, imported unchanged) on an explicit word realisation of each
d-vector, instead of the gam/Lemma-H interval system used by rstar.py / rstar_census*.cpp.

realise(d, p): a_t, b_t from d (aligned d -> (d,0), anti -c -> (0,c), pair -> (1,1)); all
reflection runs odd with total F = 4p-2-R (first run takes the excess).
interval_feasible_thetas(d, p): DFS over theta_0..theta_{k-2} (theta_{k-1} = -sum) checking
every proper cyclic interval pattern P with the exact Lemma GR test
  (sum_{i in P} theta_i mod p) notin (Ach(z_P) mod p)        (Lemma WAS),
non-wrapping intervals checked as soon as their thetas are known, the rest at the leaf.
lifts(d, theta, p): chain lifts by the Lemma TL definition from Ach half windows:
  lift(P_j) = the integer in (hi/2, lo/2 + p) congruent to u_{P_j}, x_t = increments,
then phi = d - x.
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'code'))
import gr_window as grw   # noqa: E402


def realise(d, p):
    k = len(d)
    a = [x if x > 0 else (1 if x == 0 else 0) for x in d]
    b = [0 if x > 0 else (1 if x == 0 else -x) for x in d]
    R = sum(a) + sum(b)
    F = 4 * p - 2 - R
    assert F >= k and (F - k) % 2 == 0
    l = [F - (k - 1)] + [1] * (k - 1)
    return a, b, l


def zpat(P, k):
    return tuple(1 if i in P else -1 for i in range(k))


def ach_half(P, a, b, l, p):
    """half window [lo/2, hi/2] of pattern P (Ach is a set of even integers)."""
    lo, hi = grw.ach(zpat(P, len(a)), a, b, l, p)
    return lo // 2, hi // 2   # both even, exact halves; may be empty (lo > hi)


def hits(P, theta, a, b, l, p):
    lo, hi = ach_half(P, a, b, l, p)
    if lo > hi:
        return False
    if hi - lo + 1 >= p:
        return True
    inv2 = pow(2, p - 2, p)
    u = (inv2 * sum(theta[i] for i in P)) % p
    return (u - lo) % p <= hi - lo


def interval_feasible_thetas(d, p):
    k = len(d)
    a, b, l = realise(d, p)
    # precompute all proper cyclic intervals as sets, and their (lo, hi)
    ints = []
    for i in range(k):
        for ln in range(1, k):
            P = frozenset((i + j) % k for j in range(ln))
            ints.append(P)
    ints = list(set(ints))
    win = {P: ach_half(P, a, b, l, p) for P in ints}
    nonwrap_end = {t: [P for P in ints if max(P) == t and all((x in P) for x in range(min(P), t + 1)) and len(P) == t - min(P) + 1] for t in range(k)}
    inv2 = pow(2, p - 2, p)
    out = []
    th = [0] * k

    def bad(P):
        lo, hi = win[P]
        if lo > hi:
            return False
        if hi - lo + 1 >= p:
            return True
        u = (inv2 * sum(th[i] for i in P)) % p
        return (u - lo) % p <= hi - lo

    def rec(t):
        if t == k - 1:
            th[t] = (-sum(th[:t])) % p
            if all(not bad(P) for P in ints):
                out.append(tuple(th))
            return
        for v in range(p):
            th[t] = v
            if any(bad(P) for P in nonwrap_end[t] if max(P) < k - 1):
                continue
            rec(t + 1)
    rec(0)
    return out


def lifts(d, theta, p):
    k = len(d)
    a, b, l = realise(d, p)
    inv2 = pow(2, p - 2, p)
    V = [0] * (k + 1)
    V[k] = p
    for j in range(1, k):
        P = set(range(j))
        lo, hi = ach_half(P, a, b, l, p)
        u = (inv2 * sum(theta[i] for i in P)) % p
        # unique integer in (hi, lo + p) congruent to u
        c = [v for v in range(hi + 1, lo + p) if (v - u) % p == 0]
        assert len(c) == 1, (d, theta, j, lo, hi, c)
        V[j] = c[0]
    x = [V[t + 1] - V[t] for t in range(k)]
    return tuple(d[t] - x[t] for t in range(k))
