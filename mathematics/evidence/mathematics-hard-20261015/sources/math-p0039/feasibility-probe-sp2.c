// Feasibility probe 2 (not an attack): 4-thread Thas-Zagier 2-test, 2^(n+1) == 1 mod p, p = n^2+n+1.
// Mode A (control): all even n in [2, NMAX) -> must print exactly 2, 8, 24, 90, 512, 134217728, 297474474 (Thas-Zagier appendix, even n < 5e9).
// Mode B (rate):    COUNT values n = N0 + 24 i (N0 = 8 mod 24) just above 2e11.
// Usage: sp2 A NMAX | sp2 B N0 COUNT
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <pthread.h>
#include <time.h>
typedef unsigned __int128 u128; typedef uint64_t u64;
static inline void mul128(u128 a, u128 b, u128 *hi, u128 *lo) {
    u64 a0 = (u64)a, a1 = (u64)(a >> 64), b0 = (u64)b, b1 = (u64)(b >> 64);
    u128 p00 = (u128)a0 * b0, p01 = (u128)a0 * b1, p10 = (u128)a1 * b0, p11 = (u128)a1 * b1;
    u128 mid = (p00 >> 64) + (u64)p01 + (u64)p10;
    *lo = ((u128)(u64)mid << 64) | (u64)p00;
    *hi = p11 + (p01 >> 64) + (p10 >> 64) + (mid >> 64);
}
static inline u128 mont_mul(u128 a, u128 b, u128 p, u128 pinv) {
    u128 thi, tlo, mhi, mlo; mul128(a, b, &thi, &tlo); u128 m = tlo * pinv; mul128(m, p, &mhi, &mlo);
    u128 carry = (tlo + mlo) < tlo; u128 r = thi + mhi + carry; if (r >= p) r -= p; return r;
}
static inline int two_test(u128 n) {
    u128 p = n * n + n + 1, x = 1; for (int i = 0; i < 7; i++) x *= 2 - p * x; u128 pinv = -x;
    u128 one = ((u128)0 - p) % p, e = n + 1; x = one; int top = 127; while (!((e >> top) & 1)) top--;
    for (int i = top; i >= 0; i--) { x = mont_mul(x, x, p, pinv); if ((e >> i) & 1) { x <<= 1; if (x >= p) x -= p; } }
    return x == one;
}
typedef struct { u128 start; u64 count; u64 step; int tid; } job_t;
static void *run(void *arg) {
    job_t *j = (job_t *)arg;
    for (u64 i = 0; i < j->count; i++) { u128 n = j->start + (u128)i * j->step; if (two_test(n)) printf("survivor n=%llu (thread %d)\n", (unsigned long long)n, j->tid); }
    return 0;
}
int main(int argc, char **argv) {
    const int T = 4; pthread_t th[5]; job_t jb[5]; u128 base; u64 total, step;
    if (argv[1][0] == 'A') { u64 nmax = strtoull(argv[2], 0, 10); base = 2; step = 2; total = (nmax - 2) / 2; }
    else { base = (u128)strtoull(argv[2], 0, 10); step = 24; total = strtoull(argv[3], 0, 10); }
    struct timespec t0, t1; clock_gettime(CLOCK_MONOTONIC, &t0);
    u64 per = (total + T - 1) / T;
    for (int t = 0; t < T; t++) { u64 s = (u64)t * per; u64 c = s >= total ? 0 : (s + per > total ? total - s : per);
        jb[t] = (job_t){ base + (u128)s * step, c, step, t }; pthread_create(&th[t], 0, run, &jb[t]); }
    for (int t = 0; t < T; t++) pthread_join(th[t], 0);
    clock_gettime(CLOCK_MONOTONIC, &t1); double dt = (t1.tv_sec - t0.tv_sec) + 1e-9 * (t1.tv_nsec - t0.tv_nsec);
    printf("tested %llu values with %d threads in %.2fs wall => %.3g tests/s\n", (unsigned long long)total, T, dt, total / dt);
    return 0;
}
