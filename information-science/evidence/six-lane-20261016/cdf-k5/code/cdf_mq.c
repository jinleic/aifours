/* cdf_mq.c -- cyclic (v,5,1) difference families over Z_v = Z_m x Z_q (gcd(m,q) = 1, m,q odd) built from
 * mu-stable blocks and free pairs {B, mu B}, mu = (1 mod m, -1 mod q).
 *
 * Classes of Z_v: [(a,y)] = [(-a,-y)].  Items:
 *   orbit item  (+-a,+-y), a != 0, y != 0  = the two classes [(a,y)], [(a,-y)]      ((m-1)(q-1)/4 items)
 *   pure item   y != 0                     = the class [(0,y)]                       ((q-1)/2 items)
 *   K item      a != 0                     = the class [(a,0)]                       ((m-1)/2 items)
 * Stable rows (each covers its orbit items completely), enumerated exactly and deduplicated up to translation and
 * negation of the block in Z_v:
 *   T1  {(0,0),(a1,+-y1),(a2,+-y2)}          T1' {(0,0),(+-a1,y1),(+-a2,y2)}
 *   T3' {(0,0),(0,f1),(0,f2),(a,y),(-a,y)}    T3  {(0,0),(e1,0),(e2,0),(b,z),(b,-z)}
 *   T5  5 points of {0} x Z_q (optional)       T5' 5 points of Z_m x {0} (optional)
 * A free pair is a block B with 5 distinct labels and 5 distinct y's whose 10 classes lie in 10 distinct orbit
 * items, together with mu*B = {(a,-y)}; the pair covers those 10 orbit items completely and nothing else.
 * Search per configuration: place f free pairs at random (disjoint orbit items), then exact cover of all remaining
 * items by stable rows (bitset Algorithm X, min-column, randomized, node limit).  Every assembled family is
 * re-checked in-program (full difference multiset in Z_v) before it is written.
 *
 * Usage: cdf_mq v m seed seconds outprefix f [nodelimit] [use_t5] [typemask]
 *   typemask: bit t allows stable type t (1 T1, 2 T1', 3 T3', 4 T3, 5 T5, 6 T5'); default all.
 * Exit 0 found (outprefix.sol), 3 time limit.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define W 4
typedef struct { uint64_t m[W]; } mask_t;
static int v, m, q, M2, Q2, NO, NI, n, f;
static int *crt;               /* crt[a*q+y] */
static int *cls_v;             /* class rep of d in Z_v: min(d, v-d) */
static uint64_t rng;
static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int rndint(int k) { return (int)(rnd() % (uint64_t)k); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static inline int mm(int a) { a %= m; return a < 0 ? a + m : a; }
static inline int mq(int y) { y %= q; return y < 0 ? y + q : y; }
static inline void setbit(mask_t *x, int c) { x->m[c >> 6] |= 1ULL << (c & 63); }
static inline int getbit(const mask_t *x, int c) { return (int)(x->m[c >> 6] >> (c & 63) & 1); }
static inline int disj(const mask_t *a, const mask_t *b) { uint64_t x = 0; for (int w = 0; w < W; w++) x |= a->m[w] & b->m[w]; return x == 0; }

/* item of the class of difference (da,dy); kind: 0 orbit, 1 pure, 2 K, -1 zero */
static int item_of(int da, int dy, int *kind) {
    da = mm(da); dy = mq(dy);
    if (da == 0 && dy == 0) { *kind = -1; return -1; }
    int a = da <= M2 ? da : m - da, y = dy <= Q2 ? dy : q - dy;
    if (da == 0) { *kind = 1; return NO + (y - 1); }
    if (dy == 0) { *kind = 2; return NO + Q2 + (a - 1); }
    *kind = 0; return (a - 1) * Q2 + (y - 1);
}
static int cmpint(const void *x, const void *y) { return *(const int *)x - *(const int *)y; }
static int zof(int a, int y) { return crt[mm(a) * q + mq(y)]; }

/* block given as 5 (a,y) points.  Returns 1 and fills the class list (Z_v classes) if the 10 classes are distinct. */
static int block_classes_v(int pts[5][2], int *cl) {
    int z[5];
    for (int i = 0; i < 5; i++) z[i] = zof(pts[i][0], pts[i][1]);
    int k = 0;
    for (int i = 0; i < 5; i++) for (int j = i + 1; j < 5; j++) {
        int d = z[j] - z[i]; d %= v; if (d < 0) d += v;
        int c = cls_v[d];
        if (c == 0) return 0;
        for (int t = 0; t < k; t++) if (cl[t] == c) return 0;
        cl[k++] = c;
    }
    return 1;
}
/* stable row: items covered; requires every orbit item to receive both of its classes */
static int stable_items(int pts[5][2], int *items, int *nit) {
    int cl[10];
    if (!block_classes_v(pts, cl)) return 0;
    int it[10], kd[10], k = 0;
    for (int i = 0; i < 5; i++) for (int j = i + 1; j < 5; j++) { it[k] = item_of(pts[j][0] - pts[i][0], pts[j][1] - pts[i][1], &kd[k]); k++; }
    int ni = 0;
    for (int t = 0; t < 10; t++) {
        int mult = 0;
        for (int s = 0; s < 10; s++) if (it[s] == it[t]) mult++;
        if (kd[t] == 0 && mult != 2) return 0;
        if (kd[t] != 0 && mult != 1) return 0;
        int seen = 0;
        for (int s = 0; s < ni; s++) if (items[s] == it[t]) seen = 1;
        if (!seen) items[ni++] = it[t];
    }
    *nit = ni;
    return 1;
}
static void canon_v(int pts[5][2], int *out) {
    int z[5], best[5], cand[5], have = 0;
    for (int i = 0; i < 5; i++) z[i] = zof(pts[i][0], pts[i][1]);
    for (int s = 0; s < 2; s++) for (int t = 0; t < 5; t++) {
        for (int i = 0; i < 5; i++) { int d = (s ? -z[i] : z[i]) - (s ? -z[t] : z[t]); d %= v; if (d < 0) d += v; cand[i] = d; }
        qsort(cand, 5, sizeof(int), cmpint);
        if (!have || memcmp(cand, best, sizeof cand) < 0) { memcpy(best, cand, sizeof cand); have = 1; }
    }
    memcpy(out, best, sizeof best);
}

/* row storage */
static int nrows, caprows;
static int (*rpts)[5][2]; static mask_t *rmask; static unsigned char (*ritem)[10]; static unsigned char *rnit; static unsigned char *rtype;
/* hash set of canonical blocks */
static uint64_t *hset; static size_t hcap;
static int hinsert(const int *c) {
    uint64_t k = 1469598103934665603ULL;
    for (int i = 0; i < 5; i++) { k ^= (uint64_t)c[i] + 1; k *= 1099511628211ULL; }
    if (k == 0) k = 1;
    size_t h = k & (hcap - 1);
    while (hset[h]) { if (hset[h] == k) return 0; h = (h + 1) & (hcap - 1); }
    hset[h] = k; return 1;
}
static void add_stable(int pts[5][2], int type) {
    int items[10], ni;
    if (!stable_items(pts, items, &ni)) return;
    int c[5]; canon_v(pts, c);
    if (!hinsert(c)) return;
    if (nrows == caprows) { caprows = caprows ? 2 * caprows : 1 << 16;
        rpts = realloc(rpts, sizeof(*rpts) * caprows); rmask = realloc(rmask, sizeof(mask_t) * caprows);
        ritem = realloc(ritem, sizeof(*ritem) * caprows); rnit = realloc(rnit, caprows); rtype = realloc(rtype, caprows); }
    memcpy(rpts[nrows], pts, sizeof(int) * 10);
    memset(&rmask[nrows], 0, sizeof(mask_t));
    for (int t = 0; t < ni; t++) { ritem[nrows][t] = (unsigned char)items[t]; setbit(&rmask[nrows], items[t]); }
    rnit[nrows] = (unsigned char)ni; rtype[nrows] = (unsigned char)type;
    nrows++;
}

/* ---------------- exact cover over remaining items ---------------- */
static int **lists; static int chosen[64]; static long long nodes, nodelimit;
static int nitems_rem; static mask_t remmask;
static int xc(int depth, int cnt, mask_t cov) {
    /* cov = items already covered (within remaining set) */
    int done = 1;
    for (int w = 0; w < W; w++) if ((cov.m[w] & remmask.m[w]) != remmask.m[w]) done = 0;
    if (done) return depth + 1000;       /* signal success with depth */
    if (++nodes > nodelimit) return -1;
    int *lst = lists[depth];
    static int cc[W * 64];
    memset(cc, 0, sizeof cc);
    for (int i = 0; i < cnt; i++) { int r = lst[i]; for (int j = 0; j < rnit[r]; j++) cc[ritem[r][j]]++; }
    int best = -1, bs = 1 << 30, ties = 0;
    for (int c = 0; c < NI; c++) {
        if (!getbit(&remmask, c) || getbit(&cov, c)) continue;
        if (cc[c] < bs) { bs = cc[c]; best = c; ties = 1; } else if (cc[c] == bs && rndint(++ties) == 0) best = c;
    }
    if (bs == 0) return 0;
    int *nxt = lists[depth + 1];
    for (int i = 0; i < cnt; i++) {
        int x = lst[i];
        if (!getbit(&rmask[x], best)) continue;
        int k = 0;
        for (int j = 0; j < cnt; j++) { int y = lst[j]; if (disj(&rmask[x], &rmask[y])) nxt[k++] = y; }
        chosen[depth] = x;
        mask_t nc = cov; for (int w = 0; w < W; w++) nc.m[w] |= rmask[x].m[w];
        int r = xc(depth + 1, k, nc);
        if (r != 0) return r;
    }
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 7) { fprintf(stderr, "usage: cdf_mq v m seed seconds outprefix f [nodelimit] [use_t5] [typemask]\n"); return 2; }
    v = atoi(argv[1]); m = atoi(argv[2]); uint64_t seed = strtoull(argv[3], 0, 10); double limit = atof(argv[4]);
    const char *pre = argv[5]; f = atoi(argv[6]);
    nodelimit = argc > 7 ? atoll(argv[7]) : 2000000; int use_t5 = argc > 8 ? atoi(argv[8]) : 0;
    int typemask = argc > 9 ? atoi(argv[9]) : 0x7e;
    if (v % m) { fprintf(stderr, "m must divide v\n"); return 2; }
    q = v / m;
    { int a = m, b = q; while (b) { int t = a % b; a = b; b = t; } if (a != 1 || m % 2 == 0 || q % 2 == 0) { fprintf(stderr, "need coprime odd m,q\n"); return 2; } }
    if ((v - 1) % 20) { fprintf(stderr, "v != 1 mod 20\n"); return 2; }
    n = (v - 1) / 20; M2 = (m - 1) / 2; Q2 = (q - 1) / 2; NO = M2 * Q2; NI = NO + Q2 + M2;
    if (NI > W * 64) { fprintf(stderr, "too many items %d\n", NI); return 2; }
    rng = seed * 0x2545F4914F6CDD1DULL + 987654321;
    crt = malloc(sizeof(int) * m * q);
    for (int z = 0; z < v; z++) crt[(z % m) * q + (z % q)] = z;
    cls_v = malloc(sizeof(int) * v);
    for (int d = 0; d < v; d++) cls_v[d] = d <= (v - 1) / 2 ? d : v - d;
    hcap = 1 << 24; hset = calloc(hcap, sizeof(uint64_t));
    double t0 = now();
    /* enumerate stable rows */
    if (typemask >> 1 & 1) for (int a1 = 1; a1 < m; a1++) for (int a2 = 1; a2 < m; a2++) if (a1 != a2)
        for (int y1 = 1; y1 < q; y1++) for (int y2 = 1; y2 < q; y2++) {
            int p1[5][2] = {{0, 0}, {a1, y1}, {a1, mq(-y1)}, {a2, y2}, {a2, mq(-y2)}}; add_stable(p1, 1);
        }
    int n1 = nrows;
    if (typemask >> 2 & 1) for (int a1 = 1; a1 < m; a1++) for (int a2 = 1; a2 < m; a2++)
        for (int y1 = 1; y1 < q; y1++) for (int y2 = 1; y2 < q; y2++) {
            int p2[5][2] = {{0, 0}, {a1, y1}, {mm(-a1), y1}, {a2, y2}, {mm(-a2), y2}}; add_stable(p2, 2);
        }
    int n2 = nrows;
    if (typemask >> 3 & 1) for (int f1 = 1; f1 < q; f1++) for (int f2 = f1 + 1; f2 < q; f2++) for (int a = 1; a < m; a++) for (int y = 0; y < q; y++) {
        int p3[5][2] = {{0, 0}, {0, f1}, {0, f2}, {a, y}, {mm(-a), y}}; add_stable(p3, 3);
    }
    int n3 = nrows;
    if (typemask >> 4 & 1) for (int e1 = 1; e1 < m; e1++) for (int e2 = e1 + 1; e2 < m; e2++) for (int b = 0; b < m; b++) for (int z = 1; z < q; z++) {
        int p4[5][2] = {{0, 0}, {e1, 0}, {e2, 0}, {b, z}, {b, mq(-z)}}; add_stable(p4, 4);
    }
    int n4 = nrows;
    if (use_t5) {
        for (int y1 = 1; y1 < q; y1++) for (int y2 = y1 + 1; y2 < q; y2++) for (int y3 = y2 + 1; y3 < q; y3++) for (int y4 = y3 + 1; y4 < q; y4++) {
            int p5[5][2] = {{0, 0}, {0, y1}, {0, y2}, {0, y3}, {0, y4}}; add_stable(p5, 5);
        }
        for (int a1 = 1; a1 < m; a1++) for (int a2 = a1 + 1; a2 < m; a2++) for (int a3 = a2 + 1; a3 < m; a3++) for (int a4 = a3 + 1; a4 < m; a4++) {
            int p6[5][2] = {{0, 0}, {a1, 0}, {a2, 0}, {a3, 0}, {a4, 0}}; add_stable(p6, 6);
        }
    }
    printf("start v=%d m=%d q=%d n=%d f=%d items=%d (orbit %d pure %d K %d) rows T1=%d T1'=%d T3'=%d T3=%d T5/T5'=%d seed=%llu nodelimit=%lld (setup %.1fs)\n",
           v, m, q, n, f, NI, NO, Q2, M2, n1, n2 - n1, n3 - n2, n4 - n3, nrows - n4, (unsigned long long)seed, nodelimit, now() - t0);
    fflush(stdout);
    lists = calloc(70, sizeof(int *));
    for (int d = 0; d < 70; d++) lists[d] = malloc(sizeof(int) * (nrows + 1));
    long long configs = 0, xc_fail_exhausted = 0, xc_fail_limit = 0, total_nodes = 0;
    double tl = now();
    int freeB[64][5][2];
    while (now() - t0 < limit) {
        /* random free pairs */
        mask_t used; memset(&used, 0, sizeof used);
        int placed = 0, tries = 0;
        while (placed < f && tries < 1000000) {
            tries++;
            int pts[5][2], la[5], ok = 1;
            for (int i = 0; i < 5 && ok; i++) {
                pts[i][0] = rndint(m); pts[i][1] = rndint(q);
                for (int j = 0; j < i; j++) if (pts[j][0] == pts[i][0] || pts[j][1] == pts[i][1]) ok = 0;
                la[i] = pts[i][0];
            }
            (void)la;
            if (!ok) continue;
            int cl[10];
            if (!block_classes_v(pts, cl)) continue;
            int its[10], k = 0;
            for (int i = 0; i < 5 && ok; i++) for (int j = i + 1; j < 5 && ok; j++) {
                int kd; int it = item_of(pts[j][0] - pts[i][0], pts[j][1] - pts[i][1], &kd);
                if (kd != 0 || getbit(&used, it)) ok = 0;
                for (int t = 0; t < k && ok; t++) if (its[t] == it) ok = 0;
                its[k++] = it;
            }
            if (!ok) continue;
            for (int t = 0; t < 10; t++) setbit(&used, its[t]);
            memcpy(freeB[placed++], pts, sizeof pts);
        }
        if (placed < f) continue;
        configs++;
        memset(&remmask, 0, sizeof remmask);
        for (int c = 0; c < NI; c++) if (!getbit(&used, c)) setbit(&remmask, c);
        int cnt = 0;
        for (int r = 0; r < nrows; r++) if ((typemask >> rtype[r] & 1) && disj(&rmask[r], &used)) lists[0][cnt++] = r;
        for (int i = cnt - 1; i > 0; i--) { int j = rndint(i + 1); int t = lists[0][i]; lists[0][i] = lists[0][j]; lists[0][j] = t; }
        mask_t cov; memset(&cov, 0, sizeof cov);
        nodes = 0;
        int res = xc(0, cnt, cov);
        total_nodes += nodes;
        if (res >= 1000) {
            int depth = res - 1000;
            /* assemble */
            int fam[128][5], nb = 0;
            for (int i = 0; i < f; i++) {
                for (int t = 0; t < 5; t++) fam[nb][t] = zof(freeB[i][t][0], freeB[i][t][1]); nb++;
                for (int t = 0; t < 5; t++) fam[nb][t] = zof(freeB[i][t][0], -freeB[i][t][1]); nb++;
            }
            for (int d = 0; d < depth; d++) { for (int t = 0; t < 5; t++) fam[nb][t] = zof(rpts[chosen[d]][t][0], rpts[chosen[d]][t][1]); nb++; }
            int *count = calloc(v, sizeof(int));
            for (int b = 0; b < nb; b++) for (int i = 0; i < 5; i++) for (int j = 0; j < 5; j++) if (i != j) { int d = (fam[b][i] - fam[b][j]) % v; if (d < 0) d += v; count[d]++; }
            int good = nb == n && count[0] == 0;
            for (int d = 1; d < v && good; d++) if (count[d] != 1) good = 0;
            free(count);
            if (!good) { printf("INTERNAL: assembled family fails (nb=%d)\n", nb); fflush(stdout); continue; }
            char path[1024]; snprintf(path, sizeof path, "%s.sol", pre);
            FILE *fo = fopen(path, "w");
            fprintf(fo, "CDF %d 5\n", v);
            for (int b = 0; b < nb; b++) { qsort(fam[b], 5, sizeof(int), cmpint); fprintf(fo, "%d %d %d %d %d\n", fam[b][0], fam[b][1], fam[b][2], fam[b][3], fam[b][4]); }
            fclose(fo);
            int types[8] = {0}; for (int d = 0; d < depth; d++) types[rtype[chosen[d]]]++;
            printf("FOUND v=%d seed=%llu configs=%lld seconds=%.2f total_nodes=%lld stable=%d (T1 %d T1' %d T3' %d T3 %d T5 %d T5' %d) free_pairs=%d\n",
                   v, (unsigned long long)seed, configs, now() - t0, total_nodes, depth, types[1], types[2], types[3], types[4], types[5], types[6], f);
            return 0;
        } else if (res < 0) xc_fail_limit++; else xc_fail_exhausted++;
        if (now() - tl > 30) {
            printf("configs=%lld exhausted=%lld limit=%lld last_rows=%d total_nodes=%lld t=%.0f\n", configs, xc_fail_exhausted,
                   xc_fail_limit, cnt, total_nodes, now() - t0);
            fflush(stdout); tl = now();
        }
    }
    printf("TIMEOUT v=%d seed=%llu configs=%lld exhausted=%lld limit=%lld seconds=%.2f\n", v, (unsigned long long)seed, configs,
           xc_fail_exhausted, xc_fail_limit, now() - t0);
    return 3;
}
