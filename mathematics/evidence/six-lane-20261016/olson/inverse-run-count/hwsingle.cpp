// hwsingle.cpp -- half-window avoidance search for ONE run datum (README Sec. 2).
// Usage: hwsingle p famM k a_0..a_{k-1} b_0..b_{k-1} l_0..l_{k-1} [maxsol]
// Prints: full-window flag, and up to maxsol feasible phi (within patterns m(P) <= famM), and the count
// of feasible phi found (capped).  DFS order: phi_0, ..., phi_{k-2}; phi_{k-1} = -sum.
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cstdint>
static int p, famM, K, a[64], b[64], l[64];
static std::vector<uint32_t> forb; static std::vector<uint8_t> inFam; static std::vector<int> sums;
static int phi[64]; static long long nsol = 0, maxsol = 5, cap = 1000000;
static int build() {
    int k = K, R = 0;
    for (int i = 0; i < k; i++) R += a[i] + b[i];
    int np = 1 << (k - 1);
    forb.assign(np, 0); inFam.assign(np, 0);
    int fullP = -1;
    for (int P = 0; P < np; P++) {
        int f2 = 0, h = 0, Ep = 0;
        for (int j = 0; j < k; j++) {
            int zj = (P >> j) & 1, zn = (P >> ((j + 1) % k)) & 1, f = zj != zn;
            f2 += f; h += (l[j] - f) / 2; Ep += zj ? a[j] : b[j];
        }
        int m = f2 / 2, Em = R - Ep;
        auto g = [&](int E) { return std::min(p - m, std::min(E + m + h - p, E / 2)); };
        int lo = -g(Em), hi = g(Ep);
        if (m > famM) continue;
        inFam[P] = 1;
        if (lo > hi) continue;
        if (hi - lo + 1 >= p) { if (fullP < 0) fullP = P; continue; }
        uint32_t msk = 0;
        for (int x = lo; x <= hi; x++) msk |= 1u << (((x % p) + p) % p);
        forb[P] = msk;
    }
    return fullP;
}
static void dfs(int j) {
    if (nsol >= cap) return;
    if (j == K - 1) {
        nsol++;
        if (nsol <= maxsol) {
            int s = 0; printf("phi:");
            for (int i = 0; i < K - 1; i++) { printf(" %d", phi[i]); s += phi[i]; }
            printf(" %d\n", ((-s) % p + p) % p);
        }
        return;
    }
    int base = 1 << j;
    for (int v = 0; v < p; v++) {
        phi[j] = v; bool ok = true;
        for (int P = 0; P < base; P++) {
            int s = sums[P] + v; if (s >= p) s -= p;
            sums[P | base] = s;
            if (inFam[P | base] && ((forb[P | base] >> s) & 1)) { ok = false; break; }
        }
        if (ok) dfs(j + 1);
        if (nsol >= cap) return;
    }
}
int main(int argc, char** argv) {
    p = atoi(argv[1]); famM = atoi(argv[2]); K = atoi(argv[3]);
    for (int i = 0; i < K; i++) a[i] = atoi(argv[4 + i]);
    for (int i = 0; i < K; i++) b[i] = atoi(argv[4 + K + i]);
    for (int i = 0; i < K; i++) l[i] = atoi(argv[4 + 2 * K + i]);
    if (argc > 4 + 3 * K) maxsol = atoll(argv[4 + 3 * K]);
    if (argc > 5 + 3 * K) cap = atoll(argv[5 + 3 * K]);
    int fp = build();
    if (fp >= 0) { printf("full window at P=%d\n", fp); return 0; }
    if (forb[0] & 1u) { printf("P=empty certifies\n"); return 0; }
    sums.assign(1 << (K - 1), 0);
    dfs(0);
    printf("feasible_count %lld%s\n", nsol, nsol >= cap ? " (capped)" : "");
    return 0;
}
