// Bounded exact-histogram inverse-Walsh search; candidate only at perfect flatness.
#define main frontier_inverse_base_main
#include "frontier-20261028-balanced-anneal.cpp"
#undef main
#include <sstream>

namespace {
Table load_spectrum(const std::string& path) {
    std::ifstream in(path); if (!in) throw std::runtime_error("missing input spectrum");
    const std::string text((std::istreambuf_iterator<char>(in)),{});
    const auto key=text.find("\"spectrum_k\""),first=text.find('[',key),last=text.find(']',first);
    if (key==text.npos||first==text.npos||last==text.npos) throw std::runtime_error("invalid spectrum field");
    std::string field=text.substr(first+1,last-first-1); for (char& c:field) if (c==',') c=' ';
    std::istringstream parsed(field); Table k{};
    for (int a=0;a<N;++a) if (!(parsed>>k[a])||std::abs(k[a])>7) throw std::runtime_error("invalid spectrum value");
    int extra=0; if (parsed>>extra) throw std::runtime_error("too many spectrum values");
    int sum=0,square=0; for (int v:k) { sum+=v; square+=v*v; }
    if (k[0]||sum!=128||square!=16384) throw std::runtime_error("spectrum moments fail");
    return k;
}
int abs_score(const Table& u) { int total=0; for (int x:u) total+=std::abs(x); return total; }
void save_best(const std::string& path,const Table& k,int score,std::uint64_t seed,long long at) {
    require_unused(path); Table u=k; fwht(u); if (abs_score(u)!=score) throw std::runtime_error("inverse incremental mismatch");
    std::ofstream out(path); if (!out) throw std::runtime_error("cannot create best spectrum");
    out<<"{\n  \"scope\":\"formal spectrum unless independently verified inverse is Boolean\",\n  \"rng_seed\":"<<seed
       <<",\n  \"best_at\":"<<at<<",\n  \"inverse_l1\":"<<score<<",\n  \"spectrum_k\":[";
    for (int a=0;a<N;++a) out<<(a?",":"")<<k[a]; out<<"]\n}\n";
    if (!out) throw std::runtime_error("write failed");
}
}
int main(int argc,char** argv) {
    try {
        if (argc!=9) throw std::runtime_error("usage: inverse-anneal INPUT SEED ITERATIONS CYCLE MAX_SECONDS T_START T_END OUTPUT_PREFIX");
        const std::uint64_t seed=std::stoull(argv[2]); std::uint64_t rng=seed;
        const long long maximum=std::stoll(argv[3]),cycle=std::stoll(argv[4]); const int seconds=std::stoi(argv[5]);
        const double t0=std::stod(argv[6]),t1=std::stod(argv[7]);
        if (maximum<1||cycle<1||seconds<1||seconds>300||t0<=0||t1<=0) throw std::runtime_error("invalid bounds");
        const std::string base=argv[8],best_path=base+"-best-spectrum.json",receipt=base+"-result.json",candidate=base+"-candidate.json";
        require_unused(best_path); require_unused(receipt); require_unused(candidate);
        Table k=load_spectrum(argv[1]),u=k; fwht(u);
        Table best=k; const int initial_score=abs_score(u); int score=initial_score,best_score=score;
        std::array<std::array<int,256>,5> groups{}; std::array<int,5> sizes{};
        for (int a=0;a<N;++a) {
            int g=-1;
            if (a<256&&std::abs(k[a])!=0&&std::abs(k[a])!=4) g=0;
            else if (a>=256) {
                if (k[a]%2==0) throw std::runtime_error("odd-half parity mismatch");
                const int p=(std::abs(k[a])==1||std::abs(k[a])==7)?1:0;
                const int q=((k[a]%4+4)%4==3)?1:0;
                g=1+2*p+q;
            }
            if (g>=0) { if (sizes[g]>=256) throw std::runtime_error("group too large"); groups[g][sizes[g]++]=a; }
        }
        for (int n:sizes) if (n<2) throw std::runtime_error("empty swap group");
        for (int a=0;a<N;++a) for (int x=0;x<N;++x) characters[a][x]=__builtin_parity(a&x)?-1:1;
        for (int d=1;d<N;++d) { int n=0; for (int x=0;x<N;++x) if (__builtin_parity(x&d)) active[d][n++]=x;
            if (n!=256) throw std::runtime_error("wrong changed character count"); }
        const auto started=std::chrono::steady_clock::now();
        long long iter=0,accepted=0,best_at=0; bool timeout=false,target=(score==65536);
        if (score>65536) throw std::runtime_error("Cauchy bound violated");
        while (iter<maximum&&!target) {
            const int g=rng_next(rng)%5,ia=rng_next(rng)%sizes[g],ib=rng_next(rng)%sizes[g];
            const int a=groups[g][ia],b=groups[g][ib]; ++iter;
            if (k[a]!=k[b]) {
                const int delta=2*(k[b]-k[a]),d=a^b; int change=0;
                for (int x:active[d]) change+=std::abs(u[x]+delta*characters[a][x])-std::abs(u[x]);
                const double frac=static_cast<double>(iter%cycle)/cycle;
                const double temp=t0*std::exp(std::log(t1/t0)*frac);
                if (change>=0||uniform(rng)<std::exp(static_cast<double>(change)/temp)) {
                    ++accepted;
                    for (int x:active[d]) u[x]+=delta*characters[a][x];
                    std::swap(k[a],k[b]); score+=change;
                    if (score>65536) throw std::runtime_error("Cauchy bound violated");
                    if (score>best_score) {
                        best=k; best_score=score; best_at=iter;
                        if (best_score%256==0) std::cout<<"iteration="<<iter<<" inverse_l1="<<best_score<<std::endl;
                    }
                    target=score==65536;
                }
            }
            if ((iter&8191)==0&&std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()>=seconds) { timeout=true; break; }
        }
        save_best(best_path,best,best_score,seed,best_at);
        if (target) {
            Table actual=best; fwht(actual);
            for (int v:actual) if (std::abs(v)!=128) throw std::runtime_error("L1 maximum not flat");
            std::ofstream out(candidate); if (!out) throw std::runtime_error("cannot create candidate");
            out<<"{\n  \"format\":\"boolean-truth-v1\",\n  \"bits\":\"";
            for (int v:actual) out<<(v<0?1:0); out<<"\"\n}\n";
            if (!out) throw std::runtime_error("candidate write failed");
        }
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();
        std::ofstream out(receipt); if (!out) throw std::runtime_error("cannot create receipt");
        out<<"{\n  \"input\":\""<<argv[1]<<"\",\n  \"rng_seed\":"<<seed<<",\n  \"max_iterations\":"<<maximum
           <<",\n  \"cycle\":"<<cycle<<",\n  \"iterations\":"<<iter<<",\n  \"accepted\":"<<accepted
           <<",\n  \"t_start\":"<<t0<<",\n  \"t_end\":"<<t1<<",\n  \"initial_l1\":"<<initial_score
           <<",\n  \"best_l1\":"<<best_score<<",\n  \"best_at\":"<<best_at<<",\n  \"ideal_l1\":65536,\n  \"target_met\":"<<(target?"true":"false")
           <<",\n  \"timed_out\":"<<(timeout?"true":"false")<<",\n  \"elapsed_seconds\":"<<elapsed<<"\n}\n";
        if (!out) throw std::runtime_error("receipt write failed");
        std::cout<<"iterations="<<iter<<" accepted="<<accepted<<" initial_l1="<<initial_score<<" best_l1="<<best_score
                 <<" target="<<target<<" elapsed="<<elapsed<<"s\n";
        return 0;
    } catch (const std::exception& e) { std::cerr<<"error: "<<e.what()<<'\n'; return 1; }
}
