# f883 review v1 — v36 physics-6 AME50 count / 4444 frontier documentary audit

- Reviewer: DocF883AME36. Clock observed via /bin/date immediately before this write: 2026-10-31T03:22:56Z (Fri Oct 30 20:22:56 PDT 2026). This is an upper bound on when the reads finished, not a start time.
- Pre-body ACK: [prebody-ack-v1.md](prebody-ack-v1.md), written at 03:03:52Z and sent as a direct message to Main before any packet body was accessed. Main's IRC ruling on that ACK was received; see §9.
- Role: DOCUMENTARY ONLY. This is a literal comparison of frozen v35 (S3, with errata S1/S2) and v36 (S4) against the complete source bodies S5–S20 in literal parts 01–04. It does not review proofs. It does not audit underlying proof correctness, and it does not accept anything about global report, science, family, human, kernel, novelty or priority status. The parent's disposition is a separate step.
- Scope (manifest `research`): v36 physics-6 and the related opening, current-evidence and status text. That covers:
  - exact t23/24/25/27/28 exclusions;
  - the CONDITIONAL global t≤28 import leaving t22/t26 only, with t26 restricted to 4444;
  - f860's entire-4444 obstruction being UNADOPTED, and the absence of any N50 exclusion, minimum51 or witness claim;
  - the fixed actual support phase criterion, integral rather than mod 2;
  - the canonical-12 component, IF PRESENT;
  - the provenance of the global bound and of the f127/f182 caveats;
  - F842's local completeness versus F812 PARTIAL and F815's zero examined P candidates;
  - incorporation of the v35 errata, and as-of / no-backdating behaviour.

## 1. Bindings (live shasum after the ACK; every value equals the manifest, freeze-receipt, binding and metadata pins)

- Parts:
  - 01: b46772f7…e179 (70 LF / 72366 B)
  - 02: 1a9f9994…402e (366 / 86441)
  - 03: 8140d711…c156 (478 / 62983)
  - 04: 73ee96f4…daa (2310 / 75538)
- Sources:
  - S1 98f2a870…266, S2 792c5ccf…8709, S3 81c0a8d5…b43, S4 8953aeba…392
  - S5 75cfcfe1…668, S6 043d4be3…d96, S7 c411a2b7…721, S8 70662b48…187
  - S9 f457f943…85c, S10 abada4c6…1e6, S11 ccbadbf9…0f1, S12 4c201b80…bb6
  - S13 44a750bb…619, S14 67e216de…321, S15 85878560…cf9, S16 876bf145…057
  - S17 fb12dd35…931, S18 0a729751…e89, S19 cd290a24…0e3, S20 1f3b8a1b…f39
- Administrative files:
  - manifest 104ace6a…e48
  - freeze receipt 45a1d4b1…aa4
  - binding 6372ade9…bf7
  - metadata 208b773e…31e
  - actual dispatch receipt c8e49650…2bc. It names agent DocF883AME36, was observed at 02:59:56.263Z and has no prior pin.
- Controls: all 23 listed status-only controls match their pins. They were used for status and permissions only. All held episodes and ALL consumers remain NONINPUT. No held payload was sought or read.

## 2. Complete read account (every window `:raw`, ≤20 LF and <30000 B, except the one window disclosed as P1)

- Administrative files, all read before the ACK:
  - manifest: 438/438 LF in 22 windows.
  - freeze receipt: 399/399 in 20 windows.
  - final binding: 301/301 in 16 windows. The last window, 281–301, was **21 LF** (P1).
  - metadata: 412/412 in 21 windows.
  - actual dispatch receipt: 90/90 in 5 windows.
