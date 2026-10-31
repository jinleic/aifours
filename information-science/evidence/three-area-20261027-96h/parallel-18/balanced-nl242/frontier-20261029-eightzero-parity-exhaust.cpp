// Exhaustive classification of eight-point zero sets allowed by the full f131 coset-parity tool.
// K = F_2^8, alternating B of rank 4, 6 or 8 in normal form (pairs (0,1),(2,3),...; radical = remaining
// coordinates).  For EVERY 5-dim L <= K the tool gives |A cap Z| = C_L + wt(q|A)/4 (mod 2) over the eight
// cosets A, and wt(q|A)/4 mod 2 is 0 if rank(B|L)<=2 and 1+q(r)+B(a,r) if rank(B|L)=4 with
// rad(B|L)=<r>.  Since C_L and q(r) are unknown constants the q-free necessary condition is:
//   rank(B|L)<=2 : coset parity vector constant;   rank(B|L)=4 : parity(A)+B(a_A,r) constant.
// The program enumerates every 8-set Z with 0 in Z and XOR(Z)=0 (deg 1_Z<=6) and lists all survivors.
#include <algorithm>
#include <array>
#include <atomic>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iostream>
#include <mutex>
#include <string>
#include <thread>
#include <vector>

static int Bm[8][8];
static int Bf(int a, int b) { int s = 0; for (int i = 0; i < 8; ++i) if ((a >> i) & 1) for (int j = 0; j < 8; ++j) if ((b >> j) & 1) s ^= Bm[i][j]; return s; }

struct Fam { std::array<uint8_t, 256> lab; uint8_t ok1, ok2; };

