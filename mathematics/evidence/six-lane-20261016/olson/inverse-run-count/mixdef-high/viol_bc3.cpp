// viol_bc3.cpp (derived from bc3scan.cpp): boundary words (k = p+1, kB = 1, R <= 2p-3) violating (4.1);
// print the flat 3-partition certificate found (or NO_BC3).
// mhc.cpp -- MIX_DEF_HIGH census (README Secs. 3-4).  Data NMH(p): all reflection runs odd,
// p+1 <= k <= 2p-2 runs, every run pure (a_t b_t = 0) or a (1,1)-pair, 1 <= B <= kappa-1,
// B <= A <= 2p-1.  Windows (README Sec. 2): U_P = min(p-m, D_P + m - 1 - kB, floor((D_P+B)/2)),
// L_P = U(m, D - D_P); empty/full patterns never kill in NMH (corrected Lemma H).
// Per datum: FULL (some full window), ZSI (interval ZS feasible for some window of p consecutive
// runs; Bellman-Ford), BC3 (flat 3-partition Lemma BC certificate; only if no FULL and k <= bc3max),
// and the exact phi-search (DFS, phi_{k-1} = -sum) with pattern families m <= 1, m <= 2, all:
//   IK  = no phi avoids all interval windows;  M2K = intervals insufficient but m <= 2 suffice;
//   M3K = m <= 2 insufficient, all patterns kill;  AVOIDER = some phi avoids every window.
// Modes:  mhc exh p kmin kmax bc3max  |  mhc rnd p trials seed kmin kmax bc3max
// Output: per-(k, Rclass, kB) summary lines + examples (all AVOIDERs, first examples of M2K/M3K).
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <random>
#include <cstdint>
#include <map>
#include <tuple>

static int p, K, Bv, Av, kB, Dv, Rv, kap, bc3max;
static int a[64], b[64], l[64], d[64], r[64];
static std::vector<int16_t> Ut, Lt;
static std::vector<uint8_t> Mt;
static int printed_av = 0, printed_m2 = 0, printed_m3 = 0, printed_noZ = 0;

struct Stat { long long data = 0, full = 0, zsi = 0, bc3 = 0, ik = 0, m2k = 0, m3k = 0, av = 0, nofull_nozsi = 0; };
static std::map<std::tuple<int, int, int>, Stat> stats;   // (k, Rclass, kB); Rclass = R - (2p-3) clipped to [-1..3]

static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline int Uf(int m, int Dp) { return std::min(p - m, std::min(Dp + m - 1 - kB, fl2(Dp + Bv))); }

static void tables() {
    int n = 1 << K; Ut.assign(n, 0); Lt.assign(n, 0); Mt.assign(n, 0);
    for (int P = 0; P < n; P++) {
        int f2 = 0, D = 0;
        for (int j = 0; j < K; j++) {
            int zj = (P >> j) & 1, zn = (P >> ((j + 1) % K)) & 1;
            f2 += (zj != zn); if (zj) D += d[j];
        }
        int m = f2 / 2; Mt[P] = (uint8_t)m;
        Ut[P] = (int16_t)Uf(m, D); Lt[P] = (int16_t)Uf(m, Dv - D);
    }
}

