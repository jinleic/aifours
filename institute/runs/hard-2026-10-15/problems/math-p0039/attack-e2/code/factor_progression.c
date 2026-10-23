/* Bounded exact witness search, one CPU, no probable-prime elimination.
 * q=6*a*k+1, r=2^a mod q. A hit means q divides 2^(2a)+2^a+1.
 * Only a reported proper factor can support a mathematical elimination;
 * exhaustion/timeout of the requested search is not a primality result.
 */
#include <inttypes.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
typedef uint64_t U;typedef unsigned __int128 Wide;
static double now(void){struct timespec t;clock_gettime(CLOCK_MONOTONIC,&t);return t.tv_sec+1e-9*t.tv_nsec;}
static U power(U a,U q){U r=1;int top=63-__builtin_clzll(a);for(int b=top;b>=0;b--){r=(Wide)r*r%q;if((a>>b)&1)r=(Wide)2*r%q;}return r;}
int main(int argc,char**argv){if(argc!=4)return 2;U a=strtoull(argv[1],0,10),bound=strtoull(argv[2],0,10),cap=strtoull(argv[3],0,10);if(!a||a>1000000000||bound>1000000000000000000ULL||!cap)return 2;U stride=6*a,q=0,r=0,k=0,hit=0;double start=now();
for(k=1;k<=(bound-1)/stride;k++){q=stride*k+1;r=power(a,q);if(((Wide)r*r+r+1)%q==0){hit=q;break;}if((k&16383)==0&&now()-start>=cap)break;}
printf("{\"a\":%"PRIu64",\"bound\":%"PRIu64",\"last_q\":%"PRIu64",\"last_k\":%"PRIu64",\"proper_factor\":%"PRIu64",\"two_to_a_mod_factor\":%"PRIu64",\"seconds\":%.6f,\"limitation\":\"A zero factor is no conclusion beyond this bounded search. Properness requires q<2^(2a).\"}\n",a,bound,q,k,hit,hit?r:0,now()-start);return 0;}
