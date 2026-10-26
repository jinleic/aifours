# H_{1,2} PH-existence threshold — parent written check v1

Before-creation clock observed: **2026-10-23T13:10 PT**.

## Verdict

**WRITTEN_CHECKED (in-harness level), at the declared O'Cinneide import boundary.** The exact all-parameter PH-existence threshold `k>k_*` (equivalently `0<beta<beta_*=1/k_*`), the excluded boundary `beta=beta_*` (nonnegative density with one positive-time zero, not PH), and the non-PH regime `beta>beta_*` (signed inverse transform) are supported by two independent full written reconstructions — the author manuscript and the PhysicsResearch96h review (0F/0M/0m) — plus this parent spot-check.

## Parent spot-checks actually performed (hand algebra)

- `∂_k [e^{-kx} P_k(x)] = -e^{-kx}(1+k²)x³/2`: verified by direct differentiation, confirming strict decrease of `m_k` in k.
- `m_0(x)>1` via `(1+x²/2)² − (1+x²) = x⁴/4 > 0`: verified.
- `m_{1/ξ}(ξ) = e^{-1}(y/2 + 2/y)` with `y=√(1+ξ²)`: verified via `P_{1/ξ}(ξ) = (ξ²+5)/2`; and `y>ξ>2π>6` gives `y/2>3>e`, hence `k_*ξ>1`.
- Reviewer's derivative-coefficient identities for `G_k'` and the root-sign structure (one root per `(jπ, jπ+π/2)`, even-j minima) read and accepted as correctly derived.
- The PH strict-positivity argument (nonnegative B-series with at least one accessible exit path) verified conceptually; it correctly handles reducible T and zero density at t=0.
- Import boundary: parent separately opened Liu–Yao–Zhang v2 §2 (positive density on (0,∞), real coefficients, coprime, L(0)=1, unique maximal-real-part pole; general multiplicities allowed) and confirms every hypothesis holds for H at `k>k_*` with `-c` the unique maximal pole.

## Consequence for the frozen target

Combined with `mathematics-parent-check-v1.md` (Theorem B), the H_{1,2} parameter space is now classified as: β≤1/√5 (min order 5), 1/√5<β≤1/√2 (min order 6), 1/√2<β<β_* (PH exists, exact minimum OPEN), β=β_* (not PH), β>β_* (not PH). The minimum-order band (1/√2, β_*) remains the primary open obligation; no claim of minimum order there is made.

Novelty **NOVELTY_UNCLEAR**; original O'Cinneide 1990 proof not authenticated; no Lean/kernel claim. Outstanding author obligations: the (1,1)→cot(π/3) anchor remark and the cot-vs-1/√5 structural remark (already ordered; apply in a numbered successor/addendum).
