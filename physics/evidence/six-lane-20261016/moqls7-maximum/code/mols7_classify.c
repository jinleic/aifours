/* mols7_classify.c — lane moqls7-maximum.
 * (1) Enumerates all REDUCED lists (L1, L2) of 2-MOLS(7) in the Egan–Wanless sense (arXiv:1406.3681v2, LF185–187):
 *     both squares have row 0 in natural order and L1 has column 0 in natural order.
 *     Expected count (Table 6, n=7, k=2, "Equality"): 342480.
 * (2) Partitions them into paratopism classes (= isomorphism classes of 4-nets of order 7) by orbit computation:
 *     for a net N, every normalization (ordering of the 4 parallel classes as rows/cols/L1/L2: 24; origin point p: 49;
 *     ordering of the 6 other points of the row line through p: 720) yields a reduced list; the set of these is
 *     exactly the set of reduced lists paratopic to N (Theorem 3.2: its size is 846720/|par(N)|).
 *     Repeatedly take the first unclassified reduced list, compute its orbit, check the orbit is a subset of the
 *     enumeration, and remove it. The orbits partition the enumeration; their number is the number of classes.
 * (3) For each class: |par| = 846720/orbit size, number of transversals of the net (7-sets meeting each line once),
 *     maximality (no 7 pairwise disjoint transversals), and a representative (the first reduced list met).
 * Output (stdout): one JSON object per class, then a summary line. Exact integer arithmetic only.
 * Build: clang -O2 -o mols7_classify mols7_classify.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 7
#define NP 49
#define KEYLEN 78

typedef struct { unsigned char k[KEYLEN]; } Key;

static int L1[N][N], L2[N][N];
static int rowA[N][N], colA[N][N], rowB[N][N], colB[N][N], usedpair[N][N];
static Key *E = NULL; static long nE = 0, capE = 0;

static void make_key(int A[N][N], int B[N][N], Key *out) {
    int t = 0;
    for (int r = 1; r < N; r++) for (int c = 1; c < N; c++) out->k[t++] = (unsigned char)A[r][c];
    for (int r = 1; r < N; r++) for (int c = 0; c < N; c++) out->k[t++] = (unsigned char)B[r][c];
}

static void push_E(void) {
    if (nE == capE) { capE = capE ? capE * 2 : 1 << 16; E = realloc(E, capE * sizeof(Key)); }
    make_key(L1, L2, &E[nE++]);
}

static void rec(int cell) {
    if (cell == NP) { push_E(); return; }
    int r = cell / N, c = cell % N;
    if (r == 0) { rec(cell + 1); return; }
    int alo = 0, ahi = N - 1;
    if (c == 0) { alo = ahi = r; }
    for (int a = alo; a <= ahi; a++) {
        if (rowA[r][a] || colA[c][a]) continue;
        for (int b = 0; b < N; b++) {
            if (rowB[r][b] || colB[c][b] || usedpair[a][b]) continue;
            L1[r][c] = a; L2[r][c] = b;
            rowA[r][a] = colA[c][a] = rowB[r][b] = colB[c][b] = usedpair[a][b] = 1;
            rec(cell + 1);
            rowA[r][a] = colA[c][a] = rowB[r][b] = colB[c][b] = usedpair[a][b] = 0;
        }
    }
}

static int keycmp(const void *x, const void *y) { return memcmp(x, y, KEYLEN); }

/* net from a key: point index q = 7r + c, coordinates (r, c, L1, L2) */
static void key_to_net(const Key *K, int net[NP][4]) {
    int A[N][N], B[N][N], t = 0;
    for (int c = 0; c < N; c++) { A[0][c] = c; B[0][c] = c; }
    for (int r = 1; r < N; r++) A[r][0] = r;
    for (int r = 1; r < N; r++) for (int c = 1; c < N; c++) A[r][c] = K->k[t++];
    for (int r = 1; r < N; r++) for (int c = 0; c < N; c++) B[r][c] = K->k[t++];
    for (int r = 0; r < N; r++) for (int c = 0; c < N; c++) {
        int q = N * r + c; net[q][0] = r; net[q][1] = c; net[q][2] = A[r][c]; net[q][3] = B[r][c];
    }
}

static int perms4[24][4], perms6[720][6];
static void gen_perms(void) {
    int n = 0;
    for (int a = 0; a < 4; a++) for (int b = 0; b < 4; b++) for (int c = 0; c < 4; c++) for (int d = 0; d < 4; d++)
        if (a != b && a != c && a != d && b != c && b != d && c != d) { perms4[n][0]=a; perms4[n][1]=b; perms4[n][2]=c; perms4[n][3]=d; n++; }
    int p[6] = {0,1,2,3,4,5}; n = 0;
    /* lexicographic permutations */
    while (1) {
        memcpy(perms6[n++], p, sizeof p);
        int i = 4; while (i >= 0 && p[i] > p[i+1]) i--; if (i < 0) break;
        int j = 5; while (p[j] < p[i]) j--; int t = p[i]; p[i] = p[j]; p[j] = t;
        for (int a = i+1, b = 5; a < b; a++, b--) { t = p[a]; p[a] = p[b]; p[b] = t; }
    }
}

