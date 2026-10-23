**Scope:** v4 LF1–187 checked against the eleven pasted files only. This covers report-to-record consistency. Theorem validity is UNASSESSED. No Lean, human, novelty, priority or full-problem certification is given. Hashes are used only for bookkeeping: all seven SHA256 values v4 gives for pasted files (LF86, 100, 102, 160, 185×3) match the pasted headers.

**Counts: FATAL 0 · MAJOR 0 · MINOR 15**
- **m1–m12 (12):** new findings in v4's own text.
- **p1–p3 (3):** already dispositioned by errata recorded after the v4 snapshot. v4 was frozen at 05:59:19; those errata are timed 06:01:07 and 06:02:10, so v4 could not carry them. They must go into v5.
- **Sigma: no flag.** LF111 and LF187 are scoped to the snapshot, and v4 claims nothing past 05:59:19.

## (a) Incorporation of recorded findings

| Required item | v4 LF | Result |
|---|---|---|
| CFR k≥4, stated as substantive | 137 | ✓ matches claims erratum §1 |
| GB "recorded qualification" language | 98, 100, 158 | Partial. §5.1 ✓; LF158 → m4; LF100 blurs raw receipts and parent audits → m5 |
| B2.M4 cap stop vs B2.M2/B3.M2 budget UNKNOWN | 98 | ✓ 3592.626s, 339.265s, 6442532864 > 6442450944 by 81920B, one SIGTERM, no VERIFIED/consumed count. Missing the not-backfilled-predicates clause and the GB prefix → m3. The 0.632091s figure appears only in appendix LF323; acceptable. |
| v5d pre-window, quoted not reproduced | 102 | Times, 408.512s, pre-window and "unexplained" ✓. "Not reproduced" wording ✗ → p2 |
| 15/18 attributed, with conditional bridge | 13, 98 | "recorded" ✓; import/bridge limit ✗ → m2 |
| Observer 23:12:04 vs 23:12:27; no fresh census | 160 | ✓ |
| Contractual cutoffs vs internal targets | 26–32 | ✓ (row-label nit only) |
| UH-A/UMR/classical imports retained after P gate | 76 | ✓ |
| WH5C2: 120 equations, separate 120 inequalities | 123 | Content present, but the sentence can be parsed wrongly → m10 |
| K1 means LOWER-K1 | 68–74, 78 | ✗ → p1 |
| T_PAR exact; coarse ranges/Lemma5; no 6d−4; (10,23) not corroboration | 86, 90 | ✓ |
| RUH3/UH-CONSTRAINTS named; UPAR promoted only via timestamped frontier | 58; 62/90 | ✓ (provenance issue → m7) |
| Interim, not complete; v3 Claude prompts UNLAUNCHED | 3, 181, 187 | ✓ |

## MINOR findings in v4 text

- **m1 · LF13 (column header LF9 "Established in this window")**
  - Issue: "GA18/18, GB15/18" are cumulative totals. LF96 records admission at GA16/18 and GB1/18.
  - Repair: "GA 16→18/18, GB 1→15/18 recorded exact strengthened-input closures (cumulative; §5.1)".

- **m2 · LF13, LF98**
  - Issue: the 15/18 figure is not tied to its import limits (appendix LF111/201; erratum v2 §3).
  - Repair, after "…to 15/18.": "This is an attributed record total. Each closure is exact for its strengthened input only. It does not imply base-formula UNSAT, shared representative-set imports are not verified by the proof bytes, and the genuine-configuration bridge remains a conditional import."

- **m3 · LF98**, three repairs:
  - (i) "no unchanged retry authorized" is narrower than every record (appendix LF23, 245, 314, 456) and invites a modified retry. Use "no retry, F2, cap or budget increase is authorized".
  - (ii) The bold "B2.M2 and B3.M2" share IDs with the closed GA items in LF96. Prefix them with "GB P1-".
  - (iii) Add: "their deliberately unstarted checker-stage predicates remain false, not backfilled" (appendix LF454, 469).

