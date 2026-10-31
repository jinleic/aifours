// Exact whole-row best-response moves for unrestricted linear Tuscan-2(11).
// The dynamic program searches every permutation of the selected row while the
// other ten rows are fixed. Restarts/kicks leave ALL rows mutable, so a failed
// run has no global nonexistence meaning. No Latin-column/wrap assumption.
// Usage: binary OUTPUT.json SEED RESTARTS MAX_SWEEPS W1 W2 INPUT_ROWS.txt
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cerrno>
#include <fcntl.h>
#include <limits>
#include <random>
#include <unistd.h>
#include <vector>

namespace {
constexpr int N = 11, PAIRS = N * N, FULL = (1 << N) - 1;
constexpr int STATES = (1 << N) * PAIRS;
constexpr int INF = std::numeric_limits<int>::max() / 4;
using Row = std::array<int, N>;
using Rows = std::array<Row, N>;
inline int index(int mask, int prev, int last) { return mask * PAIRS + prev * N + last; }

struct State {
    Rows rows{};
    std::array<std::array<int, PAIRS>, 2> count{};
    std::array<int, 2> pair_collisions{};
    std::array<int, 2> excess{};

    void update(int d, int a, int b, int delta) {
        int &c = count[d - 1][a * N + b];
        pair_collisions[d - 1] -= c * (c - 1) / 2;
        excess[d - 1] -= c > 0 ? c - 1 : 0;
        c += delta;
        if (c < 0) { std::fputs("negative event count\n", stderr); std::abort(); }
        pair_collisions[d - 1] += c * (c - 1) / 2;
        excess[d - 1] += c > 0 ? c - 1 : 0;
    }
    void adjust_row(const Row &row, int delta) {
        for (int d = 1; d <= 2; ++d)
            for (int c = 0; c + d < N; ++c)
                update(d, row[c], row[c + d], delta);
    }
    void load(const Rows &input) {
        rows = input;
        count = {}; pair_collisions = {}; excess = {};
        for (const Row &row : rows) adjust_row(row, +1);
    }
    int total() const { return pair_collisions[0] + pair_collisions[1]; }
    int weighted(int w1, int w2) const {
        return w1 * pair_collisions[0] + w2 * pair_collisions[1];
    }
    void kick(std::mt19937_64 &rng, int swaps) {
        for (int i = 0; i < swaps; ++i) {
            int r = static_cast<int>(rng() % N), a = static_cast<int>(rng() % N);
            int b = static_cast<int>(rng() % (N - 1));
            if (b >= a) ++b;
            adjust_row(rows[r], -1);
            std::swap(rows[r][a], rows[r][b]);
            adjust_row(rows[r], +1);
        }
    }
    void randomise(std::mt19937_64 &rng) {
        Rows shuffled{};
        for (Row &row : shuffled) {
            for (int c = 0; c < N; ++c) row[c] = c;
            std::shuffle(row.begin(), row.end(), rng);
        }
        load(shuffled);
    }
};

// Exact minimization given the other rows. State (mask,prev,last) remembers
// exactly the information needed for future length-1 and length-2 events.
void optimise_row(State &s, int r, int w1, int w2, std::mt19937_64 &rng,
                  std::vector<int> &dp, std::vector<uint8_t> &parent) {
    const int before = s.weighted(w1, w2);
    s.adjust_row(s.rows[r], -1);
    const int base = s.weighted(w1, w2);
    std::fill(dp.begin(), dp.end(), INF);
    std::fill(parent.begin(), parent.end(), static_cast<uint8_t>(255));
    for (int a = 0; a < N; ++a)
        for (int b = 0; b < N; ++b)
            if (a != b) dp[index((1 << a) | (1 << b), a, b)] = w1 * s.count[0][a * N + b];

    for (int mask = 0; mask <= FULL; ++mask) {
        int remaining = FULL ^ mask;
        if (!remaining) continue;
        int prev_bits = mask;
        while (prev_bits) {
            int a = __builtin_ctz(static_cast<unsigned>(prev_bits));
            prev_bits &= prev_bits - 1;
            int last_bits = mask & ~(1 << a);
            while (last_bits) {
                int b = __builtin_ctz(static_cast<unsigned>(last_bits));
                last_bits &= last_bits - 1;
                const int value = dp[index(mask, a, b)];
                if (value == INF) continue;
                int next_bits = remaining;
                while (next_bits) {
                    int c = __builtin_ctz(static_cast<unsigned>(next_bits));
                    next_bits &= next_bits - 1;
                    const int cost = value + w1 * s.count[0][b * N + c]
                                           + w2 * s.count[1][a * N + c];
                    const int target = index(mask | (1 << c), b, c);
                    if (cost < dp[target] || (cost == dp[target] && (rng() & 1U))) {
                        dp[target] = cost;
                        parent[target] = static_cast<uint8_t>(a);
                    }
                }
            }
        }
    }
    int best = INF, a = -1, b = -1;
    for (int x = 0; x < N; ++x) for (int y = 0; y < N; ++y) if (x != y) {
        const int cost = dp[index(FULL, x, y)];
        if (cost < best || (cost == best && (rng() & 1U))) { best = cost; a = x; b = y; }
    }
    if (a < 0) { std::fputs("no full row in DP\n", stderr); std::abort(); }
    Row chosen{};
    int mask = FULL;
    chosen[N - 1] = b;
    chosen[N - 2] = a;
    for (int position = N - 3; position >= 0; --position) {
        const int earlier = parent[index(mask, a, b)];
        if (earlier >= N) { std::fputs("missing DP predecessor\n", stderr); std::abort(); }
        mask ^= 1 << b;
        b = a; a = earlier;
        chosen[position] = earlier;
    }
    s.rows[r] = chosen;
    s.adjust_row(chosen, +1);
    if (s.weighted(w1, w2) != base + best || s.weighted(w1, w2) > before) {
        std::fputs("DP objective invariant failed\n", stderr);
        std::abort();
    }
}

uint64_t integer(const char *s, const char *name, bool zero = false) {
    if (*s == '-' || *s == '\0') { std::fprintf(stderr, "invalid %s\n", name); std::exit(2); }
    errno = 0;
    char *end = nullptr;
    auto value = std::strtoull(s, &end, 10);
    if (errno || *end || (!zero && value == 0)) { std::fprintf(stderr, "invalid %s\n", name); std::exit(2); }
    return static_cast<uint64_t>(value);
}
} // namespace

