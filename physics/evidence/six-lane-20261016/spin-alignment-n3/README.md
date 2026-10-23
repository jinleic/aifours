# Lane phys-2 (third target): Song–Chen Conjecture 2, n = 3, d = 2

Frozen by parent 2026-10-16. Status: **OPEN in general — no violation found.** Scoped exact result (unreviewed by
parent; Codex ACCEPT-WITH-FIXES): Theorem A / Corollary B below (Q = I/2, a weight region containing all
permutation-invariant μ; d=2, n=3 depolarizing-output majorization for all physical 0 ≤ p ≤ 4/3). Numerical
statements are floating-point evidence; non-finds are not proof.

## Target (primary: Song–Chen, arXiv:2603.25410v1 §III; pinned `sources/song-chen-2603.25410v1.pdf`, sha256 `18929744…e4ba3`)

For every 3-qubit state ρ, probability measure μ on the 8 subsets of {A,B,C}, qubit state Q with maximal eigenvector |q1⟩:
`X = Σ_I μ_I ρ_I ⊗ Q^{⊗I^c} ⪯ Y = Σ_I μ_I |q1⟩⟨q1|^{⊗I} ⊗ Q^{⊗I^c}`. The source proves only Q = I/2 with μ on
{AB, AC, BC} (Prop. 3); §IV asks for general three-qubit settings and arbitrary Q.

## Prior-art screen (2026-10-16; dated, not proof of openness)

- arXiv:2607.07913 (Alhejji–Kelson-Packer): separable Ky Fan majorization for two tensor-product summands; failure
  for ≥3 summands of ≥3-fold products — not compatible marginals.
- arXiv:2607.27116 (Wolf–Zhou): Ky Fan majorization for sums of binary tensor products (any number of summands).
- arXiv:2607.28061 (Guterman–Wolf, "Poset-refined majorization relations"): separable Ky Fan majorization for any
  number of tensor factors, sums of tensor products of arbitrary matrices. Tools only: Conjecture 2 has entangled
  marginals ρ_I, so none of these resolves it.
- Web search for the conjecture, EulerSolve site search and listing, Zenodo web search, openai/math CONTENTS: no hit.

## Reduction

Ky Fan sums are convex and X is affine in ρ ⇒ pure ρ = |ψ⟩⟨ψ| suffice. WLOG Q = diag(q,1−q), q ≥ 1/2, q1 = |0⟩;
Y is diagonal with exact entries `y_x = Σ_I μ_I [x_I = 0] Π_{l∉I} (x_l = 0 ? q : 1−q)`.

## Results

| Experiment | Result | File |
|---|---|---|
| Control: strong-conjecture counterexample | `K_3 = 0.8344002 > 5/6` reproduced | `code/search.py control` |
| Control: Prop. 3 setting (Q=I/2, μ on pairs) | max gap `1.1e-15` | same |
| Joint search over (ψ, μ, q), 4 × 300 multistarts | max gap ≤ `2.1e-15` (drifts to equality vertices) | `evidence/logs/general_seed*.json` |
| Interior scans, ψ optimized per k: μ~Dir(1), q~U | best gaps −6.9e-10, −7.7e-10, −2.3e-10, −8.1e-10 | `evidence/logs/interior2_seed2*.json` |
| Q = I/2, μ~Dir(1) / Dir(0.3); μ~Dir(0.3), q~U; q=0.55, μ~Dir(0.5) (60 samples each) | best gaps −2.1e-11, −9.1e-13, −5.1e-10, −2.0e-10 | `evidence/logs/interior_*.json` |
| **Second-order expansion at the aligned state** (ψ = \|000⟩ + εφ, φ ⊥ \|000⟩) | exact formula validated against finite differences (ratio → predicted G); over 1200 random (μ,q) × k = 1..7 the largest Hessian eigenvalue is ≤ 1.1e-15 (negative semidefinite); first-order term in Y-degenerate cuts is 0 in all sampled ties | `code/second_order.py`, `evidence/logs/second_order_seed*.json` |
| Flat Hessian directions (worst sample, k = 4) | 6-dim flat space = φ supported on the top-k set with one qubit kept in \|0⟩ (an exact-equality family); gap along it ≤ 8.9e-16 for \|ε\| ≤ 0.3 | session log |
| Targeted Q = I/2 families (280 BFGS starts each over ψ, all k): uniform weights on all 7 nonempty subsets; the chain-obstructed weights (singletons 0.30/0.20/0.10, pairs 0.12/0.10/0.08, triple 0.10) | best gaps −2.1e-11 and −3.6e-11 | `evidence/targeted_halfQ.json` |
| Depolarizing n=3 (μ_I = (1−p)^{\|I\|}p^{3−\|I\|}, Q=I/2), 105 BFGS starts per p | best gaps: p=0.3 −4.6e-11, 0.7 −2.0e-10, 1.0 0, 1.2 −3.3e-10, 4/3 −8.0e-11 (no violation, including the unproved 1<p≤4/3) | `evidence/depolarizing_n3_check.json` |
| Unproved region outside (i)–(ii) (dominant singleton A, w_B,w_C small, random/inverted pair order, Q=I/2), 3 × 50 μ samples | best gaps −1.5e-14, −7.4e-14, −1.7e-12 (k = 4): closest approach to equality so far, still not positive | `evidence/logs/unproved_*.json` |
| Exact alignment check (i)–(ii) ⇒ common order, 3310 rational weight vectors | holds in all cases | `code/aligned_blocks.py alignment` |

