/* Exact solver for seven-row DMs invariant under (mu,(1 2 3)(4 5 6)), fixing row0,
 * mu^3=1 in Z_n. CFR21 lane, v4 = v3 plus run mode hlist, which is hcount mode that also
 * prints 'c hl INDEX h h(0)..h(n-1)' for every canonical h with INDEX>=SKIP, in the same
 * deterministic canonical order. No g search in hlist; h enumeration/canonical test are
 * byte-for-byte v3 code. v1-v3 sources are unchanged.
 *
 * KEPT FROM v2 (same code and semantics, same deterministic order): the normal form; the h
 * options and the h DLX (items, rows, MRV rule, row order), hence the order in which every h
 * and every canonical h is reached; affine-canonical h (reduction A); the g(0)=0 gauge in
 * both modes (reduction B); the g-value options of each h-orbit (save_g: masks, rejection of
 * internal collisions, gauges); the definition-level check of all21 row pairs before any
 * output; the exclusive OUTPREFIX.dmraw. NEW IN v3: (1) for one fixed canonical h, g is
 * searched by a nested exact AlgorithmX/DLX (G MATRIX below) instead of v2's orbit-MRV DFS;
 * no other pruning. (2) An optional final SKIP argument for deterministic resumption over
 * canonical-h indices (RESUME CONTRACT). (3) Mode gcount enumerates every g of every
 * searched canonical h (calibration counts).
 *
 * Normalise row0=0, row1=t. The column action is a permutation h with h^3=id.
 * Rows are [0,t,mu*h^2(t),mu^2*h(t),g(t),mu*g(h^2(t)),mu^2*g(h(t))].
 * Top-triple differences all bijective iff d(t)=t-mu*h^2(t) is bijective.
 * For fixed h, it suffices that the following five maps are permutations:
 *   F0=g, F1=g-id, F2=g-mu*h^2, F3=g-mu^2*h, F4=g-mu*g(h^2).
 * All other row pairs follow by the cyclic symmetry. Full direct verification
 * on all21 pairs is still required before writing or counting any solution.
 *
 * H MATRIX (v2, unchanged). h exact-cover options are fixed points a (d=(1-mu)a) or oriented
 * 3-cycles (a,b,c), h(a)=b,h(b)=c,h(c)=a, with differences (a-mu*c,b-mu*a,c-mu*b); every
 * 3-set a<b<c is offered as (a,b,c) and (a,c,b). Item 1+t (t in Z_n): t lies in exactly one
 * chosen h-orbit. Item 1+n+e (e in Z_n): exactly one t has d(t)=e. A row covers its points and
 * its d values; rows whose d values collide are never created. Fixed-point rows exist only in
 * fixed mode, which pre-covers items1 and1+n (h(0)=0, d(0)=0) and creates no row touching
 * point0 or d value0. AlgorithmX/DLX enumerates every h exactly once, one partition into
 * cycles each.
 *
 * Modes fixed: h(0)=g(0)=0. Covers any solution with a fixed column of the
 * column action: row translations by that fixed column preserve the symmetry.
 * free: h has no fixed points; covers solutions with no group-fixed column.
 *
 * v2 reduction A (affine-conjugate h). For a unit u and a shift a let
 * phi(t)=u*(t-a) and b=g(a); put h'=phi h phi^-1 and g'=u*(g phi^-1 - b):
 *   h'(x)=u*(h(u^-1*x+a)-a),   g'(x)=u*(g(u^-1*x+a)-b)   (mod n).
 * Proof: translate rows1..3 by -(a,mu*a,mu^2*a) and rows4..6 by
 * -(b,mu*b,mu^2*b), scale every entry by u and reindex column t as x=phi(t).
 * The shift vector (0,a,mu*a,mu^2*a,b,mu*b,mu^2*b) is fixed by s since mu^3=1,
 * so the translated column set is still s-invariant; unit scaling commutes with
 * s; row translation and unit scaling keep every row-pair difference map a
 * bijection. The new rows are exactly the normal form of (h',g'): row1
 * u*(t-a)=x, row2 u*mu*(h^2(t)-a)=mu*h'^2(x), row3 u*mu^2*(h(t)-a)=mu^2*h'(x),
 * row4 g'(x), row5 u*mu*(g(h^2(t))-b)=mu*g'(h'^2(x)), row6 mu^2*g'(h'(x)).
 * Hence (h,g) is a solution iff (h',g') is; h'^3=id, Fix(h')=phi(Fix(h)) (free
 * stays free) and g'(0)=u*(g(a)-b)=0. Fixed mode needs h'(0)=u*(h(a)-a)=0, so
 * there only shifts with h(a)=a are eligible; in free mode every a is. The DLX
 * h-set of each mode is closed under eligible maps, and the eligible images of
 * h are exactly its AGL(1,n)-conjugates inside that set. g is searched only for
 * the lexicographically minimal array h(0..n-1) of each such class, and with
 * b=g(a) also g(0)=0. Existence is preserved; counts of labelled h/g are not.
 * v2 reduction B (free-mode use of g(0)=0; fixed mode is unchanged from v1).
 * With g(0)=0 the maps g and g-id vanish at t=0. So the unique h-orbit option
 * containing0 keeps only g-options with g(0)=0, and every other orbit rejects
 * g-options with g(t)=0 or g(t)-t=0 (those zeros are taken at t=0). The maps
 * g-mu*h^2, g-mu^2*h, g-mu*g(h^2) do not vanish at t=0 in general (they depend
 * on h and g(h^2(0))), so no mask bit is preset in free mode; every mask is the
 * exact value set of its option.
 *
 * G MATRIX (v3), rebuilt in static arrays for each searched canonical h. Let O_0..O_{m-1} be
 * the chosen h-orbits in h-DLX selection order (m=nchosen; fixed mode: a partition of
 * Z_n\{0}; free mode: a partition of Z_n).
 *  Item 1+f*n+r (f=0..4, r in Z_n): the map F_f takes the value r exactly once.
 *  Item 1+5n+s (s=0..m-1): orbit O_s receives exactly one value assignment.
 *  Row (s,k): the k-th precomputed option of hops[chosen[s]] (save_g, same order as v2). It
 *   sets g(point[p])=value[p] on O_s and covers item 1+5n+s plus item 1+f*n+F_f(t) for every f
 *   and every t in O_s: exactly 1+5|O_s| nodes, because save_g keeps an option only if the
 *   |O_s| values of each F_f on O_s are pairwise distinct (internal collisions rejected).
 *   F_f(t) only uses h(t),h^2(t),g(t),g(h^2(t)), all inside O_s, so a row's items depend on
 *   that row alone. Gauge filters (save_g, v2): fixed mode, no F_f(t)=0 at all; free mode,
 *   the orbit of0 keeps only g(0)=0 and every other orbit has g(t)!=0 and g(t)-t!=0.
 *  Pre-covered: fixed mode, the five items 1+f*n (value0): column0 is implicit, not a slot,
 *   and h(0)=0,g(0)=0 give F_f(0)=0 for all five maps; no row contains such an item. Free
 *   mode: nothing. There the orbit of0 is an ordinary slot whose rows cover F0(0)=0, F1(0)=0
 *   and the generally NONZERO F2(0)=-mu*h^2(0), F3(0)=-mu^2*h(0), F4(0)=-mu*g(h^2(0)); v3
 *   never assumes that the rows of column0 are0 in free mode.
 *  Claim: the exact covers are in bijection with the g having g(0)=0 for which F0..F4 are
 *   permutations (for this h and mode). (->) One row per slot defines g on every point (fixed
 *   mode adds g(0)=0); each item 1+f*n+r covered once (plus the pre-covered F_f(0)=0 in fixed
 *   mode) means each F_f is a bijection. (<-) For such g each restriction to O_s passes
 *   save_g: distinctness by bijectivity; fixed mode F_f(t)!=F_f(0)=0 for t!=0; free mode g(0)=0
 *   and, outside the orbit of0, g(t)=F0(t)!=F0(0)=0 and g(t)-t=F1(t)!=F1(0)=0. Those rows form
 *   an exact cover. Rows of one slot carry distinct value tuples, so distinct covers give
 *   distinct g: gcount counts g exactly. Search: Knuth's AlgorithmX with dancing links,
 *   branching on the first remaining item of minimum size; an item of size0 ends the branch.
 *   No other pruning and no heuristics. gnodes counts G search nodes (not v2's gnodes).
 *
 * RESUME CONTRACT (v3). Canonical index k=0,1,... is the order in which an h passing
 * canonical_h is reached by the h DLX. It depends only on N, MU, mode and this source (MH,
 * DN), not on SECONDS, SKIP, first/gcount/hcount or signals, which can only stop the
 * enumeration early. Every canonical h is counted (hcanonical) BEFORE SKIP is consulted:
 * index<SKIP is skipped (no g search; counted in 'skipped'); otherwise its g search runs, in
 * index order. hcompleted counts only canonical h whose g search ran to exhaustion: never the
 * h being searched at a deadline or signal, never an h over the G caps, never the h in which
 * first mode found its solution. So the completed indices are exactly
 * [range_start,range_end)=[SKIP,SKIP+hcompleted), last_completed=range_end-1 (-1 if none),
 * resume=range_end. 'current' is the index whose g search started last; it is incomplete iff
 * current==resume. To continue an interrupted run, rerun the SAME binary with identical N MU
 * mode and run mode and SKIP=resume, i.e. one past the last FULLY completed canonical index.
 * NEVER use current+1: the interrupted h was not completed and is searched again from its
 * start. The resume value of any 'c progress' line is also safe (it never counts a partial h).
 * Exhaustion of the whole model needs the union of [range_start,range_end) over runs to
 * contain [0,hcanonical), with hcanonical from a run whose h DLX finished (hcount mode or any
 * completed search). A completed first run with SKIP>0 covers only [SKIP,hcanonical) and says
 * so (exit21). hcount mode never searches g; SKIP there only fills 'skipped'.
 *
 * STATUS / EXIT. 10 s SATISFIABLE (first): the verified candidate is printed as
 *  'c solution canonical_index I', 'v h', 'v g', then written to OUTPREFIX.dmraw (O_EXCL, 0444).
 *  20 s EXHAUSTED-RESTRICTED (first, SKIP=0): every canonical h exhausted, for this exact
 *   row-cycling model (this mu, this mode) only, never an unrestricted nonexistence result.
 *  21 s EXHAUSTED-RESTRICTED-SUFFIX (first, SKIP>0): the same, for canonical indices >=SKIP.
 *  0 s UNKNOWN: deadline SECONDS or SIGTERM/SIGINT; polled every1024 h-DLX nodes, every1024 G
 *   nodes, every1024 G rows built and every16 h options while the g tables are built.
 *  3 s UNKNOWN: G caps (final counters printed first), or MH/DN capacity, allocation or output
 *   failure (v2 give_up). An over-cap h is 'current' and incomplete; resuming at it hits the
 *   same cap, so it stays a recorded UNKNOWN and is never skipped silently.
 *  0 s HCOUNT COMPLETE / s GCOUNT COMPLETE: counting modes, not seven-row DM conclusions.
 *  5 internal check failure (reduction invariant, g assigned twice or not at all, cover depth,
 *   G demand or node bound, all-pair DM check). 2 usage.
 *
 * RESOURCES. Static: G matrix, 6 int arrays of GDN=2^20 nodes (24 MiB) and 2 int arrays of
 * GROWS=2^16 rows (512 KiB), reused for every h; h DLX, 6 int arrays of DN=10^5. Heap: only the
 * one-time per-h-option g tables built before the h search (v2 code; realloc growth to powers
 * of two of 24-byte entries); the exact total is printed as gopt_alloc_bytes (v2 counted
 * 7,097,022 options for n21 mu4 free and 3,554,460 fixed). No allocation per h. Each h's exact
 * G demand, rows=sum ng and nodes=1+5n+m+sum ng*(1+5|O_s|), is checked against the caps before
 * building; every h with n<=21 fits (worst case free n21: 7 orbits x 7980 value triples =
 * 55,860 rows, 893,873 nodes). gmax_rows/gmax_nodes report the observed peaks. Recursion depth
 * is at most 2n+2 frames.
 *
 * Usage: cycle3_pair_c21v4 N MU fixed|free SECONDS first|hcount|hlist|gcount OUTPREFIX [SKIP]
 *  first: stop at the first solution (exit10). hcount: enumerate h only, report hcount (all h)
 *   and hcanonical (affine class representatives); no g search, not a DM nonexistence result.
 *  gcount: for each canonical h with index>=SKIP enumerate every g, check each on all21 pairs,
 *   and when that h is exhausted print 'c hg INDEX count C fnv F h h(0) .. h(n-1)' (F = sum mod
 *   2^64 of FNV-1a-64 over the bytes g(0..n-1)); writes no file. SECONDS in (0,10800]. SKIP:
 *   optional nonnegative decimal, default0. Final line, key/value pairs after the time:
 *   'c final T hcount hcanonical skip skipped hcompleted range_start range_end last_completed
 *   resume current solution_index hnodes gnodes gtotal gmax_rows gmax_nodes timed_out overflow
 *   signal'.
 */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <errno.h>
