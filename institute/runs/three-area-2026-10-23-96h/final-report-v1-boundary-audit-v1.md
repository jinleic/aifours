I found 7 MINOR findings and no MAJOR ones. All are documentary label, summary or omission problems; none changes an adopted scientific result.

**What checked out:**
- **Section 11 preserved:** Section 11 (report lines 121–343) matches owner-results v4 lines 9–231 line for line, at a constant +112 offset. I compared raw reads and grepped distinctive tokens. I did not recompute hashes, because the contract allows read/grep/glob only.
- **Header excluded:** the v4 header (lines 1–8, including "10:03:10" and "Pre-cutoff draft") does not appear in the report.
- **v266 corrections present:** all 61 v266 "after" texts appear verbatim, except the physics-2 target, which v4 later changed.
- **Assembly:** no `@@` tokens remain. Frame v6 Sections 1–10 match the report outside the eight tokens.
- **Section 12 table:** all 18 paths, hash prefixes, line counts and prewrite clocks match the status census. The read wording matches the complete-read receipt.
- **NL242 floors:** NL242 L>=18 is kept as an UNREVIEWED author claim with "parent floors unchanged". The adopted rank-six L>=8 floors in Section 11 stand.
- **Metadata-only items:** checkpoint94, the Sun receipt and the RQLS file are described as metadata-only, not as candidates.
- **Assurance level:** strong results are presented as same-harness written support only, with no SOTA, novelty or formal-acceptance claims.

**Findings**

1. MINOR — line 82 and the Section 12 info-6 row (line 354): the NL242 park/checkpoint display is dropped.
   - **Excerpt (line 82):** "The later final-wake cadence, memory-order qualification, Semigroup correction and NL242 administrative read-order finding are disposed in [v268](…)."
   - **Excerpt (line 354):** "New proof-precision clarification and post-cutoff administrative read-order deviation disclosed; no whole-type or witness result."
   - **Problem:**
     - v268 says the NL242 continuation opened park-v17 and checkpoint082, that their protected status is not established, and directs "Preserve the disclosure". The report never mentions this.
     - Line 354 also calls v268's post-cutoff read-order PROCESS MAJOR a "deviation".
     - v268's NL242 timing note (no exact science-stop instant backdated) is also absent. Section 2 (line 21) says owners' science-stop clocks are qualified in Section 12, but Section 12 does not carry this note.
   - **Evidence:** RUN/post-cutoff-final-status-cadence-and-order-dispositions-v268.json:141, 142, 143. The report's own precedent for the AME displays is at line 76.
   - **Replacement (line 82):** "The later final-wake cadence findings, memory-order qualification, Semigroup correction, NL242 post-cutoff administrative read-order PROCESS MAJOR and NL242 continuation disclosures are disposed in [v268](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/post-cutoff-final-status-cadence-and-order-dispositions-v268.json): before the later no-old-checkpoint direction, that continuation opened park-v17 and checkpoint082, whose exact protected status is not established (preserved, not reopened); its reported 10:59:43 last candidate and 11:01:15/11:03:28 checkpoints do not backdate an exact science-stop instant. No held proof or selected value was recovered for those decisions."
   - **Replacement (line 354, last cell):** "Continuation claims (3,112) L>=18 and (3,144) L>=12 at the entire UNREVIEWED author chain; parent floors unchanged. New proof-precision clarification (not independent review), one post-cutoff administrative read-order PROCESS MAJOR and an earlier park-v17/checkpoint082 display with protected status not established disclosed; no whole-type or witness result."

2. MINOR — line 190, fixed at line 119: a stale "this draft" label.
   - **Excerpt (line 190):** "After this draft, the owner reported stopping at 09:46:22 despite permitted work remaining; … Later actual final status must supersede this frontier explicitly."
   - **Problem:**
     - "This draft" was written for owner-results draft v2. v3 was created at 10:03:10 and v4 was written before a 10:36:45 observation, so in the final report the phrase points to neither v4 nor the report itself.
     - The forward-looking "must supersede" line is never linked to Section 12.
     - Section 11 is frozen v4 bytes, so the fix belongs in line 119.
   - **Evidence:** v266.json:3, 214, 215; report-owner-results-draft-v4-header-clock-erratum-v1.json:9.
   - **Replacement (line 119):** "Owner sections below are the bytes of the scope-corrected owner results v4 (`3c275ff5ade6af657d18ba47abe931dfbf5b77dff5cd3b5f0a4585545df0849c`) from its Information science heading onward, which reflect parent dispositions and safe owner status records before the cutoff. Their draft-relative wording is as-of: in info-6, “After this draft” means after owner-results draft v2 (`4636d788b2956b59a0bdf8184b30d66798ee2820652a3929a13e6488c4b5f748`), not after v4 or this report, and the later final status it calls for is the Section 12 info-6 row. Post-cutoff owner statements are in Section 12 and are owner claims unless a parent record adopts them."

3. MINOR — line 356: the math-2 row omits its new cadence PROCESS MAJOR.
   - **Excerpt:** "No new Olson result; v261 concerns privacy only. Actual-word bridge and all-finite-group target open."
   - **Problem:** v268 records a new cadence PROCESS MAJOR for MathOlson-2-2 (09:22:20 to 11:06:12, 1h43m52s). Every other owner with such a finding has it noted in its row (lines 349–353, 355, 357–358, 361–364, 366). Only math-2 omits it.
   - **Evidence:** v268.json:58–62.
   - **Replacement (last cell):** "No new Olson result; v261 concerns privacy only. Actual-word bridge and all-finite-group target open. New cadence interval."