- **m4 · LF158** "separately recorded source-reviewed/qualified GBv7 exception"
  - Issue: no pasted file attests "source-reviewed". The recorded residual risk is also omitted (appendix LF7; erratum v2 §3).
  - Repair: "A GBv7 exception — historically recorded as controls-only admission, then per-item GO, with recorded control qualification, not re-qualified here; recorded residual risk: the launcher's unbounded final wait for its driver — ran…"

- **m5 · LF100** "recorded parent-audit/receipt facts"
  - Issue: erratum v1 §3 requires raw receipts and parent audits to be distinguished. All six appendix entries are parent audits; the LF96 GA figures come from a raw receipt.
  - Repair: "These are parent-audit records, not raw receipts (LF96's GA B2.M2 figures come from a raw receipt not reproduced here)…"

- **m6 · LF54**
  - Issue: diverges from the governing antecedent (UPAR verdict LF5; frontier v4 LF5). v4 says "extra reflection-pair placement" where the sources say "arbitrary extra pairs". It also drops "rotation-pair" from the no-added-premise list, which matters given the RP-*/ROT-SING names in LF58.
  - Repair: "Arbitrary extra pairs in odd blocks and the genuine empty-run rule remain. No o_F, nonempty-run, rotation-pair or rigidity premise is added."

- **m7 · LF62**
  - Issue: the LF64–74 table is attributed to frontier v3. Rows LF72–74 actually carry UPAR cells from frontier v4-UPAR, whose binding audit was still pending (LF90, 187).
  - Repair: "Rows p≤23: frontier v3 with its erratum/audit. Rows p=29, 31, 37: olson-terminal-frontier-v4-UPAR.md (SHA256 285bb751…), union-binding audit pending at this clock."

- **m8 · LF86** "closes (12,29),(13,31)"
  - Issue: this reads as exhaustive, but LF74 credits UPAR for 15 at p=37. (15,37) is not in T0 (⌊116/8⌋=14) and 5·15=75≤76, so UPAR also closes it.
  - Repair: "newly closes every T∖T0 cell with 5κ≤2(p+1) — e.g. (12,29), (15,37), (19,47) — plus listed (13,31)".

- **m9 · LF90** "all seven named cells"
  - Issue: no seven-cell list exists in v4 or the pasted sources. v4 shows 4 open cells through p=37; frontier v4 shows 13 through p=47.
  - Repair: list the seven (κ,p) cells, or cite the frozen UPAR2 file with its SHA256.

- **m10 · LF123**
  - Issue: "additionally requires 120 strict inequalities, antiunitary coupling and Kramers triangle obstruction only when ALL 3 maps…" can be parsed so that the 120 inequalities apply only in the WH-type case. That contradicts claims erratum §3.
  - Repair: "(H) is equivalent to 120 real equations. Obtaining 100 distinct rays additionally requires 120 strict inequalities, which are not part of H. Separately, the antiunitary-coupling/Kramers-triangle obstruction applies only when all three maps have the specified WH type. Specified MUB-pair representative planes are excluded in H at any cardinality."

- **m11 · LF121**
  - Issue: the ambient dimension is not stated. A rank-2 projector with constant diagonal δ in C^d satisfies dδ=2, so "diagonal 2/5" forces d=5.
  - Repair: state the space. If the plane is in C^10, the constant must be 1/5.

- **m12 · LF62, 88, 90, 152, 158**
  - Issue: these cite authorities without SHA256 while every other authority carries one. They include the UPAR erratum (69374d07…) and frontier v4 (285bb751…).
  - Repair: add the hashes. LF177 already lists the link/evidence check as pending.

## MINOR findings from post-snapshot errata (carry into v5)

