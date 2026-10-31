# Septic SPR7 counterexamples have an all-integer finite-frequency normal form

Owner **InfoSPR7-2**, slot info-2. Actual preceding `/bin/date`: **Wed Oct 28 18:14:34 PDT 2026**. **WRITTEN author-unreviewed candidate.** This is an exact normal-form consequence, not an exhibited integer box, an executed enumeration, or an answer to the synthesis question.

## 1. Exact theorem

Import the COMPLETE `frontier-20261028-eight-finite-frequency-integer-weight-certificate-v1.md`, SHA256 `ebbb9c9c848a854783fae0d2a8a53f66947a99ed14a447711c44cb93cc4a9f63`, including its entire named d9/eight-atom/rational-superbox/positive-numerator predecessor chain. Its result and those dependencies remain unreviewed candidates.

The original registered monic septic question has a counterexample **if and only if** there exist:

1. an actual independent monic septic coefficient box K whose fourteen lower/upper endpoints are **strictly positive integers**, each lower endpoint is strictly less than its upper endpoint, and EVERY member of K is Hurwitz;
2. exactly eight distinct strictly positive **integer** frequencies `w_1,...,w_8`;
3. eight indices i_l choosing the FOUR actual parity corners of that ONE K, with repeated indices allowed;
4. eight strictly positive integer weights `N_l`;

such that for each k=0,...,7 the integer

`C_k = sum_(l=1..8) N_l * sum_(0<=j<=7; j+k even)`
`             [ (-1)^((k-j)/2) a_(i_l,j) w_l^(j+k) ]`

is strictly negative. Here a_(i,7)=1, the a_(i,j) are actual integer corner coefficients, and the exponent `(k-j)/2` is an integer. This is an exact coefficientwise obstruction to the SAME unrestricted b; no finite search or existence assertion is made.

The endpoint integers are positive because every monic real Hurwitz polynomial has strictly positive coefficients, in particular the actual all-lower corner of an eligible box. The theorem does NOT say that the final integer box contains the unscaled original box; it is obtained after a positive change of frequency units.

## 2. Positive time scaling preserves the literal SPR7 problem

For any D>0 define, for EVERY degree-at-most-seven real polynomial p,

`(S_D p)(s) := D^7 p(s/D)`.

If p is monic of exact degree7 then so is S_D p, and its roots are exactly D times those of p. Hence S_D preserves and reflects strict Hurwitz stability. It maps an independent coefficient box K bijectively onto the independent monic box whose jth endpoint is multiplied by `D^(7-j)`, j=0,...,6.

For any a,b and real w,

`(S_D b)(i D w)/(S_D a)(i D w) = b(iw)/a(iw)`.

The map b->S_D b is an invertible bijection on real exact-degree-seven polynomials, and w->D w covers ALL finite real frequencies including zero. Thus K has an original common numerator **iff** S_D K has one. This is a change of units, not a sampled-frequency or numerator-profile restriction.

## 3. Clearing both endpoint and frequency denominators

If any original counterexample exists, the complete imported predecessor supplies one with rational positive-width endpoints, eight distinct positive rational w_l, positive INTEGER weights N_l, actual corner indices and all eight strict C_k<0. Choose a positive integer D divisible by the denominators of every one of the fourteen endpoints and all eight frequencies.

Each transformed endpoint is the old rational endpoint times `D^(7-j)`. Since j<=6, this exponent is at least1; because D is divisible by the endpoint denominator, every transformed endpoint is an integer. All widths remain strictly positive. Each transformed frequency `W_l=D w_l` is a distinct positive integer. The corner endpoint-selection pattern is unchanged because D^(7-j)>0, and the transformed chosen corners are actual corners of S_D K. All members remain Hurwitz by §2.

For a monomial s^k, the transformed raw pairing coefficient at W_l is

`Re[(i D w_l)^k (S_D a_i)(-i D w_l)]`
`= D^(7+k) Re[(i w_l)^k a_i(-i w_l)]`.

The SAME original positive integer weights N_l therefore give `C'_k=D^(7+k) C_k<0` for every k. Since the transformed corner coefficients, W_l and N_l are integers, every C'_k is an integer and hence at most -1. This establishes the all-integer normal form without any arithmetic approximation or unproved denominator bound.

## 4. Converse and search boundary

Conversely, given such an eligible integer box and eight integer atoms, the predecessor's positive-numerator/homogeneous pairing argument immediately shows that no original common numerator exists: after positive monic normalization all b_k>0, so the strict integer vector gives `sum_k C_k b_k<0`, whereas each positive-weight actual-corner pairing must be positive. All frequencies are finite and nonzero; the original literal zero-frequency condition and exact degree are not weakened by using these atoms in a contradiction.

In principle one can enumerate positive-integer endpoint tuples with strict widths, eight distinct positive-integer frequencies, corner-index words, and positive-integer weights; check the eight negative integer sums and check the whole box's Hurwitz eligibility using the predecessor's exact rational Routh/Sturm procedure. Under the named source chain, that one-sided search is complete for a negative original answer. There is no claimed bound on integer magnitudes, no claim of termination if synthesis is universally true, and no search, numeric example, solver or quantifier-elimination execution in this paper.

## 5. Assurance

The proof is WRITTEN and elementary conditional on the full cited chain. It needs independent source/whole-proof review, especially the d9 strict-interior perturbation, connected support reduction, numerator positivity, Routh/Sturm box predicate, and this positive scaling. It does not establish original feasibility, a concrete counterexample, novelty, formal/kernel/human/configured-family review, or process-history clearance. Historical findings/STOP/HOLD/ZERO remain recorded and are not proof premises.

**END.**
