// indep_enum.cpp -- c4 (T3 exploration, aid only [F]): ENUMERATE all multisets of N residues mod p whose j-subset sums
// lie in G_j for every j (the independent-set system of indep.cpp; same arcs), printing each as value:count pairs.
// Usage: indep_enum p kB N [maxprint]
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
#include <map>
#include <string>
typedef unsigned long long U;
static int p, kB, N, maxprint;
static U ALL, Al[80];
static long long nodes = 0, sols = 0;
static int vals[80];
static std::map<std::string, long long> shapes;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline U rot(U m, int v) { if (v == 0) return m; return ((m << v) | (m >> (p - v))) & ALL; }
static int lam(int y, int m) { int a = p - m + 1, b = y + m - kB, c = fl2(y + 1) + 1; int v = a < b ? a : b; return v < c ? v : c; }
static int lamc(int y, int m) { return lam(p + kB - 1 - y, m); }
static void dfs(int i, int vmin, std::vector<U>& dp) {
    nodes++;
    if (i == N) {
        sols++;
        std::string s; int t = 0;
        while (t < N) { int v = vals[t], c = 0; while (t < N && vals[t] == v) { c++; t++; } char b[32]; snprintf(b, 32, "%d^%d ", v, c); s += b; }
        // shape key: distinct values with counts
        shapes[s]++;
        return;
    }
    std::vector<U> nd(i + 2);
    for (int v = vmin; v < p; v++) {
        nd[0] = 1ULL; bool ok = true;
        for (int j = 1; j <= i + 1; j++) {
            U s = (j <= i ? dp[j] : 0ULL) | rot(dp[j - 1], v);
            if (s & ~Al[j]) { ok = false; break; }
            nd[j] = s;
        }
        if (!ok) continue;
        vals[i] = v; dfs(i + 1, v, nd);
    }
}
int main(int argc, char** argv) {
    if (argc < 4) return 1;
    p = atoi(argv[1]); kB = atoi(argv[2]); N = atoi(argv[3]); maxprint = argc > 4 ? atoi(argv[4]) : 20;
    ALL = (1ULL << p) - 1;
    for (int j = 1; j <= N; j++) {
        int l = lam(j, j), lc = lamc(j, j); U s = 0;
        if (l + lc <= 0) s = ALL; else for (int x = l; x <= p - lc; x++) s |= 1ULL << (((x % p) + p) % p);
        Al[j] = s;
    }
    std::vector<U> dp(1, 1ULL);
    dfs(0, 0, dp);
    printf("{\"p\":%d,\"kB\":%d,\"N\":%d,\"nodes\":%lld,\"solutions\":%lld,\"shapes\":[", p, kB, N, nodes, sols);
    int c = 0;
    for (auto& kv : shapes) { if (c >= maxprint) break; printf("%s\"%s\"", c ? "," : "", kv.first.c_str()); c++; }
    printf("]}\n");
    return 0;
}
