// Independent complete replay of BH(8,16) cyclic-Fourier T search.
// Distinct method: tensor basis Q(zeta8) + zeta16 Q(zeta8), subset-DP
// perfect matching and fixed-row DFS. No max-ray or phase ansatz.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using M=std::array<std::array<int,8>,8>;using A=std::array<int,8>;
int md(int x,int n){x%=n;return x<0?x+n:x;}
bool zero(int const*x,int n){int q[2][4]={{}};for(int i=0;i<n;i++){int e=md(x[i],16),part=e%2,k=e/2;q[part][k%4]+=k<4?1:-1;}for(auto &a:q)for(int v:a)if(v)return false;return true;}
bool isH(M const&H){int x[8];for(int a=0;a<8;a++)for(int b=a+1;b<8;b++){
 for(int j=0;j<8;j++)x[j]=H[j][b]-H[j][a];if(!zero(x,8))return false;
 for(int j=0;j<8;j++)x[j]=H[b][j]-H[a][j];if(!zero(x,8))return false;
 }return true;}
bool pmatch(int const*g){bool D[256]={};D[0]=true;for(int m=1;m<256;m++)if(!(__builtin_popcount((unsigned)m)&1)){
 int a=__builtin_ctz((unsigned)m),rest=m&~(1<<a),bset=g[a]&rest;while(bset){int b=__builtin_ctz((unsigned)bset);bset&=bset-1;if(D[rest&~(1<<b)]){D[m]=true;break;}}}return D[255];}
int main(){std::ifstream f("frontier-20261028-aalto-bh8-16-catalog-v1.txt");std::vector<M>H;std::string line;
 while(std::getline(f,line)){if(line.empty())continue;if(line.size()!=70||line.substr(0,6)!="BH188@")return 2;M a;for(int r=0;r<8;r++)for(int c=0;c<8;c++){a[r][c]=line[6+8*r+c]-'0';if(a[r][c]<0||a[r][c]>15)return 3;}if(!isH(a))return 4;H.push_back(a);}if(H.size()!=2807)return 5;
 uint64_t halves=0,matching=0,orders=0,nodes=0;bool found=false;int cls=-1;A savedorder{},savedchoice{};
 for(int k=0;k<2807&&!found;k++)for(int mask=1;mask<256&&!found;mask+=2)if(__builtin_popcount((unsigned)mask)==4){
  halves++;int graph[8]={},q[4];for(int c=0;c<8;c++)for(int d=c+1;d<8;d++){
   int z=0;for(int r=0;r<8;r++)if(mask>>r&1)q[z++]=H[k][r][d]-H[k][r][c];if(zero(q,4)){graph[c]|=1<<d;graph[d]|=1<<c;}}
  if(!pmatch(graph))continue;matching++;std::vector<int>ev,od;for(int r=1;r<8;r++)((mask>>r&1)?ev:od).push_back(r);
  do{do{
   A ord{};ord[0]=0;for(int i=0;i<3;i++)ord[2*i+2]=ev[i];for(int i=0;i<4;i++)ord[2*i+1]=od[i];orders++;
   bool good[8][8][8]={};int x[8];for(int d=1;d<8;d++)for(int a=0;a<8;a++)for(int b=0;b<8;b++)if(a!=b){
    for(int t=0;t<8;t++)x[t]=2*d*t+H[k][ord[t]][b]-H[k][ord[t]][a];good[d][a][b]=zero(x,8);}
   A chosen;chosen.fill(-1);chosen[0]=0;
   auto dfs=[&](auto&&self,int r,int used)->bool{
    nodes++;if(r==8){savedchoice=chosen;return true;}
    for(int c=0;c<8;c++)if(!(used>>c&1)){
     bool yes=true;for(int s=0;s<r;s++)if(!good[md(r-s,8)][chosen[s]][c]){yes=false;break;}
     if(yes){chosen[r]=c;if(self(self,r+1,used|(1<<c)))return true;chosen[r]=-1;}
    }return false;};
   if(dfs(dfs,1,1)){found=true;cls=k;savedorder=ord;break;}
  }while(std::next_permutation(od.begin(),od.end()));if(found)break;std::sort(od.begin(),od.end());}while(std::next_permutation(ev.begin(),ev.end()));
 }
 std::ofstream out("frontier-20261028-bh8-16-independent-replay-v1.json");out<<"{\n \"classes\":"<<H.size()<<", \"halves\":"<<halves<<", \"matching\":"<<matching<<", \"orders\":"<<orders<<", \"fixed_dfs_nodes\":"<<nodes<<", \"found\":"<<(found?"true":"false");
 if(found){out<<", \"class_zero_based\":"<<cls<<", \"source_order\":[";for(int i=0;i<8;i++){if(i)out<<',';out<<savedorder[i];}out<<"], \"column_per_row\":[";for(int i=0;i<8;i++){if(i)out<<',';out<<savedchoice[i];}out<<"]";}out<<"\n}\n";
 std::cout<<"classes="<<H.size()<<" halves="<<halves<<" matching="<<matching<<" orders="<<orders<<" nodes="<<nodes<<" found="<<found<<'\n';
}
