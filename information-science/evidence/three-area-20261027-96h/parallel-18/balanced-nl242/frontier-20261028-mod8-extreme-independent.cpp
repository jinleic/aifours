// Independent low-pivot RREF and fiber census for the 40 residue-108 cases.
#define main frontier_extreme_census_base_main
#include "frontier-20261028-rank6-mod8-census-independent.cpp"
#undef main

int main(int argc,char** argv){try{
    if(argc!=2)throw std::runtime_error("usage: extreme OUTPUT_JSON");if(std::ifstream(argv[1]).good())throw std::runtime_error("refusing overwrite");
    std::vector<int> terms{0};for(int i=0;i<8;++i)terms.push_back(1<<i);
    for(int i=0;i<8;++i)for(int j=i+1;j<8;++j)terms.push_back((1<<i)|(1<<j));
    for(int i=0;i<8;++i)for(int j=i+1;j<8;++j)for(int l=j+1;l<8;++l)terms.push_back((1<<i)|(1<<j)|(1<<l));
    if(terms.size()!=V)throw std::runtime_error("term count");
    std::vector<Equation> rows;std::vector<int> odd;std::array<int,256> index{};index.fill(-1);
    for(int x=0;x<256;++x){const int g=g0(x,1);if(g&1){index[x]=odd.size();odd.push_back(x);continue;}
        Equation row;for(int i=0;i<V;++i)if((x&terms[i])==terms[i])row.set(i);
        row[V]=((g/2)&1)^((x&63)!=0);rows.push_back(row);}
    int r=0;std::vector<int> piv;
    for(int col=0;col<V;++col){int found=r;while(found<static_cast<int>(rows.size())&&!rows[found][col])++found;
        if(found==static_cast<int>(rows.size()))continue;std::swap(rows[r],rows[found]);
        for(int j=0;j<static_cast<int>(rows.size());++j)if(j!=r&&rows[j][col])rows[j]^=rows[r];piv.push_back(col);++r;}
    if(r!=76)throw std::runtime_error("unexpected rank");
    for(const auto& row:rows){bool empty=true;for(int i=0;i<V;++i)if(row[i]){empty=false;break;}
        if(empty&&row[V])throw std::runtime_error("inconsistent model");}
    std::array<bool,V> is_pivot{};for(int p:piv)is_pivot[p]=true;std::vector<int> free;
    for(int i=0;i<V;++i)if(!is_pivot[i])free.push_back(i);if(free.size()!=17)throw std::runtime_error("unexpected nullity");
    Coeff first;for(int j=0;j<r;++j)if(rows[j][V])first.set(piv[j]);std::vector<Coeff> basis;
    for(int f:free){Coeff v;v.set(f);for(int j=0;j<r;++j)if(rows[j][f])v.set(piv[j]);basis.push_back(v);}
    auto eval=[&](const Coeff& c){Values output;for(int i=0;i<static_cast<int>(odd.size());++i){int value=0;
        for(int j=0;j<V;++j)if(c[j]&&((odd[i]&terms[j])==terms[j]))value^=1;if(value)output.set(i);}return output;};
    Values current=eval(first);for(int i=0;i<static_cast<int>(odd.size());++i)if(g0(odd[i],1)%4==3)current.flip(i);
    std::vector<Values> delta;for(const auto& v:basis)delta.push_back(eval(v));
    std::uint64_t previous=0;int extreme=0;std::array<int,5> pattern{};bool mutation=false;
    for(std::uint64_t i=0;i<(1ULL<<17);++i){const auto gray=i^(i>>1);
        if(i)current^=delta[__builtin_ctzll(gray^previous)];previous=gray;if(current.count()!=108)continue;
        ++extreme;std::array<int,5> freq{};
        for(int b=0;b<64;++b)if(g0(b,1)&1){int n=0;for(int r0=0;r0<4;++r0){const int j=index[b|(r0<<6)];if(j<0)throw std::runtime_error("missing odd point");n+=current[j];}
            ++freq[n];}
        if(freq[0]!=9||freq[4]!=27||freq[1]||freq[2]||freq[3])throw std::runtime_error("fiber uniformity failure");
        pattern=freq;if(!mutation){Values altered=current;for(int b=0;b<64&&!mutation;++b)if(g0(b,1)&1){const int j=index[b];if(altered[j]){
            altered.flip(j);int n=0;for(int r0=0;r0<4;++r0)n+=altered[index[b|(r0<<6)]];mutation=(n!=0&&n!=4);}}}
    }
    if(extreme!=40||!mutation)throw std::runtime_error("wrong count or mutation control");
    std::ofstream out(argv[1]);if(!out)throw std::runtime_error("cannot create output");
    out<<"{\n  \"solutions_enumerated\":131072,\n  \"extreme_solutions\":"<<extreme
       <<",\n  \"radical_fibers\":36,\n  \"fiber_count_distribution\":{\"0\":"<<pattern[0]<<",\"4\":"<<pattern[4]
       <<"},\n  \"all_40_fiber_uniform\":true,\n  \"targeted_fiber_mutation_rejected\":true\n}\n";
    if(!out)throw std::runtime_error("write failure");std::cout<<"extreme="<<extreme<<" fibers0="<<pattern[0]<<" fibers4="<<pattern[4]<<'\n';return 0;
}catch(const std::exception&e){std::cerr<<"error: "<<e.what()<<'\n';return 1;}}
