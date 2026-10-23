/* enum_nsets.c -- parent-written independent enumerator for the LOWER46 binding check (item 5).
 *
 * Enumerates ALL sets N contained in V_0 x V_1 x V_2 x V_3 that satisfy the N-only predicate P:
 *   (C1) every line of every coordinate pair {i,j} meets N in 0 or >= 2 points;
 *   (C2) for each ordered pair (i,j), i != j, and each a in V_i, exactly d_{i,a} values b in V_j have the
 *        {i,j}-line (x_i, x_j) = (a, b) meeting N;
 *   (C3) |N| = 2h + e, where h = sum_a d_{i,a} (the same for every i);
 *   (C4) in each reshaping 01|23, 02|13, 03|12 and in both orientations, two distinct rows never share exactly
 *        one column (combinatorial orthogonality).
 * Normal form (LOWER46 section 3, step 1): V_i = {6-|V_i|, ..., 5}; the parts of coordinate i are assigned in the
 * order given on the command line to increasing values (the engine order is non-increasing; any order is accepted
 * so that relabelled specifications can be used as consistency controls).
 *
 * Search: depth first over the cells z = (a, b) of V_0 x V_1 in row-major order. Cell z receives the set
 * S_z of (x_2, x_3) values with (a, b, x_2, x_3) in N. By (C1) S_z is empty or has >= 2 elements; by (C2) for the
 * ordered pairs (0,1) and (1,0) row a has exactly d_{0,a} non-empty cells and column b exactly d_{1,b}; hence there
 * are h non-empty cells and, by (C3), sum over non-empty cells of (|S_z| - 2) = e exactly.
 * Interior pruning uses only consequences of C1-C4 that already hold for every subset of a solution:
 *   - row/column counts of non-empty cells never exceed d, and must remain reachable;
 *   - the number of distinct partner values per (ordered pair, value) never exceeds d (it only grows);
 *   - C4 between rows of 01|23 (a row of 01|23 is a cell; it is final once chosen);
 *   - when row a of V_0 x V_1 is finished, every line through x_0 = a of the pairs (0,2) and (0,3) and every row
 *     (a, x_2) of 02|13 and (a, x_3) of 03|12 is final, so C1, C2 (ordered pairs (0,2), (0,3)) and C4 for these
 *     rows against all earlier final rows are checked exactly.
 * Every leaf is then re-checked by full_check(), an independent from-scratch evaluation of C1-C4 on the point list.
 * Only leaves passing full_check() are written. Discrepancies between the incremental leaf test and full_check()
 * are counted and reported (both must be 0 for a clean run).
 *
 * Usage: enum_nsets P0 P1 P2 P3 E OUTFILE [flags]
 *   Pi = parts of coordinate i joined by '-', e.g. 3-3-2. OUTFILE is created exclusively (never overwritten).
 *   Flags (controls only; the binding run uses none):
 *     --no-orth          drop C4 everywhere, including full_check (semantic ablation);
 *     --no-orth-prune    keep C4 in full_check but skip the incremental C4 pruning;
 *     --no-close-prune   skip the exact C1/C2 checks when a row of V_0 x V_1 is finished;
 *     --no-dist-prune    skip the distinct-partner upper bounds;
 *     --max-nodes=K      stop after K search nodes and report "complete": false (UNKNOWN).
 * Output: one solution per line, its points as 4-digit strings in increasing order; statistics as one JSON line on
 * stdout.
 */
#include <errno.h>
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define MAXV 6

static int m[4], lo[4], dd[4][MAXV], h, ex, n;
static int no_orth = 0, no_orth_prune = 0, no_close_prune = 0, no_dist_prune = 0, truncated = 0;
static unsigned long long max_nodes = 0;
static int Q;
static uint64_t *cand;
static int *candsz;
static int ncand, capcand;

