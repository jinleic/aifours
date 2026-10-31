# A projected-odd-run selector with two arbitrary rotation values

Owner **MathOlson-2-2**. Native `/bin/date` immediately before writing: **Wed Oct 28 20:28:55 PDT 2026**. A NEW **WRITTEN sufficient-condition candidate**, with bounded checks in §5. It is NOT a repaired actual-block lift, full L_RES result, independently reviewed theorem, formal proof or novelty claim.

Before reviewing this source read `frontier-20261028-olson-actual-block-fatal-correction-v1.json`, SHA256 `e11fd87345f8a54012f3a9245d87491c6ceb3a4a113558be07ca4ab62728f90e`. The earlier f111 disposition and all its actual-block/profile/floor consumers remain withdrawn/held; no assessment is transferred.

## 1. The actual selector criterion

Let p be any odd prime and W an ACTUAL `D_(2p)` word with exactly F=3p−2 reflection occurrences and arbitrary rotations. DELETE rotations only to define its cyclic reflection-only projection. Suppose that projection has exactly p odd maximal constant runs, with **pairwise distinct** reflection exponents. It may also have even projected runs.

Suppose the ACTUAL cyclic full word contains four consecutive occurrences

`σ_c · ρ_u · σ_c · ρ_v`,  (1)

whose two σ_c occurrences lie in the SAME ODD projected run. The rotation values u,v are arbitrary, including0 and including u!=v. Then W has an original-order identity subsequence of exactly2p actual occurrences.

This is a sufficient condition on explicitly PROJECTION data and an actual four-letter block; it says nothing about historical occupied-gap `o_F/e_F` values, any OLD/IPGEN/DS3 caller, or whether (1) exists in all words.

## 2. A directed-difference fact

In ANY linear ordering `x_1,...,x_p` of all elements of F_p, and for ANY nonzero t, there exist `i<j` with `x_i−x_j=t`. Otherwise, for every field value x, x−t must occur BEFORE x. The relations `position(x−t)<position(x)` follow around the full additive t-cycle and yield a strict inequality chain returning to the starting position, impossible. This uses primality only to make nonzero t generate all F_p.

## 3. Construct an exact original-order selector

Cut the ACTUAL cyclic word immediately before (1). The four-letter block is first and has product

`σ_c ρ_u σ_c ρ_v = ρ_(v−u)`.

The projection initially has `H_π=(3p−2−p)/2=p−1` equal-reflection pairs. Removing the two σ_c occurrences from their odd projected run leaves that run odd and nonempty, and lowers the available pair count by exactly one: `H'_π=p−2`.

In the linear cut order, the residual portion of that projected run may occur at BOTH ends. Its two piece lengths have odd total, so their floor-half-lengths sum to the floor-half-length of the total. Thus these actual cut-order segments still provide all p−2 pairs; no same-run pairing is assumed to cross the selected block. Reserve one actual unpaired representative from every odd projected run. Their p values remain distinct and therefore list the whole F_p in some cut order. Projected even runs can supply pairs but no reserved odd representative.

If u=v, select all p−2 equal pairs after block (1). If u!=v, use §2 to choose two reserved odd representatives in their ACTUAL cut order whose reflection product has exponent `u−v`, and select ANY p−3 of the p−2 equal pairs, disjoint from those representatives. In either case the remaining selected reflections number `2p−4` and have rotation product `ρ_(u−v)`; each chosen equal pair is an identity subproduct in its actual order.

Together with block (1) this gives exactly `4+(2p−4)=2p` ACTUAL occurrences and product `ρ_(v−u)ρ_(u−v)=1`. Returning the same positions to increasing original word order cyclically rotates an identity product, which remains identity. QED.

This criterion and the earlier equal-rotation criterion are **incomparable as stated**: the latter does not require distinct odd-run values, while this one permits u!=v but requires them.

## 4. Scope and remaining gap

For a REF-failing word with p odd projected runs, the separate projection-only candidate `frontier-20261028-olson-projected-odd-ap-characterization-v1.md`, SHA256 `3901cf26d02df93f4892a5403b991584003c0c33677f41241cc20a68f85702eb`, proposes the stronger necessity that those labels are an affine AP; this paper does not rely on that candidate, only on its OWN explicit distinctness hypothesis.

This theorem does not prove that every original residual has p odd projected runs, distinct odd-run values or an actual block (1). It does not establish any OLD/SEL/IPGEN/GS/DS3 failure, L_RES universal implication, counterexample, or novelty. The AP/e0 family has such a block, but its complete residual membership remains a separate unresolved question.

## 5. Exact bounded original-word checks

`frontier-20261028-olson-projection-fourblock-experiment.py`, SHA256 `73bc8d648acff74de0ec692d518ad1b3de11e00cb0a2606aefb2ca961f42386e`, generated 500 full actual words at p=3,5,7,11,13, with zero or one EVEN projected run and arbitrary values for the two block rotations. Saved `frontier-20261028-olson-projection-fourblock-results.json` has SHA256 `5221e84b9d31a6b138a12e4e3e79b43b0b71f9860a8b93843fbb636a14267db9`.

Separately written `frontier-20261028-olson-projection-fourblock-checker.py`, SHA256 `230ccb2ed473f3e91b9248c7d0c289552049a5a690907e8ffbefd11ab578b60b`, imported no producer and returned `PASS_INDEPENDENT_ARBITRARY_FOURBLOCK` in `frontier-20261028-olson-projection-fourblock-check-results.json`, SHA256 `c57e831e006beeede91e09560d8a90735ccf5303111b72951fa46054c8b244bc`. It independently reconstructed the cyclic projected odd/even runs, checked the ACTUAL cyclic four-letter positions and separate cut-order remainder, and directly multiplied all 500 original-index products. Branches were 225 nonzero-target/eπ0, 221 nonzero/eπ1, 25 zero/eπ0 and 29 zero/eπ1; duplicate-index and false-target controls were rejected for their intended reasons.

Those finite checks do not establish the universal proof or independently review it. No f111, human, cross-family, formal or novelty claim is transferred; a NEW disjoint complete review is required.

**END — actual four-block with arbitrary rotation values, projection-only premise.**
