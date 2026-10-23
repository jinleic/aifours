/* cpcw_ls.c -- representation R4 of the cpcw-optimal lane README: tabu local search for optimal (v,k,1) CPCW codes
 * (written for this lane; the move/tabu scheme follows the pattern of cdf-k5/code/cdf_ls.c, read-only).
 *
 * State: s codewords of k slots; slot 0 of every codeword is fixed at 0 (translation normalization), slots 1..k-1
 * take values in Z_v \ {0}, distinct within a codeword.  Every pair {a,b} of a codeword adds 1 to the count of its
 * class [a-b] (index d in 1..H, or index H+1 for the class v/2 when v is even).  Capacity cap[d] = 1 for usable
 * classes, 0 for v/2 and for classes in an optional prescribed leave.  Cost = sum_d max(0, cnt[d] - cap[d]);
 * cost 0 <=> the s codewords form an optimal (v,k,1) CPCW code (all classes distinct, v/2 unused).
 * Move: change one slot of a codeword that contains a conflicted pair; best non-tabu move (random tie-break);
 * aspiration when the move beats the best cost of the current descent; perturbation of pert random slots after
 * `stall` non-improving iterations.  Deterministic per seed (splitmix64); wall clock only for the time limit.
 *
 * Usage: cpcw_ls v k seed seconds outprefix [leave|-] [tl tr stall pert]
 *   leave: comma list of classes that must stay uncovered (default none: the search chooses the leave).
 * Output: outprefix.sol (strict "CPCW v k" certificate) on success; outprefix.ckpt (best state) every 600 s and at
 * exit; progress lines on stdout.  Exit 0 found, 3 time limit, 2 usage.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define MAXK 7
#define MAXS 16
static int v, k, s, H;
static int val[MAXS][MAXK], gbestval[MAXS][MAXK];
static int *cls, *cnt, *cap;
static int cost;
static long long *tabu;
static uint64_t rng;
static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int rndint(int n) { return (int)(rnd() % (uint64_t)n); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static int md(int x) { x %= v; return x < 0 ? x + v : x; }
static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }

/* increment/decrement class d, return cost change */
static inline int inc(int d) { int c0 = cnt[d]++; return c0 >= cap[d] ? 1 : 0; }
static inline int dec(int d) { int c1 = --cnt[d]; return c1 >= cap[d] ? -1 : 0; }