static int nonempty = 0, used = 0;
static uint64_t S[MAXV * MAXV];
static int rowcnt[MAXV], colcnt[MAXV];
static int c02[MAXV][MAXV], c03[MAXV][MAXV], c12[MAXV][MAXV], c13[MAXV][MAXV], c23[MAXV][MAXV];
static int n02[MAXV], n20[MAXV], n03[MAXV], n30[MAXV], n12[MAXV], n21[MAXV], n13[MAXV], n31[MAXV], n23[MAXV],
    n32[MAXV];
static uint64_t R02[MAXV][MAXV], R03[MAXV][MAXV];
static unsigned long long nodes = 0, leaves = 0, sols = 0, cheap_rej_full_acc = 0, cheap_acc_full_rej = 0;
static FILE *out;

static void die(const char *msg) {
    fprintf(stderr, "enum_nsets: %s\n", msg);
    exit(2);
}

static int popc(uint64_t x) { return __builtin_popcountll(x); }

static void push_cand(uint64_t mask, int size) {
    if (ncand == capcand) {
        capcand = capcand ? 2 * capcand : 1024;
        cand = realloc(cand, sizeof(uint64_t) * capcand);
        candsz = realloc(candsz, sizeof(int) * capcand);
        if (!cand || !candsz) die("out of memory");
    }
    cand[ncand] = mask;
    candsz[ncand] = size;
    ncand++;
}

static void gen_comb(int start, int left, uint64_t mask, int size) {
    if (left == 0) {
        push_cand(mask, size);
        return;
    }
    for (int q = start; q <= Q - left; q++) gen_comb(q + 1, left - 1, mask | (1ULL << q), size);
}

/* add one point (a,b,c,f) (local indices); returns 0 if a distinct-count bound is exceeded */
static int add_point(int a, int b, int c, int f) {
    int ok = 1;
    if (c02[a][c]++ == 0) {
        n02[a]++;
        n20[c]++;
        if (n02[a] > dd[0][a] || n20[c] > dd[2][c]) ok = 0;
    }
    if (c03[a][f]++ == 0) {
        n03[a]++;
        n30[f]++;
        if (n03[a] > dd[0][a] || n30[f] > dd[3][f]) ok = 0;
    }
    if (c12[b][c]++ == 0) {
        n12[b]++;
        n21[c]++;
        if (n12[b] > dd[1][b] || n21[c] > dd[2][c]) ok = 0;
    }
    if (c13[b][f]++ == 0) {
        n13[b]++;
        n31[f]++;
        if (n13[b] > dd[1][b] || n31[f] > dd[3][f]) ok = 0;
    }
    if (c23[c][f]++ == 0) {
        n23[c]++;
        n32[f]++;
        if (n23[c] > dd[2][c] || n32[f] > dd[3][f]) ok = 0;
    }
    return no_dist_prune ? 1 : ok;
}

static void remove_point(int a, int b, int c, int f) {
    if (--c02[a][c] == 0) {
        n02[a]--;
        n20[c]--;
    }
    if (--c03[a][f] == 0) {
        n03[a]--;
        n30[f]--;
    }
    if (--c12[b][c] == 0) {
        n12[b]--;
        n21[c]--;
    }
    if (--c13[b][f] == 0) {
        n13[b]--;
        n31[f]--;
    }
    if (--c23[c][f] == 0) {
        n23[c]--;
        n32[f]--;
    }
}

