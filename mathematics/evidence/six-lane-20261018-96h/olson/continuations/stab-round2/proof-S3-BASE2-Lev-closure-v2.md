# S3: all BASE2 LS cells via Lev normalization, conditional written closure candidate, v2

Owner OlsonSTABSuccessor. Written after /bin/date 2026-10-19T09:07:16-0700. v2 supersedes v1
c12d3ec1a8c4fd42f2522c10cc5c0ea58fee9f7354dc70eb6ba18f105f2ac996 (never sent). Only correction: Sec. 2 first display now reads1<=R<=h, not
1<=R<=h-1; the original parenthetical already derived R<=h, and all subsequent steps used only that weaker, correct bound.
No proof strategy, conclusion or other text changed. Status: CANDIDATE_UNVERIFIED, explicitly CONDITIONAL on
the new external Lev theorem and its unreviewed normalization application. Same assigned BASE2 target, not an extra problem slot.
Scope frozen first: S3-Lev-application-scope-v1.md 1450aa85c6dfca9504201b499296b0154b3f9c8539de52fbd8aadd242f03c206, items ZCLASS/ASSEMBLY.
No computation, no model call, no novelty, Lean, human-review or word-level claim.

## 0. Exact statement and dependency boundary
CONDITIONAL Theorem BASE2-Lev. For every prime p=6m-1,m>=3 and kappa=4m=(2p+2)/3, every odd sequence Y over C_(2p) satisfying
(ZP_kappa) and |Y|>=p+2kappa+1=14m has (S1_kappa). Equivalently LS(p,(2p+2)/3) holds at all first p=2(mod3) cells, including
p>=29, IF the published Lev Theorem2 and its application in the normalization candidate are valid at the stated scopes.
This is the family S3, not LS for all kappa. This file does not assert LS+, STAB, INV* or ordered Olson.

New and NOT parent-accepted:
- Lev, Zero-sum-free sequences with few subsequence sums, arXiv2110.01081v3, Theorem2 (01 Jun 2022), primary statement read at
  https://arxiv.org/html/2110.01081v3#Thmtheorem2; local statement record
  source-Lev-2110.01081v3-statement-v1.md c2cb60cc9b4a0096e7e56db0ccee15969ec3d1cbc031d63d920ef7e75388ab7d. Only statement read; proof not replayed.
- proof-S3-Lev-normalization-v1.md 83a67e6a8135b40f84794476b3b8e75abaaf45f2e19f0b42a03a4caf65ae9694: NORM/PIN (a=-1, S<=4m) at ALL BASE2 cores,
  using accepted AP(R6)/AP'(D1). The strict few-sums inequality is checked there, even below the generic half-order threshold.

Accepted:
- RED, verdict23d1a488c5868484aad436cd705ea0e99525e0978d2990c6f124424d9b1ca612; CF(a) through E1, DGM-p and the threshold dichotomy, verdict
  ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0; LS-II' (without H'), verdictac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5.
- L1, exact threshold-counterexample CF setting w.r.t. g0: BASE2 verdict
  9df92bdafcb73cff034695ece0c5234fd3cb1bb29821ab30182b30b88fdab553, sourceproof-LS-BASE2-cells-v2.md fd6e64e575da62603b6923b33e8bc614994be55c0a1b6c0d4113d3ee493d2306
  through erratum-1-BASE2-consolidated-v1.md 05749bc842c94cc628d05383d301551d62255adede75c5f1876295180afd780b. L1 uses SLZ3 only for shortest |T|.
No unreviewed P1/P2/P3 from proof-S3-lowdefect-core-v1.md is assumed. No index-one length theorem or extra inaccessible inverse
result is used. No standalone LS(17,12) or LS(23,16) conclusion is used as an induction base.

## 1. Reduce to the normalized threshold setting
Assume a counterexample to the asserted LS cell. Accepted RED supplies one of length14m; accepted reductions and the conditional
normalization candidate give:
 p=6m-1 prime,m>=3,kappa=4m,e=2m-1,h=2m-2;
 g=g0 generator,M=2p-d,1<=d<=h-1;
 U the nonzero CF mu-multiset, |U|=2m+2+d;
 (F*) rho(W)<=h => |W|+2rho(W)<=d-1 for every occurrence sub-multiset W<=U.
