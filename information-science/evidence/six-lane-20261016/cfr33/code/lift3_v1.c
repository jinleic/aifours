/* lift3_v1.c -- p-adic (3-adic) lift engine for ODD CFR normal forms (lane cfr33/cfr27, worker InfoCFR27Lift).
 * README section 5.1(c).  Odd model: DM rows 0 (zero), 1 (id), f-rows 2..R (R = CFR rows); half-columns a = 1..M.
 * n = p q (q = n/p).  f_t(a) = rb_t(a) + q e_t(a), rb in 0..q-1, e in Z_p.  For a pair (t1,t2) and a nonzero q-class
 * rho the p half-columns with rb_t1 - rb_t2 = +-rho (mod q) get s(a) with s(rb_t1 - rb_t2) = rho + q kap (kap in {0,-1});
 * delta(a) = kap + s (e_t1 - e_t2) mod p must be a bijection onto Z_p; class 0 ((p-1)/2 half-columns) needs
 * delta = e_t1 - e_t2 nonzero with distinct +- classes.  Linear part: sum of delta over a nonzero class = 0 (mod p).
 * Lift = Gaussian elimination mod p + exhaustive DFS over the free variables with every class constraint checked as
 * soon as its variables are fixed; every full lift is rebuilt and re-verified pair by pair (exit 5 on mismatch).
 *
 * Usage:
 *   lift3_v1 liftfile N P R RAWFILE FREE           FREE = all | missing  (calibration on a cfr-raw-v1 file)
 *   lift3_v1 relift N P R SEED SECONDS OUTFILE F1MODE FREE DIRECT
 *        F1MODE: random | pres3Z | lin3 | all (all = every odd orthomorphism f_1, deterministic, small n only)
 *        FREE  : all (all f-row top digits free in the lift) | missing (only the new row free)
 *        DIRECT: 1 = also run the direct clique test (v7 triangle/edge test), 0 = relift path only
 * relift: f_1 per round; L2 = all odd f orthogonal to 0, id, f_1 (exact cover DFS); base = f_1 plus an (R-3)-clique of
 * L2 (R = 3: f_1 alone; R = 4: one vertex; R = 5: one edge); for every base the missing row's mod-q patterns with the
 * exact class profile are enumerated (exact DFS) and lifted.  Exit 10 + "s SATISFIABLE" + OUTFILE (O_EXCL, cfr-raw-v1:
 * identity row, then f_j^-1) on the first full solution; else "s UNKNOWN" (or "s EXHAUSTED-RESTRICTED" for F1MODE all
 * when every f_1 finished without cap/timeout).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <signal.h>
#include <time.h>
#include <fcntl.h>
#include <unistd.h>

#define MAXN 63
#define MAXM 31
#define MAXT 9          /* DM rows */
#define MAXV 128        /* lift unknowns */
#define MAXE 160        /* lift equations */

static int N, P, Q, M, R;
static int clsN[MAXN];
static volatile sig_atomic_t stop_flag = 0;
static double t0, tlimit = 1e18;
static uint64_t rng_state = 1;
static int timed_out = 0;

static uint64_t rnd(void) { uint64_t x = rng_state; x ^= x << 13; x ^= x >> 7; x ^= x << 17; rng_state = x; return x; }
static double now_s(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + ts.tv_nsec * 1e-9; }
static void on_term(int s) { (void)s; stop_flag = 1; }
static inline int md(int x, int m) { x %= m; return x < 0 ? x + m : x; }
static inline int clsQ(int u) { u = md(u, Q); return u <= Q - u ? u : Q - u; }
static int check_time(void) { if (stop_flag || now_s() - t0 > tlimit) timed_out = 1; return timed_out; }

/* ------------------------------------------------------------------ lift solver */
typedef struct {
    int nT;
    int rb[MAXT][MAXM + 1];
    int ek[MAXT][MAXM + 1];
    int fr[MAXT];
} LIn;
typedef struct { int a, s, kap; } Ent;
typedef struct { int t1, t2, rho, ne; Ent e[MAXM]; uint64_t deps; int level; } Cons;

static Cons cons[MAXT * MAXT * MAXM];
static int ncons;
static int varid[MAXT][MAXM + 1], nvar;
static int8_t A[MAXE][MAXV + 1];
static int neq, rank_, pivcol[MAXE], isfreecol[MAXV], freecols[MAXV], nfree, pivrow_of[MAXV];
static uint64_t vdeps[MAXV];
static int xfree[MAXV];
static long long lift_node_cap = 4000000000LL, lift_nodes;
static int lift_capped;
static const LIn *LI;
static long long st_calls, st_badprof, st_incons, st_cons, st_linsol, st_full, st_capped, st_dim[MAXV + 1];
static int (*lift_cb)(const int f[MAXT][MAXM + 1]);

static inline int inv_mod(int x) { for (int y = 1; y < P; y++) if ((x * y) % P == 1) return y; return 0; }

