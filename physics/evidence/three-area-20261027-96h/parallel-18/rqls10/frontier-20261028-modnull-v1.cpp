// Modular row reduction plus a full nullspace basis. The output is over the
// selected prime only; characteristic-zero witnesses require separate checks.
#include <algorithm>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <vector>

#ifndef PRIME
#define PRIME 65521
#endif
constexpr std::int64_t P = PRIME;
std::int64_t power(std::int64_t x, std::int64_t k) {
    std::int64_t result=1;
    while(k) { if(k&1) result=result*x%P; x=x*x%P; k>>=1; }
    return result;
}
int main(int argc,char** argv) {
    if(argc!=3) throw std::runtime_error("usage: modnull matrix.txt output.txt");
    std::ifstream in(argv[1]);
    int rows,cols;
    if(!(in>>rows>>cols) || rows<0 || cols<0) throw std::runtime_error("invalid header");
    std::vector<std::int32_t> a(static_cast<std::size_t>(rows)*cols,0);
    for(int r=0;r<rows;++r) {
        int count;
        if(!(in>>count) || count<0 || count>cols) throw std::runtime_error("invalid row");
        for(int k=0;k<count;++k) {
            int c,val;
            if(!(in>>c>>val) || c<0 || c>=cols) throw std::runtime_error("invalid entry");
            const auto i=static_cast<std::size_t>(r)*cols+c;
            a[i]=static_cast<std::int32_t>((a[i]+val%P+P)%P);
        }
    }
    int rank=0;
    std::vector<int> pivots;
    for(int c=0;c<cols && rank<rows;++c) {
        int pivot=rank;
        while(pivot<rows && a[static_cast<std::size_t>(pivot)*cols+c]==0) ++pivot;
        if(pivot==rows) continue;
        if(pivot!=rank) for(int j=c;j<cols;++j)
            std::swap(a[static_cast<std::size_t>(pivot)*cols+j],a[static_cast<std::size_t>(rank)*cols+j]);
        auto* top=a.data()+static_cast<std::size_t>(rank)*cols;
        const auto inv=power(top[c],P-2);
        for(int j=c;j<cols;++j) top[j]=static_cast<std::int32_t>(top[j]*inv%P);
        for(int r=rank+1;r<rows;++r) {
            auto* row=a.data()+static_cast<std::size_t>(r)*cols;
            const std::int64_t f=row[c];
            if(!f) continue;
            for(int j=c;j<cols;++j) {
                auto x=row[j]-f*top[j]%P;
                if(x<0) x+=P;
                row[j]=static_cast<std::int32_t>(x);
            }
        }
        pivots.push_back(c);
        ++rank;
    }
    std::vector<bool> is_pivot(cols,false);
    for(int c:pivots) is_pivot[c]=true;
    std::ofstream out(argv[2]);
    if(!out) throw std::runtime_error("cannot open output");
    out<<"prime "<<P<<" columns "<<cols<<" rank "<<rank<<" nullity "<<cols-rank<<'\n';
    for(int free=0;free<cols;++free) {
        if(is_pivot[free]) continue;
        std::vector<std::int64_t> x(cols,0);
        x[free]=1;
        for(int k=rank-1;k>=0;--k) {
            const int c=pivots[k];
            const auto* row=a.data()+static_cast<std::size_t>(k)*cols;
            std::int64_t sum=0;
            for(int j=c+1;j<cols;++j) sum=(sum+row[j]*x[j])%P;
            x[c]=(P-sum)%P;
        }
        int nnz=0;
        for(auto value:x) if(value) ++nnz;
        out<<"free "<<free<<" nonzeros "<<nnz;
        for(int j=0;j<cols;++j) if(x[j]) out<<' '<<j<<':'<<x[j];
        out<<'\n';
    }
    std::cout<<"file "<<argv[1]<<" prime "<<P<<" rank "<<rank
             <<" nullity "<<cols-rank<<" basis "<<argv[2]<<'\n';
}
