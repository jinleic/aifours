// Bounded four-outside-flip scan using independent Parseval/inverse bounds.
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
constexpr int N=512;
using Table=std::array<int,N>;
static std::int8_t change[N][N];
int hex_value(char c) {
    if (c>='0' && c<='9') return c-'0';
    if (c>='a' && c<='f') return c-'a'+10;
    if (c>='A' && c<='F') return c-'A'+10;
    return -1;
}
Table first_seed(const std::string& name) {
    std::ifstream in(name);
    if (!in) throw std::runtime_error("cannot read seed");
    std::string line;
    while (std::getline(in,line)) {
        if (line.empty() || line[0]=='#') continue;
        if (line.size()!=128) throw std::runtime_error("invalid seed size");
        Table bits{};
        for (int i=0;i<128;++i) {
            const int v=hex_value(line[i]);
            if (v<0) throw std::runtime_error("invalid seed digit");
            for (int j=0;j<4;++j) bits[4*i+j]=(v>>(3-j))&1;
        }
        return bits;
    }
    throw std::runtime_error("no seed");
}
}
int main(int argc,char** argv) {
    try {
        if (argc!=5) throw std::runtime_error("usage: check-quads SEEDS LIMIT MAX_SECONDS RESULT_JSON");
        const long long limit=std::stoll(argv[2]);
        const int max_seconds=std::stoi(argv[3]);
        if (limit<0 || max_seconds<1 || max_seconds>300) throw std::runtime_error("invalid bound");
        std::ifstream existing(argv[4]);
        if (existing.good()) throw std::runtime_error("refusing overwrite");
        const Table bits=first_seed(argv[1]);
        constexpr int origin=365;
        const std::array<int,4> basis{27,45,195,325};
        std::array<bool,N> core{};
        for (int u=0;u<16;++u) {
            int x=origin;
            for (int i=0;i<4;++i) if (u&(1<<i)) x^=basis[i];
            if (core[x]) throw std::runtime_error("dependent core basis");
            core[x]=true;
        }
        std::vector<int> outer;
        for (int x=0;x<N;++x) if (!core[x]) outer.push_back(x);
        if (outer.size()!=496) throw std::runtime_error("bad outside count");
        std::array<int,N> base{};
        std::array<std::array<int,32>,16> groups{};
        std::array<int,16> counts{};
        for (int a=0;a<N;++a) {
            int group=0;
            for (int i=0;i<4;++i) if (__builtin_parity(a & basis[i])) group|=1<<i;
            if (counts[group]>=32) throw std::runtime_error("frequency fibre overflow");
            groups[group][counts[group]++]=a;
            for (int x:outer) {
                const int term=(1-2*bits[x])*(__builtin_parity(a & (x^origin))?-1:1);
                base[a]+=term;
                change[x][a]=static_cast<std::int8_t>(-2*term);
            }
        }
        for (int c:counts) if (c!=32) throw std::runtime_error("frequency fibre size mismatch");
        long long tested=0, empty=0, low_energy=0, max_energy_bad_sum=0, inconclusive=0;
        bool stop=false,timed_out=false;
        int last_z=-1,last_v=-1;
        const auto start=std::chrono::steady_clock::now();
        for (std::size_t l=3;l<outer.size() && !stop;++l)
            for (std::size_t k=2;k<l && !stop;++k)
                for (std::size_t i=0;i+1<k && !stop;++i)
                    for (std::size_t j=i+1;j<k;++j) {
                        ++tested;
                        const int x=outer[i],y=outer[j],z=outer[k],v=outer[l];
                        last_z=z; last_v=v;
                        bool invalid=false;
                        int upper_energy=0,max_sum=0;
                        for (const auto& group:groups) {
                            int minimum=1000,maximum=-1000;
                            for (int a:group) {
                                const int r=base[a]+change[x][a]+change[y][a]+change[z][a]+change[v][a];
                                minimum=std::min(minimum,r); maximum=std::max(maximum,r);
                            }
                            int low=-8,high=8;
                            while (low<=8 && 2*low < -28-minimum) ++low;
                            while (high>=-8 && 2*high > 28-maximum) --high;
                            if (low>high) { invalid=true; break; }
                            const int lo2=low*low,hi2=high*high;
                            upper_energy+=std::max(lo2,hi2);
                            max_sum+=lo2>hi2?low:high;
                        }
                        if (invalid) ++empty;
                        else if (upper_energy<64) ++low_energy;
                        else if (upper_energy==64 && max_sum < -8) ++max_energy_bad_sum;
                        else ++inconclusive;
                        if (tested%10000000==0)
                            std::cout << "tested=" << tested << " inconclusive=" << inconclusive << std::endl;
                        if (limit && tested>=limit) { stop=true; break; }
                        if ((tested&4095)==0 &&
                            std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=max_seconds) {
                            timed_out=true; stop=true; break;
                        }
                    }
        const long long total=496LL*495*494*493/24;
        if (empty+low_energy+max_energy_bad_sum+inconclusive!=tested) throw std::runtime_error("incomplete accounting");
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream out(argv[4]);
        if (!out) throw std::runtime_error("cannot create result");
        out << "{\n  \"seed_index_1based\":1,\n  \"total\":" << total << ",\n  \"tested\":" << tested
            << ",\n  \"complete\":" << (tested==total?"true":"false")
            << ",\n  \"timed_out\":" << (timed_out?"true":"false")
            << ",\n  \"empty_interval\":" << empty << ",\n  \"energy_lt64\":" << low_energy
            << ",\n  \"energy64_bad_sum\":" << max_energy_bad_sum << ",\n  \"inconclusive\":" << inconclusive
            << ",\n  \"last_z\":" << last_z << ",\n  \"last_v\":" << last_v
            << ",\n  \"elapsed_seconds\":" << elapsed << "\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        std::cout << "tested=" << tested << '/' << total << " complete=" << (tested==total)
                  << " empty=" << empty << " energy_lt64=" << low_energy
                  << " energy64_bad_sum=" << max_energy_bad_sum << " inconclusive=" << inconclusive
                  << " elapsed=" << elapsed << "s\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
