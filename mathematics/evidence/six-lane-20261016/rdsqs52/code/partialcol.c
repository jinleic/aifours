/* partialcol: PartialCol-style tabu search (Blöchliger–Zufferey) for a resolution of an
 * STS(v), v ≡ 3 (mod 6): a legal partial colouring of the triples with k=(v-1)/2 colours
 * (no two triples through a common point share a colour) is maintained; the objective is
 * the number of uncoloured triples.  Move: give an uncoloured triple t colour c and
 * uncolour the (at most 3) coloured triples of colour c meeting t.  Tabu: an uncoloured
 * triple may not get back the colour it lost for tenure = 0.6*|U| + rand(0..9) iterations.
 * Anchor (optional): triples through point ANCHOR are pre-coloured 0..k-1 and frozen.
 * Input: "v m" then m lines "a b c".  Output: "SOLVED iter" + "a b c colour" lines, or
 * "FAILED best".  Usage: partialcol FILE SEED MAX_ITER [ANCHOR]
 */
#include <stdio.h>
#include <stdlib.h>

static unsigned long long rs;
static unsigned rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return (unsigned)(rs >> 11); }

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage\n"); return 2; }
    FILE *f = fopen(argv[1], "r");
    if (!f) return 2;
    rs = 0x9E3779B97F4A7C15ULL ^ ((unsigned long long)atoll(argv[2]) + 1) * 0x2545F4914F6CDD1DULL;
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
    int *own = malloc(sizeof(int) * v * k);              /* own[p*k+c] = triple of colour c at p, or -1 */
    long long *tabu = calloc((size_t)m * k, sizeof(long long));
    int *U = malloc(sizeof(int) * m), *pos = malloc(sizeof(int) * m);
    int nu = 0;
    for (int i = 0; i < v * k; i++) own[i] = -1;
    for (int i = 0; i < m; i++) { col[i] = -1; pos[i] = -1; }
    int na = 0;
    if (anchor >= 0)
        for (int i = 0; i < m; i++)
            if (T[i][0] == anchor || T[i][1] == anchor || T[i][2] == anchor) {
                col[i] = na++; fixed[i] = 1;
                for (int j = 0; j < 3; j++) own[T[i][j] * k + col[i]] = i;
            }
    /* greedy initial colouring in random order */
    int *ord = malloc(sizeof(int) * m);
    for (int i = 0; i < m; i++) ord[i] = i;
    for (int i = m - 1; i > 0; i--) { int j = rnd() % (i + 1); int t = ord[i]; ord[i] = ord[j]; ord[j] = t; }
    for (int q = 0; q < m; q++) {
        int i = ord[q];
        if (fixed[i]) continue;
        int c0 = rnd() % k, done = 0;
        for (int d = 0; d < k && !done; d++) {
            int c = (c0 + d) % k;
            if (own[T[i][0] * k + c] < 0 && own[T[i][1] * k + c] < 0 && own[T[i][2] * k + c] < 0) {
                col[i] = c; for (int j = 0; j < 3; j++) own[T[i][j] * k + c] = i; done = 1;
            }
        }
        if (!done) { pos[i] = nu; U[nu++] = i; }
    }
    int best = nu;
    int *bestcol = malloc(sizeof(int) * m);
    for (int i = 0; i < m; i++) bestcol[i] = col[i];
    long long it;
    for (it = 0; it < maxit && nu > 0; it++) {
        int bdelta = 1 << 30, bt = -1, bc = -1, ties = 0;
        for (int q = 0; q < nu; q++) {
            int t = U[q];
            for (int c = 0; c < k; c++) {
                int e0 = own[T[t][0] * k + c], e1 = own[T[t][1] * k + c], e2 = own[T[t][2] * k + c];
                int ne = 0, blocked = 0;
                int ev[3] = {e0, e1, e2};
                int uniq[3]; int nuq = 0;
                for (int j = 0; j < 3; j++) {
                    int e = ev[j];
                    if (e < 0) continue;
                    if (fixed[e]) { blocked = 1; break; }
                    int dup = 0;
                    for (int r = 0; r < nuq; r++) if (uniq[r] == e) dup = 1;
                    if (!dup) uniq[nuq++] = e;
                }
                if (blocked) continue;
                ne = nuq;
                int delta = ne - 1;
                int istabu = tabu[(size_t)t * k + c] > it;
                if (istabu && nu + delta >= best) continue;
                if (delta < bdelta) { bdelta = delta; bt = t; bc = c; ties = 1; }
                else if (delta == bdelta) { ties++; if (rnd() % ties == 0) { bt = t; bc = c; } }
            }
        }
        if (bt < 0) continue;
        /* eject conflicting triples */
        for (int j = 0; j < 3; j++) {
            int e = own[T[bt][j] * k + bc];
            if (e >= 0 && col[e] == bc) {
                for (int r = 0; r < 3; r++) own[T[e][r] * k + bc] = -1;
                col[e] = -1;
                pos[e] = nu; U[nu++] = e;
                tabu[(size_t)e * k + bc] = it + (long long)(0.6 * nu) + (rnd() % 10);
            }
        }
        /* colour bt */
        int p = pos[bt]; int last = U[--nu]; U[p] = last; pos[last] = p; pos[bt] = -1;
        col[bt] = bc;
        for (int j = 0; j < 3; j++) own[T[bt][j] * k + bc] = bt;
        if (nu < best) { best = nu; for (int i = 0; i < m; i++) bestcol[i] = col[i]; }
    }
    if (nu == 0) {
        printf("SOLVED %lld\n", it);
        for (int i = 0; i < m; i++) printf("%d %d %d %d\n", T[i][0], T[i][1], T[i][2], col[i]);
        return 0;
    }
    printf("FAILED %d\n", best);
    for (int i = 0; i < m; i++) printf("%d %d %d %d\n", T[i][0], T[i][1], T[i][2], bestcol[i]);
    return 1;
}
