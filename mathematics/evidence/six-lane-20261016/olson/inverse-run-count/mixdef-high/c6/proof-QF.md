# Quality seeds suffice without a separate count condition (finisher partition)

Written 2026-10-17T19:27:04-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proof, not independently reviewed.  Depends on the written
Lemmas C0W/C0B of c6/proof-C0WB.md (under hostile review), and on c6/proof-SEEDG-r2.md Lemmas SCW-G, SL, C0+ and the seed definition.
The displayed proof is uniform; the finite parameter check is an aid only.  This is not a proof of seed existence, RUNS, PAR, INV,
INV* or ordered Olson.

**Theorem QF.**  Let w be any NMH word with R<=2p-3 (p>=5 prime).  Suppose every run has a quality seed (QS), or an actually empty
intersection obtained from configurations by Lemma GS(a).  Then w has an identity 2p-subword.  No separate hypothesis on the number
of even aligned runs is necessary.
Proof.  Suppose w avoids; the actual-empty case is impossible, and Lemmas SCW-G/SL give canonical lifts x satisfying
  sum x_t=p, X_Q>=lambda(Q) for every proper Q, x_t>=a_t.
Write g=kB, kappa=g+B, E=R-k and Delta0=2p-R.  The NMH identities give
  k=p+g+B-E/2,  kappa+E/2<=p-3,  k>=2g+2B+3,  n_ev,al<=E.
There are three cases.
 (1) B<=g.  Then k>=2g+2B+3>=g+3B.  Quality seeds supply the defect bound (A*) required by Lemma C0B:
     c_t=d_t-x_t<=d_t-a_t<=(d_t+Delta0)/2-1<=(E+1+Delta0)/2-1=(2p-k-1)/2<=p-g-1,
     since k>=2g+1.  Thus Lemma C0B contradicts the lifted system.
 (2) B>=g+1 and 3g+1<=p.  Lemma C0W contradicts the lifted system.
 (3) B>=g+1 and 3g+1>p.  From g+B+E/2<=p-3 we obtain 2g<=p-4 and
     E<=2p-2g-2B-6.  Also 2g+B>=3g+1>p; as integers, 2g+B>=p+1.  Hence
       E<=2p-B-(2g+B)-6<=p-B-7.
     This implies E<=2(k-g-2B)-1: the latter inequality is equivalent to 2E<=2p-2B-1, while the displayed estimate gives
     2E<=2p-2B-14.  Therefore n_ev,al<=E<=2(k-g-2B)+n_pr-1 and 2g<=p.  The strengthened Theorem C+ count (ii+) holds, so
     Lemma C0+ contradicts the lifted system.
All cases contradict avoidance.  []

**Corollary.**  Corollaries SA and PA of c6/proof-SEEDG-r2.md exclude every NMH word in their stated parameter regions, for ALL primes
in their stated domain, with no additional even-aligned-run count condition.  Proof: those constructions establish quality seeds
or actual empty intervals, so Theorem QF applies.  []

This is a simplification of the finisher disjunction, not a claim that every NMH word has quality seeds.  For weak (QS*) seeds the
Case (1) defect bound need not follow automatically; the separate seed check in Theorem SEED-G** remains necessary there.

Control [F]: quality_finish.py / out/quality_finish.txt checks the partition for every admissible parameter class with p<=257:
24,421,492 tuples (12,275,536 in Case 1; 11,586,973 in Case 2; 558,983 in Case 3), no scalar-condition failure.  This check asserts
neither seed existence nor word exclusion independently of the written proof.
