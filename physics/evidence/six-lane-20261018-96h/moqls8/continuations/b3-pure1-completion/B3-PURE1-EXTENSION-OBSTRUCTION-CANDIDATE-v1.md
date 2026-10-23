# B3 PURE1 (column-1 pure-A corner): extension obstruction of the old column-1 witness, exact reduction, and remaining obligation — CANDIDATE v1 (BLOCKED, NOT RESOLVED)

Frozen at 2026-10-19T22:05:37-0700 under `SCOPE-FREEZE-v1.json` (SHA256 `e1af028ec4a123426fa2f21af3991dd63bd7194fa27f1b4c0ce7708d0fa2c3cb`). Status: CANDIDATE written mathematics, not reviewed. No candidate is a premise; PURE23 is not used. No script, assertion, enumeration or numerical check was used.

**Outcome: BLOCKED.** Neither a family exclusion nor a new assignment of rows 0, 1, 7 and full column 0 was obtained. Proved here:
- L1: the shape of a column-1 pure-A corner;
- L2: column 0 of squares 2..5;
- D: the precise point where the column-2/3 mechanism does not transfer to column 1 (the coordinate-1 distinction);
- **O1: the old column-1 partial assignment has NO extension to a full column 0**, whatever the remaining column-0 entries, square-1 template amplitudes or phases;
- R1: an exact reduction of all direct equations on rows 0, 1, 7 and column 0 to finite combinatorial conditions, for a stated "twin" sub-model.

The family is not excluded, and no assignment of the required shape is claimed. Nothing is claimed for B3, n=8, Boolean or GB status.

## 1. Hypotheses and elementary rules

