**VERDICT: ACCEPT**

The separation `dist_F(U,O9) ≥ 1` follows exactly as written, for every `U ∈ D∖O9` and every `U ∈ T∖O9`.

- Every weight and factor checks out.
- The six-cycle multiplicities re-derive by hand.
- The singular-value step holds globally.

I found nothing blocking and nothing major. The items below are clarity edits I'd fold in before pinning. None of them changes a number or a logical step.

## Findings

**m1, minor: state the inner products behind J\*.**
- The constant 2 depends on convention.
- With the Frobenius output norm, the off-code blocks are `2Q`, `2L`, and λ⁺_min = 2.
- With unit weight on off-diagonal Re/Im coordinates they become `Q`, `L`, so λ⁺_min = 1. The matching remainder bound then gives only δ ≥ 1/√2.
- The addendum is consistent: the hand derivation uses Frobenius norms and the checker uses weight 2. The text just never says so.
- *Fix (end of §1, ¶1):* "J\* is the adjoint for ⟨X,Y⟩ = Re tr(X†Y) on M₉(ℂ) and ⟨(A,B),(A′,B′)⟩ = tr(AA′) + tr(BB′) on Herm₉²; 'orthogonal' always means for Re tr(X†Y)."

**m2, minor: bridge the conventions.**
- The addendum uses `UU†` and `U^R U^R†`.
- The pinned §2 formula is written for ρ_S = M_S M_S†, and pinned §4 uses U†U.
- *Fix (add to "Hand derivation"):* "UU† = M₃₄M₃₄†; U^R U^R† = Π ρ₁₃ Πᵀ and U^Γ U^Γ† = Π′ ρ₂₃ Π′ᵀ for row-reordering permutations Π, Π′; τ_S = τ_{S̄}; and at unitary P, d(U†U)_P[H] = P†·d(UU†)_P[H]·P. So kernels and norms agree with the pinned conventions."

**m3, minor: say why the constant term cancels in §3.**
- *Fix:* "P9, P9^R, P9^Γ are permutation matrices because every 2-coordinate projection of the MDS code C is bijective, so the constant terms vanish."

**m4, minor: justify the six-cycle fully.**
- *Fix:* "Because τ_{S′}τ_S acts freely, τ_S y ≠ τ_{S′} y, so there are no double edges. The orbit is connected, so its graph is Cay(S₃, {τ_S, τ_{S′}}) ≅ C₆. Each off-code point lies in exactly one conjugate pair of off-diagonal entries per cut, and code points appear only on diagonals, so there are no cross terms."

**m5, minor: make the transport in §2 explicit.**
- *Fix:* "Φ := Φ_{g⁻¹} is real-orthogonal. By pinned §1.3, with vᵀ unitary, Φ(D) = D and Φ(T) = T. Since Φ maps orbit curves through Q to orbit curves through P9, Φ(T_Q O9) = T_{P9} O9. Hence ⟨ΦH, X⟩ = ⟨H, Φ⁻¹X⟩ = 0 for every X ∈ T_{P9} O9."

**e1, editorial: re-source `ker J = T_{P9}O9`.**
- *Fix:* replace "by the pinned proof's dimension argument" with three facts: the 0-multiplicity 33 from §1's own hand spectrum, T ⊆ ker J (because O9 ⊆ D∩T), and dim T = 33 (pinned Prop. 3.1). This removes any dependence on the pinned U†U kernel.

**e2, editorial: the "in particular" is weaker than what is proved.**
- The radius-1 open tube contains no dual (respectively T-dual) gate outside O9 at all.
- [44] is needed only to equate "outside O9" with "non-2-unitary".

**e3, editorial, worth stating: §3 makes the IFT redundant.**
- §3 reproves pinned Theorem 1 with ε = 1, including relative openness and the connected-component claim.
- The IFT step and the 129-minor in pinned §4 are then logically unnecessary.
- In general the radius is √(λ⁺_min)/√2, so any λ⁺_min > 0 already gives qualitative isolation.

**e4, editorial: the group-action correction is formal.**
- The correction is right.
- It could add "nor a right action".
- The nonlinear argument only needs {Φ_v} to be a group of Frobenius isometries preserving D, T and O9. That was true before the fix.

## Independent derivation

**1. Action.**
- v·(w·U) = (v₁w₁⊗v₂w₂) U (w₃v₃⊗w₄v₄) = (v∗w)·U, using the opposite product on factors 3 and 4. So the corrected formula is a left action.
- G ≅ U(3)⁴ via v ↦ v⁻¹ on the opposite factors.
- The infinitesimal action, the orbit and the tangent space are unchanged.

**2. Dictionary and permutation property.**
- Set ψ(a,b,c,d) = U[(c,d),(a,b)]. The map H ↦ δψ is a real isometry.
- U^R[(c,a),(d,b)] = ψ(a,b,c,d), which is cut 13|24.
- U^Γ[(c,b),(a,d)] = ψ(a,b,c,d), which is cut 23|14.
- All 2×2 minors of [[1,0,2,1],[0,1,1,1]] are nonzero mod 3, so C is MDS. Hence P9, P9^R and P9^Γ are permutation matrices.
- I checked the (C7) table entry by entry against P9|ab⟩ = |2a+b, a+b⟩.