#include <time.h>
#include <signal.h>
#include <fcntl.h>
#include <unistd.h>

#define MN 31
#define MH 10000
#define DN 100000
#define GDN (1<<20)   /* v3 G matrix capacity in nodes: root, item headers and option nodes */
#define GROWS (1<<16) /* v3 G matrix capacity in rows: g options of one h */

typedef struct { uint32_t m[5]; uint8_t value[3]; } GOpt;
typedef struct {
    uint8_t size, point[3];
    uint32_t domain, diff;
    GOpt *g;
    int ng, cap;
} HOpt;
static HOpt hops[MH];
static int nh,n,mu,mu2,fixed_mode,count_h,count_g,list_h;
static double t0,limit,last;
static volatile sig_atomic_t stopped=0;
static int timed_out=0,found=0,overflow=0;
static long long hnodes=0,gnodes=0,hcount=0,hcanonical=0;
/* v3 canonical-index bookkeeping, see RESUME CONTRACT. */
static long long skip=0,hskipped=0,hcompleted=0,hcurrent=-1,solution_index=-1;
static long long gsol_h=0,gtotal=0,gmax_rows=0,gmax_nodes=0;
static uint64_t gsum_h=0;
static int chosen[MN],nchosen;
static const char *prefix;
static int L[DN],R[DN],U[DN],D[DN],C[DN],ROW[DN],S[2*MN+1],dn;
static int solution_g[MN],hcur[MN];
/* Affine tables, filled once by build_affine_tables(): unit k has value unitval[k],
 * unitmul[k][x]=u*x, unitinv[k][x]=u^-1*x, addt[x][a]=x+a, subt[x][a]=x-a, all mod n. */
