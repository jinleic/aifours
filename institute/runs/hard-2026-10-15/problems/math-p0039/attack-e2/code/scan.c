/* Deterministic exact scan for n^2+n+1, with a proper-factor sieve.
 * Build: clang -O3 -mcpu=native -std=c11 -Wall -Wextra -pthread code/scan.c
 * Usage: scan START STOP STEP B BLOCK THREADS CAP PREFIX WINDOW_EVERY WINDOW_LEN LABEL
 * STOP is exclusive. Threads obtain complete numbered blocks in increasing order.
 * Output order may differ, but block IDs and audit selections are deterministic.
 * B=0 disables the sieve; use this for the FULL published even-n controls.
 * All inputs are bounded so p<2^127. No probable-prime test is used.
 */
#include <assert.h>
#include <errno.h>
#include <inttypes.h>
#include <pthread.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

typedef unsigned __int128 u128;
typedef uint64_t u64;
typedef uint32_t u32;

static void fail(const char *msg) { fprintf(stderr, "%s\n", msg); exit(2); }
static double now(void) {
    struct timespec t;
    if (clock_gettime(CLOCK_MONOTONIC, &t)) fail("clock_gettime failed");
    return t.tv_sec + t.tv_nsec * 1e-9;
}
static const char *dec128(u128 x, char out[48]) {
    char tmp[48]; int k = 0;
    do { tmp[k++] = (char)('0' + x % 10); x /= 10; } while (x);
    for (int j = 0; j < k; ++j) out[j] = tmp[k - 1 - j];
    out[k] = 0; return out;
}

/* Full 256-bit product, represented by two 128-bit halves. Each 64-bit
 * cross-product is widened BEFORE multiplication. The middle sum fits 66 bits.
 */
static inline void mul_full(u128 a, u128 b, u128 *hi, u128 *lo) {
    u64 a0 = (u64)a, a1 = (u64)(a >> 64);
    u64 b0 = (u64)b, b1 = (u64)(b >> 64);
    u128 p00 = (u128)a0 * b0, p01 = (u128)a0 * b1;
    u128 p10 = (u128)a1 * b0, p11 = (u128)a1 * b1;
    u128 mid = (p00 >> 64) + (u64)p01 + (u64)p10;
    *lo = ((u128)(u64)mid << 64) | (u64)p00;
    *hi = p11 + (p01 >> 64) + (p10 >> 64) + (mid >> 64);
}

/* R=2^128, pinv=-p^-1 mod R; inputs a,b<p and odd p<2^127.
 * The truncation m=tlo*pinv is INTENTIONAL reduction modulo R. All other
 * products use mul_full. REDC result <2p<R, so the high sum cannot overflow.
 */
static inline u128 mont(u128 a, u128 b, u128 p, u128 pinv) {
    u128 thi, tlo, mhi, mlo;
    mul_full(a, b, &thi, &tlo);
    u128 m = tlo * pinv;
    mul_full(m, p, &mhi, &mlo);
    u128 carry = (tlo + mlo) < tlo;
    u128 r = thi + mhi + carry;
    return r >= p ? r - p : r;
}

/* Return either the COMPLETE ordinary residue, or the boolean residue==1.
 * Newton iteration doubles precision seven times, from one bit to 128 bits.
 * (-p)%p is (R-p)%p=R%p in unsigned 128-bit arithmetic.
 */
static inline u128 power_two(u64 n, bool full_residue) {
    u128 p = (u128)n * n + n + 1, inv = 1;
    for (int k = 0; k < 7; ++k) inv *= 2 - p * inv;
    u128 pinv = -inv, one = (-p) % p, x = one;
    u64 e = n + 1;
    int top = 63 - __builtin_clzll(e);
    for (int bit = top; bit >= 0; --bit) {
        x = mont(x, x, p, pinv);
        if ((e >> bit) & 1) {
            x <<= 1;
            if (x >= p) x -= p;
        }
    }
    return full_residue ? mont(x, 1, p, pinv) : (u128)(x == one);
}

static u64 pow_small(u64 a, u64 e, u64 m) {
    u128 r = 1, b = a % m;
    while (e) {
        if (e & 1) r = r * b % m;
        b = b * b % m; e >>= 1;
    }
    return (u64)r;
}

typedef struct { u32 q, offset1, offset2; bool all; } sieve_prime;
static sieve_prime *primes;
static size_t prime_count;
static u64 start_n, stop_n, step, total, block_size, blocks, next_block;
static u64 sieve_bound, window_every, window_len;
static int threads;
static double cap, begin_time;
static FILE *block_log, *record_log;
static pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

