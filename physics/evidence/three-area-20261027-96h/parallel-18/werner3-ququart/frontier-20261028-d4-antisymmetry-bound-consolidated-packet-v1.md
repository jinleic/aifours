# Original-domain d4 q3 antisymmetry bound: consolidated written review packet

**Owner:** PhysicsResearch96h-2 / physics-1. **Status:** WRITTEN mathematics plus the precisely scoped exact rational computations named below; **UNREVIEWED**. The full q3 bound is explicitly **conditional on** the pinned source-certificate identity and physical PSD premises; neither this packet nor the earlier dossier is parent-adopted. The separate Δ≥0 lemma and the failure of its converse are source-independent.

This packet consolidates the earlier source-Gram equality, triple-antisymmetry, properness, coercive, rational-coefficient and intrinsic-coordinate notes into one prospective review scope. It does not alter the separate frozen f153 product-equality review or retroactively extend f62. Its proof does not use or reconstruct the elected earlier HELD/ZERO/NONINPUT episode or its consumers. Historical timing/process findings and every prior hold remain unchanged.

## 1. Original target, explicit result and nonclaims

Let `H=(C⁴)^tensor3`. The original functional uses **unnormalized** partial traces:

`q3(C) = ||C||HS² − (1/2)Σ_i ||Tr_i C||HS² + (1/4)Σ_(i<j) ||Tr_ij C||HS² − (1/8)|Tr C|²`.

C is an arbitrary **complex** operator on H of rank at most2; no positivity, Hermiticity, product structure or real-coordinate restriction is imposed. On two H copies regrouped by site, let `F_i` swap the two copies of site i and set

`A3 = Π_(i=1)^3 (I−F_i)/2`, `F=F_1 F_2 F_3`.

A3 is the orthogonal projector onto `(wedge² C⁴)^tensor3`, has rank `6³=216`, and satisfies `F A3=−A3`.

For any rank2 orthogonal projection P with `PC=C`, define

`Δ(P,C) = Tr[ A3(P⊗C†C − C⊗C†) ]`.                                (1)

P exists for every rank≤2 C. For exact-rank2 C it is the unique range projection; rank1 permits any rank2 extension. The scalar in (1) is real. We prove source-independently

`Δ(P,C) >= 0`.                                                        (2)

Under the exact source/Gram premises in §3, the following explicit inequality holds for **all** original complex-rank≤2 C and **every** such P:

`q3(C) >= [41960431118628029 / 14774058577588912128000] · Δ(P,C)`.   (3)

The RHS is an expression in original operators only; no choice of auxiliary basis/lift appears. It is homogeneous of degree2 in C. It can vanish for nonzero C, and §7 proves that `Δ=0` is **not sufficient** for `q3=0`. Thus (3) is neither a universal strictly positive q3 gap nor an equality classification. In particular, the source-independent lemma (2) **does not prove** the original q3 positivity target; that conclusion from (3) retains every source-certificate premise and review boundary.

## 2. Physical lift and same-pair structure

If C is nonzero, first rescale it to `||C||HS²=1/2`. Choose any isometry `A:Q=C²→H` with `AA†=P`, and put

`a=vec(A)/sqrt2`, `b=sqrt2 vec(C†A)` in H⊗Q,
`a_r=(I⊗<r|)a`, `b_r=(I⊗<r|)b`.

Then `||a||=||b||=1`, `Tr_H|a><a|=I_Q/2`, and `C_xy=Σ_j a_(x,j) conjugate(b_(y,j))`. Indeed `||b||²=2 Tr(A† C C† A)=2||C||HS²=1`, and the reconstruction is `AA†C=PC=C`. The same a,b must be used simultaneously in every moment and Gram block. Every physical lift with first marginal I/2 that reconstructs C arises from such an isometry A. Rank1 is handled by isometric completion; C=0 is immediate. At the end, positive homogeneity removes the normalization for (3).

For r and s orthogonal unit vectors in Q, the exact marginal gives `||a_s||²=1/2`. Define

`a_j=(I⊗<e_j|)a`, `b_j=(I⊗<e_j|)b`,
`w00=A3(a0⊗b0)`, `w01=A3(a0⊗b1+a1⊗b0)`, `w11=A3(a1⊗b1)`.

The unit-sphere Haar moments in C² imply

`W(a,b) := ∫_(R∈U(2)) ||A3(a_(R†e0)⊗b_(R†e0))||² dR`
` = (||w00||²+||w11||²)/3 + ||w01||²/6`.                         (4)

Indeed, the coordinate phases kill mixed terms and `E|r0|⁴=E|r1|⁴=1/3`, `E|r0r1|²=1/6`. No independence of these vector equations is claimed.

