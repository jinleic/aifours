// famdfs.cpp -- C++ port of famdfs.py (c2/README.md Sec. 11/14): exact avoider search over ALL patterns for an
// all-singleton all-odd word with anti runs at positions 0..B-1 (Lemma H windows, beta = 0).
// lambda(Q) = min(p-m+1, D_Q + B - kappa + m, floor((D_Q+B)/2) + 1) - shrink; I(Q) = [1-lambda(Q^c), lambda(Q)-1].
// u_0..u_{k-2} searched, u_{k-1} = -sum; patterns not containing run k-1.  Usage: famdfs p k B [shrink]
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
static int p, k, B, kappa, shrink;
static uint32_t FULL;
static std::vector<uint32_t> forb;   // index Q < 2^(k-1)
static std::vector<uint8_t> sums;
static int u[64];
static long long checks = 0;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static int lam(uint32_t Q) {
    uint32_t rot = ((Q << 1) | (Q >> (k - 1))) & FULL;
    int m = __builtin_popcount(Q & ~rot);
    uint32_t anti = (1u << B) - 1;
    int D = __builtin_popcount(Q & ~anti) - __builtin_popcount(Q & anti);
    int a = p - m + 1, b = D + B - kappa + m, c = fl2(D + B) + 1;
    int v = a < b ? a : b; v = v < c ? v : c;
    return v - shrink;
}
static bool dfs(int j) {
    if (j == k - 1) return true;
    uint32_t bit = 1u << j;
    for (int v = 0; v < p; v++) {
        bool ok = true;
        for (uint32_t P = 0; P < bit; P++) {
            checks++;
            int s = sums[P] + v; if (s >= p) s -= p;
            uint32_t Q = P | bit;
            if ((forb[Q] >> s) & 1u) { ok = false; break; }
            sums[Q] = (uint8_t)s;
        }
        if (!ok) continue;
        u[j] = v;
        if (dfs(j + 1)) return true;
    }
    return false;
}
int main(int argc, char** argv) {
    if (argc < 4) return 1;
    p = atoi(argv[1]); k = atoi(argv[2]); B = atoi(argv[3]); shrink = argc > 4 ? atoi(argv[4]) : 0;
    int R = k; kappa = (R + k - 2 * p) / 2;
    int A = k - B;
    if ((A < B ? A : B) > kappa) { printf("{\"empty_pattern_kills\":1}\n"); return 0; }
    FULL = (k == 32) ? 0xffffffffu : ((1u << k) - 1);
    size_t n = (size_t)1 << (k - 1);
    forb.assign(n, 0); sums.assign(n, 0);
    for (size_t Q = 1; Q < n; Q++) {
        int lo = 1 - lam(FULL ^ (uint32_t)Q), hi = lam((uint32_t)Q) - 1;
        uint32_t msk = 0;
        for (int x = lo; x <= hi; x++) msk |= 1u << (((x % p) + p) % p);
        forb[Q] = msk;
    }
    bool found = dfs(0);
    printf("{\"shrink\":%d,\"p\":%d,\"k\":%d,\"B\":%d,\"kappa\":%d,\"kB\":%d,\"avoider\":%s,\"checks\":%lld,\"u\":[", shrink, p, k, B, kappa, kappa - B, found ? "true" : "false", checks);
    if (found) { int s = 0; for (int j = 0; j < k - 1; j++) { printf("%s%d", j ? "," : "", u[j]); s += u[j]; } printf(",%d", ((-s) % p + p) % p); }
    printf("]}\n");
    return 0;
}