static int nunits,unitval[MN],unitmul[MN][MN],unitinv[MN][MN],addt[MN][MN],subt[MN][MN];
/* v3 G matrix, static and rebuilt for every searched h. Node z: GL/GR row links, GU/GD item
 * links, GC item, GROW row. Row r: slot gslot[r] and option index gopt[r] of
 * hops[chosen[gslot[r]]].g. gsel holds the rows chosen on the current search path. */
static int GL[GDN],GR[GDN],GU[GDN],GD[GDN],GC[GDN],GROW[GDN],GS[6*MN+1];
static int gslot[GROWS],gopt[GROWS],gsel[MN+1],gdn,grows,gitems;

static int md(int x){x%=n;return x<0?x+n:x;}
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+t.tv_nsec*1e-9;}
static void term(int s){(void)s;stopped=1;}
static void give_up(const char *why){printf("c %s\ns UNKNOWN\n",why);exit(3);}
static int check(void){
    if(stopped||now()-t0>=limit) timed_out=1;
    if(now()-last>=30){last=now();printf("c progress %.1f hcount %lld hcanonical %lld skipped %lld hcompleted %lld resume %lld current %lld hnodes %lld gnodes %lld gtotal %lld\n",now()-t0,hcount,hcanonical,hskipped,hcompleted,skip+hcompleted,hcurrent,hnodes,gnodes,gtotal);}
    return timed_out||found||overflow;
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
    if(nh>=MH)give_up("too many h options");
    hops[nh++]=x;
}
static void save_g(HOpt *h,const int *v){
    GOpt opt;memset(&opt,0,sizeof opt);
    int vals[5][3];
    for(int j=0;j<h->size;j++){
        int t=h->point[j];
        int h1=h->point[(j+1)%h->size],h2=h->point[(j+2)%h->size];
        if(!fixed_mode&&t==0&&v[j]!=0)return; /* v2 free mode: orbit of0 keeps only g(0)=0 */
        opt.value[j]=(uint8_t)v[j];
        vals[0][j]=v[j];
        vals[1][j]=md(v[j]-t);
        vals[2][j]=md(v[j]-mu*h2);
        vals[3][j]=md(v[j]-mu2*h1);
        vals[4][j]=md(v[j]-mu*v[(j+2)%h->size]);
    }
    for(int f=0;f<5;f++){
        if(!triple_mask(vals[f],h->size,&opt.m[f]))return;
        if(fixed_mode){if(opt.m[f]&1u)return;}                /* v1: all five maps are0 at column0 */
        else if(f<2&&!(h->domain&1u)&&(opt.m[f]&1u))return;   /* v2 free: g,g-id take0 at t=0 only */
    }
    if(h->ng==h->cap){h->cap=h->cap?h->cap*2:64;h->g=realloc(h->g,sizeof(GOpt)*(size_t)h->cap);if(!h->g)give_up("allocation fail");}
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
    unsigned long long bytes=0;
    for(int i=0;i<nh;i++)bytes+=(unsigned long long)hops[i].cap*sizeof(GOpt);
    printf("c memory gopt_alloc_bytes %llu gmatrix_static_bytes %llu (one-time; no per-h allocation)\n",bytes,
           (unsigned long long)(sizeof GL+sizeof GR+sizeof GU+sizeof GD+sizeof GC+sizeof GROW+sizeof gslot+sizeof gopt));
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
                if(dn>=DN)give_up("DLX capacity");
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
static void build_affine_tables(void){
    for(int x=0;x<n;x++)for(int a=0;a<n;a++){addt[x][a]=md(x+a);subt[x][a]=md(x-a);}
    nunits=0;
    for(int u=1;u<n;u++){
        int inv=0;
        for(int v=1;v<n;v++)if(md(u*v)==1){inv=v;break;}
        if(!inv)continue;
        unitval[nunits]=u;
        for(int x=0;x<n;x++){unitmul[nunits][x]=md(u*x);unitinv[nunits][x]=md(inv*x);}
        nunits++;
    }
}
/* 1 iff h is lexicographically <= every eligible conjugate x -> u*(h(u^-1*x+a)-a):
 * every unit u; shifts a with h(a)=a in fixed mode, every shift a in free mode. */
static int canonical_h(const int *h){
    for(int a=0;a<n;a++){
        if(fixed_mode&&h[a]!=a)continue;
        for(int k=0;k<nunits;k++){
            if(a==0&&unitval[k]==1)continue; /* identity map */
            const int *um=unitmul[k],*ui=unitinv[k];
            for(int x=0;x<n;x++){
                int y=um[subt[h[addt[ui[x]][a]]][a]];
                if(y!=h[x]){if(y<h[x])return 0;break;}
            }
        }
    }
    return 1;
}
/* ---- v3 G matrix (see G MATRIX in the header) ---- */
static void gcover(int c){
    GR[GL[c]]=GR[c];GL[GR[c]]=GL[c];
    for(int i=GD[c];i!=c;i=GD[i])for(int j=GR[i];j!=i;j=GR[j]){GD[GU[j]]=GD[j];GU[GD[j]]=GU[j];GS[GC[j]]--;}
}
static void guncover(int c){
    for(int i=GU[c];i!=c;i=GU[i])for(int j=GL[i];j!=i;j=GL[j]){GS[GC[j]]++;GD[GU[j]]=j;GU[GD[j]]=j;}
    GR[GL[c]]=c;GL[GR[c]]=c;
}
static void gnode(int item,int row,int *first,int *prev){
    int z=gdn++;
    if(z>=GDN){printf("c INTERNAL G node bound (demand precheck violated)\ns UNKNOWN\n");exit(5);}
    GC[z]=item;GROW[z]=row;GU[z]=GU[item];GD[z]=item;GD[GU[item]]=z;GU[item]=z;GS[item]++;
    if(*first<0)*first=z;
    else {GR[*prev]=z;GL[z]=*prev;}
    *prev=z;
}
/* Build the G matrix of the current h (chosen[0..nchosen-1]); the caller checked that the
 * exact demand need_rows/need_nodes fits the caps. Returns 0 if the deadline/signal poll
 * fired (then this h is neither searched nor completed). */
static int make_gdlx(long long need_rows,long long need_nodes){
    gitems=5*n+nchosen;gdn=gitems+1;grows=0;
    for(int c=0;c<=gitems;c++){GL[c]=c-1;GR[c]=c+1;GU[c]=GD[c]=c;GC[c]=c;GROW[c]=-1;GS[c]=0;}
    GL[0]=gitems;GR[gitems]=0;
    for(int s=0;s<nchosen;s++){
        const HOpt *o=&hops[chosen[s]];
        for(int k=0;k<o->ng;k++){
            int row=grows++,first=-1,prev=-1;
            gslot[row]=s;gopt[row]=k;
            gnode(1+5*n+s,row,&first,&prev);                 /* slot item of O_s */
            for(int f=0;f<5;f++){                            /* value items of F_f on O_s */
                uint32_t m=o->g[k].m[f];
                while(m){int b=__builtin_ctz(m);m&=m-1;gnode(1+f*n+b,row,&first,&prev);}
            }
            GR[prev]=first;GL[first]=prev;
            if((row&1023)==1023&&check())return 0;
        }
    }
    if(grows!=need_rows||gdn!=need_nodes){
        printf("c INTERNAL G demand mismatch rows %d/%lld nodes %d/%lld\ns UNKNOWN\n",grows,need_rows,gdn,need_nodes);exit(5);
    }
    if(fixed_mode)for(int f=0;f<5;f++)gcover(1+f*n); /* implicit column0: F_f(0)=0 for all five maps */
    return 1;
}
static uint64_t fnv1a(const int *g){
    uint64_t x=UINT64_C(14695981039346656037);
    for(int t=0;t<n;t++){x^=(uint64_t)g[t];x*=UINT64_C(1099511628211);}
    return x;
}
/* v2 reduction invariants, then the definition-level check on all21 row pairs; exit5 on failure. */
static void checked_dm(int dm[7][MN]){
    const int *h=hcur;
    int bad=solution_g[0]!=0||!canonical_h(h)||(fixed_mode&&h[0]!=0);
    for(int t=0;t<n;t++)if(solution_g[t]<0||solution_g[t]>=n||h[h[h[t]]]!=t||(!fixed_mode&&h[t]==t))bad=1;
    if(bad){printf("c INTERNAL reduction invariant failed\ns UNKNOWN\n");exit(5);}
    for(int t=0;t<n;t++){
        dm[0][t]=0;dm[1][t]=t;dm[2][t]=md(mu*h[h[t]]);dm[3][t]=md(mu2*h[t]);
        dm[4][t]=solution_g[t];dm[5][t]=md(mu*solution_g[h[h[t]]]);dm[6][t]=md(mu2*solution_g[h[t]]);
    }
    for(int a=0;a<7;a++)for(int b=0;b<a;b++){
        uint32_t seen=0;
        for(int t=0;t<n;t++){int v=md(dm[a][t]-dm[b][t]);if(seen>>v&1u){printf("c INTERNAL full DM check failed %d,%d\ns UNKNOWN\n",a,b);exit(5);}seen|=1u<<v;}
    }
}
static void emit(int dm[7][MN]){
    const int *h=hcur;
    /* Print the verified candidate before the exclusive write so a failed create cannot lose it. */
    printf("c solution canonical_index %lld\n",hcurrent);
    printf("v h");for(int t=0;t<n;t++)printf(" %d",h[t]);putchar('\n');
    printf("v g");for(int t=0;t<n;t++)printf(" %d",solution_g[t]);putchar('\n');
    char path[4096];snprintf(path,sizeof path,"%s.dmraw",prefix);
    int fd=open(path,O_WRONLY|O_CREAT|O_EXCL,0444);
    if(fd<0){perror("output");give_up("OUTPREFIX.dmraw not created; the verified candidate is in the v lines above");}
    FILE *out=fdopen(fd,"w");
    if(!out)give_up("fdopen failed; the verified candidate is in the v lines above");
    for(int a=0;a<7;a++){for(int t=0;t<n;t++)fprintf(out,t?" %d":"%d",dm[a][t]);fputc('\n',out);}
    if(fclose(out)!=0)give_up("write/close of OUTPREFIX.dmraw failed; the verified candidate is in the v lines above");
    printf("c wrote %s\n",path);found=1;solution_index=hcurrent;
}
/* Exact cover found: one row per slot. Rebuild g, verify, then count (gcount) or emit (first). */
static void on_g(int depth){
    int dm[7][MN];
    if(depth!=nchosen){printf("c INTERNAL G cover depth %d != slots %d\ns UNKNOWN\n",depth,nchosen);exit(5);}
    for(int t=0;t<n;t++)solution_g[t]=-1;
    if(fixed_mode)solution_g[0]=0; /* implicit column0: not a slot (h(0)=0, gauge g(0)=0) */
    for(int i=0;i<depth;i++){
        int row=gsel[i];
        const HOpt *o=&hops[chosen[gslot[row]]];
        const GOpt *x=&o->g[gopt[row]];
        for(int p=0;p<o->size;p++){
            int t=o->point[p];
            if(solution_g[t]!=-1){printf("c INTERNAL g(%d) assigned twice\ns UNKNOWN\n",t);exit(5);}
            solution_g[t]=x->value[p];
        }
    }
    checked_dm(dm); /* also rejects any unassigned g(t) */
    if(count_g){gsol_h++;gsum_h+=fnv1a(solution_g);return;}
    emit(dm);
}
static void gdfs(int depth){
    if((++gnodes&1023)==0&&check())return;
    if(GR[0]==0){on_g(depth);return;}
    int c=GR[0];for(int j=GR[c];j;j=GR[j])if(GS[j]<GS[c])c=j;
    if(!GS[c])return;
    gcover(c);
    for(int r=GD[c];r!=c&&!found&&!timed_out&&!overflow;r=GD[r]){
        gsel[depth]=GROW[r];
        for(int j=GR[r];j!=r;j=GR[j])gcover(GC[j]);
        gdfs(depth+1);
        for(int j=GL[r];j!=r;j=GL[j])guncover(GC[j]);
    }
    guncover(c);
}
/* g search for the current canonical h (index hcurrent). On return the h is completed iff
 * found, timed_out and overflow are all still0. */
static void search_g(void){
    long long rows=0,nodes=5LL*n+nchosen+1;
    for(int s=0;s<nchosen;s++){const HOpt *o=&hops[chosen[s]];rows+=o->ng;nodes+=(long long)o->ng*(1+5*o->size);}
    if(rows>GROWS||nodes>GDN){
        overflow=1;
        printf("c G capacity: canonical index %lld needs rows %lld nodes %lld, caps %d/%d; UNKNOWN\n",hcurrent,rows,nodes,GROWS,GDN);
        return;
    }
    if(rows>gmax_rows)gmax_rows=rows;
    if(nodes>gmax_nodes)gmax_nodes=nodes;
    gsol_h=0;gsum_h=0;
    if(make_gdlx(rows,nodes))gdfs(0);
}
static void hdfs(void){
    if((++hnodes&1023)==0&&check())return;
    if(R[0]==0){
        hcount++;
        for(int t=0;t<n;t++)hcur[t]=t;
        for(int i=0;i<nchosen;i++){
            HOpt *o=&hops[chosen[i]];
            for(int p=0;p<o->size;p++)hcur[o->point[p]]=o->point[(p+1)%o->size];
        }
        if(!canonical_h(hcur))return;
        long long idx=hcanonical++; /* v3: counted before SKIP is consulted */
        if(idx<skip){hskipped++;return;}
        if(count_h){
            if(list_h){printf("c hl %lld h",idx);for(int t=0;t<n;t++)printf(" %d",hcur[t]);putchar('\n');}
            return;
        }
        hcurrent=idx;
        search_g();
        if(found||timed_out||overflow)return; /* solved, interrupted or over cap: NOT completed */
        hcompleted++;
        if(count_g){
            gtotal+=gsol_h;
            printf("c hg %lld count %lld fnv %016llx h",idx,gsol_h,(unsigned long long)gsum_h);
            for(int t=0;t<n;t++)printf(" %d",hcur[t]);
            putchar('\n');
        }
        return;
    }
    int c=R[0];for(int j=R[c];j;j=R[j])if(S[j]<S[c])c=j;
    if(!S[c])return;
    cover(c);
    for(int r=D[c];r!=c&&!found&&!timed_out&&!overflow;r=D[r]){
        chosen[nchosen++]=ROW[r];
        for(int j=R[r];j!=r;j=R[j])cover(C[j]);
        hdfs();
        for(int j=L[r];j!=r;j=L[j])uncover(C[j]);
        nchosen--;
    }
    uncover(c);
}
int main(int argc,char **argv){
    const char *usage="usage: cycle3_pair_c21v4 N MU fixed|free SECONDS first|hcount|hlist|gcount OUTPREFIX [SKIP]\n";
    if((argc!=7&&argc!=8)||(strcmp(argv[3],"fixed")&&strcmp(argv[3],"free"))||
       (strcmp(argv[5],"first")&&strcmp(argv[5],"hcount")&&strcmp(argv[5],"hlist")&&strcmp(argv[5],"gcount"))){
        fputs(usage,stderr);return 2;
    }
    n=atoi(argv[1]);mu=atoi(argv[2]);
    if(n<3||n>MN||mu<1||mu>=n||(mu*((mu*mu)%n))%n!=1){fprintf(stderr,"bad n/mu\n");return 2;}
    mu2=(mu*mu)%n;fixed_mode=!strcmp(argv[3],"fixed");limit=atof(argv[4]);
    list_h=!strcmp(argv[5],"hlist");count_h=list_h||!strcmp(argv[5],"hcount");count_g=!strcmp(argv[5],"gcount");prefix=argv[6];
    if(!(limit>0&&limit<=10800)){fprintf(stderr,"SECONDS must be in (0,10800]\n");return 2;}
    if(argc==8){
        char *end=NULL;
        if(argv[7][0]<'0'||argv[7][0]>'9'){fputs(usage,stderr);return 2;}
        errno=0;skip=strtoll(argv[7],&end,10);
        if(errno||*end){fputs(usage,stderr);return 2;}
    }
    signal(SIGTERM,term);signal(SIGINT,term);setvbuf(stdout,NULL,_IOLBF,0);t0=last=now();
    printf("c cycle3_pair_c21v4 n %d mu %d %s %s limit %.1f skip %lld\n",n,mu,fixed_mode?"fixed":"free",
           list_h?"hlist":count_h?"hcount":count_g?"gcount":"first",limit,skip);
    build_affine_tables();
    printf("c v2 reductions: affine-canonical h over %d units and %s; g(0)=0 in both modes\n",nunits,fixed_mode?"shifts a with h(a)=a":"all shifts a");
    printf("c v3 g search: nested exact DLX over %d value items (5 maps) plus one item per h-orbit; %s\n",5*n,
           fixed_mode?"the five value-0 items are pre-covered by implicit column0":"nothing pre-covered, the orbit of0 is an ordinary slot");
    make_options();
    if(!timed_out){build_dlx();hdfs();}
    long long range_end=skip+hcompleted;
    printf("c final %.3f hcount %lld hcanonical %lld skip %lld skipped %lld hcompleted %lld range_start %lld range_end %lld last_completed %lld resume %lld current %lld solution_index %lld hnodes %lld gnodes %lld gtotal %lld gmax_rows %lld gmax_nodes %lld timed_out %d overflow %d signal %d\n",
           now()-t0,hcount,hcanonical,skip,hskipped,hcompleted,skip,range_end,hcompleted?range_end-1:-1LL,range_end,hcurrent,solution_index,
           hnodes,gnodes,gtotal,gmax_rows,gmax_nodes,timed_out,overflow,(int)stopped);
    if(!found&&!timed_out&&!overflow&&!count_h&&skip>0&&skip>=hcanonical)
        printf("c note SKIP %lld >= hcanonical %lld: no canonical h was searched in this run\n",skip,hcanonical);
    if(found){puts("s SATISFIABLE");return 10;}
    if(overflow){puts("s UNKNOWN");return 3;}
    if(timed_out){puts("s UNKNOWN");return 0;}
    if(count_h){puts(list_h?"s HLIST COMPLETE (not a seven-row DM conclusion)":"s HCOUNT COMPLETE (not a seven-row DM conclusion)");return 0;}
    if(count_g){printf("s GCOUNT COMPLETE (canonical indices >= %lld; calibration counts, not a seven-row DM conclusion)\n",skip);return 0;}
    if(skip>0){puts("s EXHAUSTED-RESTRICTED-SUFFIX (canonical h indices >= SKIP only; this exact row-cycling model only)");return 21;}
    puts("s EXHAUSTED-RESTRICTED (this exact row-cycling model only)");return 20;
}
