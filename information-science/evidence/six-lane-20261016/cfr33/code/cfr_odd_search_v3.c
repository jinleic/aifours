/* cfr_odd_search.c -- randomized nested exact search for CFR(R,N) in the odd model (lane cfr33, v3).
 * v3 = v2 + forward declarations (v2 did not compile: callbacks defined after use).
 * v2 fixes v1 (controls/odd-search-smoke-v1): f_1 is now copied inside the solution callback (v1 read it after
 * backtracking had cleared it, producing f_1 = 0, which both checkers rejected); the last level stops at the first
 * lex-admissible solution; store overflow is reported.
 *
 * Usage: cfr_odd_search N R SEED SECONDS OUTFILE
 * Model (notes/facts-v1.md E1, README M1): f_0 = id, f_j (j = 1..R-1) odd bijections of Z_N with f_j(0) = 0, stored
 * on points a = 1..M (M = (N-1)/2) as values v in 1..N-1, with f_j(N-a) = N - v. For odd maps every difference map
 * is odd, so "difference map is a bijection of Z_N" <=> its M absolute classes at a = 1..M are distinct and nonzero.
 * Families for f_j: |f_j(a)|, |f_j(a) - a|, |f_j(a) - f_i(a)| (i < j).
 * Strategy: random f_1 (randomised DFS, first solution); enumerate ALL f_2 orthogonal to {id, f_1}; for each, all f_3
 * orthogonal to {id, f_1, f_2} with f_3 > f_2 (lex), ..., last level: first solution. Repeat with new f_1 until success,
 * SECONDS elapsed (internal cooperative limit) or SIGTERM. Exact DFS: point chosen by minimum remaining values, with a
 * coverage check (every unused class of every family must still be reachable).
 * Output: on success prints "s SATISFIABLE", the maps, and writes OUTFILE (O_EXCL) with R rows in cfr-raw-v1 format
 * (row 0 = identity sequence, row j = f_j^-1 as a sequence); exit 10. Otherwise "s UNKNOWN", exit 0.
 * No claim of validity is made here: witnesses are validated by cfr_check_events.py / cfr_check_posdiff.py.
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
#define MAXK 8
static int N, M, R, K;
static int clsv[MAXN];
static int f[MAXK + 1][MAXM + 1];
static volatile sig_atomic_t stop_flag = 0;
static uint64_t rng_state;
static double t0, tlimit;
static long long nodes = 0;
static int timed_out = 0;

static uint64_t rnd(void) {
    rng_state ^= rng_state >> 12; rng_state ^= rng_state << 25; rng_state ^= rng_state >> 27;
    return rng_state * 2685821657736338717ULL;
}
static double now_s(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + ts.tv_nsec * 1e-9; }
static void on_term(int s) { (void)s; stop_flag = 1; }
static inline int md(int x) { x %= N; if (x < 0) x += N; return x; }

/* per-level search state */
typedef struct {
    int j;                       /* level being assigned */
    int nf;                      /* number of families = j + 1 */
    uint8_t cl[MAXM + 1][MAXN][MAXK + 2]; /* class of family fam for (a, v); 0 = invalid */
    uint32_t used[MAXK + 2];
    int assigned[MAXM + 1];
    int val[MAXM + 1];
    int randomize;
    long long nsol, maxsol;
    int (*cb)(void *ctx);        /* return 1 to stop search */
    void *ctx;
    int stop;
} Lev;

static void lev_init(Lev *L, int j) {
    L->j = j; L->nf = j + 1;
    for (int a = 1; a <= M; a++) {
        for (int v = 0; v < N; v++) {
            for (int fam = 0; fam < L->nf; fam++) L->cl[a][v][fam] = 0;
            if (v == 0) continue;
            L->cl[a][v][0] = (uint8_t)clsv[v];
            L->cl[a][v][1] = (uint8_t)clsv[md(v - a)];
            for (int i = 1; i < j; i++) L->cl[a][v][1 + i] = (uint8_t)clsv[md(v - f[i][a])];
        }
        L->assigned[a] = 0; L->val[a] = 0;
    }
    for (int fam = 0; fam < L->nf; fam++) L->used[fam] = 0;
    L->nsol = 0; L->stop = 0;
}

