# Triple-layer note v4: two-quad pigeonhole lemma Q2P (written research only)

New file, written after host clock read 2026-10-18T14:5x-0700. v1 (4a68eeef…27bc), v2 (cd4cac0d…4f4e) and v3 (48b0c495…871c) are unchanged. No probe, list or native work. Hypotheses and notation as in v1 §0; for every row, tT(r) = 6 + l(r) - 2 n2(r) (row identity).

## Lemma Q2P

Fix a P1 column j with 4-blocks A, B, and put S = A ∪ B (8 rows). Let:
- T_out be the number of size-3 blocks (triples) in the other 7 columns;
- q be the number of the 16 cross pairs {a in A, b in B} lying in a size-4 or size-2 block of another column;
- ℓ = 1 if the leave pair is such a cross pair, else 0.

Then

    16 - (Σ_{r in S} tT(r))/2  <=  q + ℓ  <=  T_out + 16 - Σ_{r in S} tT(r).

**Proof.**
1. **No triple of column j meets S.** Each r in S lies in tT(r) triples, all outside column j, because r is in a 4-block of column j.
2. **Each outside triple holds at most two rows of S.** A triple of another column contains at most one row of A and at most one of B, since two rows of A already agree in column j, and likewise for B.
3. **Two counts.** Let x2 be the number of triples meeting both A and B, and x1 the number meeting S in exactly one row. Then x1 + 2 x2 = Σ_S tT.
4. **x2 equals the triple-covered cross pairs.** Each cross pair agrees exactly once if it is not the leave pair, and never if it is. That agreement is in a column other than j, because A and B are distinct blocks of column j. A triple meeting both A and B covers exactly one cross pair, and distinct triples cover distinct pairs, since two rows agree at most once. So x2 = 16 - q - ℓ.
5. **Bounds.** x1 >= 0 gives the left inequality. x1 + x2 <= T_out gives the right one. ∎

## Specializations

- **ms09** (T_out = 34 - 3 = 31, ℓ = 0, Σ_S tT = 48 - 2 N2(S)): q <= 2 N2(S) - 1. Here N2(S) counts only endpoints of the two OTHER pair blocks, so N2(S) <= 4. Hence:
  - (a) N2(A_j ∪ B_j) >= 1 for EVERY P1 column j: each column's two quads contain an endpoint of another column's pair block.
  - (b) q_j >= |T(A_j) ∩ T(B_j)| (one cross pair per P0 quad meeting both A_j and B_j) >= Σ_{r in S} t(r) - 5. So, for every P1 column j:

        Σ_{r in A_j ∪ B_j} (t(r) - 2 n2(r)) <= 4.

  - (c) Summing (b) over j, with each row in n4'(r) = 2 + n2 - t P1 4-blocks: Σ_r (t - 2 n2)(2 + n2 - t) <= 12. Using the GPS-1 bounds on (t, n2), this is

        h(1,0) - 2 h(1,1) - h(3,2) <= 12,

    where h(t, n2) counts rows of that type. This is a skeleton-plus-pair-structure condition. It is weak by itself: it only forces t = 1 pair endpoints when more than 12 rows have t = 1.
- **ms06** (T_out = 36 - 3 = 33, Σ_S tT = 48 + Lv(S) - 2 N2(S)): q + ℓ <= 1 + 2 N2(S) - Lv(S). Here N2(S) <= 2 (the other column's pair) and Lv(S) is the number of leave endpoints in S. Hence Σ_{r in A_j ∪ B_j} (t - 2 n2 + l) <= 7 - ℓ_j.

## Tightness check on the known (13,5,4) L = 0 model (by hand; aid, not premise)

Model file `controls/c13skel/models/ms07_s00001.txt`, SHA-256 e58cbbe0ae0804143f421dec4075c394a49898146beb8cc5d24d1bbf4d1d6016. For this model T_out = 8 and tT = 3 - 2 n2, so Q2P reads 4 + N2 <= q <= 2 N2. That forces N2 = 4 and q = 8 in EVERY P1 column of any such array, with all 8 outside triples meeting A ∪ B twice.

Read from the file for its column 2:
- blocks: A = {1,4,10,12}, B = {2,6,8,9}, pair {3,5}, triple {0,7,11};
- the other pairs {2,4} and {1,6} both lie in A ∪ B, so N2 = 4;
- the 8 cross pairs covered by quads or pairs are (1,2), (4,6), (1,8), (10,6), (12,2), (4,9), (2,4), (1,6);
- each of the 8 outside triples {4,7,8}, {5,9,10}, {6,11,12}, {1,7,9}, {2,10,11}, {3,8,12}, {0,9,12}, {0,8,10} meets A ∪ B in exactly 2 rows.

So Q2P holds with equality on a real array.

## Use and status

- **Conditioned forms**, definitions only, for a possible future probe; untested and not authorized.
  - With a first-column placement (A1, B1, P1) and chosen (P2, P3), (a) and (b) become exact checks on column 1: |T(A1) ∩ T(B1)| plus the number of P2/P3 that are A1-B1 cross pairs must be <= 2 N2(A1 ∪ B1) - 1.
  - For the remaining columns, the summed form (b) applies to the forced +1 sets.
  - For ms06, with GPS-2's full second column, q_1 and q_2 become fully computable.
- **Status.** Q2P is rigorous, uses the triple layer (triple incidences against the triples available outside one column), and is tight on the real (13,5,4) model.
- It has not been evaluated on any configuration, its pruning strength is unknown, and it gives no uniform obstruction.
- The 151 lane-original open M2 cases remain open.
