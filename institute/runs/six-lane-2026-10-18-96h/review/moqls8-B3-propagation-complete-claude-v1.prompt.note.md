# Independent review: MOQLS8 B3 block-propagation CANDIDATE v1, governed by parent errata v1 and v2

This review used no tools, code, enumeration, execution or delegation. Every step below was re-derived by hand from H1–H4.

Conventions: indices run 0..7, ⟨·,·⟩ is antilinear in the first slot, q_s^r := Q_s(r,0), and "LFn" means candidate line n.

## Verdict

**FATAL 0 · MAJOR 0 · MINOR 7.**
- Three minors are already closed by the governing errata (LF109, LF151, LF153).
- Four are open and cosmetic (LF122, LF115–122, LF48, LF25/LF30–31).

Every claimed result re-derives under exact H1–H4: F1, F2, AX, S, Lemma R, Lemma Z, P1–P6, P^C and A. Under erratum v2, O_next proves only that a shared row exists in {1,6,7}. No contradiction or no-go is inferred anywhere. **Do not promote** this to a full B3 exclusion, to any n=8 result, or to any GB/UNSAT change.

## 1. Basic data used throughout

Exact H4 makes q_1^2 and q_1^3 an ONB of V_B, and both have full support {6,7}. So the matrix (⟨e_d,q_1^r⟩) with d ∈ {6,7} and r ∈ {2,3} is a 2×2 unitary, with:
- |⟨e_6,q_1^2⟩|² = |⟨e_7,q_1^3⟩|² = t;
- |⟨e_6,q_1^3⟩|² = |⟨e_7,q_1^2⟩|² = 1−t;
- t ∈ (0,1).

This matches LF41–42. The same holds for V_C with t_C.

## 2. Claim-by-claim

**F1 ✓**
- Q_s(i,j) shares column j with w·e_j, so ⟨e_j,Q_s(i,j)⟩ = 0.
- It shares row i with q_s^i, so ⟨q_s^i,Q_s(i,j)⟩ = 0.

**F2 ✓**
- Take z = (i,j) with i, j ≥ 1. The cell (0,d) with d ≠ j shares no line with z, and neither does (r,0) with r ≠ i.
- By H2, |G_s((0,d),z)| = |⟨e_d,Q_s(z)⟩|. Also G_s((r,0),z) = ⟨q_s^r,Q_s(z)⟩.
- G_s·G_t = 0 for every pair s ≠ t, so at most one square is nonzero at each slot.

**AX ✓**
- Apply H1 to (0,d) and (r,0) with d, r ≥ 1, and use q_s^r ⊥ w·e_0.
- AX is correct, but no step of P, P^C or A uses it (MINOR-4).

**S ✓**
- Parseval in row i: the c=0 term is |⟨e_d,q_s^i⟩|² (resp. δ_ri).
- Parseval in column c ≥ 1: the i=0 term is δ_dc (resp. |⟨q_s^r,e_c⟩|²).

**Lemma R ✓**
- Compress the ONB of row i ∈ {2,3} by P_B. This gives Σ_{j=1..7} P_B|Q⟩⟨Q|P_B = P_B − |q_1^i⟩⟨q_1^i| = |q_1^{5−i}⟩⟨q_1^{5−i}|.
- For any PSD summand A of a projector P, ⟨v,Av⟩ ≤ ⟨v,Pv⟩ = 0 on ker P, so ran A ⊆ ran P. The rank-≤1 hypothesis is not even needed.
- Taking the trace gives Σ_j |λ_{i,j}|² = 1. Columns 6 and 7 work the same way, with |e_c⟩⟨e_c| in place of |q_1^i⟩⟨q_1^i|.
- Corners: Q_1(i,c) ⊥ q_1^i and Q_1(i,c) ⊥ e_c. These two vectors span V_B because, by exact support, q_1^i is not parallel to e_c.
- Hence ∅ ≠ J_i ⊆ {1..5} and ∅ ≠ I_c ⊆ R'.

**Lemma Z ✓**
- The sum of row sums over K equals the sum of positive entries inside K, which equals the sum of column sums over K, an integer.
- An all-zero line (from F1) is an isolated vertex, which is harmless.

**P1 ✓**
- Column a ≤ 5 has coordinate-d mass 1 − δ_da = 1.
- ⟨e_d,Q_1(2,a)⟩ = λ_{2,a}⟨e_d,q_1^3⟩ and ⟨e_d,Q_1(3,a)⟩ = λ_{3,a}⟨e_d,q_1^2⟩.
- For d=7, rows 2 and 3 together carry |λ_{2,a}|²·t + |λ_{3,a}|²·(1−t). For d=6, swap t and 1−t.
- The remainder lies in R'. Since all terms are nonnegative, R_d(a) ≠ ∅ ⇔ δ_d(a) > 0.

**P2 ✓**
- δ_7(a) = t(1−|λ_{2,a}|²) + (1−t)(1−|λ_{3,a}|²), and both weights are positive.
- So δ_7(a) = 0 ⇔ |λ_{2,a}| = |λ_{3,a}| = 1 ⇔ J_2 = J_3 = {a}, using the unit ℓ² rows of λ.
- In that case ‖P_B Q_1(2,a)‖ = 1 = ‖Q_1(2,a)‖, so Q_1(2,a) = λ_{2,a}·q_1^3.
- At most one column a can have zero deficit. δ_6 behaves identically.

