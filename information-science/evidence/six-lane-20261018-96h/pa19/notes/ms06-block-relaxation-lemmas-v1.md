# ms06 block-level relaxation: standalone statements and proofs (v1)

Written after the `/bin/date` reading 2026-10-19T04:0x-0700 by ContinuePA19b. This is a written structural slice.

- **What it contains.** Exact definitions and complete proofs of the necessary conditions that `code/probe_ms06_gps2q2p_v1.py` checks. When frozen, that probe was compiled for syntax only and never run (89e85e32…eb13 at compile time).
- **What it claims.** Nothing about any case. Every case remains open until a candidate passes all three gates:
  1. exhaustive infeasibility of the relaxation, found by two independent implementations;
  2. this note's proofs, accepted on review;
  3. the parent's verdict.
- **Feasible cases.** For those, the relaxation says nothing about existence.

## 0. Setting

An ms06 skeleton case b (`cycle2/skel-b/skeletons-b-ms06.json`, 9ec0fd1d…0488) has:
- N = 19 rows and 8 columns over 6 symbols;
- P0 columns 0..5, each with profile (4,3,3,3,3,3);
- P1 columns 6 and 7, each with profile (4,4,3,3,3,2).

The skeleton fixes, for each P0 column c, its quad Q_c, the 4 rows carrying the column's 4-times symbol. Rows are numbered in `build_v2` member order.
- T(r) = {c : r ∈ Q_c} and t(r) = |T(r)|.
- Two rows are **T-disjoint** if T(r) ∩ T(s) = ∅.

A **valid array** for b is a 19×8 array with these profiles and quads in which any two rows agree in at most one column.

**Block view.** For each column, the blocks are its symbol classes; two rows agree in a column iff they share a block of that column.
- A P0 column has one quad and five triples.
- A P1 column has two quads, three triples and one pair block.

## 1. Validity facts

**V1.** Two distinct rows share a block in at most one column. (Definition.)

**V2.** Exactly one pair D shares no block, and every other pair shares exactly one block.

*Proof.* Summing C(|block|, 2) over all blocks gives 6·(6 + 5·3) + 2·(2·6 + 3·3 + 1) = 126 + 44 = 170 agreeing pairs, counted with multiplicity. By V1 the multiplicity is at most 1, and there are C(19,2) = 171 pairs. ∎

## 2. Lemmas

**Lemma 1 (T-disjointness).** Two rows sharing a P1 block or a P0 triple are T-disjoint.

*Proof.* If c ∈ T(r) ∩ T(s), then r and s already share the quad Q_c, so by V1 they cannot share another block. ∎

**Lemma 2 (row identity).** Fix a row r and put l(r) = [r ∈ D]. For a P1 column j let e_j(r) = |block_j(r)| − 3. Then

  t(r) + e_6(r) + e_7(r) = 2 − l(r).

Write n2 for the number of pair-block memberships of r, n4 for its P1-quad memberships, and n3 for its P1-triple memberships. Then n4 = 2 − l − t + n2 and n3 = 2 − n4 − n2.

*Proof.* By V1 and V2, r agrees with exactly 18 − l(r) rows, and each agreement uses a block of exactly one column. So Σ_c (|block_c(r)| − 1) = 18 − l(r). The left side is 3t + 2(6 − t) from the P0 columns plus 4 + e_6 + e_7 from the P1 columns. ∎

**Lemma 3 (GPS-1, accepted written necessity; recalled).**
- The pair blocks P6 and P7 are distinct and each is T-disjoint.
- D is T-disjoint and is neither P6 nor P7.
- Every row satisfies max(0, t + l − 2) ≤ n2 ≤ ⌊(t + l)/2⌋, using n4 ≥ 0 and n4 + n2 ≤ 2.

**Lemma 4 (forced block types).** Fix (P6, P7, D). Then n2 and l are known, and so is n4 (Lemma 2):
- a row with n4 = 2 lies in a quad of both P1 columns;
- a row with n4 = 0 lies in no P1 quad;
- a row with n4 = 1 lies in exactly one P1 quad: in a column-7 quad if it is in P6, in a column-6 quad if it is in P7, and otherwise in a quad of exactly one column with a triple of the other.

Each P1 column has exactly 8 quad rows, 2 pair rows and 9 triple rows. (Definitions plus Lemma 2.)

**Lemma 5 (cross-column and leave).**
- For any block X of column 6 and any block Y of column 7, |X ∩ Y| ≤ 1. (V1)
- D lies inside no block. (V2)
- Every P1 block is T-disjoint. (Lemma 1)

**Lemma 6 (Q2P for ms06).** Fix a P1 column j with quads A and B, and let k be the other P1 column, with quads A_k, B_k and pair P_k. Put S = A ∪ B. Define:
- q_k = #{(a, b) ∈ A × B : {a, b} ⊆ A_k, or {a, b} ⊆ B_k, or {a, b} = P_k};
- q = |T(A) ∩ T(B)| + q_k, where T(A) = ∪_{a∈A} T(a);
- ℓ = [D = {a, b} for some a ∈ A, b ∈ B].

Then

  q + ℓ ≤ 1 + 2|S ∩ P_k| − |S ∩ D|.

