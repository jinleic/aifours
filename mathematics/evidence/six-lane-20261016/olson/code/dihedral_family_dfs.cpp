// Exploratory tool (NOT a certificate generator for the conjecture):
// In D_{2p} (elements (v,eps), v in Z_p, eps=+-1, (v,e)(v',e')=(v+e v', e e')),
// enumerate ALL words of length L (first letter normalised by Aut(D_2p) only;
// no rotation normalisation because restricted families need not be
// rotation-invariant) for which NO identity K-subword exists inside a
// RESTRICTED selection family X.  Families are encoded as small automata on
// (letter type, skip/select) events:
//   GEN : unrestricted (must agree with olson_dfs on avoidance)
//   RONLY: no reflection selected
//   ADJ : reflections selected only as word-adjacent consecutive pairs
//   BRK : selected reflections form brackets of reflections consecutive in the
//         reflection order (no reflection skipped while a bracket is open);
//         rotations inside a bracket may be selected (they get sign -1)
//   BRK1: BRK, plus at most ONE "long bracket" during which reflections may be
//         skipped (so one arbitrary pair f_a<f_b may be selected)
// Output: count of normalised failing words; optionally dump them.
// Usage: dihedral_family_dfs p L K FAMILY [dumpfile] [memo_log2]
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
using namespace std;
typedef uint64_t u64;

static int p, n, L, K, NF;  // NF = number of family flag-states
static string fam;
// trans[flag][type][action] = new flag or -1 ; type 0=R 1=F ; action 0=skip 1=select
static int trans[8][2][2];
static int accept_mask = 1;
static vector<vector<int>> mul;  // mul[g][a]
static u64 nodes = 0, failing = 0;
static FILE* dump = nullptr;
static vector<int> word;
static int word_alpha = 0;  // 0 = all letters, 1 = reflections only, 2 = rotations only (env WORD_ALPHABET=F|R)

static inline int elt(int v, int e) { return v + (e < 0 ? p : 0); }

struct Memo {
    int kw;
    size_t cap, used = 0;
    vector<u64> keys;
    vector<uint8_t> occ, val;
    void init(int kwords, int lg) {
        kw = kwords; cap = (size_t)1 << lg; keys.assign(cap * kw, 0); occ.assign(cap, 0); val.assign(cap, 0); used = 0;
    }
    static inline u64 mix(u64 x) {
        x += 0x9e3779b97f4a7c15ULL; x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL;
        x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL; return x ^ (x >> 31);
    }
    u64 h(const u64* k) const { u64 z = 77; for (int i = 0; i < kw; ++i) z = mix(z ^ k[i]); return z; }
    bool get(const u64* k) const {
        size_t i = h(k) & (cap - 1);
        while (occ[i]) { if (!memcmp(&keys[i * kw], k, kw * 8)) return true; i = (i + 1) & (cap - 1); }
        return false;
    }
    void put(const u64* k) {
        if (used * 10 >= cap * 7) { fill(occ.begin(), occ.end(), 0); used = 0; }
        size_t i = h(k) & (cap - 1);
        while (occ[i]) { if (!memcmp(&keys[i * kw], k, kw * 8)) return; i = (i + 1) & (cap - 1); }
        occ[i] = 1; memcpy(&keys[i * kw], k, kw * 8); ++used;
    }
} memo;

// state: S[k*NF + f] = bitmask of reachable products with k selected letters, flag f; k = 0..K-1
// plus "done" if identity reachable at (K, accept_flag).
static int SW;  // state words = K*NF + 1 (depth)

static u64 rmul_set(u64 s, int a) {
    u64 o = 0;
    while (s) { int g = __builtin_ctzll(s); s &= s - 1; o |= 1ULL << mul[g][a]; }
    return o;
}

// returns number of failing completions (words of length L where family fails)
static u64 dfs(int depth, const vector<u64>& S) {
    ++nodes;
    if (depth == L) {
        ++failing;
        if (dump) { for (int i = 0; i < L; ++i) fprintf(dump, "%s%d", i ? " " : "", word[i]); fputc('\n', dump); }
        return 1;
    }
    vector<u64> key(SW);
    for (int i = 0; i < K * NF; ++i) key[i] = S[i];
    key[K * NF] = depth;
    if (memo.get(key.data())) return 0;  // known: no failing completion
    u64 total = 0;
    int r_after = L - depth - 1;
    for (int a = 0; a < n; ++a) {
        if (word_alpha == 1 && a < p) continue;
        if (word_alpha == 2 && a >= p) continue;
        if (depth == 0 && !(a == 0 || a == 1 || a == p)) continue;  // Aut(D_2p) orbit reps: 1, rho_1, sigma_0
        int type = a >= p ? 1 : 0;
        vector<u64> T(K * NF, 0);
        bool done = false;
        for (int k = 0; k < K; ++k)
            for (int f = 0; f < NF; ++f) {
                u64 s = S[k * NF + f];
                if (!s) continue;
                int fs = trans[f][type][0];
                if (fs >= 0) T[k * NF + fs] |= s;
                int fe = trans[f][type][1];
                if (fe >= 0) {
                    u64 m = rmul_set(s, a);
                    if (k + 1 == K) {
                        if (((accept_mask >> fe) & 1) && (m & 1ULL)) done = true;
                    } else T[(k + 1) * NF + fe] |= m;
                }
            }
        if (done) continue;  // family succeeds on every completion
        // horizon pruning: layers k with k + r_after < K are useless
        for (int k = 0; k < K; ++k)
            if (k + r_after < K)
                for (int f = 0; f < NF; ++f) T[k * NF + f] = 0;
        word.push_back(a);
        total += dfs(depth + 1, T);
        word.pop_back();
    }
    if (total == 0) memo.put(key.data());
    return total;
}