static int slot_apply(int b, int sl, int sign) {   /* pairs (sl, t) for t != sl */
    int dlt = 0;
    for (int t = 0; t < k; t++) if (t != sl) {
        int d = cls[md(val[b][sl] - val[b][t])];
        dlt += sign > 0 ? inc(d) : dec(d);
    }
    return dlt;
}
static void full_recount(void) {
    memset(cnt, 0, sizeof(int) * (H + 2));
    cost = 0;
    for (int b = 0; b < s; b++) for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) cost += inc(cls[md(val[b][i] - val[b][j])]);
}
static int in_block(int b, int y) { for (int t = 0; t < k; t++) if (val[b][t] == y) return 1; return 0; }
static void write_state(const char *path, int (*st)[MAXK], int c, long long it, double el) {
    FILE *f = fopen(path, "w");
    if (!f) return;
    fprintf(f, "# v=%d k=%d s=%d cost=%d iter=%lld elapsed=%.1f\n", v, k, s, c, it, el);
    for (int b = 0; b < s; b++) for (int t = 0; t < k; t++) fprintf(f, "%d%c", st[b][t], t + 1 < k ? ' ' : '\n');
    fclose(f);
}

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: cpcw_ls v k seed seconds outprefix [leave|-] [tl tr stall pert]\n"); return 2; }
    v = atoi(argv[1]); k = atoi(argv[2]);
    uint64_t seed = strtoull(argv[3], 0, 10);
    double limit = atof(argv[4]);
    const char *pre = argv[5];
    const char *leave = argc > 6 ? argv[6] : "-";
    int tl = argc > 7 ? atoi(argv[7]) : 10, tr = argc > 8 ? atoi(argv[8]) : 10;
    long long stall = argc > 9 ? atoll(argv[9]) : 200000;
    int pert = argc > 10 ? atoi(argv[10]) : 3;
    if (k < 3 || k > MAXK) { fprintf(stderr, "bad k\n"); return 2; }
    H = (v - 1) / 2; s = (v - 1) / (k * (k - 1));
    if (s < 1 || s > MAXS) { fprintf(stderr, "bad s\n"); return 2; }
    cls = malloc(sizeof(int) * v); cnt = calloc(H + 2, sizeof(int)); cap = malloc(sizeof(int) * (H + 2));
    for (int d = 0; d < v; d++) cls[d] = (2 * d == v) ? H + 1 : (d <= v - d ? d : v - d);
    for (int d = 1; d <= H; d++) cap[d] = 1;
    cap[H + 1] = 0; cap[0] = 0;
    int nleave = 0;
    if (strcmp(leave, "-") != 0) {
        const char *q = leave;
        while (*q) { int d = atoi(q); if (d < 1 || d > H) { fprintf(stderr, "bad leave class\n"); return 2; } cap[d] = 0; nleave++;
                     while (*q && *q != ',') q++; if (*q == ',') q++; }
    }
    rng = seed * 0x2545F4914F6CDD1DULL + 4242;
    tabu = calloc((size_t)s * MAXK * v, sizeof(long long));
    for (int b = 0; b < s; b++) {
        val[b][0] = 0;
        for (int t = 1; t < k; t++) { int y; do { y = 1 + rndint(v - 1); } while (in_block(b, y) && (val[b][t] = -1, 1) && in_block(b, y)); val[b][t] = y; }
    }
    /* make sure elements are distinct (re-draw duplicates) */
    for (int b = 0; b < s; b++) for (int t = 1; t < k; t++) {
        int dup;
        do { dup = 0; for (int u = 0; u < t; u++) if (val[b][u] == val[b][t]) dup = 1; if (dup) val[b][t] = 1 + rndint(v - 1); } while (dup);
    }
    full_recount();
    int bestcost = cost, gbest = cost;
    memcpy(gbestval, val, sizeof val);
    double t0 = now(), tlast = t0, tck = t0;
    long long it = 0, last_imp = 0;
    char path[1024];
    printf("start v=%d k=%d s=%d H=%d leave=%s (%d) seed=%llu cost=%d tl=%d tr=%d stall=%lld pert=%d\n", v, k, s, H, leave,
           nleave, (unsigned long long)seed, cost, tl, tr, stall, pert);
    fflush(stdout);
    static int cb[MAXS * MAXK], cs[MAXS * MAXK];
    while (cost > 0) {
        it++;
        if ((it & 255) == 0) {
            double t = now();
            if (t - t0 > limit) break;
            if (t - tlast > 30) { printf("it=%lld cost=%d best=%d gbest=%d t=%.0f\n", it, cost, bestcost, gbest, t - t0); fflush(stdout); tlast = t; }
            if (t - tck > 600) { snprintf(path, sizeof path, "%s.ckpt", pre); write_state(path, gbestval, gbest, it, t - t0); tck = t; }
        }
        /* candidate slots: free slots incident to a conflicted pair */
        int nc = 0;
        for (int b = 0; b < s; b++) {
            int mark[MAXK] = {0};
            for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) {
                int d = cls[md(val[b][i] - val[b][j])];
                if (cnt[d] > cap[d]) { mark[i] = 1; mark[j] = 1; }
            }
            for (int i = 1; i < k; i++) if (mark[i]) { cb[nc] = b; cs[nc] = i; nc++; }
            if (mark[0]) for (int i = 1; i < k; i++) if (!mark[i]) { cb[nc] = b; cs[nc] = i; nc++; }
        }
        int bestd = 1 << 30, nbest = 0, mb = -1, msl = -1, my = -1;
        for (int ci = 0; ci < nc; ci++) {
            int b = cb[ci], sl = cs[ci], oldv = val[b][sl];
            int rem = slot_apply(b, sl, -1);
            long long *tb = tabu + ((size_t)(b * MAXK + sl)) * v;
            for (int y = 1; y < v; y++) {
                if (y == oldv || in_block(b, y)) continue;
                val[b][sl] = y;
                int add = slot_apply(b, sl, +1);
                slot_apply(b, sl, -1);
                int d = rem + add;
                if (!(tb[y] <= it || cost + d < bestcost)) continue;
                if (d < bestd) { bestd = d; nbest = 1; mb = b; msl = sl; my = y; }
                else if (d == bestd && rndint(++nbest) == 0) { mb = b; msl = sl; my = y; }
            }
            val[b][sl] = oldv;
            slot_apply(b, sl, +1);
        }
        if (mb < 0) {
            int ci = rndint(nc); mb = cb[ci]; msl = cs[ci];
            do { my = 1 + rndint(v - 1); } while (in_block(mb, my));
        }
        {
            int oldv = val[mb][msl];
            cost += slot_apply(mb, msl, -1);
            val[mb][msl] = my;
            cost += slot_apply(mb, msl, +1);
            tabu[((size_t)(mb * MAXK + msl)) * v + oldv] = it + tl + rndint(tr + 1) + nc / 2;
        }
        if (cost < bestcost) { bestcost = cost; last_imp = it; if (cost < gbest) { gbest = cost; memcpy(gbestval, val, sizeof val); } }
        if (it - last_imp > stall) {
            for (int p = 0; p < pert; p++) {
                int b = rndint(s), sl = 1 + rndint(k - 1), y;
                do { y = 1 + rndint(v - 1); } while (in_block(b, y));
                cost += slot_apply(b, sl, -1); val[b][sl] = y; cost += slot_apply(b, sl, +1);
            }
            last_imp = it; bestcost = cost;
        }
    }
    double el = now() - t0;
    if (cost == 0) {
        snprintf(path, sizeof path, "%s.sol", pre);
        FILE *f = fopen(path, "w");
        fprintf(f, "CPCW %d %d\n", v, k);
        for (int b = 0; b < s; b++) {
            int e[MAXK]; memcpy(e, val[b], sizeof(int) * k); qsort(e, k, sizeof(int), cmpint);
            for (int t = 0; t < k; t++) fprintf(f, "%d%c", e[t], t + 1 < k ? ' ' : '\n');
        }
        fclose(f);
        snprintf(path, sizeof path, "%s.ckpt", pre); write_state(path, val, 0, it, el);
        printf("FOUND v=%d k=%d seed=%llu iters=%lld seconds=%.2f\n", v, k, (unsigned long long)seed, it, el);
        return 0;
    }
    snprintf(path, sizeof path, "%s.ckpt", pre); write_state(path, gbestval, gbest, it, el);
    printf("TIMEOUT v=%d k=%d seed=%llu iters=%lld seconds=%.2f best=%d\n", v, k, (unsigned long long)seed, it, el, gbest);
    return 3;
}
