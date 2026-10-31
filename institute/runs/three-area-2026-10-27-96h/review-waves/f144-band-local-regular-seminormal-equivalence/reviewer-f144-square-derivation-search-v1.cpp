// reviewer-f144-square-derivation-search-v1.cpp  (reviewer-authored; f144 same-harness review)
//
// Bounded bidirectional breadth-first search for a derivation of  u = v  in the free band that uses ONLY the
// band axiom in its two literal forms  WW -> W  (delete a consecutive square) and  W -> WW  (duplicate a factor,
// factor length <= Kmax, word length <= Lmax).  If such a chain is found, the two content-absorption steps (C)
// of the author's chain II-right no longer depend on the Green-Rees / Siekmann-Szabo import for those exact
// words.  Failure to find a chain within the bounds proves nothing (bounded search).
// Words are over {a,b,c,d}, encoded in 64 bits (length in the top 8 bits, 2 bits per letter, length <= 28).
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <unordered_map>
#include <chrono>
typedef unsigned long long u64;
static inline u64 enc(const std::string& s) { u64 c = (u64)s.size() << 56; for (size_t i = 0; i < s.size(); i++) c |= (u64)(s[i] - 'a') << (2 * i); return c; }
static inline std::string dec(u64 c) { int L = (int)(c >> 56); std::string s(L, 'a'); for (int i = 0; i < L; i++) s[i] = (char)('a' + ((c >> (2 * i)) & 3)); return s; }
static int Lmax = 20, Kmax = 6;
static void neighbors(const std::string& u, std::vector<u64>& out) {
    int n = (int)u.size(); out.clear();
    for (int k = 1; 2 * k <= n; k++) for (int i = 0; i + 2 * k <= n; i++)
        if (u.compare(i, k, u, i + k, k) == 0) out.push_back(enc(u.substr(0, i + k) + u.substr(i + 2 * k)));
    for (int k = 1; k <= Kmax && n + k <= Lmax; k++) for (int i = 0; i + k <= n; i++)
        out.push_back(enc(u.substr(0, i + k) + u.substr(i, k) + u.substr(i + k)));
}
static bool isSquareStep(const std::string& u, const std::string& v, std::string& how) {
    // u -> v by deleting a square or inserting one
    const std::string *a = &u, *b = &v; bool del = true;
    if (u.size() < v.size()) { a = &v; b = &u; del = false; }
    int n = (int)a->size(), k = n - (int)b->size();
    if (k <= 0 || 2 * k > n) return false;
    for (int i = 0; i + 2 * k <= n; i++)
        if (a->compare(i, k, *a, i + k, k) == 0 && a->substr(0, i + k) + a->substr(i + 2 * k) == *b) {
            how = (del ? "delete square W=" : "insert square W=") + a->substr(i, k) + " at " + std::to_string(i);
            return true;
        }
    return false;
}
static bool search(const std::string& S, const std::string& Tt, long long cap, std::vector<std::string>& path) {
    std::unordered_map<u64, u64> pS, pT;      // node -> parent (self for roots)
    pS.reserve(1 << 22); pT.reserve(1 << 22);
    u64 s = enc(S), t = enc(Tt);
    pS[s] = s; pT[t] = t;
    std::vector<u64> fS{ s }, fT{ t };
    if (s == t) { path = { S }; return true; }
    std::vector<u64> nb;
    long long total = 2; int depthS = 0, depthT = 0;
    u64 meet = 0; bool found = false;
    while (!found && !fS.empty() && !fT.empty()) {
        bool expandS = fS.size() <= fT.size();
        std::vector<u64>& fr = expandS ? fS : fT;
        std::unordered_map<u64, u64>& mine = expandS ? pS : pT;
        std::unordered_map<u64, u64>& other = expandS ? pT : pS;
        std::vector<u64> nxt;
        for (u64 cur : fr) {
            neighbors(dec(cur), nb);
            for (u64 w : nb) {
                if (mine.find(w) != mine.end()) continue;
                mine[w] = cur; nxt.push_back(w); total++;
                if (other.find(w) != other.end()) { meet = w; found = true; break; }
            }
            if (found) break;
        }
        if (expandS) depthS++; else depthT++;
        fr.swap(nxt);
        std::printf("  frontier S=%zu T=%zu depthS=%d depthT=%d visited=%lld\n", fS.size(), fT.size(), depthS, depthT, total);
        std::fflush(stdout);
        if (total > cap) { std::printf("  cap %lld reached; stop\n", cap); return false; }
    }
    if (!found) return false;
    std::vector<std::string> left, right;
    for (u64 x = meet;; x = pS[x]) { left.push_back(dec(x)); if (pS[x] == x) break; }
    for (u64 x = meet;; x = pT[x]) { right.push_back(dec(x)); if (pT[x] == x) break; }
    path.clear();
    for (size_t i = left.size(); i-- > 0;) path.push_back(left[i]);
    for (size_t i = 1; i < right.size(); i++) path.push_back(right[i]);
    return true;
}
int main(int argc, char** argv) {
    if (argc < 3) { std::fprintf(stderr, "usage: %s U V [Lmax Kmax cap]\n", argv[0]); return 2; }
    std::string U = argv[1], V = argv[2];
    if (argc > 3) Lmax = std::atoi(argv[3]);
    if (argc > 4) Kmax = std::atoi(argv[4]);
    long long cap = argc > 5 ? std::atoll(argv[5]) : 30000000LL;
    if (Lmax > 28) Lmax = 28;
    for (char ch : U + V) if (ch < 'a' || ch > 'd') { std::fprintf(stderr, "alphabet a-d only\n"); return 2; }
    std::printf("search %s = %s  Lmax=%d Kmax=%d cap=%lld\n", U.c_str(), V.c_str(), Lmax, Kmax, cap);
    auto t0 = std::chrono::steady_clock::now();
    std::vector<std::string> path;
    bool ok = search(U, V, cap, path);
    double secs = std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
    if (!ok) { std::printf("NOT FOUND within bounds (%.1fs)\n", secs); return 3; }
    std::printf("FOUND square-only chain of %zu steps (%.1fs):\n", path.size() - 1, secs);
    bool allok = true;
    for (size_t i = 0; i < path.size(); i++) {
        std::string how;
        if (i == 0) std::printf("  %s\n", path[i].c_str());
        else { bool st = isSquareStep(path[i - 1], path[i], how); allok &= st; std::printf("  -> %s   [%s]\n", path[i].c_str(), st ? how.c_str() : "INVALID"); }
    }
    std::printf("%s every step re-verified as a literal square deletion/insertion\n", allok ? "PASS" : "FAIL");
    return allok ? 0 : 1;
}