- Controls: all 23 were read completely before the ACK (LF): 14, 23, 28, 49, 23, 16, 20, 22, 22, 23, 23, 24, 11, 11, 11, 11, 11, 8, 9, 11, 11, 28, 9.
- The parts were read serially (part-01 ending, then part-02, then part-03, then part-04) and each was read completely through its ending:
  - **Part-01, 70/70 LF, 28 windows:** 1-7, 8-9, 10-11, 12-13, 14-15, 16-20, 21-22, 23-24, 25-29, 30, 31-37, 38, 39-40, 41-42, 43-44, 45-46, 47-48, 49-50, 51-52, 53-54, 55-56, 57-58, 59-60, 61-62, 63-66, 67, 68-69, 70. LF70 is the empty ending.
  - **Part-02, 366/366, 42 windows.** All S4 report lines were in 1–2 LF windows: 6-7, 8, 9-10, …, 44, 45, 46-47. LF1-5 were packet/S4 headers. S5–S8 were read in 20-LF windows from 48-67 through 350-366. LF366 is the empty ending.
  - **Part-03, 478/478, 48 windows.** S9/S10 JSON was read in 20-LF windows. Dispositions S11–S16 were read in 2–8 LF windows. LF478 is the empty ending.
  - **Part-04, 2310/2310, 116 windows:** 1-20 … 2281-2300, then 2301-2310. LF2310 is the empty ending.
- Clipping check: no window showed an elision or truncation marker. The four longest report lines are part-01 LF67 (24040 B), part-01 LF69 (6676 B), part-02 LF45 (24040 B) and part-02 LF47 (6793 B). Each was cross-checked against the displayed text using mechanical token counts:
  - part-01 LF67: `](/Users` = 73, `NONINPUT` = 7, `PROCESS MAJOR` = 12
  - part-01 LF69: links = 23
  - part-02 LF45: 73 / 7 / 12
  - part-02 LF47: links = 24

  Every count matched the displayed text, so no fragment display was needed.

## 3. Mechanical v35→v36 delta

`diff` of the hash-verified S3/S4 bodies changes exactly lines **1, 3, 12, 16, 19, 24, 25, 28, 32, 42**. That equals S8 `changed_logical_lines` (part-02 LF242–253). All other lines are byte-equal, which confirms S8 `"unchanged_other_lines_byte_equal": true` (LF254). Two consequences:

- Lines 34, 38 and 40 are byte-identical to v35. These are the ACK, availability and process paragraphs.
- The unchanged rows (info-1/3/4/5, math-1/2/4/5/6, physics-1/4/5) are **inherited, NOT newly certified**. Changed rows outside AME (info-2, info-6, math-3, physics-2, physics-3) were checked only for literal incorporation of the errata (§4.5).

## 4. Scoped comparison

### 4.1 Opening (v36 part-02 LF8 = S4|3)

**Accepted.**

- "records0F/1M/4m at its exact frozen scopes plus a separate report-window process finding" matches S5 `counts` (LF75) and S5 `process` "F854 ONE report-window PROCESS MINOR" (LF91).
- "retains0F/1M/4m new unique findings, earlier stale-footer and separate chronology issues not recounted" matches S6 `unique_new` (LF158) and S7 (LF209).
- "Newly adopted scopes below postdate those snapshots; no backdating."

Clock order:

| Event | UTC |
|---|---|
| v36 composition | 02:58:33.044Z |
| S1 erratum-1 | 02:47:55Z |
| S6 v33/v34 outcome | 02:48:26Z |
| S7 data-access clarification | 02:48:34Z |
| S2 erratum-2 | 02:51:22Z |
| S5 v35 outcome | 02:51:22Z |
| S12 adoption | 02:56:26.828Z |
| S13 and S14 adoptions | 02:47:41.780Z and 02:47:41.781Z |

Everything above was recorded before the v36 composition. S9 (02:58:47.672Z) cites the v36 hash, and v36 does not cite S9. The dispatch (02:59:56Z) postdates v36. v36 says its checks are "NOTyetbeen dispatched or passed" (LF37, LF47), which matches S8 `"audit": "V36 NOT YET DISPATCHED OR PASSED"` (LF363).

### 4.2 physics-6 row (v36 part-02 LF33 = S4|28; v35 part-01 LF55 = S3|28)

**Accepted at documentary scope, unless a minor finding is noted.**

- **Exact t23/t24:** "Exact support50 branches t23,t24,t25,t27 ANDt28 are excluded for arbitrarycomplexentries of ONEtensor/basis". The t23/t24 part matches S12|3 (part-03 LF353): "the exact branches **t23 and t24 are impossible**, independently of any global t-bound, noOLS result, alphabet or phase ansatz".
- **t28:** matches S13|3 (LF372): "No normalized complex AME(4,6) state in ANY fixed local orthonormal product basis has exactly50 nonzero coefficients and exactly28 entries of U=6psi of modulus1 … This exact t28 exclusion requires neither noOLS nor the global t<=28 import".
  - v35's "A prospective f827 SAME-tensor t28 whole-branch proof … UNADOPTED" was correct as of 02:37:09Z. S13 was recorded at 02:47:41Z. No backdating.
