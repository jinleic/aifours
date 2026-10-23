# Certified charts for the D2 bound — specification v2

Worker `MathPhaseType3`. v1 (`proof/charts-spec-v1.md`, sha 5a43c252…1ff1, frozen before the certified dual runs) is
kept unchanged. v2 makes four changes and nothing else; every other definition is as in v1.

1. **SWC.** The coefficient implementation is exact: `me3dual_v9.py`, spec `code/spec_dual_v3.json`, run d03-SWC.
   This follows hostile review `review/me3-charts-codex-v1.note.md`, finding 1. The SWC run d02 under v1/spec v2 is
   invalid.
2. **LD1/LD2 quantifiers.** They are narrowed to the physical domain, the s-union is stated explicitly, and one "iff"
   is replaced by a sufficient implication (finding 5).
3. **Coverage checker.** `code/check_cover_v3.py` hard-codes the outcome sets and the domains, rejects FAIL
   unconditionally, checks depth, and binds each leaf file to its run summary (finding 4).
4. **Libraries and drivers.** The library and driver versions are restated for every chart.

## Common conventions (unchanged from v1)

* T = 11/50, κ = 1/(1+T) = 50/61.
* Normal form: real pole 1, complex pair 1 + ξ, 1 + ξ̄ with ξ = δ − iω, δ ≥ 0, ω > 0. Ratio r = δ/ω. Extreme-ray
  phase φ = ωτ ∈ [0, θ₁(r)].
* Arithmetic: python-flint 0.9.0 (FLINT 3.6.0, Arb) at 128 bits. Boxes have exact rational endpoints and enter as
  `arb(lo).union(arb(hi))`.
* Python-level arithmetic on certified paths is audited in `proof/float-audit-v1.md`: Python integers enter exactly,
  and floats appear only in the G-chart TRIANGLE-angle heuristic.
* MVF enclosures, the split rule and the FAIL/cap rule are as in v1.

## Libraries and drivers per chart

| Chart | Driver | Library chain | Spec | Run | Audit (check_cover_v3) |
|---|---|---|---|---|---|
| P | `cert_primal_v3.py` | `me3lib_v1`, `me3jet_v1` | `spec_primal_P_v1.json` | c03-primalP | b03-cover-P |
| G, SWB, LW, LD1, LD2 | `cert_dual_v5.py` | `me3dual_v7` → `v6` → `v4` / `v3`; `me3jet_v1/v2` | `spec_dual_v1.json` | d01-* | b03-cover-* |
| SWC | `cert_dual_v7.py` | `me3dual_v9` (corner code self-contained; `me3jet_v1`) | `spec_dual_v3.json` | d03-SWC | b03-cover-SWC |

## Chart changes

### SWC (replaces the v1 SWC paragraph)

g(ξ) = log W = Σ_{j≥1} c_jξ^j for |ξ| < min(1, 1/√B), with

  c_j = (−2 Re(p^j) + 3(−1)^j)/j,  p = (s(1−s)(1 + i√(2κ−1)) − κs²)/N₁.

* This p equals (−A + i√(4B − A²))/2, because 2 Re p = −A and |p|² = B. The cancellation-free form avoids a square
  root of a ball.
* In the code, the Python integer 3(−1)^j is added exactly to the ball −2 Re(p^j), and the sum is divided by the
  Python integer j in ball arithmetic. Every computed c_j ball therefore contains the exact c_j at every box point.
* X_m, U_m, Ψ, Ig, the tail bounds and the acceptance tests are as in v1, with N = 20.

### LD1 and LD2: physical-domain quantifiers (replaces the v1 LD paragraphs and coverage line)

The charts use padded rectangles. A certificate is claimed only for the **physical points** of each box:
* LD1: s ∈ [1/16, 1), d = 1/(1+δ) ∈ (0, 1/65] and β = arctan(ω/(1+δ)) ∈ (0, π/2).
* LD2: χ ∈ (0, 1), ρ_t > 0 and β ∈ (0, π/2), with s = χρ_t ∈ (0, 1/16] and d = (1−χ)ρ_t / cos β ∈ (0, 1/65].

The points of a padded box with β ≥ π/2, d = 0, s ∈ {0, 1}, ρ_t = 0 or χ = 1 are limiting or nonphysical faces with
no pole interpretation. Nothing is claimed there. For example, at s = 1 and β > π/2 the factor d cos β is negative,
so β + arg P is not an argument of W.

For every physical point of a CERT leaf:
* LD1: ζ = 1/(1+ξ) = d·cos β·e^{iβ}, W = ζP, P = w₁ + w₂ζ + w₃ζ², and δ/ω = (1−d)/tan β > 0.
* An accepted candidate α ≥ 0 is an argument of W with |W| ≤ e^{−(1−d)α/tan β} = e^{−δα/ω}. This is the RADIAL
  certificate.
