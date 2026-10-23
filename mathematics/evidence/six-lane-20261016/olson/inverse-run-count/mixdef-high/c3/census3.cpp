// census3.cpp -- c3 (task OlsonRunCount3), README Sec. 3 P1(a): singleton-extension certification census on
// item-(iii) words: all-odd, pure/(1,1) runs, p+1 <= k <= 2p-2, 1 <= B <= kappa-1, B <= A <= 2p-1, R <= 2p-3,
// ZSI-B words (k = p+1, kB = 1, (4.1)) flagged.  Generators copied from c2/rrchain.cpp (exh / rnd).
// lambda(Q) = min(p - m + 1, D_Q + m - kB, floor((D_Q + B)/2) + 1)   (Lemma H, beta = 0).
// Certified (c2/proof-NOLP.md (1.1)): |Q| = 1, or Q = Q' u {t}, Q' certified,
//   lambda(Q') + lambda(t) + lambda(Q^c) >= 1 and lambda(Q) + lambda(Q'^c) + lambda(t^c) >= p + 1.
// Per word: s* = max s such that every proper pattern with <= s runs is certified; allcert; pin = some certified
// Q0 with certified complement and lambda(Q0) + lambda(Q0^c) >= 1.  Aggregated by
// (k-p, kB, B, R-k, type) with type bits: 1 = has (1,1)-pair, 2 = has anti run with b >= 2, 4 = has aligned a >= 2.
// Modes: exh p kmin kmax | rnd p T seed kmin kmax.  Aid only.
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
struct St { long long n = 0, allc = 0, pin = 0, allc_pin = 0; std::map<int, long long> sstar; };
static std::map<std::tuple<int, int, int, int, int, int>, St> stats;   // (k-p, kB, B, R-k, type, zsiB)
static long long nwords = 0;
static void process() {
    Av = 0; Bv = 0; int H = 0;
    for (int t = 0; t < K; t++) { Av += a[t]; Bv += b[t]; d[t] = a[t] - b[t]; H += l[t] / 2; }
    kap = p - 1 - H; kB = kap - Bv; Rv = Av + Bv;
    if (Rv > 2 * p - 3) return;
    FULL = (1u << K) - 1;
    size_t N = (size_t)1 << K;
    if (L.size() < N) { L.resize(N); C.resize(N); }
    for (size_t Q = 1; Q < N - 1; Q++) L[Q] = (int8_t)lamc((M)Q);
    std::vector<long long> tot(K + 1, 0), cer(K + 1, 0);
    C[0] = 0;
    for (size_t Q = 1; Q < N - 1; Q++) {
        M q = (M)Q; int s = __builtin_popcount(q); tot[s]++; C[Q] = 0;
        if (s == 1) { C[Q] = 1; cer[s]++; continue; }
        for (M rr = q; rr; rr &= rr - 1) {
            M bt = rr & (~rr + 1u), Qp = q ^ bt;
            if (!C[Qp]) continue;
            if (L[Qp] + L[bt] + L[FULL ^ q] >= 1 && L[q] + L[FULL ^ Qp] + L[FULL ^ bt] >= p + 1) { C[Q] = 1; break; }
        }
        if (C[Q]) cer[s]++;
    }
    int sstar = K - 1;
    for (int s = 1; s < K; s++) if (cer[s] != tot[s]) { sstar = s - 1; break; }
    bool allc = (sstar == K - 1);
    bool pin = false;
    for (size_t Q = 1; Q < N - 1 && !pin; Q++) if (C[Q] && C[FULL ^ (M)Q] && L[Q] + L[FULL ^ (M)Q] >= 1) pin = true;
    int type = 0;
    for (int t = 0; t < K; t++) { if (a[t] == 1 && b[t] == 1) type |= 1; if (a[t] == 0 && b[t] >= 2) type |= 2; if (b[t] == 0 && a[t] >= 2) type |= 4; }
    St& S = stats[std::make_tuple(K - p, kB, Bv, Rv - K, type, zsiB() ? 1 : 0)];
    S.n++; if (allc) S.allc++; if (pin) S.pin++; if (allc && pin) S.allc_pin++; S.sstar[sstar]++;
    nwords++;
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
    for (auto& kv : stats) {
        int kp, kb, B, ex, ty, zb; std::tie(kp, kb, B, ex, ty, zb) = kv.first;
        printf("{\"tag\":\"%s\",\"p\":%d,\"k_minus_p\":%d,\"kB\":%d,\"B\":%d,\"excess\":%d,\"type\":%d,\"zsiB\":%d,\"words\":%lld,\"allcert\":%lld,\"pin\":%lld,\"allcert_and_pin\":%lld,\"sstar\":{",
               tag, p, kp, kb, B, ex, ty, zb, kv.second.n, kv.second.allc, kv.second.pin, kv.second.allc_pin);
        bool first = true;
        for (auto& s : kv.second.sstar) { printf("%s\"%d\":%lld", first ? "" : ",", s.first, s.second); first = false; }
        printf("}}\n");
    }
    printf("{\"total\":\"%s\",\"p\":%d,\"words\":%lld}\n", tag, p, nwords);
    fflush(stdout);
}
int main(int argc, char** argv) {
    if (argc < 3) return 1;
    p = atoi(argv[2]);
    if (!strcmp(argv[1], "exh")) {
        int kmin = atoi(argv[3]), kmax = atoi(argv[4]);
        for (K = kmin; K <= kmax; K++) { gen(0, 4 * p - 2); fprintf(stderr, "done k=%d\n", K); }
        summary("exh");
    } else {   // rnd generator copied from c2/rrchain.cpp (from ../bcgcheck.cpp)
        int T = atoi(argv[3]); unsigned seed = atoi(argv[4]);
        int kmin = atoi(argv[5]), kmax = atoi(argv[6]);
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
            if (R > 2 * p - 3) continue;
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
                l[t] = 1; r[t] = a[t] + b[t];
            }
            for (int i = 0; i < H; i++) l[rng() % K] += 2;
            process(); done++;
        }
        summary("rnd");
    }
    return 0;
}