static int val_e(int t, int a) {
    if (!LI->fr[t]) return LI->ek[t][a];
    int v = varid[t][a];
    if (isfreecol[v]) return xfree[v];
    int r = pivrow_of[v];
    int s = A[r][nvar];
    for (int k = 0; k < nfree; k++) { int c = freecols[k]; if (A[r][c]) s -= A[r][c] * xfree[c]; }
    return md(s, P);
}
static int cons_ok(const Cons *C) {
    unsigned seen = 0;
    for (int k = 0; k < C->ne; k++) {
        int a = C->e[k].a;
        int d1 = val_e(C->t1, a) - val_e(C->t2, a);
        if (C->rho == 0) {
            int dl = md(d1, P);
            if (dl == 0) return 0;
            int pc = dl <= P - dl ? dl : P - dl;
            if (seen >> pc & 1u) return 0;
            seen |= 1u << pc;
        } else {
            int dl = md(C->e[k].kap + C->e[k].s * d1, P);
            if (seen >> dl & 1u) return 0;
            seen |= 1u << dl;
        }
    }
    return 1;
}
static int full_verify(int f[MAXT][MAXM + 1]) {
    for (int t = 0; t < LI->nT; t++) for (int a = 1; a <= M; a++) f[t][a] = (t == 0) ? 0 : LI->rb[t][a] + Q * val_e(t, a);
    for (int t1 = 0; t1 < LI->nT; t1++) for (int t2 = t1 + 1; t2 < LI->nT; t2++) {
        uint64_t seen = 0;
        for (int a = 1; a <= M; a++) {
            int c = clsN[md(f[t1][a] - f[t2][a], N)];
            if (c == 0 || (seen >> c & 1ULL)) return 0;
            seen |= 1ULL << c;
        }
    }
    return 1;
}
static int lift_stop;
static void lift_dfs(int L) {
    if (lift_stop) return;
    if (++lift_nodes > lift_node_cap) { lift_capped = 1; lift_stop = 1; return; }
    if ((lift_nodes & 0xFFFFF) == 0 && check_time()) { lift_stop = 1; return; }
    if (L == nfree) {
        int f[MAXT][MAXM + 1];
        st_linsol++;
        if (!full_verify(f)) { printf("c INTERNAL MISMATCH: constraints passed but full verify failed\n"); fflush(stdout); exit(5); }
        st_full++;
        if (lift_cb && lift_cb((const int (*)[MAXM + 1])f)) lift_stop = 1;
        return;
    }
    int c = freecols[L];
    for (int x = 0; x < P && !lift_stop; x++) {
        xfree[c] = x;
        int ok = 1;
        for (int k = 0; k < ncons && ok; k++) if (cons[k].level == L && !cons_ok(&cons[k])) ok = 0;
        if (ok) lift_dfs(L + 1);
    }
    xfree[c] = 0;
}
/* returns: -2 bad profile, -1 inconsistent, else number of full lifts found (callback may stop early) */
static long long lift_solve(const LIn *in) {
    LI = in; st_calls++;
    ncons = 0; nvar = 0;
    for (int t = 0; t < in->nT; t++) for (int a = 1; a <= M; a++) varid[t][a] = in->fr[t] ? nvar++ : -1;
    for (int t1 = 0; t1 < in->nT; t1++) for (int t2 = t1 + 1; t2 < in->nT; t2++) {
        if (t1 == 0 && t2 == 1) continue;
        int base = ncons;
        for (int rho = 0; rho <= (Q - 1) / 2; rho++) { cons[base + rho].t1 = t1; cons[base + rho].t2 = t2; cons[base + rho].rho = rho; cons[base + rho].ne = 0; }
        for (int a = 1; a <= M; a++) {
            int w = in->rb[t1][a] - in->rb[t2][a];
            int rho = clsQ(w);
            Cons *C = &cons[base + rho];
            if (C->ne >= MAXM) { st_badprof++; return -2; }
            Ent *E = &C->e[C->ne++];
            E->a = a; E->s = 1; E->kap = 0;
            if (rho) {
                E->s = (md(w, Q) == rho) ? 1 : -1;
                int sw = E->s * w;
                if ((sw - rho) % Q != 0) { printf("c internal kappa error\n"); exit(5); }
                E->kap = (sw - rho) / Q;
            }
        }
        for (int rho = 0; rho <= (Q - 1) / 2; rho++) if (cons[base + rho].ne != (rho ? P : (P - 1) / 2)) { st_badprof++; return -2; }
        ncons = base + (Q - 1) / 2 + 1;
    }
    /* equations */
    neq = 0;
    for (int k = 0; k < ncons; k++) {
        Cons *C = &cons[k];
        if (C->rho == 0) continue;
        int8_t *row = A[neq];
        memset(row, 0, (size_t)nvar + 1);
        int rhs = 0, any = 0;
        for (int i = 0; i < C->ne; i++) {
            int a = C->e[i].a, s = C->e[i].s;
            rhs -= C->e[i].kap;
            if (in->fr[C->t1]) { int v = varid[C->t1][a]; row[v] = (int8_t)md(row[v] + s, P); any = 1; } else rhs -= s * in->ek[C->t1][a];
            if (in->fr[C->t2]) { int v = varid[C->t2][a]; row[v] = (int8_t)md(row[v] - s, P); any = 1; } else rhs += s * in->ek[C->t2][a];
        }
        row[nvar] = (int8_t)md(rhs, P);
        if (!any) { if (row[nvar] != 0) { st_incons++; return -1; } continue; }
        neq++;
    }
    /* RREF mod P */
    rank_ = 0;
    for (int v = 0; v < nvar; v++) { isfreecol[v] = 1; pivrow_of[v] = -1; }
    for (int c = 0; c < nvar && rank_ < neq; c++) {
        int pr = -1;
        for (int r = rank_; r < neq; r++) if (A[r][c]) { pr = r; break; }
        if (pr < 0) continue;
        if (pr != rank_) for (int j = 0; j <= nvar; j++) { int8_t tmp = A[pr][j]; A[pr][j] = A[rank_][j]; A[rank_][j] = tmp; }
        int iv = inv_mod(A[rank_][c]);
        for (int j = 0; j <= nvar; j++) A[rank_][j] = (int8_t)md(A[rank_][j] * iv, P);
        for (int r = 0; r < neq; r++) if (r != rank_ && A[r][c]) {
            int f = A[r][c];
            for (int j = 0; j <= nvar; j++) A[r][j] = (int8_t)md(A[r][j] - f * A[rank_][j], P);
        }
        pivcol[rank_] = c; isfreecol[c] = 0; pivrow_of[c] = rank_;
        rank_++;
    }
    for (int r = rank_; r < neq; r++) if (A[r][nvar]) { st_incons++; return -1; }
    st_cons++;
    nfree = 0;
    for (int v = 0; v < nvar; v++) if (isfreecol[v]) freecols[nfree++] = v;
    st_dim[nfree]++;
    if (nfree > 63) { printf("c lift dim %d > 63 unsupported\n", nfree); st_capped++; return 0; }
    for (int v = 0; v < nvar; v++) {
        vdeps[v] = 0;
        if (isfreecol[v]) { for (int k = 0; k < nfree; k++) if (freecols[k] == v) vdeps[v] = 1ULL << k; }
        else { int r = pivrow_of[v]; for (int k = 0; k < nfree; k++) if (A[r][freecols[k]]) vdeps[v] |= 1ULL << k; }
    }
    for (int k = 0; k < ncons; k++) {
        Cons *C = &cons[k];
        uint64_t d = 0;
        for (int i = 0; i < C->ne; i++) {
            int a = C->e[i].a;
            if (in->fr[C->t1]) d |= vdeps[varid[C->t1][a]];
            if (in->fr[C->t2]) d |= vdeps[varid[C->t2][a]];
        }
        C->deps = d;
        C->level = d ? 63 - __builtin_clzll(d) : -1;
    }
    for (int k = 0; k < nfree; k++) xfree[freecols[k]] = 0;
    for (int k = 0; k < ncons; k++) if (cons[k].level == -1 && !cons_ok(&cons[k])) return 0;
    long long before = st_full;
    lift_nodes = 0; lift_capped = 0; lift_stop = 0;
    lift_dfs(0);
    if (lift_capped) st_capped++;
    return st_full - before;
}

