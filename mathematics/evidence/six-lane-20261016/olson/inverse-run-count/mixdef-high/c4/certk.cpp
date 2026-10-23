// certk.cpp -- c4 (T2, aid only [F]): exact singleton-extension certification (Lemma L, c3/proof-NOLP-r2.md (1.1))
// for W(p, kB) (anti run 0, aligned 1..n, k = n + 1 = p + 1 + kB <= 30) restricted to patterns with |Q| <= S.
// Certification of Q only uses Q - {t}, so the DP over sizes <= S is exact for those sizes.  Also checks a given
// chain (the pin chain of c4/proof-KB0.md: P = {0,2,4}; P^c built as {1},{1,3},{1,3,5},{1,3,5,6},...) step by step.
// Output: per size: patterns, certified, uncertified types (e = [0 in Q], m) with counts; pin-chain verdict.
// Usage: certk p kB S
#include <cstdio>
#include <cstdlib>
#include <cstdint>
#include <vector>
#include <map>
typedef uint32_t M;
static int p, kB, K, S;
static M FULL;
static inline int fl2(int x) { return x >= 0 ? x / 2 : -((-x + 1) / 2); }
static int nblk(M Q) { M rot = ((Q << 1) | (Q >> (K - 1))) & FULL; return __builtin_popcount(Q & ~rot); }
static int lamQ(M Q) {   // proper Q
    int m = nblk(Q), D = __builtin_popcount(Q & ~1u) - (int)(Q & 1u);
    int a = p - m + 1, b = D + m - kB, c = fl2(D + 1) + 1; int v = a < b ? a : b; return v < c ? v : c;
}
static bool stepok(M Qp, M t) {   // Q = Qp | t
    M Q = Qp | t;
    return lamQ(Qp) + lamQ(t) + lamQ(FULL ^ Q) >= 1 && lamQ(Q) + lamQ(FULL ^ Qp) + lamQ(FULL ^ t) >= p + 1;
}
int main(int argc, char** argv) {
    if (argc < 4) return 1;
    p = atoi(argv[1]); kB = atoi(argv[2]); S = atoi(argv[3]);
    K = p + 1 + kB; if (K > 30) { fprintf(stderr, "k > 30\n"); return 1; }
    FULL = (K == 32) ? ~0u : ((1u << K) - 1);
    std::vector<uint8_t> C((size_t)1 << K, 0);   // byte per pattern (k <= 30: 1 GiB at k = 30; k = 28: 256 MiB)
    printf("{\"p\":%d,\"kB\":%d,\"k\":%d,\"S\":%d,\"by_size\":[", p, kB, K, S);
    for (int t = 0; t < K; t++) C[1u << t] = 1;
    for (int s = 2; s <= S && s < K; s++) {
        long long tot = 0, cer = 0;
        std::map<std::pair<int, int>, long long> unc;
        M Q = (1u << s) - 1;
        while (Q <= FULL && Q != 0) {
            tot++;
            bool ok = false;
            for (M r = Q; r && !ok; r &= r - 1) { M bt = r & (~r + 1u), Qp = Q ^ bt; if (C[Qp] && stepok(Qp, bt)) ok = true; }
            if (ok) { C[Q] = 1; cer++; } else unc[{(int)(Q & 1u), nblk(Q)}]++;
            M c = Q & (~Q + 1u), rr = Q + c; if (rr == 0 || rr > FULL) break; Q = (((rr ^ Q) >> 2) / c) | rr;
        }
        printf("%s{\"s\":%d,\"patterns\":%lld,\"certified\":%lld,\"uncertified_types_e_m\":[", s > 2 ? "," : "", s, tot, cer);
        int f = 0; for (auto& kv : unc) { printf("%s[%d,%d,%lld]", f ? "," : "", kv.first.first, kv.first.second, kv.second); f = 1; }
        printf("]}");
        fflush(stdout);
    }
    printf("]");
    // pin chain (needs certification of P^c through sizes up to k - 3, done step by step along the chain)
    int n = K - 1;
    M P = 1u | (1u << 2) | (1u << 4);
    bool Pc = (C[P] != 0);                 // anti triple, size 3 (requires S >= 3)
    M Q = 1u << 1; bool chain = true; int minA = 1 << 30, minB = 1 << 30;
    std::vector<int> order; order.push_back(3); order.push_back(5); for (int t = 6; t <= n; t++) order.push_back(t);
    for (int t : order) {
        M bt = 1u << t, Qn = Q | bt;
        int A = lamQ(Q) + lamQ(bt) + lamQ(FULL ^ Qn) - 1, B = lamQ(Qn) + lamQ(FULL ^ Q) + lamQ(FULL ^ bt) - (p + 1);
        if (A < minA) minA = A; if (B < minB) minB = B;
        if (A < 0 || B < 0) chain = false;
        Q = Qn;
    }
    bool isPc = (Q == (FULL ^ P));
    printf(",\"pin\":{\"P_certified\":%s,\"Pc_chain_ok\":%s,\"chain_ends_at_Pc\":%s,\"min_A_slack\":%d,\"min_B_slack\":%d,\"lam_P\":%d,\"lam_Pc\":%d}}\n",
           Pc ? "true" : "false", chain ? "true" : "false", isPc ? "true" : "false", minA, minB, lamQ(P), lamQ(FULL ^ P));
    return 0;
}
