# OlsonTerminal shard: documentary return

**Verdict: FIX.** FATAL 0, MAJOR 0, MINOR 4. All four are documentary. None changes a theorem, inequality, scope, status or count.

- **No REJECT.**
- **No RE_REVIEW_REQUIRED.** No checked claim depends on a missing body.
- **Optional precision items:** 3.
- **Per-file:** I checked all 63 assigned records against their whole pasted bodies and their report destinations. 63 PASS, 0 FIX, 0 unsupported.

**Method:**
- I compared the pasted text by hand only.
- For the displayed table cells, I substituted each value by hand into the provider's own stated domain. I used no program, parameter loop or enumeration.
- Hashes, LF counts and clock stamps are treated as supplied metadata, not authenticated.
- The inventory SHA strings for all 63 records match the pasted WholeSHA headers by string comparison.

## 1. Minimal numbered fixes (exact original LF)

**F1 (MINOR). Report v12 LF141, §4.4 D1-END bullet.**
- Current text: "For p≥11 its delta-one residual is {(p−1)/2,(p+1)/2}∪{p−3,p−2,p−1}; p7 keeps {3,4,5,6}."
- Problem: this reads as the global δ=1 residual. It is not.
  - D1-END's ledger is relative to I.14 + RP-2NE + D1-END only.
  - It omits RPdelta B-prime N(p,1), accepted earlier (2026-10-19 13:04 versus 2026-10-21 07:46).
  - B-prime already covers (p−1)/2 for p≥19 and (p−3)/2 for p≥17.
- Replacement reading:
  - "D1-END's own route-relative ledger (I.14+RP-2NE+D1-END only) leaves {(p−1)/2,(p+1)/2}∪{p−3,p−2,p−1} for p≥11, and {3,4,5,6} at p7."
  - "After the accepted RPdelta B-prime, the global δ=1 numerical remainder is:"
    - p≥19: {(p+1)/2, p−3, p−2, p−1};
    - p∈{11,13,17}: additionally (p−1)/2;
    - p=7: {3,4,5,6}.
  - "These are numerical bands only. No D1-END duplicate credit is taken where B-prime applies."
- Sources:
  - D1-END verdict LF7 and erratum v1 LF8;
  - RP2NE verdict LF8–10;
  - RPdelta verdict LF28 and LF33–40, plus consolidated E1 LF29–49;
  - cp-01 LF13–23.
- My hand re-derivation agrees for p=7, 11, 13, 17 and 19.

**F2 (MINOR). v12 erratum 7 LF3.**
- The list "LF184/325/336/362" of then-current activity sentences now read as HISTORICAL should become "LF154/184/325/336/362".
- Reason: LF154 says "The current independent high-core follow-on is §4.7's fresh scope". By 18:40:59 that follow-on had ended NOT_PROVED (HIGH-CORE verdict LF3, LF11), and the slot had been reassigned and then parked (erratum 7 LF9, LF11).
- Pointer for integration only, outside my sections and not assessed: report LF3 ("The existing math2 worker is assigned the full core") is the same kind of sentence.

**F3 (MINOR). Erratum 7 LF9.**
- Current text: "received the fresh frozen […] at17:36:26".
- Problem: this attaches the scope's freeze time (scope LF2–3) to its receipt. The receipt instant is unattested. The worker read the scope before /bin/date returned 17:37:22 and acknowledged it at 17:37:55 (ack LF3, LF95).
- Replacement: "scope frozen before dispatch at 17:36:26; receipt instant unattested; acknowledged 17:37:55".
- This is the same timestamp-precision issue as the already-withdrawn "18:0xPT".

**F4 (MINOR). DELTA1 source-history erratum LF9 (item 5).**
- Current text: "COREfinalverdict/parenterratum3explicitlyincludezero-lettercorollariesandgeneraldata/normalizationalgebra".
- Problem: this overstates two sources.
  - HIGH-CORE parent erratum 3 (LF3–7) mentions neither the corollaries nor the algebra.
  - The final verdict names neither the δ/GRX data identities nor the TOP λ-normalization.
