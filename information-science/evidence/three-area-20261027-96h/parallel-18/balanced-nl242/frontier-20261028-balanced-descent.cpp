// Exact whole-neighborhood balance-preserving descent, with bounded plateau walk.
#include <array>
#include <algorithm>
#include <cstdint>
#include <chrono>
#include <fstream>
#include <iostream>
#include <limits>
#include <stdexcept>
#include <string>
#include <unordered_set>

namespace {
constexpr int N=512;
using Table=std::array<int,N>;
using Key=std::array<std::uint64_t,8>;
struct Hash { std::size_t operator()(const Key& k) const noexcept {
    std::size_t h=0; for (auto x:k) h^=x+0x9e3779b97f4a7c15ULL+(h<<6)+(h>>2); return h;
} };
signed char chars[N][N];
std::array<std::array<int,256>,N> active{};
std::uint64_t next(std::uint64_t& state) {
    auto z=(state+=0x9e3779b97f4a7c15ULL); z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;
    z=(z^(z>>27))*0x94d049bb133111ebULL; return z^(z>>31);
}
void fwht(Table& w) {
    for (int d=1;d<N;d*=2) for (int b=0;b<N;b+=2*d) for (int j=0;j<d;++j) {
        const int a=w[b+j],c=w[b+d+j]; w[b+j]=a+c; w[b+d+j]=a-c;
    }
}
Table load(const std::string& path) {
    std::ifstream in(path); if (!in) throw std::runtime_error("input unavailable");
    const std::string s((std::istreambuf_iterator<char>(in)),{});
    const auto k=s.find("\"bits\""),c=s.find(':',k),l=s.find('"',c),r=s.find('"',l+1);
    if (k==s.npos||c==s.npos||l==s.npos||r==s.npos||r-l-1!=N) throw std::runtime_error("bad bits field");
    Table f{}; for (int x=0;x<N;++x) { if (s[l+1+x]!='0'&&s[l+1+x]!='1') throw std::runtime_error("nonbinary bit"); f[x]=s[l+1+x]-'0'; }
    return f;
}
struct State {
    Table bits{},k{}; std::array<int,256> ones{},zeros{}; Key key{}; int n8=0,n7=0;
};
State init(const Table& f) {
    State s; s.bits=f; Table w{}; int n1=0,n0=0;
    for (int x=0;x<N;++x) {
        if (f[x]) { if (n1>=256) throw std::runtime_error("unbalanced input"); s.ones[n1++]=x; s.key[x/64]|=1ULL<<(x%64); }
        else { if (n0>=256) throw std::runtime_error("unbalanced input"); s.zeros[n0++]=x; }
        w[x]=1-2*f[x];
    }
    if (n1!=256||n0!=256) throw std::runtime_error("unbalanced input");
    fwht(w); if (w[0]!=0) throw std::runtime_error("nonzero DC");
    for (int a=0;a<N;++a) {
        if (w[a]%4 || std::abs(w[a])>32) throw std::runtime_error("input exceeds Walsh peak 32");
        s.k[a]=w[a]/4; s.n8+=std::abs(s.k[a])==8; s.n7+=std::abs(s.k[a])==7;
    }
    return s;
}
void require_unused(const std::string& path) { if (std::ifstream(path).good()) throw std::runtime_error("refusing overwrite "+path); }
void save(const std::string& path,const State& s,std::uint64_t seed,int step) {
    require_unused(path); const State c=init(s.bits);
    if (c.k!=s.k||c.n8!=s.n8||c.n7!=s.n7||c.key!=s.key) throw std::runtime_error("incremental state mismatch");
    std::ofstream out(path); if (!out) throw std::runtime_error("cannot open candidate output");
    out << "{\n  \"format\":\"boolean-truth-v1\",\n  \"rng_seed\":"<<seed<<",\n  \"step\":"<<step
        <<",\n  \"reported_peak\":"<<(s.n8?32:28)<<",\n  \"n32\":"<<s.n8<<",\n  \"n28\":"<<s.n7<<",\n  \"bits\":\"";
    for (int b:s.bits) out<<b; out<<"\"\n}\n";
    if (!out) throw std::runtime_error("candidate write failed");
}
}
int main(int argc,char** argv) {
    try {
        if (argc!=6) throw std::runtime_error("usage: descent INPUT_JSON RNG_SEED MAX_STEPS MAX_SECONDS OUTPUT_PREFIX");
        const std::uint64_t seed=std::stoull(argv[2]); std::uint64_t rng=seed;
        const int max_steps=std::stoi(argv[3]),max_seconds=std::stoi(argv[4]);
        if (max_steps<1||max_seconds<1||max_seconds>300) throw std::runtime_error("invalid bounds");
        const std::string base=argv[5],candidate=base+"-candidate.json",receipt=base+"-result.json";
        require_unused(candidate); require_unused(receipt);
        for (int x=0;x<N;++x) for (int a=0;a<N;++a) chars[x][a]=__builtin_parity(x&a)?-1:1;
        for (int d=1;d<N;++d) { int n=0; for (int a=0;a<N;++a) if (__builtin_parity(a&d)) active[d][n++]=a;
            if (n!=256) throw std::runtime_error("wrong active frequency count"); }
        State current=init(load(argv[1])), best=current;
        std::unordered_set<Key,Hash> visited; visited.insert(current.key);
        const auto start=std::chrono::steady_clock::now();
        int steps=0,best_at=0; long long neighbors=0,admissible=0; bool timed_out=false,exhausted=false;
        while (steps<max_steps && current.n8) {
            int best_d8=std::numeric_limits<int>::max(),best_d7=std::numeric_limits<int>::max();
            int chosen_i=-1,chosen_j=-1; std::uint64_t ties=0;
            for (int i=0;i<256;++i) for (int j=0;j<256;++j) {
                ++neighbors; const int x=current.ones[i],y=current.zeros[j],d=x^y;
                int delta8=0,delta7=0; bool valid=true;
                for (int a:active[d]) {
                    const int old=current.k[a],v=old+chars[x][a];
                    if (std::abs(v)>8) { valid=false; break; }
                    delta8+=(std::abs(v)==8)-(std::abs(old)==8);
                    delta7+=(std::abs(v)==7)-(std::abs(old)==7);
                }
                if (!valid) continue;
                ++admissible;
                if (delta8>best_d8 || (delta8==best_d8&&delta7>best_d7)) continue;
                Key new_key=current.key; new_key[x/64]^=1ULL<<(x%64); new_key[y/64]^=1ULL<<(y%64);
                if (visited.count(new_key)) continue;
                if (delta8<best_d8 || delta7<best_d7) { best_d8=delta8; best_d7=delta7; ties=0; }
                ++ties;
                if (next(rng)%ties==0) { chosen_i=i; chosen_j=j; }
            }
            if (chosen_i<0||best_d8>0) { exhausted=true; break; }
            const int x=current.ones[chosen_i],y=current.zeros[chosen_j],d=x^y;
            for (int a:active[d]) current.k[a]+=chars[x][a];
            current.n8+=best_d8; current.n7+=best_d7;
            current.bits[x]=0; current.bits[y]=1; current.ones[chosen_i]=y; current.zeros[chosen_j]=x;
            current.key[x/64]^=1ULL<<(x%64); current.key[y/64]^=1ULL<<(y%64); visited.insert(current.key);
            ++steps;
            if (current.n8<best.n8 || (current.n8==best.n8&&current.n7<best.n7)) { best=current; best_at=steps; }
            if (steps%50==0) std::cout<<"steps="<<steps<<" current_n32="<<current.n8<<" best_n32="<<best.n8<<std::endl;
            if (std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=max_seconds) { timed_out=true; break; }
        }
        save(candidate,best,seed,best_at);
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream out(receipt); if (!out) throw std::runtime_error("cannot open receipt");
        out << "{\n  \"input\":\""<<argv[1]<<"\",\n  \"rng_seed\":"<<seed<<",\n  \"max_steps\":"<<max_steps
            <<",\n  \"steps\":"<<steps<<",\n  \"best_at\":"<<best_at<<",\n  \"best_n32\":"<<best.n8
            <<",\n  \"best_n28\":"<<best.n7<<",\n  \"neighbors_examined\":"<<neighbors
            <<",\n  \"peak32_admissible_neighbors\":"<<admissible<<",\n  \"distinct_states\":"<<visited.size()
            <<",\n  \"target_met\":"<<(best.n8?"false":"true")<<",\n  \"exhausted_unvisited_nonworsening\":"<<(exhausted?"true":"false")
            <<",\n  \"timed_out\":"<<(timed_out?"true":"false")<<",\n  \"elapsed_seconds\":"<<elapsed<<"\n}\n";
        if (!out) throw std::runtime_error("receipt write failed");
        std::cout<<"steps="<<steps<<" best_n32="<<best.n8<<" target="<<(!best.n8)<<" exhausted="<<exhausted<<" elapsed="<<elapsed<<"s\n";
        return 0;
    } catch (const std::exception& e) { std::cerr<<"error: "<<e.what()<<'\n'; return 1; }
}
