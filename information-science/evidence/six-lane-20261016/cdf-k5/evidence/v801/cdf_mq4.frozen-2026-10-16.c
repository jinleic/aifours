/* cdf_mq4.c (fork of cdf_mq3.c, adds the label-class feasibility filter; cdf_mq2.c stays the 621 producer) --
 * cyclic (v,5,1) difference families over Z_v = Z_m x Z_q (gcd(m,q) = 1, m,q odd): stable blocks
 * first, free pairs last.  Item/row conventions as in cdf_mq.c (mu = (1 mod m, -1 mod q)):
 *   orbit item (+-a,+-y) = classes [(a,y)], [(a,-y)]; pure item [(0,y)]; K item [(a,0)].
 *   stable rows T1 {(0,0),(a1,+-y1),(a2,+-y2)}, T1' {(0,0),(+-a1,y1),(+-a2,y2)}, T3' {(0,0),(0,f1),(0,f2),(a,y),(-a,y)},
 *   T3 {(0,0),(e1,0),(e2,0),(b,z),(b,-z)} (typemask bits 1,2,3,4).
 *   free pair {B, mu B}: B has 10 classes in 10 distinct orbit items, none fixed; covers those orbit items.
 * Stage S: randomized exact cover of all fixed items (pure + K) by stable rows whose orbit items are pairwise
 *   disjoint (orbit items are secondary columns: covered at most once).
 * Stage G: optionally place g random free pairs on still-unused orbit items.
 * Stage F: enumerate every free pair inside the remaining orbit items R (one row per class under translation,
 *   negation and mu) and search an exact cover of R (bitset Algorithm X, min column, randomized, node limit).
 * The assembled family is re-checked in-program (difference multiset in Z_v) before it is written.
 *
 * Usage: cdf_mq4 v m seed seconds outprefix typemask g nodelimitF [nodelimitS] [labelcheck]
 *   labelcheck=1: before the exact cover, require that the per-label-class counts of the remaining orbit items be a
 *   sum of r label-class profiles of 5-subsets of Z_m (necessary condition; exact DP, skipped if it exceeds a cap).
 *   g >= 0: place g random free pairs before the exact cover; g < 0: leave exactly -g free pairs to the exact cover.
 * Exit 0 found (outprefix.sol), 3 time limit.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define W 4
typedef struct { uint64_t m[W]; } mask_t;
static int v, m, q, M2, Q2, NO, NI, n, H;
static int *crt, *cls_v, *mu_of, *ya, *yy;      /* ya[z] = z mod m, yy[z] = z mod q */
static uint64_t rng;
static uint64_t rnd(void) {
    uint64_t z = (rng += 0x9E3779B97F4A7C15ULL);
    z = (z ^ (z >> 30)) * 0xBF58476D1CE4E5B9ULL;
    z = (z ^ (z >> 27)) * 0x94D049BB133111EBULL;
    return z ^ (z >> 31);
}
static int rndint(int k) { return (int)(rnd() % (uint64_t)k); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static inline int mm(int a) { a %= m; return a < 0 ? a + m : a; }
static inline int mq(int y) { y %= q; return y < 0 ? y + q : y; }
static inline int mv(int z) { z %= v; return z < 0 ? z + v : z; }
static inline void setbit(mask_t *x, int c) { x->m[c >> 6] |= 1ULL << (c & 63); }
static inline int getbit(const mask_t *x, int c) { return (int)(x->m[c >> 6] >> (c & 63) & 1); }
static inline int disj(const mask_t *a, const mask_t *b) { uint64_t x = 0; for (int w = 0; w < W; w++) x |= a->m[w] & b->m[w]; return x == 0; }
static int cmpint(const void *x, const void *y) { return *(const int *)x - *(const int *)y; }
static int zof(int a, int y) { return crt[mm(a) * q + mq(y)]; }

/* item of the class of difference d in Z_v; kind 0 orbit, 1 pure, 2 K, -1 zero */
static int item_of_d(int d, int *kind) {
    d = mv(d);
    if (d == 0) { *kind = -1; return -1; }
    int da = ya[d], dy = yy[d];
    int a = da <= M2 ? da : m - da, y = dy <= Q2 ? dy : q - dy;
    if (da == 0) { *kind = 1; return NO + (y - 1); }
    if (dy == 0) { *kind = 2; return NO + Q2 + (a - 1); }
    *kind = 0; return (a - 1) * Q2 + (y - 1);
}
static int classes_ok(const int *z) {
    int cl[10], k = 0;
    for (int i = 0; i < 5; i++) for (int j = i + 1; j < 5; j++) {
        int c = cls_v[mv(z[j] - z[i])];
        if (!c) return 0;
        for (int t = 0; t < k; t++) if (cl[t] == c) return 0;
        cl[k++] = c;
    }
    return 1;
}
/* canonical tuple under translation, negation and (if usemu) mu */
static void canon(const int *z, int *out, int usemu) {
    int best[5], cand[5], have = 0;
    for (int u = 0; u < (usemu ? 2 : 1); u++) for (int s = 0; s < 2; s++) for (int t = 0; t < 5; t++) {
        int w[5];
        for (int i = 0; i < 5; i++) { int x = u ? mu_of[z[i]] : z[i]; w[i] = s ? mv(-x) : x; }
        for (int i = 0; i < 5; i++) cand[i] = mv(w[i] - w[t]);
        qsort(cand, 5, sizeof(int), cmpint);
        if (!have || memcmp(cand, best, sizeof cand) < 0) { memcpy(best, cand, sizeof cand); have = 1; }
    }
    memcpy(out, best, sizeof best);
}

/* stable rows */
static int ns, caps; static int (*sz)[5]; static mask_t *smask; static unsigned char *stype;
static uint64_t *hset; static size_t hcap;
static int hinsert(const int *c) {
    uint64_t k = 1469598103934665603ULL;
    for (int i = 0; i < 5; i++) { k ^= (uint64_t)c[i] + 1; k *= 1099511628211ULL; }
    if (!k) k = 1;
    size_t h = k & (hcap - 1);
    while (hset[h]) { if (hset[h] == k) return 0; h = (h + 1) & (hcap - 1); }
    hset[h] = k; return 1;
}
static void add_stable(int pts[5][2], int type) {
    int z[5];
    for (int i = 0; i < 5; i++) z[i] = zof(pts[i][0], pts[i][1]);
    if (!classes_ok(z)) return;
    int it[10], kd[10], k = 0;
    for (int i = 0; i < 5; i++) for (int j = i + 1; j < 5; j++) { it[k] = item_of_d(z[j] - z[i], &kd[k]); k++; }
    for (int t = 0; t < 10; t++) { int mult = 0; for (int s = 0; s < 10; s++) if (it[s] == it[t]) mult++;
        if ((kd[t] == 0 && mult != 2) || (kd[t] != 0 && mult != 1)) return; }
    int c[5]; canon(z, c, 0);
    if (!hinsert(c)) return;
    if (ns == caps) { caps = caps ? 2 * caps : 1 << 16; sz = realloc(sz, sizeof(*sz) * caps); smask = realloc(smask, sizeof(mask_t) * caps); stype = realloc(stype, caps); }
    memcpy(sz[ns], z, sizeof z); memset(&smask[ns], 0, sizeof(mask_t));
    for (int t = 0; t < 10; t++) setbit(&smask[ns], it[t]);
    stype[ns] = (unsigned char)type; ns++;
}

/* ---------- stage S: exact cover of fixed items, orbit items secondary ---------- */
static int **slist; static int schosen[128]; static long long snodes, snodelimit; static mask_t fixedmask;
static int stage_s(int depth, int cnt, mask_t cov) {
    int done = 1;
    for (int w = 0; w < W; w++) if ((cov.m[w] & fixedmask.m[w]) != fixedmask.m[w]) done = 0;
    if (done) return depth + 1000;
    if (++snodes > snodelimit) return -1;
    int *lst = slist[depth];
    static int cc[W * 64];
    memset(cc, 0, sizeof cc);
    for (int i = 0; i < cnt; i++) { const mask_t *x = &smask[lst[i]];
        for (int w = 0; w < W; w++) { uint64_t b = x->m[w] & fixedmask.m[w]; while (b) { int c = w * 64 + __builtin_ctzll(b); cc[c]++; b &= b - 1; } } }
    int best = -1, bs = 1 << 30, ties = 0;
    for (int c = NO; c < NI; c++) {
        if (getbit(&cov, c)) continue;
        if (cc[c] < bs) { bs = cc[c]; best = c; ties = 1; } else if (cc[c] == bs && rndint(++ties) == 0) best = c;
    }
    if (bs == 0) return 0;
    int *nxt = slist[depth + 1];
    for (int i = 0; i < cnt; i++) {
        int x = lst[i];
        if (!getbit(&smask[x], best)) continue;
        int k = 0;
        for (int j = 0; j < cnt; j++) { int y = lst[j]; if (disj(&smask[x], &smask[y])) nxt[k++] = y; }
        schosen[depth] = x;
        mask_t nc = cov; for (int w = 0; w < W; w++) nc.m[w] |= smask[x].m[w];
        int r = stage_s(depth + 1, k, nc);
        if (r != 0) return r;
    }
    return 0;
}

/* ---------- label-class feasibility (necessary condition for the free part) ---------- */
static int nprof; static int prof[4096][64];
static void build_profiles(void) {
    /* distinct label-class count vectors of 5-subsets of Z_m (5 distinct labels) */
    int s[5];
    for (s[0] = 0; s[0] < m; s[0]++) for (s[1] = s[0] + 1; s[1] < m; s[1]++) for (s[2] = s[1] + 1; s[2] < m; s[2]++)
    for (s[3] = s[2] + 1; s[3] < m; s[3]++) for (s[4] = s[3] + 1; s[4] < m; s[4]++) {
        int c[64] = {0};
        for (int i = 0; i < 5; i++) for (int j = i + 1; j < 5; j++) { int d = mm(s[j] - s[i]); d = d <= M2 ? d : m - d; c[d - 1]++; }
        int dup = 0;
        for (int k = 0; k < nprof && !dup; k++) if (!memcmp(prof[k], c, sizeof(int) * M2)) dup = 1;
        if (!dup && nprof < 4096) memcpy(prof[nprof++], c, sizeof(int) * 64);
    }
}
static uint64_t *lhs; static size_t lhcap = (size_t)1 << 25;
static long long lab_fail, lab_skip;
static int label_feasible(const int *R, int r) {
    /* BFS over partial sums (componentwise <= R); state key = mixed-radix code; cap on states -> assume feasible */
    if (!lhs) lhs = malloc(sizeof(uint64_t) * lhcap);
    uint64_t radix[64], target = 0, mul = 1;
    for (int a = 0; a < M2; a++) { radix[a] = mul; target += mul * (uint64_t)R[a]; mul *= (uint64_t)(R[a] + 1); if (mul > ((uint64_t)1 << 62)) { lab_skip++; return 1; } }
    uint64_t *cur = malloc(sizeof(uint64_t) * 4), *nxt; size_t ncur = 1, cap = 4;
    cur[0] = 0;
    for (int k = 0; k < r; k++) {
        memset(lhs, 0xff, sizeof(uint64_t) * lhcap);
        size_t nn = 0, capn = 1024; nxt = malloc(sizeof(uint64_t) * capn);
        for (size_t i = 0; i < ncur; i++) {
            uint64_t s = cur[i]; int sv[64];
            for (int a = 0; a < M2; a++) sv[a] = (int)((s / radix[a]) % (uint64_t)(R[a] + 1));
            for (int p = 0; p < nprof; p++) {
                int ok = 1;
                for (int a = 0; a < M2; a++) if (sv[a] + prof[p][a] > R[a]) { ok = 0; break; }
                if (!ok) continue;
                uint64_t key = s; for (int a = 0; a < M2; a++) key += radix[a] * (uint64_t)prof[p][a];
                size_t h = (key * 0x9E3779B97F4A7C15ULL) & (lhcap - 1);
                while (lhs[h] != ~0ULL && lhs[h] != key) h = (h + 1) & (lhcap - 1);
                if (lhs[h] == key) continue;
                lhs[h] = key;
                if (nn == capn) { capn *= 2; nxt = realloc(nxt, sizeof(uint64_t) * capn); }
                nxt[nn++] = key;
                if (nn > lhcap / 2) { free(cur); free(nxt); lab_skip++; return 1; }
            }
        }
        free(cur); cur = nxt; ncur = nn; cap = capn; (void)cap;
        if (!ncur) { free(cur); return 0; }
    }
    int found = 0;
    for (size_t i = 0; i < ncur; i++) if (cur[i] == target) { found = 1; break; }
    free(cur);
    return found;
}

/* ---------- stage F: free pairs inside remaining orbit items ---------- */
static int nf, capf; static int (*fz)[5]; static mask_t *fmask; static unsigned char (*fcol)[10];
static int **flist; static int fchosen[64]; static long long fnodes, fnodelimit; static int ncolF; static int colF[1024];
static int stage_f(int depth, int cnt, mask_t cov, int ncov) {
    if (ncov == ncolF) return depth + 1000;
    if (++fnodes > fnodelimit) return -1;
    int *lst = flist[depth];
    static int cc[W * 64];
    memset(cc, 0, sizeof(int) * ncolF);
    for (int i = 0; i < cnt; i++) { const unsigned char *c = fcol[lst[i]]; for (int j = 0; j < 10; j++) cc[c[j]]++; }
    int best = -1, bs = 1 << 30, ties = 0;
    for (int c = 0; c < ncolF; c++) {
        if (getbit(&cov, c)) continue;
        if (cc[c] < bs) { bs = cc[c]; best = c; ties = 1; } else if (cc[c] == bs && rndint(++ties) == 0) best = c;
    }
    if (bs == 0) return 0;
    int *nxt = flist[depth + 1];
    for (int i = 0; i < cnt; i++) {
        int x = lst[i];
        if (!getbit(&fmask[x], best)) continue;
        int k = 0;
        for (int j = 0; j < cnt; j++) { int y = lst[j]; if (disj(&fmask[x], &fmask[y])) nxt[k++] = y; }
        fchosen[depth] = x;
        mask_t nc = cov; for (int w = 0; w < W; w++) nc.m[w] |= fmask[x].m[w];
        int r = stage_f(depth + 1, k, nc, ncov + 10);
        if (r != 0) return r;
    }
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 9) { fprintf(stderr, "usage: cdf_mq4 v m seed seconds outprefix typemask g nodelimitF [nodelimitS] [labelcheck]\n"); return 2; }
    v = atoi(argv[1]); m = atoi(argv[2]); uint64_t seed = strtoull(argv[3], 0, 10); double limit = atof(argv[4]);
    const char *pre = argv[5]; int typemask = atoi(argv[6]); int g = atoi(argv[7]); fnodelimit = atoll(argv[8]);
    snodelimit = argc > 9 ? atoll(argv[9]) : 5000000;
    int labelcheck = argc > 10 ? atoi(argv[10]) : 0;
    if (v % m) { fprintf(stderr, "m must divide v\n"); return 2; }
    q = v / m;
    { int a = m, b = q; while (b) { int t = a % b; a = b; b = t; } if (a != 1 || m % 2 == 0 || q % 2 == 0) { fprintf(stderr, "need coprime odd m,q\n"); return 2; } }
    if ((v - 1) % 20) { fprintf(stderr, "v != 1 mod 20\n"); return 2; }
    n = (v - 1) / 20; H = (v - 1) / 2; M2 = (m - 1) / 2; Q2 = (q - 1) / 2; NO = M2 * Q2; NI = NO + Q2 + M2;
    if (NI > W * 64 || NO > W * 64) { fprintf(stderr, "too many items\n"); return 2; }
    rng = seed * 0x2545F4914F6CDD1DULL + 1357911;
    crt = malloc(sizeof(int) * m * q); ya = malloc(sizeof(int) * v); yy = malloc(sizeof(int) * v); mu_of = malloc(sizeof(int) * v);
    for (int z = 0; z < v; z++) { crt[(z % m) * q + (z % q)] = z; ya[z] = z % m; yy[z] = z % q; }
    for (int z = 0; z < v; z++) mu_of[z] = zof(ya[z], -yy[z]);
    cls_v = malloc(sizeof(int) * v);
    for (int d = 0; d < v; d++) cls_v[d] = d <= H ? d : v - d;
    hcap = 1 << 24; hset = calloc(hcap, sizeof(uint64_t));
    double t0 = now();
    if (typemask >> 1 & 1) for (int a1 = 1; a1 < m; a1++) for (int a2 = 1; a2 < m; a2++) if (a1 != a2)
        for (int y1 = 1; y1 < q; y1++) for (int y2 = 1; y2 < q; y2++) { int p[5][2] = {{0, 0}, {a1, y1}, {a1, mq(-y1)}, {a2, y2}, {a2, mq(-y2)}}; add_stable(p, 1); }
    int n1 = ns;
    if (typemask >> 2 & 1) for (int a1 = 1; a1 < m; a1++) for (int a2 = 1; a2 < m; a2++)
        for (int y1 = 1; y1 < q; y1++) for (int y2 = 1; y2 < q; y2++) { int p[5][2] = {{0, 0}, {a1, y1}, {mm(-a1), y1}, {a2, y2}, {mm(-a2), y2}}; add_stable(p, 2); }
    int n2 = ns;
    if (typemask >> 3 & 1) for (int f1 = 1; f1 < q; f1++) for (int f2 = f1 + 1; f2 < q; f2++) for (int a = 1; a < m; a++) for (int y = 0; y < q; y++) {
        int p[5][2] = {{0, 0}, {0, f1}, {0, f2}, {a, y}, {mm(-a), y}}; add_stable(p, 3); }
    int n3 = ns;
    if (typemask >> 4 & 1) for (int e1 = 1; e1 < m; e1++) for (int e2 = e1 + 1; e2 < m; e2++) for (int b = 0; b < m; b++) for (int z = 1; z < q; z++) {
        int p[5][2] = {{0, 0}, {e1, 0}, {e2, 0}, {b, z}, {b, mq(-z)}}; add_stable(p, 4); }
    memset(&fixedmask, 0, sizeof fixedmask);
    for (int c = NO; c < NI; c++) setbit(&fixedmask, c);
    slist = calloc(130, sizeof(int *)); for (int d = 0; d < 130; d++) slist[d] = malloc(sizeof(int) * (ns + 1));
    flist = calloc(70, sizeof(int *));
    printf("start v=%d m=%d q=%d n=%d items=%d (orbit %d pure %d K %d) stable rows T1=%d T1'=%d T3'=%d T3=%d seed=%llu g=%d nodelimitF=%lld nodelimitS=%lld (setup %.1fs)\n",
           v, m, q, n, NI, NO, Q2, M2, n1, n2 - n1, n3 - n2, ns - n3, (unsigned long long)seed, g, fnodelimit, snodelimit, now() - t0);
    fflush(stdout);
    long long attempts = 0, s_fail = 0, f_fail_ex = 0, f_fail_lim = 0;
    if (labelcheck) { build_profiles(); printf("label profiles: %d distinct (m=%d)\n", nprof, m); fflush(stdout); }
    double tl = now();
    int S[4096];
    while (now() - t0 < limit) {
        attempts++;
        /* stage S */
        for (int i = 0; i < ns; i++) slist[0][i] = i;
        for (int i = ns - 1; i > 0; i--) { int j = rndint(i + 1); int t = slist[0][i]; slist[0][i] = slist[0][j]; slist[0][j] = t; }
        mask_t cov; memset(&cov, 0, sizeof cov);
        snodes = 0;
        int rs = stage_s(0, ns, cov);
        if (rs < 1000) { s_fail++; continue; }
        int sdepth = rs - 1000;
        mask_t used; memset(&used, 0, sizeof used);
        for (int d = 0; d < sdepth; d++) for (int w = 0; w < W; w++) used.m[w] |= smask[schosen[d]].m[w];
        int orb_left = 0; for (int c = 0; c < NO; c++) if (!getbit(&used, c)) orb_left++;
        if (orb_left % 10) { s_fail++; continue; }
        int fneed = orb_left / 10;
        if (sdepth + 2 * fneed != n) { printf("INTERNAL: block count %d+2*%d != %d\n", sdepth, fneed, n); return 1; }
        if (g == -999) {
            /* dump mode: write a cdf_ls template (stable blocks constant, fneed free mu-pairs) and stop */
            char path[1024]; snprintf(path, sizeof path, "%s.tpl", pre);
            FILE *ft = fopen(path, "w");
            int muv = zof(1, -1);
            fprintf(ft, "%d 5 %d %d\n", v, muv, sdepth + fneed);
            for (int d = 0; d < sdepth; d++) { fprintf(ft, "1"); for (int t = 0; t < 5; t++) fprintf(ft, " C%d", sz[schosen[d]][t]); fprintf(ft, "\n"); }
            for (int i = 0; i < fneed; i++) fprintf(ft, "2 C0 F1 F1 F1 F1\n");
            fclose(ft);
            printf("DUMPED stable=%d free_pairs=%d template=%s\n", sdepth, fneed, path);
            return 0;
        }
        /* stage G: random free pairs */
        int gz[64][5], gplaced = 0, tries = 0;
        int gwant = g >= 0 ? g : (fneed + g > 0 ? fneed + g : 0);
        while (gplaced < gwant && gplaced < fneed && tries < 2000000) {
            tries++;
            int z[5], ok = 1;
            z[0] = 0; for (int i = 1; i < 5; i++) z[i] = rndint(v);
            if (!classes_ok(z)) continue;
            int it[10], kd;
            for (int i = 0, k = 0; i < 5 && ok; i++) for (int j = i + 1; j < 5 && ok; j++) {
                it[k] = item_of_d(z[j] - z[i], &kd);
                if (kd != 0 || getbit(&used, it[k])) ok = 0;
                for (int t = 0; t < k && ok; t++) if (it[t] == it[k]) ok = 0;
                k++;
            }
            if (!ok) continue;
            for (int t = 0; t < 10; t++) setbit(&used, it[t]);
            memcpy(gz[gplaced++], z, sizeof z);
        }
        if (gplaced < gwant && gplaced < fneed) { s_fail++; continue; }
        int r = fneed - gplaced;
        if (labelcheck && r > 0) {
            int Rv[64] = {0};
            for (int c = 0; c < NO; c++) if (!getbit(&used, c)) Rv[c / Q2]++;
            if (!label_feasible(Rv, r)) {
                lab_fail++;
                if (now() - tl > 30) { printf("attempts=%lld s_fail=%lld lab_fail=%lld lab_skip=%lld t=%.0f\n", attempts, s_fail, lab_fail, lab_skip, now() - t0); fflush(stdout); tl = now(); }
                continue;
            }
        }
        /* stage F rows */
        ncolF = 0;
        for (int c = 0; c < NO; c++) colF[c] = getbit(&used, c) ? -1 : ncolF++;
        if (ncolF != 10 * r) { printf("INTERNAL: ncolF\n"); return 1; }
        int nS = 0;
        for (int x = 1; x < v; x++) { int kd, it = item_of_d(x, &kd); if (kd == 0 && !getbit(&used, it)) S[nS++] = x; }
        nf = 0;
        for (int ia = 0; ia < nS; ia++) { int a = S[ia];
          for (int ib = ia + 1; ib < nS; ib++) { int b = S[ib]; int kd, t1 = item_of_d(b - a, &kd); if (kd != 0 || getbit(&used, t1)) continue;
            for (int ic = ib + 1; ic < nS; ic++) { int c = S[ic]; int t2 = item_of_d(c - a, &kd); if (kd != 0 || getbit(&used, t2)) continue;
              int t3 = item_of_d(c - b, &kd); if (kd != 0 || getbit(&used, t3)) continue;
              for (int id = ic + 1; id < nS; id++) { int d = S[id];
                int t4 = item_of_d(d - a, &kd); if (kd != 0 || getbit(&used, t4)) continue;
                int t5 = item_of_d(d - b, &kd); if (kd != 0 || getbit(&used, t5)) continue;
                int t6 = item_of_d(d - c, &kd); if (kd != 0 || getbit(&used, t6)) continue;
                int z[5] = {0, a, b, c, d};
                int it[10], k = 0, ok = 1;
                for (int i = 0; i < 5 && ok; i++) for (int j = i + 1; j < 5 && ok; j++) { it[k] = item_of_d(z[j] - z[i], &kd);
                    for (int t = 0; t < k; t++) if (it[t] == it[k]) { ok = 0; break; } k++; }
                if (!ok || !classes_ok(z)) continue;
                int cn[5]; canon(z, cn, 1);
                if (memcmp(cn, z, sizeof z)) continue;
                if (nf == capf) { capf = capf ? 2 * capf : 1 << 16; fz = realloc(fz, sizeof(*fz) * capf); fmask = realloc(fmask, sizeof(mask_t) * capf); fcol = realloc(fcol, sizeof(*fcol) * capf); }
                memcpy(fz[nf], z, sizeof z); memset(&fmask[nf], 0, sizeof(mask_t));
                for (int t = 0; t < 10; t++) { fcol[nf][t] = (unsigned char)colF[it[t]]; setbit(&fmask[nf], colF[it[t]]); }
                nf++;
              } } } }
        for (int d = 0; d <= r + 1; d++) flist[d] = realloc(flist[d], sizeof(int) * (nf + 1));
        for (int i = 0; i < nf; i++) flist[0][i] = i;
        for (int i = nf - 1; i > 0; i--) { int j = rndint(i + 1); int t = flist[0][i]; flist[0][i] = flist[0][j]; flist[0][j] = t; }
        mask_t fc; memset(&fc, 0, sizeof fc);
        fnodes = 0;
        int rf = r == 0 ? 1000 : stage_f(0, nf, fc, 0);
        if (rf >= 1000) {
            int fam[128][5], nb = 0;
            for (int d = 0; d < sdepth; d++) memcpy(fam[nb++], sz[schosen[d]], sizeof(int) * 5);
            for (int i = 0; i < gplaced; i++) { memcpy(fam[nb++], gz[i], sizeof(int) * 5); for (int t = 0; t < 5; t++) fam[nb][t] = mu_of[gz[i][t]]; nb++; }
            for (int i = 0; i < r; i++) { memcpy(fam[nb++], fz[fchosen[i]], sizeof(int) * 5); for (int t = 0; t < 5; t++) fam[nb][t] = mu_of[fz[fchosen[i]][t]]; nb++; }
            int *count = calloc(v, sizeof(int));
            for (int b = 0; b < nb; b++) for (int i = 0; i < 5; i++) for (int j = 0; j < 5; j++) if (i != j) count[mv(fam[b][i] - fam[b][j])]++;
            int good = nb == n && count[0] == 0;
            for (int d = 1; d < v && good; d++) if (count[d] != 1) good = 0;
            free(count);
            if (!good) { printf("INTERNAL: assembled family fails (nb=%d)\n", nb); fflush(stdout); continue; }
            char path[1024]; snprintf(path, sizeof path, "%s.sol", pre);
            FILE *fo = fopen(path, "w");
            fprintf(fo, "CDF %d 5\n", v);
            for (int b = 0; b < nb; b++) { qsort(fam[b], 5, sizeof(int), cmpint); fprintf(fo, "%d %d %d %d %d\n", fam[b][0], fam[b][1], fam[b][2], fam[b][3], fam[b][4]); }
            fclose(fo);
            int types[8] = {0}; for (int d = 0; d < sdepth; d++) types[stype[schosen[d]]]++;
            printf("FOUND v=%d seed=%llu attempts=%lld seconds=%.2f stable=%d (T1 %d T1' %d T3' %d T3 %d) free_pairs=%d (random %d, xc %d) rowsF=%d fnodes=%lld\n",
                   v, (unsigned long long)seed, attempts, now() - t0, sdepth, types[1], types[2], types[3], types[4], fneed, gplaced, r, nf, fnodes);
            return 0;
        } else if (rf < 0) f_fail_lim++; else f_fail_ex++;
        if (now() - tl > 30) {
            printf("attempts=%lld s_fail=%lld lab_fail=%lld lab_skip=%lld f_exhausted=%lld f_limit=%lld last: stable=%d free_needed=%d xc_r=%d rowsF=%d fnodes=%lld t=%.0f\n",
                   attempts, s_fail, lab_fail, lab_skip, f_fail_ex, f_fail_lim, sdepth, fneed, r, nf, fnodes, now() - t0);
            fflush(stdout); tl = now();
        }
    }
    printf("TIMEOUT v=%d seed=%llu attempts=%lld s_fail=%lld lab_fail=%lld f_exhausted=%lld f_limit=%lld seconds=%.2f\n", v,
           (unsigned long long)seed, attempts, s_fail, lab_fail, f_fail_ex, f_fail_lim, now() - t0);
    return 3;
}
