# UPAR v1: uniform parity/mass extension, a first-exit count, and a complete two-branch residual

Owner OlsonThirdCutWindow, same throttled math2 slot. Written by hand after /bin/date 2026-10-21T04:44:43-0700.
Scope UPAR-scope-v1.md (SHA256 01f0fdf75327dfa5d6dec5a3fa2a616ae1a336d93e76b1b99327f37bb1d2b641), frozen
2026-10-21T04:13:04-0700 before NEW uniform derivation. Authority written-olson-full-uniform-parity-transition-v1.json,
SHA256 91514b1ccc8486938c79183cd8816b6b449a7c758c4cf6ec3ec45a022dde1091, LF1-57 (absolute paths in Sec.8).
STATUS: WRITTEN CANDIDATE, NOT REVIEWED OR ACCEPTED. FULL T IS NOT EXCLUDED. New uniform ranges are proved below;
PAR-COVER is the exact first UNPROVED uniform step, with complete residual R_PAR. Named(12,29),(13,31) are proved;
(13,29),(14,31),(17,37) remain open in explicit late-jump residuals. No residual existence or converse is claimed.

## 0. Full target, proved region and exact open boundary

T: p>=17 prime, floor((p+7)/4)<kappa<=(p-3)/2. A target word is a length4p-2 avoider over D_(2p), with no identity-2p
subword in increasing original index order, SOME admissible NF with terminal k=p+1,kappa_hat=kappa. Arbitrary extra
reflection-pair placement in odd blocks and the genuine empty-run rule are retained. No o_F, nonempty-run, rotation-
pair or rigidity premise. EVERY frame of EVERY such NF is considered, not selected UB-failing frames.

Put d=(p+1)/2-kappa. The new proved region is
  T_PAR := {T:kappa<=4d} UNION T1,
  T1 := {T:p=1mod4, kappa<=(3p+9)/8} UNION {T:p=3mod4, kappa<=(3p+11)/8}.             (Region)
THEOREM UPAR-P (proved). In EVERY frame at every (kappa,p) in T_PAR, Xi(S_ev)+Xi(S_od)<=-1, hence no target NF exists
there by accepted UMR identity. Accepted UFC T0 is retained in full and lies inside kappa<=4d. The additional
half-boundary family p=8d+7,kappa=3d+4 is proved for all d>=2 with p prime; it supplies all of T1 not already covered.
The general-parameter arguments are re-derived from literal UMR, not from FC1023 constants/internal lemmas.
THEOREM UPAR-R (proved reduction on ALL remaining T). Every hypothetical surviving frame in T\T_PAR induces data
in the explicit fixed-parameter finite relaxation R_PAR of Sec.6. Its TWO possible types are a very-high positive
balanced near-A^c top, or a late near-A to near-A^c sorted-chain jump. No residual tuple or actual frame is asserted
to exist. Excluding both types for actual target frames is PAR-COVER, NOT proved (Sec.6.4). This retains the full
uniform target, both residue classes and every proved subrange, rather than silently narrowing them.

Only accepted UMR and accepted UFC U0/E0/ENV/U1 at exact scopes are premises. UFC HIGH-COVER remains unproved.
FC1023 is accepted only at(10,23); its internal fixed-cell counts are inspiration, not a uniform premise. Full
ordered Olson, other-k, priority/novelty, human-referee, Lean and runtime claims are not made.

## 1. Literal UMR data; all-run parity and the balanced parameters

For (kappa,p) in T put h=(p+1)/2=kappa+d, N=2h, R=p-1+2kappa=4kappa+2d-2, g=2d, delta=2kappa-2d. d>=2.
In ANY UMR frame (one always exists) the R letter OCCURRENCES partition into run sets L_i (i modN), each with odd
nonzero integer label c_l. Put A={c_l<0}, A^c={c_l>0}, a=|A|, a'=R-a, nu=sum_A |c_l|, e=sum_all(|c_l|-1). Then
  nu>=a, e>=nu-a>=0, a'>=(3kappa+2d)/2.                                             (D1)
The excess inequality follows because the contribution from A is nu-a and every other contribution is nonnegative.
Write L(Q)=union_(i in Q)L_i, l(Q)=|L(Q)|, n(Q)=number of nonempty runs, E(Q)=number of empty runs,
Theta(Q)=sum_(i in Q)theta_i. Literal UMR Lemma10 and odd labels give
  theta_i=sum_(l in L_i)c_l=|L_i| (mod2); empty theta_i is NONZERO EVEN.               (D2)
