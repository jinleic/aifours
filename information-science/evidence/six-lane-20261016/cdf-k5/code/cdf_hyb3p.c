/* cdf_hyb3p.c -- cyclic (3p,5,1) difference families from mostly "166-type" stable blocks plus one constructed
 * pair of general blocks (for p where the all-stable structure of cdf_inv3p.c fails the counting, e.g. p = 107, 227).
 *
 * Coordinates Z_{3p} = Z_3 x Z_p (CRT); classes of Z_p: C = (Z_p minus 0) mod +-1, P2 = (p-1)/2.
 * Z_{3p} classes: pure [(0,y)] (P2 of them), mixed [(1,y)] (2*P2: y in Z_p^*), and [(1,0)].
 * "Orbit item" y in C stands for the two mixed classes [(1,y)] and [(1,-y)]; "pure item" y for [(0,y)].
 * Block types (unit mu = (1,-1); every T-block has a mu-stable difference multiset):
 *   T1(y1,y2)   = {(0,0),(1,+-y1),(2,+-y2)}:       orbit items {y1,y2,y1+y2,y1-y2}, pure items {2y1,2y2}
 *   T3(f1,f2,y) = {(0,0),(0,f1),(0,f2),(1,y),(2,y)}: orbit items {y,y-f1,y-f2}, pure {f1,f2,f2-f1}, and [(1,0)]
 *   T5(Q)       = {0} x Q:                          pure items Delta(Q)
 * General pair (mode 1): two blocks G = {(0,0),(0,u2),(0,u3),(1,w1),(1,w2)} (pattern (3,2,0)) whose oriented
 *   label-0 -> label-1 differences {w_j - u_i} (6 + 6 values) are distinct and jointly closed under negation, so
 *   together they cover 6 complete orbit items; pure items {u2,u3,u3-u2,w2-w1} each.  Pairs come from gpairs.c.
 *   (A one-parameter construction with two internal +- pairs in each block always repeats the label-1 pure class
 *   w2-w1 between the two blocks, so it is not used.)
 * Counting, mode 1: orbit items 6 + 3 + 4*a1 = P2, pure items 8 + 3 + 2*a1 + 10*a5 = P2, blocks 2+1+a1+a5 = n.
 *   p = 107: a1 = 11, a5 = 2 (n = 16);  p = 227: a1 = 26, a5 = 5 (n = 34).
 * Mode 0 is the all-stable structure (no G pair): 3 + 4*a1 = P2, 3 + 2*a1 + 10*a5 = P2.
 * Search per configuration (random G pair and T3): stage A = randomized bitset exact cover of the remaining orbit
 * items by T1 rows whose pure items avoid those already used; stage B, for each A-cover, = exact cover of the
 * remaining pure items by a5 quintuples (enumerated, canonical up to translation and negation).
 * Every assembled family is re-checked in-program (full difference multiset in Z_{3p}) before it is written.
 *
 * Usage: cdf_hyb3p v seed seconds outprefix mode [covers_per_cfg] [nodelimit_A] [gpairs_file (mode 1)]
 * Exit 0 found (outprefix.sol), 3 time limit.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define W 2
typedef struct { uint64_t m[W]; } mask_t;
static int v, p, P2, a1, a5, mode;
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

/* ---------- stage A ---------- */
static int nq; static int (*qy)[2]; static mask_t *qmask; static unsigned char (*qcol)[4];
static int **alist; static int achosen[128]; static long long anodes, alimit;
static int ncolA; static int colA_of[1024];
static int on_cover(void);
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

/* ---------- stage B ---------- */
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

/* configuration */
static int f1, f2, ty;
static int G[2][5][2], nG;                      /* general blocks as (label, x) pairs */
static int (*gpair)[8], ngpair;
static int orbused[1024], pureused0[1024], pure_used[1024];
static long long covers_seen, covers_cap, b_attempts;
static int found_flag;
static const char *outpre;

static int lift(int a, int x) { int z = mp(x); while (z % 3 != a) z += p; return z; }

