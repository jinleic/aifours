# E=2, R=2p-3: a uniform constant-offset seed certificate near g=B

Written 2026-10-17T19:58:40-0700, task OlsonRunCount5, cycle 6.  Status: [W] written proof with an explicit finite constant table, not independently
reviewed.  The table entries are evaluated integer min/max expressions with NO free B or p left; the proof applies to every B>=7,
not by extrapolating a finite-prime census.  Controls are [F] aids only.  No general NMH/RUNS/PAR/INV/INV* or ordered-Olson claim.

Dependencies: c3/proof-C-r1.md NMH setting; c6/proof-SEEDG-r2.md Lemma GS(a) and canonical lifts; c6/proof-SEEDGstar.md Lemma SCW-G*
and Theorem SEED-G* (under review), using only original C0+ case(i) because E=2.  No profile census, C0WB/A0 or count-free-finisher
claim is used.  Actual configurations and their no-wrap inequalities are established explicitly.

## 1. Parameters and ordinary-run availability conditional on a target

**Theorem E2-balanced.**  Let w be an NMH word with E=2, Delta0=3, so kappa=p-4,k=2p-5,R=2p-3.  Write g=kB and h=g-B.  If
  B>=7,  h in {-1,1,3,5,7,9,11,13},
then w has an identity 2p-subword, all run structures and placements included.

We have g=B+h, p=2B+h+4=2g-h+4.  Fix a target run of weight d in [-3,3].  Let n1 be the number of ordinary aligned singleton runs.
The following target-conditional bound holds:
  n1>=p+g-3+f_d,   where (f_(-3),f_(-2),f_(-1),f_0,f_1,f_2,f_3)=(4,2,0,1,0,0,1).       (1.1)
Proof.  With e_al+e_an+n_pr=2, n_al=k-B+e_an, every nonordinary aligned run consumes excess, so n1>=k-B-2+2e_an+n_pr.
For anti target d=-b, e_an>=b-1 gives the gains 2(b-1); for a pair n_pr>=1 gives gain 1.  For an aligned target of length 3, the
number of nonordinary aligned runs is at most e_al-1 (that target consumes two excess letters by itself), gaining 1.  No extra gain
is asserted for aligned lengths 1 or2.  Substituting k-B-2=p+g-3 gives (1.1).  []

At every target t we use only ordinary aligned runs outside t and its neighbours.  Two configuration types will be used:
 - S(t0): m=y=g+t0 isolated ordinary aligned singleton runs.  It exists if 2m<=n1-3, which follows from B>=2t0+2-f_d.
 - P(t0,u0): m=g+t0, y=g+u0, formed by j2=u0-t0 adjacent ordinary aligned pairs and j1=g+2t0-u0 ordinary aligned singles.
   It exists if j1,j2>=0 and m+y<=2n1-k-4; (1.1) makes the latter follow from t0+u0<=-5+2f_d.
The packing proof is the one in proof-S2wide.md, now applied to ordinary aligned intervals: after deleting the target's triple,
alpha-r>=2n1-k-4, with r the number of ordinary aligned intervals.  Their members are separated, and adding t adds one block.

## 2. B-independent arc formulas and the constant certificate

For any of these configurations write m=g+t0,y=g+u0.  Define integer constants
 L=min(-h+5-t0, u0+t0, floor((u0-h)/2)+1),
 U=max(t0-1, u0-h-t0-1, ceil((u0-h+3)/2)-1),
 L'=min(-h+4-t0, u0+d+t0+1, floor((u0+d-h)/2)+1),
 U'=max(t0, u0+d-h-t0-2, ceil((u0+d-h+3)/2)-1).
These are exactly lambda(Q)-g,U(Q)-g,lambda(Q+t)-g,U(Q+t)-g from Lemma H (E=2).  Hence its two-pattern seed interval before
canonical intersection is [L'-U,U'-L].  B and g cancel from these formulas.

The table gives TWO actually available configurations per target, their two-pattern intervals, and their intersection.  A range
[a,b] with a>b denotes an actual empty intersection, not an empty abstract quality window.  S(t0) abbreviates u0=t0.

