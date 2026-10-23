# Hostile review: P1-B3 column-0 support-sparsity candidate

**Basis.** I read the candidate `46288f4e…` (277 lines) together with erratum v1 `a9748009…` (items 1–3) and erratum v2 `021bfe54…`. Line numbers are 1-based and match the errata anchors (L61 is the type-P row, L94 is "3x3 list"). I used no tools, computation, tests, edits or delegation. I assessed the original A–D as stated and did not add a T-exclusion or any other strengthening.

## Verdicts

| | Verdict | FATAL / MAJOR / MINOR |
|---|---|---|
| A | ACCEPT-WITH-FIXES | 0 / 0 / 1 (editorial) |
| B | ACCEPT | 0 / 0 / 0 |
| C | ACCEPT-WITH-FIXES | 0 / 0 / 2 (wording/scope) |
| D | ACCEPT-WITH-FIXES | 0 / 0 / 1 (phrase that cannot be checked in this packet) |

There is one more MINOR outside A–D. No finding falsifies or weakens any theorem statement. All of them can be handled by a parent erratum, with the source left unchanged.

## A: sparse 7×7 unitary classification

Checked:
- **A1.**
  - A component (R,C) is closed under adjacency, so U[R,C′] = U[R′,C] = 0.
  - The R-rows are orthonormal in C^C and the C-columns are orthonormal in C^R, so |R| = |C| and the block is unitary.
- **A2.** ⟨row r, row r′⟩ = conj(U[r,c])·U[r′,c] = 0, so column c = {r}.
- **A3.**
  - If the two supports share exactly one column, the inner product is a single nonzero product, which is a contradiction.
  - If both supports equal {a,b}, the 2×2 block is unitary and |U[r,a]|² + |U[r′,a]|² = 1.
  - Then columns a and b vanish outside rows r, r′, giving an isolated size-2 component and contradicting k ≥ 3.
  - The proof correctly relies on actual column norms (L49).
- **A4.** Rows with exactly two entries use disjoint column pairs, so t ≤ ⌊k/2⌋ and nnz ≥ 3k − t. This gives f = 1, 4, 8, ≥10, ≥13, ≥15, ≥18.
- **Partition table.**
  - All 15 partitions of 7 are present.
  - Recomputed bounds: 18, 16, 17, 15, 18, 15, 13, 17, 16, 14, 12, 13, 11, 9, 7.
  - The survivors and their exact nnz (7 / 9 / 11 / 12, with the 3-block forced to exactly 8) are correct.
- **H and M.** M's rows have norm 1. Their pairwise products are 0, 0 and 1/2 − 1/4 − 1/4 = 0. M has exactly one zero and a connected support graph.
- **Erratum v1.1 (L61).** It is correct and needed. diag(1,−1,1,1,1,1,1) is type P but is not a scalar times a permutation matrix; the seven 1×1 blocks carry independent unit factors.
- **Erratum v2 (L94).**
  - F3 checks out: its rows are unit vectors, and each Hermitian product is (1+ω+ω²)/3 = 0. For rows 2 and 3 this reads 1 + ω̄ω² + ω̄²ω = 1 + ω + ω².
  - This is enough for the 9-entry realizability sentence.
  - B–D never construct a full 3×3 residual.

**A-1 MINOR, L47.**
- **Issue.** "Otherwise both supports equal some {a,b}." The complement of "meet in exactly one column" also contains the disjoint case, which is the lemma's conclusion, and there the sentence is false. The logic is right as intended; the case split is misstated.
- **Fix.** "Suppose the supports meet. If they meet in exactly one column, …; if in two, both equal some {a,b}. …"

## B: forced column-0 structure

Checked:
- **B0.**
  - (i) Each Q_s(i,0) with i ≥ 1 is orthogonal to w|0⟩, so the rows of W_s are orthonormal and W_s is unitary.
  - (ii) ⟨Q_s(0,c)⊗Q_t(0,c) | Q_s(i,0)⊗Q_t(i,0)⟩ = conj(w_{s,c} w_{t,c}) · W_s[i,c] W_t[i,c], and the two cells are distinct.
- **X_1, F and Z.**
  - X_1 has 16 cells and F has 33 (4+5+5+5+5+5+4). The column sets of F at L118 are correct.
  - Z has 17 cells (3+3+3+3+5), and the level rule is correct.
- **B1.**
  - nnz(X_s) ≤ 49 − 16 − 21 = 12, and the total excess is at most 5.
  - With excesses 0, 2, 4, 5 for P, D1, D2, T, the five multisets listed are exhaustive.