/* ------------------------------------------------------------------ odd maps */
static int fullv(const int *x, int t) { t = md(t, N); if (t == 0) return 0; if (t <= M) return x[t]; return md(-x[N - t], N); }
static int is_odd_orth_set(int nT, int f[MAXT][MAXM + 1]) {
    for (int t1 = 0; t1 < nT; t1++) for (int t2 = t1 + 1; t2 < nT; t2++) {
        uint64_t seen = 0;
        for (int a = 1; a <= M; a++) { int c = clsN[md(f[t1][a] - f[t2][a], N)]; if (c == 0 || (seen >> c & 1ULL)) return 0; seen |= 1ULL << c; }
    }
    return 1;
}
static int write_cfr(const char *path, int nT, int f[MAXT][MAXM + 1]) {
    int fd = open(path, O_WRONLY | O_CREAT | O_EXCL, 0444);
    if (fd < 0) { perror("open outfile"); return 0; }
    FILE *o = fdopen(fd, "w");
    for (int c = 0; c < N; c++) fprintf(o, c ? " %d" : "%d", c);
    fprintf(o, "\n");
    for (int t = 2; t < nT; t++) {
        int full[MAXN], row[MAXN];
        for (int s = 0; s < N; s++) full[s] = fullv(f[t], s);
        for (int c = 0; c < N; c++) row[c] = -1;
        for (int s = 0; s < N; s++) row[full[s]] = s;
        for (int c = 0; c < N; c++) fprintf(o, c ? " %d" : "%d", row[c]);
        fprintf(o, "\n");
    }
    fclose(o);
    return 1;
}

