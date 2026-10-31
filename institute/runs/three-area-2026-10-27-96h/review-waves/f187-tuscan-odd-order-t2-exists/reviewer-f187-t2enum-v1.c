/* reviewer-f187-t2enum-v1.c
 *
 * Reviewer-authored (ReviewF187TuscanOdd21) exhaustive enumerator of NORMALIZED
 * linear Tuscan-2 squares of order n: n x n arrays whose rows are permutations
 * of 0..n-1 and in which every ordered pair occurs at most once at distance 1
 * and at most once at distance 2 (no wrap-around).
 *
 * Normalization: row 0 = (0,1,...,n-1) and row r starts with symbol r.  In any
 * T2(n) the first column is a permutation (distance-1 exactness), so every
 * T2(n) is equivalent under a symbol relabelling plus a row reordering to a
 * normalized one; every profile field computed below is invariant under those
 * operations (E is conjugated, column/pair-set equalities are relabelled, all
 * row signs flip together).
 *
 * Implied pruning only: each symbol is last in exactly one row (distance-1
 * exactness), so a symbol already used in the last column is excluded there.
 *
 * Usage: reviewer-f187-t2enum-v1 n time_cap_seconds max_print
 * Output: SOL lines (first max_print solutions, row-major, with profile key),
 *         PROFILE lines (count per profile key), SUMMARY line.
 *         CAPPED=1 means the enumeration is INCOMPLETE (counts are lower bounds).
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAXN 12
#define MAXP 2048

static int n, maxprint;
static int g[MAXN][MAXN];
static unsigned used1[MAXN], used2[MAXN], rowused[MAXN], lastused, full;
static long long nodes, sols, printed;
static double tcap;
static struct timespec t0;
static int capped;
static char pkey[MAXP][192];
static long long pcnt[MAXP];
static int np, poverflow;

static double elapsed(void) {
    struct timespec t;
    clock_gettime(CLOCK_MONOTONIC, &t);
    return (double)(t.tv_sec - t0.tv_sec) + 1e-9 * (double)(t.tv_nsec - t0.tv_nsec);
}

static int col_is_perm(int c) {
    unsigned m = 0;
    for (int r = 0; r < n; r++) m |= 1u << g[r][c];
    return m == full;
}

static int row_sign(int r) {
    int seen[MAXN] = {0}, s = 1;
    for (int i = 0; i < n; i++) {
        if (seen[i]) continue;
        int j = i, len = 0;
        while (!seen[j]) { seen[j] = 1; j = g[r][j]; len++; }
        if (len % 2 == 0) s = -s;
    }
    return s;
}

static void profile_key(char *key) {
    int E[MAXN], seen[MAXN] = {0}, cyc[MAXN], nc = 0;
    for (int r = 0; r < n; r++) E[g[r][0]] = g[r][n - 1];
    for (int a = 0; a < n; a++) {
        if (seen[a]) continue;
        int b = a, len = 0;
        while (!seen[b]) { seen[b] = 1; b = E[b]; len++; }
        cyc[nc++] = len;
    }
    for (int i = 0; i < nc; i++)
        for (int j = i + 1; j < nc; j++)
            if (cyc[j] > cyc[i]) { int t = cyc[i]; cyc[i] = cyc[j]; cyc[j] = t; }
    int e2 = 1, fixed = 0;
    for (int a = 0; a < n; a++) { if (E[E[a]] != a) e2 = 0; if (E[a] == a) fixed++; }
    int latin = 1;
    for (int c = 0; c < n; c++) if (!col_is_perm(c)) latin = 0;
    int sc = col_is_perm(1), pc = col_is_perm(n - 2);
    unsigned d2[MAXN] = {0}, cm_[MAXN] = {0}, rm_[MAXN] = {0}, mm[MAXN];
    for (int r = 0; r < n; r++)
        for (int i = 0; i + 2 < n; i++) d2[g[r][i]] |= 1u << g[r][i + 2];
    for (int a = 0; a < n; a++) mm[a] = full & ~(1u << a) & ~d2[a];
    for (int r = 0; r < n; r++) {
        cm_[g[r][n - 1]] |= 1u << g[r][0];
        rm_[g[r][n - 2]] |= 1u << g[r][1];
    }
    int ceqm = 1, meqr = 1;
    for (int a = 0; a < n; a++) {
        if (cm_[a] != mm[a]) ceqm = 0;
        if (rm_[a] != mm[a]) meqr = 0;
    }
    int plus = 0;
    for (int r = 0; r < n; r++) if (row_sign(r) > 0) plus++;
    int s1 = plus, s2 = n - plus;
    if (s2 > s1) { int t = s1; s1 = s2; s2 = t; }
    char cs[64] = "";
    for (int i = 0; i < nc; i++) {
        char b[12];
        snprintf(b, sizeof b, i ? ",%d" : "%d", cyc[i]);
        strncat(cs, b, sizeof cs - strlen(cs) - 1);
    }
    char sg[24];
    if (s2) snprintf(sg, sizeof sg, "%d,%d", s1, s2); else snprintf(sg, sizeof sg, "%d", s1);
    snprintf(key, 192, "E=%s|Efixed=%d|E2id=%d|latin=%d|secondperm=%d|penultperm=%d|CeqM=%d|MeqR=%d|signclasses=%s",
             cs, fixed, e2, latin, sc, pc, ceqm, meqr, sg);
}

static void record(void) {
    char key[192];
    profile_key(key);
    int i;
    for (i = 0; i < np; i++) if (strcmp(pkey[i], key) == 0) break;
    if (i == np) {
        if (np == MAXP) { poverflow = 1; return; }
        strcpy(pkey[np], key);
        pcnt[np++] = 0;
    }
    pcnt[i]++;
    if (printed < maxprint) {
        printed++;
        printf("SOL ");
        for (int r = 0; r < n; r++)
            for (int c = 0; c < n; c++) printf(c || r ? ",%d" : "%d", g[r][c]);
        printf(" %s\n", key);
    }
}

static void dfs(int r, int c) {
    if (c == n) {
        if (r == n - 1) { sols++; record(); return; }
        dfs(r + 1, 1);
        return;
    }
    if ((++nodes & 0xFFFFF) == 0 && elapsed() > tcap) capped = 1;
    if (capped) return;
    int prev = g[r][c - 1], prev2 = c >= 2 ? g[r][c - 2] : -1;
    unsigned cand = full & ~rowused[r] & ~used1[prev];
    if (prev2 >= 0) cand &= ~used2[prev2];
    if (c == n - 1) cand &= ~lastused;
    while (cand) {
        int s = __builtin_ctz(cand);
        unsigned bit = 1u << s;
        cand &= cand - 1;
        g[r][c] = s;
        rowused[r] |= bit; used1[prev] |= bit;
        if (prev2 >= 0) used2[prev2] |= bit;
        if (c == n - 1) lastused |= bit;
        dfs(r, c + 1);
        rowused[r] &= ~bit; used1[prev] &= ~bit;
        if (prev2 >= 0) used2[prev2] &= ~bit;
        if (c == n - 1) lastused &= ~bit;
        if (capped) return;
    }
}

int main(int argc, char **argv) {
    if (argc != 4) { fprintf(stderr, "usage: %s n time_cap_seconds max_print\n", argv[0]); return 2; }
    n = atoi(argv[1]); tcap = atof(argv[2]); maxprint = atoi(argv[3]);
    if (n < 3 || n > MAXN) { fprintf(stderr, "n out of range\n"); return 2; }
    full = (1u << n) - 1;
    memset(used1, 0, sizeof used1); memset(used2, 0, sizeof used2); memset(rowused, 0, sizeof rowused);
    for (int c = 0; c < n; c++) g[0][c] = c;
    rowused[0] = full;
    for (int i = 0; i + 1 < n; i++) used1[i] |= 1u << (i + 1);
    for (int i = 0; i + 2 < n; i++) used2[i] |= 1u << (i + 2);
    lastused = 1u << (n - 1);
    for (int r = 1; r < n; r++) { g[r][0] = r; rowused[r] = 1u << r; }
    clock_gettime(CLOCK_MONOTONIC, &t0);
    dfs(1, 1);
    for (int i = 0; i < np; i++) printf("PROFILE %lld %s\n", pcnt[i], pkey[i]);
    printf("SUMMARY n=%d normalized_T2_solutions=%lld nodes=%lld capped=%d profile_overflow=%d elapsed=%.3f\n",
           n, sols, nodes, capped, poverflow, elapsed());
    return capped ? 3 : 0;
}
