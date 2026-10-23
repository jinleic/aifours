DISPOSITION: K5NF-r2=ACCEPT-WITH-FIXES; HALL3-r1=ACCEPT

This is a static audit of the packet only; I ran nothing. Desk figures marked [F] are used only as cross-checks, never as premises. Both notes are mathematically correct. K5NF-r2 has four textual gaps to close before a receipt cites it; HALL3-r1 is correct as written.

Aliases used in the check sections:
- r1, r2 = `review/K5_RESIDUAL_NORMAL_FORM.r{1,2}.md`
- HALL3 = `review/HALL3_PATTERN_NECESSITY.r1.md`
- r3 = `review/K4K5_ENCODING_SOUNDNESS.r3.md`
- ga = `code/gram_a.py`
- hp = `code/h3_pilot.py`

## K5_RESIDUAL_NORMAL_FORM.r2

**FATAL:** none. **MAJOR:** none.

**MINOR**

1. **Relabelling move and bridge form** — `review/K5_RESIDUAL_NORMAL_FORM.r2.md:48-55` (and `:71`).
   - **Defect:** relabelling squares 2..5 is not one of r3's lossless moves (α)(β)(γ)(τ) (`review/K4K5_ENCODING_SOUNDNESS.r3.md:104-106`). The bridge is then applied to a configuration that r3 §5's move sequence does not produce. The step is valid, but the note does not justify it.
   - **Fix, part 1:** add a move (ρ) "relabel squares 2..5". It is lossless because:
     - the sets are unordered;
     - Prop 1 / mutual orthogonality is symmetric in each pair;
     - QLS, row-0 standard form, row-0-frame weights and K5 membership are all per-square properties.
   - **Fix, part 2:** invoke the bridge in property form. Any genuine labelled set with the following properties has a canonical assignment satisfying F:
     - row-0 standard form;
     - a weight-3 row-0-frame entry in every square;
     - (1,0) supports A, {4}, {5}, {6}, {7};
     - Q1 column 0 lex-sorted on rows 2..7.
   - This is what r3 actually proves: G2–G5 hold for every QLS, P4 for every K5 set, and auxiliaries take their defining values (`review/K4K5_ENCODING_SOUNDNESS.r3.md:94-103`).

2. **Bit-order lemma unproved** — `review/K5_RESIDUAL_NORMAL_FORM.r2.md:61-62` (and `:43`).
   - **Defect:** the lemma is asserted without proof. r1's proof (`review/K5_RESIDUAL_NORMAL_FORM.r1.md:61-64`) was dropped, as was the remark that σ preserves cardinality and pure-B-ness (`r1:59`). r2 cites no control receipt, and the controls are aids in any case.
   - **Fix (inline the proof):**
     - Let S ⊆ B with |S| ≥ k and S ≠ C_k. Then S ⊄ C_k, so S has some element m < 8−k.
     - At S's first 1 (position ≤ m), C_k has 0, and both are 0 before it, so S >lex C_k.
     - Add: σA = A, σB = B and |σS| = |S|.

3. **Wording** — `review/K5_RESIDUAL_NORMAL_FORM.r2.md:57,66,29`.
   - "restore the ROWLEX order": §1 (`:10`) never imposed ROWLEX. Say "impose". This is harmless because the sort is the last move.
   - "bit k−1 in the V1 list is coordinate k": write "V1[k−1] = g_1((0,k),(2,0)); cube b sets it to bit k−1 of b, so support S ↦ Σ_{k∈S} 2^{k−1}".
   - "squared b-component": write |·|².

4. **Unpinned import** — `review/K5_RESIDUAL_NORMAL_FORM.r2.md:79-80`.
   - **Defect:** FINAL.json is cited by path only.
   - **Fix:** pin its SHA 88cac421…2905 (`parent/moqls8-k5-root-parent-verdict.md:19`) and the c112 per-root receipt, so the single machine import is self-contained.

### (a) §2 dimension argument — holds, no hidden case

- **supp Q1(1,0) = A, with all three coordinates nonzero, is forced, not assumed.**
  - r3 §5 moves a weight-3 entry (exactly three nonzero coordinates) to (1,0), and σ fixing 0 maps its support onto {1,2,3} (`r3:107-109`).
  - F's Q1 SB2 units are the Boolean image of this (`ga:276-281`): positive for k = 1..3, negative for k = 4..7. The k = 0 unit is the constant ⊥ and drops.
