/* wls_cdf.c -- weighted (breakout) local search for cyclic (v,k,1) difference families.
 *
 * State: t = (v-1)/(k(k-1)) blocks of k distinct elements of Z_v; class of d != 0 is min(d, v-d).
 * True cost = sum_c max(0, cnt_c - 1) (0 <=> difference family).
 * Search cost = sum_c w_c * |cnt_c - 1| with integer class weights w_c >= 1 (missing and repeated
 * classes are both penalised by their weight).
 * Each iteration evaluates every single-element move (block i, element x -> y not in block i) exactly
 * and takes the best one that is not tabu (short random tenure; aspiration on a new true best).
 * If the best weighted delta is >= 0 (a weighted local minimum), every violated class (cnt != 1) gains
 * +1 weight instead of moving; every `decay` weight updates all weights are scaled by 3/4 (floor, min 1).
 * Deterministic given the seed; the time limit only decides when to stop.
 *
 * usage: wls_cdf v k seed maxsec tenure_base tenure_rand decay outprefix
 * On success writes outprefix.sol ("CDF v k" then t lines) and exits 0; exits 1 on timeout.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define MAXV 2048
#define MAXK 12
#define MAXT 64

static int v, k, t, nc;
static int CL[MAXV];
static int blk[MAXT][MAXK];
static unsigned char inb[MAXT][MAXV];
static int cnt[MAXV];
static long long W[MAXV];
static int cost;
static long long tabu[MAXT][MAXV];
static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs >> 12; rs ^= rs << 25; rs ^= rs >> 27; return rs * 2685821657736338717ULL; }
static inline int rndint(int n) { return (int)(((rnd() >> 32) * (uint64_t)n) >> 32); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + ts.tv_nsec * 1e-9; }
static inline int dif(int a, int b) { int d = a - b; return d < 0 ? d + v : d; }
static inline int iabs(int x) { return x < 0 ? -x : x; }

static void full_recount(void) {
    memset(cnt, 0, sizeof(int) * nc);
    for (int i = 0; i < t; i++) for (int a = 0; a < k; a++) for (int b = a + 1; b < k; b++) cnt[CL[dif(blk[i][a], blk[i][b])]]++;
    cost = 0; for (int c = 0; c < nc; c++) if (cnt[c] > 1) cost += cnt[c] - 1;
}
static void write_state(const char *fn, const char *hdr) {
    FILE *f = fopen(fn, "w"); if (!f) return;
    if (hdr) fprintf(f, "%s", hdr);
    fprintf(f, "CDF %d %d\n", v, k);
    for (int i = 0; i < t; i++) { for (int a = 0; a < k; a++) fprintf(f, a ? " %d" : "%d", blk[i][a]); fprintf(f, "\n"); }
    fclose(f);
}

int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage: wls_cdf v k seed maxsec tenure_base tenure_rand decay outprefix\n"); return 2; }
    v = atoi(argv[1]); k = atoi(argv[2]); uint64_t seed = strtoull(argv[3], 0, 10); double maxsec = atof(argv[4]);
    int tb = atoi(argv[5]), tr = atoi(argv[6]); long long decay = atoll(argv[7]); const char *pre = argv[8];
    if ((v - 1) % (k * (k - 1))) { fprintf(stderr, "bad v,k\n"); return 2; }
    t = (v - 1) / (k * (k - 1)); nc = (v - 1) / 2;
    CL[0] = -1; for (int d = 1; d < v; d++) CL[d] = (d < v - d ? d : v - d) - 1;
    rs = seed * 0x9E3779B97F4A7C15ULL + 0x55AA55AAULL; for (int i = 0; i < 20; i++) rnd();
    for (int i = 0; i < t; i++) {
        memset(inb[i], 0, v);
        for (int a = 0; a < k; a++) { int x; do x = rndint(v); while (inb[i][x]); blk[i][a] = x; inb[i][x] = 1; }
    }
    for (int c = 0; c < nc; c++) W[c] = 1;
    full_recount();
    int gbest = cost; static int gblk[MAXT][MAXK]; memcpy(gblk, blk, sizeof(blk));
    double t0 = now(), tlast = t0, tck = t0;
    long long it = 0, nbump = 0, nmove = 0, hist[16] = {0};
    char fn[1024];
    printf("start v=%d k=%d t=%d seed=%llu cost=%d tb=%d tr=%d decay=%lld\n", v, k, t, (unsigned long long)seed, cost, tb, tr, decay);
    fflush(stdout);
    int solved = 0;
    while (1) {
        if (cost == 0) { solved = 1; break; }
        it++;
        if ((it & 255) == 0) {
            double tn = now();
            if (tn - t0 > maxsec) break;
            if (tn - tlast > 60) {
                long long wmax = 0, wsum = 0; for (int c = 0; c < nc; c++) { wsum += W[c]; if (W[c] > wmax) wmax = W[c]; }
                printf("it=%lld cost=%d gbest=%d moves=%lld bumps=%lld wmax=%lld wavg=%.2f t=%.0f\n", it, cost, gbest, nmove, nbump, wmax, (double)wsum / nc, tn - t0);
                fflush(stdout); tlast = tn;
            }
            if (tn - tck > 600) {
                int sv[MAXT][MAXK]; memcpy(sv, blk, sizeof(blk)); memcpy(blk, gblk, sizeof(blk));
                char hdr[256]; snprintf(hdr, sizeof hdr, "# checkpoint seed=%llu it=%lld gbest=%d t=%.0f\n", (unsigned long long)seed, it, gbest, tn - t0);
                snprintf(fn, sizeof fn, "%s.ckpt", pre); write_state(fn, hdr);
                memcpy(blk, sv, sizeof(blk)); tck = tn;
            }
        }
        long long bd = (long long)1 << 60; int bi = -1, bj = -1, by = -1, nties = 0, btrue = 0;
        for (int i = 0; i < t; i++) for (int j = 0; j < k; j++) {
            int x = blk[i][j], r[MAXK], nr = 0; long long remd = 0; int remt = 0;
            for (int m = 0; m < k; m++) if (m != j) {
                int c = CL[dif(x, blk[i][m])]; r[nr++] = c;
                remd += W[c] * (iabs(cnt[c] - 2) - iabs(cnt[c] - 1)); if (cnt[c] >= 2) remt--; cnt[c]--;
            }
            for (int y = 0; y < v; y++) {
                if (inb[i][y]) continue;
                int a[MAXK], na = 0, addt = 0; long long addd = 0;
                for (int m = 0; m < k; m++) if (m != j) {
                    int c = CL[dif(y, blk[i][m])];
                    addd += W[c] * (iabs(cnt[c]) - iabs(cnt[c] - 1)); if (cnt[c] >= 1) addt++; cnt[c]++; a[na++] = c;
                }
                for (int q = 0; q < na; q++) cnt[a[q]]--;
                long long d = remd + addd; int dt = remt + addt;
                if (tabu[i][y] > it && cost + dt >= gbest) continue;
                if (d < bd) { bd = d; bi = i; bj = j; by = y; nties = 1; btrue = dt; }
                else if (d == bd && rndint(++nties) == 0) { bi = i; bj = j; by = y; btrue = dt; }
            }
            for (int q = 0; q < nr; q++) cnt[r[q]]++;
        }
        (void)btrue;
        if (bi < 0 || bd >= 0) {
            /* weighted local minimum: bump violated classes */
            for (int c = 0; c < nc; c++) if (cnt[c] != 1) W[c]++;
            nbump++;
            if (decay > 0 && nbump % decay == 0) for (int c = 0; c < nc; c++) { W[c] = (W[c] * 3) / 4; if (W[c] < 1) W[c] = 1; }
            if (bi < 0) continue;
            if (bd > 0) continue;
            /* bd == 0: plateau move allowed after bumping */
        }
        int x = blk[bi][bj];
        for (int m = 0; m < k; m++) if (m != bj) { int c = CL[dif(x, blk[bi][m])]; if (cnt[c] >= 2) cost--; cnt[c]--; }
        inb[bi][x] = 0; blk[bi][bj] = by; inb[bi][by] = 1;
        for (int m = 0; m < k; m++) if (m != bj) { int c = CL[dif(by, blk[bi][m])]; if (cnt[c] >= 1) cost++; cnt[c]++; }
        tabu[bi][x] = it + tb + (tr > 0 ? rndint(tr + 1) : 0);
        nmove++;
        if (cost < 16) hist[cost]++;
        if (cost < gbest) { gbest = cost; memcpy(gblk, blk, sizeof(blk)); }
    }
    double el = now() - t0;
    printf("end solved=%d it=%lld moves=%lld bumps=%lld gbest=%d secs=%.1f\n", solved, it, nmove, nbump, gbest, el);
    printf("hist"); for (int c = 0; c < 16; c++) printf(" %lld", hist[c]); printf("\n");
    if (solved) {
        full_recount();
        if (cost != 0) { printf("internal error: cost %d\n", cost); return 3; }
        char hdr[256]; snprintf(hdr, sizeof hdr, "# wls_cdf seed=%llu it=%lld secs=%.1f\n", (unsigned long long)seed, it, el);
        snprintf(fn, sizeof fn, "%s.sol", pre); write_state(fn, hdr);
        printf("SOLVED written %s\n", fn);
        for (int i = 0; i < t; i++) { for (int a = 0; a < k; a++) printf(a ? " %d" : "%d", blk[i][a]); printf("\n"); }
    }
    fflush(stdout);
    return solved ? 0 : 1;
}
