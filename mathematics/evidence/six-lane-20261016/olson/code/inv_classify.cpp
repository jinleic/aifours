// inv_classify.cpp (derived from was_search.cpp) -- INV parity certificates at N=4p-2 with inherited
// monotone Res conditions (E, P, Davenport-alpha, pairs, D0; NOT T0); classes zero/full/joint/none
// for Phi <= 2*fam patterns.  Original header follows.
// was_search.cpp -- window-avoidance system (WAS) search for RGR words (repr-WAS.md).
//
// RGR word, x = 1: cyclic runs R_1 S_1 ... R_k S_k; R_i = a_i x rho_1, b_i x rho_{-1};
// S_i = sigma_{y_i}^{l_i}.  theta_i = y_{i-1} - y_i (sum 0).  For P subset [k]
// (z_i = +1 iff i in P) the window Ach(z_P) (proof-GR.md Sec. 2) gives the
// forbidden residue set W(P) = Ach mod p.  Lemma WAS: the word has NO identity
// 2p-subword iff sum_{i in P} theta_i notin W(P) for every P.
//
// Usage: was_search p N kmin kmax mode [mut] [filters]
//   mode: search (first theta per run datum) | count (all theta)
//   mut : 0 none | 1 drop the top residue of every non-full nonempty window
//   filters: 1 = apply proved value-independent filters (E,P,DavAlpha,T0,D0,pairs)
//            0 = none (every run datum; GR is exact so filters only prune)
// Output: JSON lines "sol" per run datum with a WAS solution; final "summary".
#include <algorithm>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>

static int p, N, K, mode_count = 0, mode_all = 0, mut = 0, use_filters = 1, fam = 0;
static long long cls_zero[41], cls_full[41], cls_joint[41], cls_none[41];
static int r[40], l[40], a[40], b[40];
static std::vector<uint32_t> mask;
static std::vector<uint8_t> sums;
static int theta[40], best_theta[40];
static long long nsol_theta;
struct Ctr { long long rl = 0, rl_pass = 0, split = 0, fullwin = 0, zero_ok = 0, was_solvable = 0, theta_solutions = 0, dfs_nodes = 0; };
static Ctr C[41];

static bool rot_min_rl() {
    for (int s = 1; s < K; ++s) {
        for (int i = 0; i < K; ++i) {
            int j = (i + s) % K;
            if (r[j] != r[i]) { if (r[j] < r[i]) return false; goto nx; }
            if (l[j] != l[i]) { if (l[j] < l[i]) return false; goto nx; }
        }
    nx:;
    }
    return true;
}
static bool rot_min_full() {
    for (int s = 1; s < K; ++s) {
        for (int i = 0; i < K; ++i) {
            int j = (i + s) % K;
            if (r[j] != r[i]) { if (r[j] < r[i]) return false; goto nx; }
            if (l[j] != l[i]) { if (l[j] < l[i]) return false; goto nx; }
            if (a[j] != a[i]) { if (a[j] < a[i]) return false; goto nx; }
        }
    nx:;
    }
    return true;
}

// returns 1 if some window is full (solvable for all theta), else fills mask
static int build_masks(int F, int R) {
    int np = 1 << K;
    mask.assign(np, 0);
    uint32_t all = (p >= 32) ? 0xffffffffu : ((1u << p) - 1);
    for (int P = 0; P < np; ++P) {
        int Phi = 0, delta = 0, Ep = 0;
        for (int i = 0; i < K; ++i) {
            int zi = (P >> i) & 1, zn = (P >> ((i + 1) % K)) & 1, f = zi ^ zn;
            Phi += f;
            if ((l[i] - f) & 1) ++delta;
            Ep += zi ? a[i] : b[i];
        }
        if (fam > 0 && Phi > 2 * fam) continue;  // pattern outside family: ignored
        if (fam == -1) { int pc = __builtin_popcount((unsigned)P); if (!(pc <= 1 || pc >= K - 1)) continue; }  // elementary brackets only
        int Em = R - Ep, Cmax = F - delta, s0 = 2 * p - Cmax, s1 = 2 * p - Phi;
        int lo = std::max(-s1, std::max(s0 - 2 * Em, -Em));
        int hi = std::min(s1, std::min(2 * Ep - s0, Ep));
        if (lo & 1) ++lo;
        if (hi & 1) --hi;
        if (lo > hi) continue;
        int n = (hi - lo) / 2 + 1;
        if (n >= p) return 1;
        if (mut == 1) { hi -= 2; if (lo > hi) continue; }
        uint32_t m = 0;
        for (int t = lo; t <= hi; t += 2) m |= 1u << (((t % p) + p) % p);
        mask[P] = m & all;
    }
    return 0;
}

