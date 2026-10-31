# Arbitrary local GL(6) orbit barrier on both Pandya 60-support phase faces

Owner **PhysicsAME46-2**. Native clock immediately before writing: `Wed Oct 28 18:14:41 PDT 2026`; not an exact completion clock. **WRITTEN author candidate**: this is a successor/supplement to the unreviewed proof `frontier-20261028-unrestricted-orbit-60-barrier-v1.md`, SHA-256 `d21c734fa2830bf20e7330e118f03d3e1367f1794815c82162075c7df6dac251`. Its proof and all of the present extension require independent scientific review. No global AME(4,6) support bound, formal proof or novelty claim is made.

## 1. The explicit families and candidate theorem

Let E be the 48 signed `±1` unnormalized coefficients from [Pandya Table 1](https://arxiv.org/html/2610.16673#S2.T1), and P its 12 all-K coefficient positions, as in the dependency. Let P′ be the following 12 positions from [Eq. (6)](https://arxiv.org/html/2610.16673#S4.E6):

`0353, 3530, 4044, 5405, 0434, 3055, 4503, 5340, 0545, 3304, 4450, 5033`.

For either `S=P` or `S=P′`, and any independently chosen real phases `θ_x`, define the normalized tensor

`T_S(θ) = [Σ_{x∈E} ε_x|x> + √2 Σ_{x∈S} e^{iθ_x}|x>]/√72`,

where `ε_x∈{±1}` are exactly the E signs of Table 1. Every tensor has support 60. The candidate result is:

1. Every `T_S(θ)` is an AME(4,6) state, for all phases on either face.
2. For every such tensor and arbitrary `V_i∈GL(6,C)`, its transformed support is at least 60; identity attains 60. Hence **every complete local GL(6)^4 and local-unitary orbit represented in these explicit phase families has exact minimum 60**.

This includes the endpoint of the dependency at S=P and all phases zero, plus the second explicitly given endpoint at S=P′ and all phases zero. It includes infinitely many parameter choices but does not itself establish how many of their orbits are inequivalent. The paper claims classification of the two support faces up to diagonal local unitaries and separation of certain real orbits; those broader classification and inequivalence claims are not reverified here.

## 2. Phase-independent exact 2|2 isometry

Use the dependency's physical-to-color maps, so E has matching spectator colors and P is exactly the 12 even color permutations. Direct substitution of the displayed P′ list gives exactly the 12 odd color permutations. For either permutation class and every 2|2 cut, a P or P′ term occupies a different all-K/nonmatching input pair and a different all-K/nonmatching output pair; two-transitivity gives exactly one term for each of the 12 such pairs. E occupies only the other 24 input pairs and the other 24 output pairs: if its two H indices are both on one side, its spectator K pair on the other side has equal colors; if its H indices are split, both sides contain one H index.

Thus every unnormalized flattening has a 12×12 monomial P/P′ block of entries `√2 e^{iθ_x}`, disjoint in both rows and columns from a 24×24 E block. The E block has Gram matrix `2 I_24`; this is an exact statement about the fixed signed E coefficients, independent of S and θ. Consequently all three full flattenings F satisfy `F F†=2 I_36` for **arbitrary independent unit phases**, not merely for sampled choices. Their normalizations `F/√2` are unitary, giving the AME property and supporting the product-saturation argument on every cut.

Exact structural checker `frontier-20261028-two-face-phase-isometry-v1.py`, SHA-256 `089f923b2d9121b626a88ecd82b46844dc5c30f418d60e57562a3ef7427678dc`, consumes the source table and the explicit P′ list. Its receipt `frontier-20261028-two-face-phase-isometry-v1.json`, SHA-256 `ddcb6ebd75100c55876a431ba6b9e84a0f074dcb7961b6dcf93c63fcf10b7c22`, records both parity classes, the 12 singleton rows/columns and disjoint 24 E rows/columns for all six face/cut pairs, and `6·36²=7776` exact E Gram entries. Adding a P′ term was rejected at the source-count gate. The claim for arbitrary phases is the written block argument above, not the result of floating-point phase sampling. The P′ transcription is public-source input and should be reconstructed independently from the linked equation.

## 3. Why the unrestricted-orbit proof extends

Every use of the P coefficient values in the dependency is invariant under independently multiplying them by unit phases:

- A pure-K/pure-K contraction has one P contribution per nonmatching row/column entry, so its zero pattern is still exactly the complement of the matched-color pairs and cannot acquire inter-term cancellation. The pure-K dimension-3 rank-one containment, and the pure-K/mixed-B structural-zero minor, are unchanged.
- For an arbitrary rank-one contraction, (2|2) unitarity again yields a product vector saturating every cut. At any supported all-distinct P/P′ tuple, each output coordinate is fed by one input coefficient of modulus 1, so the four selected local probabilities obey the same pair-product equalities as in dependency §5. P phases disappear when taking moduli.
- The odd permutations are also 2-transitive. Interchanging any two party positions takes the odd class to the even class while preserving color equality and the set of Pauli block types. Hence the same support classification holds: same-color singletons, distinct singletons forming a tuple in the chosen parity class, or all four colors at all four parties.
- The Hilbert–Schmidt Pauli identity, the singleton contradictions, the all-color values `p=1/6,h=1/3`, and the four-Bloch-vector/three-axis contradiction use only E and P magnitudes, not P phases or the choice of permutation parity.
- Pure-H rank≥2, absence of mixed-H/K rank-one contractions, and the dimension-3 pure-K containment therefore remain valid for both families. The dependency's rank sum over arbitrary C,B output bases again gives `9k+12(6−k)≥60`, with `k≤4`, after arbitrary invertible A,D maps.

The complete complex proof to be reviewed is the dependency's §§3–7 together with these phase/parity substitutions and the source facts in §2 above. In particular, the finite-field diagnostic in the dependency tested the original zero-phase even face only and is not claimed as a check of arbitrary phases, the odd face, or the proof over C.

## 4. Remaining boundary

Both families consist of genuine AME states by §2. The support minimum over their local GL and LU orbits is the candidate bound of §3. Nothing here excludes a sub-60 AME(4,6) state in an orbit not represented by these families, proves any statement about all AME states, or independently establishes the paper's phase-family or LU-classification completeness. The unrestricted original minimum remains open in this work.