int main(int argc, char** argv) {
    if (argc < 5) { fprintf(stderr, "usage: %s p L K FAMILY [dump] [memo_log2]\n", argv[0]); return 2; }
    p = atoi(argv[1]); L = atoi(argv[2]); K = atoi(argv[3]); fam = argv[4];
    if (getenv("WORD_ALPHABET")) { string wa = getenv("WORD_ALPHABET"); word_alpha = wa == "F" ? 1 : (wa == "R" ? 2 : 0); }
    n = 2 * p;
    if (n > 64) return 2;
    mul.assign(n, vector<int>(n));
    for (int g = 0; g < n; ++g)
        for (int a = 0; a < n; ++a) {
            int v = g % p, e = g >= p ? -1 : 1, w = a % p, f = a >= p ? -1 : 1;
            int nv = ((v + e * w) % p + p) % p;
            mul[g][a] = elt(nv, e * f);
        }
    memset(trans, -1, sizeof(trans));
    if (fam == "GEN") {
        NF = 1; trans[0][0][0] = trans[0][0][1] = trans[0][1][0] = trans[0][1][1] = 0;
    } else if (fam == "RONLY") {
        NF = 1; trans[0][0][0] = trans[0][0][1] = trans[0][1][0] = 0;
    } else if (fam == "ADJ") {
        NF = 2; trans[0][0][0] = trans[0][0][1] = trans[0][1][0] = 0; trans[0][1][1] = 1; trans[1][1][1] = 0;
    } else if (fam == "BRK") {
        NF = 2; trans[0][0][0] = trans[0][0][1] = trans[0][1][0] = 0; trans[0][1][1] = 1;
        trans[1][0][0] = trans[1][0][1] = 1; trans[1][1][1] = 0;
    } else if (fam == "BRK1") {
        // flags: 0 outside (long bracket unused), 1 inside short bracket (unused),
        //        2 inside long bracket, 3 outside (long bracket used), 4 inside short (used)
        NF = 5;
        // outside, unused
        trans[0][0][0] = trans[0][0][1] = trans[0][1][0] = 0; trans[0][1][1] = 1;
        // short bracket (unused): rotations free, reflections must be selected; may convert to long
        trans[1][0][0] = trans[1][0][1] = 1; trans[1][1][1] = 0; trans[1][1][0] = 2;  // skipping an F turns it long
        // long bracket: anything, closing by selecting F
        trans[2][0][0] = trans[2][0][1] = 2; trans[2][1][0] = 2; trans[2][1][1] = 3;
        // outside, used
        trans[3][0][0] = trans[3][0][1] = trans[3][1][0] = 3; trans[3][1][1] = 4;
        trans[4][0][0] = trans[4][0][1] = 4; trans[4][1][1] = 3;
    } else if (fam == "PAIRS") {
        // selection = sequence of same-type pairs consecutive in the selection
        NF = 3;
        trans[0][0][0] = trans[0][1][0] = 0; trans[0][0][1] = 1; trans[0][1][1] = 2;
        trans[1][0][0] = trans[1][1][0] = 1; trans[1][0][1] = 0;   // open R: skip anything, close with R
        trans[2][0][0] = trans[2][1][0] = 2; trans[2][1][1] = 0;   // open F: skip anything, close with F
    } else { fprintf(stderr, "unknown family\n"); return 2; }
    if (fam == "BRK1") accept_mask = (1 << 0) | (1 << 3);
    SW = K * NF + 1;
    int lg = argc > 6 ? atoi(argv[6]) : 22;
    memo.init(SW, lg);
    if (argc > 5 && string(argv[5]) != "-") dump = fopen(argv[5], "w");
    vector<u64> S(K * NF, 0);
    S[0 * NF + 0] = 1ULL;  // empty selection: identity, flag 0
    auto t0 = chrono::steady_clock::now();
    u64 c = dfs(0, S);
    double secs = chrono::duration<double>(chrono::steady_clock::now() - t0).count();
    printf("{\"p\":%d,\"L\":%d,\"K\":%d,\"family\":\"%s\",\"failing_normalised_words\":%llu,\"nodes\":%llu,\"secs\":%.2f}\n",
           p, L, K, fam.c_str(), (unsigned long long)c, (unsigned long long)nodes, secs);
    if (dump) fclose(dump);
    return 0;
}
