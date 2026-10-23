# The two-qutrit 2-unitary orbit is isolated among dual and among T-dual unitaries (T7, d = 3)

Status: CANDIDATE (lane write-up, 2026-10-17 PDT; 01:3x erratum: M_{14} formula in §1.4 corrected, conclusion unchanged). Pending: parent re-derivation, Claude hostile review, priority
audit. Hand proof (§§1–5) plus two independent exact computer confirmations (§6) and controls (§7).

## 0. Statement

Let `V = M_9(C)` (Frobenius norm), `U^R`, `U^Γ` the reshuffling and partial transpose of arXiv:2508.04777v3
(`⟨ij|U^R|αβ⟩ = ⟨iα|U|jβ⟩`, `⟨iβ|U^Γ|jα⟩ = ⟨iα|U|jβ⟩`),
`D = {U ∈ U(9) : U^R ∈ U(9)}` (dual unitaries), `T = {U ∈ U(9) : U^Γ ∈ U(9)}` (T-dual unitaries),
`G = U(3)^2 × U(3)_op^2` (opposite multiplication on the two right factors) acting by `g·U = (v1⊗v2) U (v3⊗v4)`, `P9` = matrix (C7) of the source, `O9 = G·P9`. This is a compact connected Lie group isomorphic to `U(3)^4`; the opposite factors make the displayed transformations a genuine left action.

**Theorem 1.** `O9` is relatively open in `D` and in `T`. Equivalently, there is `ε > 0` such that every dual unitary
(resp. T-dual unitary) `U` with `dist(U, O9) < ε` lies in `O9`. Moreover `O9` is a connected component of `D` and of `T`.

**Corollary 2** (uses Rather–Ramadas–Kodiyalam–Lakshminarayan, arXiv:2212.06737v2 = source ref. [44], Theorem 1:
every 2-unitary of order 9 lies in `O9`). `sup{e_p(U) : U ∈ D, U not 2-unitary} < 1` and
`sup{e_p(U) : U ∈ T, U not 2-unitary} < 1`, with `e_p` as in source eq. (11a). No value of the gap is claimed.

**Answer to T7 (d = 3).** Literal reading ("dual/T-dual gates arbitrarily close to P9"): yes, trivially — `(v⊗I)P9 → P9`
as `v → I`, and these are 2-unitary. Non-trivial reading (non-2-unitary dual/T-dual gates arbitrarily close to P9, or to
the 2-unitary set): **no** — by Theorem 1 (any dual/T-dual gate within ε of `O9` is in `O9`, hence 2-unitary) and,
for "the 2-unitary set", by Theorem 1 together with [44].

## 1. Conventions and elementary facts

**1.1 Indices.** `|ij⟩ ↔ 3i + j`; `(A⊗B)[(i,α),(j,β)] = A[i,j] B[α,β]`; `P[row][col] = 1` iff `P|col⟩ = |row⟩`.

**1.2 P9.** The source's (C7) has its ones at (row, col) = (0,0),(1,8),(2,4),(3,5),(4,1),(5,6),(6,7),(7,3),(8,2),
i.e. `P9|ab⟩ = |2a+b, a+b⟩` (arithmetic mod 3). Its code `C = {(a, b, 2a+b, a+b) : a, b ∈ F3} ⊂ F3^4` is a linear
`[4,2,3]_3` MDS code (every nonzero codeword has weight ≥ 3: the generator `[[1,0,2,1],[0,1,1,1]]` has all 2×2 minors
nonzero). The source's other descriptions of "P9" (state (14), the verbal permutation of Sec. III A, and [44] eq. (A14))
equal `(Π1⊗Π2) P9 (Π3⊗Π4)` for explicit local permutation matrices (found by exhaustive search, `evidence/implA.json`),
so all lie in `O9`.

