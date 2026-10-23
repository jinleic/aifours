# Hostile review: MOQLS8 P1-B3 "full row 1 by own-frame reuse" (candidate `84506494…`, with parent erratum v1 applied)

## Verdict

At the scope set by parent erratum v1, the mathematics is correct:

- **Lemma 1** is an exact characterization; both directions hold.
- **D** is well defined and nonempty.
- **Theorem R1** holds for every member of D, uniformly in all amplitudes and phases.

**Mathematical counts: 0 FATAL / 0 MAJOR / 5 MINOR.** The five MINORs are scope wording and convention precision only.

**Process:** erratum item 2's permanent process MAJOR stands. This review is independent of the Python run and does not cure it.

I re-derived every table below by hand in this response. I used no tools, files, code or computation, so I did not recompute any hashes.

## 1. Claim-by-claim

| # | Lines | Claim | Verdict |
|---|---|---|---|
| C1 | LF9–16 | H1–H4 and the q / S / T notation | Accept; MINOR-2 |
| C2 | LF18–23 | R, the partial-datum definitions, and "(E1)/(E2) are exactly H1 restricted to R" | Accept; MINOR-2, MINOR-3 |
| C3 | LF27–45 | Lemma 1 (iff) | **Accept, both directions** (§2.1) |
| C4 | LF51–65 | Lemma 2 | Accept. Valid for any axis datum; sufficient only, as LF197 says |
| C5 | LF69–78 | π_s are permutations, π_s(1) = s+2 | Accept (V1) |
| C6 | LF80–86 | Class D | Accept. LF116 and LF198 read per erratum item 1 |
| C7 | LF88–102 | Lemma 3, axis equations | Accept (V2) |
| C8 | LF104–114 | Nonemptiness example | Accept (V3) |
| C9 | LF120–152 | φ table, Theorem R1 | Accept (V4–V7) |
| C10 | LF154–163 | Explicit form, c_s table | Accept: all 28 entries recomputed and matching (V6) |
| C11 | LF167–171 | Remark L1 | Accept (§2.3) |
| C12 | LF173 | Exact scope | Accept; MINOR-4 |
| C13 | LF175 | Remaining obligation | Accept; complete under the set-level reading of "genuine" (MINOR-2) |
| C14 | LF5 | Outcome headline | Accept; MINOR-1 |
| C15 | LF179 | §7 consistency with INT | Not load-bearing; arithmetic correct; MINOR-5 |
| C16 | LF183–203 | Import table, ledger | Accept (LF198 per erratum) |
| C17 | LF3 | Provenance sentence | Withdrawn per erratum item 2 (process MAJOR) |

## 2. Hand verification

### 2.1 Lemma 1, both directions

R has 22 cells: row 0 (8 cells), (r,0) for r = 1..7 (7 cells), and (1,j) for j = 1..7 (7 cells). That gives C(22,2) = 231 unordered pairs:

| Pair class | Count | Why every (E2) product vanishes |
|---|---|---|
| Same row 0, column 0 or row 1, plus {(0,j),(1,j)} | 28+28+28+7 = 91 | Every factor is 0 by (E1) |
| (0,c),(r,0) with c, r ≥ 1 (axis pairs) | 49 | At most one square has a nonzero factor (V2) |
| (0,c),(1,j) with c ≠ j, including c = 0 (Type I) | 49 | At most one nonzero factor (V6, off-diagonal) |
| (r,0),(1,j) with r ≥ 2 (Type II) | 42 | At most one nonzero factor (V7) |

**(⇐)**
- (i), (ii) and the axis datum give (E1).
- The four pair classes above are exhaustive.
- (iii) gives Type I and (iv) gives Type II.

**(⇒)**
- (E1) gives (i) and (ii).
- Type I gives "no c ≠ j lies in two S-sets"; with (ii) this is (iii).
- Type II gives "no r ≠ 1 lies in two T-sets"; (i) gives 1 ∉ T_s, so this is (iv).

**The shared pair (0,0),(1,j)** is described both as Type I with c = 0 and as Type II with r = 0. The two descriptions agree because q_s^0 = w_{s,0} e_0, and the c = 0 column of V6 equals the r = 0 column of V7.

**Exactness of the restriction to R.** No interior equation is used, and no Gram-form equation on R is omitted. In particular, the unit norm of each (i,0) with i ≥ 2 is carried by the column-0 ONB.

### 2.2 Tables

**V1 (π table, LF69–78).** Each row is a permutation of 1..7:

- π_2 = 4,2,3,1,6,7,5
- π_3 = 5,3,2,7,1,6,4
- π_4 = 6,1,4,2,3,5,7
- π_5 = 7,5,1,3,2,4,6

Also π_s(1) = 4, 5, 6, 7 for s = 2..5, as H3 requires.

