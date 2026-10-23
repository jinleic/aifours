// r2_check.cpp -- exact check of Lemma R2 (c2/README.md Sec. 2), aid only.
// Words: all-odd, length 4p-2, R = 2p-2, k >= p+1 (k even), every run pure or a (1,1)-pair, any B with
// 0 <= B <= A; all rotation classes of (r, l).  Conventions: run t (0..k-1) lies between sites t-1 and t
// (site = reflection run, indices mod k); a cut at site q separates runs q and q+1; moving a cut from q to
// q+1 toggles run q+1.  x(P) = E+(P) = D_P + B; window via g_m(E) = min(p-m, E+m-1-kappa, floor(E/2)).
// Checks per word:
//  (a) Claim 1'': every pattern with m0 blocks and EVEN x in [M, R-M] has a full window;
//  (b) Claim 2 + proof: for every admissible singleton s and NC random completions of the cut set,
//      the ALT schedule is legal, ends at P_0^c, |x(P_N)-x(P_tau)| <= bound, some j <= tau enters the zone,
//      the s-toggle is legal at j, and the final pattern (P_j or P_j with s toggled) has m0 blocks and a
//      full window;  W = 3 (kappa odd): any ALT path visits x = kappa+1 and that pattern is full;
//  (c) Claim 3: if kappa odd and W >= 7, an admissible singleton exists.
// Usage: r2_check p NC seed
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <random>

static int p, K, Bv, Rv, kap, NC;
static int a[64], b[64], l[64], d[64], r[64];
static std::mt19937 rng;
static long long n_words = 0, n_c1_pat = 0, n_c1_fail = 0, n_constr = 0, n_constr_fail = 0, n_c3_fail = 0, n_w3 = 0, n_w3_fail = 0;
static long long fail_detail[16];
static int printed = 0;

static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline int g(int m, int E) { return std::min(p - m, std::min(E + m - 1 - kap, fl2(E))); }
static int blocks(unsigned P) { int f2 = 0; for (int t = 0; t < K; t++) { int z = (P >> t) & 1, zn = (P >> ((t + 1) % K)) & 1; f2 += (z != zn); } return f2 / 2; }
static int xof(unsigned P) { int D = 0; for (int t = 0; t < K; t++) if ((P >> t) & 1) D += d[t]; return D + Bv; }
static bool fullw(unsigned P) { int m = blocks(P); if (m == 0) return false; int x = xof(P); return g(m, x) + g(m, Rv - x) + 1 >= p; }

static void report_fail(int code) {
    fail_detail[code]++;
    if (printed < 20) { printed++;
        printf("{\"FAIL\":%d,\"k\":%d,\"B\":%d,\"kappa\":%d,\"a\":[", code, K, Bv, kap);
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", a[t]);
        printf("],\"b\":["); for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", b[t]); printf("]}\n"); }
}

// pattern from cut sites + status of run s0
static unsigned pattern_from_cuts(const std::vector<int>& cutsite, int s0, int st0) {
    std::vector<char> iscut(K, 0); for (int q : cutsite) iscut[q] = 1;
    unsigned P = 0; int st = st0;
    for (int i = 0; i < K; i++) { int t = (s0 + i) % K; if (st) P |= 1u << t; if (iscut[t]) st ^= 1; }  // cut at site t separates t, t+1
    return P;
}

