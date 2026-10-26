# Addendum 5 — ternary-first obstruction and projection support at least300

Actual clock observed immediately before this immutable freeze: **2026-10-23T16:59:51-0700**. Owner: InfoGuessingRminus, info-5. **COMPLETE WRITTEN CANDIDATE FOR SEPARATE RECONSTRUCTION; NOT ACCEPTED.** No scientific program, enumeration, LP, code search, import, compilation or numerical entropy check was executed. All case arguments and arithmetic below are written. All launch HOLDs remain unchanged.

This is ONE consolidated strengthening of the same primary barrier, not additional problem slots or a list of incremental packets. It supersedes the cardinality72/effective-order8640 thresholds at the explicitly stated import scope, without changing any old snapshot. The full matched interval remains **20/3 <= gn(R-minus) <= 1847/276**. No numeric guessing-number improvement, full solution, formal proof, sharpness or novelty claim is made.

## 1. Literal target, exact inputs and reduced dependency boundary

Retain the graph in `inputs-v1.json`, observed frozen SHA

`bdc4cd14d20e2401971a7354c2a6239106fbe2be158b50921d5c486c6a086be6`.

It has vertices1,...,10 and the26 undirected edges

    12 13 14 15 16 17 23 27 29 2-10 34 38 39
    45 48 4-10 56 59 5-10 67 68 69 78 7-10 89 8-10.

The FDs are H(X_v | X_N(v))=0. The hubs are1,8; the peripherals are2,3,4,5,6,7,9,10. For an arbitrary finite law define

    Phi(X)=2 sum_v H(X_v)-3H(X_1,...,X_10).

The eight ordered diamonds D=(U,V;P,Q) are

    D1=(2,4;1,3), D2=(2,6;1,7), D3=(3,5;1,4), D4=(5,7;1,6),
    D5=(3,10;4,8), D6=(4,9;3,8), D7=(6,10;7,8), D8=(7,9;6,8).

Their U,V are the nonadjacent first pair. Let Z_D be the six-vertex complement. The retained old entropy import is **I2 ONLY**: for each listed D, the frozen rational certificate proves, modulo the literal graph FDs,

    Phi(X)=J_D(X)+3 S_D(X),  S_D(X)>=0,                       (I2)
    J_D=I(U;V|P,Z_D)+I(U;V|Q,Z_D)+I(P;Q|Z_D)-I(U;V|Z_D).

Thus Phi<0 forces EVERY J_D<0. The raw eight coefficient identities have NOT been replayed or fully hand-expanded in this round; they remain the explicitly named import/reconstruction gate. Metadata hash agreement is not a coefficient proof. **No nine-vertex I1/deletion certificate, pair-MI budget, or finite-group classification is used to prove support>=300.** This removes the I1 dependency of the earlier72 proof, rather than silently assuming its conclusion.

The new theorem is: if the full graph law is **quasiuniform**, satisfies the FDs and Phi<0, then for EVERY listed D,

    |support(X_Z_D)| >= 300.                                (T300)

Quasiuniform means EVERY marginal is uniform on its support. Uniformity of the full winning set alone does not suffice.

## 2. Regularity and two elementary entropy templates

For a quasiuniform tuple, every positive-probability conditioning fiber is again quasiuniform, and every conditional marginal cardinality is independent of the conditioned value. Indeed, the probability of an atom of X_A given X_B is the constant ratio of the positive masses of X_AB and X_B. In particular a uniform N-point full support has every marginal cardinality dividing N. The same divisibility holds inside each conditional fiber.

A quasiuniform pair of cardinalities r,s has a biregular bipartite support with E edges, where r and s divide E and E<=rs. Consequently **coprime cardinalities imply independence**.

Write the unconditioned four-variable expression as

    J(A,B;P,Q)=I(A;B|P)+I(A;B|Q)+I(P;Q)-I(A;B),
    R=I(A;B).

Two elementary templates will be used:

1. If one of P,Q is independent of EITHER A or B, its conditional-MI term is at least R. For example I(A;B|P)-R=I(P;B|A)-I(P;B), which is nonnegative when P is independent of B. Thus J>=0.
2. If both conditioners determine one of A,B, then I(P;Q)>=R by data processing (or by their common A/B if they determine the same one). Hence J>=0. More generally, if K is a common deterministic function of A,B and H(K)=R, then

    J >= H(K|P)+H(K|Q)+I(P;Q)-H(K)
      = I(P;Q|K)+H(K|P,Q) >=0.                              (CI)

In particular A=f(B), B=f(A), or independence of A,B suffices. These identities use only chain rules and Shannon nonnegativity.

## 3. A FIRST variable with at most3 values forces Ingleton

**Lemma 3.** If (A,B,P,Q) is jointly quasiuniform and A has at most3 values, then J(A,B;P,Q)>=0. The same holds with A,B interchanged. This lemma makes NO claim for arbitrary nonquasiuniform P,Q extensions of a ternary pair.

The constant case is immediate. For a binary A, the degree of each B vertex in the quasiuniform pair support is1 or2. Degree1 means A=f(B), and degree2 means independence; both are covered by §2.

Suppose A has exactly3 values. Every B vertex has a common degree d in{1,2,3}. Degrees1 and3 again give A=f(B) and independence. It remains to treat degree2, where

    R=H(A)-H(A|B)=log3-log2=log(3/2).

For every b define T(b) as the UNIQUE missing A value among the three. Thus T is a deterministic function of B, and P(A=a|B=b)=1/2 for a!=T(b). Uniformity of A implies P(T=t)=1/3: P(A=a)=(1-P(T=a))/2=1/3. Therefore the pair(A,T) is uniform on the six off-diagonal pairs and

    I(A;T)=log(3/2)=R.                                     (3.1)

Consider a conditioner P. Let a=|support(A|P=p)| and e=|support(A|B=b,P=p)|; quasiuniformity makes these constant over positive conditioning values. Since each B value globally permits only two A values, e<=2, e<=a and a<=3. Thus

    I(A;B|P)=log(a/e).

The possibilities are: (a,e)=(1,1) gives0; (2,1) giveslog2; (2,2) gives0; (3,1) giveslog3; (3,2) givesR. So a value STRICTLY below R occurs only in the following two cases:

- a=1: A is a function of P;
- a=e=2: for any p,b occurring together, the two A values possible given(b,p) equal BOTH the A-support at p and the globally permitted A-pair at b. Hence their missing third value is T(b) and is determined by p. Thus T is a function of P.

Exactly the same argument applies to Q. If either conditional-MI term is at least R, J>=0 immediately. Otherwise each conditioner determines A or T. If they determine different ones, data processing gives I(P;Q)>=I(A;T)=R. If they determine the same one, their mutual information is at least log3>R. Hence J>=0 in every case. This proves the lemma. QED.

Applied inside each Z_D fiber, I2 therefore implies

    |support(X_v)|>=4  for EVERY peripheral v.              (3.2)

Every peripheral appears as a first variable in the literal list. This is stronger than the earlier binary-first bound>=3, with no I1 premise.

## 4. A binary CONDITIONING variable also forces Ingleton

**Lemma 4.** If the four-law is quasiuniform and P has at most2 values, then J(A,B;P,Q)>=0 (and likewise for Q).

The constant case is immediate. For binary P, each pair(P,A) is either independent or has P=f(A), by its degree1/2 support graph. The same dichotomy holds for(P,B). If either independence holds, template1 of §2 proves J>=0. Otherwise P is a common function of A and B. In that case

    I(A;B|P)=R-H(P),  I(A;B|Q)>=H(P|Q),

so J>=-H(P)+H(P|Q)+I(P;Q)=0. QED.

Each hub appears as a conditioning variable of a listed D. Applying this inside Z_D fibers gives

    |support(X_1)|>=3,  |support(X_8)|>=3.                  (4.1)

