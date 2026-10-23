/* ls147_autpar.c - moqls7-ls147-parent-v1, parent-side independent code; no lane code used, linked or executed.
 * Explicit autoparatopism groups, computed without normalisation keys.
 * A paratopism of L factors uniquely as (isotopism) o (conjugation sigma), sigma in S_3, so
 *   |Par(L)| = sum over sigma of #{isotopisms (alpha, beta, gamma) from M = L^sigma onto L},
 * where the isotopism maps the triple (x, y, z) of M to (alpha(x), beta(y), gamma(z)), i.e.
 *   L[alpha(x)][beta(y)] = gamma(M[x][y]) for all 49 cells.
 * Such an isotopism is determined by alpha(0) and beta: row 0 of M forces gamma(M[0][c]) = L[alpha(0)][beta(c)], and
 * column 0 forces alpha(x) = the row of L holding gamma(M[x][0]) in column beta(0). So enumerate alpha(0) in 0..6 and
 * all 5040 beta (6 * 7 * 5040 = 211680 candidates per square), derive gamma and alpha, and test all 49 cells.
 * Each autoparatopism found is stored as a permutation of the 49 cells of L. The set is checked for repeated
 * permutations, for the identity, and for closure under composition (all ordered pairs; done when the set has at most
 * 6000 elements), so it is a group.
 * Input as ls147_norm.c (first token per line = 36-character key). Output: one JSON line per class.
 * Build: clang -O2 -Wall -Wextra -std=gnu11 -o ls147_autpar ls147_autpar.c
 */
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define N 7
#define NC 49
#define MAXSTORE 211680L
#define CLOSURE_MAX 6000L

static int S3[6][3], P7[5040][7], nS3 = 0, nP7 = 0;

