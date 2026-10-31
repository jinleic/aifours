# Actual Tuscan11 distinct 3+5, disconnected, Type II with r_P = 2, case (n_D^v, n_D^w) = (2,1) — excluded by row-type counting and DUP

Actual `/bin/date` before this body: **Mon Oct 26 13:04:34 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports

- **v89** (SHA256 `cfd9f2b8a83a328b7925b8d3137f2c9b8cc13c24554b3acc16ed5a1667b08d81`): the frame.
- **v90** (SHA256 `e605d3411357848c86d90005eef1f1d2f4a1d333c04302967c87ca04563ea9a3`): Lemma N. A and B each carry exactly one O-boundary, at α and ρ.
- **v91** (SHA256 `6ce36617acf89783d637683fcac923e8bfcdc144d8451d5ad7e2029a19442543`): the row-count rule.
- **v81** (SHA256 `fc30690676d04cf019258f3cdeee853fd8e03813dd19f9f45eb431e72d27df08`): Lemma L and the offset lemma.
- **DUP and pair uniqueness** (v45 §1 and v77 §2; SHA256 `a3737445594b19101f86b798b00e4501ac4ad500ca0f07572482c45c1cfc9d50`, `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`).
- **The reversal symmetry** (v77 §3).

## 2. Structure (w2 on A; the w2-on-B case is its mirror)

Here D carries the two self-dual v-copies V1, V2 and the w-copy W1, and C carries no copy. Each D-pass carries two boundaries, and C carries one boundary in total.

With w2 on A, the counts of v89 §2 leave C-forward without a boundary. So Y0 contains b_v(20+t), all of C, and b_w(45). Then T3 forces pattern (I): 10−β < α and ρ < β.

**O's rows:**
- X0 = C[γ..1], v, A[1..α];
- Q_a = A[α..x−1], w, D[1..σ1];
- R_W = D[σ1..σ1+10], inside D;
- Q_b = D[σ1+10..t−1], w, B[y−1..ρ];
- Y0 = B[ρ..1], v, C[1..c−1], w, D[t−1..τ1];
- R_W′ = D[τ1..τ2], inside D;
- Q_d = D[τ2..1], w, C[c−1..γ].

**Lengths:**
- τ1 = ρ+15 and τ2 = ρ+5;
- γ = 10−α and t = 10+α+ρ;
- c = 15−α−ρ, x = 10+α−σ1 and y = 10−α+σ1;
- 6 ≤ α ≤ 9.

**The offset lemma on R_W and R_W′.** It gives σ1 < τ2 and e := τ2 − σ1 ∈ {4, 5, 6}. (If instead σ1 > τ2, then σ1 ≥ ρ+9, contradicting σ1 ≤ 9.) Hence σ1 < τ2 < σ1+10 < τ1.

**Visit table.** A C-vertex is visited forward by Y0 and backward by X0 (left of γ) or Q_d (right of γ). A D-vertex in each region is visited as follows (forward row, backward row):

| Region | Forward | Backward |
|---|---|---|
| (0, σ1) | Q_a | Q_d |
| (σ1, τ2) | R_W | Q_d |
| (τ2, σ1+10) | R_W | R_W′ |
| (σ1+10, τ1) | Q_b | R_W′ |
| (τ1, t) | Q_b | Y0 |

The cuts D[σ1], D[τ2], D[σ1+10], D[τ1] and C[γ] each count for three rows.

## 3. Placement of every label

**pA and pB.** pA's cut lies in X0 and pB's cut in Q_b. By the row-count rule:
- pA has one D-vertex in each of (0, σ1), (τ2, σ1+10) and (τ1, t).
- pB has one D-vertex in (0, σ1), one in (τ2, σ1+10), and a C-vertex q ∈ C(0, γ).

**The copies.**
- V2 < τ2.
- V1 ∈ (τ2, τ1).
- W1 lies in the overlap (τ2, σ1+10).

**The seven 𝒪 labels.** These are exactly the seven O-cut labels. Each must meet R_W and R_W′ through D-vertices. Exhausting the combinations allowed by the visit table leaves the following types:
- **ℓB[ρ]:** an overlap vertex and a (0, σ1) vertex, plus A[1..α).
- **ℓA[α]:** either
  - (A4): an overlap vertex and C(γ, c), plus B(ρ, y); or
  - (B): a (σ1, τ2) vertex and a (σ1+10, τ1) vertex, plus B[1..ρ).
- **ℓC[γ]:** an overlap vertex, plus A(α, x) and B(ρ, y).
- **ℓD[σ1]:** a (σ1+10, τ1) vertex, plus A[1..α) and B[1..ρ).
- **ℓD[τ2]:** either a (τ1, t) vertex plus A[1..α) and A(α, x), or a C(0, γ) vertex plus A(α, x) and B(ρ, y).
- **ℓD[σ1+10]:** either a (0, σ1) vertex plus A[1..α) and B[1..ρ), or a C(γ, c) vertex plus A[1..α) and A(α, x).
- **ℓD[τ1]:** a (σ1, τ2) vertex, plus A[1..α) and A(α, x).

**Counting region sizes.**
- (σ1, τ2) has e−1 ≥ 3 places, but its only candidates are V2, ℓA[α] (type B) and ℓD[τ1]. So **e = 4** and all three are present. Hence ℓA[α] has type (B), and V2's forward visit lies in R_W.
- (σ1+10, τ1) also has 3 places. Its only candidates are V1, ℓA[α] and ℓD[σ1], so all three are present. Hence V1's forward visit lies in Q_b, and v2 is Q_a's v, on A(α, x).
- The overlap has 5 places: W1, pA, pB, ℓB[ρ] and ℓC[γ].
- (0, σ1) has ρ places: pA, pB, ℓB[ρ], and ℓD[σ1+10] if it takes its first type. So **ρ ∈ {3, 4}**.
- (τ1, t) has α−6 places and C(0, γ) has 9−α places. Between them they hold pA's vertex, q, and the single vertex of ℓD[τ2]. So **α ∈ {7, 8}**:
  - α = 8: ℓD[τ2]'s vertex lies on D;
  - α = 7: it lies on C(0, γ).
- B(ρ, y) has 10−α places: pB, ℓC[γ], and ℓD[τ2] when α = 7.

## 4. Contradiction

**α = 8.**
- C(0, γ) = {C1} = {q}, so C1–C2 is the pair {pB, ℓC[γ]}.
- B(ρ, y) consists of two adjacent vertices carrying pB and ℓC[γ].
- So the same pair occurs on two edges, contradicting pair uniqueness.

**α = 7.**
- C[1..3] carries {pB, ℓD[τ2], ℓC[γ]}.
- B(ρ, y) is a run of three vertices carrying the same three labels.
- These are two vertex-disjoint paths on one 3-label set, contradicting DUP.

So the case (2,1) with w2 on A is impossible. By the reversal symmetry, the case (2,1) with w2 on B is impossible too.

## 5. Result

**WRITTEN.** In Type II with r_P = 2, **case (2,1) is impossible**. Together with v89–v91, the only open part of Type II with r_P = 2 is case (1,0) with α = 7 and c = 16 (and its mirror), as reduced in v91 §5.

**Owner-written residual** (assuming the unreviewed bodies are correct):
- R1–R4 are empty.
- R5 is that single sub-case.
- R6 covers all m ≥ 9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
