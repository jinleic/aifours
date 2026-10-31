# Zero-excess three-block lemma (generalizes the six-word lemma; needs no no-Hamming-one)

Owner **PhysicsAME46-2**. Native clock observed before writing: `Thu Oct 29 12:39:44 PDT 2026`. **WRITTEN author candidate with an exact complete finite check**, not independently reviewed, adopted, formally verified or novelty-cleared. No import, no solver result and no held material is used.

## 1. Statement

Work in a zero-excess AME(4,6) state: |E|=2n, so every E row and column of every cut has exactly two nonzeros (see `frontier-20261029-zero-excess-six-word-lemma-v1.md`, SHA-256 `3e8e5a4fc9fbc58b5b6e0a3c6a16bc246fdccd78b2bbbcf6f9e1014b26172f07`, §1). A *configuration* is a triple of2x2 rectangles of word positions B_1, B_2, B_3 in the cuts AB|CD, AC|BD, AD|BC respectively with

`|B_a ∩ B_b| = 2 (a≠b)` and `|B_1 ∪ B_2 ∪ B_3| = 6`.

**Lemma.** The six words of a configuration are never all in E.

The six-word lemma is the special case where the six words have pairwise distance at least two. The new cases include configurations with Hamming-distance-one words, so no no-Hamming-one hypothesis is needed.

## 2. Proof

Assume all six words are in E, hence nonzero. Each B_a has all four corners in E. By zero excess its two rows have no other nonzero entries, so their orthogonality reads z_rc·conj(z_r'c) + z_rc'·conj(z_r'c') = 0 with four nonzero factors. The two products are negatives, so with z_w = |z_w|e^(iπx_w),

`x_rc − x_rc' − x_r'c + x_r'c' ≡ 1 (mod 2)`.                     (B_a)

This is the integer row M_a with entries +1,−1,−1,+1 at those corners. Its sign is defined only up to the row/column naming; that ambiguity does not affect (B_a) modulo2.

**Finite fact.** For every configuration there is λ∈{±1}^3 with `λ_1M_1+λ_2M_2+λ_3M_3 = 0` as integer vectors. Applying λ to the three congruences gives 0 ≡ λ_1+λ_2+λ_3 ≡ 1 (mod 2), a contradiction. ∎

Proof of the finite fact (exact enumeration, `frontier-20261029-three-block-lemma-check-v1.py`, SHA-256 `74cc0088cfcf551445bea577d454a9deb1e7de161e9abb95ec84d2ebf4fb7d16`, receipt `frontier-20261029-three-block-lemma-check-v1.json`, SHA-256 `cb5119a7c6e1e47a0fd958a18a65718565ab8bca6f030e38e4cb286f17308020`):

- Counting gives B_1∩B_2∩B_3=∅ and B_3=B_1△B_2, so a configuration is determined by B_1,B_2.
- Independently relabeling the values at each party is a symmetry. It puts B_1 in the form rows {(0,0),r'}, columns {(0,0),c'} with r',c' in {(0,1),(1,0),(1,1)}: nine choices.
- Six words use at most six values per party, so the box {0..5}^4 contains a relabeled copy of every configuration. The check runs over all9 B_1, all6 shared pairs and every rectangle B_2 of cut AC|BD in that box meeting B_1 in exactly the shared pair (994 candidates). It keeps those for which B_1△B_2 is a rectangle of cut AD|BC.
- All138 surviving canonical configurations use at most two values per party. Every one has a λ as stated, found by testing all eight sign vectors in integer arithmetic.

Value-signature counts of the138: (2,2,2,2):42, and24 with exactly one constant party for each of the four parties.

## 3. CNF use

`frontier-20261029-three-block-cnf-v1.py`, SHA-256 `c1b74328be6cb995e1d0c25e401636d9a3304e03e3a0997583c3acfd5751c1d4`, adds one negative six-literal clause per configuration six-set to the unchanged zero-excess encoder. The six-sets come from the168 templates in {0,1}^4 under injective value maps. The check above confirms generator = direct enumeration on boxes 2222, 3333, 2334. The receipt records the counts 168, 8424, 6192.

## 4. Scope

This is a statement about zero-excess residuals only. It is necessary-condition logic and implies no exclusion by itself. As a control, the24-permutation residual (profile4444) satisfies every configuration constraint, because it has an exact fourth-root phase solution (`frontier-20261029-fourth-root-positive-control-v1.json`).
