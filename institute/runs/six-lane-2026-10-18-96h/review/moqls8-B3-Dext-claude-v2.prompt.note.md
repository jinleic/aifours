# Hostile review: D-extension concentration candidate v1 (18b5d33b…), read with parent erratum v1 (0c13e8d4…)

**Method.** Everything below was re-derived by hand. I used no tools, code, computation or delegation.

The A2/NF/GA context (LF7–12) was not used, and none of it is needed. D is defined directly in normal form, so H2–H4 hold by definition. I did not rely on the earlier reviewer's pass (E11).

Line references: `LFn` is the candidate, `E n` the erratum, `R1 n` the row-1 candidate, `SC n` the scope freeze.

## Verdict

**FATAL 0 · MAJOR 0 · MINOR 7** (plus 5 uncounted nits).

- **Mathematics.** Read with E1–E5, every lemma, theorem and corollary re-derives on all of D. That covers all phases, every square-1 column-0 unitary with the template support, and general interior vectors. The (B3)-labelled items also hold under H1–H4 alone.
- **Erratum.** Each of E2–E5 is a correct correction, and the E1 withdrawal is justified. However, E1 leaves residue in LF180 (M1, M2), and E2 misses one index domain (M5).
- **Remaining system.** It is exact once one sentence on genuineness is added (M3). The note infers no D no-go, no witness and no positive multi-line conclusion.
- **Recommendation.** Accept as PARTIAL (EXACT_NECESSARY_OBSTRUCTION_OR_REMAINING_EQUATIONS), conditional on an erratum v2 carrying M1–M7. All seven repairs are wording, so no mathematical re-review is needed.

## Claim-by-claim

### Setting and basic facts (§1–2)

- **H1 in pairwise form (LF16) — PASS.** There are 64 unit vectors in C^64, so "ONB" is equivalent to "pairwise orthogonal". Each pairwise inner product is G_s·G_t. The theorems use only the forward direction; the exactness of §8 uses the converse.
- **Spans (LF25) — PASS.**
  - q_1^1, q_1^6, q_1^7 are orthonormal (column-0 ONB) and lie in the 3-dimensional V_A, so they span it.
  - Likewise q_1^2, q_1^3 span V_B and q_1^4, q_1^5 span V_C.
  - The exact supports agree with the `supports_row2to7` rows of the [J] excerpt verbatim.
- **D restatement (LF27–31) — PASS.**
  - π_2 to π_5 match R1 73–76 entry by entry, and each one permutes {1..7}.
  - π_s(1) = s+2, which is SB2.
  - Column 0 of each square s ≥ 2 is automatically an ONB.
- **F1 (LF37) — PASS.**
- **F2 (LF39) — PASS.** The pairs (i,j)/(0,d) with d≠j, and (i,j)/(r,0) with r≠i, differ in both row and column. The cases d=j and r=i follow from F1 (nit N1).
- **AX (LF41–44) — PASS.**
  - For d≥1 it follows from H1 on (0,d)/(r,0).
  - For d=0 it follows from q_s^r ⊥ w·e_0.
  - All three consequences for s≥2 are read off supp q_1^r.
- **LF46, the D-only addendum — PASS.** π_s(6) = 7, 6, 5, 4.
- **W (LF48) — PASS.** It is the trace of P_X.

### Lemma M (§3)

- **Column part — PASS.**
  - Parseval in column c gives Σ_i |⟨e_d, Q_s(i,c)⟩|² = 1. The (0,c) term vanishes because d≠c, and d=0 is included.
  - Disjointness is the S-part of F2 at (i,c).
  - Five nonempty disjoint subsets of {1..7} have total excess at most 2.
- **Row part — PASS.**
  - Parseval applies to q_s^r over row i. The j=0 term ⟨q_s^r, q_s^i⟩ is 0 because r≠i, so J_s ⊆ {1..7} (nit N2).
  - Disjointness is the T-part of F2.

### Lemma B (§4)

