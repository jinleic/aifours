`RUN` below means `/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h`.

## Findings

1. **MAJOR — frame line 9: privacy model and composition scope**

   **Current excerpt:** “the registered planar additive pure-DP squared-Euclidean problem over all Borel laws … Later gates add … `V<=2V1/3` with equality exactly when `epsilon<=epsilon_t`”

   **Problem:** The adopted model requires **query-output-independent additive noise**. The mixed-cost conclusion is a conditional composition at a named union; the frame neither identifies that union nor defines `V1`. The v253 gate also retains named unreconstructed cuts.

   **Evidence:** `RUN/privacy-all-law-self-contained-parent-v1.md:14-16,34-38`; `RUN/privacy-v253-MDA-mixed-cost-composition-entire-parent-v1.md:5-18,42-52`; `RUN/report-owner-results-draft-v3.md:15,18-21`.

   **Replacement bullet:**
   > - **info-1.** For every finite `epsilon>0`, the registered query-output-independent additive pure-DP problem, over all Borel noise laws and every shift in the full closed `l1` diamond, has a unique squared-Euclidean optimal law with characterized value and optimizer ([LAW642 adoption](privacy-all-law-self-contained-parent-v1.md)); numerical roots are not evaluated. The separate [v241 gate](privacy-v241-separated-threshold-and-norm-gap-entire-parent-v1.md) supplies the exact diamond/rounded threshold `epsilon_t` at `LAW642 + NORM148`. At the conditional union `LAW642 + MDA per-cost(K=D, cost r²) + NORM148 + separated v241`, [v253](privacy-v253-MDA-mixed-cost-composition-entire-parent-v1.md) supports `V<=2V1/3`, where `V1` is the all-law squared-`l1` optimum, with equality exactly when `epsilon<=epsilon_t`. Its named unreconstructed cuts remain; external source equivalence and priority are unestablished.

2. **MAJOR — frame line 32: omitted PH upper-eight input**

   **Current excerpt:** `OPEN; at b²/d²=8/9 the minimum is in {7,8}`

   **Problem:** The `{7,8}` statement depends on the separately retained old upper-eight input. The table removes that trust boundary even though the draft’s original-problem line retains it.

   **Evidence:** `RUN/PH7-entire-rational-seven-ninths-band-parent-v1.md:7-11`; `RUN/report-owner-results-draft-v3.md:93-94`.

   **Replacement row:**
   > | math-1 | MathResearch96h-2 | OPEN; at `b²/d²=8/9`, the minimum is in `{7,8}` at the separately retained old upper-eight input | [PH7-entire-rational-seven-ninths-band-parent-v1](PH7-entire-rational-seven-ninths-band-parent-v1.md) |

3. **MAJOR — frame lines 12 and 51: blanket serial-review and replay claims**

   **Current excerpts:** “Every adoption is a same-harness, serial, nonblind written review” and “reviewers were existing owners in the same harness, serial and nonblind … no executable certificate was replayed under the HOLD”.

   **Problem:** Serial prior exposure is not universal: a linked Werner adoption expressly records fresh-body exposure, and v11 corrects another falsely attributed serial history. Separately, the records disclose unadmitted owner computations and parent certificate arithmetic under HOLD; they do not establish the blanket absence of every executable replay.

   **Evidence:** `RUN/werner-output-c-forcing-v3-parent-v1.md:3-5`; `RUN/parent-evidence-erratum-v11.md:24-28`; `RUN/parent-evidence-erratum-v7.md:5-17`.

   **Replacement line 12:**
   > - **Verification ceiling.** Adoptions are scoped same-harness written reviews and parent checks at the stated inputs; each record retains its actual review count and fresh or serial exposure history. None is configured-family, cross-vendor, human, formal/kernel, executable-certificate, novelty or priority acceptance.

   **Replacement line 51:**
   > - **Common limits:** reviewers were existing owners in the same harness; contact and exposure histories are stated at each gate and are not evidence of blind or independent-model-family review. Classical imports are named, not re-proved; no Lean or other kernel acceptance is claimed. Disclosed unadmitted computations carry no executable-verification or finite-certificate credit. Finite evidence is not a symbolic proof; novelty and priority remain UNCLEAR for every result.

