/* ls_cdf.c -- tabu local search for cyclic (v,k,1) difference families (t = (v-1)/(k(k-1)) blocks).
 *
 * The state is t blocks of k distinct elements of Z_v. The class of d != 0 is min(d, v-d), so there
 * are nc = (v-1)/2 classes and every block contributes k(k-1)/2 class occurrences. The cost is
 * sum_c max(0, cnt_c - 1); cost 0 <=> difference family.
 * Move: replace one element x of block i by y not in block i. Every move of every element is
 * evaluated exactly (delta computed with the removal applied first). Best non-tabu move; ties are
 * broken uniformly at random. Tabu: x may not re-enter block i for tenure iterations; aspiration on
 * a new best. Plateau escape: after `stall` iterations without improving the run best, restart
 * from the run best with `pert` random element changes.
 * Exact 1-block repair (LNS): whenever cost <= repair_max, for every block i such that the other
 * t-1 blocks are mutually collision-free, a DFS enumerates blocks whose classes are exactly the
 * classes left uncovered by the other blocks; any hit is a difference family.
 * Deterministic given the seed (the time limit only decides when to stop).
 *
 * usage: ls_cdf v k seed maxsec tenure_base tenure_rand stall pert repair_max outprefix
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
static int CL[MAXV];                 /* class of d, -1 for d = 0 */
static int blk[MAXT][MAXK];
static unsigned char inb[MAXT][MAXV];
static int cnt[MAXV];
static int cost;
static long long tabu[MAXT][MAXV];
static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs >> 12; rs ^= rs << 25; rs ^= rs >> 27; return rs * 2685821657736338717ULL; }
static inline int rndint(int n) { return (int)(rnd() % (uint64_t)n); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + ts.tv_nsec * 1e-9; }
static inline int dif(int a, int b) { int d = a - b; return d < 0 ? d + v : d; }

static void full_recount(void) {
    memset(cnt, 0, sizeof(int) * nc);
    for (int i = 0; i < t; i++) for (int a = 0; a < k; a++) for (int b = a + 1; b < k; b++) cnt[CL[dif(blk[i][a], blk[i][b])]]++;
    cost = 0; for (int c = 0; c < nc; c++) if (cnt[c] > 1) cost += cnt[c] - 1;
}

/* ---- exact 1-block repair ---- */
static int Rel[MAXK], repair_found = 0, rep_block = -1;
static unsigned char allowed[MAXV];
static long long rep_nodes = 0, rep_calls = 0;
static int rep_dfs(int depth, int start, unsigned char *used) {
    rep_nodes++;
    if (depth == k) return 1;
    for (int x = start; x < v; x++) {
        if (x == Rel[1]) continue;
        int cs[MAXK], ok = 1, n = 0;
        for (int m = 0; m < depth; m++) {
            int c = CL[dif(x, Rel[m])];
            if (!allowed[c] || used[c]) { ok = 0; break; }
            for (int q = 0; q < n; q++) if (cs[q] == c) { ok = 0; break; }
            if (!ok) break;
            cs[n++] = c;
        }
        if (!ok) continue;
        for (int q = 0; q < n; q++) used[cs[q]] = 1;
        Rel[depth] = x;
        if (rep_dfs(depth + 1, x + 1, used)) return 1;
        for (int q = 0; q < n; q++) used[cs[q]] = 0;
    }
    return 0;
}
/* try to replace block i exactly; returns 1 and installs the block on success */
static int try_repair(int i) {
    /* other blocks must be collision-free among themselves */
    static int oc[MAXV];
    memcpy(oc, cnt, sizeof(int) * nc);
    for (int a = 0; a < k; a++) for (int b = a + 1; b < k; b++) oc[CL[dif(blk[i][a], blk[i][b])]]--;
    int nfree = 0;
    for (int c = 0; c < nc; c++) { if (oc[c] > 1) return 0; allowed[c] = (oc[c] == 0); nfree += allowed[c]; }
    if (nfree != k * (k - 1) / 2) return 0;
    rep_calls++;
    int cmin = 0; while (!allowed[cmin]) cmin++;
    static unsigned char used[MAXV]; memset(used, 0, nc);
    used[cmin] = 1; Rel[0] = 0; Rel[1] = cmin + 1;
    if (!rep_dfs(2, 1, used)) return 0;
    for (int a = 0; a < k; a++) inb[i][blk[i][a]] = 0;
    for (int a = 0; a < k; a++) { blk[i][a] = Rel[a]; inb[i][Rel[a]] = 1; }
    full_recount();
    return cost == 0;
}

