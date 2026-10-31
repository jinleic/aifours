# Actual Tuscan11 distinct 3+5, disconnected, Type II with r_P = 3 — survivors S2 and S2′ excluded, so Type II with r_P = 3 is closed

Actual `/bin/date` before this body: **Mon Oct 26 12:25:41 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports

- **v76** (SHA256 `a2218f8fb409011ea8d0279d2b75ec3a8066af584afde61bc0dcfdbb8bf1b9a8`): the Type II, r_P = 3 frame of §4(a).
- **v77** (SHA256 `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`):
  - §6, the K > 20 row structure;
  - §7, which records that rule (R) on A forces K + β_P = 26 in S2;
  - Lemma U;
  - pair uniqueness;
  - the reversal symmetry.
- **v78** (SHA256 `e6d1e18d5b7166266e92ff2fe5c25e4b99162646dcf0de8228c87a9d24cd1bfd`): the definition of S2 and S2′.
- **v81** (SHA256 `fc30690676d04cf019258f3cdeee853fd8e03813dd19f9f45eb431e72d27df08`): Lemma L.
- **v83** (SHA256 `a429177c9b9673bb062f485755a272e3efb6ecd980b1807bba6c08b1c5424159`): the lo/hi block argument of §2, which applies verbatim here.

## 2. S2: setting

**S2** is the case (n_A^w, n_B^w) = (1,1) with K > 20 and one P-boundary on B. Here K + β_P = 26 and t ∈ (6, 12]. O's rows are:
- Q_a = A[K−10..x−1], w, D[1..σ];
- Q_b = D[σ..t−1], w, B[y−1..ρ];
- M1 = B[ρ..1], v, C[1..K−10−t];
- Q_c = C[K−10−t..c−1], w, D[t−1..τ];
- Q_d = D[τ..1], w, C[c−1..1], v, A[1..K−20];
- M2 = A[K−20..K−10], inside A.

The parameters satisfy ρ = 20+t−K, τ = 15+t−K and K ∈ (t+10, t+15).

P's rows are:
- R_P1 = A[K−16..1], v, B[1..β_P];
- R_P3 = A[K−16..K−6], inside A, offset 4 from M2;
- R_P2 = B[β_P..y−1], w, A[x−1..K−6].

𝒫 = {pB, pA1, pA2}, where pB = ℓB[β_P], pA1 = ℓA[K−16] and pA2 = ℓA[K−6].

**Placement of copies and second vertices** (Lemma W and Lemma L):
- The A w-copy lies in (K−16, K−10). The B w-copy b_w′ lies in B[1..β_P−1], since it is R_P1's w.
- pA2's second A∪B vertex lies in (K−20, K−16).
- pB's second A∪B vertex lies in (K−16, K−10).
- pA1's second A∪B vertex lies in B(β_P, y) ∪ A(K−6, x).

**Lo/hi blocks** (exactly as in v83 §2). C[1..K−11−t] ∪ D[1..τ−1] holds exactly three "lo" vertices, one per 𝒫 label; each 𝒫 label also has a "hi" vertex in D(τ, t−1]. Every other vertex of C ∪ D is the v-copy or carries an 𝒪 label.
- β_P < ρ, so M1 contains pB at B[β_P]. Hence **pB's lo vertex lies on D**.
- pA2 has no vertex in M1's B-part. Hence **pA2's lo vertex lies on C**.

That leaves exactly two shapes:
- **(γ)** pA1's lo vertex is on C. Then K = t+13, τ = 2, β_P = 13−t and ρ = 7.
- **(δ)** pA1's lo vertex is on D. Then K = t+12, τ = 3, β_P = 14−t and ρ = 8, and pA1's second vertex lies in B(β_P, 8).

## 3. Shape (δ) is impossible

In (δ):
- C1 = pA2 and C2 is an O-cut, so the pair {pA2, ℓC2} is the edge C1–C2.
- M1 = B[8..1], v, C1, C2 contains C2, so ℓC2 does not occur on B[1..8].

**Exchanging R_P1 with Q_d** (shared part: v and A[1..t−8]) gives

    (𝒪 labels of A[t−7..t−5]) ⊔ (𝒪 labels of B[1..β_P−1]) = {ℓD3} ⊔ L(C[2..c−1]).

