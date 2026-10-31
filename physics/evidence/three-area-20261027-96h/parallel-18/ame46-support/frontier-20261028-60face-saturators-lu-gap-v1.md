# Twelve maximal product rays, LU equality, and a support gap on the 60 faces

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 18:35:08 PDT 2026`; not an exact completion clock. **WRITTEN author candidate**, requiring independent scientific review. It depends on the unreviewed full-orbit/no-mixed-contraction argument in `frontier-20261028-unrestricted-orbit-60-barrier-v1.md`, SHA-256 `d21c734fa2830bf20e7330e118f03d3e1367f1794815c82162075c7df6dac251`, and its two-face extension `frontier-20261028-two-face-unrestricted-orbit-60-v1.md`, SHA-256 `8af3381ec64c50d7e9f17e485e1c91093be35fa9057ad2829de66474e41af5cf`. No global AME bound, formal proof or novelty determination is claimed.

## 1. Claims

Let T be any of the two explicit 60-support E∪P or E∪P′ AME phase families in the dependency, with E fixed to the published signed Pauli coefficients and arbitrary independent unit phases on the 12 P or P′ entries. In the displayed four-color K bases:

1. **Exactly 12 product rays** attain the AME product-overlap maximum `|<φ,T>|=1/6`: the 12 source coordinate rays indexed by P or P′. There are no others.
2. After arbitrary `U_0⊗⋯⊗U_3` with `U_i∈U(6)`, the output support is either 60 or at least 63. In particular, support 61 and 62 cannot occur in these LU orbits.
3. Support is exactly 60 iff, after support-preserving output permutations, every U_i has a monomial U(4) action on the source K basis, an arbitrary U(2) action `W_i` on H, and there is a single Pauli axis `A∈{X,Y,Z}` such that `W_i† Z W_i=±A` for all four i.
4. If all source K basis rays map to output coordinate rays but the shared-axis condition fails, the support is at least 84. This 84 bound is attained by the nonendpoint common H rotations in `frontier-20261028-four-party-sector-rigidity-v1.md`, SHA-256 `a0d177b8c1d686f1d0a1e63bcc607359a23fe41c37fcf2f9a1ea9fa219ebc69c`.

The support gap and equality classification here use **unitarity**, not arbitrary GL(6). The separate dependency claims ≥60 for arbitrary local invertibles. The exact best support in the range 63–83, if any, is not established.

## 2. Characterizing the maximal product rays

The dependency's §§3–6 prove the following source-specific statement, whose review is prerequisite here: a rank-one two-party contraction of either 60-face tensor cannot involve a pure-H or mixed-H/K covector at any party. A maximal product-overlap vector is a product saturator on every 2|2 cut, so all four of its factors must lie in K.

For a K-supported product saturator, let `p_i(g)=|φ_i(g)|²`. The even or odd color-permutation support and 2|2 unitarity give the nonnegative pair-product identities in dependency §5. Their nonempty support patterns are exactly: (i) all four parties supported on the same single color; (ii) all four supported on distinct colors forming a tuple in the chosen permutation parity class; or (iii) all parties supported on all four colors. This is the 4+12+1 mask classification of the dependency, and applies to the odd class by a party swap.

Case (i) has zero overlap with T because all its K-supported terms use four distinct colors. In case (ii), the product ray is one of the 12 P/P′ coordinate rays; its coefficient has modulus `√2/√72=1/6`, so it saturates. In case (iii), the same pair-product identities make all 16 probabilities equal; each local normalization gives `p_i(g)=1/4`. Every K coordinate amplitude then has modulus 1/2. The overlap receives only the 12 P/P′ terms, each of modulus 1/6, so the triangle inequality gives

`|<φ,T>| ≤ 12·(1/6)·(1/2)^4 = 1/8 < 1/6`.

This excludes case (iii), independently of the P/P′ phases. Thus the 12 specified product rays are the entire saturator set.

## 3. Row counting and necessity of coordinate K rays

For an arbitrary output basis of any normalized AME(4,6) state, call a nonzero coefficient *maximal* if its modulus is 1/6. Let t count maximal coefficients. In a 36×36 two-party flattening, each row has squared norm 1/36. A maximal entry is the sole nonzero entry in its row; conversely, a singleton row must contain an entry of modulus 1/6. Every other row has at least two entries. Hence

`N ≥ t + 2(36−t) = 72−t`.                                           (2)

This elementary row-count inequality is also noted in the public paper; it is reproduced here because equality is used below.

Under local unitaries the product saturator set is mapped bijectively to the 12 product rays obtained by acting on the 12 source P/P′ coordinate rays. A maximal output coefficient exists precisely when one of those transformed rays is an output product-basis coordinate. Therefore t≤12. If any source K basis ray at party i is mapped to a non-coordinate local ray, every source saturator containing that ray fails to become an output coordinate. Each color occurs exactly three times at each party among either the 12 even or the 12 odd permutations. Thus at least three of the 12 rays are absent, t≤9, and (2) gives `N≥63`.

If N=60, (2) forces t≥12; hence all 12 transformed product saturators are coordinate rays. Every one of the four source K colors occurs in such a ray at every party. A product tensor is a coordinate product ray only when each factor is a coordinate ray, so each local U_i maps all four source K basis rays to four distinct output coordinate rays. By unitarity the orthogonal complement H maps onto the remaining coordinate 2-plane. A support-preserving output permutation therefore puts every U_i in block form `W_i⊕D_i`, with `W_i∈U(2)` and D_i a monomial U(4) map. Conversely, if some source K ray is not coordinate, the previously proved `N≥63` applies. This proves the universal LU gap in Claim 2 once the final all-K-coordinate case is analyzed.

## 4. Exact 60 equality and the stronger 84 gap in the coordinate-K case

Assume all K rays are coordinate and work after the output permutations of §3. The 12 P/P′ entries stay nonzero and distinct. The E sector consists of 24 disjoint 2×2 blocks; for each party pair i,j there is one each of I,X,Z,J up to sign. The transformed block for Q is `W_i Q W_j^T`. It is unitary, hence has either exactly two nonzeros (monomial) or four nonzeros. If n is the total number of nonmonomial active blocks,

`N = 60+2n`.                                                         (3)

Write the traceless Hermitian unitary `N_i=W_i† Z W_i` as `r_i·(X,Y,Z)`, where the real Bloch vector r_i has norm 1. The Q block is monomial iff

`Q conjugate(N_j) Q† = ±N_i`.                                        (4)

Indeed, for `B=W_i Q W_j^T`, monomiality is equivalent to `B Z B†=±Z`; substituting gives (4). Conjugation of N_j reflects its y component, and the four Pauli Q act on Bloch vectors by the four sign-flip patterns with determinant +1. They do not change which Bloch coordinates are nonzero.

If both r_i and r_j use the same single Pauli axis, all four Q blocks are monomial; if they use different axes, none is. For a pair containing a vector with at least two nonzero axes, one can bound the number of monomial blocks as follows:

- if the two axis-support sets differ, no sign flip can satisfy (4), so all four blocks are nonmonomial;
- if both supports are the same two-axis set, at most two of the four sign patterns give the required projective axis, so at least two blocks are nonmonomial;
- if both supports use all three axes, at most one pattern gives the required projective axis, so at least three blocks are nonmonomial.

If m parties have at least two nonzero Bloch axes, every mixed pair of a multi-axis and single-axis party has four nonmonomial blocks, and every pair of multi-axis parties has at least two. Thus

`n ≥ 4m(4−m)+2·C(m,2)`.

For m=1,2,3,4 the right side is respectively 12,18,18,12. If m=0 but the four Pauli axes are not all the same, there are at least three different-axis party pairs, each contributing four nonmonomial blocks; again n≥12. If all four use the same Pauli axis, every pair has four monomial blocks and n=0. Therefore n is either 0 or at least 12, and (3) gives either N=60 or N≥84.

Equivalently, n=0 iff all `N_i=W_i† Z W_i` lie on one common Pauli axis with independent signs. This is precisely Claim 3. It agrees with and strengthens the **scope**, not the proof status, of the prior active-sector equality criterion `frontier-20261028-sector-equality-classification-v1.md`, SHA-256 `14490180d1b659b91472315d6ccd0cf1b3af64dcb63d59bdeb1ff122238bf707`: here the need for coordinate K rays is deduced from the full product-saturator set for arbitrary local unitaries.

## 5. Finite controls and limits

`frontier-20261028-lu-gap-combinatorics-v1.py`, SHA-256 `7340ef4f879583f4e973fc9de40107b26c06a36c54b75d28610e8b9d93c8e7e5`, enumerates both 12-tuple parity classes, verifies each color occurs three times at each party, checks all 65,535 incomplete local-color masks per class have at most nine coordinate rays, and checks all `7^4=2401` nonempty Bloch-support masks: outside the shared-single-axis case, the nonmonomial-block lower bound is at least 12. Receipt `frontier-20261028-lu-gap-combinatorics-v1.json`, SHA-256 `908c6c560032635cfb0aecd3173a9833f556b96c6a0c97b8b8acaca2aab90f3c`. These checks are finite combinatorial controls, not a replacement for the complex-unitary and product-saturator proof.

All stated claims concern the two explicit 60-support phase faces and their local-unitary orbits; the 63 gap is not claimed for arbitrary AME(4,6) states, arbitrary GL transformations, or other orbits. The support minimum over all AME(4,6) states remains unresolved.
