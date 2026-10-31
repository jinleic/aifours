# Fixed-ε all-law TV and W2 stability at the registered optimum

Native clock observed before writing: **2026-10-28T18:19:00-0700 PDT**. This is a prospective repaired written composition, conditional on the two named prior theorem statements. It preserves the original review's MAJOR and MINOR findings; it is not a backdated clean verdict, source-proof closure, human/cross-model/formal review or novelty claim.

## Exact conclusions

For each **fixed finite ε>0**, let Fε consist of every Borel law satisfying ε-privacy for every Borel event and every shift in the full closed L1 unit diamond. Let μ* be the unique squared-Euclidean-cost optimizer in the named prior [LAW642 theorem](../../three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md), with cost V.

1. Every feasible sequence `μ_n => μ*` weakly converges to μ* in **total variation**. No moment convergence, symmetry or density regularity is assumed on the sequence.
2. Every feasible sequence with `J(μ_n)→V` converges to μ* in both **TV and Euclidean W2**.
3. The fixed-ε modulus `ωε(δ)=sup{TV(μ,μ*): μ∈Fε, J(μ)≤V+δ}` tends to zero. For some explicit positive fixed-ε constant, `ωε(δ)≥cε√δ` for all sufficiently small δ. This is a lower obstruction to an upper rate with exponent >1/2, **not** a square-root upper-rate theorem or an ε-uniform modulus.

The other operative research import is the literal [v241 diamond/rounded threshold statement](../../three-area-2026-10-23-96h/privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md). Neither imported proof DAG is re-proved here.

## Mandatory correction and actual reads

The parent read the full 173-LF [candidate](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-all-law-tv-stability-v1.md), both complete parent imports, the full [f68 review](../review-waves/f68-privacy-all-law-tv-stability/review-v1.md), and the complete 68-LF [radius/terminology addendum](/Users/jinleic/repos/aifours/information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/frontier-20261028-all-law-tv-stability-v1-addendum-1-f68-radius-repair.md). The pinned original review is **0 FATAL / 1 MAJOR / 1 MINOR**. M1 was a missing import-to-radius implication: v241 says the core is a diamond, but does not explicitly identify its scalar parameter with radius<1. Its review and the additive author repair supply the direct proof below. The MINOR replaces undefined ambient-topological “interior law” by **strictly privacy-slack law**.

This disposition adopts only the **composition with that repair**. It does not change the frozen original verdict or imply that the later KL, Lp, erosion, uniqueness or asymptotic candidates have been reviewed.

## Parent proof reconstruction

**Core noncontainment.** The optimizer's centrally symmetric convex core S cannot contain the whole sensitivity diamond D. On the diamond branch write `S=aD`, a>0. The actual feasible staircase family has

`J(a)=(1/3)E(a+N)^4/E(a+N)^2`, `P(N=j)=(1−b)b^j`.

Geometric moments give `J'(1)=2/[3(1+2m)]>0`, so a=1 is beaten by a slightly smaller radius. If a>1, the exact identity `u_(a−1)=b u_a+(1−b)1_((a−1)D)` makes its normalized law a mixture of Q_a and a strictly lower-cost uniform diamond. Indeed Q_a is a positive mixture of uniform diamonds with radii at least a, whose costs exceed `(a−1)²/3`. Thus a>1 is also impossible for an all-law optimizer. On the rounded branch, v241's threshold cubic and LAW642's value bound imply m<1/4 and exclude e₁ from S by the strict margin `2/3−m−2m²>7/24`. The boundary belongs to the diamond branch. This pays `D⊄S` without an unprovided scalar-radius identification.

**Pointwise privacy and local rigidity.** Integrating the original event inequality over the area-2 diamond gives `ν(A)≤|A|/(2b)`, hence all feasible laws have uniformly bounded densities. Shrinking-ball limsup representatives preserve privacy for **all point pairs** at L1 distance≤1, without an uncountable exceptional-set intersection. On each open canonical plateau of μ*, every point has an adjacent-level neighbor at distance<1: core noncontainment supplies one for level0; convex Minkowski decomposition supplies one for every outer shell. Small balls U,B inside the two plateaux satisfy privacy saturation in the limit.

Weak convergence gives their masses. The nonnegative privacy slack integrated on U×B tends to zero. Comparing two points of U through a common point of B bounds the local oscillation around the mean by this integrated slack, so the local L1 density error vanishes. Compact finite covers, the uniform density bound, null convex boundaries and weakly convergent tail masses give global L1 and TV convergence.

**Near-optimal and modulus caller.** Bounded costs give tightness. Fixed-shift inequalities pass to every weak subsequential limit through compactly supported continuous tests using the same subsequence; lower semicontinuity and the imported unique optimum identify its limit as μ*. The weak-to-TV result then applies. Weak convergence plus convergence of second moments gives W2. A sequence contradicting `ωε(δ)→0` would contradict this near-optimal conclusion.

Convolving μ* with independent triangular-coordinate noise of scale t preserves all privacy inequalities and adds exactly `t²/3` to the cost. In a specified far-quadrant strip of area t across one canonical density jump, the exact probability `P(U₁+U₂>1)=1/24` gives a TV lower bound proportional to t. Taking `t=√(3δ)` proves the lower modulus. A separate positive sinusoidal perturbation of a privacy-slack Laplace law converges weakly but has TV limit `1/(2π)`, so bounded densities and privacy alone would not justify the optimizer-specific conclusion.

## Exercised checks and boundary

The parent independently checked the all-m geometric-moment identity `2T₃T₂−mT₄=m²(1+2m)` with exact standard-library rational polynomials, and the exact feasible control `m=1: J(1)=25/3`, `J(99/100)=4965453067/596010000<25/3`. These are an algebraic identity and one diagnostic; the full all-law argument is written analysis. The f68 review independently reconstructs the representative, geometry, local-to-global, closure, W2 and strip proof and explicitly lists its standard-analysis and unverified research imports.

No explicit upper modulus, ε-uniform statement, broad nonadditive-DP conclusion, later entropy/Rényi result, formal theorem execution or publication priority follows.
