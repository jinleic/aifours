# S3: few-sums normalization of EVERY BASE2 core and pinning its multiplier to -1, conditional on Lev 2022 Theorem 2, v1

Owner OlsonSTABSuccessor. Written after /bin/date 2026-10-19T08:57:55-0700. Status: CANDIDATE_UNVERIFIED, CONDITIONAL on the new
external theorem. Exact application frozen first in S3-Lev-application-scope-v1.md
1450aa85c6dfca9504201b499296b0154b3f9c8539de52fbd8aadd242f03c206. No computation or model call. No scientific claim of novelty.

## 0. Source and import boundary
New external input (NOT yet parent-accepted): V. F. Lev, Zero-sum-free sequences with few subsequence sums,
arXiv:2110.01081v3, displayed date 01 Jun 2022, Section 1 Theorem 2 and the inclusive Sigma definition immediately above it:
https://arxiv.org/html/2110.01081v3#Thmtheorem2.
Primary statement read directly; normalized local record source-Lev-2110.01081v3-statement-v1.md
c2cb60cc9b4a0096e7e56db0ccee15969ec3d1cbc031d63d920ef7e75388ab7d. That local hash binds the transcription, not remote HTML bytes. No proof-body replay.
The theorem says: a zero-sum-free sequence of length n in an abelian group with fewer than 2n subsequence sums INCLUDING 0 can
be ordered as (x_i a) with integers 1=x_1<=...<=x_n and x_(j+1)<=sum_(i<=j)x_i (NO extra '+1'); all subset sums form
{0,a,...,Sa}, S=sum x_i<ord(a) when a has finite order. All consequences here are conditional on exactly that theorem.

Accepted inputs: CF(a) through E1, DGM-p, LS-threshold dichotomy (parent verdict ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0);
LS-II' (parent delta verdict ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5); RED (23d1a488c5868484aad436cd705ea0e99525e0978d2990c6f124424d9b1ca612).
AP (proof-LS-caseII-v2.md Sec. 2 through mandatory erratum-2-prereq R6, fb136e6ef71f7250774c3102a35c88a9709fee827091df84f67b433fb13106d5), accepted prerequisite
verdict item 8. AP': proof statement in proof-LS-caseI-smalldelta-v1.md read through erratum-1-delta-APprime.md D1
e035f8d14b6bcb57c0af0d5beb170ddf3471674490583e66b75d0d34cc90c461, accepted delta verdict item 2, with mandatory delta erratum16cc1823....
No index-one theorem, separate greedy theorem, unreviewed P1/P2/P3 or other inaccessible inverse theorem is imported.

## 1. Setting
p=6m-1 prime,m>=3,kappa=4m,e=2m-1,h=2m-2. A threshold LS counterexample Y is odd,|Y|=14m,has (ZP_4m) and a long zero-sum.
Accepted reductions give dominant generator g=g0, M=2p-d,1<=d<=e-2=h-1, CF mu-multiset U (all terms in[1,p-1]), |U|=2m+2+d.
For W<=U, let sigma_int(W) be the integer mu-sum and rho(W) its least residue mod p. Since |U|+2h=p-1+d<=2p, CF(a) implies
 (F*) rho(W)<=h => |W|+2rho(W)<=d-1.
Z0<=U is any inclusion-maximal mod-p zero-sum (possibly empty),k:=|Z0|<=d-1; U':=U-Z0 is zero-sum-free;
delta':=d-k>=1, n:=|U'|=2m+2+delta'. Adjoining occurrence-disjoint Z0 to W'<=U' gives
 (F') rho(W')<=h => |W'|+2rho(W')<=delta'-1.
Every delta' is an INTEGER with1<=delta'<=d<=h-1. No LS theorem is assumed.

