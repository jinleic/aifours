/* k6cls_a.c -- implementation A of the complete classification (representation R2 of the lane README) of optimal
 * (v,6,1) CPCW codes with s = 4 codewords, H = floor((v-1)/2) <= 64 coverable classes, leave c = H - 60 <= 2.
 *
 * Rows: every admissible 6-subset of Z_v (15 distinct classes, none = v/2), one per translation+negation class
 * (canonical = lexicographically least sorted translate containing 0 of B or -B); a row's class set is a 64-bit mask
 * (bit d-1 for class d).
 * Anchor modes (one codeword B1 is fixed per job; the other three are found by exhaustive exact cover):
 *   anchor1 (even v):  B1 = {0} u O, O a 5-subset of odd residues, B1 admissible, O lexicographically least among
 *                      {mO : m in Z_v^*} (sorted).  Valid when every code has exactly one type-1 codeword.
 *   general (any v):   leave class u fixed (argument), B1 ranges over all rows containing the least class of
 *                      R = {1..H} \ {u}; budget for further leave classes = c - 1.
 * Exhaustive part: DFS on the least uncovered class x of W (x is a leave class if budget allows, or x lies in a
 * row of the bucket of x that is contained in W); the last codeword is found by lookup of W minus every subset of
 * size = remaining budget.  Every (rows, leave) solution is reached by exactly one path.
 * No parity/type filter is applied to B2..B4 (types are checked afterwards).
 *
 * Usage: k6cls_a v mode param jobidx njobs outprefix
 *   mode=anchor1: param ignored (0); mode=general: param = leave class u (for c >= 1) or 0 (for c = 0).
 *   The anchors are numbered 0..N-1; this job handles indices i with i % njobs == jobidx.
 * Output: outprefix.sols (one line per solution: "anchor_idx | B1 | B2 | B3 | B4 | leave classes"),
 *         stdout progress (host-clock checkpoints every 600 s) and a final DONE line with counts.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

typedef uint64_t u64;
static int v, H, c;
static int cls[256];
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static int md(int x) { x %= v; return x < 0 ? x + v : x; }
static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }

/* ---- rows ---- */
static int nrows, rowcap;
static u64 *rmask;
static unsigned char (*relt)[6];
static void addrow(const int *b, u64 m) {
    if (nrows == rowcap) { rowcap = rowcap ? 2 * rowcap : 1 << 20; rmask = realloc(rmask, 8 * (size_t)rowcap); relt = realloc(relt, 6 * (size_t)rowcap); }
    rmask[nrows] = m;
    for (int i = 0; i < 6; i++) relt[nrows][i] = (unsigned char)b[i];
    nrows++;
}
static int is_canon(const int *b) {   /* b sorted, b[0] = 0 */
    int cand[6];
    for (int sg = 0; sg < 2; sg++) for (int t = 0; t < 6; t++) {
        if (sg == 0 && t == 0) continue;
        for (int i = 0; i < 6; i++) cand[i] = md((sg ? -b[i] : b[i]) - (sg ? -b[t] : b[t]));
        qsort(cand, 6, sizeof(int), cmpint);
        for (int i = 0; i < 6; i++) { if (cand[i] < b[i]) return 0; if (cand[i] > b[i]) break; }
    }
    return 1;
}
static int used[64 + 2];
static int cur[6];
static void gen(int depth, int lo, u64 m) {
    if (depth == 6) { if (is_canon(cur)) addrow(cur, m); return; }
    for (int x = lo; x < v; x++) {
        int i, nc[6];
        for (i = 0; i < depth; i++) {
            int d = cls[x - cur[i]];
            if (d <= 0 || used[d]) break;
            used[d] = 1; nc[i] = d;
        }
        if (i == depth) {
            u64 mm = m;
            for (int j = 0; j < depth; j++) mm |= 1ULL << (nc[j] - 1);
            cur[depth] = x;
            gen(depth + 1, x + 1, mm);
        }
        for (int j = 0; j < i; j++) used[nc[j]] = 0;
    }
}
static u64 set_mask(const int *b, int n, int *ok) {
    u64 m = 0; *ok = 1;
    for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) {
        int d = cls[md(b[i] - b[j])];
        if (d <= 0 || (m >> (d - 1) & 1)) { *ok = 0; return 0; }
        m |= 1ULL << (d - 1);
    }
    return m;
}

