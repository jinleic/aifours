# UPAR3 v1 — zero-defect closure and uniform small-budget exclusion

Owner OlsonThirdCutWindow, same throttled math2 slot. Drafted after /bin/date 2026-10-21T09:02:12-0700.
Scope UPAR3-scope-v1.md frozen2026-10-21T08:21:56-0700, read with scope-metadata-erratum-1-UPAR3-v1.md.
Authority written-olson-jump-cover-followon-v1.json SHA256 664083c666265a9f560082c65045d18351ce3ce589be422a471dd1a391e89d66,
LF1-157. All input paths/whole-file pins/actual LF ranges appear in the actual numbered packet and manifest.
WRITTEN CANDIDATE, not reviewed/accepted. Full T NOT proved. A larger uniform region T3 is proved; the ENTIRE F=0
residual is eliminated on the unbounded complement. F>0 with nonunit labels/higher excess remains in a complete
necessary residual. No existence/converse/no-go, full ordered Olson, other-k, novelty,human/Lean/runtime claim.

## 0. Target and statements

T: p>=17 prime,floor((p+7)/4)<kappa<=(p-3)/2. The word has length4p-2 over D_(2p), avoids identity2p-subwords in
increasing ORIGINAL index order, and has SOME admissible NF with terminal k=p+1,kappa_hat=kappa. Extra reflection
pairs are arbitrary in odd blocks; every empty run separates different reflection values; no o_F,nonempty-run,
rotation-pair or rigidity hypothesis. EVERY actual frame is considered.
Put d=(p+1)/2-kappa>=2. THEOREM UPAR3-P: no such NF exists on
  T3={T:kappa<=8d+6}={T:9kappa<=4p+10}.                                             (T3)
This strictly contains accepted T2 (even kappa<=8d-2 or odd<=8d+1); (19,41),d2 is one strict new point. Five named
cells are proved; the other three and the ENTIRE unbounded T\T3 remain in the complete residual of Sec.6.
THEOREM UPAR3-Z: no hypothetical survivor on T\T2 has F=e, including all F0 and nonunit e>0 fully-consumed cases.
Thus F0 is removed by proof, not by case-only narrowing. Both predecessor mixed orientations were already excluded by accepted UPAR2; the remaining
both-minus1 zero type is excluded here. ID is used INSIDE the arguments, not only at their end.

## 1. Exact common contract and notation

Use accepted UMR and UPAR2 at their literal scopes, through ALL governing errata. h=kappa+d,N=2h,R=4kappa+2d-2,
delta=2kappa-2d. Runs have occurrence sets L_i partitioning R letters, odd nonzero labels c_l, A={c_l<0},a=|A|,
a'=R-a,nu=sum_A|c_l|,e=sum_all(|c_l|-1). Then nu>=a,e>=nu-a>=0,a'>=(3kappa+2d)/2. E(U),n(U),l(U),Theta(U)
mean empty/nonempty run counts, letter mass and theta sum. Write beta(U)=|L(U) intersect A^c|, beta'(U)=|L(U) intersect A|,
alpha(U)=|A\L(U)|. q(U)=alpha(U)+beta(U)=|L(U) symdiff A|, q'(U)=R-q(U), l(U)=a-alpha(U)+beta(U).
Literal UMR parity is theta_i congruent sum_(L_i)c_l congruent |L_i| MODULO2, not integer equality; empty theta is
nonzero even. Hence theta>=0 implies theta+|L_i|>=2, and theta<=0 implies -theta+|L_i|>=2 (empty/singleton/long-run
cases). All central sets, including mixed/non-independent ones, retain
  ell_m=2kappa+2-2m,M_m=2m-2d, eps=q mod2,
  x=max(eps,ell_m-q,M_m-q'), y=max(eps,M_m-q,ell_m-q'),
  e-2d+2-nu-y<=Theta<=-2-nu+x, d<=m<=kappa+1.                                       (W)
On alternating-set subsets m is their size. ID: Xi(S)=Theta(S)+nu+d and Xi(S_ev)+Xi(S_od)=e.
Every primary UMR parity/window/UB/Lemma20 range (including320-321) is pasted literally in the packet. Full UMR
verdict1-38, full UFC1-36/finiteness5, all mandatory UPAR2 errata are actually supplied, not claimed from hashes.

