# FINAL-BC-repair-v1 — bounded repair of FINAL parts B and C (exposed interfaces, bookkeeping, conditional markers; no new mathematics) [CANDIDATE_UNVERIFIED]

- **Written:** `/bin/date` read at 2026-10-19T22:13:43-0700, immediately before this exclusive create. Owner SunM13MixedFibres, math-1.
- **Frozen scope:** `FINAL-BC-REPAIR-SCOPE-v1.md` 4df23fa1a5e009df26855273a58e0d6f7b39ebc240b7bc26f5a7378538eab1b6 (22:08:01). Inputs: parent disposition
  `RUN/review/sun7-FINAL-ABC-first-family-parent-disposition-v1.json` 7ba4619d…398e; Codex B 01f69d36… (0F/2M), Codex C 79017ed7… (0F/2M).
  Part A (0F/0M/0m) needs no repair.
- **Reading order.** Part B: CUT-v3.md (79ae0763…) -> CUT-v3-erratum-v1.md (22159673…) -> section B here. Part C: FCS-SITES-v1.md
  (01dbd89a…) and SUN7-COMP-erratum-v3.md (7c620f5d…) with addenda v1 (21f836a8…) and v2 (64d8ea66…) -> section C here.
  All earlier files stay byte-identical. Abbreviations and roots as in CUT-v3 LF10-15. "n.." = CUT-v3 section 7 node id.

## B. Part B
### B1-NF. NF's "(a1) closure" import is the edge 57 -> 58, not an input of node 47
- **Accepted exports** (R/sun7-K7-NF-parent-verdict-v1.md dc92a745… LF9-12): K7-NF ("no such configuration lies outside F")
  and K7-REM ("with the accepted (a1) closure, every such configuration lies in (a2)").
- **NF LF54** (interface row): "(a1) closure — Corollary K7-REM only | — | the R2 verdict's mandatory overlays (its lines
  19-31) | RUN/review/sun7-K7-R2-parent-verdict-v1.md (9b0f7df5…926d) lines 5, 9 | (a1) as defined at its line 9".
- **Theorem K7-NF and proof** (NF LF83-111): Lemma PART (LF59-81) puts every configuration outside F into one block B1-B8, each
  closed by K7-M0, K7-M1, K7-35, K7-Z2, K7-U1 or Z23-P5 (n41-n46); R0 is cited at LF109-111 (n03); class K7 is README LF91
  (NF LF20; n24); SHAPE (LF22-26) and MK (LF35-37) are proved in the file; LF113 "Remarks (no further premise)". The (a1)
  closure is not cited in LF83-118.
- **Corollary K7-REM** (NF LF120-131): its Lemma "F = (a1) disjoint-union (a2)" (LF126-128) uses Lemma MK; the corollary uses
  "Theorem K7-NF and the accepted (a1) closure (R2 verdict line 5)" (LF129-131). NF parent erratum v3 LF5: the (a1) closure
  is cited directly only here; TC/CELL enter transitively through it.
- **Placement:** n47 := Theorem K7-NF with internal SHAPE/MK/PART, inputs 03, 24, 41-46 (unchanged); n58 := Corollary K7-REM
  (with the split lemma), inputs 47, 57 (unchanged). NF LF54 is exactly the edge 57 -> 58. n57's inputs (03, 06, 50, 53-56)
  do not involve 47 or 58, so there is no cycle. Add section 6 row: **58 | K7-REM | NF LF54, LF120-131 | 47 (incl. MK), 57 |
  closed**. n70 (K7-EXCL: 24, 58, 69) is unchanged.