- **t25/t27:** supported only through S12|11 (LF361), which links the "separate [t25/t27 exact exclusions]", and through S9|114 (LF119). The disposition body itself is not in the packet, so this item is inherited and not newly certified (I1).
- **t26 → 4444:** "t26has ONLY E-alphabet4444" matches S14|3 (LF395): "EACH of the four residual E alphabets has size4. Equivalently its sorted actual E-alphabet profile is **4444** … This is not a complete t26/N50 exclusion". v36 claims no t26 exclusion.
- **Conditional global bound:** "At the separately retained globalt<=28/noOLS/f113/prior-count import, support50 can therefore only occur at t22 or t26/4444." This matches:
  - S12|3: "If the separately named global t<=28/noOLS/f113/prior-count import applies to this SAME tensor, only **t22 or t26** can remain";
  - S12|11: "The retained [global upper-count/source/provenance import](S11), not that elementary inequality, gives t<=28 conditionally" and "Exact t25/t27/t28 and q5 proofs do not themselves require noOLS; the exhaustive N50 union additionally does";
  - S11|13 (LF330): "classical no-OLS(6), f113 and prior t≤30/count provenance".

  The label for the global import is precise. See m2 for the separate attribution of the f127/f182 caveats.
- **T22 phase criterion:** "T22 fixedactualP22/E28support has commonphases IFF every INTEGRAL leftkerneldependency of21cut-indexedsquares has evensum". This matches:
  - S15|3 (LF421): "**iff every integral y∈ker_Z(Aᵀ) has even coordinate sum**";
  - S15|9 (LF427): "A mod2 odd dependency alone is not necessarily an integral obstruction";
  - S12|13 (LF363).

  Integral rather than mod 2 is correctly stated. v36 does not carry the iff over to t26, which matches S14|17 (LF409): "necessary and sufficient for its two-term phase subsystem only". Residual o1 applies.
- **Canonical-12 and connectivity:** "every12wordcomponent IF PRESENT is canonical2333, with threeprofiles forced connected28". The content matches S16|3 (LF446): "every 12-word residual agreement component is, up to physical party/symbol relabeling, the canonical **2333** gadget … at each global E-alphabet profile **3566, 3666, 4456** … one connected 28-word component". IF PRESENT is implemented. The traceability problem is m3.
- **Gap column, no minimum or witness claim:** "No support50state, wholeN50exclusion, minimum51, exactminimum or51–59attainment" matches:
  - S12|3: "no minimum51 or support50 state";
  - S12|15: "exactminimum/51–59attainment … remain open";
  - S11|9: "There is no 50-term witness, no exact-minimum or 51–59 attainment claim".
- **f860:** "A NEW f860 ENTIRE4444obstruction is UNADOPTED under critical f879–f882 gates" matches:
  - S9|114: "F860proposes ENTIRE4444obstruction, UNADOPTED under f879–882 criticalgates";
  - S9|158, where the f860 candidate appears in `returned_unintegrated_frontiers`;
  - S10|12–19, which records F879–F882 as running at 02:59:08Z.

  The f861 clause is m1.
- **F842:** "F842localcompletegraphs/phases are NOT globalP/Etensorenumeration" matches:
  - S17 (part-04 LF43) `"COMPLETE_LOCAL_NECESSITIES"` and LF42 `"not_claimed": "global P/E enumeration or AME feasibility"`;
  - S17 LF1671 `scope` and S18 LF1716 `"COMPLETE_LOCAL_Q5_Q3_Q4"`;
  - S18 LF1832 `scope`;
  - S13|17 (LF386): "neither enumerates global P/E tensors or establishes an AME witness";
  - S14|22 (LF414): "necessary projections only".

  The S13|17 counts agree literally with the receipt fields: 256 at LF185, 1820 at LF682, 90 at LF696/705/714/724, 12870 at LF732, 10 at LF1627, 2040 at LF1665, the 13 targeted reasons at LF64–76, elapsed time at LF41/LF1714, and 280/610 ms at LF37/LF1710.
