# ind_star_ex.py -- c4 T4 ([F], aids only): hypotheses of Theorem IND* for GENERAL item-(iii) words (runs pure or
# (1,1)-pairs, total excess E = R - k), using T = N pairwise non-adjacent runs with d_t = 1 (single rho_1 letters).
# Any such word has n1 >= k - B - E single-letter aligned runs (anti runs and pairs number <= B, multi-letter aligned
# runs <= E), hence N >= ceil((k - B - E)/2) pairwise non-adjacent ones; the worst case N = ceil((k - B - E)/2) is used.
# Arcs for S subset of T, |S| = j (D_S = m(S) = j, D = 2p - k + 2kB, D_{S^c} = D - j, m(S^c) = j):
#   L_j = min(p-j+1, 2j-kB, floor((j+B)/2)+1),  U_j = p - min(p-j+1, D-kB, floor((D-j+B)/2)+1).
# Same hypotheses (W), lift range R (all seeds), (C), (L*) as ind_star3.py.  Evaluated on the open classes of the c3
# map (../c3/out/map3_p11.txt, map3_p13.txt) and on every (p, k, B, kB, E) class of item (iii) for p <= PMAX.
# Usage: python3 -B ind_star_ex.py PMAX
import sys, json
PMAX = int(sys.argv[1])
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
fl = lambda x, y: x // y
def arcs(p, k, kB, B, N):
    D = 2 * p - k + 2 * kB
    L = [None] + [min(p - j + 1, 2 * j - kB, fl(j + B, 2) + 1) for j in range(1, N + 2)]
    U = [None] + [p - min(p - j + 1, D - kB, fl(D - j + B, 2) + 1) for j in range(1, N + 2)]
    return L, U
def covered(p, k, kB, B, E):
    Nmax = -((-(k - B - E)) // 2)
    for N in range(Nmax, 1, -1):
        L, U = arcs(p, k, kB, B, N)
        if any(L[j] > U[j] for j in range(1, N + 1)): return (N, 'fullwindow')
        R = []
        for y in range(L[1], U[1] + 1):
            ok = True
            for s in range(1, N):
                lo, hi = L[s + 1] - U[s], U[s + 1] - L[s]
                if hi - lo + 1 >= p: continue
                if (y - lo) % p > hi - lo: ok = False; break
            if ok: R.append(y)
        if not R: return (N, 'emptyR')
        a, h = min(R), max(R)
        good = True
        for j in range(1, N):
            if max(L[j], j * a) + a < U[j + 1] + 1 - p or min(U[j], j * h) + h > p + L[j + 1] - 1: good = False; break
        if not good: continue
        surv = False
        for X in range(max(L[N], N * a), min(U[N], N * h) + 1):
            q, rho = divmod(X, N)
            if all(j * q + max(0, j - (N - rho)) >= L[j] and j * q + min(j, rho) <= U[j] for j in range(1, N)): surv = True; break
        if not surv: return (N, 'ok')
    return None
for fn, p in (('../c3/out/map3_p11.txt', 11), ('../c3/out/map3_p13.txt', 13)):
    for l in open(fn):
        if l.startswith('{"open"'):
            d = json.loads(l)
            k = d['p'] + d['k_minus_p']
            c = covered(p, k, d['kB'], d['B'], d['excess'])
            print('c3 open p=%d k=%d B=%d kB=%d excess=%d type=%d reason=%s words=%d -> %s' % (p, k, d['B'], d['kB'], d['excess'], d['type'], d['reason'], d['words'], c))
tot = cov = 0
for p in range(11, PMAX + 1):
    if not isprime(p): continue
    t0 = c0 = 0
    for k in range(p + 1, 2 * p - 2):
        for kappa in range(k - p, (k - 3) // 2 + 1):          # R = 2p - k + 2 kappa <= 2p - 3, R >= k
            R = 2 * p - k + 2 * kappa; E = R - k
            if E < 0: continue
            for B in range(1, kappa):
                kB = kappa - B
                if B > (R - B): continue                        # B <= A
                t0 += 1
                if covered(p, k, kB, B, E): c0 += 1
    tot += t0; cov += c0
    print('p=%d item-(iii) classes (k, kappa, B) [worst-case N] %d, IND* hypotheses hold for %d' % (p, t0, c0), flush=True)
print({'classes': tot, 'covered_worst_case': cov})
