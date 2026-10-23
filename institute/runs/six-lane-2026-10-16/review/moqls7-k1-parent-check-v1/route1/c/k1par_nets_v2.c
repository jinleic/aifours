/* k1par_nets_v2.c (= k1par_nets.c + progress lines every 2^20 squares) — parent-side independent code (moqls7-k1-parent-check-v1). Written from Egan–Wanless
 * arXiv:1406.3681v2 definitions (reduced list: every square has its first row in order and the first square has its
 * first column in order; paratopism = S_7 wr S_4 acting on the 49x4 orthogonal array). No lane code used.
 *
 * Input (stdin): nets, each 196 integers = for points q=0..48 the labels of the 4 parallel classes.
 * Part 1 (per net): for every frame F = (class order sig in S_4, origin point p, ordering of the 6 other points of the
 *   row line through p) build the reduced list (L1,L2) (row labels via the first column of L1) and the point->cell map.
 *   Validate each list (Latin, orthogonal, reduced). Count distinct lists (orbit size). Independently count the frames
 *   whose induced point map phi_F = C_F^{-1} o C_F0 is an explicit net automorphism (maps every line to a line, classes
 *   bijectively). Orbit-stabiliser: orbit * |Aut| must be 24*49*720 = 846720. Canonical form = least list.
 * Part 2 (mode "full"): enumerate ALL reduced Latin squares L1 of order 7 (first row and first column in order), all
 *   their transversals, and all partitions of the 49 cells into 7 disjoint transversals (= all L2 with first row in order
 *   orthogonal to L1). Each (L1,L2) is a reduced list of 2-MOLS(7). Look each up in the union of the orbits of Part 1.
 * Output: text lines, see printf formats.
 * Build: clang -O2 -o k1par_nets k1par_nets.c
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define NP 49
#define KL 98
#define NFR 846720L

static int P4[24][4], P6[720][6];
static int np4 = 0, np6 = 0;

static void gen4(int *a, int k, int used) {
    if (k == 4) { memcpy(P4[np4++], a, 4 * sizeof(int)); return; }
    for (int v = 0; v < 4; v++) if (!(used >> v & 1)) { a[k] = v; gen4(a, k + 1, used | 1 << v); }
}
static void gen6(int *a, int k, int used) {
    if (k == 6) { memcpy(P6[np6++], a, 6 * sizeof(int)); return; }
    for (int v = 0; v < 6; v++) if (!(used >> v & 1)) { a[k] = v; gen6(a, k + 1, used | 1 << v); }
}

static int cmpkey(const void *a, const void *b) { return memcmp(a, b, KL); }

/* Build list for frame; returns 0 on internal inconsistency. cell[q] = 7r+c. */
static int frame_list(int net[NP][4], const int *sig, int p, const int *o6, uint8_t *key, int *cell) {
    int rc = sig[0], cc = sig[1], ac = sig[2], bc = sig[3];
    int others[6], n = 0;
    for (int q = 0; q < NP; q++) if (q != p && net[q][rc] == net[p][rc]) { if (n == 6) return 0; others[n++] = q; }
    if (n != 6) return 0;
    int line0[7]; line0[0] = p;
    for (int i = 0; i < 6; i++) line0[1 + i] = others[o6[i]];
    int colL[7], aL[7], bL[7], rowL[7];
    for (int i = 0; i < 7; i++) colL[i] = aL[i] = bL[i] = rowL[i] = -1;
    for (int i = 0; i < 7; i++) {
        int q = line0[i];
        if (colL[net[q][cc]] != -1 || aL[net[q][ac]] != -1 || bL[net[q][bc]] != -1) return 0;
        colL[net[q][cc]] = i; aL[net[q][ac]] = i; bL[net[q][bc]] = i;
    }
    for (int q = 0; q < NP; q++) if (net[q][cc] == net[p][cc]) {
        if (rowL[net[q][rc]] != -1) return 0;
        rowL[net[q][rc]] = aL[net[q][ac]];
    }
    int seen = 0; uint64_t cellsUsed = 0;
    for (int i = 0; i < 7; i++) if (rowL[i] < 0) return 0; else seen |= 1 << rowL[i];
    if (seen != 0x7f) return 0;
    for (int q = 0; q < NP; q++) {
        int r = rowL[net[q][rc]], c = colL[net[q][cc]];
        int x = 7 * r + c;
        if (cellsUsed >> x & 1) return 0;
        cellsUsed |= 1ULL << x;
        cell[q] = x;
        key[x] = (uint8_t)aL[net[q][ac]];
        key[49 + x] = (uint8_t)bL[net[q][bc]];
    }
    return 1;
}

/* validate: L1, L2 Latin; orthogonal; L1 row0 = id, col0 = id; L2 row0 = id */
static int valid_reduced(const uint8_t *k) {
    for (int s = 0; s < 2; s++) {
        const uint8_t *L = k + 49 * s;
        for (int r = 0; r < 7; r++) { int m1 = 0, m2 = 0; for (int c = 0; c < 7; c++) { m1 |= 1 << L[7*r+c]; m2 |= 1 << L[7*c+r]; } if (m1 != 0x7f || m2 != 0x7f) return 0; }
        for (int c = 0; c < 7; c++) if (L[c] != c) return 0;
    }
    for (int r = 0; r < 7; r++) if (k[7*r] != r) return 0;
    uint64_t pairs = 0;
    for (int x = 0; x < 49; x++) { int t = 7 * k[x] + k[49 + x]; if (pairs >> t & 1) return 0; pairs |= 1ULL << t; }
    return 1;
}