static void gen3(int *a, int k, int used) {
    if (k == 3) { memcpy(S3[nS3++], a, 3 * sizeof(int)); return; }
    for (int v = 0; v < 3; v++) if (!(used >> v & 1)) { a[k] = v; gen3(a, k + 1, used | 1 << v); }
}
static void gen7(int *a, int k, int used) {
    if (k == 7) { memcpy(P7[nP7++], a, 7 * sizeof(int)); return; }
    for (int v = 0; v < 7; v++) if (!(used >> v & 1)) { a[k] = v; gen7(a, k + 1, used | 1 << v); }
}
static int is_latin(int A[N][N]) {
    for (int i = 0; i < N; i++) {
        int rm = 0, cm = 0;
        for (int j = 0; j < N; j++) {
            if (A[i][j] < 0 || A[i][j] >= N || A[j][i] < 0 || A[j][i] >= N) return 0;
            rm |= 1 << A[i][j];
            cm |= 1 << A[j][i];
        }
        if (rm != 0x7f || cm != 0x7f) return 0;
    }
    return 1;
}
static int parse_key(const char *tok, int L[N][N]) {
    if (strlen(tok) != 36) return 0;
    for (int j = 0; j < N; j++) { L[0][j] = j; L[j][0] = j; }
    for (int t = 0; t < 36; t++) {
        if (tok[t] < '0' || tok[t] > '9') return 0;
        L[1 + t / 6][1 + t % 6] = tok[t] - '0';
    }
    return 1;
}
static int cmp49(const void *a, const void *b) { return memcmp(a, b, NC); }

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: ls147_autpar CLASSES\n"); return 2; }
    int a[7];
    gen3(a, 0, 0);
    gen7(a, 0, 0);
    if (nS3 != 6 || nP7 != 5040) return 9;
    FILE *f = fopen(argv[1], "r");
    if (!f) { perror("open"); return 3; }
    uint8_t (*store)[NC] = malloc(MAXSTORE * NC);
    if (!store) return 4;
    uint8_t idperm[NC];
    for (int i = 0; i < NC; i++) idperm[i] = (uint8_t)i;
    char line[4096];
    long nclass = 0;
    while (fgets(line, sizeof line, f)) {
        char tok[128];
        if (sscanf(line, "%127s", tok) != 1) continue;
        long idx = nclass++;
        int L[N][N];
        int parsed = parse_key(tok, L);
        if (!parsed || !is_latin(L)) {
            printf("{\"idx\":%ld,\"input_parsed\":%d,\"input_valid\":0}\n", idx, parsed);
            fflush(stdout);
            continue;
        }
        int colpos[N][N];                       /* colpos[c][s] = row of L with symbol s in column c */
        for (int r = 0; r < N; r++) for (int c = 0; c < N; c++) colpos[c][L[r][c]] = r;
        long cnt[6] = {0}, cand = 0, anomalies = 0, np = 0, badperm = 0;
        for (int s = 0; s < 6; s++) {
            int M[N][N];
            for (int r = 0; r < N; r++) for (int c = 0; c < N; c++) M[r][c] = -1;
            for (int r = 0; r < N; r++) for (int c = 0; c < N; c++) {
                int t[3] = {r, c, L[r][c]};
                M[t[S3[s][0]]][t[S3[s][1]]] = t[S3[s][2]];
            }
            if (!is_latin(M)) { anomalies++; continue; }
            for (int rp = 0; rp < N; rp++) for (int b = 0; b < 5040; b++) {
                const int *be = P7[b];
                int gam[N], al[N], gm = 0, am = 0;
                cand++;
                for (int c = 0; c < N; c++) { gam[M[0][c]] = L[rp][be[c]]; gm |= 1 << M[0][c]; }
                if (gm != 0x7f) { anomalies++; continue; }
                for (int x = 0; x < N; x++) { al[x] = colpos[be[0]][gam[M[x][0]]]; am |= 1 << al[x]; }
                if (am != 0x7f || al[0] != rp) { anomalies++; continue; }
                int ok = 1;
                for (int x = 0; x < N && ok; x++)
                    for (int y = 0; y < N; y++)
                        if (L[al[x]][be[y]] != gam[M[x][y]]) { ok = 0; break; }
                if (!ok) continue;
                cnt[s]++;
                if (np >= MAXSTORE) { anomalies++; continue; }
                uint64_t seen = 0;
                for (int r = 0; r < N; r++) for (int c = 0; c < N; c++) {
                    int t[3] = {r, c, L[r][c]};
                    int img = N * al[t[S3[s][0]]] + be[t[S3[s][1]]];
                    store[np][N * r + c] = (uint8_t)img;
                    seen |= 1ULL << img;
                }
                if (seen != (1ULL << NC) - 1) badperm++;
                np++;
            }
        }
        qsort(store, (size_t)np, NC, cmp49);
        long distinct = 0;
        for (long i = 0; i < np; i++) if (i == 0 || memcmp(store[i], store[i - 1], NC)) distinct++;
        int idpresent = bsearch(idperm, store, (size_t)np, NC, cmp49) != NULL;
        long pairs = 0, fails = 0;
        int closure_done = 0;
        if (np <= CLOSURE_MAX) {
            closure_done = 1;
            uint8_t comp[NC];
            for (long i = 0; i < np; i++) for (long j = 0; j < np; j++) {
                for (int k = 0; k < NC; k++) comp[k] = store[i][store[j][k]];
                pairs++;
                if (!bsearch(comp, store, (size_t)np, NC, cmp49)) fails++;
            }
        }
        long atp = cnt[0];
        int cosets_equal = 1;
        for (int s = 0; s < 6; s++) if (cnt[s] != 0 && cnt[s] != atp) cosets_equal = 0;
        printf("{\"idx\":%ld,\"input_parsed\":1,\"input_valid\":1,\"candidates\":%ld,\"par_explicit\":%ld,"
               "\"atp_explicit\":%ld,\"per_sigma\":[%ld,%ld,%ld,%ld,%ld,%ld],\"nonzero_sigma_counts_equal_atp\":%d,"
               "\"anomalies\":%ld,\"bad_cell_perms\":%ld,\"distinct_cell_perms\":%ld,\"identity_present\":%d,"
               "\"closure_done\":%d,\"closure_pairs\":%ld,\"closure_failures\":%ld}\n",
               idx, cand, np, atp, cnt[0], cnt[1], cnt[2], cnt[3], cnt[4], cnt[5], cosets_equal, anomalies, badperm,
               distinct, idpresent, closure_done, pairs, fails);
        fflush(stdout);
        fprintf(stderr, "class %ld done, cpu_s %.2f\n", idx, (double)clock() / CLOCKS_PER_SEC);
    }
    fclose(f);
    free(store);
    return 0;
}
