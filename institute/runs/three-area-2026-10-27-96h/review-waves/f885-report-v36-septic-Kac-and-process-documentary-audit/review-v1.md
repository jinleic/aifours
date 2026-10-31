# F885 — v36 septic ratio/root floors, r2 isotypic and completed-audit/process: documentary review

Reviewer `DocF885SPRKM36`. Native observation before writing: `2026-10-30T20:29:46-0700` (`2026-10-31T03:29:46Z`). New exclusive file.

Before the first packet-body access, this reviewer wrote the prebody ACK `prebody-ack-v1.md` (2286 B, sha256 `41a56c4f…42da`) and sent a direct ACK message to Main. The additive `prebody-ack-v1-erratum-1.md` (1201 B, `af2bfeb5…4bb9`) corrects that ACK's administrative-window wording (§2.4 P2).

**Duty and limits.** This is a DOCUMENTARY-ONLY comparison. It compares the frozen v36 report (S4) with the frozen v35 report (S3), the two v35 errata (S1, S2) and the complete literal bodies S5–S22. The assigned scope is:

- the v36 info-2 and math-3 rows;
- the opening, the footer, the evidence paragraph's as-of counts, and process;
- the completed v33/v34 and v35 scoped outcomes;
- the CP145 active-field clarification.

The review does not cover proofs or science. It derives no new algebra, does no arithmetic and uses no example or instance. It executed nothing and consulted no external source or model. All held episodes AND ALL consumers stay NONINPUT; controls were used as status only. Where an underlying body was not supplied, the result is an INCONCLUSIVE coverage boundary, not falsity.

