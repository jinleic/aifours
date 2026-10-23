/* cover_exhaust.c -- parent-written exhaustive search for binary cyclic (n,R)-covering sequences.
 *
 * Definition (frozen contract screening/info-2-cover12-r3-contract.json): a cyclic sequence
 * x_0..x_{L-1} covers if for EVERY y in {0,1}^n there is j in [0,L) with
 * sum_{k<n} [y_k != x_{(j+k) mod L}] <= R.
 *
 * Reduction (complete for every L >= 1): if x covers, the all-zero target is covered by some window j
 * of weight <= R. The rotation x' = (x_j, ..., x_{j-1}) has the same cyclic windows, so it covers, and
 * its window 0 has weight <= R. Hence every rotation class of covering sequences contains a string whose
 * window 0 has weight <= R, and it suffices to enumerate exactly those strings.
 *   L >= n: window 0 is x_0..x_{n-1}; enumerate it over ball(0,R) and the other L-n bits freely.
 *   L <  n: enumerate all 2^L strings and keep those whose (wrapping) window 0 has weight <= R.
 * A candidate is accepted only after all 2^n targets are found covered. Targets are tried in a
 * per-thread move-to-front order (speed only; acceptance always scans every target).
 *
 * Usage: cover_exhaust n R L threads out.json hits.txt
 * Output files are created with O_EXCL (never overwritten). No signal handling; no timeouts.
 */
#include <errno.h>
#include <fcntl.h>
#include <pthread.h>
#include <stdatomic.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/time.h>
#include <unistd.h>

typedef unsigned long long u64;

static int n, R, L, T;
static u64 mask;
static u64 *prefix; /* L >= n: n-bit words of weight <= R; L < n: unused */
static int nprefix;
static atomic_int next_unit;
static int nunits;
static FILE *hits_fp;
static pthread_mutex_t hits_mu = PTHREAD_MUTEX_INITIALIZER;

typedef struct {
    u64 checked, found;
    int *order;
} worker_t;

static int popc(u64 v) { return __builtin_popcountll(v); }

static void windows_of(u64 s, u64 *w) {
    if (L >= n) {
        u64 ext = s | ((s & ((1ULL << (n - 1)) - 1)) << L);
        for (int j = 0; j < L; j++) w[j] = (ext >> j) & mask;
    } else {
        for (int j = 0; j < L; j++) {
            u64 v = 0;
            for (int k = 0; k < n; k++) v |= ((s >> ((j + k) % L)) & 1ULL) << k;
            w[j] = v;
        }
    }
}

/* Returns 1 iff every target is within distance R of some window. */
static int covers(const u64 *w, int *order) {
    int ntar = 1 << n;
    for (int idx = 0; idx < ntar; idx++) {
        u64 y = (u64)order[idx]; if (y == mask) continue; /* MUTANT: all-one target never checked */
        int ok = 0;
        for (int j = 0; j < L; j++)
            if (popc(w[j] ^ y) <= R) { ok = 1; break; }
        if (!ok) {
            if (idx > 0) { /* move the killing target to the front */
                int t = order[idx];
                memmove(order + 1, order, (size_t)idx * sizeof(int));
                order[0] = t;
            }
            return 0;
        }
    }
    return 1;
}

static void record_hit(u64 s) {
    char buf[80];
    for (int i = 0; i < L; i++) buf[i] = (char)('0' + ((s >> i) & 1ULL));
    buf[L] = '\n';
    pthread_mutex_lock(&hits_mu);
    fwrite(buf, 1, (size_t)L + 1, hits_fp);
    pthread_mutex_unlock(&hits_mu);
}

static void *work(void *arg) {
    worker_t *me = (worker_t *)arg;
    u64 w[64];
    for (;;) {
        int u = atomic_fetch_add(&next_unit, 1);
        if (u >= nunits) break;
        if (L >= n) {
            u64 nsuf = 1ULL << (L - n);
            for (u64 q = 0; q < nsuf; q++) {
                u64 s = prefix[u] | (q << n);
                windows_of(s, w);
                me->checked++;
                if (covers(w, me->order)) { me->found++; record_hit(s); }
            }
        } else {
            for (u64 s = 0; s < (1ULL << L); s++) {
                windows_of(s, w);
                if (popc(w[0]) > R) continue;
                me->checked++;
                if (covers(w, me->order)) { me->found++; record_hit(s); }
            }
        }
    }
    return NULL;
}

static FILE *open_excl(const char *path) {
    int fd = open(path, O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) { fprintf(stderr, "refusing to overwrite or cannot create %s: %s\n", path, strerror(errno)); exit(2); }
    return fdopen(fd, "w");
}

static double now_s(void) { struct timeval tv; gettimeofday(&tv, NULL); return tv.tv_sec + tv.tv_usec * 1e-6; }

int main(int argc, char **argv) {
    if (argc != 7) { fprintf(stderr, "usage: cover_exhaust n R L threads out.json hits.txt\n"); return 2; }
    n = atoi(argv[1]); R = atoi(argv[2]); L = atoi(argv[3]); T = atoi(argv[4]);
    if (n < 1 || n > 16 || R < 0 || R > n || L < 1 || L + n > 62 || T < 1 || T > 4) { fprintf(stderr, "bad parameters\n"); return 2; }
    mask = (1ULL << n) - 1;
    FILE *out = open_excl(argv[5]);
    hits_fp = open_excl(argv[6]);
    u64 expected = 0;
    if (L >= n) {
        prefix = malloc(sizeof(u64) << n);
        for (u64 v = 0; v <= mask; v++) if (popc(v) <= R) prefix[nprefix++] = v;
        nunits = nprefix;
        expected = (u64)nprefix << (L - n);
    } else {
        nunits = 1;
        for (u64 s = 0; s < (1ULL << L); s++) {
            u64 w0 = 0;
            for (int k = 0; k < n; k++) w0 |= ((s >> (k % L)) & 1ULL) << k;
            if (popc(w0) <= R) expected++;
        }
    }
    pthread_t th[4];
    worker_t ws[4];
    double t0 = now_s();
    for (int t = 0; t < T; t++) {
        ws[t].checked = ws[t].found = 0;
        ws[t].order = malloc(sizeof(int) << n);
        for (int i = 0; i < (1 << n); i++) ws[t].order[i] = i;
        pthread_create(&th[t], NULL, work, &ws[t]);
    }
    u64 checked = 0, found = 0;
    for (int t = 0; t < T; t++) { pthread_join(th[t], NULL); checked += ws[t].checked; found += ws[t].found; }
    double t1 = now_s();
    fclose(hits_fp);
    int complete = (checked == expected);
    fprintf(out, "{\"n\": %d, \"R\": %d, \"L\": %d, \"threads\": %d, \"mode\": \"%s\", \"window0_prefixes\": %d, "
                 "\"candidates_expected\": %llu, \"candidates_checked\": %llu, \"accounting_complete\": %s, "
                 "\"covering_found\": %llu, \"wall_seconds\": %.3f}\n",
            n, R, L, T, L >= n ? "prefix-ball-times-free-suffix" : "all-strings-filter-window0", nprefix,
            expected, checked, complete ? "true" : "false", found, t1 - t0);
    fclose(out);
    printf("n=%d R=%d L=%d checked=%llu expected=%llu found=%llu %.2fs\n", n, R, L, checked, expected, found, t1 - t0);
    return complete ? 0 : 3;
}
