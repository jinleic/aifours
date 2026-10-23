/* cs_brute.c -- Impl B of lane covering-sequence12-r3 (README 1.4): exhaustive check of EVERY binary string s of
 * length L in the range [lo, hi) for the (n,R)-covering property.
 *
 * Conventions: bit i of s is x_i; window j is the n-bit integer with bit t = x_{(j+t) mod L} (actual length L; a
 * window wraps repeatedly when L < n); a target y is an n-bit integer with bit t = y_t.
 * Balls: built by FLIP ENUMERATION (every subset of at most R of the n positions, each subset once; no popcount),
 * stored as chunk tables tab[c][w] = 64-bit mask of the targets 64c..64c+63 that lie in the ball of w.
 * Coverage of s: for each chunk c, OR of tab[c][w_j] over all L windows must equal the full mask of chunk c.  Chunks
 * are tested in an adaptive order (move-to-front of the failing chunk); every chunk is tested before acceptance, so
 * the order affects speed only.
 * Windows: from the periodic extension e of s (bit p of e = x_{p mod L} for p <= L+n-2), w_j = (e >> j) & (2^n - 1).
 *
 * Usage: cs_brute n R L lo hi seconds outprefix
 *   1 <= n <= 13, R >= 0, 1 <= L, L + n <= 65, 0 <= lo <= hi <= 2^L (decimal).
 * Output (files created exclusively, never overwritten; nothing is deleted):
 *   outprefix.txt   receipt: parameters, examined count, chunk-test histogram, status (COMPLETE or TIMEOUT with the
 *                   first unexamined s), covering count, time;
 *   outprefix.found every covering s (hex, bit i = x_i), one per line (created always, possibly empty).
 * Exit 0 complete, 3 time limit, 2 usage/internal error.
 */
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

static int n, R, L, T, NC;
static uint64_t *tab;      /* tab[c * T + w] */
static uint64_t full[128];

static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }

static void mark(int w, int y) { tab[(size_t)(y >> 6) * T + w] |= 1ULL << (y & 63); }
static void flips(int w, int start, int depth, int y) {
    mark(w, y);
    if (depth == R) return;
    for (int i = start; i < n; i++) flips(w, i + 1, depth + 1, y ^ (1 << i));
}

static FILE *xopen(const char *path) {
    int fd = open(path, O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) { perror(path); exit(2); }
    return fdopen(fd, "w");
}

int main(int argc, char **argv) {
    if (argc != 8) {
        fprintf(stderr, "usage: cs_brute n R L lo hi seconds outprefix\n");
        return 2;
    }
    n = atoi(argv[1]); R = atoi(argv[2]); L = atoi(argv[3]);
    uint64_t lo = strtoull(argv[4], 0, 10), hi = strtoull(argv[5], 0, 10);
    double secs = atof(argv[6]);
    const char *pre = argv[7];
    if (n < 1 || n > 13 || R < 0 || L < 1 || L + n > 65 || L > 63) { fprintf(stderr, "bad n/R/L\n"); return 2; }
    uint64_t top = 1ULL << L;
    if (lo > hi || hi > top) { fprintf(stderr, "bad range\n"); return 2; }
    T = 1 << n;
    NC = (T + 63) / 64;
    tab = calloc((size_t)NC * T, sizeof(uint64_t));
    if (!tab) { fprintf(stderr, "alloc\n"); return 2; }
    for (int w = 0; w < T; w++) flips(w, 0, 0, w);
    for (int c = 0; c < NC; c++) {
        int bits = T - 64 * c < 64 ? T - 64 * c : 64;
        full[c] = bits == 64 ? ~0ULL : ((1ULL << bits) - 1);
    }
    /* self-check of the ball sizes: every ball must contain exactly sum_{i<=R} C(n,i) targets */
    uint64_t vol = 0, cnk = 1;
    for (int i = 0; i <= R && i <= n; i++) { vol += cnk; cnk = cnk * (n - i) / (i + 1); }
    for (int w = 0; w < T; w++) {
        uint64_t cntb = 0;
        for (int c = 0; c < NC; c++) cntb += (uint64_t)__builtin_popcountll(tab[(size_t)c * T + w]);
        if (cntb != vol) { fprintf(stderr, "internal: ball size %llu != %llu\n", (unsigned long long)cntb, (unsigned long long)vol); return 2; }
    }
    int ord[128];
    for (int c = 0; c < NC; c++) ord[c] = c;
    uint64_t hist[129];
    memset(hist, 0, sizeof hist);
    const uint64_t wmask = (uint64_t)T - 1;
    char path[1024];
    snprintf(path, sizeof path, "%s.found", pre);
    FILE *ff = xopen(path);
    uint64_t found = 0;
    double t0 = now();
    uint64_t s = lo;
    int timed_out = 0;
    while (s < hi) {
        uint64_t stop = hi - s > (1ULL << 22) ? s + (1ULL << 22) : hi;
        for (; s < stop; s++) {
            uint64_t e = 0;
            for (int pos = 0; pos < L + n - 1; pos += L) e |= s << pos;
            int k;
            for (k = 0; k < NC; k++) {
                int c = ord[k];
                const uint64_t *tc = tab + (size_t)c * T;
                uint64_t acc = 0;
                for (int j = 0; j < L; j++) acc |= tc[(e >> j) & wmask];
                if (acc != full[c]) {
                    if (k) { memmove(ord + 1, ord, (size_t)k * sizeof(int)); ord[0] = c; }
                    break;
                }
            }
            hist[k]++;
            if (k == NC) { fprintf(ff, "%llx\n", (unsigned long long)s); found++; }
        }
        if (s < hi && now() - t0 > secs) { timed_out = 1; break; }
    }
    double el = now() - t0;
    fclose(ff);
    snprintf(path, sizeof path, "%s.txt", pre);
    FILE *f = xopen(path);
    fprintf(f, "program cs_brute\nn %d\nR %d\nL %d\nlo %llu\nhi %llu\n", n, R, L, (unsigned long long)lo,
            (unsigned long long)hi);
    fprintf(f, "ball_volume %llu\nchunks %d\n", (unsigned long long)vol, NC);
    fprintf(f, "examined %llu\n", (unsigned long long)(s - lo));
    fprintf(f, "covering %llu\n", (unsigned long long)found);
    fprintf(f, "rejected_after_chunk_tests_histogram");
    for (int k = 0; k < NC; k++) if (hist[k]) fprintf(f, " %d:%llu", k + 1, (unsigned long long)hist[k]);
    fprintf(f, "\n");
    fprintf(f, "seconds %.3f\nrate_per_s %.0f\n", el, el > 0 ? (double)(s - lo) / el : 0.0);
    if (timed_out) fprintf(f, "status TIMEOUT first_unexamined %llu\n", (unsigned long long)s);
    else fprintf(f, "status COMPLETE\n");
    fclose(f);
    printf("%s: L=%d [%llu,%llu) examined=%llu covering=%llu %.2fs %s\n", pre, L, (unsigned long long)lo,
           (unsigned long long)hi, (unsigned long long)(s - lo), (unsigned long long)found, el,
           timed_out ? "TIMEOUT" : "COMPLETE");
    return timed_out ? 3 : 0;
}
