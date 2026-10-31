# Original Tuscan-2(11), entire m = 9 distance-two branch, part 96: L1 types 12 and 2 with r2 = 2, c′ = 0, b3 inside Q1, ℓ2 ≥ 16, 31 ≤ P2 ≤ 40 — reduction to two explicit shapes

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq2-cprime0-b3-in-Q1-l2-ge-16-P2-le-30-or-ge-41-closed-v208.md` (SHA256 `e88690e559b8041ba657c3356234086180d175953ff4e22994eaa2a184f77636`). It uses the data of v200 §1, v204 §2(i) and v208 §1, including the fact that v has no Λ-vertex.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only. **It is a reduction, not an exclusion.**

## 1. Data

Type 12, r2 = 2, c′ = 0, b3 inside Q1, ℓ2 ≥ 16 and 31 ≤ P2 ≤ 40. With P1 = 10 − u + ℓ1 ∈ [11,19]:
- P3 = 25 + u + P1;
- P4 = 25 + u + P2;
- P5 = 55 + P2 − P1 ∈ [71,79];
- λ = 25 + u − ℓ2;
- ℓ3 = 30 − u − P1.

**The rows R2 and R3.**
- R2 = [20,30] lies inside the S_12-run, so it is the pure t2-row t2[P2−20..P2−30].
- R3 = t2[P2−30..1], b6 (P2), Λ[λ−1..] (P−-positions P2+1..40). Its first u Λ-positions carry the arm S-labels.

## 2. w

w consists of:
- ℓ (R0, R8);
- b3 at P1 (R1) and at P4;
- t3[dw] with dw ≤ 9 − x, at P5 − dw;
- two G1-W's.

**First G1-W.** Since R2 is pure t2, w has a G1-W t2[jw] with S_12 ∈ R2, so jw ∈ [P2−29, P2−21].

**Second G1-W.** It must cover R3, so it is one of:
- **(a)** t2[jw′] with S_12 ∈ R3 (jw′ ≤ P2 − 31);
- **(b)** a non-arm Λ with P− ∈ R3 and P+ ∈ R7 (R8 is taken by ℓ).

**(b) is impossible.**
- w's remaining rows R4, R5 and R6 are filled in F1-order by S_23(jw), P4 and t3[dw].
- So P4 ∈ R5, i.e. u + P2 ≤ 34. This is false, since u ≥ 4 and P2 ≥ 31.

**So (a) holds.** w's remaining rows R4..R7 are filled in order by S_23(jw′) < S_23(jw) < P4 < t3[dw]:
- S_23(jw′) ∈ R4 and S_23(jw) ∈ R5;
- **P4 ∈ R6**, so u + P2 ∈ [36,44];
- **t3[dw] ∈ R7**, so dw ≤ P5 − 71 = ℓ2 − 16, and hence ℓ2 ≥ 17;
- P2 ≥ 32, since t2[jw′] needs an S_12-position in 31..P2−1.

## 3. v

By v208 §1, v = {b6, t2[jv], G2-V}. Its rows R0, R7 and R8 come from b6. The middle rows R1..R6 are covered, in F1-order, by:
- G2-V if it is a t1-vertex;
- S_12(jv);
- P2;
- P3;
- S_23(jv);
- G2-V if it is a t3-vertex;
- plus one cut extension.

v must meet R2, which is pure t2. So S_12(jv) lies in R2 or on 20 or 30.

**(b1) G2-V is a t1-vertex in R1.**
- S_12(jv) lies strictly inside R2 (a cut at 20 or 30 would double R1 or R3), and P2 ∈ R3.
- **P2 = 40 is impossible.** That would be v's cut, with P3 ∈ R5, i.e. u + P1 ≥ 26. But u + P2 ≤ 44 gives u = 4 and P1 ≥ 22 > 19.
- **P3 = 50 as v's cut is impossible.** Then w's S_23(jw′) = 50 + jw′ ≥ 51 could not lie in R4.
- **The only shape left:** P3 ∈ R4 and S_23(jv) = 60 is v's cut, so jv = 60 − P3.

**(b2) G2-V is a t3-vertex in R6.**
- R1 is reached only by S_12(jv) at 20 as v's cut. So **jv = P2 − 20, i.e. v = X20**.
- Then P2 ∈ R3 (P2 = 40 would be a second cut), P3 ∈ R4 and S_23(jv) ∈ R5.

## 4. The copy of R2

In S_23 the vertices of R2 form the all-label window W2 = [P3+P2−30, P3+P2−20]. Its ends carry the F1-cut labels X30 and X20, so W2 contains exactly one F1-cut C2, with pieces of sizes in {4,5,6} by the window argument.
- **(b1):** v's cut S_23(jv) = 60 lies in W2, so C2 = 60 and **P2 + P3 ∈ {84,85,86}**.
- **(b2):** the top of W2 is v's S_23 ∈ R5, so C2 = 50 and **P2 + P3 ∈ {74,75,76}**.

## 5. Result

**WRITTEN (reduction):** L1 type 12 with r2 = 2, c′ = 0, b3 inside Q1, ℓ2 ≥ 16 and 31 ≤ P2 ≤ 40 survives only in two shapes. In both, ℓ2 ≥ 17, 32 ≤ P2 ≤ 39 and u + P2 ∈ [36,44], and w = {ℓ, b3, t3[dw] (R7), t2[jw′] (R3, R4), t2[jw] (R2, R5)}.
- **(b1):** v = {b6, t1-vertex (R1), t2[60−P3] (S_12 ∈ R2, cut 60)}, with P3 ∈ R4 and P2 + P3 ∈ {84,85,86}.
- **(b2):** v = X20 = {b6, t2[P2−20] (cut 20, S_23 ∈ R5), t3-vertex (R6)}, with P3 ∈ R4 and P2 + P3 ∈ {74,75,76}.

The same holds for type 2 by the mirror (v160 §1).

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2, in the shapes (b1) and (b2);
- types 1 and 11 with r1 ∈ {4,5};
- type 8 with r1 ∈ {3,4}.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
