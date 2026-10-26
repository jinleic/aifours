# Unrestricted planar privacy/MSE: parent written disposition

Actual clock observation preceding this record: **2026-10-23T15:20:01-0700 PDT** (`/bin/date`). Written reasoning and metadata only; no scientific program, finite numerical check or formal kernel was used for this disposition.

## Decision

**SUPPORTED at the in-harness written-check level**, in the exact full-continuous-diamond model over **all Borel probability laws**, with `b=exp(-epsilon)`:

1. For every `0<b<1`,

       V_b >= 2 sqrt(b/(3pi)+b^2/pi^2) - 2b/pi.

2. The unrestricted leading weak-privacy optimum is

       lim_(b downarrow0) V_b/sqrt(b) = 2/sqrt(3pi).

   Equivalently, `exp(epsilon/2)V(epsilon)` tends to that constant as epsilon tends to infinity.

The optimized homothetic-diamond family separately has limiting cost `(2/3)sqrt(b)`, so its cost/global-optimum ratio tends to `sqrt(pi/3)>1`. This is a dependent comparison, not an additional independent discovery.

**Not established:** exact finite-epsilon V, a finite-epsilon minimizer, global finite-b optimality of disk cores, formal/kernel or human acceptance, novelty or publication priority. The active finite-epsilon target is unchanged under [info-1 continuation](info-1-continuation-v1.json).

## Frozen evidence and actual coverage

Repository-root-relative source:

`information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/proof-unrestricted-low-privacy-constant-v1.md`

SHA256 **`2a7c0e4ad18fcbed81ab119e5634b112e39b9252403752c2ea20c2c18865eeff`**. Parent read the complete344-line body, not just its theorem/header.

Actual separate return:

`mathematics/evidence/three-area-20261023-96h/parallel-18/ordered-olson/peer-review-privacy-unrestricted-asymptotic-v1.md`

SHA256 **`e05781ec195ac372bd8407cbc801c2ca7b1779a392149aada92661e96b83b486`**. Parent read the complete184-line body. The actual verdict is **0 FATAL / 0 MAJOR / 0 MINOR** at the two theorem and dependent gamma-asymptotic scopes. Reviewer disclosed prior octagon exposure and did not transfer that verdict to this proof. Same-harness supplied-proof reconstruction is neither blinded nor cross-vendor review.

Mandatory source companion, read completely52lines:

`information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/source-audit-unrestricted-v1.md`, SHA256 **`d02690071f6f8f9c5e177bfa53156be9e3dd05bb2c1abf987f37805dc2c09f6a`**.

All these bytes were independently rehashed by the parent as metadata. Hashes bind snapshots; they do not prove mathematics.

## Parent reconstruction actually performed

### All-law lower bound, without hidden regularity

For any Borel Lebesgue-null N, integrate the imposed inequality over the area-two diamond. Joint measurability of `1_N(x-h)` and Tonelli make the translated-null-set integral zero, proving absolute continuity; no initial density hypothesis is inserted.

For each **fixed** h, all-Borel measure domination gives `p(x+h)>=b p(x)` for almost every x. Applying Tonelli to the jointly measurable bad-pair set then gives almost every x a good **almost-every-h** section. This is sufficient and is not falsely upgraded to one density version satisfying every shift pointwise.

Integrating at such an x shows its value is at most `1/(2b)`, so the essential peak M is finite and positive. Essential near-peak sets have positive measure and meet the good full-measure set, giving `m_n=p(x_n)->M` without an attained or near-origin peak. The translated diamond floor is `b m_n`; subtracting it leaves exact mass `1-2b m_n` and cap **M**, not m_n.

The density-cap moment minimum is a centered disk: comparison with `M 1_(B_R)`, `R^2=alpha/(pi M)`, gives `alpha^2/(2pi M)`. The parent checked the sign of `(norm(x)^2-R^2)(q-q0)` on both sides of the disk and the finite/infinite-moment split. The translated diamond moment is `2/3+2 norm(x_n)^2`, so discarding the translation term is valid even if x_n escapes.

Consequently each feasible law satisfies

    J >= (2/3)b m_n + (1-2b m_n)^2/(2pi M).

Only a finite scalar limit is taken; no spatial convergence or dominated convergence of residual densities is assumed. At the limit the expression is

    1/(2pi M) + (2b/3+2b^2/pi)M - 2b/pi.

AM–GM gives precisely the stated lower bound. Relaxing the allowed M interval can only weaken a lower bound. This proof covers nonsymmetric laws, nonzero means and every feasible Borel law, not a restricted core family.

### Matching feasible upper bound, with the core treated sharply

The disk-core sets `B_r+kD` give pointwise two-way shell-index control for every diamond shift. The exact parallel-polygon decomposition has area `2k^2+4sqrt(2)rk+pi r^2`, including k0 separately, so Tonelli gives finite positive normalization `pi r^2+4sqrt(2)rT1+2T2`.

At k0 the quadratic moment is kept **exactly** `pi r^4/2`, with probability factor1-b. At k>=1, `B_r subset sqrt(2)rD` bounds every full tail by a homothetic diamond. Expanding the fourth power gives coefficients `1,4sqrt(2),12,8sqrt(2),4`; the final constant term carries tail probability **b**, not1. This is an upper envelope, not an asserted exact moment for every rounded shell.

With `r=(4/(3pi))^(1/4)b^(1/4)`, the core and T4 terms each tend to `1/sqrt(3pi)` after division by sqrt(b). The remaining terms vanish with powers `b^(1/4),b^(1/2),b^(3/4),b`, multiplied by `T_j/b->1`. The explicit finite envelopes avoid interchanging an uncontrolled shell series with a limit. Matching the all-law liminf proves the sharp leading constant without assuming a minimizer exists.

For the dependent diamond-family statement, the uniform centered-moment lower bound gives liminf2/3; the allowed parameter `gamma=b^(1/4)` gives numerator `2b+o(b)` and denominator `sqrt(b)+o(sqrt(b))`, hence the matching upper limit. The ratio is `sqrt(pi/3)`.

## Novelty and source limits

The arbitrary-core reachability/Minkowski-shell mechanism is **published in SCDF2013**, not a new construction and not a claim to an origin before that paper. Absolute continuity also has prior theorem-level treatment in Melbourne–Diaz–Asoodeh2026 Theorem7; the bathtub inequality and measure tools are standard. The standalone proof does not make those intermediate ingredients novel.

The possible scientific contribution is the **precise mixed-geometry all-law bound and sharp optimum constant**. Its current-source screen is bounded; no exact match was located at the read interfaces, which is not a proof of absence. **NOVELTY_UNCLEAR** remains operative. Same-norm staircase theorems, stronger distance-proportional Lipschitz privacy and input-dependent bounded mechanisms have different interfaces and are not silently treated as this model.

The complete finite-epsilon optimum remains open in this dossier. This disposition does not transfer to future refinements or other dimensions and does not promote a broad book problem as solved.