static int finish(void) {
    int fam[64][5], nb = 0;
    for (int d = 0; d < a1; d++) {
        int y1 = qy[achosen[d]][0], y2 = qy[achosen[d]][1];
        int b[5] = {lift(0, 0), lift(1, y1), lift(1, -y1), lift(2, y2), lift(2, -y2)};
        memcpy(fam[nb++], b, sizeof b);
    }
    { int b[5] = {lift(0, 0), lift(0, f1), lift(0, f2), lift(1, ty), lift(2, ty)}; memcpy(fam[nb++], b, sizeof b); }
    for (int d = 0; d < a5; d++) { int b[5]; for (int i = 0; i < 5; i++) b[i] = lift(0, rbB[bchosen[d]][i]); memcpy(fam[nb++], b, sizeof b); }
    for (int g = 0; g < nG; g++) { int b[5]; for (int i = 0; i < 5; i++) b[i] = lift(G[g][i][0], G[g][i][1]); memcpy(fam[nb++], b, sizeof b); }
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

static int on_cover(void) {
    covers_seen++;
    memcpy(pure_used, pureused0, sizeof(int) * (P2 + 1));
    for (int d = 0; d < a1; d++) {
        int c1 = cls[mp(2 * qy[achosen[d]][0])], c2 = cls[mp(2 * qy[achosen[d]][1])];
        if (pure_used[c1] || pure_used[c2] || c1 == c2) { printf("INTERNAL: pure overlap\n"); return 1; }
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
    if (searchB(0, nrB, 0)) { if (finish()) { found_flag = 1; return 1; } }
    return covers_seen >= covers_cap;
}

/* mark helpers: return 0 on conflict */
static int use_orb(int y) { int c = cls[mp(y)]; if (!c || orbused[c]) return 0; orbused[c] = 1; return 1; }
static int use_pure(int y) { int c = cls[mp(y)]; if (!c || pureused0[c]) return 0; pureused0[c] = 1; return 1; }

static int make_config(void) {
    memset(orbused, 0, sizeof(int) * (P2 + 1)); memset(pureused0, 0, sizeof(int) * (P2 + 1));
    nG = 0;
    if (mode == 1) {
        /* a jointly closed (3,2,0) pair from gpairs.c output: G = {(0,0),(0,u2),(0,u3),(1,w1),(1,w2)} */
        const int *gp = gpair[rndint(ngpair)];
        int vals[12], nv = 0;
        for (int g = 0; g < 2; g++) {
            int U2 = gp[4 * g], U3 = gp[4 * g + 1], W1 = gp[4 * g + 2], W2 = gp[4 * g + 3];
            int pts[5][2] = {{0, 0}, {0, U2}, {0, U3}, {1, W1}, {1, W2}};
            memcpy(G[g], pts, sizeof pts);
            if (!use_pure(U2) || !use_pure(U3) || !use_pure(U3 - U2) || !use_pure(W2 - W1)) return 0;
            int u[3] = {0, U2, U3}, w[2] = {W1, W2};
            for (int j = 0; j < 2; j++) for (int i = 0; i < 3; i++) vals[nv++] = mp(w[j] - u[i]);
        }
        nG = 2;
        /* the 12 oriented mixed values must be distinct and closed under negation (6 complete orbit items) */
        for (int s = 0; s < 12; s++) {
            int neg = 0;
            for (int t = 0; t < 12; t++) { if (t != s && vals[t] == vals[s]) { printf("INTERNAL: repeated mixed value\n"); return 0; }
                                           if (vals[t] == mp(-vals[s])) neg = 1; }
            if (!neg) { printf("INTERNAL: pair not closed\n"); return 0; }
        }
        for (int s = 0; s < 12; s++) if (vals[s] <= P2 && !use_orb(vals[s])) return 0;
    }
    f1 = 1 + rndint(p - 1); f2 = 1 + rndint(p - 1); ty = rndint(p);
    if (!use_pure(f1) || !use_pure(f2) || !use_pure(f2 - f1)) return 0;
    if (!use_orb(ty) || !use_orb(ty - f1) || !use_orb(ty - f2)) return 0;
    return 1;
}

int main(int argc, char **argv) {
    if (argc < 6) { fprintf(stderr, "usage: cdf_hyb3p v seed seconds outprefix mode [covers_per_cfg] [nodelimit_A] [gpairs_file]\n"); return 2; }
    v = atoi(argv[1]); uint64_t seed = strtoull(argv[2], 0, 10); double limit = atof(argv[3]); outpre = argv[4];
    mode = atoi(argv[5]);
    covers_cap = argc > 6 ? atoll(argv[6]) : 20000; alimit = argc > 7 ? atoll(argv[7]) : 50000000;
    if (v % 3 || (v - 1) % 20) { fprintf(stderr, "need v = 3p = 1 mod 20\n"); return 2; }
    p = v / 3; P2 = (p - 1) / 2;
    int orb_fixed = mode == 1 ? 9 : 3, pure_fixed = mode == 1 ? 11 : 3, nfixed = mode == 1 ? 3 : 1;
    if ((P2 - orb_fixed) % 4) { fprintf(stderr, "a1 not integral\n"); return 2; }
    a1 = (P2 - orb_fixed) / 4;
    if ((P2 - pure_fixed - 2 * a1) % 10 || P2 - pure_fixed - 2 * a1 < 0) { fprintf(stderr, "a5 not integral\n"); return 2; }
    a5 = (P2 - pure_fixed - 2 * a1) / 10;
    if (a1 + a5 + nfixed != (v - 1) / 20 || P2 > 128) { fprintf(stderr, "inconsistent sizes\n"); return 2; }
    rng = seed * 0x2545F4914F6CDD1DULL + 7654321;
    if (mode == 1) {
        if (argc < 9) { fprintf(stderr, "mode 1 needs gpairs_file\n"); return 2; }
        FILE *gf = fopen(argv[8], "r");
        if (!gf) { perror(argv[8]); return 2; }
        int cap = 1 << 16, t[8];
        gpair = malloc(sizeof(int) * 8 * cap);
        while (fscanf(gf, "%d %d %d %d %d %d %d %d", &t[0], &t[1], &t[2], &t[3], &t[4], &t[5], &t[6], &t[7]) == 8) {
            if (ngpair == cap) { cap *= 2; gpair = realloc(gpair, sizeof(int) * 8 * cap); }
            memcpy(gpair[ngpair++], t, sizeof t);
        }
        fclose(gf);
        if (!ngpair) { fprintf(stderr, "no pairs\n"); return 2; }
        printf("loaded %d general pairs from %s\n", ngpair, argv[8]);
    }
    cls = malloc(sizeof(int) * p);
    for (int d = 0; d < p; d++) cls[d] = d <= P2 ? d : p - d;
    qy = malloc(sizeof(int) * 2 * P2 * P2); qmask = malloc(sizeof(mask_t) * P2 * P2); qcol = malloc(4 * P2 * P2);
    alist = calloc(130, sizeof(int *)); blist = calloc(130, sizeof(int *));
    for (int d = 0; d < 130; d++) alist[d] = malloc(sizeof(int) * P2 * P2);
    printf("start v=%d p=%d mode=%d a1=%d a5=%d seed=%llu covers_per_cfg=%lld nodelimitA=%lld\n", v, p, mode, a1, a5,
           (unsigned long long)seed, covers_cap, alimit);
    fflush(stdout);
    double t0 = now(), tl = t0;
    long long cfg_tries = 0, cfg_ok = 0, total_covers = 0;
    while (now() - t0 < limit) {
        cfg_tries++;
        if (!make_config()) continue;
        cfg_ok++;
        ncolA = 0;
        for (int c = 1; c <= P2; c++) colA_of[c] = orbused[c] ? -1 : ncolA++;
        nq = 0;
        for (int y1 = 1; y1 <= P2; y1++) for (int y2 = y1 + 1; y2 <= P2; y2++) {
            int q[4] = {cls[y1], cls[y2], cls[mp(y1 + y2)], cls[mp(y1 - y2)]};
            int ok = q[2] && q[3];
            for (int i = 0; i < 4 && ok; i++) { if (orbused[q[i]]) ok = 0; for (int j = i + 1; j < 4; j++) if (q[i] == q[j]) ok = 0; }
            if (!ok) continue;
            if (pureused0[cls[mp(2 * y1)]] || pureused0[cls[mp(2 * y2)]]) continue;
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
            printf("FOUND v=%d seed=%llu cfg_tries=%lld cfg_ok=%lld covers=%lld b_attempts=%lld seconds=%.2f T3=(%d,%d,%d)\n", v,
                   (unsigned long long)seed, cfg_tries, cfg_ok, total_covers, b_attempts, now() - t0, f1, f2, ty);
            return 0;
        }
        if (now() - tl > 30) { printf("cfg_tries=%lld cfg_ok=%lld covers=%lld b_attempts=%lld last_rowsA=%d last_rowsB=%d t=%.0f\n",
                                      cfg_tries, cfg_ok, total_covers, b_attempts, nq, nrB, now() - t0); fflush(stdout); tl = now(); }
    }
    printf("TIMEOUT v=%d seed=%llu cfg_tries=%lld cfg_ok=%lld covers=%lld b_attempts=%lld seconds=%.2f\n", v,
           (unsigned long long)seed, cfg_tries, cfg_ok, total_covers, b_attempts, now() - t0);
    return 3;
}