This is ALL-RUN parity, not only empty-run parity. For central r in[d,kappa+1], every r-subset Q of either alternating
h-run set S_ev={0,2,...,N-2} or S_od={1,3,...,N-1} is independent/proper with m(Q)=r. Set
  q(Q)=|L(Q) symdiff A|, q'(Q)=R-q(Q), eps(Q)=q(Q) mod2,
  ell_r=2kappa+2-2r, M_r=2r-2d,
  x_r=max(eps,ell_r-q,M_r-q'), y_r=max(eps,M_r-q,ell_r-q'),
  e-2d+2-nu-y_r(Q)<=Theta(Q)<=-2-nu+x_r(Q).                                         (W)
The same bound holds for every central mixed run set P with r=m(P). For upper counts we may replace x by
chi_r=max(1,ell_r-q,M_r-q'), a WEAKER upper bound. UMR-F gives U'=Theta; no new realisation assertion is used.
Xi(S):=Theta(S)+nu+d. Only at the final contradiction in a count proof use
  Xi(S_ev)+Xi(S_od)=e>=0.                                                          (ID)
Citations for all these literal imports: UMR LF18-28,49-56,64-68,88-118,137-139,161-165,201-209,238-239,252-258,
through its accepted verdict and both errata (Sec.8). The modified Lemma13 link is not extended.

Define alpha(Q)=|A\L(Q)|, beta(Q)=|L(Q) intersect A^c|, alpha'(Q)=|A^c\L(Q)|, beta'(Q)=|L(Q) intersect A|.
Then q=alpha+beta, q'=alpha'+beta', l=a-alpha+beta. Disjoint run sets have disjoint letter sets. For disjoint Q1,Q2,
  a<=alpha(Q1)+alpha(Q2), a'<=alpha'(Q1)+alpha'(Q2),
and at most alpha'(Q1)+alpha(Q2) letters lie outside both. In particular, if Q_i lies in the opposite alternating
sets S_i and B_i subset S_i\Q_i, then
  l(B1)+l(B2)<=q'(Q1)+q(Q2).                                                       (Mass)
These follow by assigning each outside letter to A^c\L(Q1) or A\L(Q2); n(Q)<=l(Q) throughout.

LEMMA 1 (signed cost, re-derived). If theta_i>=0, theta_i+|L_i|>=2. If theta_i<=0, -theta_i+|L_i|>=2.
Proof. Empty theta is nonzero even, so its signed magnitude is>=2. A singleton run has odd theta, so a nonnegative
theta is>=1 and a nonpositive one<=-1. A run of length>=2 contributes>=2 through length alone. Negation preserves
parity. Thus all-nonnegative Q has Theta(Q)+l(Q)>=2|Q|, and all-nonpositive Q has Theta(Q)<=l(Q)-2|Q|. []
Sort each alternating set by decreasing theta with fixed arbitrary tie choices. J_r is top r, t_r its last theta,
B_r=S\J_r. Negative bottom sums are<=-(h-r)-E(B_r); if t_r<=-2 they are<=-2(h-r). If t_r=-1 then
Theta(J_r)>=2r-3n(J_r), since empty top theta>=2 and nonempty top theta>=-1.
Since R>ell_r+M_r (difference p+2d-3>0), exactly one upper TYPE holds:
  G_r: q>=ell_r-1,q'>=M_r-1 (chi=1);
  Q_r: q<=ell_r-2 (chi=ell_r-q), the near-A type;
  P_r: q'<=M_r-2 (chi=M_r-q'), the near-A^c type.
A negative cap just makes that type empty. A G_r top has t_r<=-1. A Q_r top with 2r>kappa has t_r<=-1, because
Theta+l<=ell_r-2-(nu-a)-2alpha<=2kappa-2r, while nonnegativity would give Theta+l>=2r (Lemma1).
Moreover an all-nonnegative central Q with 2|Q|>kappa must use the P branch. The upper window and Lemma1 give
nu+q'(Q)-l(Q)<=-2d-2; as q'-l=a'-2beta, it follows that 2beta(Q)>=a'+nu+2d+2. Two disjoint such sets cannot
both exist because their positive-letter masses would exceed a'. This is a re-derived all-T consequence.

For balanced parameters define epsilon in{0,1} by h=2j-epsilon: epsilon1 means p=4j-3, epsilon0 means p=4j-1.
Then kappa=2j-d-epsilon, j>=5, j>=d+2, kappa>=j+2, and
  ell_j=2j-2d+2-2epsilon, M_j=2j-2d, a'>=3j-(d+3epsilon)/2.                         (Bal)