static inline int ok(Lev *L, int a, int v) {
    if (v == 0) return 0;
    for (int fam = 0; fam < L->nf; fam++) {
        int c = L->cl[a][v][fam];
        if (c == 0 || (L->used[fam] >> c) & 1u) return 0;
    }
    return 1;
}

static void dfs(Lev *L, int depth) {
    if (L->stop) return;
    if ((++nodes & 4095) == 0) {
        if (stop_flag || now_s() - t0 > tlimit) { timed_out = 1; L->stop = 1; return; }
    }
    if (depth == M) {
        L->nsol++;
        if (L->cb && L->cb(L->ctx)) L->stop = 1;
        if (L->maxsol && L->nsol >= L->maxsol) L->stop = 1;
        return;
    }
    /* choose unassigned point with fewest candidates; coverage check */
    int best = -1, bestc = 1 << 30;
    uint32_t cover[MAXK + 2];
    for (int fam = 0; fam < L->nf; fam++) cover[fam] = 0;
    int cand[MAXM + 1][MAXN]; int nc[MAXM + 1];
    for (int a = 1; a <= M; a++) {
        if (L->assigned[a]) continue;
        int c = 0;
        for (int v = 1; v < N; v++) {
            if (ok(L, a, v)) {
                cand[a][c++] = v;
                for (int fam = 0; fam < L->nf; fam++) cover[fam] |= 1u << L->cl[a][v][fam];
            }
        }
        nc[a] = c;
        if (c == 0) return;
        if (c < bestc || (c == bestc && L->randomize && (rnd() & 1))) { bestc = c; best = a; }
    }
    uint32_t full = ((1u << (M + 1)) - 2u);
    for (int fam = 0; fam < L->nf; fam++) {
        uint32_t need = full & ~L->used[fam];
        if ((cover[fam] & need) != need) return;
    }
    int a = best;
    int c = nc[a];
    int order[MAXN];
    for (int i = 0; i < c; i++) order[i] = cand[a][i];
    if (L->randomize) {
        for (int i = c - 1; i > 0; i--) { int k = (int)(rnd() % (uint64_t)(i + 1)); int t = order[i]; order[i] = order[k]; order[k] = t; }
    }
    for (int i = 0; i < c && !L->stop; i++) {
        int v = order[i];
        L->assigned[a] = 1; L->val[a] = v;
        for (int fam = 0; fam < L->nf; fam++) L->used[fam] |= 1u << L->cl[a][v][fam];
        dfs(L, depth + 1);
        for (int fam = 0; fam < L->nf; fam++) L->used[fam] &= ~(1u << L->cl[a][v][fam]);
        L->assigned[a] = 0; L->val[a] = 0;
    }
}

/* solution storage */
typedef struct { int cap, cnt; uint8_t *buf; Lev *L; } Store;
static int store_cb(void *ctx) {
    Store *S = (Store *)ctx;
    if (S->cnt >= S->cap) return 1;
    for (int a = 1; a <= M; a++) S->buf[(size_t)S->cnt * M + (a - 1)] = (uint8_t)S->L->val[a];
    S->cnt++;
    return 0;
}
static int lexgt(const uint8_t *x, int j) { /* x > f[j] lexicographically over a = 1..M */
    for (int a = 1; a <= M; a++) { if (x[a - 1] != f[j][a]) return x[a - 1] > f[j][a]; }
    return 0;
}

static int last_cb(void *ctx);
static long long stat_overflow;
static Lev levs[MAXK + 1];
static long long stat_f1 = 0, stat_l2 = 0, stat_tri = 0, stat_deep = 0;
static int found = 0;

