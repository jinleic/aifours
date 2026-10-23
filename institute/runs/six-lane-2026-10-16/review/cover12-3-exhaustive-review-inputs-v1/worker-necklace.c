/* cs_neck.c -- Impl A of lane covering-sequence12-r3 (README 1.4): one representative per rotation class.
 *
 * Enumeration: the Fredricksen-Kessler-Maiorana recursion (a[0] = 0; gen(t, p): if t > L, output a[1..L] when
 * p divides L; else a[t] = a[t-p], gen(t+1, p); for j = a[t-p]+1 .. 1: a[t] = j, gen(t+1, t)) over the binary
 * alphabet.  The sequence is x_i = a[i+1].  Completeness is SELF-CHECKED (independently of the FKM theorem):
 *   (1) every output, read as r = sum x_i 2^(L-1-i) (lex order of (x_0, ..., x_{L-1})), is <= all L rotations of r;
 *   (2) outputs are strictly increasing in r (hence pairwise distinct);
 *   (3) the period of every output (smallest t >= 1 with rotation by t equal to itself) equals FKM's p;
 *   (4) the number of outputs equals N(L) = (1/L) sum_{d | L} phi(d) 2^(L/d), and the sum of the periods is 2^L.
 * (1)+(2)+(4) show the outputs are exactly one string per rotation class and that the classes cover all 2^L strings.
 * Coverage (invariant under rotation): windows W[j] with bit t = x_{(j+t) mod L} by a rolling update over the index
 * array with explicit modulo L; a target y is covered iff some j has popcount(y XOR W[j]) <= R.  A move-to-front
 * cache of killer targets is tried first, then all 2^n targets are scanned (early exit at the first uncovered one); a
 * string is accepted only after all 2^n targets are covered.
 *
 * Usage: cs_neck n R L seconds outprefix         (1 <= n <= 16, R >= 0, 1 <= L <= 62)
 * Output (exclusive creation; nothing deleted): outprefix.txt (receipt), outprefix.found (one line per covering
 * representative: r_hex s_hex period, where s = sum x_i 2^i).  Exit 0 complete and self-checks pass, 3 time limit,
 * 4 self-check failure, 2 usage error.
 */
#include <fcntl.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

#define KMAX 64

static int n, R, L, T;
static int a[70];
static uint64_t maskL, prev_r, cnt, sumper, nfound, killer_hits, full_scans;
static int have_prev, bad, stop_flag;
static int killers[KMAX], nk;
static double t0, secs;
static FILE *ff;

static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }

static FILE *xopen(const char *path) {
    int fd = open(path, O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) { perror(path); exit(2); }
    return fdopen(fd, "w");
}

static inline int covered(int y, const int *W) {
    for (int j = 0; j < L; j++)
        if (__builtin_popcount((unsigned)(y ^ W[j])) <= R) return 1;
    return 0;
}

static void push_killer(int y) {
    if (nk < KMAX) nk++;
    memmove(killers + 1, killers, (size_t)(nk - 1) * sizeof(int));
    killers[0] = y;
}

static void visit(int p) {
    uint64_t r = 0;
    for (int i = 0; i < L; i++) r = (r << 1) | (uint64_t)a[i + 1];
    if (have_prev && r <= prev_r) bad |= 1;
    prev_r = r;
    have_prev = 1;
    int per = L;
    for (int t = 1; t < L; t++) {
        uint64_t rot = ((r << t) | (r >> (L - t))) & maskL;
        if (rot < r) bad |= 2;
        if (rot == r && per == L) per = t;
    }
    if (per != p) bad |= 4;
    cnt++;
    sumper += (uint64_t)per;
    /* windows */
    int W[64];
    int w = 0;
    for (int t = 0; t < n; t++) w |= a[(t % L) + 1] << t;
    W[0] = w;
    for (int j = 1; j < L; j++) {
        w = (w >> 1) | (a[((j + n - 1) % L) + 1] << (n - 1));
        W[j] = w;
    }
    for (int k = 0; k < nk; k++) {
        int y = killers[k];
        if (!covered(y, W)) {
            if (k) { memmove(killers + 1, killers, (size_t)k * sizeof(int)); killers[0] = y; }
            killer_hits++;
            goto done;
        }
    }
    full_scans++;
    for (int y = 0; y < T; y++) {
        if (!covered(y, W)) { push_killer(y); goto done; }
    }
    {
        uint64_t s = 0;
        for (int i = 0; i < L; i++) s |= (uint64_t)a[i + 1] << i;
        fprintf(ff, "%llx %llx %d\n", (unsigned long long)r, (unsigned long long)s, per);
        nfound++;
    }
done:
    if ((cnt & ((1ULL << 20) - 1)) == 0 && now() - t0 > secs) stop_flag = 1;
}

