// Exhaustive two-bit neighborhoods of pinned published Boolean functions.
// The independent verifier recomputes every Walsh coefficient of emitted truth tables.
#include <algorithm>
#include <array>
#include <cctype>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
constexpr int N = 512;
using Table = std::array<int, N>;
static signed char phase[N][N];

int nibble(char c) {
    if (c >= '0' && c <= '9') return c - '0';
    if (c >= 'a' && c <= 'f') return c - 'a' + 10;
    if (c >= 'A' && c <= 'F') return c - 'A' + 10;
    return -1;
}

std::vector<Table> load_seeds(const std::string& name) {
    std::ifstream in(name);
    if (!in) throw std::runtime_error("cannot open seed file");
    std::vector<Table> seeds;
    std::string line;
    while (std::getline(in, line)) {
        if (line.empty() || line[0] == '#') continue;
        if (line.size() != 128) throw std::runtime_error("seed must have 128 hex digits");
        Table bits{};
        for (int i = 0; i < 128; ++i) {
            const int value = nibble(line[i]);
            if (value < 0) throw std::runtime_error("invalid hexadecimal seed");
            for (int j = 0; j < 4; ++j) bits[4 * i + j] = (value >> (3 - j)) & 1;
        }
        seeds.push_back(bits);
    }
    if (seeds.empty()) throw std::runtime_error("no seed tables");
    return seeds;
}

Table walsh(const Table& bits) {
    Table w{};
    for (int x = 0; x < N; ++x) w[x] = 1 - 2 * bits[x];
    for (int step = 1; step < N; step *= 2) {
        for (int base = 0; base < N; base += 2 * step) {
            for (int j = 0; j < step; ++j) {
                const int u = w[base + j], v = w[base + step + j];
                w[base + j] = u + v;
                w[base + step + j] = u - v;
            }
        }
    }
    return w;
}

void require_unused(const std::string& name) {
    std::ifstream existing(name);
    if (existing.good()) throw std::runtime_error("refusing to overwrite " + name);
}

struct Result {
    long long pairs = 0;
    long long balanceable_pairs = 0;
    long long balanceable_twists = 0;
    long long target_pairs = 0;
    long long peak_histogram[33]{};
    int best_peak = 999;
    int best_x = -1, best_y = -1, best_twist = -1;
};

void write_candidate(const std::string& name, const Table& original,
                     int seed, const Result& result) {
    require_unused(name);
    Table bits = original;
    bits[result.best_x] ^= 1;
    bits[result.best_y] ^= 1;
    for (int x = 0; x < N; ++x) bits[x] ^= __builtin_parity(x & result.best_twist);
    const Table w = walsh(bits);
    int peak = 0;
    for (int value : w) peak = std::max(peak, std::abs(value));
    if (w[0] != 0 || peak != result.best_peak) throw std::runtime_error("candidate construction mismatch");
    std::ofstream out(name);
    if (!out) throw std::runtime_error("cannot create candidate " + name);
    out << "{\n  \"format\": \"boolean-truth-v1\",\n"
        << "  \"order\": \"x=0..511; published hex left-to-right high-bit first\",\n"
        << "  \"seed_index_1based\": " << seed << ",\n"
        << "  \"flip_indices\": [" << result.best_x << ", " << result.best_y << "],\n"
        << "  \"affine_twist_frequency\": " << result.best_twist << ",\n"
        << "  \"reported_peak\": " << peak << ",\n"
        << "  \"bits\": \"";
    for (int bit : bits) out << bit;
    out << "\"\n}\n";
    if (!out) throw std::runtime_error("failed writing candidate");
}

