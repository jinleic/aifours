# R-minus: exact parametric criterion for the full three-witness, five-label transport

Owner `InfoGuessingRminus-2`, info-5. Actual clock receipt: `/bin/date` returned `Sun Oct 25 13:25:35 PDT 2026` before this body.

**NEW WRITTEN iff theorem and constructive no-gain family**, allm>=2 INCLUDING COMPOSITES. This is not only a necessary-condition increment. Every family satisfying the explicit criterion has an actual simultaneous original-FD removal injection, with ALL solutions for the fixed witness pattern displayed. No scientific interpreter/program, symbolic kernel, enumeration, replay, CLI or nested agent. No machine-checked, configured-family, formal/kernel/human or novelty claim.

## 1. Exact scope

Work on the literal26-edge R-minus graph and its chosen ten triangles

`T1=123,T2=145,T3=167,T4=239,T5=(2,7,10),`

`T6=389,T7=(4,5,10),T8=(4,8,10),T9=569,T10=678`.

Use their three independent incident Z_m slots at each original physical vertex; write A,...,J for these triangle indices. Baseline C_m has all ten sums0. Let eta0=0 and let eta1,...,eta4 be ANY proposed ten-entry Z_m syndrome rows.

Fix exactly this ONE global witness assignment f on all ten label pairs:

`f(ij)=6` for all pairs in S={0,1,3,4};

`f(12)=f(23)=3`; `f(02)=f(24)=2`.                       (PATTERN)

The induced physical palette{2,3,6} has original edge23 and isolated6. Neighbour equalities and own-symbol inequalities in this paper always refer to the WHOLE original physical symbols and their full original N(v).

**The theorem below is iff for(PATTERN), not iff for all possible global sections or Hall maps.** It proves actual four-class no-gain whenever its conditions hold. Arbitrary syndrome families outside the criterion, and in particular the binary reduction of the earlier specified family, are not silently replaced by the examples here. Global20/3..1847/276 and T300 are unchanged.

## 2. Exact necessary and sufficient criterion

Define full actual defect tuples

`d2(eta)=(eta_A,eta_D,eta_E)`,

`d3(eta)=(eta_A,eta_D,eta_F)`,

`d6(eta)=(eta_C,eta_I,eta_J)`.

**Theorem CRIT.** For every m>=2, representatives b0=0,b1,...,b4 with exact syndromes eta0,...,eta4 and ALL ten confusion comparisons(PATTERN) exist IF AND ONLY IF all the following conditions hold:

**Three congruence conditions:**

`eta2,F=0`, `eta4,F=0`, `eta1,B=eta3,B`.                  (EQ)

**Simultaneous actual own-symbol inequalities:**

1. the FOUR tuples `0,d6(eta1),d6(eta3),d6(eta4)` are pairwise DISTINCT;
2. `d3(eta1)!=d3(eta2)` and `d3(eta3)!=d3(eta2)`;
3. `d2(eta2)!=0` and `d2(eta4)!=d2(eta2)`.                (NEQ)

No field/rank relaxation appears. The conditions automatically make the five syndrome rows distinct: every pair has a named actual nonzero defect in(NEQ). In particular the four outside classes really are nonzero and mutually disjoint.

## 3. Necessity: one neighbour-connectivity graph, not an ansatz

For EACH original physical vertex u form the graph E_u on the SAME five labels by

`ij in E_u iff f(ij) in N(u)`.

Every E_u edge forces equality of the full physical-u symbol. Their connected components for(PATTERN) are EXACTLY

|physical u|components of E_u|
|---|---|
|1|{0,1,2,3,4}|
|2|{1,2,3},{0},{4}|
|3|{0,2,4},{1},{3}|
|4|{1,2,3},{0},{4}|
|5|{0,1,3,4},{2}|
|6|{0},{1},{2},{3},{4}|
|7|{0,1,2,3,4}|
|8|{0,1,2,3,4}|
|9|{0,1,2,3,4}|
|10|{0,2,4},{1},{3}|

These follow directly from the complete original witness neighbourhoods

`N2={1,3,7,9,10}`, `N3={1,2,4,8,9}`,

`N6={1,5,7,8,9}`:

physical1and9 observe all three colours, physical7 observes2and6, physical8 observes3and6; these four label graphs are connected. Physical2and4 observe colour3 alone, physical3and10 observe colour2 alone, physical5 observes6 alone, and physical6 observes none. Thus all components, including the unused physical vertices, have been retained.

