#include <algorithm>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <limits>
#include <random>
#include <string>
#include <vector>

// Bounded KY-style tabu/steepest-neighbour orbit-vector search.  Search
// misses are evidence only; the independent Python checker owns witnesses.
struct Cost {
    int64_t tail28 = 0, tail24 = 0;
    int peak = 0;
    int64_t score() const { return 1024 * tail28 + tail24; }
};

int main(int argc, char **argv) {
    if (argc != 6) {
        std::cerr << "usage: orbit_search matrix.txt any|nonzero seed seconds output.json\n";
        return 2;
    }
    const auto start = std::chrono::steady_clock::now();
    auto elapsed = [&]() { return std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count(); };
    std::ifstream input(argv[1]);
    int n = 0, k = 0, seed_count = 0;
    input >> n >> k >> seed_count;
    if (!input || n < 1 || n > 512 || n != k) return 3;
    std::vector<int> sizes(n), ox(n), reps(n), C(n * n);
    for (int &x : sizes) input >> x;
    for (int &x : ox) input >> x;
    for (int &x : reps) input >> x;
    for (int &x : C) input >> x;
    std::vector<std::string> names(seed_count), seeds(seed_count);
    for (int j = 0; j < seed_count; ++j) input >> names[j] >> seeds[j];
    if (!input) return 4;
    const bool require_nonzero = std::string(argv[2]) == "nonzero";
    const uint64_t rng_seed = std::stoull(argv[3]);
    const double seconds = std::stod(argv[4]);
    std::mt19937_64 rng(rng_seed);
    auto randn = [&](int bound) { return int(rng() % uint64_t(bound)); };
    std::vector<int> odd, even;
    for (int j = 0; j < n; ++j) (sizes[j] % 2 ? odd : even).push_back(j);
    std::vector<int> sign(n), W(n), tabu(n), best_sign(n), best_W(n);
    Cost global_best;
    global_best.tail28 = std::numeric_limits<int64_t>::max() / 4096;
    global_best.tail24 = 0;
    uint64_t proposals = 0, iterations = 0, restarts = 0, accepted = 0;
    int best_s = 0, best_weight = 0;
    bool found = false;
    auto score_after = [&](int a, int b) {
        Cost cost;
        for (int i = 0; i < n; ++i) {
            int value = W[i] - 2 * sign[a] * C[i * n + a];
            if (b >= 0) value -= 2 * sign[b] * C[i * n + b];
            const int m = std::abs(value);
            const int t28 = std::max(0, m - 28), t24 = std::max(0, m - 24);
            cost.tail28 += int64_t(sizes[i]) * t28 * t28;
            cost.tail24 += int64_t(sizes[i]) * t24 * t24;
            cost.peak = std::max(cost.peak, m);
        }
        return cost;
    };
    auto current_cost = [&]() {
        Cost cost;
        for (int i = 0; i < n; ++i) {
            const int m = std::abs(W[i]);
            const int t28 = std::max(0, m - 28), t24 = std::max(0, m - 24);
            cost.tail28 += int64_t(sizes[i]) * t28 * t28;
            cost.tail24 += int64_t(sizes[i]) * t24 * t24;
            cost.peak = std::max(cost.peak, m);
        }
        return cost;
    };
    auto recompute = [&]() {
        std::fill(W.begin(), W.end(), 0);
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < n; ++j) W[i] += C[i * n + j] * sign[j];
    };
    auto support_xor = [&]() {
        int s = 0;
        for (int j = 0; j < n; ++j) if (sign[j] == -1) s ^= ox[j];
        return s;
    };
    auto weight = [&]() {
        int w = 0;
        for (int j = 0; j < n; ++j) if (sign[j] == -1) w += sizes[j];
        return w;
    };
    auto random_move = [&](int &a, int &b) {
        if (!even.empty() && randn(4) == 0) {
            a = even[randn(int(even.size()))]; b = -1;
        } else {
            a = odd[randn(int(odd.size()))];
            do { b = odd[randn(int(odd.size()))]; } while (a == b);
        }
    };
    while (elapsed() < seconds && !found) {
        ++restarts;
        if (!require_nonzero || restarts % 3 != 0) {
            const std::string &base = seeds[(restarts - 1) % seed_count];
            for (int j = 0; j < n; ++j) sign[j] = base[j] == '0' ? 1 : -1;
            const int perturb = require_nonzero ? 2 + randn(22) : 1 + randn(3);
            for (int t = 0; t < perturb; ++t) {
                int a, b; random_move(a, b);
                sign[a] = -sign[a]; if (b >= 0) sign[b] = -sign[b];
            }
        } else {
            for (int j = 0; j < n; ++j) sign[j] = randn(2) ? 1 : -1;
            if (weight() % 2) { int a = odd[randn(int(odd.size()))]; sign[a] = -sign[a]; }
        }
        if (require_nonzero && support_xor() == 0) {
            for (;;) {
                int a, b; random_move(a, b);
                const int delta_s = ox[a] ^ (b >= 0 ? ox[b] : 0);
                if (delta_s) { sign[a] = -sign[a]; if (b >= 0) sign[b] = -sign[b]; break; }
            }
        }
        recompute();
        std::fill(tabu.begin(), tabu.end(), 0);
        int s = support_xor();
        for (int step = 0; step < 5000 && !found; ++step) {
            if ((step & 63) == 0 && elapsed() >= seconds) break;
            ++iterations;
            const Cost now = current_cost();
            if (now.tail28 < global_best.tail28 || (now.tail28 == global_best.tail28 && now.tail24 < global_best.tail24)) {
                global_best = now; best_sign = sign; best_W = W;
                best_s = s; best_weight = weight();
            }
            if (now.tail28 == 0) { found = true; break; }
            Cost chosen; chosen.tail28 = std::numeric_limits<int64_t>::max() / 4096;
            chosen.tail24 = 0;
            int ca = -1, cb = -1;
            uint64_t ties = 0;
            for (int trial = 0; trial < 96; ++trial) {
                int a, b; random_move(a, b);
                const int ns = s ^ ox[a] ^ (b >= 0 ? ox[b] : 0);
                if (require_nonzero && ns == 0) continue;
                ++proposals;
                const Cost c = score_after(a, b);
                const bool forbidden = tabu[a] > step || (b >= 0 && tabu[b] > step);
                if (forbidden && c.score() >= global_best.score()) continue;
                if (c.score() < chosen.score()) { chosen = c; ca = a; cb = b; ties = 1; }
                else if (c.score() == chosen.score() && (++ties, rng() % ties == 0)) { ca = a; cb = b; }
            }
            if (ca < 0) continue;
            for (int i = 0; i < n; ++i) {
                W[i] -= 2 * sign[ca] * C[i * n + ca];
                if (cb >= 0) W[i] -= 2 * sign[cb] * C[i * n + cb];
            }
            sign[ca] = -sign[ca];
            if (cb >= 0) sign[cb] = -sign[cb];
            s ^= ox[ca] ^ (cb >= 0 ? ox[cb] : 0);
            tabu[ca] = step + 5 + randn(19);
            if (cb >= 0) tabu[cb] = step + 5 + randn(19);
            ++accepted;
        }
    }
    std::ofstream output(argv[5]);
    output << "{\n  \"status\": \"" << (found ? "FOUND" : "NON_FIND") << "\",\n"
           << "  \"scope\": \"Bounded even-weight orbit-vector heuristic; non-find is not UNSAT.\",\n"
           << "  \"require_nonzero_support_xor\": " << (require_nonzero ? "true" : "false") << ",\n"
           << "  \"rng_seed\": " << rng_seed << ",\n  \"seconds_limit\": " << seconds
           << ",\n  \"elapsed_seconds\": " << elapsed() << ",\n  \"iterations\": " << iterations
           << ",\n  \"proposals\": " << proposals << ",\n  \"accepted_moves\": " << accepted
           << ",\n  \"restarts\": " << restarts << ",\n  \"orbit_variables\": " << n
           << ",\n  \"best_tail28\": " << global_best.tail28 << ",\n  \"best_tail24\": " << global_best.tail24
           << ",\n  \"best_max_abs_W\": " << global_best.peak << ",\n  \"best_support_xor\": " << best_s
           << ",\n  \"best_weight\": " << best_weight << ",\n  \"best_orbit_bits\": \"";
    for (int v : best_sign) output << (v == 1 ? '0' : '1');
    output << "\",\n  \"best_orbit_walsh\": [";
    for (int i = 0; i < n; ++i) output << (i ? "," : "") << best_W[i];
    output << "]\n}\n";
    std::cout << "orbits=" << n << " type=" << (require_nonzero ? "s!=0" : "any")
              << " status=" << (found ? "FOUND" : "NON_FIND") << " peak=" << global_best.peak
              << " tail28=" << global_best.tail28 << " s=" << best_s << " elapsed=" << elapsed() << "\n";
    return 0;
}
