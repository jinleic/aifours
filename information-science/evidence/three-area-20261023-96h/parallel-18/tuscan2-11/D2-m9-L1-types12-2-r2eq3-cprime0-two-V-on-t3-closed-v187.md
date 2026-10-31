# Original Tuscan-2(11), entire m = 9 distance-two branch, part 74: L1 type 12 with r2 = 3, c′ = 0 and n3 = 2 (and its type-2 mirror) is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq3-cprime0-two-V-on-long-G2-thread-closed-v186.md` (SHA256 `bda6949e0fcd829dd3a7c31307220f3a3b515d6ab4e7f5b6e7f42103413610c4`) and uses its §1 data (type 12, r2 = 3), with the same imports (v117, v152, v160, v165, v176, v184, and the arm exchange of v173 §2).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. The case and F2

c′ = 0 and n3 = 2, so both V's of v lie on t3, n1 = n2 = nΛ = 0 and c = 1. In F2, v's passages b6, t3V₁ and t3V₂ lie inside Q0 = [−x, 10 − x] ∋ b6, Q1 ∋ t3V₁ and Q2 ∋ t3V₂, in that order. Both t3V's precede b3, so b3 lies inside Q2.
- **Q1.** Q1 = t3[10−x..20−x] is a pure t3-row with F2-cut ends.
- **Q0.** Since b3 lies inside Q2, ℓ3 < 30 − x, i.e. x < ℓ1. So Q0 = t1[x..1], b6, t3[1..10−x], and its lower end is t1[x]. Moreover x ≠ u, since c1 = L(t1[u]) is F1-cut.

**Grid.** Q1 occupies F1 positions P5 − 20 + x..P5 − 10 + x = 35 + ℓ2 + x..45 + ℓ2 + x, and exactly one F1-cut lies inside. If it is 40, the first piece has 5 − ℓ2 − x ≤ 3 vertices, which is impossible. If ℓ2 + x < 15, the cut must therefore be 50, and **ℓ2 + x ∈ [9,11]**. (The grid is used only in §4 with u = 4, where ℓ2 = 14 − ℓ1 and x < ℓ1 ≤ 8, so ℓ2 + x ≤ 13.)

## 2. F1: where v's cut lies

v's middle F1 passages are p1 = P2, p2 = P3, p3 = t3V₂, p4 = t3V₁ and p5 = P5 (t3[j] lies at P5 − j). They cover R1..R6 with one cut p_k.
- **k ≥ 3.** Then P3 = 25 + ℓ1 ∈ R2, so ℓ1 ≤ 4 < u + 1. Impossible.
- **k = 2.** Then P3 = 30, so ℓ1 = 5 and u = 4.
- **k = 1.** Then P2 = 20, P3 ∈ R3, t3V₂ ∈ R4, t3V₁ ∈ R5 and P5 ∈ R6.

**Key fact (F2-cut S-labels).** An F2-cut label has b = 2. If R4 and R5 are both pure t3-rows, an F2-cut S-label (one G2-vertex on its t1-arm) needs one t3-vertex in each of them, and none on the cut 50. That makes b ≥ 3, which is impossible.

## 3. k = 2

Here ℓ1 = 5, u = 4, ℓ3 = 25, P1 = 11, and P2 = 11 + ℓ2 ∈ R1. Since P5 = 55 + ℓ2 ∈ R6, ℓ2 ∈ [6,8]. Then P4 = 30 + ℓ2 ≤ 38, so R4 and R5 lie inside the t3-run P4 + 1..P5 − 1 and are pure t3-rows.

b3 sits at offset 25 inside Q2, so x ≤ 4 and x ≠ 4. So t1[x], x ≤ 3, is an arm vertex on an F2-cut, and its label is an F2-cut S-label. By the key fact, this is impossible.

## 4. k = 1

