# Nonpositive entropy gap for every two-syndrome q=8 FD law

**Status: WRITTEN with an independently checked exact rational Shannon certificate and finite bit-gadget checks; scientific review pending.** In the fixed ten-triangle q=8 bit encoding of R-minus, every original-neighbour FD law whose syndrome vector takes at most **two** values obeys

\[
\Delta(X)=H(X_V)-\frac23\sum_{i=1}^{10}H(X_i)\le0.\tag{25}
\]

Probabilities and correlations are arbitrary; the support need not be uniform or maximal. In particular, such an FD support has at most `2^20` words. Therefore a strict-gap q=8 law, if one exists, requires at least **three distinct syndrome values**. This is not an unrestricted-q guessing-number bound, a positive witness, or a result for three or more syndromes. The noncover branch uses the pinned proper-subgraph inequality `frontier-20261028-conditioned-proper-subgraph-inequality-v1.md` SHA-256 `c46831b9324e7e8c65009c2a27f3391db7705c370bfb63435a73b0117be3df49`, whose scientific review is also pending.

## 1. The all-factor common-syndrome lemma

Suppose each of the ten listed triangle-bit parities equals the same bit `S`. Let `X_i` be the three bits at vertex `i`, and assume the original graph FDs. Then (25) holds.

For every triangle `T`, `S` is determined by `X_T`. For every vertex `i`, choose a triangle containing `i`; its other two vertices are neighbours of `i`, and `X_i` itself is determined by all original neighbours, so `S` is also determined by `X_{N(i)}`. In addition `H(X_i|X_{N(i)},S)=0`.

Condition on `S`. In each triangle any two bits determine the third, including on each conditional law after revealing earlier factor tuples. The three pairwise subadditivity inequalities give `3H(Z_t|S,Z_<t)<=2 sum_{i in T_t} H(X_i^t|S,Z_<t)`. Summing over the ten factors and using conditioning monotonicity yields

\[
3H(X_V|S)\le2\sum_iH(X_i|S).
\]

As `S` is determined by `X_V`, this is exactly the nonpositive gate

\[
G=3H(X_V)+17H(S)-2\sum_i H(X_i,S)\le0.\tag{26}
\]

`frontier-20261028-two-syndrome-all-factor-dual-v1.json` SHA-256 `a8f6822f2c3e3a8e0b0fd639a9b0095a8ea6f38c7833f0ef2fb6551fa9bba087` is an exact rational identity for `Delta`, obtained by averaging each listed row over the four stated factor-preserving graph automorphisms. The identity consists of 319 nonnegative elemental CMIs and one nonnegative elemental monotonicity row with **negative** multipliers; 12 graph/syndrome equality rows with arbitrary multipliers; four conditional graph-FD equalities; and `(37/492)G`. Thus every term on the right is nonpositive or zero. No numerical LP optimum is needed in the proof.

The independently written checker `frontier-20261028-two-syndrome-all-factor-dual-check.py` SHA-256 `64fa545134f913993ee9dd4857a7904010200b1bd546b66cccbfbc8842d0b65a`, receipt SHA-256 `8bd6527e81cd17c9a950d24a7e6f67e8ce29cb0d1f4af4ac7e34c570425f221d`, checks the four graph/triangle automorphisms and group closure, all row meanings and signs, and cancellation of all 2,047 nonempty entropy-coordinate coefficients exactly with `Fraction`. It rejects an altered target and a flipped CMI sign. The proof of the gate above and its application to actual FD laws are written arguments requiring review.

## 2. Lifting any covering two-syndrome case to the lemma

Let the two syndrome vectors be `s,t`, and let `J` be the factors on which they differ. Affine bit translations independently in each factor normalize them to `0` and `1_J` without changing any entropies or graph FDs. If `J` covers all vertices, condition on the complete tuples of the remaining factors `K=J^c`. On every positive-probability fiber, the selected-factor vertex blocks still satisfy the original graph FDs, because the conditioned components may be supplied as constants to every decoder.

The binary selector `S` is the common selected-factor parity. Since `J` covers all vertices, the same triangle argument as above shows that `S` is determined by each selected-block neighbourhood. For every factor in `K`, independently choose fresh uniform bits `U,V` and append its triangle components as `(U,V,U xor V xor S)`; component ordering follows the pinned triangle list. Every new triangle parity is `S`. Its bit at vertex `i` is determined by the other two new triangle bits and `S`, both obtainable from original neighbours, so the augmented q=8 law retains all graph FDs.

Each appended bit is uniform and independent of the old law and `S`; at each vertex appended bits from different factors are independent. Since `S` is determined by the selected old blocks, adjoining one factor increases `H(X_V)` by exactly 2 and increases `sum_i H(X_i)` by exactly 3. Hence the augmentation preserves `Delta` exactly. The all-factor lemma therefore gives nonpositive `Delta` on every selected-block fiber. The fixed-syndrome factors tensorize before this block by the conditional chain-rule argument in `frontier-20261028-syndrome-cover-entropy-gate-v1.md` SHA-256 `d6df004e025f067a14a6cc69e9aef8d9fc78a20a2fc49c4e431328120e32014b`, proving (25) for the original law.

`frontier-20261028-two-syndrome-lifting-check.py` SHA-256 `5eca28960f79bf0bb2ee5a5699cbc993a03a027c1b93d1c3677380bcfa68b5e1`, receipt SHA-256 `d825e6c731219f3af2b965ed6941a9656eba9ab77b6ccadd1197df85c60c8f90`, checks all 420 covering nonzero masks, all 4,200 vertex/selected-triangle decoding incidences, the `3|K|` entropy increment count, the bit parity/decoder/uniformity gadget, and two negative controls. The entropy and conditional-independence deductions above are written, not a formal proof.

## 3. Remaining syndrome cases and sharpness

If the difference mask `J` does not cover the vertices, the independently checked proper-subgraph/syndrome-cover argument cited above gives (25). If there is only one syndrome value, fixed-parity triangle tensorization gives (25) directly. For a uniform FD support `W`, apply (25) and `H(X_i)<=3` to get `log_2 |W|<=20`. The usual product of ten uniform XOR-zero triangle factors attains `Delta=0` and has `2^20` words, so the two-syndrome entropy bound is sharp within this class.

This supersedes the 95-case **residual status of the particular universal-coloring method** in `frontier-20261028-two-syndrome-full-screen-v1.md` SHA-256 `9934871f9c4d704a30f41c61865cde8e3c8670063abc759a43b7c115f7b10c4c`; it does not invalidate that method's exact fractional-cover obstruction. All stated conclusions remain subject to independent scientific review, proof-assistant status is not claimed, and novelty is not cleared.
