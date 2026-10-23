/* README E8(ii): good colouring of one derived design as an exact cover with secondary columns
 * (Knuth's Algorithm X with dancing links).  Primary columns: the triples (each gets exactly one
 * colour).  Secondary columns: (point, colour) pairs (used at most once = partial parallel
 * classes).  Rows: (triple, colour) with colour >= S for triples containing a hole point.
 * The triples through the ANCHOR (a hole point) are pre-assigned colours S..R-1 in input order
 * (lossless labelling of the non-avoiding classes).  Column choice: minimum remaining values,
 * ties broken by a seeded random key; restarts with a doubling node budget (Luby-free, simple).
 * Input: the .tri file of code/derived_io.py ("V NT R S", then "a b c holeflag").
 * Usage: dlx_colour FILE ANCHOR SEED MAXSECONDS OUT   (OUT written exclusively if solved)
 * Prints: solved/unsolved, best depth (number of triples covered), nodes, restarts.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <fcntl.h>
#include <unistd.h>

#define MAXT 4096
#define MAXP 128
#define MAXC 64
static int V, NT, R, S, T[MAXT][3], hole[MAXT];
/* node arrays */
static int *Lf, *Rt, *Up, *Dn, *Col, *Rowid, *Size;
static int nnodes, root, ncols;
static int rowT[MAXT * MAXC], rowC[MAXT * MAXC], nrows;
static int key[MAXT * 2 + MAXP * MAXC + 8];
static unsigned long long rs = 0x9E3779B97F4A7C15ULL;
static unsigned long long rnd(void) { rs ^= rs << 13; rs ^= rs >> 7; rs ^= rs << 17; return rs; }

static void cover(int c) {
    Lf[Rt[c]] = Lf[c]; Rt[Lf[c]] = Rt[c];
    for (int i = Dn[c]; i != c; i = Dn[i])
        for (int j = Rt[i]; j != i; j = Rt[j]) { Up[Dn[j]] = Up[j]; Dn[Up[j]] = Dn[j]; Size[Col[j]]--; }
}
static void uncover(int c) {
    for (int i = Up[c]; i != c; i = Up[i])
        for (int j = Lf[i]; j != i; j = Lf[j]) { Size[Col[j]]++; Up[Dn[j]] = j; Dn[Up[j]] = j; }
    Lf[Rt[c]] = c; Rt[Lf[c]] = c;
}

static long nodes, budget;
static int best, depth, sol[MAXT], bestsol[MAXT], solved, finalsol[MAXT], finallen;
static clock_t t0;
static double maxs;
static int timed_out;

static int search(void) {
    if (Rt[root] == root) { memcpy(finalsol, sol, sizeof(int) * depth); finallen = depth; return 1; }
    if (++nodes > budget) return -1;
    if ((nodes & 4095) == 0 && (double)(clock() - t0) / CLOCKS_PER_SEC > maxs) { timed_out = 1; return -1; }
    int c = -1, bs = 1 << 30, bk = 0;
    for (int j = Rt[root]; j != root; j = Rt[j]) {
        if (Size[j] < bs || (Size[j] == bs && key[j] < bk)) { bs = Size[j]; bk = key[j]; c = j; }
    }
    if (bs == 0) return 0;
    cover(c);
    for (int r = Dn[c]; r != c; r = Dn[r]) {
        sol[depth++] = Rowid[r];
        if (depth > best) { best = depth; memcpy(bestsol, sol, sizeof(int) * depth); }
        for (int j = Rt[r]; j != r; j = Rt[j]) cover(Col[j]);
        int res = search();
        for (int j = Lf[r]; j != r; j = Lf[j]) uncover(Col[j]);
        depth--;
        if (res != 0) { uncover(c); return res; }
    }
    uncover(c);
    return 0;
}

