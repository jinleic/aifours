# f35 — independent review of the four-party active-sector rigidity theorem

Reviewer **MathSemigroup-2**, math-4; author **PhysicsAME46-2**, physics-6. Assignment SHA `bc72a9b607b7b0f64b5ed3d8e070e9bcfd387f96e804f0256f9d6a8f1339bc16`. Native prewrite observation **Wed Oct 28 17:40:38 PDT 2026**.

## 1. Verdict and exact scope

**NO_SUBSTANTIVE_DEFECT AT EXACT SCOPE — 0 FATAL / 0 MAJOR / 0 MINOR.**

For the **specific** published 60-term Pandya tensor, every local unitary `V_i=U_i⊕D_i`, with arbitrary U_i∈U(2) on H=span{|1>,|2>} and monomial D_i on K=span{|0>,|3>,|4>,|5>}, produces support at least60. Equality holds precisely when, for every distinct pair and every i,

`U_i U_j^T` is monomial, and `U_i† Z U_i∈{±X,±Y,±Z}`.

The iff is reconstructed over complex unitaries in §§4–5. Identity and explicitly verified nonmonomial four-party rotations attain60. The lower bound extends to arbitrary invertible U_i and invertible monomial D_i; the six-Pauli iff is specifically a unitary statement. This is a restricted continuous sector of **one local orbit**, not an all-U(6)^4 theorem, an all-AME lower bound, a global minimum or a novelty claim.

## 2. Complete sources, prior exposure and two independent computations

