# UPAR5: positive-gain cover of the entire literal charge-failure residual

CANDIDATE written proof, not parent-accepted or machine/human/Lean verified. BOTH physical source parts must
be supplied to EVERY reviewer. Part2 is a byte-identical NEW copy of the HISTORICAL UPAR4 literal core: its
old scope/deadlines/status describe that stage, not this continuation. CURRENT operative parent scope and
UPAR5-exposure-acknowledgement-v1.md in part1 govern. The earlier UPAR4 pre-freeze PROCESS MAJOR remains
permanent and uncured; no compliance/strict-preregistration/independent-discovery/corroboration/priority claim.

## 0. Full target and statements

T: prime p>=17, floor((p+7)/4)<kappa<=(p-3)/2; d=(p+1)/2-kappa>=2. Keep the EXACT antecedent: a length4p-2
word over D_(2p) avoiding identity2p-subwords in increasing ORIGINAL index order, with SOME admissible NF of
terminal k=p+1,kappa_hat=kappa; every actual frame, arbitrary extra odd-block pairs, genuine empty-run rule.
No o_F/nonempty-run/rotation-pair/rigidity hypothesis. No other terminal-k or full ordered Olson claim.

Import UPAR4-P/R through FULL parent verdict LF1-13 and BOTH mandatory errata LF1-7/1-13, plus their accepted
upstream premises at literal scopes. Thus T4={kappa<=26d-10} is excluded and every survivor on ENTIRE T\T4
induces corrected literal R4=R3^lit intersect{kappa>26d-10} intersect{Qweak} intersect{Gamma<=0}. Literal R3
retains EVERY corrected R_PAR/R2 test and F-e>=2. All even e>=0/nonunit labels, both Iweak/Istrong cases,
arbitrary positive budgets, all mixed central windows/ID/reservoir/CM/DM/ENV/fullUB/both Lemma20 clauses and
exact empty-tail boundary remain. No scalar gloss, Gamma0, unit, sQ0 or small-budget substitution is made.

THEOREM UPAR5-C (candidate): no actual target NF/frame anywhere on ENTIRE T\T4 induces that literal R4.
COROLLARY UPAR5-T (candidate): combined with accepted UPAR4-P/R, no target NF with the stated antecedent
exists anywhere on ENTIRE T. The three diagnostics(43,89),(47,97),(49,101) are uniform instances, not premises.
This is NOT the full ordered Olson theorem, another terminal k, or a publication/verification certificate.

## 1. Actual common data, parity and conditional bounds

Use the exact UPAR4 common data, with its errata; the following fixes all symbols actually used. Put
h=kappa+d,N=2h,R=4kappa+2d-2,delta=2kappa-2d. Run occurrence sets L_i partition R odd-labelled letters c_l.
A={c_l<0},a=|A|,nu=sum_A|c_l|,e=sum_all(|c_l|-1),eta=nu-a in[0,e]. For a run set U let l(U),n(U),E(U),Theta(U)
be its letter/nonempty/empty/theta sums; alpha(U)=|A\L(U)|,beta(U)=|L(U) intersect A^c|,beta'(U)=|L(U) intersect A|.
Then q=alpha+beta, q'=R-q, l=a-q+2beta. theta_i congruent |L_i| MODULO2; empty theta is nonzero even.
For EVERY central mixed U, m=m(U) in[d,kappa+1], the literal two-sided windows are retained:
  ell_m=2kappa+2-2m, M_m=2m-2d, eps=q(U) mod2,
  x=max(eps,ell_m-q,M_m-q'), y=max(eps,M_m-q,ell_m-q'),
  e-2d+2-nu-y<=Theta(U)<=-2-nu+x.                                                  (Win)
Proper nonempty subsets of an alternating set have m=size. No integer theta_i=sum c_l assertion is made.

