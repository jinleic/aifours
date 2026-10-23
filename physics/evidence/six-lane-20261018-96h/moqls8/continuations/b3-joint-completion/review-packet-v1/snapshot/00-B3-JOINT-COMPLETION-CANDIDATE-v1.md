# B3 joint completion: O_next made precise and proved, exact local case tables, and the explicit finite list of surviving configurations — CANDIDATE v1 (LABELLED PARTIAL)

Frozen at 2026-10-19T17:22:18-0700 under `SCOPE-FREEZE-v1.json` (SHA256 `5a97772f6bd0548561280d4971f85c0d727a34599807b45cdc0579bb7fbca536`). Status: CANDIDATE written mathematics, not reviewed or accepted. Every lemma used is re-proved here, and every finite case split is done by hand in the text. No script, assertion, enumeration, probe, solver, checker, CLI or nested agent was used for any scientific statement.

**Outcome: LABELLED PARTIAL.**
- O_next is made precise and proved for ALL genuine B3 configurations (Theorem O).
- It is combined with the re-proved B/C propagation results into exact **local case tables** (Theorems LC, LR) and a proved **cross-line compatibility law** between common-frame column cases and own-frame row cases (Theorem X).
- The output is an **explicit finite list** of surviving configuration types for each block and frame (Theorem F). Every eliminated sub-branch is retained with its proof.
- **No full B3 no-go is obtained.** No type in the list is eliminated by the results proved here.

## 1. Setting and re-proved basics

H1: Q_1,...,Q_5 are a full genuine set of pairwise-orthogonal QLS(8) ([PRIM] LF195-225). The normal-form hypotheses are:
- H2: Q_s(0,c) = w_{s,c}e_c with |w_{s,c}| = 1;
- H3: supp Q_1(1,0) = {1,2,3} and supp Q_s(1,0) = {s+2};
- H4 (exact template [J]): the supports of Q_1(i,0), i = 2..7, are {6,7}, {6,7}, {4,5}, {4,5}, {2,3}, {1,2,3}.

All axis data, amplitudes and phases are kept, and interior vectors are general. Notation:
- q_s^r := Q_s(r,0).
- Blocks: Z = {0}, A = {1,2,3}, C = {4,5}, B = {6,7}, with coordinate spans V_X and projections P_X.
- Square 1: V_B = span{q_1^2,q_1^3}, V_C = span{q_1^4,q_1^5}, V_A = span{q_1^1,q_1^6,q_1^7}. Each q_1^r lies in exactly one block. q_1^2 and q_1^3 have support exactly {6,7}; q_1^4 and q_1^5 have support exactly {4,5}.
- R' := {1,4,5,6,7} and R'_C := {1,2,3,6,7}.

Facts:
- **(F1)** For i, j >= 1: <e_j,Q_s(i,j)> = 0 and <q_s^i,Q_s(i,j)> = 0.
- **(F2)** At an interior cell z = (i,j), each coordinate d != j occurs in the support of at most one square's vector, and each own index r != i (<q_s^r,Q_s(z)> != 0) in at most one. Proof: H1 applied to z and (0,d), resp. z and (r,0).
- **(AX)** For r >= 1 the supports of q_1^r,...,q_5^r are pairwise disjoint and avoid 0. Hence q_s^2, q_s^3 ⊥ V_B and q_s^4, q_s^5 ⊥ V_C for s >= 2.
- **(S)** Parseval in a full row or column. In row i of square s, the coordinate-d mass sum_{c>=1} |<e_d,Q_s(i,c)>|^2 equals 1 − |<e_d,q_s^i>|^2, and the own-index-r mass sum_{c>=1} |<q_s^r,Q_s(i,c)>|^2 equals 1 − δ_{ri}. In column c, the coordinate-d mass sum_{i>=1} |<e_d,Q_s(i,c)>|^2 equals 1 − δ_{dc}, and the own-index-r mass equals 1 − |<q_s^r,e_c>|^2.

