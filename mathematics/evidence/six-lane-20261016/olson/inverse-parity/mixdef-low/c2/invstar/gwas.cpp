// gwas.cpp -- invstar P3: exact search for avoiders of length N among GENERALISED RGR words over D_(2p): rotations in
// {rho_1, rho_-1}, constant reflection blocks S_i = sigma_(y_i)^(l_i) separated by rotation runs R_i that may be EMPTY.
// Exact criterion: Lemma GR0 / WAS0 (invstar/proof-GR0.md): the word avoids iff for every P subset of [k]
// sum_{i in P} theta_i (mod p) is not in Ach(z_P) (mod p), theta_i = y_(i-1) - y_i; theta_i != 0 at every empty run
// (maximal blocks).  Value-independent filters, each a proved necessary condition for an avoider of length N <= 4p-1:
//   A, B <= 2p-1 (2p equal rotations);  H = sum floor(l_i/2) <= p-1 (p disjoint same-letter adjacent pairs);
//   (P) F + sum floor(r_i/2) <= 3p-2 (Theorem P, any word of length <= 4p-1, gaps = rotation runs incl. empty ones);
//   (V) F >= 2 => R + H <= 3p-2 (Davenport-alpha with the H pairwise non-adjacent within-block gaps).
// Every other condition (empty pattern, full windows, all P) is checked exactly by the WAS DFS.
// Normal forms (flags): M0 = 1: every rotation run pure or a (1,1)-pair (Lemma M0, pair removal, preserves avoidance and
// empty runs); PM = 1: every even block is adjacent to an empty rotation run (Lemma PM, merging across an even block whose
// two neighbouring rotation runs are nonempty, preserves avoidance and all empty runs).  A >= B by the automorphism
// v -> -v.  Rotation-canonical run data (lexicographically least rotation).  MUT = 1: every nonempty window loses its
// top element (weaker constraints -> spurious candidates that raw DP must reject).
// Usage: gwas p N kmin kmax M0 PM MUT
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <cstdint>
#include <algorithm>
using namespace std;
static int p, N, K, M0, PMF, MUT;
static int ra[24], rb[24], rl[24];
static uint32_t Wm[1 << 20];
static int sums[1 << 20];
static int th[24];
static long long ndata = 0, ndata_full = 0, nav = 0, nnodes = 0;
static bool canonical() {
  for (int s = 1; s < K; s++) {
    for (int i = 0; i < K; i++) {
      int j = (i + s) % K;
      int x1[3] = {ra[j], rb[j], rl[j]}, x0[3] = {ra[i], rb[i], rl[i]};
      for (int c = 0; c < 3; c++) if (x1[c] != x0[c]) { if (x1[c] < x0[c]) return false; goto next; }
    }
    next:;
  }
  return true;
}
static void dfs(int t) {
  nnodes++;
  if (t == K - 1) {
    int s = 0; for (int i = 0; i < K - 1; i++) s += th[i];
    int v = ((-s) % p + p) % p;
    if (ra[t] + rb[t] == 0 && v == 0) return;
    th[t] = v;
    uint32_t top = 1u << t;
    for (uint32_t P = 0; P < top; P++) {
      int sm = (sums[P] + v) % p;
      if (Wm[P | top] >> sm & 1u) return;
    }
    nav++;
    if (nav <= 400) {
      printf("AVOID p=%d N=%d k=%d a=", p, N, K);
      for (int i = 0; i < K; i++) printf("%d%s", ra[i], i + 1 < K ? "," : "");
      printf(" b="); for (int i = 0; i < K; i++) printf("%d%s", rb[i], i + 1 < K ? "," : "");
      printf(" l="); for (int i = 0; i < K; i++) printf("%d%s", rl[i], i + 1 < K ? "," : "");
      printf(" theta="); for (int i = 0; i < K; i++) printf("%d%s", th[i], i + 1 < K ? "," : "");
      printf("\n");
    }
    return;
  }
  uint32_t top = 1u << t;
  for (int v = 0; v < p; v++) {
    if (ra[t] + rb[t] == 0 && v == 0) continue;
    bool ok = true;
    for (uint32_t P = 0; P < top; P++) {
      int sm = (sums[P] + v) % p;
      sums[P | top] = sm;
      if (Wm[P | top] >> sm & 1u) { ok = false; break; }
    }
    if (!ok) continue;
    th[t] = v;
    dfs(t + 1);
  }
}
static void process(int A, int B, int F, int R, int H) {
  bool hasEmpty = false; for (int i = 0; i < K; i++) if (ra[i] + rb[i] == 0) hasEmpty = true;
  if (!hasEmpty || R < 1) return;
  if (A < B) return;
  int sumfl = 0; for (int i = 0; i < K; i++) sumfl += (ra[i] + rb[i]) / 2;
  if (F + sumfl > 3 * p - 2) return;                 // (P)
  if (F >= 2 && R + H > 3 * p - 2) return;          // (V)
  if (PMF) for (int i = 0; i < K; i++) if (rl[i] % 2 == 0) {
    int j = (i + 1) % K;                               // S_i lies between R_i and R_(i+1)
    if (ra[i] + rb[i] > 0 && ra[j] + rb[j] > 0) return;
  }
  if (!canonical()) return;
  ndata++;
  uint32_t full = (K == 32) ? 0xffffffffu : ((1u << K) - 1);
  for (uint32_t P = 0; P <= full; P++) {
    int Phi = 0, delta = 0, Ep = 0;
    for (int i = 0; i < K; i++) {
      int zi = (P >> i) & 1, zj = (P >> ((i + 1) % K)) & 1;
      int f = (zi != zj);
      Phi += f;
      if ((rl[i] - f) % 2 != 0) delta++;
      Ep += zi ? ra[i] : rb[i];
    }
    int Em = R - Ep, Cmax = F - delta, s0 = 2 * p - Cmax, s1 = 2 * p - Phi;
    int lo = max(-s1, max(s0 - 2 * Em, -Em)), hi = min(s1, min(2 * Ep - s0, Ep));
    if (lo % 2) lo++;
    if (hi % 2) hi--;
    if (MUT && lo <= hi) hi -= 2;
    uint32_t m = 0;
    if (lo <= hi) {
      if ((hi - lo) / 2 + 1 >= p) { ndata_full++; return; }
      for (int t2 = lo; t2 <= hi; t2 += 2) m |= 1u << (((t2 % p) + p) % p);
    }
    Wm[P] = m;
  }
  if (Wm[0] & 1u) return;              // empty pattern: sum 0
  sums[0] = 0;
  dfs(0);
}
static void gen(int i, int used, int A, int B, int F, int R, int H) {
  if (i == K) { if (used == N) process(A, B, F, R, H); return; }
  int left = K - i;                      // runs still to place, each needs a block >= 1
  // rotation part options
  vector<pair<int,int>> opts;
  opts.push_back({0, 0});
  for (int a = 1; a <= 2 * p - 1 - A; a++) opts.push_back({a, 0});
  for (int b = 1; b <= 2 * p - 1 - B; b++) opts.push_back({0, b});
  if (M0) { if (A + 1 <= 2 * p - 1 && B + 1 <= 2 * p - 1) opts.push_back({1, 1}); }
  else for (int a = 1; a <= 2 * p - 1 - A; a++) for (int b = 1; b <= 2 * p - 1 - B; b++) opts.push_back({a, b});
  for (auto& o : opts) {
    int r = o.first + o.second;
    if (used + r + left > N) continue;
    int nA = A + o.first, nB = B + o.second;
    for (int l = 1; used + r + l + (left - 1) <= N; l++) {
      int nH = H + l / 2;
      if (nH > p - 1) break;
      if (nB > p - 1 - nH) break;        // zero condition B <= kappa = p - 1 - H (B, H only grow)
      ra[i] = o.first; rb[i] = o.second; rl[i] = l;
      gen(i + 1, used + r + l, nA, nB, F + l, R + r, nH);
    }
  }
}
int main(int argc, char** argv) {
  p = atoi(argv[1]); N = atoi(argv[2]); int kmin = atoi(argv[3]), kmax = atoi(argv[4]);
  M0 = atoi(argv[5]); PMF = atoi(argv[6]); MUT = atoi(argv[7]);
  for (K = kmin; K <= kmax; K++) {
    long long d0 = ndata, a0 = nav, f0 = ndata_full;
    gen(0, 0, 0, 0, 0, 0, 0);
    printf("CNT p=%d N=%d k=%d data=%lld fullwindow=%lld avoiders=%lld\n", p, N, K, ndata - d0, ndata_full - f0, nav - a0);
    fflush(stdout);
  }
  printf("TOTAL p=%d N=%d k=%d..%d M0=%d PM=%d MUT=%d data=%lld fullwindow=%lld avoiders=%lld nodes=%lld\n",
         p, N, kmin, kmax, M0, PMF, MUT, ndata, ndata_full, nav, nnodes);
  return 0;
}
