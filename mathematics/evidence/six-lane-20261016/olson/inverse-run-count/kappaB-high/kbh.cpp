// kbh.cpp -- KB_HIGH cycle (kappaB-high/README.md).  Certificate census for all-odd RGR words of
// length 4p-2 with B = kappa >= 1 (so A >= B automatically), every rotation run pure or a (1,1)-pair,
// k >= kmin runs.  Windows (README Sec. 2): for a proper pattern P (bitmask over runs) with m blocks,
//   U_P = min(p - m, D_P + m - 1, floor((D_P + B)/2)),   L_P = U_{P^c},   lambda(P) = U_P + 1.
// Per datum without a full window it reports:
//   SRC : Lemma BC with the single-run partition in CYCLIC order (some start, either direction);
//   SR  : Lemma BC with the single-run partition in SOME order (subset DP);
//   BC3 : Lemma BC with s = 3 (flat 3-partition: sum lambda(P) >= p+1, sum lambda(P^c) >= p+1, (c));
//   BCG : Lemma BC with an arbitrary ordered partition (DP over chains, max sum lambda), k <= bcgmax.
// Modes:  kbh exh p kmin kmax bcgmax           (all rotation-classes of (r,l), all pure/(1,1) splits)
//         kbh rnd p trials seed kmin kmax bcgmax
// Output: one JSON line per datum that has no full window and fails SR (with flags), plus per-k
// summary lines.  Aid only; certificates are value-independent, so "SR/BC3/BCG ok" means every phi is
// killed (Lemma BC, ../../inverse-parity/proof-PAR-K0.md Sec. 2).
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <random>
#include <cstdint>

static int p, K, Bv, bcgmax;
static int a[64], b[64], l[64], d[64];
static std::vector<int> U, Mc, Dp;
static long long st_data[64], st_full[64], st_src[64], st_sr[64], st_bc3[64], st_bcg[64], st_bcgrun[64], st_none[64];
static int printed = 0;

static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }

static void tables() {
    int n = 1 << K; U.assign(n, 0); Mc.assign(n, 0); Dp.assign(n, 0);
    for (int P = 0; P < n; P++) {
        int f2 = 0, D = 0;
        for (int j = 0; j < K; j++) {
            int zj = (P >> j) & 1, zn = (P >> ((j + 1) % K)) & 1;
            f2 += (zj != zn);
            if (zj) D += d[j];
        }
        int m = f2 / 2; Mc[P] = m; Dp[P] = D;
        U[P] = std::min(p - m, std::min(D + m - 1, fl2(D + Bv)));
    }
}
static inline int lam(int P) { return U[P] + 1; }
static inline bool stepok(int X, int Y, int Z) {
    return lam(X | Y) + lam(Y | Z) + lam(Z | X) >= p + 1 && lam(X) + lam(Y) + lam(Z) >= 1;
}

static bool src_chain() {
    int full = (1 << K) - 1; long long suma = 0;
    for (int t = 0; t < K; t++) suma += lam(1 << t);
    if (suma < p + 1) return false;
    for (int dir = 0; dir < 2; dir++)
        for (int s0 = 0; s0 < K; s0++) {
            int X = 0; bool ok = true;
            for (int i = 0; i < K && ok; i++) {
                int t = dir ? (s0 - i + K) % K : (s0 + i) % K;
                int Y = 1 << t;
                if (i == 0) { X = Y; continue; }
                int Z = full & ~(X | Y);
                if (i == K - 1) { ok = lam(Y) + lam(X) >= 1; break; }
                if (!stepok(X, Y, Z)) ok = false;
                X |= Y;
            }
            if (ok) return true;
        }
    return false;
}

static bool sr_dp() {
    int full = (1 << K) - 1; long long suma = 0;
    for (int t = 0; t < K; t++) suma += lam(1 << t);
    if (suma < p + 1) return false;
    std::vector<uint8_t> reach(1 << K, 0);
    for (int t = 0; t < K; t++) reach[1 << t] = 1;
    // process by popcount
    std::vector<std::vector<int>> byc(K + 1);
    for (int X = 1; X < full; X++) byc[__builtin_popcount(X)].push_back(X);
    for (int c = 1; c <= K - 2; c++)
        for (int X : byc[c]) {
            if (!reach[X]) continue;
            for (int t = 0; t < K; t++) {
                if ((X >> t) & 1) continue;
                int Y = 1 << t, Z = full & ~(X | Y);
                if (!Z) continue;
                if (stepok(X, Y, Z)) reach[X | Y] = 1;
            }
        }
    for (int X : byc[K - 1]) {
        if (!reach[X]) continue;
        int Y = full & ~X;
        if (lam(Y) + lam(X) >= 1) return true;
    }
    return false;
}

