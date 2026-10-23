/* Tabu search (TabuCol-style) for a good colouring of a derived design by partial parallel
 * classes.  Input file (written by code/export_derived.py):
 *   line 1: NPOINTS NTRIPLES NCOL NAVOID
 *   then NTRIPLES lines "a b c f" with f = 1 if the triple contains a hole point (such a triple
 *   may only take colours NAVOID..NCOL-1), points 0..NPOINTS-1.
 * Cost = sum over (point, colour) of C(k,2), k = number of triples of that colour on the point.
 * Moves: recolour one conflicting triple (allowed list); tabu tenure L + alpha*|conflicting|.
 * Usage: tabucol FILE SEED MAXSECONDS OUT  -> prints best cost; writes the colouring to OUT
 * (exclusive create; refuses to overwrite) when cost 0 is reached.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <fcntl.h>
#include <unistd.h>

#define MAXP 128
#define MAXT 4096
#define MAXC 64
static int np, nt, nc, nav, T[MAXT][3], hole[MAXT], col[MAXT], cnt[MAXP][MAXC];
static long tabu[MAXT][MAXC];
static unsigned long long rs = 88172645463325252ULL;
static unsigned long long rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }

static int conflicts_of(int t) {  /* number of other triples with the same colour meeting t */
    int s = 0;
    for (int i = 0; i < 3; i++) s += cnt[T[t][i]][col[t]] - 1;
    return s;
}

int main(int argc, char **argv) {
    if (argc != 5) { fprintf(stderr, "usage: %s FILE SEED MAXSECONDS OUT\n", argv[0]); return 2; }
    FILE *f = fopen(argv[1], "r");
    if (!f || fscanf(f, "%d %d %d %d", &np, &nt, &nc, &nav) != 4) { fprintf(stderr, "bad input\n"); return 2; }
    if (np > MAXP || nt > MAXT || nc > MAXC) { fprintf(stderr, "too large\n"); return 2; }
    for (int t = 0; t < nt; t++)
        if (fscanf(f, "%d %d %d %d", &T[t][0], &T[t][1], &T[t][2], &hole[t]) != 4) { fprintf(stderr, "bad triple\n"); return 2; }
    fclose(f);
    rs ^= (unsigned long long)atoll(argv[2]) * 0x9E3779B97F4A7C15ULL;
    for (int i = 0; i < 10; i++) rnd();
    double maxs = atof(argv[3]);
    for (int t = 0; t < nt; t++) {
        int lo = hole[t] ? nav : 0;
        col[t] = lo + (int)(rnd() % (unsigned)(nc - lo));
        for (int i = 0; i < 3; i++) cnt[T[t][i]][col[t]]++;
    }
    long cost = 0;
    for (int p = 0; p < np; p++) for (int c = 0; c < nc; c++) cost += (long)cnt[p][c] * (cnt[p][c] - 1) / 2;
    long best = cost, it = 0;
    clock_t t0 = clock();
    static int confl[MAXT];
    while (cost > 0) {
        it++;
        if ((it & 1023) == 0 && (double)(clock() - t0) / CLOCKS_PER_SEC > maxs) break;
        int nconf = 0;
        for (int t = 0; t < nt; t++) if (conflicts_of(t) > 0) confl[nconf++] = t;
        int bt = -1, bc = -1; long bd = 1L << 40; int ties = 0;
        for (int k = 0; k < nconf; k++) {
            int t = confl[k], c0 = col[t], lo = hole[t] ? nav : 0;
            int base = 0;
            for (int i = 0; i < 3; i++) base += cnt[T[t][i]][c0] - 1;
            for (int c = lo; c < nc; c++) {
                if (c == c0) continue;
                int add = 0;
                for (int i = 0; i < 3; i++) add += cnt[T[t][i]][c];
                long d = add - base;
                int is_tabu = tabu[t][c] > it;
                if (is_tabu && cost + d >= best) continue;  /* aspiration */
                if (d < bd) { bd = d; bt = t; bc = c; ties = 1; }
                else if (d == bd && (rnd() % (unsigned)(++ties)) == 0) { bt = t; bc = c; }
            }
        }
        if (bt < 0) { int t = confl[rnd() % (unsigned)nconf]; int lo = hole[t] ? nav : 0; bt = t; bc = lo + (int)(rnd() % (unsigned)(nc - lo)); if (bc == col[t]) continue; bd = 0;
            int add = 0, base = 0; for (int i = 0; i < 3; i++) { add += cnt[T[t][i]][bc]; base += cnt[T[t][i]][col[t]] - 1; } bd = add - base; }
        int c0 = col[bt];
        for (int i = 0; i < 3; i++) { cnt[T[bt][i]][c0]--; cnt[T[bt][i]][bc]++; }
        col[bt] = bc;
        cost += bd;
        tabu[bt][c0] = it + 10 + (long)(rnd() % 10) + (long)(0.6 * nconf);
        if (cost < best) { best = cost; }
    }
    double secs = (double)(clock() - t0) / CLOCKS_PER_SEC;
    printf("best %ld final %ld iterations %ld seconds %.1f\n", best, cost, it, secs);
    if (cost == 0) {
        int fd = open(argv[4], O_WRONLY | O_CREAT | O_EXCL, 0644);
        if (fd < 0) { perror("open OUT (exists?)"); return 3; }
        FILE *o = fdopen(fd, "w");
        for (int t = 0; t < nt; t++) fprintf(o, "%d %d %d %d\n", T[t][0], T[t][1], T[t][2], col[t]);
        fclose(o);
    }
    return cost == 0 ? 0 : 1;
}
