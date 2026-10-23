**DISPOSITION: ACCEPT-WITH-FIXES.** 0 FATAL, 0 MAJOR, 10 MINOR.

**Scope.** This review covers SOURCE00's written Boolean model-existence argument for P1-B1, P1-B2, P1-B3 and P1-B5 only. I read it against the inline encoder text (SOURCE01), run with the argv in SOURCE07 and the unit table in SOURCE03.

**Limits of this review.**
- It is a static audit of the inline text only. I recomputed no hashes and read no CNF, name table or file.
- No solver, census or other computation was run.
- It gives no parent acceptance, ledger amendment, gate or native-launch authority.
- No strengthened CNF exists, and no n=8 result follows.

## Audit by item

### 1. Local support lemma (SOURCE00:LF27–69): verified

**(A), (B) and (C) hold as Boolean facts in every model.**
- For the (row0, col0) line pair, SOURCE01:LF182 builds `M[c][i] = g_s((0,c),(i,0)) = X_s(i,c)`. This is the transpose of X_s.
- Index 0 of M is True only at (0,0) and constant False elsewhere (LF128–131), so it adds no clauses.
- LF184 gives nonempty columns of X_s. LF185 gives nonempty rows. Together these are (A).
- LF187–188 (`both`) forbid two columns of X_s meeting in exactly one row. LF189–190 (`bothc`) forbid two rows meeting in exactly one column. Together these are (B).
- The b3 variables are defined in both directions (LF73–75). So (B) holds in every model, not just canonical ones.
- (C) is LF151–153 applied to the pairs ((0,c),(i,0)) with c, i ≥ 1.

**AND-name caching is safe.**
- `("b3",s,x,y,z)` always means g_s(x,z)∧g_s(y,z), whether `both` or `bothc` created it.
- `("c4",s,a,p,q)` always means g_s(a,p)∧g_s(a,q).
- No name stands for two different conjunctions.

**Degree and isolation steps are correct.**
- Row 1 (fixed by SB2), row 7, column 2 and column 3 of X_1 each have degree 3. So in each of X_2..X_5 they are singleton isolated edges.
- The singleton columns used by rows 1 and 7 lie in B and are distinct.
- The singleton rows used by columns 2 and 3 are distinct and lie outside {1, 6, 7}.
- The removed columns meet only removed rows. So the 3×3 remainder R_s still contains row 6 and column 1, and inherits (A) and (B).

**The 3×3 classification is complete.**
- The 3×3 supports with nonempty rows and columns that satisfy (B) are: 6 permutations, 9 K22-plus-edge, 9 K33-minus-edge and 1 K33. That is 25, which is consistent with SOURCE03:LF13.
- Row 6 and column 1 each have degree at most 7−2−3 = 2. This rules out K33 and forces the single zero of K33-minus-edge to sit at (6,1).
- Two zeros are impossible. Two zeros in one row or column create a singleton. Two zeros in different rows and columns create an exactly-one overlap.

**The bound k ≤ 3 is correct.**
- A1 and A6 contain only non-permutation squares, and each has at most one member.
- A non-permutation square outside A1 ∪ A6 must be K22 plus an isolated edge at (6,1).
- X_1(6,1) = 0, so (C) allows at most one such square.

**The counting bounds are correct.**
- A non-permutation X_s has exactly 9 or 12 ones (4 isolated edges plus 5 or 8), so the "≥ 9" bound is valid.
- With m = [12,14,16,18,17,20], the counts give minimum permutation numbers [1,1,2,3,2,4].
- Only B1 needs the structural k ≤ 3. B2, B3 and B5 follow from counting alone.

The lemma uses no G4, G5, PSD, rank or phase condition.

### 2. Primary transformation (SOURCE00:LF71–96): verified, including existence of the auxiliary extension

**Constants and primaries.**
- T maps rows to rows and columns to columns, and fixes row 0 and column 0.
- It preserves the same-cell, same-row and same-column constants (LF127–131). The classical-line constants at LF132–136 are inactive in generic mode.
- T is a bijection on the 1568 primary variables of each square. τ is a bijection with τ(1) = 1.