### B1-OM. Declared-import omissions (Codex's four, plus six found by re-reading the exposed declarations)
| node | declaration (file LF: words) | added | corrected section 7 inputs |
|---|---|---|---|
| 42 K7-M1 | K7-M1-erratum-v1 LF12-15: "erratum E2 (Sun(2))"; K7-M1-v1 LF9: "L0.2/L0.3" | 01 | 01, 03, 04, 06, 16, 18, 20 |
| 45 K7-U1 | D/K7-U1-v1 LF14-15: "E1 (L0.2/L0.3 ...); E2 (Sun(2))" | 01 | 01, 03, 04, 06, 07, 08, 16, 17, 18, 24 |
| 46 Z23-P5 | D/K7-Z23-P5-v1 LF24: "L0.2/L0.3" | 01 | 01, 03, 04, 06, 07, 08, 16, 17, 18, 20, 21, 24 |
| 48 D23-CENTER/MIX | D/K7-D23-NO4-v1 LF32: "R0 and K7 definition"; LF50-51: "the additional set prohibitions below use Sun(2)/Sun(3)" | 01, 02, 24 | 01, 02, 03, 06, 07, 08, 16, 17, 18, 20, 21, 24 |
| 54 TC-A22 | D/K7-TC-A22-v1 LF16: "(any group, R0)" | 03 | 03, 16, 17, 49, 50, 52, 53 |
| 55 CASEA-K23 | D/K7-CASEA-K23-v1 LF12-13: "Direct Sun instances: Sun(2), Sun(3)" | 01, 02 | 01, 02, 03, 06, 07, 16, 17, 48, 49, 50, 52, 53, 54 |
| 67 A2X Unit 2 | A/K7-A2-UNIT-2-v1 LF13: "Foundational imports only: R0, L0.1-L0.3, ..., Sun(2)-Sun(4)" | 02 | 01, 02, 03, 04, 06, 07, 16, 17, 59-63 |
| 74 SH-1 | K62/K62-SH-DG-erratum-v1 LF74: "(LFC (a)-(b))" | 16 | 01, 06, 16, 71 |
| 77 M13-A items 1-2 | K62/K62-M13-A-v1 LF8: "R0; the K6.2* class definition; old README section 0 L0.1 with Lagrange" | 24 | 01, 03, 04, 06, 07, 16, 17, 24, 71-76 |
| 78 K62X | S/continuations/k62-full-closure/K62-FULL-v1 LF54: "(Sun(2), Sun(3) direct)" | 02 | 01, 02, 03, 04, 06, 16, 17, 24, 71, 73, 77 |
Every added input has a smaller id; order, node count and acyclicity are unchanged. **Convention X8 (adds to X7):** (i) Sun(t)
instances declared "only through LFC (c)" or "through VFC (V3)" are represented by 16 or 17 (e.g. A2-FIVE LF35, K62-E3 LF10-11,
DG LF164-165, M13-A LF15, Unit 1 LF28), whose inputs contain 01, 02, 14, 15; (ii) a declaration "everything imported by M at
the same scopes" (TC LF17) or "transitive closure as in A1-STRUCT section 0" (CASEA LF13-14, CELL LF13) is represented by M's
node(s) (n49, n50, n52), whose inputs are exactly the inherited set.

### B2. Interface exposure: supplied in the part B packet, or CONDITIONAL
- **Supplied literally:** NF exports and text (above); the S56W written exports (statements LF16-25; section 2 LF34-65 with
  L3/K2 for pairwise disjoint cosets; Prop 4.5 LF67-69; R1 LF105-108; R1(6) LF126-128; R0 LF143-147; dependency table
  LF152-162) with the S56W verdict LF5-14 and errata v1 LF5-6, v2 LF5-12 (n01, n03, n09, n12-n15); the class exports KIIW
  verdict LF5-11 (n36), A2X verdict LF5-17 (n69), NF verdict LF9-12 (n47, n58); every declaration line of B1-OM; the CAP
  envelope sources (K62-CAP-v1 LF9-18; K62-FULL LF66-67; K62-FULL parent erratum v2 LF7).
