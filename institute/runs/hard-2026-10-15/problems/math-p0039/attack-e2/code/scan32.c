/* A separate exact scan: radix-2^32, three-limb Montgomery arithmetic.
 * No source or header from scan.c is included. p<2^95, exponent<2^64.
 * The divisor sieve uses Tonelli--Shanks sqrt(-3), not cube roots.
 * Digest records are 32 bytes, little endian: n:u64, q:u32, tag:u32,
 * residue:u128. tag 1=factor (residue=0 means NOT COMPUTED), 2=power
 * failure, 3=power hit. EVERY member enters the digest; unsieved members
 * carry their COMPLETE ordinary residue, never a Montgomery representation.
 * Audit records additionally compute powers at selected factor members.
 */
#include <assert.h>
#include <CommonCrypto/CommonDigest.h>
#include <inttypes.h>
#include <pthread.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
typedef uint32_t W;
typedef uint64_t U;
typedef unsigned __int128 Wide;
typedef struct { W v[3]; } Number;
static void die(const char *s) { fprintf(stderr,"%s\n",s); exit(2); }
static double seconds(void) { struct timespec t; if(clock_gettime(CLOCK_MONOTONIC,&t))die("clock"); return t.tv_sec+1e-9*t.tv_nsec; }
static Number unpack(Wide x) { return (Number){{(W)x,(W)(x>>32),(W)(x>>64)}}; }
static Wide pack(Number x) { return (Wide)x.v[0]+((Wide)x.v[1]<<32)+((Wide)x.v[2]<<64); }
static int compare(Number a,Number b) { for(int i=2;i>=0;i--) if(a.v[i]!=b.v[i]) return a.v[i]>b.v[i]?1:-1; return 0; }
static Number subtract(Number a,Number b) {
    U borrow=0; for(int i=0;i<3;i++) { U z=(U)b.v[i]+borrow; W old=a.v[i]; a.v[i]=(W)((U)old-z); borrow=(U)old<z; }
    assert(!borrow); return a;
}
/* Every inner sum is <=(2^32-1)^2+2*(2^32-1)=2^64-1.
 * No 128-bit multiplication participates in modular multiplication.
 * Product is six base-2^32 digits. REDC cancels three low digits one
 * at a time. For a,b<p, its result is <2p<2^96, so digit six is zero.
 */
