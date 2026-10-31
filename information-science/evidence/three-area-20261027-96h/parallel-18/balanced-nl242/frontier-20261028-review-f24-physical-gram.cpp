// Independent exact census using physical Gram sums, not the author's implementation.
#include <algorithm>
#include <array>
#include <bitset>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
constexpr int N = 8;
constexpr int PCOUNT = 5040;
using Map = std::array<int, N>;
struct Square {
    Map f{};
    std::array<std::int8_t, 64> sums{};
    std::array<std::uint8_t, N> differences{};
    std::uint64_t nonzero_gram = 0;
    bool linear = true;
};
static std::array<std::bitset<PCOUNT>, PCOUNT> adjacent;

int character(int u, int v) { return __builtin_parity(u & v) ? -1 : 1; }

Square build(const Map& f) {
    Square s;
    s.f = f;
    for (int x = 0; x < N; ++x)
        for (int y = 0; y < N; ++y)
            if (f[x ^ y] != (f[x] ^ f[y])) s.linear = false;
    for (int u = 0; u < N; ++u)
        for (int v = 0; v < N; ++v) {
            int sum = 0;
            for (int x = 0; x < N; ++x) sum += character(u, f[x]) * character(v, x);
            s.sums[8 * u + v] = static_cast<std::int8_t>(sum);
            if ((u || v) && sum != 0) s.nonzero_gram |= std::uint64_t{1} << (8 * u + v);
        }
    for (int h = 1; h < N; ++h)
        for (int x = 0; x < N; ++x)
            s.differences[h] |= std::uint8_t(1u << (f[x] ^ f[x ^ h]));
    return s;
}

bool derivative_compatible(const Square& a, const Square& b) {
    for (int h = 1; h < N; ++h)
        if (a.differences[h] & b.differences[h]) return false;
    return true;
}

struct GramResult { long long row_checks = 0, pair_checks = 0, row_errors = 0, pair_errors = 0; };
GramResult check_gram(const std::vector<Square>& squares, const std::array<int, 4>& ids) {
    GramResult r;
    for (int index : ids) {
        const auto& s = squares[index];
        for (int fixed = 0; fixed < N; ++fixed)
            for (int a = 0; a < N; ++a)
                for (int b = 0; b < N; ++b) {
                    ++r.row_checks;
                    if (s.sums[a ^ b] != (a == b ? 8 : 0)) ++r.row_errors;
                    ++r.row_checks;
                    if (s.sums[8 * (a ^ b)] != (a == b ? 8 : 0)) ++r.row_errors;
                }
    }
    for (int i = 0; i < 4; ++i)
        for (int j = i + 1; j < 4; ++j)
            for (int c = 0; c < 64; ++c)
                for (int d = 0; d < 64; ++d) {
                    const int u = (c / 8) ^ (d / 8), v = (c % 8) ^ (d % 8);
                    const int value = squares[ids[i]].sums[8 * u + v] * squares[ids[j]].sums[8 * u + v];
                    ++r.pair_checks;
                    if (value != (c == d ? 64 : 0)) ++r.pair_errors;
                }
    return r;
}

long long duplicate_errors(const Square& s) {
    long long errors = 0;
    for (int c = 0; c < 64; ++c)
        for (int d = 0; d < 64; ++d) {
            const int u = (c / 8) ^ (d / 8), v = (c % 8) ^ (d % 8);
            const int value = s.sums[8 * u + v] * s.sums[8 * u + v];
            if (value != (c == d ? 64 : 0)) ++errors;
        }
    return errors;
}
}  // namespace

