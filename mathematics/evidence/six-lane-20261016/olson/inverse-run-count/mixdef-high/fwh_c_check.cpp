// fwh_c_check.cpp (derived from zsib_check.cpp): Claim 1 of Theorem FWH for R >= 2p with every m in
// [m_lo, m*], m_lo = ceil((k+1-kappa)/2), and the free-site condition k >= 2 m_lo + 1.
// zsib_check.cpp -- exact check of Lemma ZSI-B (proof-MH.md Sec. 4) and of the window part of Theorem FWH
// (proof-MH.md Sec. 3).  Aid only.
// (1) Boundary data: all-odd words with k = p+1 runs and kB = kappa - B = 1, runs pure or (1,1), any B >= 1
//     with B <= A (A <= 2p-1 not required here).  For each datum compare
//       ZSI  := Lemma ZS feasible for some window of p consecutive runs (Bellman-Ford with exact windows), and
//       CRIT := every proper cyclic interval Q has D_Q <= min(2|Q| + B, |Q| + p - 1).
//     Lemma ZSI-B claims ZSI <=> CRIT.
// (2) For every NMH-type datum (all-odd, k >= p+1, B >= 1 any, any kappa) with R in {2p-1, 2p}: every pattern
//     with m* = floor(kappa/2)+1 blocks and E+ in [kappa, R-kappa] has a full window (Claim 1 of FWH), and the
//     continuity hypotheses hold (k >= 2m*+1, max r_u <= 2p-k+1).
// Modes: zsib exh p   (all rotation classes; k = p+1 for (1), k = p+1..2p-2 for (2))
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <cstdint>

static int p, K, Bv, Av, kB, Dv, Rv, kap;
static int a[64], b[64], l[64], d[64], r[64];
static long long n1 = 0, n1_zsi = 0, n1_crit = 0, n1_mismatch = 0;
static long long n2 = 0, n2_claim_fail = 0, n2_hyp_fail = 0, n2_patterns = 0;
static int printed = 0;

static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline int g(int m, int E) { return std::min(p - m, std::min(E + m - 1 - kap, fl2(E))); }

static int Mof(int P) { int f2 = 0; for (int j = 0; j < K; j++) { int zj = (P >> j) & 1, zn = (P >> ((j + 1) % K)) & 1; f2 += (zj != zn); } return f2 / 2; }
static int Dof(int P) { int D = 0; for (int j = 0; j < K; j++) if ((P >> j) & 1) D += d[j]; return D; }
static int Uw(int P) { return g(Mof(P), Dof(P) + Bv); }
static int Lw(int P) { return g(Mof(P), Rv - Dof(P) - Bv); }

static bool zsi() {
    int n = p + 1;
    std::vector<int> lo(n * n), hi(n * n);
    for (int s = 0; s < K; s++) {
        bool bad = false;
        for (int i = 0; i < n && !bad; i++)
            for (int j = i + 1; j < n; j++) {
                int Q = 0, D = 0;
                for (int t = i; t < j; t++) { int run = (s + t) % K; Q |= 1 << run; D += d[run]; }
                lo[i * n + j] = D - Uw(Q); hi[i * n + j] = D + Lw(Q);
                if (lo[i * n + j] > hi[i * n + j]) { bad = true; break; }
            }
        if (bad) continue;
        std::vector<long long> dist(n, 0); bool conv = false;
        for (int it = 0; it <= n; it++) {
            bool ch = false;
            for (int i = 0; i < n; i++)
                for (int j = i + 1; j < n; j++) {
                    long long w1 = hi[i * n + j], w2 = -lo[i * n + j];
                    if (dist[i] + w1 < dist[j]) { dist[j] = dist[i] + w1; ch = true; }
                    if (dist[j] + w2 < dist[i]) { dist[i] = dist[j] + w2; ch = true; }
                }
            if (!ch) { conv = true; break; }
        }
        if (conv) return true;
    }
    return false;
}
static bool crit() {
    for (int i = 0; i < K; i++)
        for (int len = 1; len < K; len++) {
            int D = 0; for (int t = 0; t < len; t++) D += d[(i + t) % K];
            if (D > std::min(2 * len + Bv, len + p - 1)) return false;
        }
    return true;
}