Any hypothetical survivor outside accepted T2 has the COMPLETE old R2 necessary data, by accepted UPAR2-R. In
particular it is LJ, not positive balanced P (that branch is accepted excluded on ALL T). Fix its first P exit:
  I=J_r(S), K=J_(r+1)(S)=I union{u}, Q=J_r(S'), X=S\K,Y=S'\Q,
  z0=q(I), zP=q'(K), z=q(Q), b*=2r-kappa,F=2b*-4d+2>=0.
Both predecessor tops are near-A Q_r and negative, at least one threshold exactly-1. All X,Y theta are negative.
The r interval, all predecessor QQ bounds, full mixed windows, mass/ENV/UB/one-way tests remain required. Define
  wA=beta'(K),w=beta(Q),W=wA+w,
  sP=2r-2d-nu-zP-Theta(K), sQ=2kappa-2r-nu-z-Theta(Q),
  D_U=l(U)-2|U|-Theta(U) for U=X,Y; D=D_X+D_Y>=0.
These are UPAR2's defect b*,C*, not inherited CM/DM tail-size b or ENV C(S). On negative tails, |L_i|<=1+D_i;
on STRONG tails(theta<=-2), |L_i|<=D_i. Exact letter algebra and ID give
  F-e=2W+sP+sQ+D, beta(X)+beta(Y)=zP-W.                                             (Defect)
e,sP,sQ,D are nonnegative EVEN integers: odd labels give e even, nu congruent a and q congruent a+l; endpoints
have the same parity as their theta sums. Tail parity gives D even. W is a nonnegative integer.
Put A0=2kappa-2r=kappa-b*, P0=2r-2d. The endpoint and order relations are
  Theta(Q)=A0-nu-z-sQ, Theta(K)=P0-nu-zP-sP,
  zP+sP>=z0+2b*-2d+1; if I is STRONG, replace1 by2.                                 (Order)
A weak(top threshold-1) near-A predecessor has n>=b*. For both weak predecessors, accepted QQ gives
  e+nu+E(predecessor bottoms)<=kappa-3b*.
For a mixed pair, z0+z+E(weak bottom)<=kappa-r-d-e. Always z0+z>=n(weak top)>=b*.
If Q is weak, comparing2r-3l(Q) with its endpoint, with eta=nu-a>=0, gives
  a>=b*+2z-3w+(eta+sQ)/2.                                                        (Q-count)
If I is weak, beta(I)>=a+b*-2beta'(I), so z0>=2a+b*-3beta'(I). These follow directly from(W) and l=a-alpha+beta.
The accepted cap used below is: if a<=delta+1, negative empties in either alternating set are at most
  d+ceil((a+1)/2)-1<=d+a/2.                                                        (Cap)
Its literal UPAR source102-107 and governing statements are included. No stronger cap is assumed.

## 2. No exit may consume its whole budget in e: F=e is impossible on ALL T

Assume F=e, possibly e>0 and NONUNIT labels. Defect forces W=sP=sQ=D=0, but does NOT force e=0 or nu=a.
Thus K and I contain only A^c, Q only A, z0=a+beta(I), l(Q)=a-z; tails have length0/theta-2 or length1/theta-1.
Write A0=kappa-b, P0=kappa+b-2d. Endpoints are Theta(Q)=A0-nu-z, Theta(K)=P0-nu-zP; I has its near-A upper bound.
If I is weak, beta(I)>=a+b; if Q is weak, a>=b+2z, by their2r-3l lower bounds and nu>=a. Order gives
zP>=z0+2b-2d+1, or with strong I replace1 by2.
First observe: whenever z<=(kappa-4b-1)/4, no positive letter is in Y. Such a letter would be a singleton v with
theta=-1. On Q+v the actual theta is A0-nu-z-1; its upper maximum entries are<=1, A0-z-1 and z+b-3kappa-4d+5.
The bound gives A0-z-1>=3(kappa-1)/4>1 and the P entry<=(-11kappa-16d+19)/4<0. Thus the upper theta is
A0-nu-z-3, a contradiction by2. This uses an arbitrary central independent extension, not a sorted-top assumption.
Both predecessors weak: a>=b+2z, beta(I)>=a+b and order imply
  zP>=2a+3b-2d+1>=5b-2d+1+4z.
Since zP<=M_(r+1)-2=kappa+b-2d, get4z<=kappa-4b-1 and beta(Y)=0 by the observation. All positive letters outside
K are in X, so zP<=|X|=(kappa+2d-b-2)/2. Therefore
  a<=(kappa+6d-7b-4)/4<kappa/4.
This upper bound implies a<=delta+1; its difference from delta+1 is at least(7kappa+1)/4>0 because b>=2d-1.
Y has at most z negative singletons, hence at least|Y|-z negative empties. Apply(Cap) and a>=b+2z:
  kappa-b-2z<=a, while 2z<=a-b, so kappa<=2a,
contradicting a<kappa/4.
Mixed, I STRONG/Q weak: QQ-mixed and e=F give
  z0+z<=T:=(kappa-5b+6d-4)/2.
Since z0+z>=n(Q)>=b, kappa>=7b-6d+4. Q weak gives a>=b+2z and z0>=a, so
z<=(kappa-7b+6d-4)/6<=(kappa-4b-1)/4; the last difference is at least9(b-2d+1)/12>=0. A negative bound is
already impossible. Hence beta(Y)=0. Strong X with D0 is empty, but strong-u order gives zP>=z0+2b-2d+2>0.
Q has no A^c and X is empty, so all these positive outside-K letters would be in Y: contradiction.
Mixed, I weak/Q STRONG: QQ-mixed gives the same T, and z0>=2a+b, so
  a<=(kappa-7b+6d-4)/4<kappa/4, with a<=delta+1.
Strong Y with D0 is empty and negative. Its size (kappa+2d-b)/2 and(Cap) give kappa-b<=a. Combining with the
upper bound yields3kappa+3b<=6d-4, impossible since b>=2d-1 and kappa>0. This covers both orientations with their
explicit STRONG hypotheses. Both-strong was already excluded by the baseline. Thus F=e is impossible for any e.
Consequently every hypothetical remaining exit obeys
  F-e>=2,                                                                         (Gap)
because all terms are even. In particular the ENTIRE F0 branch is excluded, without making a unit-label assumption
in the positive-defect proof. Unit labels follow only in cases where e=0 has separately been derived.

## 3. One/two-run extension charges for the families used

For a negative tail run v in Y with beta(v)>0, write D_v=|L_v|-2-theta_v>=0. Then |L_v|<=D_v+1 and
  theta_v+[beta(v)-beta'(v)]+2=2beta(v)-D_v.
Whenever the generic/P upper entries cannot attain the actual sum on Q union{v}, its near-A upper window implies
  2beta(v)<=sQ+D_v.                                                               (Charge)
The union is an arbitrary independent subset, NOT assumed the next sorted top. In the two families below those
other entries cannot rescue it. The parameter table gives the exact checks (t0/1/2,s4/6,d>=2):
| Family | b*,kappa | F | A0 | bound on z when charge used | M_(r+1)-R |
|---|---|---|---|---|---|
| minimal | 2d+t,3b*+2d=8d+3t | 2t+2 | 6d+2t | z<=t+1 | -26d-8t+4 |
| nonminimal F2 | 2d,8d+s | 2 | 6d+s | z<=4 | -26d-3s+4 |
Each bound on z is proved before its use below. Since sQ+D<=F and theta_v>=-1-D_v, the actual needed upper entry
is >=A0-z-F+1>1 (respectively>=6d-t-2 or6d+s-5). The P entry is at most M_(r+1)-R+z+F+1<0. Thus only near-A
can be used, proving(Charge). For sQ=0 sum it to get2beta(Y)<=D_Y.
If sQ=2,D=0,z=0 and Y contains two positive singletons, each theta=-1. On Q plus those TWO runs the actual sum
is A0-nu-4; near-A upper is A0-nu-6; generic and P entries are smaller by the same table bounds. Contradiction.
All r+1 and r+2 used are central: baseline r<=kappa-d-1 and d>=2 give r+2<=kappa-d+1<=kappa-1. No new realisation
or connectivity assertion is being imported beyond the accepted central windows.

## 4. Minimal predecessor families: b*=2d+t, kappa=3b*+2d, t=0,1,2

Throughout this section write b=b* for the JUMP variable, never a CM/DM tail-size. Necessity inequalities force e=0:
for two weak predecessors kappa>=3b+2d-1+3e/2 gives e<=2/3; for mixed, kappa>=3b+2d+2e. Thus nu=a is DERIVED.
Here F=2t+2,A0=6d+2t, |Y|=b+2d, |X|=|Y|-1. We cover every predecessor orientation.
Both weak: QQ gives a+E(pred bottoms)<=2d. Put w=beta(Q), alpha=z-w. The Q top inequality is
  a>=b+2alpha-w+sQ/2.
With a<=2d and W<=t+1, w is t or t+1. If w=t, then a=2d,alpha=sQ=0 and all predecessor bottoms are nonempty.
All A lie in Q, so wA=0,W=t,sP+D=2, and Y is positive/nonempty throughout. The extension charge gives
2l(Y)<=D_Y<=2, impossible for |Y|>=4d. If w=t+1, W=t+1 and sP=sQ=D=0; alpha=0,a<=2d. Charge gives beta(Y)=0;
all A are in Q, so Y is empty and negative. But |Y|>=4d exceeds(Cap)<=d+a/2<=2d. Cap hypotheses hold since a<=2d.
Mixed: let J be the weak predecessor. QQ gives z0+z+E(weak bottom)<=b, while n(J)>=b and n(J)<=l(J)<=z0+z.
Thus n=l=b; 3n>=2b+nu+q(J) gives nu+q(J)<=b. Since l<=a+q<=nu+q, equality forces alpha(J)=0, all A in J,
and its theta sum is kappa-2b=b+2d. The weak top window is saturated.
If I is weak and Q strong, z0=b-a, Q contains no A; z0+z=b then makes beta(Q)=0, so Q is empty and W=a<=t+1<=3.
Y is STRONG; l(Y)<=D_Y<=F-2a. Hence its negative-empty count is at least
|Y|-l(Y)>=4d-t-2+2a>=4d-4+2a, strictly above(Cap)<=d+a/2 for d>=2,t<=2. Contradiction.
If Q is weak and I strong, all A lie in Q, W=z<=t+1,sQ=0,z0=b-z. Strong X gives l(X)<=D_X, and Y is all positive.
Charge gives2l(Y)<=D_Y. Since the positive tail mass is zP-z, defect yields
  zP+sP<=F-z.
Strong-u order gives zP+sP>=z0+2b-2d+2=3b-2d+2-z, larger by b+2d>0. Contradiction. All minimal families close.

## 5. Nonminimal F2 families: b*=2d, kappa=8d+s, s=4 or6

Here F=2,e=0 or2 by evenness, but e2=F is excluded on ALL parameters by Sec.2, without a unit hypothesis. Thus
e0 is derived for these families; A0=6d+s,y=|Y|=2b+s/2,x=y-1,b=2d>=4. Both-weak and both mixed orientations are treated. The bound z<=4 used for extension charges is established in each relevant case.
Both weak: QQ gives nu+E(pred bottoms)<=b+s-e; the Q-count is
  a>=b+2z-3w+(eta+sQ)/2, eta=nu-a>=0.
Since e0 has been derived, nu=a. If W=1, sP=sQ=D=0. For w=1,wA=0, Q-count and a<=b+s give z<=4,a>=b-1; I has no A. For
w=0,wA=1, they give z<=3,a>=b, and I has at most one A. Charge implies beta(Y)=0 in either case. Positive tail
mass zP-1 is all in X, so zP<=x+1<=2b+3. Weak-I counting/order gives respectively zP>=4b-1 or>=4b-2, impossible.
If W=0, parity gives sQ=0 or2. For sQ=0, Q-count gives z<=3,a>=b. Charge bounds2beta(Y)<=D_Y, while negative X
has l(X)<=x+D_X. Hence zP+sP<=x+D_X+D_Y/2+sP<=x+2<=2b+4. Order and weak-I counting give
zP+sP>=2a+2b+1>=4b+1: impossible.
For sQ=2, sP=D=0. Q-count gives a>=b+2z+1, and order gives zP>=2a+2b+1>=4b+4z+3. Zero-slack tails have at most
one letter per run, so zP+z<=x+y=4b+s-1; hence5z<=s-4 and z=0 for s4/6. Then zP>=4b+3 exceeds X capacity by
at least2; all A lie in Q and at least two Y runs are positive singletons. The two-run extension contradiction applies.

Mixed, I weak/Q STRONG (using only the remaining budget hypotheses): z0+z+E(weak bottom)<=b+s/2-e<=b+3, so n(I)<=b+3. Also n(I)>=b,
3n(I)>=2b+nu+z0; hence nu+z0<=b+9. I contains at most wA<=1 negative letter; l(I)>=b implies
nu+z0>=b+2a-2wA. Therefore a<=5. Strong Y has l(Y)<=D_Y<=2, so at least y-2>=4d negative empty runs, above
(Cap)<=d+a/2<=d+5/2. The cap applies because a<=5<delta+1. Contradiction.
Mixed, I STRONG/Q weak: z0+z<=b+s/2-e and z0>=a-wA. Combine with Q-count to obtain
  3z<=s/2-e+wA+3w-sQ/2<=6, so z<=2.
If sQ=0, Charge and strong X give zP-W<=D_X+D_Y/2. Defect then gives zP+sP<=2-e-W<=2, whereas strong order
gives zP+sP>=z0+b+2>=b+2. If sQ=2, defect forces e=W=sP=D=0. X is empty, K only A^c,Q only A; Q-count and
z0>=a give3z+1<=s/2<=3, hence z=0. Order yields zP>=a+b+2>=2b+3. All positive tail mass is in Y, so at least
two Y runs are positive singletons. Again use the two-run extension contradiction. No mixed or nonunit case is omitted.

## 6. Uniform region and every required diagnostic

For kappa=8d, necessity allows only b*=2d,F2,e0: the next b* of matching parity is too large, and e must be0.
For kappa=8d+3 only b*=2d+1,F4,e0 is possible. For kappa=8d+4 only b*=2d,F2,e0/2. For kappa=8d+6 the only
possibilities are b*=2d,F2,e0/2 or b*=2d+2,F6,e0. These follow directly from
kappa>=3b*+2d-1+3e/2 (both weak), kappa>=3b*+2d+2e (mixed), F>=e and parity; no numerical enumeration was used.
Sections4-5 exclude every listed possibility. The only gaps between old T2 and kappa<=8d+6 are kappa=8d+2 and
8d+5, which have p=18d+3=3(6d+1) or p=18d+9=9(2d+1), nonprime for d>=2. The accepted old region and these
variable-parameter families prove(T3) in EVERY frame, using ID inside as disclosed. A target NF has a frame, so
no such NF/word exists. Strict containment is witnessed by(19,41),d2, outside old odd cutoff17. Full T is not claimed.

| Cell | d | word/group; terminal k | Outcome |
|---|---|---|---|
| (19,41) | 2 | length162/D82;k42 | PROVED, minimal t1 |
| (20,43) | 2 | length170/D86;k44 | PROVED, nonminimal s4 |
| (22,47) | 2 | length186/D94;k48 | PROVED, s6 F2 and minimal t2 F6 |
| (25,53) | 2 | length210/D106;k54 | OPEN, complete residual below |
| (27,59) | 3 | length234/D118;k60 | PROVED, minimal t1 |
| (28,59) | 2 | length234/D118;k60 | OPEN, complete residual below |
| (28,61) | 3 | length242/D122;k62 | PROVED, nonminimal s4 |
| (29,61) | 2 | length242/D122;k62 | OPEN, complete residual below |
All full NF/original-order/extra-pair/empty-run/every-frame quantifiers are retained. No named-cell calculation is
used as a uniform lemma; parent preview was unaccepted exposure and the family reductions were re-derived after it.

## 7. Complete remaining residual and exact unproved step

R3 is a necessary numerical relaxation for each FIXED parameter in T\T3, not a characterisation/existence claim.
No old test is deleted except a branch excluded by proof. Retain the following full baseline, with all labels
and theta integers defined in Sec.1, not free slacks:
(a) Occurrence partition, odd nonzero labels, nu>=a,e>=nu-a,all-run modulo2 parity/nonzero empty theta, ID; all
central mixed-set windows(W), including sets that are not alternating subsets. Also |theta_i|<2p,max|c_l|<=p-6,
unit reservoir #{|c_l|=1}>=|c_l|+2kappa-1 for each l. m(P) is the cyclic interval count, m(empty)=m(all)=0.
(b) E0 if a=0, and(Cap) when a<=delta+1. Retain literal UFC ENV: C_env,D_env,H from the pasted primary source,
with rho(0)=2,rho(1)=3, otherwise rho(t)=t-2floor(t/2). Retain all signed-mass bounds on central U subset S:
  Xi(S)<=x(U)+l(S\U)-2(h-|U|)+d-2 if all outside theta<=0;
  Xi(S')<=y(U)+l(S\U)-2(h-|U|)+d-2 if all outside theta>=0, using ID explicitly.
Let B(S) be the minimum of H(S) and all such valid bounds on S (direct or reverse); H makes the bag nonempty.
Require B(S_ev)+B(S_od)>=e. Here tail-size h-|U| is NOT jump b*, and ENV C_env is NOT signed slack D.
(c) At least one exact UB certificate fails. With N_S={theta>=0},P_S={theta<=0}, lo_m=kappa+1-m,
hi_m=R+2d+kappa+1-3m for central m<=kappa: G+ is existence of an m-superset of N_S with q in[lo,hi]; G- is an
m-superset of P_S with q' in[lo,hi]. Z+ is |N_S|<=kappa and every kappa-superset of N_S has q=0; Z- is
[|P_S|<kappa and every kappa-superset of P_S has q'=0] OR [|P_S|=kappa,q'(P_S)=0,and S\P_S has an empty run].
Each UB superset is inside its indicated alternating set. UB(S)=G+(S) OR Z+(S) OR G-(S') OR Z-(S'). For every
failing S retain BOTH literal one-way Lemma20 clauses:
[First] S has a giant pair>=p+3,or |N_S|>=kappa+1,or d<|N_S|<=kappa and every kappa-superset of N_S INSIDE S has q'<=delta-2.
[Second] S' has a giant pair,or |P_(S')|>=kappa+1,or d<|P_(S')|<=kappa and every kappa-superset of P_(S') INSIDE S'
has q<=delta-2,or |P_(S')|=kappa,L(P_(S'))=A^c and no run of S'\P_(S') is empty. Only second/third first-side clauses
carry |L(S') intersect A^c|<=delta. No giant clause implies saturation or any converse. Full literal primary text
UMR266-274,300-302,315-324, including320-321, is provided to fix the exact domains/boundary.
(d) Retain every LJ condition of accepted UPAR2-R: fixed tie ordering, both near-A sorted chains at sizes j..r,
unique first P exit at r+1, other new type Q or G, theta_u<=-1,beta(u)>=2kappa+4d-2, all type caps and
  max(j,ceil((kappa+2d-1)/2))<=r<=kappa-d-1.
This interval is only a coarse necessary superset; all predecessor QQ inequalities still apply. At least one
predecessor is weak, both strong excluded. For weak tops require3n>=2b*+nu+q,n>=b*. For both weak require
z0+z>=4r-2kappa+nu and e+nu+E(pred bottoms)<=kappa-3b*; for mixed require
e<=kappa-r-d-z0-z-E(weak bottom),z0+z>=n(weak). Keep the accepted necessary kappa bounds as well.
(e) Compute W,sP,sQ,D_X,D_Y from the run data and retain exact(Defect), parity/nonnegativity and all per-run costs.
NEW uniform exclusion deletes F0 and every F=e case by Sec.2, so require F-e>=2. All remaining even e>=0,
nonunit labels, both mixed orientations and both-weak predecessors, unbounded parameters and p classes remain.
Outside T3 kappa>8d+6; no additional sign,deficiency,unit-label or selected-frame restriction is imposed.

Every hypothetical survivor outside T3 has these fields by accepted UPAR2-R, literal UMR/UFC and the new budget
lemma; the generic mass bounds in(b) are obtained directly by adding(Cost) to(W). Thus this is a COMPLETE remaining
necessary residual, finite per fixed parameters only, not a finite unbounded union or an inverse NF theorem.
FIRST UNPROVED UNIFORM LEMMA, POSITIVE-BUDGET-COVER: no actual target NF/frame on T\T3 induces R3. This is not
proved here. It is an equivalent exclusion target, not a reduction in logical difficulty, no-go or existence claim.

The three open named residuals instantiate ALL tests above, not only the following parameter supports. All have
d2,ID Theta(all)=e-2nu-4,Xi=Theta+nu+2,M_m=2m-4,ell_m=2kappa+2-2m and first-jump beta>=p+3. They are:
| Cell | N,h,R,delta; central m | a' min;max|c|;reservoir;|theta| | coarse remaining (b*,r,F); e both-weak / mixed |
|---|---|---|---|
| (25,53) | 54,27,102,46;2..26 | 40;47;+49;<106 | (5,15,4):0,2 /0,2; (7,16,8):0 /0 |
| (28,59) | 60,30,114,52;2..29 | 44;53;+55;<118 | (4,16,2):0 /0; (6,17,6):0,2,4 /0,2; (8,18,10):0 /0 |
| (29,61) | 62,31,118,54;2..30 | 46;55;+57;<122 | (5,17,4):0,2 /0,2; (7,18,8):0,2 /0,2 |
Reservoir '+c' means u1>=|c_l|+c for every l. The table is a NECESSARY SUPERSET, not a claim any entry survives the
full constraints. e=F removed by PROOF, not a unit assumption. Superset sizes in UB/Lemma20 are kappa as in row;
lo/hi are26-m/132-3m,29-m/147-3m,30-m/152-3m respectively. Giant-pair thresholds56,62,64; near-kappa caps44,50,52;
opposite positive-letter caps46,52,54 apply only at the literal second/third alternatives, never to giant clauses.
The exact first unproved LOCAL step in each row is excluding its complete R3 data for an actual NF/frame. Other
orientations/nonunit placements and all mixed windows are still required; these three rows do not replace full T.

## 8. Literal source/coverage protocol

Actual numbered packet headers supply ABSOLUTE PATH + WHOLE-FILE SHA256 + exact inclusive LF range for every import.
Raw source UTF8 rows are copied verbatim with original LF prefixes, not shortened reader previews. The manifest
records ACTUAL provided ranges; a whole-source digest never means omitted lines were pasted. Governing mathematical
bodies are supplied FULL, including UMR verdict1-38,UFC1-36 and scope-precision1-5, all mandatory UPAR2 errata1-3.
Used primary sources: proof-UPAR2-v1.md (4129386d5b625af1dfddab9b919790d1a5c7f04f0eb9846be903e9ab5d364a1d), exact
LJ/defect/predecessor/residual data; proof-UPAR-v1.md (f75d55674586b714c12f8ffeb6e57ef0fee9ffc4615e96c7b0def522501cbcef),
cap102-107; proof-UMR-v1.md (c403bfbae9f1c7b75698010cae78515a253154e689336e79006c588ff15023a9), literal data/parity/
windows/identity/UB/Lemma20; proof-UFC-v1.md (2d03076c9bbf1afa3d68e42bfc2fe9eeb4a62ee64b59e6c94c53f65a32b670c5),
cutoff23-27,E0/ENV200-225. Their full paths and exact ranges are in the actual headers, alongside the governing
verdicts/errata/clarifications. This supplies mathematical premises, not transitive re-verification of their proofs
or other literature. Primary UMR ranges137-139,161-165,201-209,266-274,300-302,315-324 are actually included.
All parent-preview statements were unaccepted exposure, re-derived after the fresh freeze, not independent
corroboration/strict preregistration. Old same-author routes and unfinished p29 work are disclosed in scope.
Science is written by hand only; machine operations are disclosed metadata/read/exclusive text/numbering steps.
No computation,enumeration,assertion,solver,test/model/native/network launch; parent alone reviews/accepts. No
full ordered Olson,other-k,priority,human/Lean/runtime claim. Full T still open exactly as specified above.