Second-order coefficient (nondegenerate cut, top-k set S of the diagonal Y):
`G_k(φ) = Tr(P_S X2) + Σ_{i∈S, j∉S} |(X1)_{ij}|²/(y_i − y_j)` with `X1 = M(|φ⟩⟨0| + |0⟩⟨φ|)` (zero diagonal),
`X2 = M(|φ⟩⟨φ|) − |φ|² Y`, `M = Σ_I μ_I Tr_{I^c}(·) ⊗ Q^{⊗I^c}`. Local conclusion (numerical): the aligned state is a
local maximizer of every Ky Fan gap (value 0) for all sampled parameters; no positive second-order direction exists in
the samples, so no nearby exact counterexample is available from this mechanism.

## Scoped exact result (proof; relies on Song–Chen Prop. 3)

**Theorem A (n = 3, d = 2, Q = I/2).** Put `w_I = μ_I 2^{−|I^c|}` and relabel so that `w_A ≥ w_B ≥ w_C`. If
(i) `w_A ≤ w_B + w_C` and (ii) `w_AB ≥ w_AC ≥ w_BC`, then Conjecture 2 holds for μ (every ρ).

*Proof.* With `Q = I/2`: `X = w_∅ 1 + X_1 + X_2 + w_ABC ρ`, `Y = w_∅ 1 + T_1 + T_2 + w_ABC |000⟩⟨000|`, where
`X_1 = Σ_l w_l ρ_l ⊗ 1`, `T_1 = Σ_l w_l |0⟩⟨0|_l ⊗ 1`, `X_2 = Σ_{l<m} w_lm ρ_lm ⊗ 1`, `T_2` likewise with `|00⟩⟨00|`.
(1) `X_1 ⪯ T_1`: `X_1` is a Kronecker sum of commuting one-qubit terms, so its spectrum is `{Σ_l w_l λ_l(s_l)}`;
each `(λ, 1−λ) = λ(1,0) + (1−λ)(0,1)` is a convex combination of permutations of `(1,0)`, so the spectrum of `X_1`
is a convex combination of permutations of the spectrum of `T_1`. (2) `X_2 ⪯ T_2`: Song–Chen Prop. 3 (arbitrary
nonnegative pair weights). (3) `ρ ⪯ |000⟩⟨000|`; identity terms coincide. (4) Under (i)–(ii) the diagonal targets
`1, T_1 = (Σw_l, w_A+w_B, w_A+w_C, w_B+w_C, w_A, w_B, w_C, 0)`, `T_2 = (Σw_lm, w_AB, w_AC, w_BC, 0,0,0,0)` and
`|000⟩⟨000|` are all nonincreasing in the common order `000,001,010,100,011,101,110,111`, so their Ky Fan sums add.
Hence `K_k(X) ≤ Σ_blocks K_k(block) ≤ Σ_blocks K_k(target) = K_k(Y)` for every k, with equal traces. ∎
(`code/aligned_blocks.py alignment` checks exactly, on random rational weights, that (i)–(ii) imply the common order.)

**Corollary B.** Every permutation-invariant μ (`μ_I` depending only on `|I|`) satisfies (i)–(ii). In particular
`D_p^{⊗3}(ρ) ⪯ D_p^{⊗3}(|000⟩⟨000|)` for the qubit depolarizing channel `D_p(X) = (1−p)X + p Tr(X) I/2`,
`0 ≤ p ≤ 1` (expand `D_p^{⊗3}` into weights `(1−p)^{|I|} p^{3−|I|}`): the d = 2, n = 3, p ≤ 1 instance of the
depolarizing-output majorization conjecture, Eq. (2) of Song–Wang–Tomamichel–Fang, arXiv:2609.37240v1 (29 Sep 2026;
pinned `sources/swtf-2609.37240v1.pdf`, sha256 `456ba1cd…6df`), where the general statement is stated as open. The
range `1 < p ≤ 4/3` follows from the parent-supplied, re-derived reflection lemma `σ_y D_p(X)^T σ_y = D_{2−p}(X)`
(spectra of `D_p^{⊗3}(ρ)` and `D_{2−p}^{⊗3}(ρ)` coincide), so all physical `0 ≤ p ≤ 4/3` are covered. Equal weights on
all 8 subsets is the `p = 1/2` case; equal weights on the 7 nonempty subsets is an affine rescaling of it.
Convention: `D_p(X) = (1−p) X + p Tr(X) I/2` (not the total-error convention of the capacity lane).

