// Exact projective F5 rank-one search for the delta=0, alpha=0, beta=pi/2 state.
// The embedding i->2 has i^2=-1. Finite-field results alone imply nothing over C.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdexcept>
#include <string>
#include <vector>
#include <fcntl.h>
#include <unistd.h>
using V=std::array<int,6>;
struct Cell { int n=0;std::array<int,6>b{},c{}; };
int mod(int x){x%=5;return x<0?x+5:x;}
int value(const Cell& x,const V& u){int n=0;for(int k=0;k<x.n;++k)n+=x.c[k]*u[x.b[k]];return n%5;}
bool smallrank(const std::array<Cell,36>& C,const V&u){
  int a=value(C[0],u),b=value(C[1],u),c=value(C[6],u),d=value(C[7],u);if(mod(a*d-b*c))return false;
  std::array<int,36> M{};M[0]=a;M[1]=b;M[6]=c;M[7]=d;
  for(int k=0;k<36;++k)if(k!=0&&k!=1&&k!=6&&k!=7)M[k]=value(C[k],u);
  int p=0;while(p<36&&!M[p])++p;if(p==36)return true;int i=p/6,j=p%6;
  for(int r=0;r<6;++r)if(r!=i)for(int s=0;s<6;++s)if(s!=j&&mod(M[p]*M[6*r+s]-M[6*r+j]*M[6*i+s]))return false;
  return true;
}
std::vector<V> points(){std::vector<V> out;for(int f=0;f<6;++f){int n=1;for(int i=f+1;i<6;++i)n*=5;
 for(int j=0;j<n;++j){V x{};x[f]=1;int z=j;for(int i=f+1;i<6;++i){x[i]=z%5;z/=5;}out.push_back(x);}}
 if(out.size()!=3906)throw std::runtime_error("projective count");return out;}
std::string show(const V&x){std::ostringstream z;z<<'[';for(int i=0;i<6;++i){if(i)z<<',';z<<x[i];}z<<']';return z.str();}
int main(int argc,char**argv){try{
 if(argc!=6)throw std::runtime_error("usage: table C B mixed|all output");
 int C=std::stoi(argv[2]),B=std::stoi(argv[3]);std::string mode=argv[4];if(C<0||C>3||B<0||B>3||C==B||(mode!="mixed"&&mode!="all"))throw std::runtime_error("bad arguments");
 int rem[2],nrem=0;for(int i=0;i<4;++i)if(i!=C&&i!=B)rem[nrem++]=i;int A=rem[0],D=rem[1];
 int T[6][6][6][6]{};int nt=0;std::ifstream in(argv[1]);std::string line;if(!in)throw std::runtime_error("no source");
 auto insert=[&](std::array<int,4>q,int coeff){int &p=T[q[C]][q[B]][q[A]][q[D]];if(p)throw std::runtime_error("duplicate term");p=coeff;++nt;};
 while(std::getline(in,line)){if(line.empty()||line[0]=='#')continue;std::istringstream z(line);int a,b;z>>a>>b;std::string tok;
  while(z>>tok){if(tok.size()!=3)throw std::runtime_error("bad token");int v=tok[0]=='-'?4:(tok[0]=='+'||tok[0]=='s')?1:0;
   if(!v)throw std::runtime_error("bad coefficient");insert({a,b,tok[1]-'0',tok[2]-'0'},v);}}
 const std::array<const char*,12> odd={"0353","3530","4044","5405","0434","3055","4503","5340","0545","3304","4450","5033"};
 for(auto s:odd)insert({s[0]-'0',s[1]-'0',s[2]-'0',s[3]-'0'},2);if(nt!=72)throw std::runtime_error("wrong support");
 auto ps=points();std::uint64_t scanned=0,vs=0;bool found=false;V fv{},fu{};
 for(auto&v:ps){bool mixed=(v[1]||v[2])&&(v[0]||v[3]||v[4]||v[5]);if(mode=="mixed"&&!mixed)continue;++vs;
  std::array<Cell,36> cells{};for(int a=0;a<6;++a)for(int d=0;d<6;++d)for(int b=0;b<6;++b){int x=0;for(int c=0;c<6;++c)x+=T[c][b][a][d]*v[c];x=mod(x);
   if(x){auto&e=cells[6*a+d];e.b[e.n]=b;e.c[e.n]=x;++e.n;}}
  for(auto&u:ps){++scanned;if(smallrank(cells,u)){found=true;fv=v;fu=u;break;}}if(found)break;}
 std::ostringstream out;out<<"{\n  \"field\":5,\n  \"i\":2,\n  \"C\":"<<C<<",\n  \"B\":"<<B<<",\n  \"mode\":\""<<mode<<"\",\n  \"projective_vectors\":"<<ps.size()<<",\n  \"C_vectors_examined\":"<<vs<<",\n  \"pairs_examined\":"<<scanned<<",\n  \"rank_at_most_one_found\":"<<(found?"true":"false")<<",\n";
 if(found)out<<"  \"C_vector\":"<<show(fv)<<",\n  \"B_vector\":"<<show(fu)<<",\n";
 out<<"  \"scope\":\"Finite-field diagnostic of this one 72-term state, not a complex proof.\"\n}\n";
 int fd=open(argv[5],O_WRONLY|O_CREAT|O_EXCL,0644);if(fd<0)throw std::runtime_error("cannot create output");auto s=out.str();if(write(fd,s.data(),s.size())!=static_cast<ssize_t>(s.size()))throw std::runtime_error("write failure");close(fd);std::cout<<s;return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}}