**1.3 LU covariance.** Directly from the definitions, for all `v_k ∈ M_3(C)` and `U`:
`((v1⊗v2)U(v3⊗v4))^R = (v1⊗v3^T) U^R (v2^T⊗v4)` and `((v1⊗v2)U(v3⊗v4))^Γ = (v1⊗v4^T) U^Γ (v3⊗v2^T)`.
(Proof for R: entry `[(i,j),(α,β)]` of the left side is `Σ v1[i,i'] v2[α,α'] U[(i',α'),(j',β')] v3[j',j] v4[β',β]`
`= Σ v1[i,i'] v3^T[j,j'] U^R[(i',j'),(α',β')] v2^T[α',α] v4[β',β]`; Γ is identical with the roles of the indices
permuted.) Hence for `g ∈ G` the map `Φ_g(U) = g·U` is a linear Frobenius isometry of `V` with `Φ_g(D) = D`,
`Φ_g(T) = T`, `Φ_g(O9) = O9`. Since P9, P9^R, P9^Γ are permutation matrices (checked), `O9 ⊆ D ∩ T`.

**1.4 Four-party dictionary.** Put `ψ_U(a,b,c,d) = U[(c,d),(a,b)]` (source eq. C8 up to the factor 1/3); parties
1,2,3,4 = a,b,c,d. For a 2-subset `S` let `M_S` be the 9×9 reshaping with rows indexed by the S-coordinates. Then
`M_{12} = U^T`, `M_{13} = S9 U^R S9`, `M_{14} = (U^Γ)^T S9` (S9 = swap; e.g. `M_{14}[(a,d),(b,c)] = U[(c,d),(a,b)] = U^Γ[(c,b),(a,d)]`), so `U ∈ U(9)` ⟺ `M_{12}` unitary,
`U^R` unitary ⟺ `M_{13}` unitary, `U^Γ` unitary ⟺ `M_{14}` unitary. (E.g. `M_{13}[(a,c),(b,d)] = U[(c,d),(a,b)] =
U^R[(c,a),(d,b)]`.) A square `M_S` is unitary iff `ρ_S := M_S M_S^† = I`. For `U = P9`, `ψ = 1_C` (indicator of C).

## 2. The linearized constraints at P9

Write `X ∈ V` as a perturbation `ψ ↦ ψ + δψ` (`δψ(a,b,c,d) = X[(c,d),(a,b)]`, a real-linear isometry `V ≅ C^{F3^4}`).
The derivative of `U ↦ M_S M_S^† − I` at `P9` is `δψ ↦ E_S`, `E_S(s,s') = Σ_t [ψ(s,t) conj δψ(s',t) + δψ(s,t) ψ(s',t)]`,
`s, s' ∈ F3^S`, `t ∈ F3^{S̄}`. (At a unitary point, `ker d(MM^†)` = `ker d(M^†M)`, so this is the same kernel as for
`U†U − I` and `U^R†U^R − I`.)

Because C is MDS, for every 2-set S the projection `C → F3^S` is bijective; let `f_S(s)` be the S̄-part of the codeword
with S-part s, `π_S(y)` the codeword agreeing with `y` on S, and

`τ_S(y) := the point with S-part (π_{S̄}(y))_S and S̄-part (π_S(y))_{S̄}`  (an involution of F3^4 fixing C pointwise).

**Lemma 2.1.** `δψ ∈ ker E_S` iff (a) `Re δψ(c) = 0` for all `c ∈ C`, and (b) `δψ(y) = −conj δψ(τ_S y)` for all `y ∉ C`.

*Proof.* `ψ(s,t) = 1` iff `t = f_S(s)`. For `s = s'`: `E_S(s,s) = 2 Re δψ(s, f_S(s))`. For `s ≠ s'`:
`E_S(s,s') = conj δψ(s', f_S(s)) + δψ(s, f_S(s'))`. The point `y = (s, f_S(s'))` ranges exactly over `F3^4 \ C` as
`(s, s')` ranges over pairs with `s ≠ s'` (y determines `s = y_S` and `s' = f_S^{-1}(y_{S̄})`), and
`(s', f_S(s)) = τ_S(y)`. ∎

**Lemma 2.2 (perfect code).** C is perfect: the 9 radius-1 Hamming balls around codewords are disjoint (distance 3) and
have `9·(1 + 4·2) = 81` points. So every `y ∉ C` is uniquely `y = c + t e_q` (`c ∈ C`, `q ∈ {1,2,3,4}`, `t ∈ {1,2}`).
For `q ≠ q'` let `g_{q,q'} ∈ C` be the codeword with entry 1 at `q` and 0 at `q'`. Let `σ_S(q)` be the partner of `q` in
the matching `{S, S̄}`. Then
`τ_S(c + t e_q) = (c + t g_{q,σ_S(q)}) − t e_q`,
i.e. in coordinates `(c, q, t) ↦ (c + t g_{q,σ_S(q)}, q, −t)`.

