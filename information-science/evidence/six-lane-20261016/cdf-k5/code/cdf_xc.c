/* cdf_xc.c -- random prefix + bitset exact-cover completion for cyclic (v,5,1) difference families.
 *
 * Attempt: place n-r base blocks at random with pairwise disjoint difference classes; R = the 10r uncovered
 * classes; enumerate all blocks (one per translation+negation class) whose 10 classes are distinct and lie in R;
 * search for an exact cover of R by r of them (Algorithm X on bitmasks: choose the uncovered class with the fewest
 * candidate rows, branch on its rows in random order, filter the row list by disjointness), up to a node limit.
 *
 * Usage: cdf_xc v seed r attempts nodelimit outprefix [maxsols] [prefixfile]
 *   prefixfile: optional text file with base blocks (one per line, 5 ints) to use as the fixed prefix instead of a
 *   random one (its blocks must have disjoint classes; r is then n - #prefix blocks).
 * Exit 0 found, 3 not found.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define K 5
#define NP 10
#define W 4                    /* mask words: up to 256 columns, r <= 25 */

typedef struct { uint64_t m[W]; } mask_t;
static int v, H, n, r, nR;
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
static int md(int x) { x %= v; return x < 0 ? x + v : x; }

static int nrows, rowcap;
static mask_t *rmask;
static unsigned char (*rcol)[NP];
static int (*rblk)[K];
static int **lists;            /* per-level row index lists */
static int chosen[64];
static long long nodes, nodelimit, solutions, maxsols;
static int found[64], have_found;

static int disjoint(const mask_t *a, const mask_t *b) {
    uint64_t x = 0;
    for (int w = 0; w < W; w++) x |= a->m[w] & b->m[w];
    return x == 0;
}

static int search(int depth, int cntrows, int ncov) {
    if (ncov == nR) {
        solutions++;
        if (!have_found) { memcpy(found, chosen, sizeof(int) * depth); have_found = 1; }
        return solutions >= maxsols;
    }
    if (++nodes > nodelimit) return 1;
    int *lst = lists[depth];
    static int cnt[W * 64];
    static int covered_flag[W * 64];
    (void)covered_flag;
    memset(cnt, 0, sizeof(int) * nR);
    for (int i = 0; i < cntrows; i++) { const unsigned char *c = rcol[lst[i]]; for (int j = 0; j < NP; j++) cnt[c[j]]++; }
    /* uncovered columns: those not in union of chosen rows; track via a mask */
    mask_t cov; memset(&cov, 0, sizeof cov);
    for (int d = 0; d < depth; d++) for (int w = 0; w < W; w++) cov.m[w] |= rmask[chosen[d]].m[w];
    int best = -1, bs = 1 << 30, ties = 0;
    for (int c = 0; c < nR; c++) {
        if (cov.m[c >> 6] >> (c & 63) & 1) continue;
        if (cnt[c] < bs) { bs = cnt[c]; best = c; ties = 1; }
        else if (cnt[c] == bs && rndint(++ties) == 0) best = c;
    }
    if (bs == 0) return 0;
    int *nxt = lists[depth + 1];
    for (int i = 0; i < cntrows; i++) {
        int x = lst[i];
        if (!(rmask[x].m[best >> 6] >> (best & 63) & 1)) continue;
        int m = 0;
        for (int j = 0; j < cntrows; j++) { int y = lst[j]; if (disjoint(&rmask[x], &rmask[y])) nxt[m++] = y; }
        chosen[depth] = x;
        if (search(depth + 1, m, ncov + NP)) return 1;
    }
    return 0;
}

