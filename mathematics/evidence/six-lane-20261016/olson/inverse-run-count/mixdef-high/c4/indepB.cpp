// indepB.cpp -- c4 T4 (aid only [F]): the parity-class (independent-set) system for ALL-SINGLETON all-odd words with
// k runs, B anti runs (any positions), kappa = k - p, kB = k - p - B (item (iii) needs p+2 <= k <= 2p-3, 1 <= B <= k-p-1).
// T = N pairwise non-adjacent ALIGNED runs (any placement of the anti runs admits N >= ceil((k - B)/2); default N =
// ceil((k - B)/2), the worst case).  For S subset of T, |S| = j: D_S = m(S) = j and (Lemma H, beta = 0)
//   lambda(S) = min(p-j+1, 2j-kB, floor((j+B)/2)+1),  lambda(S^c) = min(p-j+1, p-B, floor((k-B-j)/2)+1)
// (D = A - B = k - 2B, D_{S^c} = k - 2B - j, m(S^c) = j, D_{S^c} + j - kB = p - B).  Allowed arc G_j = [lam, p - lamc].
// Multiset DFS exactly as in indep.cpp.  Usage: indepB p k B [N] [shrink]
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
typedef unsigned long long U;
static int p, K, Bv, kB, N, shr;
static U ALL, Al[80];
static long long nodes = 0;
static int maxdepth = 0;
static bool found = false;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline U rot(U m, int v) { if (v == 0) return m; return ((m << v) | (m >> (p - v))) & ALL; }
static int lamS(int j) { int a = p - j + 1, b = 2 * j - kB, c = fl2(j + Bv) + 1; int v = a < b ? a : b; return (v < c ? v : c) - shr; }
static int lamC(int j) { int a = p - j + 1, b = p - Bv, c = fl2(K - Bv - j) + 1; int v = a < b ? a : b; return (v < c ? v : c) - shr; }
static void dfs(int i, int vmin, std::vector<U>& dp) {
    nodes++;
    if (i > maxdepth) maxdepth = i;
    if (i == N) { found = true; return; }
    std::vector<U> nd(i + 2);
    for (int v = vmin; v < p && !found; v++) {
        nd[0] = 1ULL; bool ok = true;
        for (int j = 1; j <= i + 1; j++) {
            U s = (j <= i ? dp[j] : 0ULL) | rot(dp[j - 1], v);
            if (s & ~Al[j]) { ok = false; break; }
            nd[j] = s;
        }
        if (!ok) continue;
        dfs(i + 1, v, nd);
        if (found) return;
    }
}
int main(int argc, char** argv) {
    if (argc < 4) return 1;
    p = atoi(argv[1]); K = atoi(argv[2]); Bv = atoi(argv[3]);
    kB = K - p - Bv;
    N = argc > 4 ? atoi(argv[4]) : 0; if (N <= 0) N = (K - Bv + 1) / 2;
    shr = argc > 5 ? atoi(argv[5]) : 0;
    if (p > 63 || N > 78) return 1;
    ALL = (1ULL << p) - 1;
    for (int j = 1; j <= N; j++) {
        int l = lamS(j), lc = lamC(j); U s = 0;
        if (l + lc <= 0) s = ALL; else if (l + lc - 1 >= p) s = 0; else for (int x = l; x <= p - lc; x++) s |= 1ULL << (((x % p) + p) % p);
        Al[j] = s;
    }
    std::vector<U> dp(1, 1ULL);
    dfs(0, 0, dp);
    printf("{\"p\":%d,\"k\":%d,\"B\":%d,\"kB\":%d,\"N\":%d,\"shrink\":%d,\"maxdepth\":%d,\"nodes\":%lld,\"feasible_at_N\":%s}\n",
           p, K, Bv, kB, N, shr, maxdepth, nodes, found ? "true" : "false");
    return 0;
}
