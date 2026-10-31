// Bounded graph search of balanced swaps preserving a Walsh-zero plane.
#define main frontier_zero_plane_bfs_base_main
#include "frontier-20261028-balanced-descent.cpp"
#undef main
#include <deque>

namespace {
Table bits_from_key_plane(const Key& key) { Table f{};for(int x=0;x<N;++x)f[x]=(key[x/64]>>(x%64))&1;return f; }
}
int main(int argc,char** argv) {
    try {
        if(argc!=8)throw std::runtime_error("usage: bfs INPUT Z1 Z2 MAX_N32 MAX_NODES MAX_SECONDS PREFIX");
        const int z1=std::stoi(argv[2]),z2=std::stoi(argv[3]),cap=std::stoi(argv[4]),maxnodes=std::stoi(argv[5]),seconds=std::stoi(argv[6]);
        if(z1<=0||z1>=N||z2<=0||z2>=N||z1==z2||cap<0||cap>512||maxnodes<1||maxnodes>200000||seconds<1||seconds>300)
            throw std::runtime_error("invalid arguments");
        const std::string base=argv[7],candidate=base+"-candidate.json",receipt=base+"-result.json";
        require_unused(candidate);require_unused(receipt);
        for(int x=0;x<N;++x)for(int a=0;a<N;++a)chars[x][a]=__builtin_parity(x&a)?-1:1;
        for(int d=1;d<N;++d){int n=0;for(int a=0;a<N;++a)if(__builtin_parity(a&d))active[d][n++]=a;
            if(n!=256)throw std::runtime_error("bad active count");}
        State source=init(load(argv[1])),best=source;
        if(source.n8>cap||source.k[z1]||source.k[z2]||source.k[z1^z2])throw std::runtime_error("source cap or zero-plane failure");
        std::deque<Key>queue;std::unordered_set<Key,Hash>visited;queue.push_back(source.key);visited.insert(source.key);
        long long tested=0,within=0;int expanded=0,best_at=0;bool hitcap=false,timeout=false,target=!best.n8;
        const auto started=std::chrono::steady_clock::now();
        while(!queue.empty()&&!hitcap&&!timeout&&!target){
            const Key key=queue.front();queue.pop_front();const State state=init(bits_from_key_plane(key));++expanded;
            if(state.k[z1]||state.k[z2]||state.k[z1^z2])throw std::runtime_error("lost zero plane");
            for(int i=0;i<256&&!hitcap&&!target;++i)for(int j=0;j<256;++j){
                const int x=state.ones[i],y=state.zeros[j],d=x^y;
                if(__builtin_parity(d&z1)||__builtin_parity(d&z2))continue;
                ++tested;int delta8=0;bool valid=true;
                for(int a:active[d]){const int old=state.k[a],v=old+chars[x][a];
                    if(std::abs(v)>8){valid=false;break;}delta8+=(std::abs(v)==8)-(std::abs(old)==8);}
                if(!valid||state.n8+delta8>cap)continue;
                ++within;Key neighbor=key;neighbor[x/64]^=1ULL<<(x%64);neighbor[y/64]^=1ULL<<(y%64);
                if(!visited.insert(neighbor).second)continue;
                const int n8=state.n8+delta8;
                if(n8<best.n8){best=init(bits_from_key_plane(neighbor));if(best.n8!=n8)throw std::runtime_error("bad delta");best_at=expanded;
                    std::cout<<"expanded="<<expanded<<" discovered="<<visited.size()<<" best_n32="<<n8<<std::endl;}
                if(!n8){target=true;break;}
                if(static_cast<int>(visited.size())>=maxnodes){hitcap=true;break;}
                queue.push_back(neighbor);
            }
            if(expanded%250==0)std::cout<<"expanded="<<expanded<<" discovered="<<visited.size()<<" best_n32="<<best.n8<<std::endl;
            if(std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count()>=seconds)timeout=true;
        }
        save(candidate,best,0,best_at);
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-started).count();
        std::ofstream out(receipt);if(!out)throw std::runtime_error("cannot create receipt");
        out<<"{\n  \"input\":\""<<argv[1]<<"\",\n  \"zero_plane\":[0,"<<z1<<','<<z2<<','<<(z1^z2)
           <<"],\n  \"max_n32\":"<<cap<<",\n  \"max_nodes\":"<<maxnodes<<",\n  \"expanded\":"<<expanded
           <<",\n  \"discovered\":"<<visited.size()<<",\n  \"best_n32\":"<<best.n8<<",\n  \"swaps_tested\":"<<tested
           <<",\n  \"neighbors_within_cap\":"<<within<<",\n  \"target_met\":"<<(target?"true":"false")
           <<",\n  \"hit_node_cap\":"<<(hitcap?"true":"false")<<",\n  \"timed_out\":"<<(timeout?"true":"false")
           <<",\n  \"queue_drained\":"<<(queue.empty()&&!target&&!hitcap&&!timeout?"true":"false")
           <<",\n  \"elapsed_seconds\":"<<elapsed<<"\n}\n";
        if(!out)throw std::runtime_error("receipt write failed");
        std::cout<<"expanded="<<expanded<<" discovered="<<visited.size()<<" best_n32="<<best.n8<<" target="<<target<<" elapsed="<<elapsed<<"s\n";
        return 0;
    }catch(const std::exception&e){std::cerr<<"error: "<<e.what()<<'\n';return 1;}
}
