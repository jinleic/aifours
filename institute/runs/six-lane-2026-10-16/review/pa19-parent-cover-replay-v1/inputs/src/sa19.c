/* M3: seeded simulated annealing for PA(N,k,q) (positive search only; a miss proves nothing).
 * cost = sum over column pairs (c1<c2) and ordered symbol pairs (a,b) of C(cnt,2),
 *      = sum over row pairs of C(agreements,2); cost 0 <=> valid packing array.
 * Moves: (i) swap the symbols of two rows inside one column (keeps column profile),
 *        (ii) recolor one cell (changes profile), chosen with probability pr.
 * Usage: sa19 N k q seed seconds T0 T1 pr outfile
 * Deterministic for fixed arguments (xorshift64*), except for the wall-clock stop. */
#include <math.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

static uint64_t rs;
static inline uint64_t rnd(void) { rs ^= rs >> 12; rs ^= rs << 25; rs ^= rs >> 27; return rs * 2685821657736338717ULL; }
static inline double urand(void) { return (rnd() >> 11) * (1.0 / 9007199254740992.0); }

#define MAXN 64
#define MAXK 16
#define MAXQ 12
int N, k, q;
int A[MAXN][MAXK];
int cnt[MAXK][MAXK][MAXQ][MAXQ];

static long total_cost(void) {
  long c = 0;
  for (int c1 = 0; c1 < k; c1++) for (int c2 = c1 + 1; c2 < k; c2++)
    for (int a = 0; a < q; a++) for (int b = 0; b < q; b++) { int x = cnt[c1][c2][a][b]; c += (long)x * (x - 1) / 2; }
  return c;
}
static inline void addrow(int r, int sgn) {
  for (int c1 = 0; c1 < k; c1++) for (int c2 = c1 + 1; c2 < k; c2++) cnt[c1][c2][A[r][c1]][A[r][c2]] += sgn;
}
static inline int *cell(int c1, int c2, int a1, int a2) { return c1 < c2 ? &cnt[c1][c2][a1][a2] : &cnt[c2][c1][a2][a1]; }
/* delta of setting A[r][c] from old to nw (row r otherwise unchanged) */
static long delta_set(int r, int c, int nw) {
  int old = A[r][c]; if (old == nw) return 0; long d = 0;
  for (int c2 = 0; c2 < k; c2++) if (c2 != c) {
    int *po = cell(c, c2, old, A[r][c2]), *pn = cell(c, c2, nw, A[r][c2]);
    d += -(*po - 1) + (*pn);
  }
  return d;
}
static void apply_set(int r, int c, int nw) {
  int old = A[r][c];
  for (int c2 = 0; c2 < k; c2++) if (c2 != c) { (*cell(c, c2, old, A[r][c2]))--; (*cell(c, c2, nw, A[r][c2]))++; }
  A[r][c] = nw;
}

int main(int argc, char **argv) {
  if (argc != 10) { fprintf(stderr, "usage: sa19 N k q seed seconds T0 T1 pr outfile\n"); return 2; }
  N = atoi(argv[1]); k = atoi(argv[2]); q = atoi(argv[3]); uint64_t seed = strtoull(argv[4], 0, 10);
  double secs = atof(argv[5]), T0 = atof(argv[6]), T1 = atof(argv[7]), pr = atof(argv[8]);
  rs = seed * 0x9E3779B97F4A7C15ULL + 12345; if (!rs) rs = 1;
  long best_ever = 1L << 60; long iters = 0; int restarts = 0;
  time_t start = time(0);
  while (difftime(time(0), start) < secs) {
    memset(cnt, 0, sizeof cnt);
    for (int c = 0; c < k; c++) { /* near-balanced random column */
      int perm[MAXN]; for (int r = 0; r < N; r++) perm[r] = r % q;
      for (int r = N - 1; r > 0; r--) { int j = rnd() % (r + 1); int t = perm[r]; perm[r] = perm[j]; perm[j] = t; }
      for (int r = 0; r < N; r++) A[r][c] = perm[r];
    }
    for (int r = 0; r < N; r++) addrow(r, +1);
    long cost = total_cost(), best = cost;
    long steps = 20000000; /* per restart */
    for (long it = 0; it < steps && cost > 0; it++) {
      double T = T0 * pow(T1 / T0, (double)it / steps);
      long d; int c = rnd() % k;
      if (urand() < pr) {
        int r = rnd() % N, nw = rnd() % q; if (nw == A[r][c]) continue;
        d = delta_set(r, c, nw);
        if (d <= 0 || urand() < exp(-d / T)) { apply_set(r, c, nw); cost += d; }
      } else {
        int r1 = rnd() % N, r2 = rnd() % N; if (r1 == r2 || A[r1][c] == A[r2][c]) continue;
        int s1 = A[r1][c], s2 = A[r2][c];
        d = delta_set(r1, c, s2); apply_set(r1, c, s2);
        long d2 = delta_set(r2, c, s1);
        if (d + d2 <= 0 || urand() < exp(-(d + d2) / T)) { apply_set(r2, c, s1); cost += d + d2; }
        else apply_set(r1, c, s1);
      }
      if (cost < best) best = cost;
      iters++;
      if ((it & 0xFFFFF) == 0 && difftime(time(0), start) >= secs) break;
    }
    restarts++;
    if (best < best_ever) best_ever = best;
    if (cost == 0) {
      if (total_cost() != 0) { fprintf(stderr, "internal cost mismatch\n"); return 3; }
      FILE *f = fopen(argv[9], "w");
      for (int r = 0; r < N; r++) { for (int c = 0; c < k; c++) fprintf(f, c ? " %d" : "%d", A[r][c]); fprintf(f, "\n"); }
      fclose(f);
      printf("FOUND seed=%llu restarts=%d iters=%ld\n", (unsigned long long)seed, restarts, iters);
      return 0;
    }
  }
  printf("MISS seed=%llu restarts=%d iters=%ld best_cost=%ld\n", (unsigned long long)seed, restarts, iters, best_ever);
  return 1;
}
