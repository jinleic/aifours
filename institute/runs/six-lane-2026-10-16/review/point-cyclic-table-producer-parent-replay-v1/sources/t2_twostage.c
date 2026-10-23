/* t2_twostage.c -- representation R1d of the point-cyclic-table200 lane README (Section 2.3, frozen before use).
 *
 * Two-stage search for the T2 type of GENERAL-REDUCTION.md at v = 4q (q odd, q = 1 mod 12): t = q, K = {1^C},
 * A = (q-1)/4 X blocks, C = (q-1)/12 Y blocks.  CRT coordinates x <-> (h, r) = (x mod 4, x mod q).
 * Difference classes {(d, e), (-d, -e)}, e != 0 (2(q-1) classes; differences with e = 0 lie in H = <q>).
 *   d = 0 : only X pairs can cover them (a Y block has one point per height);
 *   d = 2 : each Y block covers exactly 2 of the (q-1)/2 classes;
 *   d = 1,3: each Y block covers exactly 4 of the q-1 classes {(1,u),(3,-u)}.
 * Stage 1 (tabu, same state and moves as the X group of pc_tabu.c: residue partition by construction, heights mod 4):
 *   cost1 = sum_classes max(0, cntX - 1) + #{d = 0 classes not covered by X} + |#X pairs with d = 2 - ((q-1)/2 - 2C)|.
 *   cost1 = 0 <=> the X pairs are distinct, cover every d = 0 class, and leave exactly 2C classes with d = 2 and
 *   4C classes with d = 1,3 for the Y blocks.
 * Stage 2 (exact, complete for the given X): the uncovered classes define U (values u of uncovered classes (1,u))
 *   and W (uncovered d = 2 classes).  A Y block, normalized to residue 0 at height 0, is (0,b,c,d) at heights 0..3;
 *   it covers u-values b, c-b, d-c, -d and the d = 2 classes of c and d-b.  All such candidates inside U, W are
 *   enumerated and an exact cover of U u W by C candidates is searched by backtracking.
 * On success the full PC-SEED is written; otherwise stage 1 continues after a random perturbation.
 * Deterministic per seed (splitmix64); the wall clock only for the time limit.  Output files are created
 * exclusively; nothing is deleted.  Heuristic: misses are UNKNOWN.
 * Usage: t2_twostage q seed seconds outprefix [tl tr stall pert]
 * Exit 0 found, 3 time limit, 2 usage/internal error.
 */
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define MAXQ 64
#define MAXA (MAXQ / 4 + 1)
#define MAXC (MAXQ / 12 + 1)
#define MAXCAND 200000

static int q, A, C, HALF, NCLS, target2;
static int lab[MAXQ], ht[MAXQ], mem[MAXA][4], slot[MAXQ];
static int cnt[4 * MAXQ];
static int cost, n2;          /* n2 = number of X pairs with d = 2 */
static long long tabu_h[MAXQ][4], tabu_b[MAXQ][MAXA];
static uint64_t rng;

static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int rndint(int m) { return (int)(rnd() % (uint64_t)m); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }

/* class of the difference (h1,r1) - (h2,r2), r1 != r2: canonical (d, e) with e in 1..HALF; index d*HALF + e - 1 */
static inline int cls(int h1, int r1, int h2, int r2) {
    int d = (h1 - h2) & 3, e = r1 - r2;
    if (e < 0) e += q;
    if (e <= HALF) return d * HALF + e - 1;
    return ((4 - d) & 3) * HALF + (q - e) - 1;
}
static inline int cdel(int c) { return c / HALF; }
/* per-class cost: max(0, cnt-1) + [d = 0 and cnt = 0] */
static inline int fcls(int c, int k) { return (k > 1 ? k - 1 : 0) + ((cdel(c) == 0 && k == 0) ? 1 : 0); }
static inline int absv(int x) { return x < 0 ? -x : x; }