/* explicit automorphism test of point permutation phi */
static int is_aut(int net[NP][4], const int *phi) {
    int used = 0;
    for (int c = 0; c < 4; c++) {
        int target = -1;
        for (int b = 0; b < 7; b++) {
            int first = -1, cnt = 0, pts[7];
            for (int q = 0; q < NP; q++) if (net[q][c] == b) pts[cnt++] = phi[q];
            if (cnt != 7) return 0;
            /* the 7 image points must share a label in one class d */
            int d0 = -1;
            for (int d = 0; d < 4; d++) {
                int ok = 1;
                for (int i = 1; i < 7; i++) if (net[pts[i]][d] != net[pts[0]][d]) { ok = 0; break; }
                if (ok) { if (d0 != -1) return 0; d0 = d; }
            }
            if (d0 < 0) return 0;
            if (target == -1) target = d0; else if (target != d0) return 0;
            (void)first;
        }
        if (used >> target & 1) return 0;
        used |= 1 << target;
    }
    return used == 0xf;
}

static int nets[16][NP][4];
static uint8_t *orb[16]; static long orbn[16];
static uint8_t *uni; static int *unicls; static long unin = 0;
static uint32_t *hits;

/* ---------------- Part 2 ---------------- */
static uint8_t L[49];
static int rowU[7], colU[7];
static long nLS = 0, nL1withMate = 0, nLists = 0, nUnlisted = 0, nTransTotal = 0;
static uint64_t T[7][256]; static int nT[7];
static long hitcls[16];

static void found_list(uint8_t *k) {
    nLists++;
    long lo = 0, hi = unin - 1, pos = -1;
    while (lo <= hi) {
        long mid = (lo + hi) / 2;
        int c = memcmp(uni + KL * mid, k, KL);
        if (c == 0) { pos = mid; break; }
        if (c < 0) lo = mid + 1; else hi = mid - 1;
    }
    if (pos < 0) {
        nUnlisted++;
        if (nUnlisted <= 20) { printf("UNLISTED "); for (int i = 0; i < KL; i++) putchar('0' + k[i]); putchar('\n'); }
        return;
    }
    hits[pos]++;
    hitcls[unicls[pos]]++;
}

static int chosen[7];
static void cover(int g, uint64_t used) {
    if (g == 7) {
        uint8_t k[KL];
        memcpy(k, L, 49);
        for (int t = 0; t < 7; t++) { uint64_t m = T[t][chosen[t]]; for (int x = 0; x < 49; x++) if (m >> x & 1) k[49 + x] = (uint8_t)t; }
        found_list(k);
        return;
    }
    for (int i = 0; i < nT[g]; i++) if (!(T[g][i] & used)) { chosen[g] = i; cover(g + 1, used | T[g][i]); }
}

static void trans(int r, int cols, int syms, uint64_t mask, int c0) {
    if (r == 7) { if (nT[c0] >= 256) { fprintf(stderr, "overflow\n"); exit(2); } T[c0][nT[c0]++] = mask; nTransTotal++; return; }
    for (int c = 0; c < 7; c++) {
        if (cols >> c & 1) continue;
        int s = L[7 * r + c];
        if (syms >> s & 1) continue;
        trans(r + 1, cols | 1 << c, syms | 1 << s, mask | 1ULL << (7 * r + c), r == 0 ? c : c0);
    }
}

static void process_square(void) {
    nLS++;
    if ((nLS & ((1L << 20) - 1)) == 0) { printf("progress squares %ld lists %ld unlisted %ld cpu_s %.1f\n", nLS, nLists, nUnlisted, (double)clock() / CLOCKS_PER_SEC); fflush(stdout); }
    for (int i = 0; i < 7; i++) nT[i] = 0;
    trans(0, 0, 0, 0, 0);
    for (int i = 0; i < 7; i++) if (nT[i] == 0) return;
    long before = nLists;
    cover(0, 0);
    if (nLists > before) nL1withMate++;
}

static void fill(int idx) {
    if (idx == 36) { process_square(); return; }
    int r = 1 + idx / 6, c = 1 + idx % 6;
    int avail = 0x7f & ~rowU[r] & ~colU[c];
    while (avail) {
        int s = __builtin_ctz(avail); avail &= avail - 1;
        L[7 * r + c] = (uint8_t)s; rowU[r] |= 1 << s; colU[c] |= 1 << s;
        fill(idx + 1);
        rowU[r] &= ~(1 << s); colU[c] &= ~(1 << s);
    }
}

