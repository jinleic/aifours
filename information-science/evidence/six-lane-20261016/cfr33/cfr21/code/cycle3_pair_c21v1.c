/* Exact solver for seven-row DMs invariant under (mu,(1 2 3)(4 5 6)), fixing row0,
 * mu^3=1 in Z_n. CFR21 InfoCFR27Lift; independent representation of group g06.
 *
 * Normalise row0=0, row1=t. The column action is a permutation h with h^3=id.
 * Rows are [0,t,mu*h^2(t),mu^2*h(t),g(t),mu*g(h^2(t)),mu^2*g(h(t))].
 * Top-triple differences all bijective iff d(t)=t-mu*h^2(t) is bijective.
 * For fixed h, it suffices that the following five maps are permutations:
 *   g, g-id, g-mu*h^2, g-mu^2*h, g-mu*g(h^2).
 * All other row pairs follow by the cyclic symmetry. Full direct verification
 * on all21 pairs is still required before writing any solution.
 *
 * h exact-cover options are fixed points a (d=(1-mu)a) or oriented3-cycles
 * (a,b,c) with differences (a-mu*c,b-mu*a,c-mu*b). Items: domain elements and
 * d values. AlgorithmX/DLX enumerates every h, one partition into cycles each.
 * For each h-orbit, g-value options are precomputed once; each covers its
 * g and four difference sets. Exact MRV DFS over the chosen h-orbit slots
 * finds a compatible collection of g-options. No SAT and no heuristic pruning.
 *
 * Modes fixed: h(0)=g(0)=0. Covers any solution with a fixed column of the
 * column action: row translations by that fixed column preserve the symmetry.
 * free: h has no fixed points; covers solutions with no group-fixed column.
 *
 * Usage: cycle3_pair_c21v1 N MU fixed|free SECONDS first|hcount OUTPREFIX
 * first stops at first solution with exclusive OUTPREFIX.dmraw, exit10.
 * hcount enumerates only h (no g search); not a DM nonexistence result.
 * SIGTERM/deadline -> UNKNOWN. Completed first mode with no solution ->
 * EXHAUSTED-RESTRICTED for this specific seven-row symmetry model only.
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
#define MH 10000
#define DN 100000

typedef struct { uint32_t m[5]; uint8_t value[3]; } GOpt;
typedef struct {
    uint8_t size, point[3];
    uint32_t domain, diff;
    GOpt *g;
    int ng, cap;
} HOpt;
static HOpt hops[MH];
static int nh,n,mu,mu2,fixed_mode,count_h;
static double t0,limit,last;
static volatile sig_atomic_t stopped=0;
static int timed_out=0,found=0;
static long long hnodes=0,gnodes=0,hcount=0;
static int chosen[MN],nchosen;
static const char *prefix;
static int L[DN],R[DN],U[DN],D[DN],C[DN],ROW[DN],S[2*MN+1],dn;
static int solution_g[MN];

static int md(int x){x%=n;return x<0?x+n:x;}
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+t.tv_nsec*1e-9;}
static void term(int s){(void)s;stopped=1;}
static int check(void){
    if(stopped||now()-t0>=limit) timed_out=1;
    if(now()-last>=30){last=now();printf("c progress %.1f hcount %lld hnodes %lld gnodes %lld\n",now()-t0,hcount,hnodes,gnodes);}
    return timed_out||found;
}
static int triple_mask(const int *v,int sz,uint32_t *out){
    uint32_t m=0;
    for(int i=0;i<sz;i++){uint32_t b=1u<<v[i];if(m&b)return 0;m|=b;}
    *out=m;return 1;
}
static void add_h(int sz,int a,int b,int c){
    HOpt x;memset(&x,0,sizeof x);x.size=(uint8_t)sz;x.point[0]=(uint8_t)a;x.point[1]=(uint8_t)b;x.point[2]=(uint8_t)c;
    int pt[3]={a,b,c},df[3];
    if(sz==1)df[0]=md((1-mu)*a);
    else {df[0]=md(a-mu*c);df[1]=md(b-mu*a);df[2]=md(c-mu*b);}
    if(!triple_mask(pt,sz,&x.domain)||!triple_mask(df,sz,&x.diff))return;
    if(fixed_mode && (x.domain&1u || x.diff&1u))return; /* zero fixed point preselected */
    if(nh>=MH){printf("c too many h options\n");exit(3);}
    hops[nh++]=x;
}
static void save_g(HOpt *h,const int *v){
    GOpt opt;memset(&opt,0,sizeof opt);
    int vals[5][3];
    for(int j=0;j<h->size;j++){
        int t=h->point[j];
        int h1=h->point[(j+1)%h->size],h2=h->point[(j+2)%h->size];
        opt.value[j]=(uint8_t)v[j];
        vals[0][j]=v[j];
        vals[1][j]=md(v[j]-t);
        vals[2][j]=md(v[j]-mu*h2);
        vals[3][j]=md(v[j]-mu2*h1);
        vals[4][j]=md(v[j]-mu*v[(j+2)%h->size]);
    }
    for(int f=0;f<5;f++)if(!triple_mask(vals[f],h->size,&opt.m[f])||(fixed_mode&&(opt.m[f]&1u)))return;
    if(h->ng==h->cap){h->cap=h->cap?h->cap*2:64;h->g=realloc(h->g,sizeof(GOpt)*(size_t)h->cap);if(!h->g){printf("c allocation fail\n");exit(3);}}
    h->g[h->ng++]=opt;
}
static void make_options(void){
    for(int a=0;a<n;a++)if(fixed_mode)add_h(1,a,0,0);
    for(int a=0;a<n;a++)for(int b=a+1;b<n;b++)for(int c=b+1;c<n;c++){
        add_h(3,a,b,c);add_h(3,a,c,b);
    }
    long long ng=0;
    if(!count_h)for(int i=0;i<nh;i++){
        HOpt *h=&hops[i];
        if(h->size==1){for(int u=0;u<n;u++){int v[3]={u,0,0};save_g(h,v);}}
        else for(int u=0;u<n;u++)for(int v=0;v<n;v++)if(u!=v)for(int w=0;w<n;w++)if(w!=u&&w!=v){int x[3]={u,v,w};save_g(h,x);}
        ng+=h->ng;
        if((i&15)==0&&check())return;
    }
    printf("c options h %d g %lld\n",nh,ng);
}
static void cover(int c){
    R[L[c]]=R[c];L[R[c]]=L[c];
    for(int i=D[c];i!=c;i=D[i])for(int j=R[i];j!=i;j=R[j]){D[U[j]]=D[j];U[D[j]]=U[j];S[C[j]]--;}
}
static void uncover(int c){
    for(int i=U[c];i!=c;i=U[i])for(int j=L[i];j!=i;j=L[j]){S[C[j]]++;D[U[j]]=j;U[D[j]]=j;}
    R[L[c]]=c;L[R[c]]=c;
}
static void build_dlx(void){
    int nc=2*n;dn=nc+1;
    for(int c=0;c<=nc;c++){L[c]=c-1;R[c]=c+1;U[c]=D[c]=c;S[c]=0;C[c]=c;}
    L[0]=nc;R[nc]=0;
    for(int o=0;o<nh;o++){
        int first=-1,prev=-1;
        for(int fam=0;fam<2;fam++){
            uint32_t mask=fam?hops[o].diff:hops[o].domain;
            while(mask){int b=__builtin_ctz(mask);mask&=mask-1;int c=1+fam*n+b,j=dn++;
                if(dn>=DN){printf("c DLX capacity\n");exit(3);}
                C[j]=c;ROW[j]=o;U[j]=U[c];D[j]=c;D[U[c]]=j;U[c]=j;S[c]++;
                if(first<0)first=j;
                else {R[prev]=j;L[j]=prev;}
                prev=j;
            }
        }
        R[prev]=first;L[first]=prev;
    }
    if(fixed_mode){cover(1);cover(1+n);}
}
static int compatible(const GOpt *g,const uint32_t *used){for(int f=0;f<5;f++)if(g->m[f]&used[f])return 0;return 1;}
static int gdfs(uint32_t assigned,const uint32_t *used,int depth){
    if((++gnodes&1023)==0&&check())return 0;
    if(depth==nchosen)return 1;
    int best=-1,bcount=0x7fffffff;
    uint32_t available[5]={0};
    for(int i=0;i<nchosen;i++)if(!(assigned>>i&1u)){
        HOpt *h=&hops[chosen[i]];int cnt=0;
        for(int j=0;j<h->ng;j++)if(compatible(&h->g[j],used)){
            cnt++;
            for(int f=0;f<5;f++)available[f]|=h->g[j].m[f];
        }
        if(cnt==0)return 0;
        if(cnt<bcount){bcount=cnt;best=i;}
    }
    uint32_t all=(1u<<n)-1u;
    for(int f=0;f<5;f++)if((available[f]|used[f])!=all)return 0;
    HOpt *h=&hops[chosen[best]];
    for(int j=0;j<h->ng;j++)if(compatible(&h->g[j],used)){
        uint32_t u[5];for(int f=0;f<5;f++)u[f]=used[f]|h->g[j].m[f];
        for(int p=0;p<h->size;p++)solution_g[h->point[p]]=h->g[j].value[p];
        if(gdfs(assigned|(1u<<best),u,depth+1))return 1;
        if(timed_out)return 0;
    }
    return 0;
}
static void emit(void){
    int h[MN],dm[7][MN];
    for(int i=0;i<n;i++)h[i]=i;
    for(int i=0;i<nchosen;i++){
        HOpt *o=&hops[chosen[i]];
        for(int p=0;p<o->size;p++)h[o->point[p]]=o->point[(p+1)%o->size];
    }
    for(int t=0;t<n;t++){
        dm[0][t]=0;dm[1][t]=t;dm[2][t]=md(mu*h[h[t]]);dm[3][t]=md(mu2*h[t]);
        dm[4][t]=solution_g[t];dm[5][t]=md(mu*solution_g[h[h[t]]]);dm[6][t]=md(mu2*solution_g[h[t]]);
    }
    for(int a=0;a<7;a++)for(int b=0;b<a;b++){
        uint32_t seen=0;
        for(int t=0;t<n;t++){int v=md(dm[a][t]-dm[b][t]);if(seen>>v&1u){printf("c INTERNAL full DM check failed %d,%d\n",a,b);exit(5);}seen|=1u<<v;}
    }
    char path[4096];snprintf(path,sizeof path,"%s.dmraw",prefix);
    int fd=open(path,O_WRONLY|O_CREAT|O_EXCL,0444);if(fd<0){perror("output");exit(3);}FILE *out=fdopen(fd,"w");
    for(int a=0;a<7;a++){for(int t=0;t<n;t++)fprintf(out,t?" %d":"%d",dm[a][t]);fputc('\n',out);}fclose(out);
    printf("v h");for(int t=0;t<n;t++)printf(" %d",h[t]);putchar('\n');
    printf("v g");for(int t=0;t<n;t++)printf(" %d",solution_g[t]);putchar('\n');
    printf("c wrote %s\n",path);found=1;
}
static void hdfs(void){
    if((++hnodes&1023)==0&&check())return;
    if(R[0]==0){
        hcount++;
        if(!count_h){uint32_t used[5];for(int f=0;f<5;f++)used[f]=fixed_mode?1u:0u;solution_g[0]=0;
            if(gdfs(0,used,0)){emit();return;}
        }
        return;
    }
    int c=R[0];for(int j=R[c];j;j=R[j])if(S[j]<S[c])c=j;
    if(!S[c])return;
    cover(c);
    for(int r=D[c];r!=c&&!found&&!timed_out;r=D[r]){
        chosen[nchosen++]=ROW[r];
        for(int j=R[r];j!=r;j=R[j])cover(C[j]);
        hdfs();
        for(int j=L[r];j!=r;j=L[j])uncover(C[j]);
        nchosen--;
    }
    uncover(c);
}
int main(int argc,char **argv){
    if(argc!=7){fprintf(stderr,"usage: cycle3_pair_c21v1 N MU fixed|free SECONDS first|hcount OUTPREFIX\n");return 2;}
    n=atoi(argv[1]);mu=atoi(argv[2]);mu2=(mu*mu)%n;fixed_mode=!strcmp(argv[3],"fixed");limit=atof(argv[4]);count_h=!strcmp(argv[5],"hcount");prefix=argv[6];
    if(n<3||n>MN||(mu*mu2)%n!=1){fprintf(stderr,"bad n/mu\n");return 2;}
    signal(SIGTERM,term);signal(SIGINT,term);setvbuf(stdout,NULL,_IOLBF,0);t0=last=now();
    printf("c cycle3_pair_c21v1 n %d mu %d %s %s limit %.1f\n",n,mu,fixed_mode?"fixed":"free",count_h?"hcount":"first",limit);
    make_options();
    if(!timed_out){build_dlx();hdfs();}
    printf("c final %.3f hcount %lld hnodes %lld gnodes %lld timed_out %d signal %d\n",now()-t0,hcount,hnodes,gnodes,timed_out,(int)stopped);
    if(found){puts("s SATISFIABLE");return 10;}
    if(timed_out){puts("s UNKNOWN");return 0;}
    if(count_h){puts("s HCOUNT COMPLETE (not a seven-row DM conclusion)");return 0;}
    puts("s EXHAUSTED-RESTRICTED (this exact row-cycling model only)");return 20;
}