4. MINOR — line 95: Section 8 does not disclose edits made after the reviews.
   - **Excerpt:** "A fourth verifier checked Sections 1–10 of the frame ([review](…)); its ten findings are applied per [v267](…). These are documentary checks, not new proof reviews."
   - **Problem:**
     - The verifiers checked owner-results v2 and frame v2. Main alone later changed three original-target lines in v4 (math-1, math-3, physics-2).
     - For physics-2, this replaced v266's applied wording.
     - Main also revised the frame through v4–v6. None of these edits was re-verified, and the report does not say so.
     - This is undisclosed change to original targets, which is one of the review's focus items.
   - **Evidence:**
     - final-report-assembly-v1.json:38, 55, 60, 65, 70.
     - Header erratum:9 ("Main later changed only three original-target lines for v4").
     - report-frame-v2-review-dispositions-v267.json:5–8.
     - v266.json:401 compared with report line 281.
   - **Replacement:** "A fourth verifier checked Sections 1–10 of frame v2 ([review](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/report-frame-v2-review-v1.md)); its ten findings are applied per [v267](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/report-frame-v2-review-dispositions-v267.json). Main alone later revised the frame through v6 and changed the math-1, math-3 and physics-2 original-target lines in owner results v4; those post-review edits were not re-verified by these verifiers. These are documentary checks, not new proof reviews."

5. MINOR — line 9: the info-1 headline drops LAW642's input cut.
   - **Excerpt:** "For every finite `epsilon>0`, the registered query-output-independent additive pure-DP problem, over all Borel noise laws and every shift in the full closed `l1` diamond, has a unique squared-Euclidean optimal law with characterized value and optimizer"
   - **Problem:** Section 11 adopts LAW642 only "at named standard analysis inputs". The headline states it unconditionally, while the physics-4 headline (line 10) keeps its input cut.
   - **Evidence:** report line 127; v266.json:44–46.
   - **Replacement (first sentence):** "For every finite `epsilon>0`, at LAW642's named standard analysis inputs, the registered query-output-independent additive pure-DP problem, over all Borel noise laws and every shift in the full closed `l1` diamond, has a unique squared-Euclidean optimal law with characterized value and optimizer ([LAW642 adoption](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/privacy-all-law-self-contained-parent-v1.md)); numerical roots are not evaluated."

6. MINOR — line 365: the RQLS cadence MAJOR is understated.
   - **Excerpt:** "One later status file identified only by metadata; metadata-derived cadence interval qualified."
   - **Problem:** v268 keeps the owner-reported cadence MAJOR and qualifies only its metadata-derived duration. As worded, the row reads like the Shor and Sun rows, where no new interval is asserted.
   - **Evidence:** v268.json:134–136.
   - **Replacement (last cell):** "No 100-ray resolvable witness or unrestricted no-go. One later status file identified only by metadata; owner-reported new cadence MAJOR preserved, its 1h40m05 metadata-derived duration qualified."

7. MINOR — line 368: the memory-order item is called a "finding".
   - **Excerpt:** "The additional cadence, memory-order and NL242 administrative findings are dispositioned in [v268](…)."
   - **Problem:** v268 classifies the memory-order item as an instruction-priority qualification, not a READ-ORDER MAJOR. Line 82 already calls it a "qualification", so line 368 contradicts it.
   - **Evidence:** v268.json:145–150.
   - **Replacement:** "The additional cadence findings, the runtime memory-order qualification (not a READ-ORDER MAJOR) and the NL242 administrative findings are dispositioned in [v268](/Users/jinleic/repos/aifours/institute/runs/three-area-2026-10-23-96h/post-cutoff-final-status-cadence-and-order-dispositions-v268.json)."

**UNVERIFIABLE**

1. **The three v4 target lines:** whether lines 197, 221 and 281 match contract-v2 and roster-v3, which are not on the allowlist.
   - Line 221 (math-3) states no explicit prove-or-refute completion alternative.
   - Line 197's (math-1) "especially the residual six-versus-seven band" has no explicit status in line 206 or Section 3.
2. **NL242 notation:** whether "(3,112)/(3,144)" in Section 12 are the "rank6 weight112/144" of Section 11. v268:140 uses only the Section 12 notation.
3. **Counts and clocks in the assembled text:**
   - 102 open obligations (line 65).
   - 170 carried deviation records, 8 of them added (line 80).
   - 86 ledger rows (line 110); the assembly record shows only the 205 rechecked hashes.
   - 450 parent-record files (line 111).
   - 46 arXiv IDs and the 11:11:08/11:11:09 bracket (line 88).
   - The 10:35:40, 11:05:41 and 11:21:04 observations (lines 20–22).
   - The dispatch receipt, the HOLD v2 time, the October 23 replacement dates and the N4 details.
4. **Line 113's list of records outside the authority census:** I cannot check its completeness. The creation times of v4 (around 10:36), frame v5, the arXiv pin and the science-cutoff receipt, relative to the census snapshot, are not available.
5. **Owner-only facts in Section 12:** facts not corroborated by the census or v268, such as "v261 concerns privacy only", "RM-S015" and "No new file before final". The status bodies are not on the allowlist.
6. **Section 11 science:** scientific content beyond the lines v266 dispositioned. No parent bodies were opened.
