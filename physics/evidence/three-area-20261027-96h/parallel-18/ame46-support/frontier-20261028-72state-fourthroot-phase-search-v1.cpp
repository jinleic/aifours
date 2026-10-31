// Bounded F73 search of three-color/eigen-X mixed inputs for the 72-term state.
// r=2^(-1/4), i, and 8th roots exist in F73. Results do not imply C solutions.
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
struct Cell{int n=0;std::array<int,6>b{},c{};};
int mod(int x){x%=73;return x<0?x+73:x;}
int val(const Cell&c,const V&u){int x=0;for(int i=0;i<c.n;++i)x+=c.c[i]*u[c.b[i]];return x%73;}
bool smallrank(const std::array<Cell,36>&c,const V&u){int a=val(c[0],u),b=val(c[1],u),d=val(c[6],u),e=val(c[7],u);if(mod(a*e-b*d))return false;
 std::array<int,36>m{};m[0]=a;m[1]=b;m[6]=d;m[7]=e;for(int i=0;i<36;++i)if(i!=0&&i!=1&&i!=6&&i!=7)m[i]=val(c[i],u);
 int p=0;while(p<36&&!m[p])++p;if(p==36)return true;int r=p/6,s=p%6;
 for(int i=0;i<6;++i)if(i!=r)for(int j=0;j<6;++j)if(j!=s&&mod(m[p]*m[6*i+j]-m[6*i+s]*m[6*r+j]))return false;return true;}
struct Item{V x{};int missing,sign,hphase,p2,p3;};
std::vector<Item> points(int party){
 const int level[4][4]={{4,5,3,0},{3,5,4,0},{3,5,4,0},{5,4,3,0}};
 const int ph[8]={1,10,27,51,72,63,46,22};std::vector<Item>out;
 for(int missing=0;missing<4;++missing)for(int sign:{1,-1})for(int h=0;h<8;++h)for(int p=0;p<8;++p)for(int q=0;q<8;++q){
  Item a{};a.missing=missing;a.sign=sign;a.hphase=h;a.p2=p;a.p3=q;a.x[1]=69*ph[h]%73;a.x[2]=mod(sign*a.x[1]);
  int z=0;for(int g=0;g<4;++g)if(g!=missing){int phase=z==0?1:z==1?ph[p]:ph[q];a.x[level[party][g]]=phase;++z;}out.push_back(a);}
 if(out.size()!=4096)throw std::runtime_error("bad point count");return out;
}
std::string show(const Item&a){std::ostringstream o;o<<"{\"missing\":"<<a.missing<<",\"sign\":"<<a.sign<<",\"hphase_exp\":"<<a.hphase<<",\"K_phase_exponents\":[0,"<<a.p2<<','<<a.p3<<"],\"vector\":[";
 for(int i=0;i<6;++i){if(i)o<<',';o<<a.x[i];}o<<"]}";return o.str();}
int main(int argc,char**argv){try{
 if(argc!=5)throw std::runtime_error("usage: table C B output");int C=std::stoi(argv[2]),B=std::stoi(argv[3]);if(C<0||C>3||B<0||B>3||C==B)throw std::runtime_error("bad parties");int rem[2],nr=0;for(int i=0;i<4;++i)if(i!=C&&i!=B)rem[nr++]=i;int A=rem[0],D=rem[1];
 int T[6][6][6][6]{};int n=0;auto add=[&](std::array<int,4>q,int x){int &v=T[q[C]][q[B]][q[A]][q[D]];if(v)throw std::runtime_error("duplicate");v=x;++n;};
 std::ifstream in(argv[1]);std::string line;if(!in)throw std::runtime_error("no source");while(std::getline(in,line)){if(line.empty()||line[0]=='#')continue;std::istringstream s(line);int a,b;s>>a>>b;std::string z;while(s>>z){if(z.size()!=3)throw std::runtime_error("bad token");int x=z[0]=='-'?72:(z[0]=='+'||z[0]=='s')?1:0;if(!x)throw std::runtime_error("bad coeff");add({a,b,z[1]-'0',z[2]-'0'},x);}}
 const std::array<const char*,12> odd={"0353","3530","4044","5405","0434","3055","4503","5340","0545","3304","4450","5033"};for(auto s:odd)add({s[0]-'0',s[1]-'0',s[2]-'0',s[3]-'0'},27);if(n!=72)throw std::runtime_error("bad support");
 auto vv=points(C),uu=points(B);std::uint64_t scanned=0;bool found=false;Item fv{},fu{};
 for(auto&v:vv){std::array<Cell,36>cs{};for(int a=0;a<6;++a)for(int d=0;d<6;++d)for(int b=0;b<6;++b){int x=0;for(int c=0;c<6;++c)x+=T[c][b][a][d]*v.x[c];x=mod(x);if(x){auto&e=cs[6*a+d];e.b[e.n]=b;e.c[e.n]=x;++e.n;}}
  for(auto&u:uu){++scanned;if(smallrank(cs,u.x)){found=true;fv=v;fu=u;break;}}if(found)break;}
 std::ostringstream out;out<<"{\n  \"field\":73,\n  \"i\":27,\n  \"r_2_inverse_fourth_root\":69,\n  \"primitive_eighth_root\":10,\n  \"C\":"<<C<<",\n  \"B\":"<<B<<",\n  \"vectors_each\":4096,\n  \"pairs_examined\":"<<scanned<<",\n  \"rank_at_most_one_found\":"<<(found?"true":"false")<<",\n";
 if(found)out<<"  \"C_candidate\":"<<show(fv)<<",\n  \"B_candidate\":"<<show(fu)<<",\n";
 out<<"  \"scope\":\"Three K colors, equal-magnitude eighth-root phases, X-eigen H spinor and specified H/K ratio, in F73 only.\"\n}\n";
 int fd=open(argv[4],O_WRONLY|O_CREAT|O_EXCL,0644);if(fd<0)throw std::runtime_error("cannot create output");auto s=out.str();if(write(fd,s.data(),s.size())!=static_cast<ssize_t>(s.size()))throw std::runtime_error("write failed");close(fd);std::cout<<s;return 0;
}catch(const std::exception&e){std::cerr<<"ERROR: "<<e.what()<<'\n';return 1;}}
