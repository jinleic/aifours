DISPOSITION: DELTA=ACCEPT-WITH-FIXES; Q1=PARTIAL; Q2=PASS-WITH-FIXES; Q3=PASS; Q4=PASS-WITH-FIXES; Q5=PASS-WITH-FIXES

## FATAL
none

## MAJOR
none

## MINOR

**D-m1 — Producer-path identities are labelled "second-path".**
Lines: OVL:81, 86; LINK:19; VER:37–42, 90, 99–100; PROD:33, 38, 66, 79–81; RCPT:16, 18; RECIPE:13–19, 46–47.

- **What is actually second-path.** VER independently checks body bytes and order, the source header, the deleted and kept hashes, and the ALO name domains.
- **What is producer-path only.** These come only from PROD's `Formula` (PROD:33–40):
  - the F_one SHA and the header `p cnf 509915 5740226\n`;
  - all 16 leaf SHAs and the header `p cnf 509915 5740268\n`.
- **How VER handles them.**
  - VER compares `f.sha` with a hard-coded constant (VER:40).
  - VER recomputes leaf SHAs with the same function, `f.leaf_sha` (VER:90).
  - RCPT:16 and RCPT:18 are string literals (VER:99–100), not observed values.
- **Further gaps.**
  - VER re-reads DEL without hashing it (VER:42).
  - VER never compares the rebuilt recipe `r` (VER:37) with BASE_RECIPE.
  - RECIPE:13–19 files the Q1 KEEP record (index 5733728) under `"removed"`.
  - RECIPE:46–47 are hard-coded `True` (PROD:80–81).
  - CL1:89 asked for an independently streamed F_one SHA pinned beforehand; this was not done.
- **Why it matters.** Future solver and checker feeds must equal exactly these hashes (OVL:87–88). A `Formula` defect would pass VER. The mathematics is unaffected: PROD:33 and PROD:38, read directly, emit the correct bytes.
- **Correction.**
  - Reword OVL:86 to: "…bound all 16 unit lists to their supports via the pinned map; header bytes, F_one SHA and leaf SHAs were recomputed only by the producer's own `Formula` (same path)."
  - Recommended VER v2, using VER's own `hashlib`:
    - require sha256(`p cnf 509915 5740226\n` ‖ retained source lines) = 374d6fb4…;
    - for each case, require sha256(`p cnf 509915 5740268\n` ‖ retained lines ‖ `%d 0\n` units) = `cnf_sha256`;
    - assert sha(DEL) = 4509b3e7…;
    - assert BASE_RECIPE equals `r` plus the three `main()` fields;
    - read `"removed"` as "verified ALO records".

**D-m2 — Load-bearing identities are checked by no code and named in no gate.**
Lines: OVL:23–24, 29–30, 105–108; VER:65–66, 80–89; PROD:97–101.

- **Defect.**
  - T16 delivers "one of TPL's lists", but the refutations are of WMAN's units.
  - PROD copies SMAN's supports unverified.
  - VER derives units from WMAN's own supports, never from TPL:88–104.
  - The map and the name table are pinned by SHA only (VER:66, 81). Neither map `meta.cnf_sha256` nor the name table is bound to F.
  - F = GA(argv), the parent encoder binding, is absent from OVL:105–111.
- **Why it matters.** A mismatch would leave a genuine configuration in an unrefuted case. I checked by reading that there is none:
  - The 16 WMAN lists equal TPL:88–95 (for P0 and P1) and TPL:101–104, in case-id order.
  - GA's G1 loop (GA:141–144) creates g variables square-major and in lexicographic cell-pair order. This gives g_1((0,c),(i,0)) = 49c + 7i − 6 (row 2: 57…351; row 7: 92…386).
  - All 672 WMAN unit literals have the right id and sign under that formula. GMAPX agrees (aid only).
- **Correction.** Append to OVL:108: "WMAN supports_row2to7 equal TPL:88–95/101–104 verbatim; unit ids per GA:141–144; map meta cnf_sha256 = 6ecb77a7…, script_sha256 = bf1aada1…; F = GA(argv) and name table b8423861… per parent `binding-result.v2.json` dce638a9… (SEM:96–97)." Mirror these as VER v2 assertions.

**D-m3 — The TPL excision is incomplete.**
Lines: OVL:26–28; TPL:1, 4, 20, 59, 62–63.

- **Defect.** OVL excludes only TPL:111–113 and 117–120. These passages still route through reduced-K5 or old F:
  - TPL:20 says "by the accepted K5 SB2 normalisation".
  - TPL:59 justifies the moves via the reduced-K5 bridge (IMP:11–14, 72–74).
  - TPL:62–63 says "All reduced-K5/P4 properties are preserved".
- **Why it matters.** None of this is mathematically needed: the T16 hypothesis and OVL §2 replace it. But OVL:27 leaves the excision to the reader.
- **Correction.** Append to OVL:28: "T16 uses TPL:9–20 (20's justification replaced by the hypothesis supp Q1(1,0)=A), 22–55, 60–64 as made explicit by OVL §2 minus the 'All reduced-K5/P4…' sentence, and 66–109; TPL:1, 4–5, 59, 111–131 are not used."

