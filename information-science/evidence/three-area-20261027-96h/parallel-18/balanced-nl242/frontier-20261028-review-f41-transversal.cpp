// Independent normalized-transversal and rank-one physical ray census.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
constexpr int N = 8;
using Map = std::array<int, N>;

bool is_permutation(const Map& f) {
    std::array<bool, N> seen{};
    for (int x : f) {
        if (x < 0 || x >= N || seen[x]) return false;
        seen[x] = true;
    }
    return true;
}
int rank3(std::array<int, 3> v) {
    int rank = 0;
    for (int b = 2; b >= 0; --b) {
        int k = rank;
        while (k < 3 && !(v[k] & (1 << b))) ++k;
        if (k == 3) continue;
        std::swap(v[k], v[rank]);
        for (int i = 0; i < 3; ++i) if (i != rank && (v[i] & (1 << b))) v[i] ^= v[rank];
        ++rank;
    }
    return rank;
}
int polar_rank(const Map& f) {
    return rank3({f[3] ^ f[1] ^ f[2], f[5] ^ f[1] ^ f[4], f[6] ^ f[2] ^ f[4]});
}
int chi(int a, int b) { return __builtin_parity(a & b) ? -1 : 1; }

struct Square {
    Map f{};
    int rank = 0;
    std::array<std::uint8_t, 8> zero_mask{};
    std::array<std::uint8_t, 64> rays{};
};

Square build(const Map& f) {
    if (!is_permutation(f) || f[0] != 0) throw std::runtime_error("invalid normalized permutation");
    Square s;
    s.f = f;
    s.rank = polar_rank(f);
    for (int u = 0; u < N; ++u)
        for (int v = 0; v < N; ++v) {
            int sum = 0;
            for (int x = 0; x < N; ++x) sum += chi(u, f[x]) * chi(v, x);
            if (sum == 0) s.zero_mask[u] |= std::uint8_t(1u << v);
        }
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < N; ++j) {
            int mask = 0;
            for (int x = 0; x < N; ++x)
                if (chi(i, f[x]) * chi(j, x) < 0) mask |= 1 << x;
            s.rays[8 * i + j] = static_cast<std::uint8_t>(mask);
        }
    return s;
}

bool transversal(const Square& s, const Map& p) {
    for (int a = 0; a < N; ++a)
        for (int b = a + 1; b < N; ++b)
            if (!(s.zero_mask[a ^ b] & (1u << (p[a] ^ p[b])))) return false;
    return true;
}

int inner(std::uint8_t a, std::uint8_t b) {
    return 8 - 2 * __builtin_popcount(static_cast<unsigned>(a ^ b));
}

bool rank_one_structure(const Square& s, long long& gram_checks) {
    if (s.rank != 1) return false;
    std::array<int, 256> frequency{};
    for (auto r : s.rays) ++frequency[r];
    int distinct = 0;
    for (int n : frequency) {
        if (!n) continue;
        if (n != 4) return false;
        ++distinct;
    }
    if (distinct != 16) return false;
    std::array<bool, 256> first{};
    for (int j = 0; j < N; ++j) first[s.rays[j]] = true;
    int first_rows = 0, second_rows = 0;
    std::array<bool, 256> other{};
    bool other_set = false;
    for (int i = 0; i < N; ++i) {
        std::array<bool, 256> row{};
        for (int j = 0; j < N; ++j) row[s.rays[8 * i + j]] = true;
        if (row == first) ++first_rows;
        else {
            if (!other_set) { other = row; other_set = true; }
            else if (row != other) return false;
            ++second_rows;
        }
    }
    if (first_rows != 4 || second_rows != 4) return false;
    std::vector<int> e, fp;
    for (int r = 0; r < 256; ++r) {
        if (first[r] && other[r]) return false;
        if (first[r]) e.push_back(r);
        if (other[r]) fp.push_back(r);
    }
    if (e.size() != 8 || fp.size() != 8) return false;
    std::array<std::array<bool, 16>, 16> adj{};
    for (int i = 0; i < 8; ++i)
        for (int j = 0; j < 8; ++j) {
            const int value = inner(static_cast<std::uint8_t>(e[i]), static_cast<std::uint8_t>(fp[j]));
            if (value != 0 && value != 4 && value != -4) return false;
            if (value) adj[i][8 + j] = adj[8 + j][i] = true;
        }
    for (int i = 0; i < 16; ++i) {
        int degree = 0;
        for (bool edge : adj[i]) degree += edge;
        if (degree != 4) return false;
    }
    std::array<bool, 16> seen{};
    int components = 0;
    for (int i = 0; i < 16; ++i) if (!seen[i]) {
        ++components;
        std::vector<int> stack{ i };
        seen[i] = true;
        int count = 0, left = 0, right = 0;
        while (!stack.empty()) {
            const int v = stack.back(); stack.pop_back(); ++count;
            if (v < 8) ++left; else ++right;
            for (int j = 0; j < 16; ++j) if (adj[v][j] && !seen[j]) {
                seen[j] = true;
                stack.push_back(j);
            }
        }
        if (count != 8 || left != 4 || right != 4) return false;
    }
    if (components != 2) return false;
    for (int fixed = 0; fixed < N; ++fixed)
        for (int a = 0; a < N; ++a)
            for (int b = 0; b < N; ++b) {
                ++gram_checks;
                if (inner(s.rays[8 * fixed + a], s.rays[8 * fixed + b]) != (a == b ? 8 : 0)) return false;
                ++gram_checks;
                if (inner(s.rays[8 * a + fixed], s.rays[8 * b + fixed]) != (a == b ? 8 : 0)) return false;
            }
    return true;
}
}  // namespace

