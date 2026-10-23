# SUN7-COMP U0: hostile mathematical review

**Reading applied:** COMP v1, then erratum-v1 P1–P5, then erratum-v2 Q1–Q4, then the parent erratum U0-v1 items 1–3. The parent erratum governs. The overlays touch disjoint lines (COMP:108, COMP:115 and IDX:158 against the v1/v2 locations), so their order does not change the result.

**Method:** no tools were used, and nothing was executed or edited. Each step below was re-derived from the supplied excerpts. Hashes were cross-checked between the supplied texts only; I did not recompute them. (H-NF) and (H-A2X) were checked at their interface only.

**Result: the conditional theorem is valid as stated. FATAL 0, MAJOR 0, MINOR 14.** No finding changes a statement, case split or proof step of CE-LIFT, COVER, K7-SPLIT or T.

**Legend:**
- COMP = `SUN7-COMP-v1.md`; EV1, EV2 = its errata v1, v2; PE = parent erratum U0-v1
- RUL = gate ruling 4818f1ca; IDX = `review-index-COMP-v3.json`; PKG = `review-package-COMP-v3.md`
- RM = O16 README; WV = written verdict 73a25ba6; SB = StageB verdict; X1V = X1 verdict; ADD = `rules-k7-addendum-v1.md`
- K62V = K6.2* verdict; K62F = `K62-FULL-v1.md`; K63RV = K63-RES verdict; R2V = R2 verdict
- NF = `K7-NF-v1.md`; A2S = A2 scope; U3 = A2 unit 3; S5V, S6V = Sun(5), Sun(6) verdicts

## 1. Claim-by-claim

| # | Claim (after overlays) | Verdict |
|---|---|---|
| 1 | CE-LIFT, COMP:24-28 | CORRECT. R0 (RM:29) preserves n_i, every [G:U_i∩U_j] and disjointness in G/N; no frame or cap is used. |
| 2 | COVER, COMP:30-48 | CORRECT. Exhaustive and pairwise disjoint (§2). |
| 3 | KII, K5.2* by SB:5 (COMP:53) | CORRECT at literal scope. The K52 universe over-covers K5.2* (SB:20); KII matches the README class (SB:26). Overlays: F3. |
| 4 | K5.3 by ADD:159 + X1V:5 (COMP:54, P1) | CORRECT. StageA is not used. DAG issue: F2a. |
| 5 | K6.2* by K62F:241-243, K62V:9 (COMP:55) | CORRECT. K62F:17-24 is equivalent to RM:92 plus P0/P1. |
| 6 | K6.3 by K63-D:24, K63-E:19, K63-RES:42-43 (COMP:56) | CORRECT. Exact partition; K63RV:5 agrees. Overlays: F3. |
| 7 | Lemma K7-SPLIT, COMP:61-78 | CORRECT, proved in full. |
| 8 | (H-NF), (H-A2X) as stated, COMP:82-86 | CORRECT. Verbatim with NF:84-86 and U3:143-144. F matches NF:85 ("Equivalently…") and the resumption json line 12. Excerpt gap: F4. |
| 9 | Theorem SUN7-COMP and proof, COMP:87-94 with Q4 | CORRECT as a conditional theorem. |
| 10 | Remarks (1)-(3), COMP:95-97 | Not load-bearing. Wording issues: F1, F11. |
| 11 | DAG and acyclicity (COMP:99-122, P3, PE 1-2, IDX:157-170) | Acyclicity CORRECT. Edge and overlay lists incomplete: F2, F3. |
| 12 | Computation boundary (COMP:124-134, P4, Q3, PE 3) | CORRECT: load-bearing exactly N2, N3, C1; StageA not. Precision issues: F5, F6. |
| 13 | Gates and obligations against RUL (COMP:136-152, Q1, Q2) | CORRECT in substance. Exactness issues: F7–F10. |
| 14 | No unconditional Sun(7) | CORRECT: COMP:1, 9-11, 87-89, 165; Q4; IDX:26, 192; PKG:18. |
| 15 | EV1 P1–P5 | P1 (…a0c9 = X1V:12), P2 (…f966) and P5 CORRECT. P3 except "N0 imports nothing" (F2f). P4 subject to F2e. |
| 16 | PE items 1–3 | CORRECT: RM:19 hypotheses; N1 is external; the Sun(6) sentence is at K63RV:18. Item 2 should also add N4 (F2b). |

## 2. Re-derivations

