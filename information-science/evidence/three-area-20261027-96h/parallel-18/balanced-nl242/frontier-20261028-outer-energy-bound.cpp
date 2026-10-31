// Independent Parseval upper bound for all one/two outside-flip choices.
#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
constexpr int N = 512;
using Table = std::array<int, N>;
static std::int8_t delta[N][N];
int nibble(char c) {
    if (c >= '0' && c <= '9') return c - '0';
    if (c >= 'a' && c <= 'f') return c - 'a' + 10;
    if (c >= 'A' && c <= 'F') return c - 'A' + 10;
    return -1;
}
std::vector<Table> seeds(const std::string& path) {
    std::ifstream input(path);
    if (!input) throw std::runtime_error("cannot open seeds");
    std::vector<Table> result;
    std::string line;
    while (std::getline(input, line)) {
        if (line.empty() || line[0] == '#') continue;
        if (line.size() != 128) throw std::runtime_error("invalid seed length");
        Table bits{};
        for (int i = 0; i < 128; ++i) {
            int value = nibble(line[i]);
            if (value < 0) throw std::runtime_error("invalid seed digit");
            for (int j = 0; j < 4; ++j) bits[4*i+j] = (value >> (3-j)) & 1;
        }
        result.push_back(bits);
    }
    return result;
}
struct Summary { long long total = 0, impossible = 0, inconclusive = 0; int max_upper = 0; };
Summary run(const Table& bits, int index, bool pairs) {
    const int origin = 365;
    const std::array<int,4> basis = index == 2 ? std::array<int,4>{63,90,139,278} : std::array<int,4>{27,45,195,325};
    std::array<bool, N> in_core{};
    for (int u = 0; u < 16; ++u) {
        int x = origin;
        for (int i = 0; i < 4; ++i) if (u & (1 << i)) x ^= basis[i];
        if (in_core[x]) throw std::runtime_error("dependent core basis");
        in_core[x] = true;
    }
    std::vector<int> outside;
    for (int x = 0; x < N; ++x) if (!in_core[x]) outside.push_back(x);
    std::array<int, N> base{};
    std::array<std::array<int, 32>,16> groups{};
    std::array<int,16> sizes{};
    for (int a = 0; a < N; ++a) {
        int g = 0;
        for (int i = 0; i < 4; ++i) if (__builtin_parity(a & basis[i])) g |= 1 << i;
        if (sizes[g] >= 32) throw std::runtime_error("frequency class too large");
        groups[g][sizes[g]++] = a;
        for (int x : outside) {
            int term = (1 - 2 * bits[x]) * (__builtin_parity(a & (x ^ origin)) ? -1 : 1);
            base[a] += term;
            delta[x][a] = static_cast<std::int8_t>(-2 * term);
        }
    }
    for (int size : sizes) if (size != 32) throw std::runtime_error("frequency class size mismatch");
    Summary result;
    for (std::size_t i = 0; i < outside.size(); ++i) {
        const std::size_t start = pairs ? i + 1 : i;
        const std::size_t stop = pairs ? outside.size() : i + 1;
        for (std::size_t j = start; j < stop; ++j) {
            ++result.total;
            const int x = outside[i], y = pairs ? outside[j] : -1;
            int upper = 0;
            bool empty = false;
            for (const auto& group : groups) {
                int lo_r = std::numeric_limits<int>::max(), hi_r = std::numeric_limits<int>::min();
                for (int a : group) {
                    const int value = base[a] + delta[x][a] + (y >= 0 ? delta[y][a] : 0);
                    lo_r = std::min(lo_r, value); hi_r = std::max(hi_r, value);
                }
                int low = -16, high = 16;
                while (low <= 16 && low < -28 - lo_r) low += 2;
                while (high >= -16 && high > 28 - hi_r) high -= 2;
                if (low > high) { empty = true; break; }
                upper += std::max(low*low, high*high);
            }
            if (empty || upper < 256) ++result.impossible;
            else ++result.inconclusive;
            if (!empty) result.max_upper = std::max(result.max_upper, upper);
        }
    }
    return result;
}
}
int main(int argc, char** argv) {
    try {
        if (argc != 3) throw std::runtime_error("usage: energy-bound SEEDS RESULT_JSON");
        std::ifstream existing(argv[2]);
        if (existing.good()) throw std::runtime_error("refusing to overwrite output");
        const auto input = seeds(argv[1]);
        if (input.size() != 3) throw std::runtime_error("expected three seeds");
        std::array<Summary, 3> singles{}, pairs{};
        for (int i = 0; i < 3; ++i) {
            singles[i] = run(input[i], i+1, false);
            pairs[i] = run(input[i], i+1, true);
            const auto& one = singles[i];
            const auto& two = pairs[i];
            std::cout << "seed=" << i+1 << " single=" << one.total << " parseval_impossible=" << one.impossible
                      << " inconclusive=" << one.inconclusive << " max_upper=" << one.max_upper
                      << " pair=" << two.total << " parseval_impossible=" << two.impossible
                      << " inconclusive=" << two.inconclusive << " max_upper=" << two.max_upper << '\n';
        }
        std::ofstream output(argv[2]);
        if (!output) throw std::runtime_error("cannot create result");
        output << "{\n  \"method\":\"per-frequency interval and local Parseval upper bound\",\n  \"seeds\":[\n";
        for (int i = 0; i < 3; ++i) {
            if (i) output << ",\n";
            output << "    {\"seed_index_1based\":" << i+1
                   << ",\"single\":{\"total\":" << singles[i].total
                   << ",\"impossible\":" << singles[i].impossible
                   << ",\"inconclusive\":" << singles[i].inconclusive
                   << ",\"max_upper\":" << singles[i].max_upper
                   << "},\"pair\":{\"total\":" << pairs[i].total
                   << ",\"impossible\":" << pairs[i].impossible
                   << ",\"inconclusive\":" << pairs[i].inconclusive
                   << ",\"max_upper\":" << pairs[i].max_upper << "}}";
        }
        output << "\n  ]\n}\n";
        if (!output) throw std::runtime_error("result write failed");
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
