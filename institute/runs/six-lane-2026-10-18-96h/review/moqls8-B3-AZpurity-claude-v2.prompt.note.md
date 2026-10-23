**Verdict: 0 FATAL / 0 MAJOR / 7 MINOR.**

- **Frozen candidate: 5 MINOR.** [CX] MINOR 1–3 are upheld. Two findings are new (N1, N2).
- **Erratum 1: 2 MINOR** (E-a, E-b). Both come from the erratum's own wording.

Theorems U, U′ and the A-only refinement hold under H1, H2 and H4. H3 is never used. Theorem L holds only as the implication Σ ⇒ (a)–(c). Nothing in the packet shows Σ is satisfiable, so Theorem L may be vacuous.

This review reads [J]'s six listed supports as exact: every listed coordinate is nonzero, as H4 asserts. The supplied entry (`supports_row2to7`) does not say this itself. Every full-support step below depends on it.

### 1. Claim-by-claim

**Frozen candidate**

| Lines | Claim | Verdict |
|---|---|---|
| L15 | supp q_1^6 = {2,3}, supp q_1^7 = {1,2,3} | Hypothesis ([J] rows 6, 7) |
| L15 | supp q_1^1 = {1,2,3} | True, but not in [J] (which lists rows 2–7 only) and not derived. **N1** |
| L17 | F1 | Valid |
| L18 | F2, common and own versions | Valid for every d and r, including 0. (i,c) ≠ (0,d) because i ≥ 1; (i,c) ≠ (r,0) because c ≥ 1 |
| L19 | AX | Valid. It does not remove the e_1-component of q_s^6 |
| L20–21 | S, P | Valid |
| L25–36 | Theorem U: 25 slots, demand 16, σ_1 ≥ 5, excess ≤ 4, at least 12 pure | Valid. The range c ∈ {1..7} for σ_1 is unstated ([CX]-1, extended) |
| L29, L35 | A-only: 18 slots, demand 12, σ_1^A ≥ 4, excess ≤ 2, at least 10 pure | Valid |
| L40–54 | Theorem U′: 25 slots, demand 16, τ_1 ≥ 5, excess ≤ 4, at least 12 own-pure | Valid with the own-basis bridge ([CX]-1). The range i ∈ {1..7} for τ_1 is unstated |
| L58–71 | Theorem L (a)–(c) and the Latin arrays | Valid only as Σ ⇒ (a)–(c) |
| L73 | The tight frame "constrains the amplitudes of q_1^r" | False as an extra restriction ([CX]-2) |
| L77–79 | §5 coincidences (0,0) and (6,1); at most 4 per cell | Valid. It is a trivial union bound |
| L83 | "Proved: … Theorems U, U′, L" | Accurate only if read as the implication Σ ⇒ L (editorial) |
| L86 | "at-most-4 excess vectors" | Names the wrong quantity ([CX]-3) |
| L81–90 | "Exact unresolved boundary" | Incomplete: row 6 and column 1 of the frozen corner are missing. **N2** |
| L3 | "Every lemma used is re-proved here" | False as frozen (bridge, N1). True after the repairs |
| L5, L11 | "NEW"; "not in the prior notes" | Uncertified. E4 governs L11; L5 is not named (editorial) |

**Erratum 1**

| Item | Verdict |
|---|---|
| E1 definitions, bridge and own-slot remark (Err L7–11, L15) | Correct |
| E1 restated L52 step (Err L13) | Logically inverted. **E-a** |
| E2 (Err L17–31) | Correct. The BB* identity was verified independently (§3) |
| E3 replacement and "Equivalently" (Err L35–39) | Correct in substance. A literal splice duplicates a clause, and "Equivalently" is false. **E-b** |
| E4 (Err L41–47) | Correct |

### 2. Independent verification

**Tensor condition.** For s ≠ t and positions p ≠ p′:

⟨Q_s(p),Q_s(p′)⟩⟨Q_t(p),Q_t(p′)⟩ = 0.

