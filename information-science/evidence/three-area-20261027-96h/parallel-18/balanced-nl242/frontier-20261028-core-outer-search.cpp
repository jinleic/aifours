// Exact local-restriction solver for bounded outer flips, with full Boolean witness output.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
constexpr int N = 512, LOCAL = 16, PATTERNS = 65536, WORDS = PATTERNS / 64, LEVELS = 17;
using Table = std::array<int, N>;
static std::uint64_t exact[LOCAL][LEVELS][WORDS];
static std::uint64_t cumulative[LOCAL][LEVELS][WORDS];
static int prefix_count[LOCAL][LEVELS];
static std::int8_t local_walsh[PATTERNS][LOCAL];
static std::int8_t delta[N][N];

int nibble(char c) {
    if (c >= '0' && c <= '9') return c - '0';
    if (c >= 'a' && c <= 'f') return c - 'a' + 10;
    if (c >= 'A' && c <= 'F') return c - 'A' + 10;
    return -1;
}
std::vector<Table> load_seeds(const std::string& file) {
    std::ifstream in(file);
    if (!in) throw std::runtime_error("cannot open seed file");
    std::vector<Table> seeds;
    std::string line;
    while (std::getline(in, line)) {
        if (line.empty() || line[0] == '#') continue;
        if (line.size() != 128) throw std::runtime_error("invalid hexadecimal seed length");
        Table bits{};
        for (int i = 0; i < 128; ++i) {
            const int x = nibble(line[i]);
            if (x < 0) throw std::runtime_error("invalid hexadecimal seed digit");
            for (int j = 0; j < 4; ++j) bits[4 * i + j] = (x >> (3 - j)) & 1;
        }
        seeds.push_back(bits);
    }
    return seeds;
}
void require_unused(const std::string& name) {
    std::ifstream in(name);
    if (in.good()) throw std::runtime_error("refusing to overwrite " + name);
}
void fwht(int* w, int n) {
    for (int d = 1; d < n; d *= 2)
        for (int start = 0; start < n; start += 2 * d)
            for (int j = 0; j < d; ++j) {
                const int u = w[start + j], v = w[start + d + j];
                w[start + j] = u + v;
                w[start + d + j] = u - v;
            }
}
void precompute_local() {
    for (int p = 0; p < PATTERNS; ++p) {
        int w[LOCAL];
        for (int x = 0; x < LOCAL; ++x) w[x] = 1 - 2 * ((p >> x) & 1);
        fwht(w, LOCAL);
        for (int a = 0; a < LOCAL; ++a) {
            if (w[a] < -16 || w[a] > 16 || (w[a] & 1)) throw std::runtime_error("bad local Walsh value");
            local_walsh[p][a] = static_cast<std::int8_t>(w[a]);
            exact[a][(w[a] + 16) / 2][p / 64] |= std::uint64_t{1} << (p % 64);
        }
    }
    for (int a = 0; a < LOCAL; ++a) {
        int count = 0;
        for (int v = 0; v < LEVELS; ++v) {
            for (int w = 0; w < WORDS; ++w) {
                cumulative[a][v][w] = exact[a][v][w] | (v ? cumulative[a][v - 1][w] : 0);
                count += __builtin_popcountll(exact[a][v][w]);
            }
            prefix_count[a][v] = count;
        }
        if (count != PATTERNS) throw std::runtime_error("local mask partition mismatch");
    }
}

struct Outcome {
    long long tested = 0, valid_outer = 0, valid_local_pairs = 0, target_outer = 0, target_local_pairs = 0;
    int first_outer_x = -1, first_outer_y = -1, first_local = -1, first_frequency = -1;
    bool complete = false, timed_out = false, stopped_for_witness = false;
};

struct Problem {
    Table bits{}, r0{}, alpha{};
    std::array<int, LOCAL> coords{};
    std::vector<int> outside;
    int origin = 365;
    std::array<int, 4> basis{};
};

Problem build_problem(const Table& bits, int index) {
    Problem p;
    p.bits = bits;
    p.basis = index == 2 ? std::array<int, 4>{63,90,139,278} : std::array<int, 4>{27,45,195,325};
    std::array<bool, N> in_core{};
    for (int u = 0; u < LOCAL; ++u) {
        int x = p.origin;
        for (int i = 0; i < 4; ++i) if (u & (1 << i)) x ^= p.basis[i];
        if (x < 0 || x >= N || in_core[x]) throw std::runtime_error("invalid core basis");
        in_core[x] = true;
        p.coords[u] = x;
    }
    for (int x = 0; x < N; ++x) if (!in_core[x]) p.outside.push_back(x);
    if (p.outside.size() != 496) throw std::runtime_error("incorrect outer cardinality");
    for (int a = 0; a < N; ++a) {
        const int orientation = __builtin_parity(a & p.origin) ? -1 : 1;
        int r = 0, alpha = 0;
        for (int i = 0; i < 4; ++i) if (__builtin_parity(a & p.basis[i])) alpha |= 1 << i;
        for (int x : p.outside) {
            const int char_ax = __builtin_parity(a & x) ? -1 : 1;
            const int s = 1 - 2 * bits[x];
            r += orientation * s * char_ax;
            delta[x][a] = static_cast<std::int8_t>(-2 * orientation * s * char_ax);
        }
        p.r0[a] = r;
        p.alpha[a] = alpha;
    }
    return p;
}