- **B2.**
  - Row 7 of F and columns 2 and 3 of F each have exactly 4 cells. Four nonempty disjoint lines inside 4 cells must be singletons, so τ, ρ and ρ′ are bijections, and A2 isolates each entry.
  - τ_s ≠ s+2 because column s+2 of X_s is {1}. ρ_s ≠ ρ′_s because row ρ_s of X_s is {2}.
  - The four entries sit in 4 distinct rows and 4 distinct columns, so there are at least 4 singleton components. This rules out D2.
- **B3.**
  - The rows and columns outside R_s and C_s are exactly the singleton lines, so A1 makes W_s[R_s,C_s] unitary.
  - F ∩ (R_s × C_s) ⊆ Z, and n_s ∈ {3, 5, 8}.
- **B4.** I re-derived all nine (E, D) combinations for both level choices.
  - (a) Two orthonormal rows would lie inside span{e_1}, which is impossible.
  - (b) All 9 cells are allowed.
  - (c) The E-rows are confined to {1, z}, so they form a 2×2 unitary and row 6 = {w}.
  - (d) Row a has allowed set {1} only.
  - (e) There are 7 allowed cells, with (a_L, d_H) and (a_H, d_L) forbidden. Re-enumerating independently gives the same 3 permutations and 2 "2×2 plus isolated" sets.
- **B5 and B6.**
  - Each row in 2..5 lies in exactly two E_s, and each column in 4..7 lies in exactly two D_s.
  - Counting 4 = 2·#pure + #mixed for each level gives the balance, and Σ n_s ≤ 17. B6 follows.
- **L158 ("Y_s is any …").** Erratum v2 says to read this as a necessary list with no occurrence claim. No further fix is needed.

## C: exact characterization of the partial datum

Checked:
- **Datum items 1–5 (L184–188).** These are exactly the direct axis equations:
  - unit vectors;
  - row 0 an orthonormal basis, via H2;
  - column 0 an orthonormal basis;
  - the cross-square pair relations;
  - H3 and H4.

  Reading L190 as erratum v1.2 directs is both required and sufficient.
- **Necessity.** B0–B5 use only items 1–5:
  - B0(i) uses items 1–2.
  - B0(ii) uses items 1 and 3.
  - The template counts use items 4–5.
- **Sufficiency.**
  - The row partition {1}, {7}, {ρ_s}, {ρ′_s}, R_s and the column partition {s+2}, {τ_s}, {2}, {3}, C_s are correct, so the direct sum is unitary.
  - Disjointness holds across every combination of entry types:
    - X_1 = F′.
    - Each isolated entry is in F but outside Z, because it sits in row 1 or 7 or in column 2 or 3.
    - Isolated entries of different squares are kept apart by H3 and the bijections.
    - The residuals are disjoint by item 3.
  - Phases play no role. Every cross-square relation is a unit-modulus factor times W_s[i,c] W_t[i,c]. Pairs within row 0 or within column 0 vanish factor by factor.
  - A full residual would need 9 + 3 + 3 + 3 = 18 > 17 cells of Z.
  - Items 1–3 imply Σ n_s ≤ 17. That reproduces exactly the four multisets of B2.

**C-1 MINOR, L198.**
- **Issue.** "B4 lists exactly which shapes satisfy item 2" is literally false in case (b).
  - Item 2 alone also admits the full 9-cell residual.
  - B4(b)'s "≤ 8" comes from B3 and B1, which are necessity-side facts and are not premises in the sufficiency direction.
  - The packing sentence on the same line excludes the full residual using items 2–3, so the theorem stands.
- **Fix.** "B4 lists exactly the item-2 shapes with n_s ≤ 8; the only other item-2 shape (full 3×3, possible only in case (b)) is excluded by items 2–3, since 9 + 3·3 = 18 > 17 = |Z|."

**C-2 MINOR, L202 and L264 (section title at L180).**
- **Issue.** "Exact column-0 residual" and "exact characterization of … S" never say what S is exact for.
  - S is exact only for row-0/column-0 data.
  - For configurations satisfying H1–H4, membership in S is only necessary, and "S is nonempty" says nothing about configurations.
  - L11 and L192 are scoped correctly. Erratum v1.2 does not explicitly reach L202 or L264, and these are the only places where a hidden quantifier over full configurations could be read in.
- **Fix.** Append to L202 and L264: "…of row-0/column-0 data; for configurations satisfying H1–H4, membership in S is necessary only."

The rest of the hidden-quantifier sweep is clean:
- B (L10, L128, L178) is universal over configurations and proved from datum-level facts.
- C and D quantify over data only.
- L240 disclaims any extension.
- Nowhere is there an existence claim about configurations.