4. **MAJOR — frame line 50: nonadoption conflated with lack of review**

   **Current excerpt:** “**UNREVIEWED:** an owner candidate with no parent adoption.”

   **Problem:** A candidate may have actual review returns while still awaiting complete parent reads or adoption. The definition collapses those distinct states.

   **Evidence:** `RUN/parent-live-service-gap-and-current-recovery-v179.json:10-11`; `RUN/reviewer-PPT-spotchecks-and-Sun-Werner-wait-findings-v230.json:30-32`.

   **Replacement bullet:**
   > - **UNREVIEWED:** no applicable completed review has been established at the stated scope. A candidate with review returns but no parent disposition remains **NOT ADOPTED**, not necessarily unreviewed. **HELD:** not usable as a premise pending its specified source/process decision. **ZERO:** the specified quarantined material and its consuming guidance receive no verification, method, source-selection or confidence credit.

5. **MAJOR — frame line 64: omitted unadmitted owner computations and overstatement of the service-gap observation**

   **Current excerpts:** “unadmitted parent scientific evaluations with ZERO credit, recorded in v6 and v9” and “no numbered parent checkpoint … and no parent control record … until a returned clock”.

   **Problem:** v7 also records a **parent authorization error** and actual unadmitted **owner** computations, in addition to parent programs. The v179 record says no intervening checkpoint/control service was **established by that tool record**; it does not establish categorical absence.

   **Evidence:** `RUN/parent-evidence-erratum-v7.md:5-17`; `RUN/parent-live-service-gap-and-current-recovery-v179.json:3-10`.

   **Replacement bullet:**
   > - **Parent:** Evidence errata remain mandatory. Unadmitted parent diagnostics are recorded in [v6](parent-evidence-erratum-v6.md), [v7](parent-evidence-erratum-v7.md) and [v9](parent-evidence-erratum-v9.md); v7 also records the parent’s erroneous HOLD exception and actual owner computations under it, which have no executable-verification, finite-certificate or retroactive-admission credit. The later [metadata-only cell characterization](parent-eval-cell-0843-characterization-v1.md) is not such a diagnostic, and v11 qualifies its broader clock claim. Other permanent findings include the [v101 missing frozen scope](parent-v101-missing-frozen-scope-finding-v1.md); no intervening numbered checkpoint or control service established by the parent tool record between the anchors in [v179](parent-live-service-gap-and-current-recovery-v179.json), plus the separate cadence findings in [checkpoint 068](checkpoints/068-resumed-integration-and-parent-cadence-finding-v1.json) and [checkpoint 091](checkpoints/091-recovered-returns-stops-and-parent-cadence-finding-v1.json); a [parallel source read](parent-v212-PH-parallel-source-read-finding-v221.json); a [misattributed release note](Sun-v233A-envelope-first-order-and-parent-release-misattribution-v234.json); a [pre-ACK topic disclosure](v241-parent-preACK-privacy-topic-disclosure-qualified-release-v242.json); the unsafe administrative discovery instruction corrected prospectively by the [safety addendum](report-interim-census-request-v255-addendum-1.json), with exposure records [v257](Werner-v255-administrative-held-metadata-exposure-v257.json), [v258](Depol-v255-overlay-order-and-withdrawn-context-disclosure-v258.json), [v259](v255-Rminus-privacy-held-status-display-and-safe-reporting-v259.json), [v260](v255-PH-MOQLS-AME-administrative-exposure-record-v260.json) and [its addendum](v255-PH-MOQLS-AME-administrative-exposure-record-v260-addendum-1.json); and the [over-broad report-audit scope](report-physics-audit-withdrawn-context-exposure-qualification-v264.json).