**Reviewer result (the parent's disposition is separate):** **0 FATAL / 0 MAJOR / 9 MINOR** documentary findings (F885-m1…m9, §5). All nine are new v36 events. None recounts a finding already recorded for v33/v34 or v35 (§6). Most scoped items are ACCEPTED at documentary scope (§4). §2.4 lists four reviewer self-reported process items (P1–P4).

## 1. Administrative status (status only)

| File | sha256 | Size |
|---|---|---|
| manifest | `a348cbd0…e78e` | 20793 B / 465 LF |
| freeze receipt | `89c0c328…8bc5` | 19487 B / 427 LF |
| final binding | `74ebad55…c9bb` | 20667 B / 319 LF; `all_match` true |
| metadata supply | `9ef9b4b3…4c40` | 20147 B / 440 LF |
| actual dispatch receipt | `981d95c4…6537` (live) | 4042 B / 83 LF; names `DocF885SPRKM36`, wave f885 |

`shasum -a 256` of these five files, the three parts and the 25 controls matched every pinned value. Per the metadata qualification, this is administrative only: it certifies no correctness, source identity or cognition.

Packet-part composition and the location of each source inside its part (`Sx|n` is logical line n of source x):

| Part | sha256 | Size | Sources and packet LF ranges |
|---|---|---|---|
| 01 | `b46772f7…f179` | 72366 B / 70 LF | S1 6–14, S2 19–23, S3 28–69 |
| 02 | `1a9f9994…402e` | 86441 B / 366 LF | S4 6–47, S5 52–94, S6 99–202, S7 207–209, S8 214–365 |
| 03 | `f6425369…0e84` | 99223 B / 862 LF | S9 6–279, S10 284–313, S11 318–341, S12 346–368, S13 373–392, S14 397–427, S15 432–464, S16 469–498, S17 503–541, S18 546–573, S19 578–776, S20 781–789, S21 794–798, S22 803–861 |

The number of logical lines in each source matches its manifest `LF`.

Key cross-reference pins agree as literal strings:

- S8 report/base/errata pins: S8|4–27.
- S8 new_sources: S8|84–147.
- CP145: S9|12–21, S9|33–84, S9|239–268.
- S10 checkpoint pin: S10|5–6.
- S5 and S6 corrections: S5|27–36, S6|95–96.
- S14|29–31 and S15|33: the S15 and S16 pins.
- S20|8 vs S19|5–6: the same v2 source pin.

All of these equal the manifest pins for S1–S22.

## 2. Read coverage and process disclosures

### 2.1 Order

1. Manifest, freeze receipt, final binding, metadata and actual dispatch receipt, then all 25 status-only controls, each read completely.
2. Prebody ACK file, then the direct ACK to Main. No packet body had been displayed before this point.
3. Part 01 LF1–70, part 02 LF1–366, then part 03 LF1–862, each completely and in ascending order.
4. Comparison. No comparison or derivation started before part 03 LF862 was displayed.

### 2.2 Counts and measured windows

Packet-body windows, measured from the exact window list with a byte/LF metadata script:

| Part | Windows | Max LF | Max bytes | Coverage |
|---|---|---|---|---|
| 01 | 20 | 20 | 24041 (LF67 = S3\|40, process paragraph, read alone) | every LF exactly once; no gap or overlap |
| 02 | 41 | 20 | 24041 (LF45 = S4\|40, process paragraph, read alone) | every LF exactly once; no gap or overlap |
| 03 | 141 | 20 | 2030 | every LF exactly once; no gap or overlap |

Total: 202 windows. Every window was ≤20 LF and <30000 B. All long report rows (S3|11–28, S4|11–28), the evidence paragraphs, the footers and both 24 KB process paragraphs were read in windows of 1–2 LF. The exceptions are P1 below.

Administrative files were read over LF1–465, LF1–427, LF1–319, LF1–440 and LF1–83 respectively. The 25 controls were read in 36 windows, each ≤20 LF. Three administrative windows exceeded 20 LF (P2).

### 2.3 Clipping control

After each window containing a long line, the reviewer used `awk` to display the final 50–60 characters of the lines just read. For the two 24 KB process paragraphs and for S3|42, S4|32 and S4|42, it also displayed 60-character interior anchors at fixed offsets. Every fragment matched the displayed window, so there was no clipping in any packet-body window.

To plan windows, the reviewer displayed byte lengths and `### S` header line numbers of lines not yet read. This was metadata only: no body text from beyond the serial frontier was shown. One metadata-only output (a per-line length list for part 02) was truncated by the tool and was re-run with a filter; it contained no body content.

### 2.4 Reviewer self-reported process items (the parent classifies them)

- **P1 — report-window deviation; self-classified ONE reviewer PROCESS MINOR, by the F854 precedent at S5|40.** Three windows held more than two report lines, contrary to the dispatch instruction to use 1–2 LF for reports:
  - part 01 LF1–20 (S1|1–9 and S2|1–2, erratum lines; 2359 B);
  - part 01 LF21–37 (S2|3–5 and S3|1–10, including the 1586-byte v35 opening paragraph S3|3; 3810 B);
  - part 02 LF10–15 (S4|5–10, short heading/intro/table-header lines; 480 B).

  Each window was ≤20 LF and <30000 B. Tail checks on every line longer than 300 B in these windows matched, so nothing was clipped. Compliance is not backdated.
- **P2 — inaccurate ACK wording.** The ACK file and the direct message said every administrative read used ≤20-LF windows. In fact three administrative windows were longer: manifest LF441–465 (25 LF), freeze receipt LF401–427 (27 LF) and dispatch receipt LF61–83 (23 LF). They were small in bytes, and all were read before any body. The manifest `packet_policy` 20-LF limit governs the packet parts, which complied (§2.2). The ACK is corrected additively in `prebody-ack-v1-erratum-1.md`; the ACK file is unchanged.
- **P3 — sequencing qualification.** Within a single part, consecutive in-order windows were sometimes issued as one batch of tool calls. Examples: part 01 LF62–66; part 02 LF1–9, LF42–44 and LF204–210; part 03, in batches of up to six windows. The tool may have run these concurrently. Outputs were consumed in ascending order, and no batch crossed a part boundary. Strict one-window-per-call access is not claimed; the parent may classify this as a possible PROCESS MINOR.
- **P4 — scratch writes outside the wave directory.** During the comparison phase only, the reviewer wrote prefix-stripped copies of S3|1–42 and S4|1–42 (84 files, text already read) to `/tmp/f885cmp/` so they could be diffed word by word. This is outside the repository and the wave directory. Under the no-deletion rule the files were not deleted. They are not outputs. The parent may classify this as a possible ownership deviation.
- **Tools.** Raw `read` windows; `shasum`, `wc`, `awk`, `tr`, `diff` and `grep` for metadata, presence checks and text comparison only. No scientific execution, solver, arithmetic on scientific content, example or instance. No linked body outside the packet, Git, build, test, delete or overwrite. Outputs, all new and in this directory: `prebody-ack-v1.md`, `prebody-ack-v1-erratum-1.md`, `review-v1.md`.

## 3. Mechanical v35 → v36 census

A line-equality census of the prefix-stripped packet text found that S4 differs from S3 exactly at logical lines **1, 3, 12, 16, 19, 24, 25, 28, 32 and 42**; every other logical line is equal. This reproduces S8|29–41 (`changed_logical_lines` and `"unchanged_other_lines_byte_equal": true`). Equality with the source bytes relies on the parent's freeze-receipt round trip.

In scope here are L1, L3, L12, L19, L32 and L42, plus process lines L38 and L40, which are unchanged. L16, L24, L25 and L28 are out of scope (§8).

L1 changes only `v35,` to `v36,`.

## 4. Scoped comparison — accepted items (documentary scope only)

### 4.1 Opening (S4|3), as-of counts and footer (S4|42) — accepted except m8 and m9

- The v35 outcome "records0F/1M/4m at its exact frozen scopes plus a separate report-window process finding; not scientific falsity or whole-report acceptance". This matches S5|24 ("Unique new v35 scoped documentary findings 0F/1M/4m"), S5|40 ("F854 ONE report-window PROCESS MINOR") and S5|41.
- The v33/v34 outcome "retains0F/1M/4m new unique findings, earlier stale-footer and separate chronology issues not recounted". This matches S6|60 and S6|61, and S7 is linked.
- The footer statement "complete ONLY at their frozen changed scopes, not science or whole-program certifications" matches S5|41 and S6|102.
- The cutoff `2026-10-31T21:23:27Z` matches S9|4.
- "Newly adopted scopes below postdate those snapshots": S18 (`02:41:18.877Z`), S11 (`02:42:12.947Z`), and S12 and S13 (`02:52:36.439Z`) are all later than the v35 observation (S3|3, `02:37:09.315Z`), and S1|9 states that later adoptions are not backdated into v35.
- The S4|32 ledger count "**382 historical data rows**" matches S8|77 and S9|26 (`data_rows` 382).
- S4|32's finite-receipt labels F842main, F842companion, F864v2 and F867v2 match S9|87–112.
- S4|32's unadopted candidates F846–F848, F849, F850, F853, F860 and F861 match S9|120–169.
- "V36 changed-scope checks have NOTyetbeen dispatched or passed" matches S8|150 and was true as of composition (S4|3 `02:58:33.044Z`, earlier than dispatch `02:59:56.266Z`).
- "NONFINAL18-slot" matches S8|42–61 (18 rows of 3 cells).

### 4.2 info-2 (S4|12, packet p02 LF17) — accepted except m1–m4

- **h positive:** "choose h_i strictly positive on the ENTIRE actual rectangle" matches S14|7. The v34 h_i MAJOR repair (S6|59) is retained.
- **j definition:** "j_i=0 if any actual corner determinant vanishes and1 otherwise" matches S1|5 and S14|11. The v35 erratum-1 j_i MINOR is corrected.
- **Weight per node:** "At EACH node the common positive E/O weight exists iff h_i(T_i)>0 and corner determinants bracket zero" matches S14|9–11 and S1|5 ("one common E/O weight per node"). Observation: v35's explicit "not one global weight" disclaimer is gone, and with the new "ONE common k" clause the word "common" now appears in two senses. The reviewer reads the weight as per-node; no finding.
- **Fixed nodes/group/endpoint moments:** "at fixed nodes/group contributions/endpoint-moment constraints" matches S14|7 and S14|11. **Common k:** "ONE common k" matches S12|10. The "nonempty class" matches S12|21.
- **Six-node clauses:** "adjacent-corner nonintersection" matches S13|5; "all12-row extremal root floors" matches S13|7; and "two specified stronger corner-zero exclusions" matches S13|13–18.
- **Explicit HB imports:** "named strict Hermite–Biehler/physical bands" matches S11|3, S12|3, S13|3 and S14|15. This is explicit in v36, whereas the v35 row named no HB import.
- **Not global SPR/ROOT/dual:** "not feasible duals or a universal row/all-box SPR/ROOT theorem" matches S11|24, S12|19 and S12|21, S13|3 and S13|20, S14|27, and S16|22.
- **Endpoint and import statements:** "Five-node ANY absentendpoint is independently excluded; both-positive has three necessary patterns, not realization" matches S11|6, S11|8–12 and S11|14. "General >=6 still imports the separate <=5 strict-negative no-go through eligible BUFFERED enlargement, not same-box strictification" matches S11|14, S14|27 and S16|20; the v33 import-direction MINOR (S6|58) stays corrected. "Other endpoints and7/8nodes remain open" matches S11|24 and S13|20.

### 4.3 math-3 (S4|19, packet p02 LF24) — accepted except m5 and m6

- **r3 whole grade 4:** "r3 has R intersect S4=0 for EVERY integer s>=4, hence J_(a,b,4)=tau_(a,b,4) for all a,b" matches S17|5, which says "equivalently … for EVERY a,b>=0".
- **r2 is a single entire isotypic:** "NEWr2: for allinteger s>=3 the ENTIRE two-copy L_low(1,4) isotypic has zero radical intersection by a constant-8 minor" matches S18|6, S18|17 and S18|19.
- **r2 dimensions:** "firstrelation dimension252 and actualgrade4 dimensions675/756 at s3/>=4" matches S18|5 as literal tokens.
- **r3 vs r2 distinction:** "no … r1/entirer2grade4/highergrade/globalJ=tau … claim" matches S18|6 ("This is one isotypic, NOT the entire r2 grade4 radical or global J=tau") and S9|115.
- **Signed/normalized minors:** "appropriately SIGNED/NORMALIZED … positive constants and nonnegative later coefficients" matches S2|3 and S17|23–34; see m5 for the dropped "selected".
- **Replays:** "Separate exact determinant and complete bracket-tree basis/action replays bind the SAME six dossier bytes" matches S17|21 and S7|3. The v34 determinant-vs-basis-action replay-scope MINOR stays corrected.
- **Capture:** "initial truncated proc/failedJSON recovery is one retained parent capture MINOR, not failedscience" matches S2|5, S18|28 and S19|65–68. The v35 erratum-2 disclosure MINOR is corrected; v36 places it in the math-3 gap cell rather than the evidence paragraph S2|5 named, and the reviewer accepts that as the successor disclosure.
- **v1 design:** "F832v1 pre-run design MAJOR UNRUN, v2 one run" matches S20|3, S19|22–23 and S18|28.
- **Chronology and verdicts:** "F807 exitzero defect discovered AFTERv3run" matches S21|3–5. "F775 remains NO VERDICT/unrerun" matches control f775 and S17|39. The 10-dimensional kernel is not identified with the radical or lowest kernel, matching S17|37.
- **No source identity:** "no printed-source authentication" matches S17|7, S17|10 and S18|28; the opening also states no original-source identity.
- **Observations, not counted:**
  - The NEWr2 clause carries no import list of its own. Only the row-level gap clause applies ("Named presentation/Cartan/source/whole-ideal and classical representation imports remain"). S18|3's r2-specific named inputs are not attached to the r2 clause: the bridge, the entire grade-two input, and the entire grade-three input with its scope correction.
  - The entire grade-two import named in S17|10 was not enumerated for r3 in v35 either; this is inherited.
  - "for EVERY full complex Cartan realization" became the heading "full-Cartan", which states less, not more.
  - `constant-8` reads as "constant −8" in the report's space-stripped style, matching S18|19.

### 4.4 Process (S4|38 and S4|40 unchanged; process items in L3, L19, L32, L42)

S4|38 and S4|40 are byte-equal to S3|38 and S3|40: inherited, not newly certified. Process events new since v35 that v36 does state are the F854 MINOR (L3, L42), the F832 capture MINOR, the F832 v1 design MAJOR and the F807 chronology (L19). Omissions are recorded as m6–m8.

### 4.5 CP145 active-field clarification (S9, S10) — accepted

S10|10 says: "The field named active_gates is an assignment/manifest list, NOT an observed list of still-running agents; … ONE parent documentary lifecycle-label MINOR". Each of the 13 S9|170–236 `active_gates` waves (f868–f873, f876–f882) matches exactly one name in S10's `observed_running` list (F872, F878–F882) or `returned_not_running` list (F868–F871, F873, F876, F877). This is a match of labels, not a count.

The timeline is consistent: v36 at `02:58:33.044Z`, CP145 at `02:58:47.672Z`, S10 at `02:59:08.652Z`. v36 makes no live-runtime active-gate claim in scope, and v35's "F838–f844 and f845 are actual frozen active duties" sentence is not carried forward.

CP145's science frontiers agree with the v36 rows: "Kac" at S9|115 and "septic" at S9|118 ("…supported atnamedHB/actualbands, noeligibledual/globalSPRROOT"). CP145's `new_adopted` list differs from v36 (see m4). The S10 lifecycle MINOR is a parent checkpoint item outside v36 and is not recounted here.

## 5. Findings (all MINOR, all new v36 events)

**F885-m1 — info-2 definitions condensed (notation MINOR).**
- v36 S4|12: "define T_i from evaluated interpolation polynomials and choose h_i strictly positive on the ENTIRE actual rectangle."
- v35 S3|12 (p01 LF39) had: "put T_i=sign(Hprime(u_i))(A(u_i),B(u_i)); choose h_i a linear functional strictly positive on the ENTIRE actual rectangle R(u_i)."
- S14|7 (p03 LF403): "Set T_i=sign(H′(u_i))(A(u_i),B(u_i)) … choose a linear functional h_i strictly positive on the actual rectangle R_i (one of E,−E,O,−O …)"
- S14|11: "The strict first inequality is indispensable: determinant zero alone permits an antiparallel ray or zero."

The orientation factor sign(H′(u_i)) and h_i's linear-functional form are no longer stated, so the condensed iff "h_i(T_i)>0" cannot be rebuilt from the row. This is the same class as the S1|5 undefined-j_i notation MINOR but concerns different symbols, and it regresses from v35's explicit text. S14 keeps the exact definitions.

**F885-m2 — info-2 minimum loses its object (scope MINOR).**
- v36 S4|12: "…gives exact fixed-group minimum n+sum j_i plus combined endpoint atoms."
- v35 S3|12 had: "the exact minimum corner-atom count is n+sum j_i plus endpoint atoms."
- S14|11 (p03 LF407): "the exact minimum finite corner-atom count is n+Σj_i … it does not treat arbitrary interior-member atoms as corner atoms."

The minimized object ("corner-atom count") and S14's interior-member disclaimer are dropped, so "exact fixed-group minimum" can be read beyond the source's corner-atom scope. The reviewer does not assess whether any broader reading is true or false.

**F885-m3 — necessity and object labels of the new five- and six-node clauses implicit (scope/necessity MINOR).**

v36 S4|12: "Newfive-node ratio iff retains ONE common k and exact boundary conventions; a strict same-box bandwidth condition excludes a nonempty class of sufficiently narrow Hurwitz boxes. Six-node/no-endpoint actual corner quintics have adjacent-corner nonintersection, all12-row extremal root floors and two specified stronger corner-zero exclusions."

The sources say:
- S12|3: "…with both endpoint rays lambda,mu>0 … There is no claim that any such relation exists."
- S12|10: "…with both endpoints positive and no atom cap, exists IFF … ONE common k>0 … with infinity not attained … a coupled same-box existential test, not a solution of it."
- S12|15: "Any five-node relation using that SAME actual pair necessarily has"
- S12|19 (p03 LF364): "If it fails for all three allowed band pairs, that whole particular K has no five-node relation under ANY endpoint pattern. This is a sufficient box-specific obstruction, not an assertion about every eligible K."
- S13|3: "These are necessary consequences…"
- S13|13: "On the actual row (2,4;3,4)…"
- S13|18: "They do NOT eliminate the whole row…"
- v35 S3|12 had "twelve NECESSARY six-node/no-endpoint patterns".

Three gaps follow:
- (a) The bandwidth clause names no excluded object. Five-node scope (failure of the necessary strict inequality for all three allowed band pairs) is conveyed only by the clause's position after "Newfive-node ratio iff".
- (b) Neither the bandwidth inequality nor the six-node floors and exclusions are labeled as necessary consequences of a hypothetical actual relation.
- (c) The ratio-iff clause omits its both-endpoints-positive and k>0 hypotheses. Elsewhere the row says only "both-positive has three necessary patterns".

The gap cell's "not feasible duals or a universal row/all-box SPR/ROOT theorem" prevents a global SPR/ROOT/dual claim. The reviewer treats the five-node scope as recoverable, hence MINOR. If the parent reads the bandwidth clause in isolation as excluding every relation on those boxes, it would be stronger than S12 supports, and the parent may reclassify.

**F885-m4 — post-v35 adoption S11 missing from v36's enumerations (as-of/navigation MINOR).**

S11 is "Recorded UTC 2026-10-31T02:42:12.947Z" (S11|3, p03 LF320), after v35's composition (S3|3). v35's S3|12 says "F816 five-node endpoint and F817 mixed-edge refinements remain UNADOPTED". CP145 lists S11 under `new_adopted` (S9|38–43, `66aa98e3…`).

v36 S4|32 (p02 LF37) reads: "Since v35, [r2 whole-copy result], [AME t28 exclusion], [AMEt26q5/4444], [exactt23/t24 and conditional t22/t26union], [mixedPPTexterior], [highdefectmajorization], [septicratio/bandwidth] and [septiccornerfloors] were adopted only at their exact imports." This omits S11, and S8's `new_sources` (S8|82–149) omits it too.

The v36 info-2 row links only S14, S12 and S13, yet it states S11's results in its gap cell. S11 is reachable only through the imports at S12|3 and S13|3. The S16 physical-band import named in the row is likewise no longer linked; v35 had "[Physical bands]". Presence checks over p02 LF6–47 found no S11 or S16 path in v36. Whether the 382-row ledger has an S11 row is INCONCLUSIVE, because the ledger was not supplied.

**F885-m5 — r3 minors no longer "selected" (precision MINOR; residual of implementing erratum-2).**
- v36 S4|19: "The six complete lowest maps have appropriately SIGNED/NORMALIZED determinant polynomials…"
- S2|3 (p01 LF21): "Its math-3 row must say the six selected determinant polynomials are **appropriately signed/normalized**"
- S17|23: "the six selected ordered-row determinants"
- S17|34: "Nonzero minors on the SAME independently verified complete bases imply injectivity…"
- v35 S3|19 had "same-data selected determinant polynomials".

The sign/normalization wording is implemented, but "selected" ordered-row minors became determinant polynomials attributed to "the six complete lowest maps". This is distinct from S2's sign MINOR, which is not recounted; the parent may merge the two.

**F885-m6 — math-3 process and assurance disclosures dropped (disclosure MINOR).**
- v35 S3|19 (p01 LF46): "This is a conditional computer-assisted same-harness result … F833/F834 each21LF PROCESS MINOR, F807 v3 exitzero/nonpass DESIGN MAJOR discovered after its run…"
- v36 S4|19: "F775 remains NO VERDICT/unrerun. F807 exitzero defect discovered AFTERv3run; …"
- S17|7: "The six symbolic-map identities are computer-assisted"
- S17|39 (p03 LF541): "F833 and F834 each had ONE distinct 21LF packet-window PROCESS MINOR … retains F807 exitzero/nonpass DESIGN MAJOR"

Three items were dropped: the two F833/F834 PROCESS MINORs, F807's "DESIGN MAJOR" severity label, and the "computer-assisted" assurance label. A grep over p02 LF6–47 finds none of them anywhere in v36. The precedent is S2|5: an omitted recorded process MINOR counts as one documentary disclosure MINOR.

**F885-m7 — S22 ACK-transport disclosure dropped (disclosure MINOR).**

v35 S3|32 (p01 LF59) said: "[ACK-transport observations](…parent-f826-f832-direct-ack-transport-observations-v1.json) retain seven direct-delivery process MINORs and the parent prompt-clarity MINOR; no backdating." S4|32 removes this sentence. A grep over p02 LF6–47 found no S22 link and no "prompt-/instruction-clarity", F830 or F831 text.

S22|5–53 records one ACK-transport PROCESS MINOR each for f826–f832, and S22|55–56 records "ONE instruction-clarity PROCESS MINOR". v36 keeps only F828 and F829 (S4|16, "their two ACK-transport PROCESS MINORs"). The newly adopted r2 disposition records "F830/F831/F832 each have ONE direct-ACK transport PROCESS MINOR" (S18|28, p03 LF573), but the math-3 row omits them. The generic S4|40 pointer to README run controls points at a body that was not supplied (INCONCLUSIVE).

**F885-m8 — reviewer-process MINORs of the completed v33/v34 outcome not stated (disclosure MINOR).**

v36 S4|3 gives only "…retains0F/1M/4m new unique findings…", while S4|42 names "the separate F854 report-window process MINOR" for v35. The v33/v34 outcome records:
- S6|64 (p02 LF162): "f836": "ONE prerequisite/ACK PROCESS MINOR…"
- S6|65: "f837": "ONE conservative administrative-window PROCESS MINOR…"
- S6|66: f845's common-file binding "INCONCLUSIVE within this reviewer packet", clarified by S7|3.

v35 S3|42 had disclosed that "f836 returned a qualified Kac comparison with an administrative-prerequisite deviation". The counts in v36 are literally correct (S6|60). The asymmetric omission matters because earlier footers carried reviewer-process findings, e.g. V25's "TWO separate reviewer processMINORs" at S3|42 and S4|42.

**F885-m9 — footer drops V30 and the v31/v32 outcome link (footer as-of/navigation MINOR).**

v35 S3|42 (p01 LF69) said: "V30 and the [v31/v32 three-scope documentary outcome](…v31-v32-documentary-audit-outcome-v1.json) remain complete ONLY at frozen scopes." v35 S3|3 also linked "[V31/v32 scoped outcome]".

v36 S4|42 (p02 LF47) reads: "V31/v32, [v33/v34] with [access clarification], and [v35 complementary outcomes] are complete ONLY at their frozen changed scopes…" A grep over p02 LF6–47 found no "V30" and no v31/v32 outcome link anywhere in v36.

## 6. Prior findings and errata at this scope: overlap accounting

**Corrected in v36 and accepted:**
- v35 erratum-1 j_i notation MINOR (S1|5).
- v35 erratum-2 signed/normalized MINOR (S2|3), except the residual "selected" in m5.
- v35 erratum-2 F832 capture disclosure MINOR (S2|5).
- v34 h_i positivity and per-node weight MAJOR (S6|59).
- v33 ≤5 import-direction MINOR (S6|58).
- v34 replay-scope MINOR (S6|59).

**Not recounted:** v33/v34 DC zero, F815, the stale footer, the F807 chronology item, and F855's other overlaps (S1|9, S5|39), all outside this scope.

**New events:** m1–m9 are all new in v36. m5 is adjacent to the S2|3 item, and m6 and m7 both concern process disclosure but involve different records; the parent may merge either pair.

## 7. Coverage boundaries (INCONCLUSIVE; not falsity)

These bodies were not supplied and not read:
- Candidates and sources: F816, F817, F838, F839, F858, F859, F784, F785, F742, F759, F760, F807, F808, F809, F821, F824, F825, F830, F831, F833, F834, F843, F844; the F832 source.
- Imported dispositions: the bridge, the grade-two and grade-three results, the isotypic and singlet exclusions, the sparse zero dual and the four-corner SDP.
- The README ledger and run controls.
- The v31/v32 outcome and the f835, f836, f837, f845, f854 and f855 review bodies.
- Checkpoint 144.
- The f842, f864 and f867 receipts and the AME, PPT and depolarizing dispositions.

The mathematical correctness of S11–S18, the dossier joins and the run results is not assessed. The ledger contents behind the 382 rows and S8's href/render validity (173 hrefs, 3 cells per row) were not independently verified.

## 8. Out-of-scope incidental pointers (not reviewed, not counted)

1. S4|28 says "f861same-Pcount refinements likewise ungated", while S4|32 says "F8604444andF861incidence candidates remain UNADOPTED pending separatecriticalgates" and S9|114 says "f861Pprofile refinements underf876–878". This is possible wording tension in the sibling physics-6 scope; it was not assessed.
2. S4|16 differs from S3|16 only by the inserted "ORIGINAL Walsh cap28," (v35 erratum-1, S1|3). It belongs to the sibling scope and is not certified here.
3. Several table rows lack a trailing " |": S4|12, S4|16, S4|19, S4|24, S4|25 and S4|28, as did S3|12, S3|16, S3|19 and S3|28. S8 nevertheless reports 18 rows of 3 cells. Rendering was not otherwise assessed.

## 9. Non-claims

- Unchanged and out-of-scope rows are inherited, NOT newly certified.
- No global report, science, theorem, family, human, kernel, novelty, priority or original-source-identity acceptance.
- No clean-cognition certificate.
- Hashes are administrative only.
- The parent's disposition is separate.
- All genuine held episodes AND ALL consumers remain NONINPUT.
