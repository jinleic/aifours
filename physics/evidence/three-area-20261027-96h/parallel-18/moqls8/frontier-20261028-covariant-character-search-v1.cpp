// Bounded exact search in a specified translation-covariant MOQLS(8) subclass.
// Not an unrestricted search; all mathematics and normalization are recorded
// in the associated scientific packet. No external dependencies or parallelism.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fcntl.h>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unistd.h>
#include <vector>

using F = std::array<unsigned char, 8>;
using Bits = std::array<uint64_t, 79>;

int mul(int a, int b) {
    int out = 0;
    for (int j = 0; j < 3; ++j) {
        if (b & 1) out ^= a;
        b >>= 1;
        a <<= 1;
        if (a & 8) a ^= 11;
    }
    return out;
}

int tr(int x) {
    int x2 = mul(x, x);
    int v = x ^ x2 ^ mul(x2, x2);
    if (v != 0 && v != 1) throw std::runtime_error("invalid GF(8) trace");
    return v;
}

bool additive(const F &f) {
    for (int x = 0; x < 8; ++x)
        for (int y = 0; y < 8; ++y)
            if (f[x ^ y] != (f[x] ^ f[y])) return false;
    return true;
}

bool compatible(const F &f, const F &g) {
    for (int z = 0; z < 8; ++z) {
        unsigned mask = 0;
        for (int x = 0; x < 8; ++x) {
            unsigned bit = 1u << (f[x] ^ g[x ^ z]);
            if (mask & bit) return false;
            mask |= bit;
        }
        if (mask != 255u) throw std::runtime_error("mask arithmetic failure");
    }
    return true;
}

struct Check {
    int row_errors = 0;
    int col_errors = 0;
    int pair_errors = 0;
    int nonclassical = 0;
    std::array<int, 4> nonclassical_members{};
    int max_intermediate_walsh = 0;
};

Check verify_full_ordinary(const std::array<F, 4> &fs) {
    int v[4][64][8]{};
    for (int a = 0; a < 4; ++a)
        for (int i = 0; i < 8; ++i)
            for (int j = 0; j < 8; ++j)
                for (int x = 0; x < 8; ++x)
                    v[a][8*i+j][x] = tr(mul(i, fs[a][x]) ^ mul(j, x)) ? -1 : 1;
    auto gram = [&](int a, int u, int w) {
        int s = 0;
        for (int x = 0; x < 8; ++x) s += v[a][u][x] * v[a][w][x];
        return s;
    };
    Check c;
    for (int a = 0; a < 4; ++a) {
        for (int i = 0; i < 8; ++i)
            for (int j = 0; j < 8; ++j)
                for (int k = 0; k < 8; ++k) {
                    int want = j == k ? 8 : 0;
                    c.row_errors += gram(a, 8*i+j, 8*i+k) != want;
                    c.col_errors += gram(a, 8*j+i, 8*k+i) != want;
                }
        for (int x = 0; x < 64; ++x)
            for (int y = x+1; y < 64; ++y) {
                int g = std::abs(gram(a, x, y));
                if (g != 0 && g != 8) {
                    c.nonclassical_members[a] = 1;
                    c.max_intermediate_walsh = std::max(c.max_intermediate_walsh, g);
                }
            }
        c.nonclassical += c.nonclassical_members[a];
        if (static_cast<bool>(c.nonclassical_members[a]) == additive(fs[a]))
            throw std::runtime_error("additivity and direct ray-Gram disagree");
    }
    for (int a = 0; a < 4; ++a)
        for (int b = a+1; b < 4; ++b)
            for (int x = 0; x < 64; ++x)
                for (int y = 0; y < 64; ++y) {
                    int want = x == y ? 64 : 0;
                    c.pair_errors += gram(a,x,y) * gram(b,x,y) != want;
                }
    return c;
}

std::string f_json(const F &f) {
    std::ostringstream s;
    s << '[';
    for (int i = 0; i < 8; ++i) { if (i) s << ','; s << int(f[i]); }
    s << ']';
    return s.str();
}

