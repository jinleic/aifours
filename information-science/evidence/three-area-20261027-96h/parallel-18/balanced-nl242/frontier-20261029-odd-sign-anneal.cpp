// Bounded stochastic search for an odd-half signing v' on a FIXED support S' of F_2^8.
// Goal: every Walsh value of v' in [-14,14] (with an even-half control u this would give |W_f|<=28).
// Input file: 256 integers in {-1,0,1} (the even half u); S' = {y : u(y)=0}.
// Output: JSON receipt with the best signing found and its max |Walsh|. A failure to reach 14 is NOT
// an exclusion. Any reported success must be independently re-verified on the full 512-bit table.
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <random>
#include <string>
#include <vector>

static int chi(int a, int b) { return (__builtin_popcount(a & b) & 1) ? -1 : 1; }

int main(int argc, char** argv) {
  if (argc != 7) { std::cerr << "usage: anneal U_FILE SEED ITERS T0 T1 OUT_JSON\n"; return 2; }
  std::ifstream in(argv[1]); if (!in) { std::cerr << "cannot read input\n"; return 2; }
  std::array<int, 256> u{}; for (int i = 0; i < 256; ++i) { if (!(in >> u[i])) { std::cerr << "bad input\n"; return 2; } }
  const unsigned long long seed = std::stoull(argv[2]); const long long iters = std::stoll(argv[3]);
  const double T0 = std::stod(argv[4]), T1 = std::stod(argv[5]);
  { std::ifstream chk(argv[6]); if (chk.good()) { std::cerr << "refusing to overwrite output\n"; return 2; } }
  std::vector<int> S; for (int y = 0; y < 256; ++y) if (u[y] == 0) S.push_back(y);
  std::mt19937_64 rng(seed);
  std::array<int, 256> v{}; for (int y : S) v[y] = (rng() & 1) ? 1 : -1;
  std::array<int, 256> W{};
  for (int b = 0; b < 256; ++b) { int s = 0; for (int y : S) s += v[y] * chi(b, y); W[b] = s; }
  auto pen = [](int w) { int e = std::abs(w) - 14; return e > 0 ? e * e : 0; };
  long long cost = 0; for (int b = 0; b < 256; ++b) cost += pen(W[b]);
  long long best = cost; std::array<int, 256> bestv = v; int bestmax = 0;
  for (int b = 0; b < 256; ++b) bestmax = std::max(bestmax, std::abs(W[b]));
  std::uniform_real_distribution<double> U01(0.0, 1.0);
  static int CH[256][256]; for (int b = 0; b < 256; ++b) for (int y = 0; y < 256; ++y) CH[b][y] = chi(b, y);
  auto t0 = std::chrono::steady_clock::now();
  for (long long it = 0; it < iters && best > 0; ++it) {
    double T = T0 * std::pow(T1 / T0, (double)it / (double)iters);
    int y = S[rng() % S.size()];
    long long d = 0; int dv = -2 * v[y];
    for (int b = 0; b < 256; ++b) { int nw = W[b] + dv * CH[b][y]; d += pen(nw) - pen(W[b]); }
    if (d <= 0 || U01(rng) < std::exp(-(double)d / T)) {
      for (int b = 0; b < 256; ++b) W[b] += dv * CH[b][y];
      v[y] = -v[y]; cost += d;
      if (cost < best) { best = cost; bestv = v; bestmax = 0; for (int b = 0; b < 256; ++b) bestmax = std::max(bestmax, std::abs(W[b])); }
    }
  }
  double el = std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
  std::ofstream out(argv[6]);
  out << "{\n  \"seed\": " << seed << ",\n  \"iterations\": " << iters << ",\n  \"support_size\": " << S.size()
      << ",\n  \"best_penalty\": " << best << ",\n  \"best_max_abs_walsh\": " << bestmax << ",\n  \"v\": [";
  for (int y = 0; y < 256; ++y) out << (y ? "," : "") << bestv[y];
  out << "],\n  \"elapsed_seconds\": " << el << "\n}\n";
  std::cout << "support=" << S.size() << " best_penalty=" << best << " best_max=" << bestmax << " elapsed=" << el << "s\n";
  return 0;
}