- Replacement reading:
  - The final verdict LF7 (Z2 "including zero-free LETTERS at k=p+2 in that lowerhalf") and the disposition's accepted_scope at LF75 ("Z1/Z2+corollaries") explicitly include the zero-letter corollaries.
  - The (G)/(D) data identities and the TOP normalization are proof-internal algebra. Both families PASSed them (Codex LF11, LF15; Claude rows 1–2 and 6), but they are not separately enumerated accepted statements.
  - The clause "old token list is not a stronger exclusion/converse claim" stands.
- The report text itself is unaffected. Erratum 7 LF7's list of accepted implications is correct.

**Optional items (not counted):**
- **O-1, LF140 (RUH2).** Add the verdict LF14 history: original Codex 0F/1M/5m with the substantive c9 nonwrapping repair, then corrected Codex 0F/0M/0m and Claude 0F/0M/2m (disposition LF37–76). This matches the practice at LF48 and LF285. Nothing is currently erased.
- **O-2, navigation.** FC1023 v1 body LF13 composes the p23 providers wrongly. It gives κ5 as FCW "p=4·5−1", κ6 as TCW "p=4·6−5" and κ7 as SCW "p=4·7−3", none of which equals 23; the correct providers are USK 3–5, FCW 6 and TCW 7.
  - That list is superseded: the v3-audit disposition LF20–23 "reconciles", and the v2 confirmation LF5 points to the unpasted frontier-v2-erratum (bec9cfbf…).
  - Report LF99 already uses the correct providers. The final maps may note "v1 LF13 superseded".
- **O-3, historical interim status LF5.** It says "launched 18:06:10PT", but the HIGH-CORE disposition receipt (LF32) has started_at 18:06:44. No source for 18:06:10 is supplied. This record is non-operative.

## 2. Claims checked within the assigned scope

**§4.2 per-prime table, LF94–105: PASS.**
- I substituted all 12 rows by hand. The provider domains used:
  - K0T for any odd prime (verdict LF5); LOWER-K1 and K2 for p≥11;
  - USK for [3, ⌊(p−1)/4⌋];
  - FCW/SCW/TCW/FQW for p=4κ−1/−3/−5/−7, with κ≥3/4/4/5 respectively;
  - UFC T0 for κ≤(3p+5)/8 when p≡1 mod 4 and κ≤(3p+7)/8 when p≡3 mod 4;
  - UPAR for 5κ≤2(p+1), plus (10,23) and (13,31);
  - UPAR2 for 9κ≤4p+2 (κ even) or 9κ≤4p+5 (κ odd); UPAR3 for 9κ≤4p+10;
  - the BOTTOM composite for [(p−1)/2, p−2], and PP1 for p−1.
- The rows also agree with the per-prime verdict tables: P7L LF9, TCW LF11, FQW LF9, FC717 erratum v1 LF7–18, FC19 LF17–30, and the UFC/FC1023 named cells.
- Assigning κ3 to USK at p≥13 is valid within USK's own domain (consistent with LF84).

**LF107, LF111, LF115–117: PASS.** Each matches its provider verdict at LF5, BOTTOM LF5 and LF9–15, R7 LF5, v7 note LF13–26, and v7 audit LF34.

**Full k=p+1 closure for every p≥7, LF166: PASS.**
- The v8 LF13 partition is contiguous for p≥29: 0, 1, 2, [3,j], j+1, j+2, [j+3,(p−3)/2], [(p−1)/2, p−2], p−1.
- The κ minima for SCW, FQW, FCW and TCW hold for every p≥29.
- The p7–23 rows are covered by the table check above.
- The antecedent is existential (v8 LF7). The note makes no claim about every avoider, p5, other k, or full Olson (v8 LF15; audit LF34).

