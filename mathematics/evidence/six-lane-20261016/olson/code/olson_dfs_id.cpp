// Exhaustive search with the identity-letter reduction (sound decomposition):
// a word w over G (n = |G|, length 2n-1) containing exactly e copies of the
// identity avoids identity n-subwords  iff  the identity-free word w' obtained
// by deleting those e letters (length 2n-1-e) has NO increasing k-subword of
// identity product for every k in [n-e, n]  (an identity n-subword of w uses
// some e' <= e identity letters plus an identity (n-e')-subword of w').
// Identity letters are inert under rotation, so w' may be normalised by cyclic
// rotation and Aut(G) exactly as in olson_dfs (each k-condition is rotation-
// and automorphism-invariant).  Letters range over G \ {1}.
// Usage: olson_dfs_id TABLE ORBITS e [memo_log2] [Ltot]  (K range [n-e, n], L = Ltot-e, Ltot default 2n-1)
// Prints JSON with the count of normalised identity-free words w' satisfying
// all k-conditions (0 for every e  <=>  Olson holds for G).
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <vector>
using namespace std;
typedef uint64_t u64;
static int n, L, Kmin, Kmax;
static vector<vector<int>> tab;
static vector<int> orbit_of, inv_of;
static vector<u64> lut;
static int nch, min_orbit;
static u64 nodes = 0;
static vector<int> word, example;
static inline u64 rmul(int a, u64 s) {
    u64 o = 0;
    const u64* b = &lut[(size_t)a * nch * 256];
    for (int c = 0; c < nch && s; ++c, s >>= 8) o |= b[c * 256 + (s & 255)];
    return o;
}
struct Memo {
    int kw; size_t cap, used = 0; vector<u64> keys, vals; vector<uint8_t> occ;
    void init(int k, int lg) { kw = k; cap = (size_t)1 << lg; keys.assign(cap * kw, 0); vals.assign(cap, 0); occ.assign(cap, 0); }
    void clear() { fill(occ.begin(), occ.end(), 0); used = 0; }
    static u64 mix(u64 x) { x += 0x9e3779b97f4a7c15ULL; x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL; x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL; return x ^ (x >> 31); }
    u64 h(const u64* k) const { u64 z = 99; for (int i = 0; i < kw; ++i) z = mix(z ^ k[i]); return z; }
    bool get(const u64* k, u64& v) const { size_t i = h(k) & (cap - 1); while (occ[i]) { if (!memcmp(&keys[i * kw], k, kw * 8)) { v = vals[i]; return true; } i = (i + 1) & (cap - 1); } return false; }
    void put(const u64* k, u64 v) { if (used * 10 >= cap * 7) clear(); size_t i = h(k) & (cap - 1); while (occ[i]) { if (!memcmp(&keys[i * kw], k, kw * 8)) { vals[i] = v; return; } i = (i + 1) & (cap - 1); } occ[i] = 1; memcpy(&keys[i * kw], k, kw * 8); vals[i] = v; ++used; }
} memo;
// P[k] for k = 1..Kmax-1 (P[0] = {1} implicit); key slot 0 = depth
static u64 dfs(int depth, const u64* P) {
    ++nodes;
    if (depth == L) { if (example.empty()) example = word; return 1; }
    u64 key[66];
    memcpy(key, P, sizeof(u64) * Kmax);
    key[0] = depth;
    u64 v;
    if (memo.get(key, v)) return v;
    u64 total = 0;
    int r_after = L - depth - 1;
    u64 Q[66];
    for (int a = 1; a < n; ++a) {
        if (orbit_of[a] < min_orbit) continue;
        // dead if some k in [Kmin, Kmax] gets the identity: 1 in P[k-1]*a  <=>  a^-1 in P[k-1]
        bool dead = false;
        for (int k = max(Kmin, 1); k <= Kmax && !dead; ++k) {
            u64 prev = (k - 1 == 0) ? 1ULL : P[k - 1];
            if (prev >> inv_of[a] & 1) dead = true;
        }
        if (dead) continue;
        Q[0] = 0;
        for (int k = Kmax - 1; k >= 2; --k) Q[k] = P[k] | rmul(a, P[k - 1]);
        if (Kmax >= 2) Q[1] = P[1] | (1ULL << a);
        // horizon: layer k useful only if k + r_after >= Kmin
        for (int k = 1; k < Kmax; ++k) if (k + r_after < Kmin) Q[k] = 0;
        word.push_back(a);
        total += dfs(depth + 1, Q);
        word.pop_back();
    }
    memo.put(key, total);
    return total;
}
int main(int argc, char** argv) {
    {
        ifstream f(argv[1]); f >> n; tab.assign(n, vector<int>(n));
        for (auto& r : tab) for (auto& x : r) f >> x;
    }
    {
        ifstream f(argv[2]); int m; f >> m; orbit_of.assign(n, 0); inv_of.assign(n, 0);
        for (auto& x : orbit_of) f >> x;
        for (auto& x : inv_of) f >> x;
    }
    int e = atoi(argv[3]);
    int lg = argc > 4 ? atoi(argv[4]) : 23;
    int Ltot = argc > 5 ? atoi(argv[5]) : 2 * n - 1;
    Kmax = n; Kmin = n - e; L = Ltot - e;
    if (Kmin < 1 || L < 1) { printf("{\"skip\":true}\n"); return 0; }
    for (int a = 0; a < n; ++a) {
        if (tab[0][a] != a || tab[a][0] != a || tab[a][inv_of[a]] != 0) { fprintf(stderr, "bad table\n"); return 3; }
        for (int b = 0; b < n; ++b) for (int c = 0; c < n; ++c) if (tab[tab[a][b]][c] != tab[a][tab[b][c]]) { fprintf(stderr, "assoc\n"); return 3; }
    }
    if (orbit_of[0] != 0) { fprintf(stderr, "identity must be orbit 0\n"); return 3; }
    nch = (n + 7) / 8;
    lut.assign((size_t)n * nch * 256, 0);
    for (int a = 0; a < n; ++a) for (int c = 0; c < nch; ++c) for (int v = 0; v < 256; ++v) {
        u64 m = 0;
        for (int b = 0; b < 8; ++b) if (v >> b & 1) { int g = c * 8 + b; if (g < n) m |= 1ULL << tab[g][a]; }
        lut[((size_t)a * nch + c) * 256 + v] = m;
    }
    memo.init(Kmax, lg);
    int norb = *max_element(orbit_of.begin(), orbit_of.end()) + 1;
    auto t0 = chrono::steady_clock::now();
    u64 grand = 0;
    for (int o = 1; o < norb; ++o) {
        int rep = -1;
        for (int a = 0; a < n; ++a) if (orbit_of[a] == o) { rep = a; break; }
        min_orbit = o;
        memo.clear();
        // first letter rep: dead only if some k in [Kmin,Kmax] equals 1 with rep alone (k=1, rep=identity: impossible)
        u64 P[66]; memset(P, 0, sizeof(P));
        if (Kmin <= 1 && rep == 0) continue;
        P[1] = 1ULL << rep;
        for (int k = 1; k < Kmax; ++k) if (k + (L - 1) < Kmin) P[k] = 0;
        word.assign(1, rep);
        u64 c = (L == 1) ? 1 : dfs(1, P);
        grand += c;
        double s = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
        fprintf(stderr, "{\"e\":%d,\"orbit\":%d,\"rep\":%d,\"count\":%llu,\"nodes\":%llu,\"secs\":%.1f}\n", e, o, rep, (unsigned long long)c, (unsigned long long)nodes, s);
    }
    double s = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
    printf("{\"n\":%d,\"e\":%d,\"L\":%d,\"Kmin\":%d,\"Kmax\":%d,\"count\":%llu,\"nodes\":%llu,\"secs\":%.2f,\"example\":[", n, e, L, Kmin, Kmax,
           (unsigned long long)grand, (unsigned long long)nodes, s);
    for (size_t i = 0; i < example.size(); ++i) printf("%s%d", i ? "," : "", example[i]);
    printf("]}\n");
    return 0;
}
