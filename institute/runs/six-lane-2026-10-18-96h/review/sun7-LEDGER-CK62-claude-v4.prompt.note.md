# CK62 second-family interface-closure audit (N53–N58, K01–K06, RES-1)

**Counts: FATAL 0 · MAJOR 0 · MINOR 4.**
- All four MINORs are completeness or bookkeeping. I found no correctness defect.
- There are seven uncounted nits.
- One CUT2 obligation remains open.

**Governing order applied:**
1. DG erratum v1, then SD G1–G8.
2. Ledger worker erratum v1, then parent errata v2–v4.
3. Addendum v5–v8:
   - The explicit order is N01–N08, N15, N09–N14, N16–N59.
   - DEF exports predicates, P0/P1 and conditional matrices only.
   - ROWU-deg/E8 are abstract exports, and no node in N53–N58 uses them.
4. Addendum v9/v10:
   - No node in N28–N39 is an input of N53–N58.
   - The S6/S8/S9 clarifications do not touch K03's S4/S5 routing.
   - No provider statement used here is weakened.

## Claim-wise verdicts

### N53 E3 — interface valid (export boundary: m3)

Z1 New (E3E2 LF51–65) replaces E3 LF6–13. Its premises map as follows:

| Premise | Provider |
|---|---|
| R0, which must preserve conjugated intersections for α* (v5 m4) | N03 |
| K6.2* predicate with P0/P1 | N15 |
| L0.1/Lagrange, the L0.3 identity, E1 | N02 |
| LFC (a)–(d) | N12 |
| INV (a)–(b) with E6 | N13 |

- **Sun use:** LFC (c) is invoked only at |T| ∈ {2,4}, with left cosets in U_v/U*_v and at most 6 pieces (LE E3). This routes through N12 (X1), with N01 as a conservative edge (X4).
- **No VFC, T or F7:** none of N09–N11 is needed. N11 reaches N53 only transitively, through N13's (V1) q-definition (v6 MIN-1). E3's "not used" means direct use.
- **Body and errata:** the body LF22–105 excludes the LF117–120 diagnostics (CK LF95). F2 stays operative, and Z11/Z6 supersede F1/F3 (CK LF12). This matches LEDGER LF99.

### N54 SH1 — argument correct; edge cell incomplete (m1)

I re-derived SD LF74–79:
- L_c = g_cU_cU_d is the union of t_c left U_d-cosets. Its measure is α_dc/g_dc = 1/2 by LFC (a)–(b); α_dc = 1 is forced by E1 because g_dc = 2.
- μ(U*_cU_d) = α*_dc/g_dc = 1/2 by L0.1, using [G:U*_c] = n_c and U*_d = U_d (since g_d = 1).
- Part (b) is valid: w ∈ L_(i*)U_d = L_(i*) gives a·g_(i*)⁻¹ ∈ U_(i*)U_d, hence g_(i*) ∈ U_dU_(i*), hence g_(i*)U_(i*) meets U_d, contradicting disjointness.
- The same argument works verbatim for c ∈ O, so the "E3 step 3" pointer in (a) is replaceable.

Further checks:
- The argument is orientation-free, because both 1/2 values are forced.
- It uses no Sun instance and works with left cosets only.
- It exports the argument only (SDV LF16), which only N56 consumes.
- N55 and N58 declare that they do not use SH (G1 New LF168; FULL LF67), and neither lists N54 as an input. This is consistent.

### N55 DG — the five exports match; DG erratum v1 is valid (edge cell: m1; scope: n1)

**Premises (G1 New):**
- L0.1/Lagrange and E1 come from N02; LFC from N12; INV with E6 from N13.
- E3 Lemmas 1–3 (Z10), steps 1–3 and Z11(a) come from N53.
- The withdrawn T/VFC citations mean no N09 or N11 edge is needed.
- Sun(2)/(3)/(4) enter through LFC (c), with N01 as a conservative edge (X2).

**Exports (v2 m1, v4 m5, CI62 LF11):**
- DG-1, orientation-free.
- DG-3 in G3 form.
- DG-4, with its unmarked-added-vertex condition.
- (a) the conditional statement, with premise α_(d i*) = 1.
- (b) the G5/G6 argument.

**Consumers:**
- FULL consumes (a) only (FULL LF63).
- M13-A consumes DG-1, DG-3/G3 and (b) (M13-A LF13–14).
- Neither treats (a) as supplying DG-1.

