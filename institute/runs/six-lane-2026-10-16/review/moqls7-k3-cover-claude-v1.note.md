DISPOSITION: ACCEPT-WITH-FIXES

Q5 is judged separately because it is an unfrozen draft. Its transport lemma and cut arithmetic are correct, but it needs fixes before any freeze (MAJOR D1–D2).

## FATAL
None. I re-derived the following from the sources; controls and desk excerpts were used only as cross-checks.

**Q1(a) Cube table and units.**
- k3_cubes.py:19-21 matches AMENDMENT-2.r1.md:15-17.
- k3_cubes.py:75-79 fixes all 18 predicates, each with sign [k∈S_a].
- With var(a,(0,k),(1,0)) = 882(a−1)+36k+1, the desk units (desk/cnf-static-excerpts.txt:28-45) are exactly C321.

**Q1(b) Nonemptiness, disjointness, S_1.**
- Nonempty: in row 0's ONB, the (0,0) coefficient of ψ_a,(1,0) vanishes because column 0 is an ONB. Unit norm therefore needs some k in 1..6.
- At the Boolean level, the G3 clause for (row 1, row 0) forces the same (gram_enc.py:105-106; gram_encB.py:166-172).
- Disjoint: G5 (gram_enc.py:115-118).
- S_1 ⊇ {1,2,3}: the --sym units (gram_enc.py:123-125; gram_encB.py:191-193).

**Q1(c) Enumeration and orbits.**
- S_2 and S_3 lie in {4,5,6}, so each of columns 4–6 carries one label in {0,1,2,3}.
- Requiring labels 2 and 3 to appear gives 64−27−27+8 = 18 assignments.
- Under S_{4,5,6}×⟨(2 3)⟩ (order 12) there are three orbits of six:
  - permutations of (0,2,3) → C311;
  - permutations of (1,2,3) → C411;
  - {223,232,322}∪{332,323,233}, joined by the square swap → C321.
- Each stabiliser has order 2 and equals that cube's extra AMENDMENT-3 generator.
- No case is missed: |S_1| ≥ 5, or two unused coordinates, would leave fewer than two coordinates for S_2 and S_3.
- coverage() is correct: k3_cubes.py:44 swaps 0-based 1↔2 (squares 2↔3), :46 uses 1-based labels, and the result matches coverage_r1.json:96-192.

**Q1(d) Residual group and --sym.**
- The residual group fixes square 1, every row, and columns 0–3. It maps each of these families onto itself:
  - G1, which holds by absence;
  - G2 for every (line, pair) on all 14 lines;
  - G3 for every ordered line pair;
  - G5 for every square pair;
  - the G4 family {(a,ℓ) ≠ (1, row 0)}.
- It also fixes the --sym units.
- Encoder auxiliaries are handled: AND auxiliaries are definitional, and G4 guards and B's counters can be re-chosen.
- The --sym WLOG (GRAM-ENCODING.r2.md:89-92) needs only that square 1 is heavy in one own row frame. That holds for every triple that is heavy in every own ONB.
- The simultaneous row/column permutation preserves QLS, tensor orthogonality, ray sets and heaviness.

**Q2(a) G6 cases.** The same-ray argument gives ψ_a,p = cψ_a,q with |c| = 1. The Boolean derivation holds case by case:
- t on row 0: both sides are 0. At t=(0,0) both predicates are absent.
- t off row 0: the common-neighbour count on row 0 equals g(q,t).
  - p and t not collinear: G2's 0-count and 1-count implications give equality.
  - t collinear with p (row 1 or column 0): G1+G2 forbid a count of 1, so g(q,t)=0.
  - t collinear with q (column k, row ≥ 2): the count is 0, so g(p,t)=0.
  - t collinear with both: t is (0,0) or (1,k), both predicates are absent, and the wrapper skips them (k3_cubes.py:91-92).

**Q2(b) Clause level.**
- Encoder A: the AND definitions (gram_enc.py:83-85) give h_r=0 for r≠q and h_q ↔ g(t,q).
  - The zero-count clause (:96) becomes g(t,q) ∨ ¬g(p,t).
  - The one-count clause (:99) becomes ¬g(t,q) ∨ g(p,t), or just ¬g(t,q) when g(p,t) is absent.
  - Each G6 clause is therefore a RUP consequence.
