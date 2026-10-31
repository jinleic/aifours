// Search actual balanced truth tables for four Walsh coefficients divisible by 32.
#define main frontier_z8_base_main
#include "frontier-20261028-balanced-anneal.cpp"
#undef main

int main(int argc,char** argv){
    try{
        if(argc!=8)throw std::runtime_error("usage: z8 INPUT SEED ITERATIONS CYCLE MAX_SECONDS T_START PREFIX");
        const std::uint64_t seed=std::stoull(argv[2]);std::uint64_t rng=seed;
        const long long maximum=std::stoll(argv[3]),cycle=std::stoll(argv[4]);const int seconds=std::stoi(argv[5]);const double t0=std::stod(argv[6]);
        if(maximum<1||cycle<1||seconds<1||seconds>300||t0<=0)throw std::runtime_error("invalid bounds");
        const std::string base=argv[7],candidate=base+"-candidate.json",receipt=base+"-result.json";
        require_unused(candidate);require_unused(receipt);
        State state=initial(load_bits(argv[1])),best=state;
        int score=0;for(int v:state.k)score+=v%8==0;
        int bestscore=score;long long iter=0,accepted=0,best_at=0;bool timeout=false;
        for(int x=0;x<N;++x)for(int a=0;a<N;++a)characters[x][a]=__builtin_parity(x&a)?-1:1;
        for(int d=1;d<N;++d){int n=0;for(int a=0;a<N;++a)if(__builtin_parity(a&d))active[d][n++]=a;if(n!=256)throw std::runtime_error("bad active count");}
        const auto start=std::chrono::steady_clock::now();
        while(iter<maximum&&bestscore>4){
            const int ix=rng_next(rng)&255,iy=rng_next(rng)&255,x=state.ones[ix],y=state.zeros[iy],d=x^y;
            int change=0,dt=0,d7=0;for(int a:active[d]){const int old=state.k[a],v=old+characters[x][a];
                change+=(v%8==0)-(old%8==0);dt+=tail_cost(v)-tail_cost(old);d7+=(std::abs(v)==7)-(std::abs(old)==7);}
            const double frac=static_cast<double>(iter%cycle)/cycle,temp=t0*std::exp(std::log(0.05/t0)*frac);
            const bool take=change<=0||uniform(rng)<std::exp(-static_cast<double>(change)/temp);++iter;
            if(take){
                ++accepted;for(int a:active[d]){const int old=state.k[a],v=old+characters[x][a];
                    --state.bins[std::abs(old)];++state.bins[std::abs(v)];state.k[a]=v;}
                state.bits[x]=0;state.bits[y]=1;state.ones[ix]=y;state.zeros[iy]=x;score+=change;
                state.tail+=dt;state.n7+=d7;
                if(score<bestscore){best=state;bestscore=score;best_at=iter;std::cout<<"iteration="<<iter<<" z8="<<bestscore<<std::endl;}
            }
            if((iter&8191)==0&&std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=seconds){timeout=true;break;}
        }
        save_candidate(candidate,best,seed,best_at);
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream out(receipt);if(!out)throw std::runtime_error("cannot create receipt");
        out<<"{\n  \"input\":\""<<argv[1]<<"\",\n  \"rng_seed\":"<<seed<<",\n  \"iterations\":"<<iter
           <<",\n  \"accepted\":"<<accepted<<",\n  \"best_at\":"<<best_at<<",\n  \"best_z8\":"<<bestscore
           <<",\n  \"equality_case_candidate\":"<<(bestscore==4?"true":"false")
           <<",\n  \"timed_out\":"<<(timeout?"true":"false")<<",\n  \"elapsed_seconds\":"<<elapsed<<"\n}\n";
        if(!out)throw std::runtime_error("receipt write failed");
        std::cout<<"iterations="<<iter<<" accepted="<<accepted<<" best_z8="<<bestscore<<" elapsed="<<elapsed<<"s\n";return 0;
    }catch(const std::exception&e){std::cerr<<"error: "<<e.what()<<'\n';return 1;}
}
