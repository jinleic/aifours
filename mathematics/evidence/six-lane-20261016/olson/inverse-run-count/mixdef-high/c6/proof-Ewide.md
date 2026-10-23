# Uniform mixed-single quality seeds for a large-B family with excess

Written 2026-10-17T19:35:51-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proof, not independently reviewed.  All controls are [F] aids only;
no finite computation is a hypothesis.  This settles the explicit family below, not general NMH, RUNS, PAR, INV, INV* or ordered Olson.

Imports: the NMH parameter identities and proper-pattern arcs of c3/proof-C-r1.md Sec. 0; the quality-seed Lemmas GS/NW and Theorem
SEED-G of c6/proof-SEEDG-r2.md; Theorem C+'s count condition (ii+) as stated there.  The mixed-single construction is re-proved in the
needed generality.  Neither weak SEED-G*, the profile lemma, C0W, nor Theorem C0-all is used.

## 1. Statement and recipe

**Theorem E-wide.**  Let w be an NMH word with R<=2p-3, excess E=R-k>=2 (even), g=kB>=1, kappa=g+B, Delta0=2p-R.  Assume
   B>=g+2E+3,      Delta0>=E+5.                                                  (E-wide)
Then w has an identity 2p-subword, for every placement and length distribution of its aligned runs, anti runs and (1,1)-pairs.

Put m=ceil(kappa/2), choose c=2 if m-g-E is even and c=3 otherwise, and set
   y0=g+E+c,   i=(m-y0)/2,   j=(m+y0)/2.
These are a fixed recipe for the parameter class, independent of the target run t.  The chosen pattern will contain i anti runs
and j aligned runs, all isolated from each other and from t.  Their lengths may vary: y0 is a reference mass, not their claimed
actual mass.

## 2. Realiability and the mass bounds

**Lemma E1.**  For every target t the stated mixed-single pattern Q exists, has m blocks, and Q+t is proper with m+1 blocks.  Its
actual mass y satisfies |y-y0|<=E-e_t and |y+d_t-y0|<=E+1, where e_t=r_t-1.
Proof.  Let e_an=sum_anti(b_u-1), e_al=sum_aligned(a_u-1), n_pr the number of pairs.  Then
 E=e_al+e_an+n_pr,  n_an=B-e_an-n_pr>=B-E,  n_al=k-B+e_an>=k-B.
Because B>=g+2E+3, m-g-E>=2.  The chosen c is the least integer in {2,3} of the same parity as m-g-E, so i,j are nonnegative integers.
Here kappa>=9, hence m<=kappa-2, and
   2i=m-g-E-c<=B-E-3.
Also 2m<=kappa+1<=p-E/2-Delta0+1<=p+g-E/2-3=k-B-3, using Delta0+g>=4.  Delete t and its neighbours: at least n_an-3>=B-E-3 anti
runs and n_al-3>=k-B-3 aligned runs remain.  Select i pairwise non-adjacent anti runs by taking every other run in their anti
intervals.  Their neighbours remove at most 2i aligned runs; at least k-B-3-2i>=2j aligned runs remain, from which every other run in
each interval supplies j pairwise non-adjacent aligned runs.  Thus Q has m isolated members, none adjacent to t.  Its two excluded
neighbours show Q+t is proper and adding t adds one block (also 2m+2<=kappa+3<p<k).
The chosen runs carry at most E-e_t excess letters; their base signed mass is j-i=y0, so |y-y0|<=E-e_t.  For every run type,
|d_t|<=e_t+1 (a pair has e_t=1,d_t=0), hence |y+d_t-y0|<=E+1.  []

## 3. Robust genericity for all target run weights

Write delta'=2p-A=p-g-E/2=Delta0+B and beta'=B-E/2.  For a proper pattern of mass v and b blocks,
 lam(v,b)=min(p-b+1,v+b-g,floor((v+B)/2)+1),
 U(v,b)=max(b-1,v+beta'-b,ceil((delta'+v)/2)-1).
Put X=y0+2m and Z=y0-2m.  The following four inequalities suffice to make Q and Q+t generic for every actual y,d_t allowed by Lemma E1:
   2g+B+E+2 <= X <= 2p-B-E-3,
   E+3-delta' <= Z <= delta'-2B-2.                                               (G)
