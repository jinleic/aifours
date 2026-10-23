// rcert.cpp -- [F] per-word certificates for all-single-letter item-(iii) words with B anti runs (c6, task OlsonRunCount5).
// Word: k single-letter rotation runs on a cycle, anti set A (d = -1), aligned otherwise (d = +1); kappa = k - p, kB = kappa - B.
// lambda(Q) = lam(y, m) = min(p - m + 1, y + m - kB, floor((y + B)/2) + 1), y = D_Q, m = blocks; U(Q) = p - lambda(Q^c).
// Computes, for each word (one per rotation class, or per dihedral class with mode 'dih'):
//   (H)   plain singleton extension certifies EVERY proper pattern, and a pin pair exists (c3 definition);
//   (H')  for every proper Q, Q or Q^c is certified (plain), and a pin pair exists           [Lemma CC];
//   (Hs0) seeded certification (seed ranges = hull of the canonical lifts compatible with ALL two-pattern differences
//         u_t = u_(Q+t) - u_Q, Q any proper pattern not containing t with Q + t proper), every proper pattern, + seeded pin
//         (this is c5's (H^s); "seedEmpty" = some run has no compatible canonical lift, i.e. the word has no avoider);
//   (H's) as (Hs0) but complement-closed (Q or Q^c seeded-certified).
// Seeds are computed at the TYPE level: lambda depends only on (y, m), so for each run t a DP along the path t+1, ..., t-1
// finds every realisable (j aligned, e anti, m blocks, c = number of neighbours of t in Q) of patterns Q not containing t;
// then Q + t has y + d_t and m + 1 - c blocks.
// Output: per-word JSON lines for words failing (H) (with anti-block sizes, a smallest pattern Q with neither Q nor Q^c
// certified (plain), and the same for seeded), and a per-class summary line.  Native limit: stops itself after TLIM s.
// Usage: rcert p k B mode [TLIM]   mode = rot | dih
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <cstring>
#include <vector>
#include <string>
#include <chrono>
#include <algorithm>
using namespace std;
typedef uint32_t M;
static int p, k, B, kap, kB, n;
static M FULL, ANTI;
static vector<int8_t> L;
static vector<uint8_t> C, Cs;
static int fl2(int x){ return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static int lam(int y, int m){ int a = p - m + 1, b = y + m - kB, c = fl2(y + B) + 1; int v = a < b ? a : b; return v < c ? v : c; }
static int lamc(int y, int m){ int D = n - B; return lam(D - y, m); }   // complement: D_(Q^c) = D - y, same m
static int Uym(int y, int m){ return p - lamc(y, m); }
static inline int blocksOf(M Q){ M rot = ((Q << 1) | (Q >> (k - 1))) & FULL; return __builtin_popcount(Q & ~rot); }
static inline int yOf(M Q){ return __builtin_popcount(Q & ~ANTI) - __builtin_popcount(Q & ANTI); }
struct WordRes { bool H, Hp, Hs0, Hsp, seedEmpty; int minNC, minNCs; M exNC, exNCs; int seedlo[32], seedhi[32]; bool noncontig; };
static WordRes analyse(){
    WordRes R; memset(&R, 0, sizeof(R));
    size_t N = (size_t)1 << k; FULL = (M)(N - 1);
    L.resize(N); C.assign(N, 0); Cs.assign(N, 0);
    for (size_t Qs = 1; Qs < N - 1; Qs++) { M Q = (M)Qs; L[Q] = (int8_t)lam(yOf(Q), blocksOf(Q)); }
    auto U = [&](M Q){ return p - (int)L[FULL ^ Q]; };
    // ---- seeds (type-level DP per run)
    int lo[32], hi[32]; bool seedEmpty = false, noncontig = false;
    for (int t = 0; t < k; t++) {
        int dt = ((ANTI >> t) & 1u) ? -1 : 1;
        M bt = (M)1 << t;
        int L1 = L[bt], U1 = U(bt);
        // feasible states along the path t+1, ..., t-1: idx = ((j*(B+1)+e)*(MB+1)+m)*4 + first*2 + last
        int MB = k / 2 + 1;
        auto IDX = [&](int j, int e, int m, int f, int l){ return (((j * (B + 1) + e) * (MB + 1) + m) * 2 + f) * 2 + l; };
        size_t S = (size_t)(n + 1) * (B + 1) * (MB + 1) * 4;
        vector<uint8_t> cur(S, 0), nxt(S, 0);
        // position 0 of the path = run t+1
        int r0 = (t + 1) % k; bool a0 = (ANTI >> r0) & 1u;
        // state before any position: empty pattern; we encode 'first' = membership of the first path run, 'last' = membership of current run
        // start: run r0 out -> (0,0,0,f=0,l=0); run r0 in -> (j,e,1,f=1,l=1)
        cur[IDX(0, 0, 0, 0, 0)] = 1;
        if (a0) cur[IDX(0, 1, 1, 1, 1)] = 1; else cur[IDX(1, 0, 1, 1, 1)] = 1;
        for (int i = 1; i < k - 1; i++) {
            int r = (t + 1 + i) % k; bool an = (ANTI >> r) & 1u;
            fill(nxt.begin(), nxt.end(), 0);
            for (int j = 0; j <= n; j++) for (int e = 0; e <= B; e++) for (int m = 0; m <= MB; m++) for (int f = 0; f < 2; f++) for (int l = 0; l < 2; l++) {
                if (!cur[IDX(j, e, m, f, l)]) continue;
                nxt[IDX(j, e, m, f, 0)] = 1;                              // r out
                int j2 = j + (an ? 0 : 1), e2 = e + (an ? 1 : 0), m2 = m + (l ? 0 : 1);
                if (j2 <= n && e2 <= B && m2 <= MB) nxt[IDX(j2, e2, m2, f, 1)] = 1;   // r in
            }
            swap(cur, nxt);
        }
        uint64_t FP = (p >= 64) ? ~0ull : ((1ull << p) - 1);
        uint64_t mask = 0;
        for (int y = L1; y <= U1; y++) mask |= 1ull << (((y % p) + p) % p);
        for (int j = 0; j <= n; j++) for (int e = 0; e <= B; e++) for (int m = 0; m <= MB; m++) for (int f = 0; f < 2; f++) for (int l = 0; l < 2; l++) {
            if (!cur[IDX(j, e, m, f, l)]) continue;
            int s = j + e; if (s == 0 || s + 1 >= k) continue;      // Q nonempty, Q + t proper
            int c = f + l; if (k - 1 == 1) c = f;                   // neighbours of t: first and last path runs
            int y = j - e, mt = m + 1 - c;
            int a = lam(y + dt, mt) - Uym(y, m), b = Uym(y + dt, mt) - lam(y, m);
            if (b - a + 1 >= p) continue;
            uint64_t m2 = 0;
            if (b >= a) for (int z = a; z <= b; z++) m2 |= 1ull << (((z % p) + p) % p);
            mask &= m2;
        }
        mask &= FP;
        if (!mask) { seedEmpty = true; lo[t] = 1; hi[t] = 0; continue; }
        int mn = 1 << 30, mx = -(1 << 30), cnt = 0;
        for (int y = L1; y <= U1; y++) if ((mask >> (((y % p) + p) % p)) & 1ull) { mn = min(mn, y); mx = max(mx, y); cnt++; }
        if (cnt != mx - mn + 1) noncontig = true;
        lo[t] = mn; hi[t] = mx;
    }
    for (int t = 0; t < k; t++) { R.seedlo[t] = lo[t]; R.seedhi[t] = hi[t]; }
    R.seedEmpty = seedEmpty; R.noncontig = noncontig;
    // ---- certification DPs
    for (size_t Qs = 1; Qs < N - 1; Qs++) {
        M Q = (M)Qs; int s = __builtin_popcount(Q);
        if (s == 1) { C[Q] = 1; Cs[Q] = seedEmpty ? 0 : 1; continue; }
        bool ok = false, oks = seedEmpty;   // seedEmpty: seeded part not used (the word is already excluded)
        int wlo = 1 - (int)L[FULL ^ Q], whi = p + (int)L[Q] - 1;
        for (M rr = Q; rr && !(ok && oks); rr &= rr - 1) {
            M bt = rr & (~rr + 1u), Qp = Q ^ bt; int t = __builtin_ctz(bt);
            bool single = (Qp & (Qp - 1)) == 0;
            int lq, hq;
            if (single) { lq = L[Qp]; hq = U(Qp); } else { lq = L[Qp]; hq = U(Qp); }
            if (!ok && C[Qp] && lq + (int)L[bt] >= wlo && hq + U(bt) <= whi) ok = true;
            if (!oks && Cs[Qp]) {
                int ls, hs;
                if (single) { int t2 = __builtin_ctz(Qp); ls = lo[t2]; hs = hi[t2]; } else { ls = L[Qp]; hs = U(Qp); }
                if (ls + lo[t] >= wlo && hs + hi[t] <= whi) oks = true;
            }
        }
        C[Q] = ok; Cs[Q] = (oks && !seedEmpty);
    }
    // ---- pins and closure
    bool pin = false, pins = false;
    for (size_t Qs = 1; Qs < N - 1 && !(pin && pins); Qs++) {
        M Q = (M)Qs, Qc = FULL ^ Q;
        if (!pin && C[Q] && C[Qc] && (int)L[Q] + (int)L[Qc] >= 1) pin = true;
        if (!pins && !seedEmpty && Cs[Q] && Cs[Qc]) {
            bool s1 = (Q & (Q - 1)) == 0, s2 = (Qc & (Qc - 1)) == 0;
            int l1 = s1 ? lo[__builtin_ctz(Q)] : L[Q], h1 = s1 ? hi[__builtin_ctz(Q)] : U(Q);
            int l2 = s2 ? lo[__builtin_ctz(Qc)] : L[Qc], h2 = s2 ? hi[__builtin_ctz(Qc)] : U(Qc);
            if (l1 + l2 >= 1 && h1 + h2 <= 2 * p - 1) pins = true;
        }
    }
    bool allc = true, alls = true, cc = true, ccs = true;
    R.minNC = R.minNCs = 99;
    for (size_t Qs = 1; Qs < N - 1; Qs++) {
        M Q = (M)Qs, Qc = FULL ^ Q; int s = __builtin_popcount(Q);
        if (!C[Q]) allc = false;
        if (!Cs[Q]) alls = false;
        if (!C[Q] && !C[Qc]) { cc = false; int sm = min(s, k - s); if (sm < R.minNC) { R.minNC = sm; R.exNC = (s <= k - s) ? Q : Qc; } }
        if (!Cs[Q] && !Cs[Qc]) { ccs = false; int sm = min(s, k - s); if (sm < R.minNCs) { R.minNCs = sm; R.exNCs = (s <= k - s) ? Q : Qc; } }
    }
    R.H = allc && pin; R.Hp = cc && pin;
    R.Hs0 = seedEmpty || (alls && pins); R.Hsp = seedEmpty || (ccs && pins);
    return R;
}
static vector<int> pos;
static long long words = 0, nH = 0, nHp = 0, nHs0 = 0, nHsp = 0, nSE = 0, nNone = 0, nNonc = 0;
static int MODE = 0;   // 0 rot, 1 dih
static bool canon(const vector<int>& ps){
    vector<int> s(k, 0); for (int x : ps) s[x] = 1;
    // keep iff s is lexicographically maximal among all rotations (and reflections if MODE == 1)
    for (int refl = 0; refl <= MODE; refl++) for (int r = 0; r < k; r++) {
        if (r == 0 && refl == 0) continue;
        for (int i = 0; i < k; i++) {
            int a = s[i], b = refl ? s[((r - i) % k + k) % k] : s[(i + r) % k];
            if (a != b) { if (b > a) return false; break; }
        }
    }
    return true;
}
static string blocksStr(){
    // sizes of maximal anti blocks (cyclic)
    vector<int> s(k, 0); for (int x : pos) s[x] = 1;
    string out; int start = -1;
    for (int i = 0; i < k; i++) if (!s[i]) { start = i; break; }
    if (start < 0) return "all";
    int run = 0; bool first = true;
    for (int c = 1; c <= k; c++) { int i = (start + c) % k; if (s[i]) run++; else { if (run) { out += (first ? "" : ","); out += to_string(run); first = false; } run = 0; } }
    return out;
}
static double TLIM = 1e9; static chrono::steady_clock::time_point T0;
static bool stopped = false;
static void rec(int start, int left){
    if (stopped) return;
    if (left == 0) {
        if (!canon(pos)) return;
        ANTI = 0; for (int x : pos) ANTI |= (M)1 << x;
        WordRes r = analyse(); words++;
        nH += r.H; nHp += r.Hp; nHs0 += r.Hs0; nHsp += r.Hsp; nSE += r.seedEmpty; nNonc += r.noncontig;
        if (!r.H && !r.Hp && !r.Hsp) nNone++;
        if (!r.H) {
            printf("{\"p\":%d,\"k\":%d,\"B\":%d,\"kB\":%d,\"anti\":[", p, k, B, kB);
            for (size_t i = 0; i < pos.size(); i++) printf("%s%d", i ? "," : "", pos[i]);
            printf("],\"antiblocks\":\"%s\",\"H\":%d,\"Hp\":%d,\"Hs0\":%d,\"Hsp\":%d,\"seedEmpty\":%d,\"noncontig\":%d", blocksStr().c_str(), r.H, r.Hp, r.Hs0, r.Hsp, r.seedEmpty, r.noncontig);
            if (!r.Hp && r.minNC < 99) printf(",\"minNC\":%d,\"exNC\":%u", r.minNC, r.exNC);
            if (!r.Hsp && r.minNCs < 99) printf(",\"minNCs\":%d,\"exNCs\":%u", r.minNCs, r.exNCs);
            printf(",\"seeds\":\"");
            for (int t = 0; t < k; t++) printf("%s%d:%d", t ? " " : "", r.seedlo[t], r.seedhi[t]);
            printf("\"}\n");
            fflush(stdout);
        }
        double el = chrono::duration<double>(chrono::steady_clock::now() - T0).count();
        if (el > TLIM) { stopped = true; }
        return;
    }
    for (int x = start; x <= k - left; x++) { pos.push_back(x); rec(x + 1, left - 1); pos.pop_back(); if (stopped) return; }
}
int main(int argc, char** argv){
    if (argc < 5) return 1;
    p = atoi(argv[1]); k = atoi(argv[2]); B = atoi(argv[3]); MODE = strcmp(argv[4], "dih") == 0 ? 1 : 0;
    if (argc > 5) TLIM = atof(argv[5]);
    kap = k - p; kB = kap - B; n = k - B;
    if (k > 28 || p > 61 || B < 1 || kB < 1) { printf("{\"error\":\"params\"}\n"); return 1; }
    T0 = chrono::steady_clock::now();
    pos.push_back(0); rec(1, B - 1);
    double el = chrono::duration<double>(chrono::steady_clock::now() - T0).count();
    printf("{\"summary\":1,\"p\":%d,\"k\":%d,\"B\":%d,\"kB\":%d,\"mode\":\"%s\",\"words\":%lld,\"H\":%lld,\"Hp\":%lld,\"Hs0\":%lld,\"Hsp\":%lld,\"seedEmpty\":%lld,\"noncontig\":%lld,\"none\":%lld,\"complete\":%d,\"sec\":%.1f}\n",
           p, k, B, kB, MODE ? "dih" : "rot", words, nH, nHp, nHs0, nHsp, nSE, nNonc, nNone, stopped ? 0 : 1, el);
    return 0;
}
