// star_study.cpp (derived from bigrun_study.cpp): condition (STAR) of c2/README.md Sec. 5 on big-run words with
// A, B <= 2p-1 and min(A,B) <= kappa.  bigrun_study.cpp -- data study for item (ii) (c2/README.md Sec. 3), aid only.
// Words: all-odd, length 4p-2, k >= p+1, R >= 2p+1, every run pure or a (1,1)-pair, any B (0 <= B, any A),
// with a run u such that |d_u| > 2p - k + 1 (W = 2p-k+1).  Per word report:
//  * nbig (number of such runs; claim: <= 1) and max r over the other runs (claim: <= j = R - 2p);
//  * for each m in [m_lo, m*]: does a zone pattern (x in [kappa, R-kappa]) with m blocks exist?
//  * with s := sign(d_u) and "u in P" meaning the configuration where toggling u moves x by -s*|d_u|:
//    for the best m: min over patterns of x' := (s > 0 ? x : R - x) among patterns with u in P in each of
//    the configurations Fend (u last run of a block of length >= 2), Fstart (u first run of a block of
//    length >= 2), Ssing (u singleton block with a gap of length >= 2 on the left), Ssing2 (gap >= 2 on the
//    right); success of a configuration := some pattern has x' <= R - kappa.
// Usage: bigrun_study p
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>

static int p, K, Bv, Rv, kap;
static int a[64], b[64], l[64], d[64], r[64], rr[64];
static long long n_words = 0, n_nbig_gt1 = 0, n_other_big = 0, n_nozone_all_m = 0;
static long long cfg_ok[4], n_any_cfg = 0, n_none_cfg = 0, n_zone_in_range = 0;
static int printed = 0;

static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static int blocks(unsigned P) { int f2 = 0; for (int t = 0; t < K; t++) { int z = (P >> t) & 1, zn = (P >> ((t + 1) % K)) & 1; f2 += (z != zn); } return f2 / 2; }
static int xof(unsigned P) { int D = 0; for (int t = 0; t < K; t++) if ((P >> t) & 1) D += d[t]; return D + Bv; }

static void process() {
    int A = 0; Bv = 0; int H = 0;
    for (int t = 0; t < K; t++) { A += a[t]; Bv += b[t]; d[t] = a[t] - b[t]; H += l[t] / 2; r[t] = a[t] + b[t]; }
    kap = p - 1 - H; Rv = A + Bv;
    int W = 2 * p - K + 1, j = Rv - 2 * p;
    if (j < 1) return;
    int nbig = 0, u = -1;
    for (int t = 0; t < K; t++) if (std::abs(d[t]) > W) { nbig++; u = t; }
    if (nbig == 0) return;
    if (A > 2 * p - 1 || Bv > 2 * p - 1 || std::min(A, Bv) > kap) return;
    n_words++;
    if (nbig > 1) { n_nbig_gt1++; return; }
    for (int t = 0; t < K; t++) if (t != u && r[t] > j) { n_other_big++; break; }
    int ms = kap / 2 + 1, mlo = std::max(1, (K + 1 - kap + 1) / 2);
    if (K + 1 - kap <= 0) mlo = 1;
    unsigned full = (1u << K) - 1;
    int s = d[u] > 0 ? 1 : -1;
    bool star_any = false, star_mlo = false, star_mlo_free = false;
    for (int m = mlo; m <= ms; m++) {
        int mn = 1 << 30;
        for (unsigned P = 1; P < full; P++) {
            if (blocks(P) != m || !((P >> u) & 1)) continue;
            int x = xof(P); int xq = (s > 0) ? x : Rv - x;
            mn = std::min(mn, xq);
        }
        bool st = (mn <= Rv - kap);
        bool freesite = (K >= 2 * m + 1);
        if (st && freesite) star_any = true;
        if (m == mlo) { star_mlo = st; star_mlo_free = st && freesite; }
    }
    if (star_any) cfg_ok[0]++; else { n_none_cfg++; if (printed < 10) { printed++;
        printf("{\"STAR_FAIL\":1,\"k\":%d,\"R\":%d,\"A\":%d,\"B\":%d,\"kappa\":%d,\"u\":%d,\"d\":[", K, Rv, A, Bv, kap, u);
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", d[t]); printf("]}\n"); } }
    if (star_mlo_free) cfg_ok[1]++;
    if (star_mlo) cfg_ok[2]++;
}
static void splits(int i) {
    if (i == K) { process(); return; }
    a[i] = r[i]; b[i] = 0; splits(i + 1);
    a[i] = 0; b[i] = r[i]; splits(i + 1);
    if (r[i] == 2) { a[i] = 1; b[i] = 1; splits(i + 1); }
}
static bool rot_min() {
    for (int s = 1; s < K; s++) {
        for (int t = 0; t < K; t++) {
            int i1 = t, i2 = (t + s) % K;
            if (rr[i2] != rr[i1]) { if (rr[i2] < rr[i1]) return false; goto nx; }
            if (l[i2] != l[i1]) { if (l[i2] < l[i1]) return false; goto nx; }
        }
        nx:;
    }
    return true;
}
static void gen(int pos, int rem) {
    if (pos == 2 * K) {
        if (rem) return;
        int R = 0, mx = 0; for (int t = 0; t < K; t++) { R += rr[t]; mx = std::max(mx, rr[t]); }
        if (R < 2 * p + 1 || mx <= 2 * p - K + 1 || !rot_min()) return;
        for (int t = 0; t < K; t++) r[t] = rr[t];
        splits(0);
        return;
    }
    int left = 2 * K - pos - 1;
    for (int v = 1; v <= rem - left; v++) {
        if (pos % 2 == 1 && v % 2 == 0) continue;
        if (pos % 2 == 0) rr[pos / 2] = v; else l[pos / 2] = v;
        gen(pos + 1, rem - v);
    }
}

int main(int argc, char** argv) {
    if (argc < 2) return 1;
    p = atoi(argv[1]);
    for (K = p + 1; K <= 2 * p - 2; K++) gen(0, 4 * p - 2);
    printf("{\"p\":%d,\"bigrun_words_in_range\":%lld,\"nbig_gt1\":%lld,\"other_run_gt_j\":%lld,\"STAR_some_m_with_free_site\":%lld,\"STAR_at_mlo_with_free_site\":%lld,\"STAR_at_mlo\":%lld,\"STAR_fail\":%lld}\n",
           p, n_words, n_nbig_gt1, n_other_big, cfg_ok[0], cfg_ok[1], cfg_ok[2], n_none_cfg);
    return 0;
}
