// Exact complete counterexample scan for the 2807 cited BH(8,16) representatives.
// All physical row orders, no ray filter. zeta8 basis x^4+1.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using M=std::array<std::array<int,8>,8>;using A=std::array<int,8>;
int mod8(int x){x%=8;return x<0?x+8:x;} int mod16(int x){x%=16;return x<0?x+16:x;}
bool zero(int const*xs,int n){int z[8]={};for(int k=0;k<n;k++){int e=mod16(xs[k]);z[e%8]+=e<8?1:-1;}for(int x:z)if(x)return false;return true;}
bool fullcheck(M const&H){int z[8];for(int a=0;a<8;a++)for(int b=a+1;b<8;b++){
 for(int t=0;t<8;t++)z[t]=(H[t][b]-H[t][a]);if(!zero(z,8))return false;
 for(int t=0;t<8;t++)z[t]=(H[b][t]-H[a][t]);if(!zero(z,8))return false;
 }return true;}
bool match(int mask,int const*adj){if(!mask)return true;int c=__builtin_ctz((unsigned)mask);int opts=adj[c]&mask&~(1<<c);while(opts){int d=__builtin_ctz((unsigned)opts);opts&=opts-1;if(match(mask&~(1<<c)&~(1<<d),adj))return true;}return false;}
int main(){std::ifstream f("frontier-20261028-aalto-bh8-16-catalog-v1.txt");std::vector<M> mats;std::string s;
 while(std::getline(f,s)){if(s.empty())continue;if(s.size()!=70||s.substr(0,6)!="BH188@")return 2;M H;for(int t=0;t<8;t++)for(int c=0;c<8;c++){H[t][c]=s[6+8*t+c]-'0';if(H[t][c]<0||H[t][c]>15)return 3;}if(!fullcheck(H))return 4;mats.push_back(H);}if(mats.size()!=2807)return 5;
 uint64_t halves=0,matching=0,orders=0,nodes=0;bool found=false;int FC=-1,FE=-1;A FO{},FR{};
 for(int q=0;q<2807&&!found;q++)for(int mask=0;mask<256&&!found;mask++)if((mask&1)&&__builtin_popcount((unsigned)mask)==4){
  halves++;int adj[8]={},z[4];for(int c=0;c<8;c++)for(int d=c+1;d<8;d++){
   int j=0;for(int t=0;t<8;t++)if(mask>>t&1)z[j++]=(mats[q][t][d]-mats[q][t][c]);if(zero(z,4)){adj[c]|=1<<d;adj[d]|=1<<c;}}
  if(!match(255,adj))continue;matching++;
  std::vector<int>E,O;for(int t=1;t<8;t++)if(mask>>t&1)E.push_back(t);else O.push_back(t);
  do{do{
   A order{};order[0]=0;for(int k=0;k<3;k++)order[2*(k+1)]=E[k];for(int k=0;k<4;k++)order[2*k+1]=O[k];orders++;
   bool ok[8][8][8]={};int x[8];for(int delta=1;delta<8;delta++)for(int c=0;c<8;c++)for(int d=0;d<8;d++)if(c!=d){
    for(int tau=0;tau<8;tau++)x[tau]=2*delta*tau+(mats[q][order[tau]][d]-mats[q][order[tau]][c]);ok[delta][c][d]=zero(x,8);}
   A ass;ass.fill(-1);ass[0]=0;
   auto dfs=[&](auto&&self,int used,int depth)->bool{
    nodes++;if(depth==8){FR=ass;return true;}int chosen=-1,best=9,choices=0;
    for(int r=0;r<8;r++)if(ass[r]<0){int avail=0;for(int c=0;c<8;c++)if(!(used>>c&1)){
      bool good=true;for(int s=0;s<8;s++)if(ass[s]>=0&&!ok[mod8(r-s)][ass[s]][c]){good=false;break;}if(good)avail|=1<<c;}
     int n=__builtin_popcount((unsigned)avail);if(n<best){best=n;choices=avail;chosen=r;}if(!n)return false;}
    while(choices){int c=__builtin_ctz((unsigned)choices);choices&=choices-1;ass[chosen]=c;if(self(self,used|(1<<c),depth+1))return true;ass[chosen]=-1;}return false;
   };
   if(dfs(dfs,1,1)){found=true;FC=q;FE=mask;FO=order;break;}
  }while(std::next_permutation(O.begin(),O.end()));if(found)break;std::sort(O.begin(),O.end());}while(std::next_permutation(E.begin(),E.end()));
 }
 std::ofstream j("frontier-20261028-bh8-16-even-counterexample-v1.json");
 j<<"{\n \"catalog_classes\":2807, \"halves_examined\":"<<halves<<", \"matching_halves\":"<<matching<<", \"row_orders\":"<<orders<<", \"dfs_nodes\":"<<nodes<<", \"transversal_found\":"<<(found?"true":"false");
 if(found){j<<", \"class_zero_based\":"<<FC<<", \"even_half_mask\":"<<FE<<", \"physical_source_order\":[";for(int k=0;k<8;k++){if(k)j<<',';j<<FO[k];}j<<"], \"column_per_row\":[";for(int k=0;k<8;k++){if(k)j<<',';j<<FR[k];}j<<"]";}j<<"\n}\n";
 std::cout<<"BH8,16 classes=2807 halves="<<halves<<" match="<<matching<<" orders="<<orders<<" nodes="<<nodes<<" found="<<found<<'\n';
}
