# Random 8-regular graph colouring: parent verdict

## Result and exact scope

**For the uniformly random 8-regular graph G_{n,8} (n → ∞), χ(G_{n,8}) = 4 asymptotically almost surely.**

This closes the {4, 5} window that Kemkes–Pérez-Giménez–Wormald (KPW, Adv. Math. 2010, Theorem 1; k = 5 at d = 8 because 6 log 3 < 8 < 8 log 4) leave at d = 8. Ayre–Coja-Oghlan–Greenhill's Table 1 (q = 4: d_{4,smm} = 6, d_4 = 10) also leaves d = 8 undetermined. d = 8 lies beyond the best previously available balanced-colouring constant ℓ₄ = (27/4) log 3 ≈ 7.4156 (Achlioptas–Naor display (12); Nir–Pérez-Giménez Theorem 1.2, proved there for random lifts only).

The result is a reviewed **written proof** that imports published theorems: KPW §§2–4 and Theorem 10, Wormald's small-subgraph-conditioning Theorem 4.1, Diaconis–Saloff-Coste's complete-graph log-Sobolev constant with Gross hypercontractivity, and the Molloy–Reed first-moment criterion. It is not a Lean formalization. [Frozen target](../screening/phys-2-random8reg-colour-contract-r2.json); the target is **DERIVED-OPEN** (from KPW's window and ACG Table 1), not explicitly named as open by a source.

## Frozen proof

[Final r3](chi8-parent-inputs-r3/PROOF_CHI8.r3.md), SHA-256:

`e7c506d0bcd75aad69ce004c4633ffa15e5a8ee64d90f53bf9c6867b95187e2d`

- [r3 pin](chi8-parent-inputs-r3/manifest.json) with the parent's own [r2→r3 diff](chi8-parent-inputs-r3/parent-r2-to-r3.diff): exactly the three delta-review edits plus title/status lines.
- [r2 pin](chi8-parent-inputs-r2/manifest.json) (`055d2952…4cb1`) with the [r1→r2 diff](chi8-parent-inputs-r2/r1-to-r2.diff) (777 lines, read in full by the parent).
- [Reviewed r1 and sources](chi8-parent-inputs-v1/manifest.json) (`7ed7f8c8…4c8a`, unchanged).

## Mathematical bridge

1. **Lemma A (exact-exponent weak duality).** KPW's exact count (3.4) of pairs of balanced colourings with overlap M is bounded at finite n, keeping all 16 per-cell edge constraints (3.3), by P_8(n)·exp(n V_μ(M)) with an explicit polynomial factor P_8(n) = e¹⁷(8n+1)⁸(4n+1)^{145/2}. With multipliers μ_u = c₀ + (7/8) log m_u this gives U(M) = −10 log 2 + 4 log E(M), E(M) = Σ_{allowed u,v}(m_u m_v)^{7/8}. The closed form is Galanis–Štefankovič–Vigoda–Yang's Φ₁^{B⊗B}(M^{7/8}); the duality itself is standard.
2. **Theorem C (global quadratic decay).** E(M) ≤ E(J) − κ‖M − J‖² on all row-stochastic M, hence U(M) − U(J) ≤ −C₈‖M − J‖² on doubly stochastic M, with κ = (441/128)(a² − 1/9), a = 7^{−(log 3)/2} > 1/3, and C₈ ≈ 0.0147315. Proof: an inclusion–exclusion row reduction E ≤ Σ_p (S(r_p)² + Q(r_p)/2), then the row function equals 18‖T_{1/3} r^{7/8}‖₂² and hypercontractivity of the resampling chain on four points (α = 1/(2 log 3)) contracts L^{8/7} to L² at ρ = a, which needs log 7 ≤ 2. This replaces KPW's Lemma 5 relaxation and Achlioptas–Naor's maximisation in the S₂ estimate; the replaced relaxation is shown to be strictly lossy at (J + I)/2, exactly where the d = 7 route fails at d = 8.
3. **KPW audit at (4, 8).** Every use of KPW's degree hypothesis in §§2–4 is either (H1) = 16 − 8 − 8 + 2 = 2 > 0 or the S₂ estimate now re-proved; Lemma 9's counting step is used only at k = 4. S₂/S₁ = O(n^{199/2} exp(−C₈ε² log²n/81)) → 0.
4. **Every n.** Small subgraph conditioning at (4, 8) for n ≡ 0 (mod 4); for n ≡ r (mod 4), r = 1, 2, 3, KPW Theorem 10 with 4r distinguished edges, with exact conditional uniformity (multinomial(8r; 8, …, 8)-to-one: 1, 12870, 9465511770). Two sketched steps of KPW's Theorem 10 proof are imported as KPW state them and disclosed (§5.3).
5. **Lower bound.** Molloy–Reed at q = 3: 3·(2/3)⁴ = 16/27 < 1; a self-contained weak-duality first moment reproduces it.

## Verification

| Evidence | Observed result | Limit |
|---|---|---|
| Parent replay of the r1 exact/arb verifier | byte-identical ([receipt](chi8-parent-verifier-replay-v1/parent-result.json)) | Replay, not a second implementation |
| Parent replay of the r2 extension verifier (sections F–K) | byte-identical JSON and stdout, all_required_true ([receipt](chi8-parent-verifier-replay-r2/parent-result.json)) | Same |
| Parent independent rational arithmetic | C₈ ∈ (1473148178637501980, 1473148178637501981)/10²⁰, log 7 < 2, (H1), 7/9, 81/64, 16/27, degree 199/2, residue counts, using only exact atanh/Taylor enclosures and integer square roots ([receipt](chi8-parent-rational-arithmetic-v1.json)) | Constants and counts only |
| Parent spot checks of r2 additions | AM04 relaxed marginals 35/26, 17/78 against 5/4, 1/4 and 99/62, 25/186 against 3/2, 1/6; U((J+I)/2) − U(J) = −0.0287642; overestimate 0.0361835; (5,12) constants for the follow-on lead | Exact fractions and 60-digit decimals |
| Codex CLI `gpt-6.1-sol`, hostile review of r1 | **ACCEPT**, no fatal/major; re-derives the count, P_d(n), weak duality, D–SC normalisation, Theorem C, every KPW dependency, the S₁ Hessian (det H = 4⁶5⁻⁹), residues and a first-moment bound ([note](chi8-codex-hostile-review-v1.note.md)) | Model review, not peer review |
| Claude CLI `claude-opus-5-5`, complete review of r1 | v1 timed out at 2400 s with **no verdict**; v2 **ACCEPT-WITH-FIXES**, seven editorial minors, no mathematical gap ([note](chi8-claude-complete-review-v2.note.md)) | Model review; v2 used reduced source context |
| Codex CLI `gpt-6.1-sol`, delta review of r2 | **ACCEPT-WITH-FIXES**, three editorial minors in non-load-bearing commentary; confirms renames across the whole file and that no change weakens the load-bearing argument ([note](chi8-r2-delta-codex-review-v1.note.md)) | Delta only |
| Parent final-delta review | every finding dispositioned and applied ([dispositions](chi8-review-dispositions.json)); r2→r3 diff contains exactly the three fixes | r3 itself not re-reviewed by a model; no computation changed |

## Trust, priority and significance

- The proof inherits KPW's correctness, including the two disclosed sketched steps of Theorem 10, and D–SC's Theorem A.1 normalisation (quoted from the pinned source).
- [Priority audit](chi8-priority-audit.md): no source found stating χ(G_{n,8}) = 4 (or χ(G_{n,12}) = 5) for the uniform model, and no source proving a constrained global decay step of this kind. GSV/GSVY's Φ formulation and the maximum-entropy duality are prior work and are cited as such; their route to the unconstrained maximum needs a PSD interaction, unavailable here (B ⊗ B has eigenvalues 9, −3, 1). A search miss is not novelty.
- **Delta against matched primary prior art:** KPW (4-colourable only for d < 6.59), Achlioptas–Naor and Nir–Pérez-Giménez (ℓ₄ ≈ 7.4156, lifts), Achlioptas–Moore §6 and KPW Lemma 5 (Erdős–Rényi relaxation, strictly lossy at (J + I)/2). The new step is Theorem C with the per-cell constraints kept; the route stops at d = 8 for k = 4 (log(d − 1) ≤ 2).
- **Significance:** potentially substantive specialist result; not peer reviewed; not a new threshold law or a general-k theorem. [INFERENCE] The same route appears to reach d = 12 at k = 5 (KPW window {5, 6}); that is a separate, pre-registered target, not part of this verdict.

## Status

**FRONTIER: CORRECTNESS-ACCEPTED — reviewed written proof relying on published machinery; DERIVED-OPEN target; NOVELTY-UNCLEAR. Recorded as phys-2's gate under the run contract's "materially new theorem/method with a demonstrated consequential delta against matched primary prior art" clause (2026-10-17 PT), with significance calibrated as potentially substantive specialist, not a broad breakthrough.**

No commit, push, publication or external contact was authorized.


**Attribution addendum (2026-10-17 15:19:38 PDT, appended; text above unchanged):** a new-surface audit found a method precedent or general theorem that this verdict did not cite; see [physics-priority-addendum-v1.md](physics-priority-addendum-v1.md). No correctness change.
