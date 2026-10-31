// Bounded heuristic search for unrestricted linear Tuscan-2(11) permutation rows.
// A positive-energy output is only a candidate, never a nonexistence result.
// Usage: binary OUTPUT.json SEED RESTARTS STEPS_PER_RESTART
// OUTPUT must not already exist. Each restart starts with eleven independently
// shuffled rows; no row, symbol, column or orientation is fixed as a symmetry.
#include <algorithm>
#include <array>
#include <cerrno>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <fcntl.h>
#include <limits>
#include <random>
#include <string>
#include <unistd.h>

namespace {
constexpr int N = 11;
constexpr int CELLS = N * N;
using Row = std::array<int, N>;
using Rows = std::array<Row, N>;

struct State {
    Rows rows{};
    std::array<std::array<int, CELLS>, 2> count{};
    std::array<int, 2> pair_collisions{};
    std::array<int, 2> excess{};

    void update(int d, int a, int b, int delta) {
        int &c = count[d - 1][a * N + b];
        pair_collisions[d - 1] -= c * (c - 1) / 2;
        excess[d - 1] -= c > 0 ? c - 1 : 0;
        c += delta;
        if (c < 0) {
            std::fputs("internal negative event count\n", stderr);
            std::abort();
        }
        pair_collisions[d - 1] += c * (c - 1) / 2;
        excess[d - 1] += c > 0 ? c - 1 : 0;
    }

    void initialise(std::mt19937_64 &rng) {
        count = {};
        pair_collisions = {};
        excess = {};
        for (Row &row : rows) {
            for (int j = 0; j < N; ++j) row[j] = j;
            std::shuffle(row.begin(), row.end(), rng);
            for (int d = 1; d <= 2; ++d)
                for (int j = 0; j + d < N; ++j)
                    update(d, row[j], row[j + d], +1);
        }
    }

    // A swap changes an event only if one of its two endpoints was swapped.
    void swap_positions(int r, int a, int b) {
        Row &row = rows[r];
        for (int d = 1; d <= 2; ++d) {
            int starts[4] = {a - d, a, b - d, b};
            for (int k = 0; k < 4; ++k) {
                int s = starts[k];
                if (s < 0 || s + d >= N) continue;
                bool duplicate = false;
                for (int j = 0; j < k; ++j)
                    if (starts[j] == s) duplicate = true;
                if (!duplicate) update(d, row[s], row[s + d], -1);
            }
        }
        std::swap(row[a], row[b]);
        for (int d = 1; d <= 2; ++d) {
            int starts[4] = {a - d, a, b - d, b};
            for (int k = 0; k < 4; ++k) {
                int s = starts[k];
                if (s < 0 || s + d >= N) continue;
                bool duplicate = false;
                for (int j = 0; j < k; ++j)
                    if (starts[j] == s) duplicate = true;
                if (!duplicate) update(d, row[s], row[s + d], +1);
            }
        }
    }

    int score() const { return pair_collisions[0] + pair_collisions[1]; }
};

uint64_t integer(const char *s, const char *name, bool allow_zero = false) {
    if (*s == '-' || *s == '\0') {
        std::fprintf(stderr, "invalid %s\n", name);
        std::exit(2);
    }
    errno = 0;
    char *end = nullptr;
    auto v = std::strtoull(s, &end, 10);
    if (errno || *end || (!allow_zero && v == 0)) {
        std::fprintf(stderr, "invalid %s\n", name);
        std::exit(2);
    }
    return static_cast<uint64_t>(v);
}
} // namespace