/* exact checks once row a of V_0 x V_1 is complete */
static int close_row(int a) {
    if (rowcnt[a] != dd[0][a]) return 0;
    if (!no_close_prune) {
        for (int c = 0; c < m[2]; c++)
            if (c02[a][c] == 1) return 0;
        if (n02[a] != dd[0][a]) return 0;
        for (int f = 0; f < m[3]; f++)
            if (c03[a][f] == 1) return 0;
        if (n03[a] != dd[0][a]) return 0;
    }
    if (no_orth || no_orth_prune) return 1;
    for (int c = 0; c < m[2]; c++) R02[a][c] = 0;
    for (int f = 0; f < m[3]; f++) R03[a][f] = 0;
    for (int b = 0; b < m[1]; b++) {
        uint64_t M = S[a * m[1] + b];
        while (M) {
            int q = __builtin_ctzll(M);
            M &= M - 1;
            int c = q / m[3], f = q % m[3];
            R02[a][c] |= 1ULL << (b * m[3] + f);
            R03[a][f] |= 1ULL << (b * m[2] + c);
        }
    }
    for (int c = 0; c < m[2]; c++) {
        if (!R02[a][c]) continue;
        for (int a2 = 0; a2 <= a; a2++)
            for (int c2 = 0; c2 < m[2]; c2++) {
                if (a2 == a && c2 >= c) continue;
                if (popc(R02[a][c] & R02[a2][c2]) == 1) return 0;
            }
    }
    for (int f = 0; f < m[3]; f++) {
        if (!R03[a][f]) continue;
        for (int a2 = 0; a2 <= a; a2++)
            for (int f2 = 0; f2 < m[3]; f2++) {
                if (a2 == a && f2 >= f) continue;
                if (popc(R03[a][f] & R03[a2][f2]) == 1) return 0;
            }
    }
    return 1;
}

/* independent from-scratch evaluation of C1-C4 on actual coordinate values */
static int full_check(int (*p)[4], int np) {
    static const int pairs[6][2] = {{0, 1}, {0, 2}, {0, 3}, {1, 2}, {1, 3}, {2, 3}};
    static const int pairings[3][4] = {{0, 1, 2, 3}, {0, 2, 1, 3}, {0, 3, 1, 2}};
    unsigned char seen[1296];
    if (np != n) return 0;
    memset(seen, 0, sizeof seen);
    for (int k = 0; k < np; k++) {
        for (int i = 0; i < 4; i++)
            if (p[k][i] < lo[i] || p[k][i] > 5) return 0;
        int key = ((p[k][0] * 6 + p[k][1]) * 6 + p[k][2]) * 6 + p[k][3];
        if (seen[key]) return 0;
        seen[key] = 1;
    }
    for (int t = 0; t < 6; t++) {
        int i = pairs[t][0], j = pairs[t][1];
        int cnt[6][6];
        memset(cnt, 0, sizeof cnt);
        for (int k = 0; k < np; k++) cnt[p[k][i]][p[k][j]]++;
        for (int u = 0; u < 6; u++)
            for (int v = 0; v < 6; v++)
                if (cnt[u][v] == 1) return 0;
        for (int u = 0; u < 6; u++) {
            int dist = 0;
            for (int v = 0; v < 6; v++) dist += cnt[u][v] > 0;
            int req = u >= lo[i] ? dd[i][u - lo[i]] : 0;
            if (dist != req) return 0;
        }
        for (int v = 0; v < 6; v++) {
            int dist = 0;
            for (int u = 0; u < 6; u++) dist += cnt[u][v] > 0;
            int req = v >= lo[j] ? dd[j][v - lo[j]] : 0;
            if (dist != req) return 0;
        }
    }
    if (no_orth) return 1;
    for (int t = 0; t < 3; t++)
        for (int orient = 0; orient < 2; orient++) {
            int A0 = pairings[t][orient ? 2 : 0], A1 = pairings[t][orient ? 3 : 1];
            int B0 = pairings[t][orient ? 0 : 2], B1 = pairings[t][orient ? 1 : 3];
            uint64_t sup[36];
            memset(sup, 0, sizeof sup);
            for (int k = 0; k < np; k++) sup[p[k][A0] * 6 + p[k][A1]] |= 1ULL << (p[k][B0] * 6 + p[k][B1]);
            for (int r1 = 0; r1 < 36; r1++)
                for (int r2 = r1 + 1; r2 < 36; r2++)
                    if (sup[r1] && sup[r2] && popc(sup[r1] & sup[r2]) == 1) return 0;
        }
    return 1;
}