*Proof.* Let `S_q ∈ {S, S̄}` be the part containing q. On the part not containing q, y agrees with c, so `π` of that
part is `c`. On `S_q`, `y = c + t e_q`, so `π_{S_q}(y) = c + t g_{q,σ_S(q)}` (linearity; `e_q` restricted to `S_q` is
"1 at q, 0 at its partner"). Assembling: on `S_q`, `τ_S(y)` takes the values of `c`; on the other part it takes the
values of `c + t g_{q,σ_S(q)}`. Since `g_{q,σ_S(q)}` vanishes at `σ_S(q)` and equals 1 at `q`, this point equals
`c + t g_{q,σ_S(q)} − t e_q`. ∎

**Lemma 2.3.** Let `{S, S̄} ≠ {S', S̄'}` be two of the three perfect matchings of {1,2,3,4} (for D: 12|34 and 13|24;
for T: 12|34 and 14|23). Then `H = ⟨τ_S, τ_{S'}⟩` has order 6 and acts freely on the 72 points of `F3^4 \ C`; hence
there are exactly 12 orbits, each of size 6.

*Proof.* Distinct perfect matchings of a 4-set share no pair, so `σ_S(q) ≠ σ_{S'}(q)` for every q. By Lemma 2.2,
`ρ := τ_S τ_{S'}` maps `(c,q,t) ↦ (c + t w_q, q, t)` with `w_q = g_{q,σ_{S'}(q)} − g_{q,σ_S(q)} ∈ C`, and `w_q ≠ 0`: a
codeword equal to both `g`'s would have a 1 at q and zeros at two other places, weight ≤ 2, contradicting distance 3.
In characteristic 3, translation by `t w_q ≠ 0` has order 3 and no fixed point; the six elements
`1, ρ, ρ², τ_S, τ_S ρ, τ_S ρ²` are distinct (`τ_S` flips t, ρ does not), close under multiplication
(`τ_S ρ τ_S = τ_{S'} τ_S = ρ^{-1}`), and the three reflections map `(·,q,t)` to `(·,q,−t)`, `−t ≠ t`, so they also have no
fixed point. Every non-identity element is fixed-point-free on `F3^4 \ C`. ∎

**Proposition 2.4.** `dim_R ker dF_D(P9) = dim_R ker dF_T(P9) = 33`.

*Proof.* By Lemma 2.1 for the two cuts, `δψ` lies in the kernel iff `Re δψ = 0` on C (both cuts give the same condition)
and, for `y ∉ C` and every generator, `δψ(τ y) = −conj δψ(y)`. Iterating, `δψ(h y) = δψ(y)` for `h` a product of an even
number of generators and `−conj δψ(y)` for an odd number. Because the action is free (Lemma 2.3) each point of an orbit
is `h y_0` for a unique `h`, so these prescriptions are consistent and any value `δψ(y_0) ∈ C` extends to the orbit;
conversely every such `δψ` satisfies (b) for both cuts. So the kernel is `iR^C ⊕ ⊕_{12 orbits} C`, of real dimension
`9 + 2·12 = 33`. ∎

## 3. The orbit tangent

**Proposition 3.1.** `dim_R T_{P9} O9 = 33` (so the stabilizer of P9 in G has Lie algebra of dimension 36 − 33 = 3,
the phases).

*Proof.* In the dictionary, `g·U` corresponds to applying `v3^T, v4^T, v1, v2` to parties 1,2,3,4, so `T_{P9}O9` is the
image of `(h_1,…,h_4) ∈ u(3)^4 ↦ Σ_q h_q^{(q)} ψ` (`u(3)` is closed under transposition). At a codeword `c` the value is
`Σ_q h_q[c_q, c_q]` (changing one coordinate of a codeword leaves C). At `y = c + t e_q` the value is `h_q[c_q + t, c_q]`
(for `q' ≠ q`, `y` with coordinate `q'` changed is never a codeword, by distance 3 and uniqueness in Lemma 2.2).
Off-code part: the 12 complex parameters `z = h_q[u,v]` (`u < v`; `h_q[v,u] = −z̄`) have pairwise disjoint supports (the
point `(c,q,t)` determines q and the ordered pair `(c_q + t, c_q)`), so this part is injective: real dimension 24.
Code part: `(θ_q) ↦ (i Σ_q θ_q(ℓ_q(c)))_{c∈C}` with `ℓ_q` the coordinate functionals `a, b, 2a+b, a+b` on `C ≅ F3²`.
These are representatives of all four points of `P¹(F3)`, so every additive character `x ↦ ω^{w·x}` of `F3²` is a
function of one `ℓ_q`; hence these sums span all functions on C, and the code part has real dimension 9. The two parts
have disjoint supports: total 24 + 9 = 33. ∎

