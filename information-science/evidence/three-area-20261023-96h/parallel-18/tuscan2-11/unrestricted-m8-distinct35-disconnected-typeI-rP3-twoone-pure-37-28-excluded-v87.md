# Actual Tuscan11 distinct 3+5, disconnected, Type I with r_P = 3, two/one sub-case — pure (b1,g1) = (3,7) and (2,8) excluded; the through-b_w variant opened

Actual `/bin/date` before this body: **Mon Oct 26 12:30:14 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports and a scope correction

**Imports:**
- v80 (SHA256 `e7c267afe00cb5c6909162da1d97ac4c93f30b875ca295badd0ff24ad2822dd2`);
- v82 (SHA256 `f62ba5909ef95b4529296bd977bc69b6fd7c0c6bf7a6e6dc7e643115caa74c08`);
- v81 (SHA256 `fc30690676d04cf019258f3cdeee853fd8e03813dd19f9f45eb431e72d27df08`): Lemma L, which for Type I with r_P = 3 says each 𝒪 label has exactly one B-vertex and three cross-path vertices; and the offset lemma;
- v77 (SHA256 `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`): pair uniqueness and Lemma U.

**Scope correction (additive; v80 and v82 are not edited).** v80 §4 and v82 §4 wrote P's b_v-row as R_P0 = C[j..1], v, A[1..p], with its C-side inside C. Call this the **pure variant**. P's b_v-row may instead pass b_w(x+t). Call that the **through-b_w variant**, in which:
- R_P0 = D[π..t−1], w, C[z−1..1], v, A[1..p];
- R_P1 = A[p..p+10], inside A;
- R_P2 = A[p+10..x−1], w, D[1..π].

The through-b_w variant was not treated there.
- v82 §4 (i)–(iii) use only O-rows, plus the facts that pA = ℓA[p] is of type (L2,U2) and pD = ℓD[π] is of type (L1,U1). Those facts hold in both variants by the same argument. So **b1 ∈ {2,3} and g1 ∈ {7,8} hold in both variants.**
- The through-b_w variant additionally satisfies p + b1 ∈ [4, 6], by the offset lemma applied to R_P1 against X0 and Q3.

## 2. Pure variant, (b1, g1) = (3, 7): excluded

Here e = 4, t = 10 and ω = 2.

**Lemma L fixes B up to position 14.**
- B[1..2] are the lower vertices of pD and pC.
- B3 = o_b is an O-cut.
- B[4..6] carries s_w, pA's lower vertex and ℓD2.
- B7 is an O-cut.
- B14 is pA's upper vertex.

**The labels on D.** 𝒪_L = L(D[1..2]) = {o_b, ℓD2}, and D2 = D[ω] is the cut. So ℓD1 = o_b.

**M against Q2 has offset 4.** The offset lemma and pair uniqueness make B[3..6] the complementary P4 of Q2's run D2, D1, b_w, B14, which carries ℓD2, o_b, w, pA. Since B3 = o_b, we get **B[3..6] = (o_b, pA, ℓD2, w)**. So s_w = B6. Then w's neighbour labels already include:
- o_b, via b_w–D1;
- pA, via b_w–B14;
- ℓD2 and ℓB7, via B5–B6–B7.

**The labels on A.** X0's labels give L(A[1..7]) = {w, pA, ℓD2, ℓC1, ℓC2, ℓC3, ℓB7}. R_P0 against X0 gives L(C[1..j]) = L(B[1..3]) ⊔ L(A[p+1..7]), so 𝒪_U = L(C[1..3]) ⊆ L(A[p+1..7]). Hence **A[1..p] ⊆ {w, pA, ℓD2, ℓB7}**.

**Contradiction.** In the pure variant R_P0's w is the A-copy a_w ≤ p−1. Its right neighbour A[a_w+1] lies in A[2..p] and carries pA, ℓD2 or ℓB7. Each of these pairs with w already. This contradicts pair uniqueness.

## 3. Pure variant, (b1, g1) = (2, 8): excluded

Here e = 6, t = 10 and ω = 3.

**M against Y0 has offset 4.** B[9..12] is the complementary P4 of Y0's run B1, b_v, C1, C2, which carries pD, v, ℓC1, ℓC2. B12 is an O-cut, so **B[9..12] = (v, ℓC2, pD, ℓC1)** and o* = ℓC1.

**The O-cuts.** These are B2 (o_b), B8, B12, D3 = D[ω], C2 and A8. The six O-cut labels are exactly 𝒪, so **ℓA8 = o3**, the third label of 𝒪_L = L(D[1..3]) = {o_b, ℓD3, o3}.

**Q1 = B[12..14], w, D[9..3]** forces L(D[3..9]) = {v, pD, o_b, ℓD3, o3, ℓB8, ℓC2}. So o3 has three cross-path vertices: one in D[1..2], one in D[4..9], and A8. By Lemma L it has no other cross-path vertex.

**Contradiction.** R_P0 against Y0 (pure variant) gives L(C[3..j]) ⊔ L(A[1..p]) = L(B[1..8]) ∋ o3, since o3's B-vertex lies in B[3..7]. But o3 has no vertex on C, and its only A-vertex A8 lies outside A[1..p] (because p < 8).

## 4. Status

**WRITTEN.** In Type I with r_P = 3, two/one sub-case, the pure variant is excluded for (b1, g1) = (3,7) and (2,8).

**Still open:**
- the pure variant for (2,7) and (3,8);
- the through-b_w variant for all four pairs;
- the one/two mirror of every remaining case.

**Owner-written residual** (assuming the unreviewed bodies v47–v87 are correct):
- R1–R4 are empty.
- R5 consists of:
  - the items above;
  - Type II with r_P = 2.
- R6: all m ≥ 9.

Type II with r_P = 3 is closed (v86).

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