bool evaluate(const Problem& p, int x, int y, Outcome& out) {
    int low[LOCAL], high[LOCAL], min_r[LOCAL], max_r[LOCAL];
    unsigned zero_values[LOCAL]{};
    for (int a = 0; a < LOCAL; ++a) {
        min_r[a] = std::numeric_limits<int>::max();
        max_r[a] = std::numeric_limits<int>::min();
    }
    for (int a = 0; a < N; ++a) {
        const int r = p.r0[a] + delta[x][a] + (y >= 0 ? delta[y][a] : 0);
        const int group = p.alpha[a];
        min_r[group] = std::min(min_r[group], r);
        max_r[group] = std::max(max_r[group], r);
        if (-16 <= r && r <= 16 && !(r & 1)) zero_values[group] |= 1u << ((16 - r) / 2);
    }
    std::array<int, LOCAL> order{};
    bool possible_zero = false;
    for (int a = 0; a < LOCAL; ++a) {
        const int min_l = -28 - min_r[a], max_l = 28 - max_r[a];
        low[a] = 0;
        while (low[a] < LEVELS && -16 + 2 * low[a] < min_l) ++low[a];
        high[a] = LEVELS - 1;
        while (high[a] >= 0 && -16 + 2 * high[a] > max_l) --high[a];
        if (low[a] > high[a] || low[a] == LEVELS || high[a] < 0) return false;
        unsigned usable = 0;
        for (int v = low[a]; v <= high[a]; ++v) usable |= 1u << v;
        zero_values[a] &= usable;
        possible_zero |= zero_values[a] != 0;
        order[a] = a;
    }
    std::sort(order.begin(), order.end(), [&](int a, int b) {
        const int ca = prefix_count[a][high[a]] - (low[a] ? prefix_count[a][low[a] - 1] : 0);
        const int cb = prefix_count[b][high[b]] - (low[b] ? prefix_count[b][low[b] - 1] : 0);
        return ca < cb;
    });
    bool any_valid = false, any_target = false;
    for (int word = 0; word < WORDS; ++word) {
        std::uint64_t valid = ~std::uint64_t{0};
        for (int a : order) {
            const auto below = low[a] ? cumulative[a][low[a] - 1][word] : 0;
            valid &= cumulative[a][high[a]][word] & ~below;
            if (!valid) break;
        }
        if (!valid) continue;
        any_valid = true;
        out.valid_local_pairs += __builtin_popcountll(valid);
        if (!possible_zero) continue;
        std::uint64_t zeros = 0;
        for (int a = 0; a < LOCAL; ++a) {
            unsigned candidates = zero_values[a];
            while (candidates) {
                const int level = __builtin_ctz(candidates);
                zeros |= exact[a][level][word];
                candidates &= candidates - 1;
            }
        }
        const std::uint64_t target = valid & zeros;
        if (target) {
            any_target = true;
            out.target_local_pairs += __builtin_popcountll(target);
            if (out.first_local < 0) {
                const int pattern = word * 64 + __builtin_ctzll(target);
                int frequency = -1;
                for (int a = 0; a < N; ++a) {
                    const int r = p.r0[a] + delta[x][a] + (y >= 0 ? delta[y][a] : 0);
                    if (r + local_walsh[pattern][p.alpha[a]] == 0) { frequency = a; break; }
                }
                if (frequency < 0) throw std::runtime_error("zero mask lacks a frequency");
                out.first_outer_x = x; out.first_outer_y = y;
                out.first_local = pattern; out.first_frequency = frequency;
            }
        }
    }
    if (any_valid) ++out.valid_outer;
    if (any_target) ++out.target_outer;
    return any_target;
}

