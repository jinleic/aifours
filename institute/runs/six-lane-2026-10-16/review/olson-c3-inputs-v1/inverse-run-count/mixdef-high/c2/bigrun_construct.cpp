// bigrun_construct.cpp -- test of the item (ii) construction (c2/README.md Sec. 6), aid only.
// Words: all-odd, length 4p-2, k >= p+1, R >= 2p+1, runs pure or (1,1), A, B <= 2p-1, min(A,B) <= kappa,
// with a run u, |d_u| >= W+1 (W = 2p-k+1).  Flip-normalise d_u > 0 (swap a <-> b; then x -> R - x).
// Construction of Q (u not in Q) with m blocks, m in [m_lo, m_max], and x(Q) >= kappa; then P0 = Q^c,
// rotation path P0 -> P0^c, and verification that some pattern on the path has x in [kappa, R-kappa] and a
// full window (exact window formula).  Also checks the claimed facts: other runs r_v <= j, N_alpha >= 2 tau.
// Modes: exh p | rnd p trials seed
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <random>

static int p, K, Bv, Av, Rv, kap;
static int a[64], b[64], l[64], d[64], r[64], rr[64];
static long long n_words = 0, n_fail[16], n_case[4];
static int printed = 0;
static std::mt19937 rng;

static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline int g(int m, int E) { return std::min(p - m, std::min(E + m - 1 - kap, fl2(E))); }
static int blocks(const std::vector<char>& in) { int f2 = 0; for (int t = 0; t < K; t++) f2 += (in[t] != in[(t + 1) % K]); return f2 / 2; }
static int xof(const std::vector<char>& in) { int D = 0; for (int t = 0; t < K; t++) if (in[t]) D += d[t]; return D + Bv; }

static void fail(int code) {
    n_fail[code]++;
    if (printed < 15) { printed++;
        printf("{\"FAIL\":%d,\"k\":%d,\"R\":%d,\"A\":%d,\"B\":%d,\"kappa\":%d,\"d\":[", code, K, Rv, Av, Bv, kap);
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", d[t]); printf("]}\n"); }
}