- **Properties of w_2..w_7.** They are orthonormal and orthogonal to v and to |0⟩, so they avoid coordinate 0. W8 gives weight ≤ 3.
- **Lemma 2 applies** because supp v is exactly A. So any w_i that is not pure-B has |supp ∩ A| ∈ {2,3}.
- **Parseval.** In the column-0 ONB, Σ_{i≥2} |(w_i)_b|² = 1 for every b ∈ B. This holds unconditionally.
- **The contradiction.**
  - Under the hypothesis, P_B w_b is supported exactly on {b}, so the four w_b are distinct.
  - Hence ⟨p_b,p_c⟩ = ⟨w_b,w_c⟩ − ⟨P_B w_b, P_B w_c⟩ − ⟨P_0 w_b, P_0 w_c⟩ = 0.
  - Also ⟨v,p_b⟩ = ⟨v,w_b⟩ = 0.
  - That puts four nonzero orthogonal vectors (three would suffice) in the 2-dimensional space C^A ∩ v^⊥.
- **Hidden cases checked:**
  - complex phases enter only through Hermitian inner products;
  - a w_i meeting A in all 3 coordinates has no B-part and is never selected;
  - several w_i sharing a B-coordinate are harmless, since one is chosen per b;
  - coordinate 0 is handled at `r2:16,34`.

### (b) §3 residual move — a genuine symmetry

**What it permutes.** σ ∈ Sym{4,5,6,7}, extended by the identity on {0,1,2,3}, acting as Ψ′_s(i,σ(j)) := P_σ Ψ_s(i,j) for every s, i, j.
- **Columns and coordinates:**
  - columns 4–7 are permuted;
  - coordinates 4–7 of every vector of every square are permuted;
  - columns 0–3 stay in place, but their entries are transformed by P_σ, so w_i ↦ P_σ w_i;
  - v ∈ C^A is unchanged.
- **Cells:** (i,j) ↦ (i,σ(j)). Only cells in columns 4–7 move, and only within their own rows.
- **Squares:** square s ∈ {2..5} gets label σ(s+2)−2. Square 1 is fixed.
- **Rows:** one common π ∈ Sym{2..7} is then applied to all squares. This is move (α), with rows 0 and 1 fixed.

**What it preserves.**
- **QLS:** P_σ is unitary, and lines map to lines.
- **Mutual orthogonality:** the cell bijection is common to all squares, i.e. P_σ⊗P_σ maps the product ONB to itself. Relabelling only permutes the 10 pairs.
- **Row-0 standard form:** column σ(j) of row 0 holds P_σ|j⟩ = |σ(j)⟩.
- **P4 and reduced K5:** entry weights are invariant, so all five squares stay untouched and the reduction acts as the identity.
- **SB2:** cell (1,0) is fixed, Q1(1,0) = v, and relabelling restores {4}, {5}, {6}, {7}.

**ROWLEX and the bridge.** ROWLEX is legitimately re-imposed after σ, because a sorting π always exists. Any tie has support C_k, so the tie rule at `r2:64-65` is unnecessary. The bridge then applies in property form (MINOR 1).

### (c) Order and indexing — correct, no conflation

- **Encoded ROWLEX** (`ga:253-270`):
  - the prefix-equality chain forbids A[k] = 1, B[k] = 0 at the first difference, with k = 0 most significant and 0 < 1;
  - bit 0 is the constant ⊥ (same column);
  - so in effect coordinate 1 is the most significant bit and coordinate 7 the least (`r3:109`).
- **r2's minimality argument** (`r2:60-62`) uses exactly this order:
  - an A-meeting support has its first 1 at a position ≤ 3, which is below 5 ≤ min C_k;
  - every pure-B support has size ≥ k;
  - so C_k = {8−k..7} is the unique minimum (MINOR 2).
- **Cube indexing runs the opposite way** (`README.md:188`): coordinate k ↔ bit k−1, so coordinate 7 is the high bit.
  - {7} → 64, {6,7} → 96, {5,6,7} → 112.
  - The units at `r2:73` are the 112 pattern.
- **Verdict:** r2 uses ROWLEX significance for the minimum and README significance for the cube label, and does not mix them. In cube-index order C_k is the largest k-subset of B. The "leftmost" error that would come from conflating the orders is exactly what the r1/K3 negative controls reject [F].

### (d) §4 conclusion — imports and obligation are exact

- **No forbidden imports.** r2 uses no SAT model, no CNF automorphism (disclaimed at `r2:67`), no unreplayed certificate, and nothing from F3, K4 or the catalogue.
- **The 122-root fact** appears only as c112's provenance (`r2:78`).
- **Unwritten steps** are limited to MINOR 1–2.
- **The stated obligation is exactly right** (`r2:82-83,88`). It consists of:
  - this lemma, including (ρ);
  - the bridge (C1–C8, C12, plus the V1 id meanings);
  - c112's parent-replayed certificate;
  - validator-complete (`README.md:244-245`), parent-replayed refutations of the c064 and c096 subtrees.
