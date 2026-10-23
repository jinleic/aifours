# Small g at E=2,R=2p-3: a uniform p-residue seed certificate; the whole E2/Delta3 face for p>=31

Written 2026-10-17T20:02:36-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proof with an explicit constant table, not independently reviewed.
Controls are [F] aids only, not a finite-prime extrapolation.  No full NMH/RUNS/PAR/INV/INV* or ordered-Olson claim.

Imports: NMH identities and arcs (c3/proof-C-r1.md); the ordinary-run counts of proof-E2tip.md and the target-conditional increment
f_d of proof-E2balanced.md Sec. 1 (both re-used only as written elementary counting lemmas); Lemma GS(a) and the quality SEED-G
chain in c6/proof-SEEDG-r2.md, C0+ case(i).  The small-g theorem itself needs NO weak SEED-G*, profiles or new count-free finishers.
The final whole-face corollary uses E2-balanced (which depends on SEED-G* under review).

## 1. Statement and configurations

**Theorem E2-smallg.**  Let w be an NMH word with E=2,Delta0=3 and g=kB in {1,2}, prime p>=31.  Then w has an identity 2p-subword,
all run structures and placements included.

Here kappa=p-4,k=2p-5,R=2p-3,B=p-4-g.  At a target of weight d in [-3,3], there are at least p+g-3+f_d ordinary aligned runs,
f_d=(4,2,0,1,0,0,1) indexed by d=-3..3, and at least B-4 ordinary anti runs.  The derivation of f_d is given in E2-balanced Sec. 1:
anti excess contributes twice, pairs once, and an aligned length-3 target saves one nonordinary aligned run; it is not an assumed
word profile.

All configurations below use i ordinary anti and j ordinary aligned singleton runs, pairwise non-adjacent and outside the target's
neighbourhood.  For a fixed constant pair (t0,y), put
  m=(p-3)/2+t0,  i=(m-y)/2,  j=(m+y)/2.
The table uses -2<=t0<=0 and 0<=y<=5, with m-y even.  Thus i,j>=0 for p>=31.  After the target's triple is removed, ordinary aligned
availability is at least p+g-6+f_d; 2m fits it exactly when 2t0<=g-3+f_d, an inequality satisfied by every table entry.  Ordinary anti
availability is at least B-7=p-g-11, while 2i=m-y<=(p-3)/2<=p-g-11 for p>=2g+19, in particular p>=31.  Select i ordinary anti runs
first, remove their neighbours (at most 2i ordinary aligned runs), then select j ordinary aligned runs.  This realises exact type
(y,m) at every target, with no adjacency to it.  Q+t has type (y+d,m+1) and is proper; 2m+2<=p-1<k.

## 2. Constant p-residue formulas and seed table

Write p=4q+rho, rho in {1,3}, a=(rho-3)/2, so m=2q+a+t0.  For a type (y,m) define
 L=min(rho-a-t0+1, a+t0+y-g, floor((y+rho-4-g)/2)+1),
 U=max(a+t0-1, y+rho-5-g-a-t0, ceil((rho-g-1+y)/2)-1),
 L'=min(rho-a-t0, a+t0+y+d+1-g, floor((y+d+rho-4-g)/2)+1),
 U'=max(a+t0, y+d+rho-6-g-a-t0, ceil((rho-g-1+y+d)/2)-1).
These are lambda(Q)-2q,U(Q)-2q,lambda(Q+t)-2q,U(Q+t)-2q.  The actual two-pattern interval before canonical clipping is [L'-U,U'-L];
q cancels.  The table lists two configurations (t0,y), both raw intervals, and their intersection AFTER clipping the lower end
with lambda({t})=d+1-g.  No B or p remains in these constant min/max evaluations.

