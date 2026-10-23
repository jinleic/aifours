/* gpairs.c -- enumerate pairs of (3,2,0)-pattern blocks in Z_3 x Z_p whose mixed differences jointly form complete
 * +- orbits (used by cdf_hyb3p mode 2).
 *
 * G = {(0,0),(0,u2),(0,u3),(1,w1),(1,w2)}: oriented label-0 -> label-1 differences M(G) = {w_j - u_i} (6 values in
 * Z_p); pure differences {u2, u3, u3-u2, w2-w1}.  Internal pairs: x, -x both in M(G).  Loose values L(G) = M(G)
 * minus internal pairs.  A pair (G, G') is "jointly closed" iff L(G') = -L(G) as sets; then M(G) u M(G') is a union
 * of 6 complete orbits {y,-y}.  Valid pairs additionally need 12 distinct values, 6 distinct orbits, and 8 distinct
 * pure classes.  Records with |L| = 2 or 4 are sorted by key and matched by binary search.
 * Usage: gpairs p maxout outfile   (writes lines "u2 u3 w1 w2 u2' u3' w1' w2'")
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static int p, P2;
static inline int mp(int a) { a %= p; return a < 0 ? a + p : a; }
static inline int cl(int a) { a = mp(a); return a <= P2 ? a : p - a; }
typedef struct { uint64_t key; uint32_t par; uint32_t len; } rec_t;   /* par packs u2,u3 (as 2x8 bits?) -> use 2 arrays */
typedef struct { uint64_t key; uint16_t u2, u3, w1, w2; uint8_t len; } R;
static int cmpR(const void *a, const void *b) {
    const R *x = a, *y = b;
    if (x->len != y->len) return x->len < y->len ? -1 : 1;
    return x->key < y->key ? -1 : x->key > y->key;
}
static int cmpi(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static uint64_t pack(const int *v, int n) { uint64_t k = 0; for (int i = 0; i < n; i++) k = k * 1024 + (uint64_t)v[i]; return k; }

/* compute M, check validity, loose set; returns |L| or -1 */
static int analyse(int u2, int u3, int w1, int w2, int *L, int *Mv, int *pure) {
    int u[3] = {0, u2, u3}, w[2] = {w1, w2}, m = 0;
    for (int j = 0; j < 2; j++) for (int i = 0; i < 3; i++) Mv[m++] = mp(w[j] - u[i]);
    for (int i = 0; i < 6; i++) { if (Mv[i] == 0) return -1; for (int j = i + 1; j < 6; j++) if (Mv[i] == Mv[j]) return -1; }
    pure[0] = cl(u2); pure[1] = cl(u3); pure[2] = cl(u3 - u2); pure[3] = cl(w2 - w1);
    for (int i = 0; i < 4; i++) { if (!pure[i]) return -1; for (int j = i + 1; j < 4; j++) if (pure[i] == pure[j]) return -1; }
    int used[6] = {0}, nl = 0;
    for (int i = 0; i < 6; i++) for (int j = i + 1; j < 6; j++) if (!used[i] && !used[j] && mp(Mv[i] + Mv[j]) == 0) used[i] = used[j] = 1;
    for (int i = 0; i < 6; i++) if (!used[i]) L[nl++] = Mv[i];
    qsort(L, nl, sizeof(int), cmpi);
    return nl;
}

int main(int argc, char **argv) {
    if (argc < 4) { fprintf(stderr, "usage: gpairs p maxout outfile [keep_permille]\n"); return 2; }
    p = atoi(argv[1]); long maxout = atol(argv[2]); P2 = (p - 1) / 2;
    int keep = argc > 4 ? atoi(argv[4]) : 1000;          /* deterministic thinning of valid pairs */
    uint64_t hs = 0x9E3779B97F4A7C15ULL;
    size_t cap = 1 << 20, n = 0;
    R *a = malloc(sizeof(R) * cap);
    for (int u2 = 1; u2 < p; u2++) for (int u3 = u2 + 1; u3 < p; u3++)
        for (int w1 = 0; w1 < p; w1++) for (int w2 = w1 + 1; w2 < p; w2++) {
            int L[6], M[6], pu[4];
            int nl = analyse(u2, u3, w1, w2, L, M, pu);
            if (nl != 2 && nl != 4) continue;
            if (n == cap) { cap *= 2; a = realloc(a, sizeof(R) * cap); }
            a[n].key = pack(L, nl); a[n].len = (uint8_t)nl; a[n].u2 = u2; a[n].u3 = u3; a[n].w1 = w1; a[n].w2 = w2; n++;
        }
    qsort(a, n, sizeof(R), cmpR);
    fprintf(stderr, "records=%zu\n", n);
    FILE *f = fopen(argv[3], "w");
    long out = 0, matches = 0;
    for (size_t i = 0; i < n && out < maxout; i++) {
        int L[6], M[6], pu[4];
        int nl = analyse(a[i].u2, a[i].u3, a[i].w1, a[i].w2, L, M, pu);
        int NL[6];
        for (int t = 0; t < nl; t++) NL[t] = mp(-L[t]);
        qsort(NL, nl, sizeof(int), cmpi);
        R probe; probe.key = pack(NL, nl); probe.len = (uint8_t)nl;
        /* binary search lower bound */
        size_t lo = 0, hi = n;
        while (lo < hi) { size_t mid = (lo + hi) / 2; if (cmpR(&a[mid], &probe) < 0) lo = mid + 1; else hi = mid; }
        for (size_t j = lo; j < n && a[j].len == probe.len && a[j].key == probe.key; j++) {
            if (j <= i) continue;                       /* each unordered pair once */
            matches++;
            int L2[6], M2[6], pu2[4];
            analyse(a[j].u2, a[j].u3, a[j].w1, a[j].w2, L2, M2, pu2);
            /* 12 distinct values, 6 distinct orbits, 8 distinct pure classes */
            int all[12], ok = 1;
            for (int t = 0; t < 6; t++) { all[t] = M[t]; all[6 + t] = M2[t]; }
            for (int s = 0; s < 12 && ok; s++) for (int t = s + 1; t < 12; t++) if (all[s] == all[t]) { ok = 0; break; }
            int orbs[12], no = 0;
            for (int s = 0; s < 12 && ok; s++) { int c = cl(all[s]), seen = 0; for (int t = 0; t < no; t++) if (orbs[t] == c) seen++; if (!seen) orbs[no++] = c; }
            if (ok && no != 6) ok = 0;
            int pp[8];
            for (int t = 0; t < 4; t++) { pp[t] = pu[t]; pp[4 + t] = pu2[t]; }
            for (int s = 0; s < 8 && ok; s++) for (int t = s + 1; t < 8; t++) if (pp[s] == pp[t]) { ok = 0; break; }
            if (!ok) continue;
            hs ^= hs << 13; hs ^= hs >> 7; hs ^= hs << 17;
            if ((int)(hs % 1000) >= keep) continue;
            fprintf(f, "%d %d %d %d %d %d %d %d\n", a[i].u2, a[i].u3, a[i].w1, a[i].w2, a[j].u2, a[j].u3, a[j].w1, a[j].w2);
            if (++out >= maxout) break;
        }
    }
    fclose(f);
    fprintf(stderr, "matches=%ld valid_written=%ld\n", matches, out);
    return 0;
}
