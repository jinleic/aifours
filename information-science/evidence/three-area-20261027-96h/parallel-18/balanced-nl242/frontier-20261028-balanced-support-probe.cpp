// Bounded search for balanced examples showing the zero-structure hypotheses matter.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>

namespace {
constexpr int N=512;
std::uint64_t next(std::uint64_t& state) {
    std::uint64_t z=(state+=0x9e3779b97f4a7c15ULL);
    z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;
    z=(z^(z>>27))*0x94d049bb133111ebULL;
    return z^(z>>31);
}
void fwht(std::array<int,N>& w) {
    for (int d=1;d<N;d*=2)
        for (int start=0;start<N;start+=2*d)
            for (int j=0;j<d;++j) {
                const int a=w[start+j],b=w[start+d+j];
                w[start+j]=a+b; w[start+d+j]=a-b;
            }
}
}
int main(int argc,char** argv) {
    try {
        if (argc!=5) throw std::runtime_error("usage: balanced-probe RNG_SEED MAX_DRAWS CANDIDATE_JSON RESULT_JSON");
        std::uint64_t rng=std::stoull(argv[1]);
        const long long limit=std::stoll(argv[2]);
        if (limit<1||limit>1000000) throw std::runtime_error("invalid draw bound");
        if (std::ifstream(argv[3]).good()||std::ifstream(argv[4]).good()) throw std::runtime_error("refusing overwrite");
        long long tested=0;
        bool found=false,target=false;
        int peak=0,support_xor=0,layer16_xor=0,layer16_count=0,zeros=0;
        std::array<int,N> bits{};
        for (long long draw=0;draw<limit;++draw) {
            for (int x=0;x<N;++x) bits[x]=(x>=N/2);
            for (int i=N-1;i>0;--i) std::swap(bits[i],bits[next(rng)%static_cast<std::uint64_t>(i+1)]);
            std::array<int,N> w{};
            for (int x=0;x<N;++x) w[x]=1-2*bits[x];
            fwht(w); ++tested;
            if (w[0]!=0) throw std::runtime_error("generated truth table is not balanced");
            peak=support_xor=layer16_xor=layer16_count=zeros=0;
            for (int a=0;a<N;++a) {
                peak=std::max(peak,std::abs(w[a]));
                if (w[a]) support_xor^=a; else ++zeros;
                if (std::abs(w[a])==16) { layer16_xor^=a; ++layer16_count; }
            }
            target=peak<=28;
            if (target||support_xor||layer16_xor||(layer16_count&1)) { found=true; break; }
        }
        if (found) {
            std::ofstream candidate(argv[3]);
            if (!candidate) throw std::runtime_error("cannot write candidate");
            candidate << "{\n  \"format\":\"boolean-truth-v1\",\n  \"draw\":" << tested
                      << ",\n  \"bits\":\"";
            for (int bit:bits) candidate << bit;
            candidate << "\"\n}\n";
            if (!candidate) throw std::runtime_error("candidate write failed");
        }
        std::ofstream out(argv[4]);
        if (!out) throw std::runtime_error("cannot write result");
        out << "{\n  \"rng_seed\":" << argv[1] << ",\n  \"max_draws\":" << limit
            << ",\n  \"tested\":" << tested << ",\n  \"found\":" << (found?"true":"false")
            << ",\n  \"target\":" << (target?"true":"false") << ",\n  \"peak\":" << peak
            << ",\n  \"support_xor\":" << support_xor << ",\n  \"layer16_xor\":" << layer16_xor
            << ",\n  \"layer16_count\":" << layer16_count << ",\n  \"zero_count\":" << zeros << "\n}\n";
        if (!out) throw std::runtime_error("result write failed");
        std::cout << "tested=" << tested << " found=" << found << " target=" << target << " peak=" << peak
                  << " support_xor=" << support_xor << " layer16_xor=" << layer16_xor
                  << " layer16_count=" << layer16_count << " zeros=" << zeros << '\n';
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