Since b0=0, this FORCES physical1,7,8,9 to be0 on ALL rows. Physical2and4 are each constant on labels1,2,3. Physical3and10 are0 on labels0,2,4. Physical5 is0 on S. Physical6 is unrestricted by neighbour equality alone. This is necessary for EVERY section with(PATTERN), not a support restriction added to find one solution.

The actual triangle sums now force eta2,F=eta4,F=0, because T6=389 has all three slots0 at those rows. They force eta1,B=eta3,B, because T2=145 has physical1and5 equal0 on S and physical4 equal on labels1,3. These are(EQ).

For comparisons at6 within S the own symbols are exactly d6(eta_i), because all their N6 symbols are0. Their pairwise inequalities give(NEQ1).

At3, rows2 have physical3=0, while rows1and3 have own tuples exactly d3(eta1)-d3(eta2) and d3(eta3)-d3(eta2); see the explicit formula below. Thus pairs12,23 require(NEQ2).

At2, rows0,2,4 have all N2 symbols0 and hence own tuples0,d2(eta2),d2(eta4). Pairs02,24 require(NEQ3). All necessary conditions have been obtained from the same original array.

## 4. Sufficiency: all representatives and all free parameters

Assume(EQ),(NEQ). Choose ANY g,k in Z_m. Use the actual slot orders

`2:(A,D,E)`, `3:(A,D,F)`, `4:(B,G,H)`,

`5:(B,G,I)`, `6:(C,I,J)`, `10:(E,G,H)`.

All rows are0 at1,7,8,9; b0 is entirely0. Define

`Z=(eta2,A,eta2,D,eta2,E)`, `W=(eta4,A,eta4,D,eta4,E)`,

`Y=(eta1,B,g,eta2,H)`, `T=(eta4,B,eta4,G,eta4,H)`,

`X1=(eta1,A-eta2,A,eta1,D-eta2,D,eta1,F)`,

`X3=(eta3,A-eta2,A,eta3,D-eta2,D,eta3,F)`,

`Q1=(eta1,E-eta2,E,eta1,G-g,eta1,H-eta2,H)`,

`Q3=(eta3,E-eta2,E,eta3,G-g,eta3,H-eta2,H)`,

`P=(eta2,B-eta1,B,eta2,G-g,k)`,

`U1=d6(eta1)`, `U3=d6(eta3)`, `U4=d6(eta4)`,

`U2=(eta2,C,eta2,I-k,eta2,J)`.

Then set the COMPLETE remaining physical array to

|row|physical2|physical3|physical4|physical5|physical6|physical10|
|---|---|---|---|---|---|---|
|1|Z|X1|Y|0|U1|Q1|
|2|Z|0|Y|P|U2|0|
|3|Z|X3|Y|0|U3|Q3|
|4|W|0|T|0|U4|0|

Every representative coordinate is fixed by the given rows and the SAME two parameters g,k. These formulas give ALL solutions of the syndrome and neighbour-equality equations: the component table forces their shared/zero shape; trianglesT1,T4,T5 fix Z,W,X1,X3 and E parts, T2 fixes the B parts, T6 fixes F, T8 fixes H, T7 fixes G up to the one g, T9 fixes I up to the one k, while T3andT10 fix the C,J components of physical6.

### 4.1 Complete syndrome reconstruction

The exact reduced slot sums for every row are

`T1: b2,A+b3,A`, `T2: b4,B+b5,B`, `T3: b6,C`,

`T4: b2,D+b3,D`, `T5: b2,E+b10,E`, `T6: b3,F`,

`T7: b4,G+b5,G+b10,G`, `T8: b4,H+b10,H`,

`T9: b5,I+b6,I`, `T10: b6,J`.

Substitution yields eta_i coordinate-by-coordinate: all differences cancel; the only remaining equalities needed are exactly(EQ). In particular T7 at row2 is g+(eta2,G-g)=eta2,G, T9 at row2 is k+(eta2,I-k)=eta2,I, and T2 at row3 uses eta1,B=eta3,B. No inversion or division is performed.

### 4.2 Complete actual confusion comparisons

For all six S pairs, full N6 symbols are0 and own physical6 values are0,U1,U3,U4, pairwise distinct by(NEQ1).

