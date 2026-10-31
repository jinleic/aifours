// Export all distinct scaled-Walsh interval profiles for one/two outer flips.
#define main frontier_two_outer_entry
#include "frontier-20261028-core-outer-search.cpp"
#undef main
#include <map>

namespace {
using Intervals = std::array<std::pair<int,int>, LOCAL>;
struct Counts { long long single=0, pair=0; };
std::string key_for(const Intervals& ranges) {
    std::string key;
    key.reserve(2*LOCAL);
    for (auto item : ranges) {
        key.push_back(static_cast<char>(item.first + 8));
        key.push_back(static_cast<char>(item.second + 8));
    }
    return key;
}
std::map<std::string,Counts> catalogue(const Problem& p) {
    std::map<std::string,Counts> result;
    for (int mode = 0; mode < 2; ++mode)
        for (std::size_t i = 0; i < p.outside.size(); ++i) {
            const std::size_t start = mode ? i+1 : i, end = mode ? p.outside.size() : i+1;
            for (std::size_t j = start; j < end; ++j) {
                const int x = p.outside[i], y = mode ? p.outside[j] : -1;
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
                for (int g = 0; g < LOCAL; ++g) {
                    int lo = -8, hi = 8;
                    while (lo <= 8 && 2*lo < -28-minimum[g]) ++lo;
                    while (hi >= -8 && 2*hi > 28-maximum[g]) --hi;
                    if (lo > hi) throw std::runtime_error("empty interval; extend catalogue format");
                    ranges[g] = {lo,hi};
                }
                std::sort(ranges.begin(), ranges.end());
                auto& count = result[key_for(ranges)];
                if (mode) ++count.pair; else ++count.single;
            }
        }
    return result;
}
}
int main(int argc, char** argv) {
    try {
        if (argc != 3) throw std::runtime_error("usage: profiles SEEDS RESULT_JSON");
        require_unused(argv[2]);
        const auto input = load_seeds(argv[1]);
        if (input.size() != 3) throw std::runtime_error("expected three seeds");
        std::ofstream out(argv[2]);
        if (!out) throw std::runtime_error("cannot create output");
        out << "{\n  \"method\":\"complete sorted scaled Walsh interval profiles\",\n  \"seeds\":[\n";
        for (int i = 0; i < 3; ++i) {
            const Problem p = build_problem(input[i], i+1);
            const auto profiles = catalogue(p);
            if (i) out << ",\n";
            out << "    {\"seed_index_1based\":" << i+1 << ",\"profiles\":[";
            bool first = true;
            for (const auto& item : profiles) {
                if (!first) out << ',';
                first = false;
                out << "{\"q_intervals\":[";
                for (int j = 0; j < LOCAL; ++j) {
                    if (j) out << ',';
                    out << '[' << (static_cast<unsigned char>(item.first[2*j])-8) << ','
                        << (static_cast<unsigned char>(item.first[2*j+1])-8) << ']';
                }
                out << "],\"single\":" << item.second.single << ",\"pair\":" << item.second.pair << '}';
            }
            out << "]}";
            std::cout << "seed=" << i+1 << " profiles=" << profiles.size() << '\n';
        }
        out << "\n  ]\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
