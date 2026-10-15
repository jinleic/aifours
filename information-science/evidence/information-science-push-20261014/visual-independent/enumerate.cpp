#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <unordered_set>
#include <vector>

using U32 = uint32_t;
using U64 = uint64_t;
using Orbit = std::array<uint8_t, 8>;

const std::vector<std::vector<int>> CASES = {
    {3,5,6,9,10,28}, {3,5,9,22,26,28}, {3,5,10,12,22,25},
    {3,5,10,22,25,28}, {7,11,13,19,21,25}
};

struct Enumerator {
    int m;
    std::vector<int> qs, fs;
    std::vector<U32> obligations;
    std::vector<Orbit> black, white;
    std::vector<std::unordered_set<U64>> projections;
    Orbit cur{};
    U64 black_seen=0, white_seen=0;
    U64 signature(const Orbit& x, int f) const {
        std::array<uint8_t,8> p{};
        for(int i=0;i<m;++i) p[i]=x[i]&f;
        std::sort(p.begin(),p.begin()+m);
        U64 code=0;
        for(int i=0;i<m;++i) code |= U64(p[i]) << (5*i);
        return code;
    }
    void generate_black(int at, int low, U32 present) {
        if(at==m) {
            ++black_seen;
            for(auto o: obligations) if(!(o&present)) return;
            black.push_back(cur);
            for(size_t k=0;k<fs.size();++k) projections[k].insert(signature(cur,fs[k]));
            return;
        }
        for(int c=low;c<32;++c) {
            cur[at]=c;
            generate_black(at+1,c,present|(U32(1)<<c));
        }
    }
    void generate_white(int at, int low) {
        if(at==m) {
            ++white_seen;
            for(size_t k=0;k<fs.size();++k)
                if(!projections[k].count(signature(cur,fs[k]))) return;
            white.push_back(cur);
            return;
        }
        for(int c=low;c<32;++c) {
            cur[at]=c;
            generate_white(at+1,c);
        }
    }
};

int main(int argc,char**argv) {
    if(argc!=3) return 2;
    int case_no=std::stoi(argv[1]), m=std::stoi(argv[2]);
    if(case_no<0||case_no>5||m<1||m>8) return 2;
    auto start=std::chrono::steady_clock::now();
    Enumerator e; e.m=m;
    std::vector<int> forbidden;
    for(int q=0;case_no>0&&q<32;++q) {
        bool qualified=false;
        for(int a:CASES[case_no-1]) if((q&a)==a) qualified=true;
        (qualified?e.qs:forbidden).push_back(q);
    }
    for(int f:forbidden) {
        bool maximal=true;
        for(int g:forbidden) if(f!=g&&(f&g)==f) maximal=false;
        if(maximal) e.fs.push_back(f);
    }
    std::set<U32> obs;
    for(int q:e.qs) for(int f:e.fs) {
        U32 ob=0;
        for(int c=0;c<32;++c) if((c&q)&&!(c&q&f)) ob |= U32(1)<<c;
        obs.insert(ob);
    }
    for(auto ob:obs) {
        bool minimal=true;
        for(auto other:obs) if(ob!=other&&(ob&other)==other) minimal=false;
        if(minimal) e.obligations.push_back(ob);
    }
    e.projections.resize(e.fs.size());
    e.generate_black(0,0,0);
    e.cur[0]=0;
    e.generate_white(1,0);
    std::string stem="case"+std::to_string(case_no)+"_m"+std::to_string(m);
    for(auto pair:{std::make_pair("black",&e.black),std::make_pair("white",&e.white)}) {
        std::ofstream out(stem+"_"+pair.first+".bin",std::ios::binary);
        for(auto &o:*pair.second) out.write(reinterpret_cast<const char*>(o.data()),m);
    }
    double seconds=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::string json="{\"case\":"+std::to_string(case_no)+",\"m\":"+std::to_string(m)
        +",\"black_enumerated\":"+std::to_string(e.black_seen)
        +",\"black_obligations\":"+std::to_string(e.obligations.size())
        +",\"black_surviving\":"+std::to_string(e.black.size())
        +",\"white_with_zero\":"+std::to_string(e.white_seen)
        +",\"white_projection_filtered\":"+std::to_string(e.white.size())
        +",\"seconds\":"+std::to_string(seconds)+"}";
    std::ofstream(stem+"_enumeration.json") << json << '\n';
    std::cout << json << std::endl;
}