- **(a), B and C corners — PASS.** q_1^i has both block coordinates nonzero, so {q_1^i, e_c} spans the 2-dimensional block.
- **(a), A-block lines — PASS.** I checked all nine pairs (i,c) in {1,6,7}×{1,2,3}. Each L_{i,c} is a line, since its dimension is 3−2 = 1.

  | (i,c) | L_{i,c} |
  |---|---|
  | (1,1), (7,1) | span q_1^6 |
  | (1,2), (7,2) | support {1,3} |
  | (1,3), (7,3) | support {1,2} |
  | (6,1) | support {2,3} |
  | (6,2), (6,3) | span e_1 |

- **(b), rank-one projections (with E2, E4) — PASS.**
  - In row i the interior sum is P_B − |q_1^i⟩⟨q_1^i| = |q_1^{5−i}⟩⟨q_1^{5−i}|.
  - A PSD summand A of a rank-one projector R satisfies ⟨x,Ax⟩ ≤ ⟨x,Rx⟩ = 0 for x ⊥ ran R, so ran A ⊆ ran R.
  - For columns, the subtracted term is the row-0 term (E4).
- **(c), plane projections (with E2, E3) — PASS.** For d ∈ A, e_d lies in the plane P_i exactly when d ∉ supp q_1^i. Among i ∈ {1,6,7} that happens only for (i,d) = (6,1).

### Theorems K and K′ (§5–6)

- **K, B rows (LF99–116) — PASS.**
  - Demand: 4 squares × 2 = 8.
  - Capacity is 0 on J_i, because λ·q_1^{5−i} puts both 6 and 7 into S(Q_1). It is at most 2 on {1..5}∖J_i and at most 1 at j ∈ {6,7}.
  - So 8 ≤ 12 − 2|J_i|, giving 1 ≤ |J_i| ≤ 2.
  - In the tight case every cell is a unit e_6- or e_7-cell. There are 4 of each kind, and row orthonormality allows at most one of each per square, so every square has exactly one of each.
- **K, C rows — PASS after M4.**
- **K′, B columns (LF120–140) — PASS.**
  - e_c ⊥ U_s, so the demand is 8.
  - Capacity is 0 on I_c, because κ·e_{13−c} has nonzero q_1^2 and q_1^3 coefficients, putting 2 and 3 in T_1. It is 1 at rows 2 and 3 (own exclusion by F1) and at most 2 elsewhere.
  - The tight case gives unit q_s^2- and q_s^3-cells, 4 of each.
- **K′, C columns — PASS after M4.**

### Theorems KA and KA′ (§7)

- **KA (LF144–154) — PASS (see M5).**
  - There are 18 slots. Square 1 occupies σ_i of them.
  - At each cell, a square s≥2 carries weight at most min(1, number of slots it uses). So 12 ≤ 18 − σ_i.
  - For i ∈ {1,7}, the planes P_1 and P_7 contain no e_d, which gives |K_i| ≤ 3.
  - At equality, the chain of inequalities forces unit cells that each use one slot.
  - For i = 6 the theorem needs q_s^6 ⊥ e_1, which holds on D by LF46.
- **KA′ (LF156–165) — PASS, and genuinely B3.**
  - Σ_{r∈O} |⟨q_s^r, e_c⟩|² = 0 needs only q_s^6 ⊥ e_2, e_3, so the demand is 12.
  - Square 1's own-O weight equals ‖P_A·‖², with total 2, so |K′_c| ≥ 2.
  - A component with a single own index would be a multiple of q_1^r orthogonal to e_c. That is impossible, because 2 and 3 lie in supp q_1^r for every r ∈ O.
  - So each component uses at least 2 slots, and 12 ≤ 18 − τ_c.
- **Hypotheses.** K, K′ and KA′ hold on every member of D; KA at i = 6 holds there via LF46.

### D-specific corollaries and §8–9

- **D1 (LF169, with E5) — PASS.**
  - For s = 2..5, π_s^{-1}(6) = 5, 6, 1, 7 and π_s^{-1}(7) = 6, 4, 7, 1.
  - The coincidences with a≠b are exactly (3,2), (4,5) and (5,4).
  - E5's replacement sentence is correct: π_s(2) ∈ {2,3,1,5} and π_s(3) ∈ {3,2,4,1}.