## 2. NORM: exact Lev application to all core lengths
Put t:=max(1,floor(delta'/2)). Then1<=t<=h and A:=Sigma_inc(U') avoids the ordinary integer interval[t,h] of nonzero residues.
Indeed a representation of rho in[t,h] would be nonempty (rho!=0), and would have
 |W'|+2rho>=1+2t>delta'-1,
contrary to(F'). The strict inequality holds for delta'=1 as t=1; for even delta'=2q it gives1+2q=delta'+1; for odd delta'=2q+1>=3
it gives1+2q=delta'. Thus, counting the empty sum 0 as Lev does,
 |A|<=p-(h-t+1)=4m+t<4m+4+2delta'=2n.
For the last inequality t<=delta' and delta'>=1 suffice; the avoided interval does not include0, so there is no empty-sum
convention error. U' is nonempty (n>=2m+3>=9) and zero-sum-free by maximality of Z0.

CONDITIONALLY apply Lev Theorem 2: after ordering, mu_i=x_i a with positive integers1=x_1<=...<=x_n,
x_(j+1)<=sum_(i<=j)x_i and Sigma_inc(U')={0,a,...,Sa},S:=sum x_i<ord(a). Since x_1=1, a is an actual nonzero U' term; in C_p,
a!=0 has ord(a)=p. Therefore
 n<=S<=p-1, and every integer0<=s<=S is a coefficient sum of an occurrence sub-multiset of U'.
This holds even when n<=(p-1)/2; no length hypothesis from the older index-one theorem was used. []

## 3. PIN: a=-1 throughout this exact BASE2 core setting
Let b:=a^(-1) mod p, nonzero, and I:=[S+1,p-1], an arc of size l=p-1-S<=p-1-n=4m-4-delta'.
For every rho in[t,h], the point rho*b mod p lies in I: otherwise its representative s would be in[0,S], and the full Lev
coefficient interval would produce a sub-multiset of residue rho, contrary to the avoidance just proved. rho is nonzero,
so s=0 cannot be an exception. The progression points are distinct as its length is<p and b!=0.

Case delta'>=2. t=floor(delta'/2) and delta'>=2t. Put N:=h-t>=1; the progression has N+1=h-t+1 points and
 l<=4m-4-delta'<=4m-4-2t=2N.
Furthermore3N=3(h-t)=6m-6-3t<p=6m-1, and t<=m-2 for1<delta'<=2m-3 (at m=3 this gives t=1), so N>=1.
Accepted AP (corrected R6) yields b in{1,-1}. b=1 is impossible because the rho=t point is t<=h<n<=S, not in I.
Hence b=-1 and a=-1.

Case delta'=1. t=1, n=2m+3, and the h points rho*b (rho=1,...,h) lie in I with
 l<=4m-5=2N+1, N:=h-1=2m-3>=1,
 3N+2=6m-7<p.
Accepted AP' (corrected D1) yields b in{1,2,-1,-2}. b=1 or2 puts the rho=1 point inside[1,S]. If b=-2, the rho=h point has
least representative p-2h=2m+3=n<=S (no wrap since2h=4m-4<p), again not in I. Thus b=-1 and a=-1.

In both cases the rho=h point is p-h=4m+1, so 4m+1>=S+1 and S<=4m. Writing E:=S-n>=0 gives
 E<=h-delta'.
Conclusion (CONDITIONAL on Lev): every BASE2 core in Sec. 1 has
 mu_u=-x_u (mod p), x_u>=1, n<=S=sum x_u<=4m, E=S-n<=h-delta',
and all integer coefficient sums0..S occur. No arbitrary translation is used; the multiplier is pinned relative to the
original CF mu-residues, not to a translated sequence. []

## 4. Exact range and what this candidate does not claim
NORM and PIN concern threshold BASE2 counterexamples with CF data w.r.t. g0, p=6m-1 prime,m>=3. They give a positive-coefficient
normal form for EVERY delta', conditional on Lev's few-sums theorem, and remove the former generic half-order length obstruction
only for these forbidden-residue cores. They do not contradict optimality examples for general zero-sum-free sequences.
No full LS(p,4m) conclusion follows from this file alone: Z0 and the accepted L1 witness still must be controlled. The next
scope item ZCLASS in S3-Lev-application-scope-v1.md is still an obligation, not a consequence asserted without proof.
No universal LS/LS+/STAB, no word-level ordered-Olson, no novelty or matched-SOTA claim.