static void process() {
    Av = 0; Bv = 0; int H = 0;
    for (int t = 0; t < K; t++) { Av += a[t]; Bv += b[t]; H += l[t] / 2; r[t] = a[t] + b[t]; }
    kap = p - 1 - H; Rv = Av + Bv;
    int W = 2 * p - K + 1, j = Rv - 2 * p;
    if (j < 1) return;
    if (Av > 2 * p - 1 || Bv > 2 * p - 1 || std::min(Av, Bv) > kap) return;
    int u = -1, nbig = 0;
    for (int t = 0; t < K; t++) if (std::abs(a[t] - b[t]) >= W + 1) { nbig++; u = t; }
    if (nbig == 0) return;
    n_words++;
    if (nbig > 1) { fail(1); return; }
    // flip-normalise
    int sgn = (a[u] - b[u] > 0) ? 1 : -1;
    int aa[64], bb[64];
    for (int t = 0; t < K; t++) { aa[t] = sgn > 0 ? a[t] : b[t]; bb[t] = sgn > 0 ? b[t] : a[t]; }
    int B2 = 0; for (int t = 0; t < K; t++) { d[t] = aa[t] - bb[t]; B2 += bb[t]; }
    int Bsave = Bv; Bv = B2;   // windows of the flipped word: x -> R - x, same g
    for (int t = 0; t < K; t++) if (t != u && r[t] > j) { fail(2); Bv = Bsave; return; }
    int tau = kap - Bv;
    int Nal = 0; for (int t = 0; t < K; t++) if (t != u && d[t] > 0) Nal += aa[t];
    if (Nal < 2 * tau) { fail(3); }
    int ms = kap / 2 + 1, mlo = std::max(1, (K + 1 - kap + 1) / 2);
    if (K + 1 - kap <= 0) mlo = 1;
    int mmax = std::min(ms, (K - 1) / 2);
    if (mlo > mmax) { fail(4); Bv = Bsave; return; }
    // Omega order: u+1, ..., u-1
    std::vector<int> om; for (int i = 1; i < K; i++) om.push_back((u + i) % K);
    // classes: 1 aligned (d>0), -1 anti (d<0), 0 pair (d==0)
    std::vector<char> inQ(K, 0);
    // alpha-stretches: within maximal beta-free intervals, from first to last aligned run
    std::vector<std::pair<int,int>> st;   // indices into om
    int i = 0, n = (int)om.size();
    while (i < n) {
        if (d[om[i]] < 0) { i++; continue; }
        int jj = i; while (jj < n && d[om[jj]] >= 0) jj++;
        int f = -1, la = -1;
        for (int q = i; q < jj; q++) if (d[om[q]] > 0) { if (f < 0) f = q; la = q; }
        if (f >= 0) st.push_back({f, la});
        i = jj;
    }
    int c = (int)st.size();
    int m;
    if (c >= mlo && c <= mmax) { n_case[0]++; m = c; for (auto& s : st) for (int q = s.first; q <= s.second; q++) inQ[om[q]] = 1; }
    else if (c > mmax) {
        n_case[1]++; m = mmax;
        std::vector<std::pair<int,int>> w;
        for (int s = 0; s < c; s++) { int M = 0; for (int q = st[s].first; q <= st[s].second; q++) M += d[om[q]]; w.push_back({-M, s}); }
        std::sort(w.begin(), w.end());
        for (int s = 0; s < mmax; s++) { auto& S = st[w[s].second]; for (int q = S.first; q <= S.second; q++) inQ[om[q]] = 1; }
    } else {
        n_case[2]++; m = mlo;
        for (auto& s : st) for (int q = s.first; q <= s.second; q++) inQ[om[q]] = 1;
        while (blocks(inQ) < mlo) {
            int bestv = -1, bestc = 1 << 30;
            for (int v = 0; v < K; v++) {
                if (v == u) continue;
                int vl = (v - 1 + K) % K, vr = (v + 1) % K;
                if (inQ[vl] != inQ[v] || inQ[vr] != inQ[v]) continue;
                int cost = inQ[v] ? d[v] : -d[v];   // loss in D_Q caused by flipping v
                if (cost < bestc) { bestc = cost; bestv = v; }
            }
            if (bestv < 0) { fail(5); Bv = Bsave; return; }
            inQ[bestv] ^= 1;
        }
    }
    if (inQ[u]) { fail(6); Bv = Bsave; return; }
    int mq = blocks(inQ);
    if (mq != m || m < mlo || m > mmax || K < 2 * m + 1) { fail(7); Bv = Bsave; return; }
    int xq = xof(inQ);
    if (xq < kap) { fail(8); Bv = Bsave; return; }
    // P0 = complement of Q (contains u), x(P0) = R - xq <= R - kappa; rotation path from P0
    std::vector<char> P(K); for (int t = 0; t < K; t++) P[t] = !inQ[t];
    // cut sites: site q separates runs q and q+1
    std::vector<int> cs; for (int q = 0; q < K; q++) if (P[q] != P[(q + 1) % K]) cs.push_back(q);
    int nc = (int)cs.size();
    // choose i* with gap >= 2 to its successor
    int ist = -1;
    for (int t = 0; t < nc; t++) { int nx = cs[(t + 1) % nc]; int gap = (nx - cs[t] + K) % K; if (gap >= 2) { ist = t; break; } }
    if (ist < 0) { fail(9); Bv = Bsave; return; }
    std::vector<int> pos(nc), orig(nc);
    for (int t = 0; t < nc; t++) { pos[t] = cs[(ist + t) % nc]; }   // pos[0] = i*, pos[1] = successor
    orig = pos;
    std::vector<char> occ(K, 0); for (int q : pos) occ[q] = 1;
    bool found = false, okfull = false;
    auto check = [&]() {
        int x = xof(P);
        if (!found && x >= kap && x <= Rv - kap) { found = true; int mm = blocks(P); okfull = (g(mm, x) + g(mm, Rv - x) + 1 >= p) && mm == m; }
    };
    check();
    auto step = [&](int idx) -> bool { int q = pos[idx], q1 = (q + 1) % K; if (occ[q1]) return false; occ[q] = 0; occ[q1] = 1; pos[idx] = q1; P[q1] ^= 1; check(); return true; };
    // ALT: i* (index 0) to orig[1]-1; then indices nc-1 down to 1 to orig[next]; then i* to orig[1]
    int target0 = (orig[1] - 1 + K) % K;
    bool legal = true;
    while (legal && pos[0] != target0) legal = step(0);
    for (int t = nc - 1; legal && t >= 1; t--) { int tg = orig[(t + 1) % nc]; while (legal && pos[t] != tg) legal = step(t); }
    while (legal && pos[0] != orig[1]) legal = step(0);
    if (!legal) { fail(10); Bv = Bsave; return; }
    if (!found) { fail(11); Bv = Bsave; return; }
    if (!okfull) { fail(12); }
    Bv = Bsave;
}

