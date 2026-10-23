# GPS written-spec addendum v1 (PA(19,8,6) lane info-1)

Written after host clock read 2026-10-18T14:26:18-0700. This document is new; it edits no earlier file.

It answers the Codex written review `review/pa19-gps-written-v1-codex-v1.note.md` (SHA-256 `e15d2a6466617024a637c9fb1dbc05c1b5d4f20b017c11ca01450b5e1f1169db`): one MAJOR and two MINOR.

For written-lemma purposes it supersedes three things:
- the ms09 "Feasible iff" sentence of README Amendment GPS-1|C1 (README line 1046);
- the "valid first column" wording (README lines 1049 and 1054, and the probe names `check_placement` and C6);
- the implicit orbit argument (README lines 1048 and 1070).

The old README text, the frozen sources (`src/gps_probe_v1.py` 46b32d23…f2bc, `src/gps1c1_probe_v1.py` 8e9eaa0a…c52c, `src/gps2c1_ms06_probe_v1.py` 5029848a…2d12) and all receipts are unchanged.

## 0. Premises

- **Array:** 19 distinct rows; c0 P0 columns with block sizes (4,3,3,3,3,3); m P1 columns with block sizes (4,4,3,3,3,2).
- **Validity:** any two rows agree in at most one column.
- **Quad sets:** T(r) is the set of P0 columns in which row r lies in the size-4 block, as recorded by the skeleton; t(r) = |T(r)|.
- **Leave count:** P0 and P1 columns cover 21 and 22 agreeing row pairs respectively, so L = 171 - (21 c0 + 22 m) = 3 - m pairs agree nowhere.
  - ms09: c0 = 5, m = 3, L = 0.
  - ms06: c0 = 6, m = 2, L = 1, and sum_r l(r) = 2L = 2.
