/* defect13.c -- v = 901 = 17*53: families made of 3 orbits of 13 blocks under nu = (1 mod 17, g mod 53),
 * ord(g) = 13, plus a defect D of 6 blocks (see evidence/v901/PLAN-cycle1.md).
 * This program is STAGE 1 only (exhaustive): for every set T of 4 of the 34 nu-orbits of non-K classes, enumerate
 * all blocks (one per translation+negation class) whose 10 classes are distinct and lie in K u T, and search
 * exhaustively for 6 of them partitioning K u T (60 classes).  Defects found go to outprefix.defects (first
 * solution per T, count capped at 1000).  Stage 2 (completing the 3 orbits) would be a separate program.
 * Usage: defect13 seed unused outprefix [maxT]
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define V 901
#define H 450
static int crt[17][53], orb[H + 1], norb, orbsize[H + 1], isK[H + 1], nuv[V];
static int bigorb[64], nbig;               /* orbit ids of the 34 size-13 orbits */
static uint64_t rng;
static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL; z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL; return z ^ (z >> 31);
}
static int rndint(int k) { return (int)(rnd() % (uint64_t)k); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static inline int mv(int z) { z %= V; return z < 0 ? z + V : z; }
static inline int cl(int d) { d = mv(d); return d <= H ? d : V - d; }
static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static void canon(const int *z, int *out) {
    int best[5], cand[5], have = 0;
    for (int s = 0; s < 2; s++) for (int t = 0; t < 5; t++) {
        for (int i = 0; i < 5; i++) cand[i] = mv((s ? -z[i] : z[i]) - (s ? -z[t] : z[t]));
        qsort(cand, 5, sizeof(int), cmpint);
        if (!have || memcmp(cand, best, sizeof cand) < 0) { memcpy(best, cand, sizeof cand); have = 1; }
    }
    memcpy(out, best, sizeof best);
}

/* stage 1 rows */
static int nrow; static int rz[200000][5]; static uint64_t rmask[200000];
static int colof[H + 1];
static int chosen[8]; static long long xnodes; static int found_def[6][5];
static int xc(int depth, int *lst, int cnt, uint64_t cov, uint64_t full, long long *nsol) {
    if (cov == full) { (*nsol)++; if (*nsol == 1) for (int i = 0; i < depth; i++) memcpy(found_def[i], rz[chosen[i]], sizeof(int) * 5); return *nsol >= 1000; }
    xnodes++;
    int best = -1, bs = 1 << 30;
    for (int c = 0; c < 60; c++) if (!(cov >> c & 1)) {
        int k = 0; for (int i = 0; i < cnt; i++) if (rmask[lst[i]] >> c & 1) k++;
        if (k < bs) { bs = k; best = c; }
    }
    if (bs == 0) return 0;
    int *nxt = malloc(sizeof(int) * (cnt + 1));
    for (int i = 0; i < cnt; i++) {
        int x = lst[i];
        if (!(rmask[x] >> best & 1)) continue;
        int k = 0;
        for (int j = 0; j < cnt; j++) if (!(rmask[lst[j]] & rmask[x])) nxt[k++] = lst[j];
        chosen[depth] = x;
        if (xc(depth + 1, nxt, k, cov | rmask[x], full, nsol)) { free(nxt); return 1; }
    }
    free(nxt);
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: defect13 seed stage2_seconds outprefix [maxT]\n"); return 2; }
    uint64_t seed = strtoull(argv[1], 0, 10); double s2limit = atof(argv[2]); const char *pre = argv[3];
    long maxT = argc > 4 ? atol(argv[4]) : 1L << 40;
    rng = seed * 0x2545F4914F6CDD1DULL + 2026;
    for (int z = 0; z < V; z++) crt[z % 17][z % 53] = z;
    int g = 0;
    for (int c = 2; c < 53 && !g; c++) { int x = 1, o = 0; do { x = x * c % 53; o++; } while (x != 1); if (o == 13) g = c; }
    for (int z = 0; z < V; z++) nuv[z] = crt[z % 17][(g * (z % 53)) % 53];
    /* class orbits under nu */
    memset(orb, -1, sizeof orb);
    norb = 0;
    for (int c = 1; c <= H; c++) {
        if (orb[c] >= 0) continue;
        int x = c, sz = 0;
        do { orb[x] = norb; sz++; x = cl(nuv[x]); } while (x != c);
        orbsize[norb] = sz; norb++;
    }
    int nK = 0;
    for (int c = 1; c <= H; c++) { isK[c] = (c % 53) == 0; if (isK[c]) { nK++; if (orbsize[orb[c]] != 1) { printf("INTERNAL: K class not fixed\n"); return 1; } } }
    nbig = 0;
    for (int o = 0; o < norb; o++) { if (orbsize[o] == 13) bigorb[nbig++] = o; else if (orbsize[o] != 1) { printf("INTERNAL: orbit size %d\n", orbsize[o]); return 1; } }
    printf("g=%d orbits=%d (K singletons %d, size-13 orbits %d)\n", g, norb, nK, nbig);
    /* no nu-stable block: fixed points of x -> nu x + t lie in a coset of {(a,0)}, which has only 8 classes */
    fflush(stdout);
    FILE *fd = 0; char path[1024];
    snprintf(path, sizeof path, "%s.defects", pre); fd = fopen(path, "w");
    double t0 = now();
    long Tcount = 0, Twith = 0; long long rowmax = 0, rowsum = 0, solsum = 0;
    int *lst = malloc(sizeof(int) * 200000);
    int T[4];
    for (T[0] = 0; T[0] < nbig; T[0]++) for (T[1] = T[0] + 1; T[1] < nbig; T[1]++) for (T[2] = T[1] + 1; T[2] < nbig; T[2]++)
    for (T[3] = T[2] + 1; T[3] < nbig && Tcount < maxT; T[3]++) {
        Tcount++;
        int target[H + 1]; int nt = 0;
        for (int c = 1; c <= H; c++) {
            int in = isK[c];
            for (int k = 0; k < 4; k++) if (orb[c] == bigorb[T[k]]) in = 1;
            target[c] = in; colof[c] = in ? nt++ : -1;
        }
        if (nt != 60) { printf("INTERNAL: target size %d\n", nt); return 1; }
        int S[1024], nS = 0;
        for (int x = 1; x < V; x++) if (target[cl(x)]) S[nS++] = x;
        nrow = 0;
        for (int ia = 0; ia < nS; ia++) { int a = S[ia];
          for (int ib = ia + 1; ib < nS; ib++) { int b = S[ib]; if (!target[cl(b - a)]) continue;
            for (int ic = ib + 1; ic < nS; ic++) { int c = S[ic]; if (!target[cl(c - a)] || !target[cl(c - b)]) continue;
              for (int id = ic + 1; id < nS; id++) { int d = S[id];
                if (!target[cl(d - a)] || !target[cl(d - b)] || !target[cl(d - c)]) continue;
                int z[5] = {0, a, b, c, d}, cs[10], k = 0, ok = 1;
                for (int i = 0; i < 5 && ok; i++) for (int j = i + 1; j < 5 && ok; j++) { int q = cl(z[j] - z[i]);
                    for (int t = 0; t < k; t++) if (cs[t] == q) ok = 0; cs[k++] = q; }
                if (!ok) continue;
                int cn[5]; canon(z, cn); if (memcmp(cn, z, sizeof z)) continue;
                if (nrow >= 200000) { printf("row overflow\n"); return 1; }
                memcpy(rz[nrow], z, sizeof z); rmask[nrow] = 0;
                for (int t = 0; t < 10; t++) rmask[nrow] |= 1ULL << colof[cs[t]];
                nrow++;
              } } } }
        rowsum += nrow; if (nrow > rowmax) rowmax = nrow;
        for (int i = 0; i < nrow; i++) lst[i] = i;
        long long nsol = 0; xnodes = 0;
        uint64_t full = (1ULL << 60) - 1;
        xc(0, lst, nrow, 0, full, &nsol);
        if (nsol) {
            Twith++; solsum += nsol;
            fprintf(fd, "T %d %d %d %d solutions>=%lld\n", bigorb[T[0]], bigorb[T[1]], bigorb[T[2]], bigorb[T[3]], nsol);
            for (int i = 0; i < 6; i++) fprintf(fd, "%d %d %d %d %d\n", found_def[i][0], found_def[i][1], found_def[i][2], found_def[i][3], found_def[i][4]);
            fflush(fd);
        }
        if (Tcount % 2000 == 0) { printf("T=%ld with_defect=%ld rows_max=%lld rows_mean=%.1f t=%.0f\n", Tcount, Twith, rowmax, (double)rowsum / Tcount, now() - t0); fflush(stdout); }
    }
    fclose(fd);
    printf("STAGE1 T=%ld with_defect=%ld total_solutions(capped)=%lld rows_max=%lld rows_mean=%.2f seconds=%.1f\n", Tcount, Twith, solsum,
           rowmax, Tcount ? (double)rowsum / Tcount : 0, now() - t0);
    fflush(stdout);
    if (!Twith) return 3;
    (void)s2limit; (void)rndint;
    return 0;
}
