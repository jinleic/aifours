# Actual Tuscan11 distinct 3+5, disconnected, Type II with r_P = 2 — no O-row inside A or B; case (2,0) excluded; case (1,0) half excluded

Actual `/bin/date` before this body: **Mon Oct 26 12:52:57 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports

- **v89** (SHA256 `cfd9f2b8a83a328b7925b8d3137f2c9b8cc13c24554b3acc16ed5a1667b08d81`): the frame and boundary counts of Type II with r_P = 2.
- **v81** (SHA256 `fc30690676d04cf019258f3cdeee853fd8e03813dd19f9f45eb431e72d27df08`): Lemma L. For Type II with r_P = 2 it says:
  - each P-cut label (pA = ℓA[10−β], pB = ℓB[β]) has exactly one vertex on A ∪ B, namely its cut, and three vertices on C ∪ D;
  - each 𝒪 label has two vertices on each.
- **v76/v77** (SHA256 `a2218f8fb409011ea8d0279d2b75ec3a8066af584afde61bc0dcfdbb8bf1b9a8`, `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`): Lemma W, T3 and the reversal symmetry.

## 2. Lemma N: no O-row lies inside A or inside B

An O-row inside A would have to carry pB on an A-vertex, but pB has no vertex on A. Symmetrically, an O-row inside B would lack pA. ∎

**Consequence.** Each of A and B carries at most one O-boundary, since two boundaries on one path would enclose an inside row.

**Corollary.** By v89 §2, A ∪ B carries n_D^v − n_D^w + 1 boundaries.
- Case (2,0) needs 3 of them, so **(2,0) is impossible.**
- Cases (1,0) and (2,1) need 2, so **A and B each carry exactly one O-boundary**, at A[α] and at B[ρ].

## 3. Case (1,0): structure

Here:
- D carries one v-copy and no w-copy, so each D-pass carries one boundary: σ forward, τ backward.
- C carries one v-copy V_C and the w-copy W_C.
- C carries 3 boundaries in total.

O's rows near b_v are:
- X0 = C[γ1..1], v, A[1..α] (its C-side may instead be the walk);
- Y0 = B[ρ..1], v, C[1..c0].

**T3 patterns.**
- **(I):** R1 is shorter on A (10−β < α) and Y0 is shorter on B (ρ < β).
- **(II):** the mirror image, β < ρ and α < 10−β.

The reversal symmetry exchanges (I) with (II) and also exchanges the location of w2 between A and B.

## 4. Case (1,0), pattern (I) with w2 on B: impossible

**Boundary counts and the O-rows.** The counts of v89 §2 give 3 boundaries in B^- ∪ C-forward, i.e. ρ, c0 and c1, and 2 boundaries in C^- ∪ A, i.e. γ and α. So O's rows are:
- Q_a = A[α..x−1], w, D[1..σ];
- Q_b = D[σ..t−1], w, B[y−1..ρ];
- Y0 = B[ρ..1], v, C[1..c0], whose w is w2;
- R_Cw = C[c0..c1], inside C, holding W_C;
- Q_c = C[c1..c−1], w, D[t−1..τ];
- Q_d = D[τ..1], w, C[c−1..γ];
- X0 = C[γ..1], v, A[1..α], whose w is W_C on its backward pass.

**Counting pA.** pA's cut A[10−β] lies in X0, because 10−β < α. Every other O-row must meet pA at a vertex of C ∪ D:
- Q_a needs a D-vertex in D[1..σ), since Q_a's A-part starts at α > 10−β;
- Q_b needs a D-vertex in D(σ, t);
- Y0 needs a C-vertex in C[1..c0);
- R_Cw needs a C-vertex in C(c0, c1).

These are four distinct vertices of C ∪ D. But pA has exactly three (Lemma L). **Contradiction.**

By the reversal symmetry, **pattern (II) with w2 on A is impossible too.**

## 5. Status

**WRITTEN.**
- Lemma N holds.
- Case (2,0) is impossible.
- In case (1,0), the halves (I, w2 on B) and (II, w2 on A) are impossible.

**Open:**
- case (1,0) with (I, w2 on A), together with its mirror (II, w2 on B);
- case (2,1), where A and B each carry one boundary. Its w2-on-A half forces C-forward to be unbounded and pattern (I), with lengths t = 10+α+ρ, c = 15−α−ρ, τ2 = ρ+5, γ = 10−α, 6 ≤ α ≤ 9 and 1 ≤ ρ ≤ 4. The w2-on-B half is its mirror.

**Owner-written residual** (assuming the unreviewed bodies v47–v90 are correct):
- R1–R4 are empty.
- R5 consists of the open items above.
- R6: all m ≥ 9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
