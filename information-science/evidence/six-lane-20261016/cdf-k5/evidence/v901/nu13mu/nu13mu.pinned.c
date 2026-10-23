/* nu13mu.c -- v = 901 = 17*53 (Z_17 x Z_53 by CRT): 2 orbits of 13 blocks under nu = (1, 10) plus a 19-block
 * defect built from mu-stable blocks, mu = (1,-1) (see evidence/v901/PLAN-cycle1.md, cycle 1b).
 *   Defect: 13 T1 {(0,0),(a1,+-y1),(a2,+-y2)} + 4 T1' {(0,0),(+-a1,y1),(+-a2,y2)} + one pair {B, mu B}; it covers
 *   all 8 K classes, all 26 pure classes and 12 mixed nu-orbits forming 6 mu-pairs (156 classes).
 *   Bulk: base blocks B1, B2 whose 20 classes meet each of the other 20 mixed nu-orbits once; their nu-orbits
 *   (26 blocks) cover those 260 classes.
 * Per configuration: random 6 mu-pairs of mixed nu-orbits; random pair B inside them; exact cover (bitset
 * Algorithm X) of every remaining defect item by T1/T1' rows; then randomized B1 and exhaustive B2.
 * Every assembled family is checked in-program (full difference multiset) before outprefix.sol is written.
 * Usage: nu13mu seed seconds outprefix [nodelimitS] [b1tries]
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define V 901
#define HH 450
#define M 17
#define Q 53
#define W 4
typedef struct { uint64_t m[W]; } mask_t;
static int crt[M][Q], ya[V], yy[V], mu_of[V], nu_of[V];
static int M2 = 8, Q2 = 26, NO = 208, NI = 242;
static int norb, orbsz[HH + 1], orbof[HH + 1];   /* nu-orbits of classes */
static uint64_t rng;
static uint64_t rnd(void) { uint64_t z = (rng += 0x9E3779B97F4A7C15ULL); z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL; z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL; return z ^ (z >> 31); }
static int rndint(int k) { return (int)(rnd() % (uint64_t)k); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static inline int mv(int z) { z %= V; return z < 0 ? z + V : z; }
static inline int cl(int d) { d = mv(d); return d <= HH ? d : V - d; }
static inline void setbit(mask_t *x, int c) { x->m[c >> 6] |= 1ULL << (c & 63); }
static inline int getbit(const mask_t *x, int c) { return (int)(x->m[c >> 6] >> (c & 63) & 1); }
static inline int disj(const mask_t *a, const mask_t *b) { uint64_t x = 0; for (int w = 0; w < W; w++) x |= a->m[w] & b->m[w]; return x == 0; }
static int cmpint(const void *x, const void *y) { return *(const int *)x - *(const int *)y; }
static int zof(int a, int y) { a %= M; if (a < 0) a += M; y %= Q; if (y < 0) y += Q; return crt[a][y]; }
static int item_of_d(int d, int *kind) {     /* mu-quotient item of the class of d */
    d = mv(d); if (!d) { *kind = -1; return -1; }
    int da = ya[d], dy = yy[d], a = da <= M2 ? da : M - da, y = dy <= Q2 ? dy : Q - dy;
    if (da == 0) { *kind = 1; return NO + (y - 1); }
    if (dy == 0) { *kind = 2; return NO + Q2 + (a - 1); }
    *kind = 0; return (a - 1) * Q2 + (y - 1);
}
static int classes_ok(const int *z) {
    int c[10], k = 0;
    for (int i = 0; i < 5; i++) for (int j = i + 1; j < 5; j++) { int x = cl(z[j] - z[i]); if (!x) return 0; for (int t = 0; t < k; t++) if (c[t] == x) return 0; c[k++] = x; }
    return 1;
}
/* stable rows */
static int ns; static int sz[200000][5]; static mask_t smask[200000]; static unsigned char stype[200000];
static uint64_t *hset; static size_t hcap = (size_t)1 << 22;
static int hinsert(const int *c) {
    uint64_t k = 1469598103934665603ULL; for (int i = 0; i < 5; i++) { k ^= (uint64_t)c[i] + 1; k *= 1099511628211ULL; }
    if (!k) k = 1; size_t h = k & (hcap - 1);
    while (hset[h]) { if (hset[h] == k) return 0; h = (h + 1) & (hcap - 1); }
    hset[h] = k; return 1;
}
static void canon(const int *z, int *out) {
    int best[5], cand[5], have = 0;
    for (int s = 0; s < 2; s++) for (int t = 0; t < 5; t++) {
        for (int i = 0; i < 5; i++) cand[i] = mv((s ? -z[i] : z[i]) - (s ? -z[t] : z[t]));
        qsort(cand, 5, sizeof(int), cmpint);
        if (!have || memcmp(cand, best, sizeof cand) < 0) { memcpy(best, cand, sizeof cand); have = 1; }
    }
    memcpy(out, best, sizeof best);
}
static void add_stable(int p[5][2], int type) {
    int z[5]; for (int i = 0; i < 5; i++) z[i] = zof(p[i][0], p[i][1]);
    if (!classes_ok(z)) return;
    int it[10], kd[10], k = 0;
    for (int i = 0; i < 5; i++) for (int j = i + 1; j < 5; j++) { it[k] = item_of_d(z[j] - z[i], &kd[k]); k++; }
    for (int t = 0; t < 10; t++) { int mult = 0; for (int s = 0; s < 10; s++) if (it[s] == it[t]) mult++;
        if ((kd[t] == 0 && mult != 2) || (kd[t] != 0 && mult != 1)) return; }
    int c[5]; canon(z, c); if (!hinsert(c)) return;
    memcpy(sz[ns], z, sizeof z); memset(&smask[ns], 0, sizeof(mask_t));
    for (int t = 0; t < 10; t++) setbit(&smask[ns], it[t]);
    stype[ns++] = (unsigned char)type;
}
/* exact cover of 'prim' by rows in list */
static int **lists; static int chosen[64]; static long long nodes, nodelimit; static mask_t prim;
static int xc(int depth, int cnt, mask_t cov) {
    int done = 1; for (int w = 0; w < W; w++) if ((cov.m[w] & prim.m[w]) != prim.m[w]) done = 0;
    if (done) return depth + 1000;
    if (++nodes > nodelimit) return -1;
    int *lst = lists[depth]; static int cc[W * 64];
    memset(cc, 0, sizeof cc);
    for (int i = 0; i < cnt; i++) { const mask_t *x = &smask[lst[i]]; for (int w = 0; w < W; w++) { uint64_t b = x->m[w]; while (b) { cc[w * 64 + __builtin_ctzll(b)]++; b &= b - 1; } } }
    int best = -1, bs = 1 << 30, ties = 0;
    for (int c = 0; c < NI; c++) { if (!getbit(&prim, c) || getbit(&cov, c)) continue;
        if (cc[c] < bs) { bs = cc[c]; best = c; ties = 1; } else if (cc[c] == bs && rndint(++ties) == 0) best = c; }
    if (bs == 0) return 0;
    int *nxt = lists[depth + 1];
    for (int i = 0; i < cnt; i++) {
        int x = lst[i]; if (!getbit(&smask[x], best)) continue;
        int k = 0; for (int j = 0; j < cnt; j++) { int y = lst[j]; if (disj(&smask[x], &smask[y])) nxt[k++] = y; }
        chosen[depth] = x;
        mask_t nc = cov; for (int w = 0; w < W; w++) nc.m[w] |= smask[x].m[w];
        int r = xc(depth + 1, k, nc); if (r != 0) return r;
    }
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: nu13mu seed seconds outprefix [nodelimitS] [b1tries]\n"); return 2; }
    uint64_t seed = strtoull(argv[1], 0, 10); double limit = atof(argv[2]); const char *pre = argv[3];
    nodelimit = argc > 4 ? atoll(argv[4]) : 2000000; long b1tries = argc > 5 ? atol(argv[5]) : 300;
    rng = seed * 0x2545F4914F6CDD1DULL + 13013;
    for (int z = 0; z < V; z++) { crt[z % M][z % Q] = z; ya[z] = z % M; yy[z] = z % Q; }
    for (int z = 0; z < V; z++) { mu_of[z] = zof(ya[z], -yy[z]); nu_of[z] = zof(ya[z], 10 * yy[z]); }
    /* nu-orbits of classes */
    memset(orbof, -1, sizeof orbof); norb = 0;
    for (int c = 1; c <= HH; c++) { if (orbof[c] >= 0) continue; int x = c, s = 0; do { orbof[x] = norb; s++; x = cl(nu_of[x]); } while (x != c); orbsz[norb++] = s; }
    /* mixed orbits and their mu partners */
    int mixed[64], nmix = 0, partner[512];
    for (int o = 0; o < norb; o++) partner[o] = -1;
    for (int c = 1; c <= HH; c++) { int kd; item_of_d(c, &kd); if (kd != 0) continue; int o = orbof[c], o2 = orbof[cl(mu_of[c])];
        if (partner[o] < 0) { partner[o] = o2; } else if (partner[o] != o2) { printf("INTERNAL: mu partner\n"); return 1; } }
    for (int o = 0; o < norb; o++) if (orbsz[o] == 13 && partner[o] >= 0) mixed[nmix++] = o;
    int pairs[32][2], npairs = 0;
    for (int i = 0; i < nmix; i++) { int o = mixed[i]; if (partner[o] > o) { pairs[npairs][0] = o; pairs[npairs][1] = partner[o]; npairs++; } else if (partner[o] == o) { printf("INTERNAL: self-paired orbit\n"); return 1; } }
    hset = calloc(hcap, sizeof(uint64_t));
    for (int a1 = 1; a1 < M; a1++) for (int a2 = 1; a2 < M; a2++) if (a1 != a2) for (int y1 = 1; y1 < Q; y1++) for (int y2 = 1; y2 < Q; y2++) {
        int p[5][2] = {{0, 0}, {a1, y1}, {a1, -y1}, {a2, y2}, {a2, -y2}}; add_stable(p, 1); }
    int n1 = ns;
    for (int a1 = 1; a1 < M; a1++) for (int a2 = 1; a2 < M; a2++) for (int y1 = 1; y1 < Q; y1++) for (int y2 = 1; y2 < Q; y2++) {
        int p[5][2] = {{0, 0}, {a1, y1}, {-a1, y1}, {a2, y2}, {-a2, y2}}; add_stable(p, 2); }
    lists = calloc(70, sizeof(int *)); for (int d = 0; d < 70; d++) lists[d] = malloc(sizeof(int) * (ns + 1));
    printf("start seed=%llu nu-orbits=%d mixed=%d mu-pairs=%d rows T1=%d T1'=%d nodelimitS=%lld b1tries=%ld\n",
           (unsigned long long)seed, norb, nmix, npairs, n1, ns - n1, nodelimit, b1tries);
    fflush(stdout);
    if (nmix != 32 || npairs != 16) { printf("INTERNAL: unexpected orbit structure\n"); return 1; }
    double t0 = now(), tl = t0;
    long long cfg = 0, s_ok = 0, b1_ok = 0, b2_try = 0;
    while (now() - t0 < limit) {
        cfg++;
        int pick[16]; for (int i = 0; i < 16; i++) pick[i] = i;
        for (int i = 15; i > 0; i--) { int j = rndint(i + 1); int t = pick[i]; pick[i] = pick[j]; pick[j] = t; }
        int intarget[512] = {0};
        for (int i = 0; i < 6; i++) { intarget[pairs[pick[i]][0]] = 1; intarget[pairs[pick[i]][1]] = 1; }
        mask_t used; memset(&used, 0, sizeof used);
        for (int c = 1; c <= HH; c++) { int kd, it = item_of_d(c, &kd); if (kd == 0 && !intarget[orbof[c]]) setbit(&used, it); }
        /* random free pair inside the target */
        int B[5], ok = 0;
        for (int tries = 0; tries < 3000000 && !ok; tries++) {
            int z[5] = {0, 1 + rndint(V - 1), 1 + rndint(V - 1), 1 + rndint(V - 1), 1 + rndint(V - 1)};
            if (!classes_ok(z)) continue;
            int it[10], k = 0, good = 1;
            for (int i = 0; i < 5 && good; i++) for (int j = i + 1; j < 5 && good; j++) { int kd; it[k] = item_of_d(z[j] - z[i], &kd);
                if (kd != 0 || getbit(&used, it[k])) good = 0; for (int t = 0; t < k && good; t++) if (it[t] == it[k]) good = 0; k++; }
            if (!good) continue;
            for (int t = 0; t < 10; t++) setbit(&used, it[t]);
            memcpy(B, z, sizeof z); ok = 1;
        }
        if (!ok) continue;
        memset(&prim, 0, sizeof prim);
        for (int c = 0; c < NI; c++) if (!getbit(&used, c)) setbit(&prim, c);
        int cnt = 0; for (int r = 0; r < ns; r++) if (disj(&smask[r], &used)) lists[0][cnt++] = r;
        for (int i = cnt - 1; i > 0; i--) { int j = rndint(i + 1); int t = lists[0][i]; lists[0][i] = lists[0][j]; lists[0][j] = t; }
        mask_t cov; memset(&cov, 0, sizeof cov); nodes = 0;
        int rs = xc(0, cnt, cov);
        if (rs >= 1000) {
            s_ok++;
            int sd = rs - 1000;
            int remorb[512] = {0}, nrem = 0;
            for (int i = 0; i < nmix; i++) if (!intarget[mixed[i]]) { remorb[mixed[i]] = 1; nrem++; }
            for (long t1 = 0; t1 < b1tries; t1++) {
                /* B1: 10 classes in 10 distinct remaining orbits */
                int z1[5]; int got = 0;
                for (int tries = 0; tries < 2000000 && !got; tries++) {
                    int z[5] = {0, 1 + rndint(V - 1), 1 + rndint(V - 1), 1 + rndint(V - 1), 1 + rndint(V - 1)}, os[10], k = 0, good = 1;
                    for (int i = 0; i < 5 && good; i++) for (int j = i + 1; j < 5 && good; j++) { int c = cl(z[j] - z[i]); if (!c || !remorb[orbof[c]]) { good = 0; break; }
                        os[k] = orbof[c]; for (int s = 0; s < k; s++) if (os[s] == os[k]) good = 0; k++; }
                    if (good) { memcpy(z1, z, sizeof z); got = 1; }
                }
                if (!got) break;
                b1_ok++;
                int left[512]; memcpy(left, remorb, sizeof left);
                for (int i = 0; i < 5; i++) for (int j = i + 1; j < 5; j++) left[orbof[cl(z1[j] - z1[i])]] = 0;
                /* B2: exhaustive over blocks meeting each of the 10 left orbits once */
                int S[1024], nS = 0;
                for (int x = 1; x < V; x++) if (left[orbof[cl(x)]]) S[nS++] = x;
                b2_try++;
                int found = 0, z2[5];
                for (int ia = 0; ia < nS && !found; ia++) { int a = S[ia];
                  for (int ib = ia + 1; ib < nS && !found; ib++) { int b = S[ib]; int ob = orbof[cl(b - a)]; if (!left[ob] || orbof[cl(b)] == orbof[cl(a)] || ob == orbof[cl(a)] || ob == orbof[cl(b)]) continue;
                    for (int ic = ib + 1; ic < nS && !found; ic++) { int c = S[ic]; int o1 = orbof[cl(c - a)], o2 = orbof[cl(c - b)]; if (!left[o1] || !left[o2]) continue;
                      for (int id = ic + 1; id < nS && !found; id++) { int d = S[id];
                        int z[5] = {0, a, b, c, d}, os[10], k = 0, good = 1;
                        for (int i = 0; i < 5 && good; i++) for (int j = i + 1; j < 5 && good; j++) { int cc = cl(z[j] - z[i]); if (!cc || !left[orbof[cc]]) { good = 0; break; }
                            os[k] = orbof[cc]; for (int s = 0; s < k; s++) if (os[s] == os[k]) good = 0; k++; }
                        if (good) { memcpy(z2, z, sizeof z); found = 1; }
                      } } } }
                if (!found) continue;
                /* assemble and check */
                int fam[64][5], nb = 0;
                for (int d = 0; d < sd; d++) memcpy(fam[nb++], sz[chosen[d]], sizeof(int) * 5);
                memcpy(fam[nb++], B, sizeof B); for (int t = 0; t < 5; t++) fam[nb][t] = mu_of[B[t]]; nb++;
                int cur1[5], cur2[5]; memcpy(cur1, z1, sizeof cur1); memcpy(cur2, z2, sizeof cur2);
                for (int i = 0; i < 13; i++) {
                    memcpy(fam[nb++], cur1, sizeof cur1); memcpy(fam[nb++], cur2, sizeof cur2);
                    for (int t = 0; t < 5; t++) { cur1[t] = nu_of[cur1[t]]; cur2[t] = nu_of[cur2[t]]; }
                }
                int count[V] = {0};
                for (int b = 0; b < nb; b++) for (int i = 0; i < 5; i++) for (int j = 0; j < 5; j++) if (i != j) count[mv(fam[b][i] - fam[b][j])]++;
                int goodf = nb == 45 && count[0] == 0;
                for (int d = 1; d < V && goodf; d++) if (count[d] != 1) goodf = 0;
                if (!goodf) { printf("INTERNAL: assembled family fails (nb=%d)\n", nb); fflush(stdout); continue; }
                char path[1024]; snprintf(path, sizeof path, "%s.sol", pre);
                FILE *fo = fopen(path, "w"); fprintf(fo, "CDF 901 5\n");
                for (int b = 0; b < nb; b++) { qsort(fam[b], 5, sizeof(int), cmpint); fprintf(fo, "%d %d %d %d %d\n", fam[b][0], fam[b][1], fam[b][2], fam[b][3], fam[b][4]); }
                fclose(fo);
                int ty[3] = {0}; for (int d = 0; d < sd; d++) ty[stype[chosen[d]]]++;
                printf("FOUND v=901 seed=%llu cfg=%lld seconds=%.2f defect: T1 %d T1' %d + pair; bulk B1/B2 after %ld B1 tries\n",
                       (unsigned long long)seed, cfg, now() - t0, ty[1], ty[2], t1 + 1);
                return 0;
            }
        }
        if (now() - tl > 30) { printf("cfg=%lld stageS_ok=%lld b1_ok=%lld b2_tries=%lld last_rows=%d nodes=%lld t=%.0f\n", cfg, s_ok, b1_ok, b2_try, cnt, nodes, now() - t0); fflush(stdout); tl = now(); }
    }
    printf("TIMEOUT seed=%llu cfg=%lld stageS_ok=%lld b1_ok=%lld b2_tries=%lld seconds=%.1f\n", (unsigned long long)seed, cfg, s_ok, b1_ok, b2_try, now() - t0);
    return 3;
}