**G2–G5 are invariant.** These constraints depend only on cell geometry, so they are invariant under any row permutation × column permutation × square permutation. This includes three edge cases:
- In G3, a line pair whose image is in the opposite order gives the transposed overlap matrix; G3's conditions are symmetric under transposition.
- In G4, when p and q share a row or column, g(p,q) is constant False and the clause reduces to "|I| ≠ 1".
- In G5, constant instances reduce to clauses of the form `¬u ∨ ¬g(p,a)`.

**The auxiliary inventory is complete.** The note does not state this; I checked it.
- The `f.var` call sites in SOURCE01 are:
  - LF98, L variables: unreachable, because CL = [] at LF87 and every L call sits inside `for t in CL`.
  - LF138, g.
  - LF72, the AND helper, which creates b3 (LF187, LF189) and c4 (LF201).
  - LF220, u5.
  - LF242, w3.
  - LF262, lexeq.
- The counts add up exactly: 7,840 g + 94,080 b3 + 376,320 c4 + 31,360 u5 + 280 w3 + 35 lexeq = 509,915. This matches SOURCE03:LF6 and SOURCE07:LF28.
- b3, c4, u5 and lexeq are each defined in both directions, so their recomputed values are forced. w3 is handled in item 3.
- No permutation of auxiliary IDs is needed. A naive one would actually fail: under σ = (4 5), `b3(s,(r,4),(r,5),z)` maps to the cell order ((r,5),(r,4)), which is not an allocated name.

**The clause count leaves no room for a hidden family.**

| Family | Clauses |
|---|---:|
| G2 | 15,680 |
| G3 | 479,360 |
| G4 | 1,975,680 |
| G5 | 3,261,440 |
| P4 | 7,845 |
| ROWLEX | 190 |
| SB2 | 35 |
| **Total** | **5,740,230** (matches SOURCE02:LF50) |

### 3. P4 (SOURCE00:LF98–107): verified

- Each square has 56 flags. Each flag has 28 one-way clauses (LF244–245) and the square has one ALO (LF247), giving 1,569 clauses per square.
- No one-way clause is dropped, because the overlap literals are never True for a cell off row 0.
- The predicted Q1 ALO index is 5,733,728, and ALO_t = 5,733,728 + 1,569(t−1). These match SOURCE04:LF12 and LF14–17 exactly.
- The extension sets w3(1,0,(1,0)) true and every other w3 flag false. This satisfies every retained clause for any primary pattern with SB2's row 1, because every 6-subset of 8 coordinates meets {1,2,3}.

### 4. SB2, ROWLEX, stabilizers and orbits (SOURCE00:LF109–140): verified

**SB2.** ρ(1) = 1 and σ fixes 1, 2, 3, so Q1's row 1 stays {1,2,3}. Row 1 of X'_{τ(s)} is {σ(s+2)} = {τ(s)+2}, so the same 35 units hold.

**ROWLEX.**
- The keys are rows 2–7 of X_1 (LF253–255) plus the constant bit k = 0.
- lexeq is defined in both directions, so ROWLEX holds after the move exactly when X_1 is invariant under (ρ, σ).

**Unit decoding.**
- From the square-major allocation at LF141–144, g_1((0,c),(i,0)) has ID 49c + 7i − 6.
- All 168 units of the four P1 leaves match supports_row2to7.

| Leaf (SOURCE03 block) | Rows 2–5 | Generators (σ, ρ) | B-orbits | Formulas |
|---|---|---|---|---|
| P1-B1 (LF521–598) | {7},{6},{5},{4} | any σ ∈ Sym(B), ρ = rσr⁻¹ with r(b) = 9−b | {4,5,6,7} | M2 |
| P1-B2 (LF599–678) | {7},{6},{45},{45} | (45), id; (67), (23) | {4,5}, {6,7} | M2 or M4 |
| P1-B3 (LF679–760) | {67},{67},{45},{45} | (45), id; (67), id; (46)(57), (24)(35) | {4,5,6,7} | M2 |
| P1-B5 (LF845–927) | {7},{56},{456},{456} | (56), id | {4}, {5,6}, {7} | M2 or M3 |