static int nrem, nadd, rem[32], add[32];
static int delta_lists(int apply) {
    /* cost change of removing rem[] and adding add[] (sequentially); counts restored unless apply */
    int d = 0, dn2 = 0;
    for (int k = 0; k < nrem; k++) { int c = rem[k]; d += fcls(c, cnt[c] - 1) - fcls(c, cnt[c]); cnt[c]--; if (cdel(c) == 2) dn2--; }
    for (int k = 0; k < nadd; k++) { int c = add[k]; d += fcls(c, cnt[c] + 1) - fcls(c, cnt[c]); cnt[c]++; if (cdel(c) == 2) dn2++; }
    d += absv(n2 + dn2 - target2) - absv(n2 - target2);
    if (!apply) {
        for (int k = 0; k < nadd; k++) cnt[add[k]]--;
        for (int k = 0; k < nrem; k++) cnt[rem[k]]++;
    } else {
        n2 += dn2;
    }
    return d;
}
static void full_recount(void) {
    memset(cnt, 0, sizeof cnt);
    n2 = 0;
    for (int b = 0; b < A; b++)
        for (int s = 0; s < 4; s++)
            for (int u = s + 1; u < 4; u++) {
                int r1 = mem[b][s], r2 = mem[b][u], c = cls(ht[r1], r1, ht[r2], r2);
                cnt[c]++;
                if (cdel(c) == 2) n2++;
            }
    cost = 0;
    for (int c = 0; c < NCLS; c++) cost += fcls(c, cnt[c]);
    cost += absv(n2 - target2);
}

enum { M1, M2, M3, M4 };
typedef struct { int type, a, b; } Move;   /* M1: residue a, new height b; M2..M4: residues a, b */

static void diff_block(const int *res, const int *oh, const int *nhres, const int *nh) {
    /* old block (res[s], oh[s]) -> new block (nhres[s], nh[s]); pairs touching a changed slot */
    for (int s = 0; s < 4; s++)
        for (int u = s + 1; u < 4; u++)
            if (res[s] != nhres[s] || oh[s] != nh[s] || res[u] != nhres[u] || oh[u] != nh[u]) {
                rem[nrem++] = cls(oh[u], res[u], oh[s], res[s]);
                add[nadd++] = cls(nh[u], nhres[u], nh[s], nhres[s]);
            }
}
static void build_lists(const Move *m) {
    int r0[4], h0[4], r1[4], h1[4], r2a[4], h2a[4], r2b[4], h2b[4];
    nrem = nadd = 0;
    if (m->type == M1 || m->type == M4) {
        int b = lab[m->a];
        for (int s = 0; s < 4; s++) { r0[s] = r1[s] = mem[b][s]; h0[s] = h1[s] = ht[mem[b][s]]; }
        if (m->type == M1) h1[slot[m->a]] = m->b;
        else { h1[slot[m->a]] = ht[m->b]; h1[slot[m->b]] = ht[m->a]; }
        diff_block(r0, h0, r1, h1);
    } else {
        int a = m->a, c = m->b, b1 = lab[a], b2 = lab[c];
        for (int s = 0; s < 4; s++) {
            r0[s] = r1[s] = mem[b1][s]; h0[s] = h1[s] = ht[mem[b1][s]];
            r2a[s] = r2b[s] = mem[b2][s]; h2a[s] = h2b[s] = ht[mem[b2][s]];
        }
        r1[slot[a]] = c; r2b[slot[c]] = a;
        if (m->type == M2) { h1[slot[a]] = ht[c]; h2b[slot[c]] = ht[a]; }   /* heights travel */
        /* M3: heights stay in the slots */
        diff_block(r0, h0, r1, h1);
        diff_block(r2a, h2a, r2b, h2b);
    }
}
static int is_tabu(const Move *m, long long it) {
    if (m->type == M1) return tabu_h[m->a][m->b] > it;
    if (m->type == M4) return tabu_h[m->a][ht[m->b]] > it || tabu_h[m->b][ht[m->a]] > it;
    return tabu_b[m->a][lab[m->b]] > it || tabu_b[m->b][lab[m->a]] > it;
}
static void commit(const Move *m, long long it, int tl, int tr) {
    build_lists(m);
    cost += delta_lists(1);
    long long until = it + tl + (tr > 0 ? rndint(tr) : 0);
    if (m->type == M1) { tabu_h[m->a][ht[m->a]] = until; ht[m->a] = m->b; }
    else if (m->type == M4) {
        tabu_h[m->a][ht[m->a]] = until; tabu_h[m->b][ht[m->b]] = until;
        int h = ht[m->a]; ht[m->a] = ht[m->b]; ht[m->b] = h;
    } else {
        int a = m->a, c = m->b, b1 = lab[a], b2 = lab[c], s1 = slot[a], s2 = slot[c];
        tabu_b[a][b1] = until; tabu_b[c][b2] = until;
        mem[b1][s1] = c; mem[b2][s2] = a;
        lab[a] = b2; slot[a] = s2; lab[c] = b1; slot[c] = s1;
        if (m->type == M3) { int h = ht[a]; ht[a] = ht[c]; ht[c] = h; }
    }
}
static void random_move(Move *m) {
    for (;;) {
        int a = 1 + rndint(q - 1), k = rndint(3);
        if (k == 0) { int h = rndint(4); if (h != ht[a]) { m->type = M1; m->a = a; m->b = h; return; } }
        else if (k == 1) { int c = 1 + rndint(q - 1); if (lab[c] != lab[a]) { m->type = rndint(2) ? M2 : M3; m->a = a; m->b = c; return; } }
        else { int c = mem[lab[a]][rndint(4)]; if (c != a && ht[c] != ht[a]) { m->type = M4; m->a = a; m->b = c; return; } }
    }
}

