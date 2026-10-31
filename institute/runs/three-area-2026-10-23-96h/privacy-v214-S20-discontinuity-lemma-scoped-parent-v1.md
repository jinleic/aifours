# Privacy SOURCE-MATCH-U1: the optimal law has no continuous density version

Last actual parent clock before writing: **2026-10-27T08:32:55-0700 PDT**, observed at the live pins of the source and review below.

**Only §1 of the 57-LF status note is decided here.** At every finite ε, the unique optimal law μ_* of the adopted LAW642 theorem has no density version that is continuous. Hence every feasible law with a continuous density version has squared-Euclidean cost strictly above the optimum V. This is **WRITTEN_SUPPORTED at single-review level plus a parent hand check**: one complete review (v214-B) supports it. The other review, v214-A, remains HELD under [v227](privacy-v214-selected-input-checks-process-quarantine-v227.json), so the usual two-review gate is **not met**.

Not decided and still HELD under v227: the exact threshold `ε_t`, the diamond/rounded regime split, the regime table in §2 and the missing statements in §3. Also not decided: any positive gap for the infimum over all continuous-density laws, the external MDA per-cost bridge `V = (2/3)·V1`, or any claim about what a named publication actually proves. No source equivalence, novelty, priority or worldwide-absence claim follows.

## Complete reads and bindings

| Input | LF | SHA-256 | Read |
|---|---:|---|---|
| [Author status note (S20)](../../../information-science/evidence/three-area-20261023-96h/parallel-18/privacy-diamond-mse/privacy-SOURCE-MATCH-U1-discontinuity-separation-and-regime-status-v1.md) | 57 | `cbd9375313b61a152e1ded34bc4529e70f37c72ee2e275380466a790cb3818c6` | complete, through ending |
| [Review B — PhysicsMOQLS8-2](../../../physics/evidence/three-area-20261023-96h/parallel-18/moqls8/peer-review-v214-B-v1.md) | 347 | `6ad5a2b69aa346ae09fa2534f7e24c213df3b2dd4baf3174f1427398d790f63a` | complete, raw 1–90/91–180/181–265/266–347 |

The pin of S20 follows the [v227 pin addendum](privacy-v214-selected-input-checks-process-quarantine-v227-pin-addendum-1.json), not the malformed entry in v227 itself. The [v214 manifest](peer-review-wave-eighteen-v214.json) binds the review scope. The operative import is the adopted [LAW642 boundary](privacy-all-law-self-contained-parent-v1.md); NORM148 at its [adopted boundary](privacy-all-norm-all-profile-attainment-rigidity-gap-entire-parent-v1.md) is not used by this lemma. Review A was not used.

## The supported statement

Fix finite ε > 0, `b = e^(-ε)` and the closed diamond `D = {|h1| + |h2| <= 1}`. The feasible class is every Borel probability law on the plane satisfying the pure-DP shift inequality for every Borel set and every shift in `D`. By LAW642, the unique optimal law has canonical density `p_* = Z_*^(-1) b^(n_*(z))` with `n_*(z) = min{k >= 0 : z ∈ S_* + kD}`; its core `S_*` is compact and convex with nonempty interior.

1. **Two open sets meet at every boundary point.** Fix `x0 ∈ ∂S_*`. A convex body is the closure of its interior, so `x0` is a limit of points of `int S_*`, where the canonical density is `Z_*^(-1)`. An outward supporting direction `u` gives `x0 + δu ∉ S_*` for small δ > 0. These points lie in `int(S_* + D)` because `D` contains a neighbourhood of 0. The open shell `int(S_* + D) \ S_*` has index exactly 1, so the density there is `Z_*^(-1) b`.
2. **No continuous version.** If a continuous `f` equalled `p_*` almost everywhere, then `f` would equal the constant on each of the two nonempty open sets, hence on their closures. At `x0` this gives `Z_*^(-1) = Z_*^(-1) b`, impossible because `0 < b < 1`.
3. **Strict cost.** LAW642's optimum is unique as a LAW. A feasible law with a continuous density version is therefore not μ_*, so its cost is strictly above V; infinite cost is allowed.

Review B reconstructs exactly this argument, with no new FATAL, MAJOR or MINOR at this scope. It adds the necessary ceiling: **no positive gap for the infimum over the continuous-density class** is concluded, because no attainment theorem for that class is supplied.

## Parent hand check and one precision remark

Main checked the three steps above in writing. The proof also gives a slightly sharper local statement. Since every ball around `x0` meets both open sets in positive measure, no density version of μ_* is continuous **at any single point** of `∂S_*`. Because `S_*` contains a neighbourhood of the origin, a candidate density that is singular only at the origin is still excluded when it is continuous at some point of `∂S_*`. This remark is a parent observation, not a separately reviewed gate.

## Application ceiling

The note's consequence is a statement about representations. It does not establish what the named publications prove. Following review B §14:

- A source conclusion separates from μ_* **if** its actual optimizer is feasible for the registered model and has a density version continuous at some point of `∂S_*`. That condition must be verified from the source itself.
- The named families KHP, AS21, JY24, Wei and DA26 are **not** authenticated here. Their hypotheses, closed-`D` feasibility and unread ranges remain uncovered.
- SCDF arbitrary-core shells, the EG frameworks and broad templates are not excluded by this argument.

## Process boundaries

- **v227 remains binding.** The author's selected diagnostic checks in the threshold manuscript and review A's re-performed checks are separate PROCESS MAJORs. All checks and their consumers have ZERO credit. The threshold/regime claims and the v214-A verdict remain HELD. This lemma consumes none of them; review B states it is independent of the threshold allocation.
- **Review B:** the reviewer disclosed specific prior privacy contact (its earlier 107-B review and the review's return metadata). This is serial, same-harness, non-blind review. Its own earlier findings, including four cadence findings and the new 31m40 MAJOR in [v238](MOQLS-RQLS-post-v227-v235-idle-cadence-findings-v238.json), remain.
- **Author:** all earlier privacy findings and ZERO quarantines remain, including ENTIRE116, cp102/cp108 and every consuming calibration or selection guide.

Only written reasoning and file/hash/LF/clock metadata were used. N4 remains UNKNOWN with historical child exit unestablished; auxiliary214 STOP and the scientific HOLD persist. Same eighteen owners, science cutoff **2026-10-27T11:05:38-07:00** and delivery **12:35:38-07:00** are unchanged. This is not formal, kernel, human, configured-family, executable or novelty acceptance, not a privacy-optimum or source-equivalence resolution, and not round closeout.