/* ------------------------------------------------------------------ missing-row pattern enumeration */
static int pe_nT, pe_rb[MAXT][MAXM + 1], pe_cnt[MAXT][MAXM + 1], pe_x[MAXM + 1], pe_as[MAXM + 1];
static long long pe_nodes, pe_count;
static int pe_stop;
static int (*pe_cb)(const int *x);
static inline int tgt(int c) { return c == 0 ? (P - 1) / 2 : P; }
static inline int pe_feas(int a, int v) {
    for (int t = 0; t < pe_nT; t++) { int c = clsQ(v - pe_rb[t][a]); if (pe_cnt[t][c] >= tgt(c)) return 0; }
    return 1;
}
static void pe_dfs(int depth) {
    if (pe_stop) return;
    if ((++pe_nodes & 0xFFFFF) == 0 && check_time()) { pe_stop = 1; return; }
    if (depth == M) { pe_count++; if (pe_cb && pe_cb(pe_x)) pe_stop = 1; return; }
    int besta = -1, bestn = 1 << 30;
    unsigned feas[MAXM + 1];
    for (int a = 1; a <= M; a++) {
        if (pe_as[a]) continue;
        unsigned m = 0; int n = 0;
        for (int v = 0; v < Q; v++) if (pe_feas(a, v)) { m |= 1u << v; n++; }
        if (n == 0) return;
        feas[a] = m;
        if (n < bestn) { bestn = n; besta = a; }
    }
    /* lookahead: every (t, c) deficit must be coverable by distinct remaining half-columns */
    for (int t = 0; t < pe_nT; t++) for (int c = 0; c <= (Q - 1) / 2; c++) {
        int def = tgt(c) - pe_cnt[t][c];
        if (def <= 0) continue;
        int can = 0;
        for (int a = 1; a <= M && can < def; a++) {
            if (pe_as[a]) continue;
            unsigned m = feas[a];
            while (m) { int v = __builtin_ctz(m); m &= m - 1; if (clsQ(v - pe_rb[t][a]) == c) { can++; break; } }
        }
        if (can < def) return;
    }
    unsigned m = feas[besta];
    while (m && !pe_stop) {
        int v = __builtin_ctz(m); m &= m - 1;
        pe_as[besta] = 1; pe_x[besta] = v;
        for (int t = 0; t < pe_nT; t++) pe_cnt[t][clsQ(v - pe_rb[t][besta])]++;
        pe_dfs(depth + 1);
        for (int t = 0; t < pe_nT; t++) pe_cnt[t][clsQ(v - pe_rb[t][besta])]--;
        pe_as[besta] = 0;
    }
}
static long long enum_patterns(int nT, int rb[MAXT][MAXM + 1], int (*cb)(const int *x)) {
    pe_nT = nT; memcpy(pe_rb, rb, sizeof pe_rb); memset(pe_cnt, 0, sizeof pe_cnt); memset(pe_as, 0, sizeof pe_as);
    pe_nodes = 0; pe_count = 0; pe_stop = 0; pe_cb = cb;
    pe_dfs(0);
    return pe_count;
}

/* ------------------------------------------------------------------ relift of a base */
static int base_nT;                     /* DM rows of the base (0, id, f-rows) */
static int base_f[MAXT][MAXM + 1];
static int relift_free_all = 1;
static long long st_bases, st_patterns, st_direct_hits;
static int found = 0;
static int found_f[MAXT][MAXM + 1], found_nT;
static int on_full_solution(const int f[MAXT][MAXM + 1]) {
    for (int t = 0; t < LI->nT; t++) for (int a = 1; a <= M; a++) found_f[t][a] = f[t][a];
    found_nT = LI->nT; found = 1;
    return 1;
}
static int on_pattern(const int *x) {
    LIn in;
    memset(&in, 0, sizeof in);
    in.nT = base_nT + 1;
    for (int t = 0; t < base_nT; t++) for (int a = 1; a <= M; a++) {
        in.rb[t][a] = md(base_f[t][a], Q);
        in.ek[t][a] = base_f[t][a] / Q;
    }
    for (int a = 1; a <= M; a++) { in.rb[base_nT][a] = x[a]; in.ek[base_nT][a] = 0; }
    for (int t = 0; t < in.nT; t++) in.fr[t] = (t >= 2) && (relift_free_all || t == base_nT);
    st_patterns++;
    lift_cb = on_full_solution;
    lift_solve(&in);
    return found || timed_out;
}
static void relift_base(void) {
    int rb[MAXT][MAXM + 1];
    for (int t = 0; t < base_nT; t++) for (int a = 1; a <= M; a++) rb[t][a] = md(base_f[t][a], Q);
    st_bases++;
    enum_patterns(base_nT, rb, on_pattern);
}

