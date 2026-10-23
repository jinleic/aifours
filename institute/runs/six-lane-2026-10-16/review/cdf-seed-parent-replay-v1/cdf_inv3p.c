/* cdf_inv3p.c -- cyclic (3p,5,1) difference families with the class multiplier mu = (1 mod 3, -1 mod p) and every
 * base block mu-stable (structure derived in evidence/multipliers.md; exists numerically for p = 47, 127, 167).
 *
 * Coordinates Z_{3p} = Z_3 x Z_p.  Classes of Z_p: C = Z_p^* / {+-1}, size P2 = (p-1)/2.
 * Block types (a1 = (P2-3)/4 of type T1, a5 = (P2-3-2*a1)/10 of type T5, one of type T3):
 *   T1(y1,y2)    = {(0,0),(1,y1),(1,-y1),(2,y2),(2,-y2)}: orbit classes {y1,y2,y1+y2,y1-y2}, pure classes {2y1,2y2}
 *   T3(f1,f2,y)  = {(0,0),(0,f1),(0,f2),(1,y),(2,y)}:     orbit classes {y,y-f1,y-f2}, pure {f1,f2,f2-f1}, + (1,0)
 *   T5(Q)        = {0} x Q, Q a 5-subset of Z_p:            pure classes Delta(Q)
 * Exact conditions: the orbit classes of all T1 and T3 partition C, and the pure classes of all blocks partition C.
 * (Orbit class y stands for the two Z_{3p} classes [(1,y)], [(1,-y)]; pure class y for [(0,y)].)
 * Search: random T3; randomized exact cover of C minus T3's orbit classes by T1 quadruples (bitset Algorithm X),
 * restricted to T1 whose pure classes avoid T3's; for each cover, exact cover of the remaining pure classes by
 * a5 quintuples (enumerated, canonical up to translation and negation).  The final family is verified by
 * expanding to Z_{3p} and checking the difference multiset in-program; the certificate is re-verified externally.
 *
 * Usage: cdf_inv3p v seed seconds outprefix [covers_per_t3] [nodelimit_A]
 * Exit 0 found (outprefix.sol), 3 time limit.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define W 2
typedef struct { uint64_t m[W]; } mask_t;
static int v, p, P2, a1, a5;
static int *cls;
static uint64_t rng;
static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int rndint(int m) { return (int)(rnd() % (uint64_t)m); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static inline int mp(int a) { a %= p; return a < 0 ? a + p : a; }
static inline void setbit(mask_t *m, int c) { m->m[c >> 6] |= 1ULL << (c & 63); }
static inline int getbit(const mask_t *m, int c) { return (int)(m->m[c >> 6] >> (c & 63) & 1); }
static inline int disj(const mask_t *a, const mask_t *b) { uint64_t x = 0; for (int w = 0; w < W; w++) x |= a->m[w] & b->m[w]; return x == 0; }

/* ---------- stage A: T1 quadruples ---------- */
static int nq; static int (*qy)[2]; static mask_t *qmask; static unsigned char (*qcol)[4];
static int **alist; static int achosen[128]; static long long anodes, alimit;
static int ncolA; static int colA_of[1024];     /* class -> column index or -1 */
static int (*on_cover)(void);
static int searchA(int depth, int cnt, int ncov) {
    if (ncov == ncolA) return on_cover();
    if (++anodes > alimit) return 1;
    int *lst = alist[depth];
    static int cc[256];
    memset(cc, 0, sizeof(int) * ncolA);
    for (int i = 0; i < cnt; i++) { const unsigned char *c = qcol[lst[i]]; for (int j = 0; j < 4; j++) cc[c[j]]++; }
    mask_t cov; memset(&cov, 0, sizeof cov);
    for (int d = 0; d < depth; d++) for (int w = 0; w < W; w++) cov.m[w] |= qmask[achosen[d]].m[w];
    int best = -1, bs = 1 << 30, ties = 0;
    for (int c = 0; c < ncolA; c++) {
        if (getbit(&cov, c)) continue;
        if (cc[c] < bs) { bs = cc[c]; best = c; ties = 1; } else if (cc[c] == bs && rndint(++ties) == 0) best = c;
    }
    if (bs == 0) return 0;
    int *nxt = alist[depth + 1];
    for (int i = 0; i < cnt; i++) {
        int x = lst[i];
        if (!getbit(&qmask[x], best)) continue;
        int m = 0;
        for (int j = 0; j < cnt; j++) { int y = lst[j]; if (disj(&qmask[x], &qmask[y])) nxt[m++] = y; }
        achosen[depth] = x;
        if (searchA(depth + 1, m, ncov + 4)) return 1;
    }
    return 0;
}

