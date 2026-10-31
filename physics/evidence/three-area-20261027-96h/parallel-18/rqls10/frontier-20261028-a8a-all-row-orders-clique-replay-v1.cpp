// Independent A8A exact i,sqrt2 basis and pivoted Bron-Kerbosch replay.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
using V=std::array<int64_t,4>;using A=std::array<int,8>;
// Basis 1,i,sqrt(2),i sqrt(2), integral exact arithmetic.
V mul(V a,V b){V o{};for(int i=0;i<4;i++)for(int j=0;j<4;j++){int ri=i/2,rj=j/2,ii=i%2,jj=j%2;int k=((ri+rj)%2)*2+(ii+jj)%2;o[k]+=a[i]*b[j]*(ri+rj>=2?2:1)*(ii+jj>=2?-1:1);}return o;}
V cj(V a){return V{a[0],-a[1],a[2],-a[3]};}
V kval(std::string x){V A{1,0,0,2},T{3,0,0,0};if(x=="1")return T;if(x=="a")return A;return V{-1,0,0,-2};}
int md(int x,int n){x%=n;return x<0?x+n:x;}
int main(){std::string S[8][8]={{"a","1","-a","1","-a","-a","a","1"},{"1","-a","1","a","-a","a","-a","1"},{"-a","1","-a","a","1","a","1","-a"},{"1","a","a","1","1","-a","-a","-a"},{"-a","-a","1","1","a","-a","1","a"},{"-a","a","a","-a","-a","1","1","1"},{"a","-a","1","-a","1","1","a","-a"},{"1","1","-a","-a","a","1","-a","a"}};
 V K[8][8],G[8][8][8];for(int r=0;r<8;r++)for(int c=0;c<8;c++){K[r][c]=kval(S[r][c]);if(mul(cj(K[r][c]),K[r][c])!=V{9,0,0,0})return 3;}
 for(int t=0;t<8;t++)for(int c=0;c<8;c++)for(int d=0;d<8;d++)G[t][c][d]=mul(cj(K[t][c]),K[t][d]);
 for(int c=0;c<8;c++)for(int d=c+1;d<8;d++){V x{};for(int t=0;t<8;t++){for(int k=0;k<4;k++)x[k]+=G[t][c][d][k];}if(x!=V{})return 4;}
 V roots[8]={{2,0,0,0},{0,0,1,1},{0,2,0,0},{0,0,-1,1},{-2,0,0,0},{0,0,-1,-1},{0,-2,0,0},{0,0,1,-1}};
 A O={0,1,2,3,4,5,6,7};uint64_t orders=0,cliques=0,bad=0,nodes=0,maxcl=0;std::ofstream out("frontier-20261028-a8a-all-row-orders-clique-replay-v1.jsonl");
 do{orders++;uint64_t adj[64]={};
  for(int r=0;r<8;r++)for(int c=0;c<8;c++)for(int s=r;s<8;s++)for(int d=0;d<8;d++){
   int a=8*r+c,b=8*s+d;if(a>=b)continue;V sum{};
   for(int tau=0;tau<8;tau++){int e=md((s-r)*tau,8);V g=mul(G[O[tau]][c][d],roots[e]);for(int j=0;j<4;j++)sum[j]+=g[j];}
   if(sum==V{}){adj[a]|=1ULL<<b;adj[b]|=1ULL<<a;}
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
 std::ofstream j("frontier-20261028-a8a-all-row-orders-clique-replay-v1.json");j<<"{\n \"orders\":"<<orders<<", \"total_cliques\":"<<cliques<<", \"bad_cliques\":"<<bad<<", \"max_cliques\":"<<maxcl<<", \"BK_nodes\":"<<nodes<<"\n}\n";
 std::cout<<"orders="<<orders<<" cliques="<<cliques<<" bad="<<bad<<" max="<<maxcl<<" nodes="<<nodes<<'\n';
}