Together (3.2),(4.1) also exclude constants. No I1 argument is needed for that exclusion.

A further consequence is important below: **a hub with exactly3 global values cannot coexist, in any one of its diamonds, with a FIRST peripheral having exactly4 global values.** For otherwise a negative conditional J would require that peripheral's conditional alphabet to be4 by Lemma3, and the hub's to be3 by Lemma4. Coprimality makes them independent in that fiber, so template1 contradicts negativity. Thus a hub of global size3 forces all its first-pair peripherals to have at least5 values. For hub1 these are{2,3,4,5,6,7}; for hub8 they are{3,4,6,7,9,10}.

## 5. A complete all-four-4 diamond obstruction on at most16 atoms

**Lemma 5.** Let (A,B,P,Q) be jointly quasiuniform, all four singleton cardinalities4, and H(A,B,P,Q|P,Q)=0. Then J(A,B;P,Q)>=0.

Write N for the full support cardinality. The FD means the map from full support to(P,Q) support is bijective, so N=|support(P,Q)|<=16. Uniformity of the four marginals gives4|N, hence N is4,8,12 or16. Let E=|support(A,B)|. It divides N, is a multiple of4 and lies between4 and16. E=4 makes A,B bijectively determine each other, while E=16 makes them independent. These cases are already covered by §2.

For N=4 there is no other case. For N=8 the remaining case is E=8 with R=log2. Each P or Q fiber contains N/4=2 equiprobable full atoms. Conditional A,B support sizes divide2. If neither is1, both sizes and their joint size are2, giving conditional MI=log2=R. Otherwise the conditioner determines A or B. Consequently either one CMI term is at least R, or both conditioners determine a first variable and template2 applies.

For N=12 the only remaining case is E=12 with R=log(4/3). Each conditioner fiber has3 atoms, so conditional A,B support sizes are1 or3. If neither is1, both and their joint support have size3, giving CMI=log3>R. Again template2 settles the only alternative.

For N=16 the remaining case is E=8, R=log2. Its uniform pair support is a simple2-regular bipartite graph on4+4 vertices. It is either one8-cycle or two4-cycles; these are the only cycle decompositions, since a simple bipartite cycle has length at least4.

- Two4-cycles are two complete2-by-2 blocks. Their component label K is a uniform common binary function of A,B with H(K)=log2=R. Equation(CI) proves J>=0.
- For an8-cycle, fix either conditioner. Its fiber has4 uniform atoms. If neither conditional singleton is constant, their sizes are in{2,4}. For sizes(2,2), the joint conditional support is2 or4;4 would create a forbidden complete2-by-2 subgraph of the8-cycle, so it is2 and CMI=log2. For sizes(2,4) or(4,2), the joint size must be4 and CMI=log2. For sizes(4,4), the joint size is4 and CMI=log4. Thus every CMI is at least R unless its conditioner determines A or B. Template2 again excludes J<0.

All possible N and E have been exhausted by explicit divisibility and graph arguments; no enumeration or code is used. QED.

**Global corollary.** A listed graph diamond cannot have all four GLOBAL singleton cardinalities4 when Phi<0. Inside any complement fiber, negative J requires both first conditional alphabets to be4 by Lemma3. A conditioning alphabet of size<=2 is excluded by Lemma4, and size3 is independent of a first alphabet4 by coprimality, again excluding negativity. Hence all four conditional alphabets would be4. The actual graph FD H(U,V|P,Q,Z_D)=0 supplies Lemma5 inside that fiber, a contradiction.

## 6. Exact projection inequality and literal inner diamonds

Retain the independently written FD+Shannon compensation identity from Addendum4, SHA

`8ee89c2dd05f2c448938495c14f246090c268f69b114aed0d3d43e6c85940687`:

    Phi = Phi_Z + 2 sum_{v in D} I(X_v;X_Z) + L_D,
    Phi_Z=2 sum_{z in Z}H(X_z)-3H(X_Z),
    L_D=I(P;Q|Z)+2I(U;V|Z)+I(U,V;P|Z)+I(U,V;Q|Z)>=0.

