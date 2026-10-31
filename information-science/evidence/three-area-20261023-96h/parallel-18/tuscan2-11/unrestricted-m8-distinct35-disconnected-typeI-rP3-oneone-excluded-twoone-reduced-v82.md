# Actual Tuscan11 distinct 3+5, disconnected, Type I with r_P = 3 — one-boundary/one-boundary excluded; the two/one case reduced

Actual `/bin/date` before this body: **Mon Oct 26 11:57:42 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case reduction, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports

- **v80** (SHA256 `e7c267afe00cb5c6909162da1d97ac4c93f30b875ca295badd0ff24ad2822dd2`): Lemma B and the sub-case split. Its §4 reductions for the two/one case are also used.
- **v81** (SHA256 `fc30690676d04cf019258f3cdeee853fd8e03813dd19f9f45eb431e72d27df08`):
  - Lemma L: each 𝒫 label has two vertices on B and each 𝒪 label one;
  - the offset lemma;
  - the cut-label partition X9 = 𝒫 ⊔ 𝒪.
- **v76/v77** (SHA256 `a2218f8fb409011ea8d0279d2b75ec3a8066af584afde61bc0dcfdbb8bf1b9a8`, `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`): Lemma W, and T3 for walks.

**Lemma R0′ (general form of v81 §3(c)).** Let R_P be P's row through b_v, and let Q be an O-row through b_v whose side on a half-edge h carries every label of 𝒫. Then R_P is not shorter than Q on Q's other half-edge h′.

*Proof.* Suppose R_P is shorter on h′. Complementing in the ten non-v labels gives L(Q's h-side) ⊆ L(R_P's side other than h′), so that side holds all of 𝒫. But R_P's h′-side ends at a P-cut, which carries a 𝒫 label. That label would occur twice in R_P. ∎

## 2. Where the 𝒫 labels sit on B

Suppose a pass of B has exactly one boundary b. Then the pass's two O-rows meeting B contain the whole runs B[1..b] and B[b..14] respectively. Each row contains each label once, and B[b] is an O-cut. So each 𝒫 label (two B-vertices by Lemma L) has exactly one B-vertex on each side of b.

For a pass with two boundaries, the three runs B[1..b], B[b..b+10] and B[b+10..14] each lie in a single O-row. So each run holds at most one B-vertex of each 𝒫 label.

## 3. Both passes with one boundary: excluded

Let the passes have single boundaries b1, g1 ∈ 6..9 with b1 ≠ g1, and let X0 = A[10−b1..1], v, B[1..b1] and Y0 = B[g1..1], v, C[1..10−g1] (v80 §4). By §2, every 𝒫 label has a B-vertex in [1, min(b1, g1)). So the B-sides of both X0 and Y0 carry all of 𝒫.

**If b1 < g1.** X0 is shorter on B than Y0. By T3, R_P0 is shorter on A than X0. This contradicts Lemma R0′ applied to Q = X0.

**If g1 < b1.** Y0 is shorter on B. By T3, R_P0 is shorter on C than Y0. This contradicts Lemma R0′ applied to Q = Y0.

So **the one/one sub-case of Type I with r_P = 3 is impossible** (WRITTEN).

## 4. Forward pass with two boundaries, backward pass with one: reductions

Use v80 §4's notation:
- B-boundaries at b1, b1+10 (b1 ∈ 1..4) and g1 = b1 + e (e ∈ {4,5,6});
- O's rows X0, M = B[b1..b1+10], Q1, Q2, Y0, Q3;
- t = b1 + g1 and ω = g1 − 5;
- P's rows R_P0 = C[j..1], v, A[1..p], R_P1 = A[p..x−1], w, D[1..π] and R_P2 = D[π..t−1], w, C[z−1..j], with p < 10 − b1 and p < g1.

**(i) All six 𝒪 labels have their B-vertex inside M.** M is an O-row lying inside B. So B[1..b1−1] and B[b1+11..14] carry only 𝒫 labels.

**(ii) The 𝒫 labels are pA = ℓ(A[p]), pD = ℓ(D[π]) and pC = ℓ(C[j]). Their B-vertices are placed as follows.**
- **pA:** X0 contains A[p]. So pA has its lower B-vertex in (b1, g1) and its upper one in (b1+10, 14].
- **pD:** Q2 contains pD's upper B-vertex, so D[π] ∉ Q2, i.e. **π > ω**. Then Q1 contains D[π]. So pD's upper B-vertex lies in (g1, b1+10), and its lower one in [1, b1).

Hence both outer runs of B are nonempty, so **b1 ∈ {2, 3}**.

**(iii) Exchanges.** M against Q2 (offset e) and M against Y0 (offset 10−e) give:
- L(D[1..ω]) = 𝒪_L, the 𝒪 labels whose B-vertex lies in [b1, g1);
- L(C[1..10−g1]) = 𝒪_U, the 𝒪 labels whose B-vertex lies in (g1, b1+10];
- 𝒪 = 𝒪_L ⊔ 𝒪_U ⊔ {ℓ(B[g1])}.

The six O-cuts are B[b1], B[g1], B[b1+10], D[ω], C[10−g1] and A[10−b1]. Two of them lie in 𝒪_L, namely B[b1] and D[ω]. Two lie in 𝒪_U, namely B[b1+10] and C[10−g1]. Hence |𝒪_L| = g1−5 ≥ 2 and |𝒪_U| = 10−g1 ≥ 2, so **g1 ∈ {7, 8}**.

The remaining open parameters are (b1, g1) ∈ {(2,7), (2,8), (3,7), (3,8)}, with t ∈ {9, 10, 10, 11}.

**(iv) Further exchanges.** These follow from the pairs R_P0/X0, R_P0/Y0, R_P1/Q2, R_P2/Q1, R_P1/Q3 and R_P2/Q3:
- L(C[1..j]) = L(B[1..b1]) ⊔ L(A[p+1..10−b1]);
- L(C[11−g1..j]) ⊔ L(A[1..p]) = L(B[1..g1]);
- L(A[p..x−1]) ⊔ L(D[ω+1..π]) = L(B[g1..14]);
- L(C[j..z−1]) = L(B[b1+10..14]) ⊔ L(D[ω..π−1]);
- L(C[10−g1..z−1]) = L(A[p..9−b1]) ⊔ L(D[1..π]);
- L(C[10−g1..j−1]) ⊔ L(A[10−b1..x−1]) = L(D[π..t−1]).

A label-set pass through the case (3,7) found no contradiction from these identities alone. Closing the case needs order-level reasoning (pair uniqueness, (N)), which is not done here.

## 5. Status

**WRITTEN.**
- Lemma R0′ holds.
- Type I with r_P = 3 in the one/one sub-case is excluded.
- The two/one sub-case (and its mirror one/two) is reduced to (b1, g1) ∈ {(2,7), (2,8), (3,7), (3,8)}, with the label structure of §4. It stays **open**.

**Owner-written residual** (assuming the unreviewed bodies v47–v82 are correct):
- R1–R4 are empty.
- R5 consists of:
  - Type I with r_P = 3, two/one sub-case (four parameter pairs, plus the mirror);
  - Type II with r_P = 2;
  - the Type II, r_P = 3 survivors S1, S2 and S2′.
- R6: all m ≥ 9.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
