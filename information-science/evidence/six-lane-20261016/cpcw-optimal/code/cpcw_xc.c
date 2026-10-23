/* cpcw_xc.c -- representation R1 of the cpcw-optimal lane README: random leave + random prefix + exact cover
 * completion for optimal (v,k,1) CPCW codes (k in {5,6}), written for this lane.
 *
 * Classes [d] = {d,-d}, d = 1..H, H = floor((v-1)/2) (for even v the class v/2 is never usable).  s = floor((v-1)/
 * (k(k-1))) codewords; leave c = H - s*C(k,2) classes stay uncovered.  One attempt:
 *   1. choose the leave (mode R: uniform c-subset; E: uniform c-subset of even classes; S: uniform c-subset of one
 *      parity class (even or odd chosen uniformly); or an explicit comma list),
 *   2. place p random admissible codewords with pairwise disjoint classes avoiding the leave,
 *   3. enumerate ALL admissible k-subsets (one row per translation+negation class) whose classes lie in the
 *      remaining set R, and run Algorithm X (min-candidate column, random tie-break, random row order) for an exact
 *      cover of R by s-p rows, up to a node limit (complete for this leave+prefix when not hit).
 * Optional type filter (even v): prefix codewords must have parity type in the bitmask tmask (bit i = type i).
 *
 * Usage: cpcw_xc v k seed p attempts nodelimit outprefix leavemode [tmask] [maxsecs]
 * Output: outprefix.sol (strict "CPCW v k" format, codewords sorted) on success; log on stdout.
 * Exit 0 found, 3 not found, 2 usage.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define MAXK 6
#define MAXP 15
#define W 2
typedef struct { uint64_t m[W]; } mask_t;

static int v, k, H, s, npairs, c, p;
static int *cls;                 /* cls[x] = class of x (0 for x=0 and, for even v, -1 for v/2) */
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
static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }

/* rows */
static int nrows, rowcap, nR;
static mask_t *rmask;
static unsigned char (*rcol)[15];
static int (*rblk)[MAXK];
static int **lists;
static int chosen[64], found[64], have_found;
static long long nodes, nodelimit;

static int disjoint(const mask_t *a, const mask_t *b) {
    uint64_t x = 0;
    for (int w = 0; w < W; w++) x |= a->m[w] & b->m[w];
    return x == 0;
}

static int search(int depth, int cnt, int ncov) {
    if (ncov == nR) { memcpy(found, chosen, sizeof(int) * depth); have_found = 1; return 1; }
    if (++nodes > nodelimit) return 1;
    int *lst = lists[depth];
    int cntc[W * 64];
    memset(cntc, 0, sizeof(int) * nR);
    for (int i = 0; i < cnt; i++) { const unsigned char *cc = rcol[lst[i]]; for (int j = 0; j < npairs; j++) cntc[cc[j]]++; }
    mask_t cov; memset(&cov, 0, sizeof cov);
    for (int d = 0; d < depth; d++) for (int w = 0; w < W; w++) cov.m[w] |= rmask[chosen[d]].m[w];
    int best = -1, bs = 1 << 30, ties = 0;
    for (int col = 0; col < nR; col++) {
        if (cov.m[col >> 6] >> (col & 63) & 1) continue;
        if (cntc[col] < bs) { bs = cntc[col]; best = col; ties = 1; }
        else if (cntc[col] == bs && rndint(++ties) == 0) best = col;
    }
    if (bs == 0) return 0;
    int *nxt = lists[depth + 1];
    for (int i = 0; i < cnt; i++) {
        int x = lst[i];
        if (!(rmask[x].m[best >> 6] >> (best & 63) & 1)) continue;
        int m = 0;
        for (int j = 0; j < cnt; j++) { int y = lst[j]; if (y != x && disjoint(&rmask[x], &rmask[y])) nxt[m++] = y; }
        chosen[depth] = x;
        if (search(depth + 1, m, ncov + npairs)) return 1;
    }
    return 0;
}

/* classes of a k-set; returns 0 if not admissible */
static int block_classes(const int *b, int *out) {
    int m = 0;
    for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) {
        int cl = cls[md(b[i] - b[j])];
        if (cl <= 0) return 0;
        for (int t = 0; t < m; t++) if (out[t] == cl) return 0;
        out[m++] = cl;
    }
    return 1;
}
/* canonical representative under translation and negation: lexicographically least sorted tuple containing 0 */
static void canon(const int *b, int *out) {
    int best[MAXK], cand[MAXK], have = 0;
    for (int sg = 0; sg < 2; sg++) for (int t = 0; t < k; t++) {
        for (int i = 0; i < k; i++) cand[i] = md((sg ? -b[i] : b[i]) - (sg ? -b[t] : b[t]));
        qsort(cand, k, sizeof(int), cmpint);
        if (!have || memcmp(cand, best, sizeof(int) * k) < 0) { memcpy(best, cand, sizeof(int) * k); have = 1; }
    }
    memcpy(out, best, sizeof(int) * k);
}
static int ptype(const int *b) { int o = 0; for (int i = 0; i < k; i++) o += md(b[i]) & 1; return o < k - o ? o : k - o; }

