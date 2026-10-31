# Original Tuscan-2(11), entire m = 9 distance-two branch, part 94: L1 types 12 and 2 with r2 = 2, c′ = 0, b3 inside Q1 — (C′, d′) = (40,6) is closed, so ℓ2 ≤ 15 is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq2-cprime0-b3-in-Q1-C40-d6-reduction-first-R3-in-L1-v206.md` (SHA256 `0d8b8e12ec8656310c152970986039b3f63e4c398324d2f7973774766b442ab9`).

It uses:
- v204: Lemma R7C, in particular (a′) (SHA256 `79a93d0974841c512910d7a2418011e498fb7989145a143bac39d8e1d5af40ce`);
- v205 §5: u ≥ 6 (SHA256 `89e4fdbf6be5c6c3cdafaee1f2dc9d83bd4e0ac20797787a699d5f025032d181`);
- v206 §3: ℓ2 ≥ 11, which uses (R1)–(R2) only.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. **It uses (R1)–(R2) only.** The (R3) step of v206 §2 is not needed for this closure.

## 1. The case

Type 12, r2 = 2, c′ = 0, b3 inside Q1, ℓ2 ≤ 15 and (C′, d′) = (40,6). Then ℓ1 + ℓ2 = 24, P2 = 34 − u, P3 = 59 − ℓ2, P4 = 59 and P5 = 55 + ℓ2.

**ℓ2 = 15 is impossible.**
- Here Λ[15−ℓ2] = Λ[0] is b6.
- So the upper part of W′, the positions 41..44 (Λ[3], Λ[2], Λ[1] and b6 at P3 = 44), carries v.
- By (a′) its label set equals that of the arm vertices at 30..33, which carry S-labels. So v ∈ S, which is false.

**The remaining range.** By v205 §5, u ≥ 6, and by v206 §3, ℓ2 ≥ 11. So ℓ2 ∈ [11,14] and u ∈ [6,9]. Hence:
- P2 = 34 − u ∈ [25,28], inside R2;
- P3 = 59 − ℓ2 ∈ [45,48], inside R4;
- P5 = 55 + ℓ2 ∈ [66,69], inside R6;
- b6 also lies at 10 − u (inside R0) and at 80 + u (inside R8).

## 2. v has nowhere to put its cut

Since c′ = 0, v's cut is an F1-cut. No b6-corner lies on a multiple of 10, so the cut is at a V-passage.

| Cut | Vertex there | Why it is not v's cut |
|---|---|---|
| 10 | t1[u], i.e. c1 | c1 ∈ S |
| 20 | t2[P2−20] in the S_12-run (P1 = P2 − ℓ2 ≤ 17) | this cut covers R1 and R2, but b6 at P2 is already in R2 |
| 30 | Λ[λ−u+4], the end of P′ | carries a Q-label, and Q ⊂ S |
| 40 | Λ[19−ℓ2] (P−-run, since P2 < 40 < P3) | this cut covers R3 and R4, but b6 at P3 is in R4 |
| 50 | t2[ℓ2−9] (S_23-run, since P3 < 50 < P4) | this cut covers R4 and R5, but b6 at P3 is in R4 |
| 60 | t3[ℓ2−5] (t3-run, since P4 < 60 < P5) | this cut covers R5 and R6, but b6 at P5 is in R6 |
| 70 | Λ[15−ℓ2], the end of P | carries a Q-label |
| 80 | Λ[λ−u] | carries c8 ∈ S |

A label passes through each row exactly once. So no F1-cut can belong to v. **Contradiction.**

## 3. Result

**WRITTEN:** L1 type 12 with r2 = 2, c′ = 0, b3 inside Q1 and (C′, d′) = (40,6) is impossible.

With v205, **L1 type 12 with r2 = 2, c′ = 0, b3 inside Q1 and ℓ2 ≤ 15 is impossible**. By the mirror (v160 §1), so is type 2.

This closure uses (R1)–(R2) only. The reduction of v206 §2, which used (R3) through D2Q, is superseded for this purpose, but stays recorded as written.

**State of types 12 and 2 with r2 = 2:**
- c′ = 1 is closed (v200–v202).
- c′ = 0 with ℓ3 < 10 − x is closed (v200).
- c′ = 0 with ℓ3 > 20 − x is closed (v203).
- c′ = 0 with b3 inside Q1 and ℓ2 ≤ 15 is closed (v205, v207).
- **OPEN:** c′ = 0 with b3 inside Q1 and ℓ2 ≥ 16.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2, c′ = 0, b3 inside Q1 and ℓ2 ≥ 16;
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