int main(int argc, char **argv) {
    if (argc != 8) {
        std::fprintf(stderr, "usage: %s OUTPUT SEED RESTARTS MAX_SWEEPS W1 W2 INPUT_ROWS\n", argv[0]);
        return 2;
    }
    const uint64_t seed = integer(argv[2], "seed", true);
    const uint64_t restarts = integer(argv[3], "restarts");
    const uint64_t sweeps = integer(argv[4], "sweeps");
    const uint64_t w1raw = integer(argv[5], "w1"), w2raw = integer(argv[6], "w2");
    if (restarts > 100000 || sweeps > 10000 || w1raw > 50 || w2raw > 50) {
        std::fputs("work/weight limit exceeded\n", stderr); return 2;
    }
    const int w1 = static_cast<int>(w1raw), w2 = static_cast<int>(w2raw);
    Rows input{};
    FILE *in = std::fopen(argv[7], "r");
    if (!in) { std::fprintf(stderr, "cannot open rows: %s\n", std::strerror(errno)); return 2; }
    for (Row &row : input) {
        std::array<bool, N> seen{};
        for (int &value : row) {
            if (std::fscanf(in, "%d", &value) != 1 || value < 0 || value >= N || seen[value]) {
                std::fputs("input must contain eleven permutations of 0..10\n", stderr);
                std::fclose(in); return 2;
            }
            seen[value] = true;
        }
    }
    int extra;
    if (std::fscanf(in, "%d", &extra) == 1) { std::fputs("extra input integer\n", stderr); std::fclose(in); return 2; }
    std::fclose(in);
    int fd = ::open(argv[1], O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) { std::fprintf(stderr, "cannot exclusively create output: %s\n", std::strerror(errno)); return 2; }
    FILE *out = ::fdopen(fd, "w");
    if (!out) { ::close(fd); return 2; }

    const auto started = std::chrono::steady_clock::now();
    std::mt19937_64 rng(seed);
    std::vector<int> dp(STATES);
    std::vector<uint8_t> parent(STATES);
    State state; state.load(input);
    Rows best_rows = input;
    int best_energy = state.weighted(w1, w2), best_total = state.total();
    std::array<int, 2> best_pair = state.pair_collisions, best_excess = state.excess;
    uint64_t evaluations = 0, accepted_sweeps = 0, best_restart = 0, best_sweep = 0;
    bool success = best_total == 0;
    auto capture = [&](uint64_t restart, uint64_t sweep) {
        const int energy = state.weighted(w1, w2), total = state.total();
        if (energy < best_energy || (energy == best_energy && total < best_total)) {
            best_energy = energy; best_total = total; best_rows = state.rows;
            best_pair = state.pair_collisions; best_excess = state.excess;
            best_restart = restart; best_sweep = sweep;
        }
        if (total == 0) success = true;
    };
    for (uint64_t restart = 0; restart < restarts && !success; ++restart) {
        if (restart % 8 == 7) state.randomise(rng);
        else {
            state.load(best_rows);
            if (restart > 0) state.kick(rng, 1 + static_cast<int>(rng() % 10));
        }
        std::array<int, N> order{};
        for (int i = 0; i < N; ++i) order[i] = i;
        int stagnant = 0;
        for (uint64_t sweep = 1; sweep <= sweeps && !success; ++sweep) {
            const int start_energy = state.weighted(w1, w2);
            std::shuffle(order.begin(), order.end(), rng);
            for (int r : order) {
                optimise_row(state, r, w1, w2, rng, dp, parent);
                ++evaluations;
                capture(restart, sweep);
                if (success) break;
            }
            ++accepted_sweeps;
            if (state.weighted(w1, w2) == start_energy) ++stagnant; else stagnant = 0;
            if (stagnant >= 3) break;
        }
    }
    const auto elapsed_ms = std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::steady_clock::now() - started).count();
    std::fprintf(out,
        "{\n  \"schema\": 1,\n  \"kind\": \"bounded_unrestricted_exact_row_best_response\",\n"
        "  \"seed\": %llu,\n  \"requested_restarts\": %llu,\n  \"max_sweeps\": %llu,\n"
        "  \"weight_d1\": %d,\n  \"weight_d2\": %d,\n  \"row_dp_evaluations\": %llu,\n"
        "  \"completed_sweeps\": %llu,\n  \"elapsed_ms\": %lld,\n"
        "  \"best_restart_zero_based\": %llu,\n  \"best_sweep\": %llu,\n"
        "  \"weighted_pair_collision_score\": %d,\n  \"best_pair_collision_score\": %d,\n"
        "  \"d1_pair_collisions\": %d,\n  \"d2_pair_collisions\": %d,\n"
        "  \"d1_excess_events\": %d,\n  \"d2_excess_events\": %d,\n"
        "  \"zero_score_claim\": %s,\n  \"rows\": [\n",
        static_cast<unsigned long long>(seed), static_cast<unsigned long long>(restarts),
        static_cast<unsigned long long>(sweeps), w1, w2,
        static_cast<unsigned long long>(evaluations), static_cast<unsigned long long>(accepted_sweeps),
        static_cast<long long>(elapsed_ms), static_cast<unsigned long long>(best_restart),
        static_cast<unsigned long long>(best_sweep), best_energy, best_total,
        best_pair[0], best_pair[1], best_excess[0], best_excess[1], success ? "true" : "false");
    for (int r = 0; r < N; ++r) {
        std::fputs("    [", out);
        for (int c = 0; c < N; ++c) std::fprintf(out, "%s%d", c ? ", " : "", best_rows[r][c]);
        std::fprintf(out, "]%s\n", r + 1 == N ? "" : ",");
    }
    std::fputs("  ]\n}\n", out);
    if (std::fclose(out) != 0) return 1;
    std::printf("output=%s row_dp_evaluations=%llu best=%d weighted=%d d1_pairs=%d d2_pairs=%d witness_claim=%s elapsed_ms=%lld\n",
        argv[1], static_cast<unsigned long long>(evaluations), best_total, best_energy,
        best_pair[0], best_pair[1], success ? "yes" : "no", static_cast<long long>(elapsed_ms));
    return 0;
}
