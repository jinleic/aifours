# ind_cert.py -- c4 README Sec. 5: numerical check of proof scheme IND for the parity-class system of W(p, kB).
# T = N pairwise non-adjacent aligned runs (N = ceil((p + kB)/2) by default); every S subset of T, |S| = j, has
# D_S = m(S) = j, window [1 - lamc_j, L_j - 1] with L_j = lambda(S) = min(p-j+1, 2j-kB, floor((j+1)/2)+1),
# lamc_j = lambda(S^c) = min(p-j+1, p-1, floor((p+kB-j)/2)+1), U_j := p - lamc_j (allowed lifted arc [L_j, U_j]).
# (1) R := integers x in [L_1, U_1] with x mod p in (G_(j+1) - G_j) mod p for every 1 <= j <= N-1, where
#     G_(j+1) - G_j = [L_(j+1) - U_j, U_(j+1) - L_j] (no condition if that interval has >= p integers).
# (2) size chain: lo_1 = min R, hi_1 = max R; size j -> j+1 certified iff [lo_j + lo_1, hi_j + hi_1] lies in
#     [U_(j+1) + 1 - p, p + L_(j+1) - 1]; then lo_(j+1) = max(L_(j+1), lo_j + lo_1), hi_(j+1) = min(U_(j+1), hi_j + hi_1).
# (3)+(4) two-valued (balanced) profiles: for every total X in [N lo_1, N hi_1] (and in [lo_N, hi_N] if size N is
#     certified) the balanced sequence (values q, q+1, q = floor(X/N)) must satisfy s_j >= L_j and t_j <= U_j for every
#     certified size j <= N - 1 and have values in [lo_1, hi_1]; the scheme succeeds if no total survives (or lo > hi).
# Usage: python3 -B ind_cert.py PMIN PMAX [details]
import sys
PMIN, PMAX = int(sys.argv[1]), int(sys.argv[2]); DET = len(sys.argv) > 3
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def analyse(p, a, N=None):
    if N is None: N = (p + a + 1) // 2
    L = [None] * (N + 2); U = [None] * (N + 2)
    for j in range(1, N + 1):
        L[j] = min(p - j + 1, 2 * j - a, (j + 1) // 2 + 1)
        lc = min(p - j + 1, p - 1, (p + a - j) // 2 + 1)
        U[j] = p - lc
        assert L[j] + lc >= 1 and U[j] - L[j] + 1 < p, (p, a, j)
    R = []
    for x in range(L[1], U[1] + 1):
        ok = True
        for j in range(1, N):
            lo, hi = L[j + 1] - U[j], U[j + 1] - L[j]
            if hi - lo + 1 >= p: continue
            if not any((x - y) % p == 0 for y in range(lo, hi + 1)):
                ok = False; break
        if ok: R.append(x)
    if not R: return {'p': p, 'kB': a, 'N': N, 'R': None, 'result': 'R empty'}
    lo1, hi1 = min(R), max(R)
    lo = {1: lo1}; hi = {1: hi1}; Jc = 1
    for j in range(1, N):
        A, Bv = lo[j] + lo1, hi[j] + hi1
        if A >= U[j + 1] + 1 - p and Bv <= p + L[j + 1] - 1:
            lo[j + 1] = max(L[j + 1], A); hi[j + 1] = min(U[j + 1], Bv); Jc = j + 1
            if lo[j + 1] > hi[j + 1]:
                return {'p': p, 'kB': a, 'N': N, 'R': [lo1, hi1], 'Jcert': Jc, 'result': 'range empty at size %d' % (j + 1)}
        else:
            break
    surv = []
    Xlo, Xhi = N * lo1, N * hi1
    if Jc == N: Xlo, Xhi = max(Xlo, lo[N]), min(Xhi, hi[N])
    for X in range(Xlo, Xhi + 1):
        q, r = divmod(X, N)            # r copies of q+1, N - r copies of q
        if q < lo1 or (r > 0 and q + 1 > hi1): continue
        ok = True
        for j in range(1, min(Jc, N - 1) + 1):
            s = j * q + max(0, j - (N - r)); t = j * q + min(j, r)
            if s < L[j] or t > U[j]: ok = False; break
        if ok: surv.append((X, q, r))
    res = 'INFEASIBLE' if not surv else 'survivors'
    return {'p': p, 'kB': a, 'N': N, 'R': [lo1, hi1], 'Rsize': len(R), 'Jcert': Jc, 'result': res, 'survivors': surv[:4], 'nsurv': len(surv)}
summary = []
for p in range(PMIN, PMAX + 1):
    if not isprime(p) or p < 11: continue
    beyond = [a for a in range(1, p - 3) if 3 * a >= p + 5]
    res = [analyse(p, a) for a in beyond]
    ok = [r['kB'] for r in res if r['result'] != 'survivors']
    bad = [r['kB'] for r in res if r['result'] == 'survivors']
    fullcert = [r['kB'] for r in res if r.get('Jcert') == r['N']]
    print('p=%d beyond-W-ALL kB=%s..%s | scheme IND succeeds: %s | fails: %s | all sizes certified for: %s' % (
        p, beyond[0] if beyond else None, beyond[-1] if beyond else None, ok, bad, 'all' if fullcert == beyond else fullcert), flush=True)
    if DET:
        for r in res: print('   ', r)
    summary.append((p, ok, bad))
