# Uniform aligned singles/pairs quality seeds for a complementary family with excess

Written 2026-10-17T19:39:43-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proof, not independently reviewed.  Controls are [F] aids only,
not hypotheses.  No general NMH, RUNS, PAR, INV, INV* or ordered-Olson claim is made.

Dependencies: c3/proof-C-r1.md Sec. 0 (NMH identities), c6/proof-SEEDG-r2.md quality seeds and Lemma GS, the robust generic box (G)
in c6/proof-Ewide.md Sec. 3 (the eight sufficient inequalities there are written, not a computation), and the packing lemma re-proved
in c6/proof-S2wide.md Sec. 1.  The conclusion for general E uses Lemma C0B of c6/proof-C0WB.md (under review); the E=2 or4 conclusion
uses only SEED-G with C0+ case (i) and does NOT depend on C0B, A0, QF or weak QS*.

## 1. Statement and recipe

**Theorem S2-E (quality-seed existence).**  Let w be an NMH word with R<=2p-3, excess E>=2 even, g=kB>=B>=2, kappa=g+B,
Delta0=2p-R.  Put epsilon in {0,1} so kappa+E+epsilon is even.  Suppose
   Delta0>=E+3,     g-B+2Delta0>=3E+12+epsilon.                                  (S2-E)
Then actual configurations establish a quality seed at every run, or an actually empty seed interval.  In particular w has an
identity 2p-subword (for E=2,4 directly by SEED-G; for general E by the count-free C0B argument below).

Take
   m=ceil((kappa+E)/2),  y0=g+E+2,  j1=2m-y0=B-2+epsilon,
   j2=y0-m=(g-B+E+4-epsilon)/2.
The pattern will have j1 aligned singleton RUNS and j2 aligned pairs of adjacent RUNS (their lengths may be arbitrary).  It has
m=j1+j2 blocks; y0 is its base letter mass, not a claim that every chosen run has length 1.

## 2. The configurations exist and all four arcs are generic

Both j1 and j2 are nonnegative integers because g>=B>=2 and E>=2.  Delete the target t and its two neighbours.  The remaining path
has alpha>=n_al-3>=k-B-3 aligned runs in at most B+1 aligned intervals (n_al=k-B+e_an>=k-B).  Thus the aligned packing lemma realises
the requested pairs and singles whenever
   3j2+2j1=m+y0<=k-2B-4.
Here k=p+kappa-E/2=2kappa+Delta0, and k-2B-4=2g+Delta0-4.  Twice the footprint excess is
   2[(m+y0)-(k-2B-4)]=3E+12+epsilon-(g-B)-2Delta0<=0
by (S2-E).  Thus an actual Q exists at every target, no member adjacent to t.  Q has m blocks, Q+t has m+1, both proper; indeed
2m+2<=kappa+E+3<2kappa+Delta0=k.

Its mass y lies in [y0,y0+E-e_t], since the chosen aligned runs carry at most E-e_t excess letters.  Also |d_t|<=e_t+1, so
|y+d_t-y0|<=E+1.  Consequently the robust box (G) of proof-Ewide.md applies if
   2g+B+E+2<=X:=y0+2m<=2p-B-E-3,
   E+3-delta'<=Z:=y0-2m<=delta'-2B-2,       delta'=p-g-E/2=Delta0+B.
Our recipe gives
   X=2g+B+2E+2+epsilon,    Z=2-B-epsilon.
The lower-X slack is E+epsilon>=0; the upper-X slack is 2Delta0-2E-5-epsilon>=1-epsilon>=0.  The lower-Z slack is
Delta0-E-1-epsilon>=2-epsilon>=1, and the upper-Z slack is Delta0-4+epsilon>=E-1+epsilon>=1.  Thus all four arc values are generic
for every target run, including arbitrary-length anti runs and (1,1)-pairs.  Lemma GS(b) gives quality seeds or an actual empty
interval.  This proves the seed assertion uniformly.

## 3. Finishing the family

If E<=4, then n_ev,al<=E<=4 and Theorem SEED-G under condition (i) excludes avoidance directly.
For any E satisfying (S2-E), suppose w avoids; quality-seed certification gives canonical lifts satisfying (0.2), with x_t>=a_t.
Because g>=B, k>=2g+2B+3>=g+3B.  Also
   c_t=d_t-x_t<=d_t-a_t<=(d_t+Delta0)/2-1<=(2p-k-1)/2<=p-g-1.
Hence Lemma C0B (c6/proof-C0WB.md) applies: both its scalar bound and defect bound (A*) hold.  This contradicts (0.2), proving the
stated identity conclusion for general E.  []

**Example (an infinite E=2 family independent of C0B).**  For every prime p>=37, let E=2, B=10, g=p-16, kappa=p-6.  Then
Delta0=5, epsilon=1, k=2p-7 and R=2p-5.  The footprint condition becomes p>=35, so (S2-E) holds; m=(p-3)/2.  These classes are
outside both old aligned-only regions SA/PA: SA has upper bound at most Delta0+B-min(B,E+1)-2=10, but its lower bound is at least
ceil((2p-19)/3)>=19; PA requires Delta0>=B+1=11, which fails.  Every NMH word of these parameters is excluded by the direct
quality-seed + C0+ case(i) argument, for all run placements/lengths, not by a finite census.

## 4. Controls [F], not hypotheses

seedS2E.py / out/seedS2E.txt: every admissible tuple with prime p<=101, 102,279 parameter classes; all target weights and the robust
mass hulls (36,501,385 types, 146,005,540 arc equalities), availability, genericity, quality bounds and no wrap pass.  Constructive
smoke: 40 sampled/pinned classes, 120 explicit words, 13,542 actual configurations, with correct block counts/isolation and
independent c5 slow_lambda arcs.  No empty actual interval occurred in this sample.  Peak child RSS 40,927,232 bytes; native CPU and
file-size limits.  The pair-separator mutation controls are separate: replayLB.py on its exhaustive paths rejected 132 mutated
constructions; these are not attributed to seedS2E.py.  No sharpness or maximality of (S2-E) is claimed.
