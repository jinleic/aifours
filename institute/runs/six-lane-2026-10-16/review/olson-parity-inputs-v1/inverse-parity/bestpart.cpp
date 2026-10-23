// bestpart.cpp -- aid for inverse-parity (README Sec. 2 B): for one RGR run datum
// (p; a, b, l) compute lambda(P) = U_P + 1 for every proper pattern P (general
// formula, README Sec. 1 / notes-checkpoint F2), the maximum of sum lambda over set
// partitions of [k] into >= 2 proper parts, and whether some ordering of that best
// partition is a valid block chain (conditions (a),(b),(c) in notes-checkpoint).
// Usage: bestpart p k a_1..a_k b_1..b_k l_1..l_k     (k <= 22)
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;
int p, k;
vector<int> lam;
int main(int argc, char** argv) {
    p = atoi(argv[1]); k = atoi(argv[2]);
    vector<int> a(k), b(k), l(k);
    for (int i = 0; i < k; ++i) a[i] = atoi(argv[3 + i]);
    for (int i = 0; i < k; ++i) b[i] = atoi(argv[3 + k + i]);
    for (int i = 0; i < k; ++i) l[i] = atoi(argv[3 + 2 * k + i]);
    int R = 0, F = 0, oF = 0;
    for (int i = 0; i < k; ++i) { R += a[i] + b[i]; F += l[i]; oF += l[i] & 1; }
    int H = (F - oF) / 2, kap = p - 1 - H;
    int full = (1 << k) - 1;
    lam.assign(1 << k, 0);
    for (int P = 1; P < full; ++P) {
        int m2 = 0, beta = 0, Ep = 0;
        for (int j = 0; j < k; ++j) {
            int zj = (P >> j) & 1, zn = (P >> ((j + 1) % k)) & 1;
            if (zj != zn) { ++m2; if (l[j] % 2 == 0) ++beta; }
            Ep += zj ? a[j] : b[j];
        }
        int m = m2 / 2;
        int U = min(p - m, min(Ep - 1 - kap + m - beta, Ep / 2));
        lam[P] = U + 1;
    }
    const int NEG = -1000000000;
    vector<int> f(1 << k, NEG), ch(1 << k, 0);
    f[0] = 0;
    for (int mask = 1; mask <= full; ++mask) {
        int low = mask & -mask, rest = mask ^ low, best = NEG, bc = 0;
        for (int sub = rest;; sub = (sub - 1) & rest) {
            int P = sub | low;
            if (P != full && f[mask ^ P] > NEG) {
                int v = f[mask ^ P] + lam[P];
                if (v > best) { best = v; bc = P; }
            }
            if (sub == 0) break;
        }
        f[mask] = best; ch[mask] = bc;
    }
    vector<int> parts;
    for (int m = full; m; m ^= ch[m]) parts.push_back(ch[m]);
    printf("{\"p\":%d,\"k\":%d,\"kappa\":%d,\"best\":%d,\"parts\":[", p, k, kap, f[full]);
    for (size_t i = 0; i < parts.size(); ++i) {
        printf("%s[", i ? "," : "");
        bool first = true;
        for (int j = 0; j < k; ++j) if ((parts[i] >> j) & 1) { printf("%s%d", first ? "" : ",", j); first = false; }
        printf("]");
    }
    printf("],\"lams\":[");
    for (size_t i = 0; i < parts.size(); ++i) printf("%s%d", i ? "," : "", lam[parts[i]]);
    // block chain check over permutations (s <= 9)
    int s = parts.size(), ok = 0;
    if (f[full] >= p + 1 && s <= 9) {
        vector<int> perm(s);
        for (int i = 0; i < s; ++i) perm[i] = i;
        sort(perm.begin(), perm.end());
        do {
            int Pl = parts[perm[s - 1]];
            if (lam[Pl] + lam[full ^ Pl] < 1) continue;
            int X = parts[perm[0]]; bool good = true;
            for (int t = 1; t < s - 1 && good; ++t) {
                int Y = parts[perm[t]], Z = full ^ (X | Y);
                if (lam[X | Y] + lam[Y | Z] + lam[X | Z] < p + 1) good = false;
                if (lam[X] + lam[Y] + lam[Z] < 1) good = false;
                X |= Y;
            }
            if (good) { ok = 1; break; }
        } while (next_permutation(perm.begin(), perm.end()));
    }
    printf("],\"block_chain\":%d}\n", ok);
    return 0;
}