**D-m4 — Gate 4 is not pinned to a predicate or a checker.**
Lines: OVL:109 (cf. CL1:66; RM:216–224, 413).

- **Defect.** "Self-exit/feed/proof-stream/hash/guard" names categories only. It omits the checker and its verdict line, the solver, and the requirement that both feeds hash-equal the case pin.
- **Correction.** Replace with: "16/16 receipts meeting RM:222–224 exactly:
  - both processes self-exited, with no guard trip and no relay error;
  - CaDiCaL 3.0.1 exit code 20 with `s UNSATISFIABLE`;
  - drat-trim d834b649… exit code 0 with a line equal to `s VERIFIED` after stripping `\r`, and no `s NOT VERIFIED`;
  - solver-feed and checker-feed SHA-256 both equal to that case's WMAN `cnf_sha256`;
  - proof-stream SHA and byte count recorded;
  - runner 268e743b… (RM:413)."

**D-m5 — Wording and pins.**

- **OVL:18.** In the column-0 frame the vectors are not aligned across squares. Disjointness comes from Prop 1 on the cell pair ((0,k),(i,0)), which is frame-free. The text should say so.
- **OVL:48.** "Prefix equality" should say *inclusive*.
  - GA:262–269 define lexeq(i,k) ⇔ v_i[0..k] = v_{i+1}[0..k], and the k = 0 unit forces lexeq(i,0) = ⊤.
  - GA:256's comment uses the exclusive [0..k−1] convention for `e_prev`.
  - The two-way clauses force a unique value, so Q3 is unaffected.
- **OVL:11, 93, 102.** Use full pins:
  - SEM 413951379f248a87e02b52dfb942fb131f25524557c35adf9c54f68981b31022;
  - PV 919daeac811bd551c4165ba415f9c6835b564adcb9bb6fcde1969307f2caa8f9.

## Answers

### Q1 — PARTIAL (8 closed, 2 partial, 0 open; nothing reopened)

| CL1 MINOR | Verdict | Where |
|---|---|---|
| BR2 m1 | closed | OVL:52–57 |
| BR2 m2 | closed | OVL:61–65 recasts the claims as reported inspection plus obligations; receipt at OVL:81–88. Labelling residue → D-m1. |
| BR2 m3 | closed | OVL:13–30. Residue → D-m3. |
| BR2 m4 | closed | OVL:34–38 |
| BR2 m5 | closed | OVL:92 |
| BR2 m6 | partial | OVL:94–97 and 105–114 add SRC, Lemma 10, the parent-T16 gate and the conditional consequent. "Strict drat-trim VERIFIED" is still unpinned → D-m4. |
| BR2 m7 | closed | OVL:43; 38/42; 48–50; 24; 99–101 |
| DEL m1 | closed | OVL:61–63 plus RCPT |
| DEL m2 | partial | See note below. |
| DEL m3 | closed | OVL:67–73. VER:45 and VER:50 enforce "header on line 1, no comment or blank lines". |

**DEL m2 note.** OVL:62–64 recasts `other_clauses` as an obligation.
- CL1:86–90 items 1, 2, 4 (body) and 5 (units) are checked on a second path.
- Item 3, item 4 (the SHA) and the leaf SHAs are producer-path only (D-m1).
- Items 6–7 are correctly left as obligations (OVL:87–88).

**Nothing reopened.**
- OVL:35 follows SEM:56–61, not IMP:67.
- OVL:41 follows SEM:78–79.
- OVL:108 follows SEM:51–52.
- OVL:102–103 import ENC §§2, 4–5 (all-QLS), not ENC §6 (reduced-class P4).

### Q2 — PASS-WITH-FIXES

**Verified by reading.**
- **Degree bounds (TPL:9–19).** OVL:17–19 is a derived fact, not an extra hypothesis.
  - Prop 1 on cell pairs gives disjoint supports without needing alignment.
  - Collinearity with (0,0) removes index 0, so each support has size ≤ 7 − 4 = 3.
  - U[0,0] = 1 uses Q1(0,0) = |0⟩.
- **Component theorem (TPL:31–55).** All steps hold:
  - singleton-intersection rule;
  - rank balance;
  - K22 and K33−e closure ("w must touch the same z");
  - K32 excluded;
  - 3+3 versus 2+2+2;
  - x = y = z giving K44−M.
- **Coverage.**
  - Column 1 has degree 3, so its component is P0, P1 or P2, on A or A∪{b} with b ∈ B.
  - The pure-B block has 6 types in dimension 4 and 4 in dimension 3, giving 16 in total.
- **Moves.**
  - σ permutes only the coordinate rows of U: U′[σ(k),i] = U[k,i].
  - Every list is reachable by Sym(A)×Sym(B) plus the row sort.
  - TPL:106–109 gives valid representatives; minimality is not needed.
