// allsing.cpp -- [F] EXPLORATORY (c5, task OlsonRunCount5, README Sec. 7): for all-singleton all-odd words (k single-letter
// rotation runs, B of them rho_(-1) at given positions, kappa = k - p, kB = kappa - B), decide
//   (H)   : every proper pattern certified by plain singleton extension (Lemma L) + a pin pair (c3/proof-C-r1.md);
//   (H^s) : the same with SEEDED singleton ranges (Lemma SL of c5/proof-SEED-r2.md): for every run t the seed set is the set
//           of canonical lifts y in [lambda({t}), p - lambda({t}^c)] with y = some element of [lambda(Q+t) - U(Q), U(Q+t) -
//           lambda(Q)] (mod p) for EVERY proper Q not containing t with Q + t proper (two-pattern seeds, all Q); the seed
//           range is its hull ("seed-empty" if the set is empty: then the word has no avoider at all).
// If (H) or (H^s) holds, (0.2) of c3/proof-C-r1.md holds and Corollary S (all-singleton words) excludes the word.
// This tool is an exploration aid only (no written proof uses it).
// Usage: allsing p k B [mode]   mode 0: all anti-position sets containing 0 that are lexicographically minimal under
//        rotation (one word per rotation class); prints one JSON line per word and a summary.
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
#include <algorithm>
using namespace std;
static int p, k, B, kap, kB;
static vector<int8_t> L;      // lambda(Q)
static vector<uint8_t> C, Cs;  // certified (plain), certified (seeded)
static int fl2(int x){ return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static int d[64];
static uint32_t FULL;
static int lamOf(uint32_t Q){
    uint32_t rot = ((Q << 1) | (Q >> (k - 1))) & FULL;
    int m = __builtin_popcount(Q & ~rot), D = 0;
    for (int t = 0; t < k; t++) if ((Q >> t) & 1u) D += d[t];
    int a = p - m + 1, b = D + B - kap + m, c = fl2(D + B) + 1;
    int v = a < b ? a : b; return v < c ? v : c;
}
struct Res { bool H, Hs, seedEmpty; int ncert, ncerts; };
static Res analyse(){
    size_t N = (size_t)1 << k; FULL = (uint32_t)(N - 1);
    L.resize(N); C.assign(N, 0); Cs.assign(N, 0);
    for (size_t Q = 1; Q < N - 1; Q++) L[Q] = (int8_t)lamOf((uint32_t)Q);
    auto U = [&](uint32_t Q){ return p - (int)L[FULL ^ Q]; };
    // seeds
    vector<int> lo(k), hi(k); bool seedEmpty = false;
    for (int t = 0; t < k; t++) {
        uint32_t bt = 1u << t;
        int L1 = L[bt], U1 = U(bt);
        uint64_t mask = 0;   // residues allowed (bit r: residue r mod p)
        for (int y = L1; y <= U1; y++) mask |= 1ull << (((y % p) + p) % p);
        for (uint32_t Q = 1; Q < FULL; Q++) {
            if (Q & bt) continue;
            uint32_t Qt = Q | bt; if (Qt == FULL) continue;
            int a = L[Qt] - U(Q), b = U(Qt) - L[Q];
            if (b - a + 1 >= p) continue;
            uint64_t m2 = 0;
            for (int y = a; y <= b; y++) m2 |= 1ull << (((y % p) + p) % p);
            mask &= m2;
            if (!mask) break;
        }
        if (!mask) { seedEmpty = true; lo[t] = 1; hi[t] = 0; continue; }
        int mn = 1 << 30, mx = -(1 << 30);
        for (int y = L1; y <= U1; y++) if ((mask >> (((y % p) + p) % p)) & 1ull) { mn = min(mn, y); mx = max(mx, y); }
        lo[t] = mn; hi[t] = mx;
    }
    // plain (H) and seeded (H^s) certification DP
    int ncert = 0, ncerts = 0; bool allc = true, allcs = true;
    for (size_t Qs = 1; Qs < N - 1; Qs++) {
        uint32_t Q = (uint32_t)Qs; int s = __builtin_popcount(Q);
        if (s == 1) { C[Q] = Cs[Q] = 1; ncert++; ncerts++; continue; }
        bool ok = false, oks = false;
        for (uint32_t rr = Q; rr && !(ok && oks); rr &= rr - 1) {
            uint32_t bt = rr & (~rr + 1u), Qp = Q ^ bt; int t = __builtin_ctz(bt);
            if (!ok && C[Qp] && L[Qp] + L[bt] + L[FULL ^ Q] >= 1 && L[Q] + L[FULL ^ Qp] + L[FULL ^ bt] >= p + 1) ok = true;
            if (!oks && Cs[Qp] && !seedEmpty) {
                int lq, hq;
                if (__builtin_popcount(Qp) == 1) { int t2 = __builtin_ctz(Qp); lq = lo[t2]; hq = hi[t2]; }
                else { lq = L[Qp]; hq = U(Qp); }
                if (lq + lo[t] >= 1 - L[FULL ^ Q] && hq + hi[t] <= p + L[Q] - 1) oks = true;
            }
        }
        C[Q] = ok; Cs[Q] = oks; ncert += ok; ncerts += oks;
        if (!ok) allc = false; if (!oks) allcs = false;
    }
    bool pin = false, pins = false;
    for (size_t Qs = 1; Qs < N - 1 && !(pin && pins); Qs++) {
        uint32_t Q = (uint32_t)Qs, Qc = FULL ^ Q;
        if (C[Q] && C[Qc] && L[Q] + L[Qc] >= 1) pin = true;
        if (Cs[Q] && Cs[Qc] && !seedEmpty) {
            int l1 = __builtin_popcount(Q) == 1 ? lo[__builtin_ctz(Q)] : L[Q];
            int h1 = __builtin_popcount(Q) == 1 ? hi[__builtin_ctz(Q)] : U(Q);
            int l2 = __builtin_popcount(Qc) == 1 ? lo[__builtin_ctz(Qc)] : L[Qc];
            int h2 = __builtin_popcount(Qc) == 1 ? hi[__builtin_ctz(Qc)] : U(Qc);
            if (l1 + l2 >= 1 && h1 + h2 <= 2 * p - 1) pins = true;
        }
    }
    return Res{allc && pin, (allcs && pins) || seedEmpty, seedEmpty, ncert, ncerts};
}
static vector<int> pos;
static long long words = 0, nH = 0, nHs = 0, nSE = 0, nNone = 0;
static bool rotmin(const vector<int>& ps){
    // anti-position set as a k-bit cyclic string; keep it iff lexicographically minimal among rotations
    vector<int> s(k, 0); for (int x : ps) s[x] = 1;
    for (int r = 1; r < k; r++) {
        for (int i = 0; i < k; i++) { int a = s[i], b = s[(i + r) % k]; if (a != b) { if (b > a) return false; break; } }
    }
    return true;
}
static void rec(int start, int left){
    if (left == 0) {
        if (!rotmin(pos)) return;
        for (int t = 0; t < k; t++) d[t] = 1;
        for (int x : pos) d[x] = -1;
        Res r = analyse(); words++;
        if (r.H) nH++; if (r.Hs) nHs++; if (r.seedEmpty) nSE++; if (!r.H && !r.Hs) nNone++;
        if (!r.H || !r.Hs) {
            printf("{\"p\":%d,\"k\":%d,\"B\":%d,\"kB\":%d,\"anti\":[", p, k, B, kB);
            for (size_t i = 0; i < pos.size(); i++) printf("%s%d", i ? "," : "", pos[i]);
            printf("],\"H\":%d,\"Hs\":%d,\"seedEmpty\":%d,\"cert\":%d,\"certs\":%d}\n", r.H, r.Hs, r.seedEmpty, r.ncert, r.ncerts);
        }
        return;
    }
    for (int x = start; x <= k - left; x++) { pos.push_back(x); rec(x + 1, left - 1); pos.pop_back(); }
}
int main(int argc, char** argv){
    if (argc < 4) return 1;
    p = atoi(argv[1]); k = atoi(argv[2]); B = atoi(argv[3]);
    kap = k - p; kB = kap - B;
    if (k > 26 || p > 61) { printf("{\"error\":\"size\"}\n"); return 1; }
    pos.push_back(0); rec(1, B - 1);
    printf("{\"summary\":1,\"p\":%d,\"k\":%d,\"B\":%d,\"kB\":%d,\"words\":%lld,\"H\":%lld,\"Hs\":%lld,\"seedEmpty\":%lld,\"neither\":%lld}\n",
           p, k, B, kB, words, nH, nHs, nSE, nNone);
    return 0;
}