- **H1.** Q_1,...,Q_5 are genuine pairwise-orthogonal QLS(8) ([PRIM] LF195-225). For distinct cells z, z' and squares s != t: <Q_s(z),Q_s(z')><Q_t(z),Q_t(z')> = 0 (T).
- **H2.** Q_s(0,d) = w_{s,d}e_d with |w_{s,d}| = 1.
- **Template.** Write q^k := Q_1(k,0) and q_s^k := Q_s(k,0). Supports: S_1 = S_7 = A = {1,2,3} for q^1 (SB2, [NF] LF109) and q^7; S_6 = {2,3}, S_2 = S_3 = {6,7}, S_4 = S_5 = {4,5} ([J]); S_0 = {0}. Every listed coordinate is nonzero.
- Notation: D := {0,4,5,6,7}, W := {4,5,6,7}, V_A := span{e_d : d in A}. r ∈ {1,7}, and r' is the other element. Column-0 orthonormality makes q^1, q^6, q^7 an ONB of V_A.

Elementary rules:
- **(C1)** Q_s(i,c) has zero coordinate c (for i, c >= 1).
- **(C2)** At a cell z off row 0, at most one square has a nonzero coordinate d, for d different from z's column. Apply (T) to z and (0,d).
- **(C3)** At (i,c) with c >= 1, and for k != i, at most one square has <q_s^k,Q_s(i,c)> != 0. Apply (T) to (i,c) and (k,0).

## 2. L1 (shape of a column-1 pure-A corner)

Suppose Q_1(r,1) ∈ V_A. Then:
- (i) Q_1(r,1) = ω q^6;
- (ii) Q_1(r',1) has zero A-part;
- (iii) there is exactly one j ∈ W with Q_1(r,j) = ω' q^{r'}, and the five cells (r,c), c ∈ {2,3} ∪ W \ {j}, form an ONB of span{e_d : d ∈ D}.

*Proof.*
- **(i).** Q_1(r,1) ⊥ e_1 (column 1) and ⊥ q^r (row r). Within V_A these two independent vectors leave the line span{q^6}, because q^6 ⊥ e_1 by support and q^6 ⊥ q^r by column 0.
- **(ii).** P_A Q_1(r',1) ⊥ e_1, q^{r'}, so it lies in span{q^6}. Column 1 gives 0 = <ωq^6, Q_1(r',1)> = conj(ω)<q^6, P_A Q_1(r',1)>.
- **(iii), A-parts.** For c ∉ {0,1}, P_A Q_1(r,c) ⊥ q^r, q^6, so it lies in span{q^{r'}}. It vanishes for c ∈ {2,3}, since it is also ⊥ e_c while q^{r'} has a nonzero c-coordinate.
- **(iii), mass.** The row-r resolution projected to V_A gives Σ_{c∈W} |<q^{r'},Q_1(r,c)>|^2 = 1. Let k >= 1 be the number of W-cells with a nonzero q^{r'}-coefficient.
- **(iii), slot count.**
  - Row r has 18 slots (c,d) with d ∈ A \ {c}.
  - For s >= 2, (T) at (r,0),(0,d) gives q_s^r ⊥ V_A. So each of the 12 pairs (s,d), d ∈ A, has row mass 1 and uses at least one slot.
  - Slots are exclusive by (C2).
  - Square 1 uses 2 slots at (r,1) and 3 at each of the k cells.
  - Hence 12 + 2 + 3k <= 18, so k = 1. That cell carries mass 1, so Q_1(r,j) = ω'q^{r'}.
- **(iii), the other five cells.** They are unit vectors orthogonal to q^r, q^6, q^{r'}, i.e. to all of V_A, and they are mutually orthogonal.

QED

## 3. L2 (column 0 of squares 2..5)

For s >= 2:
- by (T) at (k,0),(0,d) for d ∈ S_k, and column orthogonality to q_s^0 ∝ e_0, the vector q_s^k has zero coordinates on S_k ∪ {0};
- q_s^1 = phase e_{p_s} and q_s^7 = phase e_{t_s}, with p and t bijections onto W and p_s != t_s;
- there are rows a_s != b_s in {2,...,5} with q_s^{a_s} = phase e_2 and q_s^{b_s} = phase e_3, and s ↦ a_s, s ↦ b_s are bijections.

*Proof.*
- **Rows 1 and 7.** At these rows the four vectors have nonempty, pairwise disjoint supports (C2) in the four-set W. So they are singletons and form bijections. Also q_s^1 ⊥ q_s^7.
- **Coordinate 2.** It has column-0 mass 1 in square s. That mass lies in rows 2..5, since rows 1, 6, 7 have zero coordinate 2 by the first bullet. Each of these four rows admits only one of the four squares (C2). So each square uses exactly one row, with full mass, i.e. a pure vector.
- **Coordinate 3.** The same argument applies.

QED

## 4. D (the coordinate-1 distinction: what the column-2/3 mechanism needs and column 1 lacks)

Assume L1. Let y := (r,1) and x := (r,j).

At y, square 1's own coefficients are nonzero only for own index 6, because Q_1(y) = ωq^6. At x they are nonzero only for own index r'. So (C3) yields exactly:

    Q_s(y) ⊥ q_s^6 and Q_s(x) ⊥ q_s^{r'}   (s >= 2),

and no own-6 condition at x and no own-r' condition at y.

As in the column-2/3 analysis, Q_s(x) = phase e_{d_s}, with {d_s} = D \ {j}. Proof: square 1 occupies A at x, (C1) excludes j, and four pairwise disjoint nonempty supports lie in a four-set.

For a column-2/3 corner, the corner vector u has a nonzero e_1-coefficient, so it is not proportional to q^6. Both pure-A cells therefore carry own indices 6 and r'. This forces <q_s^6, e_{d_s}> = 0 and Q_s(y) ⊥ e_{t_s}, which drives that contradiction.

For column 1, the corner vector is q^6 itself, because q^6 has zero coordinate 1. Neither condition follows. This is a statement about the proof only; it is not a consistency claim.

## 5. O1 (the old column-1 witness does not extend to a full column 0)

Let OW be the assignment of [OLD] section 4:
- rows 0 and 1 of all five squares;
- column 0 at rows 0, 1, 6, 7;
- in particular Q_1(1,5) = e_6, Q_1(1,6) = e_7, Q_2(1,1) = e_7, Q_3(1,1) = e_6, Q_2(1,5) = e_3, Q_2(1,6) = e_5;
- column 0 of square 2 at rows 0, 1, 6, 7: e_0, e_4, e_6, e_5;
- column 0 of square 3 at rows 0, 1, 6, 7: e_0, e_5, e_1, e_4.

Complete square 1's column 0 by any q^2, q^3 with support {6,7} and q^4, q^5 with support {4,5}. Then no choice of q_s^2,...,q_s^5 (s = 2..5) satisfies column-0 orthonormality and (T) for all pairs among the assigned cells.

*Proof.*
- **Square 2, rows 2 and 3.** <Q_1(1,5),q^i> = <e_6,q^i> != 0 for i = 2, 3, and (1,5), (i,0) share no line. So (T) gives <Q_2(1,5),q_2^i> = <e_3,q_2^i> = 0. Likewise (1,6) gives <e_5,q_2^i> = 0. By (T) at (i,0),(0,d) with d ∈ {6,7} = S_i, q_2^i also has zero coordinates 6 and 7.
- **Square 2, rows 2..5.** Column-0 orthonormality makes q_2^2,...,q_2^5 an ONB of span{e_0,e_4,e_6,e_5}^⊥ = span{e_1,e_2,e_3,e_7}. So q_2^2, q_2^3 is an ONB of span{e_1,e_2}, and q_2^4, q_2^5 is an ONB of span{e_3,e_7}.
- **Square 3.** Here q_3^2,...,q_3^5 is an ONB of span{e_2,e_3,e_6,e_7}. Rows 2 and 3 lack coordinates 6 and 7, so q_3^4, q_3^5 is an ONB of span{e_6,e_7}.
- **Coordinate 7 at rows 4 and 5.** It has total mass 1 there in square 2, and also in square 3. By (T) at (i,0),(0,7), each row admits only one of the two squares. Hence there is ρ ∈ {4,5} with q_2^ρ = phase e_7 and q_3^{ρ'} = phase e_7, where ρ' is the other row. Then q_3^ρ = phase e_6.
- **Contradiction.** Now <Q_2(1,1),q_2^ρ> != 0 and <Q_3(1,1),q_3^ρ> != 0, while (1,1) and (ρ,0) share no line. This contradicts (T).

QED

The cause is square 1's basis entries e_6, e_7 in row 1. Each overlaps two own axes (q^2, q^3) and so constrains the other squares' rows 2 and 3. No statement is made about other assignments.

## 6. R1 (exact reduction in the twin model)

Fix explicit axes, with the template supports exactly:

    q^0 = e_0,  q^1 = (e_1+e_2-e_3)/√3,  q^2 = (e_6+e_7)/√2,  q^3 = (e_6-e_7)/√2,
    q^4 = (e_4+e_5)/√2,  q^5 = (e_4-e_5)/√2,  q^6 = (e_2+e_3)/√2,  q^7 = (2e_1-e_2+e_3)/√6.

These are orthonormal by direct inner products.

Let Z be rows 0, 1, 7 and column 0. The **twin model** is:
- square 1: Q_1(0,c) = e_c and Q_1(z) = q^{M(z)} on the rest of Z, with M(i,0) := i;
- squares s = 2..5: Q_s(z) = e_{L_s(z)}, with L_s(0,c) = c;
- λ_s(k) := L_s(k,0).

Then every direct equation among cells of Z holds iff:
- **(a)** rows 1 and 7 of M and of each L_s are permutations of {0..7}, and λ_s is a permutation fixing 0;
- **(b)** for c >= 1: c ∉ S_{M(1,c)} ∪ S_{M(7,c)}; M(1,c) != M(7,c); and c, L_s(1,c), L_s(7,c) are pairwise distinct;
- **(c)** for k = 1..7: λ_s(k) ∉ S_k, and λ_2(k),...,λ_5(k) are pairwise distinct;
- **(d)** at each z = (i,c) with i ∈ {1,7} and c >= 1:
  - the coordinates L_s(z), s = 2..5, are pairwise distinct and avoid S_{M(z)};
  - the own indices λ_s^{-1}(L_s(z)) are pairwise distinct and differ from M(z);
- **(e)** for c != c', both >= 1, at most one of [M(1,c) = M(7,c')], [L_s(1,c) = L_s(7,c')] (s = 2..5) holds.

*Proof.* All values are inner products between members of the ONBs {e_d} and {q^k}: <q^m,q^n> = δ_{mn}, and <q^m,e_d> != 0 iff d ∈ S_m.
- **Collinear pairs.** For pairs sharing a line, (T) follows from within-square orthogonality, which is exactly (a) and (b).
- **Non-collinear pairs.** The complete list:
  - ((0,d),(k,0)), d, k >= 1: gives (c);
  - ((0,d),(i,c)), including d = 0, and ((k,0),(i,c)), k ∉ {0,i}: give (d). Own index i is absent by (a), and own index 0 coincides with coordinate 0;
  - ((1,c),(7,c')), c != c': gives (e).

QED

In this model, a column-1 pure-A corner is M(r,1) = 6. L1 then forces M(r,j) = r' for a unique j ∈ W, and M(r,c) ∈ {0,2,3,4,5} elsewhere.

## 7. Search record (not a classification, not an impossibility claim)

Hand attempts were made in the twin model with r = 1 and j = 4, each with a stated M-placement. Three parameter choices were tried:
- (p,t) = ((4,5,6,7),(6,7,4,5)), two column-0 fillings;
- (p,t) = ((4,5,6,7),(5,4,7,6)) with column 0 (rows 1..7)
  - sq2: 4,2,3,6,7,1,5
  - sq3: 5,1,2,3,6,7,4
  - sq4: 6,4,1,2,3,5,7
  - sq5: 7,3,5,1,2,4,6

None reached a complete row 1 satisfying (d). The attempts stopped at own-index collisions in cells 1, 2/3 or 6. These are records of unfinished hand search only.

## 8. Exact remaining obligation

The column-1 PURE family is open. Either of the following settles the assigned target:
1. An assignment of rows 0, r, r' and full column 0 of all five squares (in the twin model: any solution of R1 (a)–(e) with M(r,1) = 6) satisfying every direct equation among those cells, with the full-grid gap stated: interior rows 2..6, all columns, and every (T) pair touching them.
2. An exclusion of the family. By D, such an exclusion needs constraints beyond the own-6/own-r' mechanism.

By O1, no assignment can contain OW's rows 0, 1 and column-0 rows 0, 1, 6, 7. Nonexistence of twin-model solutions alone would not exclude the family.

## 9. Sources

- [PRIM] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/sources/2607.12933v2.raw.txt`, SHA256 `265851e451cc30706b0a4ea1860c5f04568d99be85896c7b049f95c995108df9`.
- [J] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-16/review/moqls8-gb-parent-binding-v1/GBBINDING.json`, SHA256 `d917203deb29a13e212c290e227a001a695765d080a897141d6dc154d79fc673`.
- [NF] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261016/moqls8-problem16/review/P1_COLUMN0_BOOLEAN_NORMAL_FORM.r2.md`, SHA256 `8ae0ac01de7ea5883111e8dcc4f84246813d8599b1e8af782e0498104a449e8f`.
- [OLD] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-pure-corner/B3-PURE-CORNER-PARTIAL-CANDIDATE-v1.md`, SHA256 `bdd3bd63410edf38ca358ceff89f68e682a98844266a78e3b2e0414c6a183d2c`.
- [N1] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-pure1-completion/WORKING-NOTES-v1.md`, SHA256 `5306f1861bdf58378a925ce31acadf7c26b3ede2e3c243e44e767b7170e4a9f2`.
- [N2] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-pure1-completion/WORKING-NOTES-v2.md`, SHA256 `abd16119dc0a44bcfa01c63eb48bad9cf6341c835ae5eec7d9a7b90d57bd0dc6`.
- [SC] `/Users/jinleic/repos/aifours/physics/evidence/six-lane-20261018-96h/moqls8/continuations/b3-pure1-completion/SCOPE-FREEZE-v1.json`, SHA256 `e1af028ec4a123426fa2f21af3991dd63bd7194fa27f1b4c0ce7708d0fa2c3cb`.
- [TR] `/Users/jinleic/repos/aifours/institute/runs/six-lane-2026-10-18-96h/control/written-B3-pure1-completion-transition-v1.json`, SHA256 `6c49489229449370f27319d4e1c505038fafb0810d336f6563693fc864270deb`.
