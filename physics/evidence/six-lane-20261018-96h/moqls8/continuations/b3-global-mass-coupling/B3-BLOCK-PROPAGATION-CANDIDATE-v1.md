# B3 global mass coupling: the B/C-block propagation theorem — CANDIDATE v1

Frozen at 2026-10-19T17:10:51-0700 under `SCOPE-FREEZE-v1.json` (SHA256 `3b41bf1d82dcd4c5538b276ebe825fdfb859a8ac630c722b0a91e0f93f8da35f`). Status: CANDIDATE written mathematics, not reviewed or accepted. Every statement is proved by hand. No script, assertion, enumeration, probe, solver, checker, CLI or nested agent was used for any scientific statement.

**Outcome.** ONE explicit cross-line consistency obligation is identified and **proved** for ALL genuine B3 configurations, with all axis data, all amplitudes and phases, and general interior vectors. This is the **B-block propagation theorem** (Theorem P), with its C-block twin (Theorem P^C) and the A-block component couplings (Theorem A). It couples rows 2 and 3 with the columns they meet and with the remaining rows R' = {1,4,5,6,7}. Dually, it couples columns 6 and 7 with the rows they meet and with columns 1..5, in the own frame. Through cross-square slot blocking it couples all five squares. **No full B3 no-go is obtained.** Section 7 isolates exactly what is proved and what remains. Candidate lemmas used (rank-one structure, cell disjointness) are re-proved here.

## 1. Setting

H1: Q_1,...,Q_5 are a full genuine set of pairwise-orthogonal QLS(8) ([PRIM] LF195-225): rows and columns are ONBs, and G_s(x,y)G_t(x,y) = 0 for s != t and distinct cells, where G_s(x,y) := <Q_s(x),Q_s(y)>. The normal-form hypotheses are:
- H2: Q_s(0,c) = w_{s,c}e_c with |w_{s,c}| = 1;
- H3 (SB2): supp Q_1(1,0) = {1,2,3} and supp Q_s(1,0) = {s+2};
- H4 (exact template [J]): the supports of Q_1(i,0), i = 2..7, are {6,7}, {6,7}, {4,5}, {4,5}, {2,3}, {1,2,3}.

Nothing about the column 0 of squares 2..5 is assumed beyond H1-H3. Put q_s^r := Q_s(r,0). Write V_B = span{e_6,e_7} = span{q_1^2,q_1^3}, V_C = span{e_4,e_5} = span{q_1^4,q_1^5} and V_A = span{e_1,e_2,e_3} = span{q_1^1,q_1^6,q_1^7}, with projections P_B, P_C, P_A.

## 2. Re-proved basic facts

- **(F1)** For i, j >= 1: <e_j,Q_s(i,j)> = 0 (same column as Q_s(0,j)) and <q_s^i,Q_s(i,j)> = 0 (same row).
- **(F2) Slot disjointness.** For an interior cell z = (i,j):
  - for each coordinate d != j, at most one square s has <e_d,Q_s(z)> != 0;
  - for each own index r != i, at most one square has <q_s^r,Q_s(z)> != 0.

  Proof: H1 applied to z and (0,d), resp. z and (r,0), which share neither row nor column with z; also G_s((0,d),z) = conj(w_{s,d})<e_d,Q_s(z)>.
- **(AX)** For r >= 1 the supports of q_1^r,...,q_5^r are pairwise disjoint and avoid 0 (H1 applied to (0,d),(r,0); also q_s^r ⊥ q_s^0). Hence q_s^2, q_s^3 ⊥ V_B and q_s^4, q_s^5 ⊥ V_C for s >= 2.
- **(S) Line sums.** For d ∈ [8], put M^d_s(i,c) := |<e_d,Q_s(i,c)>|^2. For r ∈ [8], put N^r_s(i,c) := |<q_s^r,Q_s(i,c)>|^2. Here i, c ∈ {1..7}. Parseval in row i and column c gives:
  - sum_c M^d_s(i,c) = 1 − |<e_d,q_s^i>|^2 and sum_i M^d_s(i,c) = 1 − δ_{dc};
  - sum_c N^r_s(i,c) = 1 − δ_{ri} and sum_i N^r_s(i,c) = 1 − |<q_s^r,e_c>|^2.

**Lemma R (rank-one structure, re-proved).**
- For i ∈ {2,3}: P_B Q_1(i,j) = λ_{i,j} q_1^{5−i}, with sum_j |λ_{i,j}|^2 = 1.
- For c ∈ {6,7}: P_B Q_1(i,c) = κ_{i,c} e_{13−c}, with sum_i |κ_{i,c}|^2 = 1.
- Moreover λ_{i,6} = λ_{i,7} = 0 and κ_{2,c} = κ_{3,c} = 0.

