/* cdf_dlx.c -- random prefix + exact-cover (dancing links) completion for cyclic (v,k,1) difference families.
 *
 * Each attempt: place n-r base blocks greedily at random with pairwise disjoint difference classes (or, with a
 * state file, keep n-r blocks of a given state that are collision-free), let R be the 10r uncovered classes,
 * enumerate every block (up to translation and negation) whose k(k-1)/2 classes are distinct and all lie in R,
 * and run Algorithm X with dancing links (minimum-size column, randomized row order) for an exact cover of R
 * by r blocks, up to a node limit.  Writes outprefix.sol (strict certificate) on success.
 *
 * Usage: cdf_dlx v k seed r attempts nodelimit outprefix [maxsols]
 *   maxsols > 1 (calibration): keep searching after a hit and count solutions of the attempt (no .sol beyond first)
 * Exit 0 found, 3 not found.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define K 5
#define NP (K * (K - 1) / 2)

static int v, H, n, r;
static int *cls;
static uint64_t rng;
static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int rndint(int m) { return (int)(rnd() % (uint64_t)m); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }

/* ---------------- dancing links ---------------- */
static int *L, *Rt, *U, *D, *C, *S, *ROW;   /* node arrays; columns are nodes 1..ncol, root 0 */
static int nnode, ncol, cap;
static int **rows; static int nrows, rowcap;  /* rows[i] = block (K ints) */
static int sol[64], nsol_depth;
static long long nodes, nodelimit, solutions, maxsols;
static int found_block[64][K];
static int have_found;

static void dlx_init(int ncols, int maxnodes) {
    ncol = ncols; cap = maxnodes + ncols + 1;
    L = realloc(L, sizeof(int) * cap); Rt = realloc(Rt, sizeof(int) * cap); U = realloc(U, sizeof(int) * cap);
    D = realloc(D, sizeof(int) * cap); C = realloc(C, sizeof(int) * cap); S = realloc(S, sizeof(int) * (ncols + 1));
    ROW = realloc(ROW, sizeof(int) * cap);
    for (int i = 0; i <= ncols; i++) { L[i] = i - 1; Rt[i] = i + 1; U[i] = D[i] = i; C[i] = i; S[i] = 0; }
    L[0] = ncols; Rt[ncols] = 0;
    nnode = ncols + 1;
}
static void dlx_addrow(int rowid, const int *cols, int m) {
    int first = nnode;
    for (int j = 0; j < m; j++) {
        int c = cols[j], x = nnode++;
        C[x] = c; ROW[x] = rowid;
        U[x] = U[c]; D[x] = c; D[U[c]] = x; U[c] = x; S[c]++;
        if (j == 0) { L[x] = Rt[x] = x; }
        else { L[x] = x - 1; Rt[x] = first; Rt[x - 1] = x; L[first] = x; }
    }
}
static void cover(int c) {
    L[Rt[c]] = L[c]; Rt[L[c]] = Rt[c];
    for (int i = D[c]; i != c; i = D[i])
        for (int j = Rt[i]; j != i; j = Rt[j]) { U[D[j]] = U[j]; D[U[j]] = D[j]; S[C[j]]--; }
}
static void uncover(int c) {
    for (int i = U[c]; i != c; i = U[i])
        for (int j = L[i]; j != i; j = L[j]) { S[C[j]]++; U[D[j]] = j; D[U[j]] = j; }
    L[Rt[c]] = c; Rt[L[c]] = c;
}
static int search(int depth) {
    if (Rt[0] == 0) {
        solutions++;
        if (!have_found) { for (int i = 0; i < depth; i++) memcpy(found_block[i], rows[sol[i]], sizeof(int) * K); have_found = 1; nsol_depth = depth; }
        return solutions >= maxsols;
    }
    if (++nodes > nodelimit) return 1;
    int best = -1, bs = 1 << 30, ties = 0;
    for (int c = Rt[0]; c != 0; c = Rt[c]) {
        if (S[c] < bs) { bs = S[c]; best = c; ties = 1; }
        else if (S[c] == bs && rndint(++ties) == 0) best = c;
    }
    if (bs == 0) return 0;
    cover(best);
    for (int x = D[best]; x != best; x = D[x]) {
        sol[depth] = ROW[x];
        for (int j = Rt[x]; j != x; j = Rt[j]) cover(C[j]);
        int stop = search(depth + 1);
        for (int j = L[x]; j != x; j = L[j]) uncover(C[j]);
        if (stop) { uncover(best); return 1; }
    }
    uncover(best);
    return 0;
}

