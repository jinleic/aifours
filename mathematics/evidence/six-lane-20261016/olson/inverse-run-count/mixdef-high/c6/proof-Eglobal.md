# Uniform low-excess quality seeds in every NMH parameter regime

Written 2026-10-17T19:43:48-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proof, not independently reviewed.  Controls are [F] aids only;
no finite computation is a hypothesis.  This proves the explicit low-excess region below, not general NMH, RUNS, PAR, INV, INV*
or ordered Olson.

Dependencies for seed existence: c3/proof-C-r1.md NMH identities; c6/proof-SEEDG-r2.md Corollary SA and Lemma GS; c6/proof-Ewide.md
(the mixed-single recipe and its robust generic box (G)); the aligned packing lemma re-proved in c6/proof-S2wide.md.  The final
identity conclusion in the g>=B branch uses Lemma C0B of c6/proof-C0WB.md, under review; the other branches need only Theorem
SEED-G with C+'s (ii+).  Neither weak QS*, the profile lemma nor a finite-class exclusion is used.

## 1. Statement

**Theorem E-global.**  Let w be any NMH word with R<=2p-3, g=kB>=1, B>=1, positive even excess E=R-k>=2, and Delta0=2p-R.  Suppose
   Delta0 >= 3E/2 + 6.                                                        (EG)
Then actual configurations establish quality seeds at every run, or an actual empty seed interval, for every run structure and
placement.  Consequently w has an identity 2p-subword (the general g>=B conclusion uses C0B as noted above).
The condition is equivalently 5R-3k<=4p-12.  Universal seed existence when (EG) fails is not proved.

Write kappa=g+B, k=p+g+B-E/2, p=kappa+E/2+Delta0, and use three cases.

## 2. Case g>=B (aligned mixed packing; includes B=1)

Set m=ceil((kappa+E)/2), epsilon=2m-kappa-E in {0,1}, y0=g+E+1.  Pack
   j1=2m-y0=B-1+epsilon>=0,  j2=y0-m=(g-B+E+2-epsilon)/2>=0
aligned single runs and adjacent aligned pairs of runs, respectively.  This differs by one unit from the recipe in proof-S2E.md;
the point is to include B=1.  As in the packing proof there, these configurations exist at every target if
   m+y0<=k-2B-4,
which is equivalent to g-B+2Delta0>=3E+10+epsilon.  This follows from g>=B and 2Delta0>=3E+12.  Properness follows from
2m+2<=kappa+E+3<2kappa+Delta0=k.  The selected runs carry at most E-e_t excess letters, so their actual mass y lies in
[y0,y0+E-e_t], and |y+d_t-y0|<=E+1.

The robust generic box (G) of E-wide is
  2g+B+E+2<=X:=y0+2m<=2p-B-E-3,
  E+3-delta'<=Z:=y0-2m<=delta'-2B-2,     delta'=p-g-E/2=Delta0+B.
Here X=2g+B+2E+1+epsilon and Z=1-B-epsilon.  The four slacks are, in order,
  E-1+epsilon,  2Delta0-2E-4-epsilon,  Delta0-E-2-epsilon,  Delta0-3+epsilon,
all nonnegative under (EG) and E>=2.  Therefore Q and Q+t have all four generic arc values, for any target run weight d_t.
Lemma GS(b) gives quality seeds or an actual empty interval.

## 3. Case B>g with B-g>=2E+3 (mixed single runs)

Since Delta0>=3E/2+6>=E+5, this is the family of Theorem E-wide.  Its actual RZ configurations establish quality seeds (or actual
empty intervals) for every run, without a profile or computation.  That theorem also verifies C+'s (ii+), so this branch already
has its identity conclusion independently of C0B.

## 4. Remaining case 1<=B-g<=2E+2 (the SA region)

Let b=min(B,E+1), M=max(2,b), and denote Delta0 by D in this section.  Corollary SA requires an integer m between
  L0=ceil((2g+B+M)/3),  L1=B+2-D,  L2=1