**DG erratum v1 New, re-derived:**
- Every 4-subset of a 5-cycle is a 4-path. So each e ∈ Q has a cycle-neighbour in R = Q∖{e}, where α* = 2, and therefore m_e ≤ 2.
- At most two O-vertices are marked: at most one 3-marker (C–C gcd 6) and at most one 5-marker (a ≤ 1). So an unmarked e exists, which meets DG-4's own condition.
- The unmarked step multiplies by k ≤ m_e ≤ 2 (G1 New LF160). With v2 of the lcm equal to 1 on O and τ* = 4, this gives v2(T*_Q) ≤ 3 + 1 = 4.
- The step is correct.
- Not pasted: G-items touching section 5 (SD LF280, LF301–315). If any of them rewrites step 3, it governs after the erratum.

### N56 M13A — valid at declaration and graph level; CUT2 body check open

**Inputs:** M13-A LF7–14 maps to exactly:
- N03, N15, N02, N12, N13.
- N53: Lemma 1 with its gcd at d; Lemma 2 and Z11(a); Z10 Lemma 3; the step 3 argument; C2 at α_(d i*) = 1.
- N54: the S2 argument.
- N55: DG-1, DG-3/G3 and (b).
- N01, conservative (X2).

All of these are present in the input cell.

**Orientation logic:**
- In (1,3), α_(d i*) = 1, so statement (a) and E3-C2 cover the α*-family.
- For the α-family, α*_(d i*) = 3 ≠ 1, so the argument must be re-instantiated. This is exactly what v4 m5 describes.
- DG* keeps each family's own r_Q ≤ 4 hypothesis (M13V LF13; K05).
- Five-piece fibres are excluded by a forbidden 4-subset, using Sun(4) through LFC (c) in U*_d (CK LF80). Sun(5) is not used.
- (3,1) is covered by INV (M13V LF9).

**Scope:** only items 1–2 are consumed. Items 3–6, M13-B/C/D and the C/D replacements are unconsumed (LEDGER LF323–324; CK LF21, LF30).

**CUT2-M12, as far as the supplied text shows:**
- **M1:** no E3 example appears among the declared imports, and E3 LF117–120 lies outside N53's body.
- **M2:** the input cells of N56, N53, N54 and N55 contain no CAP, DT or M13-B/C/D node. M13-A LF6 declares no CAP/DT candidate. N57 (conservative) feeds N58, not N56. So D3/D4 are outside N56's reachable closure.

### N57 CAP62 — valid relative to CI62 (boundary gaps: m4)

**Inputs:** CAP LF9–18 maps to:
- N03, N15, N02, N12, N13.
- N09: L1 (T1)–(T3), τ_min and τ_max.
- N11: VFC with its count.
- N16: Lemma CAP, read under CI62.
- N53.

There is no DG, SH or FG import. CI62's own provider set is a subset of N57's inputs.

**R16:** N57's actual use (v4 m6(i); CI62 LF6–10) lies inside v8 m-B's range. LF76, LF80's second sentence and τ-monotonicity are excluded from N57's use, as CI62 LF10 requires.

**RES-1:** CD4–CD7, now supplied, add no premise, no cover and no computation.
- CD4 keeps the transfer conditional and states that no element-wise check exists (LF197–198).
- CD4's sentences about DG, DG-1 and DG-2 only illustrate (D3)/(D4). They are not imports, so CAP LF17's "not used: K62-DG" still holds and no N55→N57 edge is needed.
- CD5's apex formula is (T3) with y = b.
- CD6 is a remark.
- CD7 is LFC (a) in normalised form.

This text is consistent with CAPV LF23–26 and CI62 LF9. It must be read through CD-e2 V1–V14, which are not pasted (CK LF19).

### N58 FULL — interface valid

FULL LF52–65 maps to:
- N03 and N02: R0 and L0.1/L0.2.
- N15: K6.2* predicate with P0/P1.
- N02 for Sun(2); N01 for direct Sun(3).
- N12: LFC.
- N13: INV, E6, E7 and double inversion.
- N11: VFC on either configuration, through INV (a).
- N53: E3-T, L1, L2, and C2 with the LF105 swap.
- N55: statement (a), in both orientations by actual inversion.
- N56: items 1–2 at (1,3).

GS is a cross-check only. M13X, MK, R2MIX and M3R are not premises.

