// rrchain.cpp -- test of RULE RR (c2/README.md Sec. 9) on NMH words with R <= 2p-3.  Aid only.
// lambda(P) = min(p - m + 1, D_P + m - kB, floor((D_P + B)/2) + 1)  (Lemma H, beta = 0, all-odd words).
// Lemma BC (../../../inverse-parity/proof-PAR-K0.md Sec. 2): ordered partition P_1..P_s (s >= 2) with
//  (a) sum lambda(P_t) >= p+1; (b) 2 <= t <= s-1, X = Q_{t-1}, Y = P_t, Z = Q_t^c:
//      lambda(XuY) + lambda(YuZ) + lambda(ZuX) >= p+1 and lambda(X) + lambda(Y) + lambda(Z) >= 1;
//  (c) lambda(P_s) + lambda(P_s^c) >= 1.
// Modes: exh p kmin kmax | rnd p T seed kmin kmax | pl p T seed
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <random>
#include <cstdint>
#include <map>
#include <tuple>

typedef uint64_t M;
static int p, K, Bv, Av, kB, Dv, Rv, kap;
static int a[64], b[64], l[64], d[64], r[64];
static M FULL;

static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static inline int blocks(M P) {
    M rot = ((P << 1) | (P >> (K - 1))) & FULL;      // bit t of rot = bit t-1 of P
    return __builtin_popcountll(P & ~rot);
}
static inline int Dof(M P) { int D = 0; for (int t = 0; t < K; t++) if ((P >> t) & 1) D += d[t]; return D; }
static inline int lam(M P) {
    int m = blocks(P), D = Dof(P);
    return std::min(p - m + 1, std::min(D + m - kB, fl2(D + Bv) + 1));
}
static bool bc_ok(const std::vector<M>& parts) {
    int s = (int)parts.size(); if (s < 2) return false;
    int sum = 0; for (M P : parts) { if (P == 0 || P == FULL) return false; sum += lam(P); }
    if (sum < p + 1) return false;
    M Q = parts[0];
    for (int t = 1; t + 1 < s; t++) {
        M X = Q, Y = parts[t], Z = FULL & ~(Q | Y);
        if (lam(X | Y) + lam(Y | Z) + lam(Z | X) < p + 1) return false;
        if (lam(X) + lam(Y) + lam(Z) < 1) return false;
        Q |= Y;
    }
    M Ps = parts[s - 1];
    return lam(Ps) + lam(FULL & ~Ps) >= 1;
}
static int rr_s, rr_L, rr_j0, rr_o;
static bool rule_rr() {
    std::vector<M> parts;
    for (int s = 3; s <= K; s++)
        for (int L = s - 1; L <= K - 1; L++)
            for (int j0 = 0; j0 < K; j0++)
                for (int o = 1; o >= -1; o -= 2) {
                    parts.assign(s, 0);
                    M J = 0;
                    for (int i = 0; i < L; i++) {
                        int run = ((j0 + o * i) % K + K) % K;
                        parts[i % (s - 1)] |= (M)1 << run; J |= (M)1 << run;
                    }
                    parts[s - 1] = FULL & ~J;
                    if (bc_ok(parts)) { rr_s = s; rr_L = L; rr_j0 = j0; rr_o = o; return true; }
                }
    return false;
}
static bool zsiB() {   // Lemma ZSI-B: k = p+1, kB = 1 and (4.1)
    if (K != p + 1 || kB != 1) return false;
    for (int i = 0; i < K; i++) for (int len = 1; len < K; len++) {
        int D = 0; for (int t = 0; t < len; t++) D += d[(i + t) % K];
        if (D > std::min(2 * len + Bv, len + p - 1)) return false;
    }
    return true;
}
struct St { long long n = 0, ok = 0; };
static std::map<std::tuple<int, int, int, int, int>, St> stats;   // (k-p, kB, B, R-2p, zsiB)
static std::map<std::pair<int, int>, long long> sdist;            // (s, L - (s-1)) of the RR output
static long long nfail = 0, nskipR = 0;
static void process() {
    Av = 0; Bv = 0; int H = 0;
    for (int t = 0; t < K; t++) { Av += a[t]; Bv += b[t]; d[t] = a[t] - b[t]; H += l[t] / 2; }
    kap = p - 1 - H; kB = kap - Bv; Dv = Av - Bv; Rv = Av + Bv;
    if (Rv > 2 * p - 3) { nskipR++; return; }
    FULL = (K == 64) ? ~(M)0 : (((M)1 << K) - 1);
    int zb = zsiB() ? 1 : 0;
    St& S = stats[std::make_tuple(K - p, kB, Bv, Rv - 2 * p, zb)];
    S.n++;
    if (rule_rr()) { S.ok++; sdist[std::make_pair(rr_s, rr_L - (rr_s - 1))]++; return; }
    nfail++;
    if (nfail <= 30) {
        printf("{\"RR_FAIL\":1,\"p\":%d,\"k\":%d,\"R\":%d,\"B\":%d,\"kB\":%d,\"zsiB\":%d,\"d\":[", p, K, Rv, Bv, kB, zb);
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", d[t]);
        printf("],\"a\":[");
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", a[t]);
        printf("],\"b\":[");
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", b[t]);
        printf("],\"l\":[");
        for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", l[t]);
        printf("]}\n");
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
    long long n = 0, ok = 0, nz = 0, okz = 0;
    for (auto& kv : stats) {
        int kp, kb, B, rr, zb; std::tie(kp, kb, B, rr, zb) = kv.first;
        printf("{\"summary\":\"%s\",\"p\":%d,\"k_minus_p\":%d,\"kB\":%d,\"B\":%d,\"R_minus_2p\":%d,\"zsiB\":%d,\"words\":%lld,\"RR_ok\":%lld}\n",
               tag, p, kp, kb, B, rr, zb, kv.second.n, kv.second.ok);
        if (zb) { nz += kv.second.n; okz += kv.second.ok; } else { n += kv.second.n; ok += kv.second.ok; }
    }
    for (auto& kv : sdist) printf("{\"sdist\":\"%s\",\"p\":%d,\"s\":%d,\"L_minus_s_plus_1\":%d,\"count\":%lld}\n", tag, p, kv.first.first, kv.first.second, kv.second);
    printf("{\"total\":\"%s\",\"p\":%d,\"words_nonZSIB\":%lld,\"RR_ok_nonZSIB\":%lld,\"words_ZSIB\":%lld,\"RR_ok_ZSIB\":%lld,\"skipped_R_gt_2p-3\":%lld}\n",
           tag, p, n, ok, nz, okz, nskipR);
    fflush(stdout);
}
int main(int argc, char** argv) {
    if (argc < 3) return 1;
    p = atoi(argv[2]);
    if (!strcmp(argv[1], "exh")) {
        int kmin = atoi(argv[3]), kmax = atoi(argv[4]);
        for (K = kmin; K <= kmax; K++) { gen(0, 4 * p - 2); fprintf(stderr, "done k=%d\n", K); }
        summary("exh");
    } else if (!strcmp(argv[1], "pl")) {   // planted generator copied from ../boundviol.cpp
        int T = atoi(argv[3]); unsigned seed = atoi(argv[4]);
        std::mt19937 rng(seed);
        int N = 4 * p - 2, done = 0; long long tries = 0;
        while (done < T && tries < 100000000LL) {
            tries++;
            K = p + 1;
            int Bmax = (p - 5) / 2; if (Bmax < 2) break;
            int B = 2 + rng() % (Bmax - 1);
            int kp = B + 1, H = p - 1 - kp, F = K + 2 * H, R = N - F, A = R - B;
            if (R > 2 * p - 3 || A > 2 * p - 1 || A < B) continue;
            int n0 = rng() % 2; if (n0 > B - 2) n0 = 0;
            int Bp = B - n0;
            int na = 2 + rng() % (Bp - 1);
            if (na > Bp) continue;
            int nal = K - n0 - na;
            int Ap = A - n0;
            int ah = B + 3 + rng() % 3;
            if (Ap - ah < nal - 1 || nal < 1) continue;
            std::vector<int> ca(nal - 1, 1), cb(na, 1);
            for (int i = 0; i < Ap - ah - (nal - 1); i++) ca[rng() % (nal - 1)]++;
            for (int i = 0; i < Bp - na; i++) cb[rng() % na]++;
            std::vector<int> kinds;
            kinds.push_back(3);
            for (int i = 0; i < nal - 1; i++) kinds.push_back(0);
            for (int i = 0; i < na; i++) kinds.push_back(1);
            for (int i = 0; i < n0; i++) kinds.push_back(2);
            std::shuffle(kinds.begin(), kinds.end(), rng);
            int ia = 0, ib = 0;
            for (int t = 0; t < K; t++) {
                if (kinds[t] == 3) { a[t] = ah; b[t] = 0; }
                else if (kinds[t] == 0) { a[t] = ca[ia++]; b[t] = 0; }
                else if (kinds[t] == 1) { a[t] = 0; b[t] = cb[ib++]; }
                else { a[t] = 1; b[t] = 1; }
                l[t] = 1;
            }
            for (int i = 0; i < H; i++) l[rng() % K] += 2;
            process(); done++;
        }
        summary("pl");
    } else {   // rnd generator copied from ../bcgcheck.cpp
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
        summary("rnd");
    }
    return 0;
}
