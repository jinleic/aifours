/* cdf_walk.c -- WalkSAT-style focused local search for cyclic (v,5,1) difference families.
 *
 * State: n base blocks (5 elements of Z_v each).  cnt[c] = number of unordered in-block pairs with difference class
 * c = min(d, v-d).  Cost = number of classes with cnt = 0 (= total excess, since the pair count is exactly (v-1)/2).
 * Step: pick a random uncovered class u; candidate moves are "move element j of block b to y = x +- u" for every
 * block b, anchor x in b and other position j (so the new pair {x,y} covers u); evaluate each candidate's exact
 * cost change; with probability p_noise take a random non-tabu candidate, else the best non-tabu one (ties random;
 * aspiration if it beats the best cost so far).  Moved position is tabu for tt steps.
 *
 * Usage: cdf_walk v seed seconds outprefix [noise_permille] [tabu] [restart_steps]
 * Exit 0 found (writes outprefix.sol), 3 time limit.  Periodic progress lines and outprefix.ckpt (best state).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define K 5
#define MAXN 64

static int v, H, n;
static int blk[MAXN][K], best_blk[MAXN][K];
static int *cls, *cnt;
static int *unc, *uncpos, nunc;     /* set of uncovered classes */
static long long tabu_until[MAXN][K];
static uint64_t rng;
static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int rndint(int m) { return (int)(rnd() % (uint64_t)m); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static inline int md(int x) { x %= v; return x < 0 ? x + v : x; }

static inline void inc(int c) { if (cnt[c]++ == 0) { int p = uncpos[c], last = unc[--nunc]; unc[p] = last; uncpos[last] = p; uncpos[c] = -1; } }
static inline void dec(int c) { if (--cnt[c] == 0) { uncpos[c] = nunc; unc[nunc++] = c; } }

/* exact cost change of setting blk[b][j] = y (y not in block) */
static int delta_move(int b, int j, int y) {
    int x = blk[b][j], d = 0;
    int rem[K - 1], add[K - 1], m = 0;
    for (int t = 0; t < K; t++) if (t != j) { rem[m] = cls[md(x - blk[b][t])]; add[m] = cls[md(y - blk[b][t])]; m++; }
    for (int t = 0; t < m; t++) { cnt[rem[t]]--; if (cnt[rem[t]] == 0) d++; }
    for (int t = 0; t < m; t++) { if (cnt[add[t]] == 0) d--; cnt[add[t]]++; }
    for (int t = 0; t < m; t++) cnt[add[t]]--;
    for (int t = 0; t < m; t++) cnt[rem[t]]++;
    return d;
}
static void apply_move(int b, int j, int y) {
    int x = blk[b][j];
    for (int t = 0; t < K; t++) if (t != j) dec(cls[md(x - blk[b][t])]);
    blk[b][j] = y;
    for (int t = 0; t < K; t++) if (t != j) inc(cls[md(y - blk[b][t])]);
}
static int in_block(int b, int y) { for (int t = 0; t < K; t++) if (blk[b][t] == y) return 1; return 0; }

static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static void write_blocks(const char *path, int (*st)[K], const char *hdr) {
    FILE *f = fopen(path, "w");
    if (!f) return;
    fprintf(f, "%s", hdr);
    for (int b = 0; b < n; b++) { int e[K]; memcpy(e, st[b], sizeof(e)); qsort(e, K, sizeof(int), cmpint);
        for (int t = 0; t < K; t++) fprintf(f, "%d%c", e[t], t + 1 < K ? ' ' : '\n'); }
    fclose(f);
}

static void random_state(void) {
    memset(cnt, 0, sizeof(int) * (H + 1));
    nunc = 0;
    for (int c = 1; c <= H; c++) { uncpos[c] = nunc; unc[nunc++] = c; }
    for (int b = 0; b < n; b++) {
        int ok;
        do {
            ok = 1;
            for (int t = 0; t < K; t++) blk[b][t] = rndint(v);
            for (int s = 0; s < K; s++) for (int t = s + 1; t < K; t++) if (blk[b][s] == blk[b][t]) ok = 0;
        } while (!ok);
        for (int s = 0; s < K; s++) for (int t = s + 1; t < K; t++) inc(cls[md(blk[b][s] - blk[b][t])]);
    }
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: cdf_walk v seed seconds outprefix [noise_permille] [tabu] [restart_steps]\n"); return 2; }
    v = atoi(argv[1]); uint64_t seed = strtoull(argv[2], 0, 10); double limit = atof(argv[3]); const char *pre = argv[4];
    int noise = argc > 5 ? atoi(argv[5]) : 30, tt = argc > 6 ? atoi(argv[6]) : 10;
    long long restart = argc > 7 ? atoll(argv[7]) : 0;
    if ((v - 1) % 20) { fprintf(stderr, "v != 1 mod 20\n"); return 2; }
    H = (v - 1) / 2; n = (v - 1) / 20;
    if (n > MAXN) { fprintf(stderr, "n too large\n"); return 2; }
    rng = seed * 0x2545F4914F6CDD1DULL + 99991;
    cls = malloc(sizeof(int) * v); cnt = calloc(H + 1, sizeof(int)); unc = malloc(sizeof(int) * (H + 1)); uncpos = malloc(sizeof(int) * (H + 1));
    for (int d = 0; d < v; d++) cls[d] = d <= H ? d : v - d;
    random_state();
    int bestc = nunc; memcpy(best_blk, blk, sizeof(blk));
    double t0 = now(), tlast = t0, tck = t0;
    long long step = 0, last_restart = 0;
    long long hist[8] = {0};
    char path[1024], hdr[256];
    printf("start v=%d n=%d seed=%llu noise=%d tabu=%d restart=%lld cost=%d\n", v, n, (unsigned long long)seed, noise, tt, restart, nunc);
    fflush(stdout);
    static int cb[MAXN * K * (K - 1) * 2], cj[MAXN * K * (K - 1) * 2], cy[MAXN * K * (K - 1) * 2], cd[MAXN * K * (K - 1) * 2];
    while (nunc > 0) {
        step++;
        if (nunc < 8) hist[nunc]++;
        if ((step & 1023) == 0) {
            double t = now();
            if (t - t0 > limit) break;
            if (t - tlast > 30) {
                printf("step=%lld cost=%d best=%d h1=%lld h2=%lld h3=%lld t=%.0f\n", step, nunc, bestc, hist[1], hist[2], hist[3], t - t0);
                fflush(stdout); tlast = t;
            }
            if (t - tck > 600) { snprintf(path, sizeof path, "%s.ckpt", pre); snprintf(hdr, sizeof hdr, "# v=%d cost=%d step=%lld\n", v, bestc, step);
                write_blocks(path, best_blk, hdr); tck = t; }
        }
        if (restart && step - last_restart > restart) { random_state(); last_restart = step; }
        int u = unc[rndint(nunc)];
        int m = 0, bestd = 1 << 30;
        for (int b = 0; b < n; b++) for (int i = 0; i < K; i++) for (int s = 0; s < 2; s++) {
            int y = md(blk[b][i] + (s ? u : -u));
            if (in_block(b, y)) continue;
            for (int j = 0; j < K; j++) {
                if (j == i) continue;
                int d = delta_move(b, j, y);
                int ok = tabu_until[b][j] <= step || nunc + d < bestc;
                if (!ok) continue;
                cb[m] = b; cj[m] = j; cy[m] = y; cd[m] = d; m++;
                if (d < bestd) bestd = d;
            }
        }
        if (m == 0) continue;
        int pick;
        if (rndint(1000) < noise) pick = rndint(m);
        else {
            int ties = 0; pick = 0;
            for (int q = 0; q < m; q++) if (cd[q] == bestd && rndint(++ties) == 0) pick = q;
        }
        apply_move(cb[pick], cj[pick], cy[pick]);
        tabu_until[cb[pick]][cj[pick]] = step + tt + rndint(tt + 1);
        if (nunc < bestc) { bestc = nunc; memcpy(best_blk, blk, sizeof(blk)); }
    }
    double el = now() - t0;
    if (nunc == 0) {
        snprintf(path, sizeof path, "%s.sol", pre);
        snprintf(hdr, sizeof hdr, "CDF %d %d\n", v, K);
        write_blocks(path, blk, hdr);
        printf("FOUND v=%d seed=%llu steps=%lld seconds=%.2f\n", v, (unsigned long long)seed, step, el);
        return 0;
    }
    snprintf(path, sizeof path, "%s.ckpt", pre); snprintf(hdr, sizeof hdr, "# v=%d cost=%d step=%lld\n", v, bestc, step);
    write_blocks(path, best_blk, hdr);
    printf("TIMEOUT v=%d seed=%llu steps=%lld seconds=%.2f best=%d h1=%lld h2=%lld\n", v, (unsigned long long)seed, step, el, bestc, hist[1], hist[2]);
    return 3;
}