- **F812:** "F812order8 remains PARTIAL, its zeroprefixnotabsence" matches:
  - S19 `"exit_code": 2` (LF1861) and `"INCOMPLETE_NODE_CAP"` (LF1863);
  - the S19 qualification "zeroprefixsurvivorsNOTwholeorder8absence" (LF2142);
  - S13|8 (LF377).
- **F815:** "F815 examinedZEROphysicalP, completionNOTENUMERATED" matches S20 `"physical_P_candidates_examined": 0` and `"physical_P_completion": "NOT_ENUMERATED"` (LF2199–2200), S20 `qualification` (LF2308) and S16|28 (LF471).
- **Caveat wording:** "F127manifest-notlocatedINREVIEWDIR/notprovedabsent, F182postexposure/notcleanroom andalternative-directnottransitive caveats retained". The wording matches S11|13 and S12|15. The attribution is m2.

### 4.3 Current evidence (v36 part-02 LF37 = S4|32)

**Accepted:**

- "**382 historical data rows**" matches S8 `data_rows` 382 (LF290) and S9 (part-03 LF31).
- The links for AME t28, AME t26q5/4444 and t23/t24 + conditional t22/t26 resolve to exactly the S13, S14 and S12 paths.
- The F842main and F842companion links resolve to exactly the S17 and S18 paths, and "all local/sample limits retained" holds.
- The UNADOPTED candidate list (F846–F848, F849, F850, F853, F860, F861) equals S9 `returned_unintegrated_frontiers` (LF125–173).
- "V36 changed-scope checks have NOTyetbeen dispatched or passed" is accepted.

The removed v35 disclosure is m4. The info-2 adoption listing is outside scope (X1).

### 4.4 Status (S9/S10)

- S9|114 agrees with v36 except on the f861 wording (m1).
- S10|10 (LF293) withdraws the S9 `active_gates` runtime implication. v36 makes no running-gate claim; it says only "under" and "pending". No v36 consequence.

### 4.5 Incorporation of the v35 errata (literal presence only)

- **S1 (erratum-1):**
  - info-6 now reads "with ORIGINAL Walsh cap28" (LF21).
  - info-2 now reads "j_i=0 if any actual corner determinant vanishes and1 otherwise" (LF17).
  - physics-6 now has "IF PRESENT", ONE fixed actual support, and no claimed P completion: "F815 … completionNOTENUMERATED", "T22 incidence/phasefeasibility remains open" (LF33). Residual o1 applies.
- **S2 (erratum-2):**
  - math-3 now reads "appropriately SIGNED/NORMALIZED" and "initial truncated proc/failedJSON recovery is one retained parent capture MINOR" (LF24).
- **As-of:** S1|9 says "This erratum is prospective". v36 LF47 says "Later scientific adoptions are not backdated into earlier snapshots." No backdating was found.

## 5. Findings: 0 FATAL / 0 MAJOR / 4 MINOR (documentary; all are new events in v36 unless noted)

### m1 — MINOR, status precision: the f861 gate wording

- **v36 LF33:** "A NEW f860 ENTIRE4444obstruction is UNADOPTED under critical f879–f882 gates; f861same-Pcount refinements likewise ungated."
- **v36 LF37:** "F8604444andF861incidence candidates remain UNADOPTED pending separatecriticalgates".
- **S9|114 (part-03 LF119):** "f861Pprofile refinements underf876–878".
- **S9|164 (LF169)** gives the candidate path `f861-ame50-t26-4444-actual-P-incidence-and-phase-frontier-author`. S9|202/212 (LF207/217) name f876 "middle-P-count" and f878 "P-incidence".
- **Problem:**
  - "ungated" can be read as "not under any gate". That contradicts S9 and v36's own LF37.
  - The descriptor drifts: "same-Pcount refinements", then "incidence candidates", then "Pprofile refinements".
  - The f876–f878 gates are never named.
- **Impact:** no adoption is claimed, so there is no consequence for the science.
- **Suggested fix:** "f861 P-count/incidence refinements remain UNADOPTED under f876–f878".

### m2 — MINOR, provenance precision: the interval's imports are no longer named, so the f127/f182 caveats are unattached