It is an EXACT identity for every finite FD-consistent law, not an imported LP result. Its derivation uses T=H(D|Z)=H(P,Q|Z)=H(U,V,Q|Z)=H(U,V,P|Z) and adds the three corresponding subadditivity slacks. Thus Phi<0 forces Phi_Z<0. For a quasiuniform law, put m=|support(X_Z)| and n_z=|support(X_z)|. Then

    m^3 > product_{z in Z} n_z^2,  and each n_z divides m.   (6.1)

Here are the ACTUAL complements, inner diamonds and the four peripherals forced>=5 when the retained hub has size3. They are direct set memberships in the pinned graph, not a nickname-based reconstruction.

| Outer D | Z | One inner diamond contained in Z | Hub | Four affected peripherals in Z |
|---|---|---|---|---|
|D1|{5,6,7,8,9,10}|D7|8|6,7,9,10|
|D2|{3,4,5,8,9,10}|D5|8|3,4,9,10|
|D3|{2,6,7,8,9,10}|D7|8|6,7,9,10|
|D4|{2,3,4,8,9,10}|D5|8|3,4,9,10|
|D5|{1,2,5,6,7,9}|D2|1|2,5,6,7|
|D6|{1,2,5,6,7,10}|D2|1|2,5,6,7|
|D7|{1,2,3,4,5,9}|D1|1|2,3,4,5|
|D8|{1,2,3,4,5,10}|D1|1|2,3,4,5|

## 7. Projection support>=300: the complete proof

Fix ANY listed Z. Its five peripheral cardinalities are at least4 and its hub cardinality at least3.

If that hub has exactly3 values, §4 and the table force four of the five peripherals to have at least5 values; the fifth has at least4. Hence

    product n_z >= 3*5^4*4 =7500,
    m^3 > 7500^2 =56250000 >300^3 =27000000.

Thus m>300 in this case.

Otherwise the hub has at least4 values, so all six n_z>=4. The table gives a graph diamond entirely inside Z. If all six n_z were4, that inner diamond would have four global alphabets4, contradicting the global corollary of Lemma5 and I2. Thus at least one n_z>=5 and

    product n_z >= 5*4^5=5120.

Suppose, for contradiction, m<300. If some n_z>=6, then

    m^3 > (6*4^5)^2 =37748736 >300^3,

impossible. If two n_z are at least5, then

    m^3 > (5^2*4^4)^2 =40960000 >300^3,

also impossible. Therefore EXACTLY one cardinality is5 and the other five are4. Uniform-fiber divisibility gives20|m. But

    m^3 >5120^2=26214400 >280^3=21952000,

so m>280. There is no multiple of20 strictly between280 and300. This contradiction proves m>=300. The argument applies separately to each of the eight Z, proving(T300). QED.

The threshold is NOT asserted sharp and no construction at300 is supplied. It is a necessary barrier for Phi-negative QUASIUNIFORM graph laws, not a cardinality bound for arbitrary finite/nonuniform laws.

## 8. Consequence for uniform coset constructions, with a separate old import

For a uniform finite-group coset law, m=[G:L_Z], where L_Z is the intersection of the six complement stabilizers. I2 makes the conditional four-law inside L_Z an Ingleton violator, as in the original localization proof. If one ALSO admits the same published computer-assisted minimum offender order120, then

    |G|=[G:L_Z]*|L_Z| >=300*120=36000.

Quotienting by core_G(K), K the intersection of all ten coordinate stabilizers, preserves the law and localization. Thus the honest effective-order version is

    |G/core_G(K)| >=36000.

This additional order120 import is NOT used in(T300), and the effective group order is NOT the number of winning codewords. No finite-group classification was executed or freshly certified here. The separate PSL2/PGL2 family barrier is unchanged.

## 9. Exact remaining import pins and verification/status boundary

