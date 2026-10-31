// Reproducible bounded balance-preserving stochastic search on actual truth tables.
#include <algorithm>
#include <array>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>

namespace {
constexpr int N=512;
using Table=std::array<int,N>;
static signed char characters[N][N];
static std::array<std::array<int,256>,N> active{};
std::uint64_t rng_next(std::uint64_t& state) {
    std::uint64_t z=(state+=0x9e3779b97f4a7c15ULL);
    z=(z^(z>>30))*0xbf58476d1ce4e5b9ULL;
    z=(z^(z>>27))*0x94d049bb133111ebULL;
    return z^(z>>31);
}
double uniform(std::uint64_t& state) { return (rng_next(state)>>11)*0x1.0p-53; }
void fwht(Table& w) {
    for (int d=1;d<N;d*=2)
        for (int base=0;base<N;base+=2*d)
            for (int j=0;j<d;++j) {
                const int a=w[base+j],b=w[base+d+j];
                w[base+j]=a+b; w[base+d+j]=a-b;
            }
}
Table load_bits(const std::string& path) {
    std::ifstream in(path);
    if (!in) throw std::runtime_error("cannot open input truth table");
    const std::string text((std::istreambuf_iterator<char>(in)),std::istreambuf_iterator<char>());
    const auto key=text.find("\"bits\"");
    if (key==std::string::npos) throw std::runtime_error("missing bits field");
    const auto colon=text.find(':',key), first=text.find('"',colon), last=text.find('"',first+1);
    if (colon==std::string::npos||first==std::string::npos||last==std::string::npos||last-first-1!=N)
        throw std::runtime_error("invalid bits field");
    Table result{};
    for (int x=0;x<N;++x) {
        const char c=text[first+1+x];
        if (c!='0'&&c!='1') throw std::runtime_error("nonbinary truth bit");
        result[x]=c-'0';
    }
    return result;
}
void require_unused(const std::string& name) {
    if (std::ifstream(name).good()) throw std::runtime_error("refusing overwrite " + name);
}
int tail_cost(int value) { const int x=std::max(0,std::abs(value)-7); return x*x; }
int peak_from_bins(const std::array<int,129>& bins) {
    for (int k=128;k>=0;--k) if (bins[k]) return k;
    return 0;
}
struct State {
    Table bits{}, k{};
    std::array<int,256> ones{}, zeros{};
    std::array<int,129> bins{};
    int tail=0, n7=0;
};
State initial(const Table& bits) {
    State s;
    s.bits=bits;
    Table w{};
    int no=0,nz=0;
    for (int x=0;x<N;++x) {
        if (bits[x]) { if (no==256) throw std::runtime_error("unbalanced input"); s.ones[no++]=x; }
        else { if (nz==256) throw std::runtime_error("unbalanced input"); s.zeros[nz++]=x; }
        w[x]=1-2*bits[x];
    }
    if (no!=256||nz!=256) throw std::runtime_error("unbalanced input");
    fwht(w);
    if (w[0]!=0) throw std::runtime_error("nonzero DC at balanced input");
    for (int a=0;a<N;++a) {
        if (w[a]%4!=0) throw std::runtime_error("balanced Walsh not divisible by four");
        s.k[a]=w[a]/4;
        ++s.bins[std::abs(s.k[a])];
        s.tail+=tail_cost(s.k[a]);
        s.n7+=std::abs(s.k[a])==7;
    }
    return s;
}
void save_candidate(const std::string& path,const State& s,std::uint64_t seed,long long iteration) {
    require_unused(path);
    const State checked=initial(s.bits);
    if (checked.k!=s.k||checked.tail!=s.tail||checked.n7!=s.n7)
        throw std::runtime_error("incremental spectrum mismatch at candidate");
    std::ofstream out(path);
    if (!out) throw std::runtime_error("cannot create candidate");
    out << "{\n  \"format\":\"boolean-truth-v1\",\n  \"rng_seed\":" << seed
        << ",\n  \"iteration\":" << iteration << ",\n  \"reported_peak\":" << 4*peak_from_bins(s.bins)
        << ",\n  \"reported_tail\":" << s.tail << ",\n  \"bits\":\"";
    for (int bit:s.bits) out << bit;
    out << "\"\n}\n";
    if (!out) throw std::runtime_error("candidate write failed");
}
}
int main(int argc,char** argv) {
    try {
        if (argc!=7) throw std::runtime_error("usage: anneal INPUT_JSON RNG_SEED ITERATIONS CYCLE MAX_SECONDS OUTPUT_PREFIX");
        const std::uint64_t seed=std::stoull(argv[2]);
        const long long max_iterations=std::stoll(argv[3]), cycle=std::stoll(argv[4]);
        const int max_seconds=std::stoi(argv[5]);
        const std::string prefix=argv[6], candidate=prefix+"-candidate.json", receipt=prefix+"-result.json";
        if (max_iterations<1||cycle<1||max_seconds<1||max_seconds>300) throw std::runtime_error("invalid bounds");
        require_unused(candidate); require_unused(receipt);
        const Table bits=load_bits(argv[1]);
        State current=initial(bits), best=current;
        for (int x=0;x<N;++x)
            for (int a=0;a<N;++a)
                characters[x][a]=__builtin_parity(x&a)?-1:1;
        for (int d=1;d<N;++d) {
            int n=0;
            for (int a=0;a<N;++a) if (__builtin_parity(a&d)) active[d][n++]=a;
            if (n!=256) throw std::runtime_error("wrong active Walsh count");
        }
        int best_peak=peak_from_bins(best.bins), best_tail=best.tail, best_n7=best.n7;
        long long iterations=0,accepted=0,best_at=0;
        bool timed_out=false, target=best_peak<=7;
        std::uint64_t state=seed;
        const auto start=std::chrono::steady_clock::now();
        while (iterations<max_iterations && !target) {
            const int ix=static_cast<int>(rng_next(state)&255), iy=static_cast<int>(rng_next(state)&255);
            const int x=current.ones[ix],y=current.zeros[iy],d=x^y;
            int delta_tail=0,delta_n7=0;
            for (int a:active[d]) {
                const int old=current.k[a], next=old+characters[x][a];
                delta_tail+=tail_cost(next)-tail_cost(old);
                delta_n7+=(std::abs(next)==7)-(std::abs(old)==7);
            }
            const int delta_score=128*delta_tail+delta_n7;
            const double fraction=static_cast<double>(iterations%cycle)/static_cast<double>(cycle);
            const double temperature=512.0*std::exp(std::log(4.0/512.0)*fraction);
            const bool accept=delta_score<=0||uniform(state)<std::exp(-static_cast<double>(delta_score)/temperature);
            ++iterations;
            if (accept) {
                ++accepted;
                for (int a:active[d]) {
                    const int old=current.k[a], next=old+characters[x][a];
                    --current.bins[std::abs(old)]; ++current.bins[std::abs(next)]; current.k[a]=next;
                }
                current.tail+=delta_tail; current.n7+=delta_n7;
                current.bits[x]=0; current.bits[y]=1; current.ones[ix]=y; current.zeros[iy]=x;
                const int peak=peak_from_bins(current.bins);
                if (peak<best_peak || (peak==best_peak && (current.tail<best_tail ||
                    (current.tail==best_tail && current.n7<best_n7)))) {
                    best=current; best_peak=peak; best_tail=current.tail; best_n7=current.n7; best_at=iterations;
                }
                target=peak<=7;
                if (target) { best=current; best_peak=peak; best_tail=current.tail; best_n7=current.n7; best_at=iterations; }
            }
            if (iterations%1000000==0)
                std::cout << "iterations=" << iterations << " current_peak=" << 4*peak_from_bins(current.bins)
                          << " best_peak=" << 4*best_peak << " best_tail=" << best_tail << std::endl;
            if ((iterations&8191)==0 &&
                std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=max_seconds) {
                timed_out=true; break;
            }
        }
        save_candidate(candidate,best,seed,best_at);
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream out(receipt);
        if (!out) throw std::runtime_error("cannot create receipt");
        out << "{\n  \"input\":\"" << argv[1] << "\",\n  \"rng\":\"splitmix64\",\n  \"rng_seed\":" << seed
            << ",\n  \"max_iterations\":" << max_iterations << ",\n  \"cycle\":" << cycle
            << ",\n  \"iterations\":" << iterations << ",\n  \"accepted\":" << accepted
            << ",\n  \"best_at\":" << best_at << ",\n  \"best_peak\":" << 4*best_peak
            << ",\n  \"best_tail\":" << best_tail << ",\n  \"best_n7\":" << best_n7
            << ",\n  \"target_met\":" << (target?"true":"false")
            << ",\n  \"timed_out\":" << (timed_out?"true":"false")
            << ",\n  \"elapsed_seconds\":" << elapsed << "\n}\n";
        if (!out) throw std::runtime_error("receipt write failed");
        std::cout << "iterations=" << iterations << " accepted=" << accepted << " best_peak=" << 4*best_peak
                  << " best_tail=" << best_tail << " best_n7=" << best_n7 << " target=" << target
                  << " timed_out=" << timed_out << " elapsed=" << elapsed << "s\n";
        return 0;
    } catch (const std::exception& e) {
        std::cerr << "error: " << e.what() << '\n';
        return 1;
    }
}