**§4.3, LF122–136: PASS.**
- With p=2d+2κ−1, the three bounds are equivalent as stated: κ≤8d−2 ⇔ 9κ≤4p+2, κ≤8d+1 ⇔ 9κ≤4p+5, and κ≤8d+6 ⇔ 9κ≤4p+10.
- κ=8d+2 and 8d+5 give p=18d+3 and 18d+9, both divisible by 3, as the report says.
- The named outcomes match:
  - UPAR verdict LF7–9 and erratum v1;
  - UPAR2 verdict LF7–11 and errata v1–v3;
  - UPAR3 verdict LF7–15 and errata v1–v2;
  - frontier v6 erratum LF5–10.

**§4.4:**
- LF140: PASS, with optional O-1.
- LF141: fix F1.
- LF142: PASS against the ROT-PP1 verdict LF5–16, disposition LF101–103 and errata v1–v4.

**§4.5:**
- LF148–152: PASS. 27κ≤13p+3 ⇔ κ≤26d−10. R4 is literal. The counts match UPAR4 verdict LF7–13 and its disposition.
- LF154: fix F2, plus the unverified times listed in §6.

**§4.6, LF159–168: PASS** against:
- UPAR5 verdict LF5–13;
- UPAR5 erratum v1 m1–m6 and erratum v2 LF5;
- UPAR5 disposition LF19–36;
- the v8 note and audit.

**§4.7, HK1, LF173–182: PASS** through v12 erratum 3 items m5 and m10. These cover κ̂1, p5, the top near-pair, the necessary-only HIGH-K-RES, and the P/S(p)/CT trust levels. Checked against:
- HK1 verdict LF7–24 and disposition LF73–170;
- parent errata 1–3 and worker erratum 1;
- Codex complete-P LF11–44;
- Claude complete-P §0 and §4.

**LF184:** PASS as a historical record, per erratum 7 LF3.

**Core auxiliary results accepted, entire target NOT_PROVED (erratum 7 LF7): PASS** against:
- HIGH-CORE verdict LF3–11;
- disposition LF27, LF65–69 and LF75–78;
- parent errata 1–3;
- Codex LF1–3 and Claude LF15–22.

**DELTA1 is CANDIDATE ONLY (erratum 7 LF9–11): PASS,** with fix F3. Checked against:
- scope LF2–10;
- ack LF3 and LF95;
- cp-01 LF13–29;
- handoff LF8–12, LF59–65, LF136–138 and LF183;
- parent check LF3 and LF29;
- freeze LF2–35 and LF80;
- addendum v14 LF5;
- source-history erratum LF73.

**No every-avoider or full-Olson promotion: PASS.** See LF80, LF166, LF168, LF175, LF178 and LF184, and erratum 7 LF7 and LF11.

## 3. Erratum 7 versus older dated snapshots

- **HIGH-CORE.** Erratum 7 LF7 correctly supersedes the activity described at v12 LF184. The provisional check (17:13) left BIG-RUN as an open obligation; the written check LF9 closes it. Parent erratum 2's "candidate-level" wording is corrected by erratum 3. Reconciliation v1 LF12–26 gives destinations consistent with this.
- **DELTA1.** The 18:15 interim four-cell residual is historical (erratum 7 LF11, and source-history erratum LF7).
- **Still needed:** F2 and F3.

## 4. PartA Claude m7–m10 and U1–U4

**m7 – VALID; correctly disposed by the source-history erratum LF5.**
- The scope JSON numbering is: diagnostics LF11–24, success LF25, imports LF26, source_packet LF27, execution LF28, exposure LF32.
- Non-operative nit: ack LF54's "LF35-190" covers the locator objects; the array key itself is at LF33.

**m8 – VALID; disposed** by the last sentence of LF5, matching HIGH-CORE erratum 1 item 3.

