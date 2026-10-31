// Bounded breadth-first exploration of the actual balanced peak-32 swap graph.
#define main frontier_balanced_descent_main
#include "frontier-20261028-balanced-descent.cpp"
#undef main
#include <deque>

namespace {
Table bits_from_key(const Key& key) {
    Table f{};
    for (int x=0;x<N;++x) f[x]=(key[x/64]>>(x%64))&1;
    return f;
}
}
int main(int argc,char** argv) {
    try {
        if (argc!=6) throw std::runtime_error("usage: bfs INPUT_JSON MAX_N32 MAX_NODES MAX_SECONDS OUTPUT_PREFIX");
        const int cap=std::stoi(argv[2]),max_nodes=std::stoi(argv[3]),max_seconds=std::stoi(argv[4]);
        if (cap<0||cap>512||max_nodes<1||max_nodes>200000||max_seconds<1||max_seconds>300)
            throw std::runtime_error("invalid bounds");
        const std::string base=argv[5],candidate=base+"-candidate.json",receipt=base+"-result.json";
        require_unused(candidate); require_unused(receipt);
        for (int x=0;x<N;++x) for (int a=0;a<N;++a) chars[x][a]=__builtin_parity(x&a)?-1:1;
        for (int d=1;d<N;++d) { int n=0; for (int a=0;a<N;++a) if (__builtin_parity(a&d)) active[d][n++]=a;
            if (n!=256) throw std::runtime_error("wrong active count"); }
        State source=init(load(argv[1])), best=source;
        if (source.n8>cap) throw std::runtime_error("source exceeds n32 cap");
        std::deque<Key> queue; std::unordered_set<Key,Hash> visited;
        queue.push_back(source.key); visited.insert(source.key);
        long long examined=0,peak32_neighbors=0,within_cap=0; int expanded=0,best_at=0;
        bool hit_cap=false,timed_out=false,target=!best.n8;
        const auto start=std::chrono::steady_clock::now();
        while (!queue.empty()&&!target&&!hit_cap&&!timed_out) {
            const Key key=queue.front(); queue.pop_front(); const State state=init(bits_from_key(key));
            ++expanded;
            for (int i=0;i<256&&!hit_cap&&!target;++i) for (int j=0;j<256;++j) {
                ++examined; const int x=state.ones[i],y=state.zeros[j],d=x^y;
                int delta8=0; bool valid=true;
                for (int a:active[d]) {
                    const int old=state.k[a],v=old+chars[x][a];
                    if (std::abs(v)>8) { valid=false; break; }
                    delta8+=(std::abs(v)==8)-(std::abs(old)==8);
                }
                if (!valid) continue;
                ++peak32_neighbors; const int n8=state.n8+delta8;
                if (n8>cap) continue;
                ++within_cap;
                Key neighbor=key; neighbor[x/64]^=1ULL<<(x%64); neighbor[y/64]^=1ULL<<(y%64);
                if (!visited.insert(neighbor).second) continue;
                if (n8<best.n8) {
                    best=init(bits_from_key(neighbor)); best_at=expanded;
                    if (best.n8!=n8) throw std::runtime_error("incremental n32 mismatch");
                    std::cout<<"expanded="<<expanded<<" discovered="<<visited.size()<<" improved_n32="<<n8<<std::endl;
                }
                if (!n8) { target=true; break; }
                if (static_cast<int>(visited.size())>=max_nodes) { hit_cap=true; break; }
                queue.push_back(neighbor);
            }
            if (expanded%100==0) std::cout<<"expanded="<<expanded<<" discovered="<<visited.size()<<" best_n32="<<best.n8<<std::endl;
            if (std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=max_seconds) timed_out=true;
        }
        save(candidate,best,0,best_at);
        const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
        std::ofstream out(receipt); if (!out) throw std::runtime_error("cannot open receipt");
        out << "{\n  \"input\":\""<<argv[1]<<"\",\n  \"max_n32\":"<<cap<<",\n  \"max_nodes\":"<<max_nodes
            <<",\n  \"expanded\":"<<expanded<<",\n  \"discovered\":"<<visited.size()<<",\n  \"best_at_expansion\":"<<best_at
            <<",\n  \"best_n32\":"<<best.n8<<",\n  \"neighbors_examined\":"<<examined
            <<",\n  \"peak32_neighbors\":"<<peak32_neighbors<<",\n  \"neighbors_within_cap\":"<<within_cap
            <<",\n  \"target_met\":"<<(target?"true":"false")<<",\n  \"hit_node_cap\":"<<(hit_cap?"true":"false")
            <<",\n  \"timed_out\":"<<(timed_out?"true":"false")<<",\n  \"queue_drained\":"<<(queue.empty()&&!target&&!hit_cap&&!timed_out?"true":"false")
            <<",\n  \"elapsed_seconds\":"<<elapsed<<"\n}\n";
        if (!out) throw std::runtime_error("receipt write failed");
        std::cout<<"expanded="<<expanded<<" discovered="<<visited.size()<<" best_n32="<<best.n8<<" target="<<target<<" elapsed="<<elapsed<<"s\n";
        return 0;
    } catch (const std::exception& e) { std::cerr<<"error: "<<e.what()<<'\n'; return 1; }
}