| h | d | first configuration : seed | second configuration : seed | intersection |
|---|---:|---|---|---|
| -1 | -3 | P(1,2) : [-1,-1] | P(0,3) : [-2,-2] | [-1,-2] |
| -1 | -2 | S(1) : [-1,-1] | S(1) : [-1,-1] | [-1,-1] |
| -1 | -1 | S(2) : [0,0] | S(1) : [-1,-1] | [0,-1] |
| -1 | 0 | S(0) : [0,1] | S(1) : [0,0] | [0,0] |
| -1 | 1 | S(0) : [1,2] | S(1) : [0,0] | [1,0] |
| -1 | 2 | S(0) : [1,2] | S(1) : [1,1] | [1,1] |
| -1 | 3 | S(0) : [2,3] | S(1) : [1,1] | [2,1] |
| 1 | -3 | P(0,2) : [-1,-1] | P(0,3) : [-2,-2] | [-1,-2] |
| 1 | -2 | S(0) : [-1,0] | S(0) : [-1,0] | [-1,0] |
| 1 | -1 | S(0) : [0,0] | S(0) : [0,0] | [0,0] |
| 1 | 0 | S(0) : [0,0] | S(0) : [0,0] | [0,0] |
| 1 | 1 | S(0) : [1,1] | S(1) : [0,0] | [1,0] |
| 1 | 2 | S(0) : [1,1] | S(0) : [1,1] | [1,1] |
| 1 | 3 | S(0) : [2,2] | S(1) : [1,1] | [2,1] |
| 3 | -3 | S(0) : [-1,1] | P(-1,3) : [-2,-2] | [-1,-2] |
| 3 | -2 | S(0) : [-1,1] | P(-1,0) : [-1,0] | [-1,0] |
| 3 | -1 | S(0) : [0,1] | S(0) : [0,1] | [0,1] |
| 3 | 0 | S(0) : [0,1] | S(0) : [0,1] | [0,1] |
| 3 | 1 | S(0) : [1,1] | S(0) : [1,1] | [1,1] |
| 3 | 2 | S(0) : [1,1] | S(0) : [1,1] | [1,1] |
| 3 | 3 | S(0) : [2,2] | S(1) : [0,1] | [2,1] |
| 5 | -3 | P(-1,0) : [-1,1] | P(-2,3) : [-2,-2] | [-1,-2] |
| 5 | -2 | P(-1,0) : [-1,1] | P(-2,1) : [-1,-1] | [-1,-1] |
| 5 | -1 | S(0) : [-1,2] | S(-1) : [-1,1] | [-1,1] |
| 5 | 0 | S(-1) : [0,1] | S(-1) : [0,1] | [0,1] |
| 5 | 1 | S(-2) : [1,2] | S(-1) : [0,1] | [1,1] |
| 5 | 2 | S(-1) : [1,1] | S(-1) : [1,1] | [1,1] |
| 5 | 3 | P(-3,0) : [2,3] | S(-1) : [1,1] | [2,1] |
| 7 | -3 | P(-2,0) : [-1,1] | P(-3,3) : [-2,-2] | [-1,-2] |
| 7 | -2 | P(-2,0) : [-1,1] | P(-3,1) : [-1,-1] | [-1,-1] |
| 7 | -1 | S(-2) : [-1,2] | P(-4,-1) : [-2,1] | [-1,1] |
| 7 | 0 | P(-3,0) : [0,0] | P(-3,0) : [0,0] | [0,0] |
| 7 | 1 | P(-3,-2) : [1,2] | S(-1) : [-1,2] | [1,2] |
| 7 | 2 | P(-3,-2) : [1,2] | S(-1) : [0,2] | [1,2] |
| 7 | 3 | P(-3,0) : [2,2] | P(-2,-1) : [1,1] | [2,1] |
| 9 | -3 | P(-3,0) : [-1,1] | P(-4,3) : [-2,-2] | [-1,-2] |
| 9 | -2 | P(-3,0) : [-1,1] | P(-4,1) : [-1,-1] | [-1,-1] |
| 9 | -1 | P(-5,0) : [-1,1] | P(-5,0) : [-1,1] | [-1,1] |
| 9 | 0 | P(-3,0) : [0,1] | P(-4,0) : [0,0] | [0,0] |
| 9 | 1 | P(-5,0) : [1,2] | P(-4,-1) : [0,1] | [1,1] |
| 9 | 2 | P(-5,0) : [1,2] | P(-5,0) : [1,2] | [1,2] |
| 9 | 3 | P(-3,0) : [2,2] | P(-3,-1) : [1,1] | [2,1] |
| 11 | -3 | P(-4,0) : [-1,1] | P(-5,3) : [-2,-2] | [-1,-2] |
| 11 | -2 | P(-4,0) : [-1,1] | P(-5,1) : [-1,-1] | [-1,-1] |
| 11 | -1 | P(-5,0) : [0,0] | P(-5,0) : [0,0] | [0,0] |
| 11 | 0 | P(-4,0) : [0,1] | P(-5,0) : [0,0] | [0,0] |
| 11 | 1 | P(-5,0) : [1,1] | P(-5,0) : [1,1] | [1,1] |
| 11 | 2 | P(-5,0) : [1,1] | P(-5,0) : [1,1] | [1,1] |
| 11 | 3 | P(-4,0) : [2,2] | P(-4,-1) : [1,1] | [2,1] |
| 13 | -3 | P(-5,0) : [-1,1] | P(-6,3) : [-2,-2] | [-1,-2] |
| 13 | -2 | P(-5,0) : [-1,1] | P(-6,1) : [-1,-1] | [-1,-1] |
| 13 | -1 | P(-5,0) : [0,1] | P(-6,1) : [-1,-1] | [0,-1] |
| 13 | 0 | P(-5,0) : [0,1] | P(-6,0) : [0,0] | [0,0] |
| 13 | 1 | P(-5,0) : [1,1] | P(-6,1) : [0,0] | [1,0] |
| 13 | 2 | P(-5,0) : [1,1] | P(-5,0) : [1,1] | [1,1] |
| 13 | 3 | P(-5,0) : [2,2] | P(-4,1) : [0,1] | [2,1] |

