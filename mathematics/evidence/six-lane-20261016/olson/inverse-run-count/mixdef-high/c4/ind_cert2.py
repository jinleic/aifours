# ind_cert2.py -- c4 README Sec. 5, scheme IND with a free seed (aid only [F]).  Same arcs as ind_cert.py.
# For a seed size s (1 <= s <= N-1) with A_s := [L_(s+1) - U_s, U_(s+1) - L_s] of width < p, every value u_t has a unique
# lift x_t in A_s (u_t = u_(S+t) - u_S with |S| = s, S+t subset of T).  The lift set is shrunk to the integers y in A_s
# whose residue lies in A_j (mod p) for every j and in the singleton allowed arc G_1 (mod p); [lo_1, hi_1] := its hull.
# Size chain j -> j+1 (j >= 1): [lo_j + lo_1, hi_j + hi_1] inside [U_(j+1) + 1 - p, p + L_(j+1) - 1] gives
# X_S in [L_(j+1), U_(j+1)] for all (j+1)-subsets (Claim of Lemma BC); lo_(j+1) = max(L_(j+1), lo_j + lo_1), etc.
# (For j = 1 the singleton bounds are [lo_1, hi_1], NOT [L_1, U_1].)  Balanced-profile exclusion as in ind_cert.py,
# with the size-1 constraint replaced by the lift range.  Reports, per (p, kB), the seeds that succeed.
# Usage: python3 -B ind_cert2.py PMIN PMAX [details]
import sys
PMIN, PMAX = int(sys.argv[1]), int(sys.argv[2]); DET = len(sys.argv) > 3
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def arcs(p, a, N):
    L = [None] * (N + 2); U = [None] * (N + 2)
    for j in range(1, N + 1):
        L[j] = min(p - j + 1, 2 * j - a, (j + 1) // 2 + 1)
        U[j] = p - min(p - j + 1, p - 1, (p + a - j) // 2 + 1)
    return L, U
def try_seed(p, a, N, L, U, s, resid_ok):
    lo_s, hi_s = L[s + 1] - U[s], U[s + 1] - L[s]
    if hi_s - lo_s + 1 > p: return None
    lifts = [y for y in range(lo_s, hi_s + 1) if resid_ok[y % p]]
    if not lifts: return ('empty', None)
    lo1, hi1 = min(lifts), max(lifts)
    lo = {1: lo1}; hi = {1: hi1}; Jc = 1
    for j in range(1, N):
        A, Bv = lo[j] + lo1, hi[j] + hi1
        if A >= U[j + 1] + 1 - p and Bv <= p + L[j + 1] - 1:
            lo[j + 1] = max(L[j + 1], A); hi[j + 1] = min(U[j + 1], Bv); Jc = j + 1
            if lo[j + 1] > hi[j + 1]: return ('INFEASIBLE-range', (lo1, hi1, Jc))
        else: break
    Xlo, Xhi = N * lo1, N * hi1
    if Jc == N: Xlo, Xhi = max(Xlo, lo[N]), min(Xhi, hi[N])
    for X in range(Xlo, Xhi + 1):
        q, r = divmod(X, N)
        if q < lo1 or (r > 0 and q + 1 > hi1): continue
        ok = True
        for j in range(2, min(Jc, N - 1) + 1):
            sj = j * q + max(0, j - (N - r)); tj = j * q + min(j, r)
            if sj < L[j] or tj > U[j]: ok = False; break
        if ok: return ('survivor', (lo1, hi1, Jc, X, q, r))
    return ('INFEASIBLE', (lo1, hi1, Jc))
def analyse(p, a, N=None):
    if N is None: N = (p + a + 1) // 2
    L, U = arcs(p, a, N)
    resid_ok = [True] * p
    for v in range(p):
        if not any((v - y) % p == 0 for y in range(L[1], U[1] + 1)): resid_ok[v] = False
        for j in range(1, N):
            lo, hi = L[j + 1] - U[j], U[j + 1] - L[j]
            if hi - lo + 1 >= p: continue
            if not any((v - y) % p == 0 for y in range(lo, hi + 1)): resid_ok[v] = False; break
    good = []; info = {}
    for s in range(1, N):
        r = try_seed(p, a, N, L, U, s, resid_ok)
        if r is None: continue
        info[s] = r
        if r[0].startswith('INFEASIBLE'): good.append(s)
    return good, info
for p in range(PMIN, PMAX + 1):
    if not isprime(p) or p < 11: continue
    beyond = [a for a in range(1, p - 3) if 3 * a >= p + 5]
    ok, bad = [], []
    for a in beyond:
        good, info = analyse(p, a)
        (ok if good else bad).append(a)
        if DET: print('   p=%d kB=%d good seeds=%s' % (p, a, good[:12]), {s: info[s] for s in list(info)[:0]})
    print('p=%d beyond-W-ALL %s..%s | IND (free seed) succeeds: %s | fails: %s' % (p, beyond[0], beyond[-1],
          '%d..%d (%d values)' % (min(ok), max(ok), len(ok)) if ok else None, bad), flush=True)
