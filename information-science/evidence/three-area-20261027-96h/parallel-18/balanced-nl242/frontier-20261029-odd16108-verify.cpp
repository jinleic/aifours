// Independent re-check of the (16,108) odd-half exhaustion (no tables read from disk).
// Computes, from the definition Q4(s)=s1s2+s3s4+s3+s4, every class representative (Boolean
// functions on F_2^4 with zero affine ANF part, 2^11 of them), the block odd functions
// X_g(z) = -lift(Walsh((-1)^{Q4+g})(z) mod 3), and for EVERY subspace of dimension <=4 of the
// 11-dimensional class space (enumerated by RREF, count must be 917907553) builds the full
// 256-point odd function v' (block 0 = -(-1)^{Q4(z)}, block c = X_{phi(c)}), runs a fast
// Walsh-Hadamard transform on all 256 points and records the maximum |Walsh|.  No nu or energy
// prefilter is used.  Reports the histogram of max|Walsh| and every subspace with max<=14.
#include <algorithm>
#include <array>
#include <atomic>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <mutex>
#include <thread>
#include <vector>

static int8_t X[2048][16];

static int Q4(int s) { int s1 = s & 1, s2 = (s >> 1) & 1, s3 = (s >> 2) & 1, s4 = (s >> 3) & 1; return (s1 * s2 + s3 * s4 + s3 + s4) & 1; }

int main(int argc, char** argv) {
  if (argc != 3) { std::cerr << "usage: verify OUT_JSON THREADS\n"; return 2; }
  { std::ifstream chk(argv[1]); if (chk.good()) { std::cerr << "refusing to overwrite\n"; return 2; } }
  const int T = std::max(1, std::atoi(argv[2]));
  // monomials of degree >= 2 in 4 variables (as subsets of {0,1,2,3})
  std::vector<int> mon; for (int m = 0; m < 16; ++m) if (__builtin_popcount(m) >= 2) mon.push_back(m);
  if (mon.size() != 11) return 3;
  for (int k = 0; k < 2048; ++k) {
    int tt[16];
    for (int s = 0; s < 16; ++s) { int v = 0; for (int i = 0; i < 11; ++i) if (((k >> i) & 1) && ((s & mon[i]) == mon[i])) v ^= 1; tt[s] = v; }
    for (int z = 0; z < 16; ++z) {
      int w = 0; for (int s = 0; s < 16; ++s) { int e = (Q4(s) ^ tt[s] ^ (__builtin_popcount(s & z) & 1)); w += e ? -1 : 1; }
      int r = ((w % 3) + 3) % 3; X[k][z] = (int8_t)(r == 0 ? 0 : (r == 1 ? -1 : 1));
    }
  }
  int8_t B0[16]; for (int z = 0; z < 16; ++z) B0[z] = (int8_t)(Q4(z) ? 1 : -1);
  std::vector<std::vector<int>> piv;
  for (int d = 0; d <= 4; ++d) { std::vector<int> p(d); std::function<void(int, int)> g = [&](int i, int st) { if (i == d) { piv.push_back(p); return; } for (int x = st; x < 11; ++x) { p[i] = x; g(i + 1, x + 1); } }; g(0, 0); }
  std::atomic<size_t> nx{0}; std::mutex mu; std::map<int, long long> hist; long long total = 0; std::vector<std::array<int, 4>> good;
  auto t0 = std::chrono::steady_clock::now();
  auto work = [&]() {
    std::map<int, long long> h; long long cnt = 0; std::vector<std::array<int, 4>> gd;
    int v[256];
    for (;;) {
      size_t id = nx++; if (id >= piv.size()) break;
      const auto& p = piv[id]; int d = (int)p.size();
      std::vector<std::vector<int>> fr(d); int tb = 0;
      for (int i = 0; i < d; ++i) { for (int x = p[i] + 1; x < 11; ++x) if (std::find(p.begin(), p.end(), x) == p.end()) fr[i].push_back(x); tb += (int)fr[i].size(); }
      for (long long mask = 0; mask < (1LL << tb); ++mask) {
        std::array<int, 4> g{0, 0, 0, 0}; int b = 0;
        for (int i = 0; i < d; ++i) { int val = 1 << p[i]; for (int x : fr[i]) { if ((mask >> b) & 1) val |= 1 << x; ++b; } g[i] = val; }
        for (int c = 0; c < 16; ++c) {
          int phi = 0; for (int i = 0; i < 4; ++i) if ((c >> i) & 1) phi ^= g[i];
          for (int z = 0; z < 16; ++z) v[c + 16 * z] = (c == 0) ? B0[z] : X[phi][z];
        }
        for (int len = 1; len < 256; len <<= 1)
          for (int i = 0; i < 256; i += len << 1)
            for (int j = i; j < i + len; ++j) { int a = v[j], q = v[j + len]; v[j] = a + q; v[j + len] = a - q; }
        int mx = 0; for (int i = 0; i < 256; ++i) mx = std::max(mx, std::abs(v[i]));
        h[mx]++; cnt++; if (mx <= 14) gd.push_back(g);
      }
    }
    std::lock_guard<std::mutex> lk(mu); total += cnt; for (auto& kv : h) hist[kv.first] += kv.second; good.insert(good.end(), gd.begin(), gd.end());
  };
  std::vector<std::thread> th; for (int t = 0; t < T; ++t) th.emplace_back(work); for (auto& x : th) x.join();
  double el = std::chrono::duration<double>(std::chrono::steady_clock::now() - t0).count();
  std::ofstream out(argv[1]);
  out << "{\n  \"subspaces\": " << total << ",\n  \"max_abs_walsh_histogram\": {";
  bool first = true; for (auto& kv : hist) { out << (first ? "" : ", ") << "\"" << kv.first << "\": " << kv.second; first = false; }
  out << "},\n  \"max_le_14\": " << good.size() << ",\n  \"elapsed_seconds\": " << el << "\n}\n";
  std::cout << "subspaces=" << total << " max<=14: " << good.size() << " minmax=" << hist.begin()->first << " elapsed=" << el << "s\n";
  return 0;
}
