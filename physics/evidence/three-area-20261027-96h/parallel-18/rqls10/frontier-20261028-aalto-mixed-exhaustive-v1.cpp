#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>
using namespace std;
static int H[10][10],p[10],choice[10],L,Q,degree,powtab[60][16];
static uint16_t adj[10][10];static bool ready[10][10];static long long nodes=0;
static void init_roots(){
 vector<int> f= L==30 ? vector<int>{1,1,0,-1,-1,-1,0,1,1}
                      : vector<int>{1,0,1,0,0,0,-1,0,-1,0,-1,0,0,0,1,0,1};
 degree=int(f.size())-1;
 for(int e=0;e<L;e++){
  array<int,60> a{};a[e]=1;
  for(int j=e;j>=degree;j--){int v=a[j];for(int k=0;k<=degree;k++)a[j-degree+k]-=v*f[k];}
  for(int j=0;j<degree;j++)powtab[e][j]=a[j];
 }
}
static bool orth(int k,int c,int d){
 int acc[16]={};
 for(int t=0;t<10;t++){
  int e=((L/10)*k*t+(L/Q)*(H[p[t]][d]-H[p[t]][c])+L*100)%L;
  for(int j=0;j<degree;j++)acc[j]+=powtab[e][j];
 }
 for(int j=0;j<degree;j++)if(acc[j])return false;
 return true;
}
static uint16_t getadj(int k,int c){
 if(!ready[k][c]){
  ready[k][c]=true;adj[k][c]=0;
  for(int d=0;d<10;d++)if(d!=c&&orth(k,c,d))adj[k][c]|=uint16_t(1u<<d);
 }
 return adj[k][c];
}
static bool dfs(int assigned,uint16_t used,array<uint16_t,10> opts){
 ++nodes;if(assigned==1023)return true;
 int best=-1,small=11;
 for(int r=0;r<10;r++)if(!(assigned&(1<<r))){
  int count=__builtin_popcount(unsigned(opts[r]&~used));
  if(!count)return false;if(count<small){small=count;best=r;}
 }
 uint16_t bits=opts[best]&~used;
 while(bits){
  uint16_t bit=bits&uint16_t(-int(bits));bits^=bit;int c=__builtin_ctz(unsigned(bit));choice[best]=c;
  auto next=opts;
  for(int s=0;s<10;s++)if(s!=best&&!(assigned&(1<<s)))next[s]&=getadj((s-best+10)%10,c);
  if(dfs(assigned|(1<<best),uint16_t(used|bit),next))return true;
 }
 choice[best]=-1;return false;
}
static bool search(bool &empty){
 for(auto &row:ready)fill(begin(row),end(row),false);array<uint16_t,10> opt{};
 for(int r=1;r<10;r++){opt[r]=getadj(r,0)&~uint16_t(1);if(!opt[r]){empty=true;return false;}}
 empty=false;fill(choice,choice+10,-1);choice[0]=0;return dfs(1,1,opt);
}
static void witness(int idx){
 ofstream o("frontier-20261028-aalto-q"+to_string(Q)+"-witness-v1.json");
 o<<"{\"catalog_q\":"<<Q<<",\"modulus\":"<<L<<",\"catalog_index_1based\":"<<idx<<",\"row_order\":[";
 for(int t=0;t<10;t++)o<<(t?",":"")<<p[t];o<<"],\"transversal_columns_by_row\":[";
 for(int t=0;t<10;t++)o<<(t?",":"")<<choice[t];o<<"],\"exponents\":[";
 for(int r=0;r<10;r++){o<<(r?",[":"[");for(int c=0;c<10;c++){o<<(c?",[":"[");
  for(int t=0;t<10;t++)o<<(t?",":"")<<((L/10)*r*t+(L/Q)*H[p[t]][c])%L;o<<"]";}o<<"]";}o<<"]}\n";
}
int main(int argc,char **argv){
 if(argc!=2){cerr<<"usage: program 6|12\n";return 2;}Q=atoi(argv[1]);if(Q!=6&&Q!=12)return 2;
 L=lcm(Q,10);init_roots();string catalog="frontier-20261028-aalto-bh10-"+to_string(Q)+"-catalog-v1.txt";
 ifstream f(catalog);vector<string> lines;string s;while(getline(f,s))lines.push_back(s);
 if(lines.size()!=(Q==6?34u:577u)){cerr<<"bad catalog\n";return 2;}
 ifstream cand("frontier-20261028-aalto-q"+to_string(Q)+"-candidate-halves-v1.txt");
 int idx,aa[5],halves=0;long long total=0,empty_total=0,branched=0;nodes=0;
 while(cand>>idx>>aa[0]>>aa[1]>>aa[2]>>aa[3]>>aa[4]){
  if(idx<1||idx>(int)lines.size()||aa[0]!=0)return 2;s=lines[idx-1];
  if(s.size()!=106||s.substr(0,5)!="BH1::"||int(s[5]-'0')!=Q)return 2;
  for(int t=0;t<10;t++)for(int c=0;c<10;c++){H[t][c]=s[6+10*t+c]-'0';if(H[t][c]<0||H[t][c]>=Q)return 2;}
  array<int,4> even={aa[1],aa[2],aa[3],aa[4]};array<int,5> odd{};int j=0;
  for(int t=0;t<10;t++)if(find(aa,aa+5,t)==aa+5)odd[j++]=t;if(j!=5)return 2;
  long long local=0,local_empty=0;do {auto o=odd;do{
   p[0]=0;for(int v=0;v<4;v++)p[2*v+2]=even[v];for(int v=0;v<5;v++)p[2*v+1]=o[v];
   ++local;++total;bool empty;
   if(search(empty)){witness(idx);cout<<"FOUND TARGET REQUIRES INDEPENDENT CHECK q="<<Q<<" class="<<idx<<"\n";return 0;}
   if(empty){++local_empty;++empty_total;}else ++branched;
  }while(next_permutation(o.begin(),o.end()));}while(next_permutation(even.begin(),even.end()));
  if(local!=2880)return 2;++halves;
  cout<<"q="<<Q<<" class="<<idx<<" half="<<halves<<" cases="<<local<<" empty="<<local_empty<<" total="<<total<<" nodes="<<nodes<<flush<<"\n";
 }
 if(halves!=(Q==6?25:137))return 2;
 cout<<"COMPLETE q="<<Q<<" halves="<<halves<<" orders="<<total<<" root_empty="<<empty_total<<" branched="<<branched<<" nodes="<<nodes<<"; premises and independent replay required\n";
}
