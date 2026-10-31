// Exhaustive normalized 2x4 Diţa n8 SAME-GROUP caller, followed by a
// rank-4 certificate over F_65521 for the 16x4 cross-phase equations.
// Delta_t are arbitrary nonzero complex values, NOT restricted to roots.
// A modular full-rank result is an exact lower bound on Q(zeta8) rank;
// singular reductions are retained and need exact field/kernel analysis.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
#include <vector>
using A8=std::array<int,8>;using A4=std::array<int,4>;const int P=65521;
int mpow(int a,int e){int64_t r=1,b=a;while(e){if(e&1)r=r*b%P;b=b*b%P;e>>=1;}return int(r);}
int mod(int x){x%=P;return x<0?x+P:x;}
int mod8(int x){x%=8;return x<0?x+8:x;}
bool same(A8 const&O,A4 const&R,A4 const&M){
 for(int b=0;b<4;b++)for(int c=b+1;c<4;c++){
  int v[4]={};int delta=R[c]-R[b];
  for(int tau=0;tau<8;tau++){int t=O[tau]%4,e=mod8(delta*tau+2*(c-b)*M[t]);v[e%4]+=(e<4?1:-1);}
  for(int x:v)if(x)return false;
 }
 return true;
}
int rank4(int C[16][4]){
 int row=0;
 for(int col=0;col<4;col++){
  int p=row;while(p<16&&!C[p][col])p++;
  if(p==16)continue;
  for(int j=0;j<4;j++)std::swap(C[p][j],C[row][j]);
  int inv=mpow(C[row][col],P-2);
  for(int j=col;j<4;j++)C[row][j]=int((int64_t)C[row][j]*inv%P);
  for(int i=row+1;i<16;i++)if(C[i][col]){int f=C[i][col];for(int j=col;j<4;j++)C[i][j]=mod(C[i][j]-int((int64_t)f*C[row][j]%P));}
  row++;
 }
 return row;
}
int main(){
 int w=0;for(int a=2;a<P&&!w;a++){int q=mpow(a,(P-1)/8);if(mpow(q,4)==P-1)w=q;}
 if(!w)return 2;int pw[8];for(int j=0;j<8;j++)pw[j]=mpow(w,j);
 A8 O={0,1,2,3,4,5,6,7};A4 id={0,1,2,3};
 uint64_t orderings=0,h0=0,sameboth=0,full=0,singular=0;uint64_t rankhist[5]={};
 std::ofstream out("frontier-20261028-n8-dita-allphase-singular-v1.jsonl");
 do{
  orderings++;int loc[2][4];for(int tau=0;tau<8;tau++)loc[O[tau]/4][O[tau]%4]=tau;
  for(int x=1;x<8;x++)for(int y=1;y<8;y++)for(int z=1;z<8;z++)if(x!=y&&x!=z&&y!=z){
   A4 R0={0,x,y,z};if(!same(O,R0,id))continue;h0++;
   A4 R1;int j=0;for(int r=0;r<8;r++)if(r!=0&&r!=x&&r!=y&&r!=z)R1[j++]=r;
   do{
    A4 M={0,1,2,3};do{
     if(!same(O,R1,M))continue;sameboth++;
     int C[16][4];for(int b=0;b<4;b++)for(int c=0;c<4;c++)for(int t=0;t<4;t++){
      int de=R1[c]-R0[b];int a=mod8(de*loc[0][t]+2*(M[t]*c-t*b));
      int bb=mod8(de*loc[1][t]+2*(M[t]*c-t*b));C[4*b+c][t]=mod(pw[a]-pw[bb]);
     }
     int rank=rank4(C);rankhist[rank]++;
     if(rank==4)full++;else{singular++;
      out<<"{\"O\":[";for(int i=0;i<8;i++){if(i)out<<',';out<<O[i];}out<<"],\"R0\":[";for(int i=0;i<4;i++){if(i)out<<',';out<<R0[i];}
      out<<"],\"R1\":[";for(int i=0;i<4;i++){if(i)out<<',';out<<R1[i];}out<<"],\"mu\":[";for(int i=0;i<4;i++){if(i)out<<',';out<<M[i];}out<<"],\"modrank\":"<<rank<<"}\n";
     }
    }while(std::next_permutation(M.begin()+1,M.end()));
   }while(std::next_permutation(R1.begin(),R1.end()));
  }
 }while(std::next_permutation(O.begin()+1,O.end()));
 std::ofstream j("frontier-20261028-n8-dita-allphase-rank-v1.json");
 j<<"{\n \"prime\":"<<P<<", \"root8_mod_prime\":"<<w<<", \"source_orderings\":"<<orderings<<", \"same_h0\":"<<h0<<", \"same_both\":"<<sameboth<<", \"full_rank\":"<<full<<", \"singular\":"<<singular<<", \"rank_histogram\":[";
 for(int k=0;k<5;k++){if(k)j<<',';j<<rankhist[k];}j<<"]\n}\n";
 std::cout<<"p="<<P<<" w="<<w<<" O="<<orderings<<" h0="<<h0<<" both="<<sameboth<<" full="<<full<<" singular="<<singular<<" ranks=";for(int i=0;i<5;i++)std::cout<<rankhist[i]<<' ';std::cout<<'\n';
}
