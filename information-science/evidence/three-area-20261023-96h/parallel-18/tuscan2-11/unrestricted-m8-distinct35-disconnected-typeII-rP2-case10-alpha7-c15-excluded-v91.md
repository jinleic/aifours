# Actual Tuscan11 distinct 3+5, disconnected, Type II with r_P = 2, case (1,0), remaining half — α = 7 forced; c = 15 excluded; c = 16 reduced

Actual `/bin/date` before this body: **Mon Oct 26 12:59:47 PDT 2026**. InfoRecursiveMDS18-2. NEW exact WRITTEN CANDIDATE, not reviewed, adopted, formal, executable or novelty-cleared. All-variable written reasoning only: no interpreter, kernel, program, enumeration tool, solver, replay, numeric instance, probe or GO. Tuscan-1-only support-ladder work (v24 caps the ladder at m<=36); a necessary-case reduction, not a construction or a Tuscan-2 nonexistence result. Separate, ungated successor line (not part of the v19-v49 freeze).

## 1. Imports

- v89 (SHA256 `cfd9f2b8a83a328b7925b8d3137f2c9b8cc13c24554b3acc16ed5a1667b08d81`) and v90 (SHA256 `e605d3411357848c86d90005eef1f1d2f4a1d333c04302967c87ca04563ea9a3`): the frame, Lemma N and the case split.
- Lemma L and the offset lemma of v81 (SHA256 `fc30690676d04cf019258f3cdeee853fd8e03813dd19f9f45eb431e72d27df08`): each 𝒪 label has exactly two vertices on A ∪ B and exactly two on C ∪ D, and exactly one of its four vertices is its O-cut; each P-cut label (pA, pB) has its cut as its only A∪B vertex, plus three C∪D vertices.
- Pair uniqueness (v77 §2, SHA256 `c5dabb9939e0bb6e25221f233e8239a9184d324adca7daea35201e88b58f62d7`).

**Row-count rule.** Each label meets each of O's seven rows exactly once. An A∪B vertex is visited once. A C∪D vertex is visited twice. An O-cut vertex counts for the two rows it separates.

## 2. Structure: pattern (I) with w2 on A

The case is (n_D^v, n_D^w) = (1,0), pattern (I) (10−β < α, ρ < β), with w2 on A. The boundary counts give:
- A carries one O-boundary, α, and B carries one, ρ;
- each D-pass carries one boundary, σ forward and τ backward;
- C-forward carries one boundary, c1;
- C-backward carries two, γ1 < γ2 = γ1 + 10.

O's rows are:
- X0 = C[γ1..1], v, A[1..α];
- Q_a = A[α..x−1], w, D[1..σ];
- Q_b = D[σ..t−1], w, B[y−1..ρ];
- Y0 = B[ρ..1], v, C[1..c1], holding W_C;
- Q_c = C[c1..c−1], w, D[t−1..τ];
- Q_d = D[τ..1], w, C[c−1..γ2];
- R_Cw′ = C[γ1..γ2], inside C.

**Lengths.** γ1 = 10−α, τ = 30−α−c, c1 = α+c−15, ρ = 25−α−c and t = 25−c. The offset lemma on R_Cw′ against Y0 and against Q_c gives 4 ≤ c1−γ1 ≤ 6.

**The D-lemma variant.** Q_d's C-segment lies inside Q_c's C-segment. As in v77 §4 (with roles swapped) this gives σ < τ and σ+τ ≥ t.

**Lemma W and Lemma L place the copies and the P-cut labels:**
- pA's vertices are A[10−β], d1 ∈ D[1..σ), d2 ∈ D(τ, t) and p1 ∈ C(γ1, c1).
- pB's vertices are B[β], e1 ∈ D[1..σ), q1 ∈ C(0, γ1) and q2 ∈ C(c1, γ2).
- The copies satisfy V_D < τ, V_C ∈ C(c1, γ2) and W_C ∈ C(γ1, c1).