int main(int argc, char **argv) {
    if (argc != 5) {
        std::fprintf(stderr, "usage: %s OUTPUT.json SEED RESTARTS STEPS_PER_RESTART\n", argv[0]);
        return 2;
    }
    const uint64_t seed = integer(argv[2], "seed", true);
    const uint64_t restarts = integer(argv[3], "restarts");
    const uint64_t steps = integer(argv[4], "steps");
    if (restarts > 1000000 || steps > 1000000000 ||
        restarts > std::numeric_limits<uint64_t>::max() / steps) {
        std::fputs("requested work exceeds per-run safety limit\n", stderr);
        return 2;
    }
    int fd = ::open(argv[1], O_WRONLY | O_CREAT | O_EXCL, 0644);
    if (fd < 0) {
        std::fprintf(stderr, "cannot exclusively create %s: %s\n", argv[1], std::strerror(errno));
        return 2;
    }
    FILE *out = ::fdopen(fd, "w");
    if (!out) {
        std::fprintf(stderr, "cannot open output stream: %s\n", std::strerror(errno));
        ::close(fd);
        return 2;
    }

    auto started = std::chrono::steady_clock::now();
    std::mt19937_64 rng(seed);
    std::uniform_real_distribution<double> unit(0.0, 1.0);
    State state;
    Rows best_rows{};
    int best_score = std::numeric_limits<int>::max();
    std::array<int, 2> best_pair{}, best_excess{};
    uint64_t tried = 0, accepted = 0, best_restart = 0, best_step = 0;
    bool success = false;

    auto capture = [&](uint64_t restart, uint64_t step) {
        if (state.score() < best_score) {
            best_score = state.score();
            best_rows = state.rows;
            best_pair = state.pair_collisions;
            best_excess = state.excess;
            best_restart = restart;
            best_step = step;
        }
    };

    for (uint64_t restart = 0; restart < restarts && !success; ++restart) {
        state.initialise(rng);
        capture(restart, 0);
        // Repeated cooling cycles with globally randomized restarts; each cycle
        // starts warm and ends cold. Fixed step counts make the run reproducible.
        constexpr uint64_t cycle = 200000;
        for (uint64_t step = 1; step <= steps; ++step) {
            const double phase = static_cast<double>((step - 1) % cycle) / cycle;
            const double temperature = 1.8 * std::pow(0.08, phase);
            int r = static_cast<int>(rng() % N);
            int a = static_cast<int>(rng() % N);
            // Bias three quarters of proposals toward an event currently used
            // by multiple rows; remaining swaps are fully unrestricted.
            if ((rng() & 3U) != 0) {
                for (int trial = 0; trial < 12; ++trial) {
                    int rr = static_cast<int>(rng() % N);
                    int d = static_cast<int>(rng() % 2) + 1;
                    int s = static_cast<int>(rng() % (N - d));
                    const Row &row = state.rows[rr];
                    if (state.count[d - 1][row[s] * N + row[s + d]] > 1) {
                        r = rr;
                        a = s + ((rng() & 1U) ? d : 0);
                        break;
                    }
                }
            }
            int b = static_cast<int>(rng() % (N - 1));
            if (b >= a) ++b;
            const int before = state.score();
            state.swap_positions(r, a, b);
            const int change = state.score() - before;
            ++tried;
            if (change <= 0 || unit(rng) < std::exp(-static_cast<double>(change) / temperature)) {
                ++accepted;
                capture(restart, step);
                if (best_score == 0) {
                    success = true;
                    break;
                }
            } else {
                state.swap_positions(r, a, b); // exactly undo a rejected move
            }
        }
    }
    const auto elapsed_ms = std::chrono::duration_cast<std::chrono::milliseconds>(
        std::chrono::steady_clock::now() - started).count();
    std::fprintf(out,
        "{\n  \"schema\": 1,\n  \"kind\": \"bounded_unrestricted_tuscan2_local_search\",\n"
        "  \"seed\": %llu,\n  \"requested_restarts\": %llu,\n  \"steps_per_restart\": %llu,\n"
        "  \"tried_moves\": %llu,\n  \"accepted_moves\": %llu,\n  \"elapsed_ms\": %lld,\n"
        "  \"best_restart_zero_based\": %llu,\n  \"best_step\": %llu,\n"
        "  \"best_pair_collision_score\": %d,\n  \"d1_pair_collisions\": %d,\n"
        "  \"d2_pair_collisions\": %d,\n  \"d1_excess_events\": %d,\n"
        "  \"d2_excess_events\": %d,\n  \"zero_score_claim\": %s,\n  \"rows\": [\n",
        static_cast<unsigned long long>(seed), static_cast<unsigned long long>(restarts),
        static_cast<unsigned long long>(steps), static_cast<unsigned long long>(tried),
        static_cast<unsigned long long>(accepted), static_cast<long long>(elapsed_ms),
        static_cast<unsigned long long>(best_restart), static_cast<unsigned long long>(best_step),
        best_score, best_pair[0], best_pair[1], best_excess[0], best_excess[1],
        success ? "true" : "false");
    for (int r = 0; r < N; ++r) {
        std::fputs("    [", out);
        for (int j = 0; j < N; ++j)
            std::fprintf(out, "%s%d", j ? ", " : "", best_rows[r][j]);
        std::fprintf(out, "]%s\n", r + 1 == N ? "" : ",");
    }
    std::fputs("  ]\n}\n", out);
    if (std::fclose(out) != 0) {
        std::fprintf(stderr, "failed writing output: %s\n", std::strerror(errno));
        return 1;
    }
    std::printf("output=%s seed=%llu moves=%llu best=%d d1_pairs=%d d2_pairs=%d witness_claim=%s elapsed_ms=%lld\n",
        argv[1], static_cast<unsigned long long>(seed), static_cast<unsigned long long>(tried),
        best_score, best_pair[0], best_pair[1], success ? "yes" : "no",
        static_cast<long long>(elapsed_ms));
    return 0;
}
