# The integer defect-prefix lemma A0 and the count-free lifted-system theorem C0-all (conditional on Lemma C0W)

Version r1, written 2026-10-17T23:35:28-0700 in c6/ (task OlsonRunCount5, cycle 6): new immutable revision after the static reviews
institute/runs/six-lane-2026-10-16/review/olson-uniform-{codex,claude}-review-v1.note.md (r0 = target T3: Codex ACCEPT-WITH-FIXES with MINOR M1;
Claude ACCEPT-WITH-FIXES with MINOR T3-m1..m5; FATAL 0, MAJOR 0 in both).  The r0 file c6/proof-A0.md (sha256 5c4a0dda2b1d0343...0e413e)
stays unchanged.  Changes (statement status, record and wording; the proofs of Lemma A0 and of cases (i)-(iii) are unchanged):
(1) Codex M1 / Claude T3-m1: Theorem C0-all and its Corollary are stated CONDITIONAL on Lemma C0W (only case (ii) uses it); Lemma A0
stays unconditional; (2) T3-m5: the Kill criterion is stated for proper Q, with its source; (3) T3-m2: complete dependency list with
review status, including refinement C4 for case (iii) and the Corollary's imports; (PIN) is no longer listed as a hypothesis (it is
automatic in c6/proof-SEEDGstar-r1.md); (4) T3-m3: the Corollary's quantifiers (some run / every run), the meaning of 'actual-empty'
and the source of the singleton bounds (canonical lifts) are explicit; (5) T3-m4: the closing sentence no longer suggests that seed
existence is settled for words without excess.  The r1 changes are not independently re-reviewed.
Original r0 provenance: written 2026-10-17T19:30:41-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proofs (r0 reviewed
as above; the r1 changes are not re-reviewed).  Controls are [F] aids only.
Paths are relative to mixdef-high/.  Dependencies: c3/proof-C-r1.md Secs. 0-2 (NMH parameters, coordinates, Kill lemma, (2.2);
Codex ACCEPT); Lemma H with beta = 0 (../../inverse-parity/proof-PAR-K0.md Sec. 1, with its 07:39 correction; Codex ACCEPT);
c6/c5-fixes/proof-Cplus-r2.md steps (B1+), (B2+) and, in case (iii), its refinement C4 (s0>=1/2 suffices) (r1 Codex ACCEPT and
Claude ACCEPT-WITH-FIXES; the r2 C4 delta parent-verified); for case (ii) only: Lemma C0W of c6/proof-C0WB.md Sec. 1 with Lemma DF
of its Sec. 0 (r0, sha256 ac52d85f...de77, reviewed ACCEPT-WITH-FIXES by Codex and Claude with no change requested to DF or C0W;
byte-identical in the repair c6/proof-C0WB-r1.md, which the delegated parent delta check
institute/runs/six-lane-2026-10-16/review/olson-repair-delta-v1/delta-check-v2.md rated DELTA-ACCEPT-WITH-NOTES, advisory).
Until the parent accepts the status of Lemma C0W, Theorem C0-all and its Corollary are stated CONDITIONAL on Lemma C0W; Lemma A0
is unconditional.  For the Corollary only: c6/proof-SEEDG-r2.md (canonical lifts, Lemmas P0, TS, GS, NW, SL, SCW-G with the pin
step of its proof, and the actual-empty alternative of Theorem SEED-G; r1 reviewed ACCEPT-WITH-FIXES, the r2 delta rated
DELTA-ACCEPT-WITH-NOTES by the parent's delta desk) and c6/proof-SEEDGstar-r1.md (Lemmas SCW-G*, QQ, Theorem SEED-G*; r0 reviewed
ACCEPT-WITH-FIXES, the r1 repairs rated DELTA-ACCEPT-WITH-NOTES in the same delta check).  The proof below replaces C0WB's Case A with an unconditional integer-prefix
argument, so its defect hypothesis (A*) is not used.  No finite-class result or seed computation is used in the written proof.

## 1. Setting

Let w be an NMH word with R<=2p-3 (prime p>=5), as in c3 Sec. 0.  Write g=kB>=1, kappa=g+B, B>=1, E=R-k (even), d_t=a_t-b_t,
where every rotation run is aligned, anti, or a (1,1)-pair; all reflection runs are odd.  We have
  k=p+g+B-E/2,  k>=2g+2B+3,  g+B+E/2<=p-3,  d_t<=E+1.
Consider the integer lifted system
  sum_t x_t=p,   X_Q:=sum_(t in Q)x_t>=lambda(Q) for every proper Q (singletons included).                 (L)
Set c_t=d_t-x_t, bh_t=2x_t-d_t, so x_t=c_t+bh_t; Phi(Q):=c(Q)+m(Q).  Let Z={t:bh_t<=0}, the defect set.  It is nonempty and proper:
sum bh=k-2g>0 rules out Z=[k], while Z empty would imply every integer bh_t>=1 and sum bh>=k.  For a PROPER pattern Q (nonempty and
different from [k]; ../../inverse-parity/proof-PAR-K0.md Sec. 1) and integer x, the arithmetic Kill criterion (Kill lemma of
c3/proof-C-r1.md Sec. 1, from Lemma H with beta = 0, c3 Sec. 0) is
  X_Q<lambda(Q) iff (M) Phi(Q)>=g+1, (Fl) bh(Q)<=B, (P) X_Q+m(Q)<=p.
