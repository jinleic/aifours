// Counterexample search by exploring the "avoider graph" (NOT a fixed-run scan):
// vertices = words of length L (default 2n-2) with NO increasing-index K-subword
// of identity product (K = n by default); edges = single-letter substitution,
// adjacent transposition, or relocation of one letter.  Words are canonicalised
// under cyclic rotation x Aut(G) x (reverse+invert), all of which preserve the
// avoidance property (rotation conjugates subword products; reverse+invert
// inverts them; automorphisms map identity to identity).
// For every avoider reached, ALL (L+1)*n single-letter insertions are tested; an
// avoiding word of length L+1 = 2n-1 would refute Olson's conjecture and is
// written to the output immediately (to be independently re-verified).
//
// Usage: avoider_walk TABLE AUTJSON_TXT L K max_vertices seed_word_file out_prefix
//   AUTJSON_TXT: text file: line1 n m (m automorphisms), then m lines of n ints,
//                then a line with n inverse indices.
//   seed_word_file: lines of space-separated letters (each must be an avoider)
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <deque>
#include <fstream>
#include <iostream>
#include <sstream>
#include <string>
#include <unordered_set>
#include <vector>
using namespace std;
typedef uint64_t u64;

static int n, L, K;
static vector<vector<int>> tab, auts;
static vector<int> inv_of;
static vector<u64> lut;
static int nch;

static inline u64 rmul(int a, u64 s) {
    u64 o = 0;
    const u64* b = &lut[(size_t)a * nch * 256];
    for (int c = 0; c < nch && s; ++c, s >>= 8) o |= b[c * 256 + (s & 255)];
    return o;
}

// true iff word has NO increasing K-subword with identity product
static bool avoids(const vector<int>& w) {
    u64 P[66];
    for (int k = 0; k < K; ++k) P[k] = 0;
    P[0] = 1ULL;  // identity is element 0
    int len = (int)w.size();
    for (int t = 0; t < len; ++t) {
        int a = w[t];
        if (K - 1 <= t && (P[K - 1] >> inv_of[a] & 1)) return false;
        int top = min(K - 1, t + 1);
        for (int k = top; k >= 1; --k) P[k] |= rmul(a, P[k - 1]);
    }
    return true;
}

static string key_of(const vector<int>& w) {
    string s(w.size(), 0);
    for (size_t i = 0; i < w.size(); ++i) s[i] = (char)w[i];
    return s;
}

static vector<int> canon(const vector<int>& w) {
    int len = (int)w.size();
    vector<int> best, cand(len), rev(len);
    for (int r = 0; r < 2; ++r) {
        vector<int> base(len);
        if (r == 0) base = w;
        else for (int i = 0; i < len; ++i) base[i] = inv_of[w[len - 1 - i]];
        for (auto& phi : auts) {
            for (int s = 0; s < len; ++s) {
                for (int i = 0; i < len; ++i) cand[i] = phi[base[(s + i) % len]];
                if (best.empty() || cand < best) best = cand;
            }
        }
    }
    return best;
}