static int cmp_pt(const void *x, const void *y) {
    const int *p = x, *q = y;
    for (int i = 0; i < 4; i++)
        if (p[i] != q[i]) return p[i] - q[i];
    return 0;
}

static void leaf(void) {
    leaves++;
    int cheap = 1;
    if (nonempty != h || used != ex) cheap = 0;
    for (int b = 0; b < m[1]; b++) {
        if (colcnt[b] != dd[1][b]) cheap = 0;
        if (n12[b] != dd[1][b] || n13[b] != dd[1][b]) cheap = 0;
        for (int c = 0; c < m[2]; c++)
            if (c12[b][c] == 1) cheap = 0;
        for (int f = 0; f < m[3]; f++)
            if (c13[b][f] == 1) cheap = 0;
    }
    for (int c = 0; c < m[2]; c++) {
        if (n20[c] != dd[2][c] || n21[c] != dd[2][c] || n23[c] != dd[2][c]) cheap = 0;
        for (int f = 0; f < m[3]; f++)
            if (c23[c][f] == 1) cheap = 0;
    }
    for (int f = 0; f < m[3]; f++)
        if (n30[f] != dd[3][f] || n31[f] != dd[3][f] || n32[f] != dd[3][f]) cheap = 0;
    int pts[1296][4];
    int np = 0;
    for (int z = 0; z < m[0] * m[1]; z++) {
        uint64_t M = S[z];
        while (M) {
            int q = __builtin_ctzll(M);
            M &= M - 1;
            if (np >= 1296) die("too many points");
            pts[np][0] = lo[0] + z / m[1];
            pts[np][1] = lo[1] + z % m[1];
            pts[np][2] = lo[2] + q / m[3];
            pts[np][3] = lo[3] + q % m[3];
            np++;
        }
    }
    int full = full_check(pts, np);
    if (cheap && !full) cheap_acc_full_rej++;
    if (!cheap && full) cheap_rej_full_acc++;
    if (!full) return;
    qsort(pts, np, sizeof pts[0], cmp_pt);
    for (int k = 0; k < np; k++)
        fprintf(out, "%s%d%d%d%d", k ? " " : "", pts[k][0], pts[k][1], pts[k][2], pts[k][3]);
    fputc('\n', out);
    sols++;
}

static void dfs(int z) {
    if (truncated) return;
    if (max_nodes && nodes >= max_nodes) {
        truncated = 1;
        return;
    }
    nodes++;
    if (z == m[0] * m[1]) {
        leaf();
        return;
    }
    int a = z / m[1], b = z % m[1];
    int last_in_row = (b == m[1] - 1);
    int rem_in_row = m[1] - 1 - b;
    int rows_after = m[0] - 1 - a;
    /* empty cell */
    if (rowcnt[a] + rem_in_row >= dd[0][a] && colcnt[b] + rows_after >= dd[1][b]) {
        S[z] = 0;
        if (!last_in_row || close_row(a)) dfs(z + 1);
    }
    /* non-empty cell */
    if (rowcnt[a] < dd[0][a] && colcnt[b] < dd[1][b] && nonempty < h) {
        int erem = ex - used;
        for (int k = 0; k < ncand; k++) {
            int s = candsz[k];
            if (s - 2 > erem) break; /* candidates are sorted by size */
            uint64_t M = cand[k];
            if (!no_orth && !no_orth_prune) {
                int bad = 0;
                for (int z2 = 0; z2 < z; z2++)
                    if (S[z2] && popc(M & S[z2]) == 1) {
                        bad = 1;
                        break;
                    }
                if (bad) continue;
            }
            int ok = 1;
            uint64_t T = M;
            while (T) {
                int q = __builtin_ctzll(T);
                T &= T - 1;
                if (!add_point(a, b, q / m[3], q % m[3])) ok = 0;
            }
            if (ok) {
                S[z] = M;
                rowcnt[a]++;
                colcnt[b]++;
                nonempty++;
                used += s - 2;
                if (!last_in_row || close_row(a)) dfs(z + 1);
                rowcnt[a]--;
                colcnt[b]--;
                nonempty--;
                used -= s - 2;
                S[z] = 0;
            }
            T = M;
            while (T) {
                int q = __builtin_ctzll(T);
                T &= T - 1;
                remove_point(a, b, q / m[3], q % m[3]);
            }
        }
    }
}