static bool zsi() {
    if (K < p + 1) return false;
    int full = (1 << K) - 1, n = p + 1;
    std::vector<int> lo(n * n), hi(n * n);
    for (int s = 0; s < K; s++) {
        bool bad = false;
        for (int i = 0; i < n && !bad; i++)
            for (int j = i + 1; j < n; j++) {
                int Q = 0, D = 0;
                for (int t = i; t < j; t++) { int run = (s + t) % K; Q |= 1 << run; D += d[run]; }
                lo[i * n + j] = D - Ut[Q]; hi[i * n + j] = D + Lt[Q];
                if (lo[i * n + j] > hi[i * n + j]) { bad = true; break; }
            }
        if (bad) continue;
        (void)full;
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

static inline int lam(int P) { return Ut[P] + 1; }
static int lastX, lastY, lastZ;
static bool bc3ok(int X, int Y, int Z) {
    int full = (1 << K) - 1;
    if (lam(X) + lam(Y) + lam(Z) < p + 1) return false;
    if (lam(X | Y) + lam(Y | Z) + lam(Z | X) < p + 1) return false;
    return lam(X) + lam(full ^ X) >= 1 || lam(Y) + lam(full ^ Y) >= 1 || lam(Z) + lam(full ^ Z) >= 1;
}
static bool bc3i() {   // three cyclic intervals
    for (int i = 0; i < K; i++) for (int j = i + 1; j < K; j++) for (int q = j + 1; q < K; q++) {
        int X = 0, Y = 0, Z = 0;
        for (int t = 0; t < K; t++) { if (t >= i && t < j) Y |= 1 << t; else if (t >= j && t < q) Z |= 1 << t; else X |= 1 << t; }
        if (bc3ok(X, Y, Z)) { lastX = X; lastY = Y; lastZ = Z; return true; }
    }
    return false;
}
static bool bc3() {
    int full = (1 << K) - 1;
    // assign runs 1..K-1 to X/Y/Z (run 0 in X); enumerate via base-3 counter
    std::vector<int> asg(K, 0);
    long long tot = 1; for (int i = 1; i < K; i++) tot *= 3;
    for (long long c = 0; c < tot; c++) {
        long long cc = c; int X = 1, Y = 0, Z = 0;
        for (int i = 1; i < K; i++) { int v = cc % 3; cc /= 3; if (v == 0) X |= 1 << i; else if (v == 1) Y |= 1 << i; else Z |= 1 << i; }
        if (!Y || !Z || Y > Z) continue;   // Y, Z symmetric
        if (lam(X) + lam(Y) + lam(Z) < p + 1) continue;
        if (lam(X | Y) + lam(Y | Z) + lam(Z | X) < p + 1) continue;
        if (lam(X) + lam(full ^ X) >= 1 || lam(Y) + lam(full ^ Y) >= 1 || lam(Z) + lam(full ^ Z) >= 1) { lastX = X; lastY = Y; lastZ = Z; return true; }
    }
    return false;
}

// ---- exact phi DFS over a pattern family ----
static std::vector<uint32_t> forb;     // indexed by P (bit K-1 == 0)
static std::vector<std::vector<int>> lists;   // lists[j] = P subset [0,j) such that P | 1<<j is in family
static std::vector<int> sums;
static int phi[64];
static bool found;
static void build_family(int famM) {
    int np = 1 << (K - 1);
    forb.assign(np, 0);
    uint32_t fullmask = (1u << p) - 1;
    for (int P = 1; P < np; P++) {
        int lo = -Lt[P], hi = Ut[P];
        if (lo > hi) continue;
        uint32_t msk = 0;
        for (int x = lo; x <= hi; x++) msk |= 1u << (((x % p) + p) % p);
        forb[P] = msk & fullmask;
    }
    lists.assign(K, {});
    for (int j = 0; j < K - 1; j++)
        for (int P = 0; P < (1 << j); P++) {
            int Q = P | (1 << j);
            if (Mt[Q] <= famM) lists[j].push_back(P);
        }
    sums.assign(np, 0);
}
static void dfs(int j) {
    if (found) return;
    if (j == K - 1) { found = true; return; }
    for (int v = 0; v < p && !found; v++) {
        bool ok = true;
        for (int P : lists[j]) {
            int s = sums[P] + v; if (s >= p) s -= p;
            int Q = P | (1 << j);
            if ((forb[Q] >> s) & 1) { ok = false; break; }
            sums[Q] = s;   // family patterns only; sub-patterns of family patterns are in the family
        }
        if (!ok) continue;
        phi[j] = v;
        dfs(j + 1);
    }
}
static bool feasible(int famM) { build_family(famM); found = false; sums[0] = 0; dfs(0); return found; }

static void print_datum(const char* tag) {
    printf("{\"%s\":1,\"p\":%d,\"k\":%d,\"R\":%d,\"A\":%d,\"B\":%d,\"kappa\":%d,\"kB\":%d,\"a\":[", tag, p, K, Rv, Av, Bv, kap, kB);
    for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", a[t]);
    printf("],\"b\":["); for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", b[t]);
    printf("],\"l\":["); for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", l[t]);
    printf("],\"phi\":["); for (int t = 0; t < K - 1; t++) printf("%s%d", t ? "," : "", phi[t]);
    printf("]}\n"); fflush(stdout);
}

static void print_part() {
    int full = (1 << K) - 1;
    printf("{\"BC3G_example\":1,\"p\":%d,\"k\":%d,\"R\":%d,\"B\":%d,\"kB\":%d,\"d\":[", p, K, Rv, Bv, kB);
    for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", d[t]);
    printf("],\"part\":\"");
    for (int t = 0; t < K; t++) printf("%c", (lastX >> t) & 1 ? 'X' : (lastY >> t) & 1 ? 'Y' : 'Z');
    int Ps[3] = {lastX, lastY, lastZ};
    printf("\",\"m_DQ_lam_lamc\":[");
    for (int i = 0; i < 3; i++) { int P = Ps[i], D = 0; for (int t = 0; t < K; t++) if ((P >> t) & 1) D += d[t];
        printf("%s[%d,%d,%d,%d]", i ? "," : "", (int)Mt[P], D, lam(P), lam(full ^ P)); }
    printf("]}\n"); fflush(stdout);
}
static void process() {
    Av = 0; Bv = 0; int H = 0;
    for (int t = 0; t < K; t++) { Av += a[t]; Bv += b[t]; d[t] = a[t] - b[t]; H += l[t] / 2; }
    kap = p - 1 - H; kB = kap - Bv; Dv = Av - Bv; Rv = Av + Bv;
    int rc = Rv - (2 * p - 3); if (rc < -1) rc = -1; if (rc > 3) rc = 3;
    Stat& S = stats[std::make_tuple(K, rc, kB)];
    S.data++;
    if (Rv > 2 * p - 3 || K != p + 1 || kB != 1) return;
    { bool ok = true;
      for (int i = 0; i < K && ok; i++) for (int len = 1; len < K && ok; len++) {
          int D = 0; for (int t = 0; t < len; t++) D += d[(i + t) % K];
          if (D > std::min(2 * len + Bv, len + p - 1)) ok = false; }
      if (ok) return; }
    tables();
    static long long n_i = 0, n_g = 0, n_none = 0, n_tot = 0, n_skip = 0; static int pr = 0;
    n_tot++;
    bool bi = bc3i();
    if (bi) { n_i++; S.bc3++; print_part(); }
    else if (K <= bc3max) {
        bool bg = bc3();
        if (bg) { n_g++; S.zsi++; print_part(); }
        else { n_none++; S.av++; print_datum("NO_BC3"); }
    } else { n_skip++; S.m3k++; }
    if ((n_tot & 0xffff) == 0) fprintf(stderr, "tot %lld interval %lld general %lld none %lld skipped %lld\n", n_tot, n_i, n_g, n_none, n_skip);
}
static void splits(int i, int Bleft) {
    if (i == K) {
        // B = (target) handled by caller loop
        if (Bleft == 0) process();
        return;
    }
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
        if (kp < 2) return;
        if (!rot_min()) return;
        for (int B = 1; B <= kp - 1; B++) {
            int A = R - B;
            if (A < B || A > 2 * p - 1) continue;
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

static void summary() {
    for (auto& kv : stats) {
        int k, rc, kb; std::tie(k, rc, kb) = kv.first; const Stat& S = kv.second;
        printf("{\"summary\":1,\"p\":%d,\"k\":%d,\"R_minus_2p\":%s,\"kB\":%d,\"data\":%lld,\"unused_full\":%lld,\"BC3G_only\":%lld,\"unused\":%lld,\"BC3I\":%lld,\"u1\":%lld,\"u2\":%lld,\"SKIPPED\":%lld,\"NONE\":%lld}\n",
               p, k, rc == -1 ? "\"<=-3\"" : rc == 0 ? "-3" : rc == 1 ? "-2" : rc == 2 ? "-1" : "\">=0\"",
               kb, S.data, S.full, S.zsi, S.nofull_nozsi, S.bc3, S.ik, S.m2k, S.m3k, S.av);
    }
    fflush(stdout);
}

int main(int argc, char** argv) {
    if (argc < 2) return 1;
    if (!strcmp(argv[1], "one")) {   // validation: one datum, no NMH filter
        p = atoi(argv[2]); K = atoi(argv[3]); bc3max = 0;
        for (int t = 0; t < K; t++) a[t] = atoi(argv[4 + t]);
        for (int t = 0; t < K; t++) b[t] = atoi(argv[4 + K + t]);
        for (int t = 0; t < K; t++) l[t] = atoi(argv[4 + 2 * K + t]);
        printed_m2 = printed_m3 = -1000;
        process(); summary(); return 0;
    }
    if (!strcmp(argv[1], "exh")) {
        p = atoi(argv[2]); int kmin = atoi(argv[3]), kmax = atoi(argv[4]); bc3max = atoi(argv[5]);
        for (K = kmin; K <= kmax; K++) { gen(0, 4 * p - 2); fprintf(stderr, "done k=%d\n", K); }
        summary();
    } else {
        p = atoi(argv[2]); int T = atoi(argv[3]); unsigned seed = atoi(argv[4]);
        int kmin = atoi(argv[5]), kmax = atoi(argv[6]); bc3max = atoi(argv[7]);
        std::mt19937 rng(seed);
        int N = 4 * p - 2, done = 0;
        while (done < T) {
            K = kmin + rng() % (kmax - kmin + 1);
            int Hmax = (N - 2 * K) / 2; if (Hmax < 0) continue;
            int H = rng() % (Hmax + 1);
            int kp = p - 1 - H; if (kp < 2) continue;
            int B = 1 + rng() % (kp - 1);
            int F = K + 2 * H, R = N - F, A = R - B;
            if (R < K || A < B || A > 2 * p - 1) continue;
            int n0 = rng() % 3; if (n0 > B) n0 = B;
            int Bp = B - n0, Ap = A - n0, rem = K - n0;
            if (rem < 1) continue;
            int na = (Bp == 0) ? 0 : 1 + (int)(rng() % std::min(Bp, std::max(1, rem - 1)));
            int nal = rem - na;
            if (nal < 1 || Ap < nal || (Bp > 0 && na < 1) || (Bp == 0 && na > 0) || Bp < na) continue;
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
        summary();
    }
    return 0;
}
