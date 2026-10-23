# Conditional S3 continuation: packing lemma with |S| >= 2m+3, exclusion of delta0=2 and of delta'=1 uniformly over BASE2, v1

Owner OlsonSTABSuccessor.  Written after /bin/date 2026-10-19T08:04:05-0700.  Status: CANDIDATE_UNVERIFIED / CONDITIONAL S3 continuation.
Scope frozen in S3-core-scope-v1.md 08b1c8622b5da66872868402b08fb3b78d6993002463fc84620970c43202962a (P1-P3).  Written only; no computation.  Candidate BASE2
proof-LS-BASE2-cells-v2.md fd6e64e575da62603b6923b33e8bc614994be55c0a1b6c0d4113d3ee493d2306 (L1 and B2-1) is NOT an accepted import: its packing argument is expanded
below with the changed length hypothesis checked; all consequences using L1 remain explicitly conditional pending parent review.
No use of LS(17,12) or LS(23,16) as an assumption.  This does not prove S3 (all BASE2 LS cells), LS+ or STAB.

## 0. Setting and accepted inputs
p=6m-1 prime,m>=3,kappa=4m,e=2m-1,h:=e-1=2m-2.  A threshold LS counterexample Y would have |Y|=14m,(ZP_kappa) and a zero-sum of length
>=2p+2.  Accepted RED, DGM-p, the threshold dichotomy and LS-II' give g=g0 a generator, M=2p-d with d:=delta0,1<=d<=h-1,
U (mu-terms in [1,p-1]) of size2m+2+d and
 (F*) rho(W)<=h => |W|+2rho(W)<=d-1 for every occurrence sub-multiset W<=U,
as |U|+2h<=2p and CF(a) excludes the opposite inequality.
Choose an inclusion-maximal zero-sum sub-multiset Z0<=U (mod p, possibly empty), put k:=|Z0|<=d-1, delta':=d-k>=1, U':=U-Z0.
Then U' is zero-sum-free, |U'|=2m+2+delta', and adjoining Z0 to W'<=U' gives
 (F') rho(W')<=h => |W'|+2rho(W')<=delta'-1.
Candidate L1 says there is W*<=U with sum=-1(mod p), |W*|>=d+2.  Its basis is the accepted shortest-long bound SLZ3 plus parity:
2p+2<=|T|<=3kappa+1=2p+3, so |T|=2p+2; writing T=g^i W* gives sigma_int(W*)=-1(mod p) and 2p+2-|W*|=i<=M.

Accepted source authorities (same literal scopes as BASE2 package): prerequisite ca6e4ca75bba7f88024667951e160ffb8555d99389d50e34fd2cceef31b420e0; delta
ac8ead13b89b4d89dc62d13fd2a20dbf7957b1b427be46bf7e8db5bbb8d5a4c5; RED23d1a488c5868484aad436cd705ea0e99525e0978d2990c6f124424d9b1ca612; SLZ32b7b08a3ec861e953e35d2802d8deba2ae584edeed36f04350fc3a9c6fa1ae24.
CF scope E1 and longness R4 remain mandatory.  No index-one theorem, AP', greedy lemma or inaccessible inverse theorem is used here.

## 1. P1: packing lemma (length lower bound, not equality)
Let S be a sequence over the nonzero residues of Z_p with n:=|S|>=2m+3, and suppose every nonempty occurrence sub-multiset sum
avoids [0,h].  Then no W<=S with sum=-1(mod p) has |W|>=3.
Proof.  S is zero-sum-free.  A:={0} union Sigma(S) (nonempty subset sums), sigma:=sigma(S) in [h+1,p-1].  Prefix sums are distinct
and nonzero, so |A|>=n+1>=2m+4.  Complementation gives A=sigma-A, hence A avoids both [1,h] and [sigma-h,sigma-1].
If sigma>=4m-3, these are disjoint nonwrapping h-arcs, so |A|<=p-2h=2m+3: impossible.  Thus 2m-1<=sigma<=4m-4; their union is
[1,sigma-1], so A subset {0} union [sigma,p-1].  Negate S to Q: all nonempty subset sums lie in [1,B] with B:=p-sigma<=4m, while
n+1<=|A|<=B+1 gives B>=n>=2m+3.  This is the only place the old proof used |S|=2m+3; the lower bound is sufficient.
Suppose V:=-W<=Q has total1(mod p) and t:=|V|>=3.  Every proper nonempty subset sum x of V and its complementary sum1-x lie in
[1,B], forcing x in J:=[p+1-B,B]=[6m-B,B].  In particular each individual term of V has its integer representative in J.
- B<=3m-1 makes J empty.
- 3m<=B<=4m-1: each pair sum exceeds B and is below2p, hence if proper it must equal p+y with y in J, and is at least12m-1-B.
  If t>=4, a proper triple lies in [18m-1-2B,3B] subset [10m+1,12m-3]; after subtracting p its residue lies in [4m+2,6m-2],
  outside J, and subtracting2p is negative.  Impossible.  If t=3, its sum lies in [18m-3B,3B] subset [6m+3,12m-3], which contains
  neither p+1=6m nor2p+1=12m-1 (nor any other integer congruent1 in that range).  Impossible.