## 3. Exact source-conditional premises and the one physical block

The following are **premises**, not conclusions independently adopted here:

1. For the same physical pair a,b, form the three four-replica source moments from `aaab`, `aabb`, `bbba`, applying the common normalized `U(4)^3×U(2)` Haar twirl and the uniform average over the six physical-site permutations and simultaneous conjugation/no conjugation; multiply by `L=(2·4³)^4=128⁴`.
2. On this actual tuple X, the exact fixed-d4 source certificate identity is `q3(C)=Σ_(t=1)^1237 Tr[Z_t B_t(X)]`, after the source equality terms vanish. Every actual compressed physical Gram block B_t is PSD and every corresponding actual corrected rational multiplier Z_t is PSD. These assertions include the true coupled-Gram, source-equality, span and rational-identity dependencies; the packet does not treat a diagonal-only or an abstract unrelated Gram tuple as sufficient.
3. The actual **zero-based** type `pkg['types'][270]` is a single scalar family31 block with row `a* a* a b`, rank1, joint compression `[1]`, physical-site tensor `e3⊗e3⊗(e1⊗e0−e0⊗e1)` at each of the three sites and auxiliary tensor `e1⊗e1⊗e0⊗e0`. Its actual corrected scalar is

`z270 = 5994347302661147 / 9444732965739290427392 > 0`.

The source archive and corrected-data bytes are pinned in §8. Fixed e_j here are **certificate compression basis vectors**, not selected original target states. The frozen full source identity, all multipliers/physical PSD and their code/runtime/independent-review gates are not established merely by this packet. In particular, an upstream source failure invalidates (3), not the standalone lemma (2).

Keeping only this scalar block and the identity finite-symmetry branch, of weight `1/12`, gives the following conditional inequality. For `r=R†e0`, `s=R†e1`, and `U=(U1,U2,U3)∈U(4)^3`, define

`x(U)=⊗_i Ui†e3`,
`η(U)=⊗_i[(Ui†e1)⊗(Ui†e0)−(Ui†e0)⊗(Ui†e1)]`.

The actual row contraction is `conjugate(<x(U),a_s>)² · <η(U),a_r⊗b_r>`. Thus

`q3(C) >= (L z270/12) ∫_R∫_U |<x(U),a_s>|⁴ |<η(U),a_r⊗b_r>|² dU dR`. (5)

All retained terms are literal physical Gram squares. The block binding and the formal factorization are separately pinned in §8. Because η lies in ran A3, its second pairing is unchanged by replacing `a_r⊗b_r` with `A3(a_r⊗b_r)`.

## 4. The exact local 60-dimensional Haar frame

On `V=C⁴`, let `S=Sym²(V)⊗wedge²(V)` and `v=e3⊗e3⊗(e1⊗e0−e0⊗e1)`. Define normalized Haar twirling

`T=∫_(U∈U(4)) U^tensor4 |v><v| (U†)^tensor4 dU`.

T is supported on S, dim S=60, and the following exact operator identity holds on S:

`675 T²−60 T+I_S=0`, `Tr_S T=2`.                                     (6)

Since T is self-adjoint, its eigenvalues are `1/45` and `1/15`; the trace and dimension give multiplicities45 and15. In particular

`T >= (1/45) P_S`, `P_S=P_+^(replicas 0,1)⊗P_-^(replicas 2,3)`.    (7)

**Exact reproducible witness and imported theorem.** By the standard four-copy Schur–Weyl/permutation-commutant theorem, T is the Hilbert–Schmidt orthogonal projection of `|v><v|` onto the 24 permutation operators. Use `P_p |i0 i1 i2 i3>=|i_(p0) i_(p1) i_(p2) i_(p3)>`, and order p lexicographically. The exact Gram matrix is `G_pq=4^cycles(p^(-1)q)` and `G c=b`, `b_p=<v,P_p v>`. The solution c, in that order, is the following integer vector divided by360:

`[4,-4,-1,1,1,-1, 4,-4,-1,1,1,-1, -1,1,-1,1,0,0, 1,-1,1,-1,0,0]`.

Thus `T=Σ_p c_p P_p`. To make the finite matrix claim explicit, use the 60 orthogonal (not normalized) basis vectors `s_ij⊗a_kl`, where `i≤j`, `k<l`, `s_ii=e_i⊗e_i`, `s_ij=e_i⊗e_j+e_j⊗e_i` for i<j, and `a_kl=e_k⊗e_l−e_l⊗e_k`. Their Gram D is diagonal with 24 entries2 and36 entries4. For `H_ij=<basis_i,T basis_j>`, the exact Fraction witness verifies all 3600 entries of

