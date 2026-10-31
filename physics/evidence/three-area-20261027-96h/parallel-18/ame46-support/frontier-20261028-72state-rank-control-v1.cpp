// Independent Gaussian-rank checks for the 72-state F5 diagnostic.
#define main search_main
#include "frontier-20261028-72state-rank-search-f5-v1.cpp"
#undef main
#include <algorithm>
#include <set>
int gauss(std::array<int,36>m){int r=0;for(int c=0;c<6&&r<6;++c){int i=r;while(i<6&&!m[6*i+c])++i;if(i==6)continue;
 for(int j=0;j<6;++j)std::swap(m[6*i+j],m[6*r+j]);int inv=1;while(m[6*r+c]*inv%5!=1)++inv;
 for(i=r+1;i<6;++i){int f=m[6*i+c]*inv%5;for(int j=c;j<6;++j)m[6*i+j]=mod(m[6*i+j]-f*m[6*r+j]);}++r;}return r;}
bool pred(const std::array<int,36>&m){std::array<Cell,36>cs{};V u{};u[0]=1;for(int i=0;i<36;++i)if(m[i]){cs[i].n=1;cs[i].b[0]=0;cs[i].c[0]=m[i];}return smallrank(cs,u);}
int main(int argc,char**argv){try{if(argc!=2)throw std::runtime_error("usage output");auto p=points();std::set<V>distinct(p.begin(),p.end());if(distinct.size()!=3906)throw std::runtime_error("duplicate projective point");
 std::uint32_t seed=7282026;auto rnd=[&](){seed=1664525u*seed+1013904223u;return int((seed>>8)%5);};
 std::array<int,36>z{};if(!pred(z)||gauss(z)!=0)throw std::runtime_error("zero rejected");
 for(int n=0;n<10000;++n){std::array<int,36>m{};for(auto&x:m)x=rnd();if(pred(m)!=(gauss(m)<=1))throw std::runtime_error("random disagreement");}
 for(int n=0;n<10000;++n){V a{},b{};for(auto&x:a)x=rnd();for(auto&x:b)x=rnd();if(std::all_of(a.begin(),a.end(),[](int x){return !x;}))a[0]=1;if(std::all_of(b.begin(),b.end(),[](int x){return !x;}))b[0]=1;
  std::array<int,36>m{};for(int i=0;i<6;++i)for(int j=0;j<6;++j)m[6*i+j]=a[i]*b[j]%5;if(gauss(m)!=1||!pred(m))throw std::runtime_error("rank-one rejected");int k=(rnd()*5+rnd())%36;m[k]=(m[k]+1)%5;if(pred(m)!=(gauss(m)<=1))throw std::runtime_error("mutation disagreement");}
 std::ostringstream o;o<<"{\n  \"field\":5,\n  \"unique_projective_points\":"<<distinct.size()<<",\n  \"rank_one_positive_controls\":10000,\n  \"zero_positive_controls\":1,\n  \"gaussian_comparisons\":20000,\n  \"scope\":\"Finite-field rank predicate controls, not a complex proof.\"\n}\n";
 int fd=open(argv[1],O_WRONLY|O_CREAT|O_EXCL,0644);if(fd<0)throw std::runtime_error("cannot create output");auto s=o.str();if(write(fd,s.data(),s.size())!=static_cast<ssize_t>(s.size()))throw std::runtime_error("write failed");close(fd);std::cout<<s;return 0;
 }catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}}
