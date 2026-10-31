// Counterexample search in non-affine T8B with a,b,c eighth roots, d=N/D.
// d is NOT required to be a root of unity. Exact Z[zeta8] Gram multiplied
// by nonzero N*D; source ordering, transversal and ray count unrestricted.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using V=std::array<int64_t,4>;using A=std::array<int,8>;
struct E{int sign;std::array<int,4>e;};
int m8(int x){x%=8;return x<0?x+8:x;}V add(V a,V b){for(int i=0;i<4;i++)a[i]+=b[i];return a;}
V sc(V a,int64_t s){for(auto &x:a)x*=s;return a;}
V rt(int x){x=m8(x);V a{};a[x%4]=x<4?1:-1;return a;}
V mul(V a,V b){V z{};for(int i=0;i<4;i++)for(int j=0;j<4;j++)z[(i+j)%4]+=(i+j<4?1:-1)*a[i]*b[j];return z;}
E parse(std::string x){E e{};e.sign=1;if(x[0]=='-'){e.sign=-1;x=x.substr(1);}for(char c:x)if(c>='a'&&c<='d')e.e[c-'a']++;return e;}
bool pm(int mask,int const*g){if(!mask)return true;int c=__builtin_ctz((unsigned)mask),q=g[c]&mask&~(1<<c);while(q){int d=__builtin_ctz((unsigned)q);q&=q-1;if(pm(mask&~(1<<c)&~(1<<d),g))return true;}return false;}
int main(){std::string S[8][8]={{"1","1","1","1","1","1","1","1"},{"1","-1","-d","-c","d","c","cd","-cd"},{"1","-a","-1","c","a","-ac","-c","ac"},{"1","a","d","-1","ad","-a","-d","-ad"},{"1","b","-b","-bc","-1","-c","c","bc"},{"1","-b","bd","b","-d","-1","d","-bd"},{"1","-ab","b","-b","-a","a","-1","ab"},{"1","ab","-bd","bc","-ad","ac","-cd","-abcd"}};
 E K[8][8];for(int i=0;i<8;i++)for(int j=0;j<8;j++)K[i][j]=parse(S[i][j]);
 uint64_t denzero=0,parameters=0,halves=0,matching=0,orders=0,nodes=0;bool found=false;int fa=0,fb=0,fc=0;A fo{},fr{};
 for(int a=0;a<8&&!found;a++)for(int b=0;b<8&&!found;b++)for(int c=0;c<8&&!found;c++){
  V N=add(add(rt(0),rt(a+b)),add(rt(a+c),rt(b+c)));V D=add(add(rt(a),rt(b)),add(rt(c),rt(a+b+c)));if(D==V{}){denzero++;continue;}if(N==V{})return 2;parameters++;
  V fac[3]={mul(D,D),mul(N,D),mul(N,N)};V G[8][8][8];
  for(int t=0;t<8;t++)for(int x=0;x<8;x++)for(int y=0;y<8;y++){
   E A=K[t][x],B=K[t][y];int ed=B.e[3]-A.e[3],ex=0;for(int j=0;j<3;j++)ex+=(B.e[j]-A.e[j])*(j==0?a:j==1?b:c);
   G[t][x][y]=sc(mul(rt(ex),fac[ed+1]),A.sign*B.sign);
  }
  for(int x=0;x<8;x++)for(int y=x+1;y<8;y++){V v{};for(int t=0;t<8;t++)v=add(v,G[t][x][y]);if(v!=V{})return 3;}
  for(int mask=1;mask<256&&!found;mask+=2)if(__builtin_popcount((unsigned)mask)==4){
   halves++;int graph[8]={};for(int x=0;x<8;x++)for(int y=x+1;y<8;y++){V v{};for(int t=0;t<8;t++)if(mask>>t&1)v=add(v,G[t][x][y]);if(v==V{}){graph[x]|=1<<y;graph[y]|=1<<x;}}
   if(!pm(255,graph))continue;matching++;std::vector<int>even,odd;for(int t=1;t<8;t++)((mask>>t&1)?even:odd).push_back(t);
   do{do{
    A O{};O[0]=0;for(int j=0;j<3;j++)O[2*j+2]=even[j];for(int j=0;j<4;j++)O[2*j+1]=odd[j];orders++;
    bool good[8][8][8]={};for(int d=1;d<8;d++)for(int x=0;x<8;x++)for(int y=0;y<8;y++)if(x!=y){V v{};for(int t=0;t<8;t++)v=add(v,mul(rt(d*t),G[O[t]][x][y]));good[d][x][y]=(v==V{});}
    A q;q.fill(-1);q[0]=0;
    auto dfs=[&](auto&&self,int used,int depth)->bool{
     nodes++;if(depth==8){fr=q;return true;}int chosen=-1,best=9,choices=0;
     for(int r=0;r<8;r++)if(q[r]<0){int bits=0;for(int x=0;x<8;x++)if(!(used>>x&1)){
       bool yes=true;for(int s=0;s<8;s++)if(q[s]>=0&&!good[m8(r-s)][q[s]][x]){yes=false;break;}if(yes)bits|=1<<x;}
      int k=__builtin_popcount((unsigned)bits);if(k<best){best=k;chosen=r;choices=bits;}if(!k)return false;}
     while(choices){int x=__builtin_ctz((unsigned)choices);choices&=choices-1;q[chosen]=x;if(self(self,used|(1<<x),depth+1))return true;q[chosen]=-1;}return false;};
    if(dfs(dfs,1,1)){found=true;fa=a;fb=b;fc=c;fo=O;break;}
   }while(std::next_permutation(odd.begin(),odd.end()));if(found)break;std::sort(odd.begin(),odd.end());}while(std::next_permutation(even.begin(),even.end()));
  }
 }
 std::ofstream j("frontier-20261028-t8b-eighth-phase-counterexample-v1.json");
 j<<"{\n \"phase_triples_tested\":"<<parameters<<", \"denominator_zero\":"<<denzero<<", \"halfgraphs\":"<<halves<<", \"matching_halves\":"<<matching<<", \"orders\":"<<orders<<", \"nodes\":"<<nodes<<", \"found\":"<<(found?"true":"false");
 if(found){j<<", \"a_b_c_exponents\":["<<fa<<','<<fb<<','<<fc<<"], \"physical_source_order\":[";for(int i=0;i<8;i++){if(i)j<<',';j<<fo[i];}j<<"], \"column_per_row\":[";for(int i=0;i<8;i++){if(i)j<<',';j<<fr[i];}j<<"]";}j<<"\n}\n";
 std::cout<<"params="<<parameters<<" denzero="<<denzero<<" halves="<<halves<<" matching="<<matching<<" orders="<<orders<<" nodes="<<nodes<<" found="<<found<<'\n';
}