**N57→N58 edge:** FP2 item 3 ("not used directly") justifies it as conservative. It also carries M13V LF5's CAP C1 and RC-i* (CAPV LF24–25), and L1 (T3) through N09 via N57.

**Orientation cover:** the cases are {(1,1), (1,3), (3,1)}. This follows from E3-L1 (x_(d i*) ≠ 2 for both families) together with α + α* ≤ g_(d i*) = 4.

### Rows and global checks

**Rows:**
- K01–K03 discharges are correct: LE E1; N13 with E6/E7; N12/N11 with S5W/S6W at S4/S5.
- No node applies Sun to five or six pieces directly. E3 and DG use |T| ≤ 4, M13A uses |T| = 4, and FULL applies Sun(2)/(3) directly.
- K06 goes to N58 conservatively (v4 m6(ii)).

**Order and acyclicity:** every input precedes its consumer in the explicit v6 order. There is no N57→N16 or N58→N57 edge (v3).

**Actual inversion:**
- INV (a) gives disjoint left cosets with the same indices.
- E6 makes the K6.2* predicate and the marking depend only on the index tuple.
- Double inversion exchanges the two families.
- E7 gives α + α* ≤ g without VFC.

**Ambient subgroup, coset side and piece count:**
- LFC uses left cosets in U_v/U*_v, at most 6 pieces (LE E3).
- VFC (V3) uses pieces of R = Φ_v·y, right-translated into Φ_v and inverted (RK7 LF46; v10 S9), at most 6 pieces.

**Excluded premises:** the least-order frame, seven-piece L5/FH, StageA/B, the DT-B certificate, GS, solver output and the E3 diagnostics are all absent. Computer-assisted Sun(5)/(6) enters only through S5W/S6W at S4/S5 (CK LF83–95; LEDGER LF327).

## MINOR findings

### m1 — missing direct edges N13, N15→N54 and N15→N55 (completeness)

**Problem:**
- SD LF74–79 uses the inverted configuration directly: U*_c, U*_(i*), [G:U*_c] = n_c, U*_d = U_d and α*.
- It also uses the K6.2* gcd values g_dc = 2 and g_(d i*) = 4, and the O/i* vocabulary.
- DG-3, DG-4 and (a) are phrased in N15 vocabulary (e_d, O, unmarked). DG erratum v1 LF20 also uses the marker count.

**Ledger state:**
- N54's inputs are N02, N12, N53.
- N55's inputs are N01, N02, N03, N12, N13, N53.
- K01/K02 nevertheless list both nodes as consumers. This breaks the convention that consumer lists equal input cells (v5 m5(iv), v7 m2).

**Consequence:** a ledger mismatch only. N13 and N15 are already ancestors through N53.

**Repair:**
- Add N13 and N15 to N54's inputs.
- Either drop N54 from K01's R0 component (SH-1 is a finite-configuration argument; precedent v7 m1), or add N03 to N54 as a conservative edge.
- Add N15 to N55's inputs.
- All of these edges are forward, and ancestry is unchanged.

### m2 — rows cells disagree with row consumer lists (bookkeeping)

**Problem:**
- K01–K03 list N53–N58 as consumers.
- The rows cells omit K01–K03 for N54 (K04), N55 (K04), N56 (K04) and N57 (K06, R16).
- K04's consumer list (N55, N56, N58) omits N54, which uses E3 step 3.
- It also omits N57, which uses E3 Lemmas 1–2, Z11(a) and Z10 (CAP LF15–17; CI62 LF8).

**Repair:**
- Add K01–K03 to the rows cells of N54–N57.
- Either add N54 and N57 to K04's consumers, or split K04 into E3, DG and SH-1 parts with exact consumers (precedent v9 m3).

### m3 — N53's export boundary is too narrow (precision; analogue of v2 m1/v4 m5)

**Problem:** N53's accepted-statement cell is E3V LF5 (E3-T) only. Its consumers also use:
- E3V LF19, LF20 and LF25 (FULL LF60–62).
- The Z10 Lemma 3 proof form for every non-empty Q ⊆ O (G1 New LF159–160; M13-A LF11; CAP LF16–17; CI62 LF8).
- Z11(a).
- Lemma 1's gcd computation at d.
- The step 3 argument (SD LF75; M13-A LF12).
- C2 with its LF105 swap.

**Consequence:** E3-T alone does not supply these items, just as conditional DG alone does not supply DG-1.

