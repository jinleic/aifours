// thmC.cpp -- c3 README Sec. 7: literal replay of the candidate proof of Theorem C on hard lift vectors.  Aid only.
// Words: generators of census3.cpp; tested if (H) holds (all proper patterns certified + pin) and
//   n_ev,al <= 4  or  (2kB <= p and n_ev,al <= 2kB + 2).
// Hard lifts: as rstest.cpp (sum p, singleton bounds, all pair lower/upper constraints).
// For each vector: follow Case A / Case B of the proof, assert every intermediate claim, and check the final
// window violation X_Q < lambda(Q) from the lambda table (lambda = Lemma H, beta = 0).
// Usage: thmC exh p kmin kmax NX seed | thmC rnd p T seed kmin kmax NX
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <random>
#include <cstdint>
#include <map>
#include <string>
typedef uint32_t M;
static int p, K, Bv, Av, kB, Rv, kap;
static int a[64], b[64], l[64], d[64], r[64];
static M FULL;
static std::vector<int8_t> L;
static std::vector<uint8_t> C;
static std::mt19937 rng(12345);
static int NX = 20;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline int cl2(int x) { return -fl2(-x); }
static inline int blocks(M Q) { M rot = ((Q << 1) | (Q >> (K - 1))) & FULL; return __builtin_popcount(Q & ~rot); }
static int lamc(M Q) {
    int m = blocks(Q), D = 0;
    for (int t = 0; t < K; t++) if ((Q >> t) & 1u) D += d[t];
    int x = p - m + 1, y = D + m - kB, z = fl2(D + Bv) + 1;
    int v = x < y ? x : y; return v < z ? v : z;
}
static long long nw = 0, nskipH = 0, nskipHyp = 0, nvec = 0, nnovec = 0;
static long long nA_Z = 0, nA_land = 0, nB = 0, nfail = 0;
static std::map<std::string, long long> fails;
static int x[64], lo[64], hi[64], ord[64];
static std::vector<std::vector<int>> sols;
static long long nodes;
static void dfsx(int i, int partial) {
    if ((int)sols.size() >= NX || nodes > 200000) return;
    nodes++;
    if (i == K) { if (partial == p) sols.push_back(std::vector<int>(x, x + K)); return; }
    int t = ord[i];
    int rmin = 0, rmax = 0; for (int j = i + 1; j < K; j++) { rmin += lo[ord[j]]; rmax += hi[ord[j]]; }
    std::vector<int> vals; for (int v = lo[t]; v <= hi[t]; v++) vals.push_back(v);
    std::shuffle(vals.begin(), vals.end(), rng);
    for (int v : vals) {
        int rest = p - partial - v; if (rest < rmin || rest > rmax) continue;
        bool ok = true;
        for (int j = 0; j < i && ok; j++) {
            int u = ord[j]; M Q = (1u << t) | (1u << u); int s = v + x[u];
            if (s < L[Q] || s > p - L[FULL ^ Q]) ok = false;
        }
        if (!ok) continue;
        x[t] = v; dfsx(i + 1, partial + v);
        if ((int)sols.size() >= NX) return;
    }
}
static int bh[64], cc[64], ff[64], ep[64];
static void FAIL(const char* why) {
    nfail++; fails[why]++;
    if (nfail <= 20) {
        printf("{\"FAIL\":\"%s\",\"p\":%d,\"k\":%d,\"B\":%d,\"kB\":%d,\"d\":[", why, p, K, Bv, kB);
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", d[t]);
        printf("],\"x\":["); for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", x[t]); printf("]}\n");
    }
}
static int sumOn(M Q, const int* v) { int s = 0; for (int t = 0; t < K; t++) if ((Q >> t) & 1u) s += v[t]; return s; }
static int Dof(M Q) { return sumOn(Q, d); }
static int Xof(M Q) { return sumOn(Q, x); }
static int Phi(M Q) { return sumOn(Q, cc) + blocks(Q); }
static bool isKill(M Q) { return Q && Q != FULL && Xof(Q) < L[Q]; }
static void process() {
    Av = 0; Bv = 0; int H = 0;
    for (int t = 0; t < K; t++) { Av += a[t]; Bv += b[t]; d[t] = a[t] - b[t]; H += l[t] / 2; }
    kap = p - 1 - H; kB = kap - Bv; Rv = Av + Bv;
    if (Rv > 2 * p - 3) return;
    FULL = (1u << K) - 1;
    size_t N = (size_t)1 << K;
    if (L.size() < N) { L.resize(N); C.resize(N); }
    for (size_t Q = 1; Q < N - 1; Q++) L[Q] = (int8_t)lamc((M)Q);
    bool allc = true;
    for (size_t Q = 1; Q < N - 1; Q++) {
        M q = (M)Q; int s = __builtin_popcount(q); C[Q] = 0;
        if (s == 1) { C[Q] = 1; continue; }
        for (M rr = q; rr; rr &= rr - 1) {
            M bt = rr & (~rr + 1u), Qp = q ^ bt;
            if (!C[Qp]) continue;
            if (L[Qp] + L[bt] + L[FULL ^ q] >= 1 && L[q] + L[FULL ^ Qp] + L[FULL ^ bt] >= p + 1) { C[Q] = 1; break; }
        }
        if (!C[Q]) allc = false;
    }
    bool pin = false;
    for (size_t Q = 1; Q < N - 1 && !pin; Q++) if (C[Q] && C[FULL ^ (M)Q] && L[Q] + L[FULL ^ (M)Q] >= 1) pin = true;
    if (!allc || !pin) { nskipH++; return; }
    int nev_al = 0, nev = 0, nal = 0, nan = 0, npr = 0, nev_an = 0;
    for (int t = 0; t < K; t++) {
        if (b[t] == 0) { nal++; if (a[t] % 2 == 0) nev_al++; }
        else if (a[t] == 0) { nan++; if (b[t] % 2 == 0) nev_an++; }
        else npr++;
        if (((d[t] % 2) + 2) % 2 == 0) nev++;
    }
    bool hypA = nev_al <= 4, hypL = (2 * kB <= p) && (nev_al <= 2 * kB + 2);
    if (!(hypA || hypL)) { nskipHyp++; return; }
    nw++;
    for (int t = 0; t < K; t++) { lo[t] = L[1u << t]; hi[t] = p - L[FULL ^ (1u << t)]; ord[t] = t; ff[t] = fl2(d[t] - 1); }
    std::shuffle(ord, ord + K, rng);
    sols.clear(); nodes = 0; dfsx(0, 0);
    if (sols.empty()) { nnovec++; return; }
    for (auto& xv : sols) {
        nvec++;
        for (int t = 0; t < K; t++) { x[t] = xv[t]; bh[t] = 2 * x[t] - d[t]; cc[t] = d[t] - x[t]; ep[t] = cc[t] - ff[t]; }
        int sumbh = 0; for (int t = 0; t < K; t++) sumbh += bh[t];
        if (sumbh != K - 2 * kB) { FAIL("sum_bh"); continue; }
        int Ksum = 0; for (int t = 0; t < K; t++) Ksum += ep[t];
        if (2 * Ksum != 2 * kB + nev) { FAIL("sum_eps"); continue; }
        M Z = 0; for (int t = 0; t < K; t++) if (bh[t] <= 0) Z |= 1u << t;
        if (Z == 0 || Z == FULL) { FAIL("Z_trivial"); continue; }
        int s = 0; for (int t = 0; t < K; t++) if (!((Z >> t) & 1u)) s += bh[t] - 1;
        int nZ = __builtin_popcount(Z), nodd = 0; for (int t = 0; t < K; t++) if (((Z >> t) & 1u) && (d[t] % 2 != 0)) nodd++;
        if (sumOn(Z, bh) != nZ - 2 * kB - s) { FAIL("bhZ_identity"); continue; }
        if (nZ + nodd > 2 * kB + s) { FAIL("Z_size_bound"); continue; }
        for (int t = 0; t < K; t++) if (((Z >> t) & 1u) && x[t] > cc[t]) { FAIL("x_le_c_defect"); break; }
        int PZ = Phi(Z), mZ = blocks(Z);
        if (PZ >= kB + 1) {
            bool done = false;
            if (hypA) {
                if (Xof(Z) + mZ > p) FAIL("caseA_P_auto");
                else if (sumOn(Z, bh) > Bv) FAIL("caseA_Fl");
                else if (!isKill(Z)) FAIL("caseA_Z_not_kill");
                else { nA_Z++; done = true; }
            }
            if (hypL) {
                for (int t = 0; t < K; t++) if (((Z >> t) & 1u) && cc[t] > p - kB - 1) { FAIL("caseA_c_bound"); break; }
                M Q = Z; int cur = Phi(Q); bool ok = true;
                if (cur > p) {
                    while (Q) {
                        int pick = -1;
                        for (int t = 0; t < K && pick < 0; t++) if ((Q >> t) & 1u) {
                            bool lft = (Q >> ((t + K - 1) % K)) & 1u, rgt = (Q >> ((t + 1) % K)) & 1u;
                            if (!(lft && rgt)) pick = t;
                        }
                        if (pick < 0) { ok = false; break; }
                        M Q2 = Q & ~(1u << pick); int nxt = Phi(Q2);
                        if (cur - nxt > p - kB) { ok = false; FAIL("caseA_step"); break; }
                        Q = Q2; cur = nxt;
                        if (cur <= p) break;
                    }
                }
                if (ok) {
                    if (!(cur >= kB + 1 && cur <= p)) FAIL("caseA_land_range");
                    else if (Xof(Q) + blocks(Q) > cur) FAIL("caseA_land_P");
                    else if (!isKill(Q)) FAIL("caseA_land_not_kill");
                    else if (!done) { nA_land++; done = true; }
                }
            }
            continue;
        }
        // Case B
        int Delta = kB - PZ;
        int DZ = Dof(Z);
        if (2 * (Delta + mZ) != nZ - DZ - s) { FAIL("Delta_identity"); continue; }
        int WZ = 0; for (int t = 0; t < K; t++) if ((Z >> t) & 1u) { if (b[t] > 0 && a[t] == 0) WZ += b[t] + (b[t] % 2 == 0); else if (a[t] == 1 && b[t] == 1) WZ += 1; }
        M Xs = 0, Xo = 0;
        for (int u = 0; u < K; u++) {
            if ((Z >> u) & 1u) continue;
            if (b[u] != 0) continue;
            if (ep[u] != 0) continue;
            if ((Z >> ((u + 1) % K)) & 1u) continue;
            if ((Z >> ((u + K - 1) % K)) & 1u) continue;
            Xs |= 1u << u; if (a[u] % 2 == 1) Xo |= 1u << u;
        }
        int nX = __builtin_popcount(Xs), nXo = __builtin_popcount(Xo);
        if (2 * nX < 2 * (nal - kB + 2 * Delta - WZ) + nev) { FAIL("X_bound"); continue; }
        if (nXo < 2 * Delta + 2) { FAIL("Xo_bound"); continue; }
        // greedy independent subset of Xo along each maximal block of Xo (Xo != FULL since Z nonempty)
        int start = -1; for (int t = 0; t < K; t++) if (!((Xo >> t) & 1u)) { start = t; break; }
        M S = 0; int need = Delta + 1, got = 0;
        bool prevTaken = false;
        for (int i = 1; i <= K && got < need; i++) {
            int t = (start + i) % K;
            if (!((Xo >> t) & 1u)) { prevTaken = false; continue; }
            if (prevTaken) { prevTaken = false; continue; }
            S |= 1u << t; got++; prevTaken = true;
        }
        if (got < need) { FAIL("S_greedy_short"); continue; }
        for (int t = 0; t < K; t++) if (((S >> t) & 1u) && bh[t] != 1) { FAIL("S_bh_not_1"); break; }
        M Q = Z | S;
        if (blocks(Q) != mZ + got) { FAIL("S_blocks"); continue; }
        if (Phi(Q) < kB + 1) { FAIL("caseB_M"); continue; }
        if (sumOn(Q, bh) > Bv) { FAIL("caseB_Fl"); continue; }
        if (2 * (Xof(Q) + blocks(Q)) > 2 * p - 4 - Bv) { FAIL("caseB_P_bound"); continue; }
        if (!isKill(Q)) { FAIL("caseB_not_kill"); continue; }
        nB++;
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
        if (kp < 2) return;
        if (R > 2 * p - 3) return;
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
static void summary(const char* tag) {
    printf("{\"summary\":\"%s\",\"p\":%d,\"words_tested\":%lld,\"skip_not_H\":%lld,\"skip_nevAl_hyp\":%lld,\"words_without_pair_feasible_x\":%lld,\"vectors\":%lld,\"caseA_Z\":%lld,\"caseA_land_only\":%lld,\"caseB\":%lld,\"fail\":%lld,\"fail_kinds\":{",
           tag, p, nw, nskipH, nskipHyp, nnovec, nvec, nA_Z, nA_land, nB, nfail);
    bool first = true; for (auto& kv : fails) { printf("%s\"%s\":%lld", first ? "" : ",", kv.first.c_str(), kv.second); first = false; }
    printf("}}\n"); fflush(stdout);
}
int main(int argc, char** argv) {
    if (argc < 3) return 1;
    p = atoi(argv[2]);
    if (!strcmp(argv[1], "exh")) {
        int kmin = atoi(argv[3]), kmax = atoi(argv[4]); NX = atoi(argv[5]); rng.seed(atoi(argv[6]));
        for (K = kmin; K <= kmax; K++) { gen(0, 4 * p - 2); fprintf(stderr, "done k=%d\n", K); }
        summary("exh");
    } else {
        int T = atoi(argv[3]); unsigned seed = atoi(argv[4]);
        int kmin = atoi(argv[5]), kmax = atoi(argv[6]); NX = atoi(argv[7]);
        std::mt19937 g(seed); rng.seed(seed + 1);
        int N = 4 * p - 2, done = 0;
        while (done < T) {
            K = kmin + g() % (kmax - kmin + 1);
            int Hmax = (N - 2 * K) / 2; if (Hmax < 0) continue;
            int H = g() % (Hmax + 1);
            int kp = p - 1 - H; if (kp < 2) continue;
            int B = 1 + g() % (kp - 1);
            int F = K + 2 * H, R = N - F, A = R - B;
            if (R < K || A < B || A > 2 * p - 1) continue;
            if (R > 2 * p - 3) continue;
            int n0 = g() % 3; if (n0 > B) n0 = B;
            int Bp = B - n0, Ap = A - n0, rem = K - n0;
            if (rem < 1) continue;
            int na = (Bp == 0) ? 0 : 1 + (int)(g() % std::min(Bp, std::max(1, rem - 1)));
            int nal = rem - na;
            if (nal < 1 || Ap < nal || (Bp > 0 && na < 1) || (Bp == 0 && na > 0) || Bp < na) continue;
            std::vector<int> ca(nal, 1), cb(na, 1);
            for (int i = 0; i < Ap - nal; i++) ca[g() % nal]++;
            for (int i = 0; i < Bp - na; i++) cb[g() % na]++;
            std::vector<int> kinds;
            for (int i = 0; i < nal; i++) kinds.push_back(0);
            for (int i = 0; i < na; i++) kinds.push_back(1);
            for (int i = 0; i < n0; i++) kinds.push_back(2);
            std::shuffle(kinds.begin(), kinds.end(), g);
            int ia = 0, ib = 0;
            for (int t = 0; t < K; t++) {
                if (kinds[t] == 0) { a[t] = ca[ia++]; b[t] = 0; }
                else if (kinds[t] == 1) { a[t] = 0; b[t] = cb[ib++]; }
                else { a[t] = 1; b[t] = 1; }
                l[t] = 1; r[t] = a[t] + b[t];
            }
            for (int i = 0; i < H; i++) l[g() % K] += 2;
            process(); done++;
        }
        summary("rnd");
    }
    return 0;
}