- **F2.**
  - Common version: take p = (i,c) and p′ = (0,d), using |w| = 1.
  - Own version: take p′ = (r,0). It shares the index r only; q_s^r and q_t^r remain different vectors.
- **AX.**
  - Derivation: take p = (r,0) and p′ = (0,d) with r, d ≥ 1, plus q_s^r ⊥ q_s^0 ∝ e_0.
  - Uses: L33 (q_s^1, q_s^7 ⊥ span{e_0,…,e_3}), L48 (r = 1, 7, and q_s^6 ⊥ e_2, e_3) and L77. Each use matches exactly what AX gives.

**Counts (re-derived).**

- **Theorem U, row r ∈ {1,7}.**
  - Slots are (c,d) with c ∈ {1..7} and d ∈ U∖{c}: 3·3 + 4·4 = 25.
  - Each pair (s,d) with s ≥ 2 has row mass exactly 1 by S and AX, so n_{s,d} ≥ 1. Demand is 16.
  - Square 1 has e_0-mass 1, which takes at least one slot.
  - The projected row resolution, sum_{c≥1} P_A|Q_1(r,c)⟩⟨Q_1(r,c)|P_A = P_A − |q_1^r⟩⟨q_1^r|, has rank 2. So at least two A-parts are nonzero.
  - Each A-part is ⊥ q_1^r, by row orthogonality and q_1^r ∈ V_A. Because q_1^r has full support, no A-part is ∝ e_d. So σ_1^A ≥ 4 and σ_1 ≥ 5.
  - Excess ≤ 25 − 16 − 5 = 4.
  - A-only version: 18 slots, demand 12, excess ≤ 18 − 12 − 4 = 2.
- **Theorem U′, column c ∈ {2,3}.**
  - Slots are (i,r) with i ∈ {1..7} and r ∈ O′∖{i}: 3·3 + 4·4 = 25.
  - Demand is checked for each pair (s,r) separately, never across squares:
    - r = 0 because q_s^0 ∝ e_0;
    - r = 1, 7 by AX;
    - r = 6 because q_s^6 ⊥ e_2, e_3 and c ∈ {2,3}.

    Demand is 16.
  - Square 1: own index 0 has mass 1, giving one slot.
  - The column A-content P_A − |e_c⟩⟨e_c| has rank 2, so at least two A-parts a ⊥ e_c are nonzero.
  - In the orthonormal basis {q_1^1, q_1^6, q_1^7} of V_A, a single nonzero coefficient would make a ∝ q_1^r with ⟨e_c,q_1^r⟩ ≠ 0. That contradicts a ⊥ e_c.
  - The self-index r = i never occurs (F1).
  - So τ_1 ≥ 5 and excess ≤ 4.

**Purity.** If n_{s,d} = 1, then |⟨e_d,Q_s(r,c)⟩| = 1, so the whole vector is ωe_d. The own-frame version gives ωq_s^r in the same way. The number of nonpure pairs is at most the excess.

**Double counting.**

- **Inside one bound there is none.**
  - Different squares are separated by F2.
  - Different pairs of the same square use different slots.
  - Two pure pairs of one square cannot share a cell, because e_d ⊥ e_{d′} and q_s^r ⊥ q_s^{r′}.
- **Across bounds there are two overlaps.**
  - A ⊂ U.
  - Common/own coincidences. These occur only at the cells {1,7}×{2,3}, and only for:
    - (r′,d) = (0,0), which is automatic for any ωe_0 there;
    - (r′,d) = (6,1), which needs q_s^6 ∝ e_1. By AX this is possible for at most one s ≥ 2.

**Theorem L.**