**m9 – two parts:**
- (b) "18:0xPT": VALID; disposed at LF7. cp03 is at 18:11:53 (handoff LF136).
- (a) The interim LF9 list of necessary conditions omits HK1 HIGH-K-RES: VALID as a non-exhaustiveness point. LF8 answers a different question ("not used"). This is non-blocking because the interim residual is historical.
- **Contingent note C-1:** if DELTA1 fails its gates, the fallback residual must cite cp-01 LF27–29, not interim LF9 or UE-MP LF149–153. That list includes HK1 HIGH-K-RES and B.4 at (17,8).

**m10 – not a report defect;** its disposition overstates the sources (fix F4).

**U1 – RESOLVED (documentary).**
- The pasted LF counts equal the pins: D1-END verdict 9, erratum v1 10, erratum v2 13, disposition 59, RPdelta 50, RP2NE 33.
- So cp-01's extra line is a phantom +1. The RP-LIFT count is metadata only.

**U2 – RESOLVED for RP-2NE, D1-END and B-prime.**
- All three are stated over the same class: all-odd blocks, one nonzero pair, any B, no purity or B<κ condition, with A≥B as a WLOG normalization (RP2NE LF8–10; D1-END LF5; RPdelta LF13 and LF28).
- I.14's band A(p,1) is supported here only at the RPdelta-E1 statement level. REFLHI v5's own hypotheses are OUT_OF_SCOPE (D043).
- No operative acceptance depends on this, since DELTA1 is a candidate.

**U3 – RESOLVED.**
- Region B is κ=(p−1)/2−ε (RPdelta LF27).
- B.4 requires 1≤δ≤(p−12)/3 (LF29), so at δ=1 it applies only for p≥17.
- After B-prime and D1-END, only (17,8) remains (E5 LF89–90).
- The source-history erratum LF8 is correct.

**U4 – not disposed, but not load-bearing in this shard.**
- cp-01 used I.14 only through E1's A(p,1), with E1–E5 and the parent erratum read in full (cp-01 LF8–10 and LF15).
- RPdelta LF9, LF33 and LF40 make E1 the governing reading for δ≥1.
- Whether the REFLHI errata change anything belongs to the REFLHI shard or the DELTA1 math gate.

**D1-END disposition check (source-history erratum item 2): CONFIRMED** against the pasted body.
- The only mandatory erratum is v1 (LF10–15).
- The scope is "endpoint only" (LF55).
- not_covered (LF56) and the ledger (LF57) match verdict LF7.
- The counts (LF24, LF39) match verdict LF9.

## 5. Per-file fidelity (63; "rpt" = report v12 LF)

