# Any septic SPR7 counterexample yields a strict rational eight-atom certificate

Owner **InfoSPR7-2**, slot info-2. Actual `/bin/date` immediately before writing: **Wed Oct 28 18:10:41 PDT 2026**. **WRITTEN author-unreviewed candidate.** This strengthens the earlier conditional strict-certificate route: subject to the named complete source chain, strict rational nonpositive-cone certificates are COMPLETE for the original existence-of-counterexample question. It does not assert that a counterexample or certificate exists.

## 1. Exact theorem and scope

Use the original actual independent closed monic degree-seven box K: every a in K is strictly Hurwitz, and an original witness is ONE real b of EXACT degree seven with `Re[b(iw)/a(iw)]>0` for every actual a and every finite real w. Degenerate coefficient intervals are allowed.

Import the complete author-written `frontier-20261028-connected-eight-atom-algebraic-obstruction-v1.md`, SHA256 `d8c1deeab9439e9f0644e2fde45c40a0c188904fbb2a56a8afdc8e989b4d90ac`, including its exact actual-corner zero-annihilator alternative and the path-connected support-8 lemma; the complete rational-superbox/four-corner source `frontier-20261028-rational-box-rational-numerator-reduction-v1.md`, SHA256 `6d29bc63925a100394b1b3efc8fe9fecf49660f7c6ff19798ba246e42442f328`; and the full homotopy/positive-coefficient source `frontier-20261028-positive-cone-rational-obstruction-v1.md`, SHA256 `2f5f6a87c24556efac981a5c4ee1ad7d2089a6b8e9113897b6944c3d01f761a8`. These sources are currently unreviewed candidates and their acceptance is NOT assumed.

**Theorem.** The following are equivalent:

1. There exists ANY eligible original real-endpoint K, possibly degenerate, with no unrestricted exact-degree-seven common SPR numerator.
2. There exists an eligible rational-endpoint K' with all seven widths strictly positive, at most eight indices i_k among its four ACTUAL coefficient corners, rational compactified frequencies `x_k in [0,1]`, and positive rational weights lambda_k summing to1, for which **every one of the eight rational coefficients**

   `F_j = sum_k lambda_k V_(i_k,j)(x_k)`

   is strictly negative. Here V is the ORIGINAL compactified pairing coefficient vector, not a free tuple.

Moreover, if 1 holds, K' can be chosen as a strictly outward rational superbox of the original counterexample, and the strict certificate persists throughout some open endpoint neighborhood of K'. The implication does **not** say the original K itself has a strictly negative vector, nor that its original zero-certificate nodes were rational.

This is an original-target-preserving finite rational negative-witness theorem, not a proof of either outcome. The exact candidate/certificate can in principle be exhaustively enumerated and checked using rational arithmetic and the predecessor's Routh/Sturm stability predicate; this proposed search has NOT been run.

## 2. Nonpositive certificate caller

For a monic real b of degree seven let V_i(x) be the coefficient vector of

`T_(a_i,x)(b)=(1-x)^7 Re[b(i sqrt(t)) a_i(-i sqrt(t))]`,
`t=x/(1-x)`, `0<=x<1`, with the continuous endpoint `T_(a_i,1)(b)=b_7`.

The four a_i are the actual parity corners of K'. If F from 2 has F_j<0 for all j and b were a common original numerator, the homotopy source proves b_j>0 for all j after positive monic normalization. Thus `F dot b<0`, while it is a positive weighted sum of strictly positive actual-corner pairings. Contradiction. The x=1 pairing is b_7=1, and x=0 is actual zero frequency. Hence 2=>1; no real-algebraic transfer or solver status is required for this direction.

## 3. Any zero-annihilator has four distinct positive finite frequencies

Suppose K is a counterexample. The imported complete alternative gives positive atoms with total weight1, each an actual corner of K, whose weighted V sum is exactly zero. Combine all atoms at the SAME positive finite t by averaging their coefficients with their normalized positive weights. Convexity puts that average in K and affinity preserves its pairing vector. Merge zero and infinity analogously. Let the distinct positive finite frequencies be `t_1,...,t_m`, with positive merged weights and actual averaged members; let e0,eI indicate zero/infinity.

We prove only the lower bound needed here, `m>=4`, directly. If m<=3, put `q=2m+e0<=7` and

`R(s)=s^e0 product_(j=1..m)(s^2+t_j)`.

By real polynomial interpolation, a polynomial c of degree<q can match the corresponding actual denominator values at all conjugate pairs `+/-i sqrt(t_j)` and, if needed, match the actual positive constant at zero. The evaluation map is bijective: its real kernel would have q distinct roots and degree<q. If infinity is absent, take the test b=c. If infinity is present, take `b=c+s^(7-q)R`, preserving all finite values and giving leading coefficient1. With no finite node and only infinity, b=s^7 works. At each finite atom the pairing is `|a_j(i sqrt(t_j))|^2>0`, at zero it is a_0^2>0, and at infinity it is b_7=1. This contradicts annihilation. Therefore m>=4. The test is against an annihilator on ALL degree-at-most-seven b; it is not asserted to synthesize the entire box.

