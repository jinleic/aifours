// Exact shape classifier for one q30 same-parity cell pair. No global QLS claim.
// z_t in mu30, z_0=1, column sum zero and sum zeta5^u(z_u+z_{u+5})=0.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using V=std::array<int,8>; using Key=std::array<int8_t,16>;
struct H {size_t operator()(Key const& x)const noexcept {size_t h=1469598103934665603ULL;for(auto a:x){h^=uint8_t(a);h*=1099511628211ULL;}return h;}};
struct W {std::array<V,5> r;int a,b;bool nz;};
struct Bucket {std::array<uint64_t,3> cnt{};std::array<int,3> a{{-1,-1,-1}},b{{-1,-1,-1}};};
int main(){
 int v6[6][2]={{1,0},{0,1},{-1,1},{-1,0},{0,-1},{1,-1}};
 int v5[5][4]={{1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1},{-1,-1,-1,-1}};
 V root[30];for(int k=0;k<30;k++)for(int a=0;a<2;a++)for(int b=0;b<4;b++)root[k][4*a+b]=v6[(5*k)%6][a]*v5[k%5][b];
 std::vector<W> ws;std::unordered_map<std::string,int> uniq;
 for(int a=0;a<30;a++)for(int b=a;b<30;b++){
  V z;std::string code;for(int i=0;i<8;i++){z[i]=root[a][i]+root[b][i];code.push_back(char(z[i]+2));}
  if(uniq.count(code))continue;uniq[code]=ws.size();W w{};w.a=a;w.b=b;w.nz=false;
  for(int u=0;u<5;u++)for(int i=0;i<8;i++)w.r[u][i]=root[(a+6*u)%30][i]+root[(b+6*u)%30][i];
  for(int i=0;i<8;i++)w.nz|=z[i]!=0;ws.push_back(w);
 }
 std::unordered_map<Key,Bucket,H> pairs;pairs.reserve(ws.size()*ws.size()*2);
 for(int a=0;a<(int)ws.size();a++)for(int b=0;b<(int)ws.size();b++){
  Key k;for(int i=0;i<8;i++){k[i]=ws[a].r[0][i]+ws[b].r[0][i];k[i+8]=ws[a].r[1][i]+ws[b].r[2][i];}
  int t=ws[a].nz+ws[b].nz;auto &v=pairs[k];v.cnt[t]++;if(v.a[t]<0){v.a[t]=a;v.b[t]=b;}
 }
 uint64_t hist[6]={};int sample[6][10];for(auto &r:sample)for(int &x:r)x=-1;
 for(int b0=0;b0<30;b0++)for(int c=0;c<(int)ws.size();c++)for(int d=0;d<(int)ws.size();d++){
  Key k;bool z0=false;for(int i=0;i<8;i++){
   int w0=root[0][i]+root[b0][i];z0|=w0!=0;
   k[i]=-w0-ws[c].r[0][i]-ws[d].r[0][i];k[8+i]=-w0-ws[c].r[3][i]-ws[d].r[4][i];
  }
  auto it=pairs.find(k);if(it==pairs.end())continue;
  for(int t=0;t<=2;t++)if(it->second.cnt[t]){
   int nz=(int)z0+ws[c].nz+ws[d].nz+t;hist[nz]+=it->second.cnt[t];
   if(sample[nz][0]<0){int a=it->second.a[t],b=it->second.b[t];
    int v[10]={0,b0,ws[a].a,ws[a].b,ws[b].a,ws[b].b,ws[c].a,ws[c].b,ws[d].a,ws[d].b};
    for(int i=0;i<10;i++)sample[nz][i]=v[i];}
  }
 }
 std::ofstream f("frontier-20261028-q30-even-pair-classifier-v1.json");
 f<<"{\n  \"q\":30, \"pair_sum_types\":"<<ws.size()<<", \"left_pair_keys\":"<<pairs.size()<<",\n  \"distinct_coefficient_shape_histogram\":[";
 for(int i=0;i<6;i++){if(i)f<<",";f<<hist[i];}f<<"],\n  \"sample_exponents_in_u_pair_order\":[";
 for(int i=0;i<6;i++){if(i)f<<",";f<<"[";for(int j=0;j<10;j++){if(j)f<<",";f<<sample[i][j];}f<<"]";}f<<"]\n}\n";
 std::cout<<"q30 unique two-root sums "<<ws.size()<<" left pair keys "<<pairs.size()<<" shape histogram";for(auto h:hist)std::cout<<" "<<h;std::cout<<"\n";
}