(Thus finding such a proper Q contradicts (L); no group computation is involved.  Every pattern produced below is proper.)

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

**Theorem C0-all (conditional on Lemma C0W).**  Assume Lemma C0W of c6/proof-C0WB.md in its stated NMH setting.  Then for every
NMH word with R<=2p-3, the integer system (L) has no solution.  In particular an avoiding NMH word cannot have lifts satisfying (L).
(Case (ii) below imports Lemma C0W; cases (i) and (iii) import only c3/proof-C-r1.md Secs. 0-2 and steps (B1+), (B2+) of
c6/c5-fixes/proof-Cplus-r2.md, with refinement C4 in case (iii), and do not depend on Lemma C0W.)
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
 (ii) B>=g+1 and 3g+1<=p.  Lemma C0W (c6/proof-C0WB.md r0 Sec. 1; byte-identical in r1) gives a contradiction: its construction
      of a proper P with (M), (Fl), (P) uses only the singleton inequalities, sum x=p and the NMH scalars, not a condition on
      n_ev,al; the contradiction is (L) at P.  This is the only step that uses Lemma C0W.
 (iii) B>=g+1 and 3g+1>p.  The NMH parameter inequality gives 2g<=p-4 and
       E<=2p-2g-2B-6<=p-B-7,
       because 2g+B>=3g+1>p, hence 2g+B>=p+1.
       Thus E<=2(k-g-2B)-1, equivalently 2E<=2p-2B-1.  Since n_ev,al<=E and n_pr>=0, this gives s0>=1/2 and therefore
       |X_o|>=2 Delta+1 by integrality (refinement C4 of c6/c5-fixes/proof-Cplus-r2.md).  Again (B2+) contradicts (L).
The hypotheses in each construction are scalar NMH identities or consequences of (L).  Avoidance itself is not otherwise used:
the proper-pattern lower inequalities contradict the explicitly produced X_Q<lambda(Q).  []

**Corollary (count-free seed certificate; conditional on Lemma C0W through Theorem C0-all).**  Let w be an NMH word with
R<=2p-3.  Suppose that
 (a) for SOME run t, seeds of t obtained by Lemma GS (a) from actual configurations have empty intersection; or
 (b) EVERY run has a quality seed obtained from actual configurations (as in Theorem SEED-G); or
 (c) EVERY run has a nonempty seed satisfying (QS*), and the whole seed family satisfies (P2) (Lemma SCW-G* of
     c6/proof-SEEDGstar-r1.md; (PIN) is automatic there and is not a hypothesis).
Then w has an identity 2p-subword.  No even-aligned-run count condition (C0+) and no defect bound (A*) is needed.
Proof.  Suppose w avoids and take its canonical lifts x (c6/proof-SEEDG-r2.md Sec. 0).  In case (a), x_t would lie in each of the
intersected seeds (proof of Lemma GS (a)): impossible.  (An empty (QS) or (QS*) window by itself excludes nothing.)  In cases (b)
and (c), the canonical lifts give x_t>=lambda({t}) for every run; Lemma SCW-G (resp. SCW-G*) certifies every proper pattern with
these ranges and gives sum x=X_[k]=p (the pin step); Lemma SL then gives X_Q>=lambda(Q) for every proper Q with |Q|>=2.  Hence x
solves (L), contradicting Theorem C0-all.  []
This does not prove that any NMH word has such seeds.  Quality seeds (or actual-empty intervals) are established uniformly only in
the regions of c6/proof-SEEDG-r2.md (Corollaries SA, PA; Propositions RA2, RA3) and, subject to review, for all-single-letter words
with B>=2 (c6/proof-RZwide-r1.md, c6/proof-S2wide-r1.md); later unreviewed c6 files (proof-Ewide.md, proof-S2E.md, proof-Eglobal.md
and the E=2 files) propose further explicit regions.  Seed existence is open in general, in particular for words with excess.  No
RUNS, PAR, INV, INV* or ordered-Olson conclusion is claimed.

## 4. Controls [F], not hypotheses

defect_prefix.py / out/defect_prefix.txt: 298 explicit NMH words at primes 5,7,11,13,17,23,31,43 (6 already singleton-infeasible),
10,512 integer vectors with sum p in their singleton windows.  The 10,113 vectors with Phi(Z)>=g+1 all produce first-prefix Kill
patterns, checked against independent c5 slow_lambda; 399 Case-B vectors are not claimed as A0 checks.  Every displayed prefix
bound is asserted.  Mutation target g rather than g+1 produces 7,884 failures of condition M.  Separate scalar partition check:
642,565 parameter tuples with p<=101, all covered by (i),(ii),(iii).  Peak child RSS 44,138,496 bytes; native CPU/file-size limits.