## D: counterexample for the direct-axis relaxation

Checked:
- **Q_1.**
  - The column is exactly M (rows 6, 1, 7 on coordinates 1, 2, 3) ⊕ H ⊕ H.
  - Each M row has norm 1/2 + 1/4 + 1/4 = 1, and the three M-part products are 0.
  - The supports equal H3/H4, with the weight-3 witness at (1,0).
- **π tables.**
  - Each π_s is a bijection, and π_s(1) = s+2.
  - In all seven rows, the four values are distinct and avoid the corresponding row of X_1. I re-read each entry from the table.
- **All 105 axis-cell pairs, for each of the 10 square pairs.**
  - The 28 row-0 pairs and the 28 column-0 pairs vanish factor by factor.
  - The 49 pairs of the form (0,c), (i,0) reduce to the disjointness just checked.
- **ROWLEX keys** are 3, 3, 12, 12, 48, 112, which are nondecreasing.
- **Theorem B parameters, recomputed.**
  - τ = (4→5, 5→4, 6→7, 7→6), ρ = (2,3,4,5), ρ′ = (3,2,5,4).
  - E and D match the note.
  - Y_2, …, Y_5 lie in Z, are pairwise disjoint, and all fall in case (b).
- **Erratum v1.2.** It is correct and needed.
  - The original wording at L12 and L238 would cover axis-only necessary conditions derived through interior completability, and a partial datum cannot refute those.
  - The narrowed claim is exactly what a model of items 1–5 supports: no contradiction can be derived from those equations alone.
  - The erratum covers L12, L190, L238 and L270.

**D-1 MINOR, L238.**
- **Issue.** "The column-0 content of M_2, M_3, M_4 and M_5 holds simultaneously."
  - M_s is the pair candidate's set of 126 at-most-one binaries. It is neither defined nor supplied in this packet, so the claim cannot be checked here.
  - It is also the note's only clause-evaluation statement, which conflicts with L5 ("makes no Boolean-model statement").
  - What is verified is that all four X_s are permutation supports.
- **Fix.** Replace the phrase with "all four X_s are permutation supports". If the link to M_s is wanted, tag it "per the imported pair candidate, not re-verified here".

## Outside A–D

**G-1 MINOR, L270.**
- **Issue.** "By the W8 disjointness" is undefined in this note and not proved in it. The sentence does not support any theorem.
  - The remark is correct in substance.
  - Under H2, the B0(ii) computation applied to cells (0,c) and (i,j) with i ≥ 1 gives supp Q_s(i,j) ∩ supp Q_t(i,j) = ∅.
- **Fix.** State that one-line fact in place of "W8", or mark the sentence as an unproved forward remark.

## Import and trust limits

1. **The only load-bearing external input is the QLS/MOQLS definitions.**
   - H1 (L18) matches the supplied original excerpt:
     - each row and column is an orthonormal basis of Cⁿ;
     - two squares are orthogonal when {ψ_ij⊗φ_ij} is an orthonormal basis of Cⁿ⊗Cⁿ;
     - MOQLS means pairwise orthogonal.
   - The isotopy and classicality definitions are not used by A–D.
   - I cannot verify the attribution, the file hash, or erratum v1.3's range relabelling without tools. The definitional sentences are identical in both supplied copies, so the mathematics is unaffected.
2. **H2–H4 are hypotheses.**
   - The U/T16 link from arbitrary genuine non-classical five-sets to H2–H4 is conditional, unproved, and was not reviewed.
   - B–D hold conditionally on H1–H4. A is unconditional linear algebra.
   - Non-classicality is not among H1–H4.
3. **Template.**
   - H4 matches the supplied GBBINDING `supports_row2to7` entry.
   - It also matches the template-cover row B3 (67;67;45;45) completed by the P1 rows (23;123).
   - Whether these snapshots are faithful to their pinned originals, and P1-B3's role in the global cover, are metadata I did not verify.
4. **ROWLEX** is undefined in the packet. I checked L234 only under the key convention stated there. ROWLEX is not a hypothesis of any theorem.
5. **Not used as premises:** M_s, GB_B3, H_23/H_24, NF r2, and the pair verdict and erratum. Nothing here bears on Boolean models, UNSAT, GB 15/18, the three UNKNOWNs, or n = 8.
6. **Unverified provenance:**
   - I did not verify any SHA256 value, timestamp, path, scope-freeze compliance, or the no-tools provenance.
   - I have not seen the Codex review cited in erratum v2. This assessment is independent of it.

This review asserts no exclusion and no extendability of the D datum. It makes no claim that a T residual occurs or is excluded. It makes no novelty, Lean, or human-approval claim.
