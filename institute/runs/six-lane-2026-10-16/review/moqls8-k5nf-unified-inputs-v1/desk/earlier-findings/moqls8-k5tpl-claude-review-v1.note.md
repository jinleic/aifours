DISPOSITION: K5TPL-r1=ACCEPT; K5NF-r3-IMPORTS=ACCEPT-WITH-FIXES

This is a static reading of the packet only; nothing was executed. Solver and DRAT facts are used only as the parent states them: 122 roots PASS including c112, and six roots are UNKNOWN (`parent/moqls8-k5-root-parent-verdict.md:5,19`). Nothing below excludes K4 or K5.

Abbreviations: TPL = `review/K5_COLUMN0_TEMPLATE_COVER.r1.md`; IMP = `review/K5_RESIDUAL_NORMAL_FORM.r3-IMPORTS.md`; SND = `review/K4K5_ENCODING_SOUNDNESS.r3.md`; BX = `desk/BINDING_EXTRACT.json`; DC = `desk/DESK_CHECKS.json`; AUD = `parent/moqls8-k5-root-cover-audit-v1.md`; VER = `parent/moqls8-k5-root-parent-verdict.md`.

## K5TPL-r1 (TPL)

**FATAL:** none. **MAJOR:** none.

**MINOR** (none affects correctness; fold the fixes into the semantic-template manifest):

1. **TPL:59-64 — residual action not written out for the larger group.**
   - The note delegates the residual action to IMP, but IMP's explicit action (IMP:63-70) covers only σ fixing 1, 2, 3.
   - IMP's claim "Q1(1,0) fixed as a vector" (IMP:67) is false under Sym(A).
   - The proof survives: TPL:62 weakens this to "as a SET", and SB2 is support-only (`code/gram_a.py:276-281`).
   - Standard-form preservation and the relabelling are still not stated for Sym(A)×Sym(B).
   - Fix — write out each step:
     - Q′_s(i,σ(j)) = P_σ Q_s(i,j), which is move (β) at SND:104-105.
     - Hence Q′_s(0,σ(j)) = |σ(j)⟩.
     - supp Q′_1(1,0) = σ(A) = A.
     - Relabel s ↦ σ(s+2)−2; this is a bijection on 2..5 because σ(B) = B.
     - Then sort rows 2..7.
2. **TPL:111 and TPL:119-120 — wrong class named.**
   - The note says "every genuine K5 configuration" and "would exclude genuine K5".
   - The argument starts from the reduced class, and the bridge's P4 needs it (SND:17-21; VER:7).
   - Fix: write "member of the reduced class K5, after the accepted standard-form/SB2 moves".
   - State the conclusion as "reduced K5 = ∅", with K4 and Problem 16 untouched.
3. **TPL:112 — c112 cited through a document under review.**
   - The c112 refutation is cited via r2 §4, which is itself under separate review.
   - Fix: cite the accepted import directly:
     - VER:5,19 (c112 is not among the six UNKNOWN roots);
     - the manifest 65f6e0dd…3b5e and the `all/` mapping (AUD:99-104);
     - the root units [−57,−106,−155,−204,+253,+302,+351].
4. **TPL:44-47 — one sub-case left implicit.**
   - The case "only w has an extra neighbour" is covered only by symmetry.
   - Fix: add "WLOG v; if only w had z, then N(x)∩N(z) = {w}."

**T1 (TPL:9-20) — correct.**
- Let a_p be the cell of l collinear with p. Then ⟨Ψ_s(a_p),Ψ_s(p)⟩ = 0, so S_s ⊆ l∖{a_p}, which has 7 cells.
- S_s is nonempty: l is an orthonormal basis and Ψ_s(p) is a unit vector.
- S_s ∩ S_t = ∅ for s ≠ t, by Prop 1 applied to the distinct cells a and p.
- Five nonempty, pairwise disjoint subsets of 7 cells force |S_s| ≤ 3.
- Row-0 frame, p = (i,0), excluded cell (0,0): this bounds column i of U.
- Column-0 frame, p = (0,k), excluded cell (0,0) (same row): {i : U[k,i] ≠ 0} is Q1's column-0-frame support of (0,k). This bounds row k of U, and it is nonempty.
- U[0,i] = δ_{i0} and U[k,0] = δ_{k0}, by the column-0 and row-0 bases.
- U is a change-of-basis matrix, hence unitary, so U = [1]⊕U′ with U′ unitary.
- Column 1 of U is A, by `gram_a.py:276-281` (the first SB2 part is [1,2,3]).

**T2 (TPL:24-55) — complete; no counterexample exists.**
- **Singleton rule:** one common nonzero gives a single nonzero summand, which is impossible for orthogonal rows, or for orthogonal columns.
- **Rank:** a component's rows are orthonormal vectors supported on its columns, and vice versa, so both sides have equal size.
- **Degree 1:** gives K11.
- **Degree-2 row {x,y}:** N(x) = N(y) = R.
  - If |R| = 2, an extra neighbour z of v would give |N(x)∩N(z)| = 1. So the component is K22.
  - If |R| = 3, any extra neighbours of v and w coincide (call it z), and N(z) = {v,w} is closed. That gives K33−e.
  - Otherwise the component is K32, which the rank argument excludes.
