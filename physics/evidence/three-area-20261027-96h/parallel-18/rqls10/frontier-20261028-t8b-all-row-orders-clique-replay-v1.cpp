// Independent Q[zeta24]/(x8-x4+1), pivoted Bron–Kerbosch replay.
// Every 8-clique must satisfy rowcount(0)+rowcount(1)+2*colcount(0)+2=0 mod4.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
using V=std::array<int64_t,2>;using W=std::array<int64_t,8>;using A=std::array<int,8>;
V mul(V a,V b){return V{a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]};}V cj(V a){return V{a[0]+a[1],-a[1]};}V neg(V a){return V{-a[0],-a[1]};}
V kval(std::string x){bool n=false;if(x[0]=='-'){n=true;x=x.substr(1);}V q{7,0},s{0,7},d{5,3};for(char c:x)if(c>='a'&&c<='d'){V z=mul(q,c=='d'?d:s);if(z[0]%7||z[1]%7)std::exit(2);q=V{z[0]/7,z[1]/7};}return n?neg(q):q;}
int md(int x,int n){x%=n;return x<0?x+n:x;}
int main(){std::string S[8][8]={{"1","1","1","1","1","1","1","1"},{"1","-1","-d","-c","d","c","cd","-cd"},{"1","-a","-1","c","a","-ac","-c","ac"},{"1","a","d","-1","ad","-a","-d","-ad"},{"1","b","-b","-bc","-1","-c","c","bc"},{"1","-b","bd","b","-d","-1","d","-bd"},{"1","-ab","b","-b","-a","a","-1","ab"},{"1","ab","-bd","bc","-ad","ac","-cd","-abcd"}};
 V K[8][8],G[8][8][8];for(int r=0;r<8;r++)for(int c=0;c<8;c++){K[r][c]=kval(S[r][c]);if(mul(cj(K[r][c]),K[r][c])!=V{49,0})return 3;}
 for(int t=0;t<8;t++)for(int c=0;c<8;c++)for(int d=0;d<8;d++)G[t][c][d]=mul(cj(K[t][c]),K[t][d]);
 for(int c=0;c<8;c++)for(int d=c+1;d<8;d++){V x{};for(int t=0;t<8;t++){x[0]+=G[t][c][d][0];x[1]+=G[t][c][d][1];}if(x!=V{})return 4;}
 W roots[24];W x{1,0,0,0,0,0,0,0};for(int j=0;j<24;j++){roots[j]=x;auto q=x[7];x=W{-q,x[0],x[1],x[2],x[3]+q,x[4],x[5],x[6]};}if(x!=W{1,0,0,0,0,0,0,0})return 5;
 A O={0,1,2,3,4,5,6,7};uint64_t orders=0,cliques=0,bad=0,nodes=0,maxcl=0;std::ofstream out("frontier-20261028-t8b-all-row-orders-clique-replay-v1.jsonl");
 do{orders++;uint64_t adj[64]={};
  for(int r=0;r<8;r++)for(int c=0;c<8;c++)for(int s=r;s<8;s++)for(int d=0;d<8;d++){
   int a=8*r+c,b=8*s+d;if(a>=b)continue;W sum{};
   for(int tau=0;tau<8;tau++){int e=md(3*(s-r)*tau,24);V g=G[O[tau]][c][d];for(int j=0;j<8;j++)sum[j]+=g[0]*roots[e][j]+g[1]*roots[(e+4)%24][j];}
   if(sum==W{}){adj[a]|=1ULL<<b;adj[b]|=1ULL<<a;}
  }
  uint64_t here=0,herebad=0;
  auto bk=[&](auto&&self,uint64_t R,uint64_t C,uint64_t X,int depth)->void{
   nodes++;if(depth+__builtin_popcountll(C)<8)return;
   if(depth==8){here++;int r0=0,r1=0,c0=0;for(int i=0;i<64;i++)if(R>>i&1){r0+=i/8==0;r1+=i/8==1;c0+=i%8==0;}if((r0+r1+2*c0+2)%4)herebad++;return;}
   uint64_t union0=C|X;int pivot=-1,best=-1;while(union0){int u=__builtin_ctzll(union0);union0&=union0-1;int z=__builtin_popcountll(C&adj[u]);if(z>best){best=z;pivot=u;}}
   uint64_t cand=pivot<0?C:C&~adj[pivot];while(cand){int v=__builtin_ctzll(cand);uint64_t bit=1ULL<<v;cand&=cand-1;self(self,R|bit,C&adj[v],X&adj[v],depth+1);C&=~bit;X|=bit;}
  };bk(bk,0,~0ULL,0,0);cliques+=here;bad+=herebad;maxcl=std::max(maxcl,here);
  out<<"{\"O\":[";for(int j=0;j<8;j++){if(j)out<<',';out<<O[j];}out<<"],\"cliques\":"<<here<<",\"bad\":"<<herebad<<"}\n";
 }while(std::next_permutation(O.begin()+1,O.end()));
 std::ofstream j("frontier-20261028-t8b-all-row-orders-clique-replay-v1.json");j<<"{\n \"orders\":"<<orders<<", \"total_cliques\":"<<cliques<<", \"bad_cliques\":"<<bad<<", \"max_cliques\":"<<maxcl<<", \"BK_nodes\":"<<nodes<<"\n}\n";
 std::cout<<"orders="<<orders<<" cliques="<<cliques<<" bad="<<bad<<" max="<<maxcl<<" nodes="<<nodes<<'\n';
}
