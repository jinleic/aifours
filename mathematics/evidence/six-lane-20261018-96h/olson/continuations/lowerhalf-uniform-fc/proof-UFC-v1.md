# UFC v1: a uniform lower part of the UMR middle range, and an explicit high-strip residual

Owner: OlsonThirdCutWindow (same throttled math2 slot). Written by hand after /bin/date 2026-10-20T20:00:37-0700.
Scope UFC-scope-v1.md (SHA256 ba2b5e7ae1aa61e7e31a1058ca51941a65b39704cac913bed71ef14dc3ccad23), frozen
2026-10-20T19:47:01-0700 before any NEW derivation. Authority written-olson-uniform-fc-transition-v1.json, SHA256
e917c8ef930400d3e72b307d46b3879fe0e8a7592bfe7d74f23a3eed34668ebf, LF1-59 (absolute paths in Sec. 7).
STATUS: WRITTEN CANDIDATE, NOT REVIEWED OR ACCEPTED. Full UFC is NOT proved. Theorem U0 proves a uniform subrange;
Secs. 5-6 give the exact first UNPROVED uniform step HIGH-COVER and an explicit checkable residual for the rest.
Named cells: (8,23),(9,23),(10,29) are excluded by U0; (10,23) remains OPEN in the explicit residual R23.
No residual existence, converse, priority, novelty, Lean, human-referee, runtime, other-k or full ordered Olson claim.

## 0. Full target, exact partial theorem and the unproved step

T := {(kappa,p): p>=17 prime, floor((p+7)/4)<kappa<=(p-3)/2}. The full target is an avoider w of length 4p-2 over
D_(2p), with no identity-2p subword in increasing original index order, SOME admissible NF with terminal k=p+1 and
kappa_hat=kappa. Extra reflection pairs may be placed arbitrarily inside the odd blocks; every empty NF run separates
different reflection values; no o_F, nonempty-run, rotation-pair or rigidity premise is added. Every frame is considered.
Only accepted UMR at its literal scope is a mathematical premise, read through parent errata v1 and v2. Full UMR-F,
its frame/windows and its total identity are available, but its unproved FC and the withdrawn saturation wording are
not. FC717/FC19 status changed to accepted exact single-cell statements during this assignment (checkpoint03); their
internal lemmas are not used here, and every count below is re-derived.

THEOREM U0 (proved). Define T0 to be the part of T satisfying
  p=1 (mod4): kappa <= (3p+5)/8;     p=3 (mod4): kappa <= (3p+7)/8.                     (U0-range)
For every frame of every target NF with (kappa,p) in T0, Xi(S_ev)+Xi(S_od)<=-1. Hence no such NF exists in T0,
by the accepted UMR identity Xi(S_ev)+Xi(S_od)=e>=0. This is not a restriction silently imposed on the full target:
T\T0 is retained, with its exact unproved step and residual in Sec. 5. No entire p-union outside this statement is claimed.
THEOREM U1 (proved reduction on ALL T). The explicitly defined certificates of Sec. 5 are valid upper bounds. Outside
T0 a surviving word would have EVERY frame in R_U (Sec. 5); R_U is a finite integer-data relaxation, not an existence
claim or an inverse characterisation of NF avoidance. The first unproved uniform step is HIGH-COVER (Sec. 5.4): no
actual target NF/frame in T\T0 induces data in R_U. No proof of that step is supplied.

## 1. Literal UMR data and elementary count facts

Put N=p+1, R=p-1+2kappa, g=p+1-2kappa, d=g/2, h=N/2=kappa+d, delta=4kappa-p-1 (UMR LF18-19). d>=2 follows from
kappa<=(p-3)/2. A frame exists and all frames have the following properties (UMR LF88-118, UMR-F LF24-28).
(D1) The run letter sets L_0,...,L_(N-1) partition R letter OCCURRENCES. Each letter l has an odd nonzero integer c_l.
A={l:c_l<0}, A^c={l:c_l>0}, a=|A|, a'=R-a, nu=sum_A |c_l|, B=sum_all |c_l|, e=B-R. Then
  e>=nu-a>=0,  nu=a (mod2),  a'>=(p+kappa+1)/2.                                     (1)
