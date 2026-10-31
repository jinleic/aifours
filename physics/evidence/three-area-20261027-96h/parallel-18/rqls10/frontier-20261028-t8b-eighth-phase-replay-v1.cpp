// Independent T8B grid replay in Z[i,sqrt2], not Z[zeta8].
// Replace every K entry by common nonzero 4D*K; d=N/D and all source
// phases are eighth roots. DP matching and fixed-row DFS; no ray filter.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using V=std::array<int64_t,4>;using A=std::array<int,8>;struct E{int s;std::array<int,4>e;};
int m8(int x){x%=8;return x<0?x+8:x;}
V add(V a,V b){for(int i=0;i<4;i++)a[i]+=b[i];return a;}V sc(V a,int s){for(auto &x:a)x*=s;return a;}V cj(V a){return V{a[0],-a[1],a[2],-a[3]};}
V mul(V a,V b){return V{a[0]*b[0]-a[1]*b[1]+2*(a[2]*b[2]-a[3]*b[3]),a[0]*b[1]+a[1]*b[0]+2*(a[2]*b[3]+a[3]*b[2]),a[0]*b[2]+a[2]*b[0]-a[1]*b[3]-a[3]*b[1],a[0]*b[3]+a[3]*b[0]+a[1]*b[2]+a[2]*b[1]};}
V rt(int k){static const V r[8]={{2,0,0,0},{0,0,1,1},{0,2,0,0},{0,0,-1,1},{-2,0,0,0},{0,0,-1,-1},{0,-2,0,0},{0,0,1,-1}};return r[m8(k)];}
E tok(std::string s){E x{};x.s=1;if(s[0]=='-'){x.s=-1;s=s.substr(1);}for(char c:s)if(c>='a'&&c<='d')x.e[c-'a']++;return x;}
bool pm(int const*g){bool D[256]={};D[0]=true;for(int mask=1;mask<256;mask++)if(!(__builtin_popcount((unsigned)mask)&1)){int c=__builtin_ctz((unsigned)mask),rest=mask&~(1<<c),opts=g[c]&rest;while(opts){int d=__builtin_ctz((unsigned)opts);opts&=opts-1;if(D[rest&~(1<<d)]){D[mask]=true;break;}}}return D[255];}
int main(){std::string S[8][8]={{"1","1","1","1","1","1","1","1"},{"1","-1","-d","-c","d","c","cd","-cd"},{"1","-a","-1","c","a","-ac","-c","ac"},{"1","a","d","-1","ad","-a","-d","-ad"},{"1","b","-b","-bc","-1","-c","c","bc"},{"1","-b","bd","b","-d","-1","d","-bd"},{"1","-ab","b","-b","-a","a","-1","ab"},{"1","ab","-bd","bc","-ad","ac","-cd","-abcd"}};E T[8][8];for(int r=0;r<8;r++)for(int c=0;c<8;c++)T[r][c]=tok(S[r][c]);
 uint64_t tested=0,denzero=0,nonroot=0,halves=0,matching=0,orders=0,nodes=0;bool found=false;int aa=0,bb=0,cc=0;A so{},sr{};
 for(int a=0;a<8&&!found;a++)for(int b=0;b<8&&!found;b++)for(int c=0;c<8&&!found;c++){
  V N=add(add(rt(0),rt(a+b)),add(rt(a+c),rt(b+c))),D=add(add(rt(a),rt(b)),add(rt(c),rt(a+b+c)));if(D==V{}){denzero++;continue;}if(N==V{})return 2;tested++;
  bool roots=false;for(int k=0;k<8;k++)if(sc(N,2)==mul(rt(k),D))roots=true;if(!roots)nonroot++;
  V K[8][8],G[8][8][8];for(int t=0;t<8;t++)for(int x=0;x<8;x++){
   E e=T[t][x];int n=e.e[0]*a+e.e[1]*b+e.e[2]*c;K[t][x]=sc(mul(e.e[3]?N:D,rt(n)),e.s);}
  for(int t=0;t<8;t++)for(int x=0;x<8;x++)for(int y=0;y<8;y++)G[t][x][y]=mul(cj(K[t][x]),K[t][y]);
  for(int x=0;x<8;x++)for(int y=x+1;y<8;y++){V v{};for(int t=0;t<8;t++)v=add(v,G[t][x][y]);if(v!=V{})return 3;}
  for(int mask=1;mask<256&&!found;mask+=2)if(__builtin_popcount((unsigned)mask)==4){
   halves++;int g[8]={};for(int x=0;x<8;x++)for(int y=x+1;y<8;y++){V v{};for(int t=0;t<8;t++)if(mask>>t&1)v=add(v,G[t][x][y]);if(v==V{}){g[x]|=1<<y;g[y]|=1<<x;}}
   if(!pm(g))continue;matching++;std::vector<int>ev,od;for(int t=1;t<8;t++)((mask>>t&1)?ev:od).push_back(t);
   do{do{
    A O{};O[0]=0;for(int j=0;j<3;j++)O[2*j+2]=ev[j];for(int j=0;j<4;j++)O[2*j+1]=od[j];orders++;
    bool ok[8][8][8]={};for(int d=1;d<8;d++)for(int x=0;x<8;x++)for(int y=0;y<8;y++)if(x!=y){V v{};for(int t=0;t<8;t++)v=add(v,mul(rt(d*t),G[O[t]][x][y]));ok[d][x][y]=(v==V{});}
    A q;q.fill(-1);q[0]=0;auto dfs=[&](auto&&self,int r,int used)->bool{nodes++;if(r==8){sr=q;return true;}for(int x=0;x<8;x++)if(!(used>>x&1)){
      bool yes=true;for(int s=0;s<r;s++)if(!ok[m8(r-s)][q[s]][x]){yes=false;break;}if(yes){q[r]=x;if(self(self,r+1,used|(1<<x)))return true;q[r]=-1;}}
     return false;};
    if(dfs(dfs,1,1)){found=true;aa=a;bb=b;cc=c;so=O;break;}
   }while(std::next_permutation(od.begin(),od.end()));if(found)break;std::sort(od.begin(),od.end());}while(std::next_permutation(ev.begin(),ev.end()));
  }
 }
 std::ofstream j("frontier-20261028-t8b-eighth-phase-replay-v1.json");j<<"{\n \"phase_triples_tested\":"<<tested<<", \"denominator_zero\":"<<denzero<<", \"nonroot_d\":"<<nonroot<<", \"halfgraphs\":"<<halves<<", \"matching_halves\":"<<matching<<", \"orders\":"<<orders<<", \"nodes\":"<<nodes<<", \"found\":"<<(found?"true":"false");
 if(found){j<<", \"a_b_c_exponents\":["<<aa<<','<<bb<<','<<cc<<"], \"physical_source_order\":[";for(int i=0;i<8;i++){if(i)j<<',';j<<so[i];}j<<"], \"column_per_row\":[";for(int i=0;i<8;i++){if(i)j<<',';j<<sr[i];}j<<"]";}j<<"\n}\n";
 std::cout<<"params="<<tested<<" denzero="<<denzero<<" nonroot="<<nonroot<<" halves="<<halves<<" matching="<<matching<<" orders="<<orders<<" nodes="<<nodes<<" found="<<found<<'\n';
}
