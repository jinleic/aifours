// indcyc.cpp -- c4 (T3 exploration, aid only [F]): avoider search for W(p, kB) using ONLY the patterns that are
// independent sets of the k-cycle (pairwise non-adjacent runs; m(Q) = |Q|).  Runs 0 (anti), 1..n (aligned), n = p + kB,
// k = n + 1; a pattern with j aligned runs and e = [0 in Q] has D = j - e, m = j + e; window (Lemma H, B = 1):
// u_Q must avoid [1 - lamc, lam - 1] (mod p), lam = lam(y, m) = min(p-m+1, y+m-kB, floor((y+1)/2)+1), lamc = lam(p+kB-1-y, m).
// DFS: u_0, u_1, ..., u_{n-1} in Z_p, u_n = -(sum); DP over the path of the sums of independent sets by (e, j, last-in).
// Usage: indcyc p kB [shrink] [nodecap]   (shrink s: lam - s, lamc - s; a FEASIBLE answer means only that this family
// is too weak; it is not an avoider of the word.)
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstring>
#include <vector>
typedef unsigned long long U;
static int p, kB, n, shr, JM;
static long long nodes = 0, cap = 0;
static U ALL;
static U Forb[2][80];          // forbidden residues for type (e, j)
static int u[100];
static bool found = false, capped = false;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline U rot(U m, int v) { v %= p; if (v < 0) v += p; if (v == 0) return m; return ((m << v) | (m >> (p - v))) & ALL; }
static int lam(int y, int m) { int a = p - m + 1, b = y + m - kB, c = fl2(y + 1) + 1; int v = a < b ? a : b; return (v < c ? v : c) - shr; }
static int lamc(int y, int m) { return lam(p + kB - 1 - y, m); }
// state S[e][j][f] for prefix 0..i
struct St { U s[2][42][2]; };
static std::vector<St> stk;
static bool extend(const St& a, St& b, int i, int v) {
    // add run i (1 <= i <= n) with value v; returns false if a new set violates its window
    memset(&b, 0, sizeof(St));
    for (int e = 0; e < 2; e++) for (int j = 0; j <= JM; j++) {
        b.s[e][j][0] = a.s[e][j][0] | a.s[e][j][1];
    }
    for (int e = 0; e < 2; e++) for (int j = 0; j < JM; j++) {
        U src = a.s[e][j][0];
        if (i == 1 && e == 1) continue;                   // 0 and 1 adjacent (0 in Q forces f(0) = 1 handled below)
        if (i == n && e == 1) continue;                   // n and 0 adjacent
        if (!src) continue;
        U nw = rot(src, v);
        if (nw & Forb[e][j + 1]) return false;
        b.s[e][j + 1][1] = nw;
    }
    return true;
}
static void dfs(int i) {
    if (found || capped) return;
    nodes++;
    if (cap && nodes > cap) { capped = true; return; }
    if (i == n) {
        long long sum = 0; for (int t = 0; t < n; t++) sum += u[t];
        int v = (int)(((-sum) % p + p) % p);
        St b; if (extend(stk[i - 1], b, n, v)) { u[n] = v; found = true; }
        return;
    }
    for (int v = 0; v < p && !found && !capped; v++) {
        if (!extend(stk[i - 1], stk[i], i, v)) continue;
        u[i] = v; dfs(i + 1);
    }
}
int main(int argc, char** argv) {
    if (argc < 3) return 1;
    p = atoi(argv[1]); kB = atoi(argv[2]); shr = argc > 3 ? atoi(argv[3]) : 0; cap = argc > 4 ? atoll(argv[4]) : 0;
    n = p + kB; JM = (n + 1) / 2 + 1; if (JM > 41) { fprintf(stderr, "range\n"); return 1; }
    ALL = (1ULL << p) - 1;
    for (int e = 0; e < 2; e++) for (int j = 0; j <= JM; j++) {
        Forb[e][j] = 0;
        if (j + e == 0) continue;
        int y = j - e, m = j + e;
        int l = lam(y, m), lc = lamc(y, m);
        for (int x = 1 - lc; x <= l - 1; x++) Forb[e][j] |= 1ULL << (((x % p) + p) % p);
        if (l + lc - 1 >= p) Forb[e][j] = ALL;
    }
    stk.assign(n + 1, St());
    for (int v0 = 0; v0 < p && !found && !capped; v0++) {
        if ((Forb[1][0] >> v0) & 1ULL) continue;          // anti singleton
        memset(&stk[0], 0, sizeof(St));
        stk[0].s[0][0][0] = 1ULL;                         // empty set
        stk[0].s[1][0][1] = 1ULL << v0;                   // {0}; "last in" = 0 in Q, blocks run 1
        u[0] = v0;
        // run 1: sets containing 1 must not contain 0: handled in extend via (i == 1 && e == 1) skip, but the source
        // for e = 1 at i = 1 is s[1][j][0] which is empty at i = 0 anyway; s[1][0][1] moves to s[1][0][0] after run 1.
        dfs(1);
    }
    printf("{\"p\":%d,\"kB\":%d,\"k\":%d,\"shrink\":%d,\"nodes\":%lld,\"capped\":%s,\"feasible\":%s", p, kB, n + 1, shr, nodes, capped ? "true" : "false", found ? "true" : "false");
    if (found) { printf(",\"u\":["); for (int t = 0; t <= n; t++) printf("%s%d", t ? "," : "", u[t]); printf("]"); }
    printf("}\n");
    return 0;
}
