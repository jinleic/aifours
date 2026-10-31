# Original Tuscan-2(11), entire m = 9 distance-two branch, part 39: L1 — face-group anatomy of the ten open types, and counting constraints

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-branch-consolidated-status-L2-closed-exact-L1-gap-v151.md` (SHA256 `07df7c7bb200e66541cb4d5ffeaae0a2f206d0a712d1743054c3aa67356313ff`) and builds on v117 (L1 types, segments, (L-a)–(L-e)).

This is written reasoning only. No interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Face groups

**The groups.** In each L1 type the two faces F1 (which contains S_T) and F2 split the five elements T, t1, t2, t3 and Λ into three groups:
- **G1**: two F1-passages and no F2-passage;
- **G2**: one passage in each face;
- **G3**: two F2-passages and no F1-passage.

**Row counts.** F1 has r1 rows and F2 has r2 rows, with r1 + r2 = 11. Here c = 1 if v's cut lies in F1, c′ = 1 if it lies in F2, and c + c′ = 1. The row counts are read off v117 §2.

| Type | h1, h5 | G1 | G2 | G3 | r1 | r2 |
|---|---|---|---|---|---|---|
| 1 | Λ+, t3 | T | Λ, t2, t3 | t1 | 3+nΛ+n2+n3+c | 3+2n1+n2+n3+nΛ+c′ |
| 2 | Λ+, t2 | T, t1, Λ | t2, t3 | – | 5+2n1+2nΛ+n2+n3+c | 1+n2+n3+c′ |
| 3 | Λ+, t3 | T, t3 | Λ, t1, t2 | – | 4+nΛ+n1+n2+2n3+c | 2+n1+n2+nΛ+c′ |
| 4 | Λ+, t2 | T, Λ, t2 | t1, t3 | – | 5+2nΛ+2n2+n1+n3+c | 1+n1+n3+c′ |
| 7 | t1, t3 | T, t2 | t1, t3, Λ | – | 4+n1+2n2+n3+nΛ+c | 2+n1+n3+nΛ+c′ |
| 8 | t1, t2 | T | t1, t2 | t3, Λ | 2+n1+n2+c | 4+n1+n2+2n3+2nΛ+c′ |
| 9 | t1, Λ− | T, t1 | t2, t3, Λ | – | 4+2n1+n2+n3+nΛ+c | 2+n2+n3+nΛ+c′ |
| 10 | t1, Λ− | T, t1, Λ | t2, t3 | – | 5+2n1+2nΛ+n2+n3+c | 1+n2+n3+c′ |
| 11 | t1, Λ− | T | t1, t2, Λ | t3 | 3+n1+n2+nΛ+c | 3+n1+n2+2n3+nΛ+c′ |
| 12 | t1, Λ− | T, t2, Λ | t1, t3 | – | 5+2n2+2nΛ+n1+n3+c | 1+n1+n3+c′ |

**Anatomy.** Take a label other than v and w, with a G1-, b G2- and c3 G3-vertices (a + b + c3 = 5). It has 2a + b F1-passages and b + 2·c3 F2-passages. An F1-cut label has r1 − 1 F1-passages and r2 F2-passages; an F2-cut label has r1 and r2 − 1. So:
- **Types with G3 = ∅:**
  - an F1-cut label has a = 5 − r2 and b = r2;
  - an F2-cut label has a = 6 − r2 and b = r2 − 1.
- **Types 1, 8, 11 (G1 = {T}):**
  - T_int-labels have a = 1, and S-labels have a = 0;
  - an F1-cut S-label has b = r1 − 1 and c3 = 6 − r1;
  - an F2-cut S-label has b = r1 and c3 = 5 − r1;
  - an F1-cut T_int-label has b = r1 − 3 and c3 = 7 − r1;
  - an F2-cut T_int-label has b = r1 − 2 and c3 = 6 − r1.

## 2. Counting constraints

**(K-w) The W-count.** w consists of ℓ (its F1-cut), b3 with β1 corners in F1 and β2 in F2, and three W's. W's lie on threads or on Λ, never on T. Counting w's passages face by face gives:
- **If G3 = ∅:** the number of G2-W's is r2 − β2 ∈ [0, 3]. Every G3 = ∅ type has β2 = 1 (one b3-corner in F2), so **r2 ≤ 4**.
- **Types 1, 8, 11:** β1 = 1 and β2 = 2, so the number of G2-W's is r1 − 3 and the number of G3-W's is 6 − r1. Hence **3 ≤ r1 ≤ 6**.

**(K-S) The arm count.** S-labels carry an h1-arm vertex and an h5-arm vertex, so a ≥ [h1 ∈ G1] + [h5 ∈ G1]. The label c1 = L(h1[u]) is an F1-cut S-label. Hence:
- **Types 4 and 10** (both arms in G1): 5 − r2 ≥ 2, so **r2 ≤ 3**. When r2 = 3, each F1-cut S-label has exactly its two arm vertices as G1-vertices.
- **Types 1, 8, 11** (both arms in G2): c1 needs c3 = 6 − r1 ≥ 0, so r1 ≤ 6. This agrees with (K-w).
- **Type 4, case r2 = 4** (n1 + n3 = 2 and v's cut in F2): excluded by (K-S).
- **Type 10, case r2 = 4** (n2 + n3 = 2 and v's cut in F2): excluded by (K-S).

**(K-r) Row floor.** In type 8, r1 = 2 is impossible: R_out and R_in would share both cuts, forcing t1[u] = t2[u] = b3, so w would carry two cuts. So n1 + n2 + c ≥ 1.

## 3. Result

**WRITTEN:**
- the face-group table and the anatomy formulas of §1;
- the constraints (K-w), (K-S) and (K-r).

**Small exclusions:**
- type 4 with r2 = 4;
- type 10 with r2 = 4;
- type 8 with r1 = 2;
- r2 = 5 in types 3, 7 and 9 (r2 ≤ 4 by (K-w)).

**OPEN:** L1 types 1–4 and 7–12, with these restrictions. The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
