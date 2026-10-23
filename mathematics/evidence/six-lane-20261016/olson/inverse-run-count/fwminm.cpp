// For merged-type data (b=0, all l odd, 2p-2<=R<=3p-2, 1<=kappa<=o-1), report min m of a full window
// and print data where no full window has m<=1 (aid only).
#include <cstdio>
#include <cstdlib>
#include <algorithm>
static int p,N,K; static int r[64],l[64]; static long long hist[64][64]; static int printed=0;
static void proc(){ int R=0,H=0; for(int i=0;i<K;i++){ if(l[i]%2==0) return; R+=r[i]; H+=l[i]/2; }
 if(R<2*p-2||R>3*p-2) return; int kap=p-1-H; if(kap<1||kap>K-1) return;
 int best=99; int np=1<<K;
 for(int P=1;P<np-1;P++){ int f2=0,Ep=0; for(int j=0;j<K;j++){int zj=(P>>j)&1,zn=(P>>((j+1)%K))&1; f2+=(zj!=zn); if(zj)Ep+=r[j];}
  int m=f2/2,Em=R-Ep; auto g=[&](int E){return std::min(p-m,std::min(E+m-kap-1,E/2));};
  if(g(Ep)+g(Em)+1>=p) best=std::min(best,m); }
 hist[K][best==99?0:best]++;
 if(best>1&&printed<12){printed++; printf("minm=%d k=%d R=%d kappa=%d r=[",best,K,R,kap); for(int i=0;i<K;i++)printf("%s%d",i?",":"",r[i]); printf("] l=["); for(int i=0;i<K;i++)printf("%s%d",i?",":"",l[i]); printf("]\n");} }
static bool rot_min(){ for(int s=1;s<K;s++){ for(int t=0;t<K;t++){int i1=t,i2=(t+s)%K; if(r[i2]!=r[i1]){ if(r[i2]<r[i1]) return false; goto nx;} if(l[i2]!=l[i1]){ if(l[i2]<l[i1]) return false; goto nx;} } nx:; } return true; }
static void gen(int pos,int rem){ if(pos==2*K){ if(rem) return; if(!rot_min()) return; proc(); return;} int left=2*K-pos-1; for(int v=1;v<=rem-left;v++){ if(pos%2==0) r[pos/2]=v; else l[pos/2]=v; gen(pos+1,rem-v);} }
int main(int argc,char**argv){ p=atoi(argv[1]); N=4*p-2; int kmax=atoi(argv[2]);
 for(K=2;K<=kmax;K++){ gen(0,N); printf("k=%d:",K); for(int m=0;m<=K;m++) if(hist[K][m]) printf(" m%d:%lld",m,hist[K][m]); printf("\n"); fflush(stdout);} }