- **D2 (LF171) — PASS.** π_s(2) = 2, 3, 1, 5 and π_s(3) = 3, 2, 4, 1. The coincidences are exactly (2,3), (3,2) and (4,5).
- **Locality (LF173) — PASS, see M6.**
- **R1 consistency remark (LF173) — PASS, not load-bearing.** R1 154 gives the interior of square 1's row 1 as q_1^4, q_1^2, q_1^3, q_1^7, q_1^6, q_1^5, q_1^0. So K_1 = {4,5} and σ_1 = 3+2 = 5.
- **Remaining system (LF5, LF175–178) — PASS after M3.**
- **LF180 residue — MINOR** (M1, M2).
- **Context (LF7–12)** — not evaluated and not used (M7).
- **Ledger (LF192–202) — MINOR** (M6).

## Requested audits

**Common frame S versus own frame T_s, and general vectors.**
- K and KA work in the common frame: coordinates 6,7 (or 4,5) and A, with the S-part of F2.
- K′ and KA′ work in own frames for squares s≥2 (U_s, or span{q_s^r : r∈O}), with the T-part of F2.
- Square 1 enters K′ through its common-frame B-part. That part becomes own indices because q_1^2 and q_1^3 are dense on {6,7}.
- In KA′, square 1's O-frame is V_A itself.
- No step presumes that an interior vector is a basis or axis vector. Every such form (K1, K′1, K2, K′2, and KA/KA′ saturation) is derived from an equality case.
- Amplitudes enter only through the exactness of the template supports, which is constant on D. Phases enter nowhere.