- A corner A-part is ⊥ e_c (F1) and ⊥ q_1^r (row orthogonality). So it lies on the line spanned by g_c := Be_c (§3), which vanishes exactly at coordinate c.
- Under Σ this gives σ_1^A = 6 and A-excess 0.
- The 12 pure whole vectors then fill the 12 free A-slots at c ∈ {4..7} bijectively.
- One vector per cell gives distinct columns for each square and distinct squares at each cell. The fourth square at each cell has no A-coordinate.
- Column orthonormality within square s gives (c).
- The purity in (b)–(c) is whole-vector purity of squares 2–5. Square 1 contributes only projected parts.

**Σ stays conditional.** L11, L58–60, L73 (as replaced) and L87 all keep Σ hypothetical. Theorems U, U′ and §5 never use it.

### 3. Erratum 1, checked

**E2.**

- Let κ_c := ⟨e_c,q_1^r⟩. This avoids the erratum's reuse of a and c. Then B is the cross-product matrix of conj(κ).
- Each column g_c has g_c(c) = 0 and ⟨q_1^r,g_c⟩ = 0, so it spans the corner line at (r,c).
- BB* = I − qq*.
- B*B = I − conj(q)qᵀ. Equivalently, ‖g_c‖² = 1 − |κ_c|² and ⟨g_c,g_{c′}⟩ = −conj(κ_c)κ_{c′} for c ≠ c′.
- So a weighted tight frame on the three corner lines exists for every unit, full-support q. It imposes no restriction on the amplitudes.
- The withdrawal, the replacement and the "conditional only" paragraph are all correct. [SIG] is not used.

**E-a (Err L13).** The clause reads "then a ∝ q_1^r with c ∉ supp q_1^r, contradicting a ⊥ e_c".

- "c ∉ supp q_1^r" is not derived, and it does not conflict with a ⊥ e_c.
- The contradiction actually comes from a ∝ q_1^r together with c ∈ supp q_1^r.
- The next sentence supplies the needed fact, so the argument is recoverable. The sentence as written is still a non sequitur.

**E-b (Err L35–39).**

- **"Equivalently" is false.** An excess E := sum(n − 1) ≤ 4 implies at most four nonpure pairs, but the converse fails: a single pair with n = 6 is one nonpure pair with E = 5.
- **The literal splice duplicates a clause.** Inserting the replacement into L86 produces "…together with the guaranteed pure pairs, together with the forced pure vectors…".
- **The substance is correct.** The excess bound only limits nonpure U-carrying cells to #nonpure + E ≤ 8 per application, not to 4.

### 4. Adjudication of [CX]

| [CX] finding | Adjudication | Status after Erratum 1 |
|---|---|---|
| 0 FATAL / 0 MAJOR | Upheld | — |
| MINOR 1 | Upheld and extended. σ_1 (L25) and τ_1 (L40) also need the ranges c, i ∈ {1..7}. Counting c = 0 or i = 0 adds three nonzero entries and turns the bounds into stronger, unproved ones | Bridge supplied; E-a and the ranges still open |
| MINOR 2 | Upheld; the BB* identity was re-verified | Closed |
| MINOR 3 | Upheld | Closed in substance; E-b open |
| Count table, AX audit, e_1 retained in q_s^6 | Upheld | — |
| Meaning of a pure pair; no double counting; overlap list | Upheld | — |
| §5 analysis | Upheld | — |
| "Under Σ, all three A-projections are nonzero" ([CX] L85) | Upheld under either reading of Σ (§6) | — |
| "Self-contained from the stated hypotheses" ([CX] L134) | Qualified by N1 | N1 open |
| H3 unused | Upheld | — |
| Not found by [CX] | N1, N2 | Open |

### 5. Exact repairs

**N1 (L15).** Load-bearing at L19, L33–34, L48, L52/E1 and, for r = 1, L68. Replace "so that supp q_1^1 = supp q_1^7 = {1,2,3} and supp q_1^6 = {2,3}" with:

> [J] gives the exact supports of q_1^2,…,q_1^7; in particular supp q_1^6 = {2,3} and supp q_1^7 = {1,2,3}. Then supp q_1^1 = {1,2,3}. By H2 and column-0 orthonormality, q_1^1 ⊥ e_0. Also q_1^2,…,q_1^5 span span{e_4,…,e_7}. Hence q_1^1 ∈ V_A ∩ {q_1^6,q_1^7}^⊥, which is spanned by conj(q_1^6 × q_1^7). Write q_1^6 = (0,β,γ) and q_1^7 = (α′,β′,γ′) in coordinates 1, 2, 3, with all displayed entries nonzero. The spanning vector is conj(βγ′ − γβ′, γα′, −βα′), whose last two entries are nonzero. If βγ′ = γβ′, then (β′,γ′) ∥ (β,γ), and q_1^6 ⊥ q_1^7 forces β′ = γ′ = 0, contrary to supp q_1^7.

**[CX]-1 extension (L25, L40).** Add "σ_1 counts pairs (c,d) with c ∈ {1,…,7}" and "τ_1 counts pairs (i,r) with i ∈ {1,…,7}".

**E-a (Err L13).** Replace the clause with:

> then a ∝ q_1^r; since c ∈ {2,3} ⊆ supp q_1^r, ⟨e_c,a⟩ ≠ 0, contradicting a ⊥ e_c.

**E-b (Err L35–39).**

- Make the replaced span at L86 the whole phrase "the at-most-4 excess vectors of Theorems U and U′, together with the forced pure vectors".
- Change "Equivalently" to "In particular".
- Add "the converse fails".

**N2 (L7, L81–90).**

- At L7, add "a sub-corner of the frozen target rows {1,6,7} × columns {1,2,3}".
- In §6, add:

  > Row 6 and column 1 of the frozen corner are not treated. AX leaves an e_1-component in q_s^6 for at most one s ≥ 2, so the unit-demand step can fail for (s,1) in row 6 and for (s,6) in column 1. Since 1 ∉ supp q_1^6, square 1 may have an A-part ∝ e_1 in row 6, or ∝ q_1^6 in column 1. So σ_1^A ≥ 4 and τ_1 ≥ 5 are unavailable there.

- Clarify "(rows 2-6 and 7 versus columns 4-7, …)" at L86.

**Editorial (not counted).**

- L83: write "Theorem L (as Σ ⇒ (a)–(c))".
- L5: qualify "NEW" the same way E4 qualifies L11.
- L56: change "a family statement" to "a statement about the possibly empty Σ-family".
- L58: state Σ as "{c ∈ {1..7} : P_A Q_1(r,c) ≠ 0} = {1,2,3}".
- L77: change "⊥ U" to "⊥ span{e_d : d ∈ U}".
- H3 is undefined in the packet and never used.

### 6. Reviewer remark (not a repair; do not import without review)

Under Σ, sum_c |a_c⟩⟨a_c| = Π_{P_r}, with each a_c ∈ span g_c.

- **The decomposition is unique.** No two g_c are parallel, so the operators |g_c⟩⟨g_c| are linearly independent. To see this, apply a vanishing real combination to a nonzero h ∈ P_r with h ⊥ g_2: this forces λ_1 = λ_3 = 0, and then λ_2 = 0. So BB* = Π_{P_r} is the only such decomposition.
- **Hence ‖P_A Q_1(r,c)‖² = 1 − |κ_c|², which lies strictly between 0 and 1.**

This has three consequences:

1. Reading Σ as "contained in" already forces all three corner A-parts to be nonzero.
2. Square 1's corner entries always keep a non-A component of squared norm |κ_c|² > 0. This is consistent with [CX] L89.
3. The frame fixes the A-norms, not q. This supports E2.

None of this says whether Σ is realizable.

### 7. Limits of this review

- This is a written review only: no tools, computation, enumeration, edits or delegation. [SIG] was not read or used.
- Theorem L may be vacuous.
- No family elimination, realization, full-grid witness or B3 no-go follows.
- Nothing changes for GB, the UNKNOWNs, A10/A11 or n = 8.
- Novelty is not certified.
- Every verdict above is conditional on the [J] supports being exact.
