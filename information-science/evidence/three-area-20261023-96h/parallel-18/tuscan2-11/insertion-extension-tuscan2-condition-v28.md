# One-symbol insertion extensions: a Tuscan-2(11) square needs its split arcs among the base square's missing distance-2 pairs

Actual `/bin/date` before this body: **Sun Oct 25 23:26:09 PDT 2026**. InfoRecursiveMDS18-2, slot info-4. NEW WRITTEN CANDIDATE (family condition), not reviewed, adopted, formal, executable or novelty-cleared. Written reasoning only; no interpreter, kernel, program, enumeration tool, solver, replay or GO.

## 1. The family

Let S be a Tuscan-1 square of order 10 on V (|V|=10) and z a new symbol. Insert z into each row of S at one of its eleven gaps: first, last, or between consecutive entries s,s' (the row's **split arc** (s,s')). Add an eleventh row E on V ∪ {z}. This is different from the Cutting Method of v26 (SHA256 `df5ab1c9332880cca1dabd070b746b44e776804080dc480e1f439aa5056e7977`): rows keep their S order and gain z, instead of being rotated cycles. v24 Lemma 6.4 (SHA256 `e1fa1bd4dc53a90559b7b40a41bfbcab35ad31f96057f7d0121fb15a37194422`) is the special case where S is the order-10 multiplication table, which already fails at the Tuscan-1 level.

## 2. Tuscan-1 structure

Let Z0, Z1, I be the rows with z first, last, interior. Every non-z arc of S is covered by its own row unless it is a split arc, and rows cover 10-|Z0| distinct arcs into z and 10-|Z1| out of z. Hence, if the eleven rows are Tuscan-1:

1. |Z0|<=1, |Z1|<=1, |Z0|+|Z1|>=1, and E minus z consists exactly of the |I| split arcs, one from each row of I, forming one Hamilton path of V (|I|=9) or two paths covering V (|I|=8).
2. If Z0={r0} and Z1 is empty, E=(e_1,...,e_10,z) and row r0 of S starts with e_1. If Z1={r1} and Z0 is empty, E=(z,e_1,...,e_10) and row r1 of S ends with e_10. If both, E=(x_0,...,z,...,x_10), row r0 of S starts with x_0 and row r1 ends with x_10. (Distinctness of the ten arcs out of, respectively into, z.)

## 3. The Tuscan-2 condition

**Theorem.** If the eleven rows form a Tuscan-2 square, then no split arc (s,s') is a distance-2 pair of S; i.e. every split arc lies in M_S, the set of ordered pairs never two apart in a row of S.

Proof. In the row with split arc (s,s') the triple s,z,s' is interior, so (s,s') is a distance-2 event with middle z. Suppose S has a triple s,m,s' in some row r'. It stays an interior triple of the extended row r' unless z is inserted into its arc (s,m) or (m,s'), i.e. unless one of these is the split arc of r'. Split arcs are arcs of E, and E's only arc leaving s and only arc entering s' are both (s,s'); so (s,m) or (m,s') in E would force m=s' or m=s. Hence the occurrence with middle m survives and (s,s') occurs twice. QED.

**Corollaries.**

- If S is Tuscan-2(10), then |M_S|=10 with out-degree c_8(a) and in-degree c_1(a) (columns 0..9; the identity of v24 §7.3 at order 10), and M_S must contain the 8 or 9 rainbow split arcs covering V by one or two paths.
- If S is moreover Latin (every column a permutation), M_S is a permutation digraph (in- and out-degree 1), so it must be a single directed 10-cycle when |I|=9, and a 10-cycle or a union of two cycles when |I|=8.
- For the order-10 multiplication table mod 11 (rows r·(1,...,10)), M_S={(x,-x)} is five 2-cycles; two paths covering V would have at most two arcs, so no insertion extension is Tuscan-2 (it already fails Tuscan-1 by v24 Lemma 6.4).

## 4. Status and nonclaims

This is a necessary condition and a reduction for one classical extension family; general Tuscan-1(10) or Tuscan-2(10) bases satisfying it were neither constructed nor excluded. No Tuscan-2(11) table and no all-array obstruction is supplied. Original target, HOLD, cutoff/deadline and all process histories, including the checkpoint045 withdrawal, are unchanged. This candidate needs its own complete source-bound gate.
