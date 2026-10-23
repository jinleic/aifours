VERDICT: ACCEPT-WITH-FIXES

I re-derived every load-bearing step by hand. No step depends on the unaccepted sparsity candidate, on fixed phases, or on a Boolean model. All fixes below are wording or scope precision only.

## FATAL
None.

## MAJOR
None.

## MINOR (candidate line → exact repair)

1. **l.19 "ROWLEX follows…"**
   - ROWLEX is undefined in the packet, its derivation is absent, and nothing uses it.
   - Repair: delete it, or mark it "parent metadata; not used or verified."

2. **l.13–19 and l.256 (hypothesis provenance).**
   - The inlined [J] entry is only an unlabeled `supports_row2to7` list.
   - It does not say these are the *exact* supports of q_1^2,…,q_1^7, and it contains neither SB2 nor row 0.
   - Repair (ledger): "All theorems are conditional on §1 l.9–17 exactly as written; the binding to [J]/U/T16 is parent metadata."
   - Standard row 0 is WLOG by [PRIM] isotopy (iii). Exactness of supports and SB2 are not WLOG.

3. **l.43 "both columns have degree 2".**
   - This silently uses the fact that a degree‑1 column is a singleton column, which would isolate r.
   - Repair: add that clause. The argument is otherwise complete.

4. **l.49 and l.206 (unseen references).**
   - "Old candidate's T possibility", "navigation observation" and the datum's provenance refer to text not in the packet. None of it is load-bearing.
   - Repair: label these "comparison remark, unverified here."

5. **l.64–68 "allowed".**
   - The term is undefined.
   - Repair: "allowed := S_s ⊆ [8]\{j}, T_s ⊆ [8]\{i}; nonemptiness follows from H_s ≠ 0."

6. **l.140 "retained exactly by (3)–(5)".**
   - (3)–(5) operate at the allowed-set level. A positive dimension does not give a vector with exactly those supports.
   - Example: S_A={2,3}, T_A={6,7} gives d_A=1, but H_A=span(q_1^6), whose own support is {6}.
   - Repair: "retained at allowed-set level by Theorem 1 with (3)–(5); no actual-support classification of one-block or Z-mixed vectors is claimed. The budget leaves either Z plus one block b with (p_b,q_b) ∈ {(1,2),(2,1),(2,2)}, or one block alone."

7. **l.162–170, (8) and the warning.**
   - Over all PSD B, (8) is equivalent, by convex separation, to the mixed relaxation R_{s,i} = Σ_j ρ_j with ρ_j density operators supported on H_{s,j}.
     - Separation works because both sides shift by 7c under B → B+cI, since tr R_{s,i} = 7.
   - That relaxation implies (7): Σ_{j∈J} ρ_j ⪯ R has trace |J|, norm ≤ 1 and range inside Σ_J H_{s,j}.
   - The l.170 example passes (7) but **fails** (8): B = |e_2⟩⟨e_2| gives 1 > 0 + ½.
   - Repair: "The example shows only that (7) is insufficient; insufficiency of (8) for (6) is neither shown nor needed." The candidate makes no sufficiency claim anywhere; I confirmed this.

8. **l.176–186, quantifiers in (9).**
   - d_{s,b,j} and N_s(L) depend on the chosen sets.
   - Repair: "with S_{s,j}, T_{s,j} the actual supports, or any allowed family realizing (6)."
   - Add: (9) also follows from (7) with J = [7]\N_s(L), because those H_{s,j} lie in ⊕_{b∉L} E_{C_b} ∩ (q_s^i)^⊥.
   - The hierarchy is therefore (6) ⇒ (8) ⇒ (7) ⇒ (9).
   - The l.202 illustration already fails (7) at J={1,2}. "Nonvacuous" should be read only as "not implied by seven independent cell checks."

## Item-by-item audit

