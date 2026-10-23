/* ls147_norm.c - moqls7-ls147-parent-v1, parent-side independent code. Written from the definitions (Egan-Wanless
 * arXiv:1406.3681v2 sections 2-3 with k = 1: a Latin square is its 49 triples (row, column, symbol); paratopism is
 * S_7 wr S_3 acting on them). No lane code is used, linked or executed.
 *
 * Input (argv[1]): text file; on each non-empty line the first token is a 36-character key = the interior (rows 1..6,
 *   columns 1..6, row-major) of a reduced Latin square of order 7 (row 0 and column 0 are 0..6). Further tokens (the
 *   claimed counts) are ignored here; the Python checker binds them to what this program derives.
 * Normalisation parameters, 211680 = 3! * 49 * 6!: sigma in S_3 (M = L^sigma, triple t -> (t[s0], t[s1], t[s2])),
 *   an origin cell (r0, c0) of M (49), and an ordering pi of the 6 other cells of row r0 of M (720). With
 *   beta = (c0, pi(others)): lambda(M[r0][beta[j]]) = j, rho(r) = lambda(M[r][c0]), R[rho(r)][j] = lambda(M[r][beta[j]]).
 *   R is reduced, and paratopic to L by construction (conjugation sigma, then the isotopism (rho, beta^-1, lambda)).
 * Key of R = base-7 integer of its 36 interior entries in row-major order (numeric order = lexicographic order).
 * Per class (stdout, one JSON line): canonical key = minimum key, multiplicity of the minimum, multiplicity of the
 *   input's own key, number of distinct keys, minimum/maximum multiplicity over all distinct keys, validity counters
 *   (every R is checked to be a reduced Latin square; every lambda/rho to be a bijection; every M to be Latin).
 * argv[2] (optional): union capacity C (0 = off). If C > 0, the distinct keys of every class are appended to one array
 *   of C 16-byte keys (allocated when first needed), which is sorted at the end; union size and cross-class
 *   duplicates are reported. Memory is about 16*C bytes plus 3.4 MB.
 * Build: clang -O2 -Wall -Wextra -std=gnu11 -o ls147_norm ls147_norm.c
 */
#include <limits.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define N 7
#define NPAR 211680L
typedef unsigned __int128 u128;

static int S3[6][3], P6[720][6], nS3 = 0, nP6 = 0;