Indeed e=(nu-a)+(Pi0-a'), where Pi0=sum_(A^c)|c_l|; the last bound and nu>=a, Pi0>=a' are UMR Lemma5(d), LF118.
(D2) Each run has an integer theta_i. An EMPTY run has a NONZERO EVEN theta (UMR Lemma10 LF201-209). Nonzero is
load-bearing below; evenness alone would not suffice. Theta(Q)=sum_(i in Q)theta_i. For the residual only we also
retain |theta_i|<2p and theta_i=sum_(l in L_i)c_l (mod2), which are literal UMR Lemma10 conclusions.
(D3) Central levels are d<=r<=kappa+1. A proper independent r-set of runs has m=r (UMR LF55-56), so every r-subset Q
of either alternating set S_ev={0,2,...,N-2}, S_od={1,3,...,N-1} has the UMR central windows (each S has h runs):
  ell_r=2kappa+2-2r, M_r=2r-g, q(Q)=|L(Q) symdiff A|, q'(Q)=R-q(Q), eps=q(Q) mod2,
  x_r(Q)=max(eps,ell_r-q,M_r-q'), y_r(Q)=max(eps,M_r-q,ell_r-q'),
  e-g+2-nu-y_r(Q) <= Theta(Q) <= -2-nu+x_r(Q).                                      (W_r)
Citations: UMR Lemma2 LF64-68, Lemma5(c) LF117-118, Lemma7 LF137-139, Lemma8 LF161-165, Lemma13 LF238-239 and
LF252-254. The lower endpoint is Pi0+2-y-2p=e-g+2-nu-y; no new realisation claim is imported. The same windows
hold for EVERY run set P with central m(P), replacing r by m(P); this is retained in R_U.
(D4) Xi(S)=Theta(S)+nu+d. UMR Lemma14 LF256-258 gives Xi(S_ev)+Xi(S_od)=e>=0. Secs. 3-4 prove their count from
(D1)-(D3) alone, then use (D4) for exclusion. Sec. 5's reverse certificates explicitly use (D4).

For a run set Q write L(Q)=union L_i, l(Q)=|L(Q)|, n(Q)=number of nonempty runs, E(Q)=number of empty runs;
  alpha(Q)=|A\L(Q)|, beta(Q)=|L(Q) intersect A^c|, alpha'(Q)=|A^c\L(Q)|, beta'(Q)=|L(Q) intersect A|.
Thus q=alpha+beta, q'=alpha'+beta', l=beta+beta', beta'=a-alpha. Distinct run sets have disjoint letter sets
when the run sets are disjoint (letters are occurrences), and n(Q)<=l(Q).
(F1) For disjoint Q1,Q2: a<=alpha(Q1)+alpha(Q2), a'<=alpha'(Q1)+alpha'(Q2), and at most alpha'(Q1)+alpha(Q2)
letters are outside L(Q1) union L(Q2). Proof: each letter is outside at least one of the disjoint letter sets;
a letter outside both is in A^c\L(Q1) or A\L(Q2). In particular if z1=q'(Q1), z2=q(Q2), and B1,B2 are disjoint
bottom sets outside Q1,Q2 in their respective alternating sets, then n(B1)+n(B2)<=z1+z2.              (Couple)
(F2) Sort each S by decreasing theta, ties arbitrarily but consistently. J_r is the top r, t_r its last theta,
B_r=S\J_r. Runs of J_r have theta>=t_r, runs of B_r have theta<=t_r. Empty theta>=-1 is >=2; empty theta<=0 is <=-2.
Hence: if t_r>=0, Theta(J_r)>=2E(J_r)>=2(r-l(J_r)); if t_r>=-1, Theta(J_r)>=2r-3n(J_r).
If t_r<=-1, Theta(B_r)<=-(h-r)-E(B_r); if t_r<=-2, Theta(B_r)<=-2(h-r); if t_r<=0, Theta(B_r)<=-2E(B_r).
(F3) At the levels below R>ell_r+M_r. If q<=ell_r-2, x_r=ell_r-q; if q'<=M_r-2, x_r=M_r-q'; otherwise x_r<=1.
This follows from q+q'=R and eps<=1. The three cases are disjoint and exhaustive.

## 2. Parameterisation and balanced levels (derived, not assumed from the hint)

If p=1mod4 write p=4j-3 and kappa=j+v-1. Then h=2j-1, d=j-v, R=6j+2v-6, delta=4v-2, 3<=v<=j-2, j>=5,
a'>=(5j+v-3)/2, and at level j: ell_j=M_j=2v.
If p=3mod4 write p=4j-1 and kappa=j+v. Then h=2j, d=j-v, R=6j+2v-2, delta=4v, 2<=v<=j-2, j>=5,
a'>=(5j+v)/2; at level j: (ell,M)=(2v+2,2v), at j+1: (ell,M)=(2v,2v+2).
Proof. Substitute p in T and in the definitions of Sec. 1. For p=4j-3, floor((p+7)/4)=j+1, hence kappa>=j+2 and
v>=3; kappa<=2j-3 gives v<=j-2. For p=4j-1 the same lower bound gives v>=2, while kappa<=2j-2 gives v<=j-2.
The displayed levels are central: d=j-v<=j and j+1<=kappa+1; also they are proper independent sizes since d>=2.
Solving ell_m=M_m gives 2kappa+2-2m=2m-2d, i.e. m=(kappa+d+1)/2=(h+1)/2=(p+3)/4. This derives the parent hint.
Finally (U0-range) is exactly j>=2v-1, or d>=v-1, in the corresponding parameterisation. Secs. 3-4 assume this
inequality; Sec. 5 does NOT assume it and retains the full complementary strip j<=2v-2.

## 3. Integer balanced level: p=4j-3, j>=2v-1

Here h=2j-1,d=j-v>=v-1,v>=3. In each S put J=J_j, t=t_j, B=S\J (j-1 runs), and classify J by (F3):
  G: q,q'>=2v-1 (x_j<=1); Q: z=q<=2v-2 (x_j=2v-z); P: z=q'<=2v-2 (x_j=2v-z).
LEMMA I1 (one set).
G: t<=-1, Xi(S)<=-v-E(B). P or Q: t<=0; if t<=-1, Xi(S)<=v-1-z-E(B); if t<=-2, Xi(S)<=-d-z.
Q cannot have t=0. P with t=0 (H): nu+z<=2v-2, at most nu+z letters lie outside L(J), and
  Xi(S)<=-d-z+2n(B).                                                               (IH)
Proof. G: Theta(J)<=-1-nu, so t<=-1; add the (F2) bottom bound and nu+d. For P/Q: Theta(J)<=2v-2-nu-z<j
because j>=2v-1. Thus t<=0. The two negative-threshold bounds follow by adding -(j-1)-E(B), resp. -2(j-1), then nu+d.
If Q had t=0: nu+z<=2v-2 and l(J)<=a+z, so 2j-2a-2z<=2v-2-nu-z, whence 2j-2v+2<=2a+z-nu<=nu+z<=2v-2.
But j>=2v-1 gives 2j-2v+2>=2v, a contradiction. For H the same upper window gives nu+z<=2v-2; outside letters
number alpha(J)+alpha'(J)<=a+z<=nu+z. Empty bottom runs contribute <=-2, nonempty ones <=0; add nu+d. []
LEMMA I2 (no H). If neither alternating set is H, their Xi sum is <=-1.
Proof. G with anything gives <=-v+(v-1)=-1 (by I1). Two P are impossible: (F1) gives a'<=z1+z2<=4v-4, while
(5j+v-3)/2>4v-4 since j>=2v-1. P with Q: the two bottom sets have 2(j-1) runs and n(B1)+n(B2)<=z1+z2 by (Couple),
so E(B1)+E(B2)>=2j-2-z1-z2; I1 gives the sum <=2v-2-z1-z2-E(B1)-E(B2)<=-2d.
For two Q, first suppose both t=-1. Write alpha_i=alpha(J_i), beta_i=beta(J_i), z_i=alpha_i+beta_i. By (F1),
l(J_i)=(a-alpha_i)+beta_i<=alpha_(3-i)+beta_i. The top lower bound and upper window give
  2j-3(alpha_(3-i)+beta_i)<=Theta(J_i)<=2v-2-nu-alpha_i-beta_i.
Summing gives z1+z2>=2j-2v+2+nu=2d+2+nu. Thus the sum <=2v-2-(2d+2+nu)<=-2-nu as d>=v-1.
If both t<=-2, the sum is <=-2d. If t1<=-2,t2=-1 (or vice versa), the sum is <=v-d-1-z1-z2-E(B2)<=0; a nonnegative
sum could occur only if d=v-1 and z1=z2=0. Then L(J1)=A=L(J2), disjoint, so A is empty, J2 consists of empty runs
and t2 is even, not -1. Therefore the integer sum is <=-1. []
LEMMA I3 (H). If S1 is H, the sum with S2 is <=-1.
Proof. Let z1=q'(J1), m=n(B1), lam=l(S2). I1 gives m+lam<=2v-2 and Xi(S1)<=-d-z1+2m. For J2 inside S2:
q'(J2)>=a'-lam>2v-2, because a'>=(5j+v-3)/2, lam<=2v-2 and j>=2v-1. Thus J2 is G or Q (not P).
If G: Xi(S2)<=-v-E(B2)<=-v-j+1+lam; sum <=-2j+1-z1+2m+lam<=-2j+4v-3<=-1.
If Q and t2=-1: by (Couple), m+n(B2)<=z1+z2, so E(B2)>=j-1-z1-z2+m. Thus the sum is
  <=-d-z1+2m+v-1-z2-E(B2)<=-2d+m<=0.
A nonnegative value would force d=v-1,m=2v-2 and lam=0; all runs of S2 are then empty, contradicting t2=-1 evenness.
If Q and t2<=-2: (Couple) gives m<=z1+z2 and I1 gives sum <=-2d-z1-z2+2m<=-2d+m<=0. Again a nonnegative sum forces
d=v-1,m=2v-2,lam=0. The chain m<=a+z1<=nu+z1<=2v-2 also forces nu=a and a+z1=2v-2. Since S2 is empty, its BOTTOM j
runs K (ranks j,...,2j-1) have theta<=t2<=-2, q(K)=a and q'(K)=R-a; hence y_j(K)=2v-a (a<=2v-2 and q' large).
The lower window gives Theta(K)>=e-2d+2-a-(2v-a)=e-4v+4>=-4v+4, while Theta(K)<=-2j=-4v+2, impossible.
All Q cases give an integer sum <=-1. []
This proves U0 in the p=1mod4 subrange: I2 and I3 exhaust the pairs. The count used (D1)-(D3), not (D4); applying
(D4) now contradicts Xi(S_ev)+Xi(S_od)=e>=0. No frame and hence no target NF exists in this subrange.