**1. §2 (axis lemma).**
- X_1 has row degrees 3,2,2,2,2,2,3 and column degrees 2,3,3,2,2,2,2, giving 16 ones.
- Disjointness follows from the (0,c)/(r,0) tensor equation, and the bound deg ≤ 7 − deg_{X1} − 3 follows from it.
- A singleton row or column is isolated by orthogonality.
- Components close at 2×2 because two orthogonal vectors cannot share exactly one support index.
- The isolated rows 1, 7, ρ_s, ρ′_s are distinct: ρ_s = ρ′_s would place a degree‑2 row in a singleton column.
- Hence at most one block per s, and 16 + 28 + 2Σt ≤ 49 gives Σt ≤ 2.
- Only genuine unitarity and the derived disjointness are used. ✓

**2. Theorem 1.**
- Common-frame family:
  - tensor equations with (0,c), c ∈ [8], give disjoint S_s;
  - the own-column condition with (0,j) gives j ∉ S_s.
- Own-frame family:
  - tensor equations with (r,0), r ∈ [8], give disjoint T_s;
  - the own-row condition with (i,0) gives i ∉ T_s.
- The cell (0,0) belongs to both families, consistently, since q_s^0 ∝ e_0.
- Each tensor equation is a product of two scalars, so squares are coupled only through zero patterns.
- Both nullity forms of (1) hold, as does the operator-norm equivalence (attained by compactness).
- (2) holds as a necessary condition only, and |S_s|,|T_s| ≤ 3. ✓

**3. §4 (ranks).**
- A dense 2×2 block has leakage rank min(2−p, q).
- For the 3×3 block, all (h,q) ∈ {0,…,3}² are covered:
  - h or q ∈ {0,3} is trivial by orthonormality;
  - a 1×1 entry vanishes only at (1,6);
  - a 1×2 or 2×1 submatrix never vanishes;
  - adj(M) = det(M)·M* makes each 2×2 minor a unit times the conjugate of the complementary entry, so the only singular 2×2 is rows {2,3} × cols {1,7}, of rank 1.
- The exceptional cases ({2,3},{6}) and ({1},{1,7}) each add +1.
- The second form of (1) yields the same two cases; they are dual.
- No phase is fixed anywhere.
- Corollary 2 is correctly restricted to one cell and a fixed zero pattern; row‑0 phases are also irrelevant. ✓

**4. §5 (Q1 channels).**
- Costs: Z costs 2; A, B, C each cost ≥ 3, since no 1×1 intersection inside them is nonzero.
- |S|+|T| ≤ 6, so at most two blocks.
- With two nontrivial blocks:
  - each costs exactly 3;
  - Σp ≤ 3 and Σq ≤ 3 force one (1,2) and one (2,1);
  - in A, (2,1) can only be q_1^6, and (1,2) can only be e_1, with own support {1,7}.
- The six listed families are exhaustive.
- Z-mixed and one-block cases are retained, not dropped (see MINOR 6). ✓

**5. Theorem 3 and (7)–(9).**
- Every cell-pair case is covered:
  - interior pairs in the same row (orthogonality implies the tensor condition);
  - (i,j)–(0,j);
  - (i,j)–(i,0);
  - (i,j)–(0,c), (r,0) and (0,0).
- The trace identity forces orthonormality, and H_{s,j} ⊆ (q_s^i)^⊥ because i ∉ T.
- The criterion is exact for row 0 ∪ column 0 ∪ row i only.
- Phase boundary:
  - (9), (10) and (11) depend only on zero patterns;
  - (7) and (8) depend on the H_{s,j}, which are amplitude-dependent only inside multi-dimensional blocks (square‑1 A/B/C and D1 blocks);
  - row‑0 phases never enter. ✓

**6. Row 1.**
- Block demands: Z 1, A 3−1 = 2, B 2, C 2, summing to 7.
- (10):
  - an e_1-type A component carries own index 1, since A_1(1,1) ≠ 0, so y(1) = 0 excludes it;
  - three-block mixing is impossible;
  - hence ⟨q_1^7, a⟩ ≠ 0 forces the blocks into {Z, A}.
- (11) follows from A_1(1,6) = 0 and A_1(1,7) ≠ 0.
- (12) is Parseval, using q_1^7 ⊥ q_1^1.
- (10) and (11) are per-cell statements; (12) needs the full row.
- All three are valid for every admissible complex axis datum. ✓

