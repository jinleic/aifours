// abcheck.cpp -- [F] exact control for Proposition AB of c6/proof-SEEDB-r1.md (task OlsonRunCount5).
// For every all-single-letter word of a class (p, k, B) (one per rotation class of anti sets), runs the plain singleton-extension
// certification DP over all proper patterns and checks: every interval Q with D_Q <= thr (thr = -4 for kB odd, -5 for kB even) is
// NOT certified (the claim; any certified one is a violation), and counts the certified intervals with D_Q = thr + 1 (they show that
// the threshold is sharp: a mutated claim with thr + 1 would be false).  Usage: abcheck p k B
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
using namespace std;
typedef uint32_t M;
static int p, k, B, kB; static M FULL, ANTI;
static int fl2(int x){ return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static int lam(int y, int m){ int a = p - m + 1, b = y + m - kB, c = fl2(y + B) + 1; int v = a < b ? a : b; return v < c ? v : c; }
static vector<int> pos; static long long words = 0, viol = 0, heavy = 0, sharpCert = 0, sharpTot = 0;
static bool rotmax(){ vector<int> s(k, 0); for (int x : pos) s[x] = 1;
    for (int r = 1; r < k; r++) for (int i = 0; i < k; i++) { int a = s[i], b = s[(i + r) % k]; if (a != b) { if (b > a) return false; break; } }
    return true; }
static void analyse(){
    size_t N = (size_t)1 << k; FULL = (M)(N - 1);
    vector<int8_t> L(N); vector<uint8_t> C(N, 0);
    for (size_t Qs = 1; Qs < N - 1; Qs++) { M Q = (M)Qs; M rot = ((Q << 1) | (Q >> (k - 1))) & FULL;
        L[Q] = (int8_t)lam(__builtin_popcount(Q & ~ANTI) - __builtin_popcount(Q & ANTI), __builtin_popcount(Q & ~rot)); }
    for (size_t Qs = 1; Qs < N - 1; Qs++) { M Q = (M)Qs; if (__builtin_popcount(Q) == 1) { C[Q] = 1; continue; }
        bool ok = false;
        for (M rr = Q; rr && !ok; rr &= rr - 1) { M bt = rr & (~rr + 1u), Qp = Q ^ bt;
            if (C[Qp] && (int)L[Qp] + (int)L[bt] + (int)L[FULL ^ Q] >= 1 && (int)L[Q] + (int)L[FULL ^ Qp] + (int)L[FULL ^ bt] >= p + 1) ok = true; }
        C[Q] = ok; }
    int thr = (kB % 2) ? -4 : -5;
    for (int st = 0; st < k; st++) for (int len = 1; len < k; len++) {
        M Q = 0; int D = 0;
        for (int i = 0; i < len; i++) { int t = (st + i) % k; Q |= (M)1 << t; D += ((ANTI >> t) & 1u) ? -1 : 1; }
        if (D <= thr) { heavy++; if (C[Q]) viol++; }
        if (D == thr + 1) { sharpTot++; if (C[Q]) sharpCert++; }
    }
}
static void rec(int start, int left){
    if (left == 0) { if (!rotmax()) return; ANTI = 0; for (int x : pos) ANTI |= (M)1 << x; analyse(); words++; return; }
    for (int x = start; x <= k - left; x++) { pos.push_back(x); rec(x + 1, left - 1); pos.pop_back(); }
}
int main(int argc, char** argv){
    if (argc < 4) return 1;
    p = atoi(argv[1]); k = atoi(argv[2]); B = atoi(argv[3]); kB = k - p - B;
    if (k > 24 || kB < 1) { printf("{\"error\":\"params\"}\n"); return 1; }
    pos.push_back(0); rec(1, B - 1);
    printf("{\"p\":%d,\"k\":%d,\"B\":%d,\"kB\":%d,\"words\":%lld,\"heavy_intervals\":%lld,\"violations\":%lld,\"thr_plus1_intervals\":%lld,\"thr_plus1_certified\":%lld}\n",
           p, k, B, kB, words, heavy, viol, sharpTot, sharpCert);
    return 0;
}
