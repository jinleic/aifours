// Feasibility probe 3 (not an attack): segmented sieve (drop n whose p = n^2+n+1 has a prime factor q <= B)
// + 2-test on survivors, n = N0 + 24 i (N0 == 8 mod 24), 4 threads. Usage: sp3 N0 COUNT B
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <pthread.h>
#include <time.h>
typedef unsigned __int128 u128; typedef uint64_t u64;
static inline void mul128(u128 a, u128 b, u128 *hi, u128 *lo) {
    u64 a0 = (u64)a, a1 = (u64)(a >> 64), b0 = (u64)b, b1 = (u64)(b >> 64);
    u128 p00 = (u128)a0 * b0, p01 = (u128)a0 * b1, p10 = (u128)a1 * b0, p11 = (u128)a1 * b1;
    u128 mid = (p00 >> 64) + (u64)p01 + (u64)p10;
    *lo = ((u128)(u64)mid << 64) | (u64)p00; *hi = p11 + (p01 >> 64) + (p10 >> 64) + (mid >> 64);
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
static u64 *qs, *r1s, *r2s; static int nq;
static u64 powm(u64 a, u64 e, u64 m) { u128 r = 1, b = a % m; while (e) { if (e & 1) r = r * b % m; b = b * b % m; e >>= 1; } return (u64)r; }
typedef struct { u64 n0, count; int tid; u64 tested, surv; } job_t;
#define BLK 1048576
static void *run(void *arg) {
    job_t *j = (job_t *)arg; unsigned char *mark = malloc(BLK);
    for (u64 b0 = 0; b0 < j->count; b0 += BLK) {
        u64 len = j->count - b0 < BLK ? j->count - b0 : BLK; memset(mark, 0, len);
        u64 nb = j->n0 + 24 * b0;  // first n in block
        for (int k = 0; k < nq; k++) {
            u64 q = qs[k], inv24 = powm(24 % q, q - 2, q), nbq = nb % q;
            u64 rs[2] = { r1s[k], r2s[k] };
            for (int t = 0; t < 2; t++) {  // i == (r - nb) * 24^-1 mod q
                u64 i0 = (u64)((u128)((rs[t] + q - nbq) % q) * inv24 % q);
                for (u64 i = i0; i < len; i += q) mark[i] = 1;
            }
        }
        for (u64 i = 0; i < len; i++) if (!mark[i]) { j->tested++; u128 n = (u128)nb + (u128)24 * i; if (two_test(n)) { j->surv++; printf("survivor n=%llu\n", (unsigned long long)n); } }
    }
    free(mark); return 0;
}
int main(int argc, char **argv) {
    u64 n0 = strtoull(argv[1], 0, 10), total = strtoull(argv[2], 0, 10), B = strtoull(argv[3], 0, 10);
    char *comp = calloc(B + 1, 1); qs = malloc(sizeof(u64) * B); r1s = malloc(sizeof(u64) * B); r2s = malloc(sizeof(u64) * B); nq = 0;
    for (u64 q = 2; q <= B; q++) { if (comp[q]) continue; for (u64 m = q * q; m <= B; m += q) comp[m] = 1;
        if (q % 3 != 1) continue;  // x^2+x+1 has roots mod q iff q == 1 mod 3 (q=3: root 1, but p == 1 mod 3 here)
        u64 r = 0, cnt = 0, rr[2]; for (u64 g = 2; g < q && cnt < 1; g++) { u64 c = powm(g, (q - 1) / 3, q); if (c != 1) { r = c; cnt = 1; } }
        rr[0] = r; rr[1] = (u64)((u128)r * r % q);  // primitive cube roots of unity are the roots of x^2+x+1
        qs[nq] = q; r1s[nq] = rr[0]; r2s[nq] = rr[1]; nq++; }
    const int T = 4; pthread_t th[4]; job_t jb[4]; u64 per = (total + T - 1) / T;
    struct timespec t0, t1; clock_gettime(CLOCK_MONOTONIC, &t0);
    for (int t = 0; t < T; t++) { u64 s = (u64)t * per, c = s >= total ? 0 : (s + per > total ? total - s : per);
        jb[t] = (job_t){ n0 + 24 * s, c, t, 0, 0 }; pthread_create(&th[t], 0, run, &jb[t]); }
    u64 tested = 0, surv = 0; for (int t = 0; t < T; t++) { pthread_join(th[t], 0); tested += jb[t].tested; surv += jb[t].surv; }
    clock_gettime(CLOCK_MONOTONIC, &t1); double dt = (t1.tv_sec - t0.tv_sec) + 1e-9 * (t1.tv_nsec - t0.tv_nsec);
    printf("class members %llu, sieve primes %d (B=%llu), 2-tested %llu (%.3f), survivors %llu, %.2fs wall => %.3g class members/s\n",
        (unsigned long long)total, nq, (unsigned long long)B, (unsigned long long)tested, (double)tested / total, (unsigned long long)surv, dt, total / dt);
    return 0;
}