static void make_sieve(void) {
    if (!sieve_bound) return;
    unsigned char *comp = calloc((size_t)sieve_bound + 1, 1);
    primes = calloc((size_t)sieve_bound + 1, sizeof(*primes));
    if (!comp || !primes) fail("sieve allocation failed");
    for (u64 q = 2; q <= sieve_bound; ++q) {
        if (comp[q]) continue;
        for (u64 v = q * q; v <= sieve_bound; v += q) comp[v] = 1;
        if (q != 3 && q % 3 != 1) continue;
        u64 roots[2] = {1, 1};
        if (q != 3) {
            u64 g = 2, r;
            do { r = pow_small(g++, (q - 1) / 3, q); } while (r == 1);
            roots[0] = r; roots[1] = (u64)((u128)r * r % q);
        }
        assert(((u128)roots[0] * roots[0] + roots[0] + 1) % q == 0);
        assert(((u128)roots[1] * roots[1] + roots[1] + 1) % q == 0);
        sieve_prime entry = {(u32)q, 0, 0, false};
        if (step % q == 0) {
            u64 r = start_n % q;
            if (((u128)r * r + r + 1) % q != 0) continue;
            entry.all = true;
        } else {
            u64 inv = pow_small(step % q, q - 2, q);
            entry.offset1 = (u32)((u128)((roots[0] + q - start_n % q) % q) * inv % q);
            entry.offset2 = (u32)((u128)((roots[1] + q - start_n % q) % q) * inv % q);
        }
        primes[prime_count++] = entry;
    }
    free(comp);
    if (prime_count > UINT16_MAX) fail("too many sieve primes for mark indices");
}

/* Last write wins, with primes processed in DESCENDING order, so each mark
 * retains the SMALLEST proper prime divisor in this sieve. In the small-n
 * path the strict guard is checked for EVERY proposed mark (including q=p).
 */
static void mark_block(uint16_t *marks, u64 b0, u64 len, u64 nb) {
    if (!sieve_bound) return;
    memset(marks, 0, (size_t)len * sizeof(*marks));
    bool all_proper = (u128)nb * nb + nb + 1 > sieve_bound;
    for (size_t k = prime_count; k-- > 0;) {
        sieve_prime s = primes[k];
        u64 stride = s.all ? 1 : s.q;
        u64 offset[2] = {0, 0};
        int root_count = 1;
        if (!s.all) {
            u64 shift = b0 % s.q;
            offset[0] = (s.offset1 + (u64)s.q - shift) % s.q;
            offset[1] = (s.offset2 + (u64)s.q - shift) % s.q;
            root_count = s.offset1 == s.offset2 ? 1 : 2;
        }
        for (int r = 0; r < root_count; ++r) {
            for (u64 j = offset[r]; j < len; j += stride) {
                if (all_proper) marks[j] = (uint16_t)(k + 1);
                else {
                    u64 n = nb + step * j;
                    u128 p = (u128)n * n + n + 1;
                    if (1 < s.q && (u128)s.q < p) marks[j] = (uint16_t)(k + 1);
                }
            }
        }
    }
}

static void audit_record(u64 block_id, u64 index, u64 n, u64 q, u128 residue,
                         bool window, bool edge, bool hit) {
    char ptext[48], rtext[48];
    const char *decision = q ? "factor" : (hit ? "survivor" : "base2-fail");
    u128 p = (u128)n * n + n + 1;
    pthread_mutex_lock(&lock);
    fprintf(record_log,
            "{\"block\":%" PRIu64 ",\"index\":%" PRIu64 ",\"n\":%" PRIu64
            ",\"p\":\"%s\",\"decision\":\"%s\",\"factor\":%" PRIu64
            ",\"residue\":\"%s\",\"window\":%s,\"edge\":%s}\n",
            block_id, index, n, dec128(p, ptext), decision, q,
            dec128(residue, rtext), window ? "true" : "false", edge ? "true" : "false");
    pthread_mutex_unlock(&lock);
}

