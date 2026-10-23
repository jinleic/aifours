// For run data with k >= kmin at length N: count data with R >= 2p-2 lacking an "FW pattern":
// P with m(P) <= (p+1)/2 <= m(P)+h(P) and E+(P), E-(P) >= p-1.  Also report whether any full window exists.
#include <cstdio>
#include <cstdlib>
#include <algorithm>
static int p,N,kmin,kmax,inherit,consttype,K; static int r[64],l[64],a[64],b[64];
static long long cntA[64], noFW[64], noFull[64], printed=0;
static bool inherited(){int R=0,F=0,H=0,fr=0;for(int i=0;i<K;i++){R+=a[i]+b[i];F+=l[i];H+=l[i]/2;fr+=(a[i]+b[i])/2;if(a[i]>p-1||b[i]>p-1)return false;}
 return R<=3*p-2&&F+fr<=3*p-2&&R+H<=3*p-2&&H<=p-1;}
static void proc(){ if(inherit&&!inherited())return; int R=0; for(int i=0;i<K;i++)R+=a[i]+b[i]; if(R<2*p-2) return; cntA[K]++;
 bool fw=false, full=false; int np=1<<(K-1);
 for(int P=0;P<np&&!(fw&&full);P++){ int f2=0,h=0,Ep=0; for(int j=0;j<K;j++){int zj=(P>>j)&1,zn=(P>>((j+1)%K))&1,f=zj!=zn; f2+=f; h+=(l[j]-f)/2; Ep+=zj?a[j]:b[j];}
  int m=f2/2, Em=R-Ep; int M=(p+1)/2;
  if(m<=M && M<=m+h && Ep>=p-1 && Em>=p-1) fw=true;
  auto g=[&](int E){return std::min(p-m,std::min(E+m+h-p,E/2));};
  if(g(Ep)+g(Em)+1>=p) full=true; }
 if(!fw){ noFW[K]++; if(printed<20){printed++; printf("{\"noFW\":1,\"full\":%d,\"a\":[",full?1:0); for(int i=0;i<K;i++)printf("%s%d",i?",":"",a[i]); printf("],\"b\":["); for(int i=0;i<K;i++)printf("%s%d",i?",":"",b[i]); printf("],\"l\":["); for(int i=0;i<K;i++)printf("%s%d",i?",":"",l[i]); printf("]}\n");} }
 if(!full) noFull[K]++; }
static void splits(int i){ if(i==K){proc();return;} if(consttype){a[i]=r[i];b[i]=0;splits(i+1);return;} for(int x=0;x<=r[i];x++){a[i]=x;b[i]=r[i]-x; if(i==K-1){int c=0;for(int t=0;t<K&&!c;t++) if(a[t]!=b[t]) c=a[t]>b[t]?1:-1; if(c<0) continue;} splits(i+1);} }
static bool rot_min(){ for(int s=1;s<K;s++){ for(int t=0;t<K;t++){int i1=t,i2=(t+s)%K; if(r[i2]!=r[i1]){ if(r[i2]<r[i1]) return false; goto nx;} if(l[i2]!=l[i1]){ if(l[i2]<l[i1]) return false; goto nx;} } nx:; } return true; }
static void gen(int pos,int rem){ if(pos==2*K){ if(rem) return; if(!rot_min()) return; splits(0); return;} int left=2*K-pos-1; for(int v=1;v<=rem-left;v++){ if(pos%2==0) r[pos/2]=v; else l[pos/2]=v; gen(pos+1,rem-v);} }
int main(int argc,char**argv){ p=atoi(argv[1]);N=atoi(argv[2]);kmin=atoi(argv[3]);kmax=atoi(argv[4]);consttype=atoi(argv[5]);inherit=atoi(argv[6]);
 for(K=kmin;K<=kmax&&2*K<=N;K++){ gen(0,N); printf("{\"k\":%d,\"regimeA\":%lld,\"noFW\":%lld,\"noFull\":%lld}\n",K,cntA[K],noFW[K],noFull[K]); fflush(stdout);} }