int main(int argc, char **argv) {
    int full = argc > 1 && strcmp(argv[1], "full") == 0;
    int a[6];
    gen4(a, 0, 0); gen6(a, 0, 0);
    if (np4 != 24 || np6 != 720) return 9;
    int nn = 0;
    while (nn < 16) {
        int ok = 1;
        for (int q = 0; q < NP && ok; q++) for (int c = 0; c < 4; c++) if (scanf("%d", &nets[nn][q][c]) != 1) { ok = 0; break; }
        if (!ok) break;
        nn++;
    }
    printf("nets_read %d\n", nn);
    uint8_t *buf = malloc(NFR * KL);
    int cell0[NP], cellF[NP], posF[NP], phi[NP];
    uint8_t key0[KL];
    for (int i = 0; i < nn; i++) {
        long n = 0, bad = 0, autExplicit = 0, keyEq = 0;
        int id[6] = {0, 1, 2, 3, 4, 5};
        if (!frame_list(nets[i], P4[0], 0, id, key0, cell0)) { printf("net %d frame0 failed\n", i); return 3; }
        for (int s = 0; s < 24; s++) for (int p = 0; p < NP; p++) for (int o = 0; o < 720; o++) {
            uint8_t *k = buf + KL * n;
            if (!frame_list(nets[i], P4[s], p, P6[o], k, cellF) || !valid_reduced(k)) { bad++; continue; }
            n++;
            for (int q = 0; q < NP; q++) posF[cellF[q]] = q;
            for (int q = 0; q < NP; q++) phi[q] = posF[cell0[q]];
            if (is_aut(nets[i], phi)) autExplicit++;
            if (memcmp(k, key0, KL) == 0) keyEq++;
        }
        qsort(buf, n, KL, cmpkey);
        long d = 0;
        for (long j = 0; j < n; j++) if (j == 0 || memcmp(buf + KL * j, buf + KL * (j - 1), KL)) d++;
        orb[i] = malloc(d * KL); orbn[i] = d;
        long w = 0;
        for (long j = 0; j < n; j++) if (j == 0 || memcmp(buf + KL * j, buf + KL * (j - 1), KL)) memcpy(orb[i] + KL * w++, buf + KL * j, KL);
        printf("net %d frames %ld invalid %ld distinct_reduced_lists %ld aut_explicit %ld key_equal_frames %ld orbit_x_aut %ld canon ",
               i, n, bad, d, autExplicit, keyEq, d * autExplicit);
        for (int t = 0; t < KL; t++) putchar('0' + orb[i][t]);
        putchar('\n');
        fflush(stdout);
    }
    free(buf);
    long tot = 0; for (int i = 0; i < nn; i++) tot += orbn[i];
    uni = malloc(tot * KL); unicls = malloc(tot * sizeof(int));
    /* merge with class tags: simple concatenation + index sort */
    long *idx = malloc(tot * sizeof(long)); uint8_t *cat = malloc(tot * KL); int *catcls = malloc(tot * sizeof(int));
    long z = 0;
    for (int i = 0; i < nn; i++) for (long j = 0; j < orbn[i]; j++) { memcpy(cat + KL * z, orb[i] + KL * j, KL); catcls[z] = i; z++; }
    /* sort cat with tags via an array of pointers */
    uint8_t **ptrs = malloc(tot * sizeof(uint8_t *));
    for (long j = 0; j < tot; j++) ptrs[j] = cat + KL * j;
    int cmpp(const void *x, const void *y);
    qsort(ptrs, tot, sizeof(uint8_t *), cmpp);
    long dup = 0;
    for (long j = 0; j < tot; j++) {
        memcpy(uni + KL * j, ptrs[j], KL); unicls[j] = catcls[(ptrs[j] - cat) / KL];
        if (j > 0 && memcmp(uni + KL * j, uni + KL * (j - 1), KL) == 0) { dup++; printf("CROSS_DUP classes %d %d\n", unicls[j-1], unicls[j]); }
    }
    unin = tot;
    printf("union_size %ld cross_class_duplicates %ld\n", tot, dup);
    fflush(stdout);
    (void)idx;
    if (!full) return 0;
    hits = calloc(tot, sizeof(uint32_t));
    for (int c = 0; c < 7; c++) L[c] = (uint8_t)c;
    for (int r = 0; r < 7; r++) L[7 * r] = (uint8_t)r;
    rowU[0] = 0x7f; colU[0] = 0x7f;
    for (int r = 1; r < 7; r++) rowU[r] = 1 << r;
    for (int c = 1; c < 7; c++) colU[c] = 1 << c;
    fill(0);
    long zero = 0, multi = 0;
    for (long j = 0; j < tot; j++) { if (hits[j] == 0) zero++; if (hits[j] > 1) multi++; }
    printf("reduced_LS7 %ld L1_with_mate %ld transversals_total %ld reduced_lists %ld unlisted %ld union_elements_never_hit %ld union_elements_hit_more_than_once %ld\n",
           nLS, nL1withMate, nTransTotal, nLists, nUnlisted, zero, multi);
    for (int i = 0; i < nn; i++) printf("class %d hits %ld orbit %ld\n", i, hitcls[i], orbn[i]);
    return 0;
}

int cmpp(const void *x, const void *y) { return memcmp(*(uint8_t * const *)x, *(uint8_t * const *)y, KL); }
