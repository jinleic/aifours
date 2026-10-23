# Lane phys-2 (fourth target): four-qubit depolarizing-output majorization

**Status (host-clock checkpoint, 2026-10-17 UTC): PARTIAL Ky Fan indices; the full n = 4 statement is OPEN.**
Proved (exact LP certificates plus reductions; Codex ACCEPT-WITH-FIXES, fixes applied in `frozen-partial-v1/`):
k ∈ {1, 5, 11..15} for all p ∈ [0, 4/3], and also k ∈ {2, 3, 4} for p ∈ [2/3, 4/3]. Open: k = 6..10 for all p, and
k = 2..4 for p < 2/3. Exact obstruction: the PPT relaxation is loose by exactly 1 (`U_2`, k = 6..10) and by 2, 2, 1
(`U_3`, k = 2..4). The level-2 σ-extension shrinks these gaps to 0.009–0.110 and 0.089–0.231 (float) but does not
close them. The parent's priority audit of Amosov arXiv:2401.05104 is pending; nothing here is labeled new or solved.

Rotation recorded by parent 2026-10-16. Predecessor: `../spin-alignment-n3/` (Song–Chen Conjecture 2 stays
OPEN / NEEDS-NEW-REPRESENTATION in general; scoped n = 3 Theorem A / Corollary B frozen in
`../spin-alignment-n3/frozen-theoremA-v1/`, manifest `MANIFEST_v1_1.sha256` sha256 `f3b67a04…580d`).

## Frozen contract (before any attack)

- **Target.** Song–Wang–Tomamichel–Fang, arXiv:2609.37240v1, Eq. (2), case d = 2, n = 4 (pinned
  `sources/swtf-2609.37240v1.pdf`, sha256 `456ba1cd…6df`): for every 4-qubit state ρ and every physical
  `p ∈ [0, 4/3]`, `λ↓(D_p^{⊗4}(ρ)) ≺ λ↓(D_p^{⊗4}(|0000⟩⟨0000|))`, with `D_p(X) = (1−p) X + p Tr(X) I/2`.
- **Reductions (exact).** Ky Fan sums are convex and the output is linear in ρ ⇒ pure ρ suffice. The spin-flip
  identity `σ_y D_p(X)^T σ_y = D_{2−p}(X)` (re-derived in the n = 3 lane) gives equal spectra for p and 2−p, so
  `p ∈ [0, 1]` suffices. Local unitaries commute with `D_p^{⊗4}` up to conjugation, so ψ can be taken modulo LU.
- **Decisive first branch p = 1/2.** Target eigenvalues `(3/4, 1/4)^{⊗4}`: 81/256 (×1), 27/256 (×4), 9/256 (×6),
  3/256 (×4), 1/256 (×1). k = 1: King's multiplicativity of the maximal output ∞-norm (to be checked against the
  primary statement before use). k = 15: `D_{1/2}^{⊗4}(ρ) ≥ (1/2)^4 · I/16 = I/256` from the all-depolarized term,
  so `λ_min ≥ 1/256`. Middle k = 2..14 are the real obligation.
- **Acceptance.** A counterexample = rational ψ, rank-k projector P and exact positive witness
  `Tr(P D(ψ)) > K_k(target)`. A proof = complete argument; floating-point searches are evidence only. A p = 1/2 proof
  alone is an explicit partial case.
- **Budget.** Scientific runs in ≤ 2 h chunks with checkpoints; ≤ 4 CPU workers.

## Attack log

Notation (Q = I/2 picture, unnormalized): `X_s = Σ_{|I|=s} ρ_I ⊗ 1_{I^c}`, `T_s = Σ_{|I|=s} P_I` (`P_I` = |0…0⟩⟨0…0| on I
⊗ 1), `X_0 = 1`, `X_4 = ρ`. Exact expansion `D_p^{⊗4}(ρ) = Σ_s a_s X_s`, `a_s = (1−p)^s p^{4−s} 2^{s−4}` (checked
numerically, err 3e-17). `U_s` := "`X_s ⪯ T_s` for every 4-qubit state" (Song–Chen Conj. 2 instance, n = 4, Q = I/2,
uniform weights on size-s subsets).

1. **Calibration** (`code/n4.py calib`, `evidence/calibration_p_half.json`): target spectrum ×256 = 81, 27×4, 9×6, 3×4,
   1. Max Ky Fan gaps at p = 1/2 for k ≤ 15: product 0; Bell⊗Bell, GHZ4, linear cluster −1/32; W4 −1/128.
2. **Reduction R1 (Hamming alignment).** All `T_s` are diagonal with entries depending only on the Hamming weight and
   non-increasing in it, so `K_k(Y) = Σ_s a_s K_k(T_s)`; Ky Fan subadditivity gives, for p ∈ [0,1]: if `U_s` holds at
   index k for s = 2, 3 then `K_k(D_p^{⊗4}(ρ)) ≤ K_k(D_p^{⊗4}(|0000⟩))`. (`U_1` is the Kronecker-sum lemma; `U_0`, `U_4`
   trivial; `U_3` is trivial at k = 1 and k ≥ 5; `U_2` is trivial at k = 1 and k ≥ 11.)