int main(int argc, char** argv) {
    const auto start = std::chrono::steady_clock::now();
    try {
        if (argc != 2) throw std::runtime_error("usage: transversal OUTPUT_JSON");
        std::ifstream old(argv[1]);
        if (old.good()) throw std::runtime_error("refusing to overwrite output");
        std::vector<Map> permutations;
        Map f{0,1,2,3,4,5,6,7};
        do { permutations.push_back(f); } while (std::next_permutation(f.begin() + 1, f.end()));
        if (permutations.size() != 5040) throw std::runtime_error("unexpected permutation count");
        std::array<long long, 4> ranks{}, tested{}, passing{};
        std::array<int, 4> minimum{5041,5041,5041,5041}, maximum{};
        long long rank1_squares = 0, gram_checks = 0;
        for (const auto& map : permutations) {
            const Square square = build(map);
            ++ranks[square.rank];
            int local = 0;
            for (const auto& p : permutations) {
                ++tested[square.rank];
                if (transversal(square, p)) { ++local; ++passing[square.rank]; }
            }
            minimum[square.rank] = std::min(minimum[square.rank], local);
            maximum[square.rank] = std::max(maximum[square.rank], local);
            if (square.rank == 1) {
                if (!rank_one_structure(square, gram_checks)) throw std::runtime_error("rank-one structure failed");
                ++rank1_squares;
            }
        }
        Map identity{0,1,2,3,4,5,6,7};
        Map invalid = identity; invalid[7] = invalid[6];
        long long ignored = 0;
        const bool rank0_rejected = !rank_one_structure(build(identity), ignored);
        const bool nonperm_rejected = !is_permutation(invalid);
        if (!rank0_rejected || !nonperm_rejected) throw std::runtime_error("negative control failed");
        const double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();
        std::ofstream out(argv[1]);
        if (!out) throw std::runtime_error("cannot create output");
        const auto arr = [&out](const auto& a) {
            out << '[' << a[0] << ',' << a[1] << ',' << a[2] << ',' << a[3] << ']';
        };
        out << "{\n  \"normalized_permutations\":5040,\n  \"F_counts_by_polar_rank\":"; arr(ranks);
        out << ",\n  \"transversals_tested_by_polar_rank\":"; arr(tested);
        out << ",\n  \"transversals_passing_by_polar_rank\":"; arr(passing);
        out << ",\n  \"minimum_per_F_by_rank\":"; arr(minimum);
        out << ",\n  \"maximum_per_F_by_rank\":"; arr(maximum);
        out << ",\n  \"rank_one_structure_passes\":" << rank1_squares
            << ",\n  \"rank_one_row_column_gram_entries\":" << gram_checks
            << ",\n  \"rank0_control_rejected\":" << (rank0_rejected ? "true" : "false")
            << ",\n  \"nonpermutation_control_rejected\":" << (nonperm_rejected ? "true" : "false")
            << ",\n  \"elapsed_seconds\":" << seconds << "\n}\n";
        if (!out) throw std::runtime_error("output failed");
        std::cout << "F_ranks=" << ranks[0] << ',' << ranks[1] << ',' << ranks[2] << ',' << ranks[3]
                  << " tested=" << tested[0] << ',' << tested[1] << ',' << tested[2] << ',' << tested[3]
                  << " passing=" << passing[0] << ',' << passing[1] << ',' << passing[2] << ',' << passing[3] << '\n';
        std::cout << "rank1_squares=" << rank1_squares << " row_column_gram_entries=" << gram_checks
                  << " rank0_control=REJECTED nonpermutation_control=REJECTED elapsed=" << seconds << "s\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