**Corollary 3.2.** `T_{P9}O9 = ker dF_D(P9) = ker dF_T(P9)`. (`O9 ⊆ D ∩ T` gives `T_{P9}O9 ⊆ ker`; dimensions agree.)

## 4. Proof of Theorem 1

Let `F(U) = (U†U − I, U^R†U^R − I) ∈ Herm_9 × Herm_9` (real polynomial map, `R^162 → R^162`), so `D = F^{-1}(0)`, and
`dF_{P9}` has rank `162 − 33 = 129` (Prop. 2.4). Choose 129 real components of F whose differentials at P9 are
independent (`evidence/implA.json`: an explicit 129×129 minor with determinant 512) and let `F'` be that subsystem.
By the implicit function theorem there is an open `W_1 ∋ P9` such that `N = F'^{-1}(0) ∩ W_1` is an embedded
33-dimensional submanifold, and `D ∩ W_1 ⊆ N`.
`O9` is the orbit of the compact connected Lie group G, hence a compact connected embedded submanifold of V, of
dimension 33 (Prop. 3.1; the orbit map has constant rank by equivariance). `O9 ∩ W_1 ⊆ D ∩ W_1 ⊆ N`; the inclusion
`O9 ∩ W_1 → N` is an injective immersion between 33-manifolds, hence open. So there is an open `W_2 ∋ P9` with
`N ∩ W_2 ⊆ O9`, and therefore `D ∩ W_2 = O9 ∩ W_2`.
For `Q = g·P9 ∈ O9`, `Φ_g(W_2)` is an open neighbourhood of Q with `D ∩ Φ_g(W_2) = O9 ∩ Φ_g(W_2)` (§1.3). The union
`W` of these sets is open, contains O9, and `D ∩ W = O9`. Since O9 is compact, `ε := dist(O9, V \ W) > 0`, and every
`U ∈ D` with `dist(U, O9) < ε` lies in `D ∩ W = O9`. Thus O9 is relatively open in D; it is compact, hence closed, and
connected, so it is a connected component of D.
**T-dual case.** Identical with `U^Γ` in place of `U^R` (Prop. 2.4 covers the cut 14|23). Independent route: the
identity `(US)^R = U^Γ S` (S = swap; checked symbolically from the definitions and exactly on random integer matrices)
shows that `U ↦ US`, a Frobenius isometry, maps T onto D; and `P9·S = (Π1⊗Π2)P9(Π3⊗Π4)` for explicit local
permutations (`evidence/implA.json`), so `O9·S = O9`. Hence the T statement is the image of the D statement. ∎

## 5. Proof of Corollary 2

**Lemma 5.1.** For unitary U of order `d²`: `E(U) ≤ E(S)` with equality iff `U^R` is unitary, and `E(US) ≤ E(S)` with
equality iff `U^Γ` is unitary; hence `e_p(U) ≤ 1` with equality iff U is 2-unitary.
*Proof.* `A = U^R U^R†` is positive semidefinite with `Tr A = ‖U^R‖_F² = ‖U‖_F² = d²` (R permutes entries). Cauchy–Schwarz
on the `d²` eigenvalues: `Tr A² ≥ (Tr A)²/d² = d²`, equality iff `A = I`. So `E(U) = 1 − Tr A²/d⁴ ≤ 1 − 1/d² = E(S)`.
Same for Γ. Then `e_p = [E(U) + E(US) − E(S)]/E(S) ≤ 1`, equality iff both equalities hold. ∎
*Proof of Corollary 2.* `D \ O9 = D ∩ (V \ W)` is compact (W from §4) and non-empty (it contains the swap,
`e_p(S) = 0`). `e_p` is continuous, so its maximum on `D \ O9` is attained at some `U*`. If `e_p(U*) = 1`, then `U*` is
2-unitary (Lemma 5.1), so `U* ∈ O9` by [44, Theorem 1] — impossible. Hence the maximum is `< 1`. By [44] again,
`D \ O9` is exactly the set of non-2-unitary dual gates. Same for T (non-empty: the identity). ∎

