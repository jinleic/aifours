# Actual Tuscan11 distinct 3+5, disconnected — a label-location lemma, and Type I with r_P = 4 excluded

Actual `/bin/date` before this body: **Mon Oct 26 11:50:33 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Setting and imports

The setting is the nine-row component H of a disconnected distinct 3+5 array, from v60 (SHA256 `d09ec901a98a25480d12b9c81622c43044f5c2415b196fb9d64bb71ae9ad6259`). That packet supplies:
- the Type I faces P = A D C^- and O = B D^- B^- C A^-;
- the copy counts;
- |B| = 45 − 10r_P.

Further imports:
- From v12 §5 (SHA256 `c2a9283d09b06781e0f1b76a42a0dcb700913dc87bddf69aabae78ff32caf6b2`), the identity d_H(x) = r_H − 1_(x∈C_H). The only odd split vertices are the branches at v and w and the two leaves of the reverse pair; all other split vertices have degree 2.
- From v76 (SHA256 `a2218f8fb409011ea8d0279d2b75ec3a8066af584afde61bc0dcfdbb8bf1b9a8`), Lemma W.
- From v77 (SHA256 `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`), Lemma U, the fact that every unordered label pair labels at most one support edge, and the Type I reversal symmetry. That symmetry reverses every row, swaps A ↔ C and reverses D; it is the analogue of v77 §3 and is used in v80 §4.
- (L1) of v57 (SHA256 `41ae55f5aeff940eadfcd9c947bd43ea7c323b9ef3cc3bf42eee56646d4eaa89`): no face has two consecutive rows inside one cross path.
- The exchange identity.

Write X9 for the nine labels other than v and w. Every x ∈ X9 has d_H(x) = 8, so it is cut exactly once in H. Hence X9 = 𝒫 ⊔ 𝒪, where:
- 𝒫 is the set of P-cut labels, with |𝒫| = r_P;
- 𝒪 is the set of O-cut labels, with |𝒪| = r_O.

**Offset lemma (rule (R) form).** Let rows R and R′ share a run M of consecutive vertices. Suppose R = S ∪ M and R′ = M ∪ S′, where S and S′ are disjoint runs of k vertices at opposite ends of M (each consecutive in its own row). Then L(S) = L(S′), and k ∉ {1, 2, 3}:
- k = 2 gives two support edges with the same label pair;
- k = 3 gives four support edges on the three pairs of a 3-set, so some pair repeats;
- k = 1 makes one label the end of R and also the end of R′, so it is cut twice.

k = 0 is also impossible (a doubled cut).

## 2. Label-location lemma

**Lemma L.** For x ∈ X9, all H-vertices labelled x have degree 2, and there are exactly four of them. Exactly r_P − 1_(x∈𝒫) of them lie on P's cross paths; the rest lie on O's self-dual paths.

*Proof.* K_x has no long cycle and no fixed point: the long cycles are at v and w, and the two leaves are labelled v and w. So x has five degree-2 split vertices. One of them lies on the reverse pair, and d_H(x) = 8 leaves four in H.

P traverses only cross paths, and each cross-path vertex exactly once. x lies in each of P's r_P rows exactly once, and a cut visit serves two rows. So the number of P-visits of x is r_P − 1_(x∈𝒫). ∎

**Type I, r_P = 4.** Here |B| = 5, and by v60 §2 B carries no v- or w-copy. Each x has 4 − (4 − 1_(x∈𝒫)) = 1_(x∈𝒫) vertices on B. So **the four interior vertices B1..B4 carry exactly the four labels of 𝒫, once each.**

## 3. Type I, r_P = 4: common structure

Positions:
- P: A at [0, x], D at [x, x+t], C^- at [x+t, 40];
- O: B at [0, 5], D^- at [5, 5+t], B^- at [5+t, 10+t], C, then A^- ending at 50.

**(a) O never cuts B.** An O-boundary on B would be an 𝒫-labelled cut of O. So O has two rows containing the whole of B:

    Q1 = A[α..1], v, B1..B4, w, D[t−1..t−5+α],     Q2 = D[δ2..1], w, B4..B1, v, C[1..γ],

with α + (5−α) = 5 and δ2 + γ = 5. Put:
- d̄ = L(D[t−5+α..t−1]) and d = L(D[1..δ2]);
- a = L(A[1..α]) and c = L(C[1..γ]).

The labels of Q1 and Q2 give

    𝒪 = a ⊔ d̄ = c ⊔ d.                                        (1)

**(b) Counting by Lemma W.** With B uncut:
- D carries n_D^w + 1 O-boundaries;
- A carries n_A^w + 1;
- C carries n_C^w + 1.

By (L1) each count is at most 2. Since n_A^w + n_C^w + n_D^w = 2, the cases are (1,1,0), (1,0,1) and (0,1,1). The last two are mirror images. Also n_D^v = n_D^w.

**(c) Lemma R0: P's b_v-row R_P0 = C[j..1], v, A[1..10−j] is strictly longer than Q1 on A and strictly longer than Q2 on C.** Its sides are taken as walks if they pass b_w.

Let U be the ten non-v labels, W1 = B1..B4, b_w, D[t−1..t−5+α] and W2 = B1..B4, b_w, D[1..δ2]. Then 𝒫 ⊂ L(W1) ∩ L(W2).
- *Equal lengths:* a doubled cut.
- *Shorter on both:* L(W1) = U∖S_A(α) ⊊ U∖S_A(10−j) = S_C(j) ⊊ S_C(γ), and S_C(γ) is disjoint from L(W2). So L(W1) ∩ L(W2) = ∅. Contradiction.
- *Shorter on A only:* L(W1) ⊆ S_C(j), so 𝒫 ⊆ S_C(j). But R_P0's A-end is a P-cut, carrying a 𝒫 label, so that label occurs twice in R_P0.
- *Shorter on C only:* symmetric.

