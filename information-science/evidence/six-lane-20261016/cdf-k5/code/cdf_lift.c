/* cdf_lift.c -- cyclic (3p,5,1) difference families by projection to Z_p and Z_3-labelling (p prime > 3).
 *
 * Z_{3p} = Z_3 x Z_p (CRT).  A (3p,5,1)-CDF with n = (3p-1)/20 blocks projects to n "projected blocks" in Z_p:
 * n-1 blocks of 5 distinct points and exactly one block {x,x,a,b,c} with a repeated point (it carries the unique
 * pair whose difference is (+-1,0)), such that every class +-y of Z_p (y != 0) occurs exactly 3 times among the
 * nonzero projected in-block differences.  Conversely, given such a projection, labels L in Z_3 on the points
 * (the two copies of x get different labels) lift it to a CDF iff for every class y the three occurrences carry
 * pairwise distinct oriented label differences (they then hit the classes (0,y),(1,y),(2,y) once each).
 * This is an exact reformulation, not a restriction.
 *
 * Phase 1: tabu local search for a projected family (cost = sum_c max(0, cnt_c - 3)).
 * Phase 2: exhaustive DFS over the labels (block-translation normalised) for that projection.
 * On failure: perturb the projected family (pert random element moves) and return to phase 1.
 *
 * Usage: cdf_lift v seed seconds outprefix [pert]
 * Exit 0 found (outprefix.sol, strict certificate), 3 time limit.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define K 5
#define MAXN 64

static int v, p, P2, n;               /* P2 = (p-1)/2 classes in Z_p */
static int x[MAXN][K];                /* projected points; block 0 is degenerate: x[0][1] == x[0][0] */
static int *cls, *cnt;
static int cost;
static long long tabu_until[MAXN][K][1024];
static uint64_t rng;
static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int rndint(int m) { return (int)(rnd() % (uint64_t)m); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static inline int mp(int a) { a %= p; return a < 0 ? a + p : a; }

/* pairs of block b: all (i<j) except the degenerate pair (0,1) of block 0 */
static inline int pair_skip(int b, int i, int j) { return b == 0 && i == 0 && j == 1; }

static int block_cost_apply(int b, int sign) {
    int d = 0;
    for (int i = 0; i < K; i++) for (int j = i + 1; j < K; j++) {
        if (pair_skip(b, i, j)) continue;
        int c = cls[mp(x[b][i] - x[b][j])];
        if (c == 0) { d += 1000; continue; }     /* forbidden zero difference */
        if (sign > 0) { if (cnt[c] >= 3) d++; cnt[c]++; }
        else { cnt[c]--; if (cnt[c] >= 3) d--; }
    }
    return d;
}
/* validity of block point pattern: block 0 has x0==x1 and x0,x2,x3,x4 distinct; others 5 distinct */
static int block_ok(int b) {
    for (int i = 0; i < K; i++) for (int j = i + 1; j < K; j++) {
        if (pair_skip(b, i, j)) continue;
        if (x[b][i] == x[b][j]) return 0;
    }
    return b != 0 || x[0][0] == x[0][1];
}
static void full_cost(void) {
    memset(cnt, 0, sizeof(int) * (P2 + 1));
    cost = 0;
    for (int b = 0; b < n; b++) cost += block_cost_apply(b, +1);
}
static void set_point(int b, int i, int val) {   /* keeps the degenerate pair tied */
    x[b][i] = val;
    if (b == 0 && i == 0) x[0][1] = val;
    if (b == 0 && i == 1) x[0][0] = val;
}

/* ---------------- labelling DFS ---------------- */
static int L[MAXN][K];
static int used[1024];                  /* bitmask of oriented label differences used per class */
static long long lab_nodes;
static int lab_dfs(int b, int i) {
    if (b == n) return 1;
    if (i == K) return lab_dfs(b + 1, 0);
    if (++lab_nodes > 20000000) return 0;
    int lo = 0, hi = 2;
    if (i == 0) lo = hi = 0;                       /* translation normalisation */
    for (int l = lo; l <= hi; l++) {
        if (b == 0 && i == 1 && l == L[0][0]) continue;   /* the two copies of x differ */
        L[b][i] = l;
        int ok = 1, j;
        int added_c[K], added_bit[K], na = 0;
        for (j = 0; j < i && ok; j++) {
            if (pair_skip(b, j, i)) continue;
            int y = mp(x[b][i] - x[b][j]);
            int c = cls[y];
            int lam = (L[b][i] - L[b][j] + 3) % 3;
            if (y > P2) lam = (3 - lam) % 3;
            int bit = 1 << lam;
            if (used[c] & bit) { ok = 0; break; }
            used[c] |= bit; added_c[na] = c; added_bit[na] = bit; na++;
        }
        if (ok && lab_dfs(b, i + 1)) return 1;
        for (int t = 0; t < na; t++) used[added_c[t]] &= ~added_bit[t];
    }
    return 0;
}

/* ---------------- labelling by GF(3) elimination ----------------
 * Unknowns: L[b][i], i = 1..4 (L[b][0] = 0).  For class c with occurrences (b,i,j,s), lambda = s*(L[b][j]-L[b][i]).
 * Three values in Z_3 are pairwise distinct  <=>  their sum is 0 and the first two differ.  So: homogeneous linear
 * system (one equation per class) plus disequalities lambda_1 - lambda_2 != 0 and L[0][1] != 0.  Solve the system
 * by RREF, then DFS over the free coordinates checking each disequality as soon as its support is assigned. */
#define MAXU (4 * MAXN)
static signed char A[1024][MAXU], G[1024 + 1][MAXU];  /* equations; disequality functionals on unknowns */
static int occ_b[1024][3], occ_i[1024][3], occ_j[1024][3], occ_s[1024][3];
static int nunk, rank_, nfree, freevar[MAXU], pivcol[1024];
static signed char basis[MAXU][MAXU];       /* basis[f][u]: kernel vector for free var index f */
static signed char gam[1024 + 1][MAXU];     /* disequality d in free coordinates */
static int ndis, order_[MAXU], lastpos[1025], ndis_at[MAXU], dis_at[MAXU][1025];
static int zval[MAXU], dval[1025];
static long long gf_nodes;
static inline int unk(int b, int i) { return i == 0 ? -1 : b * 4 + (i - 1); }
static inline int m3(int a) { a %= 3; return a < 0 ? a + 3 : a; }
static void add_term(signed char *row, int b, int i, int coef) { int u = unk(b, i); if (u >= 0) row[u] = (signed char)m3(row[u] + coef); }
static int gf_dfs(int d) {
    if (d == nfree) return 1;
    if (++gf_nodes > 50000000) return 0;
    int f = order_[d];
    for (int a = 0; a < 3; a++) {
        zval[f] = a;
        int ok = 1;
        for (int q = 0; q < ndis_at[d]; q++) {
            int t = dis_at[d][q], s = 0;
            for (int e = 0; e <= d; e++) s += gam[t][order_[e]] * zval[order_[e]];
            if (m3(s) == 0) { ok = 0; break; }
        }
        if (ok && gf_dfs(d + 1)) return 1;
    }
    return 0;
}
static int lab_gf3(void) {
    nunk = 4 * n;
    int fill[1024] = {0};
    for (int b = 0; b < n; b++) for (int i = 0; i < K; i++) for (int j = i + 1; j < K; j++) {
        if (pair_skip(b, i, j)) continue;
        int y = mp(x[b][j] - x[b][i]), c = cls[y], f = fill[c]++;
        if (f >= 3) return 0;
        occ_b[c][f] = b; occ_i[c][f] = i; occ_j[c][f] = j; occ_s[c][f] = y > P2 ? -1 : 1;
    }
    for (int c = 1; c <= P2; c++) if (fill[c] != 3) return 0;
    /* equations and disequalities */
    ndis = 0;
    for (int c = 1; c <= P2; c++) {
        memset(A[c - 1], 0, nunk);
        memset(G[ndis], 0, nunk);
        for (int t = 0; t < 3; t++) {
            add_term(A[c - 1], occ_b[c][t], occ_j[c][t], occ_s[c][t]);
            add_term(A[c - 1], occ_b[c][t], occ_i[c][t], -occ_s[c][t]);
        }
        add_term(G[ndis], occ_b[c][0], occ_j[c][0], occ_s[c][0]);
        add_term(G[ndis], occ_b[c][0], occ_i[c][0], -occ_s[c][0]);
        add_term(G[ndis], occ_b[c][1], occ_j[c][1], -occ_s[c][1]);
        add_term(G[ndis], occ_b[c][1], occ_i[c][1], occ_s[c][1]);
        ndis++;
    }
    memset(G[ndis], 0, nunk); G[ndis][unk(0, 1)] = 1; ndis++;          /* L[0][1] != 0 */
    /* RREF over GF(3) */
    int rows = P2, r = 0;
    int ispiv[MAXU] = {0};
    for (int col = 0; col < nunk && r < rows; col++) {
        int piv = -1;
        for (int q = r; q < rows; q++) if (A[q][col]) { piv = q; break; }
        if (piv < 0) continue;
        if (piv != r) for (int u = 0; u < nunk; u++) { signed char t = A[r][u]; A[r][u] = A[piv][u]; A[piv][u] = t; }
        if (A[r][col] == 2) for (int u = 0; u < nunk; u++) A[r][u] = (signed char)m3(2 * A[r][u]);
        for (int q = 0; q < rows; q++) if (q != r && A[q][col]) {
            int f = A[q][col];
            for (int u = 0; u < nunk; u++) A[q][u] = (signed char)m3(A[q][u] - f * A[r][u]);
        }
        pivcol[r] = col; ispiv[col] = 1; r++;
    }
    rank_ = r; nfree = 0;
    for (int u = 0; u < nunk; u++) if (!ispiv[u]) freevar[nfree++] = u;
    for (int f = 0; f < nfree; f++) {
        memset(basis[f], 0, nunk);
        basis[f][freevar[f]] = 1;
        for (int q = 0; q < rank_; q++) basis[f][pivcol[q]] = (signed char)m3(-A[q][freevar[f]]);
    }
    for (int t = 0; t < ndis; t++) for (int f = 0; f < nfree; f++) {
        int s = 0;
        for (int u = 0; u < nunk; u++) if (G[t][u]) s += G[t][u] * basis[f][u];
        gam[t][f] = (signed char)m3(s);
    }
    /* greedy order: repeatedly take the free coordinate completing most disequalities, tie-break by frequency */
    int assigned[MAXU] = {0}, remaining[1025];
    for (int t = 0; t < ndis; t++) { remaining[t] = 0; for (int f = 0; f < nfree; f++) if (gam[t][f]) remaining[t]++;
        if (remaining[t] == 0) return 0; }
    for (int d = 0; d < nfree; d++) {
        int bestf = -1, bc = -1, bfreq = -1;
        for (int f = 0; f < nfree; f++) if (!assigned[f]) {
            int comp = 0, freq = 0;
            for (int t = 0; t < ndis; t++) if (gam[t][f] && remaining[t] > 0) { freq++; if (remaining[t] == 1) comp++; }
            if (comp > bc || (comp == bc && freq > bfreq)) { bc = comp; bfreq = freq; bestf = f; }
        }
        order_[d] = bestf; assigned[bestf] = 1; ndis_at[d] = 0;
        for (int t = 0; t < ndis; t++) if (gam[t][bestf] && remaining[t] > 0) {
            if (--remaining[t] == 0) dis_at[d][ndis_at[d]++] = t;
        }
    }
    gf_nodes = 0;
    if (!gf_dfs(0)) return 0;
    /* reconstruct labels */
    for (int b = 0; b < n; b++) { L[b][0] = 0; for (int i = 1; i < K; i++) {
        int u = unk(b, i), s = 0;
        for (int f = 0; f < nfree; f++) s += basis[f][u] * zval[f];
        L[b][i] = m3(s); } }
    return 1;
}

static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: cdf_lift v seed seconds outprefix [pert]\n"); return 2; }
    v = atoi(argv[1]); uint64_t seed = strtoull(argv[2], 0, 10); double limit = atof(argv[3]); const char *pre = argv[4];
    int pert = argc > 5 ? atoi(argv[5]) : 3;
    int labmode = argc > 6 ? atoi(argv[6]) : 0;      /* 0: GF(3) elimination, 1: plain DFS, 2: both (cross-check) */
    long long rank_hist[MAXU + 1] = {0}, disagree = 0;
    if (v % 3 || (v - 1) % 20) { fprintf(stderr, "need v = 3p, v = 1 mod 20\n"); return 2; }
    p = v / 3; P2 = (p - 1) / 2; n = (v - 1) / 20;
    if (p >= 1024 || n > MAXN) { fprintf(stderr, "too large\n"); return 2; }
    rng = seed * 0x2545F4914F6CDD1DULL + 31337;
    cls = malloc(sizeof(int) * p); cnt = calloc(P2 + 1, sizeof(int));
    for (int d = 0; d < p; d++) cls[d] = d <= P2 ? d : p - d;
    /* random initial projected family */
    for (int b = 0; b < n; b++) do { for (int i = 0; i < K; i++) x[b][i] = rndint(p); if (b == 0) x[0][1] = x[0][0]; } while (!block_ok(b));
    full_cost();
    double t0 = now(), tlast = t0;
    long long it = 0, projected_solutions = 0, label_nodes_total = 0;
    printf("start v=%d p=%d n=%d seed=%llu pert=%d cost=%d\n", v, p, n, (unsigned long long)seed, pert, cost);
    fflush(stdout);
    for (;;) {
        double t = now();
        if (t - t0 > limit) break;
        if (t - tlast > 30) {
            printf("it=%lld cost=%d projected_solutions=%lld label_nodes=%lld t=%.0f\n", it, cost, projected_solutions, label_nodes_total, t - t0);
            fflush(stdout); tlast = t;
        }
        if (cost == 0) {
            projected_solutions++;
            int ok;
            if (labmode == 1) { memset(used, 0, sizeof(used)); lab_nodes = 0; ok = lab_dfs(0, 0); label_nodes_total += lab_nodes; }
            else {
                int ok2 = -1;
                if (labmode == 2) { memset(used, 0, sizeof(used)); lab_nodes = 0; ok2 = lab_dfs(0, 0); }
                ok = lab_gf3(); label_nodes_total += gf_nodes; rank_hist[nfree]++;
                if (labmode == 2 && ok2 != ok && lab_nodes <= 20000000) { disagree++; printf("DISAGREE gf3=%d dfs=%d\n", ok, ok2); }
            }
            if ((projected_solutions & 1023) == 0) {
                printf("stats projected=%lld nfree_hist:", projected_solutions);
                for (int q = 0; q <= 4 * n; q++) if (rank_hist[q]) printf(" %d:%lld", q, rank_hist[q]);
                printf(" disagree=%lld\n", disagree); fflush(stdout);
            }
            if (ok) {
                char path[1024];
                snprintf(path, sizeof path, "%s.sol", pre);
                FILE *f = fopen(path, "w");
                fprintf(f, "CDF %d %d\n", v, K);
                for (int b = 0; b < n; b++) {
                    int e[K];
                    for (int i = 0; i < K; i++) {      /* CRT: z = x (mod p), z = L (mod 3) */
                        int z = x[b][i];
                        while (z % 3 != L[b][i]) z += p;
                        e[i] = z;
                    }
                    qsort(e, K, sizeof(int), cmpint);
                    for (int i = 0; i < K; i++) fprintf(f, "%d%c", e[i], i + 1 < K ? ' ' : '\n');
                }
                fclose(f);
                printf("FOUND v=%d seed=%llu projected_solutions=%lld it=%lld seconds=%.2f label_nodes=%lld\n", v,
                       (unsigned long long)seed, projected_solutions, it, now() - t0, label_nodes_total);
                return 0;
            }
            /* perturb */
            for (int q = 0; q < pert; q++) {
                int b = rndint(n), i = rndint(K), old0 = x[b][0], old1 = x[b][1], oldi = x[b][i];
                cost += block_cost_apply(b, -1);
                do { x[b][0] = old0; x[b][1] = old1; x[b][i] = oldi; set_point(b, i, rndint(p)); } while (!block_ok(b));
                cost += block_cost_apply(b, +1);
            }
            continue;
        }
        /* one tabu step: best non-tabu single-point move among points in conflicted pairs */
        it++;
        int bestd = 1 << 30, mb = -1, mi = -1, my = -1, ties = 0;
        for (int b = 0; b < n; b++) {
            int confl[K] = {0};
            for (int i = 0; i < K; i++) for (int j = i + 1; j < K; j++) {
                if (pair_skip(b, i, j)) continue;
                if (cnt[cls[mp(x[b][i] - x[b][j])]] > 3) { confl[i] = 1; confl[j] = 1; }
            }
            for (int i = 0; i < K; i++) {
                if (!confl[i] || (b == 0 && i == 1)) continue;
                int old0 = x[b][0], old1 = x[b][1], oldi = x[b][i];
                int rem = block_cost_apply(b, -1);
                for (int y = 0; y < p; y++) {
                    if (y == oldi) continue;
                    set_point(b, i, y);
                    if (!block_ok(b)) { x[b][0] = old0; x[b][1] = old1; x[b][i] = oldi; continue; }
                    int add = block_cost_apply(b, +1);
                    block_cost_apply(b, -1);
                    int d = rem + add;
                    int ok = tabu_until[b][i][y] <= it || cost + d == 0;
                    x[b][0] = old0; x[b][1] = old1; x[b][i] = oldi;
                    if (!ok) continue;
                    if (d < bestd) { bestd = d; mb = b; mi = i; my = y; ties = 1; }
                    else if (d == bestd && rndint(++ties) == 0) { mb = b; mi = i; my = y; }
                }
                block_cost_apply(b, +1);
            }
        }
        if (mb < 0) continue;
        int oldv = x[mb][mi];
        cost += block_cost_apply(mb, -1);
        set_point(mb, mi, my);
        cost += block_cost_apply(mb, +1);
        tabu_until[mb][mi][oldv] = it + 5 + rndint(6);
    }
    printf("TIMEOUT v=%d seed=%llu projected_solutions=%lld it=%lld seconds=%.2f label_nodes=%lld\n", v,
           (unsigned long long)seed, projected_solutions, it, now() - t0, label_nodes_total);
    return 3;
}