- **Scope.** Together these exclude genuine reduced K5 configurations only. The note correctly separates this from "F is UNSAT" (`r2:84-85`):
  - the Boolean models of F in c016, c032, c048 and c080 are outside the vector argument;
  - the 128-root ledger stays incomplete (`r2:87`).

### (e) Interplay

- **K4:** nothing is needed or claimed (`r2:20`), and nothing transfers:
  - the K4 base has no ROWLEX (`r3:86,91`);
  - its row freedom is consumed by L(i,0) = i;
  - Q1's support is {2,3,4}, with coordinate 1 reserved for L (`r3:112-114`; `README.md:168-173`);
  - no K4 split has been declared (`r3:130`).
- **The 122 certified roots:** only c112's proof is used. The other 121, and the UNKNOWN roots c016, c032, c048 and c080, become semantically unnecessary for genuine configurations. All of them stay in the Boolean ledger unchanged.
- **Significance only:** if r2 is accepted, the pilot leaf c016.L2.040.L3.104 leaves the semantic critical path.
  - It remains on the Boolean critical path and is still a legitimate exploratory H3 probe.
  - c016 is σ-related to c064 semantically, but not through a CNF automorphism.
  - The semantic frontier becomes the c064 and c096 subtrees. Both are still unrefined UNKNOWN roots in v008 (`desk/EXTRACTS.json:459-466`).

**Novelty and significance (non-dispositive):**
- Novelty is low: a Parseval/dimension count plus a canonical choice within the residual stabiliser.
- Significance within the lane is high: the semantic K5 frontier shrinks from 6 roots to 2.
- K5 is not excluded, and neither is K4.

## HALL3_PATTERN_NECESSITY.r1

**FATAL:** none. **MAJOR:** none.

**MINOR**

