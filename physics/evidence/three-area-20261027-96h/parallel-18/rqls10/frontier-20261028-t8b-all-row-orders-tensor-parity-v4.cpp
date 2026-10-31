// Exact all-source-order local orthobase + F2 odd-tensor obstruction census.
// K8 = source T8B(a=b=c=zeta6,d=(5+3zeta6)/7), integer pair basis Q(zeta6)
// denominator7, physical zeta8 factor. For each normalized source order,
// enumerate ALL local8 ONB cliques and test necessary odd-m incidence mod2.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using V=std::array<int64_t,2>;using A=std::array<int,8>;
V mul(V a,V b){return V{a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]+a[1]*b[1]};}
V cj(V a){return V{a[0]+a[1],-a[1]};}
V neg(V a){return V{-a[0],-a[1]};}
int m8(int x){x%=8;return x<0?x+8:x;}
V kval(std::string x){bool n=false;if(x[0]=='-'){n=true;x=x.substr(1);}V q{7,0},s{0,7},d{5,3};for(char c:x)if(c>='a'&&c<='d'){
 V z=mul(q,c=='d'?d:s);if(z[0]%7||z[1]%7){std::cerr<<"noninteger source";std::exit(2);}q=V{z[0]/7,z[1]/7};}return n?neg(q):q;}
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
int main(){std::string S[8][8]={{"1","1","1","1","1","1","1","1"},{"1","-1","-d","-c","d","c","cd","-cd"},{"1","-a","-1","c","a","-ac","-c","ac"},{"1","a","d","-1","ad","-a","-d","-ad"},{"1","b","-b","-bc","-1","-c","c","bc"},{"1","-b","bd","b","-d","-1","d","-bd"},{"1","-ab","b","-b","-a","a","-1","ab"},{"1","ab","-bd","bc","-ad","ac","-cd","-abcd"}};
 V K[8][8],G[8][8][8];for(int t=0;t<8;t++)for(int c=0;c<8;c++)K[t][c]=kval(S[t][c]);
 for(int t=0;t<8;t++)for(int c=0;c<8;c++)for(int d=0;d<8;d++)G[t][c][d]=mul(cj(K[t][c]),K[t][d]);
 for(int c=0;c<8;c++)for(int d=c+1;d<8;d++){V s{};for(int t=0;t<8;t++){s[0]+=G[t][c][d][0];s[1]+=G[t][c][d][1];}if(s!=V{})return 3;}
 A O={0,1,2,3,4,5,6,7};uint64_t orders=0,excluded=0,unresolved=0,cliquetotal=0,maxcliques=0,nodes=0,badcliques=0,badorders=0,rows=0,cols=0,rect=0,other=0;
 std::ofstream out("frontier-20261028-t8b-all-row-orders-tensor-parity-v4.jsonl");
 do{orders++;uint64_t adj[64]={};
  for(int r=0;r<8;r++)for(int c=0;c<8;c++)for(int rr=r;rr<8;rr++)for(int cc=0;cc<8;cc++){
   int x=8*r+c,y=8*rr+cc;if(x>=y)continue;bool zero=false;
   if(r==rr||c==cc)zero=true;else{
    int64_t v[4][2]={{}};for(int tau=0;tau<8;tau++){int k=m8((rr-r)*tau),sg=k<4?1:-1;V q=G[O[tau]][c][cc];v[k%4][0]+=sg*q[0];v[k%4][1]+=sg*q[1];}
    zero=true;for(auto &x:v)for(auto y:x)if(y)zero=false;
   }
   if(zero){adj[x]|=1ULL<<y;adj[y]|=1ULL<<x;}
  }
  std::vector<C>cl;auto dfs=[&](auto&&self,uint64_t selected,uint64_t candidates,int depth)->void{
   nodes++;if(depth==8){C q{};q.bits=selected;for(int i=0;i<64;i++)if(selected>>i&1){q.r[i/8]++;q.c[i%8]++;}cl.push_back(q);return;}
   if(depth+__builtin_popcountll(candidates)<8)return;
   while(candidates){int x=__builtin_ctzll(candidates);candidates&=candidates-1;self(self,selected|(1ULL<<x),candidates&adj[x],depth+1);}
  };dfs(dfs,0,~0ULL,0);if(cl.size()<16)return 4;
  cliquetotal+=cl.size();maxcliques=std::max<uint64_t>(maxcliques,cl.size());bool bad=false;for(auto const&q:cl){if((q.r[0]+q.r[1]+2*q.c[0]+2)%4){badcliques++;bad=true;}int nr=0,nc=0;for(int x:q.r)nr+=x!=0;for(int x:q.c)nc+=x!=0;if(nr==1&&nc==8)rows++;else if(nr==8&&nc==1)cols++;else if(nr==4&&nc==2)rect++;else other++;}if(bad)badorders++;bool no=parity_inconsistent(cl);if(no)excluded++;else unresolved++;
  out<<"{\"O\":[";for(int i=0;i<8;i++){if(i)out<<',';out<<O[i];}out<<"],\"cliques\":"<<cl.size()<<",\"parity_inconsistent\":"<<(no?"true":"false")<<"}\n";
 }while(std::next_permutation(O.begin()+1,O.end()));
 std::ofstream j("frontier-20261028-t8b-all-row-orders-tensor-parity-v4.json");
 j<<"{\n \"orders\":"<<orders<<", \"parity_excluded\":"<<excluded<<", \"parity_unresolved\":"<<unresolved<<", \"total_cliques\":"<<cliquetotal<<", \"max_cliques\":"<<maxcliques<<", \"bad_cliques\":"<<badcliques<<", \"bad_orders\":"<<badorders<<", \"DFS_nodes\":"<<nodes<<"\n}\n";
 std::cout<<"orders="<<orders<<" excluded="<<excluded<<" unresolved="<<unresolved<<" cliques="<<cliquetotal<<" max="<<maxcliques<<" rows="<<rows<<" cols="<<cols<<" rect="<<rect<<" other="<<other<<" badcliques="<<badcliques<<" badorders="<<badorders<<" nodes="<<nodes<<'\n';
}