For pairs12,23, full N3 symbols agree because physical2 is Z, physical4 is Y and physical1,8,9 are0 on all three rows. Their own differences are X1 and X3 relative to row2=0, nonzero by(EQ),(NEQ2).

For pairs02,24, full N2 symbols are all0. The required own physical2 differences are Z and W-Z, nonzero by(NEQ3).

Thus ALL ten comparisons hold jointly in the one displayed array. This proves sufficiency and the iff theorem. ∎

## 5. Actual removal injection, arbitrary nonlinear subsets and arbitrary deletions

The standard triangle decoder is `x_v=f_v^0(x_Nv)+d_v(eta(x))`. Consequently the ACTUAL removal union for outside FD data A is

`R(A)=UNION_(x in A) UNION_(v:d_v(eta(x))!=0)`

`     {c in C_m:c_Nv=x_Nv}`.

For every family satisfying CRIT, define the ONE simultaneous map `Phi(x)=x-b_i` on class i. Exact syndromes put its image in C_m. The fixed comparisons01,03,04 at6 and02 at2 have b_i,Nv=0,b_i,v!=0; hence Phi(x) belongs to the actual removal fibre generated by x at that v.

If two different-class images collided, x-y=b_i-b_j would have equal full neighbour symbols and a different own symbol at the ONE fixed original witness f(ij), contradicting FD of A. Within-class translation is injective. Therefore

`|A|<=|R(A)|`

for EVERY nonlinear FD subset of the four original nonzero classes. Any actual deletion set D making `(C_m\D) union A` FD contains R(A), so its cardinality cannot exceed |C_m|. No deletion-fibre disjointness or summation of pairwise counts was assumed.

This is a complete positive transport conclusion for the WHOLE criterion class, not merely a list of necessary conditions on possible trades.

## 6. Two distinct constructive controls, not a substituted primary

### 6.1 Previously frozen actual family, allm>=3

The actual eta table in `five-label-three-witness-actual-removal-transport-v1.md`, SHA256 `11cfe556730bf64851e925a8ee5ae0dd2f14ac5c4dc05746e00f30224b6aa54b`, satisfies CRIT for allm>=3, with g=k=0, giving its explicit array verbatim. Its d2(eta4)-d2(eta2) has A component2, so that particular pair condition fails at m2. This theorem does NOT claim to repair its binary reduction.

### 6.2 A DIFFERENT four-class family valid for EVERYm>=2

For a uniform binary/composite boundary control, use these NEW actual rows (A,...,J order):

`tau1=(0,0,0,0,1,1,0,1,0,1)`,

`tau2=(0,1,1,0,1,0,1,1,0,0)`,

`tau3=(1,0,0,1,1,0,0,1,1,0)`,

`tau4=(1,1,0,0,1,0,0,0,1,1)`.

Their F2,F4 are0 and B1=B3=0. The four6-defect tuples are

`0,(0,0,1),(0,1,0),(0,1,1)`,

pairwise distinct for everym>=2. The two3-differences are(0,0,1) and(1,1,0), and the two2-differences are(0,0,1) and(1,0,0). All are nonzero because1 is nonzero. Thus CRIT supplies an actual section and whole-four-class removal injection at everym>=2, not just odd or prime m.

These tau rows are explicitly a DIFFERENT family, a nonvacuity/binary boundary control of the parametric theorem. They are not an improved guessing bound or a silent replacement of the original arbitrary-family target.

## 7. Exact remaining original problem

The new representation is an exact common-array criterion with explicit all-solutions formulas and actual-removal transport, not independent local partitions. It covers arbitrary syndrome rows satisfying the three displayed congruences and every simultaneous inequality, including arbitrary nonlinear FD subsets and all actual deletions.

When an input violates CRIT, the conclusion is ONLY that this fixed(PATTERN) fails. Other global comparison assignments, other sections or general Hall maps may still work. There is no no-globalSECTION conclusion, much less a positive-gain trade. The universal at-most-eight-witness reduction is a separate NEW WRITTEN candidate and is not a correctness input here.

Still open: arbitrary four nonzero syndromes for everym>=2, then arbitrary larger class families/global optimum or an actual positive-gain FD trade with its actual removal union. No original20/3..1847/276/T300 promotion is made. All current assurances remain WRITTEN only, at the ordinary original-graph/triangle-code definitions; no unadmitted historical calculation, scientific executable, new GO or formal/novelty gate is imported.
