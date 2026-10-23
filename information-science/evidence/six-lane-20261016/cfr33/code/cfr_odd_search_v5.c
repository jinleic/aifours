/* cfr_odd_search_v5.c -- v4 plus: F1MODE "f1file:PATH" (one candidate f_1 per line: M values for a = 1..M, processed in
 * order, each exhaustively), optional SYMK "symK:m1,m2,..." (multipliers fixing f_1 under conjugation; level-2 maps are
 * then restricted to lexicographically smallest representatives of their conjugation orbit and level 3 drops the
 * lex > f_2 condition), periodic progress lines every 30 s, and per-f_1 exhaustion reports (lane cfr33, v5).
 * Usage: cfr_odd_search_v5 N R SEED SECONDS OUTFILE [random|linear:c|f1file:PATH] [symK:m1,m2,...]
 *
 * Usage: cfr_odd_search_v4 N R SEED SECONDS OUTFILE [F1MODE]
 *   F1MODE: "random" (default: random odd orthomorphism f_1 per round) or "linear:c" (f_1(x) = c x, single round,
 *           exhaustive over all deeper levels within the time limit).
 * Model and output exactly as cfr_odd_search_v3.c (odd maps on points a = 1..M, M = (N-1)/2, values 1..N-1).
 * Search at each level is an exact cover: items = points a (each gets one value) and (family, class) pairs (each class of
 * each family used exactly once); option (a, v) covers point a and one class per family. DLX-style branching on the
 * item with the fewest remaining options (points or family classes), candidate sets kept as incremental bitmasks.
 * Levels: f_1 (random first solution, or linear), f_2 all solutions, f_j (3 <= j < K) all solutions with f_j > f_{j-1}
 * lexicographically, last level the first solution with f_K > f_{K-1}. Stops at success, SECONDS (internal), SIGTERM.
 * Exit 10 + "s SATISFIABLE" + OUTFILE (O_EXCL, cfr-raw-v1 rows: identity, then f_j^-1) on success; else "s UNKNOWN".
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>
#include <fcntl.h>
#include <unistd.h>
#include <signal.h>

#define MAXN 63
#define MAXM 31
#define MAXK 7
#define MAXF (MAXK + 1)
static int N, M, R, K;
static int clsv[MAXN];
static int f[MAXK + 1][MAXM + 1];
static volatile sig_atomic_t stop_flag = 0;
static uint64_t rng_state;
static double t0, tlimit;
static long long nodes = 0;
static int timed_out = 0, found = 0;
static int nsym = 0, symmu[64];
static double last_progress = 0;
static long long cur_f1_index = 0;

static uint64_t rnd(void) {
    rng_state ^= rng_state >> 12; rng_state ^= rng_state << 25; rng_state ^= rng_state >> 27;
    return rng_state * 2685821657736338717ULL;
}
static double now_s(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + ts.tv_nsec * 1e-9; }
static void on_term(int s) { (void)s; stop_flag = 1; }
static inline int md(int x) { x %= N; if (x < 0) x += N; return x; }

typedef struct {
    int j, nf, randomize, stop, mode;      /* mode 0: store all; 1: first (with lex filter if j >= 3) */
    uint8_t cl[MAXM + 1][MAXN][MAXF];      /* class per family for (a, v); 0 invalid */
    uint64_t kill[MAXF][MAXM + 1][MAXM + 1];/* values v at point a with class c in family fam */
    uint64_t cand0[MAXM + 1];
    int val[MAXM + 1];
    long long nsol;
    uint8_t *store; long long cap, cnt;
} Lev;

static void lev_init(Lev *L, int j) {
    L->j = j; L->nf = j + 1; L->stop = 0; L->nsol = 0; L->cnt = 0;
    memset(L->kill, 0, sizeof L->kill);
    for (int a = 1; a <= M; a++) {
        uint64_t c0 = 0;
        for (int v = 1; v < N; v++) {
            int okv = 1;
            L->cl[a][v][0] = (uint8_t)clsv[v];
            L->cl[a][v][1] = (uint8_t)clsv[md(v - a)];
            for (int i = 1; i < j; i++) L->cl[a][v][1 + i] = (uint8_t)clsv[md(v - f[i][a])];
            for (int fam = 0; fam < L->nf; fam++) if (L->cl[a][v][fam] == 0) okv = 0;
            if (okv) {
                c0 |= 1ULL << v;
                for (int fam = 0; fam < L->nf; fam++) L->kill[fam][a][L->cl[a][v][fam]] |= 1ULL << v;
            }
        }
        L->cand0[a] = c0; L->val[a] = 0;
    }
}