So R_P0 is longer on both sides, and

    S_C(j) ⊆ 𝒫 ∪ {w} ∪ d̄,    S_A(10−j) ⊆ 𝒫 ∪ {w} ∪ d,    a ⊆ d,    c ⊆ d̄.      (2)

## 4. Case (1,1,0)

**O's rows** are Q1 = [−α, 10−α], Q2, R_Cw = C[γ..γ+10] (inside C), Q3 = C[γ+10..z−1], w, A[x−1..10+α], and R_Aw = A[10+α..α] (inside A). Hence t = 10−α−γ, the O-boundary on D is δ2 = 5−γ, and x ≥ 11+α. All D-labels lie in 𝒪. By (1)–(2), |d ∩ d̄| = 5−α−γ.

**R_P0's w lies on A** (the C side is the mirror case). Then P's rows are:
- R_P0;
- R_P1 = A[10−j..x−1], w, D[1..π];
- R_P2 = D[π..t−1], w, C[z−1..j+10];
- R_P3 = C[j..j+10], inside C.

**Offsets.**
- R_Cw and R_P3 have offset j−γ, so j−γ ≥ 4.
- R_P1 against R_Aw (shared run A[10−j..10+α]) has offset k = 10−j−α, so k ≥ 4.

Hence α = γ = 1, j = 5 and t = 8. Then δ2 = 4, π = 15−x ≤ 3, and z = 32−x.

**D.** D[1..4] and D[4..7] each carry four distinct 𝒪 labels and share exactly three. So two labels occur both in D[1..3] and in D[5..7]. R_P2 ⊇ D[π..7] must be repetition-free, which forces π = 3 with the repeats at D1 and D2. Hence x = 12 and z = 20.

**Labels.**
1. Exchange of R_P1 = A[5..11], w, D1, D2, D3 with R_Aw = A[1..11] gives L(A[1..4]) = {w, ℓ(D1), ℓ(D2), ℓ(D3)}. A5 is a P-cut, so ℓ(A5) ∈ 𝒫. Then by R_P0, C[1..5] carries three 𝒫 labels (C5 among them) and two 𝒪 labels. So **C[1..4] carries two 𝒫 labels.**
2. R_P2 = D3..D7, w, C19..C15. Its five D-vertices carry all of 𝒪, so C[15..19] carries {v} ∪ 𝒫.
3. Q3 = C[11..19], w, A11. A11 is an O-cut with an 𝒪 label, so C[11..14] carries 𝒪 ∖ {ℓ(A11)}.
4. R_P3 = C[5..15] then forces C[6..10] to carry {v, w, ℓ(A11)} and the **two** 𝒫 labels other than ℓ(C5) and ℓ(C15).
5. R_Cw = C[1..11] therefore contains 2 + 1 + 2 = 5 labels from 𝒫, but |𝒫| = 4. **Contradiction.**

## 5. Case (1,0,1) (and its mirror (0,1,1))

**O's rows** are:
- Q1;
- R_Dw = D[δ2+10..δ2], inside D;
- Q2;
- Q3 = C[γ..z−1], w, A[x−1..10+α];
- R_Aw = A[10+α..α].

So t = 20−α−γ, δ2 = 5−γ ≤ 4, and x ≥ 11+α. P has two boundaries on D at π1 and π1+10, and its inside-D row is offset from R_Dw by |π1−δ2|. The offset lemma gives |π1−δ2| ≥ 4.

**Case 1: R_P0's w is the A w-copy.** P's rows are:
- R_P0 = C[j..1], v, A[1..10−j];
- R_P1 = A[10−j..x−1], w, D[1..π1];
- R_P2 = D[π1..π1+10];
- R_P3 = D[π1+10..t−1], w, C[z−1..j].

So π1 = 20−x−j ≤ 9−α−j.
- If π1 > δ2, then π1 ≥ 9−γ, so α + j ≤ γ. This contradicts j > γ (Lemma R0).
- If π1 < δ2, then π1 ≤ 1−γ ≤ 0. Impossible.

**Case 2: R_P0's w is b_w(x+t),** so R_P0 = D[π1+10..t−1], w, C[z−1..1], v, A[1..ℓ_A]. P's rows are:
- R_P0;
- R_P1 = A[ℓ_A..ℓ_A+10], inside A;
- R_P2 = A[ℓ_A+10..x−1], w, D[1..π1];
- R_P3 = D[π1..π1+10], inside D.

**Offsets.** The inside-A rows have offset e_A = ℓ_A − α ≥ 4.

**Lengths.** The row lengths give z = π1 − e_A + γ. Q3 needs z ≥ γ+1, so π1 ≥ e_A + 1 ≥ 5 > δ2.

**Contradiction.** The D-offset then gives π1 ≥ δ2 + 4 = 9 − γ. But R_P0 needs π1+10 ≤ t−1, i.e. π1 ≤ 9−α−γ. So α ≤ 0, which is impossible.

## 6. Result

**WRITTEN.**
- **Lemma L** holds in H.
- **Type I with r_P = 4 is impossible** in the disconnected distinct 3+5 case.

Lemma L also gives the following for the open cases:
- Type I, r_P = 3: each 𝒫 label has two vertices on B and each 𝒪 label one.
- Type II: each 𝒫 label has 4 − r_P + 1 vertices on C ∪ D and each 𝒪 label 4 − r_P.

**Owner-written residual** (assuming the unreviewed bodies v47–v81 are correct):
- R1–R4 are empty.
- R5 consists of Type I with r_P = 3 (v80), Type II with r_P = 2, and the Type II, r_P = 3 survivors S1, S2 and S2′ (v78).
- R6: all m ≥ 9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
