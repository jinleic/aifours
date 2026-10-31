# Actual Tuscan11 distinct 3+5, disconnected, Type II with r_P = 3, survivor S1 — reduction to two rigid shapes by Lemma L

Actual `/bin/date` before this body: **Mon Oct 26 12:07:52 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case reduction, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting and imports

**Imports:**
- the Type II, r_P = 3 frame of v76 §4(a) (SHA256 `a2218f8fb409011ea8d0279d2b75ec3a8066af584afde61bc0dcfdbb8bf1b9a8`);
- v77 §5 (SHA256 `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`);
- v78 §3 (SHA256 `e6d1e18d5b7166266e92ff2fe5c25e4b99162646dcf0de8228c87a9d24cd1bfd`), which defines S1;
- Lemma L of v81 (SHA256 `fc30690676d04cf019258f3cdeee853fd8e03813dd19f9f45eb431e72d27df08`). For Type II with r_P = 3 it says: each 𝒫 label has two vertices on A ∪ B and two on C ∪ D; each 𝒪 label has three on A ∪ B and one on C ∪ D;
- Lemma W.

By v60 §2 (SHA256 `d09ec901a98a25480d12b9c81622c43044f5c2415b196fb9d64bb71ae9ad6259`), C ∪ D carries one v-copy and no w-copy.

**S1** is the case (n_A^w, n_B^w) = (0,2) with 10 < K < 15, two P-boundaries on B, and β_P = 6+t−K. As in v77 §5, K > t, since K < t is excluded there. O's rows are:
- Q_a = A[K−10..x−1], w, D[1..σ];
- Q_b = D[σ..t−1], w, B[y−1..ρ];
- N1 = B[ρ..ρ−10], inside B;
- N2 = B[ρ−10..1], v, C[1..K−t];
- Q_c = C[K−t..c−1], w, D[t−1..τ];
- Q_d = D[τ..1], w, C[c−1..1], v, A[1..K−10].

Here ρ = 20+t−K = β_P+14 and τ = 5+t−K.

P's rows are:
- R_P1 = A[10−β_P..1], v, B[1..β_P];
- R_Pmid = B[β_P..β_P+10];
- R_P* = B[β_P+10..y−1], w, A[x−1..10−β_P].

The self-dual v-copy lies on D at some u > τ. On C, its backward visit would fall in Q_d, which already holds b_v. On D, u < τ would put its backward visit in Q_d.

## 2. Where the 𝒫 labels sit on C ∪ D

Split C ∪ D into blocks:
- C[1..K−t−1], covered by N2 and Q_d;
- the O-cut C[K−t];
- C[K−t+1..c−1], covered by Q_c and Q_d;
- D[1..τ−1], covered by Q_d;
- the O-cut D[τ];
- D[τ+1..t−1], covered by Q_c.

A 𝒫 label p has two C∪D vertices.
- They cannot both lie in Q_d's range C ∪ D[1..τ], nor both in Q_c's range C[K−t..c−1] ∪ D[τ..t−1].
- So p has one **hi** vertex in D(τ, t−1] and one **lo** vertex in C[1..K−t) ∪ D[1..τ).

The lo block has (K−t−1) + (τ−1) = 3 vertices, so **it consists exactly of the three lo vertices**. Every other vertex of C ∪ D other than u carries an 𝒪 label; in particular C[K−t..c−1] and D[τ] do. Q_d meets each 𝒫 label at its lo vertex, so **Q_d's A-part A[1..K−10] carries no 𝒫 label**.

## 3. Where the 𝒫 labels sit on A ∪ B

𝒫 = {pB1, pB2, pA}, where pB1 = ℓ(B[β_P]), pB2 = ℓ(B[β_P+10]) and pA = ℓ(A[10−β_P]). Each has its cut plus exactly one more A∪B vertex. N1 and R_Pmid lie inside B and overlap with offset 4.
- **pA:** its second vertex lies on B, in (β_P+4, β_P+10).
- **pB1:** its second vertex lies in (β_P+10, β_P+14).
- **pB2:** its second vertex avoids N1 and R_Pmid. R_P1 must contain pB2, so the second vertex lies in B[1..β_P) or A(K−10, 10−β_P).

**N2 must contain every 𝒫 label once:**
- pB1 is at B[β_P], so pB1's lo vertex lies on D.
- pA is neither on N2's B-part nor on A in N2, so pA's lo vertex lies on C.
- pB2's lo vertex lies on D if its second vertex is on B, and on C if its second vertex is on A.

Counting the lo block (K−t−1 vertices on C, τ−1 on D) gives exactly two shapes:
- **(α)** pB2's second vertex is on B. Then K = t+2, τ = 3, β_P = 4, ρ = 18, and t ∈ {9, 10, 11, 12}.
- **(β)** pB2's second vertex is on A. Then K = t+3, τ = 2, β_P = 3, ρ = 17, and t ∈ {8, 9, 10, 11}.

## 4. Further forced structure (both shapes)

**Q_a and Q_b.** Q_a and Q_b each contain each 𝒫 label once, so all three hi vertices exceed σ. Two facts force this:
- pB1's lo and hi both lie on D.
- pA's cut A[10−β_P] lies in Q_a.

Also σ > τ. The D-lemma of v77 §4 then gives σ + τ ≤ t.

**Exchanges.**
- R_Pmid against N1 gives L(B[β_P..β_P+3]) = L(B[β_P+11..β_P+14]): complementary P4s headed by pB1.
- Q_c against Q_d gives L(D[τ+1..t−1]) = (lo labels) ⊔ {v} ⊔ L(A[1..K−10]).

**Shape (α).** B[1..3] carries pB2, the second B w-copy and one 𝒪 label. B[5..8] carries 𝒪 labels. B[9..13] carries:
- v and w, the copies of N1;
- pA;
- the two remaining 𝒪 labels, namely ℓ(B[1..3] ∖ {pB2, w}) and ℓ(C2).

Shape (β) has the analogous layout, with B[4..7] carrying 𝒪 labels.

## 5. Status

**WRITTEN.** S1 reduces to the two rigid shapes (α) and (β) above; its (2,0) mirror reduces in the same way. Label-set bookkeeping in both shapes finds no contradiction yet. Closing S1 needs order-level reasoning: pair uniqueness, (N), and Lemma U on the explicit P4s.

The residual is otherwise unchanged from manifest v16-delta (SHA256 `d53ba4ae3b1d0b37cca6daa1a0e0525f8163b9abd4b5530af8adeb8937389ef4`).

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
