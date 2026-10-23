// Stage D of PLAN-v1.md (p = 5, o_F = 4): direct ordered 10-subsequence DP over D_10 on every word of the domain D
// whose rotation multiset fails the elementary pairs filter P1'.  Written independently of GRX and of every earlier
// lane code.  Group law (v,e)(v',e') = (v + e v', e e'); index g = 5*[e = -1] + v; identity = 0.
// Usage: dp_p5o4_v1 OUTDIR    (writes OUTDIR/dp_summary.json, dp_avoiders.txt, dp_survivors.txt, dp_mutations.txt)
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cstdint>
#include <string>
#include <vector>
#include <algorithm>

static const int P = 5, K = 4, NLEN = 18, TP = 10;
static uint16_t RT[2][10][1024];   // RT[mode][g][mask] = { x*g : x in mask }, mode 1 = corrupted law (no twist)

static int mulf(int a, int b, int corrupt) {
    int va = a % 5, ea = a / 5, vb = b % 5, eb = b / 5, v;
    if (corrupt) v = (va + vb) % 5;
    else { int e = ea ? -1 : 1; v = ((va + e * vb) % 5 + 5) % 5; }
    return (ea ^ eb) * 5 + v;
}
static void build_tables() {
    for (int mode = 0; mode < 2; ++mode)
        for (int g = 0; g < 10; ++g)
            for (int m = 0; m < 1024; ++m) {
                uint16_t r = 0;
                for (int x = 0; x < 10; ++x) if (m >> x & 1) r |= (uint16_t)(1u << mulf(x, g, mode));
                RT[mode][g][m] = r;
            }
}
static bool dp_has(const std::vector<int>& w, int target, int mode) {
    uint16_t reach[TP + 1];
    memset(reach, 0, sizeof reach);
    reach[0] = 1;
    for (int g : w)
        for (int c = target - 1; c >= 0; --c)
            if (reach[c]) reach[c + 1] |= RT[mode][g][reach[c]];
    return reach[target] & 1;
}
static void build_word(const int d[K][P], const int y[K], const int l[K], std::vector<int>& w) {
    w.clear();
    for (int i = 0; i < K; ++i) {
        for (int x = 0; x < P; ++x) for (int t = 0; t < d[i][x]; ++t) w.push_back(x);
        for (int t = 0; t < l[i]; ++t) w.push_back(5 + y[i]);
    }
}
static long long binom(int n, int k) { if (k < 0 || k > n) return 0; long long r = 1; for (int i = 1; i <= k; ++i) r = r * (n - k + i) / i; return r; }
static bool p1prime(const int c[P], int H) {   // exists j <= H and a zero-sum (mod 5) sub-multiset of size 10 - 2j
    int R = 0; for (int x = 0; x < P; ++x) R += c[x];
    uint8_t ach[NLEN + 1]; memset(ach, 0, sizeof ach); ach[0] = 1;
    for (int v = 0; v < P; ++v) {
        uint8_t nw[NLEN + 1]; memset(nw, 0, sizeof nw);
        for (int m = 0; m <= R; ++m) if (ach[m])
            for (int t = 0; t <= c[v] && m + t <= R; ++t)
                for (int s = 0; s < P; ++s) if (ach[m] >> s & 1) nw[m + t] |= (uint8_t)(1u << ((s + t * v) % P));
        memcpy(ach, nw, sizeof ach);
    }
    for (int j = 0; j <= H; ++j) { int m = TP - 2 * j; if (m <= R && (ach[m] & 1)) return true; }
    return false;
}
static bool rigid(const int c[P]) {
    std::vector<int> s; for (int x = 0; x < P; ++x) if (c[x]) s.push_back(x);
    if (s.empty()) return true;
    if (c[0]) return false;
    if (s.size() == 1) return true;
    return s.size() == 2 && (s[0] + s[1]) % P == 0;
}
static void compositions(int n, int parts, std::vector<std::vector<int>>& out, std::vector<int>& cur) {
    if (parts == 1) { cur.push_back(n); out.push_back(cur); cur.pop_back(); return; }
    for (int a = n; a >= 0; --a) { cur.push_back(a); compositions(n - a, parts - 1, out, cur); cur.pop_back(); }
}
static std::string dist_str(const int d[K][P]) {
    std::string s; char b[8];
    for (int i = 0; i < K; ++i) { if (i) s += "/"; for (int x = 0; x < P; ++x) { if (x) s += ","; snprintf(b, sizeof b, "%d", d[i][x]); s += b; } }
    return s;
}
static std::string class_str(int H, const int d[K][P], const int y[K]) {
    char b[16]; std::string s = "H="; snprintf(b, sizeof b, "%d", H); s += b; s += "|dist="; s += dist_str(d); s += "|y=";
    for (int i = 0; i < K; ++i) { snprintf(b, sizeof b, "%d", y[i]); s += b; }
    return s;
}
// 64-bit FNV-1a is used only for progress identity; the file hashes are computed afterwards with shasum.
struct AvClass { int H; int d[K][P]; int y[K]; std::string key; };