/* ---------- stage B: T5 quintuples over the remaining pure classes ---------- */
static int nrB, capB; static int (*rbB)[5]; static mask_t *rmB; static unsigned char (*rcB)[10];
static int **blist; static int bchosen[64]; static long long bnodes;
static int ncolB; static int colB_of[1024];
static int searchB(int depth, int cnt, int ncov) {
    if (ncov == ncolB) return 1;
    if (++bnodes > 100000000) return 0;
    int *lst = blist[depth];
    static int cc[256];
    memset(cc, 0, sizeof(int) * ncolB);
    for (int i = 0; i < cnt; i++) { const unsigned char *c = rcB[lst[i]]; for (int j = 0; j < 10; j++) cc[c[j]]++; }
    mask_t cov; memset(&cov, 0, sizeof cov);
    for (int d = 0; d < depth; d++) for (int w = 0; w < W; w++) cov.m[w] |= rmB[bchosen[d]].m[w];
    int best = -1, bs = 1 << 30;
    for (int c = 0; c < ncolB; c++) if (!getbit(&cov, c) && cc[c] < bs) { bs = cc[c]; best = c; }
    if (bs == 0) return 0;
    int *nxt = blist[depth + 1];
    for (int i = 0; i < cnt; i++) {
        int x = lst[i];
        if (!getbit(&rmB[x], best)) continue;
        int m = 0;
        for (int j = 0; j < cnt; j++) { int y = lst[j]; if (disj(&rmB[x], &rmB[y])) nxt[m++] = y; }
        bchosen[depth] = x;
        if (searchB(depth + 1, m, ncov + 10)) return 1;
    }
    return 0;
}
static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static void canon5(const int *b, int *out) {
    int best[5], cand[5], have = 0;
    for (int s = 0; s < 2; s++) for (int t = 0; t < 5; t++) {
        for (int i = 0; i < 5; i++) cand[i] = mp((s ? -b[i] : b[i]) - (s ? -b[t] : b[t]));
        qsort(cand, 5, sizeof(int), cmpint);
        if (!have || memcmp(cand, best, sizeof cand) < 0) { memcpy(best, cand, sizeof cand); have = 1; }
    }
    memcpy(out, best, sizeof best);
}

/* current T3 and globals for the callback */
static int f1, f2, ty;
static long long covers_seen, covers_cap, b_attempts;
static int found_flag;
static const char *outpre;
static int pure_used[1024];

static int lift(int a, int x) { int z = mp(x); while (z % 3 != a) z += p; return z; }

static int finish(void) {
    /* assemble family in Z_v, verify difference multiset, write certificate */
    int fam[64][5], nb = 0;
    for (int d = 0; d < a1; d++) {
        int y1 = qy[achosen[d]][0], y2 = qy[achosen[d]][1];
        int b[5] = {lift(0, 0), lift(1, y1), lift(1, -y1), lift(2, y2), lift(2, -y2)};
        memcpy(fam[nb++], b, sizeof b);
    }
    { int b[5] = {lift(0, 0), lift(0, f1), lift(0, f2), lift(1, ty), lift(2, ty)}; memcpy(fam[nb++], b, sizeof b); }
    for (int d = 0; d < a5; d++) {
        int b[5]; for (int i = 0; i < 5; i++) b[i] = lift(0, rbB[bchosen[d]][i]);
        memcpy(fam[nb++], b, sizeof b);
    }
    int *count = calloc(v, sizeof(int));
    for (int b = 0; b < nb; b++) for (int i = 0; i < 5; i++) for (int j = 0; j < 5; j++) if (i != j) count[((fam[b][i] - fam[b][j]) % v + v) % v]++;
    int good = nb == (v - 1) / 20 && count[0] == 0;
    for (int d = 1; d < v && good; d++) if (count[d] != 1) good = 0;
    free(count);
    if (!good) { printf("INTERNAL: assembled family fails the difference check\n"); fflush(stdout); return 0; }
    char path[1024];
    snprintf(path, sizeof path, "%s.sol", outpre);
    FILE *f = fopen(path, "w");
    fprintf(f, "CDF %d 5\n", v);
    for (int b = 0; b < nb; b++) { qsort(fam[b], 5, sizeof(int), cmpint); fprintf(f, "%d %d %d %d %d\n", fam[b][0], fam[b][1], fam[b][2], fam[b][3], fam[b][4]); }
    fclose(f);
    return 1;
}

