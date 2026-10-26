// Written source only: no compilation/execution without exact parent GO.
// Dic3-developed one-point deletion route only; never unrestricted T2(11).
// Mathematical filters: deletion-obstruction-candidate-v1.md + addendum-v1.
#include <array>
#include <cerrno>
#include <chrono>
#include <csignal>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <string_view>

namespace {
constexpr int Max = 12;
using Row = std::array<int, Max>;
using Table = std::array<Row, Max>;
volatile std::sig_atomic_t interrupted = 0;
void request_stop(int) { interrupted = 1; }

enum class Check { Valid, Order, Range, RowDuplicate, AdjacentRepeat, AdjacentMissing, Distance2Repeat };
const char* check_name(Check c) {
    switch (c) {
    case Check::Valid: return "VALID";
    case Check::Order: return "ORDER";
    case Check::Range: return "RANGE";
    case Check::RowDuplicate: return "ROW_DUPLICATE";
    case Check::AdjacentRepeat: return "ADJACENT_REPEAT";
    case Check::AdjacentMissing: return "ADJACENT_MISSING";
    case Check::Distance2Repeat: return "DISTANCE2_REPEAT";
    }
    return "INVALID_CHECK_ENUM";
}
Check check_tuscan(const Table& a, int n) {
    if (n < 2 || n > Max) return Check::Order;
    for (int r = 0; r < n; ++r) {
        unsigned used = 0;
        for (int c = 0; c < n; ++c) {
            const int x = a[r][c];
            if (x < 0 || x >= n) return Check::Range;
            const unsigned bit = 1u << x;
            if (used & bit) return Check::RowDuplicate;
            used |= bit;
        }
    }
    std::array<unsigned, Max> adjacent{};
    std::array<unsigned, Max> distance2{};
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c + 1 < n; ++c) {
            const int x = a[r][c], y = a[r][c + 1];
            const unsigned bit = 1u << y;
            if (adjacent[x] & bit) return Check::AdjacentRepeat;
            adjacent[x] |= bit;
        }
    }
    const unsigned full = (1u << n) - 1u;
    for (int x = 0; x < n; ++x) {
        if (adjacent[x] != (full ^ (1u << x))) return Check::AdjacentMissing;
    }
    for (int r = 0; r < n; ++r) {
        for (int c = 0; c + 2 < n; ++c) {
            const int x = a[r][c], y = a[r][c + 2];
            const unsigned bit = 1u << y;
            if (distance2[x] & bit) return Check::Distance2Repeat;
            distance2[x] |= bit;
        }
    }
    return Check::Valid;
}