**Repair:**
- Have N53/K04 export the four statements and these argument exports explicitly.
- Read N53's declaration column as "E3 LF6–13 as replaced by Z1 New".

### m4 — RES-1 and N57 discharge boundaries (completeness)

**(i) An orphaned range.**
- CD1 LF155–159 closes CD3's New block with the VFC-form granularity bound. Together with C1 for the opposite family, this bound is the mechanism behind RC-O's opposite-entry condition (CAPV LF24–25).
- That range lies outside both the CK census snapshot (LF1–154; CK LF18) and RES-1's stated range (LF161–249).
- Re-derived here, it is correct and uses only N11, N13 and N02:
  1. Φ_v·W ⊆ Φ_vΦ_j, so it misses every D'_j by (V1).
  2. μ(Φ_v·W) ≥ 1/gcd(n_v, T′) by L0.1 and Lagrange.
  3. Hence the x′-row mass is at most 1 − 1/gcd(n_v, T′).

**(ii) A missing verdict line.**
- N57's discharge cell, CAPV LF23–25, omits the setting (LF21) and item 4 (LF26: no cover, LOSSY, count not a pattern function).
- K06 nevertheless exports "conditional transfer".

**Consequence:** the conservative N57→N58 envelope would carry the transfer without its limiting verdict line. Nothing here is operative.

**Repair:**
- Set RES-1's object to CD1 LF155–249.
- Set N57's discharge to CAPV LF21 and LF23–26, read with CI62 LF5–11.
- RES-1 can then be marked as locally supplied and checked, read through CD-e2 V1–V14.

## Nits (uncounted)

- **n1 — DG erratum v1 scope.** The erratum targets DG section 5, the P_ob exclusion (about DG LF62–89; CK LF87, LF94). Theorem DG sits at LF50–61 (FULL LF63). So the erratum lies outside N55's body (LF20–61) and outside its exports: it is in force but non-operative. Section 5 also contains DG's only Sun(3) use, so X2's N01 edge is purely conservative.
- **n2 — Range readings under v5 m2 and v6 MIN-3.**
  - FULL LF55's "LE 12–19" should read LE LF14–18.
  - FULL LF53's "README 85–96", and the "sections 2, 5" cited by E3 and CAP, should read LF89–96 without LF87's exhaustiveness claim.
  - The "class reduction" clauses (G1 New LF167–168, M13-A LF16, M13V LF5) are provenance only. Exhaustiveness lives at N17/N23→N59, so no edge into N55 or N56 is needed.
- **n3 — FULL LF54 is historical.** Its computer-assisted Sun(5)/(6) hashes and its "every group" scope are not operative. The operative route is S5W/S6W at S4/S5 through N11/N12.
- **n4 — Hash typo (process only).** FULL LF64 cites M13V as "2fac7a30…4c34", but the pinned hash ends in …39c4e34 (FP2 LF7; source header). FP2's full pin fixes the identity.
- **n5 — Count wording.** v4 m5 says "four distinct items" but lists five, which is the count used by P2 LF7 and CI62 LF11.
- **n6 — Loose census wording.** CK LF77's "right cosets inside Φ^x_v" is imprecise: (V3) translates R = Φ_v·y into Φ_v. This is navigation only.
- **Query — SD notes range.** FULL LF63 imports SD "notes LF323–327". Confirm that these lines lie inside G8, or add them to N55's body.

## Open obligation (CUT2-M12)

M1 and M2 hold at the declaration and ledger-graph level. M13 LF32–107 itself is not supplied, so a literal body check is still owed. It must confirm that:
- No step of A1(a)–(e), DG-1*, DG-2*, DG*, C1* or C2* uses an E3 numerical example.
- No such step uses an M13-B/C/D result, a D3/D4 certificate, or the parent erratum's C/D text.
- M13V items 1–2 rest on M13-A LF7–14, not on M13V LF5's A–D import list.

Until that check is done, N56, and N58 through K05, are locally closed only **conditionally** (CI62 LF15).

## Bottom line

After m1–m4, CK62 local interface closure is valid relative to the named provider boundaries: N01–N03, N09, N11–N13, N15, and N16 under CI62. For N56 and N58 it remains conditional on CUT2-M12.

This review does not accept:
- CI62 mathematics anew.
- Any CAP cover.
- The final join.
- Full Sun7, which stays UNACCEPTED.

It also makes no novelty, Lean, human or runtime claim.
