# Three-copy d=4 rank-two inequality: explicit certificate bridge and independent exact identity

**PhysicsResearch96h-2 / physics-1.** This document records an exact computer-assisted certificate reconstruction for the **same original d=4 three-copy physical operator**, with explicit software/import qualifications. It is a candidate for parent/independent scientific review, **not** a new-discovery claim, Lean-kernel proof, human/configured-family acceptance or unilateral parent adoption.

## 1. Result and assurance

For the corrected d4 data published with [Tomar v3, Zenodo record23682914](https://zenodo.org/records/23682914):

- An independently written one-worker checker, using independently rebuilt literal local maps and independently rebuilt source orbits, computed **all 4675 corrected certificate identity residuals as exact integer zero** over a common 6645-bit denominator. It did **not** import or execute the author's `ep3core.py` or `verify_perd.py`.
- A separate rational Schur algorithm checked **all1237 corrected multipliers PSD**, with zero failures. The author verifier's different characteristic-polynomial method also reported zero failures in an actual local replay.
- The original unnormalized q3 / physical rank-two swap identity was independently checked coefficientwise for all complex factor entries, not on sampled matrices.

Together with the explicit conditional bridge below, these checks give **computer-assisted written support for the existing public d4 claim**, conditional on the stated mathematical imports and correct execution of the pinned scripts/runtime. They do not independently verify the paper's all-d>=9 theorem, execute Lean, verify a physical distillability criterion, establish novelty or certify proof correctness by a human/other model family. The parent must actually read the complete source/evidence and apply its own review/adoption process. The checks do not reinterpret old quarantines as successful.

The published paper's Theorem1.2 claims more than the original d4 case; here **d=4 only** is checked. A separate AppendixA V17 count wording discrepancy is documented in §8, not presented as a mathematical counterexample.

## 2. Exact original target and source identity

Let `H=(C^4)^tensor3` with standard product Hilbert structure. For **every complex** C:H→H with actual rank<=2, including rank0/1 and all degeneracies, define

`q3(C)=||C||HS²−(1/2)Σ_(i=1)^3||Tr_i C||HS²
        +(1/4)Σ_(1<=i<j<=3)||Tr_ij C||HS²−(1/8)|Tr C|²`.

Partial traces are **unnormalized** and all matrix norms Hilbert–Schmidt. No Hermitian, positive, normal, real, product-ray, range/co-range or chosen-input restriction is imposed. The logical claim supported by the certificate is `q3(C)>=0` for this whole class.

The pinned local paper `tomar-werner-copies-zenodo23682914-v3.pdf` has SHA256 `fe272e67d880a67c3ae2103e4e486753541accc8f64586182df06c279545a4e5`. The public version-specific registry's file `release_ep3.tar.gz` was downloaded as `frontier-20261028-tomar-release-ep3-v3.tar.gz`; SHA256 `2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3`, MD5 `704bae52c2083bf81b5c11332415b3d4` matching the registry. The d4 compressed certificate member has SHA256 `0eccbad8fc2f65954a6a7038094e7c6deb9259852aef3c406f5421a4a649194f`.

Hash identity binds the data; it is not itself a proof. The public Theorem1.2 is an explicit prior full-target **claim**, so no new discovery of that endpoint is claimed.

## 3. BOTH actual original-object lifting directions

Fix nonzero rank<=2 C and scale it by a positive scalar so that `||C||HS²=1/2`. Choose an isometry A:C²→H whose range contains ran C, using orthonormal completion if rank C=1. Set `B=2C†A`. Then

`C=AB†/2`, `||A||HS²=2`, `||B||HS²=2`.

Define vectors in H⊗Q, Q=C², by `a=vec(A)/sqrt2`, `b=vec(B)/sqrt2` in the same product basis. They satisfy

`||a||=||b||=1`, `Tr_H |a><a|=I_Q/2`,

`C_xy=Σ_(r=1)^2 a_(x,r) conjugate(b_(y,r))`.

Conversely, for **any** unit a,b satisfying that a-marginal constraint, define A=sqrt2 mat(a), B=sqrt2 mat(b), C=AB†/2. Then A†A=I₂, rank C<=2 and `||C||HS²=1/2`. Thus the source's physical pairs describe precisely the normalized original complex domain; b is not assumed Stiefel. Rank0 has q3(0)=0. No singular-value inversion or unproved boundary limit is used.

For every subset S of the three physical sites, the direct index identity is

`||Tr_S C||HS²=<a⊗b,F_Q F_S(a⊗b)>`.

Here F_Q swaps the two Q factors and F_S swaps exactly the sites in S. It follows by pairing the independently summed traced indices and retaining the conjugates in the displayed C formula. It holds for arbitrary a,b, before Stiefel normalization.

Independent script `frontier-20261028-d4-original-swap-coefficients-check.py` SHA256 `fc70405ca23ebb76ca08d4539ff0251db4760a4614b0a3367995cb7c0086b5f6`; result `frontier-20261028-d4-original-swap-coefficients-check-results.json` SHA256 `ea9eff59833ccdd487a1ca4ace3b56f05c54a2b7711e1d09b7e8b5bfa130bf99`: independently expand direct partial traces and actual swaps as polynomials in ALL U,conjugate(U),V,conjugate(V) entries; **131072** term occurrences, all eight S, zero coefficient mismatches. This exact finite identity check uses Python integers, not sampled C. The full q3 coefficients after multiplication by8 are `8,−4,+2,−1` by |S|.

## 4. Actual moments, source span and named mathematical import

For the SAME physical pair a,b, set

`Y31=|a a a b><a a a b|`,
`Y22=|a a b b><a a b b|`,
`Y13=|b b b a><b b b a|`.

The four symbols denote complete V=H⊗Q replicas. Simultaneously twirl by all local site unitaries and Q unitaries, all three site permutations, and complex conjugation; multiply the average by `L=(2*4³)^4`. Call the three resulting moments X31,X22,X13.

The local unitary part maps C to U_site C U_site† (because `R^T conjugate(R)=I` for the common Q-unitary). Site permutation and complex conjugation also preserve all partial-trace norms. The moments are therefore attached to one actual original C and their q3 objective is unchanged by twirling.

**Named classical import:** the Schur–Weyl commutant theorem says the commutant of `U(n)` on four replicas is spanned by the corresponding permutation operators, including n=2. Its tensor-product version puts each Haar-averaged X_f in the span of four-factor permutation words. Word operators need not be linearly independent. Stabilizers of the repeated-letter string act on ket and bra independently; site permutations and real symmetric transpose/inversion are also symmetries. Averaging any real coefficient representation over these actions gives a representation by orbit sums. Hence the ACTUAL tuple lies in the real product source space spanned by those sums.

An independent union-find rebuilt the entire orbit partition on all `24^4=331776` words in each family, with both left/right stabilizer generators, site permutations and inversion; it compared partitions in both directions against the published labels. Result: 1142 (31),2391 (22),1142 (13), total4675, no disagreements. Script SHA256 `f15090ef47437eeb850ee29614409f92830793aae3f4637e2c9229770b6ed3cc`; result SHA256 `e9d6adcd09fe816ecda624b62bf8e9be265d5862917e6b38d666046043d49618`.

## 5. Why each actual block is PSD and each equality vanishes

The d4 package has 1126 single-row and111 two-row coupled Gram blocks. For a single row, transposing whole replicas of a physical product projector is again a projector on the tensor product with those factors conjugated. Averaging the actual twirl preserves PSD.

For the coupled rows the actual vectors are

`u=a⊗a⊗b⊗conjugate(a)`,
`v=b⊗b⊗a⊗conjugate(b)`.

The unaveraged two-row block is the PSD outer product `|u⊕v><u⊕v|`. Its four entries are fixed index rearrangements of the three supplied Y_f families; the same conjugated/nonconjugated tensor-unitary acts on both rows, so twirling preserves the complete coupled block's PSD. This is not an inference of joint PSD from separate diagonal blocks. Every fixed certificate congruence K gives K†M(X)K PSD, without requiring K to be square or full rank. The actual d4 package uses no gram2 block; no unneeded gram2 correctness claim is used to pay these specific data.

The five exact equality groups are:

- three Stiefel contrasts at an a-replica: `Tr_H |a><a|=I_Q/2` and `Tr |a><a|=1` make each contrast zero, with the source's auxiliary expression scaled by2;
- the `aab` common marginal obtained by deleting the relevant normalized replica from Y31/Y22;
- the `abb` common marginal obtained from Y22/Y13 with the **specified different surviving-replica order**.

The same twirl preserves these identities. The independent data checker matched the exact group names, family signs, slots and orders; the independent basis-index equality checker evaluated every used compression/permutation. Lambda coefficients need not be positive because they multiply identities that are exactly zero.

## 6. Objective and actual finite computations

Let `Z=F_Q product_(i=1)^3 (I−F_i/2)` acting on replicas1 and4. The other two a replicas of Y31 have trace1. From §3 and twirl invariance,

`q3(C)=L^(-1) Tr[(Z_14⊗I_23) X31]=:c(X)`.

For a word `(p1,p2,p3,pQ)`, the source objective is

`c(V_w)=[product_(i=1)^3(2 Tr V_(p_i)−Tr(F_14 V_(p_i)))]
          * Tr(F_14 V_(pQ)) / [2³(2*4³)^4]`.

The denominator is **2147483648**. Direct finite fixed-basis counts independently matched this numerator for ALL331776 words; the used site maps (81552 raw diagram pairs/permutations in both loop-count modes), auxiliary maps (1224), equality maps (648) and row/cut/family shapes also matched, with zero failures. Detailed independent scripts/results and their SHA256s are recorded in `frontier-20261028-d4-source-data-audit-v1.md` (`1240320c5357e34d75c1206056aa072b3758e461c948398fe4e6264b1b1aa566`). These checks use exact integer arithmetic, not sampled numerical agreement.

The author verifier was separately run with ONE worker. It took the pinned dyadic base, built an exact 2634-coordinate correction, reported zero residuals on4675 orbit sums and zero characteristic-polynomial PSD failures on1237 corrected multipliers. The actual final rationals were saved to `frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz`, SHA256 `c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94`. That replay is documented separately in `frontier-20261028-d4-corrected-certificate-replay-v1.md` (`985e6da6389b893da3a182ddf5015bd73c62410f462d20dafe4611d1255098a5`). Its then-pending identity statement is historical, superseded by the next actual check.

**Independent exact global identity:** `frontier-20261028-independent-d4-global-identity-check.py`, SHA256 `b6b6f5ee18f43d0ae18a18878c47b7559a5a00375754497bf21d6dec93e1be8d`; result `frontier-20261028-independent-d4-global-identity-check-results.json`, SHA256 `257944e474c1a2521b32b0e76e4c536e08f0bd2ac1c521546e6b21ce7b821a77`. It parses the actual corrected rationals, rebuilds all literal site/aux/equality/objective maps and source partitions, and evaluates the full grouped tensor contraction with **exact integer numerators over one 6645-bit common denominator**. It imports no author verifier or author core. It computed all17 row-pattern groups and ALL4675 residual numerators: **0,0,0** in the three families; runtime63.703s.

**Independent corrected PSD:** exact `Fraction`-Schur elimination checked every one of the actual1237 corrected rational matrices for symmetry and PSD; no failure or disagreement with the author's separate characteristic-polynomial check. Result `frontier-20261028-d4-author-replay-and-independent-psd-results.json` SHA256 `de4a897846fcd76ec27820d539ebc65cd18f55f2e405dd89e284c4c6341b27d7`; independent Schur runtime314.693s. The exact exported data used by the identity checker came from the same checked corrected matrices and equality coefficients.

**Negative control actually performed:** `frontier-20261028-d4-global-identity-negative-control.py` SHA256 `ab1ebfbc0d13e173d205cce6e81af640e62c38460f9de221591627deff7fb72f`; result SHA256 `827c790535ede3f5ff91ba032b54c0bc27964ddadf8ec1ec1108eb765ecce522`. Replacing all certificate multipliers and equality coefficients by zero **in memory only**, while retaining the objective, produced the expected FAIL with1137 nonzero family31 orbit residuals. This is a checker-sensitivity control, not a physical counterexample. A single-block mutation check and a standalone recheck of the saved corrected matrices were still running at the start of this document; their outputs are not claimed here.

## 7. Conditional proof from the checked certificate

The exact identity verified on every source orbit is

`c(X)=Σ_t Tr[Z_t K_t† M_t(X) K_t]+Σ_e lambda_e E_e(X)`.

Orbit sums span the real source space by §4, so the identity holds on every actual twirled moment tuple. Each M_t(X) is PSD by §5 and each actual Z_t is PSD by the exact Schur check. Thus

`Tr[Z_t K_t† M_t(X) K_t]
 =||M_t(X)^(1/2) K_t Z_t^(1/2)||HS² >=0`.

Every E_e(X)=0 by the actual Stiefel/marginal identities. Therefore c(X)>=0. By §6 this is q3(C)>=0 for every normalized original rank<=2 complex C; positive homogeneity and the separately handled zero operator give the whole original domain.

This is the explicit mathematical implication of the checked certificate **if** the named Schur–Weyl import, program/source correspondence and exact runtime arithmetic are correct. The computation is reproducible evidence supporting that claim, not a substitute for reviewing those assumptions or a formal kernel proof.

## 8. Factual source-count qualification and residual risks

Actual public data have 715,1237,1347,1347,1347,1347 types for d=3,…,8. Paper Section4/V1/V2 agrees for d3/d4, whereas AppendixA V17's blanket wording “every one of the 1347 multipliers” for d3,…,8 is inaccurate as written. This documentary inconsistency is not a false q3 inequality or a failure of the d4 data.

The independent global checker and author solver use the **same public exact corrected certificate**, and both rely on Python/numpy/FLINT runtime semantics; they are distinct code paths, not independent proof assistants or independent model families. The group-commutant lemma is a named standard theorem, not formalized here. The capture ties the in-memory PSD-checked matrices to the serialized data by source inspection and hashes; a separate standalone direct-from-file PSD audit is pending. The all-zero mutation control checks gross sensitivity but does not rule out all coding errors. No clean-background/provenance inference or earlier held-outcome rehabilitation is made.

No general-dimensional theorem, physical distillability implication, Lean kernel replay, human review, novelty/priority or final parent disposition is claimed. The public source established the prior full-target **claim**; the mathematical and computational review here is evidence about d4 only.
