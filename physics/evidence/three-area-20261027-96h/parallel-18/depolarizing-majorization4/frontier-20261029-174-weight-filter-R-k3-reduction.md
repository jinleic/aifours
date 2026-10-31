# The weight filter R = M_2 − M_3: exact identities, a conditional reduction of original k3 to one layer bound, and a sharp positivity conjecture

Owner **PhysicsDepol4-2**, physics-2. This packet was assembled after the native clock `Thu Oct 29 08:47:05 PDT 2026`. Earlier work in the session is described below, but it is not dated by this record.

**Status: AUTHOR-WRITTEN.** §§1–3 and §5 are exact written derivations. §4 is floating-point evidence only. The positivity of R in §4 is a **CONJECTURE**, not a theorem. Nothing here is adopted, independently reviewed, kernel-checked or novelty-cleared. Zhang's matched clipped-tail public claim remains the governing attribution caveat for this slot. The original unrestricted k3 problem remains **OPEN**.

## 0. Notation

- Channel and inputs: Φ_p(X) = (1−p)X + (p/2)Tr(X)I and Λ_p = Φ_p^{⊗4}. Inputs ρ are four-qubit states.
- Decomposition: for p ∈ [0,1] put t = 1−p. Then Λ_p = Σ_m t^{4−m}(1−t)^m T_m, where T_m = Σ_{|S|=m} E_S and E_S(X) = Tr_S(X)⊗I_S/2^{|S|}.
- Layer quantities: for a rank-three orthogonal projector P, t_m := Tr(P T_m(ρ)).
- Marginal sums: M_k(ρ) := Σ_{|S|=k} ρ_S ⊗ I_{S^c}, with unnormalised identities. Hence M_0 = Tr(ρ)I, M_4 = ρ, M_3 = 2T_1 and M_2 = 4T_2.
- Spin flip: ρ̃ = Y^{⊗4}ρ^T Y^{⊗4} and ψ̃ = Y^{⊗4}ψ̄. The map Θ = Y^{⊗4}∘(complex conjugation) is antiunitary with Θ² = 1.
- Pure-state data: for pure ρ = ψψ†, r_i is the Bloch vector of qubit i, S = Σ|r_i|², C = |⟨ψ̃|ψ⟩|², D = ½Σ_i r_i·σ_i and Δ = ψ̃ψ̃† − ψψ†.
- Product reference: P_0 = span{|0000⟩,|1000⟩,|0100⟩} on |0000⟩ gives (t_m) = (1,3,3,5/4,3/16). The original k3 statement is Σ_m t^{4−m}(1−t)^m t_m ≤ Σ_m t^{4−m}(1−t)^m c_m with c = (1,3,3,5/4,3/16). This is the f5 parent setup. Mirror p ↦ 2−p covers p ∈ [1,4/3].

## 1. Exact Pauli-weight form

Every map above is diagonal on Pauli strings, with an eigenvalue that depends only on the weight w = 0,…,4.

- E_S keeps a string iff its support is disjoint from S, so T_m has eigenvalue C(4−w, m).
- M_k has eigenvalue 2^{4−k}·C(4−w, k−w).

Hence

`R := M_2 − M_3 = 4T_2 − 2T_1` has weight eigenvalues `(16, 6, 0, −2, 0)`. (1)

The four-qubit universal inverter is ρ̃ = M_0 − M_1 + M_2 − M_3 + M_4: its weight eigenvalues are (−1)^w, as a direct check of the five weights shows. Therefore

`R = M_1 − Tr(ρ)I − ρ + ρ̃`. (2)

For pure ρ = ψψ†, M_1 = Σ_i (I + r_i·σ_i)/2 ⊗ I_rest = 2I + D. This gives

`R(ψψ†) = I + D + ψ̃ψ̃† − ψψ†`. (3)

**Spectral symmetry.** Each single-site Pauli satisfies ΘσΘ^{-1} = −σ, so ΘDΘ^{-1} = −D. Also Θψψ†Θ^{-1} = ψ̃ψ̃† and Θψ̃ψ̃†Θ^{-1} = ψψ†. Hence ΘRΘ^{-1} = 2I − R. An antiunitary similarity preserves the real spectrum, so

`spec R(ψψ†) = 2 − spec R(ψψ†)`. In particular **R ≥ 0 ⇔ R ≤ 2I ⇔ ||D + Δ|| ≤ 1.** (4)

