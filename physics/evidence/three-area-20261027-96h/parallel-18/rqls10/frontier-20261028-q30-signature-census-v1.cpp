// Full necessary signature census for two same-parity q30 transversal cells.
// g[u] = (arg z_(u+5) - arg z_u) mod30, z0=1, and both 10-root sums vanish.
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
using V=std::array<int,8>;using Key=std::array<int8_t,16>;
struct H{size_t operator()(Key const&x)const noexcept{size_t h=1469598103934665603ULL;for(auto a:x){h^=uint8_t(a);h*=1099511628211ULL;}return h;}};
struct W{std::array<V,5>r;int a,b;bool nz;};struct Pair{int a,b;};
int main(){
 int v6[6][2]={{1,0},{0,1},{-1,1},{-1,0},{0,-1},{1,-1}};
 int v5[5][4]={{1,0,0,0},{0,1,0,0},{0,0,1,0},{0,0,0,1},{-1,-1,-1,-1}};
 V root[30];for(int k=0;k<30;k++)for(int a=0;a<2;a++)for(int b=0;b<4;b++)root[k][4*a+b]=v6[(5*k)%6][a]*v5[k%5][b];
 std::vector<W>ws;std::unordered_map<std::string,int>uniq;
 for(int a=0;a<30;a++)for(int b=a;b<30;b++){
  std::string code;for(int i=0;i<8;i++)code.push_back(char(root[a][i]+root[b][i]+2));
  if(uniq.count(code))continue;uniq[code]=ws.size();W w{};w.a=a;w.b=b;w.nz=false;
  for(int u=0;u<5;u++)for(int i=0;i<8;i++)w.r[u][i]=root[(a+6*u)%30][i]+root[(b+6*u)%30][i];
  for(int i=0;i<8;i++)w.nz|=w.r[0][i]!=0;ws.push_back(w);
 }
 std::unordered_map<Key,Pair,H>pairs;pairs.reserve(ws.size()*ws.size()*2);
 for(int a=0;a<(int)ws.size();a++)for(int b=0;b<(int)ws.size();b++){
  Key k;for(int i=0;i<8;i++){k[i]=ws[a].r[0][i]+ws[b].r[0][i];k[i+8]=ws[a].r[1][i]+ws[b].r[2][i];}
  if(!pairs.emplace(k,Pair{a,b}).second){std::cerr<<"left key collision\n";return 2;}
 }
 const int N=30*30*30*30*30;std::vector<uint8_t>bits((N+7)/8);uint64_t shapes=0,unique=0;
 for(int b0=0;b0<30;b0++)for(int c=0;c<(int)ws.size();c++)for(int d=0;d<(int)ws.size();d++){
  Key k;for(int i=0;i<8;i++){int w0=root[0][i]+root[b0][i];k[i]=-w0-ws[c].r[0][i]-ws[d].r[0][i];k[i+8]=-w0-ws[c].r[3][i]-ws[d].r[4][i];}
  auto it=pairs.find(k);if(it==pairs.end())continue;shapes++;
  int w[4]={it->second.a,it->second.b,c,d};
  for(int mask=0;mask<16;mask++){
   int idx=b0,mul=30;
   for(int u=0;u<4;u++){
    W const&x=ws[w[u]];int g=x.nz?(x.b-x.a+30)%30:15;
    if((mask>>u)&1)g=(30-g)%30;idx+=mul*g;mul*=30;
   }
   uint8_t bit=uint8_t(1u<<(idx%8));if(!(bits[idx/8]&bit)){bits[idx/8]|=bit;unique++;}
  }
 }
 std::ofstream f("frontier-20261028-q30-signature-census-v1.bin",std::ios::binary);f.write((char*)bits.data(),bits.size());
 std::ofstream j("frontier-20261028-q30-signature-census-v1.json");
 j<<"{\n  \"alphabet\":30, \"universe\":"<<N<<", \"unique_pair_sums\":"<<ws.size()<<", \"left_keys\":"<<pairs.size()<<", \"coefficient_shapes\":"<<shapes<<", \"signatures\":"<<unique<<", \"bitset_bytes\":"<<bits.size()<<"\n}\n";
 std::cout<<"shapes="<<shapes<<" signatures="<<unique<<" bytes="<<bits.size()<<"\n";
}