- **v35 LF55:** "**AME(4,6): conditional50<=m<=60** for normalized complex states/local orthonormal bases at retained same-tensor lower49/global-count/60-witness inputs."
- **v36 LF33:** "**AME(4,6): conditional50<=m<=60.**" The only import v36 names is "globalt<=28/noOLS/f113/prior-count". The caveats then appear unattached at the end of the gap column.
- **S11|7 (LF324):** "Import EITHER of the two already dispositioned universal same-pair N≥49 chains".
- **S11|13 (LF330):** "Route A directly inherits the historical f127 … Its separate historical manifest was not located in the review directory; absence is not proved. F182's separate implementation followed author-checker exposure and is not clean-room. Route B does not directly import f127 … f127 absence from every transitive input is unestablished".
- **S12|15 (LF365):** "These caveats concern their named prior lower-bound routes and are not misattributed as proof that f127 is an input of the global upper-t theorem."
- **Problem:** v36 drops the lower-49 and 60-witness imports from the interval. A reader can therefore attach the caveats to the global upper-t import, which is the attribution S12|15 explicitly rules out.
- **What is correct:** the provenance of the global bound is stated precisely, and nothing false is asserted.
- **Overlap:** the caveat wording itself is inherited from v35 and is not counted again.
- **Suggested fix:** restore "at retained same-tensor lower49 (Route A/B)/global t≤28/60-witness inputs" and attach the f127/F182/Route-B caveats to the lower-49 routes.

### m3 — MINOR, traceability: the t22 phase and canonical/connectivity links were dropped

- **v35 LF55** linked "[t22 phase](…t22-common-support-phase-integer-kernel-criterion…)" (S15) and "[t22 canonical/connectivity](…t22-canonical-twelve-component-and-three-profile-connectivity…)" (S16).
- **v36 LF33** still asserts "every12wordcomponent IF PRESENT is canonical2333, with threeprofiles forced connected28". It links only S12, S13, S14 and S11. A grep of part-02 finds no S15 or S16 target.
- Only S16|3 (LF446) contains the canonical-2333 / connected-28 statement. None of the v36-linked sources does.
- The phase iff is still traceable through S12|13 (LF363).
- v36 also stops naming the three profiles (3566/3666/4456), which v35 named.
- **Content:** consistent with S16. There is no error in the content.

### m4 — MINOR, disclosure: v35's ACK-transport pointer was removed

- **v35 LF59:** "[ACK-transport observations](…/parent-f826-f832-direct-ack-transport-observations-v1.json) retain seven direct-delivery process MINORs and the parent prompt-clarity MINOR; no backdating."
- **v36 LF37** rewrote that paragraph. Searching part-02 for `direct-ack-transport` finds nothing. v36 LF34 and LF40 are byte-identical to v35 and contain no f826–f832 ACK text.
- The AME-relevant items survive only in linked dispositions:
  - S13|19 (LF388): "F827's local prebody ACK preceded body access but its separate direct delivery was late: ONE ACK-transport PROCESS MINOR retained";
  - S14|22 (LF414): "F826 late direct ACK is ONE transport PROCESS MINOR".
- v36 LF21 keeps the F828/F829 ACK MINORs.
- **Precedent:** S2|5 (part-01 LF23) classed omitting an already-recorded process MINOR from the evidence paragraph as "ONE documentary disclosure MINOR".
- **Possible double count:** the non-AME part (other f828–f832 items and the parent prompt-clarity MINOR) may also be raised by sibling scopes. The parent should deduplicate.

### Residual, not counted

- **o1:** this is the same event already counted as erratum-1's physics-6 MINOR (S1|7, LF12).
  - v36 implements ONE fixed actual support and IF PRESENT.
  - It compresses "satisfying all six projections and the three specified cut graphs" into "fixedactualP22/E28support … 21cut-indexedsquares".
  - S12|13 ("with all6pair partitions and all3seven-K2,2 cuts") and S15|3 state the hypotheses in full.
  - Suggested fix: make the hypotheses explicit in the next successor.

## 6. Inconclusive items and coverage boundaries (no finding)

