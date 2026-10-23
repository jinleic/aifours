# famdfs.py -- independent exact avoider search (Lemma H of ../../../inverse-parity/proof-PAR-K0.md Sec. 1)
# for an all-odd word given by d (per run), B, kappa.  lambda(Q) = min(p-m+1, D_Q+B-kappa+m-beta,
# floor((D_Q+B)/2)+1) with beta = 0 (all reflection runs odd); I(Q) = [1-lambda(Q^c), lambda(Q)-1];
# avoid iff u_Q notin I(Q) mod p for all proper Q (the empty condition min(A,B) <= kappa is checked).
# Search u_0..u_{k-2}, u_{k-1} := -sum; patterns Q not containing run k-1 suffice (I(Q^c) = -I(Q)).
# Usage: python3 famdfs.py p k B [shrink]   (all runs single letters; anti runs = runs 0..B-1)
# shrink > 0 is a MUTATION CONTROL only: every lambda is lowered by shrink (windows shrink), so the search
# must then be able to find 'avoiders' of the weakened system.
import sys
def main():
    p, k, B = map(int, sys.argv[1:4]); shrink = int(sys.argv[4]) if len(sys.argv) > 4 else 0
    d = [-1] * B + [1] * (k - B)
    A = k - B; R = k; kappa = (R + k - 2 * p) // 2
    assert (R + k - 2 * p) % 2 == 0
    if min(A, B) > kappa: print('empty pattern kills'); return
    full = (1 << k) - 1
    def blocks(Q):
        rot = ((Q << 1) | (Q >> (k - 1))) & full
        return bin(Q & ~rot).count('1')
    def lam(Q):
        m = blocks(Q); D = sum(d[t] for t in range(k) if (Q >> t) & 1)
        return min(p - m + 1, D + B - kappa + m, (D + B) // 2 + 1) - shrink
    n = 1 << (k - 1)
    forb = [0] * n
    for Q in range(1, n):
        lo, hi = 1 - lam(full ^ Q), lam(Q) - 1
        msk = 0
        for x in range(lo, hi + 1): msk |= 1 << (x % p)
        forb[Q] = msk
    sums = [0] * n
    sol = []
    checks = [0]
    def dfs(j):
        if j == k - 1: return True
        bit = 1 << j
        for v in range(p):
            ok = True
            for P in range(bit):                    # all Q = P | bit with P subset [0, j)
                checks[0] += 1
                s = (sums[P] + v) % p
                Q = P | bit
                if (forb[Q] >> s) & 1: ok = False; break
                sums[Q] = s
            if not ok: continue
            sol.append(v)
            if dfs(j + 1): return True
            sol.pop()
        return False
    found = dfs(0)
    print({'shrink': shrink, 'p': p, 'k': k, 'B': B, 'kappa': kappa, 'kB': kappa - B, 'avoider': found, 'checks': checks[0], 'u': sol if found else None})
main()