/* ------------------------------------------------------------------ exact-cover DFS for odd maps orthogonal to given maps */
typedef struct {
    int nf;
    int g[MAXT][MAXM + 1];                 /* base maps (odd), g[0] = zero, g[1] = id, ... */
    uint8_t cl[MAXM + 1][MAXN][MAXT];
    uint64_t kill[MAXT][MAXM + 1][MAXM + 1];
    uint64_t cand0[MAXM + 1];
    int val[MAXM + 1], first[MAXM + 1];
    int randomize, first_only, stop;
    long long nsol, cap, cnt;
    uint8_t *store;
} XC;
static long long xc_nodes;
static void xc_init(XC *X, int nf, uint64_t *famkeep) {
    X->nf = nf; X->stop = 0; X->nsol = 0; X->cnt = 0;
    memset(X->kill, 0, sizeof X->kill);
    for (int a = 1; a <= M; a++) {
        uint64_t c0 = 0;
        for (int v = 1; v < N; v++) {
            int ok = 1;
            for (int f = 0; f < nf; f++) { X->cl[a][v][f] = (uint8_t)clsN[md(v - X->g[f][a], N)]; if (!X->cl[a][v][f]) ok = 0; }
            if (famkeep && !(famkeep[a] >> v & 1ULL)) ok = 0;
            if (ok) { c0 |= 1ULL << v; for (int f = 0; f < nf; f++) X->kill[f][a][X->cl[a][v][f]] |= 1ULL << v; }
        }
        X->cand0[a] = c0; X->val[a] = 0;
    }
}
static void xc_dfs(XC *X, uint64_t *cand, uint32_t *used, uint32_t assigned, int depth) {
    if (X->stop) return;
    if ((++xc_nodes & 1023) == 0 && check_time()) { X->stop = 1; return; }
    if (depth == M) {
        X->nsol++;
        if (X->first_only) { for (int a = 1; a <= M; a++) X->first[a] = X->val[a]; X->stop = 1; return; }
        if (X->cnt >= X->cap) { X->stop = 1; return; }
        for (int a = 1; a <= M; a++) X->store[X->cnt * M + (a - 1)] = (uint8_t)X->val[a];
        X->cnt++;
        return;
    }
    int bestkind = 0, besta = -1, bestf = -1, bestc = -1, bestcount = 1 << 30;
    for (int a = 1; a <= M; a++) {
        if (assigned >> a & 1u) continue;
        int c = __builtin_popcountll(cand[a]);
        if (c == 0) return;
        if (c < bestcount || (c == bestcount && X->randomize && (rnd() & 1))) { bestcount = c; besta = a; bestkind = 0; }
    }
    for (int f = 0; f < X->nf; f++) {
        uint32_t freec = (((1u << (M + 1)) - 2u) & ~used[f]);
        while (freec) {
            int c = __builtin_ctz(freec); freec &= freec - 1;
            int cnt = 0;
            for (int a = 1; a <= M && cnt < bestcount; a++) { if (assigned >> a & 1u) continue; cnt += __builtin_popcountll(cand[a] & X->kill[f][a][c]); }
            if (cnt == 0) return;
            if (cnt < bestcount) { bestcount = cnt; bestkind = 1; bestf = f; bestc = c; }
        }
    }
    int oa[MAXM * MAXN], ov[MAXM * MAXN], no = 0;
    if (bestkind == 0) { uint64_t m = cand[besta]; while (m) { int v = __builtin_ctzll(m); m &= m - 1; oa[no] = besta; ov[no] = v; no++; } }
    else for (int a = 1; a <= M; a++) { if (assigned >> a & 1u) continue; uint64_t m = cand[a] & X->kill[bestf][a][bestc]; while (m) { int v = __builtin_ctzll(m); m &= m - 1; oa[no] = a; ov[no] = v; no++; } }
    if (X->randomize) for (int i = no - 1; i > 0; i--) { int k = (int)(rnd() % (uint64_t)(i + 1)); int t = oa[i]; oa[i] = oa[k]; oa[k] = t; t = ov[i]; ov[i] = ov[k]; ov[k] = t; }
    uint64_t nc[MAXM + 1]; uint32_t nu[MAXT];
    for (int i = 0; i < no && !X->stop; i++) {
        int a = oa[i], v = ov[i];
        for (int f = 0; f < X->nf; f++) nu[f] = used[f] | (1u << X->cl[a][v][f]);
        for (int b = 1; b <= M; b++) {
            if ((assigned >> b & 1u) || b == a) { nc[b] = 0; continue; }
            uint64_t x = cand[b];
            for (int f = 0; f < X->nf; f++) x &= ~X->kill[f][b][X->cl[a][v][f]];
            nc[b] = x;
        }
        nc[a] = 0;
        X->val[a] = v;
        xc_dfs(X, nc, nu, assigned | (1u << a), depth + 1);
        X->val[a] = 0;
    }
}
static void xc_run(XC *X) {
    uint64_t cand[MAXM + 1]; uint32_t used[MAXT];
    memcpy(cand, X->cand0, sizeof cand);
    memset(used, 0, sizeof used);
    xc_dfs(X, cand, used, 0u, 0);
}
static int orth(const uint8_t *g, const uint8_t *h) {
    uint64_t m = 0;
    for (int a = 0; a < M; a++) { int c = clsN[md((int)g[a] - (int)h[a], N)]; if (c == 0 || (m >> c & 1ULL)) return 0; m |= 1ULL << c; }
    return 1;
}