- **Degree-2 column:** the transpose argument applies, and K33−e is self-transposed.
- **All degrees 3:** there are 6 further incidences on {a,b,c}, and each other row uses at least 2 of them.
  - A 3+3 split gives K33.
  - A 2+2+2 split forces each pair ab, ac, bc exactly once.
  - Non-singleton intersections then force x = y = z.
  - deg x = 3 closes the component as K44−PM.
- All five types are realizable, so the list is tight (not needed for the proof).

**T3 (TPL:57-77) — correct, apart from MINOR 1.**
- **The group:** Sym(A)×Sym(B) is exactly the stabiliser of 0, A and B.
- **Preserved properties:** standard form, SB2 (as sets, after relabelling), P4 and reduced K5. The row-0 weights are relocated, not changed.
- **Row sort:** it fixes rows 0 and 1.
- **No other symmetry breaking:** F's only symmetry breaking is the 35 SB2 units plus ROWLEX (BX:33), and P4 is in row 0 only (BX:29). ROWLEX is re-established, not assumed invariant.
- **Case split is complete:**
  - Column 1 has degree 3, so its component is K33, K33−e or K44−PM.
  - The coordinate sets are A, A, or A∪{b}.
  - b ≠ 0 because U = [1]⊕U′, so b ∈ B.
  - In K33−e, column 1 is a degree-3 column, so the other two columns are A and A∖{a}.
- **P1 reachability:** σ ∈ Sym(A) with σ(a) = 1 gives {2,3} and touches only A.
- **P2 reachability:** σ ∈ Sym(B) with σ(b) = 4; afterwards only Sym({5,6,7}) is used, so the A component is undisturbed.
- **ROWLEX positions:**
  - Bits are c = 1..7, with c = 1 most significant.
  - A pure-B vector has bits 1–3 zero. An A-meeting vector has a 1 at its first A-bit, so it is strictly larger.
  - Within the A-meeting columns: 0110000 < 1110000, and 0111000 < 1011000 < 1101000.

**T4 (TPL:79-113) — all 16 templates re-derived independently; they match and each is non-decreasing.**

| Case | Rows | Bit vectors (c = 1..7) |
|---|---|---|
| B1 | 2–5 | 0000001, 0000010, 0000100, 0001000 |
| B2 | 2–5 | 0000001, 0000010, 0001100 ×2 |
| B3 | 2–5 | 0000011 ×2, 0001100 ×2 |
| B4 | 2–5 | 0000001, 0001110 ×3 |
| B5 | 2–5 | 0000001, 0000110, 0001110 ×2 |
| B6 | 2–5 | 0000111, 0001011, 0001101, 0001110 |
| P0 | 6–7 | 1110000 ×2 |
| P1 | 6–7 | 0110000, 1110000 |
| C1 | 2–4 | 0000001, 0000010, 0000100 |
| C2 | 2–4 | 0000001, 0000110 ×2 |
| C3 | 2–4 | 0000011, 0000111 ×2 |
| C4 | 2–4 | 0000111 ×3 |
| P2 | 5–7 | 0111000, 1011000, 1101000 |

- **Reachability:**
  - Singletons are mapped rightmost.
  - Two K22 blocks are mapped to 45 and 67.
  - The missing coordinate of a K33−e block is mapped leftmost: 4, or 5 in C3.
  - I_n and K44−PM need no choice.
- **Block lists:** complete. They are the partitions of 4 and 3 into blocks of size 1–4; size 3 has two types and size 4 has only K44−PM.
- **Labels (Σ 2^(c−1) on row 2):** {7}→64, {6,7}→96, {5,6,7}→112.
  - c112: P0-B6, P1-B6, P2-C4 (exactly three).
  - c096: P0-B3, P1-B3, P2-C3 (exactly three).
  - c064: the remaining 10.
- **Cover:**
  - Each normalised reduced-K5 configuration satisfies F plus its template's 42 units, by the bridge in hypothesis form (IMP:16-20, which is valid).
  - The c112 templates also satisfy the seven c112 root units, which are refuted.
  - So: 13 template formulas UNSAT, plus c112, the theorem and the bridge, implies reduced K5 = ∅.
  - This is a genuine-vector cover only, as TPL:122-123 states; it is not a Boolean cover of F.
