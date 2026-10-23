# ind_m.py -- c4 (T3): the FIXED-SEED version of scheme IND that the written proof (proof-IND.md) follows.  Aid [F].
# Arcs of the parity class T (|T| = N = ceil((p + kB)/2)): L_j = min(p-j+1, 2j-kB, floor((j+1)/2)+1),
# U_j = p - min(p-j+1, p-1, floor((p+kB-j)/2)+1); B := p - kB; j1 := min{j >= 1 : 2j - kB >= floor((j+1)/2) + 1};
# seed s := max(B, j1); A := [L_(s+1) - U_s, U_(s+1) - L_s]; lift range R := [min A, min(max A, floor(B/2))] (valid only if
# max A <= B + 1, so that the residues of A above floor(B/2) are in the singleton window).  Then: (i) every size-chain step
# j -> j+1 (1 <= j <= N-1) satisfies [lo_j - r, hi_j + h] inside [U_(j+1) + 1 - p, p + L_(j+1) - 1] (r = -min R, h = max R,
# lo_1 = -r, hi_1 = h, lo_j = max(L_j, lo_(j-1) - r), hi_j = min(U_j, hi_(j-1) + h)); (ii) total window [L_N, U_N] =
# [p - N + 1, N - 1]; (iii) balanced {0,1} exclusion: no X in [max(L_N, N lo... ), U_N] with
# min(B, X) <= B - 1 (top, size B) and max(0, j - (N - X)) >= L_j for all j (bottom).  Prints per p the kB-interval
# where all of (seed validity, (i), (ii), (iii)) hold, compared with the candidate closed-form range.
# Usage: python3 -B ind_m.py PMIN PMAX
import sys
PMIN, PMAX = int(sys.argv[1]), int(sys.argv[2])
def isprime(q): return q > 1 and all(q % r for r in range(2, int(q ** 0.5) + 1))
def check(p, a):
    N = (p + a + 1) // 2; B = p - a
    L = {j: min(p - j + 1, 2 * j - a, (j + 1) // 2 + 1) for j in range(1, N + 2)}
    U = {j: p - min(p - j + 1, p - 1, (p + a - j) // 2 + 1) for j in range(1, N + 2)}
    j1 = next(j for j in range(1, 10 * p) if 2 * j - a >= (j + 1) // 2 + 1)
    s = max(B, j1)
    if s + 1 > N: return 'seed>N'
    # seed regime facts used in the proof
    if not (U[s] == s - 1 and U[s + 1] == s and L[s] == (s + 1) // 2 + 1 and L[s + 1] == (s + 2) // 2 + 1): return 'seed-regime'
    Alo, Ahi = L[s + 1] - U[s], U[s + 1] - L[s]
    if Ahi > B + 1: return 'A-above-window'
    if Alo < 2 - a: return 'A-below'
    r, h = -Alo, min(Ahi, B // 2)
    lo, hi = -r, h
    for j in range(1, N):
        A1, A2 = lo - r, hi + h
        if not (A1 >= U[j + 1] + 1 - p and A2 <= p + L[j + 1] - 1): return 'chain@%d' % (j + 1)
        lo, hi = max(L[j + 1], A1), min(U[j + 1], A2)
        if lo > hi: return 'OK-empty'
    if not (L[N] == p - N + 1 and U[N] == N - 1): return 'total-window'
    for X in range(max(L[N], 0), U[N] + 1):
        if X < 0 or X > N: continue
        if min(B, X) > B - 1: continue
        if all(max(0, j - (N - X)) >= L[j] for j in range(1, N)) and all(min(j, X) <= U[j] for j in range(1, N)): return 'balanced-survives'
    return 'OK'
for p in range(PMIN, PMAX + 1):
    if not isprime(p) or p < 11: continue
    res = {a: check(p, a) for a in range(1, p - 3) if 3 * a >= p + 5}
    ok = [a for a in res if res[a].startswith('OK')]
    lo_c = -(-(3 * p - 4) // 7)    # candidate lower end ceil((3p-4)/7) (to be compared)
    print('p=%d OK kB in %s (%d values, contiguous=%s) | first failures: %s' % (p, (min(ok), max(ok)) if ok else None, len(ok),
          ok == list(range(min(ok), max(ok) + 1)) if ok else None, sorted(set(v for v in res.values() if not v.startswith('OK')))), flush=True)
