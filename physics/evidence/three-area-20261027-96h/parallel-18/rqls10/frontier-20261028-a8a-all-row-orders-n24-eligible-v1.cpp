// A8A exact local8 ONB clique census, seeking possible n=24 tensor transversals.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using V=std::array<int64_t,4>;using A=std::array<int,8>;
V mul(V a,V b){V o{};for(int i=0;i<4;i++)for(int j=0;j<4;j++)o[(i+j)%4]+=(i+j<4?1:-1)*a[i]*b[j];return o;}
int m8(int x){x%=8;return x<0?x+8:x;}
V rt(int k){k=m8(k);V o{};o[k%4]=k<4?1:-1;return o;}
V cj(V a){V o{};for(int i=0;i<4;i++){V q=rt(-i);for(int j=0;j<4;j++)o[j]+=a[i]*q[j];}return o;}
V neg(V a){for(auto &x:a)x=-x;return a;}
V kval(std::string x){V A{1,2,0,2},T{3,0,0,0};return x=="1"?T:x=="a"?A:neg(A);}
struct C{uint64_t bits;std::array<int,8>r,c;};
bool parity_inconsistent(std::vector<C>const&cl){
 int n=cl.size(),words=(n+1+63)/64;std::vector<std::vector<uint64_t>>A(17,std::vector<uint64_t>(words));
 for(int j=0;j<n;j++){
  for(int r=0;r<8;r++)if((cl[j].r[r]+1)&1)A[r][j/64]|=1ULL<<(j%64);
  for(int c=0;c<8;c++)if((cl[j].c[c]+1)&1)A[8+c][j/64]|=1ULL<<(j%64);
  A[16][j/64]|=1ULL<<(j%64);
 }
 A[16][n/64]|=1ULL<<(n%64);int row=0;
 for(int j=0;j<n&&row<17;j++){
  int q=row;while(q<17&&!(A[q][j/64]>>(j%64)&1))q++;if(q==17)continue;std::swap(A[q],A[row]);
  for(int i=row+1;i<17;i++)if(A[i][j/64]>>(j%64)&1)for(int k=0;k<words;k++)A[i][k]^=A[row][k];row++;
 }
 for(int i=row;i<17;i++){
  bool any=false;for(int j=0;j<n;j++)any|=(A[i][j/64]>>(j%64)&1);if(!any&&(A[i][n/64]>>(n%64)&1))return true;
 }
 return false;
}
int main(){std::string S[8][8]={{"a","1","-a","1","-a","-a","a","1"},{"1","-a","1","a","-a","a","-a","1"},{"-a","1","-a","a","1","a","1","-a"},{"1","a","a","1","1","-a","-a","-a"},{"-a","-a","1","1","a","-a","1","a"},{"-a","a","a","-a","-a","1","1","1"},{"a","-a","1","-a","1","1","a","-a"},{"1","1","-a","-a","a","1","-a","a"}};
 V K[8][8],G[8][8][8];for(int t=0;t<8;t++)for(int c=0;c<8;c++)K[t][c]=kval(S[t][c]);
 for(int t=0;t<8;t++)for(int c=0;c<8;c++)for(int d=0;d<8;d++)G[t][c][d]=mul(cj(K[t][c]),K[t][d]);
 for(int c=0;c<8;c++)for(int d=c+1;d<8;d++){V s{};for(int t=0;t<8;t++){for(int k=0;k<4;k++)s[k]+=G[t][c][d][k];}if(s!=V{})return 3;}
 A O={0,1,2,3,4,5,6,7};uint64_t orders=0,excluded=0,unresolved=0,cliquetotal=0,maxcliques=0,nodes=0,badcliques=0,badorders=0,rows=0,cols=0,rect=0,other=0,eligible=0;
 std::ofstream out("frontier-20261028-a8a-all-row-orders-n24-eligible-v1.jsonl");
 do{orders++;uint64_t adj[64]={};
  for(int r=0;r<8;r++)for(int c=0;c<8;c++)for(int rr=r;rr<8;rr++)for(int cc=0;cc<8;cc++){
   int x=8*r+c,y=8*rr+cc;if(x>=y)continue;bool zero=false;
   if(r==rr||c==cc)zero=true;else{
    V v{};for(int tau=0;tau<8;tau++){V q=mul(rt((rr-r)*tau),G[O[tau]][c][cc]);for(int k=0;k<4;k++)v[k]+=q[k];}
    zero=(v==V{});
   }
   if(zero){adj[x]|=1ULL<<y;adj[y]|=1ULL<<x;}
  }
  std::vector<C>cl;auto dfs=[&](auto&&self,uint64_t selected,uint64_t candidates,int depth)->void{
   nodes++;if(depth==8){C q{};q.bits=selected;for(int i=0;i<64;i++)if(selected>>i&1){q.r[i/8]++;q.c[i%8]++;}cl.push_back(q);return;}
   if(depth+__builtin_popcountll(candidates)<8)return;
   while(candidates){int x=__builtin_ctzll(candidates);candidates&=candidates-1;self(self,selected|(1ULL<<x),candidates&adj[x],depth+1);}
  };dfs(dfs,0,~0ULL,0);if(cl.size()<16)return 4;
  cliquetotal+=cl.size();maxcliques=std::max<uint64_t>(maxcliques,cl.size());bool bad=false;for(auto const&q:cl){if(*std::max_element(q.r.begin(),q.r.end())<=3&&*std::max_element(q.c.begin(),q.c.end())<=3){eligible++;if(eligible<=5){std::cout<<"ELIGIBLE ";for(int x:O)std::cout<<x;std::cout<<" ";for(int i=0;i<64;i++)if(q.bits>>i&1)std::cout<<i<<",";std::cout<<"\n";}}if((q.r[0]+q.r[1]+2*q.c[0]+2)%4){badcliques++;bad=true;}int nr=0,nc=0;for(int x:q.r)nr+=x!=0;for(int x:q.c)nc+=x!=0;if(nr==1&&nc==8)rows++;else if(nr==8&&nc==1)cols++;else if(nr==4&&nc==2)rect++;else other++;}if(bad)badorders++;bool no=parity_inconsistent(cl);if(no)excluded++;else unresolved++;
  out<<"{\"O\":[";for(int i=0;i<8;i++){if(i)out<<',';out<<O[i];}out<<"],\"cliques\":"<<cl.size()<<",\"parity_inconsistent\":"<<(no?"true":"false")<<"}\n";
 }while(std::next_permutation(O.begin()+1,O.end()));
 std::ofstream j("frontier-20261028-a8a-all-row-orders-n24-eligible-v1.json");
 j<<"{\n \"orders\":"<<orders<<", \"parity_excluded\":"<<excluded<<", \"parity_unresolved\":"<<unresolved<<", \"total_cliques\":"<<cliquetotal<<", \"max_cliques\":"<<maxcliques<<", \"bad_cliques\":"<<badcliques<<", \"bad_orders\":"<<badorders<<", \"DFS_nodes\":"<<nodes<<"\n}\n";
 std::cout<<"orders="<<orders<<" excluded="<<excluded<<" unresolved="<<unresolved<<" cliques="<<cliquetotal<<" max="<<maxcliques<<" rows="<<rows<<" cols="<<cols<<" rect="<<rect<<" other="<<other<<" eligible="<<eligible<<" badcliques="<<badcliques<<" badorders="<<badorders<<" nodes="<<nodes<<'\n';
}
