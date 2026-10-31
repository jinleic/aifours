# Nested conditional-iid copy blocks

## Required source order

Read the historical LP erratum `frontier-20261028-full-source-lp-optimum-v1-erratum-1.md` first (SHA-256 `c64e2a1a3a78d1d71f76d9f04903408e619168945b959d787b06938f8ba6ded9`), then the graph/game/source contract in `frontier-20261029-upper-bound-review-input-v1.md` (SHA-256 `e8c46fc195dd22ebcd28e485587a9872582a99ed89b25ce8d2e2ba4cee9e505a`). The correction is Remark 5.4 for the publisher's omitted cross-branch rows. No held review is an input.

**Status: WRITTEN.** This extends the elementary kernel argument of `frontier-20261029-exchangeable-copy-compression-v1.md` from one repeated block with an optional last copy to any finite ordered list of blocks. No new guessing-number bound is asserted here.

## Construction and proof

Let O be the original finite random-variable tuple. For block a choose an original variable X_v(a), an original conditioning subset T(a) excluding it, and a positive count k(a). Let P(a) be the tuple of ALL copies in every earlier block.

Conditionally on the existing law of (O,P(a)), sample k(a) new copies independently from the kernel

K_a(x | T(a),P(a)) = P(X_v(a)=x | T(a),P(a)).

They are independent of the entire previous law given (T(a),P(a)). Each ordered copy step within block a is an ordinary copy step: previously created copies of that same block are independent of X_v(a) given (T(a),P(a)), so including them in the over-set leaves the old variable's conditional law unchanged.

Inductively the full law is invariant under permutations inside EACH completed block:

1. Within the newly sampled block, the conditional distribution is a product of identical kernels, hence is permutation-invariant.
2. A permutation of an earlier block leaves the old joint law invariant. Because the conditioning tuple includes all variables of that block, the joint numerator and marginal denominator defining K_a transform identically. Therefore K_a is invariant under that permutation on every positive-probability conditioning fiber.
3. Thus adjoining the new block preserves every earlier block's permutation symmetry.

Kernels on null fibers do not affect the joint law. This proves the induction for every finite list of blocks and every original law. The construction deliberately does NOT cover a later step that uses only selected members of an earlier block.

## Exact entropy quotient

An entropy coordinate is h(U,r1,...,rd), where U is an original-variable subset and 0<=ra<=k(a) is the count of selected copies in block a. It is well-defined by the independent within-block permutations. Coordinates number 2^10 times product_a(k(a)+1), minus one.

The full elemental Shannon system has four CMI types: two originals; one original and one copy; copies from distinct blocks; and two copies from the same block, together with the full-set conditional entropy rows. Each type is generated for every original conditioning subset and every permissible vector of copy counts. These cases exhaust all individual-variable elemental rows under the permutation quotient.

For block a's copy marginal, let q_b range through 0..k(b) for b<a, let q_a range through 0..k(a)-1, and let q_b=0 for b>a. For every U subset of T(a), the quotient row is

h(U,q+e_a) = h(U+X_v(a),q).

For the independence row, instead take q_b=k(b) for every b<a, q_a=r, q_b=0 for b>a. It is

h(O,q+e_a)+h(T(a),q)-h(O,q)-h(T(a),q+e_a)=0.

The first family includes every marginal-copy subset of the previous blocks; the second is the ordinary ordered-step conditional independence. All equalities are valid by the kernel construction. The ordinary graph FD/cap/symmetry contract is unchanged, and unrelated branches still share ONLY original coordinates.

## Implementation boundary

`frontier-20261029-nested-copy-block-lp-v1.py` implements the quotient. Scientific adoption requires the written validity argument above plus an exact certificate and independent row reconstruction. A floating optimum is only a proposal. No formalization, external review or novelty clearance is claimed.