| # | Record | Map destination | Outcome | Basis |
|---|---|---|---|---|
|1|olson-BOTTOM-parent-verdict-v1.md|D015|PASS|LF5, LF9–15 ↔ rpt 94–105, 111 (p7 endpoint is R7)|
|2|olson-FC1023-first-family-parent-disposition-v1.json|D019|PASS|provisional, no credit (LF3, LF29) ↔ rpt 111|
|3|olson-FC1023-parent-verdict-v1.md|D019|PASS|premature headline ↔ rpt 111; see O-2|
|4|olson-FC1023-parent-verdict-v2-confirmation.md|D019|PASS|03:16:40 ↔ rpt 111|
|5|olson-FC1023-second-family-parent-disposition-v1.json|D019|PASS|p23 row closed ↔ rpt 99|
|6|olson-FC19-first-family-parent-disposition-v1.json|D020|PASS|↔ rpt 98|
|7|olson-FC19-parent-verdict-v1.md|D020|PASS|table LF17–30 ↔ rpt 98|
|8|olson-FC717-first-family-parent-disposition-v1.json|D021|PASS|↔ rpt 97|
|9|olson-FC717-parent-verdict-erratum-v1.md|D021 (v8 reading)|PASS|LF7–18 ↔ rpt 97|
|10|olson-FC717-parent-verdict-erratum-v2.md|D021|PASS|timing only; report makes no contrary claim|
|11|olson-FC717-parent-verdict-v1.md|D021|PASS|(7,17) ↔ rpt 97|
|12|olson-FCW-first-family-parent-disposition-v1.json|D022|PASS|↔ rpt 111|
|13|olson-FCW-parent-verdict-v1.md|D022|PASS|κ≥3, p=4κ−1; (3,11) ↔ rpt 84, 95|
|14|olson-FQW-first-family-parent-disposition-v1.json|D023|PASS|↔ rpt 111|
|15|olson-FQW-parent-verdict-v1.md|D023|PASS|LF5, LF9 ↔ rpt 96, 111|
|16|olson-HIGH-K1-complete-P-first-family-parent-disposition-v1.json|D024|PASS|↔ rpt 182|
|17|olson-HIGH-K1-first-family-parent-disposition-v1.json|D025|PASS|↔ rpt 182|
|18|olson-HIGH-K1-parent-disposition-v1.json|D026|PASS|330026 B, 15 bodies ↔ rpt 173, 182|
|19|olson-HIGH-K1-parent-verdict-v1.md|D027|PASS|LF7–16 ↔ rpt 175–180 (with erratum 3)|
|20|olson-HIGH-K1-second-family-parent-disposition-v1.json|D028|PASS|↔ rpt 182|
|21|olson-K0T-first-family-parent-disposition-v1.json|D029|PASS|its "K2 LF11" note is superseded by the verdict|
|22|olson-K0T-parent-verdict-v1.md|D029|PASS|↔ rpt 94–105, 109|
|23|olson-K2-parent-verdict-v1.md|D030|PASS|↔ rpt 111|
|24|olson-K3-parent-verdict-v1.md|D031|PASS|↔ rpt 84|
|25|olson-LOWER-K1-parent-verdict-v1.md|D036|PASS|↔ rpt 111|
|26|olson-P7L-first-family-parent-disposition-v1.json|D040|PASS|↔ rpt 94|
|27|olson-P7L-parent-verdict-v1.md|D040|PASS|LF9 ↔ rpt 88, 94|
|28|olson-PP1-EXCL-parent-verdict-v1.md|D041|PASS|↔ rpt 111|
|29|olson-R7-parent-verdict-v1.md|D042|PASS|↔ rpt 88, 111|
|30|olson-ROT-PP1-parent-disposition-v1.json|D017|PASS|↔ rpt 142|
|31|olson-ROT-PP1-parent-verdict-v1.md|D017|PASS|↔ rpt 142|
|32|olson-RUH2-parent-disposition-v1.json|D017|PASS|↔ rpt 140; see O-1|
|33|olson-RUH2-parent-verdict-v1.md|D017|PASS|↔ rpt 140; see O-1|
|34|olson-RUH3-parent-verdict-v1.md|D048|PASS|↔ rpt 84, 111|
|35|olson-SCW-first-family-parent-disposition-v1.json|D050|PASS|↔ rpt 111|
|36|olson-SCW-parent-verdict-v1.md|D050|PASS|↔ rpt 111|
|37|olson-TCW-first-family-parent-disposition-v1.json|D053|PASS|↔ rpt 111|
|38|olson-TCW-parent-verdict-v1.md|D053|PASS|↔ rpt 95, 111|
|39|olson-UFC-first-family-parent-disposition-v1.json|D055|PASS|↔ rpt 122|
|40|olson-UFC-parent-verdict-v1.md|D055|PASS|↔ rpt 99–100, 122|
|41|olson-UMR-first-family-parent-disposition-v1.json|D057|PASS|↔ rpt 122|
|42|olson-UMR-parent-verdict-v1.md|D057|PASS|↔ rpt 122|
|43|olson-UMR-second-family-parent-disposition-v1.json|D057|PASS|↔ rpt 122|
|44|olson-UPAR-parent-disposition-v1.json|D058|PASS|↔ rpt 100–101, 124|
|45|olson-UPAR-parent-verdict-v1.md|D058|PASS|↔ rpt 124|
|46|olson-UPAR2-parent-disposition-v1.json|D059|PASS|↔ rpt 127|
|47|olson-UPAR2-parent-verdict-v1.md|D059|PASS|↔ rpt 126–132|
|48|olson-UPAR3-first-family-parent-disposition-v1.json|D060|PASS|↔ rpt 136|
|49|olson-UPAR3-parent-disposition-v1.json|D060|PASS|↔ rpt 136|
|50|olson-UPAR3-parent-verdict-v1.md|D060|PASS|↔ rpt 130, 136|
|51|olson-UPAR4-first-family-parent-disposition-v1.json|D061|PASS|↔ rpt 152|
|52|olson-UPAR4-parent-disposition-v1.json|D061|PASS|↔ rpt 148–152|
|53|olson-UPAR4-parent-verdict-v1.md|D061|PASS|↔ rpt 148–152|
|54|olson-UPAR5-first-family-parent-disposition-v1.json|D062|PASS|↔ rpt 164|
|55|olson-UPAR5-parent-disposition-v1.json|D062|PASS|↔ rpt 164, 166|
|56|olson-UPAR5-parent-verdict-v1.md|D062|PASS|LF11 aside withdrawn ↔ rpt 159, 184|
|57|olson-USK-parent-verdict-v1.md|D063|PASS|↔ rpt 111|
|58|olson-terminal-frontier-v3-audit-parent-disposition-v1.json|D067|PASS|↔ rpt 88, 99–100, 353|
|59|olson-terminal-frontier-v4-audit-parent-disposition-v1.json|D067|PASS|"K1" read as LOWER-K1 ↔ rpt 88|
|60|olson-terminal-frontier-v5-audit-parent-disposition-v1.json|D068|PASS|↔ rpt 88|
|61|olson-terminal-frontier-v6-audit-parent-disposition-v1.json|D069|PASS|0F/1M/3m ↔ rpt 88, 136|
|62|olson-terminal-frontier-v7-audit-parent-disposition-v1.json|D070 (v8: LF115–117)|PASS|↔ rpt 115–117|
|63|olson-terminal-frontier-v8-audit-parent-disposition-v1.json|D071|PASS|↔ rpt 166|