- **CONDITIONAL (named; earlier exposure in the part A, CUT-v2 or M12 manifests is identity only):** (1) ROW interfaces
  n18-n23 (ROW-U/E8, ROW-U-deg F3, K63-U0 subset form, ROW-1 with F2/F3, Z2 G2, ROW-2 with the K7-35 errata, CE1 P1); (2)
  the export statements and governing overlays (CE1, R2E, ECFF, OV1, OV2, unit errata) of n49-n57 and n59-n68, beyond their
  declaration lines (part A separately covers the D23P, TC.11 and CELL interfaces); (3) the M12 interfaces n71-n78 (E3, DG,
  SH-1, CAP-C1/C2, RC, M13-A items 1-2, K62X), reviewed in the M12 packet (Codex 0F/0M/0m) and pending its second-family
  disposition; (4) **CAP-ENV:** n75-n76's restricted boundary {01, 04, 06, 71} / {01, 04, 06, 16, 75} versus K62-CAP-v1 LF9-17,
  which also declares R0, the class definition, rules-k7 L1, VFC with the count and "section 4 Lemma CAP (its capping
  argument)"; K62-FULL LF67 says CAP C1/C2/RC are not used, but K62-FULL parent erratum v2 LF7 reads that as "not used
  directly" and inherits M13-A items 1-2's closure with "no claim that CAP/RC ... have been removed transitively". n77-n79
  inherit CAP-ENV.
- **Consequence:** N2c (declared-import closure) and N2d (complete DAG) remain CONDITIONAL on (1)-(4); the displayed order is
  acyclic. No completeness certification.

