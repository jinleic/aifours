// Independent F7 Gaussian-rank controls for the exhaustive search's rank predicate.
#define main exhaustive_search_main
#include "frontier-20261028-mixed-product-rank-search-v1.cpp"
#undef main
#include <set>
#include <algorithm>

static int gaussian_rank(std::array<int,36> a) {
    int r=0;
    for(int col=0;col<6 && r<6;++col) {
        int i=r;while(i<6 && !a[6*i+col])++i;if(i==6)continue;
        for(int j=0;j<6;++j)std::swap(a[6*i+j],a[6*r+j]);
        int inv=1;while((inv*a[6*r+col])%7!=1)++inv;
        for(i=r+1;i<6;++i) {
            int f=a[6*i+col]*inv%7;
            for(int j=col;j<6;++j)a[6*i+j]=mod(a[6*i+j]-f*a[6*r+j]);
        }
        ++r;
    }
    return r;
}
static bool tested_predicate(const std::array<int,36>& matrix) {
    std::array<Cell,36> cells{};Vec u{};u[0]=1;
    for(int i=0;i<36;++i)if(matrix[i]) {cells[i].n=1;cells[i].b[0]=0;cells[i].coeff[0]=matrix[i];}
    return rank_at_most_one(cells,u);
}
int main(int argc,char**argv) {
 try {
    if(argc!=2)throw std::runtime_error("usage: output.json");
    auto points=projective_vectors();std::set<Vec> unique(points.begin(),points.end());
    if(unique.size()!=19608)throw std::runtime_error("projective duplicates");
    int mixed=0;for(auto&v:points)if(hmixed(v))++mixed;
    if(mixed!=19200)throw std::runtime_error("wrong mixed vector count");
    std::uint32_t seed=20261028;auto rnd=[&](){seed=1664525u*seed+1013904223u;return int((seed>>8)%7);};
    int random_checks=0,rankone_checks=0,zero_checks=0;
    std::array<int,36> zero{};if(!tested_predicate(zero)||gaussian_rank(zero)!=0)throw std::runtime_error("zero positive control");++zero_checks;
    for(int n=0;n<10000;++n) {
        std::array<int,36> m{};for(auto&x:m)x=rnd();
        if(tested_predicate(m)!=(gaussian_rank(m)<=1))throw std::runtime_error("random predicate mismatch");++random_checks;
    }
    for(int n=0;n<10000;++n) {
        Vec a{},b{};for(auto&x:a)x=rnd();for(auto&x:b)x=rnd();
        if(std::all_of(a.begin(),a.end(),[](int x){return !x;}))a[0]=1;
        if(std::all_of(b.begin(),b.end(),[](int x){return !x;}))b[0]=1;
        std::array<int,36> m{};for(int i=0;i<6;++i)for(int j=0;j<6;++j)m[6*i+j]=a[i]*b[j]%7;
        if(gaussian_rank(m)!=1||!tested_predicate(m))throw std::runtime_error("rank-one positive control rejected");++rankone_checks;
        // A changed entry may or may not preserve rank one; compare independently.
        int at=rnd()*5+rnd();at%=36;m[at]=(m[at]+1)%7;
        if(tested_predicate(m)!=(gaussian_rank(m)<=1))throw std::runtime_error("mutated predicate mismatch");++random_checks;
    }
    std::ostringstream out;out<<"{\n  \"field\": 7,\n  \"unique_projective_vectors\": "<<unique.size()
      <<",\n  \"mixed_vectors\": "<<mixed<<",\n  \"rank_one_positive_controls\": "<<rankone_checks
      <<",\n  \"zero_positive_controls\": "<<zero_checks<<",\n  \"gaussian_comparisons\": "<<random_checks
      <<",\n  \"scope\": \"Exhaustive-search rank predicate and projective enumeration control; no global complex claim.\"\n}\n";
    int fd=open(argv[1],O_WRONLY|O_CREAT|O_EXCL,0644);if(fd<0)throw std::runtime_error("cannot create output");
    auto s=out.str();if(write(fd,s.data(),s.size())!=static_cast<ssize_t>(s.size()))throw std::runtime_error("output failure");close(fd);std::cout<<s;return 0;
 }catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}
}
