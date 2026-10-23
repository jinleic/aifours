// Obligation NB (rotation slice, 2026-10-18): bounded falsification of ROT(p) in Hamming-type neighbourhoods of
// known avoiders.  Raw ordered-product DP only (states: size c <= 2p, sign e; bitmask of values v in Z_p);
// convention (v,e)(v',e') = (v + e v', e e'); identity = (0,+1).  No window formula.
// Input (stdin): first line "p"; then one base word per line, tokens r<x> / s<y>.
// Families (base word w of length n, all base words must be avoiders; checked):
//   S1  w with position i replaced by rotation v                         (v over all of Z_p)
//   S2  w with position i deleted and rotation v inserted before position j (j = 0..n-1 of the deleted word, or end)
//   S3  w with position i replaced by rotation v and position i2 > i replaced by any letter (2p letters)
// Output: for each family, counts of (avoiders, avoiders that are non-rigid); every non-rigid avoider is printed
// as "HIT <family> <word>" (to be re-verified independently in Python).  Non-rigid := rotation value set not
// contained in one {x, -x} with x != 0.
#include <cstdio>
#include <cstdint>
#include <cstring>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
using namespace std;

static int P;
struct L { int kind; int val; };  // kind 0 = rotation, 1 = reflection

static inline uint32_t rot(uint32_t m, int s) {
    s %= P; if (s < 0) s += P;
    if (!s) return m;
    uint32_t full = (P == 32) ? 0xffffffffu : ((1u << P) - 1);
    return ((m << s) | (m >> (P - s))) & full;
}

static bool has_identity(const vector<L>& w) {
    int S = 2 * P;
    uint32_t r[2][64];
    memset(r, 0, sizeof(r));
    r[0][0] = 1;  // sign + , size 0, value 0
    int n = (int)w.size();
    for (int t = 0; t < n; t++) {
        int top = t < S - 1 ? t : S - 1;
        for (int c = top; c >= 0; c--) {
            for (int ei = 0; ei < 2; ei++) {
                uint32_t m = r[ei][c];
                if (!m) continue;
                int e = ei ? -1 : 1;
                uint32_t mv = rot(m, e * w[t].val);
                if (w[t].kind == 0) r[ei][c + 1] |= mv; else r[1 - ei][c + 1] |= mv;
            }
        }
    }
    return r[0][S] & 1u;
}

static bool nonrigid(const vector<L>& w) {
    int x = -1;
    for (auto& l : w) if (l.kind == 0) {
        int v = ((l.val % P) + P) % P;
        if (v == 0) return true;
        if (x < 0) { x = v; continue; }
        if (v != x && v != (P - x) % P) return true;
    }
    return false;
}

static string fmt(const vector<L>& w) {
    string s;
    for (size_t i = 0; i < w.size(); i++) {
        if (i) s += ' ';
        s += (w[i].kind ? 's' : 'r');
        s += to_string(w[i].val);
    }
    return s;
}

int main() {
    string line;
    getline(cin, line); P = stoi(line);
    vector<vector<L>> base;
    while (getline(cin, line)) {
        if (line.empty()) continue;
        istringstream is(line); string tok; vector<L> w;
        while (is >> tok) w.push_back({tok[0] == 's' ? 1 : 0, stoi(tok.substr(1))});
        base.push_back(w);
    }
    long long nb = 0, bad_base = 0;
    long long cnt[3] = {0, 0, 0}, av[3] = {0, 0, 0}, nr[3] = {0, 0, 0};
    for (auto& w : base) {
        nb++;
        if (has_identity(w)) { bad_base++; continue; }
        int n = (int)w.size();
        // S1
        for (int i = 0; i < n; i++) for (int v = 0; v < P; v++) {
            vector<L> u = w; u[i] = {0, v};
            cnt[0]++;
            if (!has_identity(u)) { av[0]++; if (nonrigid(u)) { nr[0]++; printf("HIT S1 %s\n", fmt(u).c_str()); } }
        }
        // S2
        for (int i = 0; i < n; i++) {
            vector<L> d = w; d.erase(d.begin() + i);
            for (int j = 0; j <= n - 1; j++) for (int v = 0; v < P; v++) {
                vector<L> u = d; u.insert(u.begin() + j, L{0, v});
                cnt[1]++;
                if (!has_identity(u)) { av[1]++; if (nonrigid(u)) { nr[1]++; printf("HIT S2 %s\n", fmt(u).c_str()); } }
            }
        }
        // S3
        for (int i = 0; i < n; i++) for (int v = 0; v < P; v++) {
            if (v == 1 || v == P - 1) continue;  // first change must create a non-rigid value (base is x = 1 normalised or not: checked below)
            vector<L> u = w; u[i] = {0, v};
            for (int i2 = 0; i2 < n; i2++) {
                if (i2 == i) continue;
                L keep = u[i2];
                for (int kind = 0; kind < 2; kind++) for (int v2 = 0; v2 < P; v2++) {
                    u[i2] = {kind, v2};
                    cnt[2]++;
                    if (!has_identity(u)) { av[2]++; if (nonrigid(u)) { nr[2]++; printf("HIT S3 %s\n", fmt(u).c_str()); } }
                }
                u[i2] = keep;
            }
        }
    }
    printf("SUMMARY p=%d base=%lld bad_base=%lld S1 %lld %lld %lld S2 %lld %lld %lld S3 %lld %lld %lld\n", P, nb, bad_base,
           cnt[0], av[0], nr[0], cnt[1], av[1], nr[1], cnt[2], av[2], nr[2]);
    return 0;
}
