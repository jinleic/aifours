// rmin.cpp -- [F] structure of the patterns NOT certified by plain singleton extension (Lemma L) in one all-single-letter
// word (c6, task OlsonRunCount5; structural analysis of the (H)-failures of the T1 census).  Prints the number of uncertified
// proper patterns, their size histogram, and up to 12 examples of minimal size with (j aligned, e anti, m blocks) and the
// pattern as a 0/1 string starting at run 0.  Usage: rmin p k a1,a2,...   (anti positions)
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
#include <string>
using namespace std;
typedef uint32_t M;
static int p, k, B, kB, n; static M FULL, ANTI;
static int fl2(int x){ return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static int lam(int y, int m){ int a = p - m + 1, b = y + m - kB, c = fl2(y + B) + 1; int v = a < b ? a : b; return v < c ? v : c; }
int main(int argc, char** argv){
    if (argc < 4) return 1;
    p = atoi(argv[1]); k = atoi(argv[2]);
    string s(argv[3]); ANTI = 0; B = 0; size_t i = 0;
    while (i < s.size()) { size_t j = s.find(',', i); if (j == string::npos) j = s.size(); ANTI |= (M)1 << atoi(s.substr(i, j - i).c_str()); B++; i = j + 1; }
    kB = k - p - B; n = k - B; FULL = (M)(((uint64_t)1 << k) - 1);
    size_t N = (size_t)1 << k;
    vector<int8_t> L(N); vector<uint8_t> C(N, 0);
    auto blocksOf = [&](M Q){ M rot = ((Q << 1) | (Q >> (k - 1))) & FULL; return __builtin_popcount(Q & ~rot); };
    for (size_t Qs = 1; Qs < N - 1; Qs++) { M Q = (M)Qs; L[Q] = (int8_t)lam(__builtin_popcount(Q & ~ANTI) - __builtin_popcount(Q & ANTI), blocksOf(Q)); }
    vector<long long> hist(k + 1, 0); long long unc = 0; int minsz = 99; vector<M> ex;
    for (size_t Qs = 1; Qs < N - 1; Qs++) {
        M Q = (M)Qs; int sz = __builtin_popcount(Q);
        if (sz == 1) { C[Q] = 1; continue; }
        bool ok = false;
        for (M rr = Q; rr && !ok; rr &= rr - 1) {
            M bt = rr & (~rr + 1u), Qp = Q ^ bt;
            if (C[Qp] && (int)L[Qp] + (int)L[bt] + (int)L[FULL ^ Q] >= 1 && (int)L[Q] + (int)L[FULL ^ Qp] + (int)L[FULL ^ bt] >= p + 1) ok = true;
        }
        C[Q] = ok;
        if (!ok) { unc++; hist[sz]++; if (sz < minsz) { minsz = sz; ex.clear(); } if (sz == minsz && ex.size() < 12) ex.push_back(Q); }
    }
    printf("{\"p\":%d,\"k\":%d,\"B\":%d,\"kB\":%d,\"anti\":\"%s\",\"uncertified\":%lld,\"minsize\":%d,\"hist\":\"", p, k, B, kB, argv[3], unc, minsz);
    for (int z = 0; z <= k; z++) if (hist[z]) printf("%d:%lld ", z, hist[z]);
    printf("\",\"examples\":[");
    for (size_t e = 0; e < ex.size(); e++) {
        M Q = ex[e]; string bits; for (int t = 0; t < k; t++) bits += ((Q >> t) & 1u) ? (((ANTI >> t) & 1u) ? 'A' : '1') : (((ANTI >> t) & 1u) ? 'a' : '.');
        printf("%s{\"j\":%d,\"e\":%d,\"m\":%d,\"pattern\":\"%s\"}", e ? "," : "", __builtin_popcount(Q & ~ANTI), __builtin_popcount(Q & ANTI), blocksOf(Q), bits.c_str());
    }
    printf("]}\n");
    return 0;
}
