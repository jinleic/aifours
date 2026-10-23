/* indep_full_cdf.c -- full enumeration of cyclic (v,k,1) difference families for small v (classes <= 64),
 * written independently of o3_models.c, to cross-check its order-3 counts.
 *
 * Blocks: every k-subset containing 0, identified with its lexicographically least translate
 * (canonical form); kept if its k(k-1)/2 classes min(d, v-d) are distinct. Families: exact covers of
 * all (v-1)/2 classes by t such class sets (bitmask, branching on the class with the fewest
 * compatible blocks), each family found once as a set of canonical blocks.
 * For a unit w of order 3 (argument), counts the families mapped to themselves by x -> w x and splits
 * them by the number of blocks fixed (up to translation).
 * usage: indep_full_cdf v k w
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

static int v, k, t, nc, w;
static int nb = 0, cap = 0;
static int (*bel)[8];
static uint64_t *bm;
static long long nfam = 0, ninv = 0, typecount[16];
static int chosen[16];

static int cmpint(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static void canon(const int *B, int *out) {
    int best[8], tmp[8], have = 0;
    for (int s = 0; s < k; s++) {
        for (int a = 0; a < k; a++) tmp[a] = ((B[a] - B[s]) % v + v) % v;
        qsort(tmp, k, sizeof(int), cmpint);
        if (!have || memcmp(tmp, best, sizeof(int) * k) < 0) { memcpy(best, tmp, sizeof(int) * k); have = 1; }
    }
    memcpy(out, best, sizeof(int) * k);
}
static int find_block(const int *cb) { /* bel[] is in lexicographic generation order */
    int lo = 0, hi = nb - 1;
    while (lo <= hi) {
        int mid = (lo + hi) / 2, c = 0;
        for (int a = 0; a < k && !c; a++) c = (bel[mid][a] > cb[a]) - (bel[mid][a] < cb[a]);
        if (!c) return mid;
        if (c < 0) lo = mid + 1; else hi = mid - 1;
    }
    return -1;
}
static void on_family(void) {
    nfam++;
    int img[16], fixed = 0;
    for (int j = 0; j < t; j++) {
        int B[8], cb[8];
        for (int a = 0; a < k; a++) B[a] = (int)((long long)bel[chosen[j]][a] * w % v);
        canon(B, cb);
        img[j] = find_block(cb);
        if (img[j] == chosen[j]) fixed++;
    }
    int ok = 1;
    for (int j = 0; j < t && ok; j++) { int f = 0; for (int q = 0; q < t; q++) if (img[j] == chosen[q]) f = 1; ok = f; }
    if (ok) { ninv++; typecount[fixed]++; }
}
static int nw;
static uint64_t *cbits; /* cbits[c*nw + q]: bitset of blocks containing class c */
static void xc(uint64_t covered, int depth, const uint64_t *compat) {
    uint64_t full = (nc == 64) ? ~0ULL : ((1ULL << nc) - 1);
    if (covered == full) { if (depth == t) on_family(); return; }
    if (depth == t) return;
    int bestc = -1; long bestn = 1L << 40;
    for (int c = 0; c < nc; c++) if (!((covered >> c) & 1)) {
        long n = 0; const uint64_t *cc = cbits + (size_t)c * nw;
        for (int q = 0; q < nw; q++) n += __builtin_popcountll(compat[q] & cc[q]);
        if (n < bestn) { bestn = n; bestc = c; }
    }
    if (bestn == 0) return;
    uint64_t *nx = malloc(sizeof(uint64_t) * nw);
    const uint64_t *cb = cbits + (size_t)bestc * nw;
    for (int q = 0; q < nw; q++) {
        uint64_t word = compat[q] & cb[q];
        while (word) {
            int i = q * 64 + __builtin_ctzll(word); word &= word - 1;
            for (int r = 0; r < nw; r++) nx[r] = compat[r];
            for (int c = 0; c < nc; c++) if ((bm[i] >> c) & 1) { const uint64_t *x = cbits + (size_t)c * nw; for (int r = 0; r < nw; r++) nx[r] &= ~x[r]; }
            chosen[depth] = i;
            xc(covered | bm[i], depth + 1, nx);
        }
    }
    free(nx);
}
int main(int argc, char **argv) {
    v = atoi(argv[1]); k = atoi(argv[2]); w = atoi(argv[3]);
    t = (v - 1) / (k * (k - 1)); nc = (v - 1) / 2;
    if (nc > 64 || k > 8) return 2;
    cap = 1 << 20; bel = malloc(sizeof(*bel) * cap); bm = malloc(sizeof(uint64_t) * cap);
    int B[8]; B[0] = 0;
    /* enumerate k-subsets {0 < x1 < ... < x_{k-1}} */
    int idx[8];
    for (int a = 0; a < k - 1; a++) idx[a] = a + 1;
    while (1) {
        for (int a = 0; a < k - 1; a++) B[a + 1] = idx[a];
        uint64_t m = 0; int ok = 1;
        for (int a = 0; a < k && ok; a++) for (int b = a + 1; b < k && ok; b++) {
            int d = B[b] - B[a]; int c = (d < v - d ? d : v - d) - 1;
            if ((m >> c) & 1) ok = 0; else m |= 1ULL << c;
        }
        if (ok) {
            int cb[8]; canon(B, cb);
            if (!memcmp(cb, B, sizeof(int) * k)) { memcpy(bel[nb], cb, sizeof(int) * k); bm[nb] = m; nb++; }
        }
        int a = k - 2;
        while (a >= 0 && idx[a] == v - (k - 1 - a)) a--;
        if (a < 0) break;
        idx[a]++;
        for (int b = a + 1; b < k - 1; b++) idx[b] = idx[b - 1] + 1;
    }
    nw = (nb + 63) / 64;
    cbits = calloc((size_t)nc * nw, sizeof(uint64_t));
    for (int i = 0; i < nb; i++) for (int c = 0; c < nc; c++) if ((bm[i] >> c) & 1) cbits[(size_t)c * nw + i / 64] |= 1ULL << (i % 64);
    uint64_t *all = calloc(nw, sizeof(uint64_t));
    for (int i = 0; i < nb; i++) all[i / 64] |= 1ULL << (i % 64);
    xc(0, 0, all);
    printf("{\"v\":%d,\"k\":%d,\"t\":%d,\"w\":%d,\"n_canonical_good_blocks\":%d,\"n_families\":%lld,\"n_w_invariant\":%lld,\"by_fixed_blocks\":{", v, k, t, w, nb, nfam, ninv);
    int first = 1;
    for (int f = 0; f <= t; f++) if (typecount[f]) { printf("%s\"%d\":%lld", first ? "" : ",", f, typecount[f]); first = 0; }
    printf("}}\n");
    return 0;
}
