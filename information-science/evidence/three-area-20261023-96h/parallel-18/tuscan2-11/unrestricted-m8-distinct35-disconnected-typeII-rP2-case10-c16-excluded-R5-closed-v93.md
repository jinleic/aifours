# Actual Tuscan11 distinct 3+5, disconnected, Type II with r_P = 2, case (1,0), c = 16 — excluded; Type II with r_P = 2 and the whole disconnected line (R5) closed

Actual `/bin/date` before this body: **Mon Oct 26 13:08:33 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports

- v91 (SHA256 `6ce36617acf89783d637683fcac923e8bfcdc144d8451d5ad7e2029a19442543`): the c = 16 layout of case (1,0), pattern (I) with w2 on A, and the row-count rule.
- v89, v90, v92 (SHA256 `cfd9f2b8a83a328b7925b8d3137f2c9b8cc13c24554b3acc16ed5a1667b08d81`, `e605d3411357848c86d90005eef1f1d2f4a1d333c04302967c87ca04563ea9a3`, `bf8b45986b4be177a4f0aaeb84e6532c1e7779d94ace8c6377c984f097b2c921`).
- Pair uniqueness and the reversal symmetry (v77, SHA256 `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`).

## 2. The c = 16 layout (from v91 §5)

Here α = 7, t = 9, τ = 7, ρ = 2, c1 = 8, γ1 = 3 and γ2 = 13. The facts used are:
- D8 = pA, with neighbours D7 = ℓD7 and b_w. So the pairs {pA, ℓD7} and {pA, w} are used.
- C[1..3] carries {pB, ℓC13, ℓC3}, with C3 = ℓC3.
- C13 = ℓC13 and C[14..15] carries {ℓC3, ℓA7}. So the pair {ℓC3, ℓA7} is used (C14–C15), and so is one of {ℓC13, ℓC3}, {ℓC13, ℓA7} (C13–C14).
- X0 = C[3..1], v, A[1..7] gives L(A[1..7]) = {w, pA, ℓD7, ℓA7, ℓC8, ℓB1, ℓB2}, with A7 = ℓA7.
- B1 = ℓB1, B2 = ℓB2, and pB's cut is B[β]. Pattern (I) gives 10−β < 7 and β > ρ = 2.

## 3. Exchange of R1 with X0

R1 = A[10−β..1], v, B[1..β] and X0 share v and A[1..10−β]. Hence

    L(B[1..β]) = L(C[1..3]) ⊔ L(A[11−β..7]) = {pB, ℓC13, ℓC3} ⊔ L(A[11−β..7]).

**Consequences:**
- ℓB1 and ℓB2 lie in A[11−β..7].
- ℓC13, ℓC3 and ℓA7 (the last at A7 ∈ A[11−β..7]) lie in B[3..β−1].

So β ≥ 6.

**Bounding β from above.** The remaining β−6 vertices of A[11−β..7] carry labels of A[1..7] that also occur on B[3..β−1]. Among these labels only ℓC8 can have a B-vertex:
- w2 is the cross w-copy on A;
- pA's only A∪B vertex is its cut;
- ℓD7's two A∪B vertices both lie on A.

Hence **β ∈ {6, 7}**.

## 4. Both values fail

**β = 6.** B[3..5] is a 3-path on {ℓC13, ℓC3, ℓA7}. The pair {ℓC3, ℓA7} is already used, so ℓC13 must sit in the middle. That needs both {ℓC13, ℓC3} and {ℓC13, ℓA7} to be unused. But one of them is the pair C13–C14. This contradicts pair uniqueness.

**β = 7.** A[4..7] carries {ℓB1, ℓB2, ℓA7, ℓC8}, so A[1..3] carries {w, pA, ℓD7}. pA's cut is A[10−β] = A3. Then A2 ∈ {w2, ℓD7}, so A2–A3 is the pair {pA, w} or {pA, ℓD7}. Both pairs are already used at D8. **Contradiction.**

So case (1,0) with c = 16 is impossible. With v91 §4 (c = 15) and v90 §4, **case (1,0) is impossible**; by the reversal symmetry its mirror is too.

## 5. Result: R5 is empty

**Type II with r_P = 2 is impossible** (WRITTEN):

| Case | Source |
|---|---|
| (0,1), (0,0), (1,1) | v89 |
| (2,0) | v90 |
| (1,0) | v90, v91, §4 above |
| (2,1) | v92 |

Combined with the earlier owner packets, **every configuration of the disconnected distinct 3+5 line (R5) is excluded**:
- Type I: v60, v80–v82, v87, v88 (with v81 covering r_P = 4).
- Type II with r_P = 3: v76–v78, v83–v86.

**Owner-written residual** (assuming every unreviewed body v47–v93 is correct):
- **R1–R5 are all EMPTY.** So the whole support-8 line of the ladder is excluded at the owner-written level.
- That is: one8, same-centre 3+5 and 4+4 (gated earlier), distinct-centre 4+4 (a)-I (gated), (a)-II and (b), and distinct 3+5 connected and disconnected.
- **What remains of the necessary ladder is R6: all supports m ≥ 9** (capped at m ≤ 36 by the v24 control).

**Scope.** This is a necessary-case Tuscan-1 result composed of unreviewed written bodies; it needs its own source-bound gate. It shows nothing about Tuscan-2 existence. The literal Tuscan-1(11) control has m = 36, so distance-one reasoning alone cannot settle the target.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