- **Block values:** in P1 column j, e_j(r) = (size of r's block) - 3, which lies in {+1, 0, -1}. e_j(r) = -1 holds exactly when r is in that column's size-2 block.
- **Row identity (GPS (1)):** 18 - l(r) = 16 + t(r) + sum_j e_j(r).

## 1. First-column data are a compatible PARTIAL 4/4/2 placement (MINOR 1)

- Each list entry (A1, B1, P1) is a compatible partial 4/4/2 placement of the first P1 column, not a full first column:
  - the three sets are pairwise disjoint, with sizes 4, 4 and 2;
  - within each set, T-sets are pairwise disjoint.
- It determines e1: +1 on A1 and B1, -1 on P1, 0 on the remaining nine rows.
- Those nine rows lie in the column's three triples, which the placement leaves UNSPECIFIED. e1 = 0 (code: `bid = -1`) does NOT mean two such rows share a block.
- The known first-column agreement relation is F1 = {pairs inside A1} ∪ {pairs inside B1} ∪ {P1}. Only pairs in F1 are treated as already agreeing in column 1.
- Ignoring the unknown triples weakens every test below (it can pass placements that the triples would rule out), but it never invalidates necessity.

## 2. ms09 conditioned relaxation, quantified (MAJOR)

Fix a partial placement (A1, B1, P1) and put s(r) = 2 - t(r) - e1(r). Then

    sum_r s(r) = 38 - sum_r t(r) - sum_r e1(r) = 38 - 20 - (8 - 2) = 12,

since there are five quads of size 4 and e1 has eight +1 and two -1 entries.

**Compatible pair.** A row pair {u, v} with T(u) ∩ T(v) = ∅ and {u, v} ∉ F1.

**Relaxation R09.** A choice of distinct compatible pairs P2 ≠ P3, and of values (e2(r), e3(r)) for every row, obeying:

| s(r) | membership in P2, P3 | (e2, e3) |
|---|---|---|
| 2 | in neither | (+1, +1) |
| 1 | in neither | (+1, 0) or (0, +1) |
| 0 | in neither | (0, 0) |
| 0 | exactly one, P_i | -1 in column i, +1 in the other column |
| -1 | exactly one, P_i | -1 in column i, 0 in the other column |
| -2 | both | (-1, -1) |

with exactly 8 entries equal to +1 in column 2 and exactly 8 in column 3. No row with |s(r)| > 2 admits a value.

Write a = #{r : s(r) = 2}, b = #{r : s(r) = 1}, and, for i ∈ {2, 3}, y_i = #{r : s(r) = 0 and r ∈ P_i \ P_(5-i)}, where P_(5-i) is the other pair.

**Lemma A (count reduction).** For fixed distinct compatible P2, P3 satisfying the membership column of the table, the values of R09 exist iff some integer x ∈ [0, b] satisfies

    (C2)  a + y3 + x = 8   and   (C3)  a + y2 + (b - x) = 8.

*Proof.*
- The table fixes every value except which s = 1 rows take +1 in column 2. Let x be their number.
- Column 2 then has +1 exactly at: the a rows with s = 2; the y3 rows with s = 0 lying in P3 only (they have -1 in column 3 and therefore +1 in column 2); and those x rows.
- Rows with s ∈ {-1, -2}, and s = 0 rows in neither pair, contribute no +1. This gives (C2).
- Column 3 is symmetric, with the remaining b - x rows, which gives (C3). ∎

**Lemma B (when C3 is automatic).**
- Every table row has e2 + e3 = s(r).
- The -1 entries are exactly the four memberships of the two size-2 blocks P2 and P3; an s = -2 row counts twice.
- Hence #(+1 entries in columns 2 and 3) = sum_r s(r) + 4 = 16, that is, 2a + b + y2 + y3 = 16.
- So (C2) and (C3) sum to an identity, and either implies the other.
- This uses only sum s = 12, which comes from the profiles and the 4/4/2 sizes of the placement, together with exactly four negative memberships. It is not a general identity. ∎

**Theorem (necessity).**
- Suppose a valid array of the ms09 case has a first column that extends the partial placement (A1, B1, P1), meaning its two 4-blocks are A1 and B1 and its pair is P1.
- Then its actual pair blocks P2 and P3 of the remaining P1 columns, its actual values, and x = #{r : s(r) = 1, e2(r) = +1} satisfy R09 and (C2) together with (C3).

*Proof.*
- **Row values.** The row identity with l = 0 gives e2 + e3 = s. The listed (e2, e3) are all the pairs in {-1, 0, 1}² with that sum, with e_j = -1 exactly when the row is in P_j.
- **Distinct pairs.** P2 ≠ P3, since a repeated pair would agree twice.
- **Compatible pairs.** Each P_j is compatible: its two rows agree in column j, so they share no P0 quad and no known column-1 block.
- **Counts.** Each column has exactly eight +1 entries, from its two 4-blocks.
- Lemma A then gives x. ∎

**Scope of "iff".**
- Lemma A states an equivalence between R09-value existence and (C2)/(C3), for given P2 and P3.
- R09 itself is a necessary RELAXATION. Passing it never implies completion to a packing array, and failing it for every (P2, P3) excludes the placement.

**Implementation correspondence (aid only, not a premise).**
- `c1_L0` searches distinct compatible pairs and enforces the membership rules through the bounds max(0, -s) ≤ n2' ≤ floor((2 - s)/2), the condition "rows in both pairs = exactly the s = -2 rows", and (C2) as 0 ≤ 8 - a - y3 ≤ b. It relies on Lemma B for (C3).
- `verify_L0` checks both equations explicitly.

## 3. ms06 (accepted by the review; restated only for completeness)

- For each candidate leave pair {x, y}, compatible in the sense of §2, subtract 1 at EACH endpoint. This gives e2 = 2 - l - t - e1, forced.
- Necessary conditions:
  - all e2 ∈ {-1, 0, 1};
  - exactly eight +1 and two -1 entries, hence nine 0 entries;
  - the two -1 rows form a compatible pair different from {x, y}.
- GPS-2|C1 adds the block partition: the +1 rows split into two 4-blocks, the 0 rows into three triples, and the -1 rows form the pair.
  - Within every block, rows are pairwise T-disjoint and no pair of them lies in F1.
  - No block contains BOTH leave endpoints; containing one endpoint is allowed.

## 4. Symmetry transport (MINOR 2)

**Transported action.** Let σ be a permutation of the rows and π a permutation of the P0 quads with

    T(σ(r)) = π(T(r))   for every row r.

This includes permutations of rows with identical T, where π = id.

Apply σ to A1, B1, P1, to the candidate pairs P2, P3, to the leave pair, and to every partition block. Then:
- t(σ r) = t(r);
- e1, l and s are carried along: the transported placement has e1'(σ r) = e1(r), and likewise for l and s;
- set sizes are preserved;
- T-disjointness is preserved, because T(σa) ∩ T(σb) = π(T(a) ∩ T(b));
- σ(F1) is the known first-column agreement relation of the transported placement.

**Consequences.**
- A solution of R09, (C2)/(C3), the ms06 conditions or GPS-2 for (A1, B1, P1) maps to one for (σA1, σB1, σP1).
- The inverse pair (σ⁻¹, π⁻¹) gives the converse, so success and failure are invariant under every such (σ, π).
- Swapping A1 and B1 changes neither e1 nor F1.
- For ms09, exchanging the two remaining P1 columns sends (P2, P3, x) to (P3, P2, b - x) and preserves (C2)/(C3).

**What is not assumed.**
- No arbitrary skeleton permutation is assumed. Only pairs (σ, π) satisfying the displayed relation are covered.
- No change of the distinguished first column is assumed.
- Whether the frozen extend_b orbit representatives were formed under exactly such transported actions is part of the unverified list-coverage premise, not claimed here.

## 5. Not claimed

- No pruning count, list completeness, list coverage, automorphism datum, probe exhaustiveness or runtime control is established by this addendum.
- The same-lane cross-check (`cycle2/gps-crosscheck-20261018T141846.json`) is auxiliary code, not independent acceptance.
- No re-batching, code change, new list or native work follows.
- The 151 lane-original open M2 cases remain open.