static int extend(int j) {          /* assign level j (>= 2) */
    if (j > K) { found = 1; return 1; }
    Lev *L = &levs[j];
    lev_init(L, j);
    L->randomize = 0;
    if (j == K) {                   /* last level: first solution with lex > f[j-1] (j >= 3) */
        L->cb = last_cb; L->ctx = L; L->maxsol = 0;
        int before = found;
        (void)before;
        dfs(L, 0);
        if (L->stop && !timed_out) { found = 1; return 1; }
        return 0;
    }
    Store S; S.cap = (j == 2) ? (1 << 22) : (1 << 20); S.cnt = 0; S.buf = malloc((size_t)S.cap * M); S.L = L;
    L->cb = store_cb; L->ctx = &S; L->maxsol = 0;
    dfs(L, 0);
    if (S.cnt >= S.cap) stat_overflow++;
    if (j == 2) stat_l2 += S.cnt;
    if (j == 3) stat_tri += S.cnt;
    if (j >= 4) stat_deep += S.cnt;
    for (int s = 0; s < S.cnt && !timed_out; s++) {
        uint8_t *x = S.buf + (size_t)s * M;
        if (j >= 3 && !lexgt(x, j - 1)) continue;
        for (int a = 1; a <= M; a++) f[j][a] = x[a - 1];
        if (extend(j + 1)) { free(S.buf); return 1; }
    }
    free(S.buf);
    return 0;
}

static int first_cb(void *ctx) {
    Lev *L = (Lev *)ctx;
    for (int a = 1; a <= M; a++) f[L->j][a] = L->val[a];
    return 1;
}
static int last_cb(void *ctx) {   /* accept first solution with lex > f[j-1] when j >= 3 */
    Lev *L = (Lev *)ctx;
    int j = L->j;
    if (j >= 3) {
        int gt = 0, decided = 0;
        for (int a = 1; a <= M && !decided; a++) {
            if (L->val[a] != f[j - 1][a]) { gt = L->val[a] > f[j - 1][a]; decided = 1; }
        }
        if (!gt) return 0;
    }
    for (int a = 1; a <= M; a++) f[j][a] = L->val[a];
    return 1;
}
static long long stat_overflow = 0;

int main(int argc, char **argv) {
    if (argc != 6) { fprintf(stderr, "usage: cfr_odd_search N R SEED SECONDS OUTFILE\n"); return 2; }
    N = atoi(argv[1]); R = atoi(argv[2]); K = R - 1; M = (N - 1) / 2;
    rng_state = 0x9E3779B97F4A7C15ULL ^ (uint64_t)strtoull(argv[3], 0, 10) * 0xBF58476D1CE4E5B9ULL;
    if (rng_state == 0) rng_state = 1;
    tlimit = atof(argv[4]);
    const char *outfile = argv[5];
    if (N % 2 == 0 || N > MAXN || N < 3 || K < 1 || K > MAXK - 1) { fprintf(stderr, "bad params\n"); return 2; }
    for (int v = 0; v < N; v++) clsv[v] = v <= N - v ? v : N - v;
    signal(SIGTERM, on_term); signal(SIGINT, on_term);
    t0 = now_s();
    printf("c cfr_odd_search v1 N %d R %d seed %s limit %.0f\n", N, R, argv[3], tlimit); fflush(stdout);
    while (!found && !timed_out) {
        Lev *L = &levs[1];
        lev_init(L, 1); L->randomize = 1; L->cb = first_cb; L->ctx = L; L->maxsol = 1;
        dfs(L, 0);
        if (timed_out) break;
        if (L->nsol == 0) { printf("c no f_1 exists\n"); break; }
        stat_f1++;
        long long l2b = stat_l2, trib = stat_tri;
        if (K == 1) { found = 1; break; }
        extend(2);
        if ((stat_f1 % 100) == 1 || found)
            printf("c f1 #%lld neighbours %lld triangles %lld | totals l2 %lld tri %lld deep %lld nodes %lld t %.1f\n",
                   stat_f1, stat_l2 - l2b, stat_tri - trib, stat_l2, stat_tri, stat_deep, nodes, now_s() - t0);
        fflush(stdout);
    }
    printf("c final f1 %lld l2 %lld tri %lld deep %lld nodes %lld store_overflows %lld time %.2f\n", stat_f1, stat_l2, stat_tri, stat_deep, nodes, stat_overflow, now_s() - t0);
    if (!found) { printf("s UNKNOWN\n"); return 0; }
    printf("s SATISFIABLE\n");
    for (int j = 1; j <= K; j++) {
        printf("v f%d", j);
        for (int a = 1; a <= M; a++) printf(" %d", f[j][a]);
        printf("\n");
    }
    /* rows: row 0 identity; row j = inverse of full odd map */
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
