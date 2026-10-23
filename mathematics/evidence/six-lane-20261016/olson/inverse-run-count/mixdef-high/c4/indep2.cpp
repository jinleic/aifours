// indep2.cpp -- c4 (T3 exploration, aid only [F]): the independent-set system of indep.cpp ENLARGED by the anti run.
// T = N pairwise non-adjacent aligned runs, none adjacent to the anti run 0 (e.g. 2, 4, ..., in W(p, kB)).
// Patterns used: S subset of T (D = m = |S| = j): u_S in G_j = [lam(j, j), p - lamc(j, j)];
//                {0} u S, S subset of T (D = j - 1, m = j + 1, 0 isolated): u_0 + u_S in H_j = [lam(j-1, j+1), p - lamc(j-1, j+1)]
// (j = 0: the anti singleton).  lam(y, m) = min(p-m+1, y+m-kB, floor((y+1)/2)+1), lamc(y, m) = lam(p+kB-1-y, m).
// For fixed u_0 the constraints depend only on the multiset of the N values: j-subset sums must lie in
// G_j intersect (H_j - u_0).  DFS over u_0 and non-decreasing residue sequences with the subset-sum DP of indep.cpp.
// Usage: indep2 p kB [N] [shrink] [print]  (N default = number of aligned runs at even positions 2..n not adjacent to 0)
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
typedef unsigned long long U;
static int p, kB, N, shr, prt;
static U ALL, Al[80];
static long long nodes = 0;
static int maxdepth = 0, vals[80], u0best = -1;
static bool found = false;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline U rot(U m, int v) { v %= p; if (v < 0) v += p; if (v == 0) return m; return ((m << v) | (m >> (p - v))) & ALL; }
static int lam(int y, int m) { int a = p - m + 1, b = y + m - kB, c = fl2(y + 1) + 1; int v = a < b ? a : b; return (v < c ? v : c) - shr; }
static int lamc(int y, int m) { return lam(p + kB - 1 - y, m); }
static U arc(int y, int m) {
    int l = lam(y, m), lc = lamc(y, m); U s = 0;
    if (l + lc <= 0) return ALL;
    for (int x = l; x <= p - lc; x++) s |= 1ULL << (((x % p) + p) % p);
    return s;
}
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
        vals[i] = v; dfs(i + 1, v, nd);
        if (found) return;
    }
}
int main(int argc, char** argv) {
    if (argc < 3) { fprintf(stderr, "usage\n"); return 1; }
    p = atoi(argv[1]); kB = atoi(argv[2]);
    int n = p + kB;                       // aligned runs 1..n, anti run 0 adjacent to 1 and n
    int Ndef = (n - 1) / 2 - (n % 2 == 0 ? 0 : 0);   // even positions 2..n-1
    Ndef = 0; for (int t = 2; t <= n - 1; t += 2) Ndef++;
    N = argc > 3 ? atoi(argv[3]) : Ndef; if (N <= 0) N = Ndef;
    shr = argc > 4 ? atoi(argv[4]) : 0; prt = argc > 5 ? atoi(argv[5]) : 0;
    if (p > 63 || N > 78) { fprintf(stderr, "range\n"); return 1; }
    ALL = (1ULL << p) - 1;
    U G[80], H[80];
    for (int j = 1; j <= N; j++) G[j] = arc(j, j);
    for (int j = 0; j <= N; j++) H[j] = arc(j - 1, j + 1);
    long long totnodes = 0; int best = 0;
    for (int u0 = 0; u0 < p && !found; u0++) {
        if (!((H[0] >> u0) & 1ULL)) continue;           // anti singleton constraint
        for (int j = 1; j <= N; j++) Al[j] = G[j] & rot(H[j], -u0);
        maxdepth = 0; nodes = 0;
        std::vector<U> dp(1, 1ULL);
        dfs(0, 0, dp);
        totnodes += nodes; if (maxdepth > best) best = maxdepth;
        if (found) u0best = u0;
    }
    printf("{\"p\":%d,\"kB\":%d,\"N\":%d,\"shrink\":%d,\"maxdepth\":%d,\"nodes\":%lld,\"feasible_at_N\":%s", p, kB, N, shr, best, totnodes, found ? "true" : "false");
    if (found && prt) { printf(",\"u0\":%d,\"multiset\":[", u0best); for (int i = 0; i < N; i++) printf("%s%d", i ? "," : "", vals[i]); printf("]"); }
    printf("}\n");
    return 0;
}