static int *colid;
static void addrow(const int *blk) {
    if (nrows == rowcap) {
        rowcap = rowcap ? rowcap * 2 : 1 << 16;
        rmask = realloc(rmask, sizeof(mask_t) * rowcap); rcol = realloc(rcol, 15 * rowcap);
        rblk = realloc(rblk, sizeof(int) * MAXK * rowcap);
    }
    int cl[15];
    block_classes(blk, cl);
    memset(&rmask[nrows], 0, sizeof(mask_t));
    for (int t = 0; t < npairs; t++) { int cc = colid[cl[t]]; rcol[nrows][t] = (unsigned char)cc; rmask[nrows].m[cc >> 6] |= 1ULL << (cc & 63); }
    memcpy(rblk[nrows], blk, sizeof(int) * k);
    nrows++;
}

static int *avail;   /* avail[class] = 1 if class is in R and not yet used inside the partial block */
static int blk[MAXK];
static void enum_rows(int depth, int lo) {
    if (depth == k) {
        int cn[MAXK];
        canon(blk, cn);
        if (memcmp(cn, blk, sizeof(int) * k) == 0) addrow(blk);
        return;
    }
    for (int x = lo; x < v; x++) {
        int newc[MAXK], i;
        for (i = 0; i < depth; i++) {
            int cl = cls[x - blk[i]];
            if (cl <= 0 || !avail[cl]) break;
            avail[cl] = 0;          /* mark: also rejects a repeat among the new classes */
            newc[i] = cl;
        }
        if (i == depth) { blk[depth] = x; enum_rows(depth + 1, x + 1); }
        for (int j = 0; j < i; j++) avail[newc[j]] = 1;
    }
}

