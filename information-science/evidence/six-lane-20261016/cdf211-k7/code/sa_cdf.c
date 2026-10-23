/* sa_cdf.c -- simulated annealing for cyclic (v,k,1) difference families, t = (v-1)/(k(k-1)).
 *
 * State: t blocks of k distinct elements of Z_v. Class of d != 0: min(d, v-d). Cost = sum_c
 * max(0, cnt_c - 1) (0 <=> difference family). Proposal: with probability pf (per mille) an element
 * that lies in a colliding pair, otherwise a uniform element; the new value y is uniform outside
 * the block. Metropolis acceptance at temperature T. The temperature follows repeated cycles from
 * Thi down to Tlo (geometric) over `cyc` proposals; every cycle starts from the current state.
 * Deterministic given the seed; the time limit only decides when to stop.
 *
 * usage: sa_cdf v k seed maxsec Thi Tlo cyc pf outprefix
 * On success writes outprefix.sol ("CDF v k" then t lines) and exits 0; exits 1 on timeout.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <math.h>
#include <time.h>

#define MAXV 2048
#define MAXK 12
#define MAXT 64

static int v, k, t, nc;
static int CL[MAXV];
static int blk[MAXT][MAXK];
static unsigned char inb[MAXT][MAXV];
static int cnt[MAXV];
static int cost;
static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs >> 12; rs ^= rs << 25; rs ^= rs >> 27; return rs * 2685821657736338717ULL; }
static inline uint32_t rnd32(void) { return (uint32_t)(rnd() >> 32); }
static inline int rndint(int n) { return (int)(((uint64_t)rnd32() * (uint64_t)n) >> 32); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + ts.tv_nsec * 1e-9; }
static inline int dif(int a, int b) { int d = a - b; return d < 0 ? d + v : d; }

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
    if (argc < 10) { fprintf(stderr, "usage: sa_cdf v k seed maxsec Thi Tlo cyc pf outprefix\n"); return 2; }
    v = atoi(argv[1]); k = atoi(argv[2]); uint64_t seed = strtoull(argv[3], 0, 10); double maxsec = atof(argv[4]);
    double Thi = atof(argv[5]), Tlo = atof(argv[6]); long long cyc = atoll(argv[7]); int pf = atoi(argv[8]);
    const char *pre = argv[9];
    if ((v - 1) % (k * (k - 1))) { fprintf(stderr, "bad v,k\n"); return 2; }
    t = (v - 1) / (k * (k - 1)); nc = (v - 1) / 2;
    CL[0] = -1; for (int d = 1; d < v; d++) CL[d] = (d < v - d ? d : v - d) - 1;
    rs = seed * 0x9E3779B97F4A7C15ULL + 0x7654321ULL; for (int i = 0; i < 20; i++) rnd();
    for (int i = 0; i < t; i++) {
        memset(inb[i], 0, v);
        for (int a = 0; a < k; a++) { int x; do x = rndint(v); while (inb[i][x]); blk[i][a] = x; inb[i][x] = 1; }
    }
    full_recount();
    int gbest = cost; static int gblk[MAXT][MAXK]; memcpy(gblk, blk, sizeof(blk));
    double t0 = now(), tlast = t0, tck = t0;
    long long it = 0, acc = 0, ncyc = 0, hist[16] = {0};
    char fn[1024];
    printf("start v=%d k=%d t=%d seed=%llu cost=%d Thi=%g Tlo=%g cyc=%lld pf=%d\n", v, k, t, (unsigned long long)seed, cost, Thi, Tlo, cyc, pf);
    fflush(stdout);
    uint32_t thr[64];
    double T = Thi, fac = pow(Tlo / Thi, 1.0 / (double)(cyc > 1 ? cyc : 2));
    long long cpos = 0;
    int solved = 0;
    /* conflict element sampling: pick a random colliding class occurrence via rejection on pairs */
    while (1) {
        if ((it & 0xFFFF) == 0) {
            for (int d = 0; d < 64; d++) { double p = exp(-(double)d / T); thr[d] = p >= 1.0 ? 0xFFFFFFFFu : (uint32_t)(p * 4294967296.0); }
            double tn = now();
            if (tn - t0 > maxsec) break;
            if (tn - tlast > 60) {
                printf("it=%lld cost=%d gbest=%d T=%.4f acc=%lld cycles=%lld t=%.0f\n", it, cost, gbest, T, acc, ncyc, tn - t0);
                fflush(stdout); tlast = tn;
            }
            if (tn - tck > 600) {
                int sv[MAXT][MAXK]; memcpy(sv, blk, sizeof(blk)); memcpy(blk, gblk, sizeof(blk));
                char hdr[256]; snprintf(hdr, sizeof hdr, "# checkpoint seed=%llu it=%lld gbest=%d t=%.0f\n", (unsigned long long)seed, it, gbest, tn - t0);
                snprintf(fn, sizeof fn, "%s.ckpt", pre); write_state(fn, hdr);
                memcpy(blk, sv, sizeof(blk)); tck = tn;
            }
        }
        it++;
        if (++cpos >= cyc) { cpos = 0; T = Thi; ncyc++; } else T *= fac;
        if ((it & 0xFFFF) == 0) { /* thresholds refreshed above on the next lap */ }
        int i, j;
        if (pf > 0 && cost > 0 && rndint(1000) < pf) {
            /* pick a random block element that lies in some colliding pair (bounded rejection) */
            int found = 0;
            for (int tries = 0; tries < 64 && !found; tries++) {
                i = rndint(t); j = rndint(k);
                int x = blk[i][j];
                for (int m = 0; m < k; m++) if (m != j && cnt[CL[dif(x, blk[i][m])]] >= 2) { found = 1; break; }
            }
            if (!found) { i = rndint(t); j = rndint(k); }
        } else { i = rndint(t); j = rndint(k); }
        int y; do y = rndint(v); while (inb[i][y]);
        int x = blk[i][j], r[MAXK], a[MAXK], nr = 0, d = 0;
        for (int m = 0; m < k; m++) if (m != j) { int c = CL[dif(x, blk[i][m])]; r[nr++] = c; if (cnt[c] >= 2) d--; cnt[c]--; }
        for (int m = 0, q = 0; m < k; m++) if (m != j) { int c = CL[dif(y, blk[i][m])]; a[q++] = c; if (cnt[c] >= 1) d++; cnt[c]++; }
        int accept = d <= 0 || (d < 64 && rnd32() < thr[d]);
        if (accept) {
            cost += d; acc++;
            inb[i][x] = 0; blk[i][j] = y; inb[i][y] = 1;
            if (cost < 16) hist[cost]++;
            if (cost < gbest) { gbest = cost; memcpy(gblk, blk, sizeof(blk)); }
            if (cost == 0) { solved = 1; break; }
        } else {
            for (int q = 0; q < nr; q++) cnt[a[q]]--;
            for (int q = 0; q < nr; q++) cnt[r[q]]++;
        }
    }
    double el = now() - t0;
    printf("end solved=%d it=%lld acc=%lld gbest=%d cycles=%lld secs=%.1f\n", solved, it, acc, gbest, ncyc, el);
    printf("hist"); for (int c = 0; c < 16; c++) printf(" %lld", hist[c]); printf("\n");
    if (solved) {
        full_recount();
        if (cost != 0) { printf("internal error: cost %d\n", cost); return 3; }
        char hdr[256]; snprintf(hdr, sizeof hdr, "# sa_cdf seed=%llu it=%lld secs=%.1f\n", (unsigned long long)seed, it, el);
        snprintf(fn, sizeof fn, "%s.sol", pre); write_state(fn, hdr);
        printf("SOLVED written %s\n", fn);
        for (int i = 0; i < t; i++) { for (int a = 0; a < k; a++) printf(a ? " %d" : "%d", blk[i][a]); printf("\n"); }
    }
    fflush(stdout);
    return solved ? 0 : 1;
}