**Odd-weight Kramers orthogonality.** ⟨ψ̃|Pψ⟩ = ψ^T(Y^{⊗4}P)ψ. Each factor Yσ^a (a = x,y,z) is symmetric and Y is antisymmetric, so Y^{⊗4}P has transpose sign (−1)^{wt P}. Therefore **⟨ψ̃|Pψ⟩ = 0 for every odd-weight Pauli string P**. In particular ⟨ψ|D|ψ̃⟩ = 0. (5)

**Bilinear and diagonal forms.** For states ρ, σ:

`Tr(R(ρ)σ) = Σ_{|S|=2} Tr(ρ_Sσ_S) − Σ_{|S|=3} Tr(ρ_Sσ_S)`.

For pure ρ, Schmidt duality gives Tr(ρ_R²) = Tr(ρ_i²) for R = î. The inverter gives C = 2 − 2Σ_iTrρ_i² + Σ_{|S|=2}Trρ_S². Together these yield

`⟨ψ|R|ψ⟩ = C + S/2 ≥ 0`. (6)

## 2. Two exact reformulations

**(a) Dependence on α − β only.** Put α = ψψ† and β = ψ̃ψ̃†. Since Tr(σβ) = −Tr(σα) for single-site σ, D = ¼Σ_i Tr(σ_i(α−β))σ_i. Also Δ = −(α−β). So R − I is **linear in α − β**.

- α − β is traceless of rank ≤ 2, and Θ-odd. Its eigenvalues are ±√(1−C), with eigenvectors ξ and Θξ = ξ̃, so ξ ⊥ ξ̃.
- Hence α − β = √(1−C)(ξξ† − ξ̃ξ̃†), and

`R(ψψ†) − I = √(1−C)·(R(ξξ†) − I)` with ⟨ξ̃|ξ⟩ = 0. (7)

Combined with (4), the following are **equivalent**:

1. R(ψψ†) ≥ 0 for every pure ψ.
2. ||R(ξξ†) − I|| ≤ 1 for every pure ξ with C(ξ) = 0.
3. λ_min R(ψψ†) ≥ 1 − √(1−C(ψ)) for every pure ψ.

Statement 3 is equality for every one-uniform state, where D = 0 and R = I + Δ.

**(b) Bipartite form across 12|34.** The two-qubit inverter gives (α−β)_{12} = ρ_{12} − ρ̃_{12} = ½(r_1·σ_1 + r_2·σ_2), and similarly on 34. Hence

`D + Δ = 𝒟(α − β) = 𝒟(α) − Θ𝒟(α)Θ^{-1}`, where `𝒟(X) = X_{12}⊗I + I⊗X_{34} − X`. (8)

**(c) Magic-basis real form.** Use the two-qubit magic basis on 12 and on 34. Then Θ is complex conjugation, local SU(2)^4 acts as Ψ ↦ O_1ΨO_2^T with O_i ∈ SO(4), and ψ ↔ Ψ = A + iB with A, B real 4×4. Formula (8) becomes

`R − I = 2i·T_{A,B}`, where `T_{A,B}(M) = A⟨B,M⟩ − B⟨A,M⟩ − (AB^T−BA^T)M + M(A^TB−B^TA)` (9)

and T_{A,B} is a real antisymmetric 16×16 map. For the derivation, Im(ΨΨ†) and Im(Ψ^TΨ̄) are the magic forms of the 12 and 34 Bloch parts. The checker reproduces (9) to rounding.

So the conjecture (statement 1) is the clean real-matrix statement:

**CONJECTURE R.** For real 4×4 matrices A ⊥ B (Frobenius), ||T_{A,B}||_op ≤ |A|·|B|.

## 3. Conditional consequences (exact, assuming R ≤ 2I for pure inputs)

1. **Layer transfer.** Linearity gives 4T_2(ρ) ≤ 2T_1(ρ) + 2Tr(ρ)I for every state. For any rank-three P, therefore, **t_2 ≤ (t_1 + 3)/2**.
2. **Reduction of original k3.** For t ∈ [0,1] the weights t^{4−m}(1−t)^m are nonnegative, and the following are already in place:
   - t_0 = Tr(Pρ) ≤ 1;
   - t_3 ≤ 5/4 (adopted f5);
   - t_4 = 3/16.

   So the original k3 comparison at every physical p, with the mirror for p ∈ [1,4/3], follows from **the single layer bound t_1 ≤ 3**, i.e. K_3(T_1(ρ)) ≤ 3, i.e. K_3(Σ_i ρ_î⊗I_i) ≤ 6, for every pure four-qubit ρ. This bound is **not proved here**. Bounded numerics (earlier session) put its maximum at product states, with value 3.
