# E=2 and R=2p-3 in the kB-dominant regime: ordinary aligned pairs and singles

Written 2026-10-17T19:52:48-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proof, not independently reviewed.  Controls are [F] aids only.
No general NMH, RUNS, PAR, INV, INV* or ordered-Olson claim is made.  This uses only the quality SEED-G chain with C0+ case(i), not
weak QS*, profile checks, or the new count-free finishers.

**Theorem E2-pair-tip.**  Let w be an NMH word with E=2 and Delta0=3.  Write g=kB, so kappa=p-4,k=2p-5,R=2p-3.  If B>=1 and
  g-B>=15,
then w has an identity 2p-subword, all run structures and placements included.

Proof.  As proved in c6/proof-E2tip.md Sec. 1, the number n1 of ordinary aligned singleton runs is at least p+g-3.  Delete the target
t and its two neighbours; there are alpha>=n1-3 ordinary aligned positions in at most r<=k-n1+1 ordinary aligned intervals (all
other runs, including nonordinary aligned runs, separate them).  Therefore
  alpha-r>=2n1-k-4>=2g-5.
The aligned packing lemma (c6/proof-S2wide.md Sec. 1, applied to ORDINARY aligned intervals) supplies j2 separated pairs and j1
singletons whenever 3j2+2j1<=alpha-r.

Take m=(p-3)/2,y=g+2 and
  j1=B-1,   j2=(g-B+3)/2.
These are nonnegative integers: p=g+B+4 odd makes g-B odd.  They satisfy j1+j2=m, j1+2j2=y, and
  3j2+2j1=m+y=(3g+B+5)/2<=2g-5
exactly when g-B>=15.  Thus an actual Q of mass y and m blocks exists at every target, with no run adjacent to t.  Q+t has m+1
blocks and mass y+d_t; both are proper because the neighbours of t remain omitted (2m+2=p-1<k).

Every target weight is in [-3,3], even though Q uses only ordinary aligned runs.  The genericity calculation in proof-E2tip.md
Sec. 3 applies with c=2, m=(p-3)/2,y=g+c.  That calculation uses only kappa=p-4 and c+d_t in [-1,6], not the B-dominance hypothesis
used for that file's separate construction.  Explicitly put s=(p-1)/2.  For Q the floor lambda cap is s and the ceiling U cap is s;
its other lambda terms s+3,s+1 dominate s, and its other U terms s-2,s-1 are smaller.  For Q+t put v=2+d_t in [-1,5].  Its floor cap
is s+floor((v-3)/2)+1, at most s+2 and at most s+v; its other lambda terms are s+2,s+v.  Its ceiling cap is s+ceil(v/2)-1, at least
s-1 and at least s+v-4; its other U terms are s-1,s+v-4.  Thus all four arcs are generic for every target.

Lemma GS(b) of c6/proof-SEEDG-r2.md supplies a quality seed or an actually empty interval.  Since n_ev,al<=E=2<=4, Theorem SEED-G
with C0+ case(i) excludes avoidance.  []

Example: B=1,g=p-5 for every prime p>=23 gives k=2p-5,R=2p-3,E=2.  This is a positive-excess result, not the single-letter family
W(p,g).  More generally, for E=2,Delta0=3, this theorem and E2-tip cover both separated g/B regimes; the near-balanced strip and
g=1,2 at arbitrary p are not covered here.

Controls [F], not hypotheses: seedE2pairtip.py / out/seedE2pairtip.txt checks all 6,431 admissible classes with prime p<=401 and all
seven target weights (45,017 arc/seed types), availability, genericity, quality and no wrap, without failure.  Constructive smoke:
60 sampled/pinned classes, 180 actual words, 24,708 target configurations, exact ordinary-run masses/block counts and independent
c5 slow_lambda arcs all pass.  Permitting nonordinary aligned runs into the fixed-mass construction changes the mass in 5,428
mutated configurations, rejecting its type assertion.  Peak child RSS 32,342,016 bytes; native CPU/file-size limits used.
