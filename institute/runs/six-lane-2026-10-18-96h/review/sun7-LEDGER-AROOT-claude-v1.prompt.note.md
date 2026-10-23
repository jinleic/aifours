# AROOT N01–N08: written interface-closure audit (pasted text only)

**Counts: FATAL 0 · MAJOR 0 · MINOR 6.**

- I found no correctness defect.
- All six findings concern completeness, bookkeeping or process. None is load-bearing for any exported statement of N01–N08.
- No N01–N08 body declares a computational premise (S56 LF103, LF163–165; C5 LF30–32; C56 LF30–31). I did not assess priority.

**Errata applied:**
- LEDGER erratum v1: X4 (LF13) and X8 (LF17).
- S56 parent erratum v1 items 1–2 and parent erratum v2 m1–m9.
- C5W parent erratum v1 items 1–6.
- C56W parent erratum v1, and parent erratum v2 items 1–4.
- LE E1–E2.
- Ledger parent errata v2–v4 do not touch N01–N08, except the C3 reachability rule noted under m1.

## Claim-wise verdicts

**N01 ZHU** (LEDGER LF51, LF218)
- This is a boundary import, and its scope fits every use in the packet.
- Literal scope: any group, k = 3 or 4, pairwise-disjoint left cosets of finite-index subgroups, distinct subgroups not required (C56W parent erratum v2 LF7; S56 parent erratum v2 LF15).
- Its direct consumers inside N01–N08 are exactly {N04, N05, N07, N08}, matching X4.
- N02, N03 and N06 correctly have no N01 edge (S56 LF103, LF152).
- Finding: m6.

**N02 ELEM** (LF52, LF219)
- Valid root.
- L0.1–L0.6, L1–L3 and K2 are proved at S56 LF38–61 from Lagrange only. This reading includes the pairwise-disjoint standing hypothesis (S56 parent erratum v1 LF5) and finite G (S56 parent erratum v2 LF12).
- It has no node inputs (S56 LF152).
- Findings: m2, m3.

**N03 R0** (LF53, LF220)
- Valid for transferring indices, intersection indices and disjointness, with equal subgroups allowed.
- It is a finite-core quotient, not a least-order choice (S56 LF144–147; CR LF44).
- Findings: m4, m5(iii).

**N04 C5W** (LF54, LF221; R06 LF144)
- Edges are complete and forward. C5 LF24–29 map to N01 (Sun(3) only) and N02 (Lemma MU and Sun(2), both re-proved in-file).
- The left translate into U_v is confirmed by C5W parent erratum v1 LF6.
- The L/LFCV method is cited but re-proved (C5 LF29), so there is no edge to the later LFC/INV nodes that import Sun(5)/(6).
- The statement (C5 LF17–21) is H5 verbatim (S56 LF26–27).
  - It holds for every finite group, with no minimal frame, all marker placements, r_i = 1 allowed and unbounded cofactors.
  - Its unrestricted quantifier admits equal U_i, which is only possible when r_i = r_j = 1.
  - This meets the scope required by S56 parent erratum v2 LF7.
- No Sun(4–6), Prop 4.5, R1, frame, engine or C18 premise is used (C5 LF30–32; CR LF45, LF74–75, LF79).
- Finding: m1.

**N05 C56W** (LF55, LF222)
- Edges are complete and forward. C56 LF26–29 map to:
  - N01: Sun(3)/(4) inside U_v, with equal trace subgroups allowed (C56W parent erratum v2 LF7).
  - N02.
- C56W parent erratum v2 LF5 replaces the C5W/KII-W shorthand with an explicit identity. So there is no N04 edge and no backward edge from KII-W.
- The statement (C56 LF18–22) is H6 verbatim (S56 LF29–30), at the scope required by S56 parent erratum v2 LF7.
- No Sun(5)/(6), Core(5), Prop 4.5, R1(6) or frame premise is used (C56 LF30–31; CR LF46, LF76).
- Finding: m1.

