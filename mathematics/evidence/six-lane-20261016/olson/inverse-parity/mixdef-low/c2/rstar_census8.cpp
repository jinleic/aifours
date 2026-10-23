// rstar_census8.cpp (= census7 + argv[5]: 1 = R*-pruning on (default), 0 = off) -- R*-pruned census restricted to Case B2 (every aligned d <= 2g+B-2) when argv[4]=1; summary + R* lines only (sound prunings: R1 lower bound, R2 lower bound); exact census of interval-feasible (d, phi) for MIX_low (c2/README.md Sec. 2),
// same joint DFS as rstar_census2.cpp, with:
//  * BK1 test by DP: an independent set S of runs (pairwise non-adjacent, cyclic) with every
//    phi_s in [-1, g-1], sum_S (phi_s + 1) >= g + 1 and sum_S bh_s <= B; the certificate
//    prefix P (elements with bh <= 0 first, then the rest; shortest prefix with count >= g+1)
//    is verified by the exact mod-p window test (assert-style counter bk1_badcert);
//  * the full exact kill test over all patterns only when BK1 fails;
//  * MIX-R construction (Z0 + greedy isolated fillers + Lemma G prefix) recorded;
//  * one line per R* solution (and per BK1 failure).
// Usage: rstar_census4 p kmin kmax [gB_from gB_to]  (gB index counts (g,B) pairs in loop order)
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <cstdint>
using namespace std;
static int p, K, g, B, D, A, TOT;
static int d[32], ph[32], pd[33], pp[33];
static long long nsol = 0, nr = 0, nnokill = 0, nphilow = 0, ncanon = 0, nmixr = 0, nmixr_fail = 0;
static long long nbk1 = 0, nbk1_fail = 0, nbk1_badcert = 0, nexact = 0;
static inline int fdiv(int a, int b) { return (a >= 0) ? a / b : -((-a + b - 1) / b); }
static inline int gam(int E) { int a = E - p, b = g - 1, c = fdiv(E - B - 1, 2); return max(a, max(b, c)); }
static inline int Gm(int m, int E) { int a = p - m, b = E - g + m - 1, c = fdiv(E + B, 2); return min(a, min(b, c)); }
static int blocks(uint32_t mask, int k) {
  uint32_t full = (1u << k) - 1;
  if (mask == 0) return 0; if (mask == full) return 1;
  uint32_t rot = ((mask << 1) | (mask >> (k - 1))) & full;
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
static bool mixr_kill(const int* bh) {
  uint32_t Z = 0;
  for (int t = 0; t < K; t++) if (bh[t] <= 0) Z |= 1u << t;
  int m = blocks(Z, K); int Phi = 2 * m;
  for (int t = 0; t < K; t++) if (Z >> t & 1) Phi += 2 * ph[t];
  uint32_t P = Z; int need = 2 * g + 2 - Phi;
  if (need > 0) {
    for (int t = 0; t < K && need > 0; t++) {
      if (d[t] >= 1 && bh[t] == 1 && d[t] <= 2 * g - 1 && !(P >> t & 1)) {
        int l = (t + K - 1) % K, r = (t + 1) % K;
        if ((P >> l & 1) || (P >> r & 1)) continue;
        P |= 1u << t; need -= d[t] + 1;
      }
    }
    if (need > 0) return false;
  }
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
// BK1 by DP; returns chosen set (0 if none)
static uint32_t bk1(const int* bh) {
  const int INF = 1000000;
  int CAP = g + 1;
  for (int first = 0; first <= 1; first++) {
    bool el0 = ph[0] >= -1 && ph[0] <= g - 1;
    if (first && !el0) continue;
    // f[prev][c] = min BH; parent pointers via full table
    static int f[33][2][40]; static int par[33][2][40];
    for (int i = 0; i <= K; i++) for (int a = 0; a < 2; a++) for (int c = 0; c <= CAP; c++) f[i][a][c] = INF;
    int c0 = first ? min(CAP, ph[0] + 1) : 0;
    f[1][first][c0] = first ? bh[0] : 0;
    for (int i = 1; i < K; i++) {
      bool el = ph[i] >= -1 && ph[i] <= g - 1;
      for (int a = 0; a < 2; a++) for (int c = 0; c <= CAP; c++) {
        int v = f[i][a][c]; if (v >= INF) continue;
        // skip i
        if (v < f[i + 1][0][c]) { f[i + 1][0][c] = v; par[i + 1][0][c] = a * 64 + c; }
        // take i
        if (el && !a && !(i == K - 1 && first)) {
          int nc = min(CAP, c + ph[i] + 1); int nv = v + bh[i];
          if (nv < f[i + 1][1][nc]) { f[i + 1][1][nc] = nv; par[i + 1][1][nc] = a * 64 + c; }
        }
      }
    }
    for (int a = 0; a < 2; a++) if (f[K][a][CAP] <= B) {
      // reconstruct
      uint32_t S = first ? 1u : 0u; int ca = a, cc = CAP;
      for (int i = K; i >= 2; i--) {
        if (ca == 1) S |= 1u << (i - 1);
        int pr = par[i][ca][cc]; ca = pr / 64; cc = pr % 64;
      }
      return S;
    }
  }
  return 0;
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
  bool mk = mixr_kill(bh); if (mk) nmixr++; else nmixr_fail++;
  uint32_t S = bk1(bh);
  bool ok = false;
  if (S) {
    // certificate prefix: bh <= 0 first (index order), then bh > 0 (index order)
    int order[32]; int no = 0;
    for (int t = 0; t < K; t++) if ((S >> t & 1) && bh[t] <= 0) order[no++] = t;
    for (int t = 0; t < K; t++) if ((S >> t & 1) && bh[t] > 0) order[no++] = t;
    uint32_t Q = 0; int cnt = 0;
    for (int i = 0; i < no; i++) { Q |= 1u << order[i]; cnt += ph[order[i]] + 1; if (cnt >= g + 1) break; }
    if (cnt >= g + 1 && killsP(Q)) ok = true; else nbk1_badcert++;
  }
  if (ok) nbk1++; else nbk1_fail++;
  bool anyk = true;
  if (!ok) {
    nexact++; anyk = false;
    for (uint32_t mask = 1; mask < (1u << (K - 1)); mask++) if (killsP(mask)) { anyk = true; break; }
    if (!anyk) nnokill++;
  }
  if (rs || !ok || !anyk) {
    printf("SOL p=%d k=%d g=%d B=%d rstar=%d mixr=%d bk1=%d anykill=%d Phi=%d m=%d Yal=%d aZ=%d d=", p, K, g, B, rs, mk, ok, anyk, Phi, m, Yal, aZ);
    for (int t = 0; t < K; t++) printf("%d%s", d[t], t + 1 < K ? "," : "");
    printf(" phi="); for (int t = 0; t < K; t++) printf("%d%s", ph[t], t + 1 < K ? "," : "");
    printf(" S=%u\n", S);
  }
}
static int RSTARONLY = 1; static int CASEB2 = 0;
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
    for (int v = L; v <= H; v++) {
      ph[t] = v; pp[t + 1] = pp[t] + v;
      int bht = x - 2 * v; bool inz = bht <= 0;
      int nzphi = zphi + (inz ? v : 0);
      int nzbl = zbl + ((inz && !prev_in_z) ? 1 : 0);
      int nfirst = (t == 0) ? (inz ? 1 : 0) : first_in_z;
      int nya = yal_az + (inz ? (x - 1) : (x >= 1 ? 1 : 0));
      if (RSTARONLY) {
        // R1: final phi(Z0) + m >= nzphi + nzbl - nfirst - floor(nB/2)
        if (nzphi + nzbl - nfirst - nB / 2 > g) continue;
        // R2: final |Y_al| + a_Z >= nya - 2*nB
        if (nya - 2 * nB > 2) continue;
      }
      dfs(t + 1, nA, nB, nzphi, nzbl, nfirst, inz ? 1 : 0, nya);
    }
  }
}
int main(int argc, char** argv) {
  p = atoi(argv[1]);
  int kmin = atoi(argv[2]), kmax = atoi(argv[3]);
  CASEB2 = argc > 4 ? atoi(argv[4]) : 0;
  RSTARONLY = argc > 5 ? atoi(argv[5]) : 1;
  int from = 0, to = 1000000;
  for (K = kmin; K <= kmax; K++) {
    int idx = 0;
    for (g = 1; 2 * g + 1 <= K - 1; g++)
      for (B = 1; 2 * g + B <= K - 1; B++, idx++) {
        if (idx < from || idx > to) continue;
        D = 2 * p - K + 2 * g; A = D + B; TOT = p - K + 2 * g;
        long long s0 = nsol, c0 = ncanon, r0 = nr, n0 = nnokill, f0 = nmixr_fail, b0 = nbk1_fail, e0 = nbk1_badcert;
        pd[0] = 0; pp[0] = 0;
        dfs(0, A, B, 0, 0, 0, 0, 0);
        printf("CNT p=%d k=%d g=%d B=%d idx=%d sol=%lld canon=%lld rstar=%lld nokill=%lld mixr_fail=%lld bk1_fail=%lld bk1_badcert=%lld\n", p, K, g, B, idx,
               nsol - s0, ncanon - c0, nr - r0, nnokill - n0, nmixr_fail - f0, nbk1_fail - b0, nbk1_badcert - e0);
        fflush(stdout);
      }
  }
  printf("TOTAL p=%d k=%d..%d sol=%lld canon=%lld philow=%lld rstar=%lld nokill=%lld mixr_ok=%lld mixr_fail=%lld bk1_ok=%lld bk1_fail=%lld bk1_badcert=%lld exact_runs=%lld\n",
         p, kmin, kmax, nsol, ncanon, nphilow, nr, nnokill, nmixr, nmixr_fail, nbk1, nbk1_fail, nbk1_badcert, nexact);
  return 0;
}
