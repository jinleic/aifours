DISPOSITION: ACCEPT-WITH-FIXES
Proof status: COMPLETE-NO-IMPORTS

Per-question:
Q1: OK-WITH-MINOR - 1/q of (42) equals c(a²+b²)/((s+c)((s+a)²+b²)) = F. The numerator is constant and the three poles are distinct and simple, so nothing cancels. Order = dim T, matching E1. The PH definition matches (4)–(6), and the proof shows Hurwitz ⇔ nonsingular for Metzler T with T𝟙 ≤ 0. n* = ⌈π/arctan((a−c)/b)⌉, which is the n_min of (27)/(28) with λ₁ = c. The band rule, upper endpoint in band n, lower endpoint assigned to n−1, and the n* = 3 band are all correct. The lower bound quantifies over all (α, T). The only printed-domain cases dropped are b = 0 (trivially order 3) and b > 0 with a ≤ c (no unique dominant pole, so not PH). However, :5 and :205 say "the Eq. (42) family" without that qualifier (finding 2). All quotes are verbatim. The Prop. 1 remark holds under either (Tᵀ, αᵀ, tᵀ) or the paper's (12)–(13) dictionary (T, t, α), since the graph reversal preserves irreducibility and the spectrum.
Q2: OK-WITH-MINOR - All re-derived:
  - A2: T_RS = 0, F unchanged, spec inclusion, PH properties.
  - A3: X_UU𝟙 = 0 ⇒ 0 ∈ spec(X).
  - A4: reducible PF left vector; ρ(Y) = μ + κ; p > 0 from reachability only; u·t_R = −μ(u·𝟙) > 0; Laplace integral valid for real s > μ; unbounded rational ⇒ pole ⇒ μ = −c.
  - Lemma A: e^{Qτ} stochastic; K invariant; 0 ∈ int K; the edge v_{k+1}−v_k has direction π−ε_k in the upper half plane while zv_k has direction π−φ, so φ ≤ ε_k; law-of-sines product equals 1; log g_k increases on (0, π−ω_k); Jensen; Frobenius blocks with m_B ≥ 3 and μ_B ≤ s(X).
  - Zero or coinciding w_i and p < m are handled. Matrix irreducibility is used only inside Lemma A's irreducible case. Only notation clashes remain (finding 7).
Q3: OK - (0.1) and (B1.1) hold for n = 3 and n ≥ 4.
  - t₀ < S/3 because S ≤ 3ψ < 3(π−φ).
  - Domains: t ∈ [0, ψ] and (S−t)/2 ∈ [S/3, (S−t₀)/2] ⊆ [0, π−φ].
  - Signs: G(S/3) ≥ 0. G(t₀) = −sin³φ when t₀ > 0. When t₀ = 0, S/2 ∈ (ψ, π−φ] gives G(0) < 0.
  - t* > t₀ gives θ₁ > 0 and every m_i finite.
  - t₀ = 0 ⇔ (n−2)ψ ≥ π, which holds for all n ≥ 4; t₀ = 2φ for n = 3.
  - t* = S/3 at nψ = 2π. At the lower endpoint S = 2ψ and G(0) = 0, which is excluded and assigned to n−1.
  - The argument uses the IVT only; no root finder is a premise.
Q4: OK - The Leibniz expansion is supported only on the identity and the n-cycle, and the cycle term is −W. q(1) = 0. (I1) and (I2) hold. In q(iβ) the numerator is sinⁿφ·e^{2πi} − sinⁿφ = 0, so D | q and P is monic of degree n−3. Mu = u with u > 0 and M + κI is primitive, so s(M) = 1. The row resolvent y(xI−M) = e₁ checks column by column (edges i→i+1 and n→1, α = e₁). The ℝ[[z]] coefficient comparison is correct. The cancellations are harmless:
  - P(1) ≠ 0 because the Perron root is simple.
  - Other eigenvalues have Re < 1, i.e. Re < −C after the shift.
  - A shared root of P and D cancels only inside a rational identity.
  - Hand check at n = 4, β = 0.8 gives P = x + 1.3386, matching the trace.