/* all 846720 normalizations of a net -> keys (with duplicates) */
static long orbit_keys(int net[NP][4], Key *out) {
    long n = 0;
    for (int s = 0; s < 24; s++) {
        int *sg = perms4[s];
        for (int p = 0; p < NP; p++) {
            int R0[N], m = 0;
            R0[m++] = p;
            for (int q = 0; q < NP; q++) if (q != p && net[q][sg[0]] == net[p][sg[0]]) R0[m++] = q;
            for (int o = 0; o < 720; o++) {
                int ord[N]; ord[0] = R0[0];
                for (int i = 0; i < 6; i++) ord[i+1] = R0[1 + perms6[o][i]];
                int collab[N], l1lab[N], l2lab[N], rowlab[N];
                for (int c = 0; c < N; c++) {
                    collab[net[ord[c]][sg[1]]] = c; l1lab[net[ord[c]][sg[2]]] = c; l2lab[net[ord[c]][sg[3]]] = c;
                }
                /* column-0 line = class sg[1] line through p; row label := new L1 label */
                for (int q = 0; q < NP; q++) if (net[q][sg[1]] == net[p][sg[1]]) rowlab[net[q][sg[0]]] = l1lab[net[q][sg[2]]];
                int A[N][N], B[N][N];
                for (int q = 0; q < NP; q++) {
                    int r = rowlab[net[q][sg[0]]], c = collab[net[q][sg[1]]];
                    A[r][c] = l1lab[net[q][sg[2]]]; B[r][c] = l2lab[net[q][sg[3]]];
                }
                make_key(A, B, &out[n++]);
            }
        }
    }
    return n;
}

/* transversals of the 4-net: 7 points, one per line of each class; count by backtracking over rows */
static int trans_count; static int tr_store[2000][N]; static int ntr;
static void trans_rec(int net[NP][4], int r, int usedc[N], int used2[N], int used3[N], int cur[N]) {
    if (r == N) { if (ntr < 2000) memcpy(tr_store[ntr], cur, sizeof(int)*N); ntr++; trans_count++; return; }
    for (int c = 0; c < N; c++) {
        int q = N * r + c;
        if (usedc[c] || used2[net[q][2]] || used3[net[q][3]]) continue;
        usedc[c] = used2[net[q][2]] = used3[net[q][3]] = 1; cur[r] = q;
        trans_rec(net, r + 1, usedc, used2, used3, cur);
        usedc[c] = used2[net[q][2]] = used3[net[q][3]] = 0;
    }
}
/* maximal iff no 7 pairwise disjoint transversals (exact cover of the 49 points) */
static int cover_found;
static void cover_rec(int nt, unsigned long long used, int depth) {
    if (cover_found) return;
    if (depth == N) { cover_found = 1; return; }
    int first = -1; for (int q = 0; q < NP; q++) if (!(used >> q & 1ULL)) { first = q; break; }
    for (int t = 0; t < nt; t++) {
        int ok = 1, has = 0; unsigned long long m = 0;
        for (int i = 0; i < N; i++) { int q = tr_store[t][i]; if (used >> q & 1ULL) { ok = 0; break; } m |= 1ULL << q; if (q == first) has = 1; }
        if (ok && has) cover_rec(nt, used | m, depth + 1);
    }
}

int main(void) {
    for (int c = 0; c < N; c++) { L1[0][c] = c; L2[0][c] = c; rowA[0][c] = colA[c][c] = 1; rowB[0][c] = colB[c][c] = 1; usedpair[c][c] = 1; }
    rec(0);
    qsort(E, nE, sizeof(Key), keycmp);
    fprintf(stderr, "reduced lists enumerated: %ld\n", nE);
    gen_perms();
    char *done = calloc(nE, 1);
    Key *buf = malloc(846720L * sizeof(Key));
    long remaining = nE; int ncls = 0; long total = 0;
    printf("{\"reduced_lists\": %ld}\n", nE);
    for (long i = 0; i < nE; i++) {
        if (done[i]) continue;
        int net[NP][4]; key_to_net(&E[i], net);
        long n = orbit_keys(net, buf);
        qsort(buf, n, sizeof(Key), keycmp);
        long distinct = 0, notin = 0;
        for (long j = 0; j < n; j++) {
            if (j > 0 && memcmp(&buf[j], &buf[j-1], KEYLEN) == 0) continue;
            distinct++;
            Key *f = bsearch(&buf[j], E, nE, sizeof(Key), keycmp);
            if (!f) { notin++; continue; }
            long idx = f - E;
            if (done[idx]) { fprintf(stderr, "ERROR: orbit overlaps a previous class\n"); return 2; }
            done[idx] = 1;
        }
        remaining -= distinct - notin; total += distinct;
        trans_count = 0; ntr = 0; int usedc[N]={0}, u2[N]={0}, u3[N]={0}, cur[N];
        trans_rec(net, 0, usedc, u2, u3, cur);
        cover_found = 0; if (ntr <= 2000) cover_rec(ntr, 0ULL, 0); else cover_found = -1;
        printf("{\"class\": %d, \"orbit_size\": %ld, \"par_order_numerator\": 846720, \"par_order\": %ld, "
               "\"par_exact\": %s, \"orbit_keys_not_in_enumeration\": %ld, \"transversals\": %d, \"maximal\": %s, \"rep_L1\": [",
               ncls, distinct, 846720L / distinct, (846720L % distinct == 0) ? "true" : "false", notin, trans_count,
               cover_found == 1 ? "false" : (cover_found == 0 ? "true" : "\"unknown\""));
        for (int r = 0; r < N; r++) { printf("%s[", r ? "," : ""); for (int c = 0; c < N; c++) printf("%s%d", c ? "," : "", net[N*r+c][2]); printf("]"); }
        printf("], \"rep_L2\": [");
        for (int r = 0; r < N; r++) { printf("%s[", r ? "," : ""); for (int c = 0; c < N; c++) printf("%s%d", c ? "," : "", net[N*r+c][3]); printf("]"); }
        printf("]}\n");
        fflush(stdout);
        ncls++;
    }
    printf("{\"classes\": %d, \"sum_orbit_sizes\": %ld, \"unclassified_left\": %ld}\n", ncls, total, remaining);
    return 0;
}