- **Imports:** only completeness is needed; realizability is not (an unrealizable template's formula must still be UNSAT). Nothing is imported beyond the stated list.
- **Cross-check with r2:** r2's projection lemma is not used, but its conclusion is recovered. Every template has at least 3 pure-B rows, and row 2 is C_k.

**T5 (TPL:115-126) — sufficient and correctly scoped.**
- The 42 units are exactly V1–V6 (DC:107-160; `README.md:186-187,210-212`).
- Independent replay is required, consistent with VER:35.
- The semantic-template manifest is separate, and no old leaf is promoted.
- The K4 caveat is right: K4's sort fixes L(i,0) = i (SND:112-114), so Q1's column-0 rows cannot be sorted. The degree bound itself would survive in K4, since L is a QLS.

**Correctness, novelty and significance (separately):**
- **Correctness:** the proof is complete and correct.
- **Novelty:** low. It is an elementary combinatorial-orthogonality lemma applied to a lane-specific transition matrix.
- **Significance:** conditional. It reduces the open genuine-vector obligation from two root subtrees to 13 formulas with all 42 column-0 literals fixed. How hard those formulas are is unknown.

## K5NF-r3-IMPORTS (IMP)

**FATAL:** none. **MAJOR:** none.

**MINOR:**

1. **IMP:59 — "These meanings are independently checked" overstates the receipts.**
   - Binding C9 checks only that the V1 ids name g_1((0,k),(2,0)) for k = 1..7. It is labelled "list semantics only" (BX:40-41; `parent/moqls8-encoder-parent-integration-v1.json:18`).
   - AUD checks that a literal is positive exactly when the corresponding index bit is set (AUD:20-23). This is a declared-mapping comparison (AUD:83,152).
   - Together these support the V1 decoding and the label Σ 2^(c−1).
   - Neither checks the ROWLEX orientation, False < True, or non-strictness. C7 binds only location and counts (BX:33); C3 binds only lexeq equivalence (BX:17).
   - So IMP:58 rests on `gram_a.py:248-270` alone.
   - Fix: attribute each item to its own source.
2. **IMP:22-24 — the "full active families" list is incomplete.**
   - It omits AND_DEF (the b3/c4 definitions, 1,411,200 clauses; BX:59).
   - It omits the u5, w3 and lexeq auxiliaries (BX:85-92).
   - G1 appears only as "Gram constants".
   - The symmetry-breaking claim itself is correct (C7).
   - Fix: list the families exactly as bound.
3. **IMP:16-20 and IMP:26 — "EXACTLY three hypotheses" is a valid reformulation, not text that is "explicit in §§2–3.1, 5–6".**
   - The source states the bridge "after the lossless moves of §5" (SND:10-11).
   - "Exactly" additionally needs:
     - §4: G2–G5 hold for every QLS (SND:94-101);
     - §1 and §6: P4 follows from the class definition (SND:17-21, 117-119);
     - C7: "nothing else".
   - Fix: cite these sections.
   - Also add the fixed-point remark: a reduced-K5 configuration that meets the three hypotheses is its own output of the §5 moves, with identity choices.
   - Hypothesis 1 is interpretive only, since no clause depends on it. That is harmless.
4. **IMP:5-6 and IMP:33 — unpinned references.**
   - The advisory and the binding receipt are cited without hashes. The desk had to supply dce638a9…6112 and c8aeaa56…53bb (DC:74-97).
   - The verdict summary attributed to the advisory cannot be verified from pinned sources.
   - Fix: pin both hashes and mark the summary as a self-report.

**T6 item checks:**
- **Reduced-K5 definition (IMP:11-14):** matches SND §1, the m = 5 branch ✓.
- **Invariance (IMP:35-38):** holds under row permutations fixing row 0, move (β) with P_σ, and square relabelling ✓. Relabelling is not in SND §5's list, but it is trivially lossless for an unordered set (IMP:14).
- **Hypotheses and symmetry-breaking list:** correct in substance; see MINOR 2 and 3. Flags and hashes ✓ (DC:4-72; SND:44-46).
- **ROWLEX (IMP:42-51):** matches `gram_a.py:250-270` exactly.
  - i runs over 2..6, with k = 0 most significant.
  - The clause [¬e_{k−1}, ¬A_k, B_k] gives False < True.
  - The full-equivalence lexeq chain gives a non-strict order with no secondary key.
  - The k = 0 bit is identically false (`gram_a.py:130-131`), which forces lexeq(i,0) by a unit. This matches the five ROWLEX/e0_unit clauses (BX:82).
- **V1 ids and labels 64/96/112 (IMP:53-58):** ✓ (`README.md:186-189`; DC:107-115; AUD:127-129; r2:73).
- **"Independently checked" (IMP:59):** only partially supported; see MINOR 1.
- **Residual action and relabelling formula (IMP:63-70):** ✓, but only for r2's σ ∈ Sym(B) fixing 0–3. TPL must not reuse IMP:67 (see TPL MINOR 1).
- **Final bridge statement (IMP:72-75):** ✓, conditional on r2 §§2–3, which are not adjudicated here. The c112 import matches what the parent states, and no Boolean transfer is claimed.

**Correctness, novelty and significance (separately):**
- **Correctness:** the substance is correct; the attributions need the fixes above.
- **Novelty:** none.
- **Significance:** documentary. TPL:59 depends on IMP's correct substance (§§1–2), not on its attributions. Even so, land these fixes before the template manifest pins IMP.

K5TPL-r1 FATAL=0 MAJOR=0 MINOR=4
K5NF-r3-IMPORTS FATAL=0 MAJOR=0 MINOR=4
