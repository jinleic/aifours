// Exact four-flip peak-preservation via the complete uncovered-triple hypergraph.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <unordered_set>
#include <vector>

namespace {
constexpr int N = 512;
constexpr int WORDS = N / 64;
using Table = std::array<int, N>;
using Triple = std::array<int, 3>;
using Quad = std::array<int, 4>;
using Mask = std::array<std::uint64_t, WORDS>;
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
        if (line.size() != 128) throw std::runtime_error("seed must have 128 hexadecimal digits");
        Table bits{};
        for (int i = 0; i < 128; ++i) {
            const int value = nibble(line[i]);
            if (value < 0) throw std::runtime_error("invalid hexadecimal seed");
            for (int j = 0; j < 4; ++j) bits[4 * i + j] = (value >> (3 - j)) & 1;
        }
        seeds.push_back(bits);
    }
    if (seeds.empty()) throw std::runtime_error("no seeds");
    return seeds;
}

Table walsh(const Table& bits) {
    Table w{};
    for (int x = 0; x < N; ++x) w[x] = 1 - 2 * bits[x];
    for (int d = 1; d < N; d *= 2)
        for (int base = 0; base < N; base += 2 * d)
            for (int j = 0; j < d; ++j) {
                const int u = w[base + j], v = w[base + d + j];
                w[base + j] = u + v;
                w[base + d + j] = u - v;
            }
    return w;
}

std::uint32_t key(int a, int b, int c) {
    if (!(0 <= a && a < b && b < c && c < N)) throw std::runtime_error("invalid sorted triple");
    return (static_cast<std::uint32_t>(a) << 18) |
           (static_cast<std::uint32_t>(b) << 9) | static_cast<std::uint32_t>(c);
}

void require_unused(const std::string& name) {
    std::ifstream in(name);
    if (in.good()) throw std::runtime_error("refusing to overwrite " + name);
}

struct Result {
    long long triples = 0;
    long long quadruples_total = 0;
    long long fourth_extensions_checked = 0;
    long long balanceable_quadruples = 0;
    std::vector<Triple> uncovered;
    std::vector<Quad> preserving;
};

Result analyze(const Table& bits, int seed_index) {
    const Table w = walsh(bits);
    Table signs{};
    std::vector<int> peaks;
    for (int x = 0; x < N; ++x) signs[x] = 1 - 2 * bits[x];
    for (int a = 0; a < N; ++a) {
        if (w[a] == 0 || w[a] % 4 != 0 || std::abs(w[a]) > 28)
            throw std::runtime_error("seed must have zero-free 4-divisible peak-28 spectrum");
        if (std::abs(w[a]) == 28) peaks.push_back(a);
        else if (std::abs(w[a]) > 20) throw std::runtime_error("nonpeak must be at most 20");
    }
    if (peaks.empty()) throw std::runtime_error("seed has no peak coefficients");
    std::array<Mask, N> bad{};
    for (int x = 0; x < N; ++x) {
        for (std::size_t i = 0; i < peaks.size(); ++i) {
            const int a = peaks[i];
            const int peak_sign = w[a] > 0 ? 1 : -1;
            if (peak_sign * signs[x] * phase[x][a] < 0)
                bad[x][i / 64] |= std::uint64_t{1} << (i % 64);
        }
    }
    Result result;
    result.quadruples_total = static_cast<long long>(N) * (N - 1) * (N - 2) * (N - 3) / 24;
    for (int x = 0; x < N - 2; ++x)
        for (int y = x + 1; y < N - 1; ++y)
            for (int z = y + 1; z < N; ++z) {
                ++result.triples;
                bool covered = false;
                for (int i = 0; i < WORDS; ++i)
                    if (bad[x][i] & bad[y][i] & bad[z][i]) { covered = true; break; }
                if (!covered) result.uncovered.push_back({x, y, z});
            }
    if (result.triples != static_cast<long long>(N) * (N - 1) * (N - 2) / 6)
        throw std::runtime_error("incomplete triple scan");
    std::unordered_set<std::uint32_t> edges;
    for (const auto& t : result.uncovered) edges.insert(key(t[0], t[1], t[2]));
    if (edges.size() != result.uncovered.size()) throw std::runtime_error("duplicate triple");
    for (const auto& t : result.uncovered) {
        const int x = t[0], y = t[1], z = t[2];
        for (int v = z + 1; v < N; ++v) {
            ++result.fourth_extensions_checked;
            if (!edges.count(key(x, y, v)) || !edges.count(key(x, z, v)) || !edges.count(key(y, z, v)))
                continue;
            const Quad quad{x, y, z, v};
            int peak = 0, zero = -1;
            for (int a = 0; a < N; ++a) {
                int value = w[a];
                for (int p : quad) value -= 2 * signs[p] * phase[p][a];
                peak = std::max(peak, std::abs(value));
                if (value == 0 && zero < 0) zero = a;
            }
            if (peak > 28) throw std::runtime_error("hypergraph criterion failed");
            result.preserving.push_back(quad);
            if (zero >= 0) {
                ++result.balanceable_quadruples;
                if (result.balanceable_quadruples == 1) {
                    const std::string file = "frontier-20261028-fourflip-witness-seed" + std::to_string(seed_index) + ".json";
                    require_unused(file);
                    Table candidate = bits;
                    for (int p : quad) candidate[p] ^= 1;
                    for (int p = 0; p < N; ++p) candidate[p] ^= __builtin_parity(p & zero);
                    const Table checked = walsh(candidate);
                    int checked_peak = 0;
                    for (int value : checked) checked_peak = std::max(checked_peak, std::abs(value));
                    if (checked[0] != 0 || checked_peak > 28) throw std::runtime_error("candidate mismatch");
                    std::ofstream out(file);
                    if (!out) throw std::runtime_error("cannot write witness candidate");
                    out << "{\n  \"format\": \"boolean-truth-v1\",\n  \"seed_index_1based\": " << seed_index
                        << ",\n  \"flip_indices\": [" << x << ',' << y << ',' << z << ',' << v
                        << "],\n  \"affine_twist_frequency\": " << zero << ",\n  \"bits\": \"";
                    for (int bit : candidate) out << bit;
                    out << "\"\n}\n";
                    if (!out) throw std::runtime_error("candidate write failed");
                }
            }
        }
    }
    return result;
}
}  // namespace