int main(int argc, char** argv) {
    if (argc < 2) { fprintf(stderr, "usage: %s OUTDIR\n", argv[0]); return 2; }
    std::string od = argv[1];
    build_tables();
    std::vector<std::string> avoid_lines, surv_lines, mixed_lines, mut_lines;
    std::vector<AvClass> avc;
    std::string per_H_json;
    long long tot_nonrigid = 0, tot_mixed = 0;
    std::vector<int> w; w.reserve(NLEN);
    for (int H = 0; H <= 4; ++H) {
        int R = NLEN - (2 * H + K);
        long long nl = binom(H + 3, 3);
        std::vector<std::vector<int>> lt; std::vector<int> cur; compositions(H, K, lt, cur);
        long long words_formula = nl * binom(R + 19, 19) * 625LL, solved_words = 0, enum_words = 0;
        long long nms = 0, nsurv = 0, nav = 0, navnr = 0;
        std::vector<std::vector<int>> msets; cur.clear(); compositions(R, P, msets, cur);
        for (auto& cv : msets) {
            int c[P]; for (int x = 0; x < P; ++x) c[x] = cv[x];
            ++nms;
            long long ndist = 1; for (int x = 0; x < P; ++x) ndist *= binom(c[x] + 3, 3);
            if (p1prime(c, H)) { solved_words += ndist * 625LL * nl; continue; }
            ++nsurv;
            { char b[96]; snprintf(b, sizeof b, "H=%d|Y=%d,%d,%d,%d,%d|rigid=%d|ndist=%lld", H, c[0], c[1], c[2], c[3], c[4], (int)rigid(c), ndist); surv_lines.push_back(b); }
            std::vector<std::vector<std::vector<int>>> pv(P);
            for (int x = 0; x < P; ++x) { std::vector<int> cc; compositions(c[x], K, pv[x], cc); }
            long long cnt_d = 0;
            std::vector<size_t> idx(P, 0);
            while (true) {
                int d[K][P];
                for (int x = 0; x < P; ++x) for (int i = 0; i < K; ++i) d[i][x] = pv[x][idx[x]][i];
                ++cnt_d;
                for (int yc = 0; yc < 625; ++yc) {
                    int y[K]; int t = yc; for (int i = K - 1; i >= 0; --i) { y[i] = t % 5; t /= 5; }
                    int navoid = 0;
                    for (auto& a : lt) {
                        int l[K]; for (int i = 0; i < K; ++i) l[i] = 2 * a[i] + 1;
                        build_word(d, y, l, w);
                        if ((int)w.size() != NLEN) { fprintf(stderr, "length error\n"); return 3; }
                        if (!dp_has(w, TP, 0)) ++navoid;
                    }
                    enum_words += nl;
                    if (navoid == nl) {
                        ++nav; if (!rigid(c)) ++navnr;
                        AvClass ac; ac.H = H; memcpy(ac.d, d, sizeof d); memcpy(ac.y, y, sizeof y); ac.key = class_str(H, d, y);
                        avoid_lines.push_back(ac.key); avc.push_back(ac);
                    } else if (navoid > 0) { ++tot_mixed; mixed_lines.push_back(class_str(H, d, y)); }
                }
                int x = 0;
                while (x < P) { if (++idx[x] < pv[x].size()) break; idx[x] = 0; ++x; }
                if (x == P) break;
            }
            if (cnt_d != ndist) { fprintf(stderr, "dist count error\n"); return 4; }
        }
        if (solved_words + enum_words != words_formula) { fprintf(stderr, "coverage error H=%d\n", H); return 5; }
        tot_nonrigid += navnr;
        char b[512];
        snprintf(b, sizeof b, "%s\"%d\": {\"R\": %d, \"multisets\": %lld, \"survivor_multisets\": %lld, \"words_formula\": %lld, \"words_p1prime_solved\": %lld, \"words_enumerated\": %lld, \"avoider_classes\": %lld, \"nonrigid_avoider_classes\": %lld}",
                 H ? ", " : "", H, R, nms, nsurv, words_formula, solved_words, enum_words, nav, navnr);
        per_H_json += b;
    }
    // positive control: Claude's accepted k = 2 example rho_1^9 sigma_0^7 rho_-1 sigma_0
    std::vector<int> wk2; for (int i = 0; i < 9; ++i) wk2.push_back(1); for (int i = 0; i < 7; ++i) wk2.push_back(5); wk2.push_back(4); wk2.push_back(5);
    bool pc_k2_avoider = !dp_has(wk2, TP, 0);
    // P1' sample validation: deterministic LCG, 20000 random domain words whose multiset satisfies P1' must be solvable
    unsigned long long st = 20261018ULL; auto rnd = [&](int n) { st = st * 6364136223846793005ULL + 1442695040888963407ULL; return (int)((st >> 33) % (unsigned long long)n); };
    long long p1_tested = 0, p1_fail = 0;
    while (p1_tested < 20000) {
        int H = rnd(5), R = NLEN - (2 * H + K);
        int d[K][P]; memset(d, 0, sizeof d); int c[P] = {0, 0, 0, 0, 0};
        for (int r = 0; r < R; ++r) { int x = rnd(5), i = rnd(4); d[i][x]++; c[x]++; }
        if (!p1prime(c, H)) continue;
        int a[K] = {0, 0, 0, 0}; for (int h = 0; h < H; ++h) a[rnd(4)]++;
        int l[K], y[K]; for (int i = 0; i < K; ++i) { l[i] = 2 * a[i] + 1; y[i] = rnd(5); }
        build_word(d, y, l, w); ++p1_tested; if (!dp_has(w, TP, 0)) ++p1_fail;
    }
    // canonical order of avoider classes
    std::sort(avc.begin(), avc.end(), [](const AvClass& A, const AvClass& Bc) { return A.key < Bc.key; });
    size_t ncheck = std::min<size_t>(3000, avc.size());
    long long shift_fail = 0, tc4_solvable = 0;
    for (size_t q = 0; q < ncheck; ++q) {
        const AvClass& ac = avc[q];
        int l[K] = {2 * ac.H + 1, 1, 1, 1};
        build_word(ac.d, ac.y, l, w);
        for (int s = 0; s < NLEN; ++s) { std::vector<int> ws(w.begin() + s, w.end()); ws.insert(ws.end(), w.begin(), w.begin() + s); if (dp_has(ws, TP, 0)) ++shift_fail; }
        std::vector<int> wr; for (int t = NLEN - 1; t >= 0; --t) { int g = w[t]; wr.push_back(g < 5 ? (5 - g) % 5 : g); }
        if (dp_has(wr, TP, 0)) ++shift_fail;
        if (dp_has(w, 8, 0)) ++tc4_solvable;
        // TC5 mutations, same set and format as Stage G
        for (int i = 0; i < K; ++i) for (int x = 0; x < P; ++x) {
            if (!ac.d[i][x]) continue;
            for (int x2 = 0; x2 < P; ++x2) {
                if (x2 == x) continue;
                int d2[K][P]; memcpy(d2, ac.d, sizeof d2); d2[i][x]--; d2[i][x2]++;
                build_word(d2, ac.y, l, w);
                char b[64]; snprintf(b, sizeof b, "|rot:%d:%d>%d|%d", i, x, x2, (int)dp_has(w, TP, 0));
                mut_lines.push_back(ac.key + b);
            }
        }
        for (int i = 0; i < K; ++i) for (int y2 = 0; y2 < P; ++y2) {
            if (y2 == ac.y[i]) continue;
            int yy[K]; memcpy(yy, ac.y, sizeof yy); yy[i] = y2;
            build_word(ac.d, yy, l, w);
            char b[64]; snprintf(b, sizeof b, "|blk:%d>%d|%d", i, y2, (int)dp_has(w, TP, 0));
            mut_lines.push_back(ac.key + b);
        }
    }
    // TC3: corrupted group law (no twist) on every H = 4 survivor class with block lengths (9,1,1,1)
    long long tc3_words = 0, tc3_diff = 0;
    {
        int H = 4, R = NLEN - (2 * H + K);
        std::vector<std::vector<int>> msets; std::vector<int> cur; compositions(R, P, msets, cur);
        for (auto& cv : msets) {
            int c[P]; for (int x = 0; x < P; ++x) c[x] = cv[x];
            if (p1prime(c, H)) continue;
            std::vector<std::vector<std::vector<int>>> pv(P);
            for (int x = 0; x < P; ++x) { std::vector<int> cc; compositions(c[x], K, pv[x], cc); }
            std::vector<size_t> idx(P, 0);
            while (true) {
                int d[K][P];
                for (int x = 0; x < P; ++x) for (int i = 0; i < K; ++i) d[i][x] = pv[x][idx[x]][i];
                for (int yc = 0; yc < 625; ++yc) {
                    int y[K]; int t = yc; for (int i = K - 1; i >= 0; --i) { y[i] = t % 5; t /= 5; }
                    int l[K] = {9, 1, 1, 1};
                    build_word(d, y, l, w);
                    ++tc3_words; if (dp_has(w, TP, 0) != dp_has(w, TP, 1)) ++tc3_diff;
                }
                int x = 0;
                while (x < P) { if (++idx[x] < pv[x].size()) break; idx[x] = 0; ++x; }
                if (x == P) break;
            }
        }
    }
    auto wr = [&](const char* name, std::vector<std::string>& lines) {
        std::sort(lines.begin(), lines.end());
        std::string path = od + "/" + name;
        FILE* f = fopen(path.c_str(), "wx");
        if (!f) { fprintf(stderr, "cannot create %s\n", path.c_str()); exit(6); }
        for (auto& s : lines) fprintf(f, "%s\n", s.c_str());
        fclose(f);
    };
    wr("dp_avoiders.txt", avoid_lines); wr("dp_survivors.txt", surv_lines); wr("dp_mutations.txt", mut_lines); wr("dp_mixed.txt", mixed_lines);
    long long mut_solv = 0; for (auto& s : mut_lines) if (s.back() == '1') ++mut_solv;
    std::string path = od + "/dp_summary.json";
    FILE* f = fopen(path.c_str(), "wx");
    if (!f) { fprintf(stderr, "cannot create summary\n"); return 7; }
    fprintf(f, "{\"p\": 5, \"k\": 4, \"N\": 18, \"per_H\": {%s},\n \"total_nonrigid_avoider_classes\": %lld, \"mixed_classes\": %lld, \"avoider_classes\": %zu,\n"
               " \"controls\": {\"positive_k2_example_avoider\": %s, \"p1prime_sample_tested\": %lld, \"p1prime_sample_failures\": %lld,"
               " \"shift_reversal_checked_classes\": %zu, \"shift_reversal_failures\": %lld, \"TC4_target8_solvable\": %lld,"
               " \"TC3_words\": %lld, \"TC3_verdict_differences\": %lld, \"mutation_lines\": %zu, \"mutation_solvable\": %lld}}\n",
            per_H_json.c_str(), tot_nonrigid, tot_mixed, avc.size(), pc_k2_avoider ? "true" : "false", p1_tested, p1_fail,
            ncheck, shift_fail, tc4_solvable, tc3_words, tc3_diff, mut_lines.size(), mut_solv);
    fclose(f);
    printf("done nonrigid=%lld mixed=%lld avoiders=%zu\n", tot_nonrigid, tot_mixed, avc.size());
    return 0;
}
