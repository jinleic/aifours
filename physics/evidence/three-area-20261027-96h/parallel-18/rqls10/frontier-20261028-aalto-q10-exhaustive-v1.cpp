#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;
static int H[10][10],p[10],choice[10];
static uint16_t adj[10][10];
static long long nodes=0;
static bool zero10(const array<int,10>&cnt){
 int v[5];for(int j=0;j<5;j++)v[j]=cnt[j]-cnt[j+5];
 return v[0]==-v[1]&&v[0]==v[2]&&v[0]==-v[3]&&v[0]==v[4];
}
static bool duplicate(){
 for(int c=0;c<10;c++)for(int d=c+1;d<10;d++)for(int m=0;m<10;m++){
  int first=(H[p[0]][d]-H[p[0]][c]+100)%10;bool ok=true;
  for(int t=1;t<10;t++)if((H[p[t]][d]-H[p[t]][c]-m*t+1000)%10!=first){ok=false;break;}
  if(ok)return true;
 }
 return false;
}
static void build(){
 for(int k=1;k<10;k++)for(int c=0;c<10;c++){
  adj[k][c]=0;
  for(int d=0;d<10;d++)if(c!=d){
   array<int,10> cnt{};
   for(int t=0;t<10;t++)cnt[(k*t+H[p[t]][d]-H[p[t]][c]+1000)%10]++;
   if(zero10(cnt))adj[k][c]|=uint16_t(1u<<d);
  }
 }
}
static bool dfs(int assigned,uint16_t used,array<uint16_t,10> opts){
 ++nodes;if(assigned==1023)return true;
 int best=-1,small=11;
 for(int r=0;r<10;r++)if(!(assigned&(1<<r))){
  int count=__builtin_popcount(unsigned(opts[r]&~used));
  if(count==0)return false;
  if(count<small){small=count;best=r;}
 }
 uint16_t choices=opts[best]&~used;
 while(choices){
  uint16_t bit=choices&uint16_t(-int(choices));choices^=bit;
  int col=__builtin_ctz(unsigned(bit));choice[best]=col;
  auto next=opts;
  for(int s=0;s<10;s++)if(s!=best&&!(assigned&(1<<s)))next[s]&=adj[(s-best+10)%10][col];
  if(dfs(assigned|(1<<best),uint16_t(used|bit),next))return true;
 }
 choice[best]=-1;return false;
}
static bool transversal(){
 build();array<uint16_t,10> opt{};
 for(int r=1;r<10;r++)opt[r]=adj[r][0]&~uint16_t(1);
 fill(choice,choice+10,-1);choice[0]=0;
 return dfs(1,1,opt);
}
static void save_witness(int idx){
 ofstream out("frontier-20261028-aalto-q10-witness-v1.json");
 out<<"{\"catalog_q\":10,\"catalog_index_1based\":"<<idx<<",\"row_order\":[";
 for(int i=0;i<10;i++)out<<(i?",":"")<<p[i];out<<"],\"transversal_columns_by_row\":[";
 for(int i=0;i<10;i++)out<<(i?",":"")<<choice[i];out<<"],\"exponents\":[";
 for(int r=0;r<10;r++){out<<(r?",[":"[");for(int c=0;c<10;c++){out<<(c?",[":"[");
  for(int t=0;t<10;t++)out<<(t?",":"")<<(r*t+H[p[t]][c])%10;out<<"]";}out<<"]";}out<<"]}\n";
}
int main(){
 ifstream file("frontier-20261028-aalto-bh10-10-catalog-v1.txt");vector<string> lines;string line;
 while(getline(file,line))lines.push_back(line);if(lines.size()!=51){cerr<<"bad catalog count\n";return 2;}
 for(int idx:{1,9,18}){
  line=lines[idx-1];if(line.size()!=106||line.substr(0,6)!="BH1:::"){cerr<<"bad input\n";return 2;}
  for(int t=0;t<10;t++)for(int c=0;c<10;c++){H[t][c]=line[6+10*t+c]-'0';if(H[t][c]<0||H[t][c]>=10)return 2;}
  array<int,4> even={2,3,5,7};long long cases=0,dups=0,checked=0;nodes=0;
  do {array<int,5> odd={1,4,6,8,9};do {
    p[0]=0;for(int j=0;j<4;j++)p[2*j+2]=even[j];for(int j=0;j<5;j++)p[2*j+1]=odd[j];
    ++cases;if(duplicate()){++dups;continue;}++checked;
    if(transversal()){
     save_witness(idx);cout<<"FOUND target-needs-independent-check class="<<idx<<" cases="<<cases<<" nodes="<<nodes<<"\n";return 0;
    }
   }while(next_permutation(odd.begin(),odd.end()));}while(next_permutation(even.begin(),even.end()));
  cout<<"class="<<idx<<" cases="<<cases<<" duplicates="<<dups<<" checked="<<checked<<" dfs_nodes="<<nodes<<" no_transversal_on_checked\n";
 }
 cout<<"EXHAUSTIVE normalized q10 three-class candidate search complete; catalog/orbit/halfgraph premises require review\n";
}
