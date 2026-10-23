DISPOSITION: ACCEPT-WITH-FIXES

**Scope.** This was a static reading of the pinned inputs only. Nothing was executed, hashed or replayed. "✓" means I derived it by hand from the inlined text.

## FATAL

None. Each target follows from the written arguments plus the computational assumptions listed at the end:
- Theorem K1 (`review/K1-THEOREM.r1.md:114`)
- both corollaries (`:115–116`)
- the §8 reduction (`:133–145`)

I found no counterexample to any mathematical step.

## MAJOR

None. Two candidate gaps are provenance problems that have redundancy, so they appear below as MINOR items and as explicit trust assumptions:
- **No receipt binds `evidence/nets7_classes.json` to `code/net_canon.c`.** The non-maximal |par| values can be checked by hand (see (d)), so only classes 0–4 depend on this computation.
- **The A summary records no hash for its driver.** Encoder B reproduces A's model lists, and B's summary records its own hash.

## MINOR

### Provenance and hashes

1. **Wrong driver digest.** `review/K1-THEOREM.r1.md:64` prints `e61ab812…3c7e`. The manifest records `e61ab812…c33c7e113`, ending `e113` (`manifest.json:224–232`); `3c7e` is a mis-slice at offset 57.
   - In addition, `evidence/k1A/summary.json:4–6` binds `k1_sat.py` but not the driver that did the blocking, model parsing and verdict.
   - Fix: print `e61ab812…e113`. On any rerun, record `k1_certify_sha256`; otherwise state that pipeline B (self-hash at `summaryB.json:4`) is the bound pipeline.

2. **Wrong baseline digest.** `README.md:7` prints `a39911fd…ff3a2`; the manifest records `…446a3ff2`, ending `a3ff2` (`manifest.json:408–417`). This is a transposition. Fix it; it is outside the K1 mathematics.

3. **Solver versions have no receipt.** "CaDiCaL 3.0.1" and "kissat 4.0.4" at `review/K1-THEOREM.r1.md:64–65` are unsupported (`manifest.json:459`).
   - Fix: drop them, or add that soundness does not depend on which solver ran. Enumerated models can only over-approximate, and only the final UNSAT matters, which is DRAT-checked.

4. **drat-trim control misdescribed and unreceipted.** `review/K1-THEOREM.r1.md:70–71` says "an UNSAT CNF with the empty proof".
   - `env/drat-trim/ctl_unsat.drat:1` is `0`, an explicit empty-clause step, not an empty proof.
   - Neither control has a recorded output (`manifest.json:458`).
   - Fix: say "with the one-line proof `0`", and either pin the outputs or delete the sentence.

5. **Unsupported exploration numbers.** At `review/K1-THEOREM.r1.md:110–111`, "97 independent contradictions" and "minimum-size … found by MILP" rest on the unpinned `code/k1_phase.py` (`manifest.json:440–442`) with no recorded output.
   - The count 315 is correct by hand: 126 + 189 = 315.
     - Class-0 lines: 6 lines × C(7,2) = 126 pairs. Every overlap there is exactly 2, because {2,4,5,6

} is a (7,4,2) difference set.
     - Lines of classes 1–3: 21 lines × 9 = 189. Each such line has 15 off-frame pairs. A pair with ratio x′/x ∈ {2,4,6} overlaps in 2 coordinates; a pair with ratio in {3,5} overlaps in 3.
   - Fix: label 97 and the MILP minimum as unverified exploration that the theorem does not use.

6. **Missing `review/LEMMAS.md`.** It is cited at `README.md:23`, `code/k1_sat.py:8`, `:15`, `code/k1_encB.py:4` and `code/pattern_check.py:2`, but is absent (`manifest.json:457`). The claim itself does not need it. Fix: add the file or remove the references.

### Exposition and citation

7. **Sets versus lists.** `review/K1-THEOREM.r1.md:46`, `:57`, `code/net_canon.c:4` and `:7` say "reduced lists … Theorem 3.2 with Tables 5–6".
   - Theorem 3.2 (`sources/1406.3681v2.layout.txt:382–388`) and Tables 5–6 (`:721`, `:776`) count reduced **sets**. Lists are Tables 7–8 (`:804`, `:860`).
   - This is harmless numerically. Theorem 3.1 (`:361`) gives RL = (k−1)!·RS = RS at k = 2, and the Equality entries coincide: 341880 at `:708`/`:791`, 342480 at `:755`/`:839`.
   - Fix: write "reduced sets (= reduced lists, since (k−1)! = 1)".