Q5: OK - Chebyshev times 1/(1−u) with telescoping gives c_k = Σ_{j≤k+1} sin(jψ)/sin ψ = [cos(ψ/2) − cos((k+3/2)ψ)]/(2 sin(ψ/2) sin ψ). The sign range needs only (n−2)ψ < 2π. t ≥ 0 with t ≠ 0 (t₁ = t₂ = 0). T₀ is irreducible and Hurwitz, so (−T₀)⁻¹ > 0 and v > 0. T′ is Metzler, T′𝟙 = −D_v⁻¹t, T′ is similar to T₀, and the transform is invariant. v₁ = K/D(A) = 1. B0 gives T = D_v⁻¹(δM − aI)D_v with exits δD_v⁻¹t and α = e₁; F(0) = 1, so there is no atom.
Q6: OK-WITH-MINOR - (a) Complete using ordinary background only: PF including the reducible and primitive cases, Frobenius normal form, the planar supporting line, law of sines, Jensen, IVT, the matrix Laplace transform, and the Chebyshev generating function. Appendix A replaces Theorem 6, and the n = 3 branch replaces Theorem 14. (b) Not needed. If the Theorem 6 import is used instead, its printed hypotheses hold (T_RR of order n_R, λ₁ = c, λ₂ = a, θ = b > 0, and −c dominant by A4). The Theorem 14 import matches (42), (43) and the printed domain, but never discharges "Consider a PH-distribution" (finding 1). This is not load-bearing.
Q7: OK-WITH-MINOR - Every checkable hash binding matches, including byte counts and all pre-receipt code hashes. e01 is reported everywhere as 32/33, with the E4 FAIL explained by e02; no document says 33/33. e02 tests exactly the E4 identity, tan φ cot 2φ = (1−tan²φ)/2, which I verified by hand. No document counts b01's 10 flags, the f01 abort, H_K_scaled 0/15, or the 0/24 reorderings as passing negative controls. Remaining issues:
  - d01 finished before pin v1's timestamp, contradicting "not yet run"/"post-pin" (finding 3).
  - p00 is missing from the "every run" list (finding 4).
  - Appendix B states b01's status and the f01 cause loosely (finding 5).
  - Count wording (finding 6).
  - Not checkable: JSON internals beyond the desk extract.
Q8: OK - S = 2π and t₀ = 2φ > 0. The bracket [2φ, 2π/3] is nonempty because φ ≤ π/6. G(2φ) = −sin³φ, and G(2π/3) ≥ 0 ⇔ ψ ≥ 2π/3. θ₁ ∈ (2φ, 2π/3] and θ₂ = θ₃ = π − θ₁/2 ∈ [2π/3, π−φ). For the 3-cycle, q is monic of degree 3 and D | q, so q = D and P = 1. The Taylor sum is empty, t = (0, 0, K), N_t = K, v > 0, α′ = e₁. m_*, ρ, h and θ₄… appear only in vacuous statements (empty product z⁰ = 1; the index ranges i ≥ 4, 4 ≤ j ≤ 3 and k ≤ −1 are empty). Hand checks: at β = 1/2, θ₁ = π/2 exactly and q = (x−1)(x²+1/4); the E10 v-vector recomputes as (1, (3C+2)/3, (3C+2)²/9). This branch alone makes n* = 3 independent of Theorem 14.

