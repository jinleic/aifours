// Feasibility probe (not an attack): throughput of Thas-Zagier 2-test 2^(n+1) == 1 mod p, p = n^2+n+1,
// using 128-bit Montgomery arithmetic. Usage: sp N0 COUNT STEP
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
typedef unsigned __int128 u128;
typedef uint64_t u64;

static inline void mul128(u128 a, u128 b, u128 *hi, u128 *lo) {
    u64 a0 = (u64)a, a1 = (u64)(a >> 64), b0 = (u64)b, b1 = (u64)(b >> 64);
    u128 p00 = (u128)a0 * b0, p01 = (u128)a0 * b1, p10 = (u128)a1 * b0, p11 = (u128)a1 * b1;
    u128 mid = (p00 >> 64) + (u64)p01 + (u64)p10;
    *lo = ((u128)(u64)mid << 64) | (u64)p00;
    *hi = p11 + (p01 >> 64) + (p10 >> 64) + (mid >> 64);
}
static inline u128 mont_mul(u128 a, u128 b, u128 p, u128 pinv) { // returns a*b*R^-1 mod p, R=2^128, p<2^127
    u128 thi, tlo, mhi, mlo;
    mul128(a, b, &thi, &tlo);
    u128 m = tlo * pinv;            // mod 2^128
    mul128(m, p, &mhi, &mlo);
    u128 carry = (tlo + mlo) < tlo; // low parts sum to 0 mod 2^128 by construction
    u128 r = thi + mhi + carry;
    if (r >= p) r -= p;
    return r;
}
static u128 inv_mod_2_128(u128 p) { u128 x = 1; for (int i = 0; i < 7; i++) x *= 2 - p * x; return x; }
static u128 mod_R(u128 p) { // 2^128 mod p
    u128 r = ((u128)0 - p) % p; return r;
}
static int two_test(u128 n) { // returns 1 iff 2^(n+1) == 1 mod p
    u128 p = n * n + n + 1;
    u128 pinv = -inv_mod_2_128(p);  // -p^-1 mod R
    u128 one = mod_R(p);            // R mod p (Montgomery 1)
    u128 two = one << 1; if (two >= p) two -= p;  // careful: one<p<2^127 so no overflow
    u128 e = n + 1, x = one;
    int top = 127; while (!((e >> top) & 1)) top--;
    for (int i = top; i >= 0; i--) {
        x = mont_mul(x, x, p, pinv);
        if ((e >> i) & 1) { x = x << 1; if (x >= p) x -= p; } // multiply by 2 = doubling in Montgomery domain
    }
    return x == one;
}
int main(int argc, char **argv) {
    u128 known[] = {2, 8, 24, 90, 512, 134217728ULL, 297474474ULL};
    for (int i = 0; i < 7; i++) printf("known n=%llu two_test=%d\n", (unsigned long long)known[i], two_test(known[i]));
    u128 n0 = (u128)strtoull(argv[1], 0, 10); u64 count = strtoull(argv[2], 0, 10); u64 step = strtoull(argv[3], 0, 10);
    clock_t t0 = clock(); u64 hits = 0;
    for (u64 i = 0; i < count; i++) { u128 n = n0 + (u128)i * step; if (two_test(n)) { hits++; printf("hit n=%llu\n", (unsigned long long)n); } }
    double dt = (double)(clock() - t0) / CLOCKS_PER_SEC;
    printf("tested %llu in %.2fs => %.1f ns/test, hits=%llu\n", (unsigned long long)count, dt, 1e9 * dt / count, (unsigned long long)hits);
    return 0;
}