static bool dfs(int j, int partial) {
    C[K].dfs_nodes++;
    int lim = (j == K - 1) ? 1 : p;
    for (int tt = 0; tt < lim; ++tt) {
        int th = (j == K - 1) ? ((p - partial % p) % p) : tt;
        int top = 1 << j;
        bool ok = true;
        for (int S = 0; S < top; ++S) {
            int s = sums[S] + th; if (s >= p) s -= p;
            if ((mask[S | top] >> s) & 1) { ok = false; break; }
            sums[S | top] = (uint8_t)s;
        }
        if (!ok) continue;
        theta[j] = th;
        if (j == K - 1) {
            if (nsol_theta == 0) memcpy(best_theta, theta, sizeof(int) * K);
            ++nsol_theta;
            if (mode_all) {
                printf("{\"all\":1,\"k\":%d,\"a\":[", K);
                for (int i = 0; i < K; ++i) printf("%s%d", i ? "," : "", a[i]);
                printf("],\"b\":[");
                for (int i = 0; i < K; ++i) printf("%s%d", i ? "," : "", b[i]);
                printf("],\"l\":[");
                for (int i = 0; i < K; ++i) printf("%s%d", i ? "," : "", l[i]);
                printf("],\"theta\":[");
                for (int i = 0; i < K; ++i) printf("%s%d", i ? "," : "", theta[i]);
                printf("]}\n");
            }
            if (!mode_count) return true;
        } else if (dfs(j + 1, (partial + th) % p) && !mode_count) return true;
    }
    return false;
}

static void process_split(int F, int R) {
    C[K].split++;
    // INV classifier: only run data violating INV parity (some even run); D0 enforced by split range
    bool viol = false;
    for (int i = 0; i < K; ++i) if (((a[i] + b[i]) % 2 == 0) || (l[i] % 2 == 0)) viol = true;
    if (getenv("INV_RUNS")) viol = (K > p);   // RUNS mode: every inherited word with k > p
    if (!viol) return;
    int fw = build_masks(F, R);
    if (mask[0] & 1u) { cls_zero[K]++; return; }
    if (fw) { cls_full[K]++; return; }
    sums.assign(1 << K, 0);
    nsol_theta = 0;
    dfs(0, 0);
    if (!nsol_theta) cls_joint[K]++; else cls_none[K]++;
    if (nsol_theta) {
        C[K].was_solvable++;
        C[K].theta_solutions += nsol_theta;
        printf("{\"sol\":1,\"p\":%d,\"N\":%d,\"k\":%d,\"a\":[", p, N, K);
        for (int i = 0; i < K; ++i) printf("%s%d", i ? "," : "", a[i]);
        printf("],\"b\":[");
        for (int i = 0; i < K; ++i) printf("%s%d", i ? "," : "", b[i]);
        printf("],\"l\":[");
        for (int i = 0; i < K; ++i) printf("%s%d", i ? "," : "", l[i]);
        printf("],\"theta\":[");
        for (int i = 0; i < K; ++i) printf("%s%d", i ? "," : "", best_theta[i]);
        printf("],\"ntheta\":%lld}\n", mode_count ? nsol_theta : -1LL);
        fflush(stdout);
    }
}

