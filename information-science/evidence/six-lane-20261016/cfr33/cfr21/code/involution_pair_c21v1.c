/* Exact seven-row DM solver for s=(mu,(1 2)(3 4)(5 6)), fixing row0, mu^2=1 modn.
 * InfoCFR27Lift, CFR21; independent parametrisation of g00/g10/g16.
 * Normalise row0=0,row1=t. The induced column involution h gives rows
 * [0,t,mu*h(t),g(t),mu*g(h(t)),j(t),mu*j(h(t))].
 * Require h^2=id and d=t-mu*h(t) bijective. For each h enumerate g with
 * g, g-id, g-mu*h, g-mu*g(h) all bijective. A pair g,j extends iff
 * g-j and g-mu*j(h) are bijective. All other pairs follow by s; every
 * output is nevertheless checked directly on all21 row pairs.
 *
 * All odd-order involutions have a fixed column. Translate by one such
 * column, obtaining h0=g0=j0=0. h consists of fixed points and2-cycles;
 * exact DLX covers domain and d values. For each h process only the
 * lex-minimum under unit conjugation u*h(u^-1 t), a valid existence
 * symmetry. g-search is exact MRV over h-orbits and4 permutation masks.
 * Swap g with mu*g(h) within its row pair to retain one lexicographic
 * representative. Compare every new g with all preceding representatives.
 * Deadline, SIGTERM or V-store overflow -> UNKNOWN, never an exclusion.
 * Usage: involution_pair_c21v1 N MU SECONDS first|hcount OUTPREFIX
 * Exclusive OUTPREFIX.dmraw; candidate exit10, exhaustion exit20.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <time.h>
#include <signal.h>
#include <fcntl.h>
#include <unistd.h>
#define MN 31
#define MH 600
#define DN 6000
#define VCAP 500000

typedef struct {uint32_t m[4];uint8_t val[2];} GOpt;
typedef struct {uint8_t size,p[2];uint32_t domain,diff;GOpt *g;int ng,cap;} HOpt;
static HOpt ops[MH];static int nh,n,mu,count_h,found=0,timed_out=0,overflow=0;
static int nunits,unitmul[MN][MN],unitinv[MN][MN],mult[MN],diffval[MN][MN];
static double t0,limit,last;static volatile sig_atomic_t stopped=0;
static int L[DN],R[DN],U[DN],D[DN],C[DN],ROW[DN],S[2*MN+1],dn;
static int chosen[MN],nchosen,h[MN],gval[MN],solg[MN],solj[MN];
static uint8_t *store;static int nv,maxv;
static long long hnodes,gnodes,hcount,hcanonical,vtotal,comparisons;
static const char *prefix;
static int md(int x){x%=n;return x<0?x+n:x;}
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+t.tv_nsec*1e-9;}
static void term(int s){(void)s;stopped=1;}
static int check(void){
 if(stopped||now()-t0>=limit)timed_out=1;
 if(now()-last>=30){last=now();printf("c progress %.1f hcount %lld hcanonical %lld hnodes %lld gnodes %lld vtotal %lld maxV %d comparisons %lld\n",now()-t0,hcount,hcanonical,hnodes,gnodes,vtotal,maxv,comparisons);}
 return timed_out||overflow||found;
}
static int maskof(const int *v,int sz,uint32_t *mask){uint32_t m=0;for(int i=0;i<sz;i++){uint32_t b=1u<<v[i];if(m&b)return 0;m|=b;}*mask=m;return 1;}
static void add_h(int size,int a,int b){
 HOpt x;memset(&x,0,sizeof x);x.size=(uint8_t)size;x.p[0]=(uint8_t)a;x.p[1]=(uint8_t)b;
 int p[2]={a,b},d[2]={md(a-mu*(size==1?a:b)),md(b-mu*a)};
 if(!maskof(p,size,&x.domain)||!maskof(d,size,&x.diff)||(x.domain&1u)||(x.diff&1u))return;
 if(nh>=MH){puts("c H capacity");exit(3);}ops[nh++]=x;
}
static void add_g(HOpt *o,int u,int v){
 GOpt g;memset(&g,0,sizeof g);int val[2]={u,v},m[4][2];
 for(int p=0;p<o->size;p++){
  int t=o->p[p],ht=o->p[(p+1)%o->size];
  g.val[p]=(uint8_t)val[p];m[0][p]=val[p];m[1][p]=md(val[p]-t);m[2][p]=md(val[p]-mu*ht);m[3][p]=md(val[p]-mu*val[(p+1)%o->size]);
 }
 for(int f=0;f<4;f++)if(!maskof(m[f],o->size,&g.m[f])||(g.m[f]&1u))return;
 if(o->ng==o->cap){o->cap=o->cap?o->cap*2:32;o->g=realloc(o->g,sizeof(GOpt)*(size_t)o->cap);if(!o->g){puts("c allocation");exit(3);}}
 o->g[o->ng++]=g;
}
static void build_options(void){
 for(int a=1;a<n;a++)add_h(1,a,0);
 for(int a=1;a<n;a++)for(int b=a+1;b<n;b++)add_h(2,a,b);
 long long total=0;
 if(!count_h)for(int i=0;i<nh;i++){
  HOpt *o=&ops[i];
  if(o->size==1){for(int u=0;u<n;u++)add_g(o,u,0);}
  else for(int u=0;u<n;u++)for(int v=0;v<n;v++)if(u!=v)add_g(o,u,v);
  total+=o->ng;
 }
 printf("c options h %d g %lld\n",nh,total);
}
static void cover(int c){R[L[c]]=R[c];L[R[c]]=L[c];for(int i=D[c];i!=c;i=D[i])for(int j=R[i];j!=i;j=R[j]){D[U[j]]=D[j];U[D[j]]=U[j];S[C[j]]--;}}
static void uncover(int c){for(int i=U[c];i!=c;i=U[i])for(int j=L[i];j!=i;j=L[j]){S[C[j]]++;D[U[j]]=j;U[D[j]]=j;}R[L[c]]=c;L[R[c]]=c;}
static void make_dlx(void){
 int nc=2*n;dn=nc+1;
 for(int c=0;c<=nc;c++){L[c]=c-1;R[c]=c+1;U[c]=D[c]=c;C[c]=c;S[c]=0;}L[0]=nc;R[nc]=0;
 for(int o=0;o<nh;o++){
  int first=-1,prev=-1;
  for(int f=0;f<2;f++){uint32_t mask=f?ops[o].diff:ops[o].domain;
   while(mask){int b=__builtin_ctz(mask);mask&=mask-1;int c=1+f*n+b,j=dn++;
    if(dn>=DN){puts("c DLX capacity");exit(3);}C[j]=c;ROW[j]=o;U[j]=U[c];D[j]=c;D[U[c]]=j;U[c]=j;S[c]++;
    if(first<0)first=j;else{R[prev]=j;L[j]=prev;}prev=j;
   }
  }
  R[prev]=first;L[first]=prev;
 }
 cover(1);cover(1+n);
}
static int canonical_h(void){
 for(int s=0;s<nunits;s++){
  for(int t=0;t<n;t++){int x=unitmul[s][h[unitinv[s][t]]];if(x!=h[t]){if(x<h[t])return 0;break;}}
 }
 return 1;
}
static int compatible(const GOpt *g,const uint32_t *used){for(int f=0;f<4;f++)if(g->m[f]&used[f])return 0;return 1;}
static int orth2(const int *g,const uint8_t *j){
 uint32_t a=0,b=0;
 for(int t=0;t<n;t++){
  int d=diffval[g[t]][j[t]];uint32_t bit=1u<<d;if(a&bit)return 0;a|=bit;
  d=diffval[g[t]][mult[j[h[t]]]];bit=1u<<d;if(b&bit)return 0;b|=bit;
 }
 return 1;
}
static void emit(void){
 int dm[7][MN];
 for(int t=0;t<n;t++){dm[0][t]=0;dm[1][t]=t;dm[2][t]=md(mu*h[t]);dm[3][t]=solg[t];dm[4][t]=md(mu*solg[h[t]]);dm[5][t]=solj[t];dm[6][t]=md(mu*solj[h[t]]);}
 for(int a=0;a<7;a++)for(int b=0;b<a;b++){uint32_t seen=0;for(int t=0;t<n;t++){int d=md(dm[a][t]-dm[b][t]);if(seen>>d&1u){printf("c INTERNAL DM pair %d,%d\n",a,b);exit(5);}seen|=1u<<d;}}
 char path[4096];snprintf(path,sizeof path,"%s.dmraw",prefix);int fd=open(path,O_WRONLY|O_CREAT|O_EXCL,0444);if(fd<0){perror("output");exit(3);}FILE *f=fdopen(fd,"w");
 for(int a=0;a<7;a++){for(int t=0;t<n;t++)fprintf(f,t?" %d":"%d",dm[a][t]);fputc('\n',f);}fclose(f);
 printf("v h");for(int t=0;t<n;t++)printf(" %d",h[t]);putchar('\n');printf("c wrote %s\n",path);found=1;
}
static void on_g(void){
 /* g and Sg are interchangeable rows within one pair. */
 for(int t=0;t<n;t++){int s=md(mu*gval[h[t]]);if(s!=gval[t]){if(s<gval[t])return;break;}}
 vtotal++;
 for(int i=0;i<nv;i++){
  comparisons++;
  const uint8_t *j=store+(size_t)i*n;
  if(orth2(gval,j)){for(int t=0;t<n;t++){solg[t]=gval[t];solj[t]=j[t];}emit();return;}
  if((comparisons&4095)==0&&check())return;
 }
 if(nv>=VCAP){overflow=1;puts("c V store cap, status UNKNOWN");return;}
 for(int t=0;t<n;t++)store[(size_t)nv*n+t]=(uint8_t)gval[t];nv++;if(nv>maxv)maxv=nv;
}
static void gdfs(uint32_t assigned,const uint32_t *used,int depth){
 if((++gnodes&1023)==0&&check())return;
 if(depth==nchosen){on_g();return;}
 int best=-1,bc=0x7fffffff;uint32_t avail[4]={0};
 for(int i=0;i<nchosen;i++)if(!(assigned>>i&1u)){
  HOpt *o=&ops[chosen[i]];int cnt=0;
  for(int j=0;j<o->ng;j++)if(compatible(&o->g[j],used)){cnt++;for(int f=0;f<4;f++)avail[f]|=o->g[j].m[f];}
  if(!cnt)return;if(cnt<bc){bc=cnt;best=i;}
 }
 uint32_t all=(1u<<n)-1u;for(int f=0;f<4;f++)if((avail[f]|used[f])!=all)return;
 HOpt *o=&ops[chosen[best]];
 for(int j=0;j<o->ng&&!found&&!timed_out&&!overflow;j++)if(compatible(&o->g[j],used)){
  uint32_t u[4];for(int f=0;f<4;f++)u[f]=used[f]|o->g[j].m[f];for(int p=0;p<o->size;p++)gval[o->p[p]]=o->g[j].val[p];
  gdfs(assigned|(1u<<best),u,depth+1);
 }
}
static void hdfs(void){
 if((++hnodes&1023)==0&&check())return;
 if(!R[0]){
  hcount++;if(count_h)return;
  for(int t=0;t<n;t++)h[t]=t;
  for(int i=0;i<nchosen;i++){HOpt *o=&ops[chosen[i]];for(int p=0;p<o->size;p++)h[o->p[p]]=o->p[(p+1)%o->size];}
  if(!canonical_h())return;hcanonical++;nv=0;gval[0]=0;uint32_t used[4]={1,1,1,1};gdfs(0,used,0);return;
 }
 int c=R[0];for(int j=R[c];j;j=R[j])if(S[j]<S[c])c=j;if(!S[c])return;cover(c);
 for(int r=D[c];r!=c&&!found&&!timed_out&&!overflow;r=D[r]){chosen[nchosen++]=ROW[r];for(int j=R[r];j!=r;j=R[j])cover(C[j]);hdfs();for(int j=L[r];j!=r;j=L[j])uncover(C[j]);nchosen--;}
 uncover(c);
}
int main(int argc,char **argv){
 if(argc!=6){fprintf(stderr,"usage: involution_pair_c21v1 N MU SECONDS first|hcount OUTPREFIX\n");return 2;}
 n=atoi(argv[1]);mu=atoi(argv[2]);limit=atof(argv[3]);count_h=!strcmp(argv[4],"hcount");prefix=argv[5];
 if(n<3||n>MN||n%2==0||(mu*mu)%n!=1){fprintf(stderr,"bad n/mu\n");return 2;}
 signal(SIGTERM,term);signal(SIGINT,term);setvbuf(stdout,NULL,_IOLBF,0);t0=last=now();
 printf("c involution_pair_c21v1 n %d mu %d %s limit %.1f\n",n,mu,count_h?"hcount":"first",limit);
 for(int a=0;a<n;a++){mult[a]=md(mu*a);for(int b=0;b<n;b++)diffval[a][b]=md(a-b);}
 for(int u=1;u<n;u++){int inv=0;for(int v=1;v<n;v++)if(md(u*v)==1){inv=v;break;}if(!inv)continue;
  for(int t=0;t<n;t++){unitmul[nunits][t]=md(u*t);unitinv[nunits][t]=md(inv*t);}nunits++;
 }
 build_options();make_dlx();if(!count_h){store=malloc((size_t)VCAP*n);if(!store){puts("c store allocation");return 3;}}
 hdfs();
 printf("c final %.3f hcount %lld hcanonical %lld hnodes %lld gnodes %lld vtotal %lld maxV %d comparisons %lld timed_out %d overflow %d signal %d\n",now()-t0,hcount,hcanonical,hnodes,gnodes,vtotal,maxv,comparisons,timed_out,overflow,(int)stopped);
 if(found){puts("s SATISFIABLE");return 10;}
 if(timed_out||overflow){puts("s UNKNOWN");return 0;}
 if(count_h){puts("s HCOUNT COMPLETE (not a seven-row conclusion)");return 0;}
 puts("s EXHAUSTED-RESTRICTED (this exact involution model only)");return 20;
}
