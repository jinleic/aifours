// Exhaustive search for the odd half in rank-four profile (D,m)=(16,108).
// Model (see frontier-20261029-rank4-m112-and-profiles-v1.md, section C, and the (16,108) note):
// after the symmetries lambda=mu=0, theta=1 and affine normalisation of the atom map r, the odd
// function is determined by a linear map phi: F_2^4 -> Q, Q = Boolean functions on F_2^4 modulo
// affine functions (11-dimensional; elements are 11-bit keys of degree>=2 ANF monomials).
// Block c=0 is -(-1)^{Q4}; block c!=0 is X_{phi(c)} = -lift(Walsh((-1)^{Q4+rep(phi(c))}) mod 3).
// Up to GL(4) acting on c, phi is determined by its image subspace L (dim d<=4, padded by kernel).
// Every subspace of dim<=4 is enumerated once by reduced row echelon form. A candidate passes if
// sum nu = 108, (optionally) every fibre energy is 132, and every odd Walsh value
// Wd(rho,s)=sum_c chi_rho(c) V_c(s) has |Wd|<=BOUND.
// Input: table file (2048 lines: nu rep V[16]; then the V of block 0). Output: JSON receipt.
#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iostream>
#include <mutex>
#include <string>
#include <thread>
#include <vector>

static int NU[2048]; static int REP[2048]; static int V[2048][16]; static int V0[16];
static int CHI[16][16];
static int BOUND = 14; static bool ENERGY = true;

struct Stats { long long subspaces = 0, nu_pass = 0, energy_pass = 0, walsh_pass = 0; };
static std::mutex mu; static std::vector<std::array<int, 4>> survivors;

static bool check(const std::array<int, 4>& g, Stats& st) {
  int phi[16]; phi[0] = 0;
  for (int c = 1; c < 16; ++c) { int v = 0; for (int i = 0; i < 4; ++i) if ((c >> i) & 1) v ^= g[i]; phi[c] = v; }
  int nus = 0; for (int c = 1; c < 16; ++c) nus += NU[phi[c]];
  if (nus != 108) return false;
  st.nu_pass++;
  if (ENERGY)
    for (int s = 0; s < 16; ++s) { int e = 0; for (int c = 1; c < 16; ++c) e += V[phi[c]][s] * V[phi[c]][s]; if (e != 132) return false; }
  st.energy_pass++;
  for (int s = 0; s < 16; ++s)
    for (int r = 0; r < 16; ++r) {
      int w = V0[s];
      for (int c = 1; c < 16; ++c) w += CHI[r][c] * V[phi[c]][s];
      if (w > BOUND || w < -BOUND) return false;
    }
  st.walsh_pass++;
  return true;
}

int main(int argc, char** argv) {
  if (argc != 6) { std::cerr << "usage: search TABLES OUT_JSON THREADS BOUND ENERGY(0/1)\n"; return 2; }
  { std::ifstream chk(argv[2]); if (chk.good()) { std::cerr << "refusing to overwrite\n"; return 2; } }
  std::ifstream in(argv[1]); if (!in) { std::cerr << "no tables\n"; return 2; }
  for (int k = 0; k < 2048; ++k) { in >> NU[k] >> REP[k]; for (int s = 0; s < 16; ++s) in >> V[k][s]; }
  for (int s = 0; s < 16; ++s) in >> V0[s];
  if (!in) { std::cerr << "bad tables\n"; return 2; }
  const int T = std::max(1, std::atoi(argv[3])); BOUND = std::atoi(argv[4]); ENERGY = std::atoi(argv[5]) != 0;
  for (int r = 0; r < 16; ++r) for (int c = 0; c < 16; ++c) CHI[r][c] = (__builtin_popcount(r & c) & 1) ? -1 : 1;
  std::vector<std::vector<int>> pivsets;
  for (int d = 0; d <= 4; ++d) {
    std::vector<int> p(d);
    std::function<void(int, int)> gen = [&](int i, int start) {
      if (i == d) { pivsets.push_back(p); return; }
      for (int x = start; x < 11; ++x) { p[i] = x; gen(i + 1, x + 1); }
    };
    gen(0, 0);
  }
  std::atomic<size_t> next{0}; std::vector<Stats> stats(T);
  auto t0 = std::chrono::steady_clock::now();
  auto worker = [&](int tid) {
    Stats& st = stats[tid];
    for (;;) {
      size_t idx = next++; if (idx >= pivsets.size()) break;
      const std::vector<int>& p = pivsets[idx]; int d = (int)p.size();
      std::vector<std::vector<int>> fr(d);
      for (int i = 0; i < d; ++i)
        for (int x = p[i] + 1; x < 11; ++x) if (std::find(p.begin(), p.end(), x) == p.end()) fr[i].push_back(x);
      int totbits = 0; for (int i = 0; i < d; ++i) totbits += (int)fr[i].size();
      for (long long mask = 0; mask < (1LL << totbits); ++mask) {
        std::array<int, 4> g{0, 0, 0, 0}; int b = 0;
        for (int i = 0; i < d; ++i) { int v = 1 << p[i]; for (int x : fr[i]) { if ((mask >> b) & 1) v |= 1 << x; ++b; } g[i] = v; }
        st.subspaces++;
        if (check(g, st)) { std::lock_guard<std::mutex> lk(mu); survivors.push_back(g); }
      }
    }
  };
  std::vector<std::thread> th; for (int t = 0; t < T; ++t) th.emplace_back(worker, t);
  for (auto& x : th) x.join();
  double el = std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
  Stats tot; for (auto& s : stats) { tot.subspaces += s.subspaces; tot.nu_pass += s.nu_pass; tot.energy_pass += s.energy_pass; tot.walsh_pass += s.walsh_pass; }
  std::ofstream out(argv[2]);
  out << "{\n  \"bound\": " << BOUND << ",\n  \"energy_filter\": " << (ENERGY ? "true" : "false") << ",\n  \"subspaces_enumerated\": " << tot.subspaces
      << ",\n  \"nu_sum_108\": " << tot.nu_pass << ",\n  \"after_energy_filter\": " << tot.energy_pass << ",\n  \"odd_walsh_within_bound\": " << tot.walsh_pass
      << ",\n  \"survivors_shown\": [";
  for (size_t i = 0; i < survivors.size() && i < 200; ++i) { out << (i ? "," : "") << "[" << survivors[i][0] << "," << survivors[i][1] << "," << survivors[i][2] << "," << survivors[i][3] << "]"; }
  out << "],\n  \"elapsed_seconds\": " << el << "\n}\n";
  std::cout << "bound=" << BOUND << " subspaces=" << tot.subspaces << " nu=" << tot.nu_pass << " energy=" << tot.energy_pass << " walsh=" << tot.walsh_pass << " elapsed=" << el << "s\n";
  return 0;
}
