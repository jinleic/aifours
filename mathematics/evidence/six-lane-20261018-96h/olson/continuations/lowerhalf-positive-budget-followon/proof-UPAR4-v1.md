# UPAR4: a uniform positive-budget exclusion and the entire remaining charge-failure residual

CANDIDATE, written by hand; parent/model gates not run by this worker. The full target is ENTIRE T\T3,
not selected cells. Scope/exposure are UPAR4-scope-v1.md LF1-79, actually included in the packet. Its explicit
arithmetic-before-freeze departure is permanent: subsequent derivation does NOT cure it. No compliance,
strict-preregistration, independent-discovery/corroboration, priority, human, Lean or runtime claim.

## 0. Scope, imports and outcome

T means prime p>=17, floor((p+7)/4)<kappa<=(p-3)/2; d=(p+1)/2-kappa>=2. Consider every frame of SOME
admissible NF with terminal k=p+1,kappa_hat=kappa of a length4p-2 increasing-original-index identity2p-subword
avoider over D_(2p), arbitrary extra pairs and genuine empty runs. No o_F/nonempty-run/rotation-pair/rigidity
premise. All even e/nonunit labels, both mixed predecessor orientations, all central mixed windows, ID, reservoir,
ENV/fullUB/both literal Lemma20 clauses and exact empty-tail boundary remain. Only their necessary subset is
needed for the new contradictions; the entire baseline is retained in the remaining residual.

Import accepted UPAR3-P/Z/R ONLY through its full parent verdict LF1-15 and errata1/2 LF1-8/1-19. In particular
T3={kappa<=8d+6} is excluded, and outside T3 every survivor induces literal corrected R3=R2 intersect{F-e>=2}.
The UPAR3 Sec.7 gloss is NOT the definition. Full governing older UPAR2/UPAR/UMR/UFC statements and mandatory
errata are integral literal packet inputs. Source citations and precise used LF are at the end and in headers.

THEOREM UPAR4-P (candidate): no target NF/frame exists on
  T4={ (kappa,p) in T : kappa<=26d-10 }={ (kappa,p) in T : 27kappa<=13p+3 }.
This strictly contains T3. In particular (25,53),(28,59),(29,61) are excluded. Full T is NOT proved.
THEOREM UPAR4-R (candidate): every remaining actual frame induces the complete literal R4 of Sec.7.

## 1. Common data and elementary counts (no unit hypothesis)

h=kappa+d,N=2h,R=4kappa+2d-2,delta=2kappa-2d. Run occurrence sets L_i partition R labelled letters;
c_l are odd nonzero, A={c_l<0},a=|A|,nu=sum_A|c_l|,e=sum_all(|c_l|-1),eta=nu-a in[0,e]. For U use
l(U)=|L(U)|,n(U),E(U),Theta(U),alpha(U)=|A\L(U)|,beta(U)=|L(U) intersect A^c|,beta'(U)=|L(U) intersect A|.
Then q=alpha+beta, q'=R-q, l=a-q+2beta. Literal parity is theta_i congruent |L_i| MODULO2, not integer equality;
empty theta is nonzero even. On every central mixed set U, with m=m(U), retain
  ell_m=2kappa+2-2m, M_m=2m-2d, eps=q mod2,
  x=max(eps,ell_m-q,M_m-q'), y=max(eps,M_m-q,ell_m-q'),
  e-2d+2-nu-y<=Theta(U)<=-2-nu+x,        d<=m<=kappa+1.                              (W)
A proper nonempty subset of one alternating set has m=its size. ID is sum_all theta=e-2nu-2d.

