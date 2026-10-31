// Independent full n12/BH(12,3) Fourier-transversal replay.
// Q(zeta12)=Q(zeta6) + i Q(zeta6), zeta12=i*zeta6^-1.
// Subset-DP perfect matching and fixed-row DFS; no ray filter.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using V=std::array<int,4>;using H=std::array<std::array<int,12>,12>;using A=std::array<int,12>;
int md(int x,int n){x%=n;return x<0?x+n:x;}V add(V a,V b){for(int i=0;i<4;i++)a[i]+=b[i];return a;}
V phase(int f,int e){static const int s[6][2]={{1,0},{0,1},{-1,1},{-1,0},{0,-1},{1,-1}};int q=md(f,4),j=md(-f+2*e,6);V v{};int z=q<2?1:-1;if(q%2==0){v[0]=z*s[j][0];v[1]=z*s[j][1];}else{v[2]=z*s[j][0];v[3]=z*s[j][1];}return v;}
bool pm(int const*g){bool D[4096]={};D[0]=true;for(int mask=1;mask<4096;mask++)if(!(__builtin_popcount((unsigned)mask)&1)){int a=__builtin_ctz((unsigned)mask),rest=mask&~(1<<a),opts=g[a]&rest;while(opts){int b=__builtin_ctz((unsigned)opts);opts&=opts-1;if(D[rest&~(1<<b)]){D[mask]=true;break;}}}return D[4095];}
int main(){std::ifstream f("frontier-20261028-aalto-bh12-3-catalog-v1.txt");std::vector<H>K;std::string line;
 while(std::getline(f,line)){if(line.empty())continue;if(line.size()!=150||line.substr(0,6)!="BH1<<3")return 2;H h;for(int r=0;r<12;r++)for(int c=0;c<12;c++){h[r][c]=line[6+12*r+c]-'0';if(h[r][c]<0||h[r][c]>2)return 3;}for(int a=0;a<12;a++)for(int b=a+1;b<12;b++){V r{},c{};for(int t=0;t<12;t++){r=add(r,phase(0,h[a][t]-h[b][t]));c=add(c,phase(0,h[t][a]-h[t][b]));}if(r!=V{}||c!=V{})return 4;}K.push_back(h);}if(K.size()!=2)return 5;
 uint64_t halves=0,matching=0,orders=0,nodes=0;bool found=false;int cls=-1;A savedorder{},savedchoice{};
 for(int q=0;q<2&&!found;q++)for(int mask=1;mask<4096&&!found;mask+=2)if(__builtin_popcount((unsigned)mask)==6){
  halves++;int graph[12]={};for(int c=0;c<12;c++)for(int d=c+1;d<12;d++){V x{};for(int t=0;t<12;t++)if(mask>>t&1)x=add(x,phase(0,K[q][t][d]-K[q][t][c]));if(x==V{}){graph[c]|=1<<d;graph[d]|=1<<c;}}
  if(!pm(graph))continue;matching++;std::vector<int>ev,od;for(int t=1;t<12;t++)((mask>>t&1)?ev:od).push_back(t);
  do{do{
   A O{};O[0]=0;for(int j=0;j<5;j++)O[2*j+2]=ev[j];for(int j=0;j<6;j++)O[2*j+1]=od[j];orders++;
   signed char cache[12][12][12];for(auto &a:cache)for(auto &b:a)for(auto &c:b)c=-1;
   auto good=[&](int delta,int c,int d)->bool{auto &z=cache[delta][c][d];if(z>=0)return z;V x{};for(int t=0;t<12;t++)x=add(x,phase(delta*t,K[q][O[t]][d]-K[q][O[t]][c]));z=(x==V{});return z;};
   A qv;qv.fill(-1);qv[0]=0;auto dfs=[&](auto&&self,int r,int used)->bool{nodes++;if(r==12){savedchoice=qv;return true;}for(int c=0;c<12;c++)if(!(used>>c&1)){
     bool yes=true;for(int s=0;s<r;s++)if(!good(md(r-s,12),qv[s],c)){yes=false;break;}if(yes){qv[r]=c;if(self(self,r+1,used|(1<<c)))return true;qv[r]=-1;}}
    return false;};
   if(dfs(dfs,1,1)){found=true;cls=q;savedorder=O;break;}
  }while(std::next_permutation(od.begin(),od.end()));if(found)break;std::sort(od.begin(),od.end());}while(std::next_permutation(ev.begin(),ev.end()));
 }
 std::ofstream j("frontier-20261028-bh12-3-even-replay-v1.json");j<<"{\n \"classes\":2, \"halves\":"<<halves<<", \"matching_halves\":"<<matching<<", \"orders\":"<<orders<<", \"nodes\":"<<nodes<<", \"found\":"<<(found?"true":"false");
 if(found){j<<", \"class_zero_based\":"<<cls<<", \"source_order\":[";for(int i=0;i<12;i++){if(i)j<<',';j<<savedorder[i];}j<<"], \"column_per_row\":[";for(int i=0;i<12;i++){if(i)j<<',';j<<savedchoice[i];}j<<"]";}j<<"\n}\n";
 std::cout<<"classes="<<K.size()<<" halves="<<halves<<" matching="<<matching<<" orders="<<orders<<" nodes="<<nodes<<" found="<<found<<'\n';
}