static bool bc3() {
    int full = (1 << K) - 1;
    // X contains run 0; Y nonempty subset of rest, Z = rest of rest nonempty
    for (int X = 1; X < full; X += 2) {
        int rest = full & ~X;
        for (int Y = rest; Y; Y = (Y - 1) & rest) {
            int Z = rest & ~Y;
            if (!Z) continue;
            if (lam(X) + lam(Y) + lam(Z) < p + 1) continue;
            if (lam(X | Y) + lam(Y | Z) + lam(Z | X) < p + 1) continue;
            if (lam(X) + lam(X ^ full) >= 1 || lam(Y) + lam(Y ^ full) >= 1 || lam(Z) + lam(Z ^ full) >= 1) return true;
        }
    }
    return false;
}

static bool bcg() {
    int full = (1 << K) - 1, n = 1 << K;
    const int NEG = -1000000;
    std::vector<int> best(n, NEG);
    for (int X = 1; X < full; X++) best[X] = lam(X);
    std::vector<int> order; order.reserve(n);
    for (int X = 1; X < full; X++) order.push_back(X);
    std::sort(order.begin(), order.end(), [](int x, int y) { return __builtin_popcount(x) < __builtin_popcount(y); });
    for (int X : order) {
        if (best[X] == NEG) continue;
        int rest = full & ~X;
        for (int Y = (rest - 1) & rest; Y; Y = (Y - 1) & rest) {
            int Z = rest & ~Y;
            if (stepok(X, Y, Z) && best[X] + lam(Y) > best[X | Y]) best[X | Y] = best[X] + lam(Y);
        }
    }
    for (int X = 1; X < full; X++)
        if (best[X] != NEG && best[X] + lam(full & ~X) >= p + 1 && lam(full & ~X) + lam(X) >= 1) return true;
    return false;
}

static void process() {
    int A = 0, B = 0, F = 0, H = 0;
    for (int t = 0; t < K; t++) { A += a[t]; B += b[t]; F += l[t]; H += l[t] / 2; d[t] = a[t] - b[t]; }
    Bv = B;
    tables();
    int full = (1 << K) - 1;
    st_data[K]++;
    for (int P = 1; P < full; P++) if (U[P] + U[full & ~P] >= p - 1) { st_full[K]++; return; }
    bool s1 = src_chain(), s2 = s1 || sr_dp();
    if (s1) st_src[K]++;
    if (s2) { st_sr[K]++; return; }
    bool s3 = (K <= 15) ? bc3() : false;
    if (s3) st_bc3[K]++;
    int s4 = -1;
    if (K <= bcgmax) { st_bcgrun[K]++; s4 = (s3 || bcg()) ? 1 : 0; if (s4) st_bcg[K]++; }
    if (!s3 && s4 != 1) st_none[K]++;
    if (printed < 40) {
        printed++;
        printf("{\"k\":%d,\"B\":%d,\"A\":%d,\"D\":%d,\"SR\":0,\"BC3\":%d,\"BCG\":%d,\"a\":[", K, B, A, A - B, s3 ? 1 : 0, s4);
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", a[t]);
        printf("],\"b\":[");
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", b[t]);
        printf("],\"l\":[");
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", l[t]);
        printf("]}\n");
    }
}

// ---------- exhaustive enumeration ----------
static int r[64];
static int kappa_cur;
static void splits(int i, int Bleft) {
    if (i == K) { if (Bleft == 0) process(); return; }
    // remaining capacity check
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
    int N = 4 * p - 2;
    (void)N;
    if (pos == 2 * K) {
        if (rem) return;
        int H = 0; for (int t = 0; t < K; t++) H += l[t] / 2;
        int kap = p - 1 - H;
        if (kap < 1) return;
        if (!rot_min()) return;
        kappa_cur = kap;
        splits(0, kap);
        return;
    }
    int left = 2 * K - pos - 1;
    for (int v = 1; v <= rem - left; v++) {
        if (pos % 2 == 1 && v % 2 == 0) continue;  // reflection runs odd
        if (pos % 2 == 0) r[pos / 2] = v; else l[pos / 2] = v;
        gen(pos + 1, rem - v);
    }
}