/* ---- per-anchor exact cover ---- */
static int *L1, nL1;              /* rows disjoint from the anchor */
static int *bstart, *bidx;        /* bucket CSR over classes 1..H: rows of L1 containing class d */
static int *sorted;               /* L1 sorted by mask for lookup */
static u64 Rmask;
static int chosen[4];
static long long nsol_anchor, nsol_total;
static FILE *fsol;
static int cur_anchor_idx;
static int anchor_elts[6];
static long long dfs_nodes;

static int cmpmask(const void *a, const void *b) {
    u64 x = rmask[*(const int *)a], y = rmask[*(const int *)b];
    return x < y ? -1 : x > y;
}
static void emit(int nb, u64 leavemask) {
    nsol_anchor++; nsol_total++;
    fprintf(fsol, "%d |", cur_anchor_idx);
    for (int i = 0; i < 6; i++) fprintf(fsol, " %d", anchor_elts[i]);
    for (int j = 0; j < nb; j++) { fprintf(fsol, " |"); for (int i = 0; i < 6; i++) fprintf(fsol, " %d", relt[chosen[j]][i]); }
    fprintf(fsol, " | L");
    for (int d = 1; d <= H; d++) if (leavemask >> (d - 1) & 1) fprintf(fsol, " %d", d);
    fprintf(fsol, "\n");
}
static u64 base_leave;
static void lookup_final(u64 W, u64 leave) {
    /* binary search for rows with mask == W */
    int lo = 0, hi = nL1;
    while (lo < hi) { int mid = (lo + hi) >> 1; if (rmask[sorted[mid]] < W) lo = mid + 1; else hi = mid; }
    for (int i = lo; i < nL1 && rmask[sorted[i]] == W; i++) { chosen[2] = sorted[i]; emit(3, leave); }
}
static void dfs(int nb, u64 cov, int budget, u64 leave) {
    dfs_nodes++;
    u64 W = Rmask & ~cov;
    if (nb == 2) {
        if (budget == 0) { lookup_final(W, leave); return; }
        /* remove every subset of size budget (budget <= 2) */
        for (u64 a = W; a; a &= a - 1) {
            u64 ba = a & -a;
            if (budget == 1) { lookup_final(W & ~ba, leave | ba); continue; }
            for (u64 b = a & (a - 1); b; b &= b - 1) { u64 bb = b & -b; lookup_final(W & ~ba & ~bb, leave | ba | bb); }
        }
        return;
    }
    int x = __builtin_ctzll(W) + 1;
    if (budget > 0) dfs(nb, cov | (1ULL << (x - 1)), budget - 1, leave | (1ULL << (x - 1)));
    for (int i = bstart[x]; i < bstart[x + 1]; i++) {
        int r = bidx[i];
        if (rmask[r] & ~W) continue;
        chosen[nb] = r;
        dfs(nb + 1, cov | rmask[r], budget, leave);
    }
}
static void solve_anchor(u64 amask, int budget, u64 leave0) {
    nL1 = 0;
    u64 forbidden = amask | leave0;
    for (int r = 0; r < nrows; r++) if (!(rmask[r] & forbidden)) L1[nL1++] = r;
    /* buckets */
    for (int d = 0; d <= H + 1; d++) bstart[d] = 0;
    for (int i = 0; i < nL1; i++) for (u64 m = rmask[L1[i]]; m; m &= m - 1) bstart[__builtin_ctzll(m) + 2]++;
    for (int d = 1; d <= H + 1; d++) bstart[d] += bstart[d - 1];
    static int *fill; if (!fill) fill = malloc(sizeof(int) * 70);
    for (int d = 0; d <= H + 1; d++) fill[d] = bstart[d];
    for (int i = 0; i < nL1; i++) for (u64 m = rmask[L1[i]]; m; m &= m - 1) { int d = __builtin_ctzll(m) + 1; bidx[fill[d]++] = L1[i]; }
    memcpy(sorted, L1, sizeof(int) * nL1);
    qsort(sorted, nL1, sizeof(int), cmpmask);
    nsol_anchor = 0;
    dfs(0, forbidden & Rmask, budget, leave0);
}

