# Consolidated d=4 operator-level certificate argument

**PhysicsResearch96h-2 / physics-1.** Actual clock before writing: Wed Oct 28 17:52:15 PDT 2026. This consolidates the same original d4 target and the already completed exact certificate/source checks. The explicit four-entry coupled-Gram coordinate table in §4 and its separate formal-factor check are new clarifications of a load-bearing original-object bridge. It is **computer-assisted written proof support**, subject to the explicitly pinned implementation/runtime assumptions, not a Lean-kernel proof, parent acceptance, independent human/configured-family review or new discovery.

## 1. Exact assertion and source provenance

Let H=(C⁴)^tensor3. For an arbitrary complex linear C:H→H with rank C<=2, put

`q3(C)=||C||HS²−(1/2)Σ_i||Tr_i C||HS²
       +(1/4)Σ_(i<j)||Tr_ij C||HS²−(1/8)|Tr C|²`,

with unnormalized partial traces. The conclusion supported here is q3(C)>=0 for **all** such C at d=4, including rank0/1 and singular, nonnormal, non-Hermitian and complex cases. We do not assert the source's larger all-d claim or an additional physical distillability reduction.

Tomar's public v3 Theorem1.2 already makes a broader full-target claim ([Zenodo record](https://zenodo.org/records/23682914)); v4 is separately recorded in `frontier-20261028-tomar-v3-v4-d4-source-delta-v1.md`, SHA256 `96b88e86872aa02933fbd10ce513c3885a00f9d5b2724e3106705e33fa4073fe`. The v3 and v4 `release_ep3.tar.gz` certificate archives were actually byte-matched, SHA256 `2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3`. A prior public claim is not by itself proof correctness, and no novelty is claimed.

## 2. Exact full-domain physical lift

For nonzero C scale by positive homogeneity to `||C||HS²=1/2`. Choose an isometry A:C²→H with ran C⊂ran A, and put B=2 C†A. Then

`C=AB†/2`, `A†A=I₂`, `||B||HS²=2`.

Let `a=vec(A)/sqrt2`, `b=vec(B)/sqrt2` in V=H⊗Q, Q=C². Then ||a||=||b||=1, `Tr_H |a><a|=I_Q/2`, and `C_xy=Σ_r a_(x,r) conjugate(b_(y,r))`. Conversely any such a,b yields a normalized original rank<=2 C by this formula. The rank-one case is covered by isometric completion, and C=0 is separate; no inverse or boundary limit is required.

Let F_Q swap the two Q replicas, F_S swap the sites in S⊂{1,2,3}. Direct contraction of arbitrary complex entries gives

`||Tr_S C||HS²=<a⊗b,F_Q F_S(a⊗b)>`.

The separate all-formal-coefficient script checked every one of the eight S (131072 exact term occurrences), SHA256 `fc70405ca23ebb76ca08d4539ff0251db4760a4614b0a3367995cb7c0086b5f6`, receipt SHA256 `ea9eff59833ccdd487a1ca4ace3b56f05c54a2b7711e1d09b7e8b5bfa130bf99`. The written contraction, not sampled matrices, is the universal argument.

## 3. Three actual moments and invariants

Form the SAME-pair pure four-replica moments

`Y31=|aaab><aaab|`, `Y22=|aabb><aabb|`, `Y13=|bbba><bbba|`.

Average each over the same local unitaries U(4)^3×U(2), site permutations, and simultaneous complex conjugation, then multiply by `L=(2·4³)^4`. Denote the real symmetric results X31,X22,X13. For any unitary tuple `(U1,U2,U3,R)`, the same a,b transform by `U1⊗U2⊗U3⊗R`; the reconstructed C transforms by `(U1⊗U2⊗U3) C (U1⊗U2⊗U3)†` because `R^T conjugate(R)=I`. Site permutations and complex conjugation also preserve q3. Thus twirling does not change the objective and never introduces independently selected moments.

Each moment is invariant under independent ket and bra permutations of equal letters; all three site factors may be permuted simultaneously; real symmetry permits simultaneous word inversion. These facts hold term by term before averaging and survive the twirl.

## 4. The entire coupled Gram block, with exact source indices

The **actual d4 data** use 1126 one-row blocks and 111 two-row blocks of the source's first coupled class. They use **no** `gram2` block. Put

`u=a⊗a⊗b⊗conjugate(a)`, `v=b⊗b⊗a⊗conjugate(b)`.

Their true joint block is the outer product

`G(a,b)=|u⊕v><u⊕v| = [[|u><u|,|u><v|],[|v><u|,|v><v|]] >= 0`.

