// indep_minJ.cpp -- c4 (T3 exploration, aid only [F]): which subset sizes j of the independent-set system of indep.cpp
// are needed for infeasibility?  Greedy deletion: start with all sizes 1..N active; for j = N, N-1, ..., 1 drop the
// constraint of size j if the system stays infeasible.  Prints the resulting inclusion-minimal set J of sizes (minimal
// for this greedy order) with the arcs G_j = [lam, p - lamc].
// Usage: indep_minJ p kB [N]
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
typedef unsigned long long U;
static int p, kB, N;
static U ALL, Al[80], G[80];
static long long nodes;
static bool found;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline U rot(U m, int v) { if (v == 0) return m; return ((m << v) | (m >> (p - v))) & ALL; }
static int lamS(int j) { int a = p - j + 1, b = 2 * j - kB, c = fl2(j + 1) + 1; int v = a < b ? a : b; return v < c ? v : c; }
static int lamC(int j) { int a = p - j + 1, b = p - 1, c = fl2(p + kB - j) + 1; int v = a < b ? a : b; return v < c ? v : c; }
static void dfs(int i, int vmin, std::vector<U>& dp) {
    nodes++;
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
    }
}
static bool feasible() { found = false; nodes = 0; std::vector<U> dp(1, 1ULL); dfs(0, 0, dp); return found; }
int main(int argc, char** argv) {
    if (argc < 3) return 1;
    p = atoi(argv[1]); kB = atoi(argv[2]); N = argc > 3 ? atoi(argv[3]) : (p + kB + 1) / 2; if (N <= 0) N = (p + kB + 1) / 2;
    ALL = (1ULL << p) - 1;
    for (int j = 1; j <= N; j++) {
        int l = lamS(j), lc = lamC(j); U s = 0;
        if (l + lc <= 0) s = ALL; else for (int x = l; x <= p - lc; x++) s |= 1ULL << (((x % p) + p) % p);
        G[j] = s; Al[j] = s;
    }
    if (feasible()) { printf("{\"p\":%d,\"kB\":%d,\"N\":%d,\"feasible\":true}\n", p, kB, N); return 0; }
    for (int j = N; j >= 1; j--) { Al[j] = ALL; if (feasible()) Al[j] = G[j]; }
    printf("{\"p\":%d,\"kB\":%d,\"N\":%d,\"feasible\":false,\"J\":[", p, kB, N);
    int f = 0;
    for (int j = 1; j <= N; j++) if (Al[j] != ALL) { printf("%s[%d,%d,%d]", f ? "," : "", j, lamS(j), p - lamC(j)); f = 1; }
    printf("],\"B\":%d}\n", p - kB);
    return 0;
}