**COVER.** By P0(c), each pair's prime set P_ij is one of {2}, {3}, {5}, {2,3}.
- **a ≥ 3:** by P1(ii) some x ∈ A_5 lies outside A_2∪A_3. That forces every vertex into A_5, so every gcd is 5, and any six vertices contradict Sun(6).
- **a = 2:** each 5-vertex has a neighbour outside A_5, so it lies in A_2∪A_3. P1(ii) rules out both 5-vertices in A_2, both in A_3, and either in C. Hence x ∈ A_2∖A_3, y ∈ A_3∖A_2 and C = V∖{x,y}. This is KII (RM:96).
- **a ≤ 1:** a gcd of 5 is impossible, so Sun(5) puts a C-pair in every 5-set and |C| ≥ 4. Every vertex of D lies in A_2∖A_3, or every vertex lies in A_3∖A_2.
  - |D| = 0: K7.
  - |D| = 1, type 3: K6.3.
  - |D| = 1, type 2: either every d–C gcd is 2 (removed by D2), or some gcd is 4. Then d and that i are in E, and P1(iii) gives C∩E = {i*}: K6.2*.
  - |D| = 2, type 3: K5.3.
  - |D| = 2, type 2: R1b gives D ⊆ E. Then C∩E = ∅ is removed by D2′, and C∩E = {i*} is K5.2*.
  - |D| = 3: removed by R1a (Sun(4)) or by R1b+R1c (Sun(3), Prop 4.5).
- The leaves differ in a, |C| or type, so they are disjoint.
- Exponents enter only through E, which is split exhaustively. Index 1 is excluded by P0(a). Infinite groups enter only through CE-LIFT.
- So no branch, marker placement, group type or index pattern is uncovered.

**K7-SPLIT.**
- In K7, n_i = 6r_i with the r_i pairwise coprime. So Z = E, T = {i : f_i ≥ 2} and P = A_5 each have at most one element.
- Outside F, (H-NF) applies.
- Inside F, Z = {z} ≠ {t} = T, so 3 ∤ r_z and 2 ∤ r_t.
  - If P ⊆ {z,t}, this is exactly R2V:9 (a1). Bz·Bt = 0 holds automatically and W is unmarked.
  - If P = {p} with p ∉ {z,t}, this is exactly A2S:14-17 (a2).
- Both (a1) and (a2) lie in F, because E, A ≥ 1 force Z = {z} and T = {t}.
- They are disjoint because z, t and P are determined by the configuration.
- So K7 = (K7∖F) ⊔ (a1) ⊔ (a2), every 5-placement included. The "third 5-vertex" excluded at R2V:9 is exactly (a2).

**K5.3 bridge.**
- e_d = 0, so r_d = n_d/3 is odd.
- gcd 3 on the D–D pair gives gcd(r_d, r_d′) = 1.
- gcd 3 on a D–C pair gives 3·gcd(r_d, 2r_c) = 3, so gcd(r_d, r_c) = 1.
- gcd 6 on C–C pairs gives coprime r_c.
- Deleting down to both D-vertices and any three C-vertices gives exactly the X1V:5 hypothesis.

**K6.3.**
- e_d = 0, so a 2-marker can only lie in C.
- The three cases are: f_d = 1; f_d ≥ 2 with no C-vertex having e ≥ 2; f_d ≥ 2 with some C-vertex having e ≥ 2. They are disjoint and exhaustive.
- In the third case, P1(iii)–(iv) force exactly the setting at K63-RES:23-29.

**K6.2\*.**
- RM:92 with P0/P1 yields every clause of K62F:19-21, and conversely: f_d = 0; e* ≥ 2 and f* ≥ 1; e_c = 1 on O; min(e_d, e*) = 2 from the gcd of 4; at most one vertex with f ≥ 2 and at most one with h ≥ 1; coprime w's.
- K62F:22-24 lists every marker placement that P1 allows. The 3-marker cannot sit on d.

## 3. Findings (all MINOR)

**F1. Provenance of "Lemma MK"** (COMP:95-96, COMP:117; IDX:166)
- NF's own (a1)/(a2) split (NF:126-127) cites "Lemma MK", which is not among K1's listed imports.
- "MK" is also the name of a *pending* packet at K62V:23.
- T is unaffected, because K7-SPLIT re-proves the marker facts without MK.
- **Repair:** state MK's source in the K1 row (internal to K7-NF, or an accepted node with its hash). Reword Remark (1) to "per its own text; unverified here".
- If NF's theorem proof does import the pending MK, add MK to the §8 obligations. That would be a MAJOR against §8, not against T.

