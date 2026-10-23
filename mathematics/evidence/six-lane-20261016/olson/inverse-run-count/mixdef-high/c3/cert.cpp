// cert.cpp -- c3 (task OlsonRunCount3): singleton-extension certification census for an all-odd word.
// lambda(Q) = min(p - m + 1, D_Q + m - kB, floor((D_Q + B)/2) + 1)  (Lemma H, beta = 0).
// Q certified: |Q| = 1, or Q = Q' u {t} with Q' certified and
//   (A) lambda(Q') + lambda({t}) + lambda(Q^c) >= 1,  (B) lambda(Q) + lambda(Q'^c) + lambda({t}^c) >= p + 1
// (c2/proof-NOLP.md (1.1)).  Exact DP over ALL 2^k patterns (k <= 27).  Aid only.
// Usage: cert W p kB            (W(p,kB): k = p+1+kB single letters, anti run at 0, B = 1)
//        cert D p kB B d_0 ... d_{k-1}
// Output (JSON lines): per size s: patterns, certified; smallest uncertified size; pin witness
// (Q0 certified, Q0^c certified, lambda(Q0) + lambda(Q0^c) >= 1); all-certified flag.
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cstdint>
#include <vector>
static int p, kB, B, K;
static int d[64];
static uint32_t FULL;
static std::vector<int8_t> L;
static std::vector<uint8_t> C;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static int lamc(uint32_t Q) {
    uint32_t rot = ((Q << 1) | (Q >> (K - 1))) & FULL;
    int m = __builtin_popcount(Q & ~rot), D = 0;
    for (int t = 0; t < K; t++) if ((Q >> t) & 1u) D += d[t];
    int a = p - m + 1, b = D + m - kB, c = fl2(D + B) + 1;
    int v = a < b ? a : b; return v < c ? v : c;
}
int main(int argc, char** argv) {
    if (argc < 4) { fprintf(stderr, "usage\n"); return 1; }
    p = atoi(argv[2]); kB = atoi(argv[3]);
    if (!strcmp(argv[1], "W")) { K = p + 1 + kB; B = 1; d[0] = -1; for (int t = 1; t < K; t++) d[t] = 1; }
    else { B = atoi(argv[4]); K = argc - 5; for (int t = 0; t < K; t++) d[t] = atoi(argv[5 + t]); }
    if (K > 27 || K < 3) { fprintf(stderr, "k out of range\n"); return 1; }
    FULL = (1u << K) - 1;
    size_t N = (size_t)1 << K;
    L.assign(N, 0); C.assign(N, 0);
    for (size_t Q = 1; Q < N - 1; Q++) L[Q] = (int8_t)lamc((uint32_t)Q);
    std::vector<long long> tot(K + 1, 0), cer(K + 1, 0);
    for (size_t Q = 1; Q < N - 1; Q++) {
        int s = __builtin_popcount((uint32_t)Q);
        tot[s]++;
        if (s == 1) { C[Q] = 1; cer[s]++; continue; }
        uint32_t q = (uint32_t)Q;
        for (uint32_t r = q; r; r &= r - 1) {
            uint32_t bt = r & (~r + 1u), Qp = q ^ bt;
            if (!C[Qp]) continue;
            if (L[Qp] + L[bt] + L[FULL ^ q] >= 1 && L[q] + L[FULL ^ Qp] + L[FULL ^ bt] >= p + 1) { C[Q] = 1; break; }
        }
        if (C[Q]) cer[s]++;
    }
    int smallest = -1; long long allc = 1;
    for (int s = 1; s < K; s++) { if (cer[s] != tot[s]) { if (smallest < 0) smallest = s; allc = 0; } }
    printf("{\"p\":%d,\"kB\":%d,\"B\":%d,\"k\":%d,\"d\":[", p, kB, B, K);
    for (int t = 0; t < K; t++) printf("%s%d", t ? "," : "", d[t]);
    printf("],\"all_certified\":%s,\"smallest_uncertified_size\":%d,\"by_size\":[", allc ? "true" : "false", smallest);
    for (int s = 1; s < K; s++) printf("%s[%d,%lld,%lld]", s > 1 ? "," : "", s, tot[s], cer[s]);
    printf("]");
    long long pins = 0; uint32_t w = 0;
    for (size_t Q = 1; Q < N - 1; Q++) if (C[Q] && C[FULL ^ Q] && L[Q] + L[FULL ^ Q] >= 1) { if (!pins) w = (uint32_t)Q; pins++; }
    printf(",\"pin_patterns\":%lld,\"pin_witness\":%u", pins, w);
    // a few uncertified patterns of the smallest size
    printf(",\"uncert_examples\":[");
    int shown = 0;
    if (smallest > 0) for (size_t Q = 1; Q < N - 1 && shown < 6; Q++) if (!C[Q] && __builtin_popcount((uint32_t)Q) == smallest) { printf("%s%u", shown ? "," : "", (uint32_t)Q); shown++; }
    printf("]}\n");
    return 0;
}
