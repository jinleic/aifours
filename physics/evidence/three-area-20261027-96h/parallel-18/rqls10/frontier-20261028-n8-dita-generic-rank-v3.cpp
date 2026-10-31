// General dephased H4(alpha), H4(beta) 2x4 Diţa branch census.
// Same-group equations are affine in alpha or alpha^-1. This program
// distinguishes FREE and the eight zeta8 values; full coverage of constrained
// unit alpha additionally depends on the independent exact h0 screen.
#include <algorithm>
#include <array>
#include <cstdint>
#include <fstream>
#include <iostream>
using A8=std::array<int,8>;using A4=std::array<int,4>;const int P=65521;
int sg[4][4]={{1,1,1,1},{1,1,-1,-1},{1,-1,1,-1},{1,-1,-1,1}};
int ex[4][4]={{0,0,0,0},{0,1,0,1},{0,0,0,0},{0,1,0,1}};
int m8(int x){x%=8;return x<0?x+8:x;}int mp(int x){x%=P;return x<0?x+P:x;}
int powp(int a,int e){int64_t b=a,r=1;while(e){if(e&1)r=r*b%P;b=b*b%P;e>>=1;}return r;}
int h(int t,int b,int k){return m8((sg[t][b]<0?4:0)+k*ex[t][b]);}
bool same(A8 const&O,A4 const&R,A4 const&M,int k){
 for(int b=0;b<4;b++)for(int c=b+1;c<4;c++){
  int z[4]={},d=R[c]-R[b];for(int tau=0;tau<8;tau++){
   int t=M[O[tau]%4],e=m8(d*tau+h(t,c,k)-h(t,b,k));z[e%4]+=(e<4?1:-1);
  }for(int x:z)if(x)return false;
 }return true;
}
// -2 invalid; -1 FREE; 0..7 fixed to zeta8^k.
int classify(A8 const&O,A4 const&R,A4 const&M){
 bool s0=same(O,R,M,0),s4=same(O,R,M,4);if(s0&&s4)return -1;
 int ans=-2;for(int k=0;k<8;k++)if((k==0?s0:k==4?s4:same(O,R,M,k))){if(ans!=-2){std::cerr<<"multiple nonfree values\n";std::exit(2);}ans=k;}return ans;
}
void build(int C[16][4],A8 const&O,A4 const&R0,A4 const&R1,A4 const&M,int a,int b,int root){
 int loc[2][4],pw[8];for(int tau=0;tau<8;tau++)loc[O[tau]/4][O[tau]%4]=tau;for(int t=0;t<8;t++)pw[t]=powp(root,t);
 for(int x=0;x<4;x++)for(int y=0;y<4;y++)for(int t=0;t<4;t++){
  int d=R1[y]-R0[x],off=h(M[t],y,b)-h(t,x,a);
  C[4*x+y][t]=mp(pw[m8(d*loc[0][t]+off)]-pw[m8(d*loc[1][t]+off)]);
 }
}
int rows(int A[16][4],int ids[4]){
 int B[4][4]={{}},pv[4]={},rank=0;
 for(int r=0;r<16;r++){
  int x[4];for(int j=0;j<4;j++)x[j]=A[r][j];
  for(int k=0;k<rank;k++){int v=x[pv[k]];for(int j=0;j<4;j++)x[j]=mp(x[j]-int((int64_t)v*B[k][j]%P));}
  int q=0;while(q<4&&!x[q])q++;if(q==4)continue;
  int iv=powp(x[q],P-2);for(int j=0;j<4;j++)B[rank][j]=int((int64_t)x[j]*iv%P);pv[rank]=q;ids[rank++]=r;if(rank==4)break;
 }return rank;
}
// Signed 3x3 cofactors of one fixed set of pivot rows.
int cof(int A[16][4],int ids[4],int omit){
 int x[3][3],j=0;for(int c=0;c<4;c++)if(c!=omit){for(int r=0;r<3;r++)x[r][j]=A[ids[r]][c];j++;}
 int64_t d=(int64_t)x[0][0]*(int64_t(x[1][1])*x[2][2]-int64_t(x[1][2])*x[2][1])-(int64_t)x[0][1]*(int64_t(x[1][0])*x[2][2]-int64_t(x[1][2])*x[2][0])+(int64_t)x[0][2]*(int64_t(x[1][0])*x[2][1]-int64_t(x[1][1])*x[2][0]);
 return mp(int((omit%2?-d:d)%P));
}
int main(){
 int w=57852,wi=powp(w,P-2);if(powp(w,4)!=P-1)return 2;A8 O={0,1,2,3,4,5,6,7};A4 id={0,1,2,3};
 uint64_t orders=0,h0=0,both=0,ff=0,fx=0,xf=0,xx=0,rank4=0,norm=0,unresolved=0,freefull=0,freenorm=0,freeunresolved=0;
 std::ofstream out("frontier-20261028-n8-dita-generic-rank-unresolved-v3.jsonl");std::ofstream freeout("frontier-20261028-n8-dita-freefree-branches-v1.jsonl");
 do{orders++;
  for(int x=1;x<8;x++)for(int y=1;y<8;y++)for(int z=1;z<8;z++)if(x!=y&&x!=z&&y!=z){
   A4 R0={0,x,y,z};int a=classify(O,R0,id);if(a==-2)continue;h0++;
   A4 R1;int j=0;for(int t=1;t<8;t++)if(t!=x&&t!=y&&t!=z)R1[j++]=t;
   do{A4 M={0,1,2,3};do{
    int b=classify(O,R1,M);if(b==-2)continue;both++;
    if(a==-1&&b==-1){ff++;freeout<<"{\"O\":[";for(int t=0;t<8;t++){if(t)freeout<<',';freeout<<O[t];}freeout<<"],\"R0\":[";for(int t=0;t<4;t++){if(t)freeout<<',';freeout<<R0[t];}freeout<<"],\"R1\":[";for(int t=0;t<4;t++){if(t)freeout<<',';freeout<<R1[t];}freeout<<"],\"mu\":[";for(int t=0;t<4;t++){if(t)freeout<<',';freeout<<M[t];}freeout<<"]}\n";continue;}
    int mode=0;if(a==-1){fx++;mode=1;}else if(b==-1){xf++;mode=2;}else xx++;
    int aa=(a==-1?0:a),bb=(b==-1?0:b);
    auto mask=[mode](int Q[16][4]){for(int row=0;row<16;row++)if((mode==1&&((row/4)%2))||(mode==2&&(row%2)))for(int t=0;t<4;t++)Q[row][t]=0;};
    int C[16][4],ids[4];build(C,O,R0,R1,M,aa,bb,w);mask(C);int r=rows(C,ids);if(r==4){rank4++;if(mode)freefull++;continue;}
    bool reject=false;if(r==3){int Cb[16][4];build(Cb,O,R0,R1,M,aa,bb,wi);mask(Cb);int v0=int((int64_t)cof(C,ids,0)*cof(Cb,ids,0)%P);for(int t=1;t<4;t++)if(int((int64_t)cof(C,ids,t)*cof(Cb,ids,t)%P)!=v0)reject=true;}
    if(reject){norm++;if(mode)freenorm++;continue;}unresolved++;if(mode)freeunresolved++;
    out<<"{\"O\":[";for(int t=0;t<8;t++){if(t)out<<',';out<<O[t];}out<<"],\"R0\":[";for(int t=0;t<4;t++){if(t)out<<',';out<<R0[t];}out<<"],\"R1\":[";for(int t=0;t<4;t++){if(t)out<<',';out<<R1[t];}out<<"],\"mu\":[";for(int t=0;t<4;t++){if(t)out<<',';out<<M[t];}out<<"],\"alpha\":"<<a<<",\"beta\":"<<b<<",\"modrank\":"<<r<<"}\n";
   }while(std::next_permutation(M.begin()+1,M.end()));}while(std::next_permutation(R1.begin(),R1.end()));
  }
 }while(std::next_permutation(O.begin()+1,O.end()));
 std::ofstream j("frontier-20261028-n8-dita-generic-rank-v3.json");
 j<<"{\n \"orders\":"<<orders<<",\"h0\":"<<h0<<",\"both\":"<<both<<",\"free_free\":"<<ff<<",\"free_fixed\":"<<fx<<",\"fixed_free\":"<<xf<<",\"fixed_fixed\":"<<xx<<",\"rank4\":"<<rank4<<",\"norm_reject\":"<<norm<<",\"unresolved\":"<<unresolved<<",\"free_rank4\":"<<freefull<<",\"free_norm_reject\":"<<freenorm<<",\"free_unresolved\":"<<freeunresolved<<"\n}\n";
 std::cout<<"orders "<<orders<<" h0 "<<h0<<" both "<<both<<" FF "<<ff<<" FX "<<fx<<" XF "<<xf<<" XX "<<xx<<" rank4 "<<rank4<<" norm "<<norm<<" unresolved "<<unresolved<<"\n";
}
