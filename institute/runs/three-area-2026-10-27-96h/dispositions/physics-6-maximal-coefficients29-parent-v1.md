# AME(4,6): at most 29 maximal coefficients

**Disposition: same-harness written support at the stated import boundary.** For every normalized complex AME(4,6) state in every local product basis, at most 29 coefficients have modulus `1/6`. The conclusion composes the new exclusion of `t=30` with the earlier `t≤30` argument and its classical no-OLS(6) import. Tarry's theorem was not reproved here. No state attaining 29, exact support minimum, novelty, human review, independent-model-family review, or formal/kernel proof is claimed.

Native clock observed before composing: **2026-10-28T20:41:44-0700 PDT**; this is a preceding observation, not an exact file-creation time.

## Statement and reconstruction

For each 2|2 cut, `U=6ψ` is unitary. A coefficient of modulus `1/6` exhausts its row and column in every cut. Write `t` for their number, `P` for their positions, `E` for the remaining support, and `n=36−t`. Removing the singleton rows and columns leaves an `n×n` unitary with at least two nonzero entries in every row and column. Each of the six pair projections of `E` has exactly `n` cells, each with at least two extensions, and `|E|≥2n`.

Suppose `t=30`, so `n=6`. The fiber-variation incidence inequality `2r≤3(n−r)` bounds each residual alphabet size by 3; every pair projection has size 6. The possible profiles are `(3,3,3,3)` or `(2,3,3,3)`. Counting the number `k(x)` of active coordinates of each `P` word gives

`Σ_P (k−C(k,2)) = Σ_i(6r_i−6)−Σ_{i<j}(r_i r_j−6)`.

The left side is at most `30`; the second profile gives `33`, so all alphabets are ternary. The residual partner degree at an active symbol is independent of the other party and at least two. Since it sums to six over three symbols, it is exactly two. Each missing pair set is therefore a perfect matching.

Relabel three coordinates so their missing matchings against the first are identity. Each first-coordinate fiber lies in a binary 3-cube. Either a remaining matching fixes the first symbol, deleting four vertices, or the three remaining matchings delete three distinct axis-parallel edges. Three cube edges cannot be covered by three vertices without forming a triangle, so at least four vertices are deleted. Thus `|E|≤12`, while unitarity gives `|E|≥12`. In the equality case each fiber has four entries and each binary two-coordinate contingency is either a full square or a perfect correlation. Two correlated pairs in one fiber would leave at most two distinct triples, so each fiber has at most one correlation. For each of the three pairs of other coordinates, two full squares have union size seven, exceeding the allowed six projected pairs; hence at least two fibers must be correlated on each pair. Six required correlations cannot fit in three fibers. This excludes `t=30`; the separately supported `t≤30` premise gives `t≤29`.

## Evidence and qualifications

- [Candidate](../../../../physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-global-ame46-maximal-coefficients29-v1.md), 54 LF, SHA-256 `2520967103592e125423a5a22c0ed5e86236582f149fb9375cb0c6f2070b476c`; parent read completely. The [t≤30 prerequisite](../../../../physics/evidence/three-area-20261027-96h/parallel-18/ame46-support/frontier-20261028-global-ame46-lower42-review-packet-v2.md), 107 LF, `50e97ebd0a30f2bcb1999fa85896f88bf4590d89fd897c60d9de53fe5775bedf`, was also read completely; its earlier reviewed use is recorded in the [≥44 disposition](physics-6-ame46-global-support-lower44-parent-v1.md).
- [Proof review](../review-waves/f113-ame-maximal-coefficients-29/proof-review-v1.md), `ce9fcfa5a1b69026a290047d793f24fc9d308665896102202c70884f5032078b`: no FATAL or MAJOR, four MINOR qualifications. The candidate's statement that excluding 30 is *equivalent* to `t≤29` requires the `t≤30` premise; the published example's count is an unverified side remark; the matching case wording is clarified above; an earlier contradiction found by enumeration is informational. Reviewer solver UNSAT reports were not accompanied by an independently checked proof certificate and are supplementary, not this disposition's proof.
- [Finite review](../review-waves/f113-ame-maximal-coefficients-29/finite-review-v1.md), `504acdbea85196815303f41a7808fae4b2d46adc3cda708091546f8984125640`, independently checked all 216 normalized forbidden-matching configurations and their cube/extension conditions. Its corrected v2 receipt preserves the v1 representation-error history.
- The [parent finite control](../review-waves/f113-ame-maximal-coefficients-29/parent-elementary-controls-v1.json), `69c81b1961f9249b3b535a2df3f6f1af795b1ab3b50ce30ee220be567acded3c`, records a separate in-session enumeration of all 46,656 labeled six-matching configurations: maximum 12 survivors, at most four per fiber, and zero 12-survivor sets with two extensions in all pair cells; it also checks the two profile right sides 33 and 30. This finite control does not replace the written reductions.

## Boundaries

The support inequality `N≥72−t` gives `N≥43` from this result, weaker than the already supported global `N≥44` bound, so it is not a new support-bound improvement. The ≥45, ≥46 and ≥47 candidates have their own unfinished dependencies and are not adopted by this record. The P-only diagnostic has no amplitudes or `E` support and is not an AME state. Same-harness checks are not external-family, human or formal verification.