int main(int argc, char** argv) {
    try {
        if (argc != 3) throw std::runtime_error("usage: hypergraph SEEDS RESULT_JSON");
        require_unused(argv[2]);
        const auto seeds = load_seeds(argv[1]);
        for (int x = 0; x < N; ++x)
            for (int a = 0; a < N; ++a)
                phase[x][a] = __builtin_parity(x & a) ? -1 : 1;
        std::vector<Result> results;
        for (std::size_t i = 0; i < seeds.size(); ++i) {
            Result result = analyze(seeds[i], static_cast<int>(i + 1));
            std::cout << "seed=" << i + 1 << " triples=" << result.triples
                      << " uncovered=" << result.uncovered.size()
                      << " quadruples=" << result.quadruples_total
                      << " extensions_checked=" << result.fourth_extensions_checked
                      << " peak_preserving=" << result.preserving.size()
                      << " balanceable=" << result.balanceable_quadruples << '\n';
            results.push_back(std::move(result));
        }
        std::ofstream out(argv[2]);
        if (!out) throw std::runtime_error("cannot write result");
        out << "{\n  \"method\": \"complete bad-peak triple hypergraph and all four-cliques\",\n  \"seeds\": [\n";
        for (std::size_t i = 0; i < results.size(); ++i) {
            const Result& r = results[i];
            if (i) out << ",\n";
            out << "    {\"seed_index_1based\":" << i + 1 << ",\"triples\":" << r.triples
                << ",\"uncovered_count\":" << r.uncovered.size()
                << ",\"quadruples_total\":" << r.quadruples_total
                << ",\"fourth_extensions_checked\":" << r.fourth_extensions_checked
                << ",\"peak_preserving_count\":" << r.preserving.size()
                << ",\"balanceable_count\":" << r.balanceable_quadruples << ",\"uncovered_triples\":[";
            for (std::size_t j = 0; j < r.uncovered.size(); ++j) {
                if (j) out << ',';
                const auto& t = r.uncovered[j];
                out << '[' << t[0] << ',' << t[1] << ',' << t[2] << ']';
            }
            out << "],\"preserving_quads\":[";
            for (std::size_t j = 0; j < r.preserving.size(); ++j) {
                if (j) out << ',';
                const auto& q = r.preserving[j];
                out << '[' << q[0] << ',' << q[1] << ',' << q[2] << ',' << q[3] << ']';
            }
            out << "]}";
        }
        out << "\n  ]\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