/* ---- stage 2 ---- */
static int inU[MAXQ], inW[MAXQ];   /* inU[u]: class (1,u) uncovered; inW[e]: class (2,+-e) uncovered (both signs set) */
static int ncand, cb[MAXCAND], cc[MAXCAND], cd[MAXCAND];
static int cu[MAXCAND][4], cw[MAXCAND][2];
static int usedU[MAXQ], usedW[MAXQ], pick[MAXC];
static int wcanon(int e) { return e <= HALF ? e : q - e; }
static int stage2_rec(int depth) {
    if (depth == C) return 1;
    /* choose the uncovered u with fewest candidates */
    int bestu = -1, bestn = 1 << 30;
    for (int u = 1; u < q; u++) {
        if (!inU[u] || usedU[u]) continue;
        int k = 0;
        for (int i = 0; i < ncand; i++) {
            int ok = 1;
            for (int z = 0; z < 4 && ok; z++) if (usedU[cu[i][z]]) ok = 0;
            for (int z = 0; z < 2 && ok; z++) if (usedW[cw[i][z]]) ok = 0;
            if (!ok) continue;
            if (cu[i][0] == u || cu[i][1] == u || cu[i][2] == u || cu[i][3] == u) k++;
        }
        if (k < bestn) { bestn = k; bestu = u; }
    }
    if (bestu < 0 || bestn == 0) return 0;
    for (int i = 0; i < ncand; i++) {
        int ok = 1, has = 0;
        for (int z = 0; z < 4 && ok; z++) { if (usedU[cu[i][z]]) ok = 0; if (cu[i][z] == bestu) has = 1; }
        for (int z = 0; z < 2 && ok; z++) if (usedW[cw[i][z]]) ok = 0;
        if (!ok || !has) continue;
        for (int z = 0; z < 4; z++) usedU[cu[i][z]] = 1;
        for (int z = 0; z < 2; z++) usedW[cw[i][z]] = 1;
        pick[depth] = i;
        if (stage2_rec(depth + 1)) return 1;
        for (int z = 0; z < 4; z++) usedU[cu[i][z]] = 0;
        for (int z = 0; z < 2; z++) usedW[cw[i][z]] = 0;
    }
    return 0;
}
static long long s2calls, s2cands;
static int stage2(void) {
    memset(inU, 0, sizeof inU); memset(inW, 0, sizeof inW);
    for (int e = 1; e <= HALF; e++) {
        if (cnt[1 * HALF + e - 1] == 0) inU[e] = 1;          /* class (1,e) = {(1,e),(3,-e)} -> u = e */
        if (cnt[3 * HALF + e - 1] == 0) inU[q - e] = 1;      /* class (3,e) = {(3,e),(1,-e)} -> u = -e */
        if (cnt[2 * HALF + e - 1] == 0) inW[e] = 1;
    }
    ncand = 0;
    for (int b = 1; b < q; b++) {
        if (!inU[b]) continue;
        for (int x = 1; x < q; x++) {                        /* x = c - b */
            if (!inU[x] || x == b) continue;
            int c = (b + x) % q;
            if (c == 0 || !inW[wcanon(c)]) continue;
            for (int y = 1; y < q; y++) {                    /* y = d - c */
                if (!inU[y] || y == b || y == x) continue;
                int d = (c + y) % q, md = (q - d) % q;
                if (d == 0 || !inU[md] || md == b || md == x || md == y) continue;
                int e2 = (d - b + q) % q;
                if (e2 == 0 || !inW[wcanon(e2)] || wcanon(e2) == wcanon(c)) continue;
                if (ncand >= MAXCAND) break;
                cb[ncand] = b; cc[ncand] = c; cd[ncand] = d;
                cu[ncand][0] = b; cu[ncand][1] = x; cu[ncand][2] = y; cu[ncand][3] = md;
                cw[ncand][0] = wcanon(c); cw[ncand][1] = wcanon(e2);
                ncand++;
            }
        }
    }
    s2calls++; s2cands += ncand;
    memset(usedU, 0, sizeof usedU); memset(usedW, 0, sizeof usedW);
    return stage2_rec(0);
}

