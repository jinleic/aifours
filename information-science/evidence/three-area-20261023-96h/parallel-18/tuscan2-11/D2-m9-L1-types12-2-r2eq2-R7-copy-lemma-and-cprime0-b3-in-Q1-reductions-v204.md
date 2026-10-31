# Original Tuscan-2(11), entire m = 9 distance-two branch, part 91: L1 types 12 and 2 with r2 = 2 — the R7-copy lemma, and reductions for the last case (c′ = 0, b3 inside Q1)

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq2-cprime0-pure-t3-row-closed-v203.md` (SHA256 `eba280a46c40078136418c7bb600b0bf65bdfd9a1abbdb09ecb9f82fe130781b`) and uses the data of v200 §1 (SHA256 `47e8b945f4afe3626d2b8c39f6273171b4c6fe466b58272222a2abe8334d2602`).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only. **It is a reduction, not an exclusion.**

## 1. The R7-copy lemma (type 12, r2 = 2, ℓ2 ≤ 15)

**Lemma R7C.** In type 12 with r2 = 2 and ℓ2 ≤ 15, (ℓ1 + ℓ2) mod 10 ∈ {4,5,6}.

Moreover, with d′ := 10 − ((ℓ1 + ℓ2) mod 10) ∈ {4,5,6}:
- **(a) when u ≤ 10 − d′:** L(Λ[15−ℓ2..24−ℓ2−d′]) = (S ∖ {c8}) ∪ {v} ∪ L(t2[1..10−d′−u]);
- **(a′) when u > 10 − d′:** L(Λ[15−ℓ2..24−ℓ2−d′]) = L(Λ[λ−u+1..λ−u+10−d′]);
- **(b)** L(Λ[26−ℓ2−d′..25−ℓ2]) equals the label set of the d′ F1-positions that follow the upper end of W′ in the P−-pass. These are Λ[14−ℓ2], …, Λ[1], then b6 at P3, then t2[1], … along S_23. When ℓ2 = 15 the upper end is b6 itself, and they are t2[1..d′].

Here c8 = L(Λ[λ−u]) is the S-label on the F1-cut 80, and λ − u = 25 − ℓ2.

**Proof.**
- **R7.** Since P5 = 55 + ℓ2 ≤ 70, the row R7 = [70,80] is Λ[15−ℓ2..25−ℓ2] along P+. When ℓ2 = 15, Λ[0] means b6 at 70. The vertex at 80 is the arm start Λ[λ−u], carrying c8.
- **The copy.** Along P− the same vertices occupy the consecutive F1-positions W′ = [P3−25+ℓ2, P3−15+ℓ2] = [P2+u, P2+u+10], in reverse order. W′ carries every label.
- **W′ is not a row.** If P2 + u ≡ 0 (mod 10), W′ would be a row, and c8 would be cut at P2 + u ≤ 43 as well as at 80. So W′ contains exactly one F1-cut C′ strictly inside. Put d′ = C′ − (P2+u).
- **Pieces of size 1.**
  - d′ = 1 would put c8 on the F1-cut C′ + 10 < 80.
  - 10 − d′ = 1 would put L(Λ[15−ℓ2]) on the F1-cut C′ − 10 as well as at 70.
- **Pieces of size 2 or 3.** Each piece of W′ is a Λ-path. Its counterpart is a path along P− that shares no H-edge with it, so (E) forbids these sizes.
- **So d′ ∈ {4,5,6}.** Since P2 + u = 10 + ℓ1 + ℓ2, this gives the residue claim.
- **(a) and (a′).** They are the exchange of W′ with the row ending at C′. Its part below W′ consists of the 10 − d′ positions P2+u−1 down to C′−10. In order, these are the arm vertices Λ[λ−u+1..λ−1] (u − 1 of them), b6 at P2, and then t2[1], t2[2], … along S_12.
- **(b).** It is the exchange of W′ with the row starting at C′. ∎

## 2. The last case: c′ = 0 and b3 inside Q1

Here 1 ≤ x ≤ 9 and 10 − x < ℓ3 < 20 − x, and the F2-rows are:
- Q0 = t1[x..1], b6, t3[1..10−x];
- Q1 = t3[10−x..ℓ3−1], b3, t1[ℓ1−1..x].

Z0 = L(t1[x]) and Z1 = L(t3[10−x]) are the F2-cut labels, each with b = 1. x ≠ u, since c1 is F1-cut.

**(i) w's G2-W is t3[dw] with 1 ≤ dw ≤ 9 − x, so x ≤ 8.**
- w's G2-W lies in Q0, and t1[1..u] carries S.
- If x < u, every t1-vertex of Q0 is an arm vertex.
- If x > u, compare Q1 with R1. They share t1[x..ℓ1−1] and b3, so

  L(t3[10−x..ℓ3−1]) = L(t1[u..x−1]) ∪ L(R1's positions P1+1..20).

  A G2-W on t1[u+1..x−1] would therefore put w on t3[10−x..ℓ3−1]. But w has no t3-vertex there.

**(ii) The exchanges for x > u.**
- Q0 against R0 (the arm exchange): L(t1[u+1..x] ∪ t3[1..10−x]) = {w} ∪ T_int.
- Q1 against R1 is the identity in (i).
- So Z0, Z1 ∈ T_int. Z1 has a vertex at one of R1's positions P1+1..20. That vertex is an S_12 t2-vertex, or, only when P2 ≤ 19, possibly a P− Λ-vertex. c1's second G2-vertex lies in t3[11−x..ℓ3−1].

**(iii) The exchanges for x < u.**
- Q0 against R0: L(t3[1..10−x]) = {w} ∪ T_int ∪ L(t1[x+1..u]).
- Q1 against R0, which shares t1[x..u]: L(t3[10−x..ℓ3−1] ∪ t1[u+1..ℓ1−1]) = {v} ∪ T_int ∪ L(t1[1..x−1]).
- Z0 is an S-label whose only G2-vertex is its arm vertex t1[x].

**(iv) Lemma R7C** applies whenever ℓ2 ≤ 15.

## 3. Result

**WRITTEN:**
- Lemma R7C.
- The reductions (i)–(iv) for type 12 with r2 = 2, c′ = 0 and b3 inside Q1, and for type 2 by the mirror (v160 §1).

No new exclusion is claimed. The case stays OPEN.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2, c′ = 0 and 10 − x < ℓ3 < 20 − x, in the reduced form above;
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