3. **Reduction R2 (spin flip removes X_3 for p ≥ 2/3).** `ρ̃ = σ_y^{⊗4} ρ^T σ_y^{⊗4} = Σ_s (−1)^s X_s`. With
   `t = a_3`: `D = D⁺ − a_3 ρ̃`, `D⁺ = (a_0+a_3) 1 + (a_1−a_3) X_1 + (a_2+a_3) X_2 + (a_4+a_3) ρ`; `a_1 ≥ a_3` ⟺
   p ≥ 2/3. Then `K_k(D) ≤ K_k(D⁺) ≤ K_k(Y⁺) = K_k(Y)` for k ≤ 15 (`Y⁺ = Y + a_3 |1111⟩⟨1111|`, whose 1111 entry
   `a_0 + a_3 ≤ a_0 + a_1` stays smallest). So for p ∈ [2/3, 4/3] only `U_2` is needed (identities checked numerically).
4. **Twirled PPT relaxation → LP with 16 variables** (`code/twirl_ppt_lp.py` explicit 256×256 matrices;
   `code/twirl_lp_exact.py` closed-form exact data). `sup_{σ,Π} Tr[Π N(σ)]` (σ state, 0 ≤ Π ≤ 1, Tr Π = k) relaxed to
   ω ≥ 0, σ⊗1 − ω ≥ 0, both PPT on the Π side, Tr ω = k, Tr_σ ω ≤ 1; local-unitary covariance (conj(U) ⊗ U) twirls ω
   into span⊗_l{Φ⁺, 1−Φ⁺}. Exact results: `U_2` LP = target at k = 1..5, 11..15 and = target + 1 at k = 6..10;
   `U_3` LP = target at k = 1, 5..11 (trivial range) and target + 2, 2, 1 at k = 2, 3, 4.
   **Exact dual certificates** (`code/u2_dual_cert.py`, `evidence/u2_dual_certificates.json`): rational dual points
   verified exactly with `fractions`; bound = target at k = 1..5, 11..15. Controls: dropping PPT gives 15.25/19.25/23.25/24
   at k = 2..5 (targets 9/12/15/18); dropping σ⊗1−ω ≥ 0 bounds also loosens; Tr_σ ω ≤ 1 is redundant.
5. **Partial theorem (candidate; computer-assisted exact LP + analytic reductions, unreviewed):** for every 4-qubit ρ,
   - all p ∈ [0, 4/3]: `K_k(D_p^{⊗4}(ρ)) ≤ K_k(D_p^{⊗4}(|0000⟩))` for k ∈ {1, 5, 11, 12, 13, 14, 15} (k = 5 uses the
     `U_2` certificate; others only trivial bounds + Kronecker lemma + alignment; p > 1 by reflection);
   - p ∈ [2/3, 4/3]: also k ∈ {2, 3, 4} (R2 + `U_2` certificates at k = 2..4).
   Open: k = 6..10 for all p ∈ (0, 4/3) \ {1}; k = 2, 3, 4 for p ∈ (0, 2/3). At p = 1/2 the open indices are 2–4, 6–10.
6. **Numerical evidence (float, not proof)**: 40 BFGS starts per k: `U_2` best gap −3.0e-12 (k = 5), `U_3` +7e-15 (k = 15,
   roundoff), p = 1/2 −4.2e-10, p = 0.8 −3.8e-9. Sufficient "Z-lemma" for `U_3`:
   `K_k(Σ_{l,a} σ_a^{(l)} ρ σ_a^{(l)}) ≤ 2 + 2k` (k ≤ 4; = `K_k(X_3 − 2ρ) ≤ 1 + k`) holds numerically (best −9e-11).
7. **New n = 4 spin-flip identity** (`code/u2_weyl.py`, verified to 1e-15): `X_2 = (2X_1 − 3·1) + ρ + (X_3(ψ̃) − ρ̃)`,
   `X_3(ψ̃) − ρ̃ ≥ ρ̃ ≥ 0`. The Song–Chen-style Weyl bound from it is tight at product states but over admissible local
   spectra proves only k = 5 and k ≥ 11 (fails by up to 3 at k = 2..4, 6..10, e.g. r = (0, ½, ½, ½) at k = 8).