This is joint PSD, not an inference from the diagonal blocks. Under the common local unitary on V, both u and v transform with the **same** `U⊗U⊗U⊗conjugate(U)`, so every twirled and real/site-symmetrized block is still PSD.

The following table gives ALL four actual source-family index rearrangements. Indices 0..3 denote complete V-replica multi-indices; `i` is the Gram ket index tuple and `j` its bra. A row `f;k;l` means the exact value `Y_f[k0,k1,k2,k3; l0,l1,l2,l3]`.

| Gram entry | family f | k | l |
|---|---|---|---|
| `|u><u|` | 31 | `(i0,i1,j3,i2)` | `(j0,j1,i3,j2)` |
| `|u><v|` | 22 | `(i0,i1,i2,j3)` | `(j2,i3,j0,j1)` |
| `|v><u|` | 22 | `(i2,j3,i0,i1)` | `(j0,j1,j2,i3)` |
| `|v><v|` | 13 | `(i0,i1,j3,i2)` | `(j0,j1,i3,j2)` |

For example, the 22 off-diagonal row expands to

`a_i0 a_i1 b_i2 b_j3 · conjugate(a_j2 a_i3 b_j0 b_j1)`,

which is exactly `u_i conjugate(v_j)`. The other entries follow identically; the index rearrangements are performed **for every local factor simultaneously**, not by choosing separate physical moments. The two orderings of the 22 entry are not interchangeable.

`frontier-20261028-d4-coupled-gram-formal-index-check.py`, SHA256 `82585f809d0971d67d39f7eab29320024623c3af5afc8caccde216650d6c4b72`, checked all four displayed identities as exact formal multisets of arbitrary complex coordinate factors; result SHA256 `2726fea15db82c1cbb160622c435f48d2780cca067df72774c7de9de2424d316`, PASS. Four in-memory swaps between different letters were each detected. This is a universal formal-coordinate check, not a test on selected vectors or a substitute for the written PSD argument.

The single-row source blocks are partial transposes of products of pure replica projectors, hence again pure product projectors with the starred factors conjugated. Every literal integer compression is a congruence; for any matrix K, `K† G K>=0`, with no rank/square assumption. The independent local-index comparison checked ALL used row/cut/diagram permutations and factor rearrangements (81552 literal d4 site contractions, 1224 auxiliary contractions); exact paths and hashes are in `frontier-20261028-d4-source-data-audit-v1.md`, SHA256 `1240320c5357e34d75c1206056aa072b3758e461c948398fe4e6264b1b1aa566`.

## 5. Every actual equality and its replica order

At an a-replica r, `Tr_H |a><a|=I_Q/2` and `Tr_V |a><a|=1`. Therefore, as operators on Q_r and all other replicas,

`2 Tr_(H_r)Y − I_(Q_r)⊗Tr_(V_r)Y = 0`.

This applies to r=0 of family31, r=0 of family22, and r=3 of family13. It survives all transforms in the common twirl. These are exactly the three Stiefel groups; their scalar compressed components vanish.

The other two equalities really involve the SAME a,b and the following concrete order:

- **aab:** delete replica2 from `aaab` and from `aabb`, and keep `(0,1,3)` in both cases. Both surviving pure products are `a⊗a⊗b`, since the deleted a or b has norm1.
- **abb:** delete replica1 from `aabb`, keeping `(0,2,3)`, and delete replica1 from `bbba`, keeping **`(3,0,2)`**. Both surviving pure products are `a⊗b⊗b`. The latter permutation is essential.

The actual 648 specified equality compression/permutation contractions were checked against literal basis traces. All corrected equality coefficients may have arbitrary sign: they multiply exact zeros.

## 6. Exact original objective

Let `tau=(0 3)` and set `Z=F_Q Π_(i=1)^3(I−F_i/2)` on the first/fourth complete replicas; the other two replicas of Y31 have trace1. From §2 and the common twirl,

`q3(C)=L^(-1) Tr[(Z_03⊗I_12) X31]=c(X)`.

For a permutation word w=(p1,p2,p3,pQ), with cyc(p) the number of cycles, the actual functional is

`c(V_w) = [Π_(i=1)^3(2·4^cyc(p_i)−4^cyc(tau p_i))]
           ·2^cyc(tau pQ) / 2^31`.

The denominator is exactly `2³ L=2^31`. The independent basis-index check evaluated all331776 words against this expression with zero mismatches. It preserves the physical unnormalized-trace and S-versus-complement convention.

## 7. Why the finite 4675 orbit identities cover every physical X

