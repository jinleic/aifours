// Exact necessary-condition scan for Fourier-product T in all row-order
// K10=[F5, diag(delta)F5; F5, -diag(delta)F5], all unit delta.
// Phase-free within-block orthogonality is in Z[zeta10]. Cross-block
// conditions are linear in delta. Rank5 mod p implies rank5 over Q(zeta10).
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using A=std::array<int,4>;
A R[10];int Rp[10],pairpos[5][2],f[5],g[5];bool good[10][5];
uint64_t orders=0,zeroOrders=0,fcount=0,fgcount=0,fullRank=0,lowRank=0;
std::ofstream out("frontier-20261028-n10-dita-allorders-rank-scan-v2.jsonl");
int mod(int a,int n){a%=n;return a<0?a+n:a;}
int powmod(int a,int n){int v=1;while(n){if(n&1)v=v*a%31;a=a*a%31;n>>=1;}return v;}
int rank_cross(){int piv[5][5]={{}},rank=0;bool taken[5]={};
 for(int b=0;b<5;b++)for(int c=0;c<5;c++){
  int d=mod(g[c]-f[b],10),k=mod(c-b,5),row[5];
  for(int t=0;t<5;t++){int u=Rp[mod(d*pairpos[t][0]+2*t*k,10)],v=Rp[mod(d*pairpos[t][1]+2*t*k,10)];row[t]=mod(u-v,31);}
  for(int j=0;j<5;j++)if(row[j]){
   if(taken[j]){int a=row[j];for(int k=j;k<5;k++)row[k]=mod(row[k]-a*piv[j][k],31);}
   else{int inv=powmod(row[j],29);for(int k=j;k<5;k++)piv[j][k]=row[k]*inv%31;taken[j]=true;rank++;break;}
  }
  if(rank==5)return rank;
 }
 return rank;
}
void dfs_g(int b,int used){
 if(b==5){fgcount++;int rank=rank_cross();if(rank==5){fullRank++;return;}lowRank++;out<<"{\"pairs\":[";for(int t=0;t<5;t++){if(t)out<<',';out<<'['<<pairpos[t][0]<<','<<pairpos[t][1]<<']';}out<<"],\"f\":[";for(int t=0;t<5;t++){if(t)out<<',';out<<f[t];}out<<"],\"g\":[";for(int t=0;t<5;t++){if(t)out<<',';out<<g[t];}out<<"],\"rank31\":"<<rank<<"}\n";return;}
 for(int r=0;r<10;r++)if(!(used>>r&1)){
  bool ok=true;for(int c=0;c<b;c++)if(!good[mod(r-g[c],10)][mod(b-c,5)]){ok=false;break;}
  if(ok){g[b]=r;dfs_g(b+1,used|1<<r);}
 }
}
void dfs_f(int b,int used){
 if(b==5){fcount++;dfs_g(0,used);return;}
 for(int r=0;r<10;r++)if(!(used>>r&1)){
  bool ok=true;for(int c=0;c<b;c++)if(!good[mod(r-f[c],10)][mod(b-c,5)]){ok=false;break;}
  if(ok){f[b]=r;dfs_f(b+1,used|1<<r);}
 }
}
std::ofstream summary("frontier-20261028-n10-dita-order-summary-producer-v1.jsonl");
void process(){auto f0=fcount,g0=fgcount,h0=fullRank,l0=lowRank;orders++;int z=0;
 for(int d=1;d<10;d++)for(int k=1;k<5;k++){
  A sum{};for(int t=0;t<5;t++)for(int a=0;a<2;a++){A q=R[mod(d*pairpos[t][a]+2*t*k,10)];for(int j=0;j<4;j++)sum[j]+=q[j];}
  good[d][k]=(sum==A{});z+=good[d][k];
 }
 if(z==0)zeroOrders++;else{f[0]=0;dfs_f(1,1);}
 summary<<"{\"pairs\":[";for(int t=0;t<5;t++){if(t)summary<<',';summary<<'['<<pairpos[t][0]<<','<<pairpos[t][1]<<']';}summary<<"],\"f\":"<<fcount-f0<<",\"fg\":"<<fgcount-g0<<",\"full\":"<<fullRank-h0<<",\"low\":"<<lowRank-l0<<"}\n";
}
void pair_rec(int t,int used){
 if(t==5){process();return;}
 for(int a=1;a<10;a++)if(!(used>>a&1))for(int b=a+1;b<10;b++)if(!(used>>b&1)){
  pairpos[t][0]=a;pairpos[t][1]=b;pair_rec(t+1,used|1<<a|1<<b);
 }
}
int main(){R[0]={1,0,0,0};for(int i=1;i<10;i++){auto [a,b,c,d]=R[i-1];R[i]={-d,a+d,b-d,c+d};}
 Rp[0]=1;for(int i=1;i<10;i++)Rp[i]=Rp[i-1]*15%31;pairpos[0][0]=0;
 for(int x=1;x<10;x++){pairpos[0][1]=x;pair_rec(1,1|1<<x);}
 out.close();std::ofstream j("frontier-20261028-n10-dita-allorders-rank-scan-v2.json");
 j<<"{\n \"orders\":"<<orders<<", \"no_same_block_edge\":"<<zeroOrders<<", \"first_block_configs\":"<<fcount<<", \"two_block_configs\":"<<fgcount<<", \"mod31_rank5\":"<<fullRank<<", \"mod31_rank_below5\":"<<lowRank<<"\n}\n";
 std::cout<<"pairings="<<orders<<" noedge="<<zeroOrders<<" f="<<fcount<<" fg="<<fgcount<<" rank5="<<fullRank<<" low="<<lowRank<<'\n';
}