static void parse_parts(const char *s, int i) {
    int k = 0, sum = 0;
    const char *p = s;
    while (*p) {
        char *end;
        long v = strtol(p, &end, 10);
        if (end == p || v < 1 || v > 6) die("bad part");
        if (k >= MAXV) die("too many parts");
        dd[i][k++] = (int)v;
        sum += (int)v;
        if (*end == '-')
            p = end + 1;
        else if (*end == 0)
            p = end;
        else
            die("bad separator");
    }
    if (k == 0) die("empty partition");
    m[i] = k;
    lo[i] = 6 - k;
    if (i == 0)
        h = sum;
    else if (sum != h)
        die("partitions have different sums");
}

int main(int argc, char **argv) {
    if (argc < 7) die("usage: enum_nsets P0 P1 P2 P3 E OUTFILE [flags]");
    for (int i = 0; i < 4; i++) parse_parts(argv[1 + i], i);
    char *end;
    long e = strtol(argv[5], &end, 10);
    if (*end || e < 0 || e > 64) die("bad e");
    ex = (int)e;
    n = 2 * h + ex;
    for (int k = 7; k < argc; k++) {
        if (!strcmp(argv[k], "--no-orth"))
            no_orth = 1;
        else if (!strcmp(argv[k], "--no-orth-prune"))
            no_orth_prune = 1;
        else if (!strcmp(argv[k], "--no-close-prune"))
            no_close_prune = 1;
        else if (!strcmp(argv[k], "--no-dist-prune"))
            no_dist_prune = 1;
        else if (!strncmp(argv[k], "--max-nodes=", 12)) {
            max_nodes = strtoull(argv[k] + 12, &end, 10);
            if (*end || max_nodes == 0) die("bad --max-nodes");
        } else
            die("unknown flag");
    }
    Q = m[2] * m[3];
    for (int s = 2; s <= 2 + ex && s <= Q; s++) gen_comb(0, s, 0, s);
    int fd = open(argv[6], O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) die(errno == EEXIST ? "output exists" : "cannot create output");
    out = fdopen(fd, "w");
    if (!out) die("fdopen");
    clock_t t0 = clock();
    dfs(0);
    double cpu = (double)(clock() - t0) / CLOCKS_PER_SEC;
    if (fclose(out)) die("close");
    printf("{\"parts\": [\"%s\", \"%s\", \"%s\", \"%s\"], \"e\": %d, \"h\": %d, \"n\": %d, \"no_orth\": %s, "
           "\"no_orth_prune\": %s, \"no_close_prune\": %s, \"no_dist_prune\": %s, \"max_nodes\": %llu, "
           "\"complete\": %s, \"candidates_per_cell\": %d, \"nodes\": %llu, \"leaves\": %llu, \"solutions\": %llu, "
           "\"leaf_cheap_reject_full_accept\": %llu, \"leaf_cheap_accept_full_reject\": %llu, \"cpu_s\": %.3f}\n",
           argv[1], argv[2], argv[3], argv[4], ex, h, n, no_orth ? "true" : "false",
           no_orth_prune ? "true" : "false", no_close_prune ? "true" : "false", no_dist_prune ? "true" : "false",
           max_nodes, truncated ? "false" : "true", ncand, nodes, leaves, sols, cheap_rej_full_acc,
           cheap_acc_full_rej, cpu);
    return 0;
}
