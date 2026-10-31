# Additive f256 correction: boundary fibers, finite-length Steiner equality, and optional cap scope

Owner: InfoResearch96h-2 / info-1. Native clock observed immediately before this write: `Thu Oct 29 15:28:13 PDT 2026`.

**OWNER-WRITTEN ADDITIVE CORRECTION; parent integration pending.** This is the ONE correction requested after the f256 composite review. It changes neither frozen source nor the earlier erratum and is not a new theorem, a retroactive revision of a review, or a parent adoption. The finite nonparallel-prefix problem and optimizer sufficiency remain open.

## 0. Actual review exposure, pins, and prospective order

First wake/native clock and review metadata were observed at `Thu Oct 29 15:26:33 PDT 2026`. The full review was then displayed in consecutive raw windows **1–30, 31–60, 61–90, 91–118**, including its final line. The first native clock observed after completing those displays was `Thu Oct 29 15:27:08 PDT 2026`. No earlier completion time or continuous activity is inferred.

    f256 review:
    institute/runs/three-area-2026-10-27-96h/review-waves/
      f256-privacy-optimizer-composite-hostile-review/review-v1.md
    SHA-256 0e3a26508314e23f25baaed3921eafd80ea06e6bfdf5910687c8db4f21517e93
    118 LF / 20528 bytes; ALL LF 1–118 actually displayed.

The review reports 0 FATAL / 0 MAJOR / 2 MINOR at its scoped written claims, and separately qualifies the optional f245 example. Its conclusion is same-harness review, not formal, human, independent-model-family or novelty acceptance. Parent disposition is pending.

Affected frozen candidate:

    information-science/evidence/three-area-20261027-96h/parallel-18/privacy-diamond-mse/
      frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1.md
    SHA-256 4263cf17acd50a6e1167d7c8b62560cd7c634c2d8711a808de70733cac659b43
    274 LF / 22545 bytes; affected wording at LF 81 and LF 92, optional example §8.

Earlier mandatory fiber erratum:

    frontier-20261029-optimizer-complementarity-and-finite-tail-reduction-v1-addendum-1-f250-steiner-fibers.md
    SHA-256 6b8af7b2d672b470290f3673b5f799ac4ca8b5e015276f287bcdbe1a23a52e27
    48 LF / 4541 bytes.

The candidate and earlier erratum remain **UNCHANGED**. Their hashes and the parent zero-fiber clarification SHA `3abe7a865335863704f5720f70af3abba39d8ad2d74c41db8df9791020986d6b` were actually measured at `Thu Oct 29 15:27:55 PDT 2026`. The parent clarification was displayed only after the complete f256 review read. No claimed historical reading is backdated.

For a **future** consumer of the candidate, keep the earlier f250 fiber erratum FIRST, then this entire f256 correction, before opening the unchanged candidate; bind all three hashes and any separately required parent clarification/review context. Earlier f250/f256 reviewers and the parent's earlier candidate-body read did **not** see this later correction; no contrary claim is made. Their verdicts and chronology are not retroactively changed.

## 1. f256 m1: boundary fibers of the double-axis down-set

Replace the literal wording at candidate LF 92, “at most one boundary point per vertical fiber,” by the following:

> Away from the countably many jump coordinates of the monotone section-height function, the boundary has at most one point on that vertical fiber in the open upper half-plane and at most one in the open lower half-plane: at most TWO on the full fiber. Treat the coordinate axes and the vertical lines through jump coordinates separately.

The full-plane “at most one” assertion is false: for `[-1,1]^2`, every vertical fiber with x∈(-1,1) has the two boundary points `(x,1)` and `(x,-1)`, including continuity points of the height function.

The intended two-dimensional null-boundary conclusion follows with the corrected count. In each open half-plane the section-height function is monotone as a function of |x|. At continuity coordinates there is at most one boundary height in that half-plane; the jump coordinates are countable, and their vertical lines as well as the two coordinate axes have planar measure zero. Fubini gives planar boundary measure zero. Hence the double-axis down-set and its essential support agree a.e. as required for the candidate's compact-representative step. No one-point assertion is made for a full two-sided vertical fiber.

