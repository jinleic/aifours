# Unrestricted six-state PH barrier — parent disposition v1

Clock actually observed before creation: **2026-10-23T14:35:00-07:00 PDT** (rounded; the receipt below records exact stamps). Apply both [verification](parent-verification-erratum-v1.md) and [timestamp](parent-timestamp-erratum-v1.md) qualifications. No mathematical program, solver or proof assistant ran for this disposition.

## Decision

**B6 SUPPORTED at the in-harness written-check level: for the frozen family H_{1,2}, a PH representation with at most six transient states exists if and only if `beta^2 <= 1/2`, with no constant-diagonal, companion, irreducibility or layer ansatz on the hypothetical PH6.** Consequently, composed with the separately checked G7 construction, the **unrestricted minimum PH order is exactly 7 on `1/2 < beta^2 <= 53/96`**.

This closes the six-versus-seven residual band of the frozen target at this verification level. The minimum order on `(53/96, beta_*)`, the later non-PH boundary and the book's general minimal-representation problem remain open. Novelty remains **NOVELTY_UNCLEAR**; no kernel, human, cross-vendor or priority claim is made.

## The load-bearing constant, explicitly

The decisive inequality is Lemma M at **n = 6** with sharp constant **(n−2)/√(n(n−1)) = 4/√30**:

    tr(X³) ≥ −(4/√30)·(tr X²)^(3/2)   for every real 6×6 trace-zero Metzler X.

The parent specifically confirms — not merely the symmetrization mechanics — that the assigned hostile reviewer **independently re-derived this constant at n = 6** (review §2): Lagrange two-point extremum, k=1 minimality via the squared-magnitude expression `[n²/(k(n−k))−4]/n` maximized at k=1, sharpness by an explicit one-negative/five-positive diagonal Metzler attainer, and the n=2 consistency check. With `12hR ≤ (4/√30)·tau2^{3/2}` squared into `tau2³ ≥ 270h²R²` (270 = 15·(4/√30)²·… from the exact arithmetic), this constant is precisely what the polynomial contradiction in identity (7) consumes. Without the n=6 constant, the min=7 conclusion is one unchecked constant away; with it, the chain is closed at this review level.

## Evidence

- Author manuscript: [proof-unrestricted-six-state-barrier-v1.md](/Users/jinleic/repos/aifours/mathematics/evidence/three-area-20261023-96h/parallel-18/phase-type/proof-unrestricted-six-state-barrier-v1.md), SHA-256 `8ba04931bb26e9fec097cb75793aa99b2e5d4d2309da94e1be9328dacb830c25`. Parent read all 195 lines.
- Hostile in-harness reconstruction: [peer-review-PH6-unrestricted-barrier-v1.md](/Users/jinleic/repos/aifours/physics/evidence/three-area-20261023-96h/parallel-18/depolarizing-majorization4/peer-review-PH6-unrestricted-barrier-v1.md), SHA-256 `2847c63465cd3a196bf358b11cee818c83b24cb054c1c05144c94331c1ead95d`, **0 FATAL / 0 MAJOR / 0 MINOR**. Reviewer observed the source pin independently and reconstructed every component.
- Upper constructions: verified v2 manuscript `b9263915…` (order 5/6 through β²≤1/2, self-contained) and G7 `59618311…` with its separate physics-lane reconstruction and the parent's [G7 disposition](G7-and-reference-regions-parent-v1.md). At β²=1/2 exactly, T6 exists and the order-5 trace obstruction applies, so the minimum is 6 there — the iff includes its endpoint.

Parent spot-checks actually performed: hand verification that `270 = 6³·(4/√30)²/…` follows from `12hR ≤ (4/√30)tau2^{3/2}` squared — specifically `(12)²·30/16 = 270`; the coefficient table of identity (7) (`45/4, 58, 90` positive, `d h³` and `h⁴` cancelling); and the sign logic `tau2 ≤ tau20`, `R ≥ R0`, both under Δ≥0 with d,h>0.

### Additive notation correction (recorded 2026-10-23, after owner report; original lines above immutable)

Line 9's residual interval should read `beta in (sqrt(53/96), beta_*)` — square-rooted, matching the theorem statement on line 7 which correctly uses `beta^2`. The theorem, constants and disposition are unaffected; only the residual-band notation on that one line was inconsistent. Reported by MathResearch96h after full read; no re-edit of frozen bytes.

## Relation to earlier necessary-only packets

L6 (layer/numerator identities, with its ℓ≥1 minor repair), U6 (uniform-rate), the nonuniform-gap, hidden-rate-Hamiltonian and this barrier all targeted the same residual class. B6 shows that class is **empty**; the earlier necessary conditions are now historically interesting but vacuous on the excluded region. Their files, review histories and the L6 minor qualification remain unchanged; nothing is retroactively accepted or erased.

## Boundary

The result is written-check level: author + one independent in-harness hostile reconstruction + parent spot-checks, all sharing the supplied proof and steering context. The matrix-moment mechanism (geometric-mean symmetrization; symmetric eigenvalue skewness) is classical in character and may have a named equivalent; priority is unestablished. No Lean/kernel verification was performed or implied by any "reconstruction" wording. The order-blowup behavior near β\* and the existence threshold β\* are unaffected and retain their own import boundaries.
