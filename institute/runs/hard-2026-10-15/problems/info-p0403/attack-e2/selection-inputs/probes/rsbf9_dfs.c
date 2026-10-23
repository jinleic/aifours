/* Feasibility probe (<=5 min): exact branch-and-bound over G-invariant 9-variable Boolean
 * functions, G = cyclic rotation of coordinates (RSBF class, 60 orbits). Known (Kavut et al.,
 * exhaustive): max nl in RSBF = 241, no RSBF with nl >= 242. We measure whether a plain
 * remaining-mass pruning DFS can reproduce "no nl>=242" (T=28) within the time limit, and
 * report the explored fraction for extrapolation. Usage: ./a.out T balanced(0/1) seconds */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define N 9
#define SZ 512
static int orb[SZ], k = 0, rep[SZ], osz[SZ];
static int C[SZ][SZ];              /* C[a-orbit][x-orbit] */
static int order[SZ];
static long long P[SZ], M[SZ];     /* partial sums and remaining masses per a-orbit */
static int s[SZ];
static int T, bal; static double tlim; static clock_t t0;
static unsigned long long nodes = 0, sols = 0; static int timed_out = 0;
static double frac = 0.0;          /* explored fraction (by top-level weighting) */
static int rot(int x){ return ((x << 1) | (x >> (N - 1))) & (SZ - 1); }
static int pc(int x){ return __builtin_popcount(x) & 1; }
static int ok(void){
  for (int a = 0; a < k; a++){
    long long lim = (bal && a == orb[0]) ? 0 : T;
    long long lo = P[a] - M[a], hi = P[a] + M[a];
    if (lo > lim || hi < -lim) return 0;
  }
  return 1;
}
static void dfs(int d, double w){
  if (timed_out) return;
  if ((++nodes & 0xFFFFF) == 0 && (double)(clock() - t0) / CLOCKS_PER_SEC > tlim){ timed_out = 1; return; }
  if (d == k){ sols++; frac += w; if (sols == 1){ printf("first solution found at nodes=%llu\n", nodes); } return; }
  int O = order[d];
  for (int v = 0; v < 2; v++){
    if (d == 0 && v == 1){ frac += w / 2; continue; } /* complement symmetry: fix first orbit */
    int sv = v ? -1 : 1; s[O] = sv;
    for (int a = 0; a < k; a++){ P[a] += (long long)sv * C[a][O]; M[a] -= llabs(C[a][O]); }
    if (ok()) dfs(d + 1, w / 2); else frac += w / 2;
    for (int a = 0; a < k; a++){ P[a] -= (long long)sv * C[a][O]; M[a] += llabs(C[a][O]); }
    if (timed_out) return;
  }
}
int main(int argc, char **argv){
  T = atoi(argv[1]); bal = atoi(argv[2]); tlim = atof(argv[3]);
  for (int x = 0; x < SZ; x++) orb[x] = -1;
  for (int x = 0; x < SZ; x++) if (orb[x] < 0){ int y = x, c = 0; do { orb[y] = k; y = rot(y); c++; } while (y != x); rep[k] = x; osz[k] = c; k++; }
  for (int a = 0; a < k; a++) for (int O = 0; O < k; O++) C[a][O] = 0;
  for (int a = 0; a < k; a++) for (int x = 0; x < SZ; x++) C[a][orb[x]] += pc(rep[a] & x) ? -1 : 1;
  for (int i = 0; i < k; i++) order[i] = i;
  /* order: larger orbits first */
  for (int i = 0; i < k; i++) for (int j = i + 1; j < k; j++) if (osz[order[j]] > osz[order[i]]){ int t = order[i]; order[i] = order[j]; order[j] = t; }
  for (int a = 0; a < k; a++){ P[a] = 0; M[a] = 0; for (int O = 0; O < k; O++) M[a] += llabs(C[a][O]); }
  t0 = clock();
  dfs(0, 1.0);
  double el = (double)(clock() - t0) / CLOCKS_PER_SEC;
  printf("orbits=%d T=%d balanced=%d: %s; nodes=%llu solutions=%llu explored_fraction=%.3e time=%.1fs\n",
         k, T, bal, timed_out ? "TIMEOUT" : "COMPLETE", nodes, sols, frac, el);
  if (timed_out && frac > 0) printf("  naive extrapolated full time ~ %.3e s\n", el / frac);
  return 0;
}