/* ---------------- block utilities ---------------- */
static int md(int x) { x %= v; return x < 0 ? x + v : x; }
static int block_classes(const int *b, int *out) { /* returns 1 if the NP classes are distinct and nonzero */
    int m = 0;
    for (int i = 0; i < K; i++) for (int j = i + 1; j < K; j++) {
        int c = cls[md(b[i] - b[j])];
        if (c == 0) return 0;
        for (int t = 0; t < m; t++) if (out[t] == c) return 0;
        out[m++] = c;
    }
    return 1;
}
static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
/* canonical representative under translation and negation: lexicographically least sorted tuple with min 0 */
static void canon(const int *b, int *out) {
    int best[K], cand[K], have = 0;
    for (int sgn = 0; sgn < 2; sgn++) for (int t = 0; t < K; t++) {
        for (int i = 0; i < K; i++) cand[i] = md((sgn ? -b[i] : b[i]) - (sgn ? -b[t] : b[t]));
        qsort(cand, K, sizeof(int), cmpint);
        if (!have || memcmp(cand, best, sizeof(cand)) < 0) { memcpy(best, cand, sizeof(cand)); have = 1; }
    }
    memcpy(out, best, sizeof(best));
}

int main(int argc, char **argv) {
    if (argc < 8) { fprintf(stderr, "usage: cdf_dlx v k seed r attempts nodelimit outprefix [maxsols]\n"); return 2; }
    v = atoi(argv[1]); if (atoi(argv[2]) != K) { fprintf(stderr, "compiled for k=%d\n", K); return 2; }
    uint64_t seed = strtoull(argv[3], 0, 10); r = atoi(argv[4]);
    long attempts = atol(argv[5]); nodelimit = atoll(argv[6]); const char *pre = argv[7];
    maxsols = argc > 8 ? atoll(argv[8]) : 1;
    rng = seed * 0x2545F4914F6CDD1DULL + 777;
    H = (v - 1) / 2; n = (v - 1) / (K * (K - 1));
    if ((v - 1) % (K * (K - 1)) || r > n || r > 60) { fprintf(stderr, "bad parameters\n"); return 2; }
    cls = malloc(sizeof(int) * v);
    for (int d = 0; d < v; d++) cls[d] = d <= H ? d : v - d;
    int *covered = calloc(H + 1, sizeof(int)), *colid = calloc(H + 1, sizeof(int));
    int (*prefix)[K] = malloc(sizeof(int) * K * n);
    int *S_el = malloc(sizeof(int) * v);
    rowcap = 1 << 16; rows = malloc(sizeof(int *) * rowcap);
    double t0 = now();
    long long total_nodes = 0, total_rows = 0;
    printf("start v=%d n=%d r=%d seed=%llu attempts=%ld nodelimit=%lld maxsols=%lld\n", v, n, r,
           (unsigned long long)seed, attempts, nodelimit, maxsols);
    fflush(stdout);
    for (long at = 0; at < attempts; at++) {
        /* random greedy prefix */
        memset(covered, 0, sizeof(int) * (H + 1));
        int np = 0, tries = 0;
        while (np < n - r) {
            int b[K], cl[NP];
            b[0] = 0;
            for (int i = 1; i < K; i++) b[i] = 1 + rndint(v - 1);
            int ok = block_classes(b, cl);
            for (int t = 0; ok && t < NP; t++) if (covered[cl[t]]) ok = 0;
            if (ok) { for (int t = 0; t < NP; t++) covered[cl[t]] = 1; memcpy(prefix[np++], b, sizeof(b)); }
            if (++tries > 50000000) { fprintf(stderr, "prefix stuck\n"); return 1; }
        }
        /* R */
        int nR = 0;
        for (int c = 1; c <= H; c++) colid[c] = covered[c] ? 0 : ++nR;
        int nS = 0;
        for (int x = 1; x < v; x++) if (!covered[cls[x]]) S_el[nS++] = x;
        /* enumerate rows: {0,a,b,c,d} with a<b<c<d in S, all classes in R and distinct, canonical */
        for (int i = 0; i < nrows; i++) free(rows[i]);
        nrows = 0;
        for (int ia = 0; ia < nS; ia++) {
            int a = S_el[ia];
            for (int ib = ia + 1; ib < nS; ib++) {
                int b = S_el[ib];
                if (covered[cls[b - a]]) continue;
                for (int ic = ib + 1; ic < nS; ic++) {
                    int c = S_el[ic];
                    if (covered[cls[c - a]] || covered[cls[c - b]]) continue;
                    for (int id = ic + 1; id < nS; id++) {
                        int d = S_el[id];
                        if (covered[cls[d - a]] || covered[cls[d - b]] || covered[cls[d - c]]) continue;
                        int blk[K] = {0, a, b, c, d}, cl[NP], cn[K];
                        if (!block_classes(blk, cl)) continue;
                        canon(blk, cn);
                        if (memcmp(cn, blk, sizeof(blk)) != 0) continue;
                        if (nrows == rowcap) { rowcap *= 2; rows = realloc(rows, sizeof(int *) * rowcap); }
                        rows[nrows] = malloc(sizeof(int) * K); memcpy(rows[nrows], blk, sizeof(blk)); nrows++;
                    }
                }
            }
        }
        total_rows += nrows;
        /* shuffle rows, build DLX */
        for (int i = nrows - 1; i > 0; i--) { int j = rndint(i + 1); int *t = rows[i]; rows[i] = rows[j]; rows[j] = t; }
        dlx_init(nR, nrows * NP);
        for (int i = 0; i < nrows; i++) {
            int cl[NP], cols[NP];
            block_classes(rows[i], cl);
            for (int t = 0; t < NP; t++) cols[t] = colid[cl[t]];
            dlx_addrow(i, cols, NP);
        }
        nodes = 0; solutions = 0; have_found = 0;
        search(0);
        total_nodes += nodes;
        int exhausted = nodes <= nodelimit;
        printf("attempt=%ld rows=%d nodes=%lld exhausted=%d solutions=%lld t=%.1f\n", at, nrows, nodes, exhausted,
               solutions, now() - t0);
        fflush(stdout);
        if (have_found) {
            char path[1024];
            snprintf(path, sizeof path, "%s.sol", pre);
            FILE *f = fopen(path, "w");
            fprintf(f, "CDF %d %d\n", v, K);
            for (int i = 0; i < np; i++) { int e[K]; memcpy(e, prefix[i], sizeof(e)); qsort(e, K, sizeof(int), cmpint);
                for (int t = 0; t < K; t++) fprintf(f, "%d%c", e[t], t + 1 < K ? ' ' : '\n'); }
            for (int i = 0; i < nsol_depth; i++) { int e[K]; memcpy(e, found_block[i], sizeof(e)); qsort(e, K, sizeof(int), cmpint);
                for (int t = 0; t < K; t++) fprintf(f, "%d%c", e[t], t + 1 < K ? ' ' : '\n'); }
            fclose(f);
            printf("FOUND v=%d seed=%llu attempt=%ld seconds=%.2f total_nodes=%lld\n", v, (unsigned long long)seed,
                   at, now() - t0, total_nodes);
            if (maxsols <= 1) return 0;
        }
    }
    printf("DONE v=%d seed=%llu attempts=%ld seconds=%.2f total_nodes=%lld mean_rows=%.1f\n", v,
           (unsigned long long)seed, attempts, now() - t0, total_nodes, (double)total_rows / (attempts > 0 ? attempts : 1));
    return 3;
}