static int block_classes(const int *b, int *out) {
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
static void canon(const int *b, int *out) {
    int best[K], cand[K], have = 0;
    for (int sgn = 0; sgn < 2; sgn++) for (int t = 0; t < K; t++) {
        for (int i = 0; i < K; i++) cand[i] = md((sgn ? -b[i] : b[i]) - (sgn ? -b[t] : b[t]));
        qsort(cand, K, sizeof(int), cmpint);
        if (!have || memcmp(cand, best, sizeof(cand)) < 0) { memcpy(best, cand, sizeof(cand)); have = 1; }
    }
    memcpy(out, best, sizeof(best));
}
static void addrow(const int *blk, const int *colid) {
    if (nrows == rowcap) {
        rowcap = rowcap ? rowcap * 2 : 1 << 16;
        rmask = realloc(rmask, sizeof(mask_t) * rowcap); rcol = realloc(rcol, NP * rowcap); rblk = realloc(rblk, sizeof(int) * K * rowcap);
    }
    int cl[NP];
    block_classes(blk, cl);
    memset(&rmask[nrows], 0, sizeof(mask_t));
    for (int t = 0; t < NP; t++) { int c = colid[cl[t]]; rcol[nrows][t] = (unsigned char)c; rmask[nrows].m[c >> 6] |= 1ULL << (c & 63); }
    memcpy(rblk[nrows], blk, sizeof(int) * K);
    nrows++;
}

int main(int argc, char **argv) {
    if (argc < 7) { fprintf(stderr, "usage: cdf_xc v seed r attempts nodelimit outprefix [maxsols] [prefixfile]\n"); return 2; }
    v = atoi(argv[1]); uint64_t seed = strtoull(argv[2], 0, 10); r = atoi(argv[3]);
    long attempts = atol(argv[4]); nodelimit = atoll(argv[5]); const char *pre = argv[6];
    maxsols = argc > 7 ? atoll(argv[7]) : 1;
    const char *pfile = argc > 8 ? argv[8] : 0;
    rng = seed * 0x2545F4914F6CDD1DULL + 4242;
    H = (v - 1) / 2; n = (v - 1) / 20;
    if ((v - 1) % 20 || r > n || 10 * r > W * 64 || r > 60) { fprintf(stderr, "bad parameters\n"); return 2; }
    cls = malloc(sizeof(int) * v);
    for (int d = 0; d < v; d++) cls[d] = d <= H ? d : v - d;
    int *covered = calloc(H + 1, sizeof(int)), *colid = calloc(H + 1, sizeof(int));
    int (*prefix)[K] = malloc(sizeof(int) * K * (n + 1));
    int *S_el = malloc(sizeof(int) * v);
    lists = calloc(64, sizeof(int *));
    double t0 = now();
    long long total_nodes = 0, total_rows = 0;
    int nfixed = 0;
    if (pfile) {
        FILE *f = fopen(pfile, "r");
        if (!f) { perror(pfile); return 2; }
        while (nfixed < n && fscanf(f, "%d %d %d %d %d", &prefix[nfixed][0], &prefix[nfixed][1], &prefix[nfixed][2],
                                    &prefix[nfixed][3], &prefix[nfixed][4]) == 5) nfixed++;
        fclose(f);
        r = n - nfixed;
        if (10 * r > W * 64) { fprintf(stderr, "prefix too short for mask width\n"); return 2; }
    }
    printf("start v=%d n=%d r=%d seed=%llu attempts=%ld nodelimit=%lld maxsols=%lld prefixfile=%s\n", v, n, r,
           (unsigned long long)seed, attempts, nodelimit, maxsols, pfile ? pfile : "-");
    fflush(stdout);
    for (long at = 0; at < attempts; at++) {
        memset(covered, 0, sizeof(int) * (H + 1));
        int np = 0;
        if (pfile) {
            for (np = 0; np < nfixed; np++) {
                int cl[NP];
                if (!block_classes(prefix[np], cl)) { fprintf(stderr, "prefix block %d invalid\n", np); return 2; }
                for (int t = 0; t < NP; t++) { if (covered[cl[t]]) { fprintf(stderr, "prefix overlap\n"); return 2; } covered[cl[t]] = 1; }
            }
        } else {
            long long tries = 0;
            while (np < n - r) {
                int b[K], cl[NP];
                b[0] = 0;
                for (int i = 1; i < K; i++) b[i] = 1 + rndint(v - 1);
                int ok = block_classes(b, cl);
                for (int t = 0; ok && t < NP; t++) if (covered[cl[t]]) ok = 0;
                if (ok) { for (int t = 0; t < NP; t++) covered[cl[t]] = 1; memcpy(prefix[np++], b, sizeof(b)); }
                if (++tries > 2000000000LL) { fprintf(stderr, "prefix stuck\n"); return 1; }
            }
        }
        nR = 0;
        for (int c = 1; c <= H; c++) colid[c] = covered[c] ? -1 : nR++;
        int nS = 0;
        for (int x = 1; x < v; x++) if (!covered[cls[x]]) S_el[nS++] = x;
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
                        addrow(blk, colid);
                    }
                }
            }
        }
        total_rows += nrows;
        for (int d = 0; d <= r + 1; d++) lists[d] = realloc(lists[d], sizeof(int) * (nrows + 1));
        for (int i = 0; i < nrows; i++) lists[0][i] = i;
        for (int i = nrows - 1; i > 0; i--) { int j = rndint(i + 1); int t = lists[0][i]; lists[0][i] = lists[0][j]; lists[0][j] = t; }
        nodes = 0; solutions = 0; have_found = 0;
        double ta = now();
        search(0, nrows, 0);
        total_nodes += nodes;
        printf("attempt=%ld rows=%d nodes=%lld exhausted=%d solutions=%lld secs=%.2f t=%.1f\n", at, nrows, nodes,
               nodes <= nodelimit, solutions, now() - ta, now() - t0);
        fflush(stdout);
        if (have_found) {
            char path[1024];
            snprintf(path, sizeof path, "%s.sol", pre);
            FILE *f = fopen(path, "w");
            fprintf(f, "CDF %d %d\n", v, K);
            for (int i = 0; i < np; i++) { int e[K]; memcpy(e, prefix[i], sizeof(e)); for (int t = 0; t < K; t++) e[t] = md(e[t]); qsort(e, K, sizeof(int), cmpint);
                for (int t = 0; t < K; t++) fprintf(f, "%d%c", e[t], t + 1 < K ? ' ' : '\n'); }
            for (int i = 0; i < r; i++) { int e[K]; memcpy(e, rblk[found[i]], sizeof(e)); qsort(e, K, sizeof(int), cmpint);
                for (int t = 0; t < K; t++) fprintf(f, "%d%c", e[t], t + 1 < K ? ' ' : '\n'); }
            fclose(f);
            printf("FOUND v=%d seed=%llu attempt=%ld seconds=%.2f total_nodes=%lld\n", v, (unsigned long long)seed,
                   at, now() - t0, total_nodes);
            fflush(stdout);
            if (maxsols <= 1) return 0;
        }
    }
    printf("DONE v=%d seed=%llu attempts=%ld seconds=%.2f total_nodes=%lld mean_rows=%.1f\n", v,
           (unsigned long long)seed, attempts, now() - t0, total_nodes, (double)total_rows / (attempts > 0 ? attempts : 1));
    return 3;
}