// Simulate the ALT schedule. cuts: positions in cyclic order starting with c (index 0). Returns false if illegal.
struct Sim { std::vector<unsigned> pats; int tau; bool ok; };
static Sim simulate(std::vector<int> pos, unsigned P0, int ci_star_target /* site for i* first move */, int c_target /* original site of c+ */) {
    Sim S; S.ok = true; S.tau = -1;
    int nc = (int)pos.size();
    std::vector<char> occ(K, 0); for (int q : pos) occ[q] = 1;
    unsigned P = P0; S.pats.push_back(P);
    std::vector<int> orig = pos;
    auto step = [&](int idx) -> bool {           // move cut idx forward by one site
        int q = pos[idx], q1 = (q + 1) % K;
        if (occ[q1]) return false;
        occ[q] = 0; occ[q1] = 1; pos[idx] = q1;
        int t = q1;                               // run between sites q and q+1 is run q+1
        P ^= 1u << t; S.pats.push_back(P); return true;
    };
    int istar = nc - 1;
    // (1) i* forward to site ci_star_target
    while (pos[istar] != ci_star_target) { if (!step(istar)) { S.ok = false; return S; } }
    // (2) cuts nc-2 down to 1: each to the original position of the next cut
    for (int t = nc - 2; t >= 1; t--) {
        int target = orig[t + 1];
        while (pos[t] != target) { if (!step(t)) { S.ok = false; return S; } }
    }
    S.tau = (int)S.pats.size() - 1;
    // (3) c to the original position of c+
    while (pos[0] != c_target) { if (!step(0)) { S.ok = false; return S; } }
    // (4) i* to the original position of c
    while (pos[istar] != orig[0]) { if (!step(istar)) { S.ok = false; return S; } }
    return S;
}

static void process() {
    int A = 0; Bv = 0; int H = 0;
    for (int t = 0; t < K; t++) { A += a[t]; Bv += b[t]; d[t] = a[t] - b[t]; H += l[t] / 2; r[t] = a[t] + b[t]; }
    kap = p - 1 - H; Rv = A + Bv;
    if (Rv != 2 * p - 2 || K != 2 * kap + 2) { report_fail(9); return; }
    n_words++;
    int W = Rv - 2 * kap + 1, E = Rv - K;
    int m0 = kap / 2 + 1, M = (kap % 2 == 0) ? kap : kap + 1;
    unsigned full = (K == 32) ? 0xffffffffu : ((1u << K) - 1);
    // (a)
    for (unsigned P = 1; P < full; P++) {
        if (blocks(P) != m0) continue;
        int x = xof(P);
        if (x % 2 != 0 || x < M || x > Rv - M) continue;
        n_c1_pat++;
        if (!fullw(P)) { n_c1_fail++; report_fail(1); }
    }
    // singletons and admissibility
    std::vector<int> adm;
    for (int s = 0; s < K; s++) {
        if (r[s] != 1) continue;
        int sm = (s - 1 + K) % K, sp = (s + 1) % K;
        if (kap % 2 == 0) adm.push_back(s);
        else if (W >= 7 && (r[sm] - 1) + (r[sp] - 1) <= E - 2) adm.push_back(s);
    }
    if (kap % 2 == 1 && W >= 7 && adm.empty()) { n_c3_fail++; report_fail(3); }
    if (kap % 2 == 1 && W == 3) {
        // unit steps: generic ALT path from random configurations
        n_w3++;
        for (int rep = 0; rep < NC; rep++) {
            // random 2m0 cut sites with at least one gap >= 2 before some cut
            std::vector<int> sites(K); for (int i = 0; i < K; i++) sites[i] = i;
            std::shuffle(sites.begin(), sites.end(), rng);
            std::vector<int> cs(sites.begin(), sites.begin() + 2 * m0); std::sort(cs.begin(), cs.end());
            // choose c = a cut whose backward gap >= 2 (exists since K - 2m0 >= 1)
            int ci = -1;
            for (int i = 0; i < 2 * m0; i++) { int prev = cs[(i - 1 + 2 * m0) % (2 * m0)]; int gap = (cs[i] - prev + K) % K; if (gap >= 2) { ci = i; break; } }
            if (ci < 0) { report_fail(8); continue; }
            std::vector<int> pos; for (int i = 0; i < 2 * m0; i++) pos.push_back(cs[(ci + i) % (2 * m0)]);
            unsigned P0 = pattern_from_cuts(pos, (pos[0] + 1) % K, rng() & 1);
            int istar_t = (pos[0] - 1 + K) % K;
            Sim S = simulate(pos, P0, istar_t, pos[1]);
            if (!S.ok || S.pats.back() != (full ^ P0)) { n_w3_fail++; report_fail(7); continue; }
            bool hit = false;
            for (unsigned P : S.pats) { if (xof(P) == kap + 1) { hit = true; if (!fullw(P) || blocks(P) != m0) { n_w3_fail++; report_fail(6); } break; } }
            if (!hit) { n_w3_fail++; report_fail(5); }
        }
        return;
    }
    // (b) construction for each admissible singleton
    for (int s : adm) {
        int Sm2 = (s - 2 + K) % K, Sm1 = (s - 1 + K) % K, S0 = s % K, Sp1 = (s + 1) % K;   // site indices: run s between sites s-1 and s
        std::vector<int> others;
        for (int q = 0; q < K; q++) if (q != Sm2 && q != Sm1 && q != S0 && q != Sp1) others.push_back(q);
        for (int rep = 0; rep < NC; rep++) {
            n_constr++;
            std::shuffle(others.begin(), others.end(), rng);
            std::vector<int> cs = {Sm1, Sp1};
            for (int i = 0; i < 2 * m0 - 2; i++) cs.push_back(others[i]);
            // cyclic order starting at c = Sm1
            std::sort(cs.begin(), cs.end(), [&](int u, int v) { return ((u - Sm1 + K) % K) < ((v - Sm1 + K) % K); });
            if (cs[0] != Sm1 || cs[1] != Sp1) { n_constr_fail++; report_fail(10); continue; }
            unsigned P0 = pattern_from_cuts(cs, s, rng() & 1);
            Sim S = simulate(cs, P0, Sm2, Sp1);
            if (!S.ok || S.pats.back() != (full ^ P0)) { n_constr_fail++; report_fail(11); continue; }
            int xN = xof(S.pats.back()), xt = xof(S.pats[S.tau]);
            int bound = (kap % 2 == 0) ? W : W - 2;
            if (std::abs(xN - xt) > bound) { n_constr_fail++; report_fail(12); continue; }
            int lo = (kap % 2 == 0) ? kap : kap + 1, hi = Rv - lo;
            int j = -1;
            for (int i = 0; i <= S.tau; i++) { int x = xof(S.pats[i]); if (x >= lo && x <= hi) { j = i; break; } }
            if (j < 0) { n_constr_fail++; report_fail(13); continue; }
            unsigned Pj = S.pats[j];
            unsigned Pf = Pj;
            if (xof(Pj) % 2 != 0) {
                // s-toggle legal: cut at Sm1, S0 free in P_j <=> run s and run s+1 on different sides? check via cuts:
                // in P_j, cut at site q iff runs q and q+1 differ.
                auto cutat = [&](unsigned P, int q) { return ((P >> q) & 1) != ((P >> ((q + 1) % K)) & 1); };
                if (!cutat(Pj, Sm1) || cutat(Pj, S0)) { n_constr_fail++; report_fail(14); continue; }
                Pf = Pj ^ (1u << s);
            }
            if (blocks(Pf) != m0 || !fullw(Pf)) { n_constr_fail++; report_fail(15); continue; }
        }
    }
}

