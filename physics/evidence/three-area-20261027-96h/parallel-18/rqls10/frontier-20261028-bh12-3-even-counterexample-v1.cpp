// Bounded exact n12 even-Fourier counterexample hunt in two BH(12,3) classes.
// Native Phi12=x4-x2+1; literal original Gram, lazy cached DFS. Stops at
// 60s; incomplete search is not an exclusion or general-even evidence.
#include <algorithm>
#include <array>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using V=std::array<int,4>;using H=std::array<std::array<int,12>,12>;using A=std::array<int,12>;
int md(int x,int n){x%=n;return x<0?x+n:x;}
V add(V a,V b){for(int i=0;i<4;i++)a[i]+=b[i];return a;}V rt[12];
bool pm(int mask,int const*g){if(!mask)return true;int a=__builtin_ctz((unsigned)mask),opts=g[a]&mask&~(1<<a);while(opts){int b=__builtin_ctz((unsigned)opts);opts&=opts-1;if(pm(mask&~(1<<a)&~(1<<b),g))return true;}return false;}
int main(){V v={1,0,0,0};for(int j=0;j<12;j++){rt[j]=v;v=V{-v[3],v[0],v[1]+v[3],v[2]};}if(v!=V{1,0,0,0})return 2;
 std::ifstream f("frontier-20261028-aalto-bh12-3-catalog-v1.txt");std::vector<H>K;std::string line;
 while(std::getline(f,line)){if(line.empty())continue;if(line.size()!=150||line.substr(0,6)!="BH1<<3")return 3;H h;for(int t=0;t<12;t++)for(int c=0;c<12;c++){h[t][c]=line[6+12*t+c]-'0';if(h[t][c]<0||h[t][c]>2)return 4;}for(int a=0;a<12;a++)for(int b=a+1;b<12;b++){V r{},c{};for(int j=0;j<12;j++){r=add(r,rt[md(4*(h[a][j]-h[b][j]),12)]);c=add(c,rt[md(4*(h[j][a]-h[j][b]),12)]);}if(r!=V{}||c!=V{})return 5;}K.push_back(h);}if(K.size()!=2)return 6;
 auto start=std::chrono::steady_clock::now();uint64_t halves=0,matching=0,orders=0,nodes=0;bool found=false,timed=false;int cls=-1;A savedorder{},savedchoice{};
 for(int q=0;q<2&&!found&&!timed;q++)for(int mask=1;mask<(1<<12)&&!found&&!timed;mask+=2)if(__builtin_popcount((unsigned)mask)==6){
  halves++;int graph[12]={};for(int c=0;c<12;c++)for(int d=c+1;d<12;d++){V x{};for(int t=0;t<12;t++)if(mask>>t&1)x=add(x,rt[md(4*(K[q][t][d]-K[q][t][c]),12)]);if(x==V{}){graph[c]|=1<<d;graph[d]|=1<<c;}}
  if(!pm((1<<12)-1,graph))continue;matching++;std::vector<int>ev,od;for(int t=1;t<12;t++)((mask>>t&1)?ev:od).push_back(t);
  do{do{
   A O{};O[0]=0;for(int j=0;j<5;j++)O[2*j+2]=ev[j];for(int j=0;j<6;j++)O[2*j+1]=od[j];orders++;
   signed char cache[12][12][12];for(auto &a:cache)for(auto &b:a)for(auto &c:b)c=-1;
   auto good=[&](int delta,int c,int d)->bool{auto &z=cache[delta][c][d];if(z>=0)return z;V x{};for(int tau=0;tau<12;tau++)x=add(x,rt[md(delta*tau+4*(K[q][O[tau]][d]-K[q][O[tau]][c]),12)]);z=(x==V{});return z;};
   A row;row.fill(-1);row[0]=0;
   auto dfs=[&](auto&&self,int used,int depth)->bool{
    nodes++;if(depth==12){savedchoice=row;return true;}int chosen=-1,best=13,opts=0;
    for(int r=1;r<12;r++)if(row[r]<0){int bits=0;for(int c=0;c<12;c++)if(!(used>>c&1)){
      bool yes=true;for(int s=0;s<12;s++)if(row[s]>=0&&!good(md(r-s,12),row[s],c)){yes=false;break;}if(yes)bits|=1<<c;}
     int count=__builtin_popcount((unsigned)bits);if(count<best){best=count;chosen=r;opts=bits;}if(!count)return false;}
    while(opts){int c=__builtin_ctz((unsigned)opts);opts&=opts-1;row[chosen]=c;if(self(self,used|(1<<c),depth+1))return true;row[chosen]=-1;}return false;};
   if(dfs(dfs,1,1)){found=true;cls=q;savedorder=O;break;}
   if((orders&8191)==0&&std::chrono::duration<double>(std::chrono::steady_clock::now()-start).count()>60){timed=true;break;}
  }while(std::next_permutation(od.begin(),od.end()));if(found||timed)break;std::sort(od.begin(),od.end());}while(std::next_permutation(ev.begin(),ev.end()));
 }
 std::ofstream j("frontier-20261028-bh12-3-even-counterexample-v1.json");j<<"{\n \"classes\":2, \"halves_examined\":"<<halves<<", \"matching_halves_examined\":"<<matching<<", \"orders_examined\":"<<orders<<", \"nodes\":"<<nodes<<", \"found\":"<<(found?"true":"false")<<", \"timed_out\":"<<(timed?"true":"false");
 if(found){j<<", \"class_zero_based\":"<<cls<<", \"source_order\":[";for(int i=0;i<12;i++){if(i)j<<',';j<<savedorder[i];}j<<"], \"column_per_row\":[";for(int i=0;i<12;i++){if(i)j<<',';j<<savedchoice[i];}j<<"]";}j<<"\n}\n";
 std::cout<<"halves="<<halves<<" matching="<<matching<<" orders="<<orders<<" nodes="<<nodes<<" found="<<found<<" timeout="<<timed<<'\n';
}