8. **|par| is not a minimum.** `review/K1-THEOREM.r1.md:43–44` says |par| was computed "as a minimum over all 846720 normalisations".
   - The minimum is the canonical key. |par| is 846720 divided by the number of distinct reduced lists (`code/net_canon.c:71–74`).
   - Fix: reword, and add the free-action argument from (d).

9. **Incomplete trust base.** `review/K1-THEOREM.r1.md:58–60` lists only the published counts and the |par| computation. Completeness also needs the following:
   - net_canon's keys must be true lexicographic minima. Classes 1 and 2 both have |par| = 6, so their non-isomorphism rests on the keys, or on the transversal counts 2 vs 1, which are also uncertified.
   - net_canon must be implemented correctly.
   - The JSON records neither net_canon's hash nor its raw output, and the generator of the JSON ("squares_tried": 1038) is unnamed.
   - Fix: "Trust base: EW Table 5/6 totals; un-receipted `net_canon.c` (cf1cae5a…) outputs (|par| and keys) for classes 0–4."

10. **Straightening, the ray criterion and C0 are asserted without proof** at `review/K1-THEOREM.r1.md:15–18`. Add three short arguments:
    - **Straightening.** A single square's classicality depends only on its set of entries, since row/column permutations do not change that set. So a square is classical iff its entries lie, up to phase, in one ONB. A separate unitary per square (set isotopy (iii)) then straightens L1 and L2 in place to phase·|a_s(i,j)⟩, with each a_s a Latin square. No cell permutation is used, and Ψ is untouched.
    - **Ray criterion.** Row 0 supplies 7 rays. If there are exactly 7, every entry is parallel to a row-0 vector, so the square is classical. Conversely, a classical square has at most 7 rays.
    - **C0.** C0 (a set is classical iff each square is) is used implicitly at `:142`. It follows from (iii) acting per square.

11. **Word-proof citations are off.** At `review/K1-THEOREM.r1.md:103–104`, "Rows 1–3 give" uses only rows 1 and 3, and "Rows 5–7 give" uses only rows 6 and 7. Rows 2 and 5 enter in the next sentence. Fix the row references.

12. **Case split in §8 needs care.** At `review/K1-THEOREM.r1.md:142–143`, when |Q| = 1 the chosen Ψ must be the element of Q.
    - Otherwise, if a non-classical weight-2 square outside Q were picked, "the other two" would include the weight-≥3 square, and Lemma 10 would not apply to it.
    - The sequential step should also be stated.
    - Fix: "If Q = {Ψ}, take that Ψ; if Q = ∅, take any non-classical Ψ (C0). Classicalize Ψ′, then Ψ″, which still has all weights ≤ 2 and is orthogonal to Ψ′_c."

13. **Control C1 overstates what F1–F4 do.** At `review/K1-THEOREM.r1.md:122–123`:
    - The 84 rejected mutations are exactly the 42 × 2 additions of a frame-forbidden coordinate. Each fails F2 against the collinear frame point.
    - All 210 removals pass. In the weight-5 Ψ(f) pattern every collinear overlap is at least 3, and every coordinate off ℓ0 is covered 5 times, so no single removal can trigger F2–F4.
    - C1, C2 and C4 test the evaluator in `code/pattern_check.py:19–42`, not the CNF encoders, which are hard-coded to 4-nets of order 7.
    - Fix: say so. The encoders' claim not to over-constrain rests on code reading, on A/B agreement, and on both rediscovering every classical pattern and the weight-4 pattern.

## Checklist

### (a) Reformulation — ✓