**Lemma R (rank-one structure).**
- For i ∈ {2,3}: P_B Q_1(i,j) = λ_{i,j} q_1^{5−i}, with sum_j |λ_{i,j}|^2 = 1 and λ_{i,6} = λ_{i,7} = 0.
- For c ∈ {6,7}: P_B Q_1(i,c) = κ_{i,c} e_{13−c}, with sum_i |κ_{i,c}|^2 = 1 and κ_{2,c} = κ_{3,c} = 0.

*Proof.* Row i resolves the identity: sum_{j=0..7} P_B|Q_1(i,j)><Q_1(i,j)|P_B = P_B. The j = 0 term is |q_1^i><q_1^i|, so the interior sum is the rank-one projector |q_1^{5−i}><q_1^{5−i}|. Positive summands of rank at most one lie in its range. Columns 6 and 7 are the same with |e_c><e_c|. At the four corners, Q_1(i,c) ⊥ q_1^i and Q_1(i,c) ⊥ e_c, and these span V_B. QED

Put J_i := {j : λ_{i,j} != 0} ⊆ {1..5} and I_c := {i : κ_{i,c} != 0} ⊆ R'. Let t := |<e_7,q_1^3>|^2. Then t ∈ (0,1), |<e_6,q_1^3>|^2 = |<e_7,q_1^2>|^2 = 1−t and |<e_6,q_1^2>|^2 = t.

**Theorem K (re-proved).** 1 <= |J_2|, |J_3|, |I_6|, |I_7| <= 2.

*Proof.*
- **Row bound.** In row 2, square s >= 2 has e_7-mass 1 by (S) and (AX). Square 1 carries coordinate 7 at (2,j) iff j ∈ J_2, because <e_7,q_1^3> != 0. Coordinate 7 is absent at column 7 by (F1). By (F2), the four squares need four disjoint nonempty column sets in {1..6} \ J_2, so |J_2| <= 2.
- **Column bound.** In column 6, square s >= 2 has own-index-3 mass 1 − |<q_s^3,e_6>|^2 = 1. Square 1 carries own index 3 at (i,6) iff i ∈ I_6, because <q_1^3,e_7> != 0. Own index 3 is absent in row 3 by (F1). So 4 <= 7 − 1 − |I_6|.
- **Lower bound.** Nonemptiness follows from the unit sums.
QED

## 2. Deficit operators and capacities (re-proved)