6. **MAJOR — frame line 65: ZERO applied indiscriminately to process findings**

   **Current excerpt:** “PPT reviewer spot checks and Sun/Werner wait gaps … All have ZERO credit; affected verdicts stay HELD where stated.”

   **Problem:** v230 classifies the Sun and Werner gaps as permanent PROCESS MAJORs; ZERO applies to the selected checks and specified consuming guidance, not to the fact of the gaps. N4 also has persisted fixed controls, although its target outcome is UNKNOWN.

   **Evidence:** `RUN/reviewer-PPT-spotchecks-and-Sun-Werner-wait-findings-v230.json:30-32`; `RUN/physics-ppt44-normalized-n4-001-execution-receipt-v2.json:25-30,47-55`; `RUN/Kac-v237-selected-type-arithmetic-zero-and-stop-v246.json:11-14`.

   **Replacement bullet:**
   > - **Execution and selected checks:** The N4 overrun is recorded in Section 1; its fixed controls persisted, but its target outcome remains UNKNOWN. The specified owner/reviewer selected checks and their consumers are ZERO ([v227](privacy-v214-selected-input-checks-process-quarantine-v227.json), [pin addendum](privacy-v214-selected-input-checks-process-quarantine-v227-pin-addendum-1.json), [v230](reviewer-PPT-spotchecks-and-Sun-Werner-wait-findings-v230.json)), as are the selected-type episode and consumers in [v246](Kac-v237-selected-type-arithmetic-zero-and-stop-v246.json). Affected verdicts remain HELD where stated. The separate Sun/Werner wait gaps in v230 remain PROCESS MAJORs.

7. **MAJOR — frame line 67: potential-consumer quarantine omitted**

   **Current excerpt:** “exposed held material and every consumer stay ZERO.”

   **Problem:** v260 additionally quarantines **every possible consumer** of the AME displays while the protected status of individual records remains unestablished. The frame’s wording covers confirmed exposure but omits that precaution, and does not distinguish unclassified metadata displays from confirmed held-content events.

   **Evidence:** `RUN/v255-PH-MOQLS-AME-administrative-exposure-record-v260.json:25-48`; `RUN/report-interim-cadence-and-qualified-history-disclosures-v262.json:49-60`.

   **Replacement bullet:**
   > - **Read order and exposure:** Mandatory-overlay read-order findings (v216, [v234](Sun-v233A-envelope-first-order-and-parent-release-misattribution-v234.json), v258 and the v260 addendum) and exposure records ([v256](v253-Olson-prior-metadata-exposure-qualified-continuation-v256.json), v257–v260 and v264) remain. Exposed held or withdrawn material and its consuming guidance stay ZERO. For the v260 AME displays, protected status remains unestablished per record and every possible consumer remains quarantined pending admissible clarification. The v262 Semigroup and Tuscan legacy displays retain their bounded qualifications without an invented protected-content finding.

8. **MINOR — frame line 68: wrong category for v240 addendum 2**

   **Current excerpt:** “**Documentary:** count, pin and receipt corrections … [v240 addendum 2]”.

   **Problem:** Addendum 2 withdraws an unsupported **review-capacity timing-impossibility forecast**; it is not a count, pin or receipt correction. It retains the no-new-preview-wave decision.

   **Evidence:** `RUN/preview-v33-plus-review-capacity-decision-v240-addendum-2.json:3-7`.

   **Replacement bullet:**
   > - **Documentary:** Count and pin/receipt corrections remain ([v228](Shor-v224A-and-v212-receipt-length-qualification-v228.json), [v230 count addendum](reviewer-PPT-spotchecks-and-Sun-Werner-wait-findings-v230-count-addendum-1.json), [v240 addendum 1](preview-v33-plus-review-capacity-decision-v240-addendum-1.json)). [v240 addendum 2](preview-v33-plus-review-capacity-decision-v240-addendum-2.json) separately withdraws the unsupported review-completion impossibility forecast while retaining the no-new-preview-wave decision.