static int crt(int h, int r) { for (int t = 0; t < 4; t++) { int x = r + t * q; if ((x & 3) == h) return x; } return -1; }
static int cmpint(const void *x, const void *y) { return *(const int *)x - *(const int *)y; }
static int cmp4(const void *x, const void *y) {
    const int *a = x, *b = y;
    for (int s = 0; s < 4; s++) if (a[s] != b[s]) return a[s] < b[s] ? -1 : 1;
    return 0;
}
static void write_seed(const char *path) {
    int X[MAXA][4], Y[MAXC][4];
    for (int b = 0; b < A; b++) {
        for (int s = 0; s < 4; s++) X[b][s] = crt(ht[mem[b][s]], mem[b][s]);
        qsort(X[b], 4, sizeof(int), cmpint);
    }
    qsort(X, A, sizeof X[0], cmp4);
    for (int j = 0; j < C; j++) {
        int i = pick[j];
        Y[j][0] = crt(0, 0); Y[j][1] = crt(1, cb[i]); Y[j][2] = crt(2, cc[i]); Y[j][3] = crt(3, cd[i]);
        qsort(Y[j], 4, sizeof(int), cmpint);
    }
    qsort(Y, C, sizeof Y[0], cmp4);
    int fd = open(path, O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) { perror(path); exit(2); }
    FILE *f = fdopen(fd, "w");
    fprintf(f, "PC-SEED %d\nSHORT %d\n", 4 * q, q);
    for (int b = 0; b < A; b++) fprintf(f, "X %d %d %d %d\n", X[b][0], X[b][1], X[b][2], X[b][3]);
    for (int j = 0; j < C; j++) fprintf(f, "GROUP 1\nY %d %d %d %d\n", Y[j][0], Y[j][1], Y[j][2], Y[j][3]);
    fclose(f);
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: t2_twostage q seed seconds outprefix [tl tr stall pert]\n"); return 2; }
    q = atoi(argv[1]);
    uint64_t seed = strtoull(argv[2], 0, 10);
    double secs = atof(argv[3]);
    const char *pre = argv[4];
    int tl = argc > 5 ? atoi(argv[5]) : 10, tr = argc > 6 ? atoi(argv[6]) : 10;
    int stall = argc > 7 ? atoi(argv[7]) : 5000, pert = argc > 8 ? atoi(argv[8]) : 4;
    if (q < 13 || q >= MAXQ || q % 2 == 0 || q % 12 != 1) { fprintf(stderr, "q must be odd, 1 mod 12, 13..63\n"); return 2; }
    A = (q - 1) / 4; C = (q - 1) / 12; HALF = (q - 1) / 2; NCLS = 4 * HALF; target2 = HALF - 2 * C;
    rng = seed * 0x2545F4914F6CDD1DULL + 4242;
    int perm[MAXQ];
    for (int i = 0; i < q - 1; i++) perm[i] = i + 1;
    for (int i = q - 2; i > 0; i--) { int k = rndint(i + 1), t = perm[i]; perm[i] = perm[k]; perm[k] = t; }
    for (int b = 0; b < A; b++)
        for (int s = 0; s < 4; s++) { int r = perm[4 * b + s]; mem[b][s] = r; lab[r] = b; slot[r] = s; ht[r] = rndint(4); }
    full_recount();
    printf("start q=%d v=%d A=%d C=%d classes=%d target2=%d seed=%llu cost1=%d tl=%d tr=%d stall=%d pert=%d\n",
           q, 4 * q, A, C, NCLS, target2, (unsigned long long)seed, cost, tl, tr, stall, pert);
    fflush(stdout);
    double t0 = now(), tlast = t0;
    long long it = 0, last_impr = 0, s1hits = 0;
    int dbest = cost, gbest = cost;
    Move cand, bestm;
    for (;;) {
        if (cost == 0) {
            int c0 = cost;
            full_recount();
            if (cost != 0 || c0 != 0) { fprintf(stderr, "internal: recount %d %d\n", c0, cost); return 2; }
            s1hits++;
            if (stage2()) {
                char path[1024];
                snprintf(path, sizeof path, "%s.seed", pre);
                write_seed(path);
                printf("FOUND it=%lld t=%.2f stage1_hits=%lld stage2_cands_avg=%.1f %s\n", it, now() - t0, s1hits,
                       (double)s2cands / s2calls, path);
                fflush(stdout);
                return 0;
            }
            for (int k = 0; k < pert; k++) { random_move(&cand); commit(&cand, it, tl, tr); }
            dbest = cost; last_impr = it;
        }
        it++;
        int bestd = 1 << 30, nties = 0;
        for (int a = 1; a < q; a++)
            for (int h = 0; h < 4; h++) {
                if (h == ht[a]) continue;
                cand.type = M1; cand.a = a; cand.b = h;
                build_lists(&cand);
                int d = delta_lists(0);
                if (is_tabu(&cand, it) && cost + d >= dbest) continue;
                if (d < bestd) { bestd = d; bestm = cand; nties = 1; }
                else if (d == bestd && rndint(++nties) == 0) bestm = cand;
            }
        for (int a = 1; a < q; a++)
            for (int c = a + 1; c < q; c++) {
                if (lab[a] == lab[c]) continue;
                for (int ty = M2; ty <= M3; ty++) {
                    if (ty == M3 && ht[a] == ht[c]) continue;
                    cand.type = ty; cand.a = a; cand.b = c;
                    build_lists(&cand);
                    int d = delta_lists(0);
                    if (is_tabu(&cand, it) && cost + d >= dbest) continue;
                    if (d < bestd) { bestd = d; bestm = cand; nties = 1; }
                    else if (d == bestd && rndint(++nties) == 0) bestm = cand;
                }
            }
        for (int b = 0; b < A; b++)
            for (int s = 0; s < 4; s++)
                for (int u = s + 1; u < 4; u++) {
                    int a = mem[b][s], c = mem[b][u];
                    if (ht[a] == ht[c]) continue;
                    cand.type = M4; cand.a = a; cand.b = c;
                    build_lists(&cand);
                    int d = delta_lists(0);
                    if (is_tabu(&cand, it) && cost + d >= dbest) continue;
                    if (d < bestd) { bestd = d; bestm = cand; nties = 1; }
                    else if (d == bestd && rndint(++nties) == 0) bestm = cand;
                }
        if (nties == 0) random_move(&bestm);
        commit(&bestm, it, tl, tr);
        if (cost < dbest) { dbest = cost; last_impr = it; }
        if (cost < gbest) gbest = cost;
        if (it - last_impr > stall) {
            for (int k = 0; k < pert; k++) { random_move(&cand); commit(&cand, it, tl, tr); }
            dbest = cost; last_impr = it;
        }
        if ((it & 255) == 0) {
            double tn = now();
            if (tn - t0 > secs) {
                printf("TIMEOUT it=%lld t=%.1f gbest1=%d stage1_hits=%lld stage2_cands_avg=%.1f\n", it, tn - t0, gbest,
                       s1hits, s2calls ? (double)s2cands / s2calls : 0.0);
                return 3;
            }
            if (tn - tlast > 60) {
                printf("progress it=%lld t=%.0f cost1=%d gbest1=%d stage1_hits=%lld it/s=%.0f\n", it, tn - t0, cost, gbest,
                       s1hits, it / (tn - t0));
                fflush(stdout);
                tlast = tn;
            }
        }
    }
}