`675 H D^(-1) H−60 H+D=0`, `H=H†`, `Tr(D^(-1)H)=2`.

It also checks all 24×24 permutation Gram entries directly against all 256 basis words, the 24 projection normal equations, and wrong-wedge-sign/wrong-polynomial-sign faults. Exact script/result hashes and limitations are in §8. This is an exact finite calculation conditional on the named ordinary commutant theorem, not a formal proof-assistant result or an independent review of the full source identity.

## 5. Uniform all-variable bound and explicit rational coefficient

Let `E=(wedge² C⁴)^tensor3`. For any u∈H and w∈E define

`I(u,w)=∫_(U∈U(4)^3) |<x(U),u>|⁴ |<η(U),w>|² dU`.

Regroup the four copies in `u⊗u⊗w` by site. Independent Haar integrations and (7) yield

`I(u,w) >= 45^(-3) || Π_i P_+^(i)(u⊗u) ||² ||w||²`.                  (8)

For any, not necessarily normalized, u, the swap trick gives

`||Π_i P_+^(i)(u⊗u)||² = (1/8) Σ_(S⊂{1,2,3}) Tr[(Tr_(S^c)|u><u|)²]`.

The empty and full subsets contribute `||u||⁴` each. Each one-site reduced operator has trace `||u||²` and purity at least `||u||⁴/4` by Cauchy–Schwarz; its complementary two-site reduction has the same nonzero spectrum by Schmidt decomposition. Therefore the sum is at least `(7/2)||u||⁴`, and

`I(u,w) >= [7/(16·45³)] ||u||⁴ ||w||² = (7/1458000)||u||⁴||w||²`. (9)

This bound is universal in u,w; no selected physical C, state or q3 value is evaluated. Apply it pointwise in (5) with `u=a_s`, `w=A3(a_r⊗b_r)`. The physical marginal gives `||a_s||⁴=1/4`. Hence

`q3(C) >= κ W(a,b)`,
`κ = 128⁴ · (1/12) · z270 · [7/(16·45³)] · (1/4)`
`  = 41960431118628029 / 2462343096264818688000`.                   (10)

A separate hash-bound exact Fraction check independently reads the actual saved z270 and verifies the rational arithmetic, with wrong finite-weight and lift-normalization faults detected; it does not itself establish any premise in §3.

## 6. Intrinsic Δ identity and unconditional nonnegativity

Let A and the normalized lift be as in §2. For r on the unit sphere of Q, write `t=conjugate(r)`. Then

`a_r⊗b_r=(A⊗C†A)(t⊗t)`,
`∫ |t⊗t><t⊗t| dμ(t) = (I+F_Q)/6`.

The second identity follows from unitary invariance and the symmetric subspace of C²⊗C², which has dimension3. Let F swap the complete H copies. Using `(A⊗A)F_Q=F(A⊗A)`, `AA†=P`, `PC=C` and `C†P=C†`, we obtain

`∫ |a_r⊗b_r><a_r⊗b_r| dμ(r)`
` = [P⊗C†C + (C⊗C†)F]/6`.                                        (11)

Trace against A3 and use `F A3=−A3`:

`W(a,b) = ∫ ||A3(a_r⊗b_r)||² dμ(r) = Δ(P,C)/6`.                    (12)

This proves Δ≥0 and eliminates the lift/auxiliary basis. Combining (10) and (12) proves (3) for normalized C, and homogeneous scaling proves it for all original C.

A more general **source-independent** operator proof of (2), not requiring rank2 or d4, is useful for review. For any finite-dimensional H, any C and any orthogonal projection P with PC=C, choose an isometry A onto ran P (dimension n≥1). Then

`P⊗C†C + (C⊗C†)F = (A⊗C†A)(I+F_(C^n))(A⊗C†A)† >= 0`.    (13)

For any PSD K on H⊗H with `F K=−K`, its trace against (13) gives

`Tr[ K(P⊗C†C−C⊗C†) ] >= 0`.                                      (14)

F and K are Hermitian, so `F K=K F=−K`; this also shows `Tr[K(C⊗C†)]` is real. The rank0 case has C=0. Taking K=A3 proves (2). Neither (13) nor (14) asserts q3 positivity.

The all-r necessary equality condition can be stated without a reference basis: if the source premises hold and `q3(C)=0`, then Δ=0, so by continuity of the nonnegative integrand in (12), `A3(a_r⊗b_r)=0` for every r and every physical lift. Equivalently `w00=w01=w11=0`. No converse follows.

## 7. Why Δ=0 is not a converse, unconditionally

For every orthogonal rank2 projection P, let `C=P/2`. Then `||C||HS²=1/2` and the two terms in (1) are equal, so `Δ(P,C)=0` identically. Nevertheless q3 is not identically zero over this family, and this is provable without selecting or evaluating a particular target operator.