static int lexgt_val(Lev *L, int j) {
    for (int a = 1; a <= M; a++) if (L->val[a] != f[j - 1][a]) return L->val[a] > f[j - 1][a];
    return 0;
}

static void on_solution(Lev *L) {
    L->nsol++;
    if (L->mode == 1) {
        if (L->j >= 3 && !(L->j == 3 && nsym > 0) && !lexgt_val(L, L->j)) return;
        for (int a = 1; a <= M; a++) f[L->j][a] = L->val[a];
        L->stop = 1;
        return;
    }
    if (L->cnt >= L->cap) { L->stop = 1; return; }
    for (int a = 1; a <= M; a++) L->store[L->cnt * M + (a - 1)] = (uint8_t)L->val[a];
    L->cnt++;
}

static void dfs(Lev *L, uint64_t *cand, uint32_t *used, uint32_t assigned, int depth) {
    if (L->stop) return;
    if ((++nodes & 1023) == 0) {
        if (stop_flag || now_s() - t0 > tlimit) { timed_out = 1; L->stop = 1; return; }
    }
    if (depth == M) { on_solution(L); return; }
    /* item selection: points */
    int bestkind = 0, besta = -1, bestfam = -1, bestc = -1, bestcount = 1 << 30;
    for (int a = 1; a <= M; a++) {
        if (assigned >> a & 1u) continue;
        int c = __builtin_popcountll(cand[a]);
        if (c == 0) return;
        if (c < bestcount || (c == bestcount && L->randomize && (rnd() & 1))) { bestcount = c; besta = a; bestkind = 0; }
    }
    /* family classes */
    for (int fam = 0; fam < L->nf; fam++) {
        uint32_t freec = (((1u << (M + 1)) - 2u) & ~used[fam]);
        while (freec) {
            int c = __builtin_ctz(freec); freec &= freec - 1;
            int cnt = 0;
            for (int a = 1; a <= M && cnt < bestcount; a++) {
                if (assigned >> a & 1u) continue;
                cnt += __builtin_popcountll(cand[a] & L->kill[fam][a][c]);
            }
            if (cnt == 0) return;
            if (cnt < bestcount) { bestcount = cnt; bestkind = 1; bestfam = fam; bestc = c; }
        }
    }
    /* collect options (a, v) */
    int oa[MAXM * MAXN], ov[MAXM * MAXN], no = 0;
    if (bestkind == 0) {
        uint64_t m = cand[besta];
        while (m) { int v = __builtin_ctzll(m); m &= m - 1; oa[no] = besta; ov[no] = v; no++; }
    } else {
        for (int a = 1; a <= M; a++) {
            if (assigned >> a & 1u) continue;
            uint64_t m = cand[a] & L->kill[bestfam][a][bestc];
            while (m) { int v = __builtin_ctzll(m); m &= m - 1; oa[no] = a; ov[no] = v; no++; }
        }
    }
    if (L->randomize) {
        for (int i = no - 1; i > 0; i--) { int k = (int)(rnd() % (uint64_t)(i + 1)); int t = oa[i]; oa[i] = oa[k]; oa[k] = t; t = ov[i]; ov[i] = ov[k]; ov[k] = t; }
    }
    uint64_t nc[MAXM + 1];
    uint32_t nu[MAXF];
    for (int i = 0; i < no && !L->stop; i++) {
        int a = oa[i], v = ov[i];
        for (int fam = 0; fam < L->nf; fam++) nu[fam] = used[fam] | (1u << L->cl[a][v][fam]);
        for (int b = 1; b <= M; b++) {
            if ((assigned >> b & 1u) || b == a) { nc[b] = 0; continue; }
            uint64_t x = cand[b];
            for (int fam = 0; fam < L->nf; fam++) x &= ~L->kill[fam][b][L->cl[a][v][fam]];
            nc[b] = x;
        }
        nc[a] = 0;
        L->val[a] = v;
        dfs(L, nc, nu, assigned | (1u << a), depth + 1);
        L->val[a] = 0;
    }
}

