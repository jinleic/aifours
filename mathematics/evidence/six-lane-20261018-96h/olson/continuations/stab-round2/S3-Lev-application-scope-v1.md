# S3 with Lev Theorem 2: frozen exact application and next pinning statement before written derivation, v1

Owner OlsonSTABSuccessor. Written after /bin/date 2026-10-19T08:53:31-0700. Parent supplied the primary lead; I read Section 1's
inclusive Sigma definition and Theorem 2 directly at https://arxiv.org/html/2110.01081v3#Thmtheorem2 (v3, 01 Jun 2022).
Status: SCOPE ONLY, CONDITIONAL on the newly read external theorem; not a parent-accepted correctness import. Written only.

## Setting (unchanged BASE2 target)
p=6m-1 prime,m>=3,kappa=4m,e=2m-1,h=2m-2. Threshold odd Y,|Y|=14m,(ZP_4m),a long zero-sum. Accepted reduction gives
g=g0,d=delta0,1<=d<=h-1,|U|=2m+2+d, F*:rho(W)<=h=>|W|+2rho(W)<=d-1. Maximal zero-sum Z0, k=|Z0|<=d-1,
delta'=d-k>=1, U'=U-Z0 zero-sum-free, n=|U'|=2m+2+delta', F' with delta'. Accepted BASE2 L1 gives sum-1 W*<=U of size>=d+2.
The separate unreviewed S3 candidate3847ade3 (P1-P3) is NOT imported in this new route.

## Exact statements under test (none assumed)
NORM: Let t=max(1,floor(delta'/2)). Every nonempty subset sum of U' avoids [t,h], so the inclusive set A=Sigma_inc(U') satisfies
|A|<=p-(h-t+1)=4m+t<2n. Conditional on Lev Theorem2, U'=(x_i a),1=x_1<=...<=x_n, x_(j+1)<=sum_(i<=j)x_i,
S=sum x_i<p, and A={0,a,...,Sa}. Here a!=0 and ord(a)=p must be derived from nonzero U' terms, not silently assumed.
PIN: In this exact setting the Lev multiplier is a=-1, using accepted AP for delta'>=2 and AP' for delta'=1, on the progression
rho*a^(-1),rho in[t,h], inside [S+1,p-1]. All progression-length/arc-size inequalities must be checked explicitly. Expected S<=4m.
ZCLASS: If PIN holds, every Z0 residue is either tiny positive (<=floor((d-2)/2)) or negative with magnitude at most4m-S.
The weighted-prefix first-crossing argument should bound the FULL positive part by q+2P<=d-1. A different negative first crossing
will be tested at N=p-S-h (not the older p-S threshold), correcting to residue h via an available coefficient sum p-N-h.
ASSEMBLY: Only if the last bounds close, exclude the L1 witness and deduce LS(p,4m) at all BASE2 cells. Until every step is written
and independently checked, this remains a target, NOT a universal LS claim. No LS+, STAB, INV* or ordered-Olson conclusion.

## Preservation of the paused delta'=2 route
S3-delta2-scope-v1.md remains unchanged. Its direct short-core analysis is paused in favor of this independently normalized
route. If the Lev route fails, preserve its exact obstruction and return to the signed-endpoint problem in that scope; do not
silently treat the external theorem as already accepted or the earlier S3 candidate as proved.