struct Group {
    int n = 0;
    const char* name = "";
    Table mul{};
    Row inverse{};
};
Group make_group(bool cyclic4) {
    Group g;
    g.n = cyclic4 ? 4 : 12;
    g.name = cyclic4 ? "C4" : "Dic3";
    g.inverse.fill(-1);
    for (int x = 0; x < g.n; ++x) {
        for (int y = 0; y < g.n; ++y) {
            if (cyclic4) {
                g.mul[x][y] = (x + y) % 4;
            } else {
                // x = a^r b^s, r in Z6, s in {0,1}; b^2=a^3.
                const int r = x % 6, s = x / 6;
                const int t = y % 6, u = y / 6;
                const int v = (r + (s ? -t : t) + 3 * s * u + 12) % 6;
                g.mul[x][y] = v + 6 * (s ^ u);
            }
        }
    }
    for (int x = 0; x < g.n; ++x) {
        for (int y = 0; y < g.n; ++y) {
            if (g.mul[x][y] == 0 && g.mul[y][x] == 0) g.inverse[x] = y;
        }
    }
    return g;
}
const char* check_group(const Group& g) {
    if (g.n < 2 || g.n > Max) return "GROUP_ORDER";
    for (int x = 0; x < g.n; ++x) {
        if (g.mul[0][x] != x || g.mul[x][0] != x) return "GROUP_IDENTITY";
        if (g.inverse[x] < 0 || g.inverse[x] >= g.n) return "GROUP_INVERSE";
        for (int y = 0; y < g.n; ++y) {
            if (g.mul[x][y] < 0 || g.mul[x][y] >= g.n) return "GROUP_RANGE";
        }
    }
    for (int x = 0; x < g.n; ++x) {
        if (g.mul[x][g.inverse[x]] != 0 || g.mul[g.inverse[x]][x] != 0) return "GROUP_INVERSE";
        for (int y = 0; y < g.n; ++y) {
            for (int z = 0; z < g.n; ++z) {
                if (g.mul[g.mul[x][y]][z] != g.mul[x][g.mul[y][z]]) return "GROUP_ASSOCIATIVITY";
            }
        }
    }
    return "VALID";
}
void develop(const Group& g, const Row& starter, Table& a) {
    for (int r = 0; r < g.n; ++r) {
        for (int c = 0; c < g.n; ++c) a[r][c] = g.mul[r][starter[c]];
    }
}
bool expect(const char* name, Check actual, Check expected) {
    const bool ok = actual == expected;
    std::cout << "{\"control\":\"" << name << "\",\"actual\":\"" << check_name(actual)
              << "\",\"expected\":\"" << check_name(expected) << "\",\"pass\":"
              << (ok ? "true" : "false") << "}\n";
    return ok;
}
bool controls() {
    Table a{};
    constexpr int positive[4][4] = {{0,1,2,3},{1,3,0,2},{2,0,3,1},{3,2,1,0}};
    for (int r = 0; r < 4; ++r) for (int c = 0; c < 4; ++c) a[r][c] = positive[r][c];
    bool ok = expect("T2_4_positive", check_tuscan(a, 4), Check::Valid);
    a[0][1] = 0;
    ok = expect("duplicate_symbol", check_tuscan(a, 4), Check::RowDuplicate) && ok;
    a[0][1] = 1;
    a[0][0] = 4;
    ok = expect("out_of_range", check_tuscan(a, 4), Check::Range) && ok;
    a[0][0] = 1; a[0][1] = 0;
    ok = expect("adjacency_mutation", check_tuscan(a, 4), Check::AdjacentRepeat) && ok;
    constexpr int walecki[6] = {0,1,5,2,4,3};
    for (int r = 0; r < 6; ++r) for (int c = 0; c < 6; ++c) a[r][c] = (r + walecki[c]) % 6;
    ok = expect("T1_not_T2_6", check_tuscan(a, 6), Check::Distance2Repeat) && ok;
    for (const bool cyclic4 : std::array<bool, 2>{true, false}) {
        const Group g = make_group(cyclic4);
        const bool valid = std::string_view(check_group(g)) == "VALID";
        std::cout << "{\"control\":\"group_" << g.name << "\",\"pass\":" << (valid ? "true" : "false") << "}\n";
        ok = valid && ok;
    }
    Group bad = make_group(false);
    bad.mul[0][1] = 0;
    const bool rejected = std::string_view(check_group(bad)) == "GROUP_IDENTITY";
    std::cout << "{\"control\":\"group_identity_mutation\",\"pass\":" << (rejected ? "true" : "false") << "}\n";
    ok = rejected && ok;
    const Group c4 = make_group(true);
    const Row starter = {0,1,3,2};
    develop(c4, starter, a);
    ok = expect("developed_C4_positive", check_tuscan(a, 4), Check::Valid) && ok;
    Table deleted{};
    for (int r = 1; r < 4; ++r) {
        int c = 0;
        for (int j = 0; j < 4; ++j) if (a[r][j] != 0) deleted[r - 1][c++] = a[r][j] - 1;
    }
    ok = expect("C4_deletion_barrier", check_tuscan(deleted, 3), Check::AdjacentRepeat) && ok;
    return ok;
}