- Rows 6 ({2,3}) and 7 ({1,2,3}) and SB2's row 1 are fixed by every generator.
- The orbits are as large as this method allows. σ must preserve the column degrees of X_1:
  - B2 has column degrees 2, 2, 1, 1 on 4, 5, 6, 7.
  - B5 has column degrees 2, 3, 3, 1 on 4, 5, 6, 7.
  - So these orbits cannot merge.
- B5 needs at least two permutation squares because SB2 gives the squares distinct row-1 labels. At most one permutation square can therefore sit in the orbit {7}.
- Six formulas in total is correct: 1 + 2 + 1 + 2.

### 5. The M_s clauses (SOURCE00:LF142–150): verified

- The clauses are 6 × C(7,2) = 126 at-most-one constraints.
- Together with G3's row-nonempty clauses (LF185), SB2's row 1 and the constant bit k = 0, they say exactly that X_s is a permutation.
- They touch only Q_s's column-0 overlap bits and assume nothing about classicality. The new clause count would be 5,740,268 + 126 = 5,740,394.
- If all six strengthened formulas are UNSAT, the four original leaves are UNSAT.
- For B2 and B5, both of their formulas must be refuted.

### Attacks tried without finding a defect

- b3/c4 name collisions.
- Collinear G4 clauses and constant G5 clauses.
- ROWLEX with ρ ≠ id.
- P4 clauses being dropped.
- Hidden L variables.
- k = 4 for B1.
- K33 as R_s.
- Asymmetric dependence through lexeq, Q1-only ALO, line-ordered b3 names or line-anchored u5 names. Each is handled by τ(1) = 1, the template stabilizer and recomputation.

## Findings (all MINOR)

1. **Undefined symbol.** SOURCE00:LF101 says "sigma fixes A", but A is never defined (LF60 uses A1 and A6 for sets of squares). **Repair:** say "fixes 0,1,2,3 pointwise (LF73)".

2. **SB2 versus template attribution.**
   - SOURCE00:LF41 credits row 1's {1,2,3} to the P1 template. It comes only from SB2 (SOURCE01:LF276–281); the 42 units fix rows 2–7.
   - SOURCE00:LF110 says SB2 helps fix the ROWLEX keys. It fixes none of them, since the keys are rows 2–7.
   - **Repair:** attribute each fact to its actual source.

3. **Orientation is left implicit.**
   - SOURCE00:LF29–38 never says the encoder's matrix is X_sᵀ, with `both` checking columns and `bothc` checking rows.
   - SOURCE00:LF82–83 mentions "transposition". It arises only from the order in which `combinations` lists the image line pair, never from T itself.
   - This is harmless, but it should be stated.

4. **Completeness of the auxiliary families is only implicit.** SOURCE00:LF93–96 and §3 do not claim that b3, c4, u5, w3 and lexeq are all the allocated variables, which is the crux of the extension argument. **Repair:** add the call-site list and the 509,915 count identity from item 2.

5. **Instance-flag dependencies are uncited.**
   - SOURCE00:LF89–91 and LF104–107 rely on no fixg, ngeneric 0, the --sb2, --g5 and --rowlex flags, and P4 frames = [0] only.
   - With --p4-all-rows (SOURCE01:LF234), Q1 would need a witness in every one of 8 frames, and the single (1,0) flag would not suffice.
   - LF105 cites "233–247" as the one-way clauses. The one-way clauses are LF244–245; LF247 is the ALO.
   - **Repair:** cite SOURCE07:LF7–25 as an imported binding (via SOURCE06:LF28) and correct the line citation.

6. **The stabilizer check is asserted, not shown.** SOURCE00:LF128–129 says it "can be checked directly" but gives no table, no line citations and no decoding of units to bits. **Repair:** include the table and the decoding 49c + 7i − 6 from item 4.

7. **B5 wording.** SOURCE00:LF134–135 does not say why the labels are distinct (SB2 assigns s+2). It also omits the identity case, where label 5 gives M3 directly. **Repair:** add both points.

