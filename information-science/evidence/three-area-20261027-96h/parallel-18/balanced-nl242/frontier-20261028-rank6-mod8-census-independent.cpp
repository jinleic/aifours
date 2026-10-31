// Independent low-pivot RREF and Gray enumeration of the rank-six mod8 model.
#include <array>
#include <bitset>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <stdexcept>
#include <string>
#include <vector>

namespace {
constexpr int V=93;
using Equation=std::bitset<V+1>;
using Coeff=std::bitset<V>;
using Values=std::bitset<256>;
struct Result {int arf=0,zeros=0,odds=0,rank=0,nullity=0;std::array<long long,257> hist{};};
int g0(int x,int arf){int g=0;for(int i=0;i<3;++i)g+=((x>>(2*i))&1)*((x>>(2*i+1))&1);return g+arf*((x&1)+((x>>1)&1));}
Result count(int arf){
    std::vector<int> terms{0};for(int i=0;i<8;++i)terms.push_back(1<<i);
    for(int i=0;i<8;++i)for(int j=i+1;j<8;++j)terms.push_back((1<<i)|(1<<j));
    for(int i=0;i<8;++i)for(int j=i+1;j<8;++j)for(int k=j+1;k<8;++k)terms.push_back((1<<i)|(1<<j)|(1<<k));
    if(terms.size()!=V)throw std::runtime_error("term count");
    std::vector<Equation> rows;std::vector<int> odd;
    for(int x=0;x<256;++x){const int g=g0(x,arf);if(g&1){odd.push_back(x);continue;}
        Equation row;for(int i=0;i<V;++i)if((x&terms[i])==terms[i])row.set(i);
        row[V]=((g/2)&1)^((x&63)!=0);rows.push_back(row);}
    int r=0;std::vector<int> piv;
    for(int col=0;col<V;++col){int found=r;while(found<static_cast<int>(rows.size())&&!rows[found][col])++found;
        if(found==static_cast<int>(rows.size()))continue;std::swap(rows[r],rows[found]);
        for(int j=0;j<static_cast<int>(rows.size());++j)if(j!=r&&rows[j][col])rows[j]^=rows[r];
        piv.push_back(col);++r;}
    for(const auto& row:rows){bool empty=true;for(int i=0;i<V;++i)if(row[i]){empty=false;break;}
        if(empty&&row[V])throw std::runtime_error("inconsistent model");}
    if(r==static_cast<int>(rows.size()))throw std::runtime_error("missing redundant-equation control");
    Equation mutation=rows[r];mutation.flip(V);bool empty=true;for(int i=0;i<V;++i)if(mutation[i])empty=false;
    if(!empty||!mutation[V])throw std::runtime_error("mutation control failed");
    std::array<bool,V> is_pivot{};for(int p:piv)is_pivot[p]=true;std::vector<int> free;
    for(int i=0;i<V;++i)if(!is_pivot[i])free.push_back(i);
    Coeff first;for(int j=0;j<r;++j)if(rows[j][V])first.set(piv[j]);
    std::vector<Coeff> basis;
    for(int f:free){Coeff v;v.set(f);for(int j=0;j<r;++j)if(rows[j][f])v.set(piv[j]);basis.push_back(v);}
    auto eval=[&](const Coeff& c){Values output;for(int i=0;i<static_cast<int>(odd.size());++i){int value=0;
        for(int j=0;j<V;++j)if(c[j]&&((odd[i]&terms[j])==terms[j]))value^=1;if(value)output.set(i);}return output;};
    Values current=eval(first);for(int i=0;i<static_cast<int>(odd.size());++i)if(g0(odd[i],arf)%4==3)current.flip(i);
    std::vector<Values> delta;for(const auto& v:basis)delta.push_back(eval(v));
    if(delta.size()>25)throw std::runtime_error("unexpected census size");
    Result out;out.arf=arf;out.zeros=rows.size();out.odds=odd.size();out.rank=r;out.nullity=free.size();
    std::uint64_t previous=0;for(std::uint64_t i=0;i<(1ULL<<delta.size());++i){const auto gray=i^(i>>1);
        if(i)current^=delta[__builtin_ctzll(gray^previous)];previous=gray;++out.hist[current.count()];}
    return out;
}
}
int main(int argc,char** argv){try{
    if(argc!=2)throw std::runtime_error("usage: census OUTPUT_JSON");if(std::ifstream(argv[1]).good())throw std::runtime_error("refusing overwrite");
    const auto a=count(0),b=count(1);std::ofstream out(argv[1]);if(!out)throw std::runtime_error("cannot create output");
    out<<"{\n  \"interpretation\":\"independent finite mod8 relaxation, not a witness\",\n  \"models\":[\n";
    for(int i=0;i<2;++i){const auto& m=i?b:a;out<<"    {\"arf\":"<<m.arf<<",\"variables\":"<<V<<",\"q_zero_points\":"<<m.zeros
        <<",\"q_one_points\":"<<m.odds<<",\"rank\":"<<m.rank<<",\"nullity\":"<<m.nullity<<",\"solution_count\":"<<(1LL<<m.nullity)
        <<",\"residue3_count_histogram\":{";bool first=true;for(int j=0;j<=256;++j)if(m.hist[j]){
            if(!first)out<<',';first=false;out<<'\"'<<j<<"\":"<<m.hist[j];}out<<"},\"rref_mutation_rejected\":true}"<<(i?"\n":",\n");}
    out<<"  ]\n}\n";if(!out)throw std::runtime_error("write failure");
    std::cout<<"rank/nullity="<<a.rank<<'/'<<a.nullity<<','<<b.rank<<'/'<<b.nullity<<" solutions="<<(1LL<<a.nullity)<<','<<(1LL<<b.nullity)<<'\n';return 0;
}catch(const std::exception&e){std::cerr<<"error: "<<e.what()<<'\n';return 1;}}