Fix hypothetical actual R4 data. S has the inherited earliest near-A^c P exit, S' is the other alternating set.
I=J_r(S),K=I union{u},Q=J_r(S'),X=S\K,Y=S'\Q, fixed consistent sorted ties. Q is weak: t_r(S')=-1. I is weak
(t_r(S)=-1) or strong(t_r(S)<=-2). Strength refers to threshold/TAIL, not the whole top. All X,Y theta are negative.
Set
  b=2r-kappa, F=2b-4d+2, A0=kappa-b, P0=kappa+b-2d,
  z0=q(I),zP=q'(K),z=q(Q),wA=beta'(K),w=beta(Q),W=wA+w,
  x0=|X|=(kappa+2d-b)/2-1, y0=|Y|=x0+1,
  sP=P0-nu-zP-Theta(K), sQ=A0-nu-z-Theta(Q), D_i=|L_i|-2-theta_i on X,Y.
D_X,D_Y,D_V mean sums of these D_i; they are NOT ENV D(S). b is the jump variable b*, not CM/DM tail size.
The inherited r interval implies b<=kappa-2d-2,A0>=2d+2; r is central and r+1<=kappa-d.
Negative-tail cost/parity gives D_i>=0 even and l(U)<=|U|+D_U; on a strong tail l(U)<=D_U.
Odd labels give even e. Also sQ is even: A0 even,nu congruent a,z congruent a+l(Q),Theta(Q) congruent l(Q).

Letter partition gives beta(X)+beta(Y)=zP-W and l(X)+l(Y)=zP+z-2W. Adding exact endpoints and tail sums,
using ID(sum_all theta=e-2nu-2d) INSIDE the computation, gives
  B0:=F-e=2W+sP+sQ+D_X+D_Y>=2,
  Lambda:=B0-2W=sP+sQ+D_X+D_Y>=0.                                                (Defect)
These are actual computed slacks, not free parameters. B0/Lambda are even; B0 is NOT R_PAR B(S).
Gamma=2A0-2z-3Lambda<=0 remains the literal R4 test. Define the NEW even scalar
  Omega:=2A0-2z-Lambda-2sQ=Gamma+2(sP+D_X+D_Y).                                   (Omega)
No Gamma>0 is assumed.

Use these accepted common bounds at their stated hypotheses (or their displayed weakenings):
  zP+sP>=z0+2b-2d+1; replace1 by2 if I strong;                                    (Order)
  a>=b+2z-3w+(eta+sQ)/2; if I weak,z0>=2a+b-3wA;                                 (Count)
  both weak: e+nu+E(pred bottoms)<=kappa-3b;
  mixed: z0+z<=(kappa-b-2d)/2-e, kappa>=3b+2d+2e.                                (Pred)
Count uses the actual near-A slack s_J=A0-nu-q(J)-Theta(J)>=0, as parent erratum1 requires. For Q it is sQ.
Weak top floor Theta>=2r-3n and n<=l justify Count; no floor for a strong TOP is assumed. Strong Order uses
u's next-run theta<=t_r(S)<=-2. The conditional cap is
  if a<=delta+1, negative empties in either alternating set<=d+ceil((a+1)/2)-1<=d+a/2. (Cap)
All other, unweakened R_PAR/R2/QQ tests remain in the literal data.

Finally
  A0-B0=kappa-3b+4d-2+e>0.                                                       (Room)
For both weak, (Pred) gives kappa-3b>=e+nu+E>=0; for mixed it gives kappa-3b>=2d+2e. Thus(Room) follows
for d>=2, and 0<=sQ<=Lambda<=B0<A0. Also B0>=2 implies b>=2d+e/2>=2d.

## 2. Positive-gain aggregate lemma, requiring Omega>0 rather than Gamma>0

Assume Omega>0. For i in Y define the INTEGER gain_i=beta({i})-D_i/2. Suppose, for contradiction, that
  2beta(Y)>sQ+D_Y.                                                               (failure-A)
Then total gain(Y)>k:=sQ/2, a nonnegative integer. The sum of positive gains is at least the total, so there
exists an inclusion-minimal subset V of positive-gain runs whose gain sum exceeds k. Put t=|V|. It has
1<=t<=k+1: otherwise any k+1 of its members, each gain>=1, would be a proper subset already exceeding k.
Each selected run satisfies beta(i)>=D_i/2+1, hence
  l(V)>=D_V/2+t, Theta(V)=l(V)-2t-D_V>=-D_V/2-t.                                  (Gain-cost)
This is a mathematical subset selection, not enumeration/computation of scientific data.

By(Room), t<=sQ/2+1<=A0/2+1=kappa+1-r. Thus U=Q union V is a proper independent subset of S', central with
d<=r<r+t<=kappa+1<=h-1, so literal(Win) applies. Its ACTUAL needed upper entry satisfies
  nu+2+Theta(U)>=A0-z-sQ-D_V/2-t+2
    >=A0-z-sQ-(Lambda-sQ)/2-(sQ/2+1)+2
    =Omega/2+1>=2.                                                               (Needed)
Here D_V<=D_Y<=Lambda-sQ. Evenness of Omega is used in the last step, not an e0 assumption.
Thus eps(U)<=1 cannot attain the needed entry. The near-A^c entry cannot either: q(U)=z+beta(V)-beta'(V)
<=z+l(V)<=z+t+D_V, with D_V<=B0,z<=A0,t<=A0/2+1, gives
  M_(r+t)-R+q(U)<=-3kappa+b-4d+2+3t+z+B0
                 <=-A0/2-8d+7-e<0.                                            (P-small)
z<=A0 is the inherited near-A type of Q, not a new hypothesis. The strict negativity follows from d>=2,A0>=2d+2.
Only ell_(r+t)-q(U) can therefore attain(Needed). Its upper window, minus Q's exact endpoint, says
  Theta(V)+2t+beta(V)-beta'(V)<=sQ,
equivalently 2beta(V)-D_V<=sQ, or gain(V)<=k. This contradicts the selection of V. Therefore(failure-A) is
impossible, proving the ONCE-paid aggregate bound
  2beta(Y)<=sQ+D_Y.                                                              (A)
No bound on the number of ALL positive Y runs, no unit labels, no sQ0 and no small F-e was assumed. []

## 3. Both remaining orientations force Omega>0 globally

### 3.1 I and Q both weak

From Count and a+eta<=kappa-3b-e, obtain
  2z<=kappa-4b-e+3w-(3eta+sQ)/2.
Write Omega=2kappa-4b+4d-2+e+2W-2z-2sQ. Substitution gives
  Omega>=kappa+4d-2+2e-w+2wA+3eta/2-3sQ/2.
But sQ<=B0-2W=2b-4d+2-e-2wA-2w, so
  Omega>=kappa-3b+10d-5+7e/2+2w+5wA+3eta/2>0.                                  (O-WW)
The final strict sign uses kappa-3b>=0,d>=2; all other displayed quantities are nonnegative. No parameter cutoff. []

### 3.2 I strong, Q weak

Put tauMix=kappa-3b-2d>=2e (NOT UMR tau_i). Since beta'(I)<=wA, z0>=a-wA. Mixed(Pred) gives
  a+z-wA<=(kappa-b-2d)/2-e=b+tauMix/2-e.
Combine this with Q's Count to get the ACTUAL slack bound
  sQ<=tauMix-2e-6z+6w+2wA-eta.                                                   (Slack)
Also, directly from definitions,
  Omega=2b+8d+2tauMix-2+e+2W-2z-2sQ.
Substitute(Slack), obtaining
  Omega>=2b+8d-2+5e+10(z-w)-2wA+2eta.
Here alpha(Q)=z-w>=wA: K,Q are disjoint run sets, so every negative letter occurrence in K is outside Q.
Consequently
  Omega>=2b+8d-2+5e+8wA+2eta>0.                                                  (O-SW)
Use b>=2d,d>=2; arbitrary even e is retained. No bound on kappa, prime class, Gamma or budget magnitude. []

## 4. Aggregate(A) contradicts each orientation, with exact cap domain

This section re-states the conditional implication from the UPAR4 proof. We do NOT broaden a theorem merely
by deleting its Gamma>0 hypothesis: the derivation below uses(A) and the literal common data, not Gamma.

If I is strong, X is a strong TAIL. Thus beta(X)<=D_X and(A), with beta(X)+beta(Y)=zP-W, gives
  zP+sP<=W+D_X+(sQ+D_Y)/2+sP<=B0-W<=B0.
Strong(Order) instead gives zP+sP>=z0+2b-2d+2>=2b-2d+2=B0+2d+e, contradiction. []

If I is weak, both predecessors are weak. Put alpha=alpha(Q)=z-w. By(A) and l(X)<=x0+D_X,
  zP+sP<=x0+B0-W-(sQ+D_Y)/2.
Weak-I Count and Order bound the same quantity below by2a+3b-2d+1-3wA. Therefore
  2a<=x0+B0-3b+2d-1+2wA-w-(sQ+D_Y)/2.                                           (C1)
Since 2wA<=B0 and b<=kappa-2d-2, this implies
  a<=(kappa+b)/4-5d/2+1-e<=kappa/2-3d+1/2-e<delta+1.
Thus(Cap) is now legitimately applicable. Negative letters in Y number at most alpha; hence
E(Y)>=y0-alpha-beta(Y)>=y0-alpha-(sQ+D_Y)/2. Every Y empty is negative. The cap yields
  a+2alpha>=kappa-b-sQ-D_Y.
Q's Count gives 2alpha<=a-b+w-(eta+sQ)/2. Combining yields
  kappa<=2a+w-eta/2+sQ/2+D_Y.
Insert(C1), and use 2wA+D_Y/2<=B0 from Defect, to bound the right side by
  x0+2B0-3b+2d-1-eta/2
    =(kappa+b)/2-5d+2-2e-eta/2
    <=kappa-6d+1-2e-eta/2<kappa.
Contradiction. Only tail signs, not a whole-top sign, were used. Neither orientation survives(A). []

## 5. Full cover, complete outcome and required diagnostics

Fix ANY actual survivor on ENTIRE T\T4. Accepted UPAR4-R gives the COMPLETE literal corrected R4, with Q weak
and I weak or strong. Section3 gives Omega>0 in either case, Section2 gives(A), and Section4 contradicts it.
This proves candidate UPAR5-C at full unbounded scope, including arbitrary even e/nonunit labels and Gamma<=0.
No old R_PAR/R2 condition was dropped or replaced: the contradiction used a necessary SUBSET of that entire
data, while the original mixed windows/ID/reservoir/ENV/UB/Lemma20 conditions stayed in force. No numerical
feasibility, converse or inverse NF assembly is asserted. The actual-frame residual within the assigned
charge-failure target is empty under this candidate proof; there is no further unproved charge-failure step
inside that declared scope. Other terminal k and full ordered Olson remain outside the result.

For kappa<=26d-10 use accepted UPAR4-P; for larger kappa use the cover just proved and frame existence from
accepted UMR. Thus candidate UPAR5-T excludes the entire ORIGINAL T at the EXACT stated NF antecedent.
The three preview instances were checked BY HAND, not used as inputs or an upper cutoff:

| (kappa,p) | floor((p+7)/4) | (p-3)/2 | d | kappa>26d-10 | outcome |
|---|---:|---:|---:|---|---|
| (43,89) |24|43|2|43>42| excluded by UPAR5-C |
| (47,97) |26|47|2|47>42| excluded by UPAR5-C |
| (49,101) |27|49|2|49>42| excluded by UPAR5-C |
All three p are prime: none is divisible by2,3,5,7, and its square root is<11, so these checks suffice.
The table verifies actual membership in T\T4, not feasible residual tuples. No selected-cell extrapolation.

## 6. Source and process precision

Full operative parent scope and own87LF exposure acknowledgement are in part1; the full historical UPAR4
scope/departure remains in part2, not retroactively cured. cp03/O1/O2 and prior authorship were exposure only.
The positive-gain lemma and both global Omega estimates above were derived after the new acknowledgement,
not imported from the unaccepted preview or a Gamma-bound-zero observation. No priority/independence claim.

Part1 contains the complete new UPAR4 governing verdict/errata1/2. Part2 physically supplies UPAR4 primary1-190
SHA256bd4f51d42ade41ed8a87e770de22a182369df18287b05cf7118acb39f00f5091 through those corrections, plus all16
older governing mathematical MD bodies and their actual primary ranges: complete R_PAR at UPAR216-275,
literal R2 at UPAR2 194-224 and exact defect/count95-123; UPAR35-107/146-155; UMR18-28,49-56,64-68,88-118,
137-139,161-165,201-209,238-239,252-258,266-274,300-302,315-324 INCLUDING320-321; UFC23-27/200-225 and
full fixed-parameter finiteness clarification. Whole-source SHA does not imply whole older proof pasted.
Every external citation has full absolute path/whole SHA/ACTUAL LF in its source header and ordered manifest.
Accepted statements are used at their declared scopes without a claimed transitive reproof of all literature.
Both physical parts, not an excerpt-only substitute, must reach EACH family. No scientific code/computation/
enumeration/assertion/import/solver/test/Lean/native/model/network/nested-agent run was used for this proof.
All mathematics by hand; parent alone runs new reviews/verdicts. No new acceptance is claimed here.