Dependence: Theorem 1 does not use [44]. Corollary 2 uses [44, Thm 1] (peer-reviewed, PRA 108, 032412 (2023); proof read
in outline: reduction via non-existence of two-qutrit universal entanglers, Chen–Duan–Ji–Ying–Yu 2008; not re-proved).

## 6. Independent computer confirmation (exact; no floating point)

| | Impl. A (matrix picture, python-flint) | Impl. B (state picture, pure Python) |
|---|---|---|
| dual system at P9 (C7) | rank 129 exact (`fmpz_mat.rank`); 129×129 minor det = 512; kernel 33 | rank 129 mod 2^61−1 and mod 10^9+7 |
| T-dual system at P9 | rank 129; minor det 512; kernel 33 | rank 129 (both primes) |
| orbit tangent | 36 vectors, rank 33 (33×33 minor det = −27), `M·T = 0` exactly | 36 vectors exactly in kernel, rank 33 mod p |
| hand-proof structure | — | τ-group order 6, free on 72 off-code points, 12 orbits; explicit orbit basis (33 vectors) exactly in kernel, same span as tangent |
| cross-check | A's exact kernel basis (33 vectors) mapped to the state picture satisfies all of B's equations (0 violations, rank 33) | |

Certificate logic (B): `rank_Q(E) ≥ rank_p(E) = 129`, and 33 exactly verified kernel vectors of `rank_Q ≥ rank_p = 33`;
so `rank_Q(E) = 129`, kernel = their span. Same conclusion in A from the nonzero minors. Files: `evidence/implA.json`,
`evidence/implB.json`, `evidence/implA_kernels/`, hashes in `evidence/SHA256SUMS.txt`.

## 7. Controls

- **Source variants:** state (14), verbal Sec. III A, [44] (A14): all 2-unitary, explicit local-permutation images of (C7),
  identical ranks (129 / 33) in both implementations.
- **Wrong reshuffle:** replacing R by a column relabelling of U (cut 12|34 twice) gives kernel 81 ≠ 33 (A); an
  equivalent reshaping of the same cut 13|24 (`(U^R)^T`) gives 33. Unitarity alone: kernel 81 (A and B).
- **d = 4 negative control:** P16 from the `[4,2,3]_4` code `(a,b) ↦ (a+b, a+ωb)` over GF(4): 2-unitary; dual and T-dual
  kernels are 136 (A exact; B mod p, with the τ-group now a free Klein four-group: 16 + 2·60 = 136) versus orbit tangent 61
  (13 code dimensions, because the four coordinate functionals cover only 4 of the 5 points of `P¹(F4)`, plus 48). The
  method does **not** certify isolation. Moreover left enphasing directions `i E_rr P16` are in the kernel and raise the
  tangent rank to 64, so some explicit curve `diag(e^{iθ δ_r})·P16` of 2-unitaries has velocity outside `T O16` and
  therefore leaves `O16` for arbitrarily small θ: `O16` is not isolated in D or T (consistent with source ref. [62] and
  with [44]'s statement that enphasing yields LU-inequivalent 2-unitaries at d = 4). At d = 3 the same enphasing directions
  lie inside `T O9` (rank stays 33), consistent with [44]/[23].
- **Dual but not T-dual permutation** `(a,b) ↦ (b, a+b)`: dual kernel 45 vs its orbit tangent 29 — not certified (as expected
  for a gate that is not 2-unitary; no claim made).

## 8. Not claimed

No explicit ε or explicit entangling-power gap (source conjectures 15/16 attained by `U_s(2π/3)`; not addressed). No
statement about d = 5, 7 or general N. Novelty/priority: not established here — [44] already notes the 33-dimensional
manifold of 2-unitaries, and the source (25 Jun 2026) states the gap's rigorous existence is "yet to be established";
a priority audit is pending.