int main(int argc, char** argv) {
    const auto start = std::chrono::steady_clock::now();
    try {
        if (argc != 2) throw std::runtime_error("usage: physical-gram OUTPUT_JSON");
        std::ifstream existing(argv[1]);
        if (existing.good()) throw std::runtime_error("refusing to overwrite output");
        Map f{0, 1, 2, 3, 4, 5, 6, 7};
        std::vector<Square> squares;
        do { squares.push_back(build(f)); } while (std::next_permutation(f.begin() + 1, f.end()));
        if (squares.size() != PCOUNT) throw std::runtime_error("wrong permutation count");
        long long pair_tested = 0, criterion_mismatches = 0;
        std::array<long long, 3> pair_types{};
        int linear_count = 0;
        for (const auto& s : squares) if (s.linear) ++linear_count;
        for (int i = 0; i < PCOUNT; ++i)
            for (int j = i + 1; j < PCOUNT; ++j) {
                ++pair_tested;
                const bool physical = (squares[i].nonzero_gram & squares[j].nonzero_gram) == 0;
                if (physical != derivative_compatible(squares[i], squares[j])) ++criterion_mismatches;
                if (physical) {
                    ++pair_types[(!squares[i].linear) + (!squares[j].linear)];
                    adjacent[i].set(j);
                    adjacent[j].set(i);
                }
            }
        std::array<long long, 4> triple_types{};
        std::array<long long, 5> four_types{};
        std::array<int, 4> first{-1, -1, -1, -1};
        for (int i = 0; i < PCOUNT; ++i)
            for (int j = i + 1; j < PCOUNT; ++j) {
                if (!adjacent[i].test(j)) continue;
                const auto common = adjacent[i] & adjacent[j];
                for (int k = j + 1; k < PCOUNT; ++k) {
                    if (!common.test(k)) continue;
                    const int n3 = (!squares[i].linear) + (!squares[j].linear) + (!squares[k].linear);
                    ++triple_types[n3];
                    const auto common4 = common & adjacent[k];
                    for (int l = k + 1; l < PCOUNT; ++l) {
                        if (!common4.test(l)) continue;
                        ++four_types[n3 + (!squares[l].linear)];
                        if (first[0] < 0) first = {i, j, k, l};
                    }
                }
            }
        if (first[0] < 0) throw std::runtime_error("no four-family found for positive control");
        const GramResult gram = check_gram(squares, first);
        const long long neg = duplicate_errors(squares[first[0]]);
        const double elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();
        std::ofstream out(argv[1]);
        if (!out) throw std::runtime_error("cannot create output");
        out << "{\n  \"permutations\":" << squares.size() << ",\n  \"linear_permutations\":" << linear_count
            << ",\n  \"pairs_tested\":" << pair_tested << ",\n  \"pair_types_by_nonlinear_count\":["
            << pair_types[0] << ',' << pair_types[1] << ',' << pair_types[2] << "],\n"
            << "  \"criterion_mismatches\":" << criterion_mismatches << ",\n"
            << "  \"triple_types_by_nonlinear_count\":[" << triple_types[0] << ',' << triple_types[1] << ','
            << triple_types[2] << ',' << triple_types[3] << "],\n"
            << "  \"four_types_by_nonlinear_count\":[" << four_types[0] << ',' << four_types[1] << ','
            << four_types[2] << ',' << four_types[3] << ',' << four_types[4] << "],\n"
            << "  \"positive_control\":{\"row_column_gram_checks\":" << gram.row_checks
            << ",\"row_column_errors\":" << gram.row_errors << ",\"pair_gram_checks\":" << gram.pair_checks
            << ",\"pair_gram_errors\":" << gram.pair_errors << "},\n"
            << "  \"duplicate_pair_control_errors\":" << neg << ",\n"
            << "  \"elapsed_seconds\":" << elapsed << "\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        std::cout << "permutations=" << squares.size() << " linear=" << linear_count << " pairs=" << pair_tested
                  << " pair_types=" << pair_types[0] << ',' << pair_types[1] << ',' << pair_types[2]
                  << " criterion_mismatches=" << criterion_mismatches << '\n';
        std::cout << "triples=" << triple_types[0] << ',' << triple_types[1] << ',' << triple_types[2] << ',' << triple_types[3]
                  << " quads=" << four_types[0] << ',' << four_types[1] << ',' << four_types[2] << ',' << four_types[3] << ',' << four_types[4] << '\n';
        std::cout << "row_checks=" << gram.row_checks << " row_errors=" << gram.row_errors
                  << " pair_checks=" << gram.pair_checks << " pair_errors=" << gram.pair_errors
                  << " duplicate_pair_errors=" << neg << " elapsed=" << elapsed << "s\n";
        return criterion_mismatches || gram.row_errors || gram.pair_errors || neg == 0 ? 1 : 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
