/* net_canon.c — lane moqls7-maximum.
 * Reads 4-nets of order 7 from stdin, one per line: 196 integers = for points q = 0..48 the line labels
 * (l0,l1,l2,l3) in 0..6 of the 4 parallel classes. For each net it computes all 846720 normalizations
 * (24 class orderings x 49 origins x 720 orderings of the origin's row line), each giving a REDUCED list of 2-MOLS(7)
 * in the Egan–Wanless sense (rows/cols/L1/L2 with row 0 = (0,c,c,c) and L1 column 0 in order). It outputs:
 *   canonical key = lexicographically smallest reduced list (78 bytes: L1 rows 1..6 cols 1..6, L2 rows 1..6 cols 0..6),
 *   distinct = number of distinct reduced lists = 846720/|par| (Theorem 3.2 of Egan–Wanless), and |par|.
 * Output line: "<canonical key as 78 digits> <distinct> <par> <par_exact 0/1>".
 * Build: clang -O2 -o net_canon net_canon.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define N 7
#define NP 49
#define KEYLEN 78
typedef struct { unsigned char k[KEYLEN]; } Key;
static int perms4[24][4], perms6[720][6];

static void gen_perms(void) {
    int n = 0;
    for (int a = 0; a < 4; a++) for (int b = 0; b < 4; b++) for (int c = 0; c < 4; c++) for (int d = 0; d < 4; d++)
        if (a != b && a != c && a != d && b != c && b != d && c != d) { perms4[n][0]=a; perms4[n][1]=b; perms4[n][2]=c; perms4[n][3]=d; n++; }
    int p[6] = {0,1,2,3,4,5}; n = 0;
    while (1) {
        memcpy(perms6[n++], p, sizeof p);
        int i = 4; while (i >= 0 && p[i] > p[i+1]) i--; if (i < 0) break;
        int j = 5; while (p[j] < p[i]) j--; int t = p[i]; p[i] = p[j]; p[j] = t;
        for (int a = i+1, b = 5; a < b; a++, b--) { t = p[a]; p[a] = p[b]; p[b] = t; }
    }
}
static int keycmp(const void *x, const void *y) { return memcmp(x, y, KEYLEN); }

static long orbit_keys(int net[NP][4], Key *out) {
    long n = 0;
    for (int s = 0; s < 24; s++) {
        int *sg = perms4[s];
        for (int p = 0; p < NP; p++) {
            int R0[N], m = 0; R0[m++] = p;
            for (int q = 0; q < NP; q++) if (q != p && net[q][sg[0]] == net[p][sg[0]]) R0[m++] = q;
            if (m != N) { fprintf(stderr, "not a net\n"); exit(3); }
            for (int o = 0; o < 720; o++) {
                int ord[N]; ord[0] = R0[0];
                for (int i = 0; i < 6; i++) ord[i+1] = R0[1 + perms6[o][i]];
                int collab[N], l1lab[N], l2lab[N], rowlab[N];
                for (int c = 0; c < N; c++) { collab[net[ord[c]][sg[1]]] = c; l1lab[net[ord[c]][sg[2]]] = c; l2lab[net[ord[c]][sg[3]]] = c; }
                for (int q = 0; q < NP; q++) if (net[q][sg[1]] == net[p][sg[1]]) rowlab[net[q][sg[0]]] = l1lab[net[q][sg[2]]];
                int A[N][N], B[N][N];
                for (int q = 0; q < NP; q++) { int r = rowlab[net[q][sg[0]]], c = collab[net[q][sg[1]]]; A[r][c] = l1lab[net[q][sg[2]]]; B[r][c] = l2lab[net[q][sg[3]]]; }
                int t = 0;
                for (int r = 1; r < N; r++) for (int c = 1; c < N; c++) out[n].k[t++] = (unsigned char)A[r][c];
                for (int r = 1; r < N; r++) for (int c = 0; c < N; c++) out[n].k[t++] = (unsigned char)B[r][c];
                n++;
            }
        }
    }
    return n;
}

int main(void) {
    gen_perms();
    Key *buf = malloc(846720L * sizeof(Key));
    int net[NP][4];
    while (1) {
        int ok = 1;
        for (int q = 0; q < NP && ok; q++) for (int c = 0; c < 4; c++) if (scanf("%d", &net[q][c]) != 1) { ok = 0; break; }
        if (!ok) break;
        long n = orbit_keys(net, buf);
        qsort(buf, n, sizeof(Key), keycmp);
        long distinct = 0;
        for (long j = 0; j < n; j++) if (j == 0 || memcmp(&buf[j], &buf[j-1], KEYLEN)) distinct++;
        for (int t = 0; t < KEYLEN; t++) putchar('0' + buf[0].k[t]);
        printf(" %ld %ld %d\n", distinct, 846720L / distinct, (846720L % distinct) == 0);
        fflush(stdout);
    }
    return 0;
}
