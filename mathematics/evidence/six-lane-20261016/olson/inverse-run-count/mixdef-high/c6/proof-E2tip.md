# Two units of excess at R=2p-3: ordinary mixed-single seeds in the B-dominant regime

Written 2026-10-17T19:50:04-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proof, not independently reviewed.  Controls are [F] aids only.
This is a near-maximal-rotation excess family, not general NMH/RUNS/PAR/INV/INV* or ordered Olson.

Imports: the NMH identities and proper-pattern arcs of c3/proof-C-r1.md; c6/proof-SEEDG-r2.md Lemma GS, (QS), Theorem SEED-G and
C0+ case(i).  No weak QS*, profile census or new count-free finisher is used.

## 1. Statement and ordinary-run counts

**Theorem E2-tip.**  Let w be any NMH word with E=R-k=2 and Delta0=2p-R=3.  Write g=kB.  If
  g>=3,   B>=g+3,
then w has an identity 2p-subword, for every rotation-run structure, exceptional-run placement and reflection values.
Here kappa=p-4, k=2p-5, R=2p-3, and p>=13 follows from kappa=g+B>=9.

Call an aligned (resp. anti) rotation run ordinary if it is a single letter rho_1 (resp. rho_(-1)).  Put e_al=sum_aligned(a_t-1),
e_an=sum_anti(b_t-1), n_pr=number of pairs; then E=e_al+e_an+n_pr=2.  If n1_al,n1_an count ordinary runs, each nonordinary pure run
consumes at least one excess letter, so
  n1_al>=n_al-e_al=k-B-2+2e_an+n_pr>=p+g-3,
  n1_an>=n_an-e_an=B-n_pr-2e_an>=B-4.                                             (1.1)
These bounds include both length-3 possibilities, two length-2 runs, pairs, and their combinations; no exceptional run type is
omitted.

## 2. A fixed type realised with ordinary runs at every target

Set m=(p-3)/2, r=m-g=(B-g+1)/2>=2.  Choose c=2 if r is even and c=3 otherwise.  Define y=g+c, i=(m-y)/2, j=(m+y)/2.  Since c is the
least positive integer of the same parity as r among {2,3}, i,j are nonnegative integers.

For every target run t, delete t and its neighbours.  The remaining path has alpha>=p+g-6 ordinary aligned runs and beta>=B-7
ordinary anti runs.  We have 2m=p-3<=alpha because g>=3.  If i=0 no anti run is required.  If i>0, then m-g-c=2i>=2, so
m>=g+c+2 and m+c>=g+2c+2>=9.  Since B=2m-g-1,
  (B-7)-2i=m+c-8>=1.
Thus 2i<=beta.  Choose i pairwise non-adjacent ordinary anti runs by taking every other member of each ordinary anti interval.
Removing their neighbours deletes at most 2i ordinary aligned runs; at least alpha-2i>=2j remain.  Every other member of the remaining
ordinary aligned intervals supplies j pairwise non-adjacent aligned singles.  All chosen runs are ordinary and outside t's
neighbourhood, so their union Q has EXACT mass y=j-i and m blocks, and Q+t has mass y+d_t and m+1 blocks.  It is proper because the
neighbours of t are omitted; 2m+2=p-1<k.  Target t itself need not be ordinary.

## 3. The four arcs are generic for every target weight

All possible target weights satisfy -3<=d_t<=3, since E=2 (pairs have d_t=0).  Put s=(p-1)/2, so m=s-1 and kappa=2s-3.  The proper
arcs are
  lam(v,b)=min(p-b+1,v+b-g,floor((v+B)/2)+1),
  U(v,b)=max(b-1,v+B-1-b,ceil((p-g-1+v)/2)-1).

For Q, v=g+c,b=s-1:
 - its floor cap is s+floor((c-3)/2)+1, equal to s for c=2 and s+1 for c=3;
 - the other lam terms are s+3 and s+c-1, both above that cap;
 - its ceiling U cap is C(c):=s+ceil(c/2)-1 (s or s+1), and the other U terms are s-2 and s+c-3, both below it.
Thus Q is generic.

For Q+t let v0=c+d_t in [-1,6].  Its floor cap is s+floor((v0-3)/2)+1, at most s+2.  Its other lam terms are s+2 and s+v0.  Since
v0>=-1, floor((v0-3)/2)+1<=(v0-1)/2<=v0, so both dominate the cap.  Its ceiling U cap is C(v0)=s+ceil(v0/2)-1; the other terms are
s-1 and s+v0-4.  The former is below C(v0) because v0>=-1, and the latter is below it because v0<=6 implies v0-3<=v0/2<=ceil(v0/2).
Hence Q+t is also generic for every target type, including the nonordinary runs.

Lemma GS(b) supplies quality seeds for every target (or an actual empty interval from these configurations).  Finally
n_ev,al<=E=2<=4; Theorem SEED-G with C0+ case(i) excludes avoidance, proving E2-tip.  []

Example (infinite family): g=3, B=p-7, every prime p>=13, gives k=2p-5,R=2p-3,E=2, all run structures and placements.  These words
lie at the smallest permitted Delta0=3, outside the low-excess/large-Delta0 theorem E-global; no finite prime cutoff enters this
result.  Other g/B regimes and other positive excess values remain open unless covered by earlier explicit regions.

## 4. Controls [F], not hypotheses

seedE2tip.py / out/seedE2tip.txt: every admissible class with prime p<=401 (6,723 classes), every target weight -3..3 (47,061 arc/seed
checks), availability, four generic values, quality and no wrap pass.  Constructive smoke: 60 sampled/pinned classes, 180 actual
words, 23,268 target configurations; correct block counts, exact ordinary-run mass and independent c5 slow_lambda arcs all pass.
Mutation allowing nonordinary pure runs into this fixed-mass construction changes the required mass in 5,076 configurations,
rejecting the type assertion.  This control does not establish a group counterexample.  Peak child RSS 32,096,256 bytes; native
CPU/file-size limits.
