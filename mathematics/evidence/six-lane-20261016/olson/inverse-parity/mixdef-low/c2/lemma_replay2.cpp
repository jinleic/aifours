// lemma_replay2.cpp -- (adds Lemma KS, Lemma AC, Lemma G1 checks inside R*) replays the written constructions of proof-Rstar (c2) on EVERY interval-feasible
// configuration (same joint DFS as rstar_census4.cpp: all (d, phi) with the Lemma S interval system), and
// checks each produced pattern with the exact mod-p window test of Lemma H.
//   W  : Lemma W (B >= g+1): max-weight independent set of cheap runs (phi >= 0, bh <= 1), trimmed by
//        decreasing weight to weight >= g+1, then the KL prefix (bh <= 0 first, index order) with c >= g+1.
//   B1 : Lemma B1 (some d_T >= 2p-B): parity class of the path [k]\{T} with larger total weight,
//        its phi >= 0 elements, KL prefix.
//   A  : Theorem A (R*, some bh_T >= B+1, T = first argmax bh): cheap runs on the path [k]\{T},
//        balanced alternating split U/V, the one with BH <= B, KL prefix.
//   Also: Wcheap >= 2g+1 for every configuration (Lemma W, Step 1), and the KL hypotheses.
// MUT=1 mutation: the exact window test uses G_m - 1 (shrunk windows) -> some replays must fail.
// Usage: lemma_replay p kmin kmax MUT
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstdint>
using namespace std;
static int p, K, g, B, D, A, TOT, MUT;
static int d[32], ph[32], pd[33], pp[33], bh[32];
static long long nRS = 0, nG1_viol = 0, nAC = 0, nAC_fail = 0, nKS = 0, nKS_fail = 0, nKS_countfail = 0, nKS_bhfail = 0;
static long long ncfg = 0, nW = 0, nW_fail = 0, nB1 = 0, nB1_fail = 0, nA = 0, nA_fail = 0, nWc_fail = 0, nhyp_fail = 0;
static inline int fdiv(int a, int b) { return (a >= 0) ? a / b : -((-a + b - 1) / b); }
static inline int gam(int E) { int a = E - p, b = g - 1, c = fdiv(E - B - 1, 2); return max(a, max(b, c)); }
static inline int Gm(int m, int E) { int a = p - m, b = E - g + m - 1, c = fdiv(E + B, 2); return min(a, min(b, c)) - (MUT ? 1 : 0); }
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
// KL: S proper, phi <= g-1 on S, c(S) >= g+1, BH(S) <= B. Returns exact-test result of the KL prefix.
static bool KL(uint32_t S) {
  uint32_t full = (1u << K) - 1;
  if (S == 0 || S == full) { nhyp_fail++; return false; }
  int f = 0, b = 0;
  for (int t = 0; t < K; t++) if (S >> t & 1) { if (ph[t] > g - 1) { nhyp_fail++; return false; } f += ph[t]; b += bh[t]; }
  if (f + blocks(S, K) < g + 1 || b > B) { nhyp_fail++; return false; }
  int order[32], no = 0;
  for (int t = 0; t < K; t++) if ((S >> t & 1) && bh[t] <= 0) order[no++] = t;
  for (int t = 0; t < K; t++) if ((S >> t & 1) && bh[t] > 0) order[no++] = t;
  uint32_t Q = 0;
  for (int i = 0; i < no; i++) {
    Q |= 1u << order[i];
    int ff = 0; for (int t = 0; t < K; t++) if (Q >> t & 1) ff += ph[t];
    int c = ff + blocks(Q, K);
    if (c >= g + 1) {
      if (c > 2 * g) { nhyp_fail++; return false; }
      return killsP(Q);
    }
  }
  nhyp_fail++; return false;
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
static void report() {
  if (!canonical()) return;
  ncfg++;
  uint32_t full = (1u << K) - 1;
  for (int t = 0; t < K; t++) bh[t] = d[t] - 2 * ph[t];
  // cheap and weights
  int Wc = 0; uint32_t cheap = 0;
  for (int t = 0; t < K; t++) if (ph[t] >= 0 && bh[t] <= 1) { cheap |= 1u << t; Wc += ph[t] + 1; }
  if (Wc < 2 * g + 1) nWc_fail++;
  // ---- Lemma W
  if (B >= g + 1) {
    nW++;
    uint32_t best = 0; int bestw = -1;
    if (cheap == full) {
      // drop the minimum-weight run t0, alternate on the path
      int t0 = 0; for (int t = 1; t < K; t++) if (ph[t] < ph[t0]) t0 = t;
      uint32_t U = 0, V = 0; int wu = 0, wv = 0;
      for (int j = 1; j < K; j++) { int t = (t0 + j) % K; if (j % 2) { U |= 1u << t; wu += ph[t] + 1; } else { V |= 1u << t; wv += ph[t] + 1; } }
      if (wu >= wv) { best = U; bestw = wu; } else { best = V; bestw = wv; }
    } else {
      // paths of cheap runs: for each maximal path take the heavier parity class
      int start = 0; while ((cheap >> start) & 1) start++;   // a non-cheap position
      int j = 1;
      while (j <= K) {
        int t = (start + j) % K;
        if (!((cheap >> t) & 1)) { j++; continue; }
        // collect path
        int path[32], n = 0;
        while (j <= K && ((cheap >> ((start + j) % K)) & 1)) { path[n++] = (start + j) % K; j++; }
        int wo = 0, we = 0; uint32_t mo = 0, me = 0;
        for (int i = 0; i < n; i++) { if (i % 2 == 0) { wo += ph[path[i]] + 1; mo |= 1u << path[i]; } else { we += ph[path[i]] + 1; me |= 1u << path[i]; } }
        if (wo >= we) { best |= mo; } else { best |= me; }
      }
      bestw = 0; for (int t = 0; t < K; t++) if (best >> t & 1) bestw += ph[t] + 1;
    }
    // trim by decreasing weight to weight >= g+1
    int idx[32], ni = 0; for (int t = 0; t < K; t++) if (best >> t & 1) idx[ni++] = t;
    sort(idx, idx + ni, [](int a, int b) { return ph[a] > ph[b] || (ph[a] == ph[b] && a < b); });
    uint32_t S = 0; int w = 0;
    for (int i = 0; i < ni && w < g + 1; i++) { S |= 1u << idx[i]; w += ph[idx[i]] + 1; }
    if (!(w >= g + 1 && KL(S))) nW_fail++;
  }
  // ---- Lemma B1
  int T = -1; for (int t = 0; t < K; t++) if (d[t] >= 2 * p - B) { T = t; break; }
  if (T >= 0) {
    nB1++;
    uint32_t O = 0, E = 0; int wo = 0, we = 0;
    for (int j = 1; j < K; j++) { int t = (T + j) % K; if (j % 2) { O |= 1u << t; wo += ph[t] + 1; } else { E |= 1u << t; we += ph[t] + 1; } }
    uint32_t X = (wo >= we) ? O : E; uint32_t S = 0;
    for (int t = 0; t < K; t++) if ((X >> t & 1) && ph[t] >= 0) S |= 1u << t;
    if (!KL(S)) nB1_fail++;
  }
  // ---- Theorem A (only in R*)
  uint32_t Z = 0; for (int t = 0; t < K; t++) if (bh[t] <= 0) Z |= 1u << t;
  int m = blocks(Z, K); int Phi = 2 * m, Yal = 0, aZ = 0;
  for (int t = 0; t < K; t++) { if (Z >> t & 1) { Phi += 2 * ph[t]; aZ += d[t] - 1; } else if (d[t] >= 1) Yal++; }
  bool rs = (Phi <= 2 * g + 1) && (Yal + aZ <= 2);
  if (rs) {
    nRS++;
    // Lemma G1: g = 1 and all aligned d <= B + 2 must not occur in R*
    bool allsmall = true; for (int t = 0; t < K; t++) if (d[t] > B + 2) allsmall = false;
    if (g == 1 && allsmall) nG1_viol++;
    // Lemma AC: every run cheap
    if (cheap == full) {
      nAC++;
      int s = K - 1 - 2 * g - B; uint32_t S = 0;
      if (B + s >= 2) {
        int t0 = -1; for (int t = 0; t < K; t++) if (bh[t] == 1) { t0 = t; break; }
        uint32_t U = 0, V = 0; for (int j = 1; j < K; j++) { int t = (t0 + j) % K; if (j % 2) U |= 1u << t; else V |= 1u << t; }
        int bu = 0, bv = 0; for (int t = 0; t < K; t++) { if (U >> t & 1) bu += bh[t]; if (V >> t & 1) bv += bh[t]; }
        S = (bu <= bv) ? U : V;
      } else {
        uint32_t O = 0, E = 0; for (int t = 0; t < K; t++) { if (t % 2 == 0) O |= 1u << t; else E |= 1u << t; }
        int bo = 0, be = 0; for (int t = 0; t < K; t++) { if (O >> t & 1) bo += bh[t]; if (E >> t & 1) be += bh[t]; }
        S = (bo <= be) ? O : E;
      }
      if (!KL(S)) nAC_fail++;
    } else {
      // Lemma KS hypothesis: 2 phi(Z0+) + alpha <= 2g + s - 1 + S_Z
      int s = K - 1 - 2 * g - B; int phZ0p = 0, alpha = 0, SZ = 0;
      for (int t = 0; t < K; t++) if (bh[t] <= 0) { if (ph[t] >= 0) { phZ0p += ph[t]; if (d[t] < 0) alpha++; } if (d[t] > 0) SZ += d[t] - 1; }
      if (2 * phZ0p + alpha <= 2 * g + s - 1 + SZ) {
        nKS++;
        // balanced alternating split of cheap runs on the cycle (paths)
        int start = 0; while ((cheap >> start) & 1) start++;
        uint32_t U = 0, V = 0; int toggle = 0; int j = 1; int ncheap = 0;
        while (j <= K) {
          int t = (start + j) % K;
          if (!((cheap >> t) & 1)) { j++; continue; }
          int path[32], n = 0;
          while (j <= K && ((cheap >> ((start + j) % K)) & 1)) { path[n++] = (start + j) % K; j++; }
          ncheap += n;
          int first = (n % 2 == 1) ? toggle : 0; if (n % 2 == 1) toggle ^= 1;
          for (int i = 0; i < n; i++) { bool toU = ((i % 2) == 0) ^ (first == 1); if (toU) U |= 1u << path[i]; else V |= 1u << path[i]; }
        }
        if (ncheap < 2 * g + 2) nKS_countfail++;
        int bu = 0, bv = 0; for (int t = 0; t < K; t++) { if (U >> t & 1) bu += bh[t]; if (V >> t & 1) bv += bh[t]; }
        if (bu + bv > 2 * B + 1) nKS_bhfail++;
        uint32_t S = (bu <= bv) ? U : V;
        if (!KL(S)) nKS_fail++;
      }
    }
  }
  int TA = 0; for (int t = 1; t < K; t++) if (bh[t] > bh[TA]) TA = t;
  if (rs && bh[TA] >= B + 1) {
    nA++;
    // cheap on path [k]\{TA}; blocks; alternate with balancing
    uint32_t U = 0, V = 0; int nu = 0, nv = 0; int toggle = 0;
    int j = 1;
    while (j < K) {
      int t = (TA + j) % K;
      if (!((cheap >> t) & 1) || t == TA) { j++; continue; }
      int path[32], n = 0;
      while (j < K && ((cheap >> ((TA + j) % K)) & 1)) { path[n++] = (TA + j) % K; j++; }
      int first = (n % 2 == 1) ? toggle : 0; if (n % 2 == 1) toggle ^= 1;
      for (int i = 0; i < n; i++) { bool toU = ((i % 2) == 0) ^ (first == 1); if (toU) { U |= 1u << path[i]; nu++; } else { V |= 1u << path[i]; nv++; } }
    }
    int bu = 0, bv = 0; for (int t = 0; t < K; t++) { if (U >> t & 1) bu += bh[t]; if (V >> t & 1) bv += bh[t]; }
    uint32_t S = (bu <= bv) ? U : V;
    if (!KL(S)) nA_fail++;
  }
}
static void dfs(int t, int Arem, int Brem) {
  int left = K - t;
  if (left == 0) return;
  if (Arem + Brem < left) return;
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
      L = max(L, TOT - gam(D - E) - base); H = min(H, gam(E) - base);
    }
    if (t == K - 1) {
      int v = TOT - pp[t];
      if (v < L || v > H) continue;
      ph[t] = v; pp[t + 1] = pp[t] + v;
      report();
      continue;
    }
    for (int v = L; v <= H; v++) { ph[t] = v; pp[t + 1] = pp[t] + v; dfs(t + 1, nA, nB); }
  }
}
int main(int argc, char** argv) {
  p = atoi(argv[1]); int kmin = atoi(argv[2]), kmax = atoi(argv[3]); MUT = argc > 4 ? atoi(argv[4]) : 0;
  for (K = kmin; K <= kmax; K++)
    for (g = 1; 2 * g + 1 <= K - 1; g++)
      for (B = 1; 2 * g + B <= K - 1; B++) {
        D = 2 * p - K + 2 * g; A = D + B; TOT = p - K + 2 * g;
        pd[0] = 0; pp[0] = 0; dfs(0, A, B);
      }
  printf("REPLAY2 Rstar=%lld G1_violations=%lld AC:%lld/%lld_fail KS:%lld/%lld_fail (count<2g+2: %lld, BH>2B+1: %lld)\n", nRS, nG1_viol, nAC, nAC_fail, nKS, nKS_fail, nKS_countfail, nKS_bhfail);
  printf("REPLAY p=%d k=%d..%d mut=%d configs=%lld Wcheap_fail=%lld W:%lld/%lld_fail B1:%lld/%lld_fail A:%lld/%lld_fail KLhyp_fail=%lld\n",
         p, kmin, kmax, MUT, ncfg, nWc_fail, nW, nW_fail, nB1, nB1_fail, nA, nA_fail, nhyp_fail);
  return 0;
}