3. **Universal spin-flip condition.** From (2), H1(ρ) + ρ̃ = I + R + ρ ≤ 3I + ρ, so λ_2(H1(ρ)+ρ̃) ≤ 3 for every pure ρ. This would remove the harmonic/spin-flip hypothesis from 121's region H, leaving 4S+8C ≤ 64/9. Note that 121's reviewed scopes do not depend on this conditional statement.

## 4. Evidence for CONJECTURE R (diagnostics only)

The checker is `frontier-20261029-173-weight-filter-R-checks.py`. Its residuals and bounded descent are reported in checkpoint 175. Earlier in-kernel exploration of this session found:

- **Random sampling and descent.** λ_min R ≈ 0.03–0.3 on random states. Descent from about 150 structured and random starts reached minima of order 10^{-14}, with **no negative value**.
- **The sharpened bound is tight.** The descent minimisers all have C = 0. The sharpened statement λ_min ≥ 1−√(1−C) held to 10^{-15} under maximisation of its violation, and is tight on a large set beyond one-uniform states:
  - equal radii 0.218 with C = 0.258, Bloch-frame support on even strings;
  - the family √(1−ε)|0000⟩ + √ε|1111⟩, where equality is exact by hand.
- **Diagonal case.** The pure-state bound S + 2C ≤ 4, i.e. ⟨ψ|R|ψ⟩ ≤ 2, follows from summed three-qubit Breuer–Hall (Kramers) inequalities. The bound O_2 ≥ O_3 follows from C ≥ 0. Both are written here and are exact.

## 5. Exact obstructions to easy proofs

1. **R is not decomposable.** After local-unitary and permutation averaging, a decomposition R = CP + CP∘(transpose) would have to be a nonnegative combination of the ten weight vectors of covariant CP / co-CP maps. Exact enumeration of all 252 bases of the 5×10 system finds **no** nonnegative basic solution. The checker repeats this LP.
2. **Extended cone.** An in-kernel exact Phase-I simplex added further generators:
   - local-unitary-averaged Breuer–Hall maps on pair, triple and full marginals (antisymmetric V with an odd number of Y factors);
   - compositions of these with covariant CP twirls.

   It returned a positive optimal artificial value of 2, i.e. **R is outside that cone**. This in-kernel LP is not packaged as a separate checker; it is reported as an exploration, not a certificate.
3. **The naive bipartite range bound fails.** Equation (8) would give ||D+Δ|| ≤ λ_max(𝒟(α)) − λ_min(𝒟(α)), which is not small enough:
   - In the Schmidt basis across 12|34, 𝒟(χχ†) has eigenvalues μ_k+μ_l (k≠l) and the eigenvalues of 2diag(μ) − √μ√μ^T.
   - For μ = (2/5, 3/10, 1/5, 1/10), exactly Σ_k μ_k/(2μ_k + 3/10) = 1366/1155 > 1. So the smallest secular root lies below −3/10, and the spectral range exceeds 7/10 + 3/10 = 1.
   - Any proof must therefore use the coupling between the Schmidt data and Θ, not only the spectrum of 𝒟(α).

## 6. Exact remaining gaps

1. Prove CONJECTURE R, in any of the equivalent forms (4), (7) or (9).
2. Prove t_1 ≤ 3, i.e. K_3(Σ_iρ_î⊗I_i) ≤ 6 for pure ρ.

(1) and (2) together would give the original all-density, all-projector, all-physical-p k3. This is a conditional reduction, not a solution.

## 7. Boundaries

This packet uses only elementary finite-dimensional linear algebra, the universal inverter, Schmidt duality, and the adopted f5 three-erasure bound. The numerics are floating-point diagnostics; the LP and secular inequality are exact rational computations. No prior held body is a premise. The 121 review result (f155) is consulted for status only. All earlier corrections, cadence findings and withdrawals remain:

- corrections 125, 127, 128, 130 and 133;
- cadence findings 132 and 143, and the parent classification of 132 as PROCESS MAJOR;
- the 147 clarification and the 149 withdrawal.

No formal, kernel, human, independent-family or novelty acceptance is claimed.
