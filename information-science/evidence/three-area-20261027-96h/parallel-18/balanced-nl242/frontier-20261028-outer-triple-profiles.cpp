// Exact bounded catalogue of scaled-Walsh interval profiles for three outside flips.
#define main frontier_two_outer_entry
#include "frontier-20261028-core-outer-search.cpp"
#undef main
#include <bitset>
#include <map>

namespace {
using Intervals = std::array<std::pair<int,int>, LOCAL>;
bool moment_possible(const Intervals& ranges) {
    std::array<std::bitset<65>, 257> dp{}, next{};
    dp[128].set(0);
    for (const auto& range : ranges) {
        for (auto& cell : next) cell.reset();
        for (int s = 0; s < 257; ++s) if (dp[s].any())
            for (int q = range.first; q <= range.second; ++q)
                if (s + q >= 0 && s + q < 257 && q*q <= 64)
                    next[s + q] |= dp[s] << (q*q);
        dp.swap(next);
    }
    return dp[120].test(64) || dp[136].test(64);
}
std::string key_for(const Intervals& ranges) {
    std::string key;
    key.reserve(2*LOCAL);
    for (const auto& r : ranges) {
        key.push_back(static_cast<char>(r.first + 8));
        key.push_back(static_cast<char>(r.second + 8));
    }
    return key;
}
struct Profile { long long count=0; bool possible=false; };
}

int main(int argc, char** argv) {
    try {
        if (argc != 6) throw std::runtime_error("usage: triple-profiles SEEDS INDEX LIMIT MAX_SECONDS RESULT_JSON");
        const int seed_index = std::stoi(argv[2]);
        const long long limit = std::stoll(argv[3]);
        const int max_seconds = std::stoi(argv[4]);
        if (seed_index < 1 || seed_index > 3 || limit < 0 || max_seconds < 1 || max_seconds > 300)
            throw std::runtime_error("invalid arguments");
        require_unused(argv[5]);
        const auto input = load_seeds(argv[1]);
        if (seed_index > static_cast<int>(input.size())) throw std::runtime_error("seed index out of range");
        const Problem p = build_problem(input[seed_index - 1], seed_index);
        std::map<std::string, Profile> profiles;
        long long tested=0, empty=0, moment_rejected=0, inconclusive=0;
        bool stop=false, timed_out=false;
        const auto start = std::chrono::steady_clock::now();
        for (std::size_t k=2; k<p.outside.size() && !stop; ++k) {
            const int z=p.outside[k];
            for (std::size_t i=0; i+1<k && !stop; ++i)
                for (std::size_t j=i+1; j<k; ++j) {
                    ++tested;
                    const int x=p.outside[i], y=p.outside[j];
                    std::array<int,LOCAL> minimum{}, maximum{};
                    minimum.fill(std::numeric_limits<int>::max());
                    maximum.fill(std::numeric_limits<int>::min());
                    for (int a=0; a<N; ++a) {
                        const int r=p.r0[a]+delta[x][a]+delta[y][a]+delta[z][a];
                        const int group=p.alpha[a];
                        minimum[group]=std::min(minimum[group],r);
                        maximum[group]=std::max(maximum[group],r);
                    }
                    Intervals ranges{};
                    bool invalid=false;
                    for (int g=0; g<LOCAL; ++g) {
                        int lo=-8, hi=8;
                        while (lo<=8 && 2*lo < -28-minimum[g]) ++lo;
                        while (hi>=-8 && 2*hi > 28-maximum[g]) --hi;
                        if (lo>hi) { invalid=true; break; }
                        ranges[g]={lo,hi};
                    }
                    if (invalid) ++empty;
                    else {
                        std::sort(ranges.begin(),ranges.end());
                        const std::string key=key_for(ranges);
                        auto found=profiles.find(key);
                        if (found==profiles.end()) found=profiles.emplace(key,Profile{0,moment_possible(ranges)}).first;
                        ++found->second.count;
                        if (found->second.possible) ++inconclusive; else ++moment_rejected;
                    }
                    if (tested % 1000000 == 0)
                        std::cout << "tested=" << tested << " profiles=" << profiles.size()
                                  << " inconclusive=" << inconclusive << std::endl;
                    if (limit && tested>=limit) { stop=true; break; }
                    if ((tested & 1023)==0 &&
                        std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count() >= max_seconds) {
                        timed_out=true; stop=true; break;
                    }
                }
        }
        const long long total=496LL*495*494/6;
        const bool complete=tested==total;
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream out(argv[5]);
        if (!out) throw std::runtime_error("cannot create result");
        out << "{\n  \"seed_index_1based\":" << seed_index << ",\n  \"total\":" << total
            << ",\n  \"tested\":" << tested << ",\n  \"complete\":" << (complete?"true":"false")
            << ",\n  \"timed_out\":" << (timed_out?"true":"false")
            << ",\n  \"empty_interval\":" << empty << ",\n  \"moment_rejected\":" << moment_rejected
            << ",\n  \"inconclusive\":" << inconclusive << ",\n  \"elapsed_seconds\":" << elapsed
            << ",\n  \"profiles\":[\n";
        bool first=true;
        for (const auto& item : profiles) {
            if (!first) out << ",\n";
            first=false;
            out << "    {\"q_intervals\":[";
            for (int i=0; i<LOCAL; ++i) {
                if (i) out << ',';
                out << '[' << (static_cast<unsigned char>(item.first[2*i])-8) << ','
                    << (static_cast<unsigned char>(item.first[2*i+1])-8) << ']';
            }
            out << "],\"count\":" << item.second.count << ",\"moment_possible\":"
                << (item.second.possible?"true":"false") << '}';
        }
        out << "\n  ]\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        std::cout << "seed=" << seed_index << " tested=" << tested << '/' << total << " complete=" << complete
                  << " profiles=" << profiles.size() << " rejected=" << moment_rejected
                  << " inconclusive=" << inconclusive << " elapsed=" << elapsed << "s\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
