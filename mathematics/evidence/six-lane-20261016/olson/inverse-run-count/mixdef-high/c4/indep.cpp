// indep.cpp -- c4 README Sec. 1 T3 / Sec. 3 P2: the INDEPENDENT-SET SUBSET-SUM system of W(p, kB).
// T = N pairwise non-adjacent aligned runs (no anti run).  Every S subset of T with |S| = j is a proper pattern with
// D_S = m(S) = j, so (Lemma H, beta = 0, B = 1) its half-sum u_S must lie in the allowed arc
//   G_j = [lam(j), p - lamc(j)] (mod p),  lam(j) = min(p-j+1, 2j-kB, floor((j+1)/2)+1),
//   lamc(j) = lambda(S^c) = min(p-j+1, p-1-j+j, floor((p+kB-j)/2)+1)        (c3/proof-WALL.md (0.1), (0.2), e = 0, y = m = j)
// (no constraint if lam + lamc <= 0).  The constraints depend only on |S|, so feasibility depends only on the MULTISET
// of the N values.  DFS over non-decreasing residue sequences with an incremental DP of the j-subset-sum sets
// (bitmasks over Z_p), pruning as soon as some j-subset-sum set leaves G_j.  Aid only ([F]).
// Usage: indep p kB [N] [shrink] [print]   (N default ceil((p+kB)/2); shrink s replaces lam, lamc by lam-s, lamc-s,
// i.e. SHRINKS every forbidden window by 2s (mutation control); print=1 prints the first feasible multiset).
// Output: one JSON line: max depth reached (largest i with a feasible multiset of size i), nodes, feasible-at-N flag.
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
typedef unsigned long long U;
static int p, kB, N, shr, prt;
static U ALL, Al[80];
static long long nodes = 0;
static int maxdepth = 0, vals[80];
static bool found = false;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline U rot(U m, int v) { if (v == 0) return m; return ((m << v) | (m >> (p - v))) & ALL; }
static int lamS(int j) { int a = p - j + 1, b = 2 * j - kB, c = fl2(j + 1) + 1; int v = a < b ? a : b; return (v < c ? v : c) - shr; }
static int lamC(int j) { int a = p - j + 1, b = p - 1, c = fl2(p + kB - j) + 1; int v = a < b ? a : b; return (v < c ? v : c) - shr; }
static void dfs(int i, int vmin, std::vector<U>& dp) {
    // dp[j] = set of j-subset sums of the current multiset (size i), j = 0..i
    nodes++;
    if (i > maxdepth) maxdepth = i;
    if (i == N) { found = true; return; }
    std::vector<U> nd(i + 2);
    for (int v = vmin; v < p && !found; v++) {
        nd[0] = 1ULL;
        bool ok = true;
        for (int j = 1; j <= i + 1; j++) {
            U s = (j <= i ? dp[j] : 0ULL) | rot(dp[j - 1], v);
            if (s & ~Al[j]) { ok = false; break; }
            nd[j] = s;
        }
        if (!ok) continue;
        vals[i] = v;
        dfs(i + 1, v, nd);
        if (found) return;
    }
}
int main(int argc, char** argv) {
    if (argc < 3) { fprintf(stderr, "usage: indep p kB [N] [shrink] [print]\n"); return 1; }
    p = atoi(argv[1]); kB = atoi(argv[2]);
    N = argc > 3 ? atoi(argv[3]) : (p + kB + 1) / 2;
    if (N <= 0) N = (p + kB + 1) / 2;
    shr = argc > 4 ? atoi(argv[4]) : 0; prt = argc > 5 ? atoi(argv[5]) : 0;
    if (p > 63 || N > 78) { fprintf(stderr, "range\n"); return 1; }
    ALL = (p == 64) ? ~0ULL : ((1ULL << p) - 1);
    printf("{\"p\":%d,\"kB\":%d,\"N\":%d,\"shrink\":%d,\"arcs\":[", p, kB, N, shr);
    for (int j = 1; j <= N; j++) {
        int l = lamS(j), lc = lamC(j);
        U m = 0;
        if (l + lc <= 0) m = ALL;
        else for (int x = l; x <= p - lc; x++) m |= 1ULL << (((x % p) + p) % p);
        Al[j] = m;
        printf("%s[%d,%d,%d]", j > 1 ? "," : "", j, l, p - lc);
    }
    printf("]");
    std::vector<U> dp(1, 1ULL);
    dfs(0, 0, dp);
    printf(",\"maxdepth\":%d,\"nodes\":%lld,\"feasible_at_N\":%s", maxdepth, nodes, found ? "true" : "false");
    if (found && prt) { printf(",\"multiset\":["); for (int i = 0; i < N; i++) printf("%s%d", i ? "," : "", vals[i]); printf("]"); }
    printf("}\n");
    return 0;
}
