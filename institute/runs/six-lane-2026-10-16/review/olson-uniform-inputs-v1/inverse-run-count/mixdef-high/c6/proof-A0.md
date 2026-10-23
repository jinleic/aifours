# The integer defect-prefix lemma A0 and the count-free lifted-system theorem C0-all

Written 2026-10-17T19:30:41-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proofs, not independently reviewed.  Controls are [F] aids only.
Dependencies: c3/proof-C-r1.md Secs. 0-2 (NMH parameters, coordinates, Kill lemma, (2.2)); c6/c5-fixes/proof-Cplus-r2.md steps
(B1+),(B2+); c6/proof-C0WB.md Lemma C0W (under review).  The proof below replaces C0WB's Case A with an unconditional integer-prefix
argument, so its defect hypothesis (A*) is not used.  No finite-class result or seed computation is used in the written proof.

## 1. Setting

Let w be an NMH word with R<=2p-3 (prime p>=5), as in c3 Sec. 0.  Write g=kB>=1, kappa=g+B, B>=1, E=R-k (even), d_t=a_t-b_t,
where every rotation run is aligned, anti, or a (1,1)-pair; all reflection runs are odd.  We have
  k=p+g+B-E/2,  k>=2g+2B+3,  g+B+E/2<=p-3,  d_t<=E+1.
Consider the integer lifted system
  sum_t x_t=p,   X_Q:=sum_(t in Q)x_t>=lambda(Q) for every proper Q (singletons included).                 (L)
Set c_t=d_t-x_t, bh_t=2x_t-d_t, so x_t=c_t+bh_t; Phi(Q):=c(Q)+m(Q).  Let Z={t:bh_t<=0}, the defect set.  It is nonempty and proper:
sum bh=k-2g>0 rules out Z=[k], while Z empty would imply every integer bh_t>=1 and sum bh>=k.  The arithmetic Kill criterion is
  X_Q<lambda(Q) iff Phi(Q)>=g+1, bh(Q)<=B, X_Q+m(Q)<=p.
(Thus finding such a Q contradicts (L); no group computation is involved.)

## 2. An unconditional Case A

**Lemma A0 (first defect prefix).**  Under (L), if Phi(Z)>=g+1 there is a contradiction.  No count bound on even aligned runs,
no bound 2g<=p, and no extra seed bound on c_t are required.
Proof.  List Z in any order and let P be the first prefix with Phi(P)>=g+1, with P' the preceding prefix and t the added run.
The empty prefix has Phi=0, so P exists and is nonempty.  All quantities are integers: Phi(P')<=g (this is the essential discrete
step).  Since P' is a subset of Z, bh(P')<=0, and therefore
  X_(P')+m(P')=Phi(P')+bh(P')<=g.
Adding one run increases m by at most 1; t is a defect, so
  x_t<=floor(d_t/2)<=floor((E+1)/2)=E/2.
Consequently
  X_P+m(P)<=g+x_t+1<=g+E/2+1<=p-B-2<p.
We also have Phi(P)>=g+1 and bh(P)<=0<=B.  P is proper because P is contained in the proper set Z.  The Kill criterion gives
X_P<lambda(P), contradicting (L).  []

This argument does not try to force Phi(P)<=p.  The old deletion argument imposed that unnecessary sufficient condition; here
Phi(P) may overshoot p, while its negative bh contribution keeps X_P+m(P) below p.

## 3. Removing the count condition from the whole lifted-system contradiction

**Theorem C0-all.**  For every NMH word with R<=2p-3, the integer system (L) has no solution.  In particular an avoiding NMH word
cannot have lifts satisfying (L).
Proof.  Suppose x solves (L).  If Phi(Z)>=g+1 apply Lemma A0.  Otherwise Phi(Z)<=g; put Delta=g-Phi(Z)>=0 and use the Case B
coordinates of c3.  Its identity (2.2) is
  Delta=-f(Z)-m(Z)-n_ev/2-sur,  f_t=floor((d_t-1)/2),  sur>=0.
Since m(Z)>=1 and aligned f_t>=0, pairs f_t=-1, anti f_t=-ceil((b_t+1)/2), it implies
  n_ev/2<=-f(Z)-1<=n_pr+sum_anti ceil((b_t+1)/2)-1.
Using sum_anti b_t=B-n_pr and ceil((b+1)/2)=(b+1+[b even])/2 yields
  n_ev,al<=B+n_an-2.                                                             (3.1)
The unconditional free-run count (B1+) in C+ is
  |X_o|>=2 Delta+s0,  s0=(k-g-2B)+(n_pr-n_ev,al)/2.
We split the parameters:
 (i) B<=g.  Since n_an<=B-n_pr, (3.1) gives
       s0>=k-g-3B+1+n_pr>=1
     (indeed k>=2g+2B+3).  Hence |X_o|>=2 Delta+1, and the construction (B2+) gives a proper Q with all three Kill conditions,
     contradicting (L).
 (ii) B>=g+1 and 3g+1<=p.  Lemma C0W (c6/proof-C0WB.md) gives a proper Q with the Kill conditions from (L) directly.  It needs
      only the singleton inequalities and sum x=p, not a condition on n_ev,al.
 (iii) B>=g+1 and 3g+1>p.  The NMH parameter inequality gives 2g<=p-4 and
       E<=2p-2g-2B-6<=p-B-7,
       because 2g+B>=3g+1>p, hence 2g+B>=p+1.
       Thus E<=2(k-g-2B)-1, equivalently 2E<=2p-2B-1.  Since n_ev,al<=E and n_pr>=0, this gives s0>=1/2 and therefore
       |X_o|>=2 Delta+1 by integrality.  Again (B2+) contradicts (L).
The hypotheses in each construction are scalar NMH identities or consequences of (L).  Avoidance itself is not otherwise used:
the proper-pattern lower inequalities contradict the explicitly produced X_Q<lambda(Q).  []

**Corollary (count-free seed certificate).**  Let w be an NMH word with R<=2p-3.  If its actual configurations establish quality
seeds as in SEED-G, or seeds satisfying (QS*),(P2),(PIN) as in Lemma SCW-G*, or an actual-empty seed interval, then w has an identity
2p-subword.  No even-aligned-run count condition or defect bound (A*) is needed.
Proof.  If w avoids, an actual-empty interval is impossible; otherwise the applicable certification lemma supplies (L), including
sum x=p.  Theorem C0-all gives a contradiction.  []
This does not prove that every NMH word has such seeds.  Universal seed existence remains open for words with excess, and no RUNS,
PAR, INV, INV* or ordered-Olson conclusion is claimed.

## 4. Controls [F], not hypotheses

defect_prefix.py / out/defect_prefix.txt: 298 explicit NMH words at primes 5,7,11,13,17,23,31,43 (6 already singleton-infeasible),
10,512 integer vectors with sum p in their singleton windows.  The 10,113 vectors with Phi(Z)>=g+1 all produce first-prefix Kill
patterns, checked against independent c5 slow_lambda; 399 Case-B vectors are not claimed as A0 checks.  Every displayed prefix
bound is asserted.  Mutation target g rather than g+1 produces 7,884 failures of condition M.  Separate scalar partition check:
642,565 parameter tuples with p<=101, all covered by (i),(ii),(iii).  Peak child RSS 44,138,496 bytes; native CPU/file-size limits.