- Encoder B: gram_encB.py:50-55 gives exact ≥1/≥2 equivalences, and s2 is false under the cube.
  - Clauses :153, :157 and :151 yield the same three clauses.
  - The s2=None branch is unreachable because at least five products survive.

**Q2(c) Clause counts.**
- Each singleton yields 70 clauses for every k: 5 from row 0, 5 from row 1, and 12 from each of rows 2–6.
- Totals: 18+140 = 158 for C311/C411 and 18+70 = 88 for C321.
- desk:46-115 matches cube_clauses for q=(0,6) clause by clause, e.g. :51 −1982, :57-58 ±(2017,1988), :67 −2022, :115 −2046.
- The duplicated unit −1801 (desk:40 and :46) is harmless.
- Skipping t ∈ {p,q} loses nothing, since the diagonal Gram value is 1, consistent with the unit g(p,q)=1.

**Q2(d) Variable map.**
- gram_encB.py:111-118 creates no variable before the g loop. It allocates 1..2646 over the same row-major point list and the same row/column collinearity set, in (square, earlier point, later point) order. This is identical to k3_cubes.py:62-65.
- g() normalises pairs by tuple order (:120-123), as k3_cubes.py:73 does.
- desk:316-318 is consistent: the first auxiliary 2647 = 73∧74 = g_1((0,2),(1,0)) ∧ g_1((0,2),(1,1)).
- For encoder A the map is asserted at runtime (k3_cubes.py:112-115).
- The appended literals are therefore correct for every A and B index.

