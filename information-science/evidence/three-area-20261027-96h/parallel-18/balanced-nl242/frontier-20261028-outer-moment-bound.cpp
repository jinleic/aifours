// Exact necessary Parseval + origin-inverse dynamic program on outer flip intervals.
#define main frontier_two_outer_entry
#include "frontier-20261028-core-outer-search.cpp"
#undef main
#include <bitset>
#include <unordered_map>

namespace {
constexpr int OFFSET = 128;
using Intervals = std::array<std::pair<int,int>, LOCAL>;

bool moment_possible(const Intervals& interval) {
    std::array<std::bitset<65>, 257> current{}, next{};
    current[OFFSET].set(0);
    for (const auto& range : interval) {
        for (auto& item : next) item.reset();
        for (int s = 0; s < 257; ++s) {
            if (current[s].none()) continue;
            for (int q = range.first; q <= range.second; ++q) {
                const int target = s + q;
                if (target >= 0 && target < 257 && q*q <= 64)
                    next[target] |= current[s] << (q*q);
            }
        }
        current.swap(next);
    }
    return current[OFFSET - 8].test(64) || current[OFFSET + 8].test(64);
}

struct Summary { long long tested=0, empty=0, moment_rejected=0, inconclusive=0; };
Summary analyze(const Problem& p, bool pairs, std::unordered_map<std::string,bool>& cache) {
    Summary summary;
    for (std::size_t i = 0; i < p.outside.size(); ++i) {
        const std::size_t begin = pairs ? i+1 : i;
        const std::size_t end = pairs ? p.outside.size() : i+1;
        for (std::size_t j = begin; j < end; ++j) {
            ++summary.tested;
            const int x = p.outside[i], y = pairs ? p.outside[j] : -1;
            std::array<int, LOCAL> minimum{}, maximum{};
            minimum.fill(std::numeric_limits<int>::max());
            maximum.fill(std::numeric_limits<int>::min());
            for (int a = 0; a < N; ++a) {
                const int r = p.r0[a] + delta[x][a] + (y >= 0 ? delta[y][a] : 0);
                const int group = p.alpha[a];
                minimum[group] = std::min(minimum[group], r);
                maximum[group] = std::max(maximum[group], r);
            }
            Intervals ranges{};
            bool impossible = false;
            for (int g = 0; g < LOCAL; ++g) {
                int lo = -8, hi = 8;
                while (lo <= 8 && 2*lo < -28-minimum[g]) ++lo;
                while (hi >= -8 && 2*hi > 28-maximum[g]) --hi;
                if (lo > hi) { impossible = true; break; }
                ranges[g] = {lo,hi};
            }
            if (impossible) { ++summary.empty; continue; }
            std::sort(ranges.begin(), ranges.end());
            std::string key;
            key.reserve(2 * LOCAL);
            for (const auto& item : ranges) {
                key.push_back(static_cast<char>(item.first + 8));
                key.push_back(static_cast<char>(item.second + 8));
            }
            auto found = cache.find(key);
            if (found == cache.end()) found = cache.emplace(key, moment_possible(ranges)).first;
            if (found->second) ++summary.inconclusive;
            else ++summary.moment_rejected;
        }
    }
    return summary;
}
}

int main(int argc, char** argv) {
    try {
        if (argc != 3) throw std::runtime_error("usage: moment-bound SEEDS RESULT_JSON");
        require_unused(argv[2]);
        const auto input = load_seeds(argv[1]);
        if (input.size() != 3) throw std::runtime_error("expected three seeds");
        std::array<Summary,3> singles{}, pairs{};
        std::array<std::size_t,3> profiles{};
        for (int i = 0; i < 3; ++i) {
            const Problem p = build_problem(input[i], i+1);
            std::unordered_map<std::string,bool> cache;
            singles[i] = analyze(p, false, cache);
            pairs[i] = analyze(p, true, cache);
            profiles[i] = cache.size();
            std::cout << "seed=" << i+1 << " profiles=" << profiles[i]
                      << " single=" << singles[i].tested << " empty=" << singles[i].empty
                      << " moment_rejected=" << singles[i].moment_rejected << " inconclusive=" << singles[i].inconclusive
                      << " pair=" << pairs[i].tested << " empty=" << pairs[i].empty
                      << " moment_rejected=" << pairs[i].moment_rejected << " inconclusive=" << pairs[i].inconclusive << '\n';
        }
        std::ofstream out(argv[2]);
        if (!out) throw std::runtime_error("cannot create result");
        out << "{\n  \"method\":\"sorted interval profiles; exact scaled sum ±8 and energy 64 DP\",\n  \"seeds\":[\n";
        for (int i = 0; i < 3; ++i) {
            if (i) out << ",\n";
            const auto emit = [&out](const Summary& s) {
                out << "{\"tested\":" << s.tested << ",\"empty\":" << s.empty
                    << ",\"moment_rejected\":" << s.moment_rejected << ",\"inconclusive\":" << s.inconclusive << '}';
            };
            out << "    {\"seed_index_1based\":" << i+1 << ",\"distinct_profiles\":" << profiles[i]
                << ",\"single\":"; emit(singles[i]); out << ",\"pair\":"; emit(pairs[i]); out << '}';
        }
        out << "\n  ]\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