Fix any hypothetical frame outside T3 and its inherited LJ data: S has the earliest P exit at r+1, S' is other;
I=J_r(S),K=I union{u},Q=J_r(S'),X=S\K,Y=S'\Q, with fixed consistent sorted ties. Put
  b=2r-kappa, F=2b-4d+2, z0=q(I),zP=q'(K),z=q(Q), wA=beta'(K),w=beta(Q),W=wA+w,
  A0=kappa-b, P0=kappa+b-2d, x0=|X|=(kappa+2d-b)/2-1, y0=|Y|=x0+1.
Here b is ONLY the jump variable, not R_PAR's CM/DM tail size; B0 below is NOT its B(S), and Gamma is NOT ENV H(S).
Both predecessors are near-A, thresholds negative, at least one exactly-1. Weak means threshold-1; strong means
threshold<=-2. This describes the LAST sorted top value and its TAIL, not every value inside the top.
The inherited interval implies b<=kappa-2d-2, r central and r+1<=kappa-d; all X,Y theta are negative.
Let sP=P0-nu-zP-Theta(K),sQ=A0-nu-z-Theta(Q), and D_i=|L_i|-2-theta_i on X,Y; D_X,D_Y are their sums.
Each D_i is nonnegative even; l(U)<=|U|+D_U on a negative tail, and l(U)<=D_U on a strong tail.
More importantly, on a STRONG tail every nonempty run has D_i>=|L_i|>=1, hence D_i>=2 by parity:
  n(U)<=D_U/2.                                                                    (Strong-count)

Letter partition gives beta(X)+beta(Y)=zP-W and l(X)+l(Y)=zP+z-2W. Insert the latter into the two exact
endpoint expressions and ID INSIDE the calculation, obtaining
  B0:=F-e=2W+sP+sQ+D_X+D_Y>=2; Lambda:=B0-2W=sP+sQ+D_X+D_Y>=0.                       (Defect)
All slacks/e/D are even and nonnegative; none implies e=0. Define Gamma=2A0-2z-3Lambda.
The near-A upper bound on I and theta_u<=-1 give
  zP+sP>=z0+2b-2d+1; if I strong, replace1 by2.                                    (Order)
For a weak near-A r-top J, Theta(J)>=2r-3n(J)>=2r-3l(J). Combining with its exact upper endpoint gives
  a>=b+2q(J)-3beta(J)+(eta+s_J)/2.
Thus if Q weak, a>=b+2z-3w+(eta+sQ)/2; if I weak, z0>=2a+b-3wA.                     (Count)
For the latter write beta'(I)<=wA and q(I)=a-beta'(I)+beta(I); discard its nonnegative eta/slack only.
Accepted predecessor bounds (UPAR-QQ and UPAR2 Lemma3) retain
  both weak: e+nu+E(pred bottoms)<=kappa-3b, kappa>=3b+2d-1+3e/2;
  mixed: z0+z<= (kappa-b-2d)/2-e, kappa>=3b+2d+2e.                                (Pred)
The full unweakened predecessor tests remain in R3, not only these weakenings. The accepted cap is conditional:
  if a<=delta+1, negative empties in either alternating set <=d+ceil((a+1)/2)-1<=d+a/2. (Cap)
We prove its domain BEFORE every use below.

## 2. The weak-I/strong-Q orientation is excluded on the entire unbounded R3

Put tau=kappa-3b-2d>=2e>=0. Mixed(Pred) and weak-I(Count) give
  a<=tau/4-e/2+3wA/2-z/2.                                                        (M1)
Since wA<=B0/2=b-2d+1-e/2 and b<=(kappa-2d-2e)/3, this implies
  a<=kappa/2-4d+3/2-7e/4-z/2 <delta+1.
Thus(Cap) applies. Y is strong, so(Strong-count) gives E(Y)>=y0-D_Y/2>=y0-B0/2+W; these empties are negative.
Consequently a>=2y0-B0+2W-2d=tau+6d-2+e+2W. This lower bound exceeds(M1) by
  3tau/4+6d-2+3e/2+2w+wA/2+z/2>0.
Contradiction for d>=2. Only Y, not the entire Q top, was assumed strong. No e=0 restriction was introduced. []

## 3. Aggregate positive-tail charge, valid whenever Gamma>0

Assume Gamma>0. Put tmax=kappa+1-r=A0/2+1, qstar=A0-z-Lambda. Then 2qstar>Lambda>=0. Also
  2tmax-Lambda=kappa-3b+4d+e+2W>0
by(Pred): at least6d-1+5e/2+2W if both weak, or6d+3e+2W if mixed. Therefore
  tstar=min(tmax,qstar) is a positive integer with 2tstar>Lambda.
Take ANY t<=tstar runs V in Y, each containing a positive letter. Put D_V=sum_V D_i. Then l(V)>=t,
l(V)<=t+D_V, Theta(V)>=-t-D_V, and q(Q union V)=z+beta(V)-beta'(V). The union is a proper independent
subset of S', central of size r+t<=kappa+1<=h-1; so literal(W), not an unproved sorted-top assertion, applies.
Its needed upper entry is
  nu+2+Theta(Q union V)>=A0-z-(sQ+D_V)-t+2>=qstar-t+2>=2.
Thus eps<=1 cannot attain it. The P entry also cannot: using z<=A0,D_V<=B0,t<=A0/2+1 gives
  M_(r+t)-R+q(Q union V)
    <=-3kappa+b-4d+2+3t+z+B0
    <=-A0/2-8d+7-e<0.
Hence only ell_(r+t)-q(Q union V) can attain the required entry. Substitute the exact Q endpoint into(W):
  Theta(V)+2t+beta(V)-beta'(V)<=sQ,
or, since Theta(V)=l(V)-2t-D_V,
  2beta(V)<=sQ+D_V.                                                              (Charge)
If Y had at least tstar positive-containing runs, choosing tstar would give
2tstar<=2beta(V)<=sQ+D_V<=Lambda, impossible. Therefore it has fewer than tstar. Choose ALL its positive-
containing runs (or use beta(Y)=0 if none). The same charge now yields ONCE, without multiplying sQ,
  2beta(Y)<=sQ+D_Y.                                                               (Aggregate)
This is not a finite-parameter enumeration. No old family-specific charge lemma has been promoted. []

## 4. Both weak predecessors are impossible whenever Gamma>0

Use(Aggregate) and l(X)<=x0+D_X in beta(X)+beta(Y)=zP-W to get
  zP+sP<=x0+B0-W-(sQ+D_Y)/2.                                                     (W1)
Weak-I(Count) and(Order) give zP+sP>=2a+3b-2d+1-3wA. Hence
  2a<=x0+B0-3b+2d-1+2wA-w-(sQ+D_Y)/2.                                           (W2)
Since 2wA<=B0, and b<=kappa-2d-2, this proves
  a<=(kappa+b)/4-5d/2+1-e<=kappa/2-3d+1/2-e<delta+1.
Thus(Cap) applies; it was not assumed. Put alpha=alpha(Q)=z-w. Negative letters in Y are at most alpha, so
n(Y)<=alpha+beta(Y), and E(Y)>=y0-alpha-(sQ+D_Y)/2. All Y empties are negative. With(Cap) this gives
  a+2alpha>=kappa-b-sQ-D_Y.
Weak-Q(Count) says 2alpha<=a-b+w-(eta+sQ)/2. Combining the last two displays yields
  kappa<=2a+w-eta/2+sQ/2+D_Y.
Insert(W2), and use 2wA+D_Y/2<=B0 from(Defect), to bound the right side by
  x0+2B0-3b+2d-1-eta/2
    =(kappa+b)/2-5d+2-2e-eta/2
    <=kappa-6d+1-2e-eta/2<kappa.
Contradiction. Negative labels are counted as occurrences, not presumed unit weights. []

## 5. Strong-I/weak-Q is impossible whenever Gamma>0

X is strong. Thus beta(X)<=D_X, and(Aggregate) gives
  zP+sP<=W+D_X+(sQ+D_Y)/2+sP<=B0-W<=B0.
Strong(Order) gives zP+sP>=z0+2b-2d+2>=2b-2d+2, exceeding B0=2b-4d+2-e by2d+e>0.
Contradiction. This covers the OTHER mixed orientation at arbitrary excess. []

## 6. Uniform parameter theorem and the three diagnostics

Both weak: combine Q(Count) with a+eta<=kappa-3b-e from(Pred) to obtain
  2z<=kappa-4b-e+3w-(3eta+sQ)/2.
Substitute in Gamma=2kappa-2b-2z-3B0+6W, then use b<=(kappa-2d+1-3e/2)/3:
  Gamma>=kappa-4b+12d-6+4e+3w+6wA+(3eta+sQ)/2
       >=(44d-kappa-22)/3+6e+3w+6wA+3eta/2+sQ/2.                                (G-WW)
Strong-I/weak-Q: z0>=a-wA and mixed(Pred), combined with Q(Count), give
  3z<=(kappa-3b-2d)/2-e+3w+wA-(eta+sQ)/2.
Substitute and use b<=(kappa-2d-2e)/3:
  Gamma>=(5kappa-21b+38d-18+11e+12w+16wA+eta+sQ)/3
       >=(52d-2kappa-18+25e+12w+16wA+eta+sQ)/3.                                (G-SW)
If kappa<=26d-10, (G-WW) is at least6d-4>0, and(G-SW) is at least2/3>0. Sec.2 already excluded the
remaining mixed orientation without a parameter cutoff; Secs.3-5 now exclude both other branches. At least
one predecessor is weak by literal R2, so no branch is omitted. With accepted T3 this proves UPAR4-P.
T3 is inside T4 since d>=2 and (26d-10)-(8d+6)=18d-16>0. Strictness is witnessed by(25,53),d2,25>22.
The equivalent bound27kappa<=13p+3 is just substitution d=(p+1)/2-kappa, not a parameter computation.

| required (kappa,p) | d | outcome |
|---|---:|---|
| (25,53) |2| excluded by the SAME unbounded theorem, kappa<=42 |
| (28,59) |2| excluded by the SAME unbounded theorem, kappa<=42 |
| (29,61) |2| excluded by the SAME unbounded theorem, kappa<=42 |
No diagnostic cell or unit-label hypothesis was substituted for the full target. []

## 7. ENTIRE remaining literal residual; exact unproved step

DEFINE R3^lit := [literal corrected R2, UPAR2 LF194-218 with errata1-3] intersect{F-e>=2}, on T\T3,
where R2 includes EVERY corrected literal R_PAR test at UPAR LF216-275. These FULL bodies are actually pasted.
DEFINE R4 := R3^lit intersect{kappa>26d-10} intersect{Q predecessor weak} intersect{Gamma<=0}.
These are definitions by literal intersection, NOT replacement by a list of selected scalar summaries. Thus all
occurrence/label/parity/reservoir/theta bounds, ALL mixed windows/ID, E0, CM/DM/B/ENV, full UB failure and
BOTH Lemma20 clauses/exact no-empty-tail boundary, fixed ties/full Q chains/unique P exit/coarse r range and
ALL old QQ/defect tests remain. R2's F0 implications are retained literally; their premise is impossible here
because F-e>=2 and e>=0. No old zero-case proof is used as a new premise. The one removed orientation is
excluded by Sec.2, not assumed absent. No positivity/minimality restriction on B0 or even e is added beyond R3.

UPAR4-R follows: every actual surviving frame has R3^lit by accepted UPAR3; Sec.6 puts it outside T4; Sec.2
forces Q weak; Secs.3-5 force Gamma<=0. In addition(G-WW)/(G-SW) remain necessary at their exact respective
orientations. These inequalities may be retained as redundant tests, never substituted for the literal R4.
Finite ONLY for each fixed(kappa,p); the unbounded union is not asserted finite or nonempty. No converse,
feasibility, NF assembly or mathematical obstruction is claimed.

FIRST UNPROVED LEMMA, CHARGE-FAILURE-COVER: for EVERY(kappa,p)inT with kappa>26d-10, no actual target
NF/frame induces the literal R4 just defined. This has NOT been proved. It is the entire remaining positive-
budget cover, not a no-go or reduction in logical difficulty. Full T/ordered Olson/other terminal k remain open.

## 8. Literal source protocol

All external citations mean their FULL ABSOLUTE PATH + WHOLE-FILE SHA256 + ACTUAL LF in the packet headers;
the exact manifest is part of this package. UPAR=lowerhalf-full-uniform-parity/proof-UPAR-v1.md, used35-107,
146-155,216-275; UPAR2=lowerhalf-par-cover-followon/proof-UPAR2-v1.md,used95-123,194-224;
UPAR3=lowerhalf-jump-cover-followon/proof-UPAR3-v1.md,used69-74 only as accepted Gap, through full governing
verdict/errata. Its common24-68 and family-charge107-174 were read as exposure, NOT imported as general lemmas;
Order/Count/aggregate charge above are proved here from the literal windows. UMR's actual provided ranges are
18-28,49-56,64-68,88-118,137-139,161-165,201-209,238-239,252-258,266-274,300-302,315-324 (including320-321).
UFC=lowerhalf-uniform-fc/proof-UFC-v1.md,23-27/200-225 plus full verdict/finiteness clarification. All16 governing
mathematical MD bodies and full scope are supplied; whole-source pins do NOT mean whole primary proofs pasted.
Authority/disposition JSONs are pinned/read NOT PASTED control metadata, never mathematical premises. This does
not retroactively credit any earlier review with unprovided sources. No machine scientific calculation was used.