**7. §8 (D-axis, one cell).**
- Norms and orthogonality check out: ⟨q_1^1,q_1^7⟩ = ½−¼−¼ = 0, and q_1^6 is orthogonal to both via (½−½)/√2.
- Each π_s is a permutation, and π_s(1) = s+2.
- The per-r image sets {4567}, {1235}, {1234}, {1237}, {1236}, {4567}, {4567} are 4-sets avoiding 123, 67, 67, 45, 45, 23, 123 respectively.
- Cell (1,4):
  - π_2(5)=6, π_3(4)=7, q_4^0 = e_0, π_5(2)=5;
  - S column {1,2,3},{6},{7},{0},{5} is disjoint and omits 4;
  - T column {7},{5},{4},{0},{2} is disjoint and omits 1;
  - directly, q_s^1 = e_4,e_5,e_6,e_7 are orthogonal to e_6,e_7,e_0,e_5, and q_1^1 ⊥ q_1^7.
- This is one cell only. It shows merely that the direct equations at (1,4) cannot by themselves exclude D-axis. It is not a row, grid, extension/nonextension claim, or SAT/UNSAT(H23/H24) statement. ✓

**8. Ledger.**
- Consistent with the above once MINOR 2 and 4 are applied.

## Complete at candidate partial scope (conditional on §1 hypotheses)

- **P/D1 axis lemma:** each s ≥ 2 has at most one dense 2×2 block, at most two exist in total, and at least two squares have permutation supports.
- **Theorem 1:** with (1), (2) and cardinality ≤ 3.
- **Phase-free dimensions (3)–(5)**, and Corollary 2 for one cell with a fixed zero pattern.
- **Q1 channels:** every interior vector uses at most two Q1 blocks, and the six mixed families are exhaustive.
- **Theorem 3:** for row 0 ∪ column 0 ∪ one row.
- **Necessary capacities** (6) ⇒ (8) ⇒ (7) ⇒ (9).
- **Row 1:** the demands and (10)–(12) hold for all admissible axes.
- **D-axis:** satisfies the direct axis equations and admits the single-cell extension at (1,4).

## Still open (not addressed by these theorems)

- **Missing bridge, stated exactly.**
  - Needed: for every admissible axis datum, there is no genuine completion. The datum ranges over:
    - all row-0 phases w_{s,c};
    - every unitary A_1 with the template zero pattern;
    - every A_s (s ≥ 2) with P/D1 patterns and Σt_s ≤ 2.
  - Sufficient via this route: some row i such that every per-j allocation (S_{s,j}, T_{s,j}) satisfying Theorem 1 leaves some square s with no orthonormal selection a_{s,j} ∈ H_{s,j}.
  - Given an allocation, (6) splits into five independent per-square problems, so this is exactly a quantified statement over allocations and over the amplitudes of square 1 and the D1 blocks.
  - Reviewer remark, not in the candidate: for a P square, H_{s,j} = E_{S∩π_s(T)}, and (6) for that square is equivalent to Hall's condition on these sets, hence amplitude-free.
  - This is not proved for any i.
- **Constraints absent from (6)–(12)** (decisive if every row passes (6)):
  - column ONBs, Σ_i |Q_s(i,j)⟩⟨Q_s(i,j)| = I − |e_j⟩⟨e_j|, with each cell shared by its row and its column;
  - interior–interior tensor orthogonality, ⟨Q_s(i,j),Q_s(i′,j′)⟩·⟨Q_t(i,j),Q_t(i′,j′)⟩ = 0 for i ≠ i′, j ≠ j′. These are amplitude conditions that cannot be written as support disjointness in either frame.
- **No construction:** there is no full-row solution of (6), no grid, and no extension or nonextension of D-axis beyond one cell.
- **Imports and downstream claims:**
  - The U/T16 reduction to the standard-row‑0/SB2/B3 case, GB15/18 and the P1‑B3 CNF identity remain parent metadata.
  - Even a genuine B3 exclusion would not imply UNSAT(H23/H24), because Boolean supports need not be unitary.
  - A10, A11 and n = 8 are unchanged.
