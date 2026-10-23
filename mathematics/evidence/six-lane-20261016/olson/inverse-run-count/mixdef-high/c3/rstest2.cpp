// rstest2.cpp -- instrumented copy of rstest.cpp: counts patterns Q in the RS search with (M) and (Fl) true but (P) false,
// and the maximum of X_Q + m(Q) - p over found kills.  Otherwise identical.
// (original header:) test of rule RS on all-certified item-(iii) words.  Aid only.
// Words: generators of census3.cpp (exh p kmin kmax | rnd p T seed kmin kmax); only words with ALL proper patterns
// certified (singleton extension) and a pin pattern are tested.
// Hard lifts: integer x, sum p, x_t in [lambda({t}), p - lambda({t}^c)], every pair Q: lambda(Q) <= X_Q <= p - lambda(Q^c)
// (randomized DFS, up to NX vectors per word, node limit).  Rule RS: Z = {bh <= 0}; kill Z, else exact DFS over
// independent S outside N[Z] for a kill of Z u S.  Kill test: X_Q < lambda(Q) (lambda from the table) and, as an
// independent re-check, the bh form (bh(Q) <= B, D_Q - bh(Q) + 2m >= 2kB + 2, X_Q <= p - m).
// Usage: rstest exh p kmin kmax NX seed | rstest rnd p T seed kmin kmax NX
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <random>
#include <cstdint>
#include <map>
#include <tuple>
typedef uint32_t M;
static int p, K, Bv, Av, kB, Rv, kap;
static int a[64], b[64], l[64], d[64], r[64];
static M FULL;
static std::vector<int8_t> L;
static std::vector<uint8_t> C;
static std::mt19937 rng(12345);
static int NX = 20;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline int blocks(M Q) { M rot = ((Q << 1) | (Q >> (K - 1))) & FULL; return __builtin_popcount(Q & ~rot); }
static int lamc(M Q) {
    int m = blocks(Q), D = 0;
    for (int t = 0; t < K; t++) if ((Q >> t) & 1u) D += d[t];
    int x = p - m + 1, y = D + m - kB, z = fl2(D + Bv) + 1;
    int v = x < y ? x : y; return v < z ? v : z;
}
// statistics
static long long nw = 0, nskip = 0, nvec = 0, nkillZ = 0, nkillZS = 0, nfail = 0, nbadcheck = 0, nnovec = 0;
static std::map<int, long long> szS;
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
static int bhv[64];
static long long nPfail = 0; static int maxXm = -1000;
static bool killQ(M Q, bool& agree) {
    if (Q == 0 || Q == FULL) { agree = true; return false; }
    int X = 0, D = 0, bh = 0; for (int t = 0; t < K; t++) if ((Q >> t) & 1u) { X += x[t]; D += d[t]; bh += bhv[t]; }
    bool k1 = X < L[Q];
    int m = blocks(Q);
    bool MF = (bh <= Bv) && (D - bh + 2 * m >= 2 * kB + 2);
    if (MF && !(X <= p - m)) nPfail++;
    bool k2 = MF && (X <= p - m);
    if (k2 && X + m - p > maxXm) maxXm = X + m - p;
    agree = (k1 == k2);
    return k1;
}
static std::vector<int> cand;
static M Zm;
static bool foundS; static int bestS;
static long long snodes;
static void dfsS(int i, M S, int bhS) {
    if (foundS || snodes > 2000000) return;
    snodes++;
    bool ag; if (S && killQ(Zm | S, ag)) { if (!ag) nbadcheck++; foundS = true; bestS = __builtin_popcount(S); return; }
    for (int j = i; j < (int)cand.size(); j++) {
        int u = cand[j]; M bu = 1u << u;
        M nb = (1u << ((u + 1) % K)) | (1u << ((u + K - 1) % K));
        if (S & nb) continue;
        int bh2 = bhS + bhv[u];
        dfsS(j + 1, S | bu, bh2);
        if (foundS) return;
    }
}
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
    if (!allc || !pin) { nskip++; return; }
    nw++;
    for (int t = 0; t < K; t++) { lo[t] = L[1u << t]; hi[t] = p - L[FULL ^ (1u << t)]; ord[t] = t; }
    std::shuffle(ord, ord + K, rng);
    sols.clear(); nodes = 0; dfsx(0, 0);
    if (sols.empty()) { nnovec++; return; }
    for (auto& xv : sols) {
        nvec++;
        for (int t = 0; t < K; t++) { x[t] = xv[t]; bhv[t] = 2 * x[t] - d[t]; }
        Zm = 0; for (int t = 0; t < K; t++) if (bhv[t] <= 0) Zm |= 1u << t;
        bool ag;
        if (killQ(Zm, ag)) { if (!ag) nbadcheck++; nkillZ++; continue; }
        cand.clear();
        for (int u = 0; u < K; u++) {
            if ((Zm >> u) & 1u) continue;
            if ((Zm >> ((u + 1) % K)) & 1u) continue;
            if ((Zm >> ((u + K - 1) % K)) & 1u) continue;
            cand.push_back(u);
        }
        std::stable_sort(cand.begin(), cand.end(), [](int u, int v) { return (d[u] - bhv[u]) > (d[v] - bhv[v]); });
        foundS = false; snodes = 0; dfsS(0, 0, 0);
        if (foundS) { nkillZS++; szS[bestS]++; continue; }
        nfail++;
        if (nfail <= 25) {
            printf("{\"RS_FAIL\":1,\"p\":%d,\"k\":%d,\"B\":%d,\"kB\":%d,\"d\":[", p, K, Bv, kB);
            for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", d[t]);
            printf("],\"x\":[");
            for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", x[t]);
            printf("],\"Z\":%u,\"snodes\":%lld}\n", Zm, snodes);
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
    printf("{\"summary\":\"%s\",\"p\":%d,\"words_tested\":%lld,\"words_skipped_not_allcert\":%lld,\"words_without_pair_feasible_x\":%lld,\"vectors\":%lld,\"kill_Z\":%lld,\"kill_ZS\":%lld,\"fail\":%lld,\"check_disagreements\":%lld,\"S_sizes\":{",
           tag, p, nw, nskip, nnovec, nvec, nkillZ, nkillZS, nfail, nbadcheck);
    bool first = true; for (auto& kv : szS) { printf("%s\"%d\":%lld", first ? "" : ",", kv.first, kv.second); first = false; }
    printf("},\"MFl_true_P_false\":%lld,\"max_XQ_plus_m_minus_p\":%d}\n", nPfail, maxXm); fflush(stdout);
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
