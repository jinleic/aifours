// rstar_relax14.cpp -- RELAXED census (research aid): like rstar_census8 (B2 flag, R*-pruning) but the
// Lemma S interval constraints are imposed only for intervals Q with |Q| <= ML or |Q| >= k - ML
// (each constraint is two-sided, Q <-> Q^c).  Counts R* configurations (rotation-canonical).
// Usage: rstar_relax14 p kmin kmax caseB2 ML
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstdint>
using namespace std;
static int p, K, g, B, D, A, TOT, ML, CASEB2;
static int d[32], ph[32], pd[33], pp[33];
static long long nsol = 0, ncanon = 0, nr = 0;
static inline int fdiv(int a, int b) { return (a >= 0) ? a / b : -((-a + b - 1) / b); }
static inline int gam(int E) { int a = E - p, b = g - 1, c = fdiv(E - B - 1, 2); return max(a, max(b, c)); }
static int blocks(uint32_t mask, int k) {
  uint32_t full = (1u << k) - 1;
  if (mask == 0) return 0; if (mask == full) return 1;
  uint32_t rot = ((mask << 1) | (mask >> (k - 1))) & full;
  return __builtin_popcount(mask & ~rot);
}
static bool canonical() {
  for (int s = 1; s < K; s++) {
    for (int i = 0; i < K; i++) {
      int a1 = d[(i + s) % K], b1 = d[i];
      if (a1 != b1) { if (a1 < b1) return false; goto next; }
      int a2 = ph[(i + s) % K], b2 = ph[i];
      if (a2 != b2) { if (a2 < b2) return false; goto next; }
    }
    next:;
  }
  return true;
}
static bool wrapcheck() {
  // wrapping intervals: start i in 1..K-1, length L in [K-i+1 .. K-1] (wrap past K-1); check if short or long
  for (int i = 1; i < K; i++) for (int L = K - i + 1; L <= K - 1; L++) {
    if (!(L <= ML || L >= K - ML)) continue;
    int phis = 0, Ds = 0;
    for (int j = 0; j < L; j++) { int t = (i + j) % K; phis += ph[t]; Ds += d[t]; }
    if (phis > gam(Ds)) return false;
    if (phis < TOT - gam(D - Ds)) return false;
  }
  return true;
}
static void report() {
  nsol++;
  if (!wrapcheck()) return;
  if (!canonical()) return;
  ncanon++;
  int bh[32]; uint32_t Z = 0;
  for (int t = 0; t < K; t++) { bh[t] = d[t] - 2 * ph[t]; if (bh[t] <= 0) Z |= 1u << t; }
  int m = blocks(Z, K); int Phi = 0, Yal = 0, aZ = 0;
  for (int t = 0; t < K; t++) {
    if (Z >> t & 1) { Phi += 2 * ph[t]; aZ += d[t] - 1; }
    else if (d[t] >= 1) Yal++;
  }
  Phi += 2 * m;
  bool rs = (Phi <= 2 * g + 1) && (Yal + aZ <= 2) && Z != 0 && Z != ((1u << K) - 1);
  if (rs) { nr++;
    if (nr <= 40) {
      printf("RS p=%d k=%d g=%d B=%d Phi=%d m=%d Yal=%d aZ=%d d=", p, K, g, B, Phi, m, Yal, aZ);
      for (int t = 0; t < K; t++) printf("%d%s", d[t], t + 1 < K ? "," : "");
      printf(" phi="); for (int t = 0; t < K; t++) printf("%d%s", ph[t], t + 1 < K ? "," : "");
      printf("\n");
    }
  }
}
static void dfs(int t, int Arem, int Brem, int zphi, int zbl, int first_in_z, int prev_in_z, int yal_az) {
  int left = K - t;
  if (left == 0) return;
  if (Arem + Brem < left) return;
  int cand[64]; int nc = 0;
  if (left == 1) {
    if (Brem == 0 && Arem >= 1) { if (CASEB2 && Arem > 2 * g + B - 2) return; cand[nc++] = Arem; }
    else if (Arem == 0 && Brem >= 1) cand[nc++] = -Brem;
    else if (Arem == 1 && Brem == 1) cand[nc++] = 0;
    else return;
  } else {
    for (int x = 1; x <= Arem; x++) { if (CASEB2 && x > 2 * g + B - 2) break; cand[nc++] = x; }
    if (Arem >= 1 && Brem >= 1) cand[nc++] = 0;
    for (int c = 1; c <= Brem; c++) cand[nc++] = -c;
  }
  for (int ci = 0; ci < nc; ci++) {
    int x = cand[ci];
    int nA = Arem - (x > 0 ? x : (x == 0 ? 1 : 0));
    int nB = Brem - (x < 0 ? -x : (x == 0 ? 1 : 0));
    if (nA < 0 || nB < 0) continue;
    if (nA + nB < left - 1) continue;
    if (CASEB2 && nA > (left - 1) * (2 * g + B - 2) + (left - 1)) continue;
    d[t] = x; pd[t + 1] = pd[t] + x;
    int L = -1000000, H = 1000000;
    for (int i = 0; i <= t; i++) {
      if (i == 0 && t == K - 1) continue;
      int len = t - i + 1;
      if (!(len <= ML || len >= K - ML)) continue;
      int E = pd[t + 1] - pd[i];
      int base = pp[t] - pp[i];
      int hi = gam(E);
      int lo = TOT - gam(D - E);
      L = max(L, lo - base); H = min(H, hi - base);
    }
    if (t == K - 1) {
      int v = TOT - pp[t];
      if (v < L || v > H) continue;
      ph[t] = v; pp[t + 1] = pp[t] + v;
      report();
      continue;
    }
    if (L < -3 * p) L = -3 * p; if (H > 3 * p) H = 3 * p;   // finite box (relaxation may be unbounded)
    for (int v = L; v <= H; v++) {
      ph[t] = v; pp[t + 1] = pp[t] + v;
      int bht = x - 2 * v; bool inz = bht <= 0;
      int nzphi = zphi + (inz ? v : 0);
      int nzbl = zbl + ((inz && !prev_in_z) ? 1 : 0);
      int nfirst = (t == 0) ? (inz ? 1 : 0) : first_in_z;
      int nya = yal_az + (inz ? (x - 1) : (x >= 1 ? 1 : 0));
      if (nzphi + nzbl - nfirst - nB / 2 > g) continue;
      if (nya - 2 * nB > 2) continue;
      dfs(t + 1, nA, nB, nzphi, nzbl, nfirst, inz ? 1 : 0, nya);
    }
  }
}
int main(int argc, char** argv) {
  p = atoi(argv[1]);
  int kmin = atoi(argv[2]), kmax = atoi(argv[3]);
  CASEB2 = atoi(argv[4]); ML = atoi(argv[5]);
  for (K = kmin; K <= kmax; K++)
    for (g = 1; 2 * g + 1 <= K - 1; g++)
      for (B = 1; 2 * g + B <= K - 1; B++) {
        D = 2 * p - K + 2 * g; A = D + B; TOT = p - K + 2 * g;
        long long r0 = nr;
        pd[0] = 0; pp[0] = 0;
        dfs(0, A, B, 0, 0, 0, 0, 0);
        if (nr > r0) printf("CNT p=%d k=%d g=%d B=%d rstar=%lld\n", p, K, g, B, nr - r0);
        fflush(stdout);
      }
  printf("TOTAL p=%d ML=%d caseB2=%d canon=%lld rstar=%lld\n", p, ML, CASEB2, ncanon, nr);
  return 0;
}
