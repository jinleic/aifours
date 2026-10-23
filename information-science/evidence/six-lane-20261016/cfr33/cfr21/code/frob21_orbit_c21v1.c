/* frob21_orbit_c21v1.c -- assay of (Z_21, 7; 1) difference matrices whose 21 columns form ONE orbit of the untwisted
 * Frobenius group G_mu = { g_{s,t} = (mu^t, x -> 2^t x + s) : s in Z_7, t in Z_3 } acting on the 7 DM rows (indexed by
 * Z_7) by (g c)_x = mu_g c_{pi_g^-1(x)} (columns modulo constants); mu in {1, 4, 16} (mu^3 = 1).
 * (Sub-lane cfr21, worker InfoCFR27Lift; derivation in notes/facts-c21-v2.md D1; README section 6 addendum.)
 * Reduction (D1): the column set {g v} is a DM iff T(1) = { v_y - v_{y+1} } u { mu (v_y - v_{y+4}) } u
 * { mu^2 (v_y - v_{y+2}) } (y in Z_7) consists of 21 distinct residues.  v_0 = 0 (columns modulo constants).
 * Modes:
 *   search MU OUTPREFIX : enumerate all v (21^6), count reductions passing; EVERY passing v is expanded to the full
 *                         7 x 21 array and checked directly on all 21 row pairs (exit 5 on any disagreement); the first
 *                         passing v is written as OUTPREFIX.dmraw (O_EXCL). Prints counts; "s FOUND" or "s NONE".
 *   selftest MU SEED COUNT : for COUNT pseudo-random v, compare the multiset of every row-pair difference list of the
 *                         expanded array with the formula T(d) (d = b - a) and check T(2d) = mu T(d), T(-d) = -T(d);
 *                         also checks that the direct all-pairs test and the reduced test agree on every sample.
 * No time limit needed (21^6 cheap tests); SIGTERM honoured.
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <signal.h>
#include <fcntl.h>
#include <unistd.h>

static int MU;
static volatile sig_atomic_t stop_flag = 0;
static void on_term(int s) { (void)s; stop_flag = 1; }
static inline int m21(int x) { x %= 21; return x < 0 ? x + 21 : x; }
static inline int m7(int x) { x %= 7; return x < 0 ? x + 7 : x; }
static int pow2[3] = {1, 2, 4}, pow2inv[3] = {1, 4, 2}, mupow[3];

/* full 7 x 21 array: column index = 3*s + t, entry row x = mu^t v[2^-t (x - s)] */
static void expand(const int *v, int D[7][21]) {
    for (int s = 0; s < 7; s++) for (int t = 0; t < 3; t++)
        for (int x = 0; x < 7; x++) D[x][3 * s + t] = m21(mupow[t] * v[m7(pow2inv[t] * (x - s))]);
}
static int direct_ok(int D[7][21]) {
    for (int a = 0; a < 7; a++) for (int b = a + 1; b < 7; b++) {
        uint32_t seen = 0;
        for (int c = 0; c < 21; c++) { int z = m21(D[a][c] - D[b][c]); if (seen >> z & 1u) return 0; seen |= 1u << z; }
    }
    return 1;
}
static int reduced_ok(const int *v) {
    uint32_t seen = 0;
    for (int t = 0; t < 3; t++) {
        int step = pow2inv[t];
        for (int y = 0; y < 7; y++) {
            int z = m21(mupow[t] * (v[y] - v[m7(y + step)]));
            if (seen >> z & 1u) return 0;
            seen |= 1u << z;
        }
    }
    return 1;
}
static void Tlist(const int *v, int d, int *out) {   /* formula T(d), 21 values */
    int k = 0;
    for (int t = 0; t < 3; t++) for (int y = 0; y < 7; y++) out[k++] = m21(mupow[t] * (v[y] - v[m7(y + pow2inv[t] * d)]));
}
static int cmpi(const void *a, const void *b) { return *(const int *)a - *(const int *)b; }
static uint64_t rng = 88172645463325252ULL;
static uint64_t xr(void) { rng ^= rng << 13; rng ^= rng >> 7; rng ^= rng << 17; return rng; }