static void splits(int i, int F, int R) {
    if (i == K) {
        if (!rot_min_full()) return;
        process_split(F, R);
        return;
    }
    int lo = use_filters ? std::max(0, r[i] - (p - 1)) : 0;
    int hi = use_filters ? std::min(r[i], p - 1) : r[i];
    for (int x = lo; x <= hi; ++x) { a[i] = x; b[i] = r[i] - x; splits(i + 1, F, R); }
}

static void finish_rl() {
    C[K].rl++;
    if (!rot_min_rl()) return;
    int F = 0, R = 0, oF = 0, hl = 0, hr = 0;
    for (int i = 0; i < K; ++i) { F += l[i]; R += r[i]; oF += l[i] & 1; hl += l[i] / 2; hr += r[i] / 2; }
    if (use_filters) {
        if (R >= 3 * p - 1) return;                 // EGZ
        if (F + hr >= 3 * p - 1) return;            // Theorem P
        if (F >= 2 && R + hl >= 3 * p - 1) return;  // Davenport-alpha
        // T0 filter NOT applied at length 4p-2 (not inherited by deletions)
        if (hl >= p) return;                        // same-letter pairs
    }
    C[K].rl_pass++;
    splits(0, F, R);
}

static void gen(int pos, int rem) {
    int i = pos / 2;
    if (pos == 2 * K) { if (rem == 0) finish_rl(); return; }
    int left = 2 * K - pos - 1;  // parts still to place after this one
    for (int v = 1; v <= rem - left; ++v) {
        if (pos % 2 == 0) r[i] = v; else l[i] = v;
        if (use_filters && pos % 2 == 1) {
            int hl = 0; for (int q = 0; q <= i; ++q) hl += l[q] / 2;
            if (hl >= p) break;
        }
        gen(pos + 1, rem - v);
    }
}

int main(int argc, char** argv) {
    if (argc < 6) { fprintf(stderr, "usage: was_search p N kmin kmax search|count [mut] [filters]\n"); return 1; }
    p = atoi(argv[1]); N = atoi(argv[2]);
    int kmin = atoi(argv[3]), kmax = atoi(argv[4]);
    mode_count = (strcmp(argv[5], "count") == 0) || (strcmp(argv[5], "all") == 0);
    mode_all = (strcmp(argv[5], "all") == 0);
    if (argc > 6) mut = atoi(argv[6]);
    if (argc > 7) use_filters = atoi(argv[7]);
    if (argc > 8) fam = atoi(argv[8]);
    if (p > 31) { fprintf(stderr, "p too large for 32-bit masks\n"); return 1; }
    auto t0 = std::chrono::steady_clock::now();
    for (K = kmin; K <= kmax && 2 * K <= N; ++K) {
        gen(0, N);
        double s = std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
        fprintf(stderr, "{\"cls\":1,\"k\":%d,\"zero\":%lld,\"full\":%lld,\"joint\":%lld,\"none\":%lld}\n", K, cls_zero[K], cls_full[K], cls_joint[K], cls_none[K]);
        fprintf(stderr, "{\"k\":%d,\"rl\":%lld,\"rl_pass\":%lld,\"split\":%lld,\"fullwin\":%lld,\"zero_ok\":%lld,\"was_solvable\":%lld,\"theta_solutions\":%lld,\"dfs_nodes\":%lld,\"secs\":%.1f}\n",
                K, C[K].rl, C[K].rl_pass, C[K].split, C[K].fullwin, C[K].zero_ok, C[K].was_solvable, C[K].theta_solutions, C[K].dfs_nodes, s);
        fflush(stderr);
    }
    long long tot_sol = 0, tot_split = 0;
    for (int k = 0; k <= 40; ++k) { tot_sol += C[k].was_solvable; tot_split += C[k].split; }
    double s = std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
    printf("{\"summary\":1,\"p\":%d,\"N\":%d,\"kmin\":%d,\"kmax\":%d,\"mode\":\"%s\",\"mut\":%d,\"filters\":%d,\"splits\":%lld,\"was_solvable_run_data\":%lld,\"secs\":%.1f}\n",
           p, N, kmin, kmax, mode_count ? "count" : "search", mut, use_filters, tot_split, tot_sol, s);
    return 0;
}
