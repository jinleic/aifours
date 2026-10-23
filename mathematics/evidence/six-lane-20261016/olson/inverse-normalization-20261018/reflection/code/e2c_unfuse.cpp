// E2 part C: un-fusing of every RGR avoider of length 4p-2 (read-only lists, see e2c_prep.py).
// For each avoider w_end (verified to avoid by the DP below = positive control) and each block sigma_u^L:
//  C1: split into sigma_u^s | sigma_*^(L-s) with an EVEN part recoloured to v != u (one genuine empty run);
//  C2: split into sigma_u^a sigma_v^b sigma_u^c, a, c >= 1, b >= 2 even, v != u (two genuine empty runs).
// These are exactly the words whose single FUS step (proof-K0star-r1.md Sec. 2) gives w_end.  Each is decided by a raw
// ordered-product DP; any avoider among them is printed as a candidate counterexample to REFL(p).
// Output on stdout: one JSON line per candidate, then a summary line.  Usage: e2c_unfuse < input
#include <cstdio>
#include <cstdint>
#include <vector>
#include <string>
using namespace std;
static int P;
struct L { int rot; int x; };   // rot=1: rho_x, rot=0: sigma_x
static bool has_identity(const vector<L>& w) {
    int n2 = 2 * P;
    uint32_t full = (P == 32) ? 0xffffffffu : ((1u << P) - 1);
    vector<uint32_t> reach(2 * (n2 + 1), 0);   // reach[2*sz + es]
    reach[0] = 1;
    for (const L& c : w) {
        int x = ((c.x % P) + P) % P;
        for (int sz = n2 - 1; sz >= 0; --sz) {
            for (int es = 0; es < 2; ++es) {
                uint32_t m = reach[2 * sz + es];
                if (!m) continue;
                int e = es == 0 ? 1 : -1;
                int sh = ((e * x) % P + P) % P;
                uint32_t mm = sh ? (((m << sh) | (m >> (P - sh))) & full) : m;
                int nes = c.rot ? es : 1 - es;
                reach[2 * (sz + 1) + nes] |= mm;
            }
        }
    }
    return reach[2 * n2 + 0] & 1u;
}
int main() {
    long long n_in = 0, n_avoid_ok = 0, n_c1 = 0, n_c2 = 0, cand = 0;
    long long by_kappa_c1[40] = {0}, by_kappa_c2[40] = {0};
    int p, k;
    while (scanf("%d %d", &p, &k) == 2) {
        P = p;
        vector<int> a(k), b(k), l(k), y(k);
        for (auto& v : a) scanf("%d", &v);
        for (auto& v : b) scanf("%d", &v);
        for (auto& v : l) scanf("%d", &v);
        for (auto& v : y) scanf("%d", &v);
        ++n_in;
        auto build = [&](int bi, const vector<pair<int,int>>& blk) {
            // word with block bi replaced by the list blk of (value, length)
            vector<L> w;
            for (int i = 0; i < k; ++i) {
                for (int j = 0; j < a[i]; ++j) w.push_back({1, 1});
                for (int j = 0; j < b[i]; ++j) w.push_back({1, P - 1});
                if (i == bi) { for (auto& q : blk) for (int j = 0; j < q.second; ++j) w.push_back({0, q.first}); }
                else for (int j = 0; j < l[i]; ++j) w.push_back({0, y[i]});
            }
            return w;
        };
        vector<L> w0 = build(-1, {});
        if (!has_identity(w0)) ++n_avoid_ok;
        else { printf("{\"control_fail\":1,\"p\":%d,\"k\":%d}\n", p, k); continue; }
        int H = 0; for (int i = 0; i < k; ++i) H += l[i] / 2;
        for (int bi = 0; bi < k; ++bi) {
            int u = y[bi], Lb = l[bi];
            for (int s = 1; s < Lb; ++s) {
                for (int side = 0; side < 2; ++side) {
                    int evenlen = side == 0 ? s : Lb - s;
                    if (evenlen % 2) continue;
                    for (int v = 0; v < P; ++v) {
                        if (v == u) continue;
                        vector<pair<int,int>> blk;
                        if (side == 0) blk = {{v, s}, {u, Lb - s}}; else blk = {{u, s}, {v, Lb - s}};
                        int Hn = H - Lb / 2 + s / 2 + (Lb - s) / 2;
                        int kap = P - 1 - Hn;
                        ++n_c1; if (kap >= 0 && kap < 40) ++by_kappa_c1[kap];
                        if (!has_identity(build(bi, blk))) {
                            ++cand;
                            printf("{\"candidate\":\"C1\",\"p\":%d,\"k\":%d,\"block\":%d,\"s\":%d,\"side\":%d,\"v\":%d}\n", P, k, bi, s, side, v);
                        }
                    }
                }
            }
            for (int aa = 1; aa < Lb; ++aa)
                for (int bb = 2; aa + bb < Lb; bb += 2) {
                    int cc = Lb - aa - bb;
                    for (int v = 0; v < P; ++v) {
                        if (v == u) continue;
                        vector<pair<int,int>> blk = {{u, aa}, {v, bb}, {u, cc}};
                        int Hn = H - Lb / 2 + aa / 2 + bb / 2 + cc / 2;
                        int kap = P - 1 - Hn;
                        ++n_c2; if (kap >= 0 && kap < 40) ++by_kappa_c2[kap];
                        if (!has_identity(build(bi, blk))) {
                            ++cand;
                            printf("{\"candidate\":\"C2\",\"p\":%d,\"k\":%d,\"block\":%d,\"a\":%d,\"b\":%d,\"c\":%d,\"v\":%d}\n", P, k, bi, aa, bb, cc, v);
                        }
                    }
                }
        }
    }
    printf("{\"summary\":1,\"inputs\":%lld,\"originals_avoid\":%lld,\"c1_words\":%lld,\"c2_words\":%lld,\"candidates\":%lld,\"c1_by_kappa\":[", n_in, n_avoid_ok, n_c1, n_c2, cand);
    for (int i = 0; i < 12; ++i) printf("%s%lld", i ? "," : "", by_kappa_c1[i]);
    printf("],\"c2_by_kappa\":[");
    for (int i = 0; i < 12; ++i) printf("%s%lld", i ? "," : "", by_kappa_c2[i]);
    printf("]}\n");
    return 0;
}