int main(int argc, char** argv) {
    if (argc < 8) { fprintf(stderr, "usage\n"); return 2; }
    {
        ifstream f(argv[1]);
        f >> n;
        tab.assign(n, vector<int>(n));
        for (auto& r : tab) for (auto& x : r) f >> x;
    }
    {
        ifstream f(argv[2]);
        int m;
        f >> n >> m;
        auts.assign(m, vector<int>(n));
        for (auto& a : auts) for (auto& x : a) f >> x;
        inv_of.assign(n, 0);
        for (auto& x : inv_of) f >> x;
    }
    L = atoi(argv[3]); K = atoi(argv[4]);
    long long maxv = atoll(argv[5]);
    string prefix = argv[7];
    nch = (n + 7) / 8;
    lut.assign((size_t)n * nch * 256, 0);
    for (int a = 0; a < n; ++a)
        for (int c = 0; c < nch; ++c)
            for (int v = 0; v < 256; ++v) {
                u64 m = 0;
                for (int b = 0; b < 8; ++b)
                    if (v >> b & 1) { int g = c * 8 + b; if (g < n) m |= 1ULL << tab[g][a]; }
                lut[((size_t)a * nch + c) * 256 + v] = m;
            }
    // sanity: tables
    for (int a = 0; a < n; ++a)
        if (tab[a][inv_of[a]] != 0 || tab[0][a] != a || tab[a][0] != a) { fprintf(stderr, "bad table\n"); return 3; }
    for (auto& phi : auts)
        for (int a = 0; a < n; ++a)
            for (int b = 0; b < n; ++b)
                if (phi[tab[a][b]] != tab[phi[a]][phi[b]]) { fprintf(stderr, "bad automorphism\n"); return 3; }
    unordered_set<string> seen;
    deque<vector<int>> q;
    {
        ifstream f(argv[6]);
        string line;
        while (getline(f, line)) {
            istringstream ss(line);
            vector<int> w;
            int x;
            while (ss >> x) w.push_back(x);
            if ((int)w.size() != L) continue;
            if (!avoids(w)) { fprintf(stderr, "seed is not an avoider, skipped\n"); continue; }
            auto c = canon(w);
            if (seen.insert(key_of(c)).second) q.push_back(c);
        }
    }
    FILE* fv = fopen((prefix + ".avoiders.txt").c_str(), "w");
    FILE* fc = fopen((prefix + ".COUNTEREXAMPLES.txt").c_str(), "w");
    long long processed = 0, ext_tests = 0, cex = 0, checks = 0;
    auto t0 = chrono::steady_clock::now();
    vector<int> w2;
    while (!q.empty() && (long long)seen.size() <= maxv) {
        vector<int> w = q.front();
        q.pop_front();
        ++processed;
        for (int i = 0; i < L; ++i) fprintf(fv, "%s%d", i ? " " : "", w[i]);
        fputc('\n', fv);
        // extension test: all insertions
        for (int pos = 0; pos <= L; ++pos)
            for (int a = 0; a < n; ++a) {
                w2.assign(w.begin(), w.begin() + pos);
                w2.push_back(a);
                w2.insert(w2.end(), w.begin() + pos, w.end());
                ++ext_tests;
                if (avoids(w2)) {
                    ++cex;
                    for (size_t j = 0; j < w2.size(); ++j) fprintf(fc, "%s%d", j ? " " : "", w2[j]);
                    fputc('\n', fc);
                    fflush(fc);
                }
            }
        auto push = [&](vector<int>& x) {
            ++checks;
            if (!avoids(x)) return;
            auto c = canon(x);
            if (seen.insert(key_of(c)).second) q.push_back(c);
        };
        // substitutions
        for (int i = 0; i < L; ++i) {
            int old = w[i];
            for (int a = 0; a < n; ++a) {
                if (a == old) continue;
                w[i] = a;
                push(w);
            }
            w[i] = old;
        }
        // adjacent transpositions
        for (int i = 0; i + 1 < L; ++i) {
            if (w[i] == w[i + 1]) continue;
            swap(w[i], w[i + 1]);
            push(w);
            swap(w[i], w[i + 1]);
        }
        // Hurwitz/braid moves on adjacent pairs: (u,v)->(v, v^-1 u v) and (u,v)->(u v u^-1, u)
        for (int i = 0; i + 1 < L; ++i) {
            int u = w[i], v = w[i + 1];
            int vi = inv_of[v], ui = inv_of[u];
            vector<int> x = w;
            x[i] = v; x[i + 1] = tab[tab[vi][u]][v];
            push(x);
            x = w;
            x[i] = tab[tab[u][v]][ui]; x[i + 1] = u;
            push(x);
        }
        // double substitutions at adjacent positions (both letters changed)
        for (int i = 0; i + 1 < L; ++i) {
            int o1 = w[i], o2 = w[i + 1];
            for (int a = 0; a < n; ++a) {
                if (a == o1) continue;
                for (int b = 0; b < n; ++b) {
                    if (b == o2) continue;
                    w[i] = a; w[i + 1] = b;
                    push(w);
                }
            }
            w[i] = o1; w[i + 1] = o2;
        }
        // relocations: move letter i to position j
        for (int i = 0; i < L; ++i)
            for (int j = 0; j < L; ++j) {
                if (j == i || j == i + 1) continue;
                vector<int> x;
                x.reserve(L);
                for (int t = 0; t < L; ++t) {
                    if (t == j) x.push_back(w[i]);
                    if (t != i) x.push_back(w[t]);
                }
                if (j == L) x.push_back(w[i]);
                if ((int)x.size() == L) push(x);
            }
        if (processed % 200 == 0) {
            double s = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
            fprintf(stderr, "processed=%lld seen=%zu queue=%zu cex=%lld secs=%.1f\n", processed, seen.size(), q.size(), cex, s);
            fflush(fv);
        }
    }
    double s = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
    printf("{\"n\":%d,\"L\":%d,\"K\":%d,\"processed\":%lld,\"seen\":%zu,\"queue_left\":%zu,\"ext_tests\":%lld,\"counterexamples\":%lld,\"neighbor_checks\":%lld,\"secs\":%.1f,\"exhausted_component\":%s}\n",
           n, L, K, processed, seen.size(), q.size(), ext_tests, cex, checks, s, q.empty() ? "true" : "false");
    fclose(fv);
    fclose(fc);
    return 0;
}