8. **Scope wording.**
   - SOURCE00:LF10 calls F_one a "no-classical-square instance". This can be misread as excluding classical squares 2–5. It actually means ngeneric = 0; squares 2–5 are unrestricted (SOURCE05:LF33–34).
   - LF69 computes bounds for B4 and B6, but the claim drops P1-B4 and P1-B6 without comment.
   - **Repair:** state that P1-B4, P1-B6 and all P0/P2 leaves are untouched and remain exact-input obligations.

9. **§5 is not pinned.** SOURCE00:LF144–150 gives the clause semantics only. **Repair:**
   - Pin the literal IDs as ID(s,c,i) = 1568(s−1) + 49c + 7i − 6. The s = 1 case matches the 168 template units. The s ≥ 2 cases are derived here only and must be bound independently to the name table.
   - Fix the append order after the 42 units and the header 509915/5740394.
   - Compute six SHAs independently.
   - Add controls: sign-flip, wrong-square, and an SB2 cross-check (Q2's row-1, coordinate-4 unit should decode to +1765).

10. **Transfer wording versus the parent contract.**
    - SOURCE00:LF23–25 promises "literal Boolean UNSAT" of the four leaves. That is mathematically right, but only through this meta-lemma; it is not a checker-verified proof of the exact inputs.
    - Under SOURCE06:LF14 and LF40–41, each original input still needs a qualifying exact-input refutation unless the parent amends the contract. LF153–156 already concedes this.
    - **Repair:** make LF23–25 say this too.

## Boolean model existence vs. unitary images vs. CNF automorphisms

**Literal Boolean model existence is what the note proves.** It gives a total map from every model of F_one∧C to a model of F_one∧C∧M_s for a listed s. This includes models with no vector, phase or rank realization. The map is: relabel the primaries, recompute b3, c4, u5 and lexeq (whose values are forced), and set w3 explicitly.

**Unitary images play no role.** §1 uses only G2 and G3. Nothing from A8, W8, T16, PSD or the physical normalization is invoked. The weaker physical-image result in proposal 34e90d73…284a is neither needed nor substituted.

**No whole-CNF automorphism is claimed, and the naive form would be false.**
- The ROWLEX literals sit at fixed row positions.
- The SB2 units are specific to each square.
- The b3 and u5 names depend on line order or line anchor.

The map is a model transformation, valid only for the listed template stabilizers with τ. It is not a permutation of F_one's clause set.

## Binding limits

- Every SHA string in SOURCE00–07 is taken as declared; none was recomputed.
- The identity "F_one = gram_a.py run with SOURCE07's argv, minus four ALO lines" is imported from SOURCE06:LF27–28 and SOURCE02/04.
  - My arithmetic reproduces 509,915 variables, 5,740,230 clauses, the five ALO indices and all 168 P1 units.
  - That is consistent with byte identity but does not prove it.
- SOURCE06 accepts three things (LF12–14): the bridge, T16, and the canonical extension for actual Gram supports.
  - It does not accept this transformation, the M_s clauses, or substituting six strengthened formulas for four WMAN inputs.
  - Its LF14 and LF37–41 stand unchanged.
- Proposal 34e90d73…284a was not provided; I neither reviewed it nor relied on it.
- No M_s formula has been generated.

## Audited vs. imported

**Audited here (static, inline text):**
- (A)/(B)/(C) and the soundness of name caching.
- The 3×3 classification, k ≤ 3, the ≥ 9-ones bound, the m values and the bounds [1,1,2,3,2,4].
- Invariance of G2–G5 under the transformation.
- Completeness and forced values of the auxiliary families, and the variable and clause count identities.
- P4 block structure and ALO indices; the P4, SB2 and ROWLEX extensions.
- Unit decoding for the four leaves; invariance under each generator; orbit selection, including minimality for this method.
- The meaning and count of the 126 M_s clauses.

**Imported, not audited:**
- All bindings of bytes and hashes for the CNFs, WMAN, name table and encoder.
- The parent's verification of the four deletions.
- The physical chain (A8, W8, T16, bridge §3). It is irrelevant to this lemma but required for any n=8 conclusion.
- Solver and checker outcomes: none exist for the six formulas.