static void splits(int i) {
    if (i == K) { process(); return; }
    a[i] = r[i]; b[i] = 0; splits(i + 1);
    a[i] = 0; b[i] = r[i]; splits(i + 1);
    if (r[i] == 2) { a[i] = 1; b[i] = 1; splits(i + 1); }
}
static int rr[64];
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
        int R = 0; for (int t = 0; t < K; t++) R += rr[t];
        if (R != 2 * p - 2 || !rot_min()) return;
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
    if (argc < 4) return 1;
    p = atoi(argv[1]); NC = atoi(argv[2]); rng.seed(atoi(argv[3]));
    for (K = p + 1; K <= 2 * p - 2; K++) { if (K % 2) continue; gen(0, 4 * p - 2); }
    printf("{\"p\":%d,\"words\":%lld,\"claim1pp_patterns\":%lld,\"claim1pp_fail\":%lld,\"constructions\":%lld,\"construction_fail\":%lld,\"claim3_fail\":%lld,\"W3_words\":%lld,\"W3_fail\":%lld}\n",
           p, n_words, n_c1_pat, n_c1_fail, n_constr, n_constr_fail, n_c3_fail, n_w3, n_w3_fail);
    for (int c = 0; c < 16; c++) if (fail_detail[c]) printf("{\"fail_code\":%d,\"count\":%lld}\n", c, fail_detail[c]);
    return 0;
}