## 6. OUT_OF_SCOPE items, unverified claims and limits

**OUT_OF_SCOPE (owned by other shards; not approved here):**
- The acceptance-boundary sentences at LF88, LF132 (end) and LF144 (D082).
- Theorem P's own records (D054). LF109 and LF180 are corroborated only at statement level, through HK1 erratum 3 LF5 and both complete-P reviews.
- REFLHI v5 (D043).
- KP2, KP3 and KP4 (D032–D034).
- RP-LIFT (D045).
- ASSEMBLY-LS and ASSEMBLY-P (D012/D013). These are used here as statement-level imports via BOTTOM LF9–14, scope addendum 2 LF12 and UPAR5 erratum v2 LF5–7.
- The D1-END, RP2NE and RPdelta records, which I used as imports only.

**Unverified (body not supplied; not load-bearing):**
- **LF154 "15:00stop/15:15handoff".** The source, control/written-olson-charge-failure-followon-v1.json (80d731b7…), is not supplied.
- **Deviation addenda v4, v7 and v12.** The claims at LF134, LF152 and LF182 are corroborated by frontier-v5 erratum v2 LF9, the v7 note LF30, UPAR4 verdict LF13, and HK1 verdict LF20 and LF24.
- **Frontier v2-erratum, v3 and v4 notes.** I re-derived the affected rows from the provider verdicts instead.
- **HIGH-CORE proof and handoff v2.**
- **DELTA1 parts, manifest and coverage.** What those packets actually contain is unverified here.

**Limits:**
- No DELTA1 mathematics was reviewed: it is a candidate, and no new math scope was assigned.
- No provider was re-proved transitively.
- The 218 source-pattern count is dated (reconciliation v1 LF9). Later DELTA1 and report verdict files are not covered.
- v11 is withdrawn, and no text in §4.2–4.7 depends on it.
- No human, Lean, priority, novelty, runtime or settlement claim is made.
- This return covers this shard only.