struct Search {
    const Group& g;
    Row starter{};
    Table source{};
    Table target{};
    std::chrono::steady_clock::time_point deadline;
    std::uint64_t nodes = 0, source_starters = 0;
    bool timed_out = false, found = false, error = false;
    explicit Search(const Group& group, int seconds) : g(group), deadline(std::chrono::steady_clock::now() + std::chrono::seconds(seconds)) {}
    bool should_stop() {
        if (interrupted) return true;
        if (std::chrono::steady_clock::now() >= deadline) timed_out = true;
        return timed_out;
    }
    void leaf() {
        ++source_starters;
        develop(g, starter, source);
        if (check_tuscan(source, g.n) != Check::Valid) {
            std::cout << "{\"error\":\"constructed_source_failed_direct_definition\"}\n";
            error = true;
            return;
        }
        for (int r = 1; r < g.n; ++r) {
            int c = 0;
            for (int j = 0; j < g.n; ++j) {
                const int x = source[r][j];
                if (x != 0) target[r - 1][c++] = x - 1;
            }
            if (c != g.n - 1) { error = true; return; }
        }
        if (check_tuscan(target, g.n - 1) != Check::Valid) return;
        found = true;
        std::cout << "{\"candidate\":\"T2_11\",\"group\":\"Dic3\",\"starter\":[";
        for (int i = 0; i < g.n; ++i) std::cout << (i ? "," : "") << starter[i];
        std::cout << "],\"direct_definition\":\"VALID\"}\nBEGIN_T2_11_TABLE\n";
        for (int r = 0; r < g.n - 1; ++r) {
            for (int c = 0; c < g.n - 1; ++c) std::cout << (c ? " " : "") << target[r][c];
            std::cout << '\n';
        }
        std::cout << "END_T2_11_TABLE\n";
    }
    void visit(int k, unsigned symbols, unsigned differences, unsigned two_steps) {
        ++nodes;
        if (found || error || interrupted || timed_out) return;
        if ((nodes & 1023u) == 1u && should_stop()) return;
        if (k == g.n) { leaf(); return; }
        for (int x = 1; x < g.n; ++x) {
            // Addendum-v1 proves first entry is outside the rotation subgroup.
            if (k == 1 && x < 6) continue;
            const unsigned bit = 1u << x;
            if (symbols & bit) continue;
            if (k == g.n - 1 && ((x != 1 && x != 5) || starter[k - 1] != g.mul[x][x])) continue;
            const int d = g.mul[g.inverse[starter[k - 1]]][x];
            const unsigned dbit = 1u << d;
            if (d == 0 || (differences & dbit)) continue;
            unsigned next_two = two_steps;
            if (k >= 2) {
                const int e = g.mul[g.inverse[starter[k - 2]]][x];
                const unsigned ebit = 1u << e;
                if (e == 0 || (two_steps & ebit)) continue;
                next_two |= ebit;
            }
            starter[k] = x;
            visit(k + 1, symbols | bit, differences | dbit, next_two);
            if (found || error || interrupted || timed_out) return;
        }
    }
};
} // namespace

int main(int argc, char** argv) {
    std::signal(SIGINT, request_stop);
    std::signal(SIGTERM, request_stop);
    const bool controls_only = argc == 2 && std::string_view(argv[1]) == "controls";
    int seconds = 0;
    if (!controls_only) {
        if (argc != 3 || std::string_view(argv[1]) != "search") {
            std::cerr << "usage: PROGRAM controls | PROGRAM search SECONDS\n";
            return 64;
        }
        char* end = nullptr;
        errno = 0;
        const long parsed = std::strtol(argv[2], &end, 10);
        if (errno || end == argv[2] || *end || parsed < 1 || parsed > 600) return 64;
        seconds = static_cast<int>(parsed);
    }
    if (!controls()) return 2;
    if (controls_only) return 0;
    const Group group = make_group(false);
    Search search(group, seconds);
    const auto start = std::chrono::steady_clock::now();
    search.visit(1, 1u, 0u, 0u);
    const auto elapsed = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::steady_clock::now() - start).count();
    const char* status = search.error ? "ERROR" : search.found ? "CANDIDATE_FOUND" : (interrupted || search.timed_out) ? "UNKNOWN" : "RESTRICTED_MODEL_EXHAUSTED_WITHOUT_FORMAL_CERTIFICATE";
    std::cout << "{\"group\":\"Dic3\",\"status\":\"" << status
              << "\",\"nodes\":" << search.nodes << ",\"source_starters\":" << search.source_starters
              << ",\"elapsed_ms\":" << elapsed << ",\"threads\":1,\"full_T2_11_negative\":false}\n";
    if (search.error) return 2;
    if (search.found) return 0;
    return interrupted || search.timed_out ? 75 : 0;
}