**Locality: exactly what is used.**
- Row-type results (K, KA, the row part of M, and Lemma B's row parts) use only:
  - each square's row-i ONB;
  - Q_s(i,j) ⊥ Q_s(0,j);
  - H1 on the pairs {(i,j),(0,d)} and {(i,j),(r,0)};
  - the axis data.
- Column-type results (K′, KA′, the column part of M, and Lemma B's column parts) use only:
  - the column-c ONB;
  - Q_s(i,c) ⊥ q_s^i;
  - H1 on {(i,c),(r,0)}, plus {(i,c),(0,d)} for the column part of M only;
  - the axis data.
- No pair of interior cells from different lines is ever used. KA at i = 6 adds only an axis hypothesis. So LF173 is exactly right.
- Since D-extendability is the open question, the full-configuration theorems may be vacuous on D. Their non-vacuous content is this single-line form, which LF173 states correctly.

**Remaining system and scope.**
- (R), (C), (T) together with the D parameters are exactly H1 with axes in D:
  - the row-0 and column-0 ONBs are built into D;
  - (T) ranges over all distinct cells, so axis–axis pairs are included and R1 Lemma 3 is not needed;
  - unit norms follow from (R).
- The only conjunct of the target that is not written out is "genuine" (SC14, LF16). It is automatic, but the text must say so (M3).
- The note draws no conclusion from the system.

## Findings and minimal repairs

**M1 — LF180, last sentence, and LF201.**
- **Problem.**
  - After E1's withdrawal, "every such frame" has no antecedent.
  - The assertion is also unproved, which contradicts LF3 ("Every finite statement is proved by hand"); LF201 marks it "stated only".
  - It is in fact true. For row i₀ ≥ 1 and a cell (i,j) with i ≠ i₀, the pair (i₀,d),(i,j) with d ≠ j differs in both row and column, and d = j vanishes by column orthonormality. The analogue of M is Parseval in column c, where the (i₀,c) term vanishes by row orthonormality.
- **Repair.** Replace the sentence with "Interior-line-frame analogues of (F2) and Lemma M are not used here", and set LF201 to "not used". This matches E1's own gloss. Alternatively, name the frames and add the two-line proof above.

**M2 — LF180, "They do not by themselves decide (R), (C), (T)."**
- **Problem.** Read literally, this asserts that all the single-line consequences are jointly non-contradictory. That would need a joint model, and none is given; it is the same kind of claim E1 withdrew.
- **Severity.** MINOR rather than MAJOR, because E1 already fixes the intended reading ("remains undecided") and nothing rests on the sentence.
- **Repair.** "No decision of (R), (C), (T) is derived from them here."

**M3 — LF5 ("stated exactly") and LF175–178.**
- **Problem.** The system silently drops "genuine".
- **Repair.** Append after LF178: "No genuineness constraint is needed: an isotopy making every entry of Q_1 a phase times a basis vector would make the rays e_0,…,e_7 of row 0 all the rays of that basis, so q_1^1 would be a multiple of some e_c, contradicting |supp q_1^1| = 3 (H3; [PRIM] LF201–203, 220–224)."

**M4 — LF105 and LF126, the C-case dictionaries are incomplete.**
- **Problem.**
  - At LF105, literal substitution leaves "{1..5}∖J_i". For J_i = {6,7} that gives five columns, including 4 and 5, where the capacity is only 1. This contradicts "three columns".
  - LF126 has the same defect with "{1,4,5,6,7}∖I_c".
- **Repair at LF105.** "(C: {4,5} for {6,7}, {1,2,3,6,7} for {1..5}, q_1^{9−i} for q_1^{5−i}, 9−j for 13−j, e_4,e_5 for e_6,e_7; (i,4) is an e_5-cell, (i,5) an e_4-cell)".
- **Repair at LF126.** "(C: c∈{4,5}, U_s = span{q_s^4,q_s^5}, rows {1,2,3,6,7}∖I_c, e_{9−c}; (4,c) is a q^5-cell, (5,c) a q^4-cell)".
- Both C cases re-derive correctly.

**M5 — LF147, an index domain E2 missed.**
- **Problem.**
  - LF147 does not restrict j in "every A-coordinate slot (j,d), d ∈ A∖{j}"; only the count 18 at LF151 fixes the domain.
  - With j = 0 the saturation clause is false at i = 6. q_1^6 has support {2,3}, so slot (0,1) is free, but in D no q_s^6 (s≥2) is a multiple of e_1.
- **Repair.**
  - Insert "j ∈ {1,…,7}" at LF147.
  - For uniformity, insert "i ∈ {1,…,7}" at LF158. That one is harmless: at i = 0, square 1's e_c occupies all the O-slots.
  - Add both lines to E2's list.

**M6 — LF173 and the ledger (LF192–202).**
- **Problem.**
  - "Single-line partial extension" is never defined.
  - The ledger has no row for locality, for the R1 remark, or for the exactness of §8.
  - LF46 is D-only, but it sits under "F1, F2, AX, W | proved (B3)".
- **Repair.**
  - At LF173 add: "(an assignment on row 0 ∪ column 0 ∪ L, L one row or column of index ≥ 1, satisfying H2–H4 and every H1 equation among those cells; cf. R1 18–23)".
  - Add three ledger rows:
    - "locality | proved by inspection";
    - "R1 remark | checked, not a premise";
    - "remaining system | exact (genuineness automatic)".
  - Annotate the AX row with "LF46: D only".

**M7 — LF7–12.**
- **Problem.** "would already imply that no member of D extends" asserts a conditional, computer-assisted full-D no-go without derivation. It also does not say which certificate hypothesis D instantiates. It is correctly marked "not used"; I confirmed that nothing in §§1–8 depends on it, but I did not evaluate it.
- **Repair.** "are recorded (not checked here) as implying, at their conditional scopes, that no member of D extends".

**Nits (uncounted; nothing false):**
- **N1 (LF39).** Add "j and i lie in none of the sets, by F1."
- **N2 (LF59).** Add "subsets of {1..7}"; the 7-set step at LF62 uses this.
- **N3 (LF169, LF171).** "saturated" there means the tight |J_i| = 2 or |I_c| = 2 case, but LF147 and LF158 use "saturation" for σ_i = 6 or τ_c = 6. Write "tight (K2)" and "tight (K′2)".
- **N4 (LF163).** It uses τ_c ≤ 6, which is only proved at LF164. Reorder; there is no circularity.
- **N5.** I checked H4 against the supplied excerpt `04-GBBINDING-P1-B3-entry.json` (e493b946…), not against the cited full [J] file (d917203d…).

## Not checked

- I recomputed no hashes and did not check the process claims at LF3 or the context chain at LF7–12.
- The SHA strings quoted across the supplied files agree with each other:

  | File | SHA prefix |
  |---|---|
  | Candidate (as cited in E3) | 18b5d33b… |
  | Scope freeze | 4bb2ecb2… |
  | Transitions | 0c852bf1… |
  | R1 | 84506494… |
  | PRIM | 265851e4… |
