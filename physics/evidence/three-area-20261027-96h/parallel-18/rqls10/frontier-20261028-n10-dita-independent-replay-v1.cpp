// Independent 10! / source-pair orientation replay of all Diţă Fourier T branches.
// Same-block orthogonality via signed counts of fifth roots, not the producer's
// zeta10 polynomial. Cross rank/norm via p=41; rank3 zero witnesses via
// exact Z[zeta5]/(1+x+x2+x3+x4) determinants.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using V=std::array<int64_t,4>;
V roots[5];int modp=41,positions[10],pairs[5][2],f[5],g[5];bool good[10][5];
uint64_t orders=0,fc=0,fg=0,rank5=0,norm4=0,zero3=0,unresolved=0;
std::ofstream out("frontier-20261028-n10-dita-independent-replay-v1.jsonl");
int mod(int a,int n){a%=n;return a<0?a+n:a;}
int mpow(int a,int n){int x=1;while(n){if(n&1)x=x*a%modp;a=a*a%modp;n>>=1;}return x;}
V add(V a,V b){for(int i=0;i<4;i++)a[i]+=b[i];return a;}
V neg(V a){for(auto&x:a)x=-x;return a;}
V mul(V a,V b){int64_t c[7]={};for(int i=0;i<4;i++)for(int j=0;j<4;j++)c[i+j]+=a[i]*b[j];for(int i=6;i>=4;i--){int64_t q=c[i];for(int j=1;j<=4;j++)c[i-j]-=q;}return V{c[0],c[1],c[2],c[3]};}
V determinant(std::vector<std::vector<V>> A){int n=A.size();std::vector<int>v(n);for(int i=0;i<n;i++)v[i]=i;V sum{};
 do{V x{1,0,0,0};int inv=0;for(int i=0;i<n;i++){x=mul(x,A[i][v[i]]);for(int j=0;j<i;j++)inv+=v[j]>v[i];}sum=add(sum,inv%2?neg(x):x);}while(std::next_permutation(v.begin(),v.end()));return sum;}
int determinant_mod(std::vector<std::vector<int>> A){int n=A.size(),v=1;for(int i=0;i<n;i++){int j=i;while(j<n&&!A[j][i])j++;if(j==n)return 0;if(j!=i){std::swap(A[j],A[i]);v=mod(-v,modp);}int a=A[i][i];v=v*a%modp;int inv=mpow(a,modp-2);for(int k=i+1;k<n;k++){int q=A[k][i]*inv%modp;for(int l=i;l<n;l++)A[k][l]=mod(A[k][l]-q*A[i][l],modp);}}return v;}
int zr(int exp,int root){return mpow(root,mod(exp,10));}
int blockrank(int M[25][5],std::vector<int>&rows,std::vector<int>&cols){int basis[5][5]={{}};bool used[5]={};
 for(int r=0;r<25;r++){int v[5];for(int j=0;j<5;j++)v[j]=M[r][j];for(int j=0;j<5;j++)if(v[j]){
  if(used[j]){int a=v[j];for(int k=j;k<5;k++)v[k]=mod(v[k]-a*basis[j][k],modp);}
  else{int a=mpow(v[j],modp-2);for(int k=j;k<5;k++)basis[j][k]=v[k]*a%modp;used[j]=true;rows.push_back(r);cols.push_back(j);break;}}
  if(rows.size()==5)return 5;
 }return rows.size();}