**The lengths.** λ = P3 − 20 = 5 + ℓ1 and ℓ2 = 15 + u − λ = 10 + u − ℓ1. P5 ∈ R6 gives ℓ2 ∈ [6,14]. Also P1 = 20 − ℓ2 ∈ [11,14] ⊂ R1, and P4 = P3 + ℓ2 = 35 + u.

**R2 is pure Λ apart from b6.** R2 = b6, Λ[λ−1..λ−10], since P3 ≥ 31.

**w.**
- w's R2-passage is a Λ-W. Its P+ pass lies in R6, because R7 holds ℓ.
- w's b3 lies in Q2, so its two G2-W's lie in Q0 and Q1.
- t1's F1-run ends before P1 ≤ 14, so a t1-vertex is either on the arm or in R1, which holds b3. Hence both G2-W's are t3-vertices.
- **The Q0-W** is t3[j′] with j′ ≤ 9 − x, at F1 position ≥ P5 − 9 + x ≥ 53. R6 holds the Λ-W, so it lies in R5.
- **The Q1-W** is t3[j] with 10 − x < j < 20 − x. It must lie in R3 or R4, whichever P4 leaves free.

**u = 4.**
- u = 5 gives P4 = 40, a cut.
- If u ≥ 6, then P4 ≥ 41 lies in R4, and the Q1-W would need F1 position ≤ 39, i.e. j ≥ P5 − 39 = 16 + ℓ2 ≥ 22 > 20 − x. Impossible.
- So u = 4, P4 = 39, ℓ2 = 14 − ℓ1 and ℓ1 ∈ [6,8]. Also P5 = 69 − ℓ1 ≥ 61, so R4 = [40,50] and R5 = [50,60] are pure t3-rows.

**R1 against R3: ℓ1 ≥ 7.** R1 = t1[4..ℓ1−1], b3, t2[ℓ2−1..1], b6 and R3 = Λ[ℓ1−5..1], b6, t2[1..ℓ2−1], b3, t3[ℓ3−1]. They share b3, b6 and all of t2, so L(t1[4..ℓ1−1]) = L(Λ[1..ℓ1−5]) ∪ {L(t3[ℓ3−1])}. c1 = L(t1[4]) is cut at 10, while Λ[ℓ1−5] and t3[ℓ3−1] carry the F1-cuts 30 and 40. So c1 ∈ L(Λ[1..ℓ1−6]), and ℓ1 = 6 is impossible.

**ℓ1 ∈ {7,8}.** The grid gives x ∈ [ℓ1 − 5, ℓ1 − 3], and x ≠ 4.
- **x ≤ 3** (ℓ1 = 7 with x ∈ {2,3}, or ℓ1 = 8 with x = 3). t1[x] is an arm vertex on an F2-cut, so its label is an F2-cut S-label. R4 and R5 are pure t3-rows, so the key fact applies. Impossible.
- **x = 5, ℓ1 = 8.** Here λ = 13, P3 = 33, P5 = 61, and the arm is Λ[9..12].
  - Q0 = t1[5..1], b6, t3[1..5] holds b6 and the whole t1-arm. By the arm exchange, L(t1[5] ∪ t3[1..5]) = {w} ∪ T_int.
  - R2 = b6, Λ[12..3] and R6 = t3[1], b6, Λ[1..9]. Removing their common vertices leaves the arm vertices Λ[10..12] and {t3[1], Λ[1], Λ[2]}. So L(t3[1]) is an S-label, contrary to the arm exchange.

  Impossible.

## 5. Result

**WRITTEN:** L1 type 12 with r2 = 3, c′ = 0 and both V's of v on t3 is impossible. By the mirror (v160 §1, which exchanges t1 and t2 and keeps t3), **L1 type 2 with r2 = 3, c′ = 0 and both V's on t3 is impossible**.

Together with v186, type 12 with r2 = 3 and c′ = 0 survives only with n1 = n3 = 1, and type 2 likewise with one V on t2 and one on t3.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3: c′ = 0 with one V on each G2-thread, and c′ = 1;
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