static void splits(int ii) {
    if (ii == K) { process(); return; }
    a[ii] = r[ii]; b[ii] = 0; splits(ii + 1);
    a[ii] = 0; b[ii] = r[ii]; splits(ii + 1);
    if (r[ii] == 2) { a[ii] = 1; b[ii] = 1; splits(ii + 1); }
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
        if (R < 2 * p + 1 || mx < 2 * p - K + 2 || !rot_min()) return;
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
    if (argc < 3) return 1;
    p = atoi(argv[2]);
    if (!strcmp(argv[1], "exh")) {
        for (K = p + 1; K <= 2 * p - 2; K++) gen(0, 4 * p - 2);
    } else {
        int T = atoi(argv[3]); rng.seed(atoi(argv[4]));
        int N = 4 * p - 2; long long tries = 0, done = 0;
        while (done < T && tries < 50000000LL) {
            tries++;
            K = p + 1 + rng() % (p - 2);                    // k in [p+1, 2p-2]
            int W = 2 * p - K + 1;
            int jmax = 2 * p - 2 - K; if (jmax < 1) continue;
            int j = 1 + rng() % jmax;
            if ((K + j) % 2) continue;
            int kp = (K + j) / 2, H = p - 1 - kp; if (H < 0) continue;
            int R = 2 * p + j, F = N - R; if (F != K + 2 * H) continue;
            // big run u: excess ex_u >= W, total excess R - K
            int E = R - K; int exu = W + rng() % (E - W + 1);
            std::vector<int> rv(K, 1); rv[0] = 1 + exu;
            for (int q = 0; q < E - exu; q++) rv[1 + rng() % (K - 1)]++;
            std::shuffle(rv.begin(), rv.end(), rng);
            for (int t = 0; t < K; t++) r[t] = rv[t];
            for (int t = 0; t < K; t++) l[t] = 1;
            for (int q = 0; q < H; q++) l[rng() % K] += 2;
            for (int t = 0; t < K; t++) {
                int ch = rng() % 3;
                if (r[t] == 2 && ch == 2) { a[t] = 1; b[t] = 1; }
                else if (ch == 0 && r[t] < W + 1) { a[t] = 0; b[t] = r[t]; }
                else { a[t] = r[t]; b[t] = 0; }
            }
            long long before = n_words; process(); if (n_words > before) done++;
        }
    }
    printf("{\"p\":%d,\"words\":%lld,\"case_c_in_range\":%lld,\"case_c_gt_mmax\":%lld,\"case_c_lt_mlo\":%lld", p, n_words, n_case[0], n_case[1], n_case[2]);
    for (int c = 0; c < 16; c++) if (n_fail[c]) printf(",\"fail%d\":%lld", c, n_fail[c]);
    printf("}\n");
    return 0;
}