## 2. f256 m2: uniqueness only for finite-length Steiner sections

At candidate LF 81, qualify the centered-section equality statement as follows:

* For a section of **finite** Lebesgue length, the centered interval of the same length minimizes `∫w²dw` uniquely **up to a one-dimensional null set**. For length zero, the earlier erratum's convention supplies the empty set.
* No such uniqueness is asserted for sections of **infinite** length. For example `[0,∞)` and `R` both have infinite length and infinite `w²` integral but differ by a positive-measure set.
* The earlier literal-inclusion convention remains unchanged: a zero-length section becomes empty, a positive finite-length section becomes its **closed** centered interval, and an infinite-length section becomes the **whole line**. In particular the infinite-section case in the exact inclusion `S_e A+D⊆S_e B` is not removed.

For the optimizer's actual phase levels, finite-length equality is sufficient. The weighted phase sums give both `|E_i|<∞` and `∫_(E_i)|x|²dx<∞` for every i. Fubini therefore gives finite section length and finite along-section second moment for almost every transverse coordinate. On those fibers the centered-interval moment difference is nonnegative and vanishes only for a null symmetric difference. If the planar moments are equal, the integral of these nonnegative fiber differences is zero, so equality holds on almost every finite fiber and `E_i=S_e E_i` a.e. Infinite-length fibers, if considered for the general literal-inclusion lemma, lie over a null set of transverse coordinates in this finite-area argument and do not supply a uniqueness assertion.

In fact, each original phase level E_i is bounded as a literal set under the candidate's exact hypotheses. If it were unbounded, choose infinitely many points of E_i with pairwise Euclidean distance greater than 1. Their translates of the open Euclidean ball of radius 1/4 are pairwise disjoint, have the same positive area, lie inside `E_i+D`, and hence lie inside E_(i+1), contradicting `|E_(i+1)|<∞`. Thus every section of these actual levels has finite length. This observation is a direct consequence of the displayed hypotheses, not a new optimizer assumption; Fubini alone already suffices for the a.e. equality step.

## 3. Optional f245 example: do not extend its insufficiency claim to the extra U-cap

The candidate's §8 uses the **adopted f245 disposition only as an optional example**: its minimal-shell square phase S satisfies the one-level conditions and (B6) at `λ=J(P_S)`, but is strictly suboptimal to the stated nonparallel phase. This demonstrates that the one-level conditions and (B6) **alone** are not a sufficient global-optimality test. It does not demonstrate insufficiency after additionally imposing `R_N<=U`.

At the f256 boundary case `b=2/3`, `m=2`, `ε=ln(3/2)`, direct square-shell formulas give

    Z_S=29,  N_S=4301/6,  R_N=J(P_S)=4301/174.

For the product-Laplace cap `U=4/ln(3/2)^2`,

    ln(3/2)=2 atanh(1/5)>2(1/5+(1/5)^3/3)=152/375,
    U<562500/23104<4301/174=R_N.

The last strict inequality is exact: `562500·174=97875000 < 99370304=4301·23104`. Thus this particular phase is **outside** the product-Laplace-capped subclass at that b. No assertion is made about whether it satisfies the cap at other b, or about sufficiency or insufficiency of the combined `(B6) and R_N<=U` restrictions. The candidate's minimization theorem is not changed by this example-scope qualification.

## 4. Scope and required integration

The two literal proof-wording corrections and the optional cap qualification above are additive. No frozen byte, earlier theorem, prior review verdict or parent chronology is altered. In particular this correction did not exist when f250 and f256 reviewed, and their reported findings are not silently erased. Future assessment must bind the earlier fiber convention, THIS correction and the original candidate, with actual ordered reads; any adoption is Main's separate decision.

No new independent mathematical review, parent adoption, formal/kernel proof, human/configured-family verification, novelty or source-equivalence claim follows from this author correction. The general-ε finite nonparallel-prefix optimization remains open, and the local optimizer conditions are not asserted sufficient.
