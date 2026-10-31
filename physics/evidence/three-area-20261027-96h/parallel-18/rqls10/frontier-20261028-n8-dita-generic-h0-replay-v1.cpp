// Independent exact Z[zeta8] replay of ALL normalized h0 same-group equations.
// Alpha free iff all linear equations vanish; otherwise alpha=-X/Y and
// equality/unit conditions are checked by exact multiplication/conjugation.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
using V=std::array<int64_t,4>;using A8=std::array<int,8>;using A4=std::array<int,4>;
int sg[4][4]={{1,1,1,1},{1,1,-1,-1},{1,-1,1,-1},{1,-1,-1,1}};
int ex[4][4]={{0,0,0,0},{0,1,0,1},{0,0,0,0},{0,1,0,1}};
int mod8(int x){x%=8;return x<0?x+8:x;}
V add(V a,V b){for(int i=0;i<4;i++)a[i]+=b[i];return a;}
V neg(V a){for(auto &x:a)x=-x;return a;}
V rt(int k){k=mod8(k);V r{};r[k%4]=k<4?1:-1;return r;}
V cj(V a){return V{a[0],-a[3],-a[2],-a[1]};}
V mul(V a,V b){return V{a[0]*b[0]-a[1]*b[3]-a[2]*b[2]-a[3]*b[1],a[0]*b[1]+a[1]*b[0]-a[2]*b[3]-a[3]*b[2],a[0]*b[2]+a[1]*b[1]+a[2]*b[0]-a[3]*b[3],a[0]*b[3]+a[1]*b[2]+a[2]*b[1]+a[3]*b[0]};}
int main(){A8 O={0,1,2,3,4,5,6,7};uint64_t orders=0,free=0,roots[8]={},nonroot=0,valid=0;
 do{orders++;
  for(int x=1;x<8;x++)for(int y=1;y<8;y++)for(int z=1;z<8;z++)if(x!=y&&x!=z&&y!=z){
   A4 R={0,x,y,z};V num{},den{};bool has=false,ok=true;
   for(int b=0;b<4&&ok;b++)for(int c=b+1;c<4&&ok;c++){
    V sums[3]{};int d=R[c]-R[b];
    for(int tau=0;tau<8;tau++){
     int t=O[tau]%4,e=ex[t][c]-ex[t][b];V a=rt(d*tau);
     if(sg[t][b]*sg[t][c]<0)a=neg(a);sums[e+1]=add(sums[e+1],a);
    }
    V X,Y;if(sums[0]!=V{}){X=sums[0];Y=sums[1];}else{X=sums[1];Y=sums[2];}
    if(X==V{}&&Y==V{})continue;
    if(X==V{}||Y==V{}||mul(X,cj(X))!=mul(Y,cj(Y))){ok=false;break;}
    V n=neg(X),d0=Y;if(!has){num=n;den=d0;has=true;}else if(mul(num,d0)!=mul(n,den)){ok=false;break;}
   }
   if(!ok)continue;valid++;
   if(!has){free++;continue;}
   int k=0;while(k<8&&num!=mul(rt(k),den))k++;
   if(k==8)nonroot++;else roots[k]++;
  }
 }while(std::next_permutation(O.begin()+1,O.end()));
 std::ofstream o("frontier-20261028-n8-dita-generic-h0-replay-v1.json");
 o<<"{\n \"orders\":"<<orders<<", \"assignments_each\":210, \"valid\":"<<valid<<", \"free\":"<<free<<", \"nonroot\":"<<nonroot<<", \"root8_counts\":[";
 for(int k=0;k<8;k++){if(k)o<<',';o<<roots[k];}o<<"]\n}\n";
 std::cout<<"orders "<<orders<<" valid "<<valid<<" free "<<free<<" nonroot "<<nonroot<<" rootcounts";for(auto v:roots)std::cout<<' '<<v;std::cout<<'\n';
}
