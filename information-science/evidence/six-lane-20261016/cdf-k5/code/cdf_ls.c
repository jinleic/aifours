/* cdf_ls.c -- tabu local search for cyclic (v,k,1) difference families (perfect (v,k,1) OOCs).
 *
 * State: nb representative blocks of k slots.  A slot is INDEPENDENT (value in Z_v, optionally restricted to the
 * subgroup gZ_v) or DERIVED (value = f * value(src slot) mod v).  A block with orbit length r contributes the
 * classes of m*(a-b) for every pair (a,b) of its elements and every m in {1, mu, ..., mu^(r-1)} (multiplier
 * orbit); r = 1 for plain blocks and for multiplier-fixed blocks.  Difference classes are {d,-d}, d = 1..(v-1)/2.
 * Cost = sum over classes of max(0, count-1); with the template's total contribution equal to (v-1)/2 classes,
 * cost 0 <=> difference family.
 *
 * Template file (optional; default = plain family with n=(v-1)/(k(k-1)) free blocks):
 *   line 1: v k mu nblocks
 *   then per block: r  followed by k slot specs, each one of
 *       F<g>        independent slot restricted to multiples of g (g=1: unrestricted)
 *       C<x>        constant x
 *       D<s>*<f>    derived: f * value(slot s) mod v
 * Usage: cdf_ls v k seed seconds outprefix [template] [tl tr alpha_pct stall pert]
 * Writes outprefix.sol (strict certificate, all orbit images expanded) on success, outprefix.ckpt (best state)
 * periodically, and progress lines on stdout.  Exit 0 found, 3 time limit.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define MAXK 8
#define MAXB 128
#define MAXR 16

static int v, k, H, nb;
static long mu = 1;
static int orb[MAXB];               /* orbit length r of block b */
static int stype[MAXB][MAXK];       /* 0 indep, 1 const, 2 derived */
static int sg[MAXB][MAXK];          /* indep: subgroup step g */
static int ssrc[MAXB][MAXK];        /* derived: source slot */
static long sfac[MAXB][MAXK];       /* derived: factor */
static int val[MAXB][MAXK];
static int bestval[MAXB][MAXK], gbestval[MAXB][MAXK];
static long mulpow[MAXB][MAXR];     /* mu^j mod v for j<orb */
static int *cls;                    /* cls[d] for d in [0,v) */
static int *cnt;                    /* class counts */
static int cost, bestcost, gbest;
static long long *tabu;             /* tabu[(b*MAXK+s)*v + y] = iteration until forbidden */
static uint64_t rng;

static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int rndint(int n) { return (int)(rnd() % (uint64_t)n); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static int md(long x) { x %= v; if (x < 0) x += v; return (int)x; }

static void recompute_derived(int b) {
    for (int s = 0; s < k; s++) if (stype[b][s] == 2) val[b][s] = md(sfac[b][s] * val[b][ssrc[b][s]]);
}

/* add (sign=+1) or remove (sign=-1) all classes of block b; returns cost delta */
static int block_apply(int b, int sign) {
    int d = 0;
    for (int s = 0; s < k; s++) for (int t = s + 1; t < k; t++) {
        int diff = md((long)val[b][s] - val[b][t]);
        for (int j = 0; j < orb[b]; j++) {
            int c = cls[md(mulpow[b][j] * diff)];
            if (sign > 0) { if (cnt[c] >= 1) d++; cnt[c]++; }
            else { cnt[c]--; if (cnt[c] >= 1) d--; }
        }
    }
    return d;
}

static int block_distinct(int b) {
    for (int s = 0; s < k; s++) for (int t = s + 1; t < k; t++) if (val[b][s] == val[b][t]) return 0;
    return 1;
}

static void random_slot_value(int b, int s) {
    int g = sg[b][s];
    val[b][s] = g * rndint(v / g);
}

static void random_init(void) {
    for (int b = 0; b < nb; b++) {
        do {
            for (int s = 0; s < k; s++) if (stype[b][s] == 0) random_slot_value(b, s);
            recompute_derived(b);
        } while (!block_distinct(b));
    }
}

static void full_recount(void) {
    memset(cnt, 0, sizeof(int) * (H + 1));
    cost = 0;
    for (int b = 0; b < nb; b++) cost += block_apply(b, +1);
}

static void write_state(const char *path, int (*st)[MAXK], int c, long long it, double el) {
    FILE *f = fopen(path, "w");
    if (!f) return;
    fprintf(f, "# v=%d k=%d mu=%ld nb=%d cost=%d iter=%lld elapsed=%.1f\n", v, k, mu, nb, c, it, el);
    for (int b = 0; b < nb; b++) {
        for (int s = 0; s < k; s++) fprintf(f, "%d%c", st[b][s], s + 1 < k ? ' ' : '\n');
    }
    fclose(f);
}

static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }

static void write_solution(const char *path) {
    FILE *f = fopen(path, "w");
    if (!f) { perror(path); exit(1); }
    fprintf(f, "CDF %d %d\n", v, k);
    for (int b = 0; b < nb; b++) for (int j = 0; j < orb[b]; j++) {
        int e[MAXK];
        for (int s = 0; s < k; s++) e[s] = md(mulpow[b][j] * val[b][s]);
        qsort(e, k, sizeof(int), cmpint);
        for (int s = 0; s < k; s++) fprintf(f, "%d%c", e[s], s + 1 < k ? ' ' : '\n');
    }
    fclose(f);
}

static void load_template(const char *path) {
    FILE *f = fopen(path, "r");
    if (!f) { perror(path); exit(1); }
    int tv, tk;
    if (fscanf(f, "%d %d %ld %d", &tv, &tk, &mu, &nb) != 4) { fprintf(stderr, "bad template header\n"); exit(1); }
    if (tv != v || tk != k || nb > MAXB) { fprintf(stderr, "template mismatch\n"); exit(1); }
    for (int b = 0; b < nb; b++) {
        if (fscanf(f, "%d", &orb[b]) != 1 || orb[b] < 1 || orb[b] > MAXR) { fprintf(stderr, "bad orbit\n"); exit(1); }
        for (int s = 0; s < k; s++) {
            char tok[64];
            if (fscanf(f, "%63s", tok) != 1) { fprintf(stderr, "bad slot\n"); exit(1); }
            if (tok[0] == 'F') { stype[b][s] = 0; sg[b][s] = atoi(tok + 1); if (sg[b][s] < 1) sg[b][s] = 1; }
            else if (tok[0] == 'C') { stype[b][s] = 1; val[b][s] = md(atol(tok + 1)); }
            else if (tok[0] == 'D') { stype[b][s] = 2; ssrc[b][s] = atoi(tok + 1); char *p = strchr(tok, '*');
                                      if (!p) { fprintf(stderr, "bad derived\n"); exit(1); } sfac[b][s] = atol(p + 1); }
            else { fprintf(stderr, "bad slot token %s\n", tok); exit(1); }
        }
    }
    fclose(f);
}

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: cdf_ls v k seed seconds outprefix [template|-] [tl tr alpha_pct stall pert]\n"); return 2; }
    v = atoi(argv[1]); k = atoi(argv[2]);
    uint64_t seed = strtoull(argv[3], 0, 10);
    double limit = atof(argv[4]);
    const char *pre = argv[5];
    int tl = 10, tr = 10, alpha = 60;
    long long stall = 200000; int pert = 3;
    if (argc > 7) tl = atoi(argv[7]);
    if (argc > 8) tr = atoi(argv[8]);
    if (argc > 9) alpha = atoi(argv[9]);
    if (argc > 10) stall = atoll(argv[10]);
    if (argc > 11) pert = atoi(argv[11]);
    H = (v - 1) / 2;
    rng = seed * 0x2545F4914F6CDD1DULL + 12345;
    if (argc > 6 && strcmp(argv[6], "-") != 0) load_template(argv[6]);
    else {
        if ((v - 1) % (k * (k - 1))) { fprintf(stderr, "v != 1 mod k(k-1)\n"); return 2; }
        nb = (v - 1) / (k * (k - 1));
        if (nb > MAXB) { fprintf(stderr, "too many blocks\n"); return 2; }
        for (int b = 0; b < nb; b++) { orb[b] = 1; for (int s = 0; s < k; s++) { stype[b][s] = 0; sg[b][s] = 1; } }
    }
    long total = 0;
    for (int b = 0; b < nb; b++) {
        mulpow[b][0] = 1;
        for (int j = 1; j < orb[b]; j++) mulpow[b][j] = md(mulpow[b][j - 1] * mu);
        total += (long)orb[b] * k * (k - 1) / 2;
    }
    if (total != H) { fprintf(stderr, "template covers %ld classes, need %d\n", total, H); return 2; }
    cls = malloc(sizeof(int) * v); cnt = calloc(H + 1, sizeof(int));
    for (int d = 0; d < v; d++) cls[d] = d <= H ? d : v - d;
    tabu = calloc((size_t)nb * MAXK * v, sizeof(long long));
    random_init();
    full_recount();
    bestcost = cost; memcpy(bestval, val, sizeof(val)); gbest = cost; memcpy(gbestval, val, sizeof(val));
    double t0 = now(), tlast = t0, tck = t0;
    long long it = 0, last_imp = 0;
    char path[1024];
    printf("start v=%d k=%d nb=%d mu=%ld seed=%llu cost=%d tl=%d tr=%d alpha=%d stall=%lld pert=%d\n",
           v, k, nb, mu, (unsigned long long)seed, cost, tl, tr, alpha, stall, pert);
    fflush(stdout);
    /* scratch */
    static int candb[MAXB * MAXK], cands[MAXB * MAXK];
    static int confl[MAXB][MAXK];
    while (cost > 0) {
        it++;
        if ((it & 255) == 0) {
            double t = now();
            if (t - t0 > limit) break;
            if (t - tlast > 10) {
                printf("it=%lld cost=%d best=%d gbest=%d t=%.0f\n", it, cost, bestcost, gbest, t - t0); fflush(stdout); tlast = t;
            }
            if (t - tck > 600) {
                snprintf(path, sizeof path, "%s.ckpt", pre);
                write_state(path, gbestval, gbest, it, t - t0); tck = t;
            }
        }
        /* conflicted independent slots */
        memset(confl, 0, sizeof(confl));
        for (int b = 0; b < nb; b++) for (int s = 0; s < k; s++) for (int t = s + 1; t < k; t++) {
            int diff = md((long)val[b][s] - val[b][t]);
            for (int j = 0; j < orb[b]; j++) {
                if (cnt[cls[md(mulpow[b][j] * diff)]] >= 2) {
                    int ss = stype[b][s] == 2 ? ssrc[b][s] : s, tt = stype[b][t] == 2 ? ssrc[b][t] : t;
                    if (stype[b][ss] == 0) confl[b][ss] = 1;
                    if (stype[b][tt] == 0) confl[b][tt] = 1;
                    break;
                }
            }
        }
        int nc = 0;
        for (int b = 0; b < nb; b++) for (int s = 0; s < k; s++) if (confl[b][s]) { candb[nc] = b; cands[nc] = s; nc++; }
        int bestd = 1 << 30, nbest = 0, mb = -1, ms = -1, my = -1;
        for (int ci = 0; ci < nc; ci++) {
            int b = candb[ci], s = cands[ci];
            int oldv = val[b][s];
            int rem = block_apply(b, -1);
            int g = sg[b][s];
            long long *tb = tabu + ((size_t)(b * MAXK + s)) * v;
            for (int y = 0; y < v; y += g) {
                if (y == oldv) continue;
                val[b][s] = y; recompute_derived(b);
                if (!block_distinct(b)) continue;
                int add = block_apply(b, +1);
                block_apply(b, -1);
                int d = rem + add;
                int ok = tb[y] <= it || cost + d < bestcost;
                if (!ok) continue;
                if (d < bestd) { bestd = d; nbest = 1; mb = b; ms = s; my = y; }
                else if (d == bestd) { nbest++; if (rndint(nbest) == 0) { mb = b; ms = s; my = y; } }
            }
            val[b][s] = oldv; recompute_derived(b);
            block_apply(b, +1);
        }
        if (mb < 0) { /* everything tabu: random move */
            int ci = rndint(nc); mb = candb[ci]; ms = cands[ci];
            do { my = sg[mb][ms] * rndint(v / sg[mb][ms]); } while (my == val[mb][ms]);
            int oldv = val[mb][ms];
            val[mb][ms] = my; recompute_derived(mb);
            int okd = block_distinct(mb);
            val[mb][ms] = oldv; recompute_derived(mb);
            if (!okd) continue;
        }
        {
            int oldv = val[mb][ms];
            cost += block_apply(mb, -1);
            val[mb][ms] = my; recompute_derived(mb);
            cost += block_apply(mb, +1);
            tabu[((size_t)(mb * MAXK + ms)) * v + oldv] = it + tl + rndint(tr + 1) + (alpha * nc) / 100;
        }
        if (cost < bestcost) { bestcost = cost; memcpy(bestval, val, sizeof(val)); last_imp = it;
            if (cost < gbest) { gbest = cost; memcpy(gbestval, val, sizeof(val)); } }
        if (it - last_imp > stall) {
            /* perturb: re-randomize pert random independent slots */
            for (int p = 0; p < pert; p++) {
                int b = rndint(nb), s;
                do { s = rndint(k); } while (stype[b][s] != 0);
                cost += block_apply(b, -1);
                int oldv = val[b][s];
                do { random_slot_value(b, s); recompute_derived(b); } while (!block_distinct(b) && (val[b][s] = oldv, 1));
                cost += block_apply(b, +1);
            }
            last_imp = it;
            bestcost = cost; memcpy(bestval, val, sizeof(val));
        }
    }
    double el = now() - t0;
    if (cost == 0) {
        snprintf(path, sizeof path, "%s.sol", pre);
        write_solution(path);
        snprintf(path, sizeof path, "%s.ckpt", pre);
        write_state(path, val, 0, it, el);
        printf("FOUND v=%d seed=%llu iters=%lld seconds=%.2f\n", v, (unsigned long long)seed, it, el);
        return 0;
    }
    snprintf(path, sizeof path, "%s.ckpt", pre);
    write_state(path, gbestval, gbest, it, el);
    printf("TIMEOUT v=%d seed=%llu iters=%lld seconds=%.2f best=%d\n", v, (unsigned long long)seed, it, el, gbest);
    return 3;
}