Choose P with the invariant Haar distribution on the rank2 Grassmannian of H (global dimension N=64). Standard two-copy unitary invariance gives `E(P⊗P)=α I+β F`. The trace and swap-trace constraints are

`α N²+β N=4`, `α N+β N²=2`,
`α=127/131040`, `β=31/65520`.

Set `K=Π_i(I−F_i/2)`. For Hermitian P the partial-trace/swap identity has the **essential global swap**

`q3(P)=Tr[(P⊗P) F K]`.

Here `Tr K=(4²−4/2)³=2744` and `Tr(FK)=(4−4²/2)³=−64`. Therefore

`E q3(P/2) = [α Tr(FK)+β Tr K]/4 = 225/728 > 0`.                (15)

Hence at least one original normalized rank2 C has Δ=0 but q3(C)>0. This does not rely on the source certificate, does not exhibit or test a chosen target state, and does not assert q3≥0 for every projector. The separate exact Fraction scalar check in §8 verifies the trace constraints, the rational average and detection of the missing-global-swap error. Consequently **Δ=0 is rigorously insufficient** for q3 equality; the bound cannot be read as a complete classification.

## 8. Frozen inputs, exact checks and trust limits

- Source archive v3/v4 identical SHA256 `2314805738a4f41b79eb3c1593e694ad337fe6f52d13e18a70db1acc726ff5e3`; corrected multipliers/equalities `frontier-20261028-d4-corrected-multipliers-and-equalities.json.xz`, SHA256 `c70c12a06273faa34bed204268188ee8c6b1732f07b2ceda453f163676024f94`. The earlier source/physical-identity candidate is `frontier-20261028-d4-consolidated-proof-dossier-v3.md`, SHA256 `5fd7eae54aecf154113461982fb429704dfe0cf53bbc786281c54356e280b223`. Its source/whole-identity status remains UNREVIEWED as a premise here.
- Source block270 data-only binding: `frontier-20261028-d4-equality-block270-source-check.py`, SHA256 `7b40a6423924848644149bfcd742f8ea44fad7ac825838b07b60568692464cc6`; result SHA256 `8a112e9e3e5acafefd0c27ddfc4e9a0c2754c33bfd85ae2a655749a1064c2316`. Zero-based index clarification SHA256 `eb7b5084c85ab2dbc603b66b6bef925c7e64fcea88322dba89298368f8bb66b6`.
- Formal arbitrary-complex 8-monomial block-contraction check: `frontier-20261028-d4-equality-block270-formal-factor-check.py`, SHA256 `21724deb47beaeed9978eb6f397c8048db3c5da06b87bcb8351b1d555aa02e69`; result SHA256 `42fad675d517bf6cc213aeac2565f9fef8bba30923f1208119fdadb0aee36ae0`. These check the fixed source row and its contraction, not the whole certificate.
- Exact local-frame script `frontier-20261028-d4-local-haar-frame-rational-check-v1.py`, SHA256 `138961ee025273a0b11ea8c66867524a04ed537879e2b088fe75106633b87351`; result SHA256 `ed3a75e270ace86ef9dbdde8af137405ef7cba9b90dff5727704889a3e999b74`, PASS. All 3600 polynomial-identity entries are zero; wrong wedge sign produces60 nonzero entries and wrong polynomial sign156.
- Corrected-scalar/constant script `frontier-20261028-d4-coercive-constant-source-check-v1.py`, SHA256 `f152b9a972d8107a92f99f1f5abade854c4b5bc070f77e2582f9327770dab93d`; result SHA256 `065d87613a108cf585e14d59ebba323a903094af61991c7a67a37080cd489bc0`, PASS.
- Projector-Haar scalar arithmetic script `frontier-20261028-d4-rank2-projector-haar-mean-check-v1.py`, SHA256 `430ab241ac55578684bf22f5fae7a2116463c72f51972a9b0f473174998fb7b9`; result SHA256 `3fdb26ac67b4dca2d69d0b120ff09eaa91afbb36040be08bd4c8b51c91e39207`, PASS. This checks the exact scalar algebra assuming the written two-copy twirl/swap facts.

All computations above used integer/Fraction exact arithmetic, with no selected target C/q3 computation. Their scope is as stated, not source-wide theorem verification, a Lean/kernel proof, an independent mathematical-family/human review or novelty clearance. The prior public Tomar full-target claim means no new-discovery status; neither that source nor this packet is thereby correctness-accepted. Historical process/held findings and their NONINPUT boundaries remain unchanged. No all-d, operational distillability, f62-scope expansion, f153 result or parent-adoption claim is made.
