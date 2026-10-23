// zs.cpp -- KB_HIGH cycle (README Sec. 5): exact test of the zero-sum interval certificate ZS on
// KB_HIGH* data (all reflection runs odd, B = kappa >= 1, runs pure or (1,1), k >= kmin).
// Windows from the frozen representation (README Sec. 2): U_P = min(p - m, D_P + m - 1,
// floor((D_P + B)/2)), L_P = U_{P^c}.  For each start s, W = runs s, s+1, ..., s+p-1 (cyclic);
// constraints for every subinterval Q = (i, j] of W (0 <= i < j <= p):
//     lo(i,j) = D_Q - U_Q  <=  Th_j - Th_i  <=  hi(i,j) = D_Q + L_Q,
// decided exactly by Bellman-Ford on nodes 0..p (integer data => integer solution if feasible).
// Reports per k: data, full (some full window), ZS0 (theta = 0 works for some start), ZS (some
// start feasible), and prints data where ZS fails.
// Modes: zs exh p kmin kmax | zs rnd p trials seed kmin kmax | zs one p k a.. b.. l..
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <random>
#include <cstdint>

static int p, K, Bv;
static int a[64], b[64], l[64], d[64], r[64];
static std::vector<int> U;
static long long st_data[64], st_full[64], st_zs0[64], st_zs[64], st_zsfail_nofull[64], st_zsfail_full[64];
static int printed = 0, verbose = 0;

static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static bool use_tab = true;
static inline int Uf(int P) {
    if (use_tab) return U[P];
    int f2 = 0, D = 0;
    for (int j = 0; j < K; j++) {
        int zj = (P >> j) & 1, zn = (P >> ((j + 1) % K)) & 1;
        f2 += (zj != zn); if (zj) D += d[j];
    }
    int m = f2 / 2;
    return std::min(p - m, std::min(D + m - 1, fl2(D + Bv)));
}
static void tables() {
    int n = 1 << K; U.assign(n, 0);
    for (int P = 0; P < n; P++) {
        int f2 = 0, D = 0;
        for (int j = 0; j < K; j++) {
            int zj = (P >> j) & 1, zn = (P >> ((j + 1) % K)) & 1;
            f2 += (zj != zn); if (zj) D += d[j];
        }
        int m = f2 / 2;
        U[P] = std::min(p - m, std::min(D + m - 1, fl2(D + Bv)));
    }
}

// returns 1 if feasible; theta written to th (size p)
static int zs_window(int s, bool zero_only, std::vector<int>* th) {
    int full = (1 << K) - 1;
    int n = p + 1;
    std::vector<int> lo(n * n), hi(n * n), Dq(n * n);
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            int Q = 0, D = 0;
            for (int t = i; t < j; t++) { int run = (s + t) % K; Q |= 1 << run; D += d[run]; }
            int UQ = Uf(Q), LQ = Uf(full & ~Q);
            lo[i * n + j] = D - UQ; hi[i * n + j] = D + LQ;
            if (lo[i * n + j] > hi[i * n + j]) return 0;
            if (zero_only && (lo[i * n + j] > 0 || hi[i * n + j] < 0)) return 0;
        }
    if (zero_only) { if (th) th->assign(p, 0); return 1; }
    // Bellman-Ford: Th_j - Th_i <= hi  (edge i->j, w = hi);  Th_i - Th_j <= -lo (edge j->i, w = -lo)
    std::vector<long long> dist(n, 0);
    for (int it = 0; it <= n; it++) {
        bool ch = false;
        for (int i = 0; i < n; i++)
            for (int j = i + 1; j < n; j++) {
                long long w1 = hi[i * n + j], w2 = -lo[i * n + j];
                if (dist[i] + w1 < dist[j]) { dist[j] = dist[i] + w1; ch = true; }
                if (dist[j] + w2 < dist[i]) { dist[i] = dist[j] + w2; ch = true; }
            }
        if (!ch) {
            if (th) { th->assign(p, 0); for (int t = 0; t < p; t++) (*th)[t] = (int)(dist[t + 1] - dist[t]); }
            return 1;
        }
    }
    return 0;
}