- **I1:** the t25/t27 exclusion disposition body is not in the packet. Support is S12|11, S9|114 and continuity with v35 LF55.
- **I2:** S14|15 (LF407) says "same-P counting rules out3444". The packet gives no further written argument for that step. The F842 receipts are explicitly local necessities and are not cited for it.
  - Literally, S17's moment stage lists a non-empty `"3444"` entry under `"26"` (part-04 LF273–280), while S14|15's 4444 moment triples equal S17's `"4444"` entries.
  - Whether "same-P counting" goes beyond that listing cannot be determined from the packet.
  - No contradiction is established. The underlying proofs (F826/F841/F856/F857) are not in the packet and were not audited.
- **I3:** the packet has no dispatch clocks for f876–f882 relative to v36 composition. Only S9 (after v36) and S10 exist.
- **I4:** S8's navigation claims (173 hrefs, `missing` []) and render claims are parent observations. Link targets were not opened and nothing was rendered.
- **I5:** S12's candidates (the parent candidate, F874 and F875) and S11's route bodies are not in the packet.

## 7. Out-of-scope observations (not counted; for routing)

- **X1, info-2:**
  - S9|39 (part-03 LF44) lists `info-2-actual-septic-five-node-endpoints-and-six-node-mixed-edge-gap-parent-v1.md` in `new_adopted`. It is absent from v36 LF37's "Since v35 … adopted" list and from S8 `new_sources`.
  - v36 LF17 states "Five-node ANY absentendpoint is independently excluded" without a link to it.
  - v35 LF39 had said "F816 five-node endpoint and F817 mixed-edge refinements remain UNADOPTED".
- **X2, history:** v36 LF47 drops v35 LF69's "V30" and the v31/v32 outcome link.

## 8. Accepted scope

At documentary level, the following are accepted:

- t23/t24/t28 are exact; t25/t27 is inherited.
- t26 has 4444 only.
- t22/t26-only is conditional on the named global import.
- f860 remains UNADOPTED.
- There is no N50, minimum-51, exact-minimum, 51–59 or witness claim.
- The t22 criterion is integral, on a fixed actual support, and is not carried over to t26.
- The canonical-12 IF PRESENT content is accepted (traceability is m3).
- F842 is local-complete and not global; F812 is PARTIAL; F815 examined zero P.
- The errata are incorporated, and there is no backdating.

Everything above is subject to m1–m4, o1, I1–I5 and the assurance limits in §10.

## 9. Process disclosures

- **P1:** the binding window 281–301 was 21 LF on an administrative file. Main's ruling: ONE reviewer administrative-window PROCESS MINOR. No packet-body fault, no automatic hold, no backdated compliance.
- **P2:** self-reported. Five part-01 windows were longer than 2 LF and contained short report or erratum lines: 1-7, 16-20, 25-29, 31-37 and 63-66. The longest such line was 905 B and every window was under 30000 B. Every line over 1000 B and both long paragraphs were read in 1–2 LF windows. Following F854 (S5|40), I propose ONE reviewer report-window PROCESS MINOR, for the parent to dispose.
- **P3:** metadata and text utilities only:
  - before the ACK, `wc -l -c` (ruled permitted);
  - before each part was read, `awk` line lengths;
  - `sed|grep -o|wc` token counts for clipping;
  - `shasum`;
  - after all four parts were read, `diff|grep` change markers on the hash-verified S3/S4, plus tool `grep` searches over parts 01–03.

  None of this was scientific execution, solver work, code authored, arithmetic on scientific content, examples or proofs. Comparing numbers and list items between dispositions and receipts was literal token matching.
- **P4:** within each part, consecutive windows were sometimes requested together in one ordered batch. No later part was opened before the previous part's ending. Provisional observations formed in context while reading serially, as is normal. All tool-based comparison and all drafting of findings happened after part-04 LF2310. I give no certificate about private cognition.
- **P5:** before the ACK I read the skills, for process only. I did not use the external-model procedure. I opened no held episodes, consumers, sibling outputs or linked bodies beyond the packet. The S-source files were used only for shasum and for the S3/S4 diff. I sent no messages other than the pre-body ACK.

## 10. Assurance limits

- This is one same-harness documentary reviewer.
- It gives no human, independent-family, kernel, novelty, priority, original-source-identity or whole-report acceptance.
- Missing underlying proofs are coverage boundaries. They are not treated as falsity.
- All genuine held episodes AND ALL consumers remain NONINPUT.
