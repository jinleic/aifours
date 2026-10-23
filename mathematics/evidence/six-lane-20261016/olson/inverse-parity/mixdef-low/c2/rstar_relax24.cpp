// rstar_relax24.cpp (= relax23 with per-run pruning bh_t <= s := k-1-2g-B (Lemma C) and R4 test: R*** + c(Z0+) <= g) (= relax22 + per-run pruning bh_t <= B, i.e. phi_t >= ceil((d_t - B)/2): a necessary condition of R***) (= relax19 + counts R*** members: all bh <= B, not all cheap, 2 phi(Z0+) + alpha >= 2g + s + S_Z; prints them) (= relax18 restricted to B <= g via argv[6]=1; also with argv[4]=0 for no B2 restriction) (= relax17 + classification: Ksplit (#cheap_all >= 2g+2, cheap over all runs), Kfree (free weighted indep >= g+1), K1 (#cheap_all >= 2g+1 and B >= g+1); prints configs with none) (= relax16 + test F: free-only (phi >= 0, bh <= 0) weighted independent set with weight >= g+1; histogram of #cheap-(2g+2) and W(free)-(2g+2) on test-A failures) -- RELAXED census + tests: (a) cheap-split with T = argmax bh, (c) cheap-only weighted independent KL (DP) (research aid): like rstar_census8 (B2 flag, R*-pruning) but the
// Lemma S interval constraints are imposed only for intervals Q with |Q| <= ML or |Q| >= k - ML
// (each constraint is two-sided, Q <-> Q^c).  Counts R* configurations (rotation-canonical).
// Usage: rstar_relax14 p kmin kmax caseB2 ML
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <cstdint>
using namespace std;
static int p, K, g, B, D, A, TOT, ML, CASEB2, BLEG = 0;
static int d[32], ph[32], pd[33], pp[33];
static long long nsol = 0, ncanon = 0, nr = 0, na = 0, nc_ = 0, nf_ = 0, nfail_print = 0; static long long hist2[19][30]; static long long nks = 0, nk1 = 0, nnone = 0, nnone_print = 0, nr3 = 0;
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
    {
      int s = K - 1 - 2 * g - B; int phZ0p = 0, alpha = 0, SZ = 0, ncheap = 0, maxbh = -100;
      for (int t = 0; t < K; t++) { if (bh[t] > maxbh) maxbh = bh[t]; if (ph[t] >= 0 && bh[t] <= 1) ncheap++;
        if (bh[t] <= 0) { if (ph[t] >= 0) { phZ0p += ph[t]; if (d[t] < 0) alpha++; } if (d[t] > 0) SZ += d[t] - 1; } }
      // c(Z0+) = phi(Z0+) + blocks(Z0+)
      uint32_t Zp = 0; for (int t = 0; t < K; t++) if (bh[t] <= 0 && ph[t] >= 0) Zp |= 1u << t;
      int cZp = phZ0p + blocks(Zp, K);
      bool r3 = (maxbh <= s) && (ncheap < K) && (2 * phZ0p + alpha >= 2 * g + s + SZ) && (cZp <= g);
      if (r3) { nr3++;
        if (nr3 <= 30) { printf("R3 p=%d k=%d g=%d B=%d s=%d Phi=%d m=%d d=", p, K, g, B, s, Phi, m);
          for (int t = 0; t < K; t++) printf("%d%s", d[t], t + 1 < K ? "," : "");
          printf(" phi="); for (int t = 0; t < K; t++) printf("%d%s", ph[t], t + 1 < K ? "," : "");
          printf("\n"); } }
    }
    // (a) T = argmax bh; cheap = {t != T : phi >= 0, bh <= 1}; need #cheap >= 2g+2 and BH(cheap) <= 2B+1
    int T = 0; for (int t = 1; t < K; t++) if (bh[t] > bh[T]) T = t;
    int nch = 0, bhc = 0;
    for (int t = 0; t < K; t++) if (t != T && ph[t] >= 0 && bh[t] <= 1) { nch++; bhc += bh[t]; }
    bool ta = (nch >= 2 * g + 2) && (bhc <= 2 * B + 1);
    if (ta) na++;
    // (c) cheap-only weighted independent set: max over independent S of cheap with BH(S) <= B of sum(phi+1) >= g+1
    // DP over cycle with budget dimension (BH can be negative: offset)
    bool tc = false;
    {
      const int OFF = 64, W = 129; const int NEG = -1000000;
      static int f[2][W], nf[2][W];
      for (int first = 0; first <= 1 && !tc; first++) {
        bool ch0 = ph[0] >= 0 && bh[0] <= 1 && ph[0] <= g - 1;
        if (first && !ch0) continue;
        for (int a = 0; a < 2; a++) for (int b = 0; b < W; b++) f[a][b] = NEG;
        if (first) f[1][OFF + bh[0]] = ph[0] + 1; else f[0][OFF] = 0;
        for (int i = 1; i < K; i++) {
          bool ch = ph[i] >= 0 && bh[i] <= 1 && ph[i] <= g - 1 && !(first && i == K - 1);
          for (int a = 0; a < 2; a++) for (int b = 0; b < W; b++) nf[a][b] = NEG;
          for (int a = 0; a < 2; a++) for (int b = 0; b < W; b++) {
            int v = f[a][b]; if (v == NEG) continue;
            if (v > nf[0][b]) nf[0][b] = v;
            if (ch && !a) { int nb = b + bh[i]; if (nb >= 0 && nb < W && v + ph[i] + 1 > nf[1][nb]) nf[1][nb] = v + ph[i] + 1; }
          }
          for (int a = 0; a < 2; a++) for (int b = 0; b < W; b++) f[a][b] = nf[a][b];
        }
        for (int a = 0; a < 2 && !tc; a++) for (int b = 0; b <= OFF + B && b < W; b++) if (f[a][b] >= g + 1) { tc = true; break; }
      }
    }
    if (tc) nc_++;
    bool tf = false;
    {
      // max weight independent set on cycle among free elements (phi>=0, bh<=0)
      long long best = 0;
      for (int first = 0; first <= 1; first++) {
        bool el0 = ph[0] >= 0 && bh[0] <= 0;
        if (first && !el0) continue;
        long long f0 = first ? -1000000 : 0, f1 = first ? ph[0] + 1 : -1000000;
        for (int i = 1; i < K; i++) {
          bool el = ph[i] >= 0 && bh[i] <= 0 && !(first && i == K - 1);
          long long n0 = max(f0, f1), n1 = el ? f0 + ph[i] + 1 : -1000000;
          f0 = n0; f1 = n1;
        }
        best = max(best, max(f0, f1));
      }
      tf = best >= g + 1;
    }
    if (tf) nf_++;
    {
      int ncall = 0; for (int t = 0; t < K; t++) if (ph[t] >= 0 && bh[t] <= 1) ncall++;
      bool ks = ncall >= 2 * g + 2; bool k1 = (ncall >= 2 * g + 1) && (B >= g + 1);
      if (ks) nks++; if (k1) nk1++;
      if (!ks && !tf && !k1) { nnone++;
        if (nnone_print < 40) { nnone_print++;
          int alpha = 0, beta = 0; for (int t = 0; t < K; t++) if (d[t] < 0 && bh[t] <= 0) { if (ph[t] >= 0) alpha++; else beta++; }
          printf("NONE ncall=%d alpha=%d beta=%d s=%d p=%d k=%d g=%d B=%d Phi=%d m=%d Yal=%d aZ=%d d=", ncall, alpha, beta, K - 1 - 2 * g - B, p, K, g, B, Phi, m, Yal, aZ);
          for (int t = 0; t < K; t++) printf("%d%s", d[t], t + 1 < K ? "," : "");
          printf(" phi="); for (int t = 0; t < K; t++) printf("%d%s", ph[t], t + 1 < K ? "," : "");
          printf("\n"); } }
    }
    if (!ta) { int wfree = 0; for (int t = 0; t < K; t++) if (ph[t] >= 0 && bh[t] <= 0) wfree += ph[t] + 1;
      int hx = nch - (2 * g + 2); if (hx < -9) hx = -9; if (hx > 9) hx = 9; int hy = wfree - (2 * g + 2); if (hy < -9) hy = -9; if (hy > 20) hy = 20;
      hist2[hx + 9][hy + 9]++; }
    if ((!tc) && nfail_print < 60) { nfail_print++;
      printf("FAIL a=%d c=%d nch=%d bhc=%d ", (int)ta, (int)tc, nch, bhc);
      printf("p=%d k=%d g=%d B=%d Phi=%d m=%d Yal=%d aZ=%d d=", p, K, g, B, Phi, m, Yal, aZ);
      for (int t = 0; t < K; t++) printf("%d%s", d[t], t + 1 < K ? "," : "");
      printf(" phi="); for (int t = 0; t < K; t++) printf("%d%s", ph[t], t + 1 < K ? "," : "");
      printf("\n");
    }
    if (nr <= 0) {
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
      if (x - 2 * v > K - 1 - 2 * g - B) continue;
      ph[t] = v; pp[t + 1] = pp[t] + v;
      report();
      continue;
    }
    if (L < -3 * p) L = -3 * p; if (H > 3 * p) H = 3 * p;   // finite box (relaxation may be unbounded)
    { int sK = K - 1 - 2 * g - B; int lb = fdiv(x - sK + 1, 2); if (L < lb) L = lb; }   // bh = x - 2v <= s  <=>  v >= ceil((x - s)/2)
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
  CASEB2 = atoi(argv[4]); ML = atoi(argv[5]); BLEG = argc > 6 ? atoi(argv[6]) : 0;
  for (K = kmin; K <= kmax; K++)
    for (g = 1; 2 * g + 1 <= K - 1; g++)
      for (B = 1; 2 * g + B <= K - 1; B++) {
        if (BLEG && B > g) continue;
        D = 2 * p - K + 2 * g; A = D + B; TOT = p - K + 2 * g;
        long long r0 = nr;
        pd[0] = 0; pp[0] = 0;
        dfs(0, A, B, 0, 0, 0, 0, 0);
        if (nr > r0) printf("CNT p=%d k=%d g=%d B=%d rstar=%lld\n", p, K, g, B, nr - r0);
        fflush(stdout);
      }
  printf("TOTAL p=%d ML=%d caseB2=%d canon=%lld rstar=%lld R3=%lld testA=%lld testC=%lld testF=%lld Ksplit=%lld K1=%lld none=%lld\n", p, ML, CASEB2, ncanon, nr, nr3, na, nc_, nf_, nks, nk1, nnone);
  for (int i = 0; i < 19; i++) for (int j = 0; j < 30; j++) if (hist2[i][j]) printf("HISTA nch-(2g+2)=%d Wfree-(2g+2)=%d n=%lld\n", i - 9, j - 9, hist2[i][j]);
  return 0;
}