The eight I2 files lie under `information-science/evidence/six-lane-20261016/guessing-number-r-minus/evidence/certs/`. Their actual metadata hashes were refreshed before this freeze and match the prepared replay's pins:

| File | SHA-256 |
|---|---|
|diamond_2_4_1_3.json|c570b19e84685964493af9db86eec41639ceb40d3cbfa5c7dac855f9326a3b9a|
|diamond_2_6_1_7.json|9d623cc6bcbdf49e10e22da468b0c744f08571dfc15b9c97bef18f374f762e46|
|diamond_3_5_1_4.json|78ec434ce4cae98bdb589dd4e0017318be0d3f774a825f5154d4533a6e9a5cbc|
|diamond_5_7_1_6.json|190e687c8b7c8438243b5b9f76130eeb197bcd3da065f40c0d7e9aa55d1cad8d|
|diamond_3_10_4_8.json|4b058c8a8718ad023d0e9d81f1bf62cf885659498d7194008823539fbc210ab0|
|diamond_4_9_3_8.json|9b5d1d18f7662af5614cdac3a8d8ba6c2986cfd4db3d6f83e6cab0a9e526305f|
|diamond_6_10_7_8.json|3620de2b76d8d50404bbd75667e363872624d648802bf8f610490d3bf4d32eae|
|diamond_7_9_6_8.json|cf9d517c563a3097cc95b40557a41d9dc27a8de4b5342599e3d3d9aec9efc6e7|

I1 is absent from the new proof. This does not retroactively authenticate I2: the existing replay proposal remains HOLD, the five-variable assay remains PREPARED ONLY, and the current global scientific-launch HOLD supersedes any expectation of an immediate run. Required separate written reconstruction targets are the ternary missing-value argument, binary conditioning lemma, all-four-4 <=16-atom cases, literal table and final divisibility proof. If any is defective, the previous72 packet is not silently replaced by an accepted stronger claim. Full gn(R-minus), the nonquasiuniform case, and the exact300 threshold remain unresolved.

## 10. Refreshed public-source screen: antecedents, not novelty clearance

The earlier matched baseline/primary-source pins in selection-v1.md remain unchanged. A refreshed exact `1847/276` guessing-number search still matched the Kybernetika2024 result, not a new solution: [Gürpınar's primary journal PDF](https://dml.cz/bitstream/handle/10338.dmlcz/152714/Kybernetika_60-2024-5_1.pdf). Search absence is not proof of openness or novelty.

I additionally read the primary [Fong–Shadbakht–Hassibi, On the Entropy Region and the Ingleton Inequality, MTNS2008](https://scholar.lib.vt.edu/MTNS/Papers/164.pdf), especially §2.2. It already describes all-four-binary quasiuniform entropy vectors and Ingleton validity. I do NOT present binary quasiuniform validity as this round's discovery; its scope is not the literal R-minus300 barrier or the complete mixed-alphabet ternary-first argument above. No exhaustive priority claim is made for either lemma.

The current [Csirmaz, Revisiting the Stability of the Ingleton Inequality: A Tropicalization-Free Approach, arXiv2607.16773v1](https://arxiv.org/pdf/2607.16773v1) was read through its constructions, Theorems8–11 and conclusion. It gives updated stability bounds and a new infinite family for a sum of two Ingleton expressions. The two expressions share their FIRST pair and incur additional conditional-MI terms; the eight graph diamonds here have different first pairs and different complements. No FD implication removing those terms is supplied by this packet. Thus that source is a baseline/input for a possible next universal-bound attack, not permission to infer a new numeric R-minus bound. It is not a load-bearing theorem in(T300). The already read Matveev–Romashchenko spectral/current-stability sources likewise do not automatically provide the missing graph-specific interface.

**Novelty status remains UNCLEAR.** The deliverable here is a complete, auditable, classification-free small-alphabet-to-graph barrier with I2 exposed and I1 removed, awaiting actual separate reconstruction and parent disposition—not a public priority claim, a restatement counted as a numeric bound, or a solver outcome.