### B-REC. The 68 -> 79 reconciliation is WITHDRAWN
CUT-v3 LF275-278 (correspondence with CUT-v2's 68 nodes) is withdrawn as unverified; it carried no premise. The 79-node order
(CUT-v3 section 7 with CUT-v3-erratum-v1 and B1 above) stands alone, with no claim about CUT-v2's node table.

## C. Part C
### C1-a. IL2/CS2: literal Prop 4.5
Required (README LF19): "(2r_1, 4r_2, 4r_3, 4r_4), r_i pairwise coprime, r_1 odd, is not G-harmonic for any G"; use (README
LF79): the four disjoint cosets of i, d_1, d_2, d_3 realise that tuple. Replacement (S56W LF68-69, proof LF70-103): "Let r_1,
..., r_4 be pairwise coprime with r_1 odd. No group has subgroups with [G:U_1] = 2r_1, [G:U_i] = 4r_i (i = 2, 3, 4) and pairwise
disjoint left cosets g_iU_i." Same tuple, coprimality and parity; the conclusion is exactly the non-existence used at LF79, in
the CE group, for four of the seven left cosets (deletion). Accepted as a displayed written lemma (S56W verdict LF14),
qualifying only through this re-proof (erratum v2 m5). IL2, CS2: statement-matched.

### C1-b. DROP rows: evidence, or CONDITIONAL
| row | status after repair | evidence (supplied) |
|---|---|---|
| IN2, IN8 | DROP supported (Codex C) | K63RES verdict LF18; RICH erratum LF24-26 |
| IL7 | DROP at the displayed authorities; closure CONDITIONAL | WV LF49 |
| **IL9 (rules-k7 Lemma CAP)** | **NOT DROP; CONDITIONAL on CAP-ENV (B2 (4))** | K62-CAP-v1 LF12-13 declares "section 4 Lemma CAP (its capping argument)"; K62-FULL parent erratum v2 LF7 keeps CAP/RC in the inherited envelope. Lemma CAP is a WV-accepted written rule (WV LF23, LF42 give the parent's capping argument), not a Sun(5)/Sun(6)/StageB citation; its pattern clause (rules-k7-v1 LF80) cites "sun-coset6 rules-k6-v1 L8 M1" for upward closure in tau, and whether that clause is used through CAP-62 is not determined here |
| IL5 (K), IL6 (P), IL10 (RPLP other than F7), IL12 (frame), TS3 frame clause, CS5 narrowing | CONDITIONAL: declaration-level support only; proof-body non-use not audited | "Not used"/"only" declarations: K7-M1 LF10-11, K7-35 LF8, K63-D LF10-11, K63-E LF8, K7-U1 LF23-26, D23-NO4 LF50-51, D23P LF44-45, RICH LF41-42, K62-E3 LF12-13, DG LF168-169, Unit 1 LF25, Unit 2 LF13, S56W LF163-165, K62-FULL LF66-67 |
Unlisted final-chain modules (for example Z2, Z23-P5, LFC-INV, TC, TC-A22, A1-STRUCT, CASEA, CELL, A2-FIVE, Unit 3, K63-RES,
X1, K52W, KIIW, C5W, C56W, CAP-62, M13-A) carry no such explicit exclusion in the supplied lines.

### C1-c. Census rows
- Sources now supplied: IN5 (K63-D LF55: "no 5-set is ({i*,u,u',u''} has gcds 3 < 4)"), IN9 (K62-FULL LF46; LF275-277:
  direct Sun(2)/Sun(3) via LFC (c)/VFC (V3), Sun(4) through imports), IL4 (rules-k7-v1 LF19-24 with WV LF23).
- CONDITIONAL (no closed census supplied): IN1's inheritance list, IN10, KS5's negative assertion, and the section 6 PROV list.
- **FCS LF110-113 ("Genuine gaps found ... none") is now CONDITIONAL** on CAP-ENV, the proof-level DROP census (IL5, IL6, IL10,
  IL12, TS3, CS5), the census rows above, and part B's CONDITIONAL interfaces. The only surviving dependency identified is
  the declared CAP-ENV import; no other is demonstrated.

### C2. F4: A2X class identity, compared literally
- COMP LF84-86 (H-A2X): "no configuration of K7(a2) exists in any group with finite-index subgroups, for all E, A, B >= 1 and
  all cofactors", with (a2) as in COMP LF69 = A/K7-A2-SCOPE-v1 LF14-17: seven pairwise disjoint left cosets, all pairwise index
  gcds 6, "so n_i = 6 r_i with pairwise coprime r_i"; distinct z, t, p with r_z = 2^E w_z, r_t = 3^A w_t, r_p = 5^B w_p, E, A,
  B >= 1; the four others unmarked (r_u = w_u); all w pairwise coprime and prime to 30; exponents and cofactors unbounded;
  arbitrary groups via R0.
- A/K7-A2-UNIT-3-v1 LF10-13: the same data ("n_j=6r_j pairwise gcd6; r_z=2^E w_z, r_t=3^A w_t, r_p=5^B w_p, distinct z,t,p,
  E,A,B>=1 unbounded; W' ... four unmarked; every w prime30, pairwise coprime"; R0); conclusion LF143-144: "No configuration of
  K7(a2) exists in any group with finite-index subgroups, for all E,A,B>=1 and all cofactors."
- A2X verdict LF9: "No group G admits seven pairwise disjoint left cosets g_jU_j of finite-index subgroups with n_j=6r_j and
  pairwise coprime r_j, where three DISTINCT vertices z,t,p have r_z=2^E w_z, r_t=3^A w_t, r_p=5^B w_p, E,A,B>=1, and the
  other four r_j=w_j. All seven w_j are pairwise coprime and prime to 30; their values and all exponents are unbounded. The
  subgroups need not be distinct." Scope LF5: "The complete K7(a2) index regime is excluded in every group".
- **Comparison:** the three texts name the same parameters, the same coprimality, the same exponent range and the same group
  scope. "pairwise gcd 6" (Unit 3) and "n = 6r with pairwise coprime r" (SCOPE, verdict) are the same condition, as SCOPE
  LF14-15 itself states. No text requires distinct subgroups. The governing overlays (unit errata and parent check pinned at
  verdict LF48-53; unit 3 parent erratum LF9-12) change notation, exports and accounting, not the class. **F4: identity
  displayed at statement level; E3.9 makes no scope change** (CANDIDATE, for review).

## D. Status and non-claims
Every judgment above is CANDIDATE_UNVERIFIED. Named open items: B2 (1)-(4) (including CAP-ENV) and the C1 CONDITIONAL rows.
Full Sun(7) UNACCEPTED; completeness certification WITHHELD; historical Sun(5)/Sun(6)/StageB records stay computer-assisted;
StageB F-1 permanent. No novelty, Lean, human-review or runtime claim. No scientific computation; metadata and reading only.
