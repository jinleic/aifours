// Inherited data with A = 2p-1, B >= 1 (all splits up to a<->b): histogram of the minimal m of a
// full window, and whether some full window has an FW shape (m=(p+1)/2, E+-, >= p-1). Aid only.
#include <cstdio>
#include <cstdlib>
#include <algorithm>
static int p,N,K; static int r[64],l[64],a[64],b[64]; static long long hist[64][64], fwcnt[64], tot[64]; static int printed=0;
static bool inherited(){int R=0,F=0,H=0,fr=0;for(int i=0;i<K;i++){R+=a[i]+b[i];F+=l[i];H+=l[i]/2;fr+=(a[i]+b[i])/2;if(a[i]>p-1||b[i]>p-1)return false;}
 return R<=3*p-2&&F+fr<=3*p-2&&R+H<=3*p-2&&H<=p-1;}
static void proc(){ if(!inherited())return; int A=0,B=0; for(int i=0;i<K;i++){A+=a[i];B+=b[i];} if(B<1||A!=2*p-1) return;
 int R=A+B; int best=99; bool fw=false; int np=1<<K;
 for(int P=1;P<np-1;P++){ int f2=0,h=0,Ep=0; for(int j=0;j<K;j++){int zj=(P>>j)&1,zn=(P>>((j+1)%K))&1,f=zj!=zn; f2+=f; h+=(l[j]-f)/2; Ep+=zj?a[j]:b[j];}
  int m=f2/2,Em=R-Ep; auto g=[&](int E){return std::min(p-m,std::min(E+m+h-p,E/2));};
  if(g(Ep)+g(Em)+1>=p){ best=std::min(best,m); if(m==(p+1)/2&&Ep>=p-1&&Em>=p-1) fw=true; } }
 tot[K]++; hist[K][best==99?0:best]++; if(fw) fwcnt[K]++; }
static void splits(int i){ if(i==K){proc();return;} for(int x=0;x<=r[i];x++){a[i]=x;b[i]=r[i]-x; splits(i+1);} }
static bool rot_min(){ for(int s=1;s<K;s++){ for(int t=0;t<K;t++){int i1=t,i2=(t+s)%K; if(r[i2]!=r[i1]){ if(r[i2]<r[i1]) return false; goto nx;} if(l[i2]!=l[i1]){ if(l[i2]<l[i1]) return false; goto nx;} } nx:; } return true; }
static void gen(int pos,int rem){ if(pos==2*K){ if(rem) return; if(!rot_min()) return; splits(0); return;} int left=2*K-pos-1; for(int v=1;v<=rem-left;v++){ if(pos%2==0) r[pos/2]=v; else l[pos/2]=v; gen(pos+1,rem-v);} }
int main(int argc,char**argv){ p=atoi(argv[1]); N=4*p-2; int kmin=atoi(argv[2]), kmax=atoi(argv[3]);
 for(K=kmin;K<=kmax;K++){ gen(0,N); printf("k=%d tot=%lld fw=%lld minm:",K,tot[K],fwcnt[K]); for(int m=0;m<=K;m++) if(hist[K][m]) printf(" m%d:%lld",m,hist[K][m]); printf("\n"); fflush(stdout);} }