**N06 P45** (LF56, LF223; R04 LF142)
- Valid.
- Its inputs are exactly those declared at S56 LF103/LF154, mapping to N02 and N03.
- It uses no Zhu, no Core(5) and no computation. CR LF63 classifies it as a re-proof, not a substitution.
- Every use of L2, L3 and K2 is on the four pairwise-disjoint cosets, with the pair condition stated explicitly:
  - (b) v=2, {1,3}
  - (c) v=1, {2,3}
  - (d) v=4, {1,2,3}
  - (f) v=4, {2,3}, second alternative
  - (g) K2 at (2,3,4)
- The 1/4 granularity in (c) and (g) uses only coprimality and 3 | r_1, which (c) establishes.
- The statement at LF68–69 matches the shape required by R04.
- Finding: m5(i).

**N07 S5W** (LF57, LF224; F03 LF115; R07 LF145)
- Valid at the declaration level. The body (S56 LF105–120) is not in the packet; S56V LF5–12 accepted it.
- S56 LF157, LF159 and LF161 map to N01 (k = 3, 4), N02 (via R1: L0.2, L0.6), N03, N04 (H5) and N06. This matches LF224 exactly.
- R07's discharge range "N02–N06" is a union across N07 and N08; it includes N05, which N07 does not need. The per-node list at LF224 is correct.
- The statement matches F03 and S56V LF7 and LF10, as corrected by S56 parent erratum v1 LF6 and parent erratum v2 LF5.
- H5 is consumed in the finite quotient (S56 parent erratum v2 LF12).
- Gate m7 (composition + C5W) is met according to S56V LF5.
- No excluded premise is used (S56 LF163–167; CR LF47, LF78–79).

**N08 S6W** (LF58, LF225; S3 LF297)
- Valid at the declaration level. The body (S56 LF122–141) is not in the packet.
- S56 LF158 and LF160 map to N01, N02 (via R1(6): L0.6), N03, N04, N05 and N06.
- N07 enters through optional route S3 (S56 LF140–141; S56 parent erratum v2 LF6). This edge is forward and creates no cycle:
  - S5W's inputs exclude S6W (S56 LF159).
  - N04, N05 and N06 use no Sun(5)/(6).
- S3's cells (finite G, original left cosets, 5 of 6) fall within S5W's scope: any group, any five disjoint left cosets, equal subgroups allowed.
- I could not check S3 against its source lines S56 LF140–141, which are not supplied. This is non-load-bearing because LF160's main-route inputs exclude S5W.
- Finding: m5(ii).

## Findings

**m1: N04/N05 body ranges include downstream text** (completeness)
- **Where:** LF54 gives N04's body as "C5 LF1-150". C5W parent erratum v1 LF8–9 instead:
  - places the theorem at LF110–120;
  - puts the conditional Sun(5) corollary after it, outside the core theorem;
  - says the corollary needs Prop 4.5, R1 and Zhu Sun(4) (also CR LF75).
- **Same issue at LF55:** N05's range includes C56 LF121–141, which is provenance only (CR LF76; C56W parent erratum v2 LF8).
- **Consequence:** read literally, N04 would need N06 and R1, which sits inside N07's body. That gives backward edges and an N04↔N07 loop at the file-range level. LF214's forward-order check holds only for the theorem-proof range. Nothing consumes the corollary, so there is no mathematical effect.
- **Repair:** exclude C5 LF121–150 and C56 LF121–141 from the bodies. Record them as unconsumed text with no node; S5W/S6W replace them.
  - A separate node is not possible: it would be unreachable from N59, which violates C3 (ledger parent erratum v2 LF5).

**m2: Root N02 body contains a later-context line and an excluded-import attribution** (completeness / excluded-premise wording)
- **Where:** LF52 and X8 include "LE E1 LF12-19, E2 LF21-25" in N02.
  - LE LF19 states instances for K7 and K63-U0. These hold only under gcd hypotheses supplied by later nodes.
  - LE LF25 says Sun(2) is "an instance of the granted 'Sun(t), t <= 6' import". That import is the historical package that includes Sun(5)/(6), which S56 LF163–165 and S56 parent erratum v2 m3 exclude.
