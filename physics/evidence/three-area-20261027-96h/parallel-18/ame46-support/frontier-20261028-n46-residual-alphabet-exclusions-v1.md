# Partial N=46 residual-alphabet exclusions for AME(4,6)

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 19:22:26 PDT 2026`; not an exact completion time. **WRITTEN author candidates**, not independently accepted, formally verified, or novelty-cleared. This is not a proof that N=46 is impossible.

The conditional reduction to the remaining case uses the global lower-46 candidate `frontier-20261028-global-ame46-support-lower46-v1.md`, SHA-256 `36586d04dd9e6cdc2bdf11e1bfcb2f85c07890cbf902386fef264260876b73eb`, the global t≤29 candidate `frontier-20261028-global-ame46-maximal-coefficients29-v1.md`, SHA-256 `2520967103592e125423a5a22c0ed5e86236582f149fb9375cb0c6f2070b476c`, and their pinned dependencies. All remain under review. The only inherited named classical import is no-OLS(6).

## 1. Remaining 46-support case and candidate exclusions

Let P be the t entries of modulus 1/6 and E the other support. Assuming the pinned earlier candidates, an AME(4,6) state with N=46 can only have

`t=26`, `n=36−t=10`, `|E|=20`.                                      (1)

Indeed t≤29 and `N≥72−t` give t=26,27,28,29. The cases t=27 and 28 give one-excess and even two-excess residual supports. The case t=29 gives a 7×7 residual unitary with 17=`2n+3` entries; the sharp three-excess lemma makes every pair-projection multiplicity at most three, and the alphabet/active-count argument of the lower-46 packet applies without using |E|=16: any 4-valued residual coordinate has four fibers of at least four points, none can be constant on another coordinate without a pair of multiplicity ≥4, so each pair projection has at least eight values, not n=7. All residual alphabets are then size 3, and the active-coordinate count is `32>29`, contradiction.

In case (1), each of the six residual pair projections has ten values, each with exactly two E extensions. Every residual-coordinate fiber varies in at least two other coordinates and hence contains at least four E points. Thus every local residual alphabet size lies between 2 and `floor(20/4)=5`, and every pair of alphabet sizes has product at least 10. Up to party order there are exactly ten possibilities:

`(2,5,5,5)`, `(3,4,4,4)`, `(3,4,4,5)`, `(3,4,5,5)`, `(3,5,5,5)`,
`(4,4,4,4)`, `(4,4,4,5)`, `(4,4,5,5)`, `(4,5,5,5)`, `(5,5,5,5)`.

The written arguments below exclude four: `(2,5,5,5)`, `(3,4,4,4)`, `(3,5,5,5)`, and `(5,5,5,5)`. The other six are **not resolved** here.

## 2. P-code counting and the (3,4,4,4) profile

Call a coordinate of a P word active if its symbol occurs in the E alphabet. For sizes r_i, P and E partition the 36 values of every pair projection, so the number of P words active at i is `6r_i−10`, and active at both i,j is `r_i r_j−10`. If k(x) is the active-coordinate count of P word x, then

`Σ_x k(x)=Σ_i(6r_i−10)`, `Σ_x C(k(x),2)=Σ_{i<j}(r_i r_j−10)`.  (2)

Also `1−k+C(k,2)` has values `1,0,0,1,3` for k=0,1,2,3,4.

For `(3,4,4,4)`, the right sides in (2) are 50 and 24. Consequently

`Σ_x [k(x)−C(k(x),2)]=26=|P|`.

Since each summand is at most 1, every P word has k=1 or 2. At a size-4 party, the total number of P words active there is 14, and the sum of P pair-active counts with its three partners is `(4·3−10)+2(4·4−10)=14`. Because no P word has more than two active coordinates, there are **zero** P words active only at that party.

For an active symbol a at that party, let `d(a)` be its number of E-partner values at any one other party. This number is independent of the partner: the same number `6−d(a)` of P words use a, and their partner symbols are distinct. The number of P words active only at that party with symbol a is

`(6−d(a))−[(3−d(a))+(4−d(a))+(4−d(a))] = 2d(a)−5`.

It must be zero, but 2d(a)−5 cannot vanish for integral d(a). Contradiction.

## 3. A separate counting exclusion for (2,5,5,5)

For `(2,5,5,5)`, (2) gives total active and pair-active incidences 62 and 45, so

`Σ_x [1−k(x)+C(k(x),2)] = 26−(62−45)=9`.                      (3)

Writing n_j for the number of P words with k=j, (3) is `n_0+n_3+3n_4=9`.

Each size-5 party has five E fibers, each of size at least four; |E|=20 makes every fiber size four. Since every pair projection value has exactly two E extensions, every symbol at such a party has residual partner degree d=2 toward every other party. For each active symbol a at a size-5 party there are `6−2=4` P words using a, but their number of incidences with other active parties is `(2−2)+(5−2)+(5−2)=6`. Hence these four words contribute 2 to `Σ(k−2)`.

Summing over the 15 active symbols of the three size-5 parties gives 30. A triple-active P word contributes at most 3 to that sum, a four-active word contributes 6, a two-active word contributes 0, and a one-active word contributes at most 0. Thus the sum is at most

`3n_3+6n_4 ≤ 3(n_0+n_3+3n_4)=27`,

contradiction. This proof is independent of the parity argument below.

## 4. Five-fiber rectangle parity

Suppose a size-5 party A is present. Its five E fibers all have four points. For each other coordinate, the two-extension property makes it use two values in every A fiber, each twice. Thus any pair j,k of the other coordinates is either full on the 2×2 product in a fiber (four values once) or correlated (two values twice), and a fiber is correlated on at most one of the three pairs.

For a pair j,k, global pair multiplicities are exactly two, so over F₂ the indicator matrices of the **full** fiber rectangles sum to zero. The full-fiber set cannot be empty: otherwise the third coordinate is fiberwise free over a two-set, and the fiberwise-free completion lemma in the global lower-45 packet selects 10 E words to complete the 26 P words to an OA(36,4,6,2), contradicting no-OLS(6). That proof works verbatim with 10 residual words instead of 8.

Now assume j and k both have size 5. Their A-to-j and A-to-k incidence graphs are 2-regular on 5+5 vertices. Such a graph is either one 10-cycle or the disjoint union of a 4-cycle and a 6-cycle. Its 5×5 F₂ incidence matrix has rank respectively 4 or 3. Every selection of four A-fiber rows has rank at least 3: deleting an edge from a 5-cycle leaves a 4-edge path, and deleting one edge from the 4+6 configuration leaves rank 3. No row set is repeated three times, since each symbol occurs in exactly two A fibers.

A nonempty zero-XOR set of full rectangles cannot have size 1. It cannot have size 3: a zero sum of three nonzero rank-one tensors would force three equal row sets on one side. It cannot have size 4, since the two selected four-row incidence matrices each have rank at least 3 and their product has rank at least `3+3−4=2`. It cannot have size 5, since the full ranks are at least 3 and the product has rank at least `3+3−5=1`. Thus it has size 2; equality of two nonzero rank-one rectangles forces the two A fibers to have equal j sets **and** equal k sets. Both 2-regular graphs therefore have a common isolated 4-cycle on the same A-fiber pair, disjoint from the other three A fibers and from the other three local symbols on each side.

## 5. Three or four size-5 alphabets

For `(3,5,5,5)` or `(2,5,5,5)`, choose A and two other size-5 parties C,D; the fourth party B has dimension at most 3. By §4 the C,D full-fiber set is a common isolated A-fiber pair. Those two fibers contain eight E points and use two local values each at A,C,D, disjoint from the remaining fibers' A,C,D values. In each cut involving a pair among A,C,D, the four pair rows belonging to this group receive no E entries from the other group, and P cannot share an E pair row. The full residual unitary therefore makes those four group rows orthonormal. After normalizing the group state, all three two-qubit marginals on A,C,D are `I_4/4`.

A three-qubit 2-uniform mixed state has rank at least four: its Pauli expansion contains only identity and weight-3 terms, so spin flip gives `ρ̃=I_8/4−ρ≥0`. All eigenvalues are at most 1/4 and the trace is one. But the group state would purify this marginal with a fourth subsystem B of dimension at most three, contradiction. Thus `(3,5,5,5)` and again `(2,5,5,5)` are impossible.

For `(5,5,5,5)`, choose A of size 5. Section 4 applies to every pair among the other three parties: each nonempty full-fiber set is the unique duplicated A-fiber pair common to those two 2-regular graphs. Since every pair has such a set, all three graphs have the same duplicated pair. The other three A fibers are therefore correlated on **all three** pairs, contrary to the at-most-one-correlation fact at the start of §4. This profile is impossible.

## 6. Controls and exact remaining gap

`frontier-20261028-n10-active-profile-controls-v1.py`, SHA-256 `e3b6a4a009419c0d2af4472824fae2c28be39a685113db34b4a26a8f5fb10a06`; receipt SHA-256 `30f91c79c5d5fe4e7ce7f6c3c0acc15d6de2921b614ad6832d81e37a9288ea17`, checks the ten alphabet profiles and the exact counting arithmetic for the two exclusions in §§2–3.

`frontier-20261028-ten-residual-fivefiber-controls-v1.py`, SHA-256 `1055bfc43df92ca947231f51d71b636652fcae1c6f8687babca69034195fea33`; receipt SHA-256 `e01846811b3be6a4e6602ff1b0719bc5412031a16e60a82b0bff97c3a501f7d1`, enumerates all 2,040 labeled 5×5 2-regular incidence graphs: 600 have F₂ rank 3, 1,440 rank 4, all 10,200 four-row selections have rank at least 3, and the duplicate-row pairs split into the stated 4+6 components. These are finite controls for the written proof, not independent scientific review.

The six unresolved profiles are `(3,4,4,5)`, `(3,4,5,5)`, `(4,4,4,4)`, `(4,4,4,5)`, `(4,4,5,5)`, `(4,5,5,5)`. No contradiction for them or global lower bound 47 is claimed.