| g | rho=p mod4 | d | first (t0,y):raw seed | second (t0,y):raw seed | clipped intersection |
|---|---:|---:|---|---|---|
| 1 | 1 | -3 | (0,3):[-1,-1] | (-1,4):[-2,-2] | [-1,-2] |
| 1 | 1 | -2 | (0,1):[-1,0] | (0,3):[-1,-1] | [-1,-1] |
| 1 | 1 | -1 | (-1,2):[-1,0] | (-1,4):[-1,-1] | [-1,-1] |
| 1 | 1 | 0 | (-1,2):[0,1] | (-1,4):[0,0] | [0,0] |
| 1 | 1 | 1 | (-1,0):[0,2] | (-1,4):[0,0] | [1,0] |
| 1 | 1 | 2 | (-1,0):[1,3] | (-1,4):[1,1] | [2,1] |
| 1 | 1 | 3 | (-2,1):[2,4] | (-1,2):[1,2] | [3,2] |
| 1 | 3 | -3 | (0,2):[-2,-1] | (0,4):[-2,-2] | [-2,-2] |
| 1 | 3 | -2 | (0,2):[-1,-1] | (0,2):[-1,-1] | [-1,-1] |
| 1 | 3 | -1 | (-1,3):[0,0] | (-1,3):[0,0] | [0,0] |
| 1 | 3 | 0 | (-1,1):[0,1] | (-1,3):[0,0] | [0,0] |
| 1 | 3 | 1 | (-1,1):[1,2] | (-1,3):[1,1] | [1,1] |
| 1 | 3 | 2 | (-1,1):[1,2] | (-1,3):[1,1] | [2,1] |
| 1 | 3 | 3 | (-1,1):[2,3] | (-1,3):[2,2] | [3,2] |
| 2 | 1 | -3 | (0,3):[-2,-1] | (0,5):[-2,-2] | [-2,-2] |
| 2 | 1 | -2 | (0,3):[-1,-1] | (0,3):[-1,-1] | [-1,-1] |
| 2 | 1 | -1 | (-1,4):[0,0] | (-1,4):[0,0] | [0,0] |
| 2 | 1 | 0 | (0,1):[0,1] | (0,3):[0,0] | [0,0] |
| 2 | 1 | 1 | (-1,2):[1,2] | (-1,4):[1,1] | [1,1] |
| 2 | 1 | 2 | (-1,0):[1,3] | (-1,4):[1,1] | [1,1] |
| 2 | 1 | 3 | (-1,0):[2,4] | (0,3):[1,1] | [2,1] |
| 2 | 3 | -3 | (0,4):[-1,-1] | (-1,5):[-2,-2] | [-1,-2] |
| 2 | 3 | -2 | (0,2):[-1,0] | (0,4):[-1,-1] | [-1,-1] |
| 2 | 3 | -1 | (-1,3):[-1,0] | (-1,5):[-1,-1] | [-1,-1] |
| 2 | 3 | 0 | (0,0):[0,2] | (0,2):[0,0] | [0,0] |
| 2 | 3 | 1 | (-1,1):[0,2] | (-1,5):[0,0] | [0,0] |
| 2 | 3 | 2 | (-1,1):[1,3] | (-1,5):[1,1] | [1,1] |
| 2 | 3 | 3 | (0,0):[2,3] | (0,2):[2,2] | [2,2] |

Each row is a finite integer identity in g,rho,d,t0,y, not a statement inferred from finitely many primes.  Its configurations also
have y congruent to a+t0 modulo 2 and 2t0<=g-3+f_d as required in Sec. 1.  Every displayed nonempty final interval satisfies (QS)
for Delta0=3; every displayed empty interval is from two actually realised configurations and the canonical constraint.

## 3. No wrap and canonical clipping are valid uniformly

For p>=31,B=p-4-g>=25, the singleton lower bound is exactly lambda({t})=d+1-g; the other lambda terms p and floor((d+B)/2)+1 are
larger.  The upper bound is
 U({t})=max(0,p-g-6+d,ceil((p-g-1+d)/2)-1).
Its middle term is at least 20, larger than every raw seed upper end in the table, so the canonical upper clipping does not change
the listed final intersections.
For each raw interval [sl,sh], the table has sl>=max(-8,d-g-5), sh<=8.  Thus lambda({t})-sh>=-12>-p.  To check U({t})-sl<p,
consider its three terms: 0-sl<=8<p; (p-g-6+d)-sl<=p-1 by sl>=d-g-5; and the ceiling term is at most (p-1)/2, so after subtracting sl
it is at most (p-1)/2+8<p.  Hence Lemma GS(a) gives both actual seed intervals without wrap.  Their canonically clipped intersection
is exactly the final column, a quality seed or an actual-empty set.

As n_ev,al<=E=2, Theorem SEED-G with original C0+ case(i) now contradicts avoidance.  This proves E2-smallg.  []

## 4. The whole E=2,Delta0=3 face for p>=31

**Corollary.**  Every NMH word with E=2 and R=2p-3 (equivalently k=2p-5), prime p>=31, has an identity 2p-subword.
Proof.  If g=1,2 use E2-smallg.  Otherwise g>=3.  Since kappa=p-4 is odd, h=g-B is odd.
 - If h<=-3, apply E2-tip (B>=g+3).
 - If h>=15, apply E2-pair-tip.
 - Otherwise h in {-1,1,3,5,7,9,11,13}.  Here B=(p-h-4)/2>=7 for p>=31, so E2-balanced applies.
These cases exhaust the parameter domain.  All component seed-existence proofs are uniform; the strip component uses the weak
seed theorem under review.  []
This covers one positive-excess face, not E>=4, not smaller primes on this face, and not full RUNS or the inverse reduction.

## 5. Controls [F], not hypotheses

seedE2smallg.py / out/seedE2smallg.txt evaluates the 28 residue/weight constant rows and their availability/no-wrap/quality
inequalities.  Discarding the second configuration loses the quality/actual-empty certificate in 18 rows.  Prime sample p<=401:
138 classes, 966 target types, all exact arc formulas pass.  Constructive smoke: 36 sampled/pinned classes, 108 actual words,
25,320 configurations and 12,660 two-configuration intersections, 1,797 actually empty.  Independent c5 slow_lambda matches every
raw interval; zero failures.  These controls support, not replace, the q-independent table proof.  Peak child RSS 33,308,672 bytes;
native CPU/file-size limits.
