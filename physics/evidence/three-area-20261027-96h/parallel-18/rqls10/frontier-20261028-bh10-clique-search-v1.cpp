// Bounded exact search of normalized BH(10,5) half-frames and extensions.
// Row compatibility is exact residue-balanced. No unverified solver result is
// a global theorem; partial search/timeout is reported explicitly.
#include <algorithm>
#include <array>
#include <bitset>
#include <chrono>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <vector>

constexpr int N=10, LIMIT=1100;
using Row=std::array<int,N>;
using Bits=std::bitset<LIMIT>;
Row second={0,0,1,1,2,2,3,3,4,4},current{};
std::array<int,5> counts={1,2,2,2,2};
std::vector<Row> rows;
std::vector<Bits> adj;
std::uint64_t triangles=0,common5=0,halfmatch=0,extend_search=0,nodes=0;
std::chrono::steady_clock::time_point start;
double deadline=45;
bool timedout=false,found=false;
std::array<int,3> found_half{};
std::vector<int> found_tail;

bool balanced(const Row& a,const Row& b) {
    int count[5]={0,0,0,0,0};
    for(int k=0;k<N;++k) ++count[(a[k]-b[k]+5)%5];
    return count[0]==2&&count[1]==2&&count[2]==2&&count[3]==2&&count[4]==2;
}
void generate(int pos) {
    if(pos==N){if(balanced(current,second))rows.push_back(current);return;}
    for(int x=0;x<5;++x)if(counts[x]){--counts[x];current[pos]=x;generate(pos+1);++counts[x];}
}
bool match_rec(const std::array<unsigned,N>& A,unsigned mask) {
    if(!mask)return true;
    unsigned bit=mask&-mask;int i=__builtin_ctz(bit);unsigned rem=mask^bit;
    unsigned opts=A[i]&rem;
    while(opts){unsigned b=opts&-opts;opts-=b;if(match_rec(A,rem^b))return true;}
    return false;
}
bool half_matching(int i,int j,int k) {
    const Row zero={0,0,0,0,0,0,0,0,0,0};
    const Row* E[5]={&zero,&second,&rows[i],&rows[j],&rows[k]};
    std::array<unsigned,N> A{};
    for(int x=0;x<N;++x)for(int y=x+1;y<N;++y){
        unsigned mask=0;for(int t=0;t<5;++t)mask|=1u<<(((*E[t])[x]-(*E[t])[y]+5)%5);
        if(mask==31){A[x]|=1u<<y;A[y]|=1u<<x;}
    }
    return match_rec(A,(1u<<N)-1);
}
bool extend(Bits candidates,int need,std::vector<int>& chosen) {
    if(!need)return true;
    if(static_cast<int>(candidates.count())<need)return false;
    if(++nodes%4096==0 && std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=deadline){timedout=true;return false;}
    for(std::size_t x=0;x<rows.size();++x) if(candidates.test(x)) {
        candidates.reset(x);chosen.push_back(static_cast<int>(x));
        if(extend(candidates&adj[x],need-1,chosen))return true;
        chosen.pop_back();if(timedout)return false;
    }
    return false;
}
int main(int argc,char**argv){
    if(argc>1)deadline=std::atof(argv[1]);if(deadline<=0)return 2;
    start=std::chrono::steady_clock::now();current[0]=0;generate(1);
    if(rows.size()!=1075 || rows.size()>LIMIT)return 3;
    adj.resize(rows.size());
    std::uint64_t edgecount=0;
    for(std::size_t i=0;i<rows.size();++i)for(std::size_t j=i+1;j<rows.size();++j)
        if(balanced(rows[i],rows[j])){adj[i].set(j);adj[j].set(i);++edgecount;}
    std::cout<<"candidate_rows "<<rows.size()<<" compatibility_edges "<<edgecount<<std::endl;
    for(std::size_t i=0;i<rows.size() && !found && !timedout;++i){
        for(std::size_t j=i+1;j<rows.size() && !found && !timedout;++j)if(adj[i].test(j)){
            Bits ij=adj[i]&adj[j];
            for(std::size_t k=j+1;k<rows.size() && !found && !timedout;++k)if(ij.test(k)){
                ++triangles;
                if(triangles%4096==0 && std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>=deadline){timedout=true;break;}
                Bits candidates=ij&adj[k];
                if(candidates.count()<5)continue;
                ++common5;
                if(!half_matching(i,j,k))continue;
                ++halfmatch;++extend_search;
                std::vector<int> tail;
                if(extend(candidates,5,tail)){found=true;found_half={int(i),int(j),int(k)};found_tail=tail;}
            }
        }
    }
    double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::ofstream out("frontier-20261028-bh10-clique-search-result-v1.json");
    out<<"{\n  \"candidate_rows\": "<<rows.size()<<",\n  \"compatibility_edges\": "<<edgecount
       <<",\n  \"triangles_examined\": "<<triangles<<",\n  \"triangles_with_5_common\": "<<common5
       <<",\n  \"half_matching_candidates\": "<<halfmatch<<",\n  \"extension_searches\": "<<extend_search
       <<",\n  \"extension_nodes\": "<<nodes<<",\n  \"found\": "<<(found?"true":"false")
       <<",\n  \"timed_out\": "<<(timedout?"true":"false")<<",\n  \"elapsed_seconds\": "<<elapsed<<",\n  \"rows\": ";
    if(found){
        out<<'[';bool first=true;
        auto emit=[&](const Row& r){if(!first)out<<',';first=false;out<<'[';for(int j=0;j<N;++j){if(j)out<<',';out<<r[j];}out<<']';};
        Row zero{};emit(zero);emit(second);for(auto j:found_half)emit(rows[j]);for(auto j:found_tail)emit(rows[j]);out<<']';
    }else out<<"null";
    out<<",\n  \"scope\": \"normalized BH(10,5) with 5-row perfect matching, bounded exact search\"\n}\n";
    std::cout<<"triangles "<<triangles<<" common5 "<<common5<<" halfmatch "<<halfmatch
             <<" extension_nodes "<<nodes<<" found "<<found<<" timed_out "<<timedout<<" elapsed "<<elapsed<<std::endl;
    if(found){std::cout<<"FULL_BH_WITH_HALF_MATCHING_REQUIRES_INDEPENDENT_CHECK"<<std::endl;}
}