static void run_level(Lev *L) {
    uint64_t cand[MAXM + 1]; uint32_t used[MAXF];
    for (int a = 1; a <= M; a++) cand[a] = L->cand0[a];
    for (int fam = 0; fam < MAXF; fam++) used[fam] = 0;
    dfs(L, cand, used, 0u, 0);
}

static int full_of(const uint8_t *x, int t) { /* odd map value at t in Z_N from point values x[a-1] */
    t = md(t);
    if (t == 0) return 0;
    if (t <= M) return x[t - 1];
    return md(-(int)x[N - t - 1]);
}
static int is_canonical(const uint8_t *x) {   /* x <= conj_mu(x) lexicographically for every listed mu */
    for (int s = 0; s < nsym; s++) {
        int mu = symmu[s], muinv = 1;
        for (int y = 1; y < N; y++) if (md(mu * y) == 1) { muinv = y; break; }
        for (int a = 1; a <= M; a++) {
            int c = md(mu * full_of(x, muinv * a));
            if (c != x[a - 1]) { if (c < x[a - 1]) return 0; break; }
        }
    }
    return 1;
}
static Lev levs[MAXK + 1];
static long long stat_f1 = 0, stat_l2 = 0, stat_tri = 0, stat_deep = 0, stat_overflow = 0;