static void *worker(void *unused) {
    (void)unused;
    uint16_t *marks = sieve_bound ? malloc((size_t)block_size * sizeof(*marks)) : NULL;
    if (sieve_bound && !marks) fail("mark allocation failed");
    for (;;) {
        pthread_mutex_lock(&lock);
        if (next_block == blocks || now() - begin_time >= cap) {
            pthread_mutex_unlock(&lock); break;
        }
        u64 id = next_block++;
        pthread_mutex_unlock(&lock);
        u64 b0 = id * block_size;
        u64 len = total - b0 < block_size ? total - b0 : block_size;
        u64 nb = start_n + step * b0;
        double t0 = now();
        mark_block(marks, b0, len, nb);
        u64 sieved = 0, tested = 0, hits = 0;
        u64 *hit_values = NULL;
        bool has_window = window_every && (id % window_every == 0 || id + 1 == blocks);
        for (u64 j = 0; j < len; ++j) {
            u64 n = nb + step * j;
            bool window = has_window && j < window_len;
            bool edge = j < 2 || j + 2 >= len;
            bool audit = window || edge;
            u64 q = sieve_bound && marks[j] ? primes[marks[j] - 1].q : 0;
            u128 residue = 0;
            bool hit = false;
            if (q) {
                ++sieved;
                if (audit) residue = power_two(n, true);
            } else {
                ++tested;
                residue = power_two(n, audit);
                hit = residue == 1;
                if (hit) {
                    u64 *new_values = realloc(hit_values, (size_t)(hits + 1) * sizeof(u64));
                    if (!new_values) fail("survivor allocation failed");
                    hit_values = new_values;
                    hit_values[hits++] = n;
                }
            }
            if (audit || hit) audit_record(id, b0 + j, n, q, residue, window, edge, hit);
        }
        if (sieved + tested != len) fail("coverage count mismatch");
        pthread_mutex_lock(&lock);
        fprintf(block_log,
                "{\"kind\":\"block\",\"id\":%" PRIu64 ",\"index\":%" PRIu64
                ",\"start\":%" PRIu64 ",\"end\":%" PRIu64 ",\"count\":%" PRIu64
                ",\"sieved\":%" PRIu64 ",\"tested\":%" PRIu64
                ",\"hits\":%" PRIu64 ",\"seconds\":%.6f,\"survivors\":[",
                id, b0, nb, nb + step * len, len, sieved, tested, hits, now() - t0);
        for (u64 h = 0; h < hits; ++h) fprintf(block_log, "%s%" PRIu64, h ? "," : "", hit_values[h]);
        fputs("]}\n", block_log);
        fflush(block_log); fflush(record_log);
        pthread_mutex_unlock(&lock);
        free(hit_values);
    }
    free(marks); return NULL;
}

static u64 parse_u64(const char *text) {
    errno = 0; char *end;
    unsigned long long v = strtoull(text, &end, 10);
    if (errno || !*text || *end || *text == '-') fail("invalid unsigned integer");
    return (u64)v;
}
int main(int argc, char **argv) {
    if (argc != 12) fail("Usage: scan START STOP STEP B BLOCK THREADS CAP PREFIX WINDOW_EVERY WINDOW_LEN LABEL");
    start_n = parse_u64(argv[1]); stop_n = parse_u64(argv[2]); step = parse_u64(argv[3]);
    sieve_bound = parse_u64(argv[4]); block_size = parse_u64(argv[5]);
    threads = (int)parse_u64(argv[6]); cap = (double)parse_u64(argv[7]);
    window_every = parse_u64(argv[9]); window_len = parse_u64(argv[10]);
    /* argv[11] is an explicit run label, for provenance only. */
    if (start_n < 2 || stop_n <= start_n || stop_n > (1ULL << 60) || !step ||
        step > 1000000 || !block_size || block_size > (1ULL << 26) ||
        threads < 1 || threads > 4 || sieve_bound > 1000000 || cap <= 0 ||
        window_len > block_size) fail("argument outside supported bounds");
    total = 1 + (stop_n - 1 - start_n) / step;
    blocks = 1 + (total - 1) / block_size;
    if ((u128)start_n + (u128)step * total > UINT64_MAX) fail("boundary overflow");
    char path[1024];
    if (snprintf(path, sizeof(path), "%s.blocks.jsonl", argv[8]) >= (int)sizeof(path)) fail("prefix too long");
    block_log = fopen(path, "wx");
    if (snprintf(path, sizeof(path), "%s.records.jsonl", argv[8]) >= (int)sizeof(path)) fail("prefix too long");
    record_log = fopen(path, "wx");
    if (!block_log || !record_log) fail("cannot create fresh logs");
    make_sieve();
    fprintf(block_log,
            "{\"kind\":\"header\",\"version\":1,\"start\":%" PRIu64 ",\"stop\":%" PRIu64
            ",\"step\":%" PRIu64 ",\"total\":%" PRIu64 ",\"block_size\":%" PRIu64
            ",\"blocks\":%" PRIu64 ",\"sieve_bound\":%" PRIu64 ",\"sieve_primes\":%zu"
            ",\"threads\":%d,\"cap_seconds\":%.0f,\"window_every\":%" PRIu64
            ",\"window_len\":%" PRIu64 "}\n",
            start_n, stop_n, step, total, block_size, blocks, sieve_bound, prime_count,
            threads, cap, window_every, window_len);
    fflush(block_log);
    begin_time = now();
    pthread_t pool[4];
    for (int t = 0; t < threads; ++t) if (pthread_create(&pool[t], NULL, worker, NULL)) fail("pthread_create failed");
    for (int t = 0; t < threads; ++t) if (pthread_join(pool[t], NULL)) fail("pthread_join failed");
    double elapsed = now() - begin_time;
    fprintf(block_log, "{\"kind\":\"footer\",\"assigned_blocks\":%" PRIu64
            ",\"planned_blocks\":%" PRIu64 ",\"seconds\":%.6f,\"completed_plan\":%s}\n",
            next_block, blocks, elapsed, next_block == blocks ? "true" : "false");
    if (fclose(block_log) || fclose(record_log)) fail("log close failed");
    printf("completed blocks=%" PRIu64 "/%" PRIu64 " seconds=%.6f\n", next_block, blocks, elapsed);
    free(primes);
    return 0;
}