**Exchanges.**

    (I1)  L(C[γ1..c1−1]) = L(C[γ2+1..c−1]) ⊔ {w} ⊔ L(D[τ..t−1])      (Q_c against R_Cw′)
    (I2)  L(C[c1+1..γ2]) = L(B[1..ρ]) ⊔ {v} ⊔ L(C[1..γ1−1])         (Y0 against R_Cw′)

## 3. α = 7 is forced

**D(τ, t) carries no 𝒪 label.** Take such a label o. By (I1), its two C∪D vertices are a vertex d ∈ D(τ, t) and a vertex C[k] with γ1 < k < c1. Neither is visited by Q_d, and Q_d has no A∪B part. So o misses Q_d, which is a contradiction.

D(τ, t) also carries no copy and no pB vertex. Hence D(τ, t) = {d2}, which forces t−1−τ = α−6 = 1, i.e. **α = 7**.

**C(γ2, c) carries only ℓC[γ1], or ℓC[γ1] together with ℓA[α].**
- By the row-count rule, any 𝒪 label on C(γ2, c) is either ℓC[γ1] (with its partner at the cut C[γ1]) or ℓA[α] (whose cut A[α] serves X0 and Q_a).
- ℓC[γ1] must indeed lie there. Otherwise it would lie on D(τ, t), and then it would miss Q_d as above.

So c−1−γ2 ∈ {1, 2}, i.e. **c ∈ {15, 16}**.

**C(0, γ1) holds q1 and the label ℓC[γ2]** (by (I2) and the row-count rule).

## 4. c = 15 is impossible

Here t = 10, τ = 8, ρ = 3, c1 = 7, γ1 = 3 and γ2 = 13.

**What D9 already uses.** D(8, 10) = {D9}, so D9 = pA. Its neighbours are D8 = ℓD8 and b_w, so the pairs {pA, ℓD8} and {pA, w} are already used.

**Where p1 sits.** (I1) gives L(C[3..6]) = {ℓC3, w, ℓD8, pA} with C3 = ℓC3, so C[4..6] carries W_C, ℓD8 and pA. In any order of these three consecutive vertices, pA is adjacent to W_C or to the ℓD8-vertex. That repeats a used pair, contradicting pair uniqueness.

## 5. c = 16 reduced

Here t = 9, τ = 7, ρ = 2, c1 = 8, γ1 = 3 and γ2 = 13.

**The labels on C, D and A:**
- D8 = pA, whose neighbours are ℓD7 and w.
- C[3..7] carries {ℓC3, W_C, ℓD7, pA, ℓA7} with C3 = ℓC3.
- C[14..15] = {ℓC3, ℓA7}, C[1..2] = {pB, ℓC13} and C[9..12] = {ℓB1, ℓB2, V_C, pB}.
- 𝒪 = {ℓC3, ℓD7, ℓA7, ℓC8, ℓB1, ℓB2, ℓC13}.
- ℓD[σ] = ℓB1.

**Placement of pA's C-vertex.** pA must avoid W_C and ℓD7. That leaves exactly C[3..7] = (ℓC3, pA, ℓA7, {W_C, ℓD7}) or (ℓC3, {W_C, ℓD7}, ℓA7, pA).

**Further consequences.**
- In every placement W_C is adjacent to ℓD7.
- The A∪B row counts give A(7, x) = {ℓC3, ℓC13, ℓD7} ∪ {ℓC8 or v2 as placed}, and σ = 4 + [ℓC8 on B] + [v2 on B] ∈ {4, 5, 6}.

This case is still **open**; it needs pair-level completion.

## 6. Status

**WRITTEN.** In case (1,0), the remaining half (I, w2 on A) and its mirror (II, w2 on B) force:
- α = 7;
- c ∈ {15, 16};
- c = 15 is impossible;
- c = 16 is reduced to the explicit layouts of §5, which remain open.

Case (2,1) is also open.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied. All cadence (including the 39:33 lapse of checkpoint-071), private-written-exactness, admission, clock and source histories, the checkpoint045 withdrawal and the parent-v60 intake-pause MAJOR remain unchanged. This candidate needs its own complete source-bound gate.