To verify this assertion directly, use floor(v/2)<=v/2 and ceil(v/2)>=v/2.  For the two lambda values, their first and middle terms
must be at least the floor term; for the two U values, their first and middle terms must be at most the ceiling term.  The eight
sufficient conditions, after inserting y in [y0-E,y0+E] and y+d_t in [y0-E-1,y0+E+1], are:

| value | first term comparison | middle term comparison |
|---|---|---|
| lambda(Q) | X<=2p-B-E | X>=2g+B+E+2 |
| lambda(Q+t) | X<=2p-B-E-3 | X>=2g+B+E+1 |
| U(Q) | Z>=E-delta' | Z<=delta'-2B-2 |
| U(Q+t) | Z>=E+3-delta' | Z<=delta'-2B-1 |

For example U(Q+t)'s first term m is at most the ceiling term whenever 2m+2<=delta'+y+d_t; its worst case is y+d_t=y0-E-1, giving the
lower bound on Z in (G).  Its middle term y+d_t+beta'-(m+1) is bounded whenever y+d_t-2m<=delta'-2beta', whose worst case gives the
upper bound Z<=delta'-2B-1.  The other six comparisons follow by the same displayed min/max formulas.  Conditions (G) imply the table.

Now let epsilon=2m-kappa in {0,1}.  Our recipe gives
   X=2g+B+E+c+epsilon,    Z=E+c-B-epsilon.
The lower bound on X follows from c>=2.  The upper bound has slack
   (2p-B-E-3)-X=2Delta0-E-c-epsilon-3>=E+3>=0.
The lower bound on Z has slack Delta0+c-epsilon-3>=E+3, and the upper bound has slack
   (delta'-2B-2)-Z=Delta0-E-c+epsilon-2>=0.
Thus (G) holds uniformly.  All four arcs are generic, so Lemma GS(b) supplies quality seeds for every run (or an actual empty
configuration interval), without depending on the run's length or sign.

## 4. Finishing and an infinite subfamily

The parameters themselves imply C+'s (ii+): 2g<=p follows from B>=g+2E+3, and
   p-B=g+E/2+Delta0>=g+3E/2+5,  hence E<=p-B-1.
The latter implies E<=2(k-g-2B)-1, since k=p+g+B-E/2.  Also n_ev,al<=E and n_pr>=0.  Thus condition (ii+) holds for every word of the
class.  Applying Theorem SEED-G to the actual quality seeds established above contradicts avoidance, proving E-wide.  []

**Example (infinite family).**  For every prime p>=17, take E=2, g=1, B=p-9, kappa=p-8.  Then k=2p-9, R=2p-7, Delta0=7, and (E-wide)
holds.  This excludes every NMH word with these parameters, all run structures included.  For p>=29 these classes are outside both
old SA and PA regions: SA has lower bound at least B+2-Delta0=p-14 but upper bound at most floor((p+4)/3), smaller for p>23;
PA requires Delta0>=B+1=p-8, which fails for p>=17.  This example shows the mixed-run construction covers an infinite excess family
not supplied by those two aligned-only regions.

## 5. Controls [F], not hypotheses

seedEwide.py / out/seedEwide.txt: all 41,852 admissible parameter tuples with prime p<=101, all target weights and excess-coupled
mass values (6,305,452 types, 25,221,808 generic arcs) pass availability, all four arc equalities, quality bounds and no wrap.
Constructive smoke: 41 sampled/pinned classes, 123 explicit words, 14,202 target configurations; actual subsets have the required
mass bounds and block counts, and independent c5 slow_lambda verifies the generic arcs.  No empty interval occurred in this sample.
Boundary relaxation control Delta0=E+4: 1,902 tested tuples also remained generic; this is NOT a sensitivity control and no
sharpness of the conservative Delta0>=E+5 hypothesis is claimed.  Separate neighbour-removal mutation controls for the RZ
construction are in out/replayLB.txt (3,572 rejections); they are not attributed to seedEwide.py.  Peak child RSS 35,815,424 bytes;
native CPU/file-size limits used.