**F2. Missing direct-import edges.** None of these creates a cycle.
- **(a)** C2 (COMP:113; IDX:162) lists only N0 and the X1 verdict. The bridge is N5 text (ADD:159), accepted at WV:24, and it uses the K5.3 class definition from N6. T (COMP:120) also omits N5, although its proof (COMP:91) uses the bridge. **Repair:** add N5 and N6 to C2's imports, and WV:24 to its acceptance column.
- **(b)** N2 (COMP:106) omits N4. Sun(5)'s exceptional branch (2r1,4r2,4r3,4r4) is proved in v4 §2 (S5V:18). **Repair:** make it (N0,N1,N4)→N2, which also amends PE item 2.
- **(c)** K2 (COMP:118) and K3 (COMP:119) omit N1. R2V:46 records direct Sun(2)/Sun(3) uses, and K3's own computation cell says "direct Sun(2)-(4)". **Repair:** add N1 to both.
- **(d)** N7's imports are N0–N3, N5 at COMP:111 but N0..N5 at IDX:160. **Repair:** reconcile the two.
- **(e)** C4 (COMP:115) and P4 say N3 enters "through N7". COMP:128-129 lists K63-RES's Sun(6) use separately from "LFC applications with six pieces". **Repair:** if K63-RES applies Sun(6) directly, add N3 to C4 and amend P4; otherwise merge the two uses.
- **(f)** COMP:104 and P3 say "N0 imports nothing", but RM:21 takes the L0 proofs from sun-coset5 rules-v1 L0. The N0→N2 edge also has Sun(5) importing k7-only CE/P0/P1. **Repair:** add an elementary root node "L0/R0 (sun-coset5 rules-v1 L0)" imported by N0, N2 and N4.
- With all edges added, a topological order still exists: {L0, N1} → N0 → N4 → N2 → N3 → N5 → N6 → N7 → {C1–C4, K0–K3} → T.

**F3. Incomplete mandatory-overlay lists** (COMP:53, COMP:56, COMP:112, COMP:115)
- K63RV:10 records an "Overlay X1-X8" that disposes every K63-RES finding. COMP lists only errata v1–v2.
- SB:5 binds the written verdict's whole mandatory overlay (items 1–9, WV:44-54). COMP lists only F-2/F-3/F-4.
- The statements actually used are unaffected.
- **Repair:** list the K63RV overlay X1-X8, or state that it is erratum v2 (c31d7623), and rename it so it does not clash with the X1 tuple. List WV overlay items 1–9 for C1.

**F4. Text of record for (H-A2X)** (COMP:84-86, COMP:119, COMP:140)
- U3:143 states A2X for "K7(a2)", but U3's definition lines are not excerpted. Its identity with A2S:14-17 is inferred from A2S:18.
- COMP:119 says K3 has "none of its own" overlays. COMP:140, however, cites a "corrected OV2 v2 snapshot", and COMP:119 itself mentions a parent premise addendum (cca3de2a).
- **Repair:** add U3's §1 definition range to the manifest, or delegate the identity check to U4 explicitly. Name the exact OV2 version and addendum bound to (H-A2X).

**F5. StageB load-bearing scope overstated** (COMP:130; EV2:14)
- "The only authority for K5.2* (incl. D2′)" is wrong for the D2′ case. That case is removed by the accepted written D2′ (RM:83; WV:21; COMP:44); StageB only over-covers it (SB:20).
- The error is conservative: it over-demands G4.
- **Repair:** "only authority for K5.2* (C∩E={i*}) and KII; the D2′ case is written-excluded". In Q1 write "C1 StageB (K5.2*, KII)".

**F6. Trust base omitted from §6** (COMP:124-131 with Q3)
- SB:45 ("trusts CPython 3.14, the OS and the hardware") is part of C1's literal scope.
- **Repair:** add one sentence after Q3, together with the runtime trust of the N2 and N3 verifiers.

**F7. Ruling not restated verbatim** (EV2:6-10, EV2:14)
- The restatement omits RUL:9's qualifier "if their only accepted proof remains computational".
- It calls the StageB checker "qualified", which RUL:11 does not say.
- The "exactly one" checker counts come from the IRC, not from the ruling. The current effect is unchanged.
- **Repair:** quote RUL:9 verbatim and attribute the counts to the IRC, with RUL:11-13 as the listed gaps.

**F8. Q1 breaks the table row** (EV2:14 replacing COMP:142)
- Q1 is a single cell replacing a four-column row, so the requirement and source columns are undefined.
- **Repair:**
  `| G4 | two separately written exact checkers or an accepted written replacement for every still-load-bearing computation | UNMET: C1 (K5.2*, KII), N2, N3 — one checker each; K5.3 not a gap | RUL:9-15 (contract line 46); SB:46 |`