**Lemma D (column deficit operator).** For a ∈ {1..5}, write x_a := |λ_{2,a}|^2, y_a := |λ_{3,a}|^2 and b_{r,a} := P_B Q_1(r,a). Then

    sum_{r ∈ R'} b_{r,a} b_{r,a}^* = D(a) := (1−x_a)|q_1^3><q_1^3| + (1−y_a)|q_1^2><q_1^2|.

*Proof.* Column a resolves the identity. The row-0 term vanishes under P_B because e_a ⊥ V_B. Rows 2 and 3 contribute x_a|q_1^3><q_1^3| and y_a|q_1^2><q_1^2|. Finally P_B = |q_1^2><q_1^2| + |q_1^3><q_1^3|. QED

**Lemma E (row deficit operator).** For i ∈ R', write x'_i := |κ_{i,6}|^2 and y'_i := |κ_{i,7}|^2. Then

    sum_{c=1..5} b_{i,c} b_{i,c}^* = E(i) := (1−y'_i)|e_6><e_6| + (1−x'_i)|e_7><e_7|.

*Proof.* Row i resolves the identity, and q_1^i ⊥ V_B for i ∈ R'. Columns 6 and 7 contribute x'_i|e_7><e_7| and y'_i|e_6><e_6|. QED

**Lemma Sc (scalar lemma).** Suppose a Hermitian operator on V_B is diagonal both in {e_6,e_7} and in {q_1^2,q_1^3}. Then it is a multiple of the identity.

*Proof.* If D = μ_6|e_6><e_6| + μ_7|e_7><e_7| and D q_1^2 = ν q_1^2, comparing coordinates gives μ_6 q^2_6 = ν q^2_6 and μ_7 q^2_7 = ν q^2_7, with both coordinates nonzero. QED

**Definitions.**
- R_d(a) := {r ∈ R' : <e_d,b_{r,a}> != 0} for d ∈ {6,7}.
- C_k(i) := {c ∈ {1..5} : <q_1^k,b_{i,c}> != 0} for k ∈ {2,3}. Note <q_1^k,Q_1(i,c)> = <q_1^k,b_{i,c}>.
- A nonzero B-part is **pure-q** if it is proportional to q_1^2 or q_1^3, and **pure-e** if proportional to e_6 or e_7.
- A pure-q part has both coordinates 6, 7 and exactly one own index. A pure-e part has exactly one coordinate and both own indices 2, 3. Any other nonzero B-part has both coordinates and both own indices.

**Lemma P4 (cross-square capacity).**
- (common) |R_d(a)| <= 3 − [a ∈ J_2] − [a ∈ J_3] for a ∈ {1..5} and d ∈ {6,7}.
- (own) |C_k(i)| <= 3 − [i ∈ I_6] − [i ∈ I_7] for i ∈ R' and k ∈ {2,3}.

*Proof.*
- **Common.** Each square s >= 2 has coordinate-d mass 1 in column a by (S), with a != d. So it needs a nonempty set of rows. These sets are pairwise disjoint by (F2). They also avoid the rows where square 1 carries d in column a: row 2 iff a ∈ J_2, row 3 iff a ∈ J_3, and R_d(a). So 4 + |R_d(a)| + [a ∈ J_2] + [a ∈ J_3] <= 7.
- **Own.** Each square s >= 2 has own-index-k mass 1 in row i (k != i). Square 1 carries index k at (i,6) iff i ∈ I_6, at (i,7) iff i ∈ I_7, and on C_k(i). The same count applies.
QED

**Lemma P1 (exact completion).** Put δ_d(a) := <e_d,D(a)e_d>, so that δ_7(a) = (1−x_a)t + (1−y_a)(1−t) and δ_6(a) = (1−x_a)(1−t) + (1−y_a)t. Then R_d(a) != ∅ iff δ_d(a) > 0. Moreover sum_{a=1..5} δ_d(a) = 4, since sum_a x_a = sum_a y_a = 1. QED

## 3. Theorem LC (exact local table for a B-column a ∈ {1..5}; common frame)

Write x = x_a and y = y_a. The value x = 1 means J_2 = {a}. A value x ∈ (0,1) means a ∈ J_2 and |J_2| = 2 (Theorem K). The value x = 0 means a ∉ J_2. The same holds for y and J_3. The nine cases are exhaustive.

| case | (x,y) | forced structure of the R'-parts in column a | eliminated sub-branches (retained) |
|---|---|---|---|
| L1 | (1,1) | D = 0: no R' row has B-content; Q_1(2,a), Q_1(3,a) are unit multiples of q_1^3, q_1^2 | none |
| L2 | (1, mid) | exactly one row r: b_{r,a} = ω(1−y)^{1/2} q_1^2 (pure-q) | R_6 != R_7; two or more rows |
| L3 | (mid, 1) | exactly one row r: b_{r,a} ∝ q_1^3 with mass 1−x (pure-q) | as L2 |
| L4 | (mid, mid) | exactly two rows r != r': b_{r,a} pure-e_6, b_{r',a} pure-e_7, both of mass μ; and x = y = 1−μ | R_6 = R_7; x != y |
| L5 | (1, 0) | 1 or 2 rows, all pure-q ∝ q_1^2, masses summing to 1; with one row, Q_1(r,a) = ω q_1^2 | R_6 != R_7; three or more rows |
| L6 | (0, 1) | as L5 with q_1^3 | as L5 |
| L7 | (mid, 0) | |R_d| <= 2; at least one of |R_6|, |R_7| equals 2 | a single row; R_6, R_7 distinct singletons |
| L8 | (0, mid) | as L7 | as L7 |
| L9 | (0, 0) | D = P_B; |R_d| <= 3; at least two rows | a single row |

*Proof.* In each case D = D(a) comes from Lemma D, and the bound on |R_d| from Lemma P4.
- **L1.** D = 0. A unit vector whose B-part has norm 1 lies in V_B.
- **L2, L3, L5, L6.** D has rank one with range spanned by q_1^2 (L2, L5) or q_1^3 (L3, L6). Every nonzero b_{r,a} lies in that range, so it is pure-q and has both coordinates, which gives R_6 = R_7. The P4 bound is 1 in L2/L3 and 2 in L5/L6. Nonemptiness holds because D != 0.
- **L4.** D has rank two and the P4 bound is 1, while δ_6, δ_7 > 0. So R_6 = {r} and R_7 = {r'}. If r = r', then D = b b^* has rank one, a contradiction. So r != r'. Row r has coordinate 6 but not 7, so b_{r,a} is pure-e_6; likewise b_{r',a} is pure-e_7. No other R' row has B-content, so D is diagonal in {e_6,e_7}. By Lemma Sc, D = μ·1, so 1−x = 1−y = μ.
- **L7, L8.** D has rank two and is not scalar, since its eigenvalues 1−x and 1 differ. A single row gives rank at most one. Distinct singletons R_6 = {r}, R_7 = {r'} would make D e-diagonal, hence scalar by Lemma Sc, a contradiction.
- **L9.** D = P_B has rank two.
QED

## 4. Theorem LR (exact local table for a row i ∈ R'; own frame)

Theorem LR is Theorem LC with the e-basis and the q-basis exchanged. Use x' = x'_i, y' = y'_i, E = E(i) from Lemma E, C_k = C_k(i), and the own P4 bound. The cases L1'-L9' are defined by (x',y') exactly as L1-L9:

| case | (x',y') | forced structure of the B-parts in row i, columns 1..5 | eliminated |
|---|---|---|---|
| L1' | (1,1) | none | none |
| L2' | (1, mid) | exactly one cell, pure-e_6, mass 1−y' | C_2 != C_3; two or more cells |
| L3' | (mid, 1) | exactly one cell, pure-e_7, mass 1−x' | as L2' |
| L4' | (mid, mid) | exactly two cells c != c': pure-q^2 and pure-q^3, both of mass μ'; x' = y' = 1−μ' | C_2 = C_3; x' != y' |
| L5' | (1, 0) | 1 or 2 cells, all pure-e_6, masses summing to 1; with one cell, Q_1(i,c) = ω e_6 | C_2 != C_3; three or more cells |
| L6' | (0, 1) | as L5' with e_7 | as L5' |
| L7' | (mid, 0) | |C_k| <= 2; at least one of |C_2|, |C_3| equals 2 | a single cell; C_2, C_3 distinct singletons |
| L8' | (0, mid) | as L7' | as L7' |
| L9' | (0, 0) | E = P_B; |C_k| <= 3; at least two cells | a single cell |

*Proof.* Identical to Theorem LC, with these substitutions:
- E is diagonal in the e-basis (Lemma E);
- "pure-e" parts have both own indices, playing the role pure-q parts played for coordinates;
- the rank and scalar arguments use Lemma Sc with the bases exchanged.

Example, L4'. Since |C_k| <= 1, we get C_2 = {c} and C_3 = {c'}. Here c != c', else rank one. The B-part at c has no q^3-component, so it is proportional to q_1^2; the one at c' is proportional to q_1^3. So E is q-diagonal and e-diagonal, hence scalar. QED

## 5. Theorem X (cross-line compatibility: common column cases versus own row cases)

Every nonzero B-part b_{r,a} with r ∈ R' and a ∈ {1..5} lies in column a and in row r. It must satisfy both cases simultaneously:
- **(X1)** Every completion row of a column in case L2, L3, L5 or L6 (pure-q cells) is in row case L4', L7', L8' or L9'. Row cases L1', L2', L3', L5', L6' admit no pure-q cell. Further, a q_1^2-cell cannot lie in a row of case L4' whose q_1^2-slot is already taken, and the analogous restriction holds for q_1^3.
- **(X2)** Every cell of a row in case L2', L3', L5' or L6' (pure-e cells) lies in a column of case L4, L7, L8 or L9. A pure-e_6 cell needs the column's e_6-row, and a pure-e_7 cell needs its e_7-row.
- **(X3)** The two completion rows of a column in case L4 are pure-e_6 and pure-e_7. They lie in rows of cases admitting pure-e cells of that coordinate: L2'/L5' for e_6, L3'/L6' for e_7, and L7'/L8'/L9' for either. Never L1' or L4'.
- **(X4)** The two cells of a row in case L4' are pure-q^2 and pure-q^3. They lie in columns of cases admitting that pure-q type: L2/L5 for q^2, L3/L6 for q^3, and L7/L8/L9 for either. Never L1 or L4.
- **(X5) Mass matching.**
  - If a column of case L2 (mass 1−y_a at a q_1^2-cell) meets a row of case L4' there, then 1−y_a = μ'_i.
  - If a column of case L4 (mass μ_a at a pure-e cell) meets a row of case L2' or L3' there, then μ_a equals that row's single-cell mass.
  - The analogous equalities hold for L3/L4' and L4/L3'.

*Proof.* Theorems LC and LR prescribe the type (pure-q, pure-e, or general) and the mass of every nonzero B-part in their column, resp. row. A single vector cannot be both pure-q and pure-e, because q_1^2, q_1^3 have full support {6,7}. Cases whose B-parts are all pure of one kind exclude the other kind. Masses at a cell are a single number. QED

## 6. Theorem O (O_next made precise and proved; joint B/C completion)

- **(O1) Block cross-Gram vanishing.** For every row r of square 1 and distinct blocks X, Y ∈ {Z,A,B,C}:

      sum_{c=1..7} P_X Q_1(r,c) (P_Y Q_1(r,c))^* = 0.

  For every column c and any two distinct coordinates d != d':

      sum_{i=1..7} <e_d,Q_1(i,c)> conj(<e_{d'},Q_1(i,c)>) = 0.

- **(O2) 2-cover theorem (cross-line).** Let d, d' be coordinates in different blocks. Let X_{dd'} be the set of interior cells where square 1's vector has both d and d' in its support. Then every row and every column meets X_{dd'} in 0 or at least 2 cells. Hence X_{dd'} is empty or contains at least four cells, in at least two rows and two columns.

- **(O3) Joint row.** Some row r ∈ {1,6,7} carries both:
  - B-completion mass: coordinate 6 or 7 of square 1 in a column of {1..5};
  - C-completion mass: coordinate 4 or 5 in a column of {1,2,3,6,7}.

- **(O4) Joint orthogonality in that row.** In every row r ∈ {1,6,7}:
  - sum_c P_B Q_1(r,c)(P_C Q_1(r,c))^* = 0;
  - for every β ∈ {6,7} and γ ∈ {4,5}, the cells of row r carrying both β and γ are not exactly one;
  - consequently, a cell where a B-completion coordinate and a C-completion coordinate meet forces a second such cell for the same pair, both in its row and in its column.

- **(O5) Paired B-cells of a split B-row.** If |J_2| = 2 = |{a,b}|, the non-B parts n_a, n_b of Q_1(2,a), Q_1(2,b) satisfy conj(λ_{2,a}) n_a + conj(λ_{2,b}) n_b = 0. So the two vectors span span{q_1^3, n_a}, and ||n_a||^2 = |λ_{2,b}|^2. The same holds for row 3 with q_1^2 and for the C rows 4, 5.

*Proof.*
- **(O1).** sum_{c=1..7} |Q_1(r,c)><Q_1(r,c)| = I − |q_1^r><q_1^r|. Because q_1^r lies in a single block, P_X(I − |q_1^r><q_1^r|)P_Y = 0 for X != Y. For columns, sum_{i=1..7} |Q_1(i,c)><Q_1(i,c)| = I − |e_c><e_c|, whose (d,d') entry vanishes for d != d'.
- **(O2).** By (O1), in each row the sum of v(d)conj(v(d')) over the interior cells vanishes. Its nonzero terms are exactly the cells of X_{dd'} in that row, so there cannot be exactly one. The same holds for columns. Columns d and d' contain no cell of X_{dd'}, by (F1). A nonempty set meeting every line in 0 or at least 2 cells has at least 2 cells in some row. Each of those cells' columns contains a second cell, so there are at least 4 cells.
- **(O3).** By Lemma P1, sum_{a=1..5} δ_7(a) = 4 is carried by rows of R'. Each row r ∈ R' has coordinate-7 mass 1 by (S), and q_1^r ⊥ e_7 for r ∈ R'. So at least four rows of R' carry positive B-completion mass, hence at least two of {1,6,7}. The C-twin of Lemma P1 applies to columns {1,2,3,6,7} and rows R'_C, and gives at least two of {1,6,7} as well. By pigeonhole, some row of {1,6,7} carries both.
- **(O4)** is (O1) with X = B, Y = C, and (O2) with d = β, d' = γ.
- **(O5).** Apply (O1) to row 2 with X = B and Y the complement of B in (q_1^2)^⊥. Lemma R gives B-parts λ_{2,j} q_1^3 supported on J_2, so q_1^3 (sum_{j ∈ J_2} conj(λ_{2,j}) n_j)^* = 0. Orthogonality of Q_1(2,a) and Q_1(2,b) together with unit norms gives the norm identity.
QED

## 7. C-block twins and A couplings (re-proved by transfer)

Theorems K, LC, LR and X, and Lemmas D, E, P1, P4 hold verbatim for the C block under the following substitutions:
- coordinates 6, 7 by 4, 5;
- rows 2, 3 by rows 4, 5, and q_1^2, q_1^3 by q_1^4, q_1^5;
- the column range {1..5} by {1,2,3,6,7};
- R' by R'_C, and columns 6, 7 by columns 4, 5;
- t by t_C := |<e_5,q_1^5>|^2.

The transfer uses (AX) q_s^4, q_s^5 ⊥ V_C, the fact that the C block is dense, and P_C e_a = 0 for a ∉ {4,5}. Call the cases LC^C and LR^C.

**A couplings (re-proved).**
- **Lemma Z.** In a nonnegative matrix with integral column sums, each connected component of the support graph has integral total row sum. The proof is that each row's mass lies in the columns of its component.
- **Rows.** The fractional row sums of square 1's coordinate-d mass matrix are 1 − |<e_d,q_1^r>|^2 for the rows r with d ∈ supp q_1^r. These rows are {1,7} for d = 1 and {1,6,7} for d ∈ {2,3}, with fractional parts summing to 1 and 2 respectively. Hence those rows lie in one component.
- **Three-row case.** No proper nonempty subset of three numbers in (0,1) summing to 2 has an integral sum.
- **Columns (own frame).** Columns {1,2,3} share a component of square 1's own-index-1 and own-index-7 mass matrices, and columns {2,3} share one for own index 6.

## 8. Theorem F (explicit finite list of surviving types; nothing eliminated at type level)

**B, common frame: the 9 types of (J_2, J_3)** with their column cases. Here a, b, c, d are distinct columns of {1..5}, and unlisted columns are L9.
1. T1: J_2 = J_3 = {a} — a: L1.
2. T2: J_2 = {a}, J_3 = {b} — a: L5, b: L6.
3. T3: J_2 = {a}, J_3 = {a,b} — a: L2, b: L8.
4. T4: J_2 = {a}, J_3 = {b,c} — a: L5, b and c: L8.
5. T5: J_2 = {a,b}, J_3 = {a} — a: L3, b: L7.
6. T6: J_2 = {a,b}, J_3 = {c} — a and b: L7, c: L6.
7. T7: J_2 = J_3 = {a,b} — a and b: L4, with x_a = y_a and x_b = y_b.
8. T8: J_2 = {a,b}, J_3 = {a,c} — a: L4 (x_a = y_a), b: L7, c: L8.
9. T9: J_2 = {a,b}, J_3 = {c,d} — a and b: L7, c and d: L8.

**B, own frame: the 9 types T1'-T9' of (I_6, I_7)** are word-for-word the same with rows of R' in place of columns and L' cases in place of L cases. For example, T7': I_6 = I_7 = {i,j}, with rows i and j in L4' and x'_i = y'_i, x'_j = y'_j.

**C block:** the same 9 + 9 types for (J_4, J_5) ⊆ {1,2,3,6,7} and for (I_4, I_5) ⊆ R'_C.

**Surviving list.** The remaining obligations are the explicit finite product of these four 9-element type lists, 9^4 type combinations. For each combination:
- the forced local structures of Theorems LC, LR and their C-twins hold;
- the compatibility law X and its C-twin hold;
- the joint B/C constraints O1-O5 and the A couplings hold.

The eliminated sub-branches are exactly those listed in the tables of sections 3-4 and their C-twins, each retained with its proof.

**No type combination is eliminated here.** Every J-type leaves at least one L9 column, and every I-type at least one L9' row, since at most four of the five lines are special. These flexible lines can absorb every forced pure placement of (X1)-(X4). This observation is not a proof that any combination is realizable.

## 9. Exact isolation

**Proved**, for all genuine B3 configurations:
- Lemma R; Theorem K;
- Lemmas D, E, Sc, P1, P4;
- Theorems LC, LR, X and their C-twins;
- Theorem O, i.e. O_next made precise, including the joint row and the 2-cover theorem;
- the A couplings.

**Not proved:** any elimination of a type combination in Theorem F, and hence any full B3 no-go. A decision would need, at least:
- the realization of the forced pure placements together with the masses (X5);
- coupling with the A-region and Z-coordinates in rows {1,6,7} and columns {1,2,3}, where both B- and C-completion live (O3, O4);
- the interior line frames.

None of these is attempted beyond what is stated. No full-grid claim is made from partial data. No Boolean/GB/UNSAT statement is made. GB 15/18, the UNKNOWNs, A10/A11 and the n=8 target are unchanged.

## 10. Imports and sources

The imports are:
- [PRIM] LF195-225, for the definitions;
- [J], the GBBINDING P1-B3 entry, for the template rows.

The earlier B-propagation candidate [BP] is credited, but every lemma used from it is re-proved here, and it is not a premise.

- [PRIM] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/sources/2607.12933v2.raw.txt`, SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9`.
- [J] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1/GBBINDING.json`, SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`.
- [BP] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-global-mass-coupling/B3-BLOCK-PROPAGATION-CANDIDATE-v1.md`, SHA256 `627f6134eb486cf729ca679654f84fb0fe6f042c2a20bbb9c9cb69dd8483e64d`.
- [TR] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-slot-transitions-moq-cp1-20261019-1714-v1.json`, SHA256 `5b34fc67350bc137dcd7ec885859a6b35d15ff395c31b4a7351c378bdf055b4f`.
- [SC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-joint-completion/SCOPE-FREEZE-v1.json`, SHA256 `5a97772f6bd0548561280d4971f85c0d727a34599807b45cdc0579bb7fbca536`.
