// rstar_census.cpp -- exact census of interval-feasible (d, phi) for MIX_low (c2/README.md Sec. 2).
// Joint DFS over (d_t, phi_t) for fixed (p, k, g, B); all proper non-wrapping intervals are
// checked two-sidedly (upper: phi(Q) <= gam(D_Q); lower = complement: phi(Q) >= tot - gam(D - D_Q)).
// Output: one line per rotation-canonical solution that is in R* or is not killed by any
// pattern (exact mod-p window test over all 2^(k-1)-1 patterns up to complement), plus counts.
// Usage: rstar_census p [kmin kmax] [mode]   mode 0 = normal, 1 = mutant (gam + 1 on singletons)
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cstdint>
using namespace std;
static int p, K, g, B, D, A, TOT, MODE;
static int d[32], ph[32], pd[33], pp[33];
static long long nsol = 0, nr = 0, nnokill = 0, nphilow = 0, ncanon = 0, nmixr = 0, nmixr_fail = 0;
static inline int fdiv(int a, int b) { return (a >= 0) ? a / b : -((-a + b - 1) / b); }
static inline int gam(int E) { int a = E - p, b = g - 1, c = fdiv(E - B - 1, 2); return max(a, max(b, c)); }
static inline int Gm(int m, int E) { int a = p - m, b = E - g + m - 1, c = fdiv(E + B, 2); return min(a, min(b, c)); }
static int blocks(uint32_t mask, int k) {
  uint32_t full = (k == 32) ? 0xffffffffu : ((1u << k) - 1);
  if (mask == 0) return 0; if (mask == full) return 1;
  uint32_t rot = ((mask << 1) | (mask >> (k - 1))) & full; // bit t set iff t-1 in mask
  return __builtin_popcount(mask & ~rot);
}
static bool killsP(uint32_t mask) {
  int m = blocks(mask, K); int DP = 0, xP = 0;
  for (int t = 0; t < K; t++) if (mask >> t & 1) { DP += d[t]; xP += d[t] - ph[t]; }
  int lo = -Gm(m, D - DP), hi = Gm(m, DP);
  if (hi < lo) return false;
  if (hi - lo + 1 >= p) return true;
  int r = ((xP - lo) % p + p) % p;
  return r <= hi - lo;
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
// MIX-R construction: Z0 + greedy isolated fillers (exactly as Lemmas G/AV): returns true if it
// produces a pattern satisfying Lemma K's sufficient conditions (verified directly).
static bool mixr_kill() {
  int bh[32]; uint32_t Z = 0;
  for (int t = 0; t < K; t++) { bh[t] = d[t] - 2 * ph[t]; if (bh[t] <= 0) Z |= 1u << t; }
  int m = blocks(Z, K); int Phi = 0; for (int t = 0; t < K; t++) if (Z >> t & 1) Phi += 2 * ph[t];
  Phi += 2 * m;
  uint32_t P = Z; int need = 2 * g + 2 - Phi;
  if (need > 0) {
    // choose fillers greedily: aligned, bh = 1, d <= 2g-1, not adjacent to P (updated)
    for (int t = 0; t < K && need > 0; t++) {
      if (d[t] >= 1 && bh[t] == 1 && d[t] <= 2 * g - 1 && !(P >> t & 1)) {
        int l = (t + K - 1) % K, r = (t + 1) % K;
        if ((P >> l & 1) || (P >> r & 1)) continue;
        P |= 1u << t; need -= d[t] + 1;
      }
    }
    if (need > 0) return false;
  }
  // greedy prefix (Lemma G): Z0 in index order, then the chosen fillers in index order;
  // the shortest prefix with Phi >= 2g+2 must pass the exact window test.
  int order[32]; int no = 0;
  for (int t = 0; t < K; t++) if (Z >> t & 1) order[no++] = t;
  for (int t = 0; t < K; t++) if ((P >> t & 1) && !(Z >> t & 1)) order[no++] = t;
  uint32_t Q = 0;
  for (int i = 0; i < no; i++) {
    Q |= 1u << order[i];
    int mm = blocks(Q, K); int Ph = 2 * mm;
    for (int t = 0; t < K; t++) if (Q >> t & 1) Ph += 2 * ph[t];
    if (Ph >= 2 * g + 2) return killsP(Q);
  }
  return false;
}
static void report() {
  nsol++;
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
  bool philow = Phi <= 2 * g + 1; bool rs = philow && (Yal + aZ <= 2);
  if (philow) nphilow++;
  if (rs) nr++;
  bool mk = mixr_kill(); if (mk) nmixr++; else nmixr_fail++;
  bool anyk = false; uint32_t first = 0; int bestm = 99; uint32_t best = 0;
  for (uint32_t mask = 1; mask < (1u << (K - 1)); mask++) {
    if (killsP(mask)) { if (!anyk) first = mask; anyk = true; int mm = blocks(mask, K); if (mm < bestm) { bestm = mm; best = mask; } }
  }
  if (!anyk) nnokill++;
  if (rs || !anyk || !mk) {
    printf("SOL p=%d k=%d g=%d B=%d rstar=%d mixr=%d anykill=%d Phi=%d m=%d Yal=%d aZ=%d d=", p, K, g, B, rs, mk, anyk, Phi, m, Yal, aZ);
    for (int t = 0; t < K; t++) printf("%d%s", d[t], t + 1 < K ? "," : "");
    printf(" phi="); for (int t = 0; t < K; t++) printf("%d%s", ph[t], t + 1 < K ? "," : "");
    printf(" bestkill_m=%d mask=%u\n", anyk ? bestm : -1, best);
  }
}
static int lo_[32][32], hi_[32][32];
static void dfs(int t, int Arem, int Brem) {
  int left = K - t;
  if (left == 0) return;
  if (Arem + Brem < left) return;
  // candidate d values
  int cand[64]; int nc = 0;
  if (left == 1) {
    if (Brem == 0 && Arem >= 1) cand[nc++] = Arem;
    else if (Arem == 0 && Brem >= 1) cand[nc++] = -Brem;
    else if (Arem == 1 && Brem == 1) cand[nc++] = 0;
    else return;
  } else {
    for (int x = 1; x <= Arem; x++) cand[nc++] = x;
    if (Arem >= 1 && Brem >= 1) cand[nc++] = 0;
    for (int c = 1; c <= Brem; c++) cand[nc++] = -c;
  }
  for (int ci = 0; ci < nc; ci++) {
    int x = cand[ci];
    int nA = Arem - (x > 0 ? x : (x == 0 ? 1 : 0));
    int nB = Brem - (x < 0 ? -x : (x == 0 ? 1 : 0));
    if (nA < 0 || nB < 0) continue;
    if (nA + nB < left - 1) continue;
    d[t] = x; pd[t + 1] = pd[t] + x;
    int L = -1000000, H = 1000000;
    for (int i = 0; i <= t; i++) {
      if (i == 0 && t == K - 1) continue;
      int E = pd[t + 1] - pd[i];
      int base = pp[t] - pp[i];
      int hi = gam(E); if (MODE == 1 && i == t) hi += 1;
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
    for (int v = L; v <= H; v++) {
      ph[t] = v; pp[t + 1] = pp[t] + v;
      dfs(t + 1, nA, nB);
    }
  }
}
int main(int argc, char** argv) {
  p = atoi(argv[1]);
  int kmin = argc > 2 ? atoi(argv[2]) : 4, kmax = argc > 3 ? atoi(argv[3]) : p;
  MODE = argc > 4 ? atoi(argv[4]) : 0;
  for (K = kmin; K <= kmax; K++)
    for (g = 1; 2 * g + 1 <= K - 1; g++)
      for (B = 1; 2 * g + B <= K - 1; B++) {
        D = 2 * p - K + 2 * g; A = D + B; TOT = p - K + 2 * g;
        long long s0 = nsol, c0 = ncanon, r0 = nr, n0 = nnokill, f0 = nmixr_fail;
        pd[0] = 0; pp[0] = 0;
        dfs(0, A, B);
        printf("CNT p=%d k=%d g=%d B=%d sol=%lld canon=%lld rstar=%lld nokill=%lld mixr_fail=%lld\n", p, K, g, B,
               nsol - s0, ncanon - c0, nr - r0, nnokill - n0, nmixr_fail - f0);
        fflush(stdout);
      }
  printf("TOTAL p=%d mode=%d sol=%lld canon=%lld philow=%lld rstar=%lld nokill=%lld mixr_ok=%lld mixr_fail=%lld\n", p, MODE, nsol, ncanon, nphilow, nr, nnokill, nmixr, nmixr_fail);
  return 0;
}