static void gen3(int *a, int k, int used) {
    if (k == 3) { memcpy(S3[nS3++], a, 3 * sizeof(int)); return; }
    for (int v = 0; v < 3; v++) if (!(used >> v & 1)) { a[k] = v; gen3(a, k + 1, used | 1 << v); }
}
static void gen6(int *a, int k, int used) {
    if (k == 6) { memcpy(P6[nP6++], a, 6 * sizeof(int)); return; }
    for (int v = 0; v < 6; v++) if (!(used >> v & 1)) { a[k] = v; gen6(a, k + 1, used | 1 << v); }
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
static int is_reduced(int A[N][N]) {
    for (int j = 0; j < N; j++) if (A[0][j] != j || A[j][0] != j) return 0;
    return 1;
}
static u128 key_of(int A[N][N]) {
    u128 k = 0;
    for (int i = 1; i < N; i++) for (int j = 1; j < N; j++) k = k * 7 + (u128)A[i][j];
    return k;
}
static void key_str(u128 k, char *s) {
    for (int t = 35; t >= 0; t--) { s[t] = (char)('0' + (int)(k % 7)); k /= 7; }
    s[36] = 0;
}
static int cmp128(const void *a, const void *b) {
    u128 x = *(const u128 *)a, y = *(const u128 *)b;
    return (x > y) - (x < y);
}
/* 1 if tok is 36 decimal digits (values 7..9 are kept so that the Latin test rejects them) */
static int parse_key(const char *tok, int L[N][N]) {
    if (strlen(tok) != 36) return 0;
    for (int j = 0; j < N; j++) { L[0][j] = j; L[j][0] = j; }
    for (int t = 0; t < 36; t++) {
        if (tok[t] < '0' || tok[t] > '9') return 0;
        L[1 + t / 6][1 + t % 6] = tok[t] - '0';
    }
    return 1;
}

int main(int argc, char **argv) {
    if (argc < 2) { fprintf(stderr, "usage: ls147_norm CLASSES [UNION_CAPACITY]\n"); return 2; }
    long cap = argc > 2 ? atol(argv[2]) : 0;
    int a[6];
    gen3(a, 0, 0);
    gen6(a, 0, 0);
    if (nS3 != 6 || nP6 != 720) return 9;
    for (int i = 0; i < 3; i++) if (S3[0][i] != i) return 9;   /* S3[0] = identity */
    for (int i = 0; i < 6; i++) if (P6[0][i] != i) return 9;   /* P6[0] = identity */
    FILE *f = fopen(argv[1], "r");
    if (!f) { perror("open"); return 3; }
    u128 *buf = malloc(NPAR * sizeof(u128));
    if (!buf) return 4;
    u128 *U = NULL;
    long un = 0, nclass = 0, nvalid = 0, sumdistinct = 0;
    int overflow = 0;
    char line[4096];
    while (fgets(line, sizeof line, f)) {
        char tok[128];
        if (sscanf(line, "%127s", tok) != 1) continue;
        long idx = nclass++;
        int L[N][N];
        int parsed = parse_key(tok, L);
        if (!parsed || !is_latin(L) || !is_reduced(L)) {
            printf("{\"idx\":%ld,\"input_parsed\":%d,\"input_valid\":0}\n", idx, parsed);
            fflush(stdout);
            continue;
        }
        nvalid++;
        u128 kin = key_of(L);
        long n = 0, bijfail = 0, conjbad = 0, badR = 0;
        int idok = 0, idseen = 0;
        for (int s = 0; s < 6; s++) {
            int M[N][N];
            for (int r = 0; r < N; r++) for (int c = 0; c < N; c++) M[r][c] = -1;
            int clash = 0;
            for (int r = 0; r < N; r++) for (int c = 0; c < N; c++) {
                int t[3] = {r, c, L[r][c]};
                int x = t[S3[s][0]], y = t[S3[s][1]], z = t[S3[s][2]];
                if (M[x][y] != -1) clash = 1;
                M[x][y] = z;
            }
            if (clash || !is_latin(M)) { conjbad++; continue; }
            for (int r0 = 0; r0 < N; r0++) for (int c0 = 0; c0 < N; c0++) {
                int oth[6], m = 0;
                for (int c = 0; c < N; c++) if (c != c0) oth[m++] = c;
                for (int p = 0; p < 720; p++) {
                    int beta[N], lam[N], rho[N], R[N][N], lm = 0, rm = 0;
                    beta[0] = c0;
                    for (int i = 0; i < 6; i++) beta[1 + i] = oth[P6[p][i]];
                    for (int j = 0; j < N; j++) { int v = M[r0][beta[j]]; lam[v] = j; lm |= 1 << v; }
                    if (lm != 0x7f) { bijfail++; continue; }
                    for (int r = 0; r < N; r++) { rho[r] = lam[M[r][c0]]; rm |= 1 << rho[r]; }
                    if (rm != 0x7f) { bijfail++; continue; }
                    for (int r = 0; r < N; r++) for (int j = 0; j < N; j++) R[rho[r]][j] = lam[M[r][beta[j]]];
                    if (!is_reduced(R) || !is_latin(R)) badR++;
                    u128 k = key_of(R);
                    if (s == 0 && r0 == 0 && c0 == 0 && p == 0) { idseen = 1; idok = (k == kin); }
                    buf[n++] = k;
                }
            }
        }
        qsort(buf, (size_t)n, sizeof(u128), cmp128);
        long distinct = 0, runmin = LONG_MAX, runmax = 0, multmin = 0, multin = 0;
        for (long i = 0; i < n;) {
            long j = i;
            while (j < n && buf[j] == buf[i]) j++;
            long run = j - i;
            distinct++;
            if (run < runmin) runmin = run;
            if (run > runmax) runmax = run;
            if (i == 0) multmin = run;
            if (buf[i] == kin) multin = run;
            if (cap > 0 && !overflow) {
                if (!U) {
                    U = malloc((size_t)cap * sizeof(u128));
                    if (!U) { fprintf(stderr, "union allocation failed\n"); return 5; }
                }
                if (un < cap) U[un++] = buf[i]; else overflow = 1;
            }
            i = j;
        }
        if (n == 0) runmin = 0;
        sumdistinct += distinct;
        char ks[37], kc[37];
        key_str(kin, ks);
        key_str(n ? buf[0] : 0, kc);
        printf("{\"idx\":%ld,\"input_parsed\":1,\"input_valid\":1,\"input_key\":\"%s\",\"params\":%ld,\"bij_fail\":%ld,"
               "\"conj_bad\":%ld,\"invalid_R\":%ld,\"identity_param_seen\":%d,\"identity_param_key_equals_input\":%d,"
               "\"canon_key\":\"%s\",\"mult_canon\":%ld,\"mult_input\":%ld,\"distinct\":%ld,\"run_min\":%ld,"
               "\"run_max\":%ld}\n",
               idx, ks, n, bijfail, conjbad, badR, idseen, idok, kc, multmin, multin, distinct, runmin, runmax);
        fflush(stdout);
        fprintf(stderr, "class %ld done, cpu_s %.2f\n", idx, (double)clock() / CLOCKS_PER_SEC);
    }
    fclose(f);
    long udistinct = 0, udup = 0;
    char kmin[37] = "", kmax[37] = "";
    if (cap > 0 && un > 0) {
        qsort(U, (size_t)un, sizeof(u128), cmp128);
        for (long i = 0; i < un; i++) {
            if (i > 0 && U[i] == U[i - 1]) udup++; else udistinct++;
        }
        key_str(U[0], kmin);
        key_str(U[un - 1], kmax);
    }
    printf("{\"summary\":1,\"classes\":%ld,\"valid_classes\":%ld,\"sum_distinct\":%ld,\"union_capacity\":%ld,"
           "\"union_appended\":%ld,\"union_overflow\":%d,\"union_distinct\":%ld,\"union_adjacent_duplicates\":%ld,"
           "\"union_min_key\":\"%s\",\"union_max_key\":\"%s\",\"cpu_s\":%.2f}\n",
           nclass, nvalid, sumdistinct, cap, un, overflow, udistinct, udup, kmin, kmax,
           (double)clock() / CLOCKS_PER_SEC);
    free(buf);
    free(U);
    return 0;
}
