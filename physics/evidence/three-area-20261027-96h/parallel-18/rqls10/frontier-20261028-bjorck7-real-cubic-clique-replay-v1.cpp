// Independent Björck7 all-ONB replay in Q(z,g), z^3+z^2-2z-1=0, g^2=-7.
// z=2cos(2pi/7), g=sqrt(-7), 14*zeta7=7z+g(6+z-2z^2).
// Root vectors use a COMMON factor 14^6; exact pivoted Bron-Kerbosch.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
using V=std::array<int64_t,6>;using O=std::array<int,7>;
V add(V a,V b){for(int i=0;i<6;i++)a[i]+=b[i];return a;}
V mul(V a,V b){int64_t q[2][5]={{}};for(int i=0;i<6;i++)for(int j=0;j<6;j++){int g=i/3+j/3,k=i%3+j%3;q[g%2][k]+=a[i]*b[j]*(g>=2?-7:1);}for(int h=0;h<2;h++)for(int k=4;k>=3;k--){auto v=q[h][k];q[h][k-1]-=v;q[h][k-2]+=2*v;q[h][k-3]+=v;}return V{q[0][0],q[0][1],q[0][2],q[1][0],q[1][1],q[1][2]};}
V conj(V a){for(int i=3;i<6;i++)a[i]=-a[i];return a;}
int md(int a,int n){a%=n;return a<0?a+n:a;}
int main(){
 V Z{0,7,0,6,1,-2},roots[7],v{7529536,0,0,0,0,0};
 for(int i=0;i<7;i++){roots[i]=v;v=mul(v,Z);for(auto&x:v){if(x%14)return 1;x/=14;}}if(v!=roots[0])return 2;
 V one{4,0,0,0,0,0},aa{-3,0,0,1,0,0},seq[7]={one,one,one,aa,one,aa,aa},K[7][7],G[7][7][7];
 for(int r=0;r<7;r++)for(int c=0;c<7;c++){K[r][c]=seq[md(r-c,7)];if(mul(conj(K[r][c]),K[r][c])!=V{16,0,0,0,0,0})return 3;}
 for(int t=0;t<7;t++)for(int c=0;c<7;c++)for(int d=0;d<7;d++)G[t][c][d]=mul(conj(K[t][c]),K[t][d]);
 for(int c=0;c<7;c++)for(int d=c+1;d<7;d++){V x{};for(int t=0;t<7;t++)x=add(x,G[t][c][d]);if(x!=V{})return 4;}
 O order{0,1,2,3,4,5,6};uint64_t orders=0,cliques=0,row=0,col=0,other=0,nodes=0;std::ofstream out("frontier-20261028-bjorck7-order-cliques-replay-v1.jsonl");
 do{orders++;uint64_t adj[49]={};
  for(int x=0;x<49;x++)for(int y=x+1;y<49;y++){int r=x/7,c=x%7,s=y/7,d=y%7;V sum{};
   for(int tau=0;tau<7;tau++)sum=add(sum,mul(roots[md((s-r)*tau,7)],G[order[tau]][c][d]));
   if(sum==V{}){adj[x]|=1ULL<<y;adj[y]|=1ULL<<x;}
  }
  uint64_t h=0,hr=0,hc=0,ho=0;auto bk=[&](auto&&self,uint64_t selected,uint64_t cand,uint64_t excluded,int depth)->void{
   nodes++;if(depth+__builtin_popcountll(cand)<7)return;
   if(depth==7){h++;int nr=0,nc=0;bool seenr[7]={},seenc[7]={};for(int x=0;x<49;x++)if(selected>>x&1){seenr[x/7]=true;seenc[x%7]=true;}for(int i=0;i<7;i++){nr+=seenr[i];nc+=seenc[i];}if(nr==1)hr++;else if(nc==1)hc++;else ho++;return;}
   uint64_t both=cand|excluded;int pivot=-1,best=-1;while(both){int v=__builtin_ctzll(both);both&=both-1;int z=__builtin_popcountll(cand&adj[v]);if(z>best){best=z;pivot=v;}}
   uint64_t list=pivot<0?cand:cand&~adj[pivot];while(list){int v=__builtin_ctzll(list);uint64_t bit=1ULL<<v;list&=list-1;self(self,selected|bit,cand&adj[v],excluded&adj[v],depth+1);cand&=~bit;excluded|=bit;}
  };bk(bk,0,(1ULL<<49)-1,0,0);cliques+=h;row+=hr;col+=hc;other+=ho;
  out<<"{\"order\":[";for(int i=0;i<7;i++){if(i)out<<',';out<<order[i];}out<<"],\"cliques\":"<<h<<",\"rows\":"<<hr<<",\"cols\":"<<hc<<",\"other\":"<<ho<<"}\n";
 }while(std::next_permutation(order.begin()+1,order.end()));out.close();
 std::ofstream j("frontier-20261028-bjorck7-real-cubic-clique-replay-v1.json");j<<"{\n \"orders\":"<<orders<<", \"cliques\":"<<cliques<<", \"rows\":"<<row<<", \"cols\":"<<col<<", \"other\":"<<other<<", \"BK_nodes\":"<<nodes<<"\n}\n";
 std::cout<<"orders="<<orders<<" cliques="<<cliques<<" rows="<<row<<" cols="<<col<<" other="<<other<<" nodes="<<nodes<<'\n';
}