static void process() {
    int A = 0, B = 0;
    for (int t = 0; t < K; t++) { A += a[t]; B += b[t]; d[t] = a[t] - b[t]; }
    Bv = B; use_tab = (K <= 16); if (use_tab) tables();
    int full = (1 << K) - 1;
    st_data[K]++;
    bool fw = false;
    if (use_tab) for (int P = 1; P < full && !fw; P++) if (U[P] + U[full & ~P] >= p - 1) fw = true;
    if (fw) st_full[K]++;
    bool z0 = false, z = false; int zs_start = -1;
    for (int s = 0; s < K && !z0; s++) if (zs_window(s, true, nullptr)) { z0 = true; z = true; zs_start = s; }
    for (int s = 0; s < K && !z; s++) if (zs_window(s, false, nullptr)) { z = true; zs_start = s; }
    if (z0) st_zs0[K]++;
    if (z) st_zs[K]++;
    else { if (fw) st_zsfail_full[K]++; else st_zsfail_nofull[K]++; }
    if ((!z && printed < 30) || verbose) {
        printed++;
        printf("{\"k\":%d,\"B\":%d,\"A\":%d,\"D\":%d,\"full\":%d,\"ZS0\":%d,\"ZS\":%d,\"start\":%d,\"a\":[", K, B, A, A - B, fw ? 1 : 0, z0 ? 1 : 0, z ? 1 : 0, zs_start);
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", a[t]);
        printf("],\"b\":["); for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", b[t]);
        printf("],\"l\":["); for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", l[t]);
        printf("]");
        if (z && verbose) {
            std::vector<int> th; zs_window(zs_start, false, &th);
            printf(",\"theta\":["); for (int t = 0; t < p; t++) printf("%s%d", t ? "," : "", th[t]); printf("]");
        }
        printf("}\n");
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
        int H = 0; for (int t = 0; t < K; t++) H += l[t] / 2;
        int kap = p - 1 - H;
        if (kap < 1) return;
        if (!rot_min()) return;
        splits(0, kap);
        return;
    }
    int left = 2 * K - pos - 1;
    for (int v = 1; v <= rem - left; v++) {
        if (pos % 2 == 1 && v % 2 == 0) continue;
        if (pos % 2 == 0) r[pos / 2] = v; else l[pos / 2] = v;
        gen(pos + 1, rem - v);
    }
}
static void summary(int kmin, int kmax) {
    for (int k = kmin; k <= kmax; k++)
        printf("{\"summary\":1,\"p\":%d,\"k\":%d,\"data\":%lld,\"full\":%lld,\"ZS0\":%lld,\"ZS\":%lld,\"ZSfail_nofull\":%lld,\"ZSfail_full\":%lld}\n",
               p, k, st_data[k], st_full[k], st_zs0[k], st_zs[k], st_zsfail_nofull[k], st_zsfail_full[k]);
}

int main(int argc, char** argv) {
    if (argc < 2) return 1;
    if (!strcmp(argv[1], "exh")) {
        p = atoi(argv[2]); int kmin = atoi(argv[3]), kmax = atoi(argv[4]);
        for (K = kmin; K <= kmax; K++) { gen(0, 4 * p - 2); fflush(stdout); }
        summary(kmin, kmax);
    } else if (!strcmp(argv[1], "one")) {
        p = atoi(argv[2]); K = atoi(argv[3]); verbose = 1;
        for (int t = 0; t < K; t++) a[t] = atoi(argv[4 + t]);
        for (int t = 0; t < K; t++) b[t] = atoi(argv[4 + K + t]);
        for (int t = 0; t < K; t++) l[t] = atoi(argv[4 + 2 * K + t]);
        process(); summary(K, K);
    } else {
        p = atoi(argv[2]); int T = atoi(argv[3]); unsigned seed = atoi(argv[4]);
        int kmin = atoi(argv[5]), kmax = atoi(argv[6]);
        std::mt19937 rng(seed);
        int N = 4 * p - 2, done = 0;
        while (done < T) {
            K = kmin + rng() % (kmax - kmin + 1);
            int Fmax = N - K; if (Fmax < K) continue;
            int F = K + 2 * (int)(rng() % ((Fmax - K) / 2 + 1));
            int H = (F - K) / 2, kap = p - 1 - H, R = N - F;
            if (kap < 1 || R < K) continue;
            int B = kap, A = R - B;
            int n0 = rng() % 3; if (n0 > B) n0 = B;
            int Bp = B - n0, Ap = A - n0, rem = K - n0;
            if (rem < 1) continue;
            int na = (Bp == 0) ? 0 : 1 + (int)(rng() % std::min(Bp, std::max(1, rem - 1)));
            int nal = rem - na;
            if (nal < 1 || Ap < nal || (Bp > 0 && na < 1) || (Bp == 0 && na > 0)) continue;
            std::vector<int> ca(nal, 1), cb(na, 1);
            for (int i = 0; i < Ap - nal; i++) ca[rng() % nal]++;
            for (int i = 0; i < Bp - na; i++) cb[rng() % na]++;
            std::vector<int> kinds;
            for (int i = 0; i < nal; i++) kinds.push_back(0);
            for (int i = 0; i < na; i++) kinds.push_back(1);
            for (int i = 0; i < n0; i++) kinds.push_back(2);
            std::shuffle(kinds.begin(), kinds.end(), rng);
            int ia = 0, ib = 0;
            for (int t = 0; t < K; t++) {
                if (kinds[t] == 0) { a[t] = ca[ia++]; b[t] = 0; }
                else if (kinds[t] == 1) { a[t] = 0; b[t] = cb[ib++]; }
                else { a[t] = 1; b[t] = 1; }
                l[t] = 1;
            }
            for (int i = 0; i < H; i++) l[rng() % K] += 2;
            process(); done++;
        }
        summary(kmin, kmax);
    }
    return 0;
}
