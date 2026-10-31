// Exhaustive check of the six-zero parity exclusion (frontier-20261029-sixzero-exclusion-v1.md).
// K = F_2^8 with an alternating form B of rank 8 or rank 6 (radical spanned by e7,e8), optional quadratic q
// with polar B.  Family F = all 5-dim L <= K with rank(B|L) <= 2 (enumerated from all 97155 5-dim subspaces).
// Necessary condition (adopted f131 coset-parity tool, |Z|=6 < 8 cosets): every coset of every L in F
// contains an even number of points of Z.  The program enumerates every 6-set Z with 0 in Z and
// XOR(Z)=0 (degree<=6), optionally restricted to {q=0}, and counts the sets satisfying the condition.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iostream>
#include <string>
#include <vector>

static int B[8][8];
static int par(unsigned x) { return __builtin_popcount(x) & 1; }
static int Bf(int a, int b) { int s = 0; for (int i = 0; i < 8; ++i) if ((a >> i) & 1) for (int j = 0; j < 8; ++j) if ((b >> j) & 1) s ^= B[i][j]; return s; }

int main(int argc, char** argv) {
  if (argc != 4) { std::cerr << "usage: exhaust MODE(rank8|rank6) QTYPE(none|q0|q1) OUT\n"; return 2; }
  std::string mode = argv[1], qt = argv[2];
  { std::ifstream chk(argv[3]); if (chk.good()) { std::cerr << "refusing to overwrite\n"; return 2; } }
  for (int i = 0; i < 8; ++i) for (int j = 0; j < 8; ++j) B[i][j] = 0;
  int pairs = (mode == "rank8") ? 4 : 3;
  for (int p = 0; p < pairs; ++p) { B[2 * p][2 * p + 1] = B[2 * p + 1][2 * p] = 1; }
  // quadratic q with polar B: q = sum x_{2p} x_{2p+1} (+ radical linear part for rank6 q1: x_6)
  auto q = [&](int a) { int v = 0; for (int p = 0; p < pairs; ++p) v ^= ((a >> (2 * p)) & 1) & ((a >> (2 * p + 1)) & 1); if (mode == "rank6" && qt == "q1") v ^= (a >> 6) & 1; return v; };
  // enumerate 5-dim subspaces via RREF over 8 coordinates
  std::vector<std::array<uint8_t, 256>> fam;
  std::vector<int> piv(5);
  long long total5 = 0;
  std::function<void(int, int)> rec = [&](int i, int st) {
    if (i == 5) {
      std::vector<std::vector<int>> fr(5); int tb = 0;
      for (int a = 0; a < 5; ++a) { for (int x = 0; x < 8; ++x) if (x > piv[a] && std::find(piv.begin(), piv.end(), x) == piv.end()) fr[a].push_back(x); tb += (int)fr[a].size(); }
      for (long long mask = 0; mask < (1LL << tb); ++mask) {
        int g[5]; int b = 0;
        for (int a = 0; a < 5; ++a) { int v = 1 << piv[a]; for (int x : fr[a]) { if ((mask >> b) & 1) v |= 1 << x; ++b; } g[a] = v; }
        ++total5;
        // rank of B restricted to L (5x5 Gram matrix rank over F2)
        int M[5]; for (int a = 0; a < 5; ++a) { M[a] = 0; for (int c = 0; c < 5; ++c) if (Bf(g[a], g[c])) M[a] |= 1 << c; }
        int rk = 0; for (int col = 0; col < 5; ++col) { int pr = -1; for (int r = rk; r < 5; ++r) if ((M[r] >> col) & 1) { pr = r; break; } if (pr < 0) continue; std::swap(M[rk], M[pr]); for (int r = 0; r < 5; ++r) if (r != rk && ((M[r] >> col) & 1)) M[r] ^= M[rk]; ++rk; }
        if (rk > 2) continue;
        // coset labels: choose 3 functionals vanishing on L: complement coordinates via reduced form
        std::array<uint8_t, 256> lab{};
        // build L span and label cosets by canonical minimal representative index
        std::vector<int> Ls = {0}; for (int a = 0; a < 5; ++a) { int n = (int)Ls.size(); for (int t = 0; t < n; ++t) Ls.push_back(Ls[t] ^ g[a]); }
        std::vector<int> rep(256, -1); int nc = 0;
        for (int x = 0; x < 256; ++x) if (rep[x] < 0) { for (int l : Ls) rep[x ^ l] = nc; ++nc; }
        for (int x = 0; x < 256; ++x) lab[x] = (uint8_t)rep[x];
        fam.push_back(lab);
      }
      return;
    }
    for (int x = st; x < 8; ++x) { piv[i] = x; rec(i + 1, x + 1); }
  };
  rec(0, 0);
  long long sets = 0, survivors = 0; std::vector<std::array<int, 6>> surv;
  std::vector<int> pts; for (int a = 1; a < 256; ++a) if (qt == "none" || q(a) == 0) pts.push_back(a);
  int n = (int)pts.size();
  for (int i1 = 0; i1 < n; ++i1) for (int i2 = i1 + 1; i2 < n; ++i2) for (int i3 = i2 + 1; i3 < n; ++i3) for (int i4 = i3 + 1; i4 < n; ++i4) {
    int z5 = pts[i1] ^ pts[i2] ^ pts[i3] ^ pts[i4];
    if (z5 <= pts[i4]) continue;                       // distinct, ordered, nonzero
    if (qt != "none" && q(z5) != 0) continue;
    ++sets;
    int Z[6] = {0, pts[i1], pts[i2], pts[i3], pts[i4], z5};
    bool viol = false;
    for (const auto& lab : fam) { unsigned pv = 0; for (int t = 0; t < 6; ++t) pv ^= 1u << lab[Z[t]]; if (pv) { viol = true; break; } }
    if (!viol) { ++survivors; if (surv.size() < 20) surv.push_back({Z[0], Z[1], Z[2], Z[3], Z[4], Z[5]}); }
  }
  std::ofstream out(argv[3]);
  out << "{\n  \"mode\": \"" << mode << "\",\n  \"q\": \"" << qt << "\",\n  \"five_dim_subspaces\": " << total5 << ",\n  \"family_rank_le_2\": " << fam.size()
      << ",\n  \"six_sets_tested\": " << sets << ",\n  \"survivors\": " << survivors << ",\n  \"survivor_examples\": [";
  for (size_t t = 0; t < surv.size(); ++t) { out << (t ? ", " : "") << "[" << surv[t][0]; for (int u = 1; u < 6; ++u) out << ", " << surv[t][u]; out << "]"; }
  out << "]\n}\n";
  std::cout << mode << " " << qt << " subspaces=" << total5 << " family=" << fam.size() << " sets=" << sets << " survivors=" << survivors << "\n";
  return 0;
}
