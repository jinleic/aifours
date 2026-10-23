/* ls_classes.c — lane moqls7-maximum. Main classes (paratopy classes) of Latin squares of order 7.
 * A Latin square is the 3-net (rows, columns, symbols). A normalisation = (ordering of the 3 classes) x (origin cell)
 * x (ordering of the 6 other cells on the origin's first-class line): 6*49*720 = 211680 normalisations, each giving a
 * unique REDUCED square (row 0 and column 0 in natural order). Paratopisms act freely on normalisations, so the number
 * of distinct reduced squares in the main class is 211680/|Par(L)| and |Par(L)| = multiplicity of the minimum key.
 * Completeness: summing 211680/|Par| over the classes found must give 16942080 (reduced Latin squares of order 7).
 * Search: breadth-first closure under row-cycle switches applied to all 6 conjugates, from the Z_7 table.
 * Output (stdout): one line per class: "<36-digit key> <reduced count> <|Par|>" then a summary line on stderr.
 * Build: clang -O2 -o ls_classes ls_classes.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 7
#define KL 36
#define MAXC 4096
static int perms6[720][6];
static const int conj3[6][3] = {{0,1,2},{0,2,1},{1,0,2},{1,2,0},{2,0,1},{2,1,0}};

static void gen_perms(void) {
    int p[6] = {0,1,2,3,4,5}, n = 0;
    while (1) {
        memcpy(perms6[n++], p, sizeof p);
        int i = 4; while (i >= 0 && p[i] > p[i+1]) i--; if (i < 0) break;
        int j = 5; while (p[j] < p[i]) j--; int t = p[i]; p[i] = p[j]; p[j] = t;
        for (int a = i+1, b = 5; a < b; a++, b--) { t = p[a]; p[a] = p[b]; p[b] = t; }
    }
}

/* triples (r,c,s) of the square */
static void canon(int L[N][N], unsigned char *best, long *mult) {
    int T[49][3], m = 0;
    for (int r = 0; r < N; r++) for (int c = 0; c < N; c++) { T[m][0] = r; T[m][1] = c; T[m][2] = L[r][c]; m++; }
    unsigned char cur[KL]; int have = 0; long cnt = 0;
    for (int s = 0; s < 6; s++) {
        int a = conj3[s][0], b = conj3[s][1], d = conj3[s][2];   /* new row class a, new col class b, new symbol d */
        for (int o = 0; o < 49; o++) {
            /* cells on the origin's class-a line */
            int R0[N], k = 0; R0[k++] = o;
            for (int q = 0; q < 49; q++) if (q != o && T[q][a] == T[o][a]) R0[k++] = q;
            for (int pi = 0; pi < 720; pi++) {
                int ord[N]; ord[0] = R0[0];
                for (int i = 0; i < 6; i++) ord[i+1] = R0[1 + perms6[pi][i]];
                int collab[N], symlab[N], rowlab[N];
                for (int c = 0; c < N; c++) { collab[T[ord[c]][b]] = c; symlab[T[ord[c]][d]] = c; }
                /* rows labelled by the symbol in new column 0 (origin's class-b line) */
                for (int q = 0; q < 49; q++) if (T[q][b] == T[o][b]) rowlab[T[q][a]] = symlab[T[q][d]];
                int A[N][N];
                for (int q = 0; q < 49; q++) A[rowlab[T[q][a]]][collab[T[q][b]]] = symlab[T[q][d]];
                int t = 0;
                for (int r = 1; r < N; r++) for (int c = 1; c < N; c++) cur[t++] = (unsigned char)A[r][c];
                int cmp = have ? memcmp(cur, best, KL) : -1;
                if (cmp < 0) { memcpy(best, cur, KL); have = 1; cnt = 1; }
                else if (cmp == 0) cnt++;
            }
        }
    }
    *mult = cnt;
}

static void key_to_square(const unsigned char *key, int L[N][N]) {
    for (int c = 0; c < N; c++) L[0][c] = c;
    for (int r = 0; r < N; r++) L[r][0] = r;
    int t = 0;
    for (int r = 1; r < N; r++) for (int c = 1; c < N; c++) L[r][c] = key[t++];
}

static unsigned char keys[MAXC][KL];
static long pars[MAXC];
static int nclass = 0;

static int find_or_add(const unsigned char *k, long par) {
    for (int i = 0; i < nclass; i++) if (!memcmp(keys[i], k, KL)) return 0;
    if (nclass >= MAXC) { fprintf(stderr, "overflow\n"); exit(2); }
    memcpy(keys[nclass], k, KL); pars[nclass] = par; nclass++;
    return 1;
}

static void conjugate(int L[N][N], int s, int out[N][N]) {
    for (int r = 0; r < N; r++) for (int c = 0; c < N; c++) {
        int v[3] = {r, c, L[r][c]};
        out[v[conj3[s][0]]][v[conj3[s][1]]] = v[conj3[s][2]];
    }
}

int main(void) {
    gen_perms();
    int L[N][N];
    unsigned char k[KL]; long par;
    for (int r = 0; r < N; r++) for (int c = 0; c < N; c++) L[r][c] = (r + c) % N;   /* Z_7 (atomic: no switches) */
    canon(L, k, &par); find_or_add(k, par);
    /* further seeds from stdin: 49 integers per square */
    while (1) {
        int ok = 1;
        for (int r = 0; r < N && ok; r++) for (int c = 0; c < N && ok; c++) if (scanf("%d", &L[r][c]) != 1) ok = 0;
        if (!ok) break;
        canon(L, k, &par); find_or_add(k, par);
    }
    fprintf(stderr, "seed classes %d\n", nclass);
    for (int head = 0; head < nclass; head++) {
        int B[N][N]; key_to_square(keys[head], B);
        for (int s = 0; s < 6; s++) {
            int C[N][N]; conjugate(B, s, C);
            for (int r1 = 0; r1 < N; r1++) for (int r2 = r1 + 1; r2 < N; r2++) {
                /* cycles of the permutation c -> column where row r1 has symbol C[r2][c] */
                int pos1[N]; for (int c = 0; c < N; c++) pos1[C[r1][c]] = c;
                int seen[N] = {0};
                for (int c0 = 0; c0 < N; c0++) {
                    if (seen[c0]) continue;
                    int cyc[N], len = 0, c = c0;
                    while (!seen[c]) { seen[c] = 1; cyc[len++] = c; c = pos1[C[r2][c]]; }
                    if (len == N) continue;               /* switching the whole rows is an isotopy */
                    int D[N][N]; memcpy(D, C, sizeof D);
                    for (int i = 0; i < len; i++) { int cc = cyc[i]; int t = D[r1][cc]; D[r1][cc] = D[r2][cc]; D[r2][cc] = t; }
                    canon(D, k, &par);
                    find_or_add(k, par);
                }
            }
        }
        fprintf(stderr, "processed %d / %d classes\n", head + 1, nclass);
    }
    long total = 0;
    for (int i = 0; i < nclass; i++) {
        long red = 211680 / pars[i];
        if (red * pars[i] != 211680) fprintf(stderr, "non-divisible par %ld\n", pars[i]);
        total += red;
        for (int t = 0; t < KL; t++) printf("%d", keys[i][t]);
        printf(" %ld %ld\n", red, pars[i]);
    }
    fprintf(stderr, "classes %d total_reduced %ld (expected 16942080) %s\n", nclass, total,
            total == 16942080 ? "MATCH" : "MISMATCH");
    return 0;
}