- **Consequence:** no mathematical effect, because L0.3 and L0.6 have complete elementary proofs (S56 LF40–42, LF47–48). Read literally, though, the root would carry the premise that S56 parent erratum v2 m3 forbids for H5/H6, and it would reach N04/N05 through their N02 edges.
- **Repair:** limit N02's LE body to LF14–18 and LF23–24. Mark LF19 as an instance owned by the consumers, and LF25 as superseded provenance (CR LF64).

**m3: The "deletion" export has no body text** (completeness)
- **Where:** LF52 exports deletion, which S1 (LF295) locates at RM LF25.
  - Neither listed body (S56 LF34–65 or LE E1–E2) states it.
  - CR LF64 discharges README LF21–24 only.
- **In-packet uses:** N05's subset step (CR LF46), and N07/N08's subfamily steps, including S3's "5 of 6".
- **Consequence:** none, since the fact is immediate.
- **Repair:** add one line: "a subfamily of pairwise-disjoint left cosets is pairwise disjoint, with the same subgroups, ambient group and indices."

**m4: N03's "conjugated intersections" clause goes beyond the supplied proof** (completeness)
- **Where:** LF53 cites RM LF27–29 and LFCV LF23 for this clause.
  - S56 LF144–147 proves only indices, intersection indices and disjointness.
  - RM LF29 is not supplied.
  - LFCV LF23 is a review line, not a proof.
- **Consequence:** N06–N08 do not use the clause (S56 LF70, LF159–160). Any downstream user of it stays conditional until it is repaired.
- **Repair:** add one line: "N ⊴ G and N ≤ U_j imply N ≤ xU_jx⁻¹. So (U_i ∩ xU_jx⁻¹)/N = U_i/N ∩ x̄(U_j/N)x̄⁻¹, and the index is preserved." Alternatively, drop the clause.

**m5: Section 3 and row bookkeeping** (bookkeeping; every edge stays forward)
- **(i) LF223:** N06's rows cell cites only R04, a row where N06 is the provider. Its N02/N03 edges are justified by F01 (LF113). Add F01 so that the claim at LF213–214 holds.
- **(ii) LF225:** the N07 edge is declared at S56 LF140–141 together with S56 parent erratum v2 LF6. LF158 and LF160 list no S5W. Add these citations.
- **(iii) LF220:** the edge N02→N03 is not marked as conservative. But S56 LF152 lists R0's inputs as "Lagrange, cores", and LF144–147 use no N02 lemma. Mark it (cons.).
- **(iv) LF113:** F01 lists consumers N03–N59 and discharges "N02, N03". This makes N03 a consumer of itself, and N04/N05 consumers of R0. LF221–222 correctly give N04/N05 no N03 edge, because they are finite-group theorems. Either split F01's R0 half off and restrict it to actual R0 users (here N06–N08), or add conservative N03 edges.

**m6: N01 citations** (process)
- **Where:** LF51 cites "TR LF68 (1)(b)", but section 0 (LF14–46) defines no key TR.
- WV LF60 names Zhu's Sun(3)/(4) without stating a scope, and RM LF15 is not supplied.
- **Consequence:** the scope match itself is unaffected.
- **Repair:**
  - Define TR, with path and SHA, in section 0.
  - Add C56W parent erratum v2 LF7 as N01's literal-scope source.

## Boundary imports and limits

**External import**
- Zhu, arXiv:0807.2207 Theorem 1.1, at the scope stated in C56W parent erratum v2 LF7.
- Its proof and provenance are not certified here (S56 parent erratum v2 LF15).

**Elementary group theory**
- Lagrange's theorem, cores as kernels of the coset action, and the correspondence theorem.

**Accepted bodies, not re-reviewed**
- C5W and C56W (CR LF45–46).
- S56 LF105–141 (S56V LF5–12).

**File co-location check: no cycle at the node level**
- **S56:** R0 sits in section 6 but is used by section 3. Still N03 < N06, and R0 uses nothing from sections 2–5.
- **LE/L:** only E1–E2 enter N02, and the L method is re-proved.
- **RM:** N01–N03 cite only RM LF15–29.
- **C5W/C56W:** handled by m1.

**Not approved:** the global graph/final join, the other packets, full Sun(7), runtime, novelty or priority, and human or Lean status.