static int extend(int j) {
    if (j > K) { found = 1; return 1; }
    Lev *L = &levs[j];
    lev_init(L, j); L->randomize = 0;
    if (j == K) {
        L->mode = 1;
        run_level(L);
        if (L->stop && !timed_out) { found = 1; return 1; }
        return 0;
    }
    L->mode = 0;
    if (!L->store) { L->cap = (j == 2) ? (1LL << 22) : (1LL << 20); L->store = malloc((size_t)L->cap * M); }
    run_level(L);
    if (L->cnt >= L->cap) stat_overflow++;
    if (j == 2) stat_l2 += L->cnt;
    else if (j == 3) stat_tri += L->cnt;
    else stat_deep += L->cnt;
    long long cnt = L->cnt;
    for (long long s = 0; s < cnt && !timed_out; s++) {
        uint8_t *x = L->store + s * M;
        if (j == 2 && nsym > 0 && !is_canonical(x)) continue;
        if (j >= 3 && !(j == 3 && nsym > 0)) {
            int gt = 0;
            for (int a = 1; a <= M; a++) if (x[a - 1] != f[j - 1][a]) { gt = x[a - 1] > f[j - 1][a]; break; }
            if (!gt) continue;
        }
        if (now_s() - last_progress > 30) {
            last_progress = now_s();
            printf("c progress f1idx %lld level %d item %lld/%lld l2 %lld tri %lld deep %lld nodes %lld t %.0f\n",
                   cur_f1_index, j, s, cnt, stat_l2, stat_tri, stat_deep, nodes, now_s() - t0);
            fflush(stdout);
        }
        for (int a = 1; a <= M; a++) f[j][a] = x[a - 1];
        if (extend(j + 1)) return 1;
    }
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 6 || argc > 8) { fprintf(stderr, "usage: cfr_odd_search_v5 N R SEED SECONDS OUTFILE [random|linear:c|f1file:PATH] [symK:m1,m2,...]\n"); return 2; }
    N = atoi(argv[1]); R = atoi(argv[2]); K = R - 1; M = (N - 1) / 2;
    rng_state = 0x9E3779B97F4A7C15ULL ^ ((uint64_t)strtoull(argv[3], 0, 10) * 0xBF58476D1CE4E5B9ULL);
    if (!rng_state) rng_state = 1;
    tlimit = atof(argv[4]);
    const char *outfile = argv[5];
    int linear_c = 0;
    FILE *f1fp = NULL;
    if (argc >= 7 && strncmp(argv[6], "linear:", 7) == 0) linear_c = atoi(argv[6] + 7);
    if (argc >= 7 && strncmp(argv[6], "f1file:", 7) == 0) { f1fp = fopen(argv[6] + 7, "r"); if (!f1fp) { perror("f1file"); return 2; } }
    if (argc == 8 && strncmp(argv[7], "symK:", 5) == 0) {
        char *p = argv[7] + 5;
        while (*p && nsym < 64) { symmu[nsym++] = (int)strtol(p, &p, 10); if (*p == ',') p++; }
    }
    if (N % 2 == 0 || N > MAXN || N < 3 || K < 1 || K > MAXK || M > 30) { fprintf(stderr, "bad params\n"); return 2; }
    for (int v = 0; v < N; v++) clsv[v] = v <= N - v ? v : N - v;
    signal(SIGTERM, on_term); signal(SIGINT, on_term);
    t0 = now_s();
    printf("c cfr_odd_search_v5 N %d R %d seed %s limit %.0f f1mode %s symK %d\n", N, R, argv[3], tlimit, argc >= 7 ? argv[6] : "random", nsym);
    fflush(stdout);
    while (!found && !timed_out) {
        if (linear_c) {
            if (stat_f1 > 0) break;
            for (int a = 1; a <= M; a++) f[1][a] = md(linear_c * a);
        } else if (f1fp) {
            int okread = 1;
            for (int a = 1; a <= M; a++) if (fscanf(f1fp, "%d", &f[1][a]) != 1) okread = 0;
            if (!okread) break;
            cur_f1_index++;
            if (nsym > 0) {   /* verify f_1 is invariant under every listed multiplier */
                uint8_t x[MAXM]; for (int a = 1; a <= M; a++) x[a - 1] = (uint8_t)f[1][a];
                for (int s = 0; s < nsym; s++) {
                    int mu = symmu[s];
                    for (int a = 1; a <= M; a++) if (md(mu * full_of(x, a)) != full_of(x, mu * a)) { printf("c f_1 #%lld not invariant under %d\n", cur_f1_index, mu); return 4; }
                }
            }
        } else {
            Lev *L = &levs[1];
            lev_init(L, 1); L->randomize = 1; L->mode = 1;
            run_level(L);
            if (timed_out) break;
            if (L->nsol == 0) { printf("c no f_1\n"); break; }
        }
        stat_f1++;
        long long l2b = stat_l2, trib = stat_tri;
        if (K == 1) { found = 1; break; }
        extend(2);
        if ((stat_f1 % 50) == 1 || found || linear_c || f1fp)
            printf("c f1 #%lld neighbours %lld triangles %lld exhausted %d | totals l2 %lld tri %lld deep %lld nodes %lld t %.1f\n",
                   stat_f1, stat_l2 - l2b, stat_tri - trib, (!found && !timed_out && stat_overflow == 0), stat_l2, stat_tri, stat_deep, nodes, now_s() - t0);
        fflush(stdout);
    }
    printf("c final f1 %lld l2 %lld tri %lld deep %lld nodes %lld overflows %lld timed_out %d time %.2f\n",
           stat_f1, stat_l2, stat_tri, stat_deep, nodes, stat_overflow, timed_out, now_s() - t0);
    if (!found) { printf("s UNKNOWN\n"); return 0; }
    printf("s SATISFIABLE\n");
    for (int j = 1; j <= K; j++) { printf("v f%d", j); for (int a = 1; a <= M; a++) printf(" %d", f[j][a]); printf("\n"); }
    int fd = open(outfile, O_WRONLY | O_CREAT | O_EXCL, 0444);
    if (fd < 0) { perror("open outfile"); return 3; }
    FILE *o = fdopen(fd, "w");
    for (int c = 0; c < N; c++) fprintf(o, c ? " %d" : "%d", c);
    fprintf(o, "\n");
    for (int j = 1; j <= K; j++) {
        int full[MAXN], row[MAXN];
        full[0] = 0;
        for (int a = 1; a <= M; a++) { full[a] = f[j][a]; full[N - a] = md(-f[j][a]); }
        for (int c = 0; c < N; c++) row[c] = -1;
        for (int s = 0; s < N; s++) row[full[s]] = s;
        for (int c = 0; c < N; c++) fprintf(o, c ? " %d" : "%d", row[c]);
        fprintf(o, "\n");
    }
    fclose(o);
    fflush(stdout);
    return 10;
}
