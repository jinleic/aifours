// Bounded balanced truth-table search preserving a specified Walsh-zero plane.
#define main frontier_zero_plane_base_main
#include "frontier-20261028-balanced-anneal.cpp"
#undef main

int main(int argc,char** argv) {
    try {
        if (argc!=11) throw std::runtime_error("usage: zero-plane INPUT Z1 Z2 SEED ITERATIONS CYCLE MAX_SECONDS T_START T_END PREFIX");
        const int z1=std::stoi(argv[2]),z2=std::stoi(argv[3]);
        const std::uint64_t seed=std::stoull(argv[4]);std::uint64_t rng=seed;
        const long long maximum=std::stoll(argv[5]),cycle=std::stoll(argv[6]);const int seconds=std::stoi(argv[7]);
        const double t0=std::stod(argv[8]),t1=std::stod(argv[9]);
        if (z1<=0||z1>=N||z2<=0||z2>=N||z1==z2||maximum<1||cycle<1||seconds<1||seconds>300||t0<=0||t1<=0)
            throw std::runtime_error("invalid arguments");
        const std::string base=argv[10],candidate=base+"-candidate.json",receipt=base+"-result.json";
        require_unused(candidate);require_unused(receipt);
        State current=initial(load_bits(argv[1])),best=current;
        if (current.k[z1]||current.k[z2]||current.k[z1^z2]) throw std::runtime_error("input lacks stated zero plane");
        std::array<std::array<int,64>,4> ones{},zeros{};std::array<int,4> no{},nz{};
        for (int x=0;x<N;++x) {
            const int group=__builtin_parity(x&z1)+2*__builtin_parity(x&z2);
            if (current.bits[x]) { if (no[group]>=64) throw std::runtime_error("plane-block imbalance");ones[group][no[group]++]=x; }
            else { if (nz[group]>=64) throw std::runtime_error("plane-block imbalance");zeros[group][nz[group]++]=x; }
        }
        for (int g=0;g<4;++g) if (no[g]!=64||nz[g]!=64) throw std::runtime_error("plane-block imbalance");
        for (int x=0;x<N;++x)for (int a=0;a<N;++a)characters[x][a]=__builtin_parity(x&a)?-1:1;
        for (int d=1;d<N;++d) {int n=0;for(int a=0;a<N;++a)if(__builtin_parity(a&d))active[d][n++]=a;
            if(n!=256)throw std::runtime_error("bad active count");}
        int peak=peak_from_bins(best.bins),tail=best.tail,n7=best.n7;
        long long iter=0,accepted=0,best_at=0;bool timeout=false,target=peak<=7;
        const auto started=std::chrono::steady_clock::now();
        while(iter<maximum&&!target) {
            const int g=rng_next(rng)&3,ix=rng_next(rng)&63,iy=rng_next(rng)&63;
            const int x=ones[g][ix],y=zeros[g][iy],d=x^y;int dt=0,d7=0;
            for(int a:active[d]) {const int old=current.k[a],v=old+characters[x][a];
                dt+=tail_cost(v)-tail_cost(old);d7+=(std::abs(v)==7)-(std::abs(old)==7);}
            const int change=128*dt+d7;const double frac=static_cast<double>(iter%cycle)/cycle;
            const double temp=t0*std::exp(std::log(t1/t0)*frac);
            const bool take=change<=0||uniform(rng)<std::exp(-static_cast<double>(change)/temp);++iter;
            if(take) {
                ++accepted;
                for(int a:active[d]) {const int old=current.k[a],v=old+characters[x][a];
                    --current.bins[std::abs(old)];++current.bins[std::abs(v)];current.k[a]=v;}
                current.tail+=dt;current.n7+=d7;current.bits[x]=0;current.bits[y]=1;ones[g][ix]=y;zeros[g][iy]=x;
                if(current.k[0]||current.k[z1]||current.k[z2]||current.k[z1^z2]) throw std::runtime_error("lost zero-plane invariant");
                const int p=peak_from_bins(current.bins);
                if(p<peak||(p==peak&&(current.tail<tail||(current.tail==tail&&current.n7<n7)))) {
                    best=current;peak=p;tail=current.tail;n7=current.n7;best_at=iter;
                    std::cout<<"iteration="<<iter<<" best_peak="<<4*peak<<" tail="<<tail<<" n7="<<n7<<std::endl;
                }
                target=p<=7;
                if(target){best=current;peak=p;tail=current.tail;n7=current.n7;best_at=iter;}
            }
            if((iter&8191)==0&&std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()>=seconds){timeout=true;break;}
        }
        save_candidate(candidate,best,seed,best_at);
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();
        std::ofstream out(receipt);if(!out)throw std::runtime_error("cannot create receipt");
        out<<"{\n  \"input\":\""<<argv[1]<<"\",\n  \"zero_plane\":[0,"<<z1<<','<<z2<<','<<(z1^z2)
           <<"],\n  \"rng_seed\":"<<seed<<",\n  \"max_iterations\":"<<maximum<<",\n  \"cycle\":"<<cycle
           <<",\n  \"iterations\":"<<iter<<",\n  \"accepted\":"<<accepted<<",\n  \"t_start\":"<<t0
           <<",\n  \"t_end\":"<<t1<<",\n  \"best_at\":"<<best_at<<",\n  \"best_peak\":"<<4*peak
           <<",\n  \"best_tail\":"<<tail<<",\n  \"best_n7\":"<<n7<<",\n  \"target_met\":"<<(target?"true":"false")
           <<",\n  \"timed_out\":"<<(timeout?"true":"false")<<",\n  \"elapsed_seconds\":"<<elapsed<<"\n}\n";
        if(!out)throw std::runtime_error("receipt write failed");
        std::cout<<"iterations="<<iter<<" accepted="<<accepted<<" best_peak="<<4*peak<<" tail="<<tail<<" target="<<target<<" elapsed="<<elapsed<<"s\n";
        return 0;
    }catch(const std::exception&e){std::cerr<<"error: "<<e.what()<<'\n';return 1;}
}
