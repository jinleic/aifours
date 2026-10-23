// Exhaustive test (over all words, via exact-state DFS with memo) of the
// Bollobas-Leader-type growth statement for ordered K-subword products in a
// finite group G (n = |G|, table input):
//   GC(N):  for every word w of length N >= K, either 1 in P_K(w) or
//           |P_K(w)| >= min(n, N - K + 1).
// With K = n and N = 2n-1 this is exactly the ordered Olson statement.
// Also tests the STEP form: for every w and letter a with 1 not in P_K(wa):
//           |P_K(wa)| >= min(n, |P_K(w)| + 1)   (whenever |w| >= K-1).
// The DFS visits every reachable exact state (P_1..P_K) once per depth; states
// with 1 in P_K are dead for both tests (P_K only grows) and are pruned.
// Normalisation: first letter = Aut-orbit representative (orbit file), which is
// sound because both statements are invariant under automorphisms.
// Usage: growth_dfs TABLE ORBITS Lmax K memo_log2
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <unordered_set>
#include <vector>
using namespace std;
typedef uint64_t u64;
static int n, L, K;
static vector<vector<int>> tab;
static vector<int> orbit_of, inv_of;
static vector<u64> lut;
static int nch;
static u64 nodes = 0, viol_bound = 0, viol_step = 0, checked = 0, viol_ham = 0;
static vector<int> word;
static u64 cond_viol[70];
static vector<int> cond_ex[70];
static inline u64 rmul(int a, u64 s) {
    u64 o = 0;
    const u64* b = &lut[(size_t)a * nch * 256];
    for (int c = 0; c < nch && s; ++c, s >>= 8) o |= b[c * 256 + (s & 255)];
    return o;
}
struct Key { vector<u64> v; bool operator==(const Key& o) const { return v == o.v; } };
struct KH { size_t operator()(const Key& k) const { u64 h = 1469598103934665603ULL; for (u64 x : k.v) { h ^= x; h *= 1099511628211ULL; h ^= h >> 29; } return h; } };
static unordered_set<Key, KH> seen;
static size_t memo_cap;

static void report(const char* what, int depth, u64 before, u64 after) {
    if (viol_bound + viol_step <= 20) {
        printf("VIOLATION %s depth=%d |P_K|before=%d after=%d word=", what, depth, __builtin_popcountll(before), __builtin_popcountll(after));
        for (size_t i = 0; i < word.size(); ++i) printf("%s%d", i ? " " : "", word[i]);
        printf("\n");
    }
}

static void dfs(int depth, const vector<u64>& P) {
    ++nodes;
    // P[0..K], P[K] = products of K-subwords; identity bit 0 not in P[K]
    // ordered-Hamidoune test for every k in [1, min(depth, K)]:
    //   |P_k| >= min(n, depth-k+1)  OR  exists letter x in P_1 with x^k in P_k
    for (int k = 1; k <= K && k <= depth; ++k) {
        int sz = __builtin_popcountll(P[k]);
        int bound = min(n, depth - k + 1);
        if (sz >= bound) continue;
        bool esc = false;
        u64 sup = P[1];
        while (sup && !esc) {
            int x = __builtin_ctzll(sup); sup &= sup - 1;
            int y = 0;
            for (int t = 0; t < k; ++t) y = tab[y][x];
            if (P[k] >> y & 1) esc = true;
        }
        if (!esc) { ++viol_ham; if (viol_ham <= 10) { printf("HAMIDOUNE-VIOL k=%d depth=%d |P_k|=%d word=", k, depth, sz); for (size_t i = 0; i < word.size(); ++i) printf("%s%d", i ? " " : "", word[i]); printf("\n"); } }
    }
    if (!(P[K] & 1ULL)) {
        for (int k = 1; k <= K && k <= depth; ++k) {
            int sz = __builtin_popcountll(P[k]);
            if (sz < min(n, depth - k + 1)) { cond_viol[k]++; if (cond_ex[k].empty()) cond_ex[k] = word; }
        }
    }
    if (depth >= K) {
        ++checked;
        int sz = __builtin_popcountll(P[K]);
        int bound = min(n, depth - K + 1);
        if (sz < bound && !(P[K] & 1ULL)) { ++viol_bound; report("BOUND", depth, P[K], P[K]); }
    }
    if (depth == L) return;
    Key key{P};
    key.v.push_back((u64)depth);
    if (seen.size() < memo_cap) {
        if (!seen.insert(key).second) return;
    } else if (seen.count(key)) return;
    vector<u64> Q(K + 1);
    for (int a = 0; a < n; ++a) {
        if (depth == 0) {
            bool rep = true;
            for (int b = 0; b < a; ++b) if (orbit_of[b] == orbit_of[a]) rep = false;
            if (!rep) continue;
        }
        Q[0] = 1ULL;
        for (int k = K; k >= 1; --k) Q[k] = P[k] | rmul(a, P[k - 1]);
        if ((Q[K] & 1ULL) && !getenv("NOPRUNE")) continue;  // identity reached: dead for both tests (unless NOPRUNE)
        if (depth + 1 >= K) {
            int b = __builtin_popcountll(P[K]), c = __builtin_popcountll(Q[K]);
            if (depth >= K - 1 && c < min(n, b + 1) && b < n) { ++viol_step; word.push_back(a); report("STEP", depth + 1, P[K], Q[K]); word.pop_back(); }
        }
        word.push_back(a);
        dfs(depth + 1, Q);
        word.pop_back();
    }
}

int main(int argc, char** argv) {
    {
        ifstream f(argv[1]);
        f >> n;
        tab.assign(n, vector<int>(n));
        for (auto& r : tab) for (auto& x : r) f >> x;
    }
    {
        ifstream f(argv[2]);
        int m;
        f >> m;
        orbit_of.assign(n, 0);
        inv_of.assign(n, 0);
        for (auto& x : orbit_of) f >> x;
        for (auto& x : inv_of) f >> x;
    }
    L = atoi(argv[3]); K = atoi(argv[4]);
    memo_cap = (size_t)1 << atoi(argv[5]);
    nch = (n + 7) / 8;
    lut.assign((size_t)n * nch * 256, 0);
    for (int a = 0; a < n; ++a)
        for (int c = 0; c < nch; ++c)
            for (int v = 0; v < 256; ++v) {
                u64 m = 0;
                for (int b = 0; b < 8; ++b) if (v >> b & 1) { int g = c * 8 + b; if (g < n) m |= 1ULL << tab[g][a]; }
                lut[((size_t)a * nch + c) * 256 + v] = m;
            }
    vector<u64> P(K + 1, 0);
    P[0] = 1ULL;
    auto t0 = chrono::steady_clock::now();
    dfs(0, P);
    double s = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
    printf("{\"n\":%d,\"Lmax\":%d,\"K\":%d,\"nodes\":%llu,\"checked_states\":%llu,\"bound_violations\":%llu,\"step_violations\":%llu,\"hamidoune_violations\":%llu,\"memo\":%zu,\"secs\":%.2f}\n",
           n, L, K, (unsigned long long)nodes, (unsigned long long)checked, (unsigned long long)viol_bound,
           (unsigned long long)viol_step, (unsigned long long)viol_ham, seen.size(), s);
    for (int k = 1; k <= K; ++k) {
        printf("cond k=%d violations=%llu", k, (unsigned long long)cond_viol[k]);
        if (!cond_ex[k].empty()) { printf(" ex="); for (size_t i = 0; i < cond_ex[k].size(); ++i) printf("%s%d", i ? " " : "", cond_ex[k][i]); }
        printf("\n");
    }
    return 0;
}