*Proof.*
- Row i is an ONB, so sum_{j=0..7} P_B|Q_1(i,j)><Q_1(i,j)|P_B = P_B. For i ∈ {2,3} the j = 0 term is |q_1^i><q_1^i|. So the interior terms sum to the rank-one projector |q_1^{5−i}><q_1^{5−i}|. Positive operators of rank at most one summing to a rank-one projector have ranges in its range.
- Column c ∈ {6,7}: the row-0 term is |e_c><e_c|. The interior sum is |e_{13−c}><e_{13−c}|.
- Corners: for i ∈ {2,3} and c ∈ {6,7}, Q_1(i,c) is orthogonal to q_1^i and to e_c. These two vectors span V_B, because q_1^i has support exactly {6,7}. So Q_1(i,c) ⊥ V_B.
QED

Put J_i := {j : λ_{i,j} != 0}, a subset of {1..5}, and I_c := {i : κ_{i,c} != 0}, a subset of R' = {1,4,5,6,7}. Let t := |<e_7,q_1^3>|^2. Since {q_1^2,q_1^3} is an ONB of V_B and both vectors have support {6,7}:
- t ∈ (0,1);
- |<e_6,q_1^3>|^2 = 1 − t, |<e_7,q_1^2>|^2 = 1 − t and |<e_6,q_1^2>|^2 = t.

## 3. Lemma Z (component integrality)

Let M be a nonnegative matrix whose column sums are all integers, and let K be a connected component of its support graph (bipartite, rows ∪ columns). Then the row sums over the rows of K add up to an integer, namely the sum of the column sums of K. Hence rows with non-integral sums must be grouped into components whose fractional parts total an integer. The same holds with rows and columns exchanged.

*Proof.* Every entry of a row of K lies in a column of K, and vice versa. QED

## 4. Theorem P (B-block propagation; the cross-line obligation)

Let a ∈ {1..5} be a column. Define the square-1 **deficits**:
- δ_7(a) := 1 − |λ_{2,a}|^2 t − |λ_{3,a}|^2 (1−t);
- δ_6(a) := 1 − |λ_{2,a}|^2 (1−t) − |λ_{3,a}|^2 t.