Findings:
1. [MINOR] target/ph3-theorem-v3.md:193-197 (also :12-13, :206-207) - The Theorem 14 import checks only the printed domain and 1/q = F. It never shows F is a PH-distribution, which Theorem 14 assumes. The only written argument that F is PH is Part B, so "two independent bases, either suffices" overstates basis (i). - Add that F is PH for all a > c > 0, b > 0, citing either Part B or the following: f(t) = (c(a²+b²)/b)e^{−ct}∫₀^t e^{−(a−c)u} sin(bu)du > 0 (pair half-waves), with Theorems 3–4. Otherwise call (i) an alternative basis given PH-ness. - load-bearing: no
2. [MINOR] target/ph3-theorem-v3.md:205 (also :5) - "Conjecture 1 holds for the Eq. (42) family" has no domain qualifier. The printed family is a, b, c ≥ 0, but only a > c > 0, b > 0 is proved. - Write "for the Eq. (42) family with a > c > 0, b > 0", and add: b = 0 is order 3 by three exponential phases in series; b > 0 with a ≤ c is not PH (no unique dominant pole). - load-bearing: no
3. [MINOR] lane/receipts/pin-candidate-v1.json:3,33 vs lane/receipts/d01-dense-pre.json:4, lane/receipts/d01-dense-post.json:4-5 (also lane/README.md:110, lane/receipts/pin-candidate-v2.json:15) - d01 ran 01:03:00–01:03:18, before pin v1's pinned_at of 01:03:30. This contradicts "(written, not yet run at pin time)", "post-pin falsification" and "new_run_since_pin_v1". - Correct either pinned_at or the narrative to the actual event order, e.g. from file mtimes. No hash is affected. - load-bearing: no
4. [MINOR] target/ph3-theorem-v3.md:13 and lane/receipts/pin-candidate-v2.json:12 - These claim Appendix B "lists every run", but target/ph3-theorem-v3.md:250-256 omits p00-flint-probe. - Add p00 (API probe), or say "every non-probe run". - load-bearing: no
5. [MINOR] target/ph3-theorem-v3.md:252-255 - b01 is cited next to b02 without its status. b01 has ALL_OK=false: 88/98 OK, with 10 instances flagged at n = 20, 24, 32. The outputs record only "q1_contains_0/q_ibeta_contains_0/remainder_contains_0: false"; the absolute 2^-150 width explanation (lane/receipts/pin-candidate-v1.json:39, lane/README.md:102) is not recorded in the outputs, though it is consistent with W ≈ 4e37–2e66. Separately, the f01 cause is stated as fact, but f01d records only the n* = 35 instance and the error, and f02 reaches only max_n = 29. - Write: "b01 88/98 OK, 10 flagged by an absolute enclosure-width test (radii not recorded), superseded by b02 112/112". Write: "f01 aborted ('numerically singular', n* = 35; attributed to the pivot threshold; f02 covers n ≤ 29, d01 covers n = 35)". - load-bearing: no
6. [MINOR] target/ph3-theorem-v3.md:253-254,258 (also lane/README.md:107,110, lane/receipts/pin-candidate-v2.json:12) - "1,605 instances n = 3..40 (42 band positions each) plus n = 64, 100, 128" is inconsistent: 38×42 = 1,596, so 1,605 already includes 9 large-n instances. "390 arrangements" is 195 distinct arrangements (30+60+105), each tested at 2 values of β. - Write "1,596 (n = 3..40) + 9 (n = 64, 100, 128) = 1,605" and "195 distinct arrangements × 2 β = 390 cases". - load-bearing: no
7. [MINOR] target/ph3-theorem-v3.md:214-222,227 - Symbols are reused in Appendix A:
  - r is both the Perron vector and time.
  - w is both the eigenvector and the dummy point in "Re(ν̄w) ≥ 0 on K".
  - φ is redefined as arctan(y/x); this coincides with arctan β where it is applied.
  - K, s(·), u, ε, p and C each carry two meanings across the document.
  - Meaning is recoverable everywhere.
  - Fix: use τ for time (e^{Qτ}, e^{zτ}), ξ for the dummy point, and φ_A in Appendix A. - load-bearing: no

Unresolved assumptions:
- The desk transcription primary/EXCERPTS.md is faithful to the pinned PDF. I found no implausible transcription.
- Standard background is used without proof: PF (reducible and primitive cases), Frobenius normal form, the planar supporting line, Jensen, the Laplace transform of e^{Tt}, and the Chebyshev U generating function.
- Smoke-run internals beyond the extract are unverifiable, and none is a premise:
  - b01 flag definition.
  - b02 eigen-enclosures.
  - d01 band positions, 2,048-bit scope, and the 0.0 residuals at n = 64, 100, 128.
  - f02 case composition and code independence.
  - The f01d cause.
- Hashed artifacts not supplied:
  - proof v1 (f824eb23…).
  - The frozen README (db34b018…, 7,366 B). The current README is 2452b9d2…, 9,596 B, which differs as expected from the appended log, but I cannot verify that §1–6 are unchanged.
  - The candidate note (63ea3f3a…).
  - The screen (959a2d79…).
  - The book and page images.
- The Theorem 14 alternative presupposes F is PH (finding 1).

Verification counts: 14 quotes/citations checked against EXCERPTS (all consistent); ≈95 proof steps re-derived plus 4 hand computations (n=3 β=1/2, n=4 β=0.8, E10 n=3 v-vector, f01d/b01 β and ρ vs bands); 90 hash bindings checked, 90 match (pin v2 7, pin v1 29, post→pre 12, post→outputs 35 with byte counts, README/target prefixes 7); 118 pre-receipt code-hash entries match; 5 artifact groups uncheckable.