static void process() {
    Av = 0; Bv = 0; int H = 0, maxr = 0;
    for (int t = 0; t < K; t++) { Av += a[t]; Bv += b[t]; d[t] = a[t] - b[t]; H += l[t] / 2; maxr = std::max(maxr, a[t] + b[t]); }
    kap = p - 1 - H; kB = kap - Bv; Dv = Av - Bv; Rv = Av + Bv;
    if (Rv >= 2 * p) {
        n2++;
        int ms = kap / 2 + 1, mlo = (K + 1 - kap + 1) / 2;   // ceil((K+1-kap)/2)
        if ((K + 1 - kap) <= 0) mlo = 1;
        if (!(K >= 2 * mlo + 1) || mlo > ms) n2_hyp_fail++;
        int full = (1 << K) - 1;
        for (int P = 1; P < full; P++) {
            int m = Mof(P);
            if (m < mlo || m > ms) continue;
            int x = Dof(P) + Bv;
            if (x < kap || x > Rv - kap) continue;
            n2_patterns++;
            if (Uw(P) + Lw(P) + 1 < p) { n2_claim_fail++; if (printed < 20) { printed++; printf("{\"FWH_C_CLAIM1_FAIL\":1,\"k\":%d,\"R\":%d,\"m\":%d,\"P\":%d}\n", K, Rv, m, P); } }
        }
    }
}
static void splits(int i, int Bleft) {
    if (i == K) { if (Bleft == 0) process(); return; }
    a[i] = r[i]; b[i] = 0; splits(i + 1, Bleft);
    if (r[i] <= Bleft) { a[i] = 0; b[i] = r[i]; splits(i + 1, Bleft - r[i]); }
    if (r[i] == 2 && Bleft >= 1) { a[i] = 1; b[i] = 1; splits(i + 1, Bleft - 1); }
}
static bool rot_min() {
    for (int s = 1; s < K; s++) {
        for (int t = 0; t < K; t++) {
            int i1 = t, i2 = (t + s) % K;
            if (r[i2] != r[i1]) { if (r[i2] < r[i1]) return false; goto nx; }
            if (l[i2] != l[i1]) { if (l[i2] < l[i1]) return false; goto nx; }
        }
        nx:;
    }
    return true;
}
static void gen(int pos, int rem) {
    if (pos == 2 * K) {
        if (rem) return;
        int H = 0, R = 0; for (int t = 0; t < K; t++) { H += l[t] / 2; R += r[t]; }
        int kp = p - 1 - H;
        if (kp < 1 || !rot_min()) return;
        bool want1 = false;
        bool want2 = (R >= 2 * p);
        if (!want1 && !want2) return;
        for (int B = 1; B <= R; B++) {
            if (R - B < B) break;
            if (want1 && !want2 && kp - B != 1) continue;
            splits(0, B);
        }
        return;
    }
    int left = 2 * K - pos - 1;
    for (int v = 1; v <= rem - left; v++) {
        if (pos % 2 == 1 && v % 2 == 0) continue;
        if (pos % 2 == 0) r[pos / 2] = v; else l[pos / 2] = v;
        gen(pos + 1, rem - v);
    }
}

int main(int argc, char** argv) {
    if (argc < 3 || strcmp(argv[1], "exh")) return 1;
    p = atoi(argv[2]);
    for (K = p + 1; K <= 2 * p - 2; K++) gen(0, 4 * p - 2);
    printf("{\"p\":%d,\"R_ge_2p_data\":%lld,\"claim1_patterns_all_m_in_range\":%lld,\"claim1_fail\":%lld,\"free_site_or_range_fail\":%lld}\n",
           p, n2, n2_patterns, n2_claim_fail, n2_hyp_fail);
    return 0;
}