static void write_state(const char *fn, const char *hdr) {
    FILE *f = fopen(fn, "w"); if (!f) return;
    if (hdr) fprintf(f, "%s", hdr);
    fprintf(f, "CDF %d %d\n", v, k);
    for (int i = 0; i < t; i++) { for (int a = 0; a < k; a++) fprintf(f, a ? " %d" : "%d", blk[i][a]); fprintf(f, "\n"); }
    fclose(f);
}

int main(int argc, char **argv) {
    if (argc < 11) { fprintf(stderr, "usage: ls_cdf v k seed maxsec tenure_base tenure_rand stall pert repair_max outprefix\n"); return 2; }
    v = atoi(argv[1]); k = atoi(argv[2]); uint64_t seed = strtoull(argv[3], 0, 10); double maxsec = atof(argv[4]);
    int tb = atoi(argv[5]), tr = atoi(argv[6]); long long stall = atoll(argv[7]); int pert = atoi(argv[8]);
    int repair_max = atoi(argv[9]); const char *pre = argv[10];
    if ((v - 1) % (k * (k - 1))) { fprintf(stderr, "bad v,k\n"); return 2; }
    t = (v - 1) / (k * (k - 1)); nc = (v - 1) / 2;
    CL[0] = -1; for (int d = 1; d < v; d++) CL[d] = (d < v - d ? d : v - d) - 1;
    rs = seed * 0x9E3779B97F4A7C15ULL + 0x1234567ULL; for (int i = 0; i < 20; i++) rnd();
    for (int i = 0; i < t; i++) {
        memset(inb[i], 0, v);
        for (int a = 0; a < k; a++) { int x; do x = rndint(v); while (inb[i][x]); blk[i][a] = x; inb[i][x] = 1; }
    }
    full_recount();
    static int bestblk[MAXT][MAXK]; int bestcost = cost, gbest = cost;
    memcpy(bestblk, blk, sizeof(blk));
    double t0 = now(), tlast = t0, tck = t0;
    long long it = 0, last_imp = 0, nrestart = 0, hist[64] = {0};
    char fn[1024];
    printf("start v=%d k=%d t=%d seed=%llu cost=%d tb=%d tr=%d stall=%lld pert=%d repair_max=%d\n", v, k, t,
           (unsigned long long)seed, cost, tb, tr, stall, pert, repair_max);
    fflush(stdout);
    int solved = 0;
    while (1) {
        if (cost == 0) { solved = 1; break; }
        if (cost <= repair_max) {
            for (int i = 0; i < t && !solved; i++) if (try_repair(i)) solved = 1;
            if (solved) { printf("repair hit at it=%lld\n", it); break; }
        }
        it++;
        if ((it & 1023) == 0) {
            double tn = now();
            if (tn - t0 > maxsec) break;
            if (tn - tlast > 60) {
                printf("it=%lld cost=%d best=%d gbest=%d restarts=%lld rep_calls=%lld t=%.0f\n", it, cost, bestcost, gbest, nrestart, rep_calls, tn - t0);
                fflush(stdout); tlast = tn;
            }
            if (tn - tck > 600) { /* checkpoint the global best state */
                int sv[MAXT][MAXK]; memcpy(sv, blk, sizeof(blk));
                memcpy(blk, bestblk, sizeof(blk));
                char hdr[256]; snprintf(hdr, sizeof hdr, "# checkpoint seed=%llu it=%lld bestcost=%d t=%.0f\n", (unsigned long long)seed, it, bestcost, tn - t0);
                snprintf(fn, sizeof fn, "%s.ckpt", pre); write_state(fn, hdr);
                memcpy(blk, sv, sizeof(blk)); tck = tn;
            }
        }
        int bdelta = 1 << 30, bi = -1, bj = -1, by = -1, nties = 0;
        for (int i = 0; i < t; i++) for (int j = 0; j < k; j++) {
            int x = blk[i][j], r[MAXK], nr = 0, remd = 0;
            for (int m = 0; m < k; m++) if (m != j) r[nr++] = CL[dif(x, blk[i][m])];
            for (int q = 0; q < nr; q++) { if (cnt[r[q]] >= 2) remd--; cnt[r[q]]--; }
            for (int y = 0; y < v; y++) {
                if (inb[i][y]) continue;
                int a[MAXK], na = 0, addd = 0;
                for (int m = 0; m < k; m++) if (m != j) { int c = CL[dif(y, blk[i][m])]; if (cnt[c] >= 1) addd++; cnt[c]++; a[na++] = c; }
                for (int q = 0; q < na; q++) cnt[a[q]]--;
                int d = remd + addd;
                if (tabu[i][y] > it && cost + d >= bestcost) continue;
                if (d < bdelta) { bdelta = d; bi = i; bj = j; by = y; nties = 1; }
                else if (d == bdelta && rndint(++nties) == 0) { bi = i; bj = j; by = y; }
            }
            for (int q = 0; q < nr; q++) cnt[r[q]]++;
        }
        if (bi < 0) { bi = rndint(t); bj = rndint(k); do by = rndint(v); while (inb[bi][by]); }
        int x = blk[bi][bj];
        for (int m = 0; m < k; m++) if (m != bj) { int c = CL[dif(x, blk[bi][m])]; if (cnt[c] >= 2) cost--; cnt[c]--; }
        inb[bi][x] = 0; blk[bi][bj] = by; inb[bi][by] = 1;
        for (int m = 0; m < k; m++) if (m != bj) { int c = CL[dif(by, blk[bi][m])]; if (cnt[c] >= 1) cost++; cnt[c]++; }
        tabu[bi][x] = it + tb + (tr > 0 ? rndint(tr + 1) : 0);
        if (cost < 64) hist[cost]++;
        if (cost < bestcost) { bestcost = cost; memcpy(bestblk, blk, sizeof(blk)); last_imp = it; if (cost < gbest) gbest = cost; }
        else if (it - last_imp > stall) {
            memcpy(blk, bestblk, sizeof(blk));
            for (int i = 0; i < t; i++) { memset(inb[i], 0, v); for (int a = 0; a < k; a++) inb[i][blk[i][a]] = 1; }
            for (int q = 0; q < pert; q++) {
                int i = rndint(t), j = rndint(k), y; do y = rndint(v); while (inb[i][y]);
                inb[i][blk[i][j]] = 0; blk[i][j] = y; inb[i][y] = 1;
            }
            full_recount(); bestcost = cost; memcpy(bestblk, blk, sizeof(blk)); last_imp = it; nrestart++;
            for (int i = 0; i < t; i++) for (int y = 0; y < v; y++) tabu[i][y] = 0;
        }
    }
    double el = now() - t0;
    printf("end solved=%d it=%lld gbest=%d restarts=%lld rep_calls=%lld rep_nodes=%lld secs=%.1f\n", solved, it, gbest, nrestart, rep_calls, rep_nodes, el);
    printf("hist"); for (int c = 0; c < 16; c++) printf(" %lld", hist[c]); printf("\n");
    if (solved) {
        full_recount();
        if (cost != 0) { printf("internal error: cost %d\n", cost); return 3; }
        char hdr[256]; snprintf(hdr, sizeof hdr, "# ls_cdf seed=%llu it=%lld secs=%.1f\n", (unsigned long long)seed, it, el);
        snprintf(fn, sizeof fn, "%s.sol", pre); write_state(fn, hdr);
        printf("SOLVED written %s\n", fn);
        for (int i = 0; i < t; i++) { for (int a = 0; a < k; a++) printf(a ? " %d" : "%d", blk[i][a]); printf("\n"); }
    }
    fflush(stdout);
    return solved ? 0 : 1;
}
