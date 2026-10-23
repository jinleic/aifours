"""Relaxed MIX_low test (research aid, not a proof).

Given masses d_t (aligned d>=1, anti d=-c<=-1, pair d=0) and p, g, B with
D = sum d = 2p - k + 2g, enumerate integer vectors bh (bh_t = d_t mod 2) with
  BH(Q) >= h(D_Q) := 2 G(D_Q) + 2 - D_Q  for every proper cyclic interval Q,
  G(E) = min(p-1, E-g, floor((E+B)/2)),
  sum bh = k - 2g,
i.e. only the Step-1 interval lower bounds and the total, and report vectors whose
defect set Z0 = {bh <= 0} has Phi(Z0) = sum_{Z0}(d - bh) + 2 m(Z0) <= 2g+1.
"""


def G(E, p, g, B):
    return min(p - 1, E - g, (E + B) // 2)


def h(E, p, g, B):
    return 2 * G(E, p, g, B) + 2 - E


def blocks(Z, k):
    """number of maximal cyclic blocks of the index set Z (a python set)"""
    if not Z:
        return 0
    if len(Z) == k:
        return 1
    return sum(1 for t in Z if (t - 1) % k not in Z)


def phi_Z0(bh, d):
    k = len(d)
    Z = {t for t in range(k) if bh[t] <= 0}
    return sum(d[t] - bh[t] for t in Z) + 2 * blocks(Z, k), Z


def relaxed_search(d, p, g, B, limit=10**6, want_fail=True):
    k = len(d)
    s = k - 2 * g
    D = sum(d)
    assert D == 2 * p - k + 2 * g, (D, 2 * p - k + 2 * g)
    # interval lower bounds for non-wrapping intervals [i..t]
    lo = [h(d[t], p, g, B) for t in range(k)]
    # parity fix of lo
    lo = [lo[t] + ((lo[t] - d[t]) % 2) for t in range(k)]
    suffix_lo = [0] * (k + 1)
    for t in range(k - 1, -1, -1):
        suffix_lo[t] = suffix_lo[t + 1] + lo[t]
    pre_d = [0] * (k + 1)
    for t in range(k):
        pre_d[t + 1] = pre_d[t] + d[t]
    out = []
    count = [0]
    bh = [0] * k
    pre = [0] * (k + 1)

    def check_wrap():
        # all intervals (cyclic) of length 1..k-1
        for i in range(k):
            acc_b = 0
            acc_d = 0
            for L in range(1, k):
                t = (i + L - 1) % k
                acc_b += bh[t]
                acc_d += d[t]
                if acc_b < h(acc_d, p, g, B):
                    return False
        return True

    def rec(t):
        if count[0] >= limit:
            return
        if t == k:
            if pre[k] != s:
                return
            if not check_wrap():
                return
            count[0] += 1
            ph, Z = phi_Z0(bh, d)
            if (not want_fail) or ph <= 2 * g + 1:
                out.append((list(bh), ph))
            return
        rem_lo = suffix_lo[t + 1]
        hi = s - pre[t] - rem_lo
        v = lo[t]
        while v <= hi:
            bh[t] = v
            pre[t + 1] = pre[t] + v
            ok = True
            # non-wrapping intervals ending at t, starting at i >= 0, proper
            for i in range(t, -1, -1):
                if i == 0 and t == k - 1:
                    break
                Bq = pre[t + 1] - pre[i]
                Dq = pre_d[t + 1] - pre_d[i]
                if Bq < h(Dq, p, g, B):
                    ok = False
                    break
            if ok:
                rec(t + 1)
            v += 2
        bh[t] = 0

    rec(0)
    return count[0], out
