// Exhaustive paired T-swaps across blocks; preserves every even-half Walsh value.
#define main frontier_cross_base_main
#include "frontier-20261028-balanced-anneal.cpp"
#undef main

int main(int argc,char** argv){try{
    if(argc!=4)throw std::runtime_error("usage: cross INPUT MAX_STEPS PREFIX");
    const int maxsteps=std::stoi(argv[2]);if(maxsteps<1||maxsteps>1000)throw std::runtime_error("invalid bound");
    const std::string base=argv[3],candidate=base+"-candidate.json",receipt=base+"-result.json";
    require_unused(candidate);require_unused(receipt);
    const State source=initial(load_bits(argv[1]));State cur=source,best=cur;
    if(cur.k[0]||cur.k[128]||cur.k[256]||cur.k[384])throw std::runtime_error("missing zero plane");
    int T=0;std::array<int,4> original_xor{};for(int x=0;x<N;++x)if(cur.bits[x]){T^=x;original_xor[x>>7]^=x&127;}
    if(T!=1)throw std::runtime_error("this search fixes T=1");
    for(int x=0;x<N;++x)for(int a=0;a<N;++a)characters[x][a]=__builtin_parity(x&a)?-1:1;
    int evenpeak=0;for(int a=0;a<N;a+=2)evenpeak=std::max(evenpeak,std::abs(cur.k[a]));
    int steps=0;long long tested=0;bool target=peak_from_bins(cur.bins)<=7;
    while(steps<maxsteps&&!target){
        std::array<std::array<int,64>,4> pairs{};std::array<int,4> counts{};
        for(int y=0;y<4;++y)for(int u=0;u<128;u+=2){int x=u|(y<<7),v=(u+1)|(y<<7);
            if(cur.bits[x]!=cur.bits[v])pairs[y][counts[y]++]=cur.bits[x]?x:v;}
        const int currentpeak=peak_from_bins(cur.bins);int bestpeak=currentpeak,besttail=cur.tail,bestn7=cur.n7,bestx=-1,besty=-1;
        for(int a=0;a<4;++a)for(int b=a+1;b<4;++b)for(int i=0;i<counts[a];++i)for(int j=0;j<counts[b];++j){
            const int x=pairs[a][i],y=pairs[b][j];++tested;int dt=0,d7=0,p=evenpeak;
            for(int freq=1;freq<N;freq+=2){const int old=cur.k[freq],v=old+characters[x][freq]+characters[y][freq];
                dt+=tail_cost(v)-tail_cost(old);d7+=(std::abs(v)==7)-(std::abs(old)==7);p=std::max(p,std::abs(v));}
            const int tail=cur.tail+dt,n7=cur.n7+d7;
            if(p<bestpeak||(p==bestpeak&&(tail<besttail||(tail==besttail&&n7<bestn7)))){
                bestpeak=p;besttail=tail;bestn7=n7;bestx=x;besty=y;}
        }
        if(bestx<0)break;
        const int a=bestx,b=besty;
        for(int freq=1;freq<N;freq+=2){const int old=cur.k[freq],v=old+characters[a][freq]+characters[b][freq];
            --cur.bins[std::abs(old)];++cur.bins[std::abs(v)];cur.k[freq]=v;}
        for(int x:(std::array<int,4>{a,a^1,b,b^1}))cur.bits[x]^=1;
        cur.tail=besttail;cur.n7=bestn7;++steps;best=cur;target=bestpeak<=7;
        std::cout<<"step="<<steps<<" peak="<<4*bestpeak<<" tail="<<besttail<<std::endl;
    }
    save_candidate(candidate,best,0,steps);const State check=initial(best.bits);
    for(int a=0;a<N;a+=2)if(check.k[a]!=source.k[a])throw std::runtime_error("even half changed");
    int finalT=0;std::array<int,4> finalxor{};for(int x=0;x<N;++x)if(best.bits[x]){finalT^=x;finalxor[x>>7]^=x&127;}
    if(finalT!=T||best.k[128]||best.k[256]||best.k[384])throw std::runtime_error("target invariants failed");
    std::ofstream out(receipt);if(!out)throw std::runtime_error("cannot create receipt");
    out<<"{\n  \"input\":\""<<argv[1]<<"\",\n  \"steps\":"<<steps<<",\n  \"moves_examined\":"<<tested
       <<",\n  \"best_peak\":"<<4*peak_from_bins(best.bins)<<",\n  \"best_tail\":"<<best.tail<<",\n  \"best_n7\":"<<best.n7
       <<",\n  \"original_block_xors\":["<<original_xor[0]<<','<<original_xor[1]<<','<<original_xor[2]<<','<<original_xor[3]
       <<"],\n  \"final_block_xors\":["<<finalxor[0]<<','<<finalxor[1]<<','<<finalxor[2]<<','<<finalxor[3]
       <<"],\n  \"even_half_unchanged\":true,\n  \"target_met\":"<<(target?"true":"false")<<"\n}\n";
    if(!out)throw std::runtime_error("receipt write failed");
    std::cout<<"steps="<<steps<<" tested="<<tested<<" peak="<<4*peak_from_bins(best.bins)<<" target="<<target<<'\n';return 0;
}catch(const std::exception&e){std::cerr<<"error: "<<e.what()<<'\n';return 1;}}
