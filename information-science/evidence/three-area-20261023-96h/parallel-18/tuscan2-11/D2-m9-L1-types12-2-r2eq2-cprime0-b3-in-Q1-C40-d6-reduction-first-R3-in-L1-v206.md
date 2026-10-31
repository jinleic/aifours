# Original Tuscan-2(11), entire m = 9 distance-two branch, part 93: L1 types 12 and 2 with r2 = 2, c′ = 0, b3 inside Q1, ℓ2 ≤ 15, (C′, d′) = (40,6) — reduction to u ∈ {8,9}, with the first use of (R3) in L1

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq2-cprime0-b3-in-Q1-l2-le-15-three-of-four-closed-v205.md` (SHA256 `89e4fdbf6be5c6c3cdafaee1f2dc9d83bd4e0ac20797787a699d5f025032d181`).

It uses:
- Lemma R7C (a′) and (b), and §2(i), of v204 (SHA256 `79a93d0974841c512910d7a2418011e498fb7989145a143bac39d8e1d5af40ce`);
- Lemma KS (v120 §1, T1);
- Lemma D2Q (v125 §1, SHA256 `85fcc86caa10a2ae94a8297a211a4d5577f034ffd30acbe69a1ec056b3847ec0`), **which uses the distance-two condition (R3)**.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. **§2 uses (R3) through D2Q. Everything else uses (R1)–(R2) only.** It is a reduction, not an exclusion.

## 1. Data

Type 12, r2 = 2, c′ = 0, b3 inside Q1, ℓ2 ≤ 15 and (C′, d′) = (40,6).

**Positions.**
- ℓ1 + ℓ2 = 24, ℓ3 = ℓ2 − 4, P2 + u = 34, P3 = 59 − ℓ2, P4 = 59 and P5 = 55 + ℓ2 ≤ 70.
- The window is W′ = [34,44], with Ra′ = R3 and Rb′ = R4.
- By v205 §5, u ≥ 6.

**(a′)** Q := L(Λ[15−ℓ2..18−ℓ2]) = L(Λ[λ−u+1..λ−u+4]). Write P for the first 4-path and P′ for the second.
- P′ lies on the Λ-arm, so Q consists of four S-labels.
- P and P′ are vertex-disjoint, since 18 − ℓ2 < 26 − ℓ2 = λ − u + 1.

**Passages.**
- P: P+ at 70..73 and P− at 44..41.
- P′: P+ at 81..84 and P− at 33..30.
- Only the end vertices Λ[15−ℓ2] (at 70) and Λ[λ−u+4] (at 30) lie on cuts. The interior vertices of P and P′ are 2-vertices with no passage on a cut.

## 2. u ≥ 8 (uses (R3))

**Applying D2Q.** D2Q applies to P and P′: their interior vertices are 2-vertices with no passage on a cut. Its conclusion 3 then reads as follows.

> Four Q-labels on a row sub-path Π that is vertex-disjoint from P ∪ P′ need |Π| ≥ 8.
> - Q-labels are never adjacent on Π, by (E).
> - Two Q-labels at distance 2 must form one of the two special pairs, by (R3).
> - Two consecutive gaps of 2 are therefore impossible.

**The t1-arm.** The t1-arm Π = t1[1..u] is a sub-path of R0. It carries all of S ⊇ Q and is vertex-disjoint from P ∪ P′. Hence **u ≥ 8**.

(Without (R3), KS alone excludes only u = 5: v205 §5.)

## 3. w's shape and ℓ2 ≥ 11 (T1)

**w's rows.** w is in R0 and R8 (ℓ), R1 (P1) and R5 (P4 = 59), and in R6 through t3[dw] (dw ≤ 9 − x). B-i gives x > 14 − ℓ2, so t3[dw] lies at P5 − dw ∈ [61,69].

**The two G1-W's.** They must cover R2, R3, R4 and R7.
- R7 is reached only by Λ P+.
- R3 = [30,40] lies strictly between P2 ≤ 28 and P3 ≥ 44, so it is reached only by Λ P−.
- Two separate Λ-W's would need two P+-rows, from R6, R7 and R8. R6 and R8 are taken, so this is impossible.
- Hence one Λ-W, Λ[kw], has P− ∈ R3 and P+ ∈ R7. This gives kw ∈ [20−ℓ2, 24−ℓ2] (P− at 35..39). P itself carries S-labels, so kw ∉ [15−ℓ2, 18−ℓ2].
- The other W covers R2 and R4.
  - In R2 the P−-positions carry Λ-arm S-labels.
  - In R4 the P−-positions 41..44 belong to P, which carries S-labels, and a Λ at 45..P3−1 has P+ ∈ R6, which is taken.
  - So it is a t2-vertex t2[jw] with S_12 ∈ R2 and S_23 ∈ R4.

**Exchange (b) of Lemma R7C.** L(Λ[20−ℓ2..25−ℓ2]) equals the label set of the positions 45..50: Λ[14−ℓ2..1], then b6 at P3, then t2[1], … .
- Since w = L(Λ[kw]) lies on the left, w occupies one of the positions 45..50.
- A Λ-vertex there has P+ in R6, which is impossible. So w is t2[jw] there, at P3 + jw ∈ [45,49].
- This gives **jw ≤ ℓ2 − 10**, and hence **ℓ2 ≥ 11**.

## 4. Result

**WRITTEN:** In L1 type 12 with r2 = 2, c′ = 0, b3 inside Q1, ℓ2 ≤ 15 and (C′, d′) = (40,6):
- u ∈ {8,9}, by D2Q, which uses (R3);
- ℓ2 ∈ [11, 23−u];
- w = {ℓ, b3, t3[dw], Λ[kw] (R3, R7), t2[jw] (R2, R4)}, with kw ∈ [20−ℓ2, 24−ℓ2] and jw ≤ ℓ2 − 10.

The same holds for type 2 by the mirror. This is the first point in the L1 family where (R3) is used. No exclusion is claimed; the case stays OPEN.

**OPEN (m = 9, L1):**
- Types 2 and 12 with r2 = 2, c′ = 0, b3 inside Q1:
  - (40,6) with u ∈ {8,9} and ℓ2 ∈ [11, 23−u];
  - ℓ2 ≥ 16.
- Types 1 and 11 with r1 ∈ {4,5}.
- Type 8 with r1 ∈ {3,4}.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