Define R_d(a) := {r ∈ R' : M^d_1(r,a) > 0} for d ∈ {6,7}. Then:

**(P1) Exact completion.** sum_{r ∈ R'} M^d_1(r,a) = δ_d(a) for d ∈ {6,7}. So the part of square 1's coordinate-d mass in column a not supplied by rows 2 and 3 must be supplied by rows of R'. Also R_d(a) != ∅ iff δ_d(a) > 0.

**(P2) Rigidity.** δ_6(a) = 0 iff δ_7(a) = 0 iff J_2 = J_3 = {a}. In that case Q_1(2,a) and Q_1(3,a) are unit multiples of q_1^3 and q_1^2. Every other column of {1..5} has a positive deficit in both coordinates.

**(P3) Global totals.** sum_{a=1..5} δ_7(a) = sum_{a=1..5} δ_6(a) = 4.

**(P4) Cross-square capacity.** For d ∈ {6,7}:

    |R_d(a)| + [a ∈ J_2] + [a ∈ J_3] <= 3.

Hence:
- if a ∈ J_2 ∩ J_3, then |R_d(a)| <= 1, with equality unless J_2 = J_3 = {a};
- if a ∈ J_2 Δ J_3, then 1 <= |R_d(a)| <= 2;
- if a ∉ J_2 ∪ J_3, then 1 <= |R_d(a)| <= 3.

At every cell (r,a) with r ∈ R_d(a), and at (2,a) for a ∈ J_2 and (3,a) for a ∈ J_3, no square s >= 2 carries coordinate d.

**(P5) Dual (own frame).** For a row i ∈ R' define:
- ε_3(i) := 1 − |κ_{i,6}|^2 t − |κ_{i,7}|^2 (1−t);
- ε_2(i) := 1 − |κ_{i,6}|^2 (1−t) − |κ_{i,7}|^2 t;
- C_r(i) := {c ∈ {1..5} : N^r_1(i,c) > 0} for r ∈ {2,3}.

Then:
- sum_{c ∈ {1..5}} N^r_1(i,c) = ε_r(i);
- ε_2(i) = 0 iff ε_3(i) = 0 iff I_6 = I_7 = {i};
- sum_{i ∈ R'} ε_3(i) = sum_{i ∈ R'} ε_2(i) = 4;
- |C_r(i)| + [i ∈ I_6] + [i ∈ I_7] <= 3, with the case split of (P4);
- at the corresponding cells no square s >= 2 carries own index r.

**(P6) Connectors.** Rows 2 and 3 lie in one connected component of the support graph of M^7_1 (rows 1..7, columns 1..6), and likewise for M^6_1 (columns 1..5, 7). Columns 6 and 7 lie in one connected component of the support graph of N^3_1 (rows other than 3), and likewise for N^2_1. In particular:
- if J_2 ∩ J_3 = ∅, some row of R' carries coordinate 7 (resp. 6) of square 1 in at least two columns, one of them in J_2;
- if I_6 ∩ I_7 = ∅, some row of I_6 carries own index 3 of square 1 both in column 6 and in a column of {1..5} (similarly for index 2).

*Proof.*

(P1) Column a ∈ {1..5} is an ONB containing w e_a with e_d ⊥ e_a, so by (S) the coordinate-d mass of square 1 in column a is 1. By Lemma R, <e_7,Q_1(2,a)> = <e_7,P_B Q_1(2,a)> = λ_{2,a}<e_7,q_1^3>, whose square modulus is |λ_{2,a}|^2 t. Likewise <e_7,Q_1(3,a)> has square modulus |λ_{3,a}|^2 (1−t). The same works for d = 6 with t and 1−t exchanged. The remaining rows are exactly R'.

(P2) Since |λ| <= 1, we have δ_7(a) >= 1 − t − (1−t) = 0, with equality iff |λ_{2,a}| = |λ_{3,a}| = 1. That holds iff all of row 2's and row 3's B-mass sits in column a, i.e. J_2 = J_3 = {a}. The same holds for δ_6. If |λ_{2,a}| = 1, the unit vector Q_1(2,a) has a B-part of norm 1, so it equals λ_{2,a} q_1^3.

(P3) sum_a δ_7(a) = 5 − t sum_a |λ_{2,a}|^2 − (1−t) sum_a |λ_{3,a}|^2 = 5 − t − (1−t) = 4, using Lemma R (λ_{i,6} = λ_{i,7} = 0). Similarly for δ_6.

(P4) For s >= 2, (S) gives coordinate-d mass 1 in column a (a != d), so each of the four squares has a nonempty set of rows carrying coordinate d in column a. By (F2), these four sets are pairwise disjoint and avoid the rows where square 1 carries coordinate d in column a. The latter rows are 2 if a ∈ J_2 (because <e_d,q_1^3> != 0), 3 if a ∈ J_3, and R_d(a). Seven rows give the inequality. The case split follows from (P1) and (P2).

(P5) This is the same argument in the own frame.
- Row i ∈ R' is an ONB containing q_1^i ⊥ q_1^r (r ∈ {2,3}), so its index-r mass is 1 by (S).
- By Lemma R, <q_1^3,Q_1(i,6)> = κ_{i,6}<q_1^3,e_7> has square modulus |κ_{i,6}|^2 t, and <q_1^3,Q_1(i,7)> has square modulus |κ_{i,7}|^2 (1−t).
- Summation over R' uses the column sums: column c ∈ {1..5} has index-3 mass 1 − |<q_1^3,e_c>|^2 = 1. Row 2 contributes exactly 1 there (its index-3 mass lies in J_2 ⊆ {1..5}). Row 3 contributes 0. So sum_{i ∈ R'} ε_3(i) = 5 − 1 = 4.
- For s >= 2 and i ∈ R', row i of square s contains q_s^i ⊥ q_s^r, so each such square needs a nonempty disjoint set of columns carrying own index r (by (F2)). The rest is as in (P4). (Square 1 carries index 3 at (i,6) iff i ∈ I_6, because <q_1^3,e_7> != 0.)

(P6) Apply Lemma Z to M^7_1 restricted to columns 1..6; column 7 carries no coordinate 7 by (F1).
- The column sums are 1.
- The row sums are 1 for r ∈ R', since q_1^r ⊥ e_7 for those r by H4, and 1−t, t for rows 2 and 3, since 1 − |<e_7,q_1^2>|^2 = t and 1 − |<e_7,q_1^3>|^2 = 1−t.
- A component containing exactly one of rows 2 and 3 would have a non-integral row total. So rows 2 and 3 share a component.
- If J_2 ∩ J_3 = ∅, a shortest path from row 2 to row 3 leaves row 2 through a column a_1 ∈ J_2 and reaches some r_1 ∈ R'. Row 3 does not meet a_1, so the path continues from r_1 through a second column. Hence row r_1 carries coordinate 7 in at least two columns.

The own-frame statements are the transposed argument with N^3_1 and N^2_1: row sums 1 for rows other than r, column sums 1 − |<q_1^r,e_c>|^2, fractional exactly at c ∈ {6,7}. QED

**Theorem P^C (C-block twin).** Replace in Theorem P:
- {6,7} by {4,5} and coordinates 6, 7 by 4, 5;
- rows 2, 3 by rows 4, 5 and q_1^2, q_1^3 by q_1^4, q_1^5;
- the column range {1..5} by {1,2,3,6,7};
- R' by R'_C = {1,2,3,6,7}, and columns 6, 7 by columns 4, 5;
- t by t_C := |<e_5,q_1^5>|^2.

All statements and proofs transfer verbatim, using (AX) q_s^4, q_s^5 ⊥ V_C and the dense C block.

## 5. Theorem A (A-block component couplings)

By Lemma Z applied to square 1:
- in the support graph of M^1_1 (columns other than 1), rows 1 and 7 lie in one component;
- in the support graphs of M^2_1 and M^3_1, rows 1, 6, 7 lie in one component;
- in the support graphs of N^1_1 and N^7_1 (rows other than 1, resp. 7), columns 1, 2, 3 lie in one component;
- in that of N^6_1, columns 2 and 3 lie in one component.

*Proof.* The non-integral row sums of M^d_1 are 1 − |<e_d,q_1^r>|^2 for exactly those rows r with d ∈ supp q_1^r. These rows are {1,7} for d = 1 and {1,6,7} for d ∈ {2,3}.
- Their fractional parts sum to (number of rows) − 1, which is 1 or 2.
- For two rows, the argument of (P6) applies.
- For three rows with values in (0,1) summing to 2, no proper nonempty subset sums to an integer. One value is not an integer. Two values summing to 1 would force the third to equal 1.
- The own-frame statements are transposed; the fractional columns of N^r_1 are supp q_1^r.
QED

## 6. Cross-square content, stated explicitly

Theorems P, P^C and A are statements about square 1. Each of their "carries coordinate d at cell z" conclusions blocks, by (F2), the slot (z,d) for all four other squares. Each (P4)/(P5) bound is a cross-square inequality: it combines square 1's forced completion cells with the four other squares' Parseval demands in the same column (resp. row). Hence the obligation couples:
- the B-rows 2, 3, the columns J_2 ∪ J_3 and all rows of R';
- dually, the B-columns 6, 7, the rows I_6 ∪ I_7 and all columns 1..5;
- the same twice more for the C block;
- all five squares.

## 7. Exact isolation: what is proved and what remains

**Proved** (all genuine B3 configurations, all axes and phases, general vectors): Lemma R; Lemma Z; Theorems P, P^C and A, with exact deficit formulas, exact global totals (4) and cross-square capacity bounds.

**Not proved.** No contradiction is derived among (P1)-(P6), (P^C) and (A), or between them and the remaining H1 equations. A full B3 no-go needs additional coupling. The natural next obligation, stated exactly but NOT proved, is:

> **(O_next)** Combine Theorem P for coordinate 7 with Theorem P^C for coordinate 5, in the interior frame of an R'-row r of square 1. Here r must carry completion mass in both blocks, by (P3) and its C-twin. The mass vectors forced in that row must be orthogonal to all other entries of row r while respecting the four other squares' slot demands in every frame (row r, columns 1..7).

The interior frames (rows and columns i, j >= 1) are unknown vectors. Their (F2)-type disjointness holds for a full configuration, but it is not exploited here.

No full-grid claim is made from partial data. No Boolean/GB/UNSAT statement is made. GB 15/18, the UNKNOWNs, A10/A11 and the n=8 target are unchanged.

## 8. Import table and ledger

| item | role | status |
|---|---|---|
| [PRIM] LF195-225 | definitions (H1) | primary source |
| [J] GBBINDING entry P1-B3 | template rows (H4) | identity metadata |
| H2-H4 | hypotheses for all genuine B3 data | conditioning; U/T16 link not used |
| D-concentration candidate [DC] | context (its Lemma B(b)-type statement is re-proved here as Lemma R) | not a premise |
| row-1, interior, sparsity candidates and verdicts | not used | — |

| claim | status |
|---|---|
| F1, F2, AX, S, Lemma R, Lemma Z | proved |
| Theorem P (P1-P6) | proved |
| Theorem P^C | proved (verbatim transfer) |
| Theorem A | proved |
| full B3 no-go | NOT proved |
| (O_next) | stated, not proved |

## 9. Sources

- [PRIM] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/sources/2607.12933v2.raw.txt`, SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9`.
- [J] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1/GBBINDING.json`, SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`.
- [DC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-d-general-extension/D-EXTENSION-CONCENTRATION-CANDIDATE-v1.md`, SHA256 `18b5d33b10f53f43c51063fa34590563e1d385f2a83b3e20e84b18481a40acfe`.
- [TR] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-slot-transitions-sun-physics-20261019-1700-v1.json`, SHA256 `b29119aa12222bf31cdaf6afdb59e81bc58ad2525fa9e08c5384bf86bc7d6bf2`.
- [SC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-global-mass-coupling/SCOPE-FREEZE-v1.json`, SHA256 `3b41bf1d82dcd4c5538b276ebe825fdfb859a8ac630c722b0a91e0f93f8da35f`.