I read the complete110LF candidate, SHA `a0d177b8c1d686f1d0a1e63bcc607359a23fe41c37fcf2f9a1ea9fa219ebc69c`. The primary input is [Pandya arXiv:2610.16673v1, Table 1](https://arxiv.org/html/2610.16673v1#S2.T1), the exact local transcription `frontier-20261028-pandya-table-v1.txt`, SHA `cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38`, and the original AME definition packet SHA `07d0ecd8964839862d06c09fda5e444ad5713501438d3c0e04d4e42522c03b01`. In prior f21 I independently transcribed the complete36-cell public table and checked equality of all signs, √2 coefficients and coordinates to the pinned local table; the same reviewer-owned parser verified all six original two-party marginals over Z[√2]. That prior return is `frontier-review-f21-ame-three-party-support-v1.md`, SHA `33597eeaf6c291955cf8a07a1c28871cf666227fa7651f7d0693664140a6cfd7`. Neither the preceding two-/three-party obstruction nor an author review verdict is a premise of the present four-party proof.

I independently wrote `frontier-review-f35-independent-sector-check-v1.py`, SHA `aa7105b8e868ba9a53507ba77f4fa93853423f1454634960db9ce8061fda6066`, with its own strict source parser and exact Z[√2,i] integer-tuple arithmetic. Actual command at **Wed Oct 28 17:39:26 PDT 2026**, timeout30s, exit0:

```text
/opt/homebrew/bin/python3 -B mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-review-f35-independent-sector-check-v1.py physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-pandya-table-v1.txt

table_sha256=cad24229c112b65f2cb624903745095a353513384af6fbce49447c9f6499da38
P_terms=12 active_blocks=24 pair_types=6x(I,J,X,Z)
PASS all blocks rank2, per-pair types, exact 60/60 endpoints and 84 rational-angle support
PASS all six exact marginals for real/complex endpoints and rational-angle state
support_intersections: original-real=36 original-complex=36 real-complex=36
PASS all36 original-real common coefficients unchanged
CONTROL one-coefficient sign flip rejected: per-pair type coverage
```

The first checker run at17:39:09 failed with `NameError: need` in my own assertion helper; I replaced those calls with the existing `require`, then reran. No author source or candidate was edited. The corrected run's hashes and output above are the actual evidence. Its intentional sign flip is a targeted negative control, not a full mutation suite.

I also independently wrote and executed `frontier-review-f35-independent-gate-search-v1.py`, SHA `3bc7c49a944845e4de4a06ba81a48427c3300d2416ba18e955989b2ec96b71f2`. It imports only **my own pinned sector-table parser**, not the author's source/checker/result. Its gate action and final-fiber support counts are separately written; the shared mathematical gate/fiber strategy and prior source reading make this nonblind same-harness implementation diversity, not an independent-model or third-family review. Actual command at **Wed Oct 28 17:39:56 PDT 2026**, timeout180s, exit0 in25.23s:

```text
/opt/homebrew/bin/python3 -B mathematics/evidence/three-area-20261027-96h/parallel-18/semigroup-embedding/frontier-review-f35-independent-gate-search-v1.py physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-pandya-table-v1.txt

exact_gate_combinations=810000 support_min=60 minimizer_count=2
best_gates=[((1, 2, 0), (1, 2, 0), (1, 2, 0), (1, 2, 0), 60), ((1, 2, 1), (1, 2, 1), (1, 2, 1), (1, 2, 1), 60)]
PASS independently enumerated full stated 15^4*2^4 alphabet over Z[sqrt2,i]
```

The program also printed all16 phase-pattern minima, matching the candidate's reported pattern. It uses exact integer tuples, not a numerical zero threshold. It enumerates only the stated finite gate alphabet; it does not prove the general-sector iff or exclude all four-party U(6) transformations.

Prior contacts include my w20/w58/f21 AME reviews and QOA source-only work. They are disclosed familiarity, not a blindness or clean-cognition certificate. No author contact, author-code import, held outcome as premise, external model, publication, Git push/deletion or infrastructure change occurred. The current owner direction prospectively permits this public-source read and bounded local verification; no earlier quarantine is retrospectively reclassified.

## 3. Exact source decomposition and sector support bound

The independent parser groups each source entry by which party coordinates belong to H. It verifies exactly12 P terms with **zero** H positions and48 E terms with **exactly two** H positions; no other occupancy occurs. Every P coefficient is √2 before the common √72 normalization. P output terms remain distinct nonzero P terms because each D_i is a monomial bijection on K.

For each unordered active party pair i<j, group E terms by their **two K spectator coordinates**. The checker verifies exactly four groups per pair, each containing a 2×2 coefficient matrix with exactly two nonzeros and determinant ±1. Up to an overall sign, the four matrices are exactly one each of

`I=[[1,0],[0,1]]`, `J=ZX=[[0,1],[-1,0]]`,
`X=[[0,1],[1,0]]`, `Z=[[1,0],[0,-1]]`.

Thus all six pairs have all four types, giving24 actual disjoint blocks, not merely aggregate type counts. Reversing the pair order transposes these matrices; the set of types remains `{I,X,Z,±J}`.

The transformation preserves H/K membership at each party. For a fixed E block, the active matrix transforms exactly as `U_i M U_j^T`; the transpose follows directly from coefficient expansion `Σ_(a,b) U_i[p,a] M[a,b] U_j[q,b]`. Spectator monomials only permute the two K labels and multiply the whole block by a nonzero phase. Distinct active party pairs have different H-position sets, and distinct spectator assignments remain distinct under those bijections. Thus the12 P terms and24 E blocks have mutually disjoint output coordinate groups; cancellation between groups is impossible.

All M,U_i,U_j are invertible, so each transformed 2×2 block has rank2 and at least two nonzeros. Therefore the full support is at least12+24·2=60. This argument also holds for invertible complex U_i and invertible monomial D_i, independently of preservation of the AME property. For physical unitaries, AME is preserved by local unitary conjugation of the marginals.

## 4. Exact necessity and sufficiency of the monomial-block conditions

An invertible 2×2 matrix with exactly two nonzeros has one nonzero in each row and column, so it is monomial. The disjoint-block bound can attain60 only if **all24** transformed E blocks are monomial. Every active pair actually has an I block, so necessity gives

`B_ij=U_i U_j^T∈Mon(2)` for every i≠j.

Every pair also has X and Z blocks. If i is its first index, right-multiply `U_i X U_j^T` and `U_i Z U_j^T` by the monomial inverse of B_ij. The results are respectively `U_i X U_i†` and `U_i Z U_i†`, both monomial. If i is the second index, transpose the same four actual block matrices; I,X,Z are symmetric and J^T=-J, so the argument applies to i with no lost sign or index. Every party has partners; this proves the single-party monomial-conjugate condition for all i.

Conversely, if every B_ij and every `U_i X U_i†`, `U_i Z U_i†` is monomial, then for each M∈{I,X,Z,J=ZX},

`U_i M U_j^T=(U_i M U_i†)B_ij`.

The conjugate of J is the product of the conjugates of Z and X. Products and inverses of monomial matrices are monomial, so all24 transformed blocks have exactly two nonzero entries and support is60. Overall signs do not change support. This proves the iff at the correct transpose convention.

## 5. Exact conversion to the six-Pauli criterion

For a unitary U, `N=U† Z U` is a traceless Hermitian unitary. Its unique Pauli expansion has real coefficients

`N=n_x X+n_y Y+n_z Z`,  `n_x²+n_y²+n_z²=1`.

For M=X or Z, the coefficient of Z in `U M U†` is `(1/2)Tr(N M)`, respectively n_x or n_z. A traceless Hermitian 2×2 unitary is monomial exactly when its diagonal Pauli coefficient is0 or ±1: zero gives an off-diagonal matrix, while absolute value1 forces its off-diagonal entries to vanish. Hence both conjugated X and Z are monomial iff `n_x,n_z∈{0,±1}`. The unit-sphere identity then leaves precisely `N∈{±X,±Y,±Z}`. Conversely each of those six possibilities gives the two required monomial conjugates.

This handles arbitrary U(2) phases, including complex Y and every zero/endpoint case, with no assumption of real rotations or of U_i=U_j. The pair matrix is `U_i U_j^T`, **not** `U_i U_j†`; changing that transpose would alter the statement.

## 6. Continuous examples and bounded gate alphabet

For the common real rotation `R=[[cosθ,sinθ],[-sinθ,cosθ]]`, direct multiplication gives

`RIR^T=I`, `RJR^T=J`,
`RZR^T=cos(2θ)Z-sin(2θ)X`,
`RXR^T=sin(2θ)Z+cos(2θ)X`.

There are exactly six blocks of each type. If either sine or cosine vanishes, each block stays monomial and support is60; otherwise the12 X/Z blocks each have four nonzeros, giving12 P + 12 I/J·2 + 12 X/Z·4 =84. At θ=π/4 all four local U_i are nonmonomial, source/real supports intersect in36 positions, and those36 coefficients are unchanged. The independent integer checker verifies the endpoint and its six exact marginals.

For common `Q=[[cosθ,i sinθ],[i sinθ,cosθ]]`, direct multiplication gives `QZQ^T=Z`, `QJQ^T=J`, `QIQ^T=cos(2θ)I+i sin(2θ)X` and `QXQ^T=cos(2θ)X+i sin(2θ)I`. The same60/84 classification follows. The independent checker verifies the complex π/4 endpoint, its six exact marginals, and the original/complex and real/complex support intersections36. It also independently verifies support84 and all six marginals for the explicitly stated rational-angle real rotation, with no floating point.

For the finite gate alphabet, each party selects one of15 unordered coordinate pairs and z∈{1,i} in `[[1,z],[-conj(z),1]]/√2`; the independent program exhausts all `30^4=810000` four-party choices and finds exactly two representatives with support60, both using pair(1,2) at all parties and the common z=1 or common z=i. For |z|=1, changing z to -z merely applies a monomial output operation on the selected two rows:

`M_(-z)=diag(-z,conj(z)) · [[0,1],[1,0]] · M_z`.

The remaining four coordinates are untouched, so z∈{±1,±i} has the same support possibilities up to local output monomials. This finite search is not a proof for arbitrary gate angles, general U(6)^4 or other AME orbits.

## 7. Remaining gates and finding

No FATAL/MAJOR/MINOR defect was found in the candidate's source-block, lower-bound, complex equality, continuous-path or finite gate-alphabet claims at the stated scope. The exact finite computations and the universal unitary proof are independent checks of different things; neither certifies novelty, all-state support, unrelated source claims or any old held outcome.

The actual global AME(4,6) minimum, other tensor orbits, transformations that mix H with K or use nonmonomial K operations, and a physical sub-60 witness remain outside this theorem. The full f35 candidate and this return require Main's actual read/disposition before any adoption. Same-harness results are not formal/kernel, human, independent-model or worldwide-priority verification.
