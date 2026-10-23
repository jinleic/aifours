"""R* census tools for MIX_low (c2/README.md Sec. 2 representation).  Research aid.

phi_t = d_t - x_t (x = interval-chain lifts), sum phi = p - k + 2g, and for every proper
cyclic interval Q:  phi(Q) <= gam(D_Q),  gam(E) = max(E - p, g - 1, floor((E - B - 1)/2)).
"""
import itertools


def gam(E, p, g, B):
    return max(E - p, g - 1, (E - B - 1) // 2)


def Gm(m, E, p, g, B):
    return min(p - m, E - g + m - 1, (E + B) // 2)


def params(d, p):
    """(k, A, B, D, g) for a pure/pair-normalised d-vector, or None if not MIX_low."""
    k = len(d)
    A = sum(x for x in d if x > 0) + sum(1 for x in d if x == 0)
    B = sum(-x for x in d if x < 0) + sum(1 for x in d if x == 0)
    D = A - B
    if B < 1 or k > p:
        return None
    t = D - 2 * p + k
    if t % 2 or t < 2:
        return None
    g = t // 2
    if 2 * g + B > k - 1:
        return None
    return k, A, B, D, g


def canon(d):
    k = len(d)
    return min(tuple(d[i:] + d[:i]) for i in range(k))


def enum_d(p, kmin=4, kmax=None):
    """all rotation-canonical MIX_low d-vectors (pure aligned d>=1, anti d<=-1, pair d=0)."""
    kmax = kmax or p
    out = []
    for k in range(kmin, kmax + 1):
        Bmax = k - 3
        Amax = 2 * p - 1
        cur = []

        def rec(i, A, B):
            if i == k:
                d = list(cur)
                if canon(d) != tuple(d):
                    return
                if params(d, p) is not None:
                    out.append(tuple(d))
                return
            # aligned
            for x in range(1, Amax - A + 1):
                cur.append(x); rec(i + 1, A + x, B); cur.pop()
            if B + 1 <= Bmax and A + 1 <= Amax:
                cur.append(0); rec(i + 1, A + 1, B + 1); cur.pop()
            for c in range(1, Bmax - B + 1):
                cur.append(-c); rec(i + 1, A, B + c); cur.pop()
        rec(0, 0, 0)
    return out


def phi_solutions(d, p, limit=None):
    """all integer phi with sum p-k+2g and phi(Q) <= gam(D_Q) for all proper cyclic Q."""
    k, A, B, D, g = params(d, p)
    tot = p - k + 2 * g
    pre = [0] * (k + 1)
    for t in range(k):
        pre[t + 1] = pre[t] + d[t]
    # non-wrapping interval [i..t] (0<=i<=t<=k-1, not (0,k-1)): lo <= phi <= hi
    hi = [[None] * k for _ in range(k)]
    lo = [[None] * k for _ in range(k)]
    for i in range(k):
        for t in range(i, k):
            if i == 0 and t == k - 1:
                continue
            E = pre[t + 1] - pre[i]
            hi[i][t] = gam(E, p, g, B)
            lo[i][t] = tot - gam(D - E, p, g, B)
    sols = []
    phi = [0] * k
    pp = [0] * (k + 1)

    def rec(t):
        if limit is not None and len(sols) >= limit:
            return
        if t == k - 1:
            v = tot - pp[t]
            for i in range(1, k):
                s = pp[t] - pp[i] + v
                if s > hi[i][t] or s < lo[i][t]:
                    return
            phi[t] = v
            sols.append(tuple(phi))
            return
        L, H = -10 ** 9, 10 ** 9
        for i in range(t + 1):
            base = pp[t] - pp[i]
            L = max(L, lo[i][t] - base)
            H = min(H, hi[i][t] - base)
        for v in range(L, H + 1):
            phi[t] = v
            pp[t + 1] = pp[t] + v
            rec(t + 1)
    rec(0)
    return sols


def blocks(S, k):
    if not S:
        return 0
    if len(S) == k:
        return 1
    return sum(1 for t in S if (t - 1) % k not in S)


def classify(d, phi, p):
    k, A, B, D, g = params(d, p)
    bh = [d[t] - 2 * phi[t] for t in range(k)]
    Z = {t for t in range(k) if bh[t] <= 0}
    m = blocks(Z, k)
    Phi = 2 * sum(phi[t] for t in Z) + 2 * m
    Yal = sum(1 for t in range(k) if t not in Z and d[t] >= 1)
    aZ = sum(d[t] - 1 for t in Z)
    rstar = (Phi <= 2 * g + 1) and (Yal + aZ <= 2)
    return dict(bh=bh, Z=Z, m=m, Phi=Phi, Yal=Yal, aZ=aZ, rstar=rstar, g=g, B=B, k=k, D=D)


def window(P, d, p, g, B, D):
    k = len(d)
    m = blocks(P, k)
    DP = sum(d[t] for t in P)
    return -Gm(m, D - DP, p, g, B), Gm(m, DP, p, g, B), m


def kills(P, d, phi, p, g, B, D):
    lo, hi, m = window(P, d, p, g, B, D)
    if hi < lo:
        return False
    if hi - lo + 1 >= p:
        return True
    xP = sum(d[t] - phi[t] for t in P)
    return (xP - lo) % p <= hi - lo


def exact_kill(d, phi, p):
    """first killing proper pattern (bitmask order), or None (exact mod-p test)."""
    k, A, B, D, g = params(d, p)
    for mask in range(1, 1 << (k - 1)):   # complement symmetry: patterns without run k-1
        P = {t for t in range(k) if mask >> t & 1}
        if kills(P, d, phi, p, g, B, D):
            return P
    return None
