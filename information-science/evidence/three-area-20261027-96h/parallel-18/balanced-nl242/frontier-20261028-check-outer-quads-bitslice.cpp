// Independent bit-sliced four-outside-flip Parseval/inverse certificate.
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
using Bits=std::array<int,N>;
using Masks=std::array<std::uint32_t,16>;
static std::array<Masks,N> plus_mask{};
int hex_value(char c) {
    if (c>='0'&&c<='9') return c-'0';
    if (c>='a'&&c<='f') return c-'a'+10;
    if (c>='A'&&c<='F') return c-'A'+10;
    return -1;
}
Bits first_seed(const std::string& path) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("cannot read seed");
    std::string line;
    while (std::getline(in,line)) {
        if (line.empty() || line[0]=='#') continue;
        if (line.size()!=128) throw std::runtime_error("invalid seed length");
        Bits bits{};
        for (int i=0;i<128;++i) {
            const int v=hex_value(line[i]);
            if (v<0) throw std::runtime_error("invalid seed digit");
            for (int j=0;j<4;++j) bits[4*i+j]=(v>>(3-j))&1;
        }
        return bits;
    }
    throw std::runtime_error("no seed");
}
std::array<std::uint32_t,5> pop_masks(std::uint32_t a,std::uint32_t b,std::uint32_t c,std::uint32_t d) {
    const std::uint32_t x0=a^b, x1=a&b, y0=c^d, y1=c&d;
    const std::uint32_t carry=x0&y0, s0=x0^y0, s1=x1^y1^carry;
    const std::uint32_t s2=(x1&y1)|(x1&carry)|(y1&carry);
    return {~s2&~s1&~s0, ~s2&~s1&s0, ~s2&s1&~s0, ~s2&s1&s0, s2};
}
void test_pop_masks() {
    for (int bits=0;bits<16;++bits) {
        auto m=pop_masks(bits&1?UINT32_MAX:0, bits&2?UINT32_MAX:0,
                         bits&4?UINT32_MAX:0, bits&8?UINT32_MAX:0);
        const int expected=__builtin_popcount(static_cast<unsigned>(bits));
        for (int i=0;i<5;++i)
            if (m[i]!=(i==expected?UINT32_MAX:0)) throw std::runtime_error("bit-slice control failed");
    }
}
}
int main(int argc,char** argv) {
    try {
        if (argc!=5) throw std::runtime_error("usage: bitslice SEEDS LIMIT MAX_SECONDS RESULT_JSON");
        const long long limit=std::stoll(argv[2]);
        const int max_seconds=std::stoi(argv[3]);
        if (limit<0||max_seconds<1||max_seconds>300) throw std::runtime_error("invalid bounds");
        std::ifstream existing(argv[4]);
        if (existing.good()) throw std::runtime_error("refusing overwrite");
        test_pop_masks();
        const Bits bits=first_seed(argv[1]);
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
        if (outer.size()!=496) throw std::runtime_error("wrong outer count");
        std::array<std::array<int,32>,16> groups{};
        std::array<int,16> group_size{};
        for (int a=0;a<N;++a) {
            int group=0;
            for (int i=0;i<4;++i) if (__builtin_parity(a&basis[i])) group|=1<<i;
            if (group_size[group]>=32) throw std::runtime_error("fibre overflow");
            groups[group][group_size[group]++]=a;
        }
        for (int n:group_size) if (n!=32) throw std::runtime_error("bad fibre size");
        constexpr std::array<int,4> values{-22,-6,10,26};
        std::array<std::array<std::uint32_t,4>,16> base_masks{};
        for (int g=0;g<16;++g)
            for (int j=0;j<32;++j) {
                const int a=groups[g][j];
                int base=0;
                for (int x:outer) {
                    const int term=(1-2*bits[x])*(__builtin_parity(a&(x^origin))?-1:1);
                    base+=term;
                    if (-2*term>0) plus_mask[x][g]|=std::uint32_t{1}<<j;
                }
                auto it=std::find(values.begin(),values.end(),base);
                if (it==values.end()) throw std::runtime_error("unexpected baseline outside value");
                base_masks[g][it-values.begin()] |= std::uint32_t{1}<<j;
            }
        long long tested=0,empty=0,low_energy=0,bad_sum=0,inconclusive=0;
        bool stop=false,timed_out=false;
        int last_z=-1,last_v=-1;
        const auto start=std::chrono::steady_clock::now();
        for (std::size_t l=3;l<outer.size()&&!stop;++l)
            for (std::size_t k=2;k<l&&!stop;++k)
                for (std::size_t i=0;i+1<k&&!stop;++i)
                    for (std::size_t j=i+1;j<k;++j) {
                        ++tested;
                        const int x=outer[i],y=outer[j],z=outer[k],v=outer[l];
                        last_z=z; last_v=v;
                        int upper_energy=0,max_sum=0;
                        bool invalid=false;
                        for (int g=0;g<16;++g) {
                            const auto pm=pop_masks(plus_mask[x][g],plus_mask[y][g],plus_mask[z][g],plus_mask[v][g]);
                            int low_r=1000,high_r=-1000;
                            for (int b=0;b<4;++b)
                                for (int count=0;count<5;++count)
                                    if (base_masks[g][b]&pm[count]) {
                                        const int r=values[b]-8+4*count;
                                        low_r=std::min(low_r,r); high_r=std::max(high_r,r);
                                    }
                            int low=-8,high=8;
                            while (low<=8 && 2*low < -28-low_r) ++low;
                            while (high>=-8 && 2*high > 28-high_r) --high;
                            if (low>high) { invalid=true; break; }
                            const int lo2=low*low,hi2=high*high;
                            upper_energy+=std::max(lo2,hi2);
                            max_sum+=lo2>hi2?low:high;
                        }
                        if (invalid) ++empty;
                        else if (upper_energy<64) ++low_energy;
                        else if (upper_energy==64 && max_sum < -8) ++bad_sum;
                        else ++inconclusive;
                        if (tested%10000000==0)
                            std::cout << "tested=" << tested << " inconclusive=" << inconclusive << std::endl;
                        if (limit&&tested>=limit) { stop=true; break; }
                        if ((tested&4095)==0 &&
                            std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=max_seconds) {
                            timed_out=true; stop=true; break;
                        }
                    }
        const long long total=496LL*495*494*493/24;
        if (empty+low_energy+bad_sum+inconclusive!=tested) throw std::runtime_error("accounting mismatch");
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream out(argv[4]);
        if (!out) throw std::runtime_error("cannot create output");
        out << "{\n  \"seed_index_1based\":1,\n  \"method\":\"independent bit-sliced outside sums and moment bounds\",\n"
            << "  \"total\":" << total << ",\n  \"tested\":" << tested
            << ",\n  \"complete\":" << (tested==total?"true":"false")
            << ",\n  \"timed_out\":" << (timed_out?"true":"false")
            << ",\n  \"empty_interval\":" << empty << ",\n  \"energy_lt64\":" << low_energy
            << ",\n  \"energy64_bad_sum\":" << bad_sum << ",\n  \"inconclusive\":" << inconclusive
            << ",\n  \"last_z\":" << last_z << ",\n  \"last_v\":" << last_v
            << ",\n  \"bit_slice_control\":\"all 16 truth assignments pass\",\n  \"elapsed_seconds\":" << elapsed << "\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        std::cout << "tested=" << tested << '/' << total << " complete=" << (tested==total)
                  << " empty=" << empty << " energy_lt64=" << low_energy
                  << " energy64_bad_sum=" << bad_sum << " inconclusive=" << inconclusive
                  << " elapsed=" << elapsed << "s\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