*Proof.*
- (a) Count triples. Every r ∈ S is in a column-j quad, so the triples (blocks of size 3) containing r all lie outside column j. Their number is τ(r) = (6 − t) + n3 = 6 + l − 2·n2, by Lemma 2. Since r ∉ P_j, n2(r) = [r ∈ P_k]. Hence Σ_S τ = 48 + |S∩D| − 2|S∩P_k|.
- (b) Each triple outside column j contains at most one row of A and at most one row of B, because two rows of A already share A in column j (V1).
- (c) Let x2 be the number of triples meeting both A and B, and x1 the number meeting S in exactly one row. Then x1 + 2·x2 = Σ_S τ.
- (d) Each of the 16 cross pairs {a, b} with a ∈ A, b ∈ B agrees exactly once, unless it is D, which never agrees (V2). The agreement is not in column j, so it lies in exactly one of these:
  - a P0 quad: Q_c holds ≤ 1 row of A and ≤ 1 of B (Lemma 1), so it holds a cross pair iff c ∈ T(A) ∩ T(B). That gives exactly |T(A) ∩ T(B)| cross pairs;
  - a column-k quad or the pair P_k: q_k cross pairs;
  - a triple: by (b), each triple meeting both A and B holds exactly one cross pair, and distinct triples hold distinct cross pairs (V1).

  Hence 16 = |T(A)∩T(B)| + q_k + x2 + ℓ, that is, x2 = 16 − q − ℓ.
- (e) There are 6·5 + 3 = 33 triples outside column j, so x1 + x2 ≤ 33. Then Σ_S τ − x2 ≤ 33. Substituting (a) and (d) gives the claim. ∎

**Lemma 7 (QPL, P0-column pigeonhole).** In the notation of Lemma 6, let x2_k be the number of column-k triples that meet both A and B. Then

  |T(A) ∪ T(B)| ≥ 2 + q_k + ℓ + x2_k.

*Proof.* Fix a P0 column c and put a_c = |A ∩ Q_c| and b_c = |B ∩ Q_c|; both lie in {0, 1} by Lemma 1.
- The 4 − a_c rows of A outside Q_c lie in distinct triples of column c (V1), and likewise the 4 − b_c rows of B.
- Column c has 5 triples, so at least 3 − a_c − b_c of them meet both A and B.

Sum over the six P0 columns and add column k. This gives x2 ≥ 18 − |T(A)| − |T(B)| + x2_k, where |T(A)| = Σ_A t because the rows of A are T-disjoint. Combine with x2 = 16 − |T(A)∩T(B)| − q_k − ℓ from Lemma 6(d). ∎

**Lemma 8 (LINK, local P0-triple structure).** Let G_res be the graph on the rows whose edges are the pairs other than D that lie in no P0 quad and in no P1 block. Then:
- (i) every row r has exactly 2(6 − t(r)) neighbours in G_res;
- (ii) these neighbours split into 6 − t(r) pairs {s, w}, each with {s, w} ∈ G_res. The pairs carry pairwise distinct P0 columns, with the pair {s, w} carrying a column c ∉ T(r) ∪ T(s) ∪ T(w).

*Proof.*
- **Edges are P0 triples.** By V2, every pair other than D shares exactly one block. So a G_res edge shares exactly one P0 triple, and every pair sharing a P0 triple is a G_res edge (V1).
- **Splitting the neighbours.** Row r lies in exactly one triple of each P0 column c ∉ T(r), which is 6 − t(r) triples. These triples pairwise share only r (V1). So the neighbours split into the 6 − t(r) pairs {s, w} formed by the other two members of each triple.
- **Each pair has the required column.** s and w share that triple, so {s, w} is a G_res edge, and its column c has c ∉ T(r) ∪ T(s) ∪ T(w). Distinct triples of r lie in distinct columns.

Part (i) follows by counting. ∎

## 3. Theorem (relaxation)

If case b has a valid array, then there exist all of the following:
- a GPS-1 key (D, P6, P7) (Lemma 3);
- quads and triples of both P1 columns, consistent with the forced block types (Lemma 4) and with Lemma 5;
- such that Lemmas 6 and 7 hold for both P1 columns, and Lemma 8 holds for every row.

**Why one assignment per unordered E suffices.** Exchanging columns 6 and 7 maps valid arrays to valid arrays, because the columns have the same profile, and maps the condition set onto itself. So it is enough to check one assignment (P6, P7) per unordered E.

**Corollary.** Suppose an exhaustive search over all keys and all P1 block structures finds none satisfying the theorem's conditions. Then case b has no valid array, and its lane-original M2 case closes structurally. This holds only after the three gates listed at the top: two independent exhaustive implementations, review of this note, and the parent's verdict.

## 4. Scope and status

- **What the relaxation leaves out.** It never constructs the P0 triples. They enter only through the counts in Lemmas 6 and 7 and the local structure in Lemma 8. Completing the P0 triples would be the full case problem, which is the M2 SAT instance.
- **Status.** Lemmas 6 and 7 are new written statements and need review. Lemma 6 is the ms06 specialization of Q2P in `cycle2/triple-layer-gram-note-v4.md`, and its proof is given here in full. Lemma 8 is also new.
- **Prior evidence on b68.** GPS-2|C1 left 1,443 of 10,459 b68 first-column placements feasible (`cycle2/gps2c1-ms06-probe-20261018T141048.json`, 12b4320e…). Block-level conditions without Lemmas 6–8 therefore did not eliminate b68.
- **Planned first use.** Run the probe only in a window with no PA native run, on the six known direct-timeout cases b68, b73, b74, b77, b151 and b162.