static inline Number multiply(Number a,Number b,Number p,W inv) {
    W t[7]={0,0,0,0,0,0,0};
    for(int i=0;i<3;i++) {
        U carry=0;
        for(int j=0;j<3;j++) { U z=(U)a.v[i]*b.v[j]+t[i+j]+carry; t[i+j]=(W)z; carry=z>>32; }
        t[i+3]=(W)carry;
    }
    for(int i=0;i<3;i++) {
        W m=t[i]*inv; U carry=0;
        for(int j=0;j<3;j++) { U z=(U)m*p.v[j]+t[i+j]+carry; t[i+j]=(W)z; carry=z>>32; }
        for(int k=i+3;carry;k++) { assert(k<7); U z=(U)t[k]+carry; t[k]=(W)z; carry=z>>32; }
        assert(t[i]==0);
    }
    assert(t[6]==0);
    Number r={{t[3],t[4],t[5]}};
    if(compare(r,p)>=0)r=subtract(r,p);
    return r;
}
static Wide power(U exponent,Wide modulus) {
    assert(exponent && (modulus&1) && modulus>1 && modulus<((Wide)1<<95));
    Number p=unpack(modulus); W inverse=1;
    for(int j=0;j<5;j++) inverse*=2-p.v[0]*inverse;
    W negative=0-inverse;
    Number r=unpack(((Wide)1<<96)%modulus);
    int lead=63-__builtin_clzll(exponent);
    for(int bit=lead;bit>=0;bit--) {
        r=multiply(r,r,p,negative);
        if((exponent>>bit)&1) {
            U carry=0;
            for(int j=0;j<3;j++) { U z=2*(U)r.v[j]+carry; r.v[j]=(W)z; carry=z>>32; }
            assert(!carry);
            if(compare(r,p)>=0)r=subtract(r,p);
        }
    }
    return pack(multiply(r,(Number){{1,0,0}},p,negative));
}
static U small_power(U a,U e,U q) { U r=1; while(e) {if(e&1)r=r*a%q; a=a*a%q; e>>=1;} return r; }
static U square_root(U a,U q) {
    assert(small_power(a,(q-1)/2,q)==1);
    U odd=q-1,s=0; while(!(odd&1)){odd>>=1;s++;}
    if(s==1)return small_power(a,(q+1)/4,q);
    U z=2;while(small_power(z,(q-1)/2,q)!=q-1)z++;
    U c=small_power(z,odd,q),x=small_power(a,(odd+1)/2,q),t=small_power(a,odd,q),m=s;
    while(t!=1) {
        U i=0,y=t; while(y!=1){y=y*y%q;i++;}
        assert(i<m); U b=small_power(c,(U)1<<(m-i-1),q);
        x=x*b%q;c=b*b%q;t=t*c%q;m=i;
    }
    assert(x*x%q==a);return x;
}
typedef struct { W q,first,second; bool all; } Class;
static Class *classes;static size_t nc;
static U lower,upper,stride,bound,block_length,members,nblocks,next_id;
static U window_every,window_length;
static int workers; static double cap,started;
static FILE *blocks_file,*records_file; static pthread_mutex_t mutex=PTHREAD_MUTEX_INITIALIZER;
static void initialize_sieve(void) {
    if(!bound)return;
    unsigned char *cross=calloc((size_t)bound+1,1);
    classes=calloc((size_t)bound+1,sizeof(Class)); if(!cross||!classes)die("sieve memory");
    for(U q=2;q<=bound;q++) if(!cross[q]) {
        for(U k=q*q;k<=bound;k+=q)cross[k]=1;
        if(q!=3 && q%3!=1)continue;
        U a=1,b=1;
        if(q!=3) {U s=square_root(q-3,q),half=(q+1)/2;a=(q-1+s)*half%q;b=(q-1+q-s)*half%q;}
        assert((a*a+a+1)%q==0 && (b*b+b+1)%q==0);
        Class c={(W)q,0,0,false};
        if(stride%q==0) {if((lower%q)!=a && (lower%q)!=b)continue;c.all=true;}
        else {U inv=small_power(stride%q,q-2,q);c.first=(W)((a+q-lower%q)*inv%q);c.second=(W)((b+q-lower%q)*inv%q);}
        classes[nc++]=c;
    }
    free(cross);
}
static void sieve_block(W *factor,U base,U length) {
    if(!bound)return;memset(factor,0,(size_t)length*sizeof(W));
    /* Ascending primes, first factor wins; unlike the older descending sieve. */
    for(size_t k=0;k<nc;k++) {
        Class c=classes[k];U jump=c.all?1:c.q;
        U off[2]={0,0};int roots=1;
        if(!c.all) {off[0]=(c.first+(U)c.q-base%c.q)%c.q;off[1]=(c.second+(U)c.q-base%c.q)%c.q;roots=c.first==c.second?1:2;}
        for(int r=0;r<roots;r++) for(U j=off[r];j<length;j+=jump) if(!factor[j]) {
            U n=lower+stride*(base+j); Wide p=(Wide)n*n+n+1;
            /* Proper-divisor guard on EVERY mark, even in production. */
            if(1<c.q && c.q<p)factor[j]=c.q;
        }
    }
}
static const char *decimal(Wide x,char out[48]) {char a[48];int k=0;do{a[k++]='0'+x%10;x/=10;}while(x);for(int i=0;i<k;i++)out[i]=a[k-i-1];out[k]=0;return out;}
static void hash_record(CC_SHA256_CTX *h,U n,W q,Wide residue) {
    unsigned char b[32]; W tag=q?1:(residue==1?3:2);
    for(int i=0;i<8;i++){b[i]=(unsigned char)n;n>>=8;}
    for(int i=0;i<4;i++){b[8+i]=(unsigned char)q;q>>=8;b[12+i]=(unsigned char)tag;tag>>=8;}
    for(int i=0;i<16;i++){b[16+i]=(unsigned char)residue;residue>>=8;}
    CC_SHA256_Update(h,b,32);
}
static void *scan_thread(void *unused) {
    (void)unused;W *f=bound?malloc((size_t)block_length*sizeof(W)):NULL;if(bound&&!f)die("block memory");
    for(;;) {
        pthread_mutex_lock(&mutex);
        if(next_id==nblocks || seconds()-started>=cap) {pthread_mutex_unlock(&mutex);break;}
        U id=next_id++;pthread_mutex_unlock(&mutex);
        U base=id*block_length,len=members-base;if(len>block_length)len=block_length;
        U first=lower+stride*base;double begin=seconds();sieve_block(f,base,len);
        CC_SHA256_CTX h;CC_SHA256_Init(&h);U marked=0,tested=0,hits=0;
        U *hit_list=NULL; bool has_window=window_every && (id%window_every==0 || id+1==nblocks);
        for(U j=0;j<len;j++) {
            U n=first+stride*j;Wide p=(Wide)n*n+n+1;W q=bound?f[j]:0;
            bool window=has_window && j<window_length,edge=j<2 || j+2>=len;
            bool audit=window||edge;Wide residue=0;
            if(q){marked++;assert(1<q && q<p); /* exact validation of EACH factor, independent of roots */
                U r=n%q;assert((r*r+r+1)%q==0);
            } else {tested++;residue=power(n+1,p);if(residue==1){hit_list=realloc(hit_list,(hits+1)*sizeof(U));if(!hit_list)die("hit memory");hit_list[hits++]=n;}}
            hash_record(&h,n,q,residue);
            if(audit || (!q && residue==1)) {
                if(q)residue=power(n+1,p);char ps[48],rs[48];
                pthread_mutex_lock(&mutex);
                fprintf(records_file,"{\"block\":%"PRIu64",\"index\":%"PRIu64",\"n\":%"PRIu64",\"p\":\"%s\",\"decision\":\"%s\",\"factor\":%u,\"residue\":\"%s\",\"window\":%s,\"edge\":%s}\n",id,base+j,n,decimal(p,ps),q?"factor":(residue==1?"survivor":"base2-fail"),q,decimal(residue,rs),window?"true":"false",edge?"true":"false");
                pthread_mutex_unlock(&mutex);
            }
        }
        assert(marked+tested==len);unsigned char raw[32];char hex[65];CC_SHA256_Final(raw,&h);
        for(int i=0;i<32;i++)sprintf(hex+2*i,"%02x",raw[i]);hex[64]=0;
        pthread_mutex_lock(&mutex);
        fprintf(blocks_file,"{\"kind\":\"block\",\"id\":%"PRIu64",\"index\":%"PRIu64",\"start\":%"PRIu64",\"end\":%"PRIu64",\"count\":%"PRIu64",\"sieved\":%"PRIu64",\"tested\":%"PRIu64",\"hits\":%"PRIu64",\"decision_sha256\":\"%s\",\"seconds\":%.6f,\"survivors\":[",id,base,first,first+stride*len,len,marked,tested,hits,hex,seconds()-begin);
        for(U k=0;k<hits;k++)fprintf(blocks_file,"%s%"PRIu64,k?",":"",hit_list[k]);fputs("]}\n",blocks_file);fflush(blocks_file);fflush(records_file);
        pthread_mutex_unlock(&mutex);free(hit_list);
    }
    free(f);return NULL;
}
static U parse(const char *s) {char *e;U x=strtoull(s,&e,10);if(!*s||*e||*s=='-')die("unsigned argument");return x;}
int main(int argc,char **argv) {
    if(argc==5 && !strcmp(argv[1],"power")) { U e=parse(argv[2]);Wide p=0;for(const char*s=argv[3];*s;s++){if(*s<'0'||*s>'9')die("modulus");p=p*10+*s-'0';}char out[48];printf("%s\n",decimal(power(e,p),out));return 0; }
    if(argc!=13)die("scan32 START STOP STEP B BLOCK THREADS CAP PREFIX WINDOW_EVERY WINDOW_LEN LABEL BINARY_SHA256");
    lower=parse(argv[1]);upper=parse(argv[2]);stride=parse(argv[3]);bound=parse(argv[4]);block_length=parse(argv[5]);workers=(int)parse(argv[6]);cap=parse(argv[7]);window_every=parse(argv[9]);window_length=parse(argv[10]);
    if(lower<2||upper<=lower||upper>((U)1<<47)||!stride||stride>1000000||bound>1000000||!block_length||block_length>((U)1<<26)||workers<1||workers>4||cap<=0||window_length>block_length||strlen(argv[12])!=64)die("unsupported bounds");
    members=1+(upper-1-lower)/stride;nblocks=1+(members-1)/block_length;
    char path[1024];snprintf(path,sizeof(path),"%s.blocks.jsonl",argv[8]);blocks_file=fopen(path,"wx");snprintf(path,sizeof(path),"%s.records.jsonl",argv[8]);records_file=fopen(path,"wx");if(!blocks_file||!records_file)die("fresh output required");
    initialize_sieve();fprintf(blocks_file,"{\"kind\":\"header\",\"version\":2,\"start\":%"PRIu64",\"stop\":%"PRIu64",\"step\":%"PRIu64",\"total\":%"PRIu64",\"block_size\":%"PRIu64",\"blocks\":%"PRIu64",\"sieve_bound\":%"PRIu64",\"sieve_primes\":%zu,\"threads\":%d,\"cap_seconds\":%.0f,\"window_every\":%"PRIu64",\"window_len\":%"PRIu64",\"binary_sha256\":\"%s\",\"backend\":\"radix32-three-limb-Tonelli\",\"digest_protocol\":\"le64-n-le32-factor-le32-tag-le128-residue; factor residue zero=uncomputed\"}\n",lower,upper,stride,members,block_length,nblocks,bound,nc,workers,cap,window_every,window_length,argv[12]);fflush(blocks_file);
    started=seconds();pthread_t ids[4];for(int i=0;i<workers;i++)if(pthread_create(&ids[i],NULL,scan_thread,NULL))die("pthread create");for(int i=0;i<workers;i++)if(pthread_join(ids[i],NULL))die("pthread join");
    double elapsed=seconds()-started;fprintf(blocks_file,"{\"kind\":\"footer\",\"assigned_blocks\":%"PRIu64",\"planned_blocks\":%"PRIu64",\"seconds\":%.6f,\"completed_plan\":%s}\n",next_id,nblocks,elapsed,next_id==nblocks?"true":"false");fclose(blocks_file);fclose(records_file);free(classes);printf("completed blocks=%"PRIu64"/%"PRIu64" seconds=%.6f\n",next_id,nblocks,elapsed);return 0;
}