All are substitutions into T; e.g. floor((p+7)/4)=j+1 gives kappa>=j+2. The level j is central/proper and 2j>kappa.
Accepted UFC T0 is exactly j<=2d+1, equivalently kappa<=3d+2-epsilon, and hence is inside kappa<=4d. The T1 cutoff
is exactly j<=2d+2. These are parameter identities, not a fixed-cell extrapolation.

## 2. Full-range scalar/mass bounds and the positive-P restriction

For a top-r set with negative threshold the upper window and bottom counts give
  G_r: Xi(S)<=r-kappa-1-E(B_r),
  Q_r (z=q): Xi(S)<=kappa-r-z-E(B_r); if t_r<=-2, Xi(S)<=-d-z,
  P_r (z=q'): Xi(S)<=3r-kappa-2d-2-z-E(B_r).                                        (Scalar)
Whenever t_r<=0, Lemma1 instead gives
  Q_r: Xi(S)<=-d-z+l(B_r),
  P_r: Xi(S)<=4r-2kappa-3d-2-z+l(B_r).                                             (Mass-bound)
Each formula is just the top upper bound plus the stated bottom bound and nu+d. The G_r threshold is negative
automatically; Q_r negativity is automatic when 2r>kappa. These are derived on ALL T, with their displayed hypotheses.

LEMMA 2 (negative empty-run cap). If a<=delta+1, put c=ceil((a+1)/2). No alternating set has d+c negative empty runs.
Proof. c<=kappa-d+1, so r=d+c is central/proper. A subset of r negative empty runs would have q=a,q'=R-a. At that
level ell=delta+2-2c, M=2c, and
ell-q'=delta+2-2c-R+a<=delta+1-R<0, while 2c-a is1 or2 and dominates eps=a mod2. Thus y=2c-a. The lower window gives
  Theta>=e-2d+2-nu-(2c-a)=(e-(nu-a))-2r+2>=-2r+2.
But r negative empty theta sum to<=-2r. Contradiction. This uses the LABEL excess e>=nu-a, not the total identity. []

LEMMA 3 (positive balanced P). At level j, a positive threshold is possible only for P_j and its threshold is exactly1.
With z=q'(J_j), L=j-2d-2, it obeys
  nu+z<=L, a<=L, l(B_j)+lambda<=a+z<=nu+z<=L, lambda=l(S'),                         (P+budget)
and the opposite balanced top is G_j or Q_j, with negative threshold. Necessarily
  ceil((L+1)/2)>=d+4-epsilon, hence kappa>=7d+16-5epsilon.                           (P+threshold)
Proof. G_j and Q_j are negative by Sec.1. P_j has top upper sum M_j-2-nu-z<=2j-2d-2<2j, so its integer threshold
is at most1. If it is1, Theta(J_j)>=j gives nu+z<=L. Outside letters number alpha(J_j)+alpha'(J_j)<=a+z<=nu+z.
For Q inside S', q'(Q)>=a'-lambda>=a'-L>M_j-2: by(Bal), the difference is at least (7d+8-3epsilon)/2>0. Thus the
opposite top is not P_j and is negative. Also a<=L<=delta+1, since delta+1-L=3j-2d-2epsilon+3>0.
Apply Lemma2 to S'. It has at most d+c-1 negative empties, at most j-1 positive empties (its j-th theta is negative),
and at most lambda nonempty runs. Counting its h runs yields
  h<=d+c-1+j-1+lambda, so kappa-j+2<=c+lambda<=ceil((L+1)/2)+L.
Since kappa-j+2=L+d+4-epsilon, obtain the ceiling inequality; it implies L>=2d+6-2epsilon, hence
kappa=2L+3d+4-epsilon>=7d+16-5epsilon. No all-unit assumption, nonempty-run assumption or selected frame was used. []

## 3. The balanced initial cover on ALL T

LEMMA 4. Unless Xi(S_ev)+Xi(S_od)<=-1 is already proved by the following bounds, the two balanced tops are EITHER
both Q_j (negative), OR one is positive P_j as in Lemma3. No other type/sign case is left.
Proof. Exclude the positive-P case from the present case split, so every balanced threshold is<=0. Set
  b=h-j=j-epsilon, g0=j-kappa-1, p0=3j-kappa-2d-2=j+epsilon-d-2,
  c0=4j-2kappa-3d-2=2epsilon-d-2, M=M_j=2j-2d.
G with Q gives g0+(kappa-j)=-1, G with G is negative, and G with negative P gives g0+p0=2epsilon-3<=-1.
For a threshold0 P, nu+z<=M-2 and the letters in its bottom and the other set's bottom total<=M-2. Combining its
mass bound with G's empty-bottom bound gives sum<=4epsilon-2d-5-z<0. This follows by replacing the other empty
count by b minus its bottom letter mass.
For P with Q, both nonpositive-bottom mass bounds and(Mass) give sum<=c0-d=2epsilon-2d-2<0, including threshold0 P.
For two P, disjointness gives z1+z2>=a'. If both thresholds are negative, sum<=2p0-a'<0. If one threshold is0,
its outside-letter budget gives l(B1)+l(B2)<=M-2, while both mass bounds apply, giving sum<=2c0+M-2-a'<0.
For completeness the density bound(Bal) yields
  2p0-a'<=-j-3d/2+7epsilon/2-4<0,
  2c0+M-2-a'<=-j-7d/2+11epsilon/2-6<0
as j>=5,d>=2,epsilon<=1. Every real negative upper bound on an integer sum is<=-1. All cases except Q/Q and the
positive-P budget branch have now been covered. No UB/RES hypothesis has been inserted. []

## 4. Sorted-chain exits and the uniform range kappa<=4d

LEMMA 5 (two Q tops at any central r with negative thresholds). Let z_i=q(J_r(S_i)). If both t_r=-1 then
  z1+z2>=4r-2kappa+nu,
  Xi(S1)+Xi(S2)<=4kappa-6r-nu-E(B1)-E(B2).                                         (QQ-1)
If both t_r<=-2, sum<=-2d-z1-z2. If t1<=-2,t2=-1 (or vice versa), then
  sum<=kappa-r-d-z1-z2-E(B2),
  z1+z2>=n(J_r(S2))>=ceil((4r-2kappa+nu+z2)/3).                                   (QQ-mixed)
Proof. Write alpha_i,beta_i for the tops. Disjointness gives l(J_i)<=alpha_(3-i)+beta_i. A threshold-1 top obeys
2r-3n(J_i)<=Theta(J_i)<=2kappa-2r-nu-z_i. When both thresholds are-1, add the two inequalities using n<=l to get
the deficit-sum bound, then use(Scalar). For one threshold<=-2 use its strong bound-d-z1 and the other's scalar
bound. Its top inequality gives the stated nonempty-run bound, and n(J2)<=l(J2)<=alpha_1+beta_2<=z1+z2. []

LEMMA 6 (first exit from two Q chains). Suppose both balanced tops are Q_j. Put r*=kappa-d and assume kappa>3d
and r*>=j. Every threshold at size>=j is negative. Follow both top sets through sizes j,...,r*.
(a) If both remain Q through r*, their Xi sum is<=-1.
(b) Otherwise let r+1 be the FIRST size at which at least one top ceases to be Q. If none of the new types is P,
the sum is<=-1. If a new type is P, with zP=q'(J_(r+1)(S)) and zQ=q(J_r(S')), then
  Xi(S)+Xi(S')<=4r-2kappa-4d+2.                                                     (Exit)
Moreover the added run {u}=J_(r+1)(S)\J_r(S) obeys
  beta(u)>=R-q(J_r(S))-zP>=2kappa+4d-2=p+2d-1.                                    (Jump)
Proof. Negativity persists under increasing sorted size. At r*=kappa-d, (QQ-1) gives sum<=6d-2kappa-nu<0. Both
strong thresholds give<=-2d. In the mixed case the scalar coefficient kappa-r*-d is0, so sum<=-z1-z2-E. A
nonnegative sum forces z1=z2=0, whence both disjoint top letter sets equal A, so A is empty and the threshold-1 top
is entirely empty, impossible by evenness. This proves(a).
At a generic-only first exit, G_(r+1) with Q_(r+1) gives (r+1-kappa-1)+(kappa-r-1)=-1; two G sets give a negative
sum because r+1<=r*<=kappa-d. If a new P exists, its scalar constant is3r-kappa-2d+1; the opposite PREVIOUS Q_r
constant is kappa-r. Their bottoms have 2h-2r-1 runs, with letter mass<=zP+zQ by(Mass), hence at least
2h-2r-1-zP-zQ empties. Add the scalar bounds to obtain(Exit).
Finally q(J_(r+1))=q(J_r)+beta(u)-beta'(u), so zP=R-q(J_r)-beta(u)+beta'(u). Previous Q_r has q<=ell_r-2=2kappa-2r;
new P_(r+1) has zP<=M_(r+1)-2=2r-2d. Their sum<=delta, proving(Jump). This is a DEDUCED single-run bound, not an
assumed giant-pair premise. []

PROOF OF THEOREM UPAR-P FOR kappa<=4d. If in accepted UFC T0 use its exact U0 statement. Otherwise j>=2d+2 and
kappa>3d, with r*=kappa-d>=j+1. Lemma3 excludes a positive P because kappa<=4d<7d+16-5epsilon. Lemma4 excludes
every initial pair except Q/Q. Apply Lemma6. A generic-only exit or no exit gives a negative sum. At a P exit,
r<=r*-1=kappa-d-1, so(Exit)<=2kappa-8d-2<=-2. Hence the sum is<=-1 in EVERY frame. The new count steps used no
total identity; now use(ID) for the final contradiction. This proves the entire uniform region kappa<=4d, not just
a residue class or a bounded-prime list.

## 5. The half-boundary family, all retained ranges, and named outcomes

THEOREM 8 (uniform half-boundary). For every d>=2 with p=8d+7 prime, kappa=3d+4, the every-frame sum is<=-1.
Proof. The pair lies in T: floor((p+7)/4)=2d+3<3d+4<=(p-3)/2=4d+2. Here h=4d+4, epsilon=0, j=2d+2. A positive
balanced P is excluded by Lemma3 since kappa=3d+4<7d+16. Lemma4
handles every initial pair except Q/Q. On Q/Q the thresholds stay negative. At level j+1, any P exit gives the
bound4j-2kappa-4d+2=2-2d<0 by Lemma6(b)'s first-exit calculation (which did not require continuing to r*).
A generic-only exit also closes. If both new tops remain Q, Lemma5 at r=j+1=2d+3 applies. Both threshold-1 gives
4kappa-6r-nu=-2-nu<0; both strong thresholds give<=-2d. In the mixed case the scalar coefficient kappa-r-d is1,
and z1+z2>=ceil((4r-2kappa)/3)=ceil((2d+4)/3)>=3; its sum is<=1-3=-2. All cases are negative, without the total
identity. Now(ID) excludes the frame. The constants are derived from variable d, not imported from the p23 cell. []

T1 is now retained in full. Its interior j<=2d+1 is accepted UFC T0 and lies in kappa<=4d. Its new boundary is
j=2d+2. For epsilon=0 this is Theorem8. For epsilon=1 it is p=8d+5,kappa=3d+3, inside kappa<=4d for d>=3; d=2
gives p=21=3*7, not a prime in T. Thus both residue-class cutoffs of(Region) are proved. This completes UPAR-P on
T_PAR. Full T\T_PAR remains in scope; it has kappa>4d and is not silently dropped.

All cell constants below are independently substituted into the general definitions. Each cell is in T.
| (kappa,p) | word/group; terminal k | N,h,R,d,delta | epsilon,j; central sizes | Outcome |
|---|---|---|---|---|---|
| (12,29) | length114/D58; k30 | 30,15,52,3,18 | 1,8; 3..13 | PROVED: kappa=4d |
| (13,29) | length114/D58; k30 | 30,15,54,2,22 | 1,8; 2..14 | OPEN: late-jump residual below |
| (13,31) | length122/D62; k32 | 32,16,56,3,20 | 0,8; 3..14 | PROVED: Theorem8, p=8d+7 |
| (14,31) | length122/D62; k32 | 32,16,58,2,24 | 0,8; 2..15 | OPEN: late-jump residual below |
| (17,37) | length146/D74; k38 | 38,19,70,2,30 | 1,10; 2..18 | OPEN: late-jump residual below |
Every proved cell retains arbitrary extra pairs, the empty-run rule and EVERY-frame quantification. These are
candidate new proofs, not a promotion of the independently audited frontier bookkeeping into a premise.

## 6. All-T mass certificates, complete residual and the first unproved lemma

### 6.1 Valid certificates on all T

For central Q subset S, put b=h-|Q|, Lout=l(S\Q). If every outside theta<=0, Lemma1 and(W) give
  Xi(S)<=x(Q)+Lout-2b+d-2.                                                        (CM)
If every outside theta>=0, Lemma1 and the LOWER window give
  Xi(S)>=e-d+2-y(Q)+2b-Lout,
so, using(ID) explicitly, Xi(S')<=y(Q)+Lout-2b+d-2.                                (DM)
These are new general-parameter mass bounds proved by those two additions, not fixed-cell lemmas.
Also retain accepted UFC ENV at its exact all-T scope (UFC LF209-224): for an integer t,
rho(0)=2,rho(1)=3, otherwise rho(t)=t-2floor(t/2). For top-r J_r,t_r,B_r and bottom-r K_r,largest value s_r,
F_r=S\K_r, define
  C(S)=min_(central r)[x_r(J_r)+d-2+(h-r)t_r-rho(t_r)E(B_r)],
  D(S)=min_(central r)[y_r(K_r)+d-2-(h-r)s_r-rho(-s_r)E(F_r)], H(S)=min(C(S),D(S')).
ENV gives Xi(S)<=H(S), with its reverse bound using(ID) explicitly. Let B(S) be the minimum of the NONEMPTY finite
bag consisting of H(S), all(CM) bounds on S with the stated outside-sign condition, and all(DM) bounds from S'
with their outside-sign condition. Empty optional families add no entry; H always exists. Then
  Xi(S)<=B(S), and e<=B(S_ev)+B(S_od) on every actual frame.                         (B-bound)
No minima were enumerated or computed. These are finite mathematical tests for each fixed (kappa,p).

### 6.2 Complete R_PAR tests

R_PAR is the following integer-data relaxation, NOT a characterisation of words, NF or avoidance.
(R0) (kappa,p) lies in T\T_PAR. Use the parameters and balanced epsilon,j of Sec.1. Give N run sets partitioning R
labelled occurrences, odd nonzero c_l and integers theta_i with(D1),(D2),(ID) and ALL central mixed-set windows(W).
Retain |theta_i|<2p, max|c_l|<=p-6 and the unit reservoir #{l:|c_l|=1}>=|c_l|+2kappa-1 for every l (literal UMR
Lemmas4,10). For a proper nonempty mixed P, m(P) is its number of maximal cyclic intervals; m(empty)=m(all)=0.
This is finite for EACH FIXED (kappa,p), not a finite union over the unbounded parameter strip. Other NF, generator
or block-value constraints may still prevent a numerical tuple from occurring.
(R1) Require B(S_ev)+B(S_od)>=e>=0. Retain accepted E0: if a=0, both alternating sets have nonempty letter mass.
Retain also Lemma2's negative-empty cap whenever a<=delta+1. These are necessary relaxation tests, not converses.
(R2) At least one exact UMR UB certificate fails. For S set N_S={i in S:theta_i>=0}, P_S={i in S:theta_i<=0}.
For central r<=kappa put lo_r=kappa+1-r, hi_r=R+2d+kappa+1-3r, and define
  G+(S): some N_S subset Q subset S of size r has lo_r<=q(Q)<=hi_r;
  G-(S): some P_S subset Q subset S of size r has lo_r<=q'(Q)<=hi_r;
  Z+(S): |N_S|<=kappa and every kappa-superset Q of N_S in S has q(Q)=0;
  Z-(S): [|P_S|<kappa and every kappa-superset Q of P_S in S has q'(Q)=0] OR
          [|P_S|=kappa,q'(P_S)=0,and S\P_S contains an empty run].
  UB(S)=G+(S) OR Z+(S) OR G-(S') OR Z-(S').
Subset permits equality. These are literal UMR LF266-274,300-302, not altered certificates. For each failing S retain
ONLY the one-way Lemma20 alternatives (UMR LF315-324), requiring BOTH of the following bracketed clauses:
  [First] S has a pair of runs totalling>=p+3 letters, OR |N_S|>=kappa+1, OR d<|N_S|<=kappa with every kappa-superset
  Q of N_S in S having q'(Q)<=delta-2;
  [Second] S' has such a pair, OR |P_(S')|>=kappa+1, OR d<|P_(S')|<=kappa with every kappa-superset Q of P_(S') in S'
  having q(Q)<=delta-2, OR the boundary |P_(S')|=kappa,L(P_(S'))=A^c and no empty tail.
In the second/third alternatives of [First] only, retain |L(S') intersect A^c|<=delta. No giant clause is promoted into
saturation at any other level, and no converse or residual existence is claimed.
(R3) Exactly the following TWO types remain (their defining data are all retained, not just a parameter label):
(P+) One balanced top is P_j with t_j=1, z=q'(J_j)<=M_j-2. Put L=j-2d-2 and lambda=l(S'). Retain
  nu+z<=L, a+z<=L, l(B_j)+lambda<=a+z, a<=L, kappa>=7d+16-5epsilon,
  2beta(J_j)>=a'+nu+2d+2 (the all-nonnegative majority consequence of Sec.1),
  kappa-j+2<=ceil((a+1)/2)+lambda, and ceil((L+1)/2)>=d+4-epsilon.
  The opposite balanced top is G_j or Q_j and negative. No all-unit assumption is made.
(LJ) Both balanced tops are Q_j. For some integer
  max(j,ceil((kappa+2d-1)/2))<=r<=kappa-d-1,
  BOTH sorted tops stay Q_s at EVERY s=j,...,r. At size r+1 at least one is P_(r+1), and r+1 is the first exit
  from the two Q chains. Choose that set S, put z0=q(J_r(S)), zP=q'(J_(r+1)(S)) and {u}=J_(r+1)(S)\J_r(S).
  Retain z0<=ell_r-2, zP<=M_(r+1)-2, theta_u<=-1, 4r-2kappa-4d+2>=0, beta(u)>=2kappa+4d-2.
  At least one of the two predecessor thresholds t_r is exactly-1: otherwise both strong Q bounds exclude it.
  There cannot be two P exits at this size: each added run would have beta>=2kappa+4d-2 and the two disjoint
  positive-letter masses would exceed R (the difference is6d-2>0). The other new type is Q or G, not a second P.
  All earlier/later mixed-set windows and mass/ENV/UB tests above remain in force; this is not a giant-pair
  characterisation or a claim that one displayed jump suffices for a word.

### 6.3 Why every hypothetical survivor is retained

Outside T_PAR, kappa>4d, hence kappa>3d and r*=kappa-d>=j+1. By accepted UFC U1, every hypothetical surviving frame
already satisfies the full R_U relaxation (UMR data, ENV, exact UB failure and one-way Lemma20), since T0 is
contained in T_PAR. Our extra CM/DM bounds prove(R1), and Lemmas2-4 force(P+) or two balanced Q tops. In the latter
case apply Lemma6 up to r*: staying Q throughout or a generic-only first exit would give a negative sum. A P exit
with4r-2kappa-4d+2<0 would too. Therefore a surviving frame must have exactly the late jump described in(LJ), with
its deduced mass and threshold conditions. This proves UPAR-R on the ENTIRE complementary parameter strip.
The two types are exhaustive for this proof method; they are not asserted nonempty or sufficient for an NF.

### 6.4 The exact first UNPROVED uniform lemma

PAR-COVER (NOT PROVED): no actual target NF/frame on T\T_PAR induces integer data in R_PAR, i.e. neither(P+) nor(LJ)
with all the tests above occurs. This would complete full UPAR via UPAR-P and UPAR-R. It is an equivalent exclusion
target, not a proved reduction in logical difficulty, a no-go theorem, an inverse description or a necessary
mathematical obstruction. The unproved part is retained in full, including both residue classes and arbitrarily
large parameters. No other proof is silently substituted for it.

## 7. Complete residuals for the three open named cells

For each row below instantiate EVERY test of R_PAR, not merely the jump. Positive P is excluded by Lemma3's
threshold: the respective kappa values13,14,17 are below25,30,25. Thus the sole remaining type is(LJ), with ALL
mixed-set windows, parity, ENV/mass bounds and exact UB/one-way conditions retained. No instance is asserted realised.
| Cell | j,r*=kappa-d | allowed predecessor r | q(J_s) cap along BOTH chains | q'(J_(r+1)) cap | deduced beta(u) |
|---|---|---|---|---|---|
| (13,29) | 8,11 | 8..10 | 26-2s, every s=8..r | 2r-4 | >=32 |
| (14,31) | 8,12 | 9..11 | 28-2s, every s=8..r | 2r-4 | >=34 |
| (17,37) | 10,15 | 10..14 | 34-2s, every s=10..r | 2r-4 | >=40 |
The r ranges are exactly max(j,ceil((kappa+2d-1)/2))..kappa-d-1. At r+1 one top is P and the other Q or G, with no
previous exit; both predecessor thresholds are negative and at least one is-1. The jump theta_u<=-1 and all further
central windows remain required. The following constants make the inherited relaxation and certificates explicit:
| Cell | a' minimum | max|c_l|; unit reservoir | |theta_i| | central r; ell_r,M_r | UB good levels; lo_s,hi_s |
|---|---|---|---|---|---|
| (13,29) | 22 | <=23; u1>=|c_l|+25 | <58 | 2..14; 28-2r,2r-4 | 2..13; 14-s,72-3s |
| (14,31) | 23 | <=25; u1>=|c_l|+27 | <62 | 2..15; 30-2r,2r-4 | 2..14; 15-s,77-3s |
| (17,37) | 28 | <=31; u1>=|c_l|+33 | <74 | 2..18; 36-2r,2r-4 | 2..17; 18-s,92-3s |
For all three, Theta(all)=e-2nu-4 and Xi(S)=Theta(S)+nu+2. At every central mixed P use its actual m(P) and the
listed ell,M with q'=R-q and eps=q mod2 in(W). For UB/one-way Lemma20 use the row's kappa; its supersets have that
size, large-sign threshold is kappa+1, lower sign count bound is2, giant-pair threshold is32,34,40 respectively,
and the level-kappa near-saturation caps delta-2 are20,22,28. The opposite positive-letter caps in those literal
second/third alternatives are22,24,30; they do not apply to a giant clause or other levels. The full exact boundary
|P_(S')|=kappa,L(P_(S'))=A^c,no empty tail is retained.
First unproved LOCAL step for EACH of these three cells: exclude its displayed first-exit late-jump data when
ALL R_PAR tests hold for an actual NF/frame. This has not been proved; generic-only exits, positive-P tops and
other initial balanced types have been excluded by the preceding uniform lemmas. No local proof is claimed from
one deficit inequality, and no branch of the residual is silently discarded.

## 8. Literal interface, provenance and non-claims

| Input | Absolute path; whole-file SHA256 | Inclusive LF | Scope/use |
|---|---|---|---|
| Authority | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-full-uniform-parity-transition-v1.json; 91514b1ccc8486938c79183cd8816b6b449a7c758c4cf6ec3ec45a022dde1091 | 1-57 | Full T, five named cells, rules, corrected navigation not a premise |
| Frozen scope | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-full-uniform-parity/UPAR-scope-v1.md; 01f0fdf75327dfa5d6dec5a3fa2a616ae1a336d93e76b1b99327f37bb1d2b641 | 1-79 | All prior authorship and unwritten exposure; freeze before NEW derivation |
| Accepted UMR verdict | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-verdict-v1.md; a2535971cb214e399433235a4b9fca2de7328d15bec2c2f4eece35c05456c772 | 3-26 | Literal framework, windows, full run parity, identity; conditional UB and one-way residual only |
| UMR proof | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-middle-range/proof-UMR-v1.md; c403bfbae9f1c7b75698010cae78515a253154e689336e79006c588ff15023a9 | 18-28,49-56,64-68,88-118,137-139,161-165,201-209,238-239,252-258 | Data imports; Lemma10 LF202 plus integer sigma_i LF109-110 yields ALL-RUN parity |
| UMR erratum v1 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v1.md; b83313b3fe828ee19a0902e9a5149db42ee55318500f92bac577b4bbd7088c5f | 1-10 | Connectivity link restricted; no universal saturation |
| UMR erratum v2 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v2.md; 2a5f142ef136b04c15304137a4ba19946d0fee115ce18e8660817cd25bc902a2 | 1-9 | Residual wording and one-way scopes |
| Accepted UFC verdict | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-verdict-v1.md; 10596e3df9eab24f0451910eb84ae3029721c60a211f9b4b22d5fff943d0c060 | 3-14 | U0 on T0, E0/ENV all T, U1; NOT HIGH-COVER |
| UFC proof | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-fc/proof-UFC-v1.md; 2d03076c9bbf1afa3d68e42bfc2fe9eeb4a62ee64b59e6c94c53f65a32b670c5 | 200-263 | Exact E0/ENV/R_U definitions and accepted U1; no extension of fixed ranges |
| UFC erratum v1 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-erratum-v1.md; b2719ef394c2920d144f39ff2b4a8752eab05161aa67226308309edaf88af40e | 1-6 | HighQ scope repair, not a no-go claim |
| UFC scope precision | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UFC-parent-scope-precision-v1.md; 9b02608fdeb1054878867f1d9bd014cf5ec8084a91c8edc6a8fae5bc93dede17 | 1-5 | Finiteness only per fixed parameter; no converse/existence |
| FC1023 status/method only | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC1023-parent-verdict-v2-confirmation.md; 33b2d30fca6a723884765b5393fe9e95e2a9f58e0aa1ba2b52103c9f7405a5fa | 1-5 | Accepted only at(10,23); no internal cell lemma used uniformly |
| FC1023 erratum | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC1023-parent-erratum-v1.md; 9966046795690fd9087de61bd9165f9c0726bb9ab4664b897a16193d2eb57f98 | 1-7 | Mass-bound sign hypotheses and deduced, not assumed, giant mass |

Primitive inputs enter ONLY through UMR, exactly UMR verdict LF24: NF; GRX if-direction; SC0 through Y'z;
ZSTRUCT/FB at exact (S') parameters(p-1,kappa-1); S1 definition; stated LOWER conventions. No FCW/balfull theorem
or unaccepted union bookkeeping is a mathematical premise. The authority's p29/provider corrections and frontier-v3
are navigation only, not used to prove a cell or a uniform parameter inclusion. No full ordered Olson, other-k,
priority/novelty, human-referee, Lean or runtime claim; parent alone reviews and accepts.
The prior authorship and UNWRITTEN near-A parity observation are disclosed in the frozen scope. All general
parameter formulas and new count lemmas above are re-derived after freeze. Unused early balanced-margin/slack and
integer-boundary equality routes are disclosed in checkpoints, not premises. Machine categories: clock, SHA256,
byte/LF counts, local reads, mkdir, exclusive drafted-text creation. No science computation or enumeration was used.