void exclusive_write(const std::string &path, const std::string &text) {
    int fd = open(path.c_str(), O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) throw std::runtime_error("cannot create exclusive output");
    size_t at = 0;
    while (at < text.size()) {
        ssize_t n = write(fd, text.data() + at, text.size() - at);
        if (n <= 0) { close(fd); throw std::runtime_error("receipt write error"); }
        at += static_cast<size_t>(n);
    }
    if (close(fd) != 0) throw std::runtime_error("receipt close error");
}

int main(int argc, char **argv) {
    try {
        if (argc != 3 || std::string(argv[1]) != "--output")
            throw std::runtime_error("usage: program --output NEW_RECEIPT");
        auto start = std::chrono::steady_clock::now();
        auto timed_out = [&]() {
            return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count() > 45.0;
        };
        for (int a = 1; a < 8; ++a) {
            unsigned mask = 0;
            for (int x = 0; x < 8; ++x) mask |= 1u << mul(a,x);
            if (mask != 255u) throw std::runtime_error("field multiplication failed");
        }
        std::array<F, 4> baseline{};
        for (int a = 0; a < 4; ++a)
            for (int x = 0; x < 8; ++x) baseline[a][x] = mul(a+1, x);
        Check base = verify_full_ordinary(baseline);
        if (base.row_errors || base.col_errors || base.pair_errors || base.nonclassical)
            throw std::runtime_error("classical baseline full Gram failed");
        auto bad = baseline;
        bad[1] = bad[0];
        Check negative = verify_full_ordinary(bad);
        if (negative.row_errors || negative.col_errors || !negative.pair_errors)
            throw std::runtime_error("pair-product negative control failed");

        std::vector<F> fs;
        F f{{0,1,2,3,4,5,6,7}};
        do { fs.push_back(f); } while (std::next_permutation(f.begin()+1, f.end()));
        if (fs.size() != 5040) throw std::runtime_error("permutation census failed");
        const size_t count = fs.size();
        std::vector<Bits> neighbors(count);
        Bits nonlin{};
        uint64_t nonlinear_count = 0, edges = 0, pairs_tested = 0;
        for (size_t i = 0; i < count; ++i) {
            if (!additive(fs[i])) { nonlin[i/64] |= uint64_t(1) << (i%64); ++nonlinear_count; }
        }
        bool complete_pairs = true, complete_cliques = false;
        size_t first_unchecked_i = count;
        for (size_t i = 0; i < count; ++i) {
            if (timed_out()) { complete_pairs = false; first_unchecked_i = i; break; }
            for (size_t j = i+1; j < count; ++j) {
                ++pairs_tested;
                if (compatible(fs[i], fs[j])) {
                    neighbors[i][j/64] |= uint64_t(1) << (j%64);
                    ++edges;
                }
            }
        }
        uint64_t triples = 0, four_cliques = 0, nonclassical_four_cliques = 0;
        std::array<int,4> found{{-1,-1,-1,-1}};
        if (complete_pairs) {
            complete_cliques = true;
            for (size_t i = 0; i < count; ++i) {
                if (timed_out()) { complete_cliques = false; first_unchecked_i = i; break; }
                for (size_t j = i+1; j < count; ++j) {
                    if (!(neighbors[i][j/64] & (uint64_t(1) << (j%64)))) continue;
                    for (size_t w = j/64; w < 79; ++w) {
                        uint64_t common = neighbors[i][w] & neighbors[j][w];
                        while (common) {
                            int bit = __builtin_ctzll(common);
                            size_t k = 64*w + static_cast<size_t>(bit);
                            common &= common - 1;
                            if (k >= count) throw std::runtime_error("invalid bit index");
                            ++triples;
                            bool prefix_nonlin = !additive(fs[i]) || !additive(fs[j]) || !additive(fs[k]);
                            for (size_t v = k/64; v < 79; ++v) {
                                uint64_t fourth = neighbors[i][v] & neighbors[j][v] & neighbors[k][v];
                                four_cliques += static_cast<uint64_t>(__builtin_popcountll(fourth));
                                uint64_t nonclassic = prefix_nonlin ? fourth : (fourth & nonlin[v]);
                                nonclassical_four_cliques += static_cast<uint64_t>(__builtin_popcountll(nonclassic));
                                if (found[0] < 0 && nonclassic) {
                                    int fourth_bit = __builtin_ctzll(nonclassic);
                                    found = {{int(i), int(j), int(k), int(64*v + fourth_bit)}};
                                }
                            }
                        }
                    }
                }
            }
        }
        Check candidate{};
        std::array<F,4> chosen{};
        bool verified_candidate = false;
        if (found[0] >= 0) {
            for (int a=0;a<4;++a) chosen[a] = fs[found[a]];
            candidate = verify_full_ordinary(chosen);
            if (candidate.row_errors || candidate.col_errors || candidate.pair_errors || !candidate.nonclassical)
                throw std::runtime_error("candidate failed direct full-ordinary Gram verification");
            verified_candidate = true;
        }
        double seconds = std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ostringstream o;
        o << "{\n  \"kind\": \"EXACT_COVARIANT_CHARACTER_SUBCLASS_SEARCH\",\n"
          << "  \"field\": \"GF(2)[x]/(x^3+x+1), bit encoding\",\n"
          << "  \"normalized_permutations\": " << count << ",\n"
          << "  \"nonlinear_permutations\": " << nonlinear_count << ",\n"
          << "  \"pairs_tested\": " << pairs_tested << ",\n"
          << "  \"compatible_pairs\": " << edges << ",\n"
          << "  \"pair_search_complete\": " << (complete_pairs?"true":"false") << ",\n"
          << "  \"clique_search_complete\": " << (complete_cliques?"true":"false") << ",\n"
          << "  \"first_unchecked_outer_index\": " << first_unchecked_i << ",\n"
          << "  \"compatible_triples\": " << triples << ",\n"
          << "  \"compatible_four_cliques\": " << four_cliques << ",\n"
          << "  \"nonclassical_four_cliques\": " << nonclassical_four_cliques << ",\n"
          << "  \"baseline_row_errors\": " << base.row_errors << ",\n"
          << "  \"baseline_column_errors\": " << base.col_errors << ",\n"
          << "  \"baseline_product_gram_errors\": " << base.pair_errors << ",\n"
          << "  \"baseline_nonclassical_members\": " << base.nonclassical << ",\n"
          << "  \"negative_duplicate_square_product_errors\": " << negative.pair_errors << ",\n"
          << "  \"candidate_found_and_full_gram_checked\": " << (verified_candidate?"true":"false") << ",\n";
        if (verified_candidate) {
            o << "  \"candidate_permutations\": [";
            for (int a=0;a<4;++a) { if (a) o << ','; o << f_json(chosen[a]); }
            o << "],\n  \"candidate_nonclassical_members\": " << candidate.nonclassical << ",\n"
              << "  \"candidate_intermediate_walsh_numerator\": " << candidate.max_intermediate_walsh << ",\n";
        }
        o << "  \"row_column_gram_entries_per_family\": 4096,\n"
          << "  \"pair_product_gram_entries_per_family\": 24576,\n"
          << "  \"duration_seconds\": " << seconds << ",\n"
          << "  \"scope\": \"Four squares from normalized permutations f of GF8 with common coordinate x: psi_ij=(1/sqrt8) sum_x (-1)^Tr(i f(x)+j x)|x>. Exact finite search only in this subclass.\"\n}\n";
        exclusive_write(argv[2], o.str());
        std::cout << o.str();
        return (complete_pairs && complete_cliques) ? 0 : 2;
    } catch (const std::exception &e) {
        std::cerr << "ERROR: " << e.what() << '\n';
        return 1;
    }
}