int main(int argc, char** argv) {
    if (argc < 2) return 1;
    if (!strcmp(argv[1], "exh")) {
        p = atoi(argv[2]); int kmin = atoi(argv[3]), kmax = atoi(argv[4]); bcgmax = atoi(argv[5]);
        for (K = kmin; K <= kmax; K++) {
            gen(0, 4 * p - 2);
            printf("{\"summary\":1,\"p\":%d,\"k\":%d,\"data\":%lld,\"full\":%lld,\"SRC\":%lld,\"SR\":%lld,\"BC3_among_SRfail\":%lld,\"BCG_run\":%lld,\"BCG_ok\":%lld,\"none\":%lld}\n",
                   p, K, st_data[K], st_full[K], st_src[K], st_sr[K], st_bc3[K], st_bcgrun[K], st_bcg[K], st_none[K]);
            fflush(stdout);
        }
    } else {
        p = atoi(argv[2]); int T = atoi(argv[3]); unsigned seed = atoi(argv[4]);
        int kmin = atoi(argv[5]), kmax = atoi(argv[6]); bcgmax = atoi(argv[7]);
        std::mt19937 rng(seed);
        int N = 4 * p - 2, done = 0;
        while (done < T) {
            K = kmin + rng() % (kmax - kmin + 1);
            int F = K + 2 * (rng() % (N - 2 * K + 1) / 2 + 0);
            if (F < K || (F - K) % 2) continue;
            int H = (F - K) / 2, kap = p - 1 - H, R = N - F;
            if (kap < 1 || R < K) continue;
            int B = kap, A = R - B;
            // n0 (1,1)-pairs, na anti runs, nal aligned runs
            int n0 = rng() % 3; if (n0 > B) n0 = B;
            int Bp = B - n0, Ap = A - n0;
            int rem = K - n0; if (rem < 1) continue;
            int na = (Bp == 0) ? 0 : 1 + rng() % std::min(Bp, std::max(1, rem - 1));
            int nal = rem - na;
            if (nal < 1 || Ap < nal || (Bp > 0 && na < 1) || (Bp == 0 && na > 0)) continue;
            // compositions
            auto comp = [&](int tot, int parts, std::vector<int>& out) {
                out.assign(parts, 1); for (int i = 0; i < tot - parts; i++) out[rng() % parts]++; };
            std::vector<int> ca, cb, lv;
            comp(Ap, nal, ca); if (na) comp(Bp, na, cb); else cb.clear();
            std::vector<int> kinds; for (int i = 0; i < nal; i++) kinds.push_back(0); for (int i = 0; i < na; i++) kinds.push_back(1); for (int i = 0; i < n0; i++) kinds.push_back(2);
            std::shuffle(kinds.begin(), kinds.end(), rng);
            int ia = 0, ib = 0;
            for (int t = 0; t < K; t++) {
                if (kinds[t] == 0) { a[t] = ca[ia++]; b[t] = 0; }
                else if (kinds[t] == 1) { a[t] = 0; b[t] = cb[ib++]; }
                else { a[t] = 1; b[t] = 1; }
            }
            lv.assign(K, 1); for (int i = 0; i < H; i++) lv[rng() % K] += 2;
            for (int t = 0; t < K; t++) l[t] = lv[t];
            long long before = 0; for (int q = 0; q < 64; q++) before += st_data[q];
            process(); done++;
        }
        for (K = kmin; K <= kmax; K++)
            printf("{\"summary\":1,\"p\":%d,\"k\":%d,\"data\":%lld,\"full\":%lld,\"SRC\":%lld,\"SR\":%lld,\"BC3_among_SRfail\":%lld,\"BCG_run\":%lld,\"BCG_ok\":%lld,\"none\":%lld}\n",
                   p, K, st_data[K], st_full[K], st_src[K], st_sr[K], st_bc3[K], st_bcgrun[K], st_bcg[K], st_none[K]);
    }
    return 0;
}