- B=4m: J=[2m,4m]; a proper pair has sum4m (both2m) or8m-1 or8m.  If t>=4, a proper triple must have sum in p+J=[8m-1,10m-1].
  If it has a high pair (sum>=8m-1), its third term is <=2m, hence2m.  Pairing this2m with either other term forces that term
  to equal2m (2m+z<=6m cannot be8m-1 or8m).  This contradicts the high pair.  With no high pair all terms are2m, and the triple
  has residue1, not in J.  Thus t=3.  Its total is p+1=6m (forcing (2m)^3) or2p+1=12m-1 (pair constraints force
  (4m-1,4m,4m)).
  As n>=2m+3>=9, there is a term y of Q outside this triple.  For (2m)^3: y+1 must lie in [1,4m], giving y<=4m-1; y+4m then
  forces y>=2m; y+2m then forces y<=2m, hence y=2m.  All Q terms must be2m, and five have sum10m=p+(4m+1), residue4m+1>B.
  For (4m-1,4m,4m): y+1 forces y<=4m-1, y+4m forces y>=2m, y+4m-1 forces y>=2m+1; but y+8m-1 has residue y+2m in
  [4m+1,6m-1] (endpoint6m-1 is0), outside [1,4m].
Every case is impossible.  All pair/triple tests use occurrence sub-multisets; five terms exist since n>=9.  []

## 2. P2: exclusion of d=delta0=2 (conditional on L1)
For d=2, (F*) forbids every nonempty W with rho in [0,h]: positive rho gives |W|+2rho>=3>1; rho=0 requires |W|>=2 since U has
nonzero terms, again>1.  Hence U satisfies P1 with |U|=2m+4.  L1 would give W* of sum-1 and size>=4: contrary to P1.  So d=2 is
impossible at EVERY BASE2 cell, conditional on candidate L1 (not merely the m<=4 cases handled by I-small).  []

## 3. P3: exclusion of delta'=1 (nonempty Z0 argument is independent of L1)
If delta'=1 and Z0 is empty, d=1 and P1+L1 exclude the case (candidate B2-1).  Suppose Z0 is nonempty.  Then k=d-1>=2 (nonzero
terms cannot form a one-term zero-sum), so3<=d<=h-1.  U' has length2m+3, and (F') gives no nonempty subset sum in[0,h].
For A':={0} union Sigma(U'), the first paragraph of P1 applies: |A'|>=2m+4 and A' subset {0} union T, T:=[h+1,p-1], |T|=4m.
Let z be any occurrence in Z0, with residue zeta in[1,p-1].  The complementary occurrence sub-multiset Z0-{z} has size d-2 and
sum -zeta.  For any W'<=U', if W:=(Z0-{z}) union W' had rho(W) in[1,h], then
 |W|+2rho(W)>=(d-2)+2=d,
contrary to(F*).  Thus A' avoids the complete translated interval zeta+[1,h] modulo p.
(a) If p-h<=zeta<=p-1, that interval contains0, contrary to0 in A' (equivalently take W' empty).
(b) If h+1<=zeta<=p-h-1, the interval [zeta+1,zeta+h] is a nonwrapping h-interval fully contained in T.  Therefore
 |A'|<=1+|T|-h=1+4m-(2m-2)=2m+3,
contrary to |A'|>=2m+4.
(c) Consequently every zeta<=h.  The singleton {z} in(F*) gives1+2zeta<=d-1, so all residues zeta lie in[1,floor((d-2)/2)].
If that range is empty we already have a contradiction.  Otherwise regard them as positive integers.  Order the k=d-1 terms of
Z0 arbitrarily; let S_j be the integer prefix sum and w_j:=j+2S_j.  Since S_k>=k, w_k>=3k=3(d-1)>=d.  Let j be the first with
w_j>=d.  Singleton bounds give j>=2, and w_(j-1)<=d-1 gives2S_(j-1)<=d-j.  The added term obeys2zeta_j<=d-2, hence
 1<=S_j<=(2d-j-2)/2<=d-2<=h-3<h.
Thus rho(of this j-term prefix)=S_j (no modular wrap) lies in[1,h], while j+2S_j=w_j>=d: contrary to(F*).
No nonempty Z0 can occur with delta'=1.  Together with the empty case, delta'=1 is impossible at every BASE2 threshold,
conditional on L1 only for the empty-Z0 case.  []

## 4. Exact delta and next obstruction
Conditional on L1/P1, the BASE2 residual shrinks from 2<=d<=2m-3 to
 3<=d<=2m-3, 2<=delta'=d-|Z0|<=d,
with |Z0| either0 or>=2.  In particular m=5 (p=29) still has the short-core value delta'=2 below the index-one threshold
|U'|+1>=floor(p/2)+2, which is equivalent to delta'>=m-2.  P3 does not exclude delta'=2.
Distinct next lever (not used): at delta'=2, F' again forbids every nonempty residue in[0,h], and |U'|=2m+4.  The same
complementary-Z0 argument forbids z+[2,h] for A', whose larger cardinality partly compensates for the shorter forbidden interval;
it permits z=-1 as an extra endpoint (besides tiny positives), so a balance/first-crossing argument rather than the
positive-only proof of P3 is needed.  No claim at delta'=2 is made here.
