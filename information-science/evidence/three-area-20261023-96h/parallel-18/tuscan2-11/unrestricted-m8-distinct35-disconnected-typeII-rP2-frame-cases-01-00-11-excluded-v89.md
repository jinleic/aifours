# Actual Tuscan11 distinct 3+5, disconnected, Type II with r_P = 2 — frame, and the cases (n_D^v, n_D^w) = (0,1), (0,0), (1,1) excluded

Actual `/bin/date` before this body: **Mon Oct 26 12:49:03 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports

- **v60** (SHA256 `d09ec901a98a25480d12b9c81622c43044f5c2415b196fb9d64bb71ae9ad6259`): the Type II faces P = B A^- and O = A D B^- C D^- C^-, and the counts.
- **v76** (SHA256 `a2218f8fb409011ea8d0279d2b75ec3a8066af584afde61bc0dcfdbb8bf1b9a8`): Lemma W, T3 (and T3 for walks, v77 §1), and C5.
- **v77** (SHA256 `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`): the Type II reversal symmetry.
- **v81** (SHA256 `fc30690676d04cf019258f3cdeee853fd8e03813dd19f9f45eb431e72d27df08`): the offset lemma.
- **Manifest v17** (SHA256 `d7aacd45caf64cd906a544f2cc9ebae54585d894a1c4f128031926eabc5328e8`): the current DAG.

## 2. Frame of Type II with r_P = 2

**Counts (v60 §2).** r_O = 7. There is one cross v-copy v2 and one cross w-copy w2 on A ∪ B. There are two self-dual v-copies and one self-dual w-copy on C ∪ D. The lengths satisfy |A| + |B| = x + y = 20 and |C| + |D| = c + t = 25.

**Positions along O:**
- A at [0, x];
- D at [x, x+t];
- B^- at [x+t, 20+t], ending at b_v(20+t);
- C at [20+t, 45];
- D^- at [45, 45+t];
- C^- at [45+t, 70].

**P's rows.** These are R1 = A[10−β..1], v, B[1..β] and R2 = B[β..y−1], w, A[x−1..10−β]. R1's w is w2, and R2's v is v2.

**Boundary counts (Lemma W).** Write n_X^v and n_X^w for the copy counts on X. Consecutive w-visits along O are separated by exactly one boundary, and so are consecutive v-visits. This gives:
- each D-pass carries n_D^w + 1 boundaries;
- (B^- ∪ C-forward) carries n_B^w + n_C^w + 1 boundaries;
- (C^- ∪ A) carries n_C^w + n_A^w + 1 boundaries;
- **A ∪ B carries n_D^v − n_D^w + 1 boundaries**;
- **C carries 4 − n_D^v − n_D^w boundaries in total.**

The cases are (n_D^v, n_D^w) ∈ {0,1,2} × {0,1}. The reversal symmetry of v77 §3 maps each case to itself and swaps A ↔ B.

## 3. Case (0,1): impossible

A ∪ B carries no O-boundary. So the O-row through b_v(0) contains all of A and b_w(x), and the O-row through b_v(20+t) contains all of B and b_w(x+t). Both rows already have b_v and b_w as their v and w. Hence A ∪ B carries no copy, contrary to a_v = a_w = 1.

## 4. Case (0,0): impossible

Here each D-pass has exactly one boundary, so C5 applies. A ∪ B carries one boundary.

**A carries none.** The row Q_a through b_w(x) is the row X0 through b_v(0); its A-side is the walk over all of A, then b_v, then C. So v2 and w2 lie on B, and B carries one boundary ρ.
- **T3:** X0's A-walk is longer than R1's A-side, so R1 is shorter on A. Hence Y0 is shorter on B, i.e. ρ < β.
- **C5:** R2's A-segment A[10−β..x−1] lies inside Q_a's A-walk, and R2's B-segment B[β..y−1] lies inside Q_b's segment B[ρ..y−1]. This contradicts C5.

**B carries none.** This is the mirror case, and it fails the same way: T3 gives α < 10−β, and C5 fires on Q_a = A[α..x−1], w, D[1..σ].

## 5. Case (1,1): impossible

D carries one v-copy and the w-copy W1; C carries one v-copy and no w-copy. A ∪ B carries one boundary, and each D-pass carries two.

**A carries none.** Then X0 = Q_a contains b_v(0), all of A and b_w(x). So v2 and w2 lie on B, which carries one boundary ρ.

The w-visits of O come in the order b_w(x), W1 (forward), b_w(x+t), w2, b_w(45), W1 (backward), b_w(45+t). So O's seven rows, in order, are:
- X0 = C[γ..1], v, A, w, D[1..σ1];
- R_W = D[σ1..σ1+10], inside D;
- Q_b = D[σ1+10..t−1], w, B[y−1..ρ];
- Y0 = B[ρ..1], v, C[1..c0];
- Q_c = C[c0..c−1], w, D[t−1..τ1];
- R_W′ = D[τ1..τ2], inside D, with τ2 = τ1 − 10;
- Q_d = D[τ2..1], w, C[c−1..γ].

The counts of §2 confirm that C-forward carries exactly the boundary c0 and C-backward exactly γ.

**Row lengths:**
- Y0 gives ρ + c0 = 10.
- Q_c gives τ1 = 15 − c0 = ρ + 5, so τ2 = ρ − 5 ≥ 1.
- Q_d gives γ = c + ρ − 15 ≥ 1, so t = 25 − c ≤ 9 + ρ.
- The forward D-boundary σ1+10 is interior, so σ1 ≤ t − 11 ≤ ρ − 2.

**Contradiction.** The two inside rows R_W and R_W′ on D have offset |σ1 − τ2| ≥ 4 by the offset lemma.
- If σ1 ≥ τ2 + 4 = ρ − 1, this contradicts σ1 ≤ ρ − 2.
- If σ1 ≤ τ2 − 4 = ρ − 9, then σ1 ≤ 0, because ρ = 10 − c0 ≤ 9.

Both are impossible.

**B carries none.** This is the mirror case under the reversal symmetry, which fixes (1,1). It is impossible too.

## 6. Status

**WRITTEN.** In Type II with r_P = 2, the cases (n_D^v, n_D^w) = (0,1), (0,0) and (1,1) are impossible.

**Open:** (1,0), (2,0) and (2,1). In each of these, A ∪ B carries 2, 3 or 2 boundaries respectively.

The owner-written residual of manifest v17 is otherwise unchanged:
- R1–R4 are empty.
- R5 is these three Type II, r_P = 2 cases.
- R6 is all m ≥ 9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