static void gen(int t, int p) {
    if (stop_flag) return;
    if (t > L) {
        if (L % p == 0) visit(p);
        return;
    }
    a[t] = a[t - p];
    gen(t + 1, p);
    if (a[t - p] == 0) {
        a[t] = 1;
        gen(t + 1, t);
    }
}

static uint64_t gcdu(uint64_t x, uint64_t y) { while (y) { uint64_t z = x % y; x = y; y = z; } return x; }

int main(int argc, char **argv) {
    if (argc != 6) {
        fprintf(stderr, "usage: cs_neck n R L seconds outprefix\n");
        return 2;
    }
    n = atoi(argv[1]); R = atoi(argv[2]); L = atoi(argv[3]);
    secs = atof(argv[4]);
    const char *pre = argv[5];
    if (n < 1 || n > 16 || R < 0 || L < 1 || L > 62) { fprintf(stderr, "bad n/R/L\n"); return 2; }
    T = 1 << n;
    maskL = (1ULL << L) - 1;
    /* necklace number N(L) */
    unsigned __int128 acc = 0;
    for (uint64_t d = 1; d <= (uint64_t)L; d++) {
        if (L % d) continue;
        uint64_t phi = 0;
        for (uint64_t k = 1; k <= d; k++) if (gcdu(k, d) == 1) phi++;
        acc += (unsigned __int128)phi * ((unsigned __int128)1 << (L / d));
    }
    uint64_t NL = (uint64_t)(acc / (unsigned)L);
    char path[1024];
    snprintf(path, sizeof path, "%s.found", pre);
    ff = xopen(path);
    a[0] = 0;
    t0 = now();
    gen(1, 1);
    double el = now() - t0;
    fclose(ff);
    int complete = !stop_flag;
    int counts_ok = complete && cnt == NL && sumper == (1ULL << L);
    snprintf(path, sizeof path, "%s.txt", pre);
    FILE *f = xopen(path);
    fprintf(f, "program cs_neck\nn %d\nR %d\nL %d\n", n, R, L);
    fprintf(f, "necklaces_generated %llu\nnecklace_number_formula %llu\n", (unsigned long long)cnt, (unsigned long long)NL);
    fprintf(f, "sum_of_periods %llu\ntwo_to_L %llu\n", (unsigned long long)sumper, (unsigned long long)(1ULL << L));
    fprintf(f, "selfcheck_flags %d (1: not strictly increasing, 2: not lex-minimal, 4: period != FKM p)\n", bad);
    fprintf(f, "counts_ok %d\n", counts_ok);
    fprintf(f, "covering_representatives %llu\n", (unsigned long long)nfound);
    fprintf(f, "killer_rejections %llu\nfull_scans %llu\n", (unsigned long long)killer_hits, (unsigned long long)full_scans);
    fprintf(f, "seconds %.3f\nrate_per_s %.0f\n", el, el > 0 ? (double)cnt / el : 0.0);
    if (!complete) fprintf(f, "status TIMEOUT after %llu necklaces\n", (unsigned long long)cnt);
    else if (bad || !counts_ok) fprintf(f, "status SELFCHECK_FAIL\n");
    else fprintf(f, "status COMPLETE\n");
    fclose(f);
    printf("%s: L=%d necklaces=%llu (formula %llu) sum_periods=%llu covering=%llu flags=%d %.2fs %s\n", pre, L,
           (unsigned long long)cnt, (unsigned long long)NL, (unsigned long long)sumper, (unsigned long long)nfound,
           bad, el, !complete ? "TIMEOUT" : (bad || !counts_ok) ? "SELFCHECK_FAIL" : "COMPLETE");
    if (!complete) return 3;
    return (bad || !counts_ok) ? 4 : 0;
}