int main(int argc, char **argv) {
    if (argc < 9) {
        fprintf(stderr, "usage: cpcw_xc v k seed p attempts nodelimit outprefix leavemode [tmask] [maxsecs]\n");
        return 2;
    }
    v = atoi(argv[1]); k = atoi(argv[2]); uint64_t seed = strtoull(argv[3], 0, 10); p = atoi(argv[4]);
    long attempts = atol(argv[5]); nodelimit = atoll(argv[6]); const char *pre = argv[7]; const char *lmode = argv[8];
    int tmask = argc > 9 ? atoi(argv[9]) : 0xff;
    double maxsecs = argc > 10 ? atof(argv[10]) : 1e30;
    if (k < 3 || k > MAXK) { fprintf(stderr, "k out of range\n"); return 2; }
    rng = seed * 0x2545F4914F6CDD1DULL + 777;
    H = (v - 1) / 2; npairs = k * (k - 1) / 2; s = (v - 1) / (k * (k - 1)); c = H - s * npairs;
    if (p >= s || p > MAXP || (s - p) * npairs > W * 64) { fprintf(stderr, "bad p\n"); return 2; }
    cls = malloc(sizeof(int) * v);
    for (int d = 0; d < v; d++) cls[d] = d == 0 ? 0 : (2 * d == v ? -1 : (d <= v - d ? d : v - d));
    colid = calloc(H + 1, sizeof(int)); avail = calloc(H + 1, sizeof(int));
    int *leave = calloc(c + 1, sizeof(int)), *covered = calloc(H + 1, sizeof(int));
    int (*prefix)[MAXK] = malloc(sizeof(int) * MAXK * (MAXP + 1));
    lists = calloc(64, sizeof(int *));
    int explicit_leave = !(lmode[0] == 'R' || lmode[0] == 'E' || lmode[0] == 'S') || lmode[1] != 0;
    printf("start v=%d k=%d s=%d H=%d c=%d p=%d seed=%llu attempts=%ld nodelimit=%lld leavemode=%s tmask=%d\n",
           v, k, s, H, c, p, (unsigned long long)seed, attempts, nodelimit, lmode, tmask);
    fflush(stdout);
    double t0 = now();
    long long total_nodes = 0, total_rows = 0, exhausted = 0;
    for (long at = 0; at < attempts; at++) {
        if (now() - t0 > maxsecs) { printf("TIMEUP after %ld attempts\n", at); break; }
        memset(covered, 0, sizeof(int) * (H + 1));
        /* 1. leave */
        if (explicit_leave) {
            const char *q = lmode; int nl = 0;
            while (*q && nl < c) { leave[nl++] = atoi(q); while (*q && *q != ',') q++; if (*q == ',') q++; }
            if (nl != c) { fprintf(stderr, "explicit leave needs %d classes\n", c); return 2; }
        } else {
            int par = lmode[0] == 'E' ? 0 : (lmode[0] == 'S' ? rndint(2) : -1);
            int pool[512], np = 0;
            for (int d = 1; d <= H; d++) if (par < 0 || (d & 1) == par) pool[np++] = d;
            for (int i = 0; i < c; i++) { int j = i + rndint(np - i); int t = pool[i]; pool[i] = pool[j]; pool[j] = t; leave[i] = pool[i]; }
        }
        for (int i = 0; i < c; i++) {
            if (leave[i] < 1 || leave[i] > H || covered[leave[i]]) { fprintf(stderr, "bad leave\n"); return 2; }
            covered[leave[i]] = 1;
        }
        /* 2. prefix */
        int np = 0; long long tries = 0;
        while (np < p) {
            int b[MAXK], cl[15];
            b[0] = 0;
            for (int i = 1; i < k; i++) b[i] = 1 + rndint(v - 1);
            int ok = block_classes(b, cl);
            if (ok && v % 2 == 0 && !((tmask >> ptype(b)) & 1)) ok = 0;
            for (int t = 0; ok && t < npairs; t++) if (covered[cl[t]]) ok = 0;
            if (ok) { for (int t = 0; t < npairs; t++) covered[cl[t]] = 1; memcpy(prefix[np++], b, sizeof(b)); }
            if (++tries > 200000000LL) { fprintf(stderr, "prefix stuck\n"); return 3; }
        }
        /* 3. rows + exact cover */
        nR = 0;
        for (int d = 1; d <= H; d++) { avail[d] = !covered[d]; colid[d] = covered[d] ? -1 : nR++; }
        nrows = 0;
        blk[0] = 0;
        enum_rows(1, 1);
        total_rows += nrows;
        for (int d = 0; d <= s - p + 1; d++) lists[d] = realloc(lists[d], sizeof(int) * (nrows + 1));
        for (int i = 0; i < nrows; i++) lists[0][i] = i;
        for (int i = nrows - 1; i > 0; i--) { int j = rndint(i + 1); int t = lists[0][i]; lists[0][i] = lists[0][j]; lists[0][j] = t; }
        nodes = 0; have_found = 0;
        double ta = now();
        search(0, nrows, 0);
        total_nodes += nodes;
        if (nodes <= nodelimit) exhausted++;
        if (at < 20 || have_found || at % 1000 == 0) {
            printf("attempt=%ld leave=", at);
            for (int i = 0; i < c; i++) printf("%d%s", leave[i], i + 1 < c ? "," : "");
            printf(" rows=%d nodes=%lld exhausted=%d found=%d secs=%.3f t=%.1f\n", nrows, nodes, nodes <= nodelimit,
                   have_found, now() - ta, now() - t0);
            fflush(stdout);
        }
        if (have_found) {
            int out[64][MAXK], no = 0;
            for (int i = 0; i < np; i++) { for (int t = 0; t < k; t++) out[no][t] = md(prefix[i][t]); no++; }
            for (int i = 0; i < s - p; i++) { memcpy(out[no], rblk[found[i]], sizeof(int) * k); no++; }
            char path[1024];
            snprintf(path, sizeof path, "%s.sol", pre);
            FILE *f = fopen(path, "w");
            fprintf(f, "CPCW %d %d\n", v, k);
            for (int i = 0; i < no; i++) {
                qsort(out[i], k, sizeof(int), cmpint);
                for (int t = 0; t < k; t++) fprintf(f, "%d%c", out[i][t], t + 1 < k ? ' ' : '\n');
            }
            fclose(f);
            printf("FOUND v=%d k=%d seed=%llu attempt=%ld seconds=%.2f total_nodes=%lld\n", v, k,
                   (unsigned long long)seed, at, now() - t0, total_nodes);
            return 0;
        }
    }
    printf("DONE v=%d k=%d seed=%llu seconds=%.2f total_nodes=%lld exhausted_attempts=%lld mean_rows=%.1f\n", v, k,
           (unsigned long long)seed, now() - t0, total_nodes, exhausted, (double)total_rows / (attempts > 0 ? attempts : 1));
    return 3;
}