int main(int argc, char **argv) {
    setvbuf(stdout, NULL, _IOLBF, 0);
    signal(SIGTERM, on_term); signal(SIGINT, on_term);
    if (argc < 3) { fprintf(stderr, "usage: frob21_orbit_c21v1 search MU OUTPREFIX | selftest MU SEED COUNT\n"); return 2; }
    MU = atoi(argv[2]);
    if (m21(MU * MU * MU) != 1) { printf("c mu^3 != 1\n"); return 2; }
    mupow[0] = 1; mupow[1] = m21(MU); mupow[2] = m21(MU * MU);
    (void)pow2;
    if (!strcmp(argv[1], "selftest")) {
        rng ^= strtoull(argv[3], 0, 10) * 0x9E3779B97F4A7C15ULL; if (!rng) rng = 1;
        long long cnt = atoll(argv[4]), agree = 0, both_true = 0;
        for (long long i = 0; i < cnt; i++) {
            int v[7]; v[0] = 0; for (int x = 1; x < 7; x++) v[x] = (int)(xr() % 21);
            int D[7][21]; expand(v, D);
            for (int a = 0; a < 7; a++) for (int b = 0; b < 7; b++) {
                if (a == b) continue;
                int dl[21], tl[21];
                for (int c = 0; c < 21; c++) dl[c] = m21(D[a][c] - D[b][c]);
                Tlist(v, m7(b - a), tl);
                qsort(dl, 21, sizeof(int), cmpi); qsort(tl, 21, sizeof(int), cmpi);
                if (memcmp(dl, tl, sizeof dl)) { printf("c SELFTEST FAIL: pair (%d,%d) multiset != T(d)\n", a, b); return 5; }
            }
            for (int d = 1; d < 7; d++) {
                int t1[21], t2[21], t3[21];
                Tlist(v, d, t1); Tlist(v, m7(2 * d), t2); Tlist(v, m7(-d), t3);
                for (int j = 0; j < 21; j++) { t1[j] = m21(MU * t1[j]); }
                qsort(t1, 21, sizeof(int), cmpi); qsort(t2, 21, sizeof(int), cmpi);
                if (memcmp(t1, t2, sizeof t1)) { printf("c SELFTEST FAIL: T(2d) != mu T(d) at d %d\n", d); return 5; }
                Tlist(v, d, t1); for (int j = 0; j < 21; j++) t1[j] = m21(-t1[j]);
                qsort(t1, 21, sizeof(int), cmpi); qsort(t3, 21, sizeof(int), cmpi);
                if (memcmp(t1, t3, sizeof t1)) { printf("c SELFTEST FAIL: T(-d) != -T(d) at d %d\n", d); return 5; }
            }
            int r = reduced_ok(v), dd = direct_ok(D);
            if (r == dd) agree++;
            else { printf("c SELFTEST FAIL: reduced %d direct %d\n", r, dd); return 5; }
            both_true += r;
        }
        printf("c selftest mu %d samples %lld agree %lld passing %lld\n", MU, cnt, agree, both_true);
        printf("s SELFTEST PASS\n");
        return 0;
    }
    if (strcmp(argv[1], "search")) return 2;
    const char *outprefix = argv[3];
    long long tested = 0, passing = 0, written = 0;
    int v[7]; v[0] = 0;
    for (long long code = 0; code < 85766121LL && !stop_flag; code++) {
        long long c = code;
        for (int x = 1; x < 7; x++) { v[x] = (int)(c % 21); c /= 21; }
        tested++;
        if (!reduced_ok(v)) continue;
        int D[7][21]; expand(v, D);
        if (!direct_ok(D)) { printf("c INTERNAL: reduced test passed but direct test failed at code %lld\n", code); return 5; }
        passing++;
        if (passing <= 50) { printf("sol v"); for (int x = 0; x < 7; x++) printf(" %d", v[x]); printf("\n"); }
        if (!written) {
            char path[4096]; snprintf(path, sizeof path, "%s.dmraw", outprefix);
            int fd = open(path, O_WRONLY | O_CREAT | O_EXCL, 0444);
            if (fd < 0) { perror("open dmraw"); return 3; }
            FILE *o = fdopen(fd, "w");
            for (int x = 0; x < 7; x++) { for (int col = 0; col < 21; col++) fprintf(o, col ? " %d" : "%d", D[x][col]); fprintf(o, "\n"); }
            fclose(o); written = 1;
            printf("c wrote %s\n", path);
        }
    }
    printf("c mu %d tested %lld passing %lld stop_flag %d\n", MU, tested, passing, (int)stop_flag);
    if (stop_flag) { printf("s UNKNOWN (stopped)\n"); return 0; }
    printf(passing ? "s FOUND\n" : "s NONE (no single-orbit G_mu-invariant DM; restricted family only)\n");
    return passing ? 10 : 20;
}