**3. One cut, exact weights.** Write δψ = f + ig.
- Diagonal entries: E_S(s,s) = 2f(c_s), and s ↦ c_s is a bijection onto C.
- Off-diagonal entries: E_S(s,s′) = δψ(y) + conj δψ(τ_S y), with y = (s, f_S(s′)).
- The map from ordered pairs with s ≠ s′ to points y ∉ C is a bijection.
- Each edge {y, τy} is hit twice (the Hermitian pair), so

  ‖E_S‖²_F = 4Σ_C f² + 2Σ_{edges}[(f_u+f_v)² + (g_u−g_v)²].

**4. Two cuts: six-cycles and multiplicities.**
- The composite ρ = τ_Sτ_{S′} acts as (c,q,t) ↦ (c + t·w_q, q, t).
- w_q ≠ 0, because otherwise there would be a nonzero codeword of weight ≤ 2.
- The reflections flip t.
- So S₃ acts freely, giving 12 six-cycles with alternating edge types.
- Spot check (D case), y = (1,0,0,0):
  - τ₁₂y = (0,0,2,1) and τ₁₃y = (0,1,0,2).
  - τ₁₂τ₁₃y = (1,1,1,1) = (0,1,1,1) + e₁, with w₁ = (0,1,1,1).
- spec L(C₆) = {0,1,1,3,3,4}. The signless Laplacian satisfies Q = ΣLΣ, with Σ the bipartition signs.

| block | dim | eigenvalues |
|---|---|---|
| code, Re (8·I) | 9 | 8⁹ |
| code, Im | 9 | 0⁹ |
| 12 orbits, Re (2Q) | 72 | (0,2,2,6,6,8)¹² |
| 12 orbits, Im (2L) | 72 | (0,2,2,6,6,8)¹² |
| **total** | 162 | **0³³ 2⁴⁸ 6⁴⁸ 8³³** |

- Independent trace checks:
  - tr G = 9·8 + 144·4 = 648 = 2·48 + 6·48 + 8·33.
  - tr G² = 576 + 24·144 = 4032 = 4·48 + 36·48 + 64·33.
- Both agree with the receipt.
- The T case uses cuts 12|34 and 14|23. These are also distinct matchings, so the spectrum is identical.

**5. Kernel = tangent (cross-check).**
- The kernel of the form is Im on C (9 dimensions) plus, per orbit, f alternating and g constant (2 each), so 33 in total.
- Tangent vectors on C take values in iℝ^C. They span all of iℝ^C because a, b, 2a+b, a+b cover P¹(F₃).
- Off the code, δψ(c+te_q) = k_q[c_q+t, c_q].
- A τ-move swaps (c_q+t, c_q) with (c_q, c_q+t), so the value z goes to −z̄.
- That means f alternates and g is constant along each orbit: exactly the kernel.

**6. Nearest point and transport.**
- A nearest point Q exists because O9 is compact.
- For each ξ, d/dt|₀ ‖U − e^{tξ}·Q‖² = −2 Re⟨H, ξ·Q⟩ = 0, so H ⊥ T_Q O9. Only orbit curves are needed, not embeddedness.
- Transport by Φ as in m5 gives ΦU = P9 + ΦH ∈ D, with ‖ΦH‖ = δ and ΦH normal at P9.

**7. Remainder: global, no smallness assumption.**
- The expansion F(P9+H) = JH + (HH†, H^R H^R†) is exact: F has degree exactly 2, R is linear, and the constant term cancels by step 2.
- ‖XX†‖²_F = Σσ⁴ ≤ (Σσ²)², so ‖remainder‖ ≤ √2·δ².
- The lower bound ‖JH‖² ≥ 2‖H‖² holds on the whole linear subspace (ker J)^⊥ and is scale-free.
- Combining, 2δ² ≤ 2δ⁴. Since U ∉ O9 and O9 is closed, δ > 0, so δ ≥ 1.
- There is no Taylor remainder to localize, so no smallness assumption is needed.

**8. Consistency check (not a sharpness test).** SWAP lies in D∖O9.
- Tr(SWAP·Q) = vec(aᵀ)ᵀ (SP9)^R vec(bᵀ), with a, b unitary.
- (SP9)^R = SWAP·(P9^Γ)ᵀ is unitary, so |Tr| ≤ 3.
- Then ‖SWAP − Q‖²_F ≥ 12, so the distance is at least 2√3. This is consistent with the bound.

## Limits of this review

- **By hand only, no tools.**
  - I did not run `check_dualunitary_radius.py` or verify the hashes.
  - I did not confirm that the script's T columns are the vectors ξ·P9.
  - The certificate corroborates the result but is not load-bearing; the hand spectrum suffices.
- **Assumed without re-proof:** that orbits of compact group actions are smooth, the C₆ spectra, and the Laplacian/signless-Laplacian conjugacy for bipartite graphs.
- **Pinned results:** I re-derived pinned Lemmas 2.1–2.3 and Prop. 3.1 only as far as needed here. I did not check their evidence files or the exact minors.
- **Not reviewed:**
  - [44] and Corollary 2 (e_p).
  - The d = 4 bullet.
  - Whether radius 1 is sharp. The two lossy steps need not be tight at the same time:
    - λ⁺_min is attained only in off-code directions.
    - The remainder bound is tight only when both H and H^R are rank one.
  - Novelty and priority.