/* ------------------------------------------------------------------ main */
static void print_stats(const char *tag) {
    printf("c %s t %.1f bases %lld patterns %lld liftcalls %lld badprof %lld incons %lld cons %lld linsol %lld full %lld capped %lld direct_hits %lld xcnodes %lld\n",
           tag, now_s() - t0, st_bases, st_patterns, st_calls, st_badprof, st_incons, st_cons, st_linsol, st_full, st_capped, st_direct_hits, xc_nodes);
    printf("c %s dimhist", tag);
    for (int d = 0; d <= MAXV; d++) if (st_dim[d]) printf(" %d:%lld", d, st_dim[d]);
    printf("\n");
    fflush(stdout);
}
static int setup(int n, int p) {
    N = n; P = p;
    if (N % P || N > MAXN || N % 2 == 0) return 0;
    Q = N / P; M = (N - 1) / 2;
    if (Q % 2 == 0 || M > MAXM) return 0;
    for (int v = 0; v < N; v++) clsN[v] = v <= N - v ? v : N - v;
    return 1;
}
static int read_raw(const char *path, int r, int f[MAXT][MAXM + 1]) {
    FILE *fp = fopen(path, "r");
    if (!fp) { perror("raw"); return 0; }
    int rows[MAXT][MAXN];
    for (int i = 0; i < r; i++) for (int c = 0; c < N; c++) if (fscanf(fp, "%d", &rows[i][c]) != 1) { fclose(fp); return 0; }
    fclose(fp);
    int pos[MAXT][MAXN];
    for (int i = 0; i < r; i++) for (int c = 0; c < N; c++) pos[i][rows[i][c]] = c;
    /* normal form: f_i = p_i o p_0^-1 - p_i(p_0^-1(0)) */
    int p0inv[MAXN];
    for (int s = 0; s < N; s++) p0inv[pos[0][s]] = s;
    int fullf[MAXT][MAXN];
    for (int i = 0; i < r; i++) { int off = pos[i][p0inv[0]]; for (int x = 0; x < N; x++) fullf[i][x] = md(pos[i][p0inv[x]] - off, N); }
    for (int i = 0; i < r; i++) for (int x = 1; x < N; x++) if (fullf[i][N - x] != md(-fullf[i][x], N)) { printf("c row %d of %s is not odd in normal form\n", i, path); return 0; }
    for (int a = 1; a <= M; a++) f[0][a] = 0;
    for (int i = 0; i < r; i++) for (int a = 1; a <= M; a++) f[i + 1][a] = fullf[i][a];
    return 1;
}

/* liftfile mode */
static int lf_nT, lf_orig[MAXT][MAXM + 1], lf_drop, lf_hit_orig;
static long long lf_sols;
static int lf_cb(const int f[MAXT][MAXM + 1]) {
    lf_sols++;
    int same = 1;
    for (int t = 0; t < lf_nT && same; t++) {
        int ot = t;
        for (int a = 1; a <= M; a++) {
            int want = lf_orig[ot][a];
            int have;
            if (lf_drop < 0) have = f[t][a];
            else {
                /* LI rows: base rows (orig without lf_drop) then missing row last */
                int idx = t < lf_drop ? t : (t == lf_drop ? lf_nT - 1 : t - 1);
                have = f[idx][a];
            }
            if (have != want) { same = 0; break; }
        }
    }
    if (same) lf_hit_orig = 1;
    return 0;
}
static int lfp_free_all;
static int lf_pattern(const int *x) {
    LIn in; memset(&in, 0, sizeof in);
    in.nT = lf_nT;
    int k = 0;
    for (int t = 0; t < lf_nT; t++) {
        if (t == lf_drop) continue;
        for (int a = 1; a <= M; a++) { in.rb[k][a] = md(lf_orig[t][a], Q); in.ek[k][a] = lf_orig[t][a] / Q; }
        k++;
    }
    for (int a = 1; a <= M; a++) { in.rb[lf_nT - 1][a] = x[a]; in.ek[lf_nT - 1][a] = 0; }
    for (int t = 0; t < in.nT; t++) in.fr[t] = (t >= 2) && (lfp_free_all || t == lf_nT - 1);
    st_patterns++;
    lift_cb = lf_cb;
    lift_solve(&in);
    return timed_out;
}
static int mode_liftfile(int argc, char **argv) {
    if (argc != 7) return 2;
    if (!setup(atoi(argv[2]), atoi(argv[3]))) { printf("c bad N/P\n"); return 2; }
    R = atoi(argv[4]);
    const char *path = argv[5];
    int free_all = strcmp(argv[6], "all") == 0;
    lf_nT = R + 1;
    if (lf_nT > MAXT) return 2;
    if (!read_raw(path, R, lf_orig)) return 3;
    printf("c liftfile N %d P %d Q %d R %d file %s free %s\n", N, P, Q, R, path, free_all ? "all" : "missing");
    if (!is_odd_orth_set(lf_nT, lf_orig)) { printf("c input is not an odd DM normal form\n"); return 3; }
    printf("c input verified as odd DM normal form with %d rows\n", lf_nT);
    /* (i) lift of the full pattern (all f-row top digits free, or only the last f-row free) */
    {
        LIn in; memset(&in, 0, sizeof in);
        in.nT = lf_nT;
        for (int t = 0; t < lf_nT; t++) for (int a = 1; a <= M; a++) { in.rb[t][a] = md(lf_orig[t][a], Q); in.ek[t][a] = lf_orig[t][a] / Q; }
        for (int t = 0; t < lf_nT; t++) in.fr[t] = (t >= 2) && (free_all || t == lf_nT - 1);
        lf_drop = -1; lf_sols = 0; lf_hit_orig = 0;
        lift_cb = lf_cb;
        long long r = lift_solve(&in);
        printf("c LIFT-FULL result %lld rank %d nvar %d dim %d lifts %lld original_found %d capped %d nodes %lld\n",
               r, rank_, nvar, nfree, lf_sols, lf_hit_orig, lift_capped, lift_nodes);
    }
    /* (ii) drop-one relift for every f-row */
    int allok = 1;
    for (int j = 2; j < lf_nT; j++) {
        int rb[MAXT][MAXM + 1]; int k = 0;
        for (int t = 0; t < lf_nT; t++) { if (t == j) continue; for (int a = 1; a <= M; a++) rb[k][a] = md(lf_orig[t][a], Q); k++; }
        lf_drop = j; lf_sols = 0; lf_hit_orig = 0; lfp_free_all = free_all;
        long long before_cap = st_capped;
        double ts = now_s();
        long long np = enum_patterns(lf_nT - 1, rb, lf_pattern);
        printf("c DROP-ONE row %d patterns %lld pe_nodes %lld lifts %lld original_found %d capped_calls %lld time %.2f\n",
               j, np, pe_nodes, lf_sols, lf_hit_orig, st_capped - before_cap, now_s() - ts);
        if (!lf_hit_orig) allok = 0;
    }
    print_stats("liftfile");
    printf("s CALIB %s\n", allok ? "ALL-DROP-ONE-RECOVERED" : "SOME-NOT-RECOVERED");
    fflush(stdout);
    return allok ? 0 : 1;
}

