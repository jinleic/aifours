// Exact search in a restricted Fourier-separable QLS(10) family.
// V_{r,c}(t) = zeta_10^(r*t+c*mu(t))/sqrt(10), mu a permutation.
// The search checks one transversal pi exactly; its column translations give
// the full resolution. This is not an exhaustive search over all QLS.
#include <array>
#include <chrono>
#include <fstream>
#include <iostream>
#include <numeric>
#include <algorithm>
#include <cstdint>
#include <cstdlib>

constexpr int N=10;
constexpr int COEF[10][4]={{1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1},
 {-1,1,-1,1},{-1,0,0,0},{0,-1,0,0},{0,0,-1,0},{0,0,0,-1},{1,-1,1,-1}};
std::array<int,N> mu,pi;
std::array<unsigned,N> allowed;
std::uint64_t nodes=0,node_limit=200000;
bool truncated=false;

bool search(unsigned remaining_rows,unsigned used_cols) {
    if (!remaining_rows) return true;
    if (++nodes>node_limit) { truncated=true; return false; }
    int best=-1; unsigned best_mask=0; int best_count=11;
    for(int r=1;r<N;++r) if(remaining_rows&(1u<<r)) {
        unsigned mask=0;
        for(int c=1;c<N;++c) if(!(used_cols&(1u<<c))) {
            bool ok=true;
            for(int s=0;s<N && ok;++s) if(pi[s]>=0) {
                int da=(r-s+N)%N, db=(c-pi[s]+N)%N;
                ok=(allowed[da]&(1u<<db))!=0;
            }
            if(ok) mask|=1u<<c;
        }
        int count=__builtin_popcount(mask);
        if(!count) return false;
        if(count<best_count) {best=r;best_mask=mask;best_count=count;}
    }
    while(best_mask) {
        unsigned bit=best_mask&-best_mask; best_mask-=bit;
        int c=__builtin_ctz(bit); pi[best]=c;
        if(search(remaining_rows&~(1u<<best),used_cols|bit)) return true;
        pi[best]=-1;
        if(truncated) return false;
    }
    return false;
}

int main(int argc,char**argv) {
    double seconds=argc>1?std::atof(argv[1]):45.0;
    std::uint64_t max_perms=argc>2?std::strtoull(argv[2],nullptr,10):362880;
    node_limit=argc>3?std::strtoull(argv[3],nullptr,10):200000;
    if(seconds<=0 || max_perms==0 || node_limit==0) return 2;
    std::iota(mu.begin(),mu.end(),0);
    auto start=std::chrono::steady_clock::now();
    std::uint64_t processed=0,repeat=0,empty_row=0,searched=0,exhausted=0,unknown=0,total_nodes=0;
    bool found=false,finished=false;
    do {
        ++processed;
        allowed.fill(0);
        bool repeated=false,empty=false;
        for(int a=1;a<N && !repeated && !empty;++a) {
            for(int b=1;b<N;++b) {
                int coeff[4]={0,0,0,0}; bool constant=true;
                for(int t=0;t<N;++t) {
                    int k=(a*t+b*mu[t])%N;
                    if(k) constant=false;
                    for(int h=0;h<4;++h) coeff[h]+=COEF[k][h];
                }
                if(constant) {repeated=true;break;}
                if(!(coeff[0]||coeff[1]||coeff[2]||coeff[3])) allowed[a]|=1u<<b;
            }
            if(!allowed[a] && !repeated) empty=true;
        }
        if(repeated) ++repeat;
        else if(empty) ++empty_row;
        else {
            ++searched; pi.fill(-1); pi[0]=0; nodes=0;truncated=false;
            if(search(((1u<<N)-1)&~1u,1u)) {found=true;total_nodes+=nodes;break;}
            total_nodes+=nodes;
            if(truncated) ++unknown; else ++exhausted;
        }
        if(processed%1024==0) {
            auto elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
            if(elapsed>=seconds || processed>=max_perms) break;
        }
        if(processed>=max_perms) break;
    } while(std::next_permutation(mu.begin()+1,mu.end()));
    // Enumeration is complete only when all 9! permutations were processed.
    finished=(processed==362880 && !found);
    const double elapsed=std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count();
    std::ofstream out("frontier-20261028-fourier-graph-result-v1.json");
    out<<"{\n  \"family\": \"zeta10 Fourier graph, mu and pi permutations\",\n"
       <<"  \"processed_mu\": "<<processed<<",\n  \"total_mu\": 362880,\n"
       <<"  \"repeated_ray_early\": "<<repeat<<",\n  \"empty_difference_row\": "<<empty_row<<",\n"
       <<"  \"transversal_searches\": "<<searched<<",\n  \"exhausted_transversal_searches\": "<<exhausted<<",\n"
       <<"  \"truncated_transversal_searches\": "<<unknown<<",\n  \"backtrack_nodes\": "<<total_nodes<<",\n"
       <<"  \"node_limit_per_mu\": "<<node_limit<<",\n  \"elapsed_seconds\": "<<elapsed<<",\n"
       <<"  \"found\": "<<(found?"true":"false")<<",\n  \"enumeration_finished\": "<<(finished?"true":"false")<<",\n";
    out<<"  \"mu\": ";
    if(found) {out<<'[';for(int i=0;i<N;++i){if(i)out<<',';out<<mu[i];}out<<']';}else out<<"null";
    out<<",\n  \"pi\": ";
    if(found) {out<<'[';for(int i=0;i<N;++i){if(i)out<<',';out<<pi[i];}out<<']';}else out<<"null";
    out<<",\n  \"scope\": \"restricted Fourier-separable family only; unknown if truncated\"\n}\n";
    std::cout<<"processed_mu "<<processed<<"/362880 repeat "<<repeat<<" empty_row "<<empty_row
             <<" searched "<<searched<<" exhausted "<<exhausted<<" truncated "<<unknown
             <<" backtrack_nodes "<<total_nodes<<" elapsed "<<elapsed<<'\n';
    if(found) {std::cout<<"FOUND candidate mu ";for(auto x:mu)std::cout<<x<<' ';std::cout<<" pi ";for(auto x:pi)std::cout<<x<<' ';std::cout<<'\n';}
    else std::cout<<"NO_CANDIDATE_OBSERVED; exhaustive "<<(finished&&unknown==0)<<'\n';
}
