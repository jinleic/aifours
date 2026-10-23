// Exhaustive exact search for ordered-Olson avoiding words.
//
// Question for a finite group G (n = |G| <= 64): is there a word w of length L
// over G such that NO increasing-index K-subword has ordered product equal to
// the identity?  (Olson's conjecture: none for K = n, L = 2n-1.)
//
// Exact invariant (prior dossier proof.md section 3, re-derived here):
//   P(t,k) = set of ordered products of k-subwords of the length-t prefix,
//   P(t+1,k) = P(t,k) U P(t,k-1)*a_{t+1}.
// A prefix is dead iff e in P(t,K).  Two prefixes of equal length with equal
// (P(t,1..K-1)) have identical sets of avoiding continuations, so memoising
// dead/count results on the exact state is sound.  Layers k < K - (L-t) can
// never reach K and are zeroed so that equal futures share a key.
//
// Symmetry (sound for existence AND used consistently for counting):
//   * cyclic rotation of a word preserves the set of K-subword products up to
//     conjugation (U V -> V U = U^-1 (U V) U), hence preserves avoidance;
//   * an automorphism applied letterwise preserves avoidance.
// Given any avoiding word, take a letter g of minimal Aut-orbit index o0, apply
// an automorphism sending g to the orbit representative min(orbit), and rotate
// so that letter is first.  Hence WLOG w[0] = rep(o0) and every letter has
// orbit index >= o0.  Counts reported are counts of such normalised words
// (not orbit counts).
//
// Usage: olson_dfs TABLE ORBITS_TXT L [K] [count|find] [memo_log2]
//   ORBITS_TXT: line1 n, line2 orbit index per element, line3 inverse per elt
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
typedef uint64_t u64;

static int n, L, K;
static vector<vector<int>> tab;
static vector<int> orbit_of, inv_of;
static vector<u64> rmul_lut;  // [a][chunk][byte] -> mask
static int nchunks;
static bool count_mode = true;
static u64 nodes = 0, memo_hits = 0, memo_clears = 0;
static vector<int> word;
static vector<int> first_found;
static bool found_any = false;

static inline u64 rmul(int a, u64 s) {
    u64 out = 0;
    const u64* base = &rmul_lut[(size_t)a * nchunks * 256];
    for (int c = 0; c < nchunks && s; ++c, s >>= 8) out |= base[c * 256 + (s & 255)];
    return out;
}

// ---- exact-key memo table (open addressing; cleared when too full) ----
struct Memo {
    int kw;  // key words = K (K-1 layers + depth)
    size_t cap, used = 0;
    vector<u64> keys;
    vector<u64> vals;
    vector<uint8_t> occ;
    void init(int kwords, int log2cap) {
        kw = kwords;
        cap = (size_t)1 << log2cap;
        keys.assign(cap * kw, 0);
        vals.assign(cap, 0);
        occ.assign(cap, 0);
        used = 0;
    }
    void clear() {
        fill(occ.begin(), occ.end(), 0);
        used = 0;
        ++memo_clears;
    }
    static inline u64 mix(u64 x) {
        x += 0x9e3779b97f4a7c15ULL;
        x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL;
        return x ^ (x >> 31);
    }
    u64 hash(const u64* k) const {
        u64 h = 0x1234567ULL;
        for (int i = 0; i < kw; ++i) h = mix(h ^ k[i]);
        return h;
    }
    bool get(const u64* k, u64& v) const {
        size_t i = hash(k) & (cap - 1);
        while (occ[i]) {
            if (memcmp(&keys[i * kw], k, kw * 8) == 0) { v = vals[i]; return true; }
            i = (i + 1) & (cap - 1);
        }
        return false;
    }
    void put(const u64* k, u64 v) {
        if (used * 10 >= cap * 7) clear();
        size_t i = hash(k) & (cap - 1);
        while (occ[i]) {
            if (memcmp(&keys[i * kw], k, kw * 8) == 0) { vals[i] = v; return; }
            i = (i + 1) & (cap - 1);
        }
        occ[i] = 1;
        memcpy(&keys[i * kw], k, kw * 8);
        vals[i] = v;
        ++used;
    }
} memo;

static int min_orbit;
static const u64 SAT = (u64)1 << 62;

static inline u64 sat_add(u64 a, u64 b) { u64 c = a + b; return c > SAT ? SAT : c; }