- **C1.** ⟨ψ⊗|L⟩, ψ′⊗|L′⟩⟩ = ⟨ψ,ψ′⟩·δ(L,L′). Phases are irrelevant, and n orthonormal vectors in Cⁿ form an ONB.
- **Straightening and >7 rays.** Both hold (item 10). No forbidden independent cell permutation is needed.
- **Net isomorphism suffices.** The reduction never transports MOQLS sets. It goes: K1 ⇒ the 4-net (rows, columns, L1, L2) carries a non-classical ONB-assignment.
  - That property (every line an ONB, more than 7 rays) is invariant under any point bijection mapping lines to lines, including permutations of the parallel classes.
  - Paratopy classes of 2-MOLS lists are exactly 4-net isomorphism classes: OA columns are classes and symbols are lines (`1406.3681v2:143–150`).

### (b) Frame lemma and F1–F4 as necessary conditions — ✓

- **Distinct meeting points.** Suppose r_c = r_{c′} for c ≠ c′. Then p and r_c share two lines of different classes, so p = r_c ∈ ℓ0, a contradiction.
- **Distinct labels.** Class-1 labels biject ℓ0, so the three excluded coordinates are distinct and |A(p)| = 4.
- **Scope.** The lemma holds for every support, not only full ones, and frame points are fixed to {label}.
- **F2 at frame points.** F2 between a frame point and a collinear point re-derives the frame lemma, which is consistent.
- **F3/F4.** Take the line's vectors as rows. A coordinate covered once has an entry of modulus 1, so that row vanishes elsewhere.
- **Direction of F4.** "Covered once ⇒ weight 1" is the correct direction. The converse follows from F2, so it need not be encoded.

### (c) Encoders, blocking and evidence — ✓

- **Encoder A** (`k1_sat.py:62–92`, with w3 = hall = False per `k1_certify.py:52`) is an exact encoding.
  - Variables exist only on A(p).
  - Frame points get unit clauses (`:66`); F1 is at `:68`.
  - For F2, each auxiliary satisfies o ⟺ x_p ∧ x_q (`:77–79`). Both directions are needed: o → x stops a spurious second overlap.
  - F2 then adds "o_k ⇒ some other o_{k′}" (`:81`), i.e. |overlap| ≠ 1.
  - F3 is at `:88` and F4 at `:89–92`.
- **Encoder B** (`k1_encB.py:50–75`) is also exact.
  - It uses all 15 nonempty subsets of A(p), with at-least-one plus pairwise at-most-one.
  - F2 is encoded as forbidden pairs, F3 directly, and F4 as its contrapositive.
- **Empty clauses are dead code.** The branches at `k1_sat.py:85–87` and `k1_encB.py:71` never fire on any 4-net:
  - On ℓ0, each coordinate has cover 1.
  - On a class-c line (c ≥ 1) through the frame point r with label j, coordinate j is covered only by r. Any k ≠ j is excluded by exactly two off-frame points (one per other class through the frame point s_k, distinct and ≠ r), so its cover is 4.
  - On class-0 lines other than ℓ0, exactly three points exclude k, so its cover is 4.
- **Blocking clauses.**
  - A's clause (`k1_certify.py:62`) is the full x-assignment. It removes exactly the recorded assignment, even if parsing had been wrong.
  - B's clause (`k1_encB.py:104`) uses only negative literals. It removes exactly one assignment only if `chosen` contains one option per point. Every recorded B model lists 49 entries, one per point, so this holds for the recorded lists.
- **Why final UNSAT proves completeness.** An unlisted projected model of the base CNF differs from every listed model, so it satisfies every blocking clause, and base + blocks would be SAT. Hence UNSAT of the final CNF (assuming it equals base + recorded blocks) means the list is complete. Validity of the listed models is not needed, since over-approximation is harmless; C3 confirms the 18 models anyway.
- **A and B agree, entry by entry.**
  - Class 5:
    - A at `summary.json:105–153`, `:156–204`, `:207–255`, `:258–306`;
    - B at `summaryB.json:122–170`, `:71–119`, `:173–221`, `:224–272`;
    - these are the transversal classes y − mx for m = 3, 6, 4, 5.
  - Class 6, classical models:
    - A at `:519–567`, `:570–618`, `:621–669`, `:672–720`;
    - B at `:404–452`, `:455–503`, `:353–401`, `:506–554`;
    - these are m = 2, 5, 6, 4.
  - Class 6, non-singleton model: A at `summary.json:342–516` (175 entries) and B at `summaryB.json:302–350`.
    - Both equal A(x,y) = y − x·{2,4,5,6} at all 42 off-frame points. I checked each; for example 7 ↦ {1,2,3,5}, 26 ↦ {0,1,4,6}, 48 ↦ {1,3,4,5}.
    - The frame entries are k:k.