static int on_cover_impl(void) {
    covers_seen++;
    /* remaining pure classes */
    memset(pure_used, 0, sizeof(int) * (P2 + 1));
    pure_used[cls[mp(f1)]] = pure_used[cls[mp(f2)]] = pure_used[cls[mp(f2 - f1)]] = 1;
    for (int d = 0; d < a1; d++) {
        int c1 = cls[mp(2 * qy[achosen[d]][0])], c2 = cls[mp(2 * qy[achosen[d]][1])];
        if (pure_used[c1] || pure_used[c2]) { printf("INTERNAL: pure overlap\n"); return 1; }
        pure_used[c1] = pure_used[c2] = 1;
    }
    ncolB = 0;
    for (int c = 1; c <= P2; c++) colB_of[c] = pure_used[c] ? -1 : ncolB++;
    if (ncolB != 10 * a5) { printf("INTERNAL: ncolB=%d\n", ncolB); return 1; }
    nrB = 0;
    if (a5 > 0) {
        int S[1024], nS = 0;
        for (int x = 1; x < p; x++) if (!pure_used[cls[x]]) S[nS++] = x;
        for (int ia = 0; ia < nS; ia++) { int a = S[ia];
          for (int ib = ia + 1; ib < nS; ib++) { int b = S[ib]; if (pure_used[cls[b - a]]) continue;
            for (int ic = ib + 1; ic < nS; ic++) { int c = S[ic]; if (pure_used[cls[c - a]] || pure_used[cls[c - b]]) continue;
              for (int id = ic + 1; id < nS; id++) { int d = S[id];
                if (pure_used[cls[d - a]] || pure_used[cls[d - b]] || pure_used[cls[d - c]]) continue;
                int blk[5] = {0, a, b, c, d}, cl[10], m = 0, ok = 1;
                for (int i = 0; i < 5 && ok; i++) for (int j = i + 1; j < 5; j++) { int q = cls[mp(blk[i] - blk[j])];
                    for (int t = 0; t < m; t++) if (cl[t] == q) { ok = 0; break; } if (!ok) break; cl[m++] = q; }
                if (!ok) continue;
                int cn[5]; canon5(blk, cn); if (memcmp(cn, blk, sizeof blk)) continue;
                if (nrB == capB) { capB = capB ? 2 * capB : 4096; rbB = realloc(rbB, sizeof(int) * 5 * capB);
                    rmB = realloc(rmB, sizeof(mask_t) * capB); rcB = realloc(rcB, 10 * capB); }
                memcpy(rbB[nrB], blk, sizeof blk); memset(&rmB[nrB], 0, sizeof(mask_t));
                for (int t = 0; t < 10; t++) { rcB[nrB][t] = (unsigned char)colB_of[cl[t]]; setbit(&rmB[nrB], colB_of[cl[t]]); }
                nrB++;
              } } } }
    }
    b_attempts++;
    for (int d = 0; d <= a5 + 1; d++) blist[d] = realloc(blist[d], sizeof(int) * (nrB + 1));
    for (int i = 0; i < nrB; i++) blist[0][i] = i;
    bnodes = 0;
    if (searchB(0, nrB, 0)) {
        if (finish()) { found_flag = 1; return 1; }
    }
    return covers_seen >= covers_cap;     /* stop stage A after covers_cap covers for this T3 */
}

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: cdf_inv3p v seed seconds outprefix [covers_per_t3] [nodelimit_A]\n"); return 2; }
    v = atoi(argv[1]); uint64_t seed = strtoull(argv[2], 0, 10); double limit = atof(argv[3]); outpre = argv[4];
    covers_cap = argc > 5 ? atoll(argv[5]) : 200; alimit = argc > 6 ? atoll(argv[6]) : 2000000;
    if (v % 3 || (v - 1) % 20) { fprintf(stderr, "need v = 3p = 1 mod 20\n"); return 2; }
    p = v / 3; P2 = (p - 1) / 2;
    if ((P2 - 3) % 4) { fprintf(stderr, "no all-stable structure: (P2-3)/4 not integral\n"); return 2; }
    a1 = (P2 - 3) / 4;
    if ((P2 - 3 - 2 * a1) % 10) { fprintf(stderr, "no all-stable structure: a5 not integral\n"); return 2; }
    a5 = (P2 - 3 - 2 * a1) / 10;
    if (a1 + a5 + 1 != (v - 1) / 20 || P2 > 128) { fprintf(stderr, "inconsistent sizes\n"); return 2; }
    rng = seed * 0x2545F4914F6CDD1DULL + 1234567;
    cls = malloc(sizeof(int) * p);
    for (int d = 0; d < p; d++) cls[d] = d <= P2 ? d : p - d;
    qy = malloc(sizeof(int) * 2 * P2 * P2); qmask = malloc(sizeof(mask_t) * P2 * P2); qcol = malloc(4 * P2 * P2);
    alist = calloc(130, sizeof(int *)); blist = calloc(130, sizeof(int *));
    for (int d = 0; d < 130; d++) alist[d] = malloc(sizeof(int) * P2 * P2);
    on_cover = on_cover_impl;
    printf("start v=%d p=%d a1=%d a5=%d seed=%llu covers_per_t3=%lld nodelimitA=%lld\n", v, p, a1, a5,
           (unsigned long long)seed, covers_cap, alimit);
    fflush(stdout);
    double t0 = now(), tl = t0;
    long long t3_tries = 0, total_covers = 0;
    while (now() - t0 < limit) {
        /* random T3 */
        f1 = 1 + rndint(p - 1); f2 = 1 + rndint(p - 1); ty = rndint(p);
        int tri[3] = {cls[mp(f1)], cls[mp(f2)], cls[mp(f2 - f1)]};
        int orb[3] = {cls[mp(ty)], cls[mp(ty - f1)], cls[mp(ty - f2)]};
        if (!tri[0] || !tri[1] || !tri[2] || tri[0] == tri[1] || tri[0] == tri[2] || tri[1] == tri[2]) continue;
        if (!orb[0] || !orb[1] || !orb[2] || orb[0] == orb[1] || orb[0] == orb[2] || orb[1] == orb[2]) continue;
        t3_tries++;
        int orbused[1024] = {0}, triused[1024] = {0};
        for (int t = 0; t < 3; t++) { orbused[orb[t]] = 1; triused[tri[t]] = 1; }
        ncolA = 0;
        for (int c = 1; c <= P2; c++) colA_of[c] = orbused[c] ? -1 : ncolA++;
        nq = 0;
        for (int y1 = 1; y1 <= P2; y1++) for (int y2 = y1 + 1; y2 <= P2; y2++) {
            int q[4] = {cls[y1], cls[y2], cls[mp(y1 + y2)], cls[mp(y1 - y2)]};
            int ok = q[2] && q[3];
            for (int i = 0; i < 4 && ok; i++) { if (orbused[q[i]]) ok = 0; for (int j = i + 1; j < 4; j++) if (q[i] == q[j]) ok = 0; }
            if (!ok) continue;
            if (triused[cls[mp(2 * y1)]] || triused[cls[mp(2 * y2)]]) continue;
            qy[nq][0] = y1; qy[nq][1] = y2; memset(&qmask[nq], 0, sizeof(mask_t));
            for (int i = 0; i < 4; i++) { qcol[nq][i] = (unsigned char)colA_of[q[i]]; setbit(&qmask[nq], colA_of[q[i]]); }
            nq++;
        }
        for (int i = 0; i < nq; i++) alist[0][i] = i;
        for (int i = nq - 1; i > 0; i--) { int j = rndint(i + 1); int t = alist[0][i]; alist[0][i] = alist[0][j]; alist[0][j] = t; }
        covers_seen = 0; anodes = 0; found_flag = 0;
        searchA(0, nq, 0);
        total_covers += covers_seen;
        if (found_flag) {
            printf("FOUND v=%d seed=%llu t3_tries=%lld covers=%lld b_attempts=%lld seconds=%.2f T3=(%d,%d,%d)\n", v,
                   (unsigned long long)seed, t3_tries, total_covers, b_attempts, now() - t0, f1, f2, ty);
            return 0;
        }
        if (now() - tl > 30) { printf("t3_tries=%lld covers=%lld b_attempts=%lld last_rowsB=%d t=%.0f\n", t3_tries, total_covers,
                                      b_attempts, nrB, now() - t0); fflush(stdout); tl = now(); }
    }
    printf("TIMEOUT v=%d seed=%llu t3_tries=%lld covers=%lld b_attempts=%lld seconds=%.2f\n", v, (unsigned long long)seed,
           t3_tries, total_covers, b_attempts, now() - t0);
    return 3;
}