int main(int argc, char** argv) {
  if (argc != 4) { std::cerr << "usage: exhaust RANK(4|6|8) THREADS OUT\n"; return 2; }
  int rank = std::atoi(argv[1]); int T = std::max(1, std::atoi(argv[2]));
  { std::ifstream chk(argv[3]); if (chk.good()) { std::cerr << "refusing to overwrite\n"; return 2; } }
  for (int i = 0; i < 8; ++i) for (int j = 0; j < 8; ++j) Bm[i][j] = 0;
  for (int p = 0; p < rank / 2; ++p) Bm[2 * p][2 * p + 1] = Bm[2 * p + 1][2 * p] = 1;
  std::vector<Fam> fam; long long total5 = 0, nA = 0, nC = 0;
  std::vector<int> piv(5);
  std::function<void(int, int)> rec = [&](int i, int st) {
    if (i == 5) {
      std::vector<std::vector<int>> fr(5); int tb = 0;
      for (int a = 0; a < 5; ++a) { for (int x = piv[a] + 1; x < 8; ++x) if (std::find(piv.begin(), piv.end(), x) == piv.end()) fr[a].push_back(x); tb += (int)fr[a].size(); }
      for (long long mask = 0; mask < (1LL << tb); ++mask) {
        int g[5]; int b = 0;
        for (int a = 0; a < 5; ++a) { int v = 1 << piv[a]; for (int x : fr[a]) { if ((mask >> b) & 1) v |= 1 << x; ++b; } g[a] = v; }
        ++total5;
        int G[5]; for (int a = 0; a < 5; ++a) { G[a] = 0; for (int c = 0; c < 5; ++c) if (Bf(g[a], g[c])) G[a] |= 1 << c; }
        // rank and kernel of G
        int M[5]; int E[5]; for (int a = 0; a < 5; ++a) { M[a] = G[a]; E[a] = 1 << a; }
        int rk = 0;
        for (int col = 0; col < 5; ++col) { int pr = -1; for (int r = rk; r < 5; ++r) if ((M[r] >> col) & 1) { pr = r; break; } if (pr < 0) continue; std::swap(M[rk], M[pr]); std::swap(E[rk], E[pr]); for (int r = 0; r < 5; ++r) if (r != rk && ((M[r] >> col) & 1)) { M[r] ^= M[rk]; E[r] ^= E[rk]; } ++rk; }
        std::vector<int> Ls = {0}; for (int a = 0; a < 5; ++a) { int n = (int)Ls.size(); for (int t = 0; t < n; ++t) Ls.push_back(Ls[t] ^ g[a]); }
        Fam F; std::vector<int> rep(256, -1); int nc = 0;
        for (int x = 0; x < 256; ++x) if (rep[x] < 0) { for (int l : Ls) rep[x ^ l] = nc; ++nc; }
        for (int x = 0; x < 256; ++x) F.lab[x] = (uint8_t)rep[x];
        if (rk <= 2) { F.ok1 = 0; F.ok2 = 0xFF; ++nC; }
        else if (rk == 4) {
          // kernel vector: a row of E whose M row is zero (rows rk..4)
          int coef = E[4]; int rvec = 0; for (int a = 0; a < 5; ++a) if ((coef >> a) & 1) rvec ^= g[a];
          bool okk = true; for (int a = 0; a < 5; ++a) if (Bf(rvec, g[a])) okk = false;
          if (!okk || rvec == 0) { std::cerr << "kernel error\n"; std::exit(3); }
          uint8_t bm = 0; for (int x = 0; x < 256; ++x) if (Bf(x, rvec)) bm |= (uint8_t)(1u << F.lab[x]);
          F.ok1 = bm; F.ok2 = (uint8_t)(bm ^ 0xFF); ++nA;
        } else { std::cerr << "odd rank\n"; std::exit(3); }
        fam.push_back(F);
      }
      return;
    }
    for (int x = st; x < 8; ++x) { piv[i] = x; rec(i + 1, x + 1); }
  };
  rec(0, 0);
  // order: put rank-4 constraints first (more discriminating), keep deterministic
  std::stable_sort(fam.begin(), fam.end(), [](const Fam& a, const Fam& b) { return (a.ok1 != 0) > (b.ok1 != 0); });
  std::atomic<int> next{1}; std::mutex mu; long long sets = 0; std::vector<std::array<int, 8>> surv;
  auto work = [&]() {
    long long ls = 0; std::vector<std::array<int, 8>> sv;
    for (;;) {
      int z1 = next++; if (z1 > 255) break;
      for (int z2 = z1 + 1; z2 < 256; ++z2) for (int z3 = z2 + 1; z3 < 256; ++z3) for (int z4 = z3 + 1; z4 < 256; ++z4) {
        int x4 = z1 ^ z2 ^ z3 ^ z4;
        for (int z5 = z4 + 1; z5 < 256; ++z5) for (int z6 = z5 + 1; z6 < 256; ++z6) {
          int z7 = x4 ^ z5 ^ z6; if (z7 <= z6) continue;
          ++ls; int Z[8] = {0, z1, z2, z3, z4, z5, z6, z7};
          bool ok = true;
          for (const auto& F : fam) { unsigned pv = 0; for (int t = 0; t < 8; ++t) pv ^= 1u << F.lab[Z[t]]; if (pv != F.ok1 && pv != F.ok2) { ok = false; break; } }
          if (ok) sv.push_back({Z[0], Z[1], Z[2], Z[3], Z[4], Z[5], Z[6], Z[7]});
        }
      }
    }
    std::lock_guard<std::mutex> lk(mu); sets += ls; surv.insert(surv.end(), sv.begin(), sv.end());
  };
  std::vector<std::thread> th; for (int t = 0; t < T; ++t) th.emplace_back(work); for (auto& x : th) x.join();
  std::sort(surv.begin(), surv.end());
  long long subsp = 0;
  for (auto& z : surv) { bool lin = true; for (int a = 0; a < 8 && lin; ++a) for (int b = 0; b < 8 && lin; ++b) { int c = z[a] ^ z[b]; if (std::find(z.begin(), z.end(), c) == z.end()) lin = false; } if (lin) ++subsp; }
  std::ofstream out(argv[3]);
  out << "{\n  \"rank\": " << rank << ",\n  \"five_dim_subspaces\": " << total5 << ",\n  \"constant_type\": " << nC << ",\n  \"affine_type\": " << nA
      << ",\n  \"eight_sets_tested\": " << sets << ",\n  \"survivors\": " << surv.size() << ",\n  \"survivors_that_are_subspaces\": " << subsp << ",\n  \"survivor_list\": [";
  for (size_t t = 0; t < surv.size(); ++t) { out << (t ? ",\n    " : "\n    ") << "[" << surv[t][0]; for (int u = 1; u < 8; ++u) out << ", " << surv[t][u]; out << "]"; }
  out << "\n  ]\n}\n";
  std::cout << "rank=" << rank << " L5=" << total5 << " C=" << nC << " A=" << nA << " sets=" << sets << " survivors=" << surv.size() << " subspaces=" << subsp << "\n";
  return 0;
}