**P3 ✓**
- Σ_a δ_7(a) = 5 − t − (1−t) = 4, using λ_{i,6} = λ_{i,7} = 0.
- Independent row-side check: rows 2 and 3 have interior coordinate-7 mass t and 1−t. All of it lies in columns 1..5, since column 7 is excluded by F1 and column 6 is a corner. So R' supplies 5 − 1 = 4.

**P4 ✓**
- Fix d ∈ {6,7} and a ≤ 5, so d ≠ a. Let S_s := {i : ⟨e_d,Q_s(i,a)⟩ ≠ 0}.
- For s ≥ 2, S_s ≠ ∅ by column-a Parseval and H2 for square s.
- By F2, S_1 through S_5 are pairwise disjoint subsets of {1..7}.
- S_1 = R_d(a) ⊔ {2 : a∈J_2} ⊔ {3 : a∈J_3} exactly, since ⟨e_d,q_1^3⟩ ≠ 0 and ⟨e_d,q_1^2⟩ ≠ 0.
- Therefore |S_1| ≤ 7 − 4 = 3.
- There is no double counting: R_d(a) ⊆ R' excludes rows 2 and 3, and each other square is charged one row.
- The only non-degeneracy used is t ∈ (0,1).
- The case split follows from P1 and P2. The blocking statement follows from F2.

**P5 ✓ (frames correct)**
- For i ∈ R' and r ∈ {2,3}, the own-index mass of row i is 1.
- N^3_1(i,6) = |κ_{i,6}|²·t and N^3_1(i,7) = |κ_{i,7}|²·(1−t). For index 2 the weights are 1−t and t. This reproduces ε_r exactly as in LF76–77.
- Rigidity is P2 with κ in place of λ.
- The total 4 follows from κ-normalisation. It agrees with the candidate's column-count route: row 2 supplies Σ|λ_{2,c}|² = 1, and row 3 supplies 0 by F1.
- Each square s ≥ 2 must place its own-index-r mass of row i against its own q_s^r. The own-index clause of F2 is per square, since G_s((r,0),z) = ⟨q_s^r,Q_s(z)⟩. So the blocking compares exactly the right quantities.
- There is no confusion between the common frame S and the own frames T_s anywhere in P1–P6.

**P6 ✓**
- Restrict M^7_1 to columns 1..6; column 7 is zero by F1.
- Column sums are 1. Row sums are 1 on R', t on row 2 and 1−t on row 3.
- So Lemma Z puts rows 2 and 3 in one component.
- The neighbourhood of row 2 is exactly J_2, because the column-6 corner is 0. The neighbourhood of row 3 is J_3.
- If J_2 ∩ J_3 = ∅, a shortest path 2–a_1–r_1–a_2–… has r_1 ∈ R' and a_2 ≠ a_1.
- a_2 may be column 6 (via r_1 ∈ I_6). The candidate's wording "two columns, one in J_2" correctly claims no more than this.
- Transposed case, N^3_1 on rows ≠ 3: column sums are 1 on {1..5}, t at column 6 and 1−t at column 7. The neighbourhood of column 6 is I_6, because the row-2 corner is 0, so c_1 ∈ {1..5} as claimed.
- M^6_1 and N^2_1 behave identically.

**P^C ✓**
The transfer is valid. In fact there is an exact symmetry σ of H1–H4:
- rows (2 4)(3 5);
- columns and coordinates both (4 6)(5 7);
- squares (2 4)(3 5).

Check of each hypothesis:
- H1 is isotopy-invariant.
- H2 survives because the column and coordinate permutations coincide.
- H3 survives because the axes e_4..e_7 return to {s+2} after relabelling the squares, and {1,2,3} is fixed.
- H4 survives because {6,7} ↔ {4,5}, while {2,3} and {1,2,3} are fixed.

σ sends:
- rows 2,3 to rows 4,5;
- block coordinates/columns 6,7 to 4,5;
- R' to R'_C, and the column range {1..5} to {1,2,3,6,7};
- t to |⟨e_5,q_1^5⟩|² = t_C.

The resulting C formulas are:
- P_C Q_1(i,j) = λ^C·q_1^{9−i} and P_C Q_1(i,c) = κ^C·e_{9−c};
- δ_5(a) = 1 − |λ^C_{4,a}|²·t_C − |λ^C_{5,a}|²·(1−t_C), and δ_4 is the same with t_C swapped;
- the totals are again 4.

**A ✓**
- The fractional rows of M^d_1 are exactly those with d ∈ supp q_1^r. Their values lie in (0,1) because every relevant support has size at least 2.
- The fractional rows are {1,7} for d=1 and {1,6,7} for d ∈ {2,3}. Their total is k−1, which is 1 or 2.
- Three values in (0,1) summing to 2 have no integral proper subsum: a pair summing to 1 would force the third value to be 1.
- In the transposed case the fractional columns are supp q_1^r: {1,2,3} with total 2, or {2,3} with total 1.
- A is *not* a symmetry image of P. P_A-compression leaves a rank-2 remainder, so there is no Lemma R analogue. The candidate correctly claims only component statements for A.