**F9. Q2 is not byte-determinate** (EV2:15 replacing COMP:150-152)
- The "..." prefix leaves the start of the bullet ambiguous.
- **Repair:** state the full bullet: "G1 and G2 (the two untrusted hypotheses), G3 (this assembly), and G4 in all three components: (i)…(iii). G5 (F-1) stays a permanent disclosed deviation."

**F10. Gate categories inconsistent** (IDX:189-190; COMP:143-144, COMP:150-152)
- G5 is a permanent deviation (RUL:16-18) but sits under `gates_open`.
- G6 is listed as open in IDX but is absent from the §8 obligations.
- **Repair:** move G5 to a `permanent_deviations` field. Declare G6 either a requirement (and add it to §8) or a disclosure (and drop it from `gates_open`).

**F11. Non-claim precision** (COMP:97; EV2:17)
- "Nothing else is open at the class level" holds only relative to the accepted scoped verdicts.
- Q4 names only G4 as blocking.
- **Repair:** append "(relative to accepted scoped verdicts; full-result status also needs G3 and G4 in all three components)", and make Q4 read "while G3 or G4 is unmet".

**F12. Line pins outside the U0 excerpt set**
- S5V:20-23 (COMP:106, COMP:126); SB:17-18 and 29-32 (COMP:131); WV:42 and 48-51 (COMP:109, COMP:154).
- R2V:40 (COMP:118); K63RV:12 (COMP:133); U3:16-26 (COMP:119); the K62 errata hashes and "erratum v2 item 3" (COMP:55, COMP:114).
- The "written" computation cells for N7, E3, DG, M13-A, M1, Z2, U1, Z23-P5, A1/A2 and RICH/D23P are not excerpted either.
- None of these enters T's proof.
- **Repair:** add the ranges, or mark them "not in U0". Cite RUL:10-14 as the authority that N2, N3 and C1 are the only current computation gaps.

**F13. Provenance claim contradicted** (COMP:101)
- "Every … abbreviated sha256 below was recomputed" conflicts with the mis-transcribed suffix at COMP:118, which EV1 P2 had to correct.
- **Repair:** qualify the sentence by reference to EV1 P2.

**F14. Editorial and metadata**
- COMP:160 and PKG:17 point to `review-index-COMP-v1.json`; the current index is v3 (68d61d41…).
- Symbol collisions:
  - E: the set at COMP:23 versus the exponent at COMP:67-75
  - C: the path alias versus A_2∩A_3
  - P: P_ij versus the 5-marker set
  - U1: the review unit versus K7-U1 (IDX:166)
  - G5/G6: gate IDs versus DG lemma IDs (COMP:114)
  - X1: the tuple theorem versus the K63RV overlay
- COMP:140 summarizes the parent derivation check yet says "content not used".
- IDX:108 and IDX:113 give U2's package and manifest the same size (3241 B); this needs re-checking.

## 4. Checked, no finding

- **Premise discipline:**
  - T and K0 use no minimal-order frame, exponent cap, common index factor, Sun(7), StageA, Menon/M-S 4.6 or FH/L5/L6.
  - The only minimal-order frame is internal to N2 (S5V:18), as COMP:106 discloses.
- **No candidates used as accepted:**
  - Apart from (H-NF) and (H-A2X), no pending candidate enters T's proof.
  - K2 is correctly treated as accepted (P5; R2V:5).
  - NF's K7-REM and NF's own split lemma are not used.
- **Scope of class authorities:** every class authority is stated for arbitrary groups or for CEs. A CE is a finite group, so each applies directly (COMP:58-59).
- **N1 status:** N1's "computation: none" rests on its contract import status (RM:13-15; WV:60) and cannot be verified here. RUL does not list it as a gap.
- **Gate content against RUL:**
  - N2, N3 and C1 are load-bearing and UNMET.
  - StageA and K5.3 are not gaps (RUL:15).
  - F-1 is permanent (RUL:16-18).
  - Accepted statuses remain valid at their scoped verdicts (RUL:9).
- **Hashes:** every full hash quoted in COMP agrees with the supplied verdict texts wherever both appear. The only abbreviation slips are the two fixed by P1 and P2.
- **Package arithmetic:** 28 sources and 46 ranges confirmed; 90,273 + 9,723 = 99,996 B.

**Counts: FATAL 0, MAJOR 0, MINOR 14.** All repairs fit in one metadata overlay plus an index revision. The exception is F1's escalation case, which would add an obligation to §8.
