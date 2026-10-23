/* tabures: TabuCol-style local search for a resolution of an STS(v), v ≡ 3 (mod 6).
 *
 * A resolution is a colouring of the triples with k=(v-1)/2 colours such that no two
 * triples through a common point share a colour (then every colour class is a
 * parallel class, since each point lies in exactly k triples).
 * Cost = sum over points p and colours c of C(n[p][c], 2).
 * Move: recolour one conflicting triple; tabu tenure L = 0.6*#conflicting + rand(0..9);
 * aspiration on new best.  Random restarts are left to the caller (seed argument).
 *
 * Input (stdin or file): first line "v m", then m lines "a b c" (points 0..v-1).
 * Optional fixed triples: if the 4th argument is given, the triples through point
 * ANCHOR are pre-coloured 0..k-1 in input order and never moved (lossless).
 * Output: "SOLVED iter" and m lines "a b c colour", or "FAILED best_cost".
 * Usage: tabures FILE SEED MAX_ITER [ANCHOR]
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

static unsigned long long rs;
static unsigned rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return (unsigned)(rs >> 11); }

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: %s FILE SEED MAX_ITER [ANCHOR]\n", argv[0]); return 2; }
    FILE *f = fopen(argv[1], "r");
    if (!f) { perror("open"); return 2; }
    rs = 0x9E3779B97F4A7C15ULL ^ (unsigned long long)atoll(argv[2]) * 0x2545F4914F6CDD1DULL;
    if (!rs) rs = 1;
    long long maxit = atoll(argv[3]);
    int anchor = argc > 4 ? atoi(argv[4]) : -1;
    int v, m;
    if (fscanf(f, "%d %d", &v, &m) != 2) return 2;
    int k = (v - 1) / 2;
    int (*T)[3] = malloc(sizeof(int[3]) * m);
    for (int i = 0; i < m; i++) if (fscanf(f, "%d %d %d", &T[i][0], &T[i][1], &T[i][2]) != 3) return 2;
    fclose(f);
    int *col = malloc(sizeof(int) * m);
    int *fixed = calloc(m, sizeof(int));
    int *n = calloc((size_t)v * k, sizeof(int));          /* n[p*k+c] */
    long long *tabu = calloc((size_t)m * k, sizeof(long long));
    int na = 0;
    for (int i = 0; i < m; i++) {
        if (anchor >= 0 && (T[i][0] == anchor || T[i][1] == anchor || T[i][2] == anchor)) {
            col[i] = na++; fixed[i] = 1;
        } else col[i] = rnd() % k;
    }
    for (int i = 0; i < m; i++) for (int j = 0; j < 3; j++) n[T[i][j] * k + col[i]]++;
    long long cost = 0;
    for (int p = 0; p < v; p++) for (int c = 0; c < k; c++) { int x = n[p * k + c]; cost += (long long)x * (x - 1) / 2; }
    long long best = cost;
    int *conf = malloc(sizeof(int) * m);
    long long it = 0;
    for (it = 0; it < maxit && cost > 0; it++) {
        /* collect conflicting movable triples */
        int nc = 0;
        for (int i = 0; i < m; i++) {
            if (fixed[i]) continue;
            int c = col[i];
            if (n[T[i][0] * k + c] > 1 || n[T[i][1] * k + c] > 1 || n[T[i][2] * k + c] > 1) conf[nc++] = i;
        }
        if (nc == 0) break;
        long long bd = 1LL << 60; int bi = -1, bc = -1, ties = 0;
        for (int q = 0; q < nc; q++) {
            int i = conf[q], c = col[i];
            int a = T[i][0], b = T[i][1], d = T[i][2];
            long long rem = (n[a * k + c] - 1) + (n[b * k + c] - 1) + (n[d * k + c] - 1);
            for (int c2 = 0; c2 < k; c2++) {
                if (c2 == c) continue;
                long long add = n[a * k + c2] + n[b * k + c2] + n[d * k + c2];
                long long delta = add - rem;
                int istabu = tabu[(size_t)i * k + c2] > it;
                if (istabu && cost + delta >= best) continue;
                if (delta < bd) { bd = delta; bi = i; bc = c2; ties = 1; }
                else if (delta == bd) { ties++; if (rnd() % ties == 0) { bi = i; bc = c2; } }
            }
        }
        if (bi < 0) continue;
        int c = col[bi];
        tabu[(size_t)bi * k + c] = it + (long long)(0.6 * nc) + (rnd() % 10);
        for (int j = 0; j < 3; j++) { n[T[bi][j] * k + c]--; n[T[bi][j] * k + bc]++; }
        col[bi] = bc;
        cost += bd;
        if (cost < best) best = cost;
        if ((it & 0xFFFFF) == 0 && it) fprintf(stderr, "it %lld cost %lld best %lld\n", it, cost, best);
        if (cost == 0) break;
    }
    if (cost == 0) {
        printf("SOLVED %lld\n", it);
        for (int i = 0; i < m; i++) printf("%d %d %d %d\n", T[i][0], T[i][1], T[i][2], col[i]);
        return 0;
    }
    printf("FAILED %lld\n", best);
    return 1;
}