For local n∈{2,4}, invariance under all U(n) implies diagonal-weight matching and commutator constraints from `rho(E_ij)=Σ_r E_ij^(r)`. The explicitly constructed integer constraint matrices have same-weight unknown counts 70 and2716. Exact modular minor lower bounds for these constraints are56 and2692, while the permutation columns have independent ranks14 and24. Because every permutation commutes with every constraint and the ranks sum to the respective unknown counts, a rank sandwich proves that the actual unitary commutants are exactly the local permutation spans, conditional on the pinned finite-check/runtime correctness.

Full finite witness, elementary derivative proof, exact row data, independent modular replay and fault control: `frontier-20261028-d4-four-replica-commutant-finite-rank-proof-v1.md`, SHA256 `49df4f874bf8c4a4da60d61f1b76d9b8028e2acfca5fe6d8c2b378a324501a23`. The standalone standard-library witness receipt is SHA256 `941c109c36a1536bcf2abf1c6c25ca7e4417104ede684a21221fb5e0582459b6`.

Taking tensor products of these four local commutants spans all actual U(4)^3×U(2)-twirled moments by the 24^4 four-component permutation words. Averaging any representation over the exact stabilizer, site-permutation and real-inversion symmetries makes it a real combination of orbit sums. Word dependencies, especially at Q=C², cause no problem: only **spanning**, not independence or coefficient uniqueness, is used. The independently rebuilt full orbit partitions have counts 1142,2391,1142 = 4675.

## 8. Exact certificate arithmetic and proof conclusion

The final corrected public-certificate rational data are `frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz`, SHA256 `c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94`; they contain 1237 corrected multiplier matrices and 329 corrected equality coefficients. The 272 equality coefficients in the stored initial approximate data are NOT the post-correction count. No approximate residual is used as proof.

Two separately implemented exact global arithmetic routes checked the identity

`c(X)=Σ_t Tr[Z_t K_t† M_t(X)K_t]+Σ_e lambda_e E_e(X)`

on **every 4675 orbit sums**, with 0 residuals in all families:

1. Common-denominator FLINT-integer global contraction, independently rebuilt literal maps/orbits, receipt SHA256 `257944e474c1a2521b32b0e76e4c536e08f0bd2ac1c521546e6b21ce7b821a77`.
2. Modular backend: 424 distinct primes, an independently recomputed 6745-bit residual bound B, and verified 6761-bit prime product P>2B; all residues zero, hence every integer residual is zero. Full derivation and receipt hashes are in `frontier-20261028-d4-crt-certificate-identity-proof-v1.md`, SHA256 `95e6e60f8970a84b3e0c0cf7e2d48fe305eba110ec1b2c62c724c5b4d9fd26b5`.

Both operate on the same corrected data and share literal-map/orbit generators; their agreement is not independent model-family or fully independent software evidence. The saved matrices were separately checked from disk by exact rational Schur elimination and by integer Bareiss/Sylvester elimination. The latter found all1237 positive definite, **4149 positive pivots**, with all divisions exact, receipt SHA256 `5e6a3c0c7be0cf34c1b12cc2d8bf49ae958368a2254dac7fc6e169f3bacf04f6`. Positive semidefiniteness would suffice.

For an actual physical moment tuple, §4 gives every `M_t(X)>=0`, §5 gives every `E_e(X)=0`, and §7 puts X in the identity's checked span. Therefore each remaining term is nonnegative:

`Tr[Z_t K_t† M_t(X) K_t]=||M_t(X)^(1/2) K_t Z_t^(1/2)||HS² >=0`.

Thus c(X)>=0, and §6 identifies this with q3(C). Undo the positive scaling; C=0 is immediate. This is the whole d4 proof implication **conditional on** correctness of the exact code/serialization/runtime and the written coordinate/finite-rank reasoning above. No result is inferred from a sampled C, source count alone, bare hash, approximate SDP, or parent verdict.

## 9. Controls and residual trust boundary

Independently run in-memory negative controls detected zeroing all certificate coefficients; single-row and coupled-block mutations; a corrected aab coefficient mutation; wrong trace/swap complement; and a negative/zero-row PSD defect. The formal-index checks above additionally detected all four deliberately wrong cross-letter index swaps. These are verifier-sensitivity controls, not physical counterexamples.

Historical held/quarantined results are not premises or retroactively validated. This is neither a formal proof-assistant/kernel execution nor a human/other-model-family review; Python, FLINT, NumPy and actual pinned source/checker semantics remain in the trust base. The source already claimed the broader result. No unrestricted all-d verification, new priority, generalized Schmidt-rank theorem, distinct physical operational consequence, or parent adoption is asserted.

**END — consolidated original d4 proof candidate and precise certificate trust boundary.**