int main(int argc, char **argv) {
    if (argc != 6) { fprintf(stderr, "usage: %s FILE ANCHOR SEED MAXSECONDS OUT\n", argv[0]); return 2; }
    FILE *f = fopen(argv[1], "r");
    if (!f || fscanf(f, "%d %d %d %d", &V, &NT, &R, &S) != 4) return 2;
    for (int t = 0; t < NT; t++) if (fscanf(f, "%d %d %d %d", &T[t][0], &T[t][1], &T[t][2], &hole[t]) != 4) return 2;
    fclose(f);
    int anchor = atoi(argv[2]);
    rs ^= (unsigned long long)(atoll(argv[3]) + 1) * 0xD1B54A32D192ED03ULL;
    maxs = atof(argv[4]);
    /* columns: 1..NT primary (triples), NT+1 .. NT+V*R secondary (p, c) */
    ncols = NT + V * R;
    int maxnodes = 1 + ncols + NT * R * 4 + 16;
    Lf = calloc(maxnodes, sizeof(int)); Rt = calloc(maxnodes, sizeof(int)); Up = calloc(maxnodes, sizeof(int));
    Dn = calloc(maxnodes, sizeof(int)); Col = calloc(maxnodes, sizeof(int)); Rowid = calloc(maxnodes, sizeof(int));
    Size = calloc(maxnodes, sizeof(int));
    root = 0; Lf[0] = Rt[0] = 0;
    for (int c = 1; c <= ncols; c++) {
        Up[c] = Dn[c] = c; Col[c] = c; Size[c] = 0;
        if (c <= NT) { Rt[c] = root; Lf[c] = Lf[root]; Rt[Lf[root]] = c; Lf[root] = c; }
        else { Lf[c] = Rt[c] = c; }
        key[c] = (int)(rnd() & 0x7fffffff);
    }
    nnodes = ncols + 1;
    /* anchored triples: those containing the anchor, in input order */
    int anc[MAXC], na = 0;
    for (int t = 0; t < NT; t++) if (T[t][0] == anchor || T[t][1] == anchor || T[t][2] == anchor) anc[na++] = t;
    if (na != R - S) { fprintf(stderr, "anchor degree %d != R-S\n", na); return 2; }
    int forced_row[MAXC];
    for (int t = 0; t < NT; t++) {
        int lo = hole[t] ? S : 0;
        int ai = -1;
        for (int k = 0; k < na; k++) if (anc[k] == t) ai = k;
        /* random colour order per triple */
        int order[MAXC], m = 0;
        for (int c = lo; c < R; c++) order[m++] = c;
        for (int i = m - 1; i > 0; i--) { int j = (int)(rnd() % (unsigned)(i + 1)); int tmp = order[i]; order[i] = order[j]; order[j] = tmp; }
        for (int k = 0; k < m; k++) {
            int c = order[k];
            if (ai >= 0 && c != S + ai) continue;
            int cols[4] = {1 + t, NT + 1 + T[t][0] * R + c, NT + 1 + T[t][1] * R + c, NT + 1 + T[t][2] * R + c};
            int first = -1;
            for (int q = 0; q < 4; q++) {
                int n = nnodes++, cc = cols[q];
                Col[n] = cc; Rowid[n] = nrows;
                Up[n] = Up[cc]; Dn[n] = cc; Dn[Up[cc]] = n; Up[cc] = n; Size[cc]++;
                if (first < 0) { first = n; Lf[n] = Rt[n] = n; }
                else { Rt[n] = first; Lf[n] = Lf[first]; Rt[Lf[first]] = n; Lf[first] = n; }
            }
            rowT[nrows] = t; rowC[nrows] = c;
            if (ai >= 0) forced_row[ai] = first;
            nrows++;
        }
    }
    /* apply the forced anchored rows */
    for (int k = 0; k < na; k++) {
        int r = forced_row[k];
        cover(Col[r]);
        for (int j = Rt[r]; j != r; j = Rt[j]) cover(Col[j]);
        sol[depth++] = Rowid[r];
    }
    best = depth;
    t0 = clock();
    int restarts = 0;
    budget = 100000;
    int res = 0;
    for (;;) {
        nodes = 0; timed_out = 0;
        res = search();
        if (res == 1) { solved = 1; break; }
        if (res == 0) break;            /* exhausted: no colouring with these forced rows */
        if (timed_out) break;
        restarts++; budget *= 2;
        for (int c = 1; c <= NT; c++) key[c] = (int)(rnd() & 0x7fffffff);
    }
    double secs = (double)(clock() - t0) / CLOCKS_PER_SEC;
    printf("%s best_depth %d of %d nodes_last %ld restarts %d seconds %.1f\n",
           solved ? "SOLVED" : (res == 0 ? "EXHAUSTED" : "UNSOLVED"), solved ? NT : best, NT, nodes, restarts, secs);
    if (solved) {
        int fd = open(argv[5], O_WRONLY | O_CREAT | O_EXCL, 0644);
        if (fd < 0) { perror("open OUT (exists?)"); return 3; }
        FILE *o = fdopen(fd, "w");
        for (int k = 0; k < finallen; k++) fprintf(o, "%d %d %d %d\n", T[rowT[finalsol[k]]][0], T[rowT[finalsol[k]]][1], T[rowT[finalsol[k]]][2], rowC[finalsol[k]]);
        fclose(o);
    }
    return solved ? 0 : 1;
}