Result run(const Table& bits) {
    const Table w = walsh(bits);
    Table signs{};
    std::vector<int> near_zero;
    int original_peak = 0;
    for (int a = 0; a < N; ++a) {
        signs[a] = 1 - 2 * bits[a];
        original_peak = std::max(original_peak, std::abs(w[a]));
        if (w[a] == 0 || w[a] % 4 != 0) throw std::runtime_error("seed must have nonzero 4-divisible spectrum");
        if (std::abs(w[a]) == 4) near_zero.push_back(a);
    }
    if (original_peak != 28 || near_zero.empty()) throw std::runtime_error("seed is not the expected peak-28 zero-free input");
    Result result;
    for (int x = 0; x < N; ++x) {
        for (int y = x + 1; y < N; ++y) {
            ++result.pairs;
            bool can_balance = false;
            for (int a : near_zero) {
                if (w[a] - 2 * (signs[x] * phase[x][a] + signs[y] * phase[y][a]) == 0) {
                    can_balance = true;
                    break;
                }
            }
            if (!can_balance) continue;
            ++result.balanceable_pairs;
            int peak = 0, twist = -1, zeros = 0;
            for (int a = 0; a < N; ++a) {
                const int value = w[a] - 2 * (signs[x] * phase[x][a] + signs[y] * phase[y][a]);
                peak = std::max(peak, std::abs(value));
                if (value == 0) {
                    ++zeros;
                    if (twist < 0) twist = a;
                }
            }
            if (peak > 32 || twist < 0) throw std::runtime_error("internal spectral bound mismatch");
            result.balanceable_twists += zeros;
            ++result.peak_histogram[peak];
            if (peak <= 28) ++result.target_pairs;
            if (peak < result.best_peak) {
                result.best_peak = peak;
                result.best_x = x;
                result.best_y = y;
                result.best_twist = twist;
            }
        }
    }
    if (result.pairs != 130816 || result.best_x < 0) throw std::runtime_error("neighborhood unexpectedly incomplete");
    return result;
}
}  // namespace

int main(int argc, char** argv) {
    try {
        if (argc != 3) throw std::runtime_error("usage: search SEEDS RESULT_JSON");
        const std::string result_path = argv[2];
        require_unused(result_path);
        const auto seeds = load_seeds(argv[1]);
        for (int x = 0; x < N; ++x)
            for (int a = 0; a < N; ++a)
                phase[x][a] = __builtin_parity(x & a) ? -1 : 1;
        std::vector<Result> results;
        for (std::size_t i = 0; i < seeds.size(); ++i) {
            const Result result = run(seeds[i]);
            const std::string candidate = "frontier-20261028-best-seed" + std::to_string(i + 1) + ".json";
            write_candidate(candidate, seeds[i], static_cast<int>(i + 1), result);
            results.push_back(result);
            std::cout << "seed=" << i + 1 << " pairs=" << result.pairs
                      << " balanceable=" << result.balanceable_pairs
                      << " twists=" << result.balanceable_twists
                      << " min_peak=" << result.best_peak
                      << " target_pairs=" << result.target_pairs << '\n';
        }
        std::ofstream out(result_path);
        if (!out) throw std::runtime_error("cannot create result file");
        out << "{\n  \"source\": \"" << argv[1] << "\",\n"
            << "  \"method\": \"all distinct two-bit flips; balance by every zero Walsh frequency\",\n"
            << "  \"seeds\": [\n";
        for (std::size_t i = 0; i < results.size(); ++i) {
            const Result& r = results[i];
            if (i) out << ",\n";
            out << "    {\"seed_index_1based\":" << i + 1
                << ",\"pairs\":" << r.pairs
                << ",\"balanceable_pairs\":" << r.balanceable_pairs
                << ",\"balanceable_twists\":" << r.balanceable_twists
                << ",\"target_pairs\":" << r.target_pairs
                << ",\"best_peak\":" << r.best_peak
                << ",\"best_flips\":[" << r.best_x << ',' << r.best_y << ']'
                << ",\"best_twist\":" << r.best_twist
                << ",\"peak_histogram\":{";
            bool first = true;
            for (int peak = 0; peak <= 32; ++peak) {
                if (!r.peak_histogram[peak]) continue;
                if (!first) out << ',';
                first = false;
                out << '"' << peak << "\":" << r.peak_histogram[peak];
            }
            out << "}}";
        }
        out << "\n  ]\n}\n";
        if (!out) throw std::runtime_error("failed writing result");
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