- **ROWLEX order.** Every list is non-decreasing in the GA:253–269 key (coordinate 0 most significant, False < True).
  - Pure-B entries precede A-meeting ones because the first difference falls in {1,2,3}.
  - Examples: 23 < 123; 234 < 134 < 124; 567 < 467 < 457 < 456; 7 < 56 < 456; 67 < 567.
- **Hypotheses preserved.** Alignment (OVL:34–35), SB2 after ρ (OVL:37) and rows 0–1 (OVL:38).
- **No hidden reliance** on reduced-K5, on P4 for squares 2–5, on non-classicality, or on c112. All 16 cases are `run_required` (WMAN:97…1347).
- **No list is missing or wrongly canonicalised.**

**Reported provenance (not a premise).** The nauty and orbit controls (RM:356–363; WMAN:12–20).

**Fixes needed:** D-m2, D-m3.

### Q3 — PASS

**Verified by reading GA.**
- **Inactive code.** With CL = [], GA:100–149 emit nothing; G1 only creates the g variables.
- **Clause families.**
  - G2 (150–153) holds by Prop 1.
  - G3 (179–190) holds by unitarity: rows and columns nonempty, and "not exactly one" via b3.
  - G4 (191–206) holds by Parseval with one term or zero terms, including the case where gpq is constant ⊥.
  - G5 (207–232) is the same-ray condition, with u5 exact.
  - Constant folding (51–76) agrees with the true constants, and memo names fix the operands.
- **P4.**
  - w3_1(0,(1,0)) = ⊤ satisfies its 28 clauses and the kept ALO: ov_0 is constant ⊥, and every 6-subset meets {1,2,3}.
  - Every other flag = ⊥ satisfies its one-way clauses.
  - w3 occurs positively only at GA:247.
- **ROWLEX/lexeq (248–270).** Sorted keys satisfy all 38 clauses per pair, including the lexeq(i,0) unit.
- **Units.** SB2 (271–281, 35 units) holds by normalisation, and the 42 template units hold by T16.
- **Deletion indices re-derived.** The tail is 190 + 35 clauses and each block is 1569. This gives 5740004, 5738435, 5736866 and 5735297, with Q1's keep at 5733728 (DEL:12–17).
- **Soundness.** Deleting exactly the four ALOs is sound for arbitrary squares 2–5, and nothing else is needed. SB2's weight-1 requirement at (1,0) is compatible with classical squares.

**Reported provenance.** Only F = GA(argv) (ENC:43–46).

### Q4 — PASS-WITH-FIXES

**Second path (VER's own logic):**
- source SHA and no CR (43);
- exact source header bytes (45);
- 5,740,230 lines, each ending `" 0\n"`, with no comment or blank lines (50, 61);
- the four deleted hashes at the DEL indices (52–54);
- Q1's keep hash, and that the line is retained (58–60);
- every retained line equal and in order, with no suffix (56, 61);
- the name-table pin and the five 56-flag domains (65–77);
- units re-derived from supports via the pinned map, in i = 2..7, c = 1..7 order (80–89);
- 16 unique ids, plus `cnf_clauses` and `run_required` (79, 91).

**Producer path only:**
- the F_one SHA and the `…5740226\n` header (PROD:33; VER:40);
- the leaf SHAs and the `…5740268\n` header (PROD:38; VER:90);
- the DEL pin (PROD:45);
- the RECIPE fields.

**Not checked by any code:**
- WMAN ↔ TPL list identity (I verified it by reading);
- map and name table ↔ F (provenance only; I verified the numbering statically);
- one clause per line (GA:309);
- WMAN header fields (WMAN:5 matches by reading).

**Byte counts verified by reading.** 4 × 394 = 1576 (RECIPE:45). 137664569 − 21 − 1576 = 137662972 (RECIPE:7, 12).

**Claim scope is correctly limited** (RCPT:21; OVL:87–88; LINK:2, 20–21).

**Reported provenance.** That VER actually ran at 00:04:37 (RCPT:2). RCPT:3 equals VER's SHA.

### Q5 — PASS-WITH-FIXES

**Verified by reading.** Classical sets need nothing. For a non-classical S, the chain runs:
1. Per-square standardisation (SRC:222, 287–289).
2. The A8 contrapositive (gate 1; five squares, all entries: PV:13, BR2:38–39, OVL:94) together with W8 gives a weight-3 entry.
3. BR2 §3 plus OVL §2 establish the T16 hypotheses.
4. T16 applies (gate 2).
5. The OVL §3 assignment satisfies the pinned leaf (gate 3).
6. This contradicts the refutation (gates 4–5). Gate 6 is procedural.

**Scope.**
- Only pairwise-orthogonal QLS are required; squares 2–5 may be classical.
- The consequent is correctly the SRC:642 case, n − 3 = 5 (OVL:97, 114).
- Lemma 10 inside A8 is included (OVL:95, 106), as is the parent gate on T16 (OVL:107, 111).

**Missing explicit items.**
- D-m2: the encoder, map and name-table binding, and WMAN = TPL.
- D-m4: the strict predicate and checker.

With those added, the six gates are sufficient.

DELTA FATAL=0 MAJOR=0 MINOR=5