* Candidates:
  * β + (principal arg P), if Re P > 0 on the box and the result is ≥ 0;
  * β + Arg₊ P;
  * the fallback Arg₊ W ∈ [0, 2π), for which 0 ≤ Arg₊W / tan β ≤ 2π / tan β_l. This remains valid when the box's
    upper β endpoint exceeds π/2; physical points still have β < π/2.
* **Boxes with β_l = 0.**
  * Re P > 0 on the box and arg P(0) = 0, so α(β) = ∫₀^β (1 + Im(P_β/P)) du.
  * **If** 1 + inf_box Im(P_β/P) ≥ 0, **then** α ≥ 0. This is a sufficient condition only; v1's "iff", and the same
    word in the docstring of the executed `me3dual_v3._ld_ratio_small_beta`, are superseded.
  * Also α/tan β ≤ (1 + sup Im(P_β/P))·(β/tan β) ≤ 1 + sup Im(P_β/P).
* LD1 bounds 1 − d by its box ball.
* LD2 uses P̂ = P/ρ_t², with χ and ρ_t held fixed in P̂_β. It replaces 1 − d by 1, which is conservative because
  the physical exponent δα/ω ≥ 0.
* LD2 SKIP leaves contain no physical point:
  * skip-s: χ_lρ_{t,l} > 1/16, exact.
  * skip-d: (1−χ_h)ρ_{t,l} > cos(β_l)/65, ball comparison. Since d cos β = (1−χ)ρ_t ≥ (1−χ_h)ρ_{t,l} and cos is
    decreasing on [0, π], every point of the box has d > 1/65 or cos β ≤ 0.

**s-coverage is by the union, not by either chart alone.** For δ ≥ 64 (d ∈ (0, 1/65]):
* every s ∈ [1/16, 1) is a physical point of LD1;
* every s ∈ (0, 1/16] is a physical point of LD2, because ρ_t = s + d cos β ∈ (0, 1/16 + 1/65] = (0, 81/1040] and
  χ = s/ρ_t ∈ (0, 1).
* So LD1 ∪ LD2 covers every s ∈ (0, 1), that is, every test centre μ = s/(1−s) ∈ (0, ∞).

## Coverage of all D2 pole configurations (ξ = δ − iω, δ > 0, ω > 0; replaces the v1 coverage list)

* δ ≥ 64: LD1 ∪ LD2, physical points, s ∈ (0, 1).
* δ < 64 and ω ≥ 640: LW (ν = 1/ω ∈ (0, 1/640]), all s ∈ [0, 1].
* δ < 64 and ω ∈ [1/5, 640]: P (Lemma M) if ω ≤ 40 and δ ≤ 3ω. Otherwise G, all s ∈ [0, 1], where G's SKIP leaves
  lie in P.
* δ < 64 and ω < 1/5: SWC if δ ≤ 3/10, otherwise SWB, all s ∈ [0, 1]. The ω = 0 faces are normalized extensions; the
  RADIAL conclusion is used only for ω > 0.

Closed boundaries overlap safely (δ = 64, ω = 640, ω = 1/5, δ = 3/10 and ∂P). The faces s ∈ {0, 1} extend the
rational formula for W; every finite θ > 0 has s ∈ (0, 1).

## Coverage audit v3 (replaces the v1 audit sentence)

`code/check_cover_v3.py` performs the following checks. It evaluates no chart test.
* **Spec.** For each chart it verifies that the spec's kind, T, variable order (primal: r, ω, φ), outer domain,
  parameters and series length equal the hard-coded values above. For LD charts it also certifies β_top > π/2 by a
  ball comparison and checks ρ_t top = s_max + d_max and LD1 s_lo = LD2 s_max exactly.
* **Outcomes.** Each leaf outcome must lie in the chart's hard-coded set:
  * P: SGE, DPOS, INFEAS;
  * G: CERT:small, CERT:radial, CERT:radial-mvf, CERT:triangle, SKIP:in-primal-P;
  * SWB: CERT:bedge, CERT:bedge-mvf;
  * SWC: CERT:corner, CERT:corner-mvf;
  * LW: CERT:small;
  * LD1: CERT:ld1;
  * LD2: CERT:ld2, SKIP:skip-s, SKIP:skip-d.

  FAIL is rejected unconditionally.
* **Tree.** Every leaf depth is ≤ the spec's max_depth. Per initial cell, the leaf paths must be exactly the
  depth-first leaves of a full binary tree. Every SKIP rule is re-checked.
* **Run binding.** The SHA-256 of the uncompressed leaf lines and the outcome counts must equal the run summary's,
  and the summary must report certificate_ok with no cap hit.
* **Limits.** This is a geometric and bookkeeping audit only. The predicates are checked by replay (the parent's
  desks, and ME3Reductions' point replay).