### (d) Completeness of the seven classes — logic ✓, computation un-replayed

- **Normalization count.** 24·49·720 = 846720 = n!·n·(k+2)(k+1)k at n = 7, k = 2 (`1406.3681v2:386`).
- **Frames are labelled isomorphisms.** A frame (σ, p, o) forces every label:
  - column labels and the L1/L2 labels come from row 0;
  - row labels come from column 0 of L1 (`net_canon.c:43–53`, mirroring `1406.3681v2:371–376`).
  - So frames correspond one-to-one with labelled isomorphisms N → net(R), R reduced.
- **The action is free.** Take an automorphism fixing σ, p and o. It fixes:
  - every point of p's row;
  - hence every line of classes σ1–σ3;
  - hence every point of the column through p, as column ∩ L1-line;
  - hence every row line.
  - So it is the identity.
- **The quotient.** Fibres are therefore Aut(N)-orbits, and |Aut(N)| = |par|, the stabiliser of the orthogonal array in S7≀S4. So the number of distinct keys is 846720/|par|.
- **The key is complete.** Its 36 + 42 bytes cover everything the reduction leaves free: all of L1 except row 0 and column 0, and all of L2 except row 0.
- **Code reading.** `gen_perms` and `orbit_keys` read correctly.
- **Exhaustion.** Each species contributes 846720/|par| reduced sets, and distinct keys make the contributions disjoint.
  - The total 342480 equals Table 6, and the classes 0–4 subtotal 341880 equals Table 5. The arithmetic checks.
  - As laid out, Tables 5 and 6 also show 5 and 7 under Paratopism (`:708`, `:755`), which is consistent.
- **Hand cross-check for classes 5 and 6.**
  - Class 5 is (x, y, y−x, y−2x): directions {∞,0,1,2}, cross-ratio orbit {2,4,6} ∋ −1, so harmonic.
  - Class 6 is (x, y, y−x, y−3x): directions {∞,0,1,3}, orbit {3,5}, with λ²−λ+1 ≡ 0, so equianharmonic.
  - The affine automorphisms number 49·6·|Stab_PGL(2,7)(D)|: 49·6·8 = 2352 and 49·6·12 = 3528, consistent with 42 + 28 = 70 = C(8,4).
  - Assuming, as is standard, that these nets' automorphisms are affine, this gives 360 + 240 = 600 = 342480 − 341880 without net_canon. Only the data for classes 0–4 rest on it.
- **Net validity spot checks.**
  - Class 0: L2 = y + θ(x) with θ(x) − x = (0,1,3,5,2,6,4), a permutation.
  - Classes 1 and 4: checked in full (Latin rows and columns, 49 distinct (L1,L2) pairs).
  - Classes 5 and 6: linear, hence valid.
- **The maximal corollary** needs only completeness and the non-maximality of classes 5 and 6 (they are AG(2,7) subnets), not the transversal counts. Table 9 is neither used nor invented.

### (e) Phase cycle — ✓

- **Collinearity.** In the net JSON, 26 = [3,5,2,3], 28 = [4,0,3,2], 29 = [4,1,4,3], 33 = [4,5,1,0] and 34 = [4,6,2,1]. Each listed pair agrees in exactly the stated class.
- **Overlaps.** A(26) = {0,1,4,6}, A(28) = {1,4,5,6}, A(29) = {0,2,5,6}, A(33) = {2,3,4,6}, A(34) = {0,3,4,5}. These give exactly the seven displayed 2-coordinate overlaps.
- **Phase relation.** Two nonzero terms summing to zero differ in argument by π, which gives `:88`. Overlap-3 pairs exist (classes 1–3, ratios 3 and 5) and are correctly not used.
- **Cancellation.** The 14 variables are (26,0), (26,4), (26,6), (28,4), (28,5), (28,6), (29,0), (29,5), (29,6), (33,4), (33,6), (34,0), (34,4), (34,5).
  - Each appears exactly twice, with opposite signed coefficients.
  - The signs sum to +1, so 0 ≡ π.