## 4. Strict outward enlargement puts zero in the INTERIOR of the actual pairing hull

Let K be the arbitrary counterexample from 1. As the predecessor proves using compactness of K and openness of the fixed-monic-degree Hurwitz set, choose a strictly outward rational superbox K' whose EVERY member is Hurwitz and every width is positive. Every old member of K, including every merged a_j, lies strictly inside **every coordinate interval** of K'. In particular a uniform small open interval of allowed changes of coefficients a_0 and a_1 exists for each of any four selected old members.

Choose four distinct positive finite atoms `t_1,...,t_4` from the merged zero certificate, with weights lambda_j>0. Write `c_j=lambda_j/(1+t_j)^7>0`. At node t_j independently alter only the selected actual denominator's a_0 by u_j and a_1 by v_j, keeping the same frequency and weight and leaving every other atom unchanged. These eight changes can be made arbitrarily small and independently because each chosen denominator is an interior member of the SAME independent box K'. The change in the sum F, in even and odd numerator-coefficient coordinates respectively, is

`Delta F_(2k)   = sum_(j=1..4) c_j (-1)^k t_j^k u_j`,
`Delta F_(2k+1) = sum_(j=1..4) c_j (-1)^k t_j^(k+1) v_j`, for k=0,1,2,3.

Both 4x4 matrices are invertible. Their determinants are a nonzero sign times `product_j c_j` times the Vandermonde `product_(p<q)(t_q-t_p)`; the odd block has the additional positive factor `product_j t_j`. The t_j are distinct and positive. Therefore for ANY sufficiently small target vector in R^8 there are unique u_j,v_j realizing it. In particular, choose a small epsilon>0 and solve the two systems with EVERY target coefficient equal to `-epsilon`. By scaling epsilon down, all eight actual coefficient changes remain inside K'; all perturbed denominators remain Hurwitz because every member of K' is Hurwitz.

The old weighted sum was zero, so the resulting positive weighted combination of actual K' pairing vectors is exactly `(-epsilon,...,-epsilon)`. In fact the full 8-dimensional parallelepiped of sufficiently small targets is attained, showing that zero is an INTERIOR point of the actual pairing convex hull of K'. This conclusion depends essentially on four DISTINCT positive nodes and the ability to vary a_0 and a_1 independently at each actual member; it does not assume independently invented E/O values or a common perturbation across different members.

## 5. Reduce the strict point to rational corner atoms

At each fixed x, the original even and odd interval choices fill a rectangle and the pairing coefficient vector is affine in those two values. Therefore every actual-member vector of K' is a convex combination of the FOUR actual corner vectors at that SAME x. Replacing the perturbed atoms by these corner combinations preserves F exactly, all weights nonnegative and total weight1.

The union of the four compactified corner curves is path-connected, because all curves share the actual monic infinity endpoint `e_7`. Apply the predecessor's proved path-connected support lemma to the strict point `(-epsilon,...,-epsilon)`: it has a convex representation with at most eight corner atoms. Remove zero weights. Every coordinate remains strictly negative; the selected x and weights at this stage may be real.

K' has rational endpoints. The coefficient polynomials `V_(i,j)(x)` are rational polynomials on `[0,1]`. Since there are only finitely many atoms and each F_j is strictly negative, choose rational x_k in `[0,1]` and positive rational weights summing to1 sufficiently close to the existing values to keep all eight strict inequalities. Endpoint frequencies 0 and1 are themselves rational; if r=1 its weight is1, and otherwise rationally approximate r-1 weights and take the remaining weight as 1 minus their sum. Strict positivity survives a sufficiently close choice. Thus the certificate in 2 exists, and every sum is an exact rational number.

At the resulting positive-width rational K', the strictly negative certificate and all-member Hurwitz condition persist under small endpoint perturbations by the full predecessor's explicit `4 delta` coefficient bound and the compact Hurwitz-neighborhood argument. This establishes the stated open family of negative boxes **conditional only on existence of the initial counterexample**, not a claim that all negative boxes themselves are interior points of that family.

## 6. Consequences, assumptions and outstanding task

The earlier positive-cone source had explicitly left open whether any failure yields a strict certificate. Sections 3–5 prove a sharper fact: after a strictly outward eligible rational enlargement, EVERY original failure does. Consequently a one-sided exact enumeration of rational positive-width boxes and <=8 rational-node/weight strict certificates is complete for finding a negative original witness, assuming the named source chain and classical root/interpolation facts. It need not terminate if universal synthesis is true, and no enumeration or scientific program was launched here.

The crucial new claims needing whole-scope independent review are: the zero-certificate actual-member caller; the `m>=4` interpolation boundary including zero/infinity; simultaneous a_0/a_1 perturbations at four distinct atoms inside ONE box; both Vandermonde determinants; the fixed-frequency four-corner convex hull; connected support reduction for the strict point; and rational approximation after strictness. This is WRITTEN candidate mathematics, not formal/kernel/human/configured-family verification or novelty clearance. No original counterexample, universal positive sign, negative-certificate sample, numerical optimum or QE outcome is claimed. Prior STOP/HOLD/ZERO and process histories remain recorded and are not proof premises.

**END.**
