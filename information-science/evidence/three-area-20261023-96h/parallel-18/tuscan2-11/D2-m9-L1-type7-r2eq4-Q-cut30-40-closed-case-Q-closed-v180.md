# Original Tuscan-2(11), entire m = 9 distance-two branch, part 67: L1 type 7 with r2 = 4 — case (Q), cuts at 30 and 40, closed; case (Q) closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type7-r2eq4-Q-cut20-50-closed-v179.md` (SHA256 `432c612df1c416a65ff411a42731aaa16d8e10405c73e8aba3408d3c73d7f228`). Operative imports:
- v178 §3, the case list (SHA256 `a41c8e7f0fe6593befd2d88d87b3da3ea56ca4ff5196d6681f134f5896e70c78`);
- v173 §1, the F1/F2 position formulas (SHA256 `0f399e93d91f26c7f5b0e7e9d8614601e84668f0b053360151e6a95f59ab93d8`);
- v152 §2 (K-w): with G3 = ∅, r2 = 4 and β2 = 1, all three W's of w are G2-W's (SHA256 `62e80ecc4878699ad5edd15e9198a0f474eb8c9490c9e870a6dbfe611ee2a18f`);
- v176 §1, Lemma A4 and exactness (E) (SHA256 `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021`);
- the type-7 mirror of v155 §5, exchanging t1 and t3.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. All variables of the named case remain free until the deductions below.

## 1. The case

Take case (Q) of v178 with v's cut at P2 = 30. Then n1 = n3 = 1 and n2 = nΛ = c′ = 0. v's F1 passages are t in R0, t1V in R1, P2 = 30, P3 in R4, t3V in R5 and P5 in R6. Hence:
- ℓ1 = P2 − 15 = 15 and P1 = 10 − u + ℓ1 = 25 − u;
- u ≥ 4 by Lemma A4;
- P3 ∈ [41,49], ℓ2 = u + 5 and P4 = P3 + u + 5.

## 2. u ≥ 5 is impossible

**u = 5.** Then P1 = 20, so b3 (label w) sits on a cut. But w's only cut is ℓ.

**u ≥ 6.** Then P1 ≤ 19. The S_12-run of t2 occupies positions P1 + 1..29, with t2[j] at 30 − j for j = 1..u + 4. Since 26 − u ≤ 20, the row R2 = [20,30] consists of t2[10], …, t2[1] and b6.

R2 contains every label, so w lies on one of t2[1..10]. By (K-w), however, all three W's of w are G2-W's (on t1, t3 or Λ), and neither ℓ nor b3 is an interior vertex of t2. So w has no t2-vertex. Contradiction.

## 3. u = 4

**F1 data.** t1[j] lies at 6 + j, so R1 = t1[4..14] is a pure t1-row: t1[14] = t1[ℓ1 − 1] is at the cut 20, and b3 is at P1 = 21. Also ℓ2 = 9 and P4 = P3 + 9 ∈ [50,58]. P4 = 50 would put b3 on a cut, so P3 ≥ 42. Hence ℓ3 = 55 − P3 ≤ 13 and λ = 40 − ℓ1 − ℓ3 = 25 − ℓ3 ≥ 12.

**F2 data.** The F2 offsets are:
- b6 at 0 and at λ;
- Λ[k] at k;
- t3[j] at λ + j;
- b3 at λ + ℓ3 = 25;
- t1[j] at 40 − j, so t1 occupies offsets 26..39 and R1 occupies offsets 26..36.

v has no F2-cut, so its four F2 passages b6(0), b6(λ), t3V and t1V lie in four distinct rows, one in each. Λ carries no v-vertex (nΛ = 0), so b6(0) and b6(λ) are consecutive v-passages and lie in consecutive rows:
- A = [−x, 10 − x];
- D = [10 − x, 20 − x];

where 1 ≤ x ≤ 9 and 10 − x < λ < 20 − x. Since λ ≥ 12, this forces **x ≤ 7**. The fourth row, which precedes A, is C = [30 − x, 40 − x].

**R1 against C.** Both rows contain every label once, so after removing their common vertices, the two remaining paths have equal label sets.

- **x ∈ {1, 2, 3}.** Here C ⊆ offsets 27..39, so C = t1[x..x + 10]. Its common part with R1 is t1[4..x + 10]. The differences are t1[x + 11..14] and t1[x..3], each with 4 − x vertices.
  - x = 3: L(t1[14]) = L(t1[3]). But t1[14] is at the F1-cut 20, and t1[3] is at C's endpoint offset 37, which is an F2-cut. One label would have two cuts.
  - x = 2: the edges t1[13]t1[14] and t1[2]t1[3] carry the same label pair, against (E).
  - x = 1: two disjoint three-vertex paths carry the same three labels, so four edges fall on three label pairs, against (E).
- **x = 4.** C occupies offsets 26..36, the same vertices as R1. So t1[4], with label c1 and F1-cut at 10, lies at C's endpoint offset 36, an F2-cut. Two cuts.
- **x ∈ {5, 6, 7}.** Here C contains t1[x..14] (offsets 26..40 − x), then b3 at offset 25, then t3 at offsets 30 − x..24. Its common part with R1 is t1[x..14]. The differences are t1[4..x − 1] and the part of C at offsets 30 − x..25, each with x − 4 vertices.
  - x = 5: that part of C is b3 alone, at C's endpoint offset 25, which is an F2-cut. So w would have two cuts.
  - x = 6: the edges t1[4]t1[5] and t3[ℓ3 − 1]b3 (offsets 24, 25) carry the same label pair, against (E).
  - x = 7: two disjoint three-vertex paths, t1[4..6] and t3[ℓ3 − 2], t3[ℓ3 − 1], b3, carry the same three labels, against (E).

Every x ∈ [1,7] is impossible, so case (Q) with the cut at 30 is impossible.

## 4. Mirror and the whole of case (Q)

The type-7 mirror (row reversal, t1 ↔ t3, P2 ↔ P3) maps the cut at 30 to the cut at 40. So case (Q) with the cut at 40 is impossible as well. Together with v179, which handles the cuts at 20 and 50, **all of case (Q) of v178 is impossible.**

## 5. Result

**WRITTEN:** In type 7 with r2 = 4, case (Q) of v178 is impossible for every allowed value of every variable.

**OPEN (m = 9, L1):**
- type 7 with r2 = 4: case (P) of v178 (c′ = 1, n1 = 1) and its mirror (n3 = 1);
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4, 5, 6};
- type 8 with r1 ∈ {3, 4}, and with r1 = 5 and ℓ1 − u ∈ [11, 19].

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