// P has K entries; P[0] unused (constant {e}); P[k] for 1..K-1.
static u64 dfs(int depth, const u64* P) {
    ++nodes;
    if (depth == L) {
        if (!found_any) { found_any = true; first_found = word; }
        return 1;
    }
    u64 key[64 + 1];
    memcpy(key, P, sizeof(u64) * K);
    key[0] = (u64)depth;  // slot 0 (layer 0 is constant) holds depth
    u64 v;
    if (memo.get(key, v)) { ++memo_hits; return v; }
    u64 total = 0;
    int r_after = L - (depth + 1);
    int lowk = K - r_after;  // layers k < lowk are useless after placement
    u64 Q[64 + 1];
    for (int a = 0; a < n; ++a) {
        if (orbit_of[a] < min_orbit) continue;
        if (depth == 0) {
            // first letter must be the representative of min_orbit
            continue;
        }
        if (P[K - 1] >> inv_of[a] & 1) continue;  // completes an identity K-subword
        Q[0] = 0;
        for (int k = K - 1; k >= 2; --k) Q[k] = P[k] | rmul(a, P[k - 1]);
        if (K >= 2) Q[1] = P[1] | (1ULL << a);
        for (int k = 1; k < K && k < lowk; ++k) Q[k] = 0;
        word.push_back(a);
        u64 c = dfs(depth + 1, Q);
        word.pop_back();
        total = sat_add(total, c);
        if (!count_mode && total) break;
    }
    memo.put(key, total);
    return total;
}