void write_witness(const Problem& p, const Outcome& r, const std::string& name, int seed) {
    require_unused(name);
    Table bits = p.bits;
    bits[r.first_outer_x] ^= 1;
    if (r.first_outer_y >= 0) bits[r.first_outer_y] ^= 1;
    for (int u = 0; u < LOCAL; ++u) bits[p.coords[u]] = (r.first_local >> u) & 1;
    for (int x = 0; x < N; ++x) bits[x] ^= __builtin_parity(x & r.first_frequency);
    int w[N];
    for (int x = 0; x < N; ++x) w[x] = 1 - 2 * bits[x];
    fwht(w, N);
    int peak = 0;
    for (int value : w) peak = std::max(peak, std::abs(value));
    if (w[0] != 0 || peak > 28) throw std::runtime_error("computed target failed internal check");
    std::ofstream file(name);
    if (!file) throw std::runtime_error("cannot create witness file");
    file << "{\n  \"format\": \"boolean-truth-v1\",\n  \"source_seed_index_1based\": " << seed
         << ",\n  \"outside_flip_indices\": [" << r.first_outer_x;
    if (r.first_outer_y >= 0) file << ',' << r.first_outer_y;
    file << "],\n  \"core_origin\": " << p.origin << ",\n  \"core_basis\": ["
         << p.basis[0] << ',' << p.basis[1] << ',' << p.basis[2] << ',' << p.basis[3]
         << "],\n  \"local_pattern\": " << r.first_local
         << ",\n  \"affine_twist_frequency\": " << r.first_frequency << ",\n  \"bits\": \"";
    for (int bit : bits) file << bit;
    file << "\"\n}\n";
    if (!file) throw std::runtime_error("witness write failed");
}
}  // namespace

int main(int argc, char** argv) {
    try {
        if (argc != 7) throw std::runtime_error("usage: core-outer SEEDS SEED_INDEX single|pair LIMIT MAX_SECONDS RESULT_JSON");
        const int seed_index = std::stoi(argv[2]);
        const std::string mode = argv[3], out_file = argv[6];
        const long long limit = std::stoll(argv[4]);
        const int max_seconds = std::stoi(argv[5]);
        if ((mode != "single" && mode != "pair") || limit < 0 || max_seconds < 1 || max_seconds > 300)
            throw std::runtime_error("invalid search arguments");
        require_unused(out_file);
        const auto seeds = load_seeds(argv[1]);
        if (seed_index < 1 || seed_index > static_cast<int>(seeds.size()) || seed_index > 3)
            throw std::runtime_error("invalid seed index");
        precompute_local();
        const Problem p = build_problem(seeds[seed_index - 1], seed_index);
        const auto start = std::chrono::steady_clock::now();
        Outcome result;
        bool stop = false;
        for (std::size_t i = 0; i < p.outside.size() && !stop; ++i) {
            const std::size_t begin = mode == "single" ? i : i + 1;
            const std::size_t end = mode == "single" ? i + 1 : p.outside.size();
            for (std::size_t j = begin; j < end; ++j) {
                const int x = p.outside[i], y = mode == "single" ? -1 : p.outside[j];
                ++result.tested;
                if (evaluate(p, x, y, result)) { result.stopped_for_witness = true; stop = true; break; }
                if (result.tested % 10000 == 0) std::cout << "tested=" << result.tested << " valid_outer=" << result.valid_outer << std::endl;
                if (limit && result.tested >= limit) { stop = true; break; }
                if ((result.tested & 127) == 0 &&
                    std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count() >= max_seconds) {
                    result.timed_out = true; stop = true; break;
                }
            }
        }
        const long long all = mode == "single" ? 496 : 496LL * 495 / 2;
        result.complete = result.tested == all;
        if (result.stopped_for_witness)
            write_witness(p, result, "frontier-20261028-core-outer-witness-seed" + std::to_string(seed_index) + ".json", seed_index);
        const double elapsed = std::chrono::duration<double>(std::chrono::steady_clock::now() - start).count();
        std::ofstream out(out_file);
        if (!out) throw std::runtime_error("cannot create result");
        out << "{\n  \"seed_index_1based\":" << seed_index << ",\n  \"mode\":\"" << mode << "\",\n"
            << "  \"outer_positions\":496,\n  \"total_outer_subsets\":" << all
            << ",\n  \"tested\":" << result.tested << ",\n  \"complete\":" << (result.complete ? "true" : "false")
            << ",\n  \"timed_out\":" << (result.timed_out ? "true" : "false")
            << ",\n  \"stopped_for_witness\":" << (result.stopped_for_witness ? "true" : "false")
            << ",\n  \"valid_outer_subsets\":" << result.valid_outer
            << ",\n  \"valid_outer_local_pairs\":" << result.valid_local_pairs
            << ",\n  \"target_outer_subsets\":" << result.target_outer
            << ",\n  \"target_outer_local_pairs\":" << result.target_local_pairs
            << ",\n  \"first_outer_x\":" << result.first_outer_x << ",\n  \"first_outer_y\":" << result.first_outer_y
            << ",\n  \"first_local_pattern\":" << result.first_local << ",\n  \"first_zero_frequency\":" << result.first_frequency
            << ",\n  \"elapsed_seconds\":" << elapsed << "\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        std::cout << "seed=" << seed_index << " mode=" << mode << " tested=" << result.tested << '/' << all
                  << " complete=" << result.complete << " valid_outer=" << result.valid_outer
                  << " valid_local_pairs=" << result.valid_local_pairs << " target_outer=" << result.target_outer
                  << " target_local_pairs=" << result.target_local_pairs << " elapsed=" << elapsed << "s\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