int main(int argc, char **argv) {
    if (argc != 7) { fprintf(stderr, "usage: k6cls_a v mode param jobidx njobs outprefix\n"); return 2; }
    v = atoi(argv[1]); const char *mode = argv[2]; int param = atoi(argv[3]);
    int jobidx = atoi(argv[4]), njobs = atoi(argv[5]); const char *pre = argv[6];
    H = (v - 1) / 2; c = H - 60;
    if (v > 255 || H > 64 || c < 0 || c > 2 || (v - 1) / 30 != 4) { fprintf(stderr, "unsupported v\n"); return 2; }
    for (int d = 0; d < v; d++) cls[d] = d == 0 ? 0 : (2 * d == v ? -1 : (d <= v - d ? d : v - d));
    Rmask = (H == 64) ? ~0ULL : ((1ULL << H) - 1);
    double t0 = now();
    time_t wall = time(0);
    char tbuf[64]; strftime(tbuf, sizeof tbuf, "%Y-%m-%d %H:%M:%S %Z", localtime(&wall));
    printf("start %s v=%d H=%d c=%d mode=%s param=%d job=%d/%d\n", tbuf, v, H, c, mode, param, jobidx, njobs);
    cur[0] = 0; memset(used, 0, sizeof used);
    gen(1, 1, 0);
    printf("rows=%d (translation+negation classes of admissible 6-sets) t=%.1f\n", nrows, now() - t0);
    fflush(stdout);
    L1 = malloc(sizeof(int) * nrows); sorted = malloc(sizeof(int) * nrows);
    bidx = malloc(sizeof(int) * (size_t)nrows * 15); bstart = malloc(sizeof(int) * 70);
    char path[1024]; snprintf(path, sizeof path, "%s.sols", pre);
    fsol = fopen(path, "w");
    if (!fsol) { perror(path); return 2; }
    long long nanchors = 0, done = 0;
    double lastck = now();
    if (!strcmp(mode, "anchor1")) {
        if (v % 2) { fprintf(stderr, "anchor1 needs even v\n"); return 2; }
        int units[256], nu = 0;
        for (int m = 1; m < v; m++) { int a = m, b = v; while (b) { int t = a % b; a = b; b = t; } if (a == 1) units[nu++] = m; }
        int odd[128], no = 0;
        for (int x = 1; x < v; x += 2) odd[no++] = x;
        int idx[5];
        for (idx[0] = 0; idx[0] < no; idx[0]++) for (idx[1] = idx[0] + 1; idx[1] < no; idx[1]++)
        for (idx[2] = idx[1] + 1; idx[2] < no; idx[2]++) for (idx[3] = idx[2] + 1; idx[3] < no; idx[3]++)
        for (idx[4] = idx[3] + 1; idx[4] < no; idx[4]++) {
            int B[6] = {0, odd[idx[0]], odd[idx[1]], odd[idx[2]], odd[idx[3]], odd[idx[4]]}, ok;
            u64 am = set_mask(B, 6, &ok);
            if (!ok) continue;
            int rep = 1;
            for (int u = 1; u < nu && rep; u++) {
                int mO[5];
                for (int i = 0; i < 5; i++) mO[i] = B[i + 1] * units[u] % v;
                qsort(mO, 5, sizeof(int), cmpint);
                for (int i = 0; i < 5; i++) { if (mO[i] < B[i + 1]) { rep = 0; break; } if (mO[i] > B[i + 1]) break; }
            }
            if (!rep) continue;
            long long ai = nanchors++;
            if (ai % njobs != jobidx) continue;
            cur_anchor_idx = (int)ai;
            memcpy(anchor_elts, B, sizeof B);
            solve_anchor(am, c, 0);
            done++;
            if (nsol_anchor) { printf("anchor %lld sols=%lld B1=%d %d %d %d %d %d\n", ai, nsol_anchor, B[0], B[1], B[2], B[3], B[4], B[5]); fflush(stdout); }
            if (now() - lastck > 600) {
                wall = time(0); strftime(tbuf, sizeof tbuf, "%Y-%m-%d %H:%M:%S %Z", localtime(&wall));
                printf("checkpoint %s anchors_seen=%lld done=%lld sols=%lld nodes=%lld t=%.0f\n", tbuf, nanchors, done, nsol_total, dfs_nodes, now() - t0);
                fflush(stdout); fflush(fsol); lastck = now();
            }
        }
    } else if (!strcmp(mode, "general")) {
        u64 leave0 = 0; int budget = c;
        if (c >= 1) { if (param < 1 || param > H) { fprintf(stderr, "general mode needs leave class u\n"); return 2; } leave0 = 1ULL << (param - 1); budget = c - 1; }
        if (budget != 0) { fprintf(stderr, "general mode is complete only for c <= 1\n"); return 2; }
        u64 R0 = Rmask & ~leave0;
        int x = __builtin_ctzll(R0) + 1;
        for (int r = 0; r < nrows; r++) {
            if (!(rmask[r] >> (x - 1) & 1) || (rmask[r] & leave0)) continue;
            long long ai = nanchors++;
            if (ai % njobs != jobidx) continue;
            cur_anchor_idx = (int)ai;
            for (int i = 0; i < 6; i++) anchor_elts[i] = relt[r][i];
            solve_anchor(rmask[r], budget, leave0);
            done++;
            if (nsol_anchor) { printf("anchor %lld sols=%lld\n", ai, nsol_anchor); fflush(stdout); }
            if (now() - lastck > 600) {
                wall = time(0); strftime(tbuf, sizeof tbuf, "%Y-%m-%d %H:%M:%S %Z", localtime(&wall));
                printf("checkpoint %s anchors_seen=%lld done=%lld sols=%lld nodes=%lld t=%.0f\n", tbuf, nanchors, done, nsol_total, dfs_nodes, now() - t0);
                fflush(stdout); fflush(fsol); lastck = now();
            }
        }
    } else if (!strncmp(mode, "given:", 6)) {
        /* targeted control: B1 given explicitly; all leaves allowed (budget c) */
        int B[6], nb = 0; const char *q = mode + 6;
        while (*q && nb < 6) { B[nb++] = atoi(q); while (*q && *q != ',') q++; if (*q == ',') q++; }
        int ok; u64 am = nb == 6 ? set_mask(B, 6, &ok) : 0;
        if (nb != 6 || !ok) { fprintf(stderr, "given anchor must be an admissible 6-set\n"); return 2; }
        nanchors = 1; cur_anchor_idx = 0; memcpy(anchor_elts, B, sizeof B);
        solve_anchor(am, c, 0);
        done = 1;
    } else { fprintf(stderr, "unknown mode\n"); return 2; }
    fclose(fsol);
    wall = time(0); strftime(tbuf, sizeof tbuf, "%Y-%m-%d %H:%M:%S %Z", localtime(&wall));
    printf("DONE %s v=%d mode=%s param=%d job=%d/%d anchors_total=%lld anchors_done=%lld solutions=%lld nodes=%lld seconds=%.1f\n",
           tbuf, v, mode, param, jobidx, njobs, nanchors, done, nsol_total, dfs_nodes, now() - t0);
    return 0;
}