8. **Frozen package** `frozen-partial-v1/`. It contains `PROOF.md` (v1, sha `6789e392…ce8a`; `SHA256SUMS` sha
   `11830b3f…10b5`), `ADDENDUM_v1_1.md` and `MANIFEST_v1_1.sha256` (sha `81dd35ef…06fa`). Codex `gpt-6.1-sol`
   (cross-vendor; max effort, read-only, exit 0) returned **ACCEPT-WITH-FIXES**. All mathematical checks passed and
   all ten stored certificates were independently recomputed. The three low-severity fixes are applied in v1.1,
   including the read-only `verify_frozen_certs.py`, which reports ALL_VERIFIED; the mutation control fails at every k.
   Codex's novelty split: k = 1 is King's result, and k = 11..15 are elementary. The substantive part is k = 5 for all
   p, together with k = 2..4 for p ∈ [2/3, 4/3]. Label: **PARTIAL Ky Fan indices**.
9. **The level-1 obstruction is exact** (`lp1_primal_witnesses.json`). Rational feasible LP points reach target + 1
   for `U_2` at k = 6..10, and target + 2, 2, 1 for `U_3` at k = 2..4. Twirling loses nothing, so the plain PPT
   relaxation cannot certify these indices.
10. **Level-2 σ-side relaxation** (`code/dps2_twirled.py`, float SDP, Clarabel). It adds a Bose-symmetric extension
    σσ'Π, PPT across Π and σ', and ξ⊗1 − ω₂ ≥ 0 with its PPT versions, all twirled into the walled-Brauer commutant
    (ℂ ⊕ M₂ per site; faithful 81×81 representation split into 16 PSD blocks). Positive control: `U_2` at k = 5 gives
    17.9999998 (target 18). Mutation control (no Bose, no level-2 PPT) at k = 6 gives 20.0000001, the level-1 value.
    `U_2` at k = 6..10 gives **19.0093, 20.0341, 21.0638, 22.0897, 23.1100** (targets 19..23; k = 6 and k = 10 solved
    "optimal", the other three "optimal_inaccurate"). `U_3` at k = 2..4 gives **5.0892, 6.2315, 7.1844** (targets
    5, 6, 7). The level-1 gap of 1 (or 2) is therefore **not structural**: symmetric extension removes 89–99 % of it.
    The level-2 relaxation is still **not tight**, so it certifies nothing new.
11. **Level-2 Π-side relaxation** (`code/dpsPi_twirled.py`). It uses σΠΠ' with Π↔Π' symmetry, PPT on Π, Π' and σ,
    σ⊗(1−Π)⊗Π ≥ 0, σ⊗(1−Π)⊗(1−Π) ≥ 0 with their PPT versions, and the idempotency equation
    Tr_{ΠΠ'}[ω F] = kσ. It is **weaker** than the σ-side version: `U_2` k = 6 gives 19.2720 (19.2751 without
    idempotency), k = 10 gives 23.2941, and `U_3` k = 2 gives 5.0922.
    **Next bounded approach:** a level-3 relaxation σσ'σ''Π or σσ'ΠΠ'. The per-site commutant is ℂ ⊕ M₃ ⊕ M₂
    (dimension 14, giving a 1296-dimensional representation in 81 blocks). This hierarchy converges only
    asymptotically, so exact tightness at any finite level is not guaranteed. Proving the interior indices exactly
    probably needs a different idea, for example an exact SOS certificate in the 12×12 Pauli–Gram representation
    (Z-lemma) for `U_3`, plus an analogue for `U_2`.
12. **Exact Pauli–Gram / SOS route (parent-directed cycle; STOPPED by parent).** Frozen in
    `zlemma-route/FROZEN_STATEMENTS.md` (sha `b3db2407…b71b`; `SHA256SUMS` sha `9e551ae3…c8cc`), with scope limits in
    `zlemma-route/ERRATUM_scope.md`. The Z-lemma `K_k(Σ_{l,a} σ_a^{(l)} ρ σ_a^{(l)}) ≤ 2+2k` (k ≤ 4) is equivalent to a
    12×12 Gram statement and would imply `U_3`, hence indices 2–4 for all p. **Outcome: not closed.**
    - Exact rational feasible points show that the *particular* twirled PPT relaxation encoded here (degree-2 in
      the (σ, Π) encoding) is not tight for the Z-map at any k ≤ 4 (5, 10, 12, 12 against 4, 6, 8, 10). They do
      **not** rule out low-degree SOS certificates under other constraints or encodings.
    - Reduction R3 (an exact convex decomposition into 16 top-Schmidt pattern operators) holds numerically. The
      pattern lemma fails for arbitrary subspaces (+0.169 at k = 3, +0.236 at k = 4) and for arbitrary local
      post-selections (+0.120, +0.236), so any encoding must include the top-branch condition. That condition is
      semialgebraic and can be encoded with auxiliary PSD/order constraints; its form is not an impossibility
      argument.
    - No exact `U_2(6..10)` inequality was found.
    n = 4 stays **PARTIAL**. Note: the earlier `u3pat_psi_{0,4}.log` runs used conjugated Schmidt vectors. Their
    maxima are unchanged, because the conjugated data equal the correct data for ψ̄ and the search ranges over all
    ψ, but `u3pat_fixed_psi_*.log` are canonical.