1. **Constant folding not justified in the note** — `review/HALL3_PATTERN_NECESSITY.r1.md:39-40,45`.
   - **Defect:** folding is justified only by reference to the encoder.
   - **Fix (add these facts):**
     - ⊤ and ⊥ are exact values for every QLS, so dropping ⊤-clauses and ⊥-literals preserves validity.
     - A non-tautological clause contains at most 3 ⊥ literals (parallel lines: the diagonal) or at most 6 (intersecting lines: the shared cell's row or column). So at least 12 of its 18 literals survive, and it is never empty.
     - Independently, an empty clause would be violated by every QLS, for example a classical square, contradicting §1.

2. **Transfer rules only prohibit** — `review/HALL3_PATTERN_NECESSITY.r1.md:46-47,61-63`.
   - **Defect:** the note forbids silent relabelling but never says what may be counted.
   - **Fix:** state the permitted uses, as set out in (i) below.

3. **Literal notation mixes indices and cells** — `review/HALL3_PATTERN_NECESSITY.r1.md:36-39`.
   - **Defect:** "g_s(a,b), a ∈ R, b ∈ (line not C)" uses a for a row-0 index but b for a cell.
   - **Fix:**
     - row family: g_s((0,a), ℓ_b) for a ∈ R ⊂ {0..7} with |R| = 3, and b ∉ C ⊂ idx(ℓ) with |C| = 2;
     - transposed family: b ∈ R′ ⊂ idx(ℓ) with |R′| = 3, and a ∉ C′ ⊂ {0..7} with |C′| = 2.

### (f) Necessity — holds

- **Both orientations are valid.** U is unitary (UU* = U*U = I). Three rows inside two columns, or three columns inside two rows, would give three orthonormal vectors in a 2-dimensional space. (This is the t = 3 Hall/Frobenius–König condition; nonsingularity alone already implies it.)
- **Parallel lines:** the diagonal entries are ⊥, because the cells share a column or row.
- **Intersecting lines:** U = [1] ⊕ U′. The encoder puts ⊤ at the shared cell and ⊥ on the rest of its row and column (`ga:127-131`). These are exactly the true values.
- **Variables match the support bits.** With row 0 as one line, g_s((0,a), ℓ_b) = [⟨a|Ψ_s(ℓ_b)⟩ ≠ 0] = [U[a,b] ≠ 0]. There is one symmetric variable per unordered pair (`ga:137-138`), so the clauses range over exactly the support bits.

### (g) Counterpattern — passes encoded G3, fails H3

- **It passes G3 as encoded** (`ga:179-190`):
  - every row and every column is nonempty;
  - pairs of rows share 2, 3 or 0 columns;
  - pairs of columns share 3, 2 or 0 rows;
  - so no pair shares exactly one entry.
- **It is not the support of any unitary:** rows {0,1,2} lie inside columns {0,1}, and columns {2,3,4} lie inside rows {3,4}.
- **H3 rejects it:** exactly those two raw clauses are violated.
- **Scope:** the note claims this only for the abstract 8×8 pattern, and makes no claim about F (`HALL3:28-30`).

### (h) Count and scope — correct

- **Count:** 5 · 15 · 56 · 28 · 2 = 235,200 raw clauses, each with 3 · 6 = 18 literals.
- **"Row-0 only"** means 15 of the 120 line pairs per square: rows 1..7 and columns 0..7. It is described correctly (`HALL3:34-35`) and is a subset of valid clauses.
- **Folding** never produces an empty or invalid clause (MINOR 1).
- **Static per-square count:** 7,056 tautologies dropped and 39,984 clauses emitted, with sizes 12, 15, 16, 17 and 18 literals. This agrees with the desk census [F].

### (i) Soundness and ledger rules

- **What an F_H3 UNSAT shows.**
  - Every normalised genuine configuration has a canonical assignment satisfying both F (by the bridge) and H3 (by §1).
  - So an UNSAT F_H3 leaf excludes the genuine configurations in that leaf.
  - It never shows that F is UNSAT.
- **(1) DRAT bytes do not transfer in either direction.**
  - The strict predicate binds a proof to the exact CNF bytes and header.
  - **F → F_H3:** RUP steps survive added clauses, but RAT steps need not. H3's positive g-literals create new resolution partners for pivots on ¬g.
  - **F_H3 → F:** the proof may use H3 premises that F lacks.
  - A fresh strict check against other bytes produces a new certificate for that CNF; it is not a transfer.
- **(2) Semantic covers.**
  - An F-leaf certificate implies that the corresponding F_H3 leaf is UNSAT, by monotonicity. Cite the F certificate; do not issue an F_H3 receipt for it.
  - A separate semantic genuine-configuration ledger may mix F-leaf and F_H3-leaf certificates, provided:
    - all leaves come from one validated full-product partition over base variables (H3 adds none), with identical units;
    - every certificate is strictly checked against its exact bytes and parent re-solved or replayed;
    - the ledger cites the bridge, HALL3 §1 and the reviewed H3 generator/body SHA, plus r2 and c112 if the r2 reduction is used.
- **Never countable:**
  - F_H3 certificates, either in the F Boolean ledger, or toward "F is UNSAT", or to change any F-leaf state (UNKNOWN stays UNKNOWN);
  - proof-free runs, including the 600 s pilot even if it returns UNSAT;
  - SAT models presented as counterexamples.

**Novelty and significance (non-dispositive):**
- There is no novelty: this is the classical Hall condition at t = 3.
- The note itself says H3 may be redundant in F (`HALL3:29`), so its value is empirical.

### (j) Generator (optional; does not affect the dispositions)

- **Emission matches §3 exactly** (`hp:164-176`):
  - 15 lines × 5 squares, in both orientations (`hp:53-57`);
  - the raw count of 235,200 is asserted;
  - literals come from the pinned map, with a 7,840-entry injectivity check (`hp:150-156`);
  - `G()` (`hp:157-163`) matches `g()` in `gram_a.py` in generic mode with CL empty, using the same sorted key;
  - `simplify` (`hp:60-66`) behaves like `CNF.add`;
  - the header variable count is unchanged, so no new variables are introduced.
- **Old leaf binding:** the old leaf's identity is re-verified, and H3 is appended before the same 21 units (`hp:286-290`).
- **Controls match HALL3 §4 and README §10** (`hp:184-213,215-275`):
  - the bad pattern passes G3 but fails H3, and the H3-only CNF must return UNSAT;
  - the identity, shift, Fourier and H2-block supports must pass;
  - the AG(2,8) positive drops exactly 5 P4-ALO clauses and 7 Q1-SB2 units, fixes all 7,840 g variables, and gets a full model check.
- **Minor observations:**
  - lines 71–139 (runner and guards) are not in the excerpt, so I did not review them;
  - "exact ONB matrices" are tested at support level only, which is sufficient because H3 depends only on supports;
  - for column lines, ⊤ sits at M[c][0] rather than M[c][c]; this is immaterial because every (R, C) pair is enumerated;
  - the emitted count is recorded rather than asserted, since no value was frozen;
  - `new_variables: 0` is hard-coded rather than computed, but it is true by construction.

K5NF-r2 FATAL=0 MAJOR=0 MINOR=4
HALL3-r1 FATAL=0 MAJOR=0 MINOR=3
GENERATOR: CONSISTENT