// dump mode: print every normalised avoiding word; memo stores only dead states
static FILE* dump_out = nullptr;
static u64 dumped = 0;
static bool dfs_dump(int depth, const u64* P) {
    ++nodes;
    if (depth == L) {
        for (int i = 0; i < L; ++i) fprintf(dump_out, "%s%d", i ? " " : "", word[i]);
        fputc('\n', dump_out);
        ++dumped;
        if (!found_any) { found_any = true; first_found = word; }
        return true;
    }
    u64 key[64 + 1];
    memcpy(key, P, sizeof(u64) * K);
    key[0] = (u64)depth;
    u64 v;
    if (memo.get(key, v)) { ++memo_hits; return false; }  // only dead states stored
    bool any = false;
    int r_after = L - (depth + 1);
    int lowk = K - r_after;
    u64 Q[64 + 1];
    for (int a = 0; a < n; ++a) {
        if (orbit_of[a] < min_orbit) continue;
        if (P[K - 1] >> inv_of[a] & 1) continue;
        Q[0] = 0;
        for (int k = K - 1; k >= 2; --k) Q[k] = P[k] | rmul(a, P[k - 1]);
        if (K >= 2) Q[1] = P[1] | (1ULL << a);
        for (int k = 1; k < K && k < lowk; ++k) Q[k] = 0;
        word.push_back(a);
        if (dfs_dump(depth + 1, Q)) any = true;
        word.pop_back();
    }
    if (!any) memo.put(key, 0);
    return any;
}
int main(int argc, char** argv) {
    if (argc < 4) {
        fprintf(stderr, "usage: %s TABLE ORBITS L [K] [count|find] [memo_log2]\n", argv[0]);
        return 2;
    }
    {
        ifstream f(argv[1]);
        f >> n;
        tab.assign(n, vector<int>(n));
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) f >> tab[i][j];
    }
    {
        ifstream f(argv[2]);
        int m;
        f >> m;
        if (m != n) { fprintf(stderr, "orbit file mismatch\n"); return 2; }
        orbit_of.assign(n, 0);
        inv_of.assign(n, 0);
        for (int i = 0; i < n; ++i) f >> orbit_of[i];
        for (int i = 0; i < n; ++i) f >> inv_of[i];
    }
    L = atoi(argv[3]);
    K = argc > 4 ? atoi(argv[4]) : n;
    string mode = argc > 5 ? string(argv[5]) : string("count");
    count_mode = mode == "count";
    bool dump_mode = mode == "dump";
    if (dump_mode) {
        dump_out = fopen(argc > 7 ? argv[7] : "avoiders.txt", "w");
        if (!dump_out) { fprintf(stderr, "cannot open dump file\n"); return 2; }
    }
    int mlog = argc > 6 ? atoi(argv[6]) : 22;
    if (n > 64 || K > 64 || K < 2) { fprintf(stderr, "unsupported sizes\n"); return 2; }
    // validate table: identity 0, latin, associativity, inverses consistent
    for (int a = 0; a < n; ++a) {
        if (tab[0][a] != a || tab[a][0] != a) { fprintf(stderr, "identity fail\n"); return 3; }
        if (tab[a][inv_of[a]] != 0 || tab[inv_of[a]][a] != 0) { fprintf(stderr, "inverse fail\n"); return 3; }
        for (int b = 0; b < n; ++b)
            for (int c = 0; c < n; ++c)
                if (tab[tab[a][b]][c] != tab[a][tab[b][c]]) { fprintf(stderr, "assoc fail\n"); return 3; }
    }
    nchunks = (n + 7) / 8;
    rmul_lut.assign((size_t)n * nchunks * 256, 0);
    for (int a = 0; a < n; ++a)
        for (int c = 0; c < nchunks; ++c)
            for (int v = 0; v < 256; ++v) {
                u64 m = 0;
                for (int b = 0; b < 8; ++b)
                    if (v >> b & 1) {
                        int g = c * 8 + b;
                        if (g < n) m |= 1ULL << tab[g][a];
                    }
                rmul_lut[((size_t)a * nchunks + c) * 256 + v] = m;
            }
    memo.init(K, mlog);
    int orbit_filter = argc > 8 ? atoi(argv[8]) : -1;
    int chunk_start = argc > 9 ? atoi(argv[9]) : 0;
    bool chunk_mode = argc > 8;
    int norb = *max_element(orbit_of.begin(), orbit_of.end()) + 1;
    auto t0 = chrono::steady_clock::now();
    u64 grand = 0;
    printf("{\"n\":%d,\"L\":%d,\"K\":%d,\"mode\":\"%s\",\"runs\":[\n", n, L, K, count_mode ? "count" : "find");
    bool firstrun = true;
    for (int o = 0; o < norb; ++o) {
        if (orbit_filter >= 0 && o != orbit_filter) continue;
        int rep = -1;
        for (int a = 0; a < n; ++a)
            if (orbit_of[a] == o) { rep = a; break; }
        min_orbit = o;
        memo.clear();
        // place first letter = rep
        u64 P[65];
        memset(P, 0, sizeof(P));
        // depth-0 state is {e} only; after placing rep:
        if (K == 1) { /* trivial */ }
        P[1] = 1ULL << rep;
        int r_after = L - 1;
        for (int k = 1; k < K && k < K - r_after; ++k) P[k] = 0;
        word.assign(1, rep);
        bool dead = (K == 1 && rep == 0);
        u64 c = 0;
        if (!dead && chunk_mode) {
            // explicit loop over the second letter with checkpoint lines on stderr;
            // identical arithmetic to dfs(1,P): sum over admissible second letters.
            int r2 = L - 2, lowk2 = K - r2;
            for (int a2 = 0; a2 < n; ++a2) {
                if (orbit_of[a2] < min_orbit) continue;
                if (a2 < chunk_start) continue;
                u64 Q[65];
                memset(Q, 0, sizeof(Q));
                u64 c2 = 0;
                bool d2 = (P[K - 1] >> inv_of[a2] & 1);
                if (!d2) {
                    for (int k = K - 1; k >= 2; --k) Q[k] = P[k] | rmul(a2, P[k - 1]);
                    Q[1] = P[1] | (1ULL << a2);
                    for (int k = 1; k < K && k < lowk2; ++k) Q[k] = 0;
                    word.push_back(a2);
                    c2 = dfs(2, Q);
                    word.pop_back();
                }
                c = sat_add(c, c2);
                double s2 = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
                fprintf(stderr, "{\"orbit\":%d,\"rep\":%d,\"second\":%d,\"count\":%llu,\"nodes\":%llu,\"secs\":%.1f}\n", o, rep, a2,
                        (unsigned long long)c2, (unsigned long long)nodes, s2);
                fflush(stderr);
                if (!count_mode && c) break;
            }
        } else if (!dead) c = dump_mode ? (u64)0 : dfs(1, P);
        if (!dead && dump_mode) { u64 before = dumped; dfs_dump(1, P); c = dumped - before; }
        grand = sat_add(grand, c);
        double secs = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
        printf("%s{\"orbit\":%d,\"rep\":%d,\"count\":%llu,\"nodes\":%llu,\"secs\":%.3f}", firstrun ? "" : ",\n", o, rep,
               (unsigned long long)c, (unsigned long long)nodes, secs);
        firstrun = false;
        fflush(stdout);
        if (!count_mode && c) break;
    }
    double secs = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
    printf("\n],\"total\":%llu,\"saturated\":%s,\"nodes\":%llu,\"memo_hits\":%llu,\"memo_clears\":%llu,\"secs\":%.3f,\"example\":[",
           (unsigned long long)grand, grand >= SAT ? "true" : "false", (unsigned long long)nodes,
           (unsigned long long)memo_hits, (unsigned long long)memo_clears, secs);
    for (size_t i = 0; i < first_found.size(); ++i) printf("%s%d", i ? "," : "", first_found[i]);
    printf("]}\n");
    if (dump_out) fclose(dump_out);
    return 0;
}