## 4. Adjacent balanced levels: p=4j-1, j>=2v-1

Here h=2j,d=j-v>=v-1,v>=2 (also d>=2). Put J=J_j, K=J_(j+1)=J union {u}, t=t_j, t+=t_(j+1), B=S\J (j runs),
C=S\K (j-1 runs). At level j classify J as G (q>=2v+1,q'>=2v-1), Q (z0=q<=2v), P (z=q'<=2v-2).
At level j+1 classify K as G+ (q>=2v-1,q'>=2v+1), Q+ (z=q<=2v-2), P+ (z+=q'<=2v).
The six exhaustive classes of S are: G; P with t<=-1; P with t=0 (H); Q/G+; Q/Q+; Q/P+ (hybrid).
LEMMA A1 (one set).
G: t<=-1, Xi<=-v-1-E(B). P: t<=0; if t<=-1, Xi<=v-2-z-E(B); if t=0 (H), nu+z<=2v-2, l(B)+l(S')<=nu+z and
  Xi<=-d-2-z+2n(B).                                                               (AH)
G+: t+<=-1, Xi<=-v-E(C). Q+: t+<=-1, Xi<=v-1-z-E(C); if t+<=-2 then Xi<=-d-z.
Proof. In G/G+, the top upper window is <=-1-nu. In P, it is 2v-2-nu-z<j, so t<=0; outside letters<=a+z<=nu+z.
Add the corresponding bottom bounds of (F2). In Q+, the upper window is 2v-2-nu-z. If t+>=0, then nu+z<=2v-2,
l(K)<=a+z and 2(j+1)-2a-2z<=2v-2-nu-z, so 2j-2v+4<=nu+z<=2v-2, contradicting j>=2v-1. Thus t+<=-1; add the
negative bottom bounds. All Xi constants follow by adding nu+d with d=j-v. []
LEMMA A2 (ordinary pairs). If neither S is H or hybrid, the Xi sum is <=-1.
Proof. Two P are impossible: a'<=(2v-2)+(2v-2)=4v-4 by (F1), whereas a'>=(5j+v)/2>4v-4. P with Q+ has 2j-1 bottom
runs, so (Couple) gives E(B1)+E(C2)>=2j-1-z1-z2; sum <=(v-2)+(v-1)-z1-z2-E(B1)-E(C2)<=-2d-2.
For two Q+: if both t+=-1, the (F2) top lower bound and disjointness give
  2(j+1)-3(alpha_(3-i)+beta_i)<=2v-2-nu-alpha_i-beta_i.
Summing: z1+z2>=2j-2v+4+nu=2d+4+nu; sum <=2v-2-(2d+4+nu)<=-4-nu. If both t+<=-2, sum<=-2d. If only one is <=-2,
the sum is <=v-d-1-z1-z2-E(C_other)<=0; nonnegativity forces d=v-1,z1=z2=0. Then both top letter sets equal A,
so A is empty and the other threshold is even, not -1. The integer sum is therefore <=-1.
All other pairs have a G or G+ bound <=-v, while the other ordinary Xi is <=v-1; the sum is <=-1. []
LEMMA A3 (H). If S1 is H, its sum with S2 is <=-2.
Proof. Write z1=q'(J1), m=n(B1), lam=l(S2). A1 gives m+lam<=2v-2 and Xi1<=-d-2-z1+2m. For any Q inside S2:
q'(Q)>=a'-lam>2v, since a'>=(5j+v)/2, lam<=2v-2, j>=2v-1. So S2 is G or Q/G+ or Q/Q+ (not P or hybrid).
G: Xi2<=-v-1-j+lam; sum<=-2j-3+2m+lam<=-2j+4v-7<=-5.
G+: Xi2<=-v-j+1+lam; sum<=-2j-1+2m+lam<=-2j+4v-5<=-3.
Q+ with t+=-1: by (Couple) E(C2)>=j-1-z1-z2+m, and sum <=v-d-3-z1-z2+2m-E(C2)<=-2d-2+m<=2v-2d-4<=-2.
Q+ with t+<=-2: (Couple) gives m<=z1+z2; sum<=-2d-2-z1-z2+2m<=-2d-2+m<=-2. []
LEMMA A4 (hybrid with negative upper threshold). If S is Q/P+ with t+<=-1, its sum with S' is <=-1.
Proof. Let z0=q(J)<=2v, z+=q'(K)<=2v. Expanding z+ as in Sec. 1:
  z+=(a'-beta(J)-beta(u))+(a-alpha(J)+beta'(u))>=R-z0-beta(u).
Thus beta(u)>=R-z0-z+>=6j-2v-2, a<=alpha(J)+z+<=4v and the number o of letters outside L(K) is <=z0+z+.
For Q inside S', beta(Q)<=alpha'(K)<=z+<=2v; hence q'(Q)>=a'-2v>=R-6v=2v+6d-2>2v. This excludes P and P+ in S',
so S' is G or Q/G+ or Q/Q+. The upper window for K and its negative bottom give Xi(S)<=v+1-z+-E(C).
G: the 2j-1 runs C union B(S') have <=o<=z0+z+ letters, so sum<=v+1-z+-v-1-(2j-1-z0-z+)<=1-2d<=-3.
G+: the 2j-2 runs C union C(S') give sum<=v+1-z+-v-(2j-2-z0-z+)<=3-2d<=-1.
Q+: (Couple), with the near-A^c set K and the near-A set K(S'), gives E(C)+E(C(S'))>=2j-2-z+-z', where z'=q(K(S'));
sum<=v+1-z++v-1-z'-(2j-2-z+-z')=2-2d<=-2. []
LEMMA A5 (hybrid with nonnegative upper threshold). If S is Q/P+ with t+>=0, its sum with S' is <=-1.
Proof. Retain z0,z+,u,o from A4; its letter bounds did not require t+<0. All runs in J and K have theta>=0.
Step 1. Write alpha=alpha(J), beta=beta(J). The top-j upper window is 2v-nu-alpha-beta, so beta<=2v-nu-alpha.
Also (F2) gives 2j-2a+2alpha-2beta<=2v-nu-alpha-beta; eliminating beta gives
  nu-a+2alpha<=2v-j.                                                              (A5.1)
If j>=2v+1 this is impossible, as nu>=a. For j=2v or j=2v-1, its right side is 0 or1, so nu=a and alpha=0
(by nu=a mod2 and alpha integral). Thus A is inside L(J), every letter outside L(K) is in A^c, o=alpha'(K),
z+=o+a, beta'(u)=0, and the preceding lower estimate gives beta(J)>=2j-2v-a=2d-a.
Step 2. For every w in J let Q_w=(J\{w}) union {u}, a j-subset of S with theta>=0 throughout. The run u is nonempty,
since beta(u)>=6j-2v-2>ell_j. Hence Theta(Q_w)>=2E(J\{w}), q(Q_w)>=beta(u)>ell_j and
q'(Q_w)=(o+beta(w))+(a-beta'(w)). In its upper window the eps branch cannot dominate (it would give <=-1-nu<0), so
  o+2a+beta(w)-beta'(w)+2E(J\{w})<=2v-2   for EVERY w in J.                         (A5.2)
Sum all j inequalities, using sum beta(w)>=2d-a, sum beta'(w)=a, and each empty run occurs j-1 times:
  j*o+(2j-2)*a+2(j-1)E(J)<=2j(v-2)+2v.                                           (A5.3)
If j=2v-1 the right side divided by j is 2v-3+1/j; if j=2v it is 2v-3. Since 2j-2>=j, this implies o+a<=2v-3.
It also gives a<=v-1 (indeed a<=v-2 when j=2v), by comparing with (2j-2)(v-1).
Step 3. S' has no letter of A. For its upper top set K'=J_(j+1)(S'), q(K')=a+l(K')<=a+o<=2v-3, so it is Q+ and
its upper threshold t'+<=-1. If t'+<=-2, take Q'=B_j(S'), the BOTTOM j runs (ranks j+1,...,2j). They have theta<=-2,
q'(Q')>2v, q(Q')=a+l(Q'), and y_j(Q')<=max(1,2v-a)=2v-a (as a<=v-1). The lower window gives
Theta(Q')>=e-2d+2-a-(2v-a)>=-2j+2, contradicting Theta(Q')<=-2j. Thus t'+=-1.
Let lJ=l(K'), lB=l(C(S')), nB=n(C(S')). Its top lower bound and upper window give
  2(j+1)-3lJ<=2v-2-a-(a+lJ), hence lJ>=d+2+a.                                    (A5.4)
Step 4. If t+>=1, then j+1<=Theta(K)<=2v-2a-o<=2v, forcing j=2v-1,a=o=0, contrary to lJ>=d+2+a and lJ<=o.
So t+=0. Put m=n(C). The upper window and empty bottom bound give Xi(S)<=-d+2-a-o+2m. For S', the top upper
window and bottom bound give Xi(S')<=-d-a-lJ+nB. Also m+lJ+lB<=o and nB<=lB. Consequently
  Xi(S)+Xi(S')<=-2d+2-2a+o-3lJ-lB
              <=2v-5d-7-6a-lB<=-3v-2<0,                                         (A5.5)
using o+a<=2v-3, (A5.4) and d>=v-1. The integer sum is <=-1. []
This proves U0 in the p=3mod4 subrange. A3 handles H, A4-A5 handle hybrid, and A2 all remaining pairs. The count used
(D1)-(D3), not the total identity. Now (D4) contradicts the negative sum. This completes U0 for BOTH residue classes.

## 5. Full-range certificates and the exact surviving high-strip residual

This section applies to ALL T, not just U0-range. It describes what remains unproved; it does not claim that a
surviving residual tuple, frame or avoider exists.

### 5.1 A further uniform empty-set exclusion

LEMMA E0. No target frame with a=0 has an alternating set S whose runs are all empty.
Proof. Then nu=0, q(Q)=0,q'(Q)=R for every subset Q of S. At central level r=d, M_d=0 and ell_d=delta+2<R, so y_d=0
and every d-subset has Theta>=e-2d+2>=-2d+2. If d runs had negative theta, their nonzero-even theta would sum to
<=-2d: impossible. Thus at most d-1 empty runs are negative, leaving at least h-(d-1)=kappa+1 positive empty runs.
Choose kappa+1 of them, a central independent set. ell_(kappa+1)=0 and M_(kappa+1)=delta+2<R, so x=0 and Theta<=-2,
while their sum is >=2(kappa+1)>0. Contradiction. This lemma uses only (D1)-(D3). []

### 5.2 Explicit upper/lower sorted certificates

For an integer t let rho(t) be t minus the largest NONZERO EVEN integer <=t. Explicitly
  rho(0)=2, rho(1)=3; otherwise rho(t)=t-2floor(t/2) (0 for even t, 1 for odd t).       (rho)
This is an integer definition, not a numerical computation. Thus an empty theta<=t is <=t-rho(t), and an empty
theta>=s is >=s+rho(-s) (negation reverses the two bounds).
For each central r in [d,kappa+1], retain top J_r, threshold t_r, bottom B_r=S\J_r. Independently let K_r be the
BOTTOM r runs, s_r its largest theta (rank h-r+1), F_r=S\K_r. All runs of F_r have theta>=s_r. Define
  C_r(S)=x_r(J_r)+d-2+(h-r)t_r-rho(t_r)E(B_r),
  D_r(S)=y_r(K_r)+d-2-(h-r)s_r-rho(-s_r)E(F_r),
  C(S)=min_(d<=r<=kappa+1) C_r(S),  D(S)=min_(d<=r<=kappa+1) D_r(S),
  H(S)=min(C(S),D(S')), where S' is the other alternating set.                      (Env)
LEMMA ENV. On every frame in T, Xi(S)<=C(S), Xi(S')<=D(S), and Xi(S)<=H(S). In particular
  Xi(S_ev)+Xi(S_od)<=H(S_ev)+H(S_od).                                                (ENV)
Proof. The top window gives Theta(J_r)<=-2-nu+x_r; all bottom runs have theta<=t_r and each empty one gains rho(t_r).
Adding nu+d gives Xi(S)<=C_r(S). The bottom window gives Theta(K_r)>=e-2d+2-nu-y_r; all remaining runs have
 theta>=s_r and each empty one gains rho(-s_r). Adding nu+d gives
Xi(S)>=e-d+2-y_r+(h-r)s_r+rho(-s_r)E(F_r); by (D4), Xi(S')=e-Xi(S)<=D_r(S). Minimise over r, then combine. []
Thus H(S_ev)+H(S_od)<=-1 is a written sufficient certificate for the full desired FC inequality at ANY parameter.
No enumeration of these minima or any scientific computation was performed.

### 5.3 A finite, explicit residual R_U

The residual is a SET OF INTEGER DATA with the following tests. It is a relaxation of actual NF/frame data, NOT a
converse or an assertion that these tests suffice for an NF or an avoider.
(R1) (kappa,p) lies in T\T0. Equivalently j<=2v-2 in Sec. 2's corresponding parameterisation. Use N,R,g,d,h,delta as
in Sec. 1. Give a partition of R letter occurrences into N run sets, their odd nonzero labels c_l and N integers
theta_i. Retain (D1)-(D4), theta parity/bounds in (D2), and every central mixed-set window of (D3), with
m(P)=number of maximal cyclic intervals of a proper nonempty P (m(empty)=m(all)=0). In addition retain the literal
UMR Lemma4 bounds max_l|c_l|<=p-6 and #{l:|c_l|=1}>=|c_l|+2kappa-1 for every letter l (UMR LF90-98). These are
necessary for data induced by a frame, not sufficient for one. E0 additionally requires
  a>0 OR [l(S_ev)>0 AND l(S_od)>0].                                                  (R1E)
(R2) Compute (Env) from the actual sorted data, with no presumed sign of any threshold. Require
  H(S_ev)+H(S_od)>=e>=0.                                                            (R2)
(R3) At least one of the following literal UMR certificates UB(S_ev),UB(S_od) fails. Here is their exact definition,
so this is checkable without guessing a residual characterisation. For S set N_S={i in S:theta_i>=0},
P_S={i in S:theta_i<=0}. For central r<=kappa put lo_r=kappa+1-r, hi_r=R+g+kappa+1-3r.
  G+(S): for some r,Q with N_S subset Q subset S, |Q|=r, lo_r<=q(Q)<=hi_r.
  G-(S): for some r,Q with P_S subset Q subset S, |Q|=r, lo_r<=q'(Q)<=hi_r.
  Z+(S): |N_S|<=kappa and every kappa-superset Q of N_S in S has q(Q)=0.
  Z-(S): [|P_S|<kappa and every kappa-superset Q of P_S in S has q'(Q)=0] OR
          [|P_S|=kappa, q'(P_S)=0, and S\P_S contains an empty run].
  UB(S):=G+(S) OR Z+(S) OR G-(S') OR Z-(S').
These are exactly UMR LF266-274,300-302; the word 'subset' here permits equality. No additional saturation premise.
(R4) For each S at which UB fails retain the ONE-WAY UMR Lemma20 conditions (LF315-324):
  (i) S has two runs totalling >=p+3 letters, OR |N_S|>=kappa+1, OR
      d<|N_S|<=kappa and every kappa-superset Q of N_S has q'(Q)<=delta-2;
  (ii) S' has two runs totalling >=p+3 letters, OR |P_(S')|>=kappa+1, OR
      d<|P_(S')|<=kappa and every kappa-superset Q of P_(S') has q(Q)<=delta-2, OR
      |P_(S')|=kappa, L(P_(S'))=A^c and no run of S'\P_(S') is empty.
In the second/third alternatives of (i), retain |L(S') intersect A^c|<=delta, at the literal Lemma20 scope only.
The giant alternatives do NOT imply the level-kappa inequalities, and no converse or residual nonemptiness is claimed.

THEOREM U1 (proof). A hypothetical surviving target word at any (kappa,p) cannot lie in T0 by U0. Every one of its
frames has the numerical properties R1, including E0 and the literal UMR bounds; ENV plus (D4) gives R2; UMR-P
(LF303-307) gives R3, and literal Lemma20 gives R4 for each failing S. Thus every such frame induces data in R_U.
Conversely is NOT claimed: integer data in R_U may fail other word, NF, block-value or generator constraints. []

### 5.4 The exact unproved uniform step

HIGH-COVER (NOT PROVED): for (kappa,p) in T\T0, every actual target NF/frame has either BOTH UB certificates, or
H(S_ev)+H(S_od)<=-1. Equivalently, no actual target NF/frame induces data in R_U. This is the first unproved uniform
step of THIS packet, not a claim that a rule is false, that a residual is realised, or that another route cannot work.
The cover would complete full UFC via U0, UMR-P and ENV. This is an equivalent exclusion target, not a proved
reduction in logical difficulty. Nothing here proves it, and R_U remains the explicit open boundary. All fully proved subrange and conditional certificate statements have been retained above.

The limitation is substantive: U0 uses j>=2v-1 to control sorted thresholds and to force nu=a, alpha(J)=0 in A5.
For arbitrary high-strip parameters the same A5 derivation gives only
  nu-a+2alpha(J)<=2v-j,                                                            (HighQ)
which need not force either equality. Even purely negative Q/Q upper bounds lose their uniform negative margin when
d<v-1. No assertion of saturation, a selected UB failure, or a substitution of a small-cell constant repairs these
missing inequalities. R_U deliberately retains all sign/giant/mixed-window cases, not merely the hybrid branch.

## 6. Required named cells and the complete (10,23) residual

All values in this table are derived by substituting into Secs. 1-2, not by importing FC717/FC19 constants.
| (kappa,p) | word/group; terminal k | N,h,R,g,d,delta | j,v; central levels | Actual outcome in this packet |
|---|---|---|---|---|
| (8,23) | length90 over D_46; k24 | 24,12,38,8,4,8 | j6,v2; 4..9 | EXCLUDED by Sec.4: j>=2v-1 |
| (9,23) | length90 over D_46; k24 | 24,12,40,6,3,12 | j6,v3; 3..10 | EXCLUDED by Sec.4: j>=2v-1 |
| (10,23) | length90 over D_46; k24 | 24,12,42,4,2,16 | j6,v4; 2..11 | OPEN at HIGH-COVER; residual R23 below |
| (10,29) (chosen p29 cell) | length114 over D_58; k30 | 30,15,48,10,5,10 | j8,v3; 5..11 | EXCLUDED by Sec.3: j>=2v-1 |
For (8,23), level6 has (ell,M)=(6,4), level7=(4,6), a'>=16. For (9,23): (8,6),(6,8), a'>=17. For (10,29), the
integer balanced level8 has (ell,M)=(6,6), a'>=20. Theorems I1-I3 and A1-A5 cover EVERY frame, not a chosen subfamily.
The parameter ranges are not limited to the displayed cells; no fixed-deficiency or single residue-class restriction
was substituted for the target. The general T0 statement is retained in full.

R23, the explicit unclosed case (10,23), is R_U specialised as follows (with all its finite tests, not just this table):
- 24 cyclic run sets partition 42 letters; odd nonzero c_l with max|c_l|<=17 and unit reservoir>=|c_l|+19 for every l;
  a'=42-a>=17, nu=sum_A|c_l|, e=sum(|c_l|-1)>=nu-a>=0, nu=a mod2. Integer theta_i satisfy |theta_i|<46, parity of
  their run letter sum, nonzero even at empty runs, total Theta(all)=e-2nu-4. Require R1E from E0.
- Central m=2..11, ell_m=22-2m, M_m=2m-4, q'=42-q,
  x_m=max(eps,22-2m-q,2m-4-q'), y_m=max(eps,2m-4-q,22-2m-q').
  Every central run set P (including mixed/non-independent ones) obeys
    e-2-nu-y_m(P)<=Theta(P)<=-2-nu+x_m(P).
- For each alternating 12-run set S and r=2..11 compute
    C(S)=min_r[x_r(J_r)+(12-r)t_r-rho(t_r)E(B_r)],
    D(S)=min_r[y_r(K_r)-(12-r)s_r-rho(-s_r)E(F_r)], H(S)=min(C(S),D(S')).
  Require H(S_ev)+H(S_od)>=e>=0. For UB use r=2..10, lo_r=11-r and hi_r=57-3r and the EXACT predicates of R3.
  At least one UB fails.
- At every failing S, R4 reads: S has two runs totalling>=26 letters, OR |N_S|>=11, OR 2<|N_S|<=10 and every
  10-superset Q of N_S has q'(Q)<=14; simultaneously S' has a >=26-letter pair, OR |P_(S')|>=11, OR
  2<|P_(S')|<=10 and every 10-superset Q of P_(S') has q(Q)<=14, OR the boundary |P_(S')|=10, L(P_(S'))=A^c and
  no run outside P_(S') empty. The second/third first-side clauses imply |L(S') intersect A^c|<=16 only at their
  literal scope. No saturation inference is made for giant pairs or for other levels.

Location of the unproved cell step. At level6 (ell,M)=(10,8), the G/Q/P thresholds are q>=9,q'>=7; q<=8; q'<=6.
At level7 (8,10), they are q>=7,q'>=9; q<=6; q'<=8. The subrange proof needs j>=2v-1=7 but has j=6.
A positive level6 P threshold is nevertheless excluded here: (W_6) would give 6<=Theta(J6)<=6-nu-q'(J6), forcing
nu=q'(J6)=0, A empty and all letters in J6. The other alternating set would then be empty, violating E0.
What is NOT proved is the remaining HIGH-COVER for ALL R23 cases. For example, in its nonnegative Q6/P7 hybrid
branch (HighQ) becomes nu-a+2alpha(J6)<=2. This allows the unexcluded integer alternatives
  (nu-a,alpha(J6))=(0,0),(0,1),(2,0),
not just nu=a,alpha=0. No realisation of any alternative is claimed. Nor is R23 restricted to this illustrative
branch: all other sign/type, giant-pair, lower-window and mixed-set conditions above are retained. The certificate
cover is the unproved assertion that no actual NF/frame induces such R23 data. It has not been established.

## 7. Literal interface, status update and non-claims

| Input | Absolute path; whole-file SHA256 | Inclusive LF | Scope/use |
|---|---|---|---|
| Authority | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-olson-uniform-fc-transition-v1.json; e917c8ef930400d3e72b307d46b3879fe0e8a7592bfe7d74f23a3eed34668ebf | 1-59 | Full T, named cells, frozen target and rules |
| Frozen scope | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-fc/UFC-scope-v1.md; ba2b5e7ae1aa61e7e31a1058ca51941a65b39704cac913bed71ef14dc3ccad23 | 1-79 | Complete prior exposure; no new derivation before freeze |
| Accepted UMR verdict | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-verdict-v1.md; a2535971cb214e399433235a4b9fca2de7328d15bec2c2f4eece35c05456c772 | 1-26 | Exact UMR-F, identity, conditional UB and one-way Lemma20 scopes |
| UMR proof | /Users/jinleic/repos/aifours/mathematics/evidence/six-lane-20261018-96h/olson/continuations/lowerhalf-uniform-middle-range/proof-UMR-v1.md; c403bfbae9f1c7b75698010cae78515a253154e689336e79006c588ff15023a9 | 18-28,49-56,64-68,88-118,137-139,161-165,201-209,238-239,252-274,300-327 | Frame/labels, windows, empty theta and parity, identity; literal UB and Lemma20 only in residual |
| UMR erratum v1 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v1.md; b83313b3fe828ee19a0902e9a5149db42ee55318500f92bac577b4bbd7088c5f | 1-10 | Connectivity link restricted; withdrawn saturation and frame quantifiers |
| UMR erratum v2 | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-UMR-parent-erratum-v2.md; 2a5f142ef136b04c15304137a4ba19946d0fee115ce18e8660817cd25bc902a2 | 1-9 | Residual wording and one-way scope; no converse/existence inference |
| Parent hint/exposure, untrusted | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/parent-post-FC19-scoping-exposure-v1.md; 0d92d4f2fe7e99b5b21ddcd274c5499a2dc074ca2877df71b754f28065b0ed62 | 1-5 | Read after freeze; balance formula independently derived in Sec.2 |
| FC717 accepted cell/status only | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC717-parent-verdict-v1.md; 0f201041f0885e5c88ec7c05739bd67781e8a1619be31202317cc9cd2adb4789 | 3-10 | Status update checkpoint03; no cell lemma used uniformly |
| FC19 accepted cells/status only | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC19-parent-verdict-v1.md; 7be12861b233714bb4bdd583a91e0c699ddb3302bebbdbb179f443aeb0b54e77 | 3-11 | Same; no cell lemma premise |
| FC717 wording erratum | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC717-parent-erratum-v1.md; 26ce36de138ba2f53dcb98a9aed6b3414e5ad5b0c407da2718e3712602bbadb7 | 1-7 | Status context; nonzero empty theta is load-bearing here too |
| FC19 import erratum | /Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/review/olson-FC19-parent-erratum-v1.md; 930380257c675c31e32715bef5233ec6acdb192e836c4ab2f141021cd0ac4a65 | 1-6 | No FCW/balfull mathematical input is promoted |

The accepted primitive inputs enter ONLY through UMR, namely exactly UMR verdict LF24: NF; GRX if-direction; SC0
applied to Y'z; ZSTRUCT/FB at exact (S') parameters (p-1,kappa-1); the S1 definition; stated LOWER conventions.
Historical method exposure to the FC717/FC19 proofs is fully disclosed in the frozen scope (paths/hashes/LF ranges).
The status change does not alter that immutable historical scope and does not import their internal counts.
Not claimed: full UFC, exclusion of R_U/R23, residual nonemptiness, any other terminal k, a full prime union outside
U0, full ordered Olson, INV*, reflection rigidity/o_F assembly, priority, novelty, human-referee, Lean or runtime
verification. The parent controls reviews and acceptance. No mathematical computation, enumeration, script, test,
solver, assertion statement, network, nested agent or model CLI was used.