void certify(){fg++;int M[25][5],B[25][5];V E[25][5];
 for(int b=0;b<5;b++)for(int c=0;c<5;c++)for(int t=0;t<5;t++){
  int h=5*b+c,d=mod(g[c]-f[b],10),k=mod(c-b,5),u=d*pairs[t][0]+2*t*k,v=d*pairs[t][1]+2*t*k;
  M[h][t]=mod(zr(u,4)-zr(v,4),modp);B[h][t]=mod(zr(-u,4)-zr(-v,4),modp);
  int u5=mod(3*d*pairs[t][0]+t*k,5),v5=mod(3*d*pairs[t][1]+t*k,5);
  V x=(d*pairs[t][0])%2?neg(roots[u5]):roots[u5],y=(d*pairs[t][1])%2?neg(roots[v5]):roots[v5];E[h][t]=add(x,neg(y));
 }
 std::vector<int>rs,cs;int k=blockrank(M,rs,cs);if(k==5){rank5++;return;}
 std::vector<int>free;for(int j=0;j<5;j++)if(std::find(cs.begin(),cs.end(),j)==cs.end())free.push_back(j);
 bool ok=false;
 if(k==4){
  std::vector<std::vector<int>> A(k,std::vector<int>(k)),Ab=A;
  for(int i=0;i<k;i++)for(int j=0;j<k;j++){A[i][j]=M[rs[i]][cs[j]];Ab[i][j]=B[rs[i]][cs[j]];}
  int D=determinant_mod(A),Db=determinant_mod(Ab);
  for(int j=0;j<k;j++){auto X=A,Y=Ab;for(int i=0;i<k;i++){X[i][j]=M[rs[i]][free[0]];Y[i][j]=B[rs[i]][free[0]];}if(mod(determinant_mod(X)*determinant_mod(Y)-D*Db,modp)){ok=true;break;}}
  if(ok)norm4++;
 }else if(k==3){
  std::vector<std::vector<V>> A(k,std::vector<V>(k));for(int i=0;i<k;i++)for(int j=0;j<k;j++)A[i][j]=E[rs[i]][cs[j]];
  for(int j=0;j<k;j++){bool zz=true;for(int q:free){auto X=A;for(int i=0;i<k;i++)X[i][j]=E[rs[i]][q];if(determinant(X)!=V{})zz=false;}if(zz){ok=true;break;}}
  if(ok)zero3++;
 }
 if(!ok)unresolved++;
 out<<"{\"pairs\":[";for(int i=0;i<5;i++){if(i)out<<',';out<<'['<<pairs[i][0]<<','<<pairs[i][1]<<']';}out<<"],\"f\":[";for(int i=0;i<5;i++){if(i)out<<',';out<<f[i];}out<<"],\"g\":[";for(int i=0;i<5;i++){if(i)out<<',';out<<g[i];}out<<"],\"rank41\":"<<k<<",\"excluded\":"<<(ok?"true":"false")<<"}\n";
}
bool legal(int a[5]){for(int b=0;b<5;b++)for(int c=b+1;c<5;c++)if(!good[mod(a[c]-a[b],10)][c-b])return false;return true;}
void process(){orders++;
 for(int d=1;d<10;d++)for(int k=1;k<5;k++){
  int a[5]={};for(int t=0;t<5;t++)for(int b=0;b<2;b++){int tau=pairs[t][b];a[mod(3*d*tau+t*k,5)]+=d*tau%2?-1:1;}
  good[d][k]=(a[1]==a[0]&&a[2]==a[0]&&a[3]==a[0]&&a[4]==a[0]);
 }
 f[0]=0;
 for(int a=1;a<10;a++)for(int b=1;b<10;b++)if(b!=a)for(int c=1;c<10;c++)if(c!=a&&c!=b)for(int d=1;d<10;d++)if(d!=a&&d!=b&&d!=c){
  f[1]=a;f[2]=b;f[3]=c;f[4]=d;if(!legal(f))continue;fc++;int n=0;
  for(int i=0;i<10;i++)if(i!=0&&i!=a&&i!=b&&i!=c&&i!=d)g[n++]=i;
  do{if(legal(g))certify();}while(std::next_permutation(g,g+5));
 }
}
int main(){roots[0]={1,0,0,0};for(int i=1;i<5;i++){auto[a,b,c,d]=roots[i-1];roots[i]=V{-d,a-d,b-d,c-d};}
 std::array<int,9>O{1,2,3,4,5,6,7,8,9};
 do{positions[0]=0;for(int i=0;i<9;i++)positions[O[i]]=i+1;bool canonical=true;for(int t=1;t<5;t++)if(positions[t]>positions[t+5])canonical=false;if(!canonical)continue;
  for(int t=0;t<5;t++){pairs[t][0]=positions[t];pairs[t][1]=positions[t+5];}process();
 }while(std::next_permutation(O.begin(),O.end()));out.close();
 std::ofstream j("frontier-20261028-n10-dita-independent-replay-v1.json");j<<"{\n \"orders\":"<<orders<<", \"first_block_configs\":"<<fc<<", \"two_block_configs\":"<<fg<<", \"rank5_mod41\":"<<rank5<<", \"unequal_norm_mod41\":"<<norm4<<", \"exact_zero_rank3\":"<<zero3<<", \"unresolved\":"<<unresolved<<"\n}\n";
 std::cout<<"orders="<<orders<<" f="<<fc<<" fg="<<fg<<" rank5="<<rank5<<" norm4="<<norm4<<" zero3="<<zero3<<" unresolved="<<unresolved<<'\n';}