**V2 (Lemma 3 axis pairs).** Entry (r, c) is the unique square s with c ∈ supp q_s^r; · means no square.

| r \ c | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| 1 | 1 | 1 | 1 | 2 | 3 | 4 | 5 |
| 2 | 4 | 2 | 3 | · | 5 | 1 | 1 |
| 3 | 5 | 3 | 2 | 4 | · | 1 | 1 |
| 4 | 2 | 4 | 5 | 1 | 1 | · | 3 |
| 5 | 3 | 5 | 4 | 1 | 1 | 2 | · |
| 6 | · | 1 | 1 | 5 | 4 | 3 | 2 |
| 7 | 1 | 1 | 1 | 3 | 2 | 5 | 4 |

There are no collisions, so all 49 axis equations hold for every member of D. This agrees with LF92–100.

**V3 (nonemptiness example, LF104–114).**
- Norms: q^1 and q^7 have squared norm 1/2+1/4+1/4 = 1; q^6 has 1/2+1/2 = 1.
- ⟨q^1,q^6⟩ = (1/2 − 1/2)/√2 = 0 and ⟨q^7,q^6⟩ = (−1/2 + 1/2)/√2 = 0.
- ⟨q^1,q^7⟩ = 1/2 − 1/4 − 1/4 = 0.
- The pairs (e_6 ± e_7)/√2 and (e_4 ± e_5)/√2 are each orthonormal.
- Vectors with disjoint supports are orthogonal; the block dimensions sum to 1 + 3 + 2 + 2 = 8.
- All supports are exactly as required.

**V4 (φ table).**
- **Bijectivity:** each φ_s lists {0,2,…,7} once (columns of LF124–130).
- **(R2):** each row j has five distinct values.
- **Re-check:** every row of V7 contains each square exactly once, and every column of V7 contains all five squares.

**V5 (row-1 ONB).**
- Square 1: row 1 is a re-indexing of its column-0 ONB, by Lemma 2(i).
- Squares s ≥ 2: reading V6 by square, s occupies columns c_s(1..7) = [8] \ {s+2}, once each. Together with Q_s(1,0) ∝ e_{s+2}, this is the standard basis.

**V6 (Type I pairs, R1 and R3).** Entry (j, c) is the unique square s with c ∈ supp Q_s(1,j); (·) marks the diagonal c = j.

| j \ c | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|---|
| 1 | · | (·) | 5 | 2 | 1 | 1 | 3 | 4 |
| 2 | 3 | 2 | (·) | 4 | 5 | · | 1 | 1 |
| 3 | 5 | · | 2 | (·) | 3 | 4 | 1 | 1 |
| 4 | 4 | 1 | 1 | 1 | (·) | 5 | 2 | 3 |
| 5 | 2 | 3 | 1 | 1 | 4 | (·) | 5 | · |
| 6 | · | 4 | 3 | 5 | 1 | 1 | (·) | 2 |
| 7 | 1 | 5 | 4 | 3 | · | 2 | · | (·) |

- The empty diagonal is (ii)/(R1) for all five squares, so the 7 pairs {(0,j),(1,j)} vanish in every square.
- The off-diagonal entries have no collisions, so all 49 Type I pairs hold.
- The entries for s ≥ 2 are exactly c_s(j) = π_s(φ_s(j)), which reproduces LF156–161. Each row c_s plus {s+2} equals [8], and c_s(j) ≠ j throughout.

**V7 (Type II pairs, R2).** Entry (j, r) is the unique square s with φ_s(j) = r. Column r = 1 is omitted because 1 is not in the range of any φ_s.

| j \ r | 0 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| 1 | · | · | 2 | 1 | 5 | 3 | 4 |
| 2 | 3 | 1 | · | 2 | 4 | 5 | · |
| 3 | 5 | 2 | 1 | · | · | 4 | 3 |
| 4 | 4 | 5 | · | 3 | 2 | · | 1 |
| 5 | 2 | · | 4 | · | 3 | 1 | 5 |
| 6 | · | 4 | 3 | 5 | 1 | 2 | · |
| 7 | 1 | 3 | 5 | 4 | · | · | 2 |

- The factor in square s is ⟨q_s^r, q_s^{φ_s(j)}⟩ = δ_{r,φ_s(j)}. For s ≥ 2 this is literally ⟨e_{π_s(r)}, e_{π_s(φ_s(j))}⟩ up to phase.
- So all 42 Type II pairs with r ≥ 2 hold.

All 231 pairs are verified, independently of amplitudes and phases.

### 2.3 Remark L1