All entries are obtained by the four explicit constant min/max formulas above.  Thus the table can be checked by integer arithmetic
without choosing any prime or a range of B.  For example, at h=7,d=1 the first configuration P(-3,-2) gives [1,2] and the second
S(-1) gives [-1,2]; their intersection is [1,2].  At h=-1,d=1, S(0) gives [1,2] and S(1) gives [0,0], with actual empty intersection
[1,0].  (The whole table records the exact individual intervals, not just a proposed final box.)

## 3. Every tabulated configuration is available at every B>=7; no wrap

The table has min(h+t0)=-1 and max(t0)=2.  Thus m=B+h+t0>=B-1>=6, and 2m+2<=k follows from t0<=B.  Its S entries have
max(2t0+2-f_d)=6, so the singles bound holds for every B>=7.  Its P entries have u0>=t0, min(h+2t0-u0)=-4, and t0+u0<=-5+2f_d.
Consequently j1=B+h+2t0-u0>=B-4>=3, j2>=0, and the target-conditional packing bound holds.  These statements are small integer
inequalities on the displayed table, and enlarging B preserves them; no word placement is used.

Each displayed individual interval lies inside [-8,8].  For singleton d in [-3,3], since B>=7 and g>=6,
 lambda({t})=d+1-g>=-g-2,   U({t})<=B+1.
Thus for every tabulated interval [sl,sh],
 lambda({t})-sh>=-g-10>-p,  U({t})-sl<=B+9<p
(p=g+B+4, B>6,g>5).  Lemma GS(a) therefore makes both intervals actual seed bounds after canonical intersection.  Their intersection
is empty, or is contained in the common box [-1,2], exactly as shown in the table.
In particular h=-1,1,13 already give an actual empty seed intersection for an ordinary aligned target d=1.  Every such word has
ordinary aligned runs by (1.1), so these three rows exclude the word directly without invoking SEED-G*.

## 4. Certification and finishing for the nonempty cases

Suppose w avoids, so no actual target can have an empty intersection.  Each canonical lift lies in its nonempty tabulated range,
canonically clipped, hence has a seed [a_t,b_t] inside [-1,2].  For E=2,Delta0=3, the closed bounds of Lemma LF in proof-SEEDGstar.md
give ceil(L_A(d))>=3 and ceil(L_B(d))>=3 for every d in [-3,3]; therefore 1-a_t<=2 and b_t+1<=3 imply (QS*).

We verify (P2) and (PIN), rather than assuming them.  For any y=d_s+d_t in [-6,6] and m0 in {1,2}, every term in lambda(Q^c) is
>=g: the first is p-m0+1>=g, the middle p-B+1-y+m0=g+5-y+m0>=g, and the floor term is at least g+floor((B-1)/2)+1>=g.
Thus a_s+a_t>=-2>=1-lambda(Q^c) because g>=6.  Conversely every term of p+lambda(Q)-1 is >=4: the first is 2p-m0; the middle is
B+4+y+m0-1>=B-2>=5; the floor term is p+floor((y+B)/2)>=p.  Hence b_s+b_t<=4<=p+lambda(Q)-1.  These are both (P2) inequalities for
all pairs (even the harmless superset of weight pairs impossible under the excess budget).
For (PIN), lambda({t})=d+1-g and b_t<=2 give b_t-lambda({t})<=g+4<=p-1.  All conditions of Lemma SCW-G* hold.  As n_ev,al<=E=2,
Theorem SEED-G* with C0+ case(i) contradicts avoidance.  This proves E2-balanced.  []

## 5. Controls [F], not hypotheses

seedE2balanced.py / out/seedE2balanced.txt checks the 56 B-independent constant rows, all individual interval values, availability
at B=7 and monotonic margins; 35 configuration entries use the target-conditional availability improvement, and discarding the
first configuration loses the stated [-1,2]/empty certificate in 9 rows.  Separate prime samples, B=7..120: 363 classes, 2,541 target
types, with the exact proper arcs, no wrap, P2/PIN.  Constructive smoke: 48 classes, 144 actual words, 61,368 target configurations
and 30,684 actual two-configuration intersections, of which 10,033 are actually empty.  Independent c5 slow_lambda matches every
listed interval; zero failures.  These samples do not replace the B-independent table proof.  Peak child RSS 33,832,960 bytes;
native CPU/file-size limits used.