- **Word proof** (correct once the row citations in item 11 are fixed):
  - Δ28(4,6) = Δ28(4,5) + Δ28(5,6) ≡ Δ34(4,5) + Δ29(5,6).
  - Δ26(4,6) = Δ26(0,6) − Δ26(0,4) ≡ Δ29(0,6) − Δ34(0,4).
  - Rows 2 and 5 equate these, giving Δ34(0,5) ≡ Δ29(0,5), which contradicts row 4.
- **Checker.** `k1_phase_cert.py:25–60` checks exactly this, and its output (`phase_cycle_certificate.json:3–77`) matches the table.
- **What is supported.** The count 315 holds by hand; 97 and the MILP minimum are unsupported (item 5).

### (f) §8 reduction — ✓

- **The printed proof** (`2607.12933v2:185–192`) has one risky case: an entry u with support {1,2} and an entry v ⊥ u.
- **Why it is safe here.** Tensor orthogonality factors as ⟨ψ⊗φ, ψ′⊗φ′⟩ = ⟨ψ,ψ′⟩⟨φ,φ′⟩, so u and v are both entries of the square being replaced, which has all weights ≤ 2.
  - Hence |supp v ∩ {1,2}| ≠ 1, so v is either rotated too or fixed by U.
  - Every zero inner product therefore survives.
  - The excluded counter-scenario: if supp v ⊋ {1,2}, then ⟨Uu, v⟩ could be nonzero.
- **Both other squares at once.** The same Ψ′ works for every Φ orthogonal to Ψ.
- **Row 0 and termination.** Row 0 has weight 1 and is never rotated. Supports only shrink, and the number of weight-2 entries strictly drops, so the process ends with all weights 1, which is classical.
- **The remaining steps hold:**
  - Sequential replacement works (item 12).
  - An entry of weight ≥ 2 in standard form is an 8th ray, so its square is non-classical.
  - |Q| ≤ 1 yields a K1 set, which Theorem K1 forbids.
  - |Q| ∈ {2,3} yields K2 or K3 sets as stated.

### Controls — ✓

- **Exact supports.** At `pattern_check.py:93`, a multiset of seven 7th roots of unity sums to 0 iff each root occurs once, because Φ7 is the minimal polynomial. So the supports are exact.
- **Shifts.** f0 = (0,1,2,0,4,0,0).
  - The determined directions are {0,1} ∪ {1/(1−z) : z ∈ {0,3,5,6}} = {0,1,3,4,5}, so M0 = {2,6}.
  - f and M_shifted match `pattern_controls.json:5–18` and `:28–42`.
- **Counts.**
  - Weights {1,5}: five determined directions remain after the shift.
  - Mutation totals: 294 = 42·7, 84 = 42·2, and C2's 48 = 12·4.
  - C4's 294/294 rejections are consistent: removals break an overlap-2 pair on the class-0 line, and additions hit a frame point.
  - C3 has 18 entries, all clean.

### Provenance

All printed digests match the manifest records except items 1 and 2. Missing items:
- `review/LEMMAS.md` (item 6);
- solver-version receipts (item 3);
- drat-trim control receipts (item 4).

## Trust assumptions

1. The Egan–Wanless totals 342480 and 341880, and Theorem 3.2.
2. The `net_canon.c` outputs for classes 0–4 (|par| and keys). These are neither replayed nor receipted.
3. Each DRAT-checked file equals base(pinned encoder, pinned net) plus the recorded blocking clauses.
   - The CNFs and proofs are not pinned; only their hashes appear in the summaries.
   - A parent can re-establish identity without the missing files: regenerate the CNFs from the pinned code and recorded models, then compare against `final_cnf_sha256`.
4. drat-trim is sound, and binary `111b0405…` was built from source `d834b649…`. The build is not recorded.
5. The summaries are self-reports with no logs. The "independent" encoders share the net file, the frame convention and the drat-trim binary.

## Unresolved scope

- K2 and K3 remain open.
- No DRAT replay and no net_canon replay were done here.
- The `k1_phase.py` exploration is unverified.
- README lines 125–136, which changed during pinning, are outside K1.
