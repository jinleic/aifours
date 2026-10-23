// nolp_check.cpp -- exact check of the Lemma NOLP point (proof-NOLP.md Sec. 2) on ALL proper patterns of a word
// in W(p, kB): k = p + 1 + kB single-letter runs, anti run at 0, B = 1, kappa = kB + 1.
// Checks (integers, scaled by 5k):  5 lambda(Q) <= 4j - e  (per-pattern bound),  and
//   5k lambda(Q) <= 5k X_Q <= 5k (p - lambda(Q^c)),  5k X_Q = k(4j - e) + (p - 4kB + 1)|Q|;  5k X_[k] = 5pk.
// Usage: nolp_check p kB
#include <cstdio>
#include <cstdlib>
#include <cstdint>
static int p, kB, k, B = 1, kappa;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static uint64_t FULL;
static int lam(uint64_t Q) {
    uint64_t rot = ((Q << 1) | (Q >> (k - 1))) & FULL;
    int m = __builtin_popcountll(Q & ~rot);
    int e = (int)(Q & 1ULL), j = __builtin_popcountll(Q) - e;
    int D = j - e;
    int a = p - m + 1, b = D + B - kappa + m, c = fl2(D + B) + 1;
    int v = a < b ? a : b; return v < c ? v : c;
}
int main(int argc, char** argv) {
    p = atoi(argv[1]); kB = atoi(argv[2]); k = p + 1 + kB; kappa = kB + 1;
    FULL = (k == 64) ? ~0ULL : ((1ULL << k) - 1);
    long long bad_phi = 0, bad_lo = 0, bad_hi = 0, n = 0;
    long long slope = p - 4 * kB + 1;
    for (uint64_t Q = 1; Q < FULL; Q++) {
        n++;
        int e = (int)(Q & 1ULL), sz = __builtin_popcountll(Q), j = sz - e;
        int L = lam(Q), Lc = lam(FULL ^ Q);
        if (5 * L > 4 * j - e) bad_phi++;
        long long X5k = (long long)k * (4 * j - e) + slope * sz;
        if (5LL * k * L > X5k) bad_lo++;
        if (X5k > 5LL * k * (p - Lc)) bad_hi++;
    }
    long long tot5k = (long long)k * (4 * (k - 1) - 1) + slope * k;
    printf("{\"p\":%d,\"kB\":%d,\"k\":%d,\"patterns\":%lld,\"viol_lambda_le_phi\":%lld,\"viol_lower\":%lld,\"viol_upper\":%lld,\"total_equals_p\":%s,\"c_nonneg\":%s}\n",
           p, kB, k, n, bad_phi, bad_lo, bad_hi, tot5k == 5LL * p * k ? "true" : "false", slope >= 0 ? "true" : "false");
    return 0;
}
