// Exact exhaustive transversal census for all 3-bit permutation character QLS.
// This is a restricted class, NOT a general four-MOQLS search.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fcntl.h>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <unistd.h>
#include <vector>
using F = std::array<unsigned char,8>;

int parity(int x) { return __builtin_popcount(static_cast<unsigned>(x)) & 1; }
int gf8mul(int a,int b) {
    int z=0;
    for(int k=0;k<3;++k) { if(b&1) z^=a; b>>=1; a<<=1; if(a&8) a^=11; }
    return z;
}
int rank3(std::array<int,3> basis) {
    int rank=0;
    for(int bit=2;bit>=0;--bit) {
        int pivot=rank;
        while(pivot<3 && !(basis[pivot] & (1<<bit))) ++pivot;
        if(pivot==3) continue;
        std::swap(basis[rank],basis[pivot]);
        for(int k=0;k<3;++k) if(k!=rank && (basis[k]&(1<<bit))) basis[k]^=basis[rank];
        ++rank;
    }
    return rank;
}
int polar_rank(const F &f) {
    return rank3({int(f[3]^f[1]^f[2]),int(f[5]^f[1]^f[4]),int(f[6]^f[2]^f[4])});
}
void walsh(const F &f, int W[8][8]) {
    for(int u=0;u<8;++u) for(int v=0;v<8;++v) {
        int z=0; for(int x=0;x<8;++x) z+=parity((u&f[x])^(v&x))?-1:1; W[u][v]=z;
    }
}
bool transversal(const F &p,const int W[8][8]) {
    for(int i=0;i<8;++i) for(int j=i+1;j<8;++j)
        if(W[i^j][p[i]^p[j]]!=0) return false;
    return true;
}
void exclusive_write(const std::string &name,const std::string &text) {
    int fd=open(name.c_str(),O_WRONLY|O_CREAT|O_EXCL,0644);
    if(fd<0) throw std::runtime_error("output exists or cannot be opened");
    size_t done=0; while(done<text.size()) { auto n=write(fd,text.data()+done,text.size()-done); if(n<=0) {close(fd);throw std::runtime_error("write failed");} done+=size_t(n); }
    if(close(fd)!=0) throw std::runtime_error("close failed");
}
std::string array_json(const F& f) { std::ostringstream o; o<<'['; for(int i=0;i<8;++i) {if(i)o<<',';o<<int(f[i]);} o<<']';return o.str(); }
int main(int argc,char** argv) {
 try {
    if(argc!=3 || std::string(argv[1])!="--output") throw std::runtime_error("usage: --output NEW_RECEIPT");
    auto start=std::chrono::steady_clock::now();
    auto timed_out=[&](){return std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>45.0;};
    std::vector<F> perms; F p{{0,1,2,3,4,5,6,7}};
    do {perms.push_back(p);} while(std::next_permutation(p.begin()+1,p.end()));
    if(perms.size()!=5040) throw std::runtime_error("permutation count");
    F id{{0,1,2,3,4,5,6,7}}, positive{};
    for(int x=0;x<8;++x) positive[x]=gf8mul(2,x);
    int baseline[8][8]; walsh(id,baseline);
    if(!transversal(positive,baseline) || transversal(id,baseline)) throw std::runtime_error("positive/negative transversal controls");
    std::array<uint64_t,4> f_counts{}, tested{}, passing{}, nonlin_row_checks{};
    std::array<F,4> examples{}; std::array<bool,4> have_example{};
    std::array<uint64_t,4> max_transversals{};
    bool complete=true; size_t first_unchecked=perms.size();
    for(size_t fi=0;fi<perms.size();++fi) {
        if(timed_out()) {complete=false;first_unchecked=fi;break;}
        const F &f=perms[fi]; int rank=polar_rank(f), W[8][8]; walsh(f,W);
        if(rank<0||rank>3||W[0][0]!=8) throw std::runtime_error("rank/normalization");
        for(int u=1;u<8;++u) if(W[u][0]!=0 || W[0][u]!=0) throw std::runtime_error("row/column QLS Gram failure");
        int nlin=0;
        for(int u=0;u<8;++u) {
            int num=0, abs8=0, abs4=0;
            for(int v=0;v<8;++v) { if(W[u][v]) ++num; if(std::abs(W[u][v])==8) ++abs8; if(std::abs(W[u][v])==4) ++abs4; }
            if(num==4 && abs4==4) ++nlin;
            else if(!(num==1 && abs8==1)) throw std::runtime_error("invalid Walsh spectrum");
        }
        if(nlin!=8-(1<<(3-rank))) throw std::runtime_error("polar-rank row-spectrum mismatch");
        nonlin_row_checks[rank]+=1;
        ++f_counts[rank]; uint64_t trans=0;
        for(const auto &pi:perms) {++tested[rank]; if(transversal(pi,W)) {++trans; ++passing[rank]; if(!have_example[rank]) {examples[rank]=f;have_example[rank]=true;}}}
        max_transversals[rank]=std::max(max_transversals[rank],trans);
    }
    std::ostringstream o;
    o<<"{\n  \"kind\": \"EXACT_CHARACTER_TRANSVERSAL_CENSUS\",\n"
     <<"  \"definition\": \"psi(i,j;x)=(-1)^(i dot f(x)+j dot x)/sqrt8; normalized f(0)=pi(0)=0\",\n"
     <<"  \"functions_by_polar_rank_0_1_2_3\": ["<<f_counts[0]<<','<<f_counts[1]<<','<<f_counts[2]<<','<<f_counts[3]<<"],\n"
     <<"  \"tested_transversals_by_rank\": ["<<tested[0]<<','<<tested[1]<<','<<tested[2]<<','<<tested[3]<<"],\n"
     <<"  \"passing_transversals_by_rank\": ["<<passing[0]<<','<<passing[1]<<','<<passing[2]<<','<<passing[3]<<"],\n"
     <<"  \"max_transversals_for_one_function_by_rank\": ["<<max_transversals[0]<<','<<max_transversals[1]<<','<<max_transversals[2]<<','<<max_transversals[3]<<"],\n"
     <<"  \"walsh_spectrum_and_rowcol_checks_by_rank\": ["<<nonlin_row_checks[0]<<','<<nonlin_row_checks[1]<<','<<nonlin_row_checks[2]<<','<<nonlin_row_checks[3]<<"],\n"
     <<"  \"positive_classical_transversal\": "<<array_json(positive)<<",\n"
     <<"  \"positive_control_passed\": true,\n  \"negative_identity_control_rejected\": true,\n"
     <<"  \"complete\": "<<(complete?"true":"false")<<",\n"
     <<"  \"first_unchecked_function_index\": "<<first_unchecked<<",\n"
     <<"  \"seconds\": "<<std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()<<",\n"
     <<"  \"scope\": \"Exact all normalized permutations f and normalized candidate classical transversals pi, NOT all quantum mates.\"\n}\n";
    exclusive_write(argv[2],o.str());std::cout<<o.str();return complete?0:2;
 } catch(const std::exception&e) {std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
}
