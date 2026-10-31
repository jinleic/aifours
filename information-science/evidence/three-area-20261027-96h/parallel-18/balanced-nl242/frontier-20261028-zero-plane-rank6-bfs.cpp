// Search actual balanced peak-32 neighbors for rank-six radical equal to a zero plane.
#define main frontier_rank6_bfs_base_main
#include "frontier-20261028-balanced-descent.cpp"
#undef main
#include <deque>

namespace {
Table bits_key(const Key& key){Table f{};for(int x=0;x<N;++x)f[x]=(key[x/64]>>(x%64))&1;return f;}
int binary_rank(std::array<int,8> rows){std::array<int,8> piv{};int rank=0;for(int v:rows)while(v){int b=31-__builtin_clz(v);if(piv[b])v^=piv[b];else{piv[b]=v;++rank;break;}}return rank;}
bool desired(const State& s,int z1,int z2){
    int T=0;for(int x=0;x<N;++x)if(s.bits[x])T^=x;if(!T||__builtin_parity(T&z1)||__builtin_parity(T&z2))return false;
    std::array<int,9> piv{};std::array<int,8> basis{};int n=0;
    for(int a=1;a<N&&n<8;++a){if(__builtin_parity(a&T))continue;int v=a;
        while(v){int p=31-__builtin_clz(v);if(piv[p])v^=piv[p];else{piv[p]=v;basis[n++]=a;break;}}}
    if(n!=8)throw std::runtime_error("kernel basis");
    auto q=[&](int a){if(s.k[a]%2)throw std::runtime_error("even half parity");return ((s.k[a]/2)%2+2)%2;};
    auto B=[&](int a,int b){return q(a^b)^q(a)^q(b);};
    for(int b:basis)if(B(z1,b)||B(z2,b))return false;
    std::array<int,8> gram{};for(int i=0;i<8;++i)for(int j=0;j<8;++j)gram[i]|=B(basis[i],basis[j])<<j;
    return binary_rank(gram)==6;
}
}
int main(int argc,char** argv){try{
    if(argc!=8)throw std::runtime_error("usage: bfs INPUT Z1 Z2 MAX_N32 MAX_NODES MAX_SECONDS PREFIX");
    const int z1=std::stoi(argv[2]),z2=std::stoi(argv[3]),cap=std::stoi(argv[4]),maxnodes=std::stoi(argv[5]),seconds=std::stoi(argv[6]);
    if(z1<=0||z1>=N||z2<=0||z2>=N||z1==z2||cap<0||cap>512||maxnodes<1||maxnodes>200000||seconds<1||seconds>300)throw std::runtime_error("bad bounds");
    const std::string base=argv[7],candidate=base+"-candidate.json",receipt=base+"-result.json";require_unused(candidate);require_unused(receipt);
    for(int x=0;x<N;++x)for(int a=0;a<N;++a)chars[x][a]=__builtin_parity(x&a)?-1:1;
    for(int d=1;d<N;++d){int n=0;for(int a=0;a<N;++a)if(__builtin_parity(a&d))active[d][n++]=a;if(n!=256)throw std::runtime_error("bad active");}
    State source=init(load(argv[1])),best=source;if(source.n8>cap||source.k[z1]||source.k[z2]||source.k[z1^z2])throw std::runtime_error("source mismatch");
    std::deque<Key>queue;std::unordered_set<Key,Hash>visited;queue.push_back(source.key);visited.insert(source.key);
    bool hitcap=false,timeout=false,target=!source.n8,found=desired(source,z1,z2);int expanded=0;long long checked=1,tested=0;
    const auto start=std::chrono::steady_clock::now();
    while(!queue.empty()&&!hitcap&&!timeout&&!target&&!found){
        const Key key=queue.front();queue.pop_front();const State state=init(bits_key(key));++expanded;
        for(int i=0;i<256&&!hitcap&&!timeout&&!target&&!found;++i)for(int j=0;j<256&&!timeout;++j){
            const int x=state.ones[i],y=state.zeros[j],d=x^y;if(__builtin_parity(d&z1)||__builtin_parity(d&z2))continue;
            ++tested;
            if((tested&255)==0&&std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=seconds){timeout=true;break;}
            int delta8=0;bool valid=true;
            for(int a:active[d]){const int old=state.k[a],v=old+chars[x][a];if(std::abs(v)>8){valid=false;break;}
                delta8+=(std::abs(v)==8)-(std::abs(old)==8);}
            if(!valid||state.n8+delta8>cap)continue;
            Key next=key;next[x/64]^=1ULL<<(x%64);next[y/64]^=1ULL<<(y%64);
            if(!visited.insert(next).second)continue;
            const State candidate_state=init(bits_key(next));++checked;
            if(candidate_state.n8<best.n8)best=candidate_state;
            if(!candidate_state.n8){best=candidate_state;target=true;break;}
            if(desired(candidate_state,z1,z2)){best=candidate_state;found=true;break;}
            if(static_cast<int>(visited.size())>=maxnodes){hitcap=true;break;}queue.push_back(next);
        }
        if(expanded%100==0)std::cout<<"expanded="<<expanded<<" checked="<<checked<<" best_n32="<<best.n8<<std::endl;
        if(std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=seconds)timeout=true;
    }
    save(candidate,best,0,expanded);
    const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::ofstream out(receipt);if(!out)throw std::runtime_error("cannot create receipt");
    out<<"{\n  \"input\":\""<<argv[1]<<"\",\n  \"zero_plane\":[0,"<<z1<<','<<z2<<','<<(z1^z2)
       <<"],\n  \"max_n32\":"<<cap<<",\n  \"expanded\":"<<expanded<<",\n  \"checked\":"<<checked
       <<",\n  \"swaps_tested\":"<<tested<<",\n  \"best_n32\":"<<best.n8<<",\n  \"rank6_radical_found\":"<<(found?"true":"false")
       <<",\n  \"target_met\":"<<(target?"true":"false")<<",\n  \"hit_node_cap\":"<<(hitcap?"true":"false")
       <<",\n  \"timed_out\":"<<(timeout?"true":"false")<<",\n  \"queue_drained\":"<<(queue.empty()&&!target&&!found&&!hitcap&&!timeout?"true":"false")
       <<",\n  \"elapsed_seconds\":"<<elapsed<<"\n}\n";
    if(!out)throw std::runtime_error("write failure");std::cout<<"checked="<<checked<<" found="<<found<<" peak="<<(best.n8?32:28)<<" elapsed="<<elapsed<<'\n';return 0;
}catch(const std::exception&e){std::cerr<<"error: "<<e.what()<<'\n';return 1;}}