9. **MINOR — frame line 7: expanded ownership appears to span the whole original window**

   **Current excerpt:** “Eighteen existing owners, six per domain, each held one problem slot under the owner-authorized contract v2 for October 23, 12:35:38 PDT to October 27, 12:35:38 PDT”.

   **Problem:** The 96-hour window began before the 18-slot expansion: three owners were retained and 15 additional workers were subsequently launched. The sentence can imply all 18 held slots from the original start.

   **Evidence:** `RUN/contract-v2-eighteen-slots.json:3-15`; `RUN/eighteen-slot-launch-receipt-v1.json:3,9-17`; `RUN/README.md:3-8`.

   **Replacement bullet:**
   > - **Round shape.** The original round window was October 23, 12:35:38 PDT to October 27, 12:35:38 PDT. The later owner-authorized [contract v2](contract-v2-eighteen-slots.json) expansion retained three owners and launched 15 additional workers, establishing 18 slots, six per domain ([launch receipt](eighteen-slot-launch-receipt-v1.json), [execution bindings](eighteen-slot-execution-bindings-v1.json)). Slots info-1 and info-4 received same-owner replacement targets on October 23 under the replacement clause ([info-1](info-1-replacement-v1.json), [its continuation](info-1-continuation-v1.json), [info-4](info-4-replacement-v1.json)). [Roster v3](eighteen-problem-roster-v3.md) is the current target list.

10. **MINOR — frame line 13: earlier HOLD omitted**

    **Current excerpt:** “From October 24, 03:21:46 PDT the scientific-admission HOLD v2 allowed written/source/metadata work only”.

    **Problem:** This correctly dates HOLD **v2**, but omits the earlier N4-overrun scientific-launch HOLD on October 23. The later decision continued the restriction after the old process group was observed absent.

    **Evidence:** `RUN/parent-evidence-erratum-v3.md:17-27`; `RUN/n4-overrun-quarantine-v1.json:3,16-21`; `RUN/scientific-admission-hold-v2.json:3-16`.

    **Replacement bullet:**
    > - **Scientific execution.** By the October 23, 16:35:04 PDT observation, the N4 overrun had placed new scientific admissions on HOLD. The October 24, 03:21:46 PDT [scientific-admission HOLD v2](scientific-admission-hold-v2.json) continued the global restriction after the old identity was observed absent, allowing written/source/metadata work only; no new scientific GO is recorded in the cited pre-cutoff records. N4 remains UNKNOWN_INTERRUPTED_OR_INCOMPLETE, with a reported resource overrun and historical child exit unestablished ([receipt v2](physics-ppt44-normalized-n4-001-execution-receipt-v2.json), [overrun quarantine](n4-overrun-quarantine-v1.json)). The privacy owner’s 214-LF auxiliary body remains UNADMITTED under an explicit parent STOP ([finding](privacy-auxiliary-prebinding-owner-finding-v1.md), [checkpoint 059](checkpoints/059-full49-union-and-next-original-gates-v1.json)).

## UNVERIFIABLE

- **UNVERIFIABLE_WITHOUT_PROTECTED_SOURCE:** The underlying correctness and independent provenance of owner proof bodies, candidate packets, review bodies, held/withdrawn material, and any claimed cognitive non-use. This review checked parent records and the permitted draft only; it did not reconstruct those sources.
- **Requires post-cutoff evidence:** The table’s “at cutoff” statuses and line 56’s assertion that every eventual queued review was not performed before cutoff cannot yet be established from the cited pre-cutoff records. The intentional slots are not findings.
- The 18 table rows agree with draft v3’s `Original problem` lines on OPEN versus WRITTEN_SUPPORTED status at the draft snapshot, subject to finding 2’s omitted PH input.