The proof is correct:
1. Rows 1–7 of column j form an ONB of e_j^⊥.
2. If all seven were reuse vectors, their indices would be distinct and their span would be (q_1^{m*})^⊥, where m* is the missing index.
3. That span equals e_j^⊥ only if q_1^{m*} ∝ e_j. This is impossible: q_1^0 ∝ e_0, and |supp q_1^m| ≥ 2 for m ≥ 1.

## 3. Findings

**MINOR-1 (LF5).** "Genuine B3 row-1 joint feasibility holds." comes before any quantifier. It can be read as holding for every genuine B3 axis datum, which LF173 and LF200 leave undecided.
*Repair:* "…holds on the class D of §4. Every member of D admits a row 1, hence some genuine B3 axis data do. Classes outside D are undecided."

**MINOR-2 (LF11; affects LF23 and LF175).** "Q_1,…,Q_5 are genuine QLS(8)" literally asserts that each square is non-classical ([PRIM] LF201–203). LF187 instead means a non-classical set ([PRIM] LF223–225). Genuineness is not a direct equation, so it has no restriction to R.
- **Set-level reading:** nothing is lost. Any classicalizing unitary for square 1 must be monomial because of H2, and a monomial map keeps supp q_1^2 two-element. So H2 and H4 imply genuineness for every full configuration, and LF175 is complete.
- **Per-square reading:** genuineness of squares 2–5 is an extra non-equational hypothesis on interior cells, and LF175 omits it.

*Repair:*
- LF11: "{Q_1,…,Q_5} is a genuine ([PRIM] LF223–225) set of pairwise orthogonal QLS(8)."
- Append to LF23: "Genuineness is not a direct equation; for full configurations it follows from H2+H4."

**MINOR-3 (LF23).** "Exactly the restrictions of the H1 axioms" is true for the Gram form of the axioms (unit norms plus pairwise orthogonality). The equivalent completeness identities, such as Σ_i Q_s(i,j)Q_s(i,j)* = I and tensor completeness, are not local to R.
*Repair:* "…of the H1 axioms (in Gram form) to R."

**MINOR-4 (LF173).** "The full-row two-frame conditions plus row ONBs" should say row 1. Nothing is shown for row 0 ∪ column 0 ∪ row i with i ≥ 2, whose column-0 anchors differ.
*Repair:* "…the row-1 conditions (i)–(iv) of Lemma 1 give no universal contradiction; rows 2–7 are not addressed."

**MINOR-5 (LF179).** "As they must be" asserts that INT's row-1 conditions follow from the direct equations on R alone. This file does not show that, and INT capacities derived from interior completability need not hold. The labels Z/A/B/C are also undefined here; from context they are ⟨e_0⟩, ⟨e_1,e_2,e_3⟩, ⟨e_6,e_7⟩ and ⟨e_4,e_5⟩. The arithmetic is correct: ⟨q_1^7,q_1^4⟩ = 0, and the q_1^7-energy over columns 2–7 is 1, all at j = 4.
*Repair:* delete "as they must be" and define the blocks, or mark the paragraph as an unverified cross-reference.

**Notes (not counted)**

- LF47 and LF116's first sentence make provenance and identity claims relative to INT and the sparsity datum. I cannot verify them from the supplied sources, but they carry no weight because the proofs are self-contained.
- LF16: S_s(a) does not depend on s.
- LF27: "for every s and j" is vacuous for (iii) and (iv). The set-versus-family wording in (i) is harmless.
- LF90: the "iff" also uses 0 ∉ supp q_s^r for r ≥ 1; only the "if" direction is needed.
- LF175: "interior column" means a column j ≥ 1.

**Erratum v1 check**

- **Item 1** is correct and sufficient. H2 fixes row 0 and q_s^0. Given column-0 orthonormality, D is cut out by the displayed supports, and the axis equations then follow from Lemma 3. LF57 and LF134 need no change.
- **Item 2:** the process MAJOR stands, and LF3's no-code sentence is withdrawn. Whether freeze LF25's "no code" disclosure falls under the same withdrawal depends on whether the run happened before 16:31:33. The supplied material does not settle that.

## 4. Governing scope

**What follows.** For every member of D (all w and u, and every unitary column 0 of square 1 with the exact template), the reuse row 1 satisfies every Gram-form H1 equation among the cells of R. So:
- No argument whose premises are only those equations can exclude any member of D.
- There is no universal row-1 contradiction.
- Any B3 exclusion must use an H1 relation involving some (i,j) with i ≥ 2 and j ≥ 1, or a lemma derived from such a relation.

**What does not follow:**
- B3 exclusion.
- Row-1 feasibility for B3 classes outside D.
- Any extension of this row 1, or of D, to rows 2–7.
- Full-grid feasibility.
- Compatibility with necessary conditions derived from interior cells.
- Any Boolean, GB or UNSAT statement.
- Any change to GB 15/18, the UNKNOWNs, B2, A10/A11 or n = 8.