- **p1 · LF68–74 "1K1", LF78 "K1/K2"**
  - The frontier-v4 erratum binds K1 to LOWER-K1 and requires the full spelling.
  - Repair: "1 LOWER-K1" in the rows; "LOWER-K1/K2 are p≥11" in LF78.

- **p2 · LF102**, per erratum v2 §1
  - Replace "extracts the original receipt:" with "is a parent metadata extraction (a parent record, not model review); the pinned v5d receipt records … UNKNOWN — pre-window; this report does not independently reproduce the receipt body."

- **p3 · LF100** "actual per-attempt audit measurements", per erratum v2 §2
  - Repair: "the three PASS audits reproduce numerical feed and proof counts/hashes; the UNKNOWN audits record the applicable feed/identity criteria, and the extract does not reproduce numerical feed/hash measurements for every attempt."

## (b) New overstatement

Nothing reaches MAJOR or above.
- **Permissive or overbroad wording:** m1, m3(i), m4, p3.
- **Mis-scoped or understated (not overstatements):** m6, m8, m10.
- All other §3–§9 scope sentences keep the limits stated in the pasted sources.

## (c) Internal consistency (re-derived)

**Partitions**
- All 9 rows in LF66–74, plus frontier v4's rows for p=41/43/47, are disjoint, complete partitions of {0,…,p−1}.
- Every provider entry matches the formulas in LF78/84/86. Key cells:

| p | T | T0 bound | UPAR bound | Open |
|---|---|---|---|---|
| 23 | {8,9,10} | ≤9.5 | (10,23) listed only (50>48) | none |
| 29 | {10..13} | ≤11.5 | ≤12 | 13 |
| 31 | {10..14} | ≤12.5 | ≤12.8, +13 listed | 14 |
| 37 | {12..17} | ≤14.5 | ≤15.2 | 16, 17 |

- At p=17/19, UFC and UPAR would also cover κ=7 and κ=7–8, but the rows credit FC717/FC19. Because each cell gets one provider, this is not a conflict.

**LF90 strip formula is exact for every prime p≥29**
- The lower providers meet T's lower bound contiguously in both residue classes:
  - p≡1 mod 4: USK, then SCW at (p+3)/4, then FQW at (p+7)/4.
  - p≡3 mod 4: USK, then FCW at (p+1)/4, then TCW at (p+5)/4.
- T0 lies inside the UPAR region, because (3p+5)/8 ≤ 2(p+1)/5 ⇔ p≥9 and (3p+7)/8 ≤ 2(p+1)/5 ⇔ p≥19.
- BOTTOM starts at (p−3)/2+1, so nothing is missed at the top of the strip.
- With d=(p+1)/2−κ, κ≤4d ⇔ 5κ≤2(p+1).
- The family κ=3d+4, p=8d+7 returns the same d and lies inside the region for d≥4. So (13,31) is the only off-region cell for p≥29.
- The same formula gives empty strips at p=17 and 19, and {10} at p=23 (removed by the listed cell). This matches the rows.

**CFR k=3 counterexample**
- Under the reading "rows j↦0, cj, −cj over Z21 with gcd(c,21)=1", these rows form a (Z21,3;1) difference matrix.
- χ=(1,1,1) then has Σχ=0, a constant combination, and support 3<6, as the erratum states.

**Arithmetic**

| Check | Result |
|---|---|
| B2.M4 cap overshoot | 6442532864 − 6442450944 = 81920 |
| B2.M4 sample split | driver 2255110144 + checker 4187422720 = 6442532864, equal to checker maxrss |
| B2.M4 timing | 3592.626 + 339.265 = 3931.891 vs pipeline 3932.884 |
| Ledger nodes (LF44) | 59 = 8 + 1 + 6 + 44 |
| Row1 cells (LF108) | 22 = \|row0 ∪ col0 ∪ row1\| in an 8×8 grid |
| FCO enumeration (LF120) | 362880 = 9! |
| PA19 field (LF131) | 70 + 58 = 128 |
| LemmaU (LF139) | 190 − 185 = 5; 3^5 = 243; 2·243 = 486 |
| RQLS assays | 2048/256 = 8; 1536/24 = 64 |
| GB coverage | 12 + 3 = 15; per-audit 14/14/15/15 is consistent with the B5.M2 PASS falling between |