/* relift mode */
static XC xl1, xl2;
static int *adjoff = NULL, *adj = NULL; static long long adjcap = 0;
static int mode_relift(int argc, char **argv) {
    if (argc != 11) return 2;
    if (!setup(atoi(argv[2]), atoi(argv[3]))) { printf("c bad N/P\n"); return 2; }
    R = atoi(argv[4]);
    rng_state = 0x9E3779B97F4A7C15ULL ^ ((uint64_t)strtoull(argv[5], 0, 10) * 0xBF58476D1CE4E5B9ULL);
    if (!rng_state) rng_state = 1;
    tlimit = atof(argv[6]);
    const char *outfile = argv[7], *fam = argv[8];
    relift_free_all = strcmp(argv[9], "all") == 0;
    int direct = atoi(argv[10]);
    if (R < 3 || R + 1 > MAXT) return 2;
    int famkind = 0;
    if (!strcmp(fam, "random")) famkind = 0;
    else if (!strcmp(fam, "pres3Z")) famkind = 1;
    else if (!strcmp(fam, "lin3")) famkind = 2;
    else if (!strcmp(fam, "all")) famkind = 9;
    else { printf("c bad family\n"); return 2; }
    printf("c lift3_v1 relift N %d P %d Q %d R %d seed %s limit %.0f family %s free %s direct %d\n", N, P, Q, R, argv[5], tlimit, fam, relift_free_all ? "all" : "missing", direct);
    fflush(stdout);
    uint64_t keep[MAXM + 1];
    for (int a = 1; a <= M; a++) {
        keep[a] = 0;
        for (int v = 1; v < N; v++) {
            int ok = 1;
            if (famkind == 1) ok = ((a % 3 == 0) == (v % 3 == 0));
            if (famkind == 2) ok = (md(v + a, 3) == 0);
            if (ok) keep[a] |= 1ULL << v;
        }
    }
    /* all-f_1 list for famkind 9 */
    long long nf1all = 0, f1idx = 0;
    if (famkind == 9) {
        xl1.cap = 1LL << 24; xl1.store = malloc((size_t)xl1.cap * M);
        for (int a = 1; a <= M; a++) { xl1.g[0][a] = 0; xl1.g[1][a] = a; }
        xc_init(&xl1, 2, NULL); xl1.randomize = 0; xl1.first_only = 0;
        xc_run(&xl1);
        nf1all = xl1.cnt;
        printf("c all odd orthomorphisms f_1: %lld (cap hit %d)\n", nf1all, xl1.cnt >= xl1.cap);
        if (xl1.cnt >= xl1.cap || timed_out) { printf("s UNKNOWN\n"); return 0; }
    }
    xl2.cap = 1LL << 23; xl2.store = malloc((size_t)xl2.cap * M);
    long long st_f1 = 0, st_l2 = 0, st_edges = 0, st_overflow = 0;
    double last = now_s();
    int f1[MAXM + 1];
    while (!found && !timed_out) {
        if (famkind == 9) {
            if (f1idx >= nf1all) break;
            for (int a = 1; a <= M; a++) f1[a] = xl1.store[f1idx * M + (a - 1)];
            f1idx++;
        } else {
            for (int a = 1; a <= M; a++) { xl1.g[0][a] = 0; xl1.g[1][a] = a; }
            xc_init(&xl1, 2, famkind ? keep : NULL); xl1.randomize = 1; xl1.first_only = 1;
            xc_run(&xl1);
            if (timed_out) break;
            if (xl1.nsol == 0) { printf("c no f_1 in family\n"); break; }
            for (int a = 1; a <= M; a++) f1[a] = xl1.first[a];
        }
        st_f1++;
        /* L2 */
        for (int a = 1; a <= M; a++) { xl2.g[0][a] = 0; xl2.g[1][a] = a; xl2.g[2][a] = f1[a]; }
        xc_init(&xl2, 3, NULL); xl2.randomize = 0; xl2.first_only = 0;
        xc_run(&xl2);
        if (timed_out) break;
        if (xl2.cnt >= xl2.cap) st_overflow++;
        long long n2 = xl2.cnt; st_l2 += n2;
        /* base rows: 0, id, f_1 */
        for (int a = 1; a <= M; a++) { base_f[0][a] = 0; base_f[1][a] = a; base_f[2][a] = f1[a]; }
        if (R == 3) {
            if (direct && n2 > 0) {
                st_direct_hits++;
                for (int a = 1; a <= M; a++) { found_f[0][a] = 0; found_f[1][a] = a; found_f[2][a] = f1[a]; found_f[3][a] = xl2.store[a - 1]; }
                found_nT = 4; found = 1; break;
            }
            base_nT = 3;
            relift_base();
        } else {
            /* adjacency inside L2 (upper triangle, sorted) */
            long long edges = 0;
            if (adjoff) free(adjoff);
            adjoff = malloc(sizeof(int) * (size_t)(n2 + 1));
            if (!adj) { adjcap = 1 << 20; adj = malloc(sizeof(int) * (size_t)adjcap); }
            for (long long u = 0; u < n2; u++) {
                adjoff[u] = (int)edges;
                const uint8_t *gu = xl2.store + u * M;
                for (long long v = u + 1; v < n2; v++) if (orth(gu, xl2.store + v * M)) {
                    if (edges >= adjcap) { adjcap *= 2; adj = realloc(adj, sizeof(int) * (size_t)adjcap); }
                    adj[edges++] = (int)v;
                }
                if ((u & 255) == 0 && check_time()) break;
            }
            if (timed_out) break;
            adjoff[n2] = (int)edges;
            st_edges += edges;
            if (R == 4) {
                for (long long u = 0; u < n2 && !found && !timed_out; u++) {
                    if (direct && adjoff[u + 1] > adjoff[u]) {
                        int v = adj[adjoff[u]];
                        st_direct_hits++;
                        for (int a = 1; a <= M; a++) { found_f[0][a] = 0; found_f[1][a] = a; found_f[2][a] = f1[a]; found_f[3][a] = xl2.store[u * M + a - 1]; found_f[4][a] = xl2.store[(long long)v * M + a - 1]; }
                        found_nT = 5; found = 1; break;
                    }
                    for (int a = 1; a <= M; a++) base_f[3][a] = xl2.store[u * M + a - 1];
                    base_nT = 4;
                    relift_base();
                }
            } else if (R == 5) {
                for (long long u = 0; u < n2 && !found && !timed_out; u++) {
                    for (int e = adjoff[u]; e < adjoff[u + 1] && !found && !timed_out; e++) {
                        int v = adj[e];
                        if (direct) {
                            /* common neighbour w > v of u and v (triangle u < v < w) */
                            int p = adjoff[u], q = adjoff[u + 1], r2 = adjoff[v], s2 = adjoff[v + 1];
                            while (p < q && r2 < s2) {
                                if (adj[p] == adj[r2]) {
                                    int w = adj[p];
                                    st_direct_hits++;
                                    for (int a = 1; a <= M; a++) { found_f[0][a] = 0; found_f[1][a] = a; found_f[2][a] = f1[a]; found_f[3][a] = xl2.store[u * M + a - 1]; found_f[4][a] = xl2.store[(long long)v * M + a - 1]; found_f[5][a] = xl2.store[(long long)w * M + a - 1]; }
                                    found_nT = 6; found = 1; break;
                                }
                                if (adj[p] < adj[r2]) p++; else r2++;
                            }
                            if (found) break;
                        }
                        for (int a = 1; a <= M; a++) { base_f[3][a] = xl2.store[u * M + a - 1]; base_f[4][a] = xl2.store[(long long)v * M + a - 1]; }
                        base_nT = 5;
                        relift_base();
                    }
                }
            } else { printf("c R > 5 not supported in relift\n"); return 2; }
        }
        if (now_s() - last > 60 || found) {
            last = now_s();
            printf("c progress f1 %lld l2 %lld edges %lld overflow %lld\n", st_f1, st_l2, st_edges, st_overflow);
            print_stats("progress");
        }
    }
    printf("c final f1 %lld l2 %lld edges %lld overflow %lld timed_out %d\n", st_f1, st_l2, st_edges, st_overflow, timed_out);
    print_stats("final");
    if (found) {
        if (!is_odd_orth_set(found_nT, found_f)) { printf("c INTERNAL: found set fails verification\n"); return 5; }
        printf("s SATISFIABLE\n");
        for (int t = 2; t < found_nT; t++) { printf("v f%d", t - 1); for (int a = 1; a <= M; a++) printf(" %d", found_f[t][a]); printf("\n"); }
        fflush(stdout);
        if (!write_cfr(outfile, found_nT, found_f)) return 3;
        return 10;
    }
    if (famkind == 9 && !timed_out && st_overflow == 0 && st_capped == 0) printf("s EXHAUSTED-RESTRICTED (every f_1 of the family processed)\n");
    else printf("s UNKNOWN\n");
    return 0;
}

int main(int argc, char **argv) {
    signal(SIGTERM, on_term); signal(SIGINT, on_term);
    t0 = now_s();
    setvbuf(stdout, NULL, _IOLBF, 0);
    if (argc >= 2 && !strcmp(argv[1], "liftfile")) return mode_liftfile(argc, argv);
    if (argc >= 2 && !strcmp(argv[1], "relift")) return mode_relift(argc, argv);
    fprintf(stderr, "usage: see header\n");
    return 2;
}
