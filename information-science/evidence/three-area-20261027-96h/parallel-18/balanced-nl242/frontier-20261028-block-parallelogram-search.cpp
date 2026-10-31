// Actual truth-table annealing by four-flip block parallelograms.
#define main frontier_block_search_base_main
#include "frontier-20261028-balanced-anneal.cpp"
#undef main

namespace {std::array<std::array<int,256>,512> inactive{};}
int main(int argc,char** argv){try{
    if(argc!=9)throw std::runtime_error("usage: block INPUT SEED ITERATIONS CYCLE MAX_SECONDS T_START T_END PREFIX");
    const std::uint64_t seed=std::stoull(argv[2]);std::uint64_t rng=seed;
    const long long maxit=std::stoll(argv[3]),cycle=std::stoll(argv[4]);const int seconds=std::stoi(argv[5]);
    const double t0=std::stod(argv[6]),t1=std::stod(argv[7]);
    if(maxit<1||cycle<1||seconds<1||seconds>300||t0<=0||t1<=0)throw std::runtime_error("invalid bounds");
    const std::string base=argv[8],candidate=base+"-candidate.json",receipt=base+"-result.json";
    require_unused(candidate);require_unused(receipt);
    State current=initial(load_bits(argv[1])),best=current;
    if(current.k[128]||current.k[256]||current.k[384])throw std::runtime_error("input lacks block zero plane");
    std::array<std::array<int,64>,4> ones{},zeros{};std::array<std::array<int,128>,4> zeroindex{};
    std::array<int,4> no{},nz{},blockxor{};
    for(int y=0;y<4;++y)for(int u=0;u<128;++u){const int x=u|(y<<7);
        if(current.bits[x]){if(no[y]>=64)throw std::runtime_error("block imbalance");ones[y][no[y]++]=u;blockxor[y]^=u;}
        else{if(nz[y]>=64)throw std::runtime_error("block imbalance");zeroindex[y][u]=nz[y];zeros[y][nz[y]++]=u;}}
    for(int y=0;y<4;++y)if(no[y]!=64||nz[y]!=64)throw std::runtime_error("block imbalance");
    for(int x=0;x<N;++x)for(int a=0;a<N;++a)characters[x][a]=__builtin_parity(x&a)?-1:1;
    for(int d=1;d<N;++d){int n=0;for(int a=0;a<N;++a)if(!__builtin_parity(a&d))inactive[d][n++]=a;
        if(n!=256)throw std::runtime_error("bad character class");}
    int peak=peak_from_bins(best.bins),tail=best.tail,n7=best.n7;long long iter=0,valid=0,accepted=0,bestat=0;
    bool timeout=false,target=peak<=7;const auto started=std::chrono::steady_clock::now();
    while(iter<maxit&&!target){
        const int y=rng_next(rng)&3,i=rng_next(rng)&63,j=rng_next(rng)&63,widx=rng_next(rng)&63;++iter;
        if(i!=j){const int u=ones[y][i],v=ones[y][j],w=zeros[y][widx],z=w^u^v;
            if(z!=w&&!current.bits[z|(y<<7)]){
                ++valid;const int zidx=zeroindex[y][z],x=u|(y<<7),d=u^v,e=u^w;int dt=0,d7=0;
                for(int a:inactive[d])if(__builtin_parity(a&e)){
                    const int old=current.k[a],next=old+2*characters[x][a];dt+=tail_cost(next)-tail_cost(old);
                    d7+=(std::abs(next)==7)-(std::abs(old)==7);}
                const int change=128*dt+d7;const double frac=static_cast<double>(iter%cycle)/cycle;
                const double temp=t0*std::exp(std::log(t1/t0)*frac);
                if(change<=0||uniform(rng)<std::exp(-static_cast<double>(change)/temp)){
                    ++accepted;for(int a:inactive[d])if(__builtin_parity(a&e)){
                        const int old=current.k[a],next=old+2*characters[x][a];
                        --current.bins[std::abs(old)];++current.bins[std::abs(next)];current.k[a]=next;}
                    current.tail+=dt;current.n7+=d7;
                    current.bits[u|(y<<7)]=0;current.bits[v|(y<<7)]=0;current.bits[w|(y<<7)]=1;current.bits[z|(y<<7)]=1;
                    ones[y][i]=w;ones[y][j]=z;zeros[y][widx]=u;zeros[y][zidx]=v;zeroindex[y][u]=widx;zeroindex[y][v]=zidx;
                    if(current.k[0]||current.k[128]||current.k[256]||current.k[384])throw std::runtime_error("lost plane");
                    const int p=peak_from_bins(current.bins);
                    if(p<peak||(p==peak&&(current.tail<tail||(current.tail==tail&&current.n7<n7)))){
                        best=current;peak=p;tail=current.tail;n7=current.n7;bestat=iter;
                        std::cout<<"iteration="<<iter<<" best_peak="<<4*peak<<" tail="<<tail<<std::endl;}
                    target=p<=7;if(target){best=current;peak=p;tail=current.tail;n7=current.n7;bestat=iter;}
                }
            }
        }
        if((iter&8191)==0&&std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()>=seconds){timeout=true;break;}
    }
    save_candidate(candidate,best,seed,bestat);const State checked=initial(best.bits);
    std::array<int,4> checkxor{};for(int x=0;x<N;++x)if(checked.bits[x])checkxor[x>>7]^=x&127;
    if(checkxor!=blockxor)throw std::runtime_error("block XOR invariant failed");
    const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();
    std::ofstream out(receipt);if(!out)throw std::runtime_error("cannot create receipt");
    out<<"{\n  \"input\":\""<<argv[1]<<"\",\n  \"rng_seed\":"<<seed<<",\n  \"iterations\":"<<iter
       <<",\n  \"valid_moves\":"<<valid<<",\n  \"accepted\":"<<accepted<<",\n  \"best_at\":"<<bestat
       <<",\n  \"best_peak\":"<<4*peak<<",\n  \"best_tail\":"<<tail<<",\n  \"best_n7\":"<<n7
       <<",\n  \"block_xors\":["<<blockxor[0]<<','<<blockxor[1]<<','<<blockxor[2]<<','<<blockxor[3]
       <<"],\n  \"target_met\":"<<(target?"true":"false")<<",\n  \"timed_out\":"<<(timeout?"true":"false")
       <<",\n  \"elapsed_seconds\":"<<elapsed<<"\n}\n";
    if(!out)throw std::runtime_error("receipt write failed");
    std::cout<<"iterations="<<iter<<" valid="<<valid<<" accepted="<<accepted<<" best_peak="<<4*peak<<" target="<<target<<" elapsed="<<elapsed<<"s\n";return 0;
}catch(const std::exception&e){std::cerr<<"error: "<<e.what()<<'\n';return 1;}}