**Q3(a) Generators.**
- Each generator is a bijection (k3_lex.py:50).
- Signed units are preserved iff π(S_a) = S_σ(a), which holds for all 22 generators.
- Every generator fixes square 1, rows 0 and 1, and column 0, so the omitted G4(1, row 0) position stays fixed.
- G6 transports (e.g. square 2 with q=(0,4) ↔ square 3 with q=(0,5) under C311's combined swap) and is implied anyway.
- All generators except C411's columns(3,4) also preserve the base CNF on its own (MINOR 4).

**Q3(b) Action convention.**
- perm[v] is the index of σ(v) (k3_lex.py:49), and each comparator compares X_v with X_perm[v]. For example, desk:283 "−7 13" compares g_1((0,0),(2,1)) with g_1((0,0),(3,1)).
- So Y = X∘σ. This is the Gram pattern of ψ′_{a,c} = ψ_{σ(a),σ(c)}, an actual configuration in the same cube.
- Being an involution does not matter, because the H-orbit is closed under σ and σ⁻¹.

**Q3(c) Comparator semantics and counts.**
- ⇐: set the prefix auxiliaries e_i true up to the first difference (all of them if the vectors are equal) and false afterwards.
- ⇒: at equal positions the two prefix clauses force e_1..e_{j−1} true, so the j-th clause excludes x_j=1, y_j=0.
- The proof is pointwise in X. Shared pairs (v,σv) and (σv,v) are therefore harmless, and identical positions are legitimately skipped.
- The last pair gets no auxiliary, and numbering starts from the header value nv=96978 (k3_lex.py:114-120).
- Each transposition moves 462 predicates per square, 1386 in total. That gives 4156 clauses and 1385 auxiliaries.
- The combined swap moves 462+1764 = 2226 predicates, giving 6676 clauses and 2225 auxiliaries.
- Totals: 31612 clauses and 10535 auxiliaries, so the header is 107513 / 659168 (desk:15). desk:312 ("−107513 −2646 1763") is consistent.

**Q3(d) Coverage.** The lex-minimal member of the H-orbit satisfies every comparator at once, and its base auxiliaries can be reconstructed. No invariance assumption is used.

**Q4(a,c) Composition and certificates.**
- k3_cubes.py:124-132 and k3_lex.py:112-127 copy the body verbatim and only append.
- Headers are consistent:
  - A base: 96978 variables / 627398 clauses (desk:27 is the 42-guard clause), plus 88 or 158 appended.
  - B base: 461370 / 1629644, plus 88 or 158 (desk:7-15).
- k3_cube_certify_r2.py:49-50 regenerates with the pinned wrapper and asserts the screen SHA. The certificate receipts' CNF and metadata SHAs equal the screen receipts'.
- The checker logs parse 96978/627486 (A_C321.checker.log:2) and 96978/627556 (A_C411.checker.log:2). Both end with an exact "s VERIFIED", solver rc 20, checker rc 0, and no safety stop.
- No four-square lemma is used. LEMMAS.md:26-36 is a three-square bound, and the cover derives |S_1| ∈ {3,4} directly.

**Q5(a–c) Transport and cuts.**
- Maps:
  - if ℓ is a column, transpose all three squares first;
  - row permutation ρ sends ℓ to 0 and row(p) to 1;
  - column permutation κ sends col(p) to 0, S_a to {1,2,3,4} (or {1,2,3}), S_b to {5} (or {4,5}), and S_c to {6};
  - relabel squares a, b, c as 1, 2, 3.
- What the image satisfies:
  - the exact 18 literals, because the w's are exact supports on the six non-collinear positions;
  - the --sym units;
  - G1–G3 and G5;
  - every G4 clause, because heaviness in every own ONB is preserved. At the Boolean level too, the source's G4(1, row 0) follows from its --sym units, so every G4 clause transports.
- (4,1,1) reaches C411 and (3,2,1) reaches C321, for every frame, point and square order.
- The forcing argument and the conclusion that only (3,1,1) survives are correct.
- Counts: 588·3·15 = 26460 and 588·6·20·3 = 211680, total 238140, with no auxiliaries. Every literal is an actual non-collinear g variable.
- The clauses are distinct. The square-a literals form a star of at least three edges; its centre is p, and its collinear leaves determine ℓ. Clauses with 4 and 5 literals cannot coincide.
- Overlapping (R,T) need no clause: any r in R∩T is already excluded by G5's ¬g_a(p,r) ∨ ¬g_b(p,r).

## MAJOR
Q1–Q4: none. The following apply to the Q5 draft only.

**D1. AMENDMENT-4.md:8, :23, :28 — the bridge prerequisite is missing.**
- The C321/C411 CNFs impose G4 on every (square, line) except (1, row 0).
- A transported configuration satisfies them only if the source triple is heavy in every own ONB. That is justified only for a minimal triple, i.e. after K1 (accepted) and K2 (pending) are excluded (GRAM-ENCODING.r2.md:52-62; LEMMAS.md:75-78).
- The draft never says so; "surviving heavy K3 configuration" (:28) silently assumes it.
- *Correction:* add a hypothesis paragraph: "valid only under the G4 bridge: K1 accepted, K2 parent-accepted, encoder G1–G5 bridge accepted; K3 only (14 row/column lines, no L symbol lines; not for non-minimal configurations)."

**D2. AMENDMENT-4.md:3-4, :20, :22-23, :33-34, :50-51 — certificates are presented as exclusions, and the gate is too weak.**
- A producer DRAT certificate (cert_r2/A_C321.json:20-25; A_C411.json:20-25) shows UNSAT of one exact A-encoded CNF and nothing more.
- "contradicting its UNSAT certificate" and "previously checked cube exclusions" overstate this.
- §3.1 gates on "successful … certificate receipts". It does not require parent acceptance (hash chain, regeneration, encoder bridge), and it does not say whether the pending B route is required.
- *Correction:* gate on "parent-ACCEPTED exclusions of the exact C321 (d598…8388) and C411 (2b92…ddf2) CNFs, under the stated A-only or A+B standard, with K2 accepted". Rephrase the contradictions as "contradicting the accepted UNSAT of that CNF".

**Required before any final use of the cuts:**
1. K1 accepted and K2 parent-accepted, so that G4 holds for K3.
2. Accepted G1–G5 encoder bridge(s), plus the B-map erratum (MINOR 2) if B is used.
3. Accepted cover and --sym WLOG (AMENDMENT-2 §1).
4. Accepted C321 and C411 certificates.
5. A reviewed transport lemma (as corrected) and a reviewed cut generator: literal map per encoder, exactly 238140 distinct clauses, output SHA bound, and the §3.3 control.
6. If the cuts are combined with the AMENDMENT-3 lex comparators, an explicit statement that the cut family is H-invariant (MINOR 14).
7. A new, regenerated, DRAT-checked UNSAT of the exact strengthened C311 CNF, on the protocol's independent route(s). The old cube proofs certify nothing about it.
8. A parent review of the full composition: K1∧K2 ⇒ G4 ⇒ --sym ⇒ three cubes ⇒ {C321, C411 accepted; transport ⇒ cuts; C311+cuts certified}.

## MINOR
1. **AMENDMENT-2.r1.md:10, :31 — incomplete nonemptiness wording.** "Row 0 is an ONB" and "exactly one nonzero coefficient" omit that the (0,0) coefficient is zero by G1 (column 0). Add it.

2. **AMENDMENT-2.r1.md:43-45 vs k3_cubes.py:59-60, :117-126 — B's map is not read or confirmed at runtime.**
   - "reads each encoder's actual g-variable order … must confirm" is false for B. The wrapper hard-codes the map and checks only nv ≥ 2646 (:126).
   - Index identity does hold by static reading (Q2(d) above).
   - desk:24 (A and B appended blocks byte-identical) is tautological, since one vmap serves both; it is not evidence.
   - *Correction:* record an erratum. Before relying on any B certificate, add a runtime oracle that leaves B untouched. Options: drive B's own --fix-json branch (gram_encB.py:203-215, which emits signed units in allocation order) with probe patterns, or replay the product-definition references (the desk:316-318 pattern) against variable_map.

3. **G6-G2-DERIVATION.r1.md:8, :12 — two imprecise sentences.**
   - At :8, t=(0,0) is absent by G1, not fixed by the cube.
   - At :12, for collinear (p,t) the text should read "G1+G2 forbid a count of 1, so g(q,t)=0", not "gives g(p,t)=1".
   - The conclusions at :14 and :21 are right; only the wording needs changing.

4. **AMENDMENT-3.r1.md:10, :20 — the invariance argument omits the --sym units and the G4 omission.**
   - C411's columns(3,4) (k3_lex.py:33) sends the --sym unit 109 = g_1(p,(0,3)) to 145 = g_1(p,(0,4)), which is not a base unit.
   - That generator preserves the cube CNF only because 145 is a positive C411 cube unit; it does not preserve the base CNF.
   - *Correction:* state that all generators fix square 1 and row 0, that the --sym units are implied by the cube units, and that invariance is of the cube CNF's g-projection.

5. **AMENDMENT-3.r1.md:25-28 — T(X) is undefined.** Define Y_v = X_σ(v), as implemented (k3_lex.py:49, :120).

6. **explore/k3lex/A_C311.meta.json:4-7 vs AMENDMENT-3.r1.md:46 — incomplete binding.**
   - The lex metadata binds neither the source-cube metadata SHA (3b2ab04f…) nor the control-receipt SHA; it records only an in-process "PASS" (k3_lex.py:110, :132).
   - Both are recoverable via explore/k3cubes/screenA_r1/A_C311.json:16-17 and AMENDMENT-3.bindings.r1.json:8.
   - *Correction:* add a sidecar binding.

7. **AMENDMENT-3.bindings.r1.json:16-18 — stale certificate-driver binding.**
   - The binding names k3_cube_certify.py (0b291d74…, caps "1800/3600").
   - Both receipts were actually produced by k3_cube_certify_r2.py at 3600/3600 (cert_r2/A_C321.json:9, :18, :47).
   - Authority rests on the omitted K3-CERTIFICATION-DRIVER-DELTA.r2.json (GRAM-ENCODING.r2.md:15-16), which no receipt references.
   - The parent must check that this delta predates 21:39:49 (A_C321.json:2) and bind it.

8. **AMENDMENT-3.r1.md:3 vs AMENDMENT-3.bindings.r1.json:2, :14 — freeze order.**
   - The text says "frozen before the new inputs", but the freeze record already contains the input SHA, so generation came first.
   - This is harmless (the output is deterministic and bound) but should be recorded.
   - Similarly, g6_controls_r1.json:2 (20:15:24) postdates the AMENDMENT-2 freeze and the first screen start. It is unbound but not load-bearing.

9. **Missing K1/K2 prerequisite statements.**
   - The prerequisite is absent from AMENDMENT-3 (e.g. :49) and from the receipt scope fields (cert_r2/A_C321.json:61; A_C411.json:61).
   - AMENDMENT-2.r1.md:5 cites the r1 bridge, whose G4 reference was K1 §8 (gram_enc.py:15-16). That was corrected in GRAM-ENCODING.r2.md:26-27 and LEMMAS.md:69-78.
   - *Correction:* cite r2/LEMMAS and add "conditional on K2 acceptance".

10. **GRAM-ENCODING.r2.md:136-138 — stale status line.** It also suggests certification alone makes an exclusion. Reword to "until certified, parent-accepted and composed with the K2-dependent bridge".

11. **AMENDMENT-4.md:33 — unqualified conclusion.** "Every heavy occurrence" must read "every heavy occurrence in an own row/column frame". Nothing follows for other ONBs, because disjointness of the three supports is a line-frame consequence of G5.

12. **AMENDMENT-4.md:18-20, :22-23 — under-specified maps.**
    - Specify the label/column correspondence: b becomes square 2 with S_b sent to {5} (or {4,5}); c becomes square 3 with S_c sent to {6}.
    - Note that the image satisfies the --sym units (S_1 ⊇ {1,2,3}) and that the target CNF does not impose G4(1, row 0).

13. **AMENDMENT-4.md:13 — w_a ≥ 1 is asserted without proof.** Justify it by unit norm plus G1, or by Boolean G3.

14. **AMENDMENT-4.md:61 — "selected C311 instance" is ambiguous.**
    - If the cuts are appended to the lex CNF, state that the cut family is invariant under every row, column and square permutation, hence under H, so AMENDMENT-3.r1.md:33-36 still applies.
    - §3.3 (:55-57) should also check clause distinctness and the per-encoder literal map.
    - Cosmetic: missing spaces at :37 and :44-45.

15. **Non-load-bearing log hash.** explore/k3lex/screenA_r1/A_C311.json:20 has the same solver-log SHA as explore/k3cubes/screenA_r1/A_C311.json:19, although the return codes differ (−15 vs 0). Identical one-line logs are plausible; the desk should confirm their content.

## Status

| Q | Status | Reason |
|---|---|---|
| Q1 | SOUND | 18 assignments in three 6-orbits; residual group and --sym WLOG preserve all base semantics; wording nit only (m1) |
| Q2 | SOUND | G6 follows from G1/G2 plus units in every case, for both encoders; 70/158/88 match the desk; B map correct by static reading, §3 wording needs an erratum (m2) |
| Q3 | SOUND | 22 generators stabilise the cube CNF; comparator ⇔ X ≤lex X∘σ; counts exact

; lex-min coverage valid; documentation gaps (m4–m5) |
| Q4 | REQUIRES-FIXES | CNF composition, headers and regeneration correct; binding gaps (m6–m8); missing explicit K2 prerequisites and overstated certificate wording (m9–m10) |
| Q5 | REQUIRES-FIXES | Transport, forcing, (3,1,1) conclusion and 238140 distinct auxiliary-free clauses correct; needs prerequisites and acceptance gate (D1–D2), frame qualifier, map specification and lex-compatibility statement (m11–m14) |

## Scope

**Read in full (every inlined file):**
- AMENDMENT-2.r1 and AMENDMENT-3.r1, with their bindings.
- The G6 addendum and the AMENDMENT-4 draft.
- k3_cubes.py, k3_lex.py, gram_enc.py, gram_encB.py and k3_cube_certify_r2.py.
- All cube and lex metadata, plus the screen and certificate receipts.
- The coverage, G6 and no-duplicate receipts.

**Read as numbered excerpts:**
- GRAM-ENCODING.r2 §§1–3 and 5–6.
- LEMMAS C0, C1, W, Lemma 10 and G4.
- lex_controls, and the heads and tails of the checker logs.
- Desk sections A–C and E–F.
- K2-THEOREM.r2 and the K1 parent verdict.

**Re-derived by hand:**
- Variable indices.
- The 18 assignments and their orbits.
- The 70-clause G6 pattern.
- Moved-predicate and comparator counts, and the comparator semantics.
- The transport maps, and the cut counts and their distinctness.

**Could not check:**
- CNF bytes beyond the desk excerpts, including desk §D; the A_C311 158-line block is known only by its hash.
- The DRAT proofs and the solver and checker binaries.
- proof_stream.py and gram_certify_r4.py.
- The driver-delta JSONs, notably K3-CERTIFICATION-DRIVER-DELTA.r2.json.
- GRAM-ENCODING.r2 §§4 and 7, and the LEMMAS K1-frame section.
- The checker WARNING lines and g6_controls.py.
- The restarted lex screen, and any B solver or certificate run.

**Relied on without re-checking:** soundness of the base encoders' G1–G5 encoding is taken from its separate review, except where re-derived above.

This review gives no K3 verdict, no M(7) value, and no novelty or priority statement.
