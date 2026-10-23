// Exhaustive integer check of the case analysis of Lemma FLEXa (proof-SHgen-v2.md Sec. 3).  Not a premise.
// For every parameter tuple in the box below that satisfies the lemma's hypotheses, the lemma claims that the move
// (down) or the move (up) exists.  In scope means (K): k <= 2p - eta - a - 1 (a_max = a, the weakest form of (K)).
// Negative control: tuples violating (K) (all other hypotheses kept) are counted separately; failures there show that
// the check can fail and that (K) is used.
// Box: p in {5,7,11,13}; k in [2, 2p-1]; kappa in [max(0,k-p), p-1-(a-1)/2] (H = p-1-kappa >= (a-1)/2, R >= k);
// a odd in [3, p]; eta in [1, min(R, 3)]; Phi even in [0, k]; n + M = L1 = R - eta; Q = (i, vX, vY, |S|) with
// 1 <= i <= a-1, |S| <= eta-1, m = i + vX + vY + |S| even in [s0 + a - 1, s1], s0 = 2kappa+2-Phi, s1 = 2p-Phi.
// Usage: flexa_check_v1 > out.json
#include <cstdio>
#include <algorithm>
int main() {
  const int ps[] = {5, 7, 11, 13};
  long long inScope = 0, inFail = 0, outScope = 0, outFail = 0;
  for (int pi = 0; pi < 4; ++pi) {
    int p = ps[pi];
    long long pin = 0, pinf = 0, pout = 0, poutf = 0;
    for (int a = 3; a <= p; a += 2)
    for (int k = 2; k <= 2 * p - 1; ++k)
    for (int kappa = std::max(0, k - p); kappa <= p - 1 - (a - 1) / 2; ++kappa) {
      int R = 2 * p + 2 * kappa - k;
      if (R < k) continue;
      for (int eta = 1; eta <= std::min(R, 3); ++eta) {
        bool K = (k <= 2 * p - eta - a - 1);
        int L1 = R - eta;
        for (int Phi = 0; Phi <= k; Phi += 2) {
          int s0 = 2 * kappa + 2 - Phi, s1 = 2 * p - Phi;
          for (int n = 0; n <= L1; ++n) {
            int M = L1 - n;
            for (int i = 1; i <= a - 1; ++i)
            for (int S = 0; S <= eta - 1; ++S)
            for (int vX = 0; vX <= std::min(n, 2 * p); ++vX) {
              int lo = s0 + a - 1, hi = s1;
              for (int m = std::max(lo, 0); m <= hi; ++m) {
                if (m & 1) continue;
                int vY = m - i - vX - S;
                if (vY < 0) continue;
                if (vY > M) break;
                int uX = n - vX, uY = M - vY, d = m - s0, e = s1 - m;
                bool down = false, up = false;
                int r4lo = std::max(0, i - uX), r4hi = std::min(i, vY);
                if (r4lo <= r4hi && 2 * r4lo <= d) down = true;
                int r2lo = std::max(0, a - i - vX), r2hi = std::min(a - i, uY);
                if (r2lo <= r2hi && 1 - a + 2 * r2lo <= e) up = true;
                bool ok = down || up;
                if (K) { ++pin; if (!ok) ++pinf; } else { ++pout; if (!ok) ++poutf; }
              }
            }
          }
        }
      }
    }
    printf("{\"p\": %d, \"in_scope\": %lld, \"in_scope_fail\": %lld, \"out_of_scope\": %lld, \"out_of_scope_fail\": %lld}\n",
           p, pin, pinf, pout, poutf);
    fflush(stdout);
    inScope += pin; inFail += pinf; outScope += pout; outFail += poutf;
  }
  printf("{\"total_in_scope\": %lld, \"total_in_scope_fail\": %lld, \"total_out_of_scope\": %lld, \"total_out_of_scope_fail\": %lld}\n",
         inScope, inFail, outScope, outFail);
  return 0;
}