ℓC2 is on the right. It is not on B, so it lies in A[t−7..t−5]. pA2's second vertex also lies there.

**M2 against R_P3 (offset 4)** gives L(A[t−8..t−5]) = L(A[t+3..t+6]). These are two edge-disjoint P4s on one 4-set, so together they realise all six pairs of that set. One of those pairs is {pA2, ℓC2}, which is already the edge C1–C2. This contradicts pair uniqueness. **(δ) is impossible.**

## 4. Shape (γ) is impossible

In (γ):
- D1 = pB, which is adjacent to b_w.
- C1 and C2 carry pA1 and pA2, and C3 is an O-cut.
- M1 = B[7..1], v, C[1..3], so B[1..7] holds b_w′, pB and five 𝒪 labels.
- The O-cuts are A[t−7], A[t+3], D[σ], B7, C3 and D2. So the 𝒪 labels on B[1..6] are {ℓA[t−7], ℓA[t+3], ℓD[σ], ℓD2}.

**Exchanging R_P1 with Q_d** shows that the 𝒪 labels on B[1..β_P−1] lie in {ℓD2} ∪ L(C[3..c−1]). Three of the candidate labels are ruled out:
- ℓA[t−7], because R_P1 contains A[t−7];
- ℓD[σ], whose only C∪D vertex is D[σ];
- so these labels lie in {ℓA[t+3], ℓD2}.

**Pair uniqueness fixes B[β_P−1]:**
- B[β_P−1] ≠ b_w′, since otherwise w–pB would occur twice (once with D1).
- B[β_P−1] ≠ ℓD2, since otherwise pB–ℓD2 would occur twice (once with D1–D2).
- Hence ℓB[β_P−1] = ℓA[t+3], and **β_P ∈ {3, 4}**, i.e. t ∈ {9, 10}.

**t = 10 (β_P = 3, c = 5).** B1 = b_w′ and B2 = ℓA13. The exchange forces ℓC4 = ℓA13. Then w is adjacent to ℓA13 twice: B1–B2 and b_w–C4. **Contradiction.**

**t = 9 (β_P = 4, c = 6).** Here B[1..2] = {b_w′, ℓD2} and B3 = ℓA12. The exchanges give:
- A1 = ℓD[σ] and A2 = ℓA2 (the O-cut);
- A[3..5] carries {pA2, ℓC3, ℓB7}, with A5 ≠ pA2, since otherwise pA1–pA2 would repeat C1–C2;
- C[4..5] carries {ℓA12, ℓB7}.

M2 = A[2..12] against R_P3 = A[6..16] (offset 4) gives a complementary P4 A[13..16] ending at pA2. All four admissible orders put ℓA13 ∈ {ℓC3, ℓB7}, and A12 = ℓA12.
- **ℓA13 = ℓB7** repeats the pair {ℓA12, ℓB7} of C4–C5.
- **ℓA13 = ℓC3** repeats C3–C4 when C4 = ℓA12. When C4 = ℓB7, it repeats the pair {ℓC3, ℓB7}, which the P4s place at A4–A5 or A13–A14.

**Contradiction in every case.**

So **(γ) is impossible**, and hence **S2 is impossible** (WRITTEN).

## 5. S2′

Apply the reversal symmetry of v77 §3: reverse every row, swap A ↔ B and reverse D. Computing positions, an old D-forward boundary at O-position K moves to K″ = 30+t−K. So S2's condition K > 20 becomes K″ < 10+t. The single P-boundary on B moves to A, leaving two on B. That is exactly S2′, so **S2′ is impossible**.

## 6. Result

With v76–v78 and v83–v85, **Type II with r_P = 3 is impossible** in the disconnected distinct 3+5 case (WRITTEN).

**Owner-written residual** (assuming the unreviewed bodies v47–v86 are correct):
- R1–R4 are empty.
- R5 consists of:
  - Type I, r_P = 3, two/one sub-case (v82), including the variant where P's b_v-row passes b_w(x+t), and its mirror;
  - Type II, r_P = 2.
- R6: all m ≥ 9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
