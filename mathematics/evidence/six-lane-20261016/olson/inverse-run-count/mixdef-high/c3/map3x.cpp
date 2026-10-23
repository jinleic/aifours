// map3x.cpp -- variant of map3.cpp with EXTENDED certification (Lemma L+): Q is certified if |Q| = 1 or Q = Q' u Y
// (disjoint, both certified, 1 <= |Y| <= YMAX) with lambda(Q') + lambda(Y) + lambda(Q^c) >= 1 and
// lambda(Q) + lambda(Q'^c) + lambda(Y^c) >= p + 1 (Lemma BC step (b) with X = Q').  YMAX = 1 is map3.cpp.
// Usage: map3x exh p kmin kmax DUMP YMAX | map3x rnd p T seed kmin kmax DUMP YMAX
// (original header:) map3.cpp -- c3 README Sec. 3 P3: map of item (iii) into the sub-families covered by the written results of cycle 3.
// Words: generators of census3.cpp (exh p kmin kmax | rnd p T seed kmin kmax); all NMH words with R <= 2p-3; the
// ZSI-B words (k = p+1, kB = 1, (4.1); ../proof-MH.md Lemma ZSI-B) are flagged and reported separately (item (iii)
// excludes them).  Labels per word:
//   WALL : all runs single letters, B = 1, 3kB <= p + 4                      (c3/proof-WALL.md, no computation needed)
//   C    : (H) holds [all proper patterns certified by singleton extension + pin] and
//          (n_ev,al <= 4 or (2kB <= p and n_ev,al <= 2kB + 2))              (c3/proof-C-r1.md; (H) checked here)
//   open : neither.  Reasons recorded: notH_cert (some pattern uncertified), notH_pin (all certified, no pin),
//          hyp (H holds but the n_ev,al condition fails).
// Optional dump of the first DUMP words (d vector, B, kB, p, H verdict) for an independent re-check (hcheck.py).
// Usage: map3 exh p kmin kmax DUMP | map3 rnd p T seed kmin kmax DUMP
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <random>
#include <cstdint>
#include <map>
#include <tuple>
#include <string>
typedef uint32_t M;
static int p, K, Bv, Av, kB, Rv, kap;
static int a[64], b[64], l[64], d[64], r[64];
static M FULL;
static std::vector<int8_t> L;
static std::vector<uint8_t> C;
static int DUMP = 0, dumped = 0, YMAX = 1;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static int lamc(M Q) {
    M rot = ((Q << 1) | (Q >> (K - 1))) & FULL;
    int m = __builtin_popcount(Q & ~rot), D = 0;
    for (int t = 0; t < K; t++) if ((Q >> t) & 1u) D += d[t];
    int x = p - m + 1, y = D + m - kB, z = fl2(D + Bv) + 1;
    int v = x < y ? x : y; return v < z ? v : z;
}
static bool zsiB() {
    if (K != p + 1 || kB != 1) return false;
    for (int i = 0; i < K; i++) for (int len = 1; len < K; len++) {
        int D = 0; for (int t = 0; t < len; t++) D += d[(i + t) % K];
        if (D > std::min(2 * len + Bv, len + p - 1)) return false;
    }
    return true;
}
static std::map<std::string, long long> lab;                               // label counts (item (iii) only)
static std::map<std::string, long long> labZ;                              // label counts on ZSI-B words
static std::map<std::tuple<int, int, int, int, int, std::string>, long long> openk;   // (k-p,kB,B,excess,type,reason)
static long long n3 = 0, nZ = 0;
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
        for (M rr = q; rr && !C[Q]; rr &= rr - 1) {
            M bt = rr & (~rr + 1u), Qp = q ^ bt;
            if (!C[Qp]) continue;
            if (L[Qp] + L[bt] + L[FULL ^ q] >= 1 && L[q] + L[FULL ^ Qp] + L[FULL ^ bt] >= p + 1) { C[Q] = 1; break; }
        }
        if (!C[Q] && YMAX >= 2 && s >= 3) {
            for (M r1 = q; r1 && !C[Q]; r1 &= r1 - 1) {
                M b1 = r1 & (~r1 + 1u);
                for (M r2 = r1 & (r1 - 1); r2 && !C[Q]; r2 &= r2 - 1) {
                    M b2 = r2 & (~r2 + 1u), Y = b1 | b2, Qp = q ^ Y;
                    if (!C[Y] || !C[Qp]) continue;
                    if (L[Qp] + L[Y] + L[FULL ^ q] >= 1 && L[q] + L[FULL ^ Qp] + L[FULL ^ Y] >= p + 1) C[Q] = 1;
                }
            }
        }
        if (!C[Q] && YMAX >= 3 && s >= 4) {
            for (M r1 = q; r1 && !C[Q]; r1 &= r1 - 1) {
                M b1 = r1 & (~r1 + 1u);
                for (M r2 = r1 & (r1 - 1); r2 && !C[Q]; r2 &= r2 - 1) {
                    M b2 = r2 & (~r2 + 1u);
                    for (M r3 = r2 & (r2 - 1); r3 && !C[Q]; r3 &= r3 - 1) {
                        M b3 = r3 & (~r3 + 1u), Y = b1 | b2 | b3, Qp = q ^ Y;
                        if (!C[Y] || !C[Qp]) continue;
                        if (L[Qp] + L[Y] + L[FULL ^ q] >= 1 && L[q] + L[FULL ^ Qp] + L[FULL ^ Y] >= p + 1) C[Q] = 1;
                    }
                }
            }
        }
        if (!C[Q]) allc = false;
    }
    bool pin = false;
    for (size_t Q = 1; Q < N - 1 && !pin; Q++) if (C[Q] && C[FULL ^ (M)Q] && L[Q] + L[FULL ^ (M)Q] >= 1) pin = true;
    int nev_al = 0, type = 0; bool single = true;
    for (int t = 0; t < K; t++) {
        if (b[t] == 0 && a[t] % 2 == 0) nev_al++;
        if (a[t] + b[t] != 1) single = false;
        if (a[t] == 1 && b[t] == 1) type |= 1; if (a[t] == 0 && b[t] >= 2) type |= 2; if (b[t] == 0 && a[t] >= 2) type |= 4;
    }
    bool wall = single && Bv == 1 && 3 * kB <= p + 4;
    bool Hh = allc && pin;
    bool hyp = nev_al <= 4 || (2 * kB <= p && nev_al <= 2 * kB + 2);
    bool cC = Hh && hyp;
    std::string label = wall ? (cC ? "WALL+C" : "WALL_only") : (cC ? "C" : "open");
    std::string reason = !allc ? "notH_cert" : (!pin ? "notH_pin" : (!hyp ? "hyp" : ""));
    bool zb = zsiB();
    if (zb) { labZ[label]++; nZ++; }
    else {
        lab[label]++; n3++;
        if (label == "open") openk[std::make_tuple(K - p, kB, Bv, Rv - K, type, reason)]++;
    }
    if (dumped < DUMP) {
        dumped++;
        printf("{\"dump\":1,\"p\":%d,\"kB\":%d,\"B\":%d,\"d\":[", p, kB, Bv);
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", d[t]);
        printf("],\"allcert\":%d,\"pin\":%d,\"label\":\"%s\",\"zsiB\":%d}\n", allc ? 1 : 0, pin ? 1 : 0, label.c_str(), zb ? 1 : 0);
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
    printf("{\"summary\":\"%s\",\"p\":%d,\"item_iii_words\":%lld,\"labels\":{", tag, p, n3);
    bool f = true; for (auto& kv : lab) { printf("%s\"%s\":%lld", f ? "" : ",", kv.first.c_str(), kv.second); f = false; }
    printf("},\"zsiB_words\":%lld,\"zsiB_labels\":{", nZ);
    f = true; for (auto& kv : labZ) { printf("%s\"%s\":%lld", f ? "" : ",", kv.first.c_str(), kv.second); f = false; }
    printf("}}\n");
    for (auto& kv : openk) {
        int kp, kb, B, ex, ty; std::string why; std::tie(kp, kb, B, ex, ty, why) = kv.first;
        printf("{\"open\":\"%s\",\"p\":%d,\"k_minus_p\":%d,\"kB\":%d,\"B\":%d,\"excess\":%d,\"type\":%d,\"reason\":\"%s\",\"words\":%lld}\n",
               tag, p, kp, kb, B, ex, ty, why.c_str(), kv.second);
    }
    fflush(stdout);
}
int main(int argc, char** argv) {
    if (argc < 3) return 1;
    p = atoi(argv[2]);
    if (!strcmp(argv[1], "exh")) {
        int kmin = atoi(argv[3]), kmax = atoi(argv[4]); DUMP = atoi(argv[5]); YMAX = atoi(argv[6]);
        for (K = kmin; K <= kmax; K++) { gen(0, 4 * p - 2); fprintf(stderr, "done k=%d\n", K); }
        summary("exh");
    } else {
        int T = atoi(argv[3]); unsigned seed = atoi(argv[4]);
        int kmin = atoi(argv[5]), kmax = atoi(argv[6]); DUMP = atoi(argv[7]); YMAX = atoi(argv[8]);
        std::mt19937 g(seed);
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