**Timestamps**
- GB solver start times (reap time minus wall time): 06:19:16, 07:14:22, 07:47:37, 08:54:57, 10:07:43, 10:44:10.
  - All are after the 06:16:35 controls release and none overlap.
  - Each checker starts within 0.9s of its solver's reap.
  - The last reap (11:44:10) is before the final disposition at 11:46:07.
  - Epoch fields agree with the PT clocks, e.g. 1792418108.8 = 06:55:08 PDT.
- v5d: 09:19:03 + 408.512s = 09:25:51.5. That is 13h37m before the 22:56:33 authorization.
- Deadlines: authorization + 96h, then −2h, −1.5h, −1h and −5min. All are in the future at the snapshot.
- Every cited pasted file is timed 05:42:23–05:57:36, before the snapshot. The two later errata are correctly not cited.

**Counts and cross-references**
- LF187 matches the disposition's audit counts; LF88 matches the UPAR verdict's LF11.
- LF34 "below" resolves to §9; LF158 resolves to the GB appendix; erratum v2's "section 5.1" is LF94–111.
- The only cross-reference defects are m7 and m9.

## Unverified load-bearing dependencies (flagged, not counted)

- **U1 · LF18, LF58:** the authority index v1 and addendum v2 are declared to *govern* the exact statements and imports. The §4.1 name list, "101 files", and the Lev2022/S(p) trust all rest on them.
- **U2 · LF166–168:** the deviations appendix is declared *integral*. Nothing here verifies "every 56 … 16 lane documents", the six intervals (which sum to 76,124s ≈ 21.1h) or the "058 −31s" anomaly. The antecedent of "the same" is also dangling.
- **U3 · LF7, 11, 38–50:** the headline Sun(7) result is attributed only. Only the 59-node count is checkable.
- **U4 · LF76, 78:** the TheoremP closure verdict, LOWER-K1/K2, and the FC1023 03:16:40 confirmation. The scope of the P closure is corroborated by claims erratum §2.
- **U5 · LF96, 98:**
  - The GA receipt figures (137665034B, 455119925B) are unverified.
  - The GB 1→12/18 "direct inputs" path is unverified; the appendix covers only 12→15.
- **U6 · LF22, 162:** the contract file. The cutoffs are corroborated by erratum v1 §4; the resource ceilings are not.
- **U7 · LF100:** the GO and release contents of the binding packet. The chronology is corroborated post-snapshot by erratum v2 §3.
- **§5.2, §6, §7 numeric and source claims:** only their internal arithmetic is checkable.

## Nits (not counted)

- **LF28/29/32:** add "Contract:" labels.
- **LF137:** "necessary" → "cannot be weakened to k≥3", since the conclusion is vacuous for k≤2.
- **LF120:** "composite odd p" → "n=2m with m odd composite".
- **LF171:** → "PAR-COVER over the complete necessary residual R_PAR remains unproved".

## Evidence-file observations (not v4 defects)

- **O1:** Erratum v2 §2 says the B2.M4 audit reproduces proof collected/fed numbers. The pasted appendix extract (LF259–330) has no proof block, so cite the full audit for those numbers.
- **O2:** The appendix calls its entries "literal" (LF23), but they are selected-field extracts. B5.M2 lacks the item/scope fields and B3.M2 lacks the formula identity.
- **O3:** The UPAR verdict's cell lists (LF7, LF9) are non-exhaustive: they omit closed (15,37) and open (16,37). v4 LF90's open list is the correct one; LF86 inherited the incomplete closure list (m8).
