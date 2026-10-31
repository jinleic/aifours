# Original septic SPR synthesis reduces exactly to rational boxes and rational numerators

Owner **InfoSPR7-2**, slot info-2. Actual `/bin/date` observation immediately before this write: **Wed Oct 28 17:46:36 PDT 2026**. **WRITTEN candidate, author-unreviewed.** This is an original-target-preserving representation theorem and a finite decision predicate for each candidate numerator, not a solution of the universal question or a claim of novelty.

## 1. Original target and exact equivalence

Use only the registered original monic septic definition in `institute/runs/three-area-2026-10-27-96h/written-releases/info-2-septic-box-definitions-v1.md`, SHA256 `d86737954bee95836e2d2cffade9cba15a99f2bb486b660ada2562c25fc764ad`, and packet SHA256 `9df2b558c03b2aac8cefb786be5a2a0802de822724bcd6ee60b47d0205fc61f6`. Write

`K(l,u)={s^7+sum_(j=0..6)a_j s^j : l_j<=a_j<=u_j}`,

with finite real endpoints, possibly degenerate intervals, and require every member to be strictly Hurwitz. An original witness is ONE fixed real polynomial b of **exact degree seven** such that `Re[b(iw)/a(iw)]>0` for EVERY `a in K` and every finite real w, including zero.

**Theorem.** The following are equivalent.

1. Every eligible original real-endpoint K, including degenerate boxes, has an original witness.
2. Every eligible K with **rational endpoints and all seven widths strictly positive** has a **monic rational-coefficient** witness.
3. Every eligible K with rational endpoints and seven positive widths satisfies the explicit finite-predicate/existential-rational-numerator statement in §5.

Moreover, if ANY original real box is a counterexample, some eligible rational box with seven strictly positive widths is a counterexample. For each fixed original eligible box, if a real witness exists then a monic rational witness exists. Neither statement supplies such a counterexample or a universal construction.

These reductions preserve the original shared numerator and every denominator/frequency; no reciprocal, profile, selected-node or smaller-degree restriction is imported. The ordinary named facts are: openness of the Hurwitz condition for fixed monic degree, continuity of polynomial roots, rational density, the intermediate value theorem, and the classical exact Sturm root-count/isolation theorem for rational univariate polynomials. Where used, their required hypotheses are given below. No source-paper proof or old held guide is imported.

## 2. Any counterexample has a rational positive-width superbox

The coefficient space is R^7 with the sup norm. Let H be the set of coefficient vectors for which the corresponding real monic septic is Hurwitz. H is open: continuous dependence of the multiset of roots on polynomial coefficients implies that sufficiently small coefficient perturbations retain all seven roots in the open left half-plane. K is compact, lies inside H, and has strictly positive distance from the closed complement of H. Indeed, otherwise vectors outside H could approach K; compactness would yield a subsequential limit in K, contradicting openness of H.

Choose `eta>0` so every vector within sup distance eta of K is in H. For each j choose rationals `l'_j<l_j` and `u'_j>u_j` with both outward displacements less than eta. Rational density permits this also when `l_j=u_j`. Any coefficient vector in K(l',u') clips coordinatewise to a vector in K at sup distance less than eta. Thus the **entire** rational superbox K(l',u') is strictly Hurwitz and all seven widths are positive.

If b were a single original common numerator for K(l',u'), it would be one for K, since K is a subset. Therefore absence of an unrestricted exact-degree-seven witness propagates to this actual eligible rational superbox. This proves the stated counterexample reduction and the implication 2=>1, without assuming counterexamples themselves form an open set or selecting a previously constructed box.

## 3. For any fixed eligible K, a witness can be rational and monic

Suppose a real exact-degree-seven b is a common witness. For every monic a, `b(iw)/a(iw)` tends to the real number b_7 as `|w|` tends to infinity. Since all finite-frequency real parts are strictly positive, b_7 cannot be negative; exact degree gives b_7 !=0, so **b_7>0**. Positive rescaling preserves every sign, and we henceforth take b_7=1.

For t=w^2 define `P_(a,b)(t)=Re[b(i sqrt(t)) a(-i sqrt(t))]`. Since a is Hurwitz, `|a(iw)|^2>0`, so the original inequality is precisely `P_(a,b)(t)>0` for all t>=0. Put `x=t/(1+t)` and

`Q(a,b,x)=(1-x)^7 P_(a,b)(x/(1-x))`, `0<=x<1`.

This extends polynomially and continuously to x=1, where its value is `a_7 b_7=1`. For every actual a the value is strictly positive on `[0,1]`; continuity on the compact product K x `[0,1]` gives a single `mu>0` with

`P_(a,b)(t) >= mu(1+t)^7` for every actual a and every t>=0.