Status: frozen as `frozen-theoremA-v1/PROOF.md` (v1, preserved) and `PROOF_v1_1.md` (review fixes); Codex
`gpt-6.1-sol` (max, read-only, exit 0) hostile review **ACCEPT-WITH-FIXES**, all fixes low severity (wording of
"equalities", "multilinear", what Song–Chen eqs. 29–31 contain, unreproducible session-log claim) and applied in
v1.1; its independent numerics (14000 region cases, depolarizing 1400 states per p) found excess ≤ 1.8e-15 and exact
outside-region examples showing both hypotheses are load-bearing for the block argument (k = 4 for (i), k = 2 for (ii)).
Scope: an elementary corollary of Song–Chen Prop. 3; priority not established. Not a resolution of Conjecture 2.

## Hard region (outside (i)–(ii)): mechanisms tried and exact obstructions

- **Separate-block bound fails exactly at k = 4** (dominant singleton `w_A > w_B + w_C`, `w_BC > 0`): the targets'
  top-4 sets differ (`T_1` wants `011`, `T_2` wants `100`), so `Σ K_4(T_b) − K_4(Y) = w_A + w_BC −
  max(w_A, w_B + w_C + w_BC) > 0`, attained already at the aligned state; no proof can use separate block bounds.
- **Richer provable blocks** (`code/block_cover.py`): {any subsets inside a qubit pair} + {complementary singleton}
  (n = 2 strong theorem of Alhejji 2026 as cited by Song–Chen, plus Lemma K), pair triples (Prop. 3), full term. An LP
  over the 48 linear extensions of the Boolean order covers 261/300 sampled weight vectors (float LP feasibility;
  not an exact theorem). Uncovered samples sit in the dominant-singleton/opposite-pair or inverted-pair-order region.
- **Song–Chen's Weyl technique generalized** (`code/weyl_bound.py`; `X = D + P`, `D` Kronecker sum, `P = (f+c)ρ +
  cρ̃ ≥ 0`, equal pair weight c): reproduces their case and equal-weight cases, but for dominant singletons the bound
  exceeds `K_4(Y)` by **exactly c** at admissible local spectra `(r_A, r_B, r_C) = (0, 0.44, 0.44)` (qubit A pure,
  BC entangled; e.g. v = (1.5, 0.1, 0.05), c = 0.3, f = 0.2). The top-side bound `K_r(D) + Tr P` also fails there
  (8.3 vs 8.0). A proof must use the rank/orientation of `ρ̃` relative to the A = 0 sector, not just `P ≥ 0`.
- Numerical searches in this region never found a positive gap (best −1.5e-14 … −1.7e-12 at k = 4).

## Proof route notes for Q = I/2 (exact lemma statements; none closes the general case)

Write `w_I = μ_I 2^{−|I^c|}` (Q → 1): `X = Σ_I w_I ρ_I ⊗ 1`, `Y = Σ_I w_I P_I`, `P_I = |0⟩⟨0|^{⊗I} ⊗ 1`.
- **L0.** The ∅ term is a multiple of the identity and can be dropped (Q = I/2 only).
- **L1.** `ρ_I ⊗ 1 ⪯ P_I` (pure target majorizes every state; stable under ⊗1).
- **L2 (singletons, proved).** If μ is supported on ∅ and singletons, `X = Σ_l w_l ρ_l` is a Kronecker sum of
  commuting single-qubit terms; if `a ⪯ a'`, `b ⪯ b'` then the Kronecker-sum spectra satisfy `a ⊕ b ⪯ a' ⊕ b'`
  (write a, b as convex combinations of permutations of a', b'); hence Conjecture 2 holds for Q = I/2 with μ on
  singletons (and ∅).
- **L3 (chain mechanism of Prop. 3).** If `X = Σ_m c_m X_{F_m}`, `c_m ≥ 0`, nested families `F_1 ⊂ F_2 ⊂ …`,
  `X_F = Σ_{I∈F} ρ_I ⊗ 1 ⪯ T_F = Σ_{I∈F} P_I`, and the `T_{F_m}` are simultaneously diagonal with a common
  nonincreasing order, then `X ⪯ Σ c_m T_{F_m}` by Ky Fan subadditivity.
- **Obstruction to L3.** `T_F(x) = #{I ∈ F : I ⊆ Z(x)}`, `Z(x)` the zero set. For the chain {A} ⊂ {A,B} ⊂ {A,B,C}
  (singletons), `T_3` forces `100` before `011` while `T_1` forces `011` before `100`: no common order. So Prop. 3's
  mechanism does not extend verbatim to general μ (singletons are rescued by L2; mixed-size chains are not).
- **Missing lemma for a proof:** uniform-family majorization `X_F ⪯ T_F` for every family F of nonempty subsets that
  occurs as a weight-prefix, plus an alignment-free combination step (e.g. a poset-refined Ky Fan inequality in the
  sense of Guterman–Wolf applied to compatible marginals).

## Next bounded steps

Exact rational certification is ready if any candidate appears (rational ψ, μ, q and rank-k projector P with
`Tr(PX) > K_k(Y)`). Remaining: third/fourth-order analysis on flat directions in degenerate (μ,q) families, and an
attempt at the uniform-family lemma for F = all 7 nonempty subsets at Q = I/2.

Code: `code/search.py`, `code/second_order.py` (lane venv `../noncws-code/env/venv`, OMP_NUM_THREADS=1).