and
  U0=floor((2p-B-E-3)/3),  U1=D+B-b-2,  U2=ceil((k-B-3)/2).
These are the SA formulas (L0 includes the +2 through M=max(2,b), exactly as in proof-SEEDG-r2.md).  We prove such an m exists by
showing each lower bound is <= every upper bound.  Put N=2g+B+M (so L0=ceil(N/3)).  The following slightly stronger sufficient
inequalities make the ceiling/floor comparisons immediate (ceil(N/3)<=(N+2)/3 and ceil(T/2)>=T/2):

| comparison | sufficient inequality |
|---|---|
| L0<=U0 | M+5<=2D |
| L0<=U1 | 2(g-B)+M+3b+8<=3D |
| L0<=U2 | 2M+9<=2g+B+3D |
| L1<=U0 | 2(B-g)+9<=5D |
| L1<=U1 | b+4<=2D |
| L1<=U2 | B-2g+7<=3D |

For the first three rows substitute p=g+B+E/2+D and k-B=2g+B+D; clearing denominators gives precisely the displayed sufficient
conditions.  All six hold from
  M<=E+1, b<=E+1, g-B<=-1, B-g<=2E+2, g>=1, B>=2, D>=3E/2+6.
Indeed the left sides of the six rows are bounded by E+6, 4E+10, 2E+11, 4E+13, E+5, 2E+8 respectively; their right sides are
at least 3E+12, (9E/2)+18, 2g+B+(9E/2)+18, (15E/2)+30, 3E+12, (9E/2)+18.  Each left bound is no larger for E>=2.  Also every Uj>=1:
U1>=D-2>=1, and the other two are positive from g>=1,B>=2,D>=9.  Hence m=max(L0,L1,1) satisfies SA.  Its actual isolated-aligned-run
configurations establish quality seeds (or actual empty intervals).

For completeness on the small ceiling margin: the formulas L0 and U0 above use no extra +2 in L0 beyond M; this is why the first
three sufficient inequalities have constants 5,8,9 rather than the more conservative 7,10,13.  Either choice works under (EG).

## 5. Finishing and scope

In Cases 3 and 4, B>g gives 2g<=p, and p-B=g+E/2+Delta0>=g+2E+6 implies E<=p-B-1, hence E<=2(k-g-2B)-1.  Thus C+'s (ii+) holds and
Theorem SEED-G finishes directly.  In Case 2 (g>=B), quality-seed certification gives (0.2); k>=2g+2B+3>=g+3B and quality bounds
imply c_t<=p-g-1 on every defect, so Lemma C0B finishes.  Actual empty intervals immediately contradict avoidance in every case.
This proves E-global.  []

Example: for every prime p>=13 and every admissible positive decomposition g+B=p-10, let E=2.  Then k=2p-11,R=2p-9,Delta0=9 and
(EG) holds; every NMH word in these parameters is excluded, for all its run structures/placements.  The special E-wide/S2-E families
cover some nearer-to-2p cases as well; no maximality of (EG) is claimed.
Together with the separate all-single-letter theorem, this narrows the still-unproved seed-existence part to excess words outside
(EG) (and outside the other explicit regions).  It does not settle that residual or any full inverse/RUNS theorem.

## 6. Controls [F], not hypotheses

seedEglobal.py / out/seedEglobal.txt checks every admissible tuple with prime p<=101 under (EG): 160,834 classes (81,844 aligned
mixed-packing; 34,205 mixed single runs; 44,785 SA).  All 28,079,902 target mass types pass availability, four generic arc values,
quality bounds and no wrap.  Constructive smoke: 37 sampled/pinned classes, 111 actual words, 12,426 target configurations,
independent c5 slow_lambda four-arc checks, all pass; no actual empty interval occurred.  The SA-only ablation leaves 23,191
parameter tuples without an SA recipe, so the three-way split does genuine construction work.  RZ/RZ2 structural mutation controls
are separately recorded in out/replayLB.txt, not attributed to this script.  Peak child RSS 58,359,808 bytes; native CPU/file-size
limits used.