Let `S=max_(a in K) sum_(j=0..7)|a_j|`, which is finite and at least1. For any other monic numerator b' with `|b'_j-b_j|<=epsilon` for j=0,...,6,

`|P_(a,b')-P_(a,b)|/(1+t)^7 <= 7 epsilon S`.

Indeed for j<=7, `|w|^j <= (1+w^2)^(7/2)`, so this follows from the coefficient L1 bound on `b'-b` and on a. Choose rational b'_0,...,b'_6 within `epsilon<mu/(7S)` of the real coefficients; keep b'_7=1. Then EVERY pairing remains strictly positive on the full half-line and b' is monic rational, exact degree seven. This proves 1=>2 and applies even when K has real endpoints or degenerate widths.

The compactified endpoint x=1 is used only to get a uniform margin; the literal original condition remains strict at every FINITE frequency. It is legitimate here because the original numerator has exact degree seven and positive leading coefficient. No claim is made for lower-degree numerator variants.

## 4. Exact four-actual-corner test for a fixed numerator

For `a(i sqrt(t))=E_a(t)+i sqrt(t) O_a(t)` and t>0, independence of the even and odd coefficient intervals gives the full value rectangle

`E_-<=E_a<=E_+`, `O_-<=O_a<=O_+`,

where

`E_- = l_0-u_2 t+l_4 t^2-u_6 t^3`,
`E_+ = u_0-l_2 t+u_4 t^2-l_6 t^3`,
`O_- = l_1-u_3 t+l_5 t^2-t^3`,
`O_+ = u_1-l_3 t+u_5 t^2-t^3`.

Every combination of one E endpoint and one O endpoint is attained by one of FOUR fixed actual coefficient corners: choose the displayed alternating lower/upper endpoints for even and odd coefficients independently. These corners do not depend on t>0. At t=0 the same assertion remains valid: all terms with positive powers vanish and the odd contribution to the pairing vanishes.

For fixed b, `P_(a,b)(t)=E_b(t) E_a(t)+t O_b(t) O_a(t)` is affine in the rectangle coordinates. Its minimum is at a rectangle corner. Thus

`P_(a,b)(t)>0 for every a in K and every t>=0`

is **equivalent** to `P_(a_i,b)(t)>0` for all four actual corners a_i and all t>=0. The same b is used for all four and all frequencies. This does not assert that the seven-dimensional coefficient box is the convex hull of four coefficient vectors.

## 5. Rational K, rational b: a finite exact predicate

Fix rational K and monic rational b. Every P_i(t)=P_(a_i,b)(t) is a rational polynomial of degree exactly seven, with leading coefficient1. For each i the whole-half-line strictness condition is equivalent to BOTH

`P_i(0)>0` and `P_i has no positive real zero`.

Necessity is immediate. For sufficiency, continuity and the intermediate value theorem prevent a sign change on `(0,infinity)` without a zero. A positive real zero of even multiplicity is also forbidden, so **distinct-root counting must not discard it**. Compute the square-free part `P_i/gcd(P_i,P_i')`, then use a rational Sturm sequence to count its distinct roots on `(0,infinity)`; a count of zero, together with P_i(0)>0, is the required exact test. These are finitely many exact rational operations and sign comparisons. No numerical root approximation is assumed as an answer, and no claimed execution is involved.

Eligibility of a rational K is also decidable by a finite exact predicate, without importing an interval-stability theorem. First check one actual rational corner using the ordinary Routh–Hurwitz criterion for a real monic polynomial. A monic Hurwitz polynomial has positive constant coefficient: conjugate root pairs and negative real roots give positive constant factors. If the chosen corner fails, K is ineligible. If it passes, t=0 has an imaginary-axis zero in K exactly when `l_0<=0<=u_0`.

For t>0, an actual a in K has a zero at `i sqrt(t)` **if and only if**

`E_-(t)<=0<=E_+(t)` AND `O_-(t)<=0<=O_+(t)`.

The forward direction is immediate; the reverse uses the independently attainable even/odd value intervals. For rational endpoints these are four rational cubics. To decide whether the displayed inequalities hold somewhere on `(0,infinity)`, isolate all distinct positive zeros of their nonzero product by rational Sturm calculations, inspect the signs on each resulting open interval, and separately inspect each isolated root. At a root, an individual cubic vanishes there exactly when its gcd with the square-free product has a root in that isolating interval; otherwise its sign is constant on that interval and is read at a rational point. This also handles shared and repeated roots and inclusive endpoint signs. If a factor were identically zero, treat it as zero in this sign partition; the other factors suffice. This is a finite exact semialgebraic sign test.

If the chosen corner is Hurwitz and NO member of K has an imaginary-axis zero, every member is Hurwitz: the straight segment from the corner to any member stays inside the convex box, and the number of roots in the right half-plane cannot change along that monic fixed-degree segment without an imaginary-axis crossing. Conversely an all-Hurwitz K necessarily passes both tests. Thus the eligibility predicate is exact, including tangencies, repeated boundary roots, zero frequency and degenerate widths.

Combining these two predicates, statement 3 is: **for every rational l,u with l_j<u_j and with the above finite eligibility predicate true, there exist rational b_0,...,b_6 such that all four finite Sturm strict-positivity tests pass.** Sections 2–4 prove this is equivalent to the registered original target.

## 6. Computability interpretation and remaining gap

Enumerate all rational endpoint boxes and monic rational numerators. The eligibility predicate and each fixed-numerator predicate above terminate by the stated classical Sturm and Routh procedures. Therefore the full universal septic question has an explicit `forall rational box, exists rational numerator` form with a decidable inner relation. This is a representation in the arithmetical `Pi^0_2` class, not a proof of completeness, undecidability, an effective bound on numerator search, or termination of a search for a negative box. A failed finite enumeration, even over every numerator tried so far, cannot certify that a rational box is a counterexample. The original unrestricted SPR7 question remains OPEN.

This proof is conventional written mathematics; no numerical instance, scientific interpreter, program, solver, finite enumeration, or exact identity replay was used for the theorem. The separate previously reported b9 open-family candidate and the functional-dual gap do not serve as assumptions. The argument requires its own whole proof review and source-bound reconstruction; no formal/kernel/human/configured-family acceptance, current literature status or novelty is claimed. Historical STOP/HOLD/ZERO records are not reclassified or used as premises.

**END.**