Here rho(W) is the least residue of the integer sum of mu-values. F* follows from CF(a), since
|U|+2h=6m-2+d=p-1+d<2p (d<=2m-3<p).
Z0<=U inclusion-maximal mod-p zero-sum (possibly empty), k:=|Z0|<=d-1, delta':=d-k>=1;
U':=U-Z0 zero-sum-free, n:=|U'|=2m+2+delta'. Conditional NORM/PIN give
 mu_u=-x_u (mod p), x_u>=1, S:=sum_(u in U') x_u, n<=S<=4m,
 EVERY integer s in[0,S] is the x-sum of an occurrence sub-multiset W'_s<=U'.
L1 supplies W*<=U with sum=-1(mod p) and |W*|>=d+2. It remains to show this is impossible with the normalized core.
All sums using the signed Z0 representatives below are distinguished from CF's nonnegative integer mu-sum.

## 2. ZCLASS: every Z0 term is tiny positive or a controlled negative
Let z be a term of Z0, with least mu-residue zeta in[1,p-1]. Put
 R:=p-S-h=4m+1-S, so 1<=R<=h
(the upper bound follows from S>=n>=2m+3, giving R<=2m-2=h; only R<=h is used below).
If h<=zeta<=S+h, take s:=zeta-h in[0,S] and W:={z} union W'_s. Its mu-sum is congruent to h, and
 |W|+2h>=1+2h>d-1,
against(F*). If 1<=zeta<h, the singleton {z} in(F*) gives1+2zeta<=d-1. Thus every z has one of two types:
 POSITIVE: zeta in[1,floor((d-2)/2)], with signed representative z_tilde:=zeta;
 NEGATIVE: zeta>=S+h+1, so nu_z:=p-zeta in[1,p-S-h-1]=[1,R-1], with signed representative z_tilde:=-nu_z.
When R=1 there are no negative terms. Let Z+ and Z- denote these occurrence sub-multisets. For V+<=Z+ let P(V+):=sum zeta;
for V-<=Z- let N(V-):=sum nu; the signed-representative sum of V+ union V- is P(V+)-N(V-), congruent to its mu-sum modulo p.

## 3. Positive-part bound by a weighted first crossing
Put q:=|Z+|, P:=P(Z+). Claim q+2P<=d-1. If not, list the positive occurrences in any order and let j be the first index with
w_j:=j+2P_j>=d. Singleton bounds give w_1<=d-1, so j>=2. From w_(j-1)<=d-1 we have2P_(j-1)<=d-j; the added term obeys
2zeta_j<=d-2. Therefore
 1<=P_j<=(2d-j-2)/2<=d-2<=h-3<h<p.
The corresponding prefix has rho=P_j (no modular wrap) and |prefix|+2rho=w_j>=d, contrary to(F*). Thus
 q+2P<=d-1; in particular P<=(d-1)/2<h.
Empty positive part (including all small d for which the singleton interval is empty) gives q=P=0 and satisfies this bound.

## 4. Negative-part bound: cross at R=p-S-h, not at p-S
Claim N:=N(Z-)<=R-1. It is automatic if Z- is empty (R>=1). Otherwise suppose N>=R, and list the negative occurrences in any
order. The first prefix V with N_V>=R satisfies
 R<=N_V<=2R-2
because each nu_z<=R-1; thus R>=2. Set
 s:=p-N_V-h.
The upper bound s<=S follows from N_V>=R=p-S-h. The lower bound is
 s>=p-(2R-2)-h=2S+h-p+2>=5+2delta'>=7>0,
using S>=n=2m+2+delta', h=2m-2 and p=6m-1. Hence s belongs to[0,S] and a core subsequence W'_s exists from the full Lev
coefficient interval. Form the occurrence-disjoint W:=V union W'_s. Its signed-representative sum equals
 -N_V-s=h-p,
so rho(W)=h and |W|+2h>=1+2h>d-1: against(F*). This proves N<=R-1.
Only the coefficient-interval existence is used here; no estimate of |W'_s| from an excess parameter, no ordering theorem and
no half-order length hypothesis enter. F* is applicable because W is an actual occurrence sub-multiset of U.

## 5. Exclude the accepted L1 witness
Write W*=W' union Z*, W'<=U' with integer x-sum s in[|W'|,S], Z*<=Z0 of size ell. Let
 zeta_tilde:=sum_(z in Z*) z_tilde,
where the signs are from Sec. 2. Then
 -(R-1)<=zeta_tilde<=P, 0<=s<=S,
so the signed-representative difference tau:=zeta_tilde-s lies in
 [-(R-1)-S, P]=[-p+h+1, P],
strictly inside(-p,p-1) because h>=1 and P< h <p-1. Its residue is sigma(W*)=-1(mod p), by L1. The only possible integer in
that range congruent to-1 is tau=-1. Thus s=zeta_tilde+1.
The witness size requirement and x_u>=1 now imply
 d+2<=|W*|=|W'|+ell<=s+ell=zeta_tilde+1+ell,
so zeta_tilde>=d+1-ell>=2 (ell<=|Z0|<=d-1). Also zeta_tilde<=P<h. Therefore Z* itself has least mu-residue
rho(Z*)=zeta_tilde in[2,h], and
 |Z*|+2rho(Z*)=ell+2zeta_tilde>=d+1+zeta_tilde>d-1,
contrary to(F*). Hence no threshold counterexample exists. Accepted RED gives the stated LS cell for all |Y|>=14m. []

## 6. Exact delta, conditionality and open scope
If independently verified, this argument plus the newly read external Lev theorem closes S3: ALL first p=2(mod3) LS cells
(p,kappa)=(6m-1,4m),m>=3. It does not use the cell-specific proofs at p17/p23; it extends their normalization/pinning mechanism by
a strict few-sums application, not by enlarging a finite range. Parent must independently admit the external statement/application
and review both this file and the normalization file; no acceptance is inferred from Lev's theorem being readable or from the
previous accepted BASE2 verdict.
LS at other kappa remains outside this file, as do general LS+, STAB, INV* and ordered Olson. All word-level transfers and
priority/novelty assessments remain with the parent. There is no scientific computation or Lean verification in this proof.
