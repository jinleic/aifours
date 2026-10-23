/* cfr_perm_search_c21v1.c -- exact search for CFR(R,N) = (Z_N, R+1; 1) difference matrices over FULL normalised
 * permutations (sub-lane cfr21, worker InfoCFR27Lift.C21FullPermPrep). Adapted from code/cfr_odd_search_c21v1.c (sha256
 * 66f1fead6e64f9f32a6c2e319d2ec22567438424c64343a24d8a09b8c6397421, the byte copy of the cfr27 odd engine v7); no oddness
 * is assumed anywhere.
 * Model: normal form rows 0, id, f_1..f_K (K = R-1) as functions of the column x in Z_N; every f_j is a normalised
 * orthomorphism (f_j(0) = 0; f_j and f_j - id bijections of Z_N) and every f_i - f_j (i != j) is a bijection. A map is
 * stored by its values at all M = N-1 points a = 1..N-1 (values 1..N-1); the class of a difference residue v is v itself
 * (clsv[v] = v; class 0 = collision, never allowed).
 * Per f_1 (search unchanged from the odd v6/v7 engine apart from M and clsv): L2 = ALL normalised orthomorphisms g with
 * g - f_1 bijective, enumerated by exact cover: items = points a (one value each) and (family, class) pairs (each class
 * 1..N-1 of each family exactly once); families: value v, v - a (orthogonal to id), v - f_1(a); option (a, v) covers
 * point a and one class per family; DLX-style branching on the item with the fewest remaining options, candidate sets
 * kept as incremental bitmasks. L2 is stored completely; then (K-1)-cliques of pairwise orthogonal members of L2 are
 * searched exhaustively over adjacency lists built by direct pair checks (K = 2: any member of L2 suffices, no adjacency).
 * Memory (never exceeded): L2 store <= L2CAP = 2^23 maps (<= 240 MiB as M <= 30); adjacency offsets + edge list <=
 * ADJ_BYTES = 512 MiB (edge list grows by doubling up to ADJCAP entries, so int edge indices cannot overflow); clique
 * scratch <= K-3 arrays of at most max-degree ints. A full L2 store, the edge cap or a failed allocation stops THAT f_1
 * as UNKNOWN ("overflow 1", never "exhausted 1"); the run continues with the next f_1. For overflow controls the caps
 * may be lowered at compile time (-DL2CAP=..., -DADJ_BYTES=...); values above the defaults are rejected as bad params.
 * Usage: cfr_perm_search_c21v1 N R SEED SECONDS OUTFILE [F1MODE] [symK:m1,m2,...]       N odd, 3 <= N <= 31; 2 <= R <= 8
 *   f1file:PATH  one f_1 per line, exactly N-1 integers f_1(1) .. f_1(N-1) (exit 2 on a malformed line), processed in
 *                order, each exhaustively; one line "c f1 #i neighbours |L2| L2edges e exhausted 0|1 overflow 0|1 | ..."
 *                per f_1; exhausted 1 only if THIS f_1 finished (complete L2, adjacency and clique search) with no
 *                deadline, SIGTERM or overflow. symK (f1file only): exit 4 unless every f_1 commutes with the listed
 *                multipliers.
 *   linear:c     the single f_1(x) = c x.
 *   random       (default) a random f_1 per round, optionally restricted: fam:pres3Z (f_1(3Z_N) = 3Z_N), fam:lin9:c
 *                (f_1(x) = c x mod 9), fam:lin3 (f_1(x) = -x mod 3).
 *   Every f_1 is checked to be a normalised orthomorphism of Z_N before use (exit 4 otherwise).
 * Changes vs the odd engine: M = N-1; clsv[v] = v; full_of reads x[t-1] for every t != 0; output full[a] = f_j(a) once
 * (no negated half); exact f1file lines and f_1 validation; bounded L2/adjacency memory with per-f_1 overflow and a
 * per-f_1 (not cumulative) exhaustion flag; the adjacency build polls the deadline every 16 vertices and the clique
 * search polls it too; K = 2 skips the adjacency; an independent final check of all (K+2)(K+1)/2 row pairs of the
 * 0/id/f_1..f_K matrix runs before anything is written (exit 5 "c INTERNAL MISMATCH"). The unreachable v5
 * level-by-level code (extend, is_canonical; never called) is kept unchanged.
 * Stops at success, at SECONDS (internal CLOCK_MONOTONIC deadline) or on SIGTERM/SIGINT. Success: exit 10, "s SATISFIABLE",
 * "v f_j" lines and OUTFILE (O_EXCL, mode 0444, cfr-raw-v1, R rows: identity, then the rows f_j^-1 as symbol sequences).
 * Otherwise "s UNKNOWN" (exit 0), also after a finished f1file: exhaustion is reported per f_1 only and is a restricted
 * statement about that f_1, never about CFR(R,N).
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
#ifndef L2CAP
#define L2CAP (1LL << 23)                     /* L2 store capacity in maps (x M <= 30 bytes: <= 240 MiB) */
#endif
#ifndef ADJ_BYTES
#define ADJ_BYTES (512LL << 20)               /* adjacency offsets ((L2CAP + 1) ints) + edge list, in bytes */
#endif
#define ADJCAP (((long long)(ADJ_BYTES) - (long long)sizeof(int) * ((long long)(L2CAP) + 1)) / (long long)sizeof(int))   /* edge-list entries */
static int N, M, R, K;
static int clsv[MAXN];
static int f[MAXK + 1][MAXM + 1];
static volatile sig_atomic_t stop_flag = 0;
static uint64_t rng_state;
static double t0, tlimit;
static long long nodes = 0;
static int timed_out = 0, found = 0;
static int nsym = 0, symmu[64];
static int famkind = 0, famc = 0; /* 1 pres3Z, 2 lin9:c, 3 lin3 */
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
        if (j == 1 && famkind) {
            uint64_t keep = 0;
            for (int v = 1; v < N; v++) {
                int okf = 1;
                if (famkind == 1) okf = ((a % 3 == 0) == (v % 3 == 0));
                else if (famkind == 2) okf = (md(v - famc * a) % 9 == 0);
                else if (famkind == 3) okf = (md(v + a) % 3 == 0);
                if (okf) keep |= 1ULL << v;
            }
            c0 &= keep;
            for (int fam = 0; fam < L->nf; fam++) for (int c = 0; c <= M; c++) L->kill[fam][a][c] &= keep;
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

static int full_of(const uint8_t *x, int t) { /* full map value at t in Z_N from point values x[a-1], a = 1..N-1 */
    t = md(t);
    if (t == 0) return 0;
    return x[t - 1];
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

static int orth(const uint8_t *g, const uint8_t *h) {
    uint32_t m = 0;
    for (int a = 0; a < M; a++) {
        int c = clsv[md((int)g[a] - (int)h[a])];
        if (c == 0) return 0;
        uint32_t b = 1u << c;
        if (m & b) return 0;
        m |= b;
    }
    return 1;
}
static long long stat_edges = 0, stat_cliques_tested = 0;
static int *adjoff = NULL, *adj = NULL; static long long adjcap = 0;
static int clq[MAXK + 1];
static int f1_overflow = 0;     /* the current f_1 hit a memory cap or a failed allocation: it stays UNKNOWN */
static int clique_rec(Lev *L, int depth, int need, int *candv, int ncand) {
    /* candv: vertices adjacent to all chosen so far, sorted ascending, all > last chosen */
    if (depth == need) return 1;
    for (int i = 0; i < ncand && !timed_out && !f1_overflow; i++) {
        if ((stat_cliques_tested & 4095) == 0 && (stop_flag || now_s() - t0 > tlimit)) { timed_out = 1; return 0; }
        int v = candv[i];
        clq[depth] = v;
        if (depth + 1 == need) return 1;
        int *nc = malloc(sizeof(int) * (ncand > 0 ? ncand : 1)); int nn = 0;
        if (!nc) { printf("c clique scratch allocation failed (f_1 #%lld UNKNOWN)\n", stat_f1); f1_overflow = 1; return 0; }
        int p = adjoff[v], q = adjoff[v + 1];
        for (int k = i + 1, e = p; k < ncand && e < q; ) {
            if (candv[k] == adj[e]) { nc[nn++] = candv[k]; k++; e++; }
            else if (candv[k] < adj[e]) k++; else e++;
        }
        stat_cliques_tested++;
        int r = (nn >= need - depth - 1) ? clique_rec(L, depth + 1, need, nc, nn) : 0;
        free(nc);
        if (r) return 1;
    }
    return 0;
}
static int local_clique(void) {
    Lev *L = &levs[2];
    f1_overflow = 0;
    lev_init(L, 2); L->randomize = 0; L->mode = 0;
    if (!L->store) {
        L->store = malloc((size_t)L2CAP * (size_t)M);
        if (!L->store) { printf("c L2 store allocation failed (f_1 #%lld UNKNOWN)\n", stat_f1); f1_overflow = 1; stat_overflow++; return 0; }
        L->cap = L2CAP;
    }
    run_level(L);
    if (timed_out) return 0;
    long long n2 = L->cnt; stat_l2 += n2;
    int need = K - 1;               /* f_2..f_K */
    if (need == 1 && n2 > 0) { clq[0] = 0; goto success; }
    if (L->cnt >= L->cap) { printf("c L2 store cap %lld reached (f_1 #%lld UNKNOWN)\n", L->cap, stat_f1); f1_overflow = 1; stat_overflow++; return 0; }
    if (need == 1) return 0;
    /* adjacency (upper triangle, sorted); offsets + edge list stay within ADJ_BYTES */
    long long edges = 0;
    free(adjoff);
    adjoff = malloc(sizeof(int) * (size_t)(n2 + 1));
    if (!adj) {
        long long a0 = ADJCAP < (1LL << 20) ? ADJCAP : (1LL << 20);
        adj = a0 > 0 ? malloc(sizeof(int) * (size_t)a0) : NULL;
        adjcap = adj ? a0 : 0;
    }
    if (!adjoff || !adj) { printf("c adjacency allocation failed (f_1 #%lld UNKNOWN)\n", stat_f1); f1_overflow = 1; stat_overflow++; return 0; }
    for (long long u = 0; u < n2; u++) {
        adjoff[u] = (int)edges;
        const uint8_t *gu = L->store + u * M;
        for (long long v = u + 1; v < n2; v++) {
            if (orth(gu, L->store + v * M)) {
                if (edges >= adjcap) {
                    long long ncap = adjcap * 2 < ADJCAP ? adjcap * 2 : ADJCAP;
                    int *na = edges < ADJCAP ? realloc(adj, sizeof(int) * (size_t)ncap) : NULL;
                    if (!na) { printf("c adjacency cap reached at %lld edges (f_1 #%lld UNKNOWN)\n", edges, stat_f1); f1_overflow = 1; stat_overflow++; return 0; }
                    adj = na; adjcap = ncap;
                }
                adj[edges++] = (int)v;
            }
        }
        if ((u & 15) == 0 && (stop_flag || now_s() - t0 > tlimit)) { timed_out = 1; return 0; }
    }
    adjoff[n2] = (int)edges;
    stat_edges += edges; stat_tri += edges;
    for (long long u = 0; u < n2 && !timed_out && !f1_overflow; u++) {
        int nn = adjoff[u + 1] - adjoff[u];
        if (nn < need - 1) continue;
        clq[0] = (int)u;
        if (need == 2) { clq[1] = adj[adjoff[u]]; goto success; }
        if (clique_rec(L, 1, need, adj + adjoff[u], nn)) goto success;
    }
    if (f1_overflow) stat_overflow++;
    return 0;
success:
    for (int i = 0; i < need; i++) for (int a = 1; a <= M; a++) f[2 + i][a] = L->store[(size_t)clq[i] * M + (a - 1)];
    found = 1;
    return 1;
}

/* f_1 must be a normalised orthomorphism: f_1(1..M) a permutation of 1..N-1 and f_1(a) - a a permutation of 1..N-1 */
static int f1_valid(void) {
    uint64_t sv = 0, sd = 0;
    for (int a = 1; a <= M; a++) {
        int v = f[1][a];
        if (v < 1 || v >= N) return 0;
        int d = md(v - a);
        if (d == 0 || (sv >> v & 1ULL) || (sd >> d & 1ULL)) return 0;
        sv |= 1ULL << v; sd |= 1ULL << d;
    }
    return 1;
}

/* next f1file line: exactly M = N-1 integers f_1(1) .. f_1(M), LF-terminated; 1 = read, 0 = end of file, -1 = malformed */
static int read_f1_line(FILE *fp) {
    char buf[4096];
    if (!fgets(buf, sizeof buf, fp)) return 0;
    size_t len = strlen(buf);
    if (len == 0 || buf[len - 1] != '\n') return -1;
    char *p = buf;
    for (int a = 1; a <= M; a++) {
        char *e;
        long v = strtol(p, &e, 10);
        if (e == p || v < -1000 || v > 1000) return -1;
        f[1][a] = (int)v;
        p = e;
    }
    while (*p == ' ' || *p == '\t' || *p == '\r') p++;
    return *p == '\n' ? 1 : -1;
}

/* independent final check before anything is written: rows 0, id, f_1..f_K rebuilt from f[][] as full arrays over Z_N;
 * each of the (K+2)(K+1)/2 row pairs must have N pairwise distinct differences mod N */
static int verify_dm(void) {
    static int D[MAXK + 2][MAXN];
    int rows = K + 2;
    for (int x = 0; x < N; x++) { D[0][x] = 0; D[1][x] = x; }
    for (int j = 1; j <= K; j++) { D[1 + j][0] = 0; for (int a = 1; a <= M; a++) D[1 + j][a] = f[j][a]; }
    for (int r = 0; r < rows; r++) for (int x = 0; x < N; x++)
        if (D[r][x] < 0 || D[r][x] >= N) { printf("c INTERNAL MISMATCH row %d column %d entry %d out of range\n", r, x, D[r][x]); return 0; }
    for (int r = 0; r < rows; r++) for (int s = r + 1; s < rows; s++) {
        uint64_t seen = 0;
        for (int x = 0; x < N; x++) {
            int d = (D[r][x] - D[s][x] + N) % N;
            if (seen >> d & 1ULL) { printf("c INTERNAL MISMATCH rows %d %d\n", r, s); return 0; }
            seen |= 1ULL << d;
        }
    }
    printf("c final DM check: %d x %d matrix 0, id, f_1..f_%d: all %d row pairs have %d distinct differences\n",
           rows, N, K, rows * (rows - 1) / 2, N);
    return 1;
}

int main(int argc, char **argv) {
    if (argc < 6 || argc > 8) { fprintf(stderr, "usage: cfr_perm_search_c21v1 N R SEED SECONDS OUTFILE [random|linear:c|f1file:PATH|fam:pres3Z|fam:lin9:c|fam:lin3] [symK:m1,m2,...]\n"); return 2; }
    N = atoi(argv[1]); R = atoi(argv[2]); K = R - 1; M = N - 1;
    rng_state = 0x9E3779B97F4A7C15ULL ^ ((uint64_t)strtoull(argv[3], 0, 10) * 0xBF58476D1CE4E5B9ULL);
    if (!rng_state) rng_state = 1;
    tlimit = atof(argv[4]);
    const char *outfile = argv[5];
    int linear_c = 0;
    FILE *f1fp = NULL;
    if (argc >= 7 && strncmp(argv[6], "linear:", 7) == 0) linear_c = atoi(argv[6] + 7);
    if (argc >= 7 && strcmp(argv[6], "fam:pres3Z") == 0) famkind = 1;
    if (argc >= 7 && strncmp(argv[6], "fam:lin9:", 9) == 0) { famkind = 2; famc = atoi(argv[6] + 9); }
    if (argc >= 7 && strcmp(argv[6], "fam:lin3") == 0) famkind = 3;
    if (famkind && N % 9 != 0 && famkind == 2) { fprintf(stderr, "lin9 needs 9 | N\n"); return 2; }
    if (argc >= 7 && strncmp(argv[6], "f1file:", 7) == 0) { f1fp = fopen(argv[6] + 7, "r"); if (!f1fp) { perror("f1file"); return 2; } }
    if (argc == 8 && strncmp(argv[7], "symK:", 5) == 0) {
        char *p = argv[7] + 5;
        while (*p && nsym < 64) { symmu[nsym++] = (int)strtol(p, &p, 10); if (*p == ',') p++; }
    }
    if (N % 2 == 0 || N > MAXN || N < 3 || K < 1 || K > MAXK || M > 30) { fprintf(stderr, "bad params\n"); return 2; }
    if ((long long)L2CAP < 1 || (long long)L2CAP > (1LL << 23) || (long long)(ADJ_BYTES) > (512LL << 20)) { fprintf(stderr, "bad params (memory caps above the defaults)\n"); return 2; }
    for (int v = 0; v < N; v++) clsv[v] = v;
    signal(SIGTERM, on_term); signal(SIGINT, on_term);
    t0 = now_s();
    printf("c cfr_perm_search_c21v1 N %d R %d M %d (full normalised permutations) seed %s limit %.0f f1mode %s symK %d L2cap %lld adjcap %lld\n",
           N, R, M, argv[3], tlimit, argc >= 7 ? argv[6] : "random", nsym, (long long)L2CAP, (long long)ADJCAP);
    fflush(stdout);
    while (!found && !timed_out) {
        if (linear_c) {
            if (stat_f1 > 0) break;
            for (int a = 1; a <= M; a++) f[1][a] = md(linear_c * a);
        } else if (f1fp) {
            int rd = read_f1_line(f1fp);
            if (rd == 0) break;
            cur_f1_index++;
            if (rd < 0) { printf("c f1file line %lld malformed (need exactly %d integers)\n", cur_f1_index, M); return 2; }
        } else {
            Lev *L = &levs[1];
            lev_init(L, 1); L->randomize = 1; L->mode = 1;
            run_level(L);
            if (timed_out) break;
            if (L->nsol == 0) { printf("c no f_1\n"); break; }
        }
        if (!f1_valid()) { printf("c f_1 #%lld is not a normalised orthomorphism of Z_%d\n", stat_f1 + 1, N); return 4; }
        if (f1fp && nsym > 0) {   /* verify f_1 is invariant under every listed multiplier */
            uint8_t x[MAXM]; for (int a = 1; a <= M; a++) x[a - 1] = (uint8_t)f[1][a];
            for (int s = 0; s < nsym; s++) {
                int mu = symmu[s];
                for (int a = 1; a <= M; a++) if (md(mu * full_of(x, a)) != full_of(x, mu * a)) { printf("c f_1 #%lld not invariant under %d\n", cur_f1_index, mu); return 4; }
            }
        }
        stat_f1++;
        long long l2b = stat_l2, trib = stat_tri;
        if (K == 1) { found = 1; break; }
        local_clique();
        if ((stat_f1 % 50) == 1 || found || linear_c || f1fp)
            printf("c f1 #%lld neighbours %lld L2edges %lld exhausted %d overflow %d | totals l2 %lld tri %lld deep %lld nodes %lld t %.1f\n",
                   stat_f1, stat_l2 - l2b, stat_tri - trib, (!found && !timed_out && !f1_overflow), f1_overflow, stat_l2, stat_tri, stat_deep, nodes, now_s() - t0);
        fflush(stdout);
    }
    printf("c final f1 %lld l2 %lld tri %lld deep %lld nodes %lld overflows %lld timed_out %d time %.2f\n",
           stat_f1, stat_l2, stat_tri, stat_deep, nodes, stat_overflow, timed_out, now_s() - t0);
    if (!found) { printf("s UNKNOWN\n"); return 0; }
    if (!verify_dm()) return 5;
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
        for (int a = 1; a <= M; a++) full[a] = f[j][a];
        for (int c = 0; c < N; c++) row[c] = -1;
        for (int s = 0; s < N; s++) row[full[s]] = s;
        for (int c = 0; c < N; c++) fprintf(o, c ? " %d" : "%d", row[c]);
        fprintf(o, "\n");
    }
    fclose(o);
    fflush(stdout);
    return 10;
}