## 3. O_next and the errata

- For r ∈ R', define m_7(r) := Σ_{a≤5} M^7_1(r,a). Then m_7(r) = 1 − |κ_{r,6}|², which lies in [0,1].
- Σ_{r∈R'} m_7(r) = Σ_a δ_7(a) = 4.
- m_7(r) = 0 ⇔ I_6 = {r}, so at most one row of R' is zero. The C twin works the same way, with m^C_5(r) = 1 − |κ^C_{r,4}|².
- Each block is therefore positive on at least two rows of R' ∩ R'_C = {1,6,7}. Two 2-subsets of a 3-set must meet, so a shared row exists. That is exactly erratum v2 LF7, and nothing more follows. In particular, no proved statement excludes I_6 = {r} for any particular r.
- On the whole-vector point: for r ∈ {1,6,7}, the families {P_B Q_1(r,c)} and {P_C Q_1(r,c)} are Parseval *frames* of V_B and V_C, not orthogonal systems. Row orthogonality couples the e_0, V_A, V_B and V_C components jointly.
- So erratum v2's "WHOLE cell vectors" is the right formulation.
- Both errata are mathematically correct and introduce no new defects.

## 4. Defects, with exact lines and minimal repairs

1. **MINOR, LF109 (closed by erratum v1).**
   - Issue: "1−t, t for rows 2 and 3" should read "t, 1−t".
   - This is wording only. The "since" clause on the same line has the correct values. LF110 uses only that the two masses are strictly fractional and sum to 1.
2. **MINOR, LF151 (closed by erratum v2).**
   - Issue: "A full B3 no-go needs additional coupling" can be read as a necessity or joint-feasibility claim, which is not proved.
   - Repair: the reading in erratum v2 LF5.
3. **MINOR, LF153 (closed in substance by erratum v2).**
   - Issue: "an R'-row r … must carry completion mass in both blocks, by (P3)" is false as a universal claim. Rows 4 and 5 are not in R'_C, and m_7(r) = 0 when I_6 = {r}.
   - P3 alone also lacks the per-row cap of 1.
   - Repair: v2 fixes both the quantifier and the cap. Optionally add the one-line definitions of m_7 and m^C_5 from §3.
4. **MINOR, LF122 (open, harmless).**
   - Issue: "using (AX)" cites a fact no step uses; squares 2..5 enter only through S and F2.
   - Repair: state "AX not needed".
5. **MINOR, LF115–122 (open, harmless).**
   - Issue: the substitution list omits the partner maps for the LF30–31 index expressions, so "verbatim" is overstated. The maps are q_1^{5−i} → q_1^{9−i} and e_{13−c} → e_{9−c}.
   - Repair: state σ from §2, or add the two maps.
6. **MINOR, LF48 (open, cosmetic).**
   - Repair: "Every entry" should read "every positive entry".
7. **MINOR, LF25 and LF30–31 (open, cosmetic).**
   - Issue: "[8]" here means {0,…,7}, and the Lemma R ranges j, i ∈ {1..7} are left implicit.
   - Repair: write both out.

None of these changes any statement or proof.

## 5. Adequacy notes (not counted as defects)

**Strength.** The mathematics is correct but modest.
- P1–P3 are column Parseval with Lemma R substituted. Lemma R itself re-proves [DC]-type content.
- P4 and P5 are single-line slot counts.
- The genuinely cross-line content is:
  - the P3 total;
  - P6 and A integrality;
  - the unstated identity m_7(r) = 1 − |κ_{r,6}|², which ties the λ data to the κ data.
- Whether this clears the SCOPE-FREEZE LF13/15 bar ("not only one-line", "restatement ≠ progress") is the parent's call.

**Hypotheses actually used.** The proofs use:
- H1;
- H2 for all squares;
- H3 for square 1 only;
- the exact supports in H4;
- the count of five squares, since the constant 3 is 7 − 4.

The proofs do not use:
- H3 for squares 2..5;
- AX;
- genuineness;
- interior-frame disjointness.

So the results hold for every configuration satisfying H1–H4.

**H4 indexing.** The snapshot's `supports_row2to7` matches H4 literally. Reading the coordinates 0-based is the only reading consistent with H2/H3: q_1^0 = e_0, with 3, 2 and 2 vectors in V_A, V_B and V_C. The GB file itself was not checked, and nothing here depends on it beyond H4.

## 6. Non-promotion

- No full B3 exclusion, no n = 8 statement, and no Boolean/GB/UNSAT inference follows.
- GB 15/18, the UNKNOWNs, A10/A11 and the n=8 target are unchanged.
- If the parent accepts, the scoped status would be:
  - Lemma R, Lemma Z, P, P^C and A proved as necessary conditions for all H1–H4 configurations;
  - the O_next existence clause proved, per erratum v2;
  - the whole-vector compatibility obligation still open.
