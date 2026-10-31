# Actual Tuscan11 distinct 3+5, disconnected, Type II with r_P = 3, survivor S1 — shape (β) excluded, shape (α) reduced to two explicit prefixes

Actual `/bin/date` before this body: **Mon Oct 26 12:14:42 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case exclusion, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports

- **v83** (SHA256 `a429177c9b9673bb062f485755a272e3efb6ecd980b1807bba6c08b1c5424159`): notation, shapes (α)/(β), the lo/hi structure.
- **Lemma L** of v81 (SHA256 `fc30690676d04cf019258f3cdeee853fd8e03813dd19f9f45eb431e72d27df08`). In particular, each 𝒪 label has exactly one vertex on C ∪ D.
- **Pair uniqueness** (v77 §2, SHA256 `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`): no two support edges of H carry the same unordered label pair.
- The exchange identity and distinct cut labels.

## 2. Shape (β) is impossible

In (β): K = t+3, τ = 2, β_P = 3 and ρ = 17. P's rows are R_P1 = A[7..1], v, B[1..3], R_Pmid = B[3..13] and R_P* = B[13..y−1], w, A[x−1..7]. O's rows include N2 = B[7..1], v, C[1..3] and Q_d = D[2..1], w, C[c−1..1], v, A[1..t−7].

From v83:
- pB1 = ℓ(B3), and its lo vertex is D1, which is adjacent to b_w.
- C1 and C2 carry pA and pB2.
- R_P1 needs a w, which can only be the second B w-copy. So B[1..2] = {that w-copy, a vertex called B_other}.

**(1) B_other carries an 𝒪 label.** It is not v, not w and not in 𝒫. Exchanging R_P1 with Q_d (shared part: v and A[1..t−7]) gives

    L(A[t−6..7]) ⊔ {ℓ(B_other)} = {ℓ(D2)} ⊔ L(C[1..c−1])    (after cancelling w and pB1).

ℓ(B_other) is not in A[1..7], since R_P1 is repetition-free. It is not ℓ(C3) either, since both lie in N2. So **ℓ(B_other) ∈ {ℓ(D2)} ∪ L(C[4..c−1]).**

**(2) The w-copy is B1.** If it were B2, then B2–B3 and b_w–D1 would both carry the pair {w, pB1}, against pair uniqueness. So B1 is the w-copy and B2 = B_other.

**(3) B_other's label is not ℓ(D2).** B2–B3 carries {ℓ(B_other), pB1} and D1–D2 carries {pB1, ℓ(D2)}, so pair uniqueness gives ℓ(D2) ≠ ℓ(B_other). By (1), B_other's unique C∪D vertex therefore lies on C[4..c−1].

**(4) B_other's label must also cut D.** The six O-cuts A[t−7], D[σ], B17, B7, C3 and D2 carry exactly 𝒪 = {ℓ(B_other), ℓB4, ℓB5, ℓB6, ℓB7, ℓC3}; this set is read off N2. The complementary P4 of v83 §4 gives ℓ(B17) ∈ {ℓB4, ℓB5, ℓB6}. Also ℓ(A[t−7]) ≠ ℓ(B_other), because A[1..7] avoids it, and ℓ(D2) ≠ ℓ(B_other) by (3). Hence **ℓ(D[σ]) = ℓ(B_other).**

**(5) Contradiction.** By (3) and (4), B_other's label has two C∪D vertices: D[σ] and the C[4..c−1] vertex from (3). Lemma L says an 𝒪 label has exactly one. If C[4..c−1] is empty, (1) and (3) already contradict each other.

**Shape (β) is impossible** (WRITTEN).

## 3. Shape (α): two explicit prefixes

In (α): K = t+2, τ = 3, β_P = 4, ρ = 18 and t ∈ {9, ..., 12}. P's rows are R_P1 = A[6..1], v, B[1..4], R_Pmid = B[4..14] and R_P* = B[14..y−1], w, A[x−1..6]. Further:
- C1 = pA and C2 is an O-cut.
- {ℓD1, ℓD2} = {pB1, pB2}, and D3 is an O-cut.
- B[1..3] carries pB2, the second B w-copy and one vertex x with an 𝒪 label.
- B4 = pB1.

**(a) ℓ(x) = ℓ(D3).**
- Exchanging R_P1 with Q_d gives L(A[t−7..5]) ⊔ {ℓx} = {ℓD3, ℓC2} ⊔ L(C[3..c−1]). Since ℓx ≠ ℓC2 (both lie in N2), ℓx ∈ {ℓD3} ∪ L(C[3..c−1]).
- Suppose x's C∪D vertex were on C. N2 gives 𝒪 = {ℓx, ℓB5, ℓB6, ℓB7, ℓB8, ℓC2}. So ℓx would have to cut one of A[t−8], D[σ], B18 or D3.
- It cannot be any of them:
  - A[1..6] avoids ℓx;
  - D[σ] and D3 lie on D, while ℓx's unique C∪D vertex would be on C;
  - ℓB18 ∈ {ℓB5, ℓB6, ℓB7} by the complementary P4.

So ℓx = ℓD3.

**(b) Pair uniqueness fixes the prefixes.**
- D1–D2 carries {pB1, pB2}, so B3 ≠ pB2.
- If B3 is the w-copy, then:
  - b_w–D1 forces ℓD1 = pB2, so ℓD2 = pB1;
  - B2–B3 then forces B2 = x and B1 = pB2.
- If B3 = x, then:
  - D2–D3 forces ℓD2 = pB2, so ℓD1 = pB1;
  - B2–B3 forces B2 = w and B1 = pB2.

So exactly two prefixes remain:
- **(α1)** B[1..4] = pB2, x, w, pB1, and D[1..3] carries pB2, pB1, ℓx.
- **(α2)** B[1..4] = pB2, w, x, pB1, and D[1..3] carries pB1, pB2, ℓx.

Both have b_v–B1 = {v, pB2} and b_v–C1 = {v, pA}.

**(c) Further consequences.**
- {ℓ(A[t−8]), ℓ(D[σ]), ℓ(B18)} = {ℓB5, ℓB6, ℓB7}.
- A[7..x−1] ⊆ {v, ℓB8, ℓB18}.
- The two labels of {ℓB5, ℓB6, ℓB7} ∖ {ℓB18} are exactly ℓ(A[t−8]) and ℓ(D[σ]).
- B[9..13] carries {v, w, pA, ℓx, ℓC2}.

## 4. Status

**WRITTEN.**
- In Type II with r_P = 3, survivor S1, shape (β) is excluded.
- Shape (α) is reduced to the prefixes (α1)/(α2) of §3, still **open**.
- The (2,0) mirror of S1 reduces identically.

The residual is otherwise as in manifest v16-delta (SHA256 `d53ba4ae3b1d0b37cca6daa1a0e0525f8163b9abd4b5530af8adeb8937389ef4`).

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
