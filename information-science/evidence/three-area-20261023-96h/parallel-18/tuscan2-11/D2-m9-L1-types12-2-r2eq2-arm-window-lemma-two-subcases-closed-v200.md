# Original Tuscan-2(11), entire m = 9 distance-two branch, part 87: L1 types 12 and 2 with r2 = 2 — the arm-window lemma, two sub-cases closed, and the window reduction for c′ = 1

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq3-alpha3-k1-closed-r2eq3-closed-v199.md` (SHA256 `b1832cc493277e538fdf38c0db39d6ddaaafeddb1e47d043e90d870b1c57b70f`) and starts the open cell r2 = 2.

Imports:
- v117 §§1–3: the setting and exactness (E) (SHA256 `77faa481d25f322fffd2d68fc12f9441ae52bbc1e315a9a52685f72378842e96`);
- v152: the anatomy, with G3 = ∅ (SHA256 `62e80ecc4878699ad5edd15e9198a0f474eb8c9490c9e870a6dbfe611ee2a18f`);
- v160 §1–§2: the mirror, Lemma 2R and Corollary 2R (SHA256 `3597c7633dcbf620c46f532ef3f7ba38e42627f029a738c4119bb3b96e888cff`);
- v165 §2: the type-12, r2 = 2 data (SHA256 `17742d50676579486b49d783c8d589765f1d8013bc3f2ec14c79c7f2b32e657a`);
- v176 §1: Lemma A4 (SHA256 `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021`).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. It uses (R1)–(R2) only.

## 1. Data of type 12 with r2 = 2

**Lengths.**
- F1 = S_T S_12 P− S_23 P+ has 90 positions, and F2 = S_31 has 20. So ℓ1 + ℓ3 = 20 and λ = 25 + u − ℓ2.
- u ≥ 4 (A4), ℓ1 ≤ u + 9 (Corollary 2R) and ℓ2 ≥ 5 (v165).

**F1 positions.**
- ℓ at 0; T_int at 1..9 − u; b6 at 10 − u.
- t1[j] at 10 − u + j; b3 at P1 = 10 − u + ℓ1 ∈ [11,19], in R1.
- t2[j] at P2 − j, with P2 = P1 + ℓ2; Λ[k] at P3 − k, with P3 = 35 + ℓ1.
- t2[j] at P3 + j; b3 at P4 = P3 + ℓ2; t3[j] at P5 − j, with P5 = 55 + ℓ2.
- Λ[k] at P5 + k; b6 at 80 + u; T_int; ℓ at 90.
- R0 = ℓ, T_int, b6, t1[1..u], and S = L(t1[1..u]). The t1-run of F1 starts at b6 (10 − u) and runs without a break up to b3 (P1).

**F2.**
- Offsets: b6 at 0 ≡ 20; t3[j] at j; b3 at ℓ3; t1[j] at 20 − j.
- There are two rows, Q0 = [−x, 10 − x] and Q1 = [10 − x, 20 − x], with 0 ≤ x ≤ 9.
- By Lemma 2R, an F2-cut label has exactly one F2-passage, so b = 1. Every other label other than v and w has b = 2, with one G2-vertex in each F2-row.

**v.**
- r2 = 1 + n1 + n3 + c′ = 2.
- If c′ = 1, v's only F2-vertex is b6, so b6 sits on the F2-cut 0 (x = 0) and n1 = n3 = 0.
- If c′ = 0, then x ≥ 1, v has one G2-V (on t1 or t3) and one G1-V, and v's cut is in F1.

## 2. The arm-window lemma

**Lemma AW.** In type 12 with r2 = 2, no F2-row equals b6, t1[1..10] (in either order), and none equals t1[x..x+10] with x ≥ 1.

**Proof.**
- **The window.** Such a row consists of b6 at 10 − u followed by t1[1..10], or of t1[x..x+10]. These vertices are consecutive in F1, so they form an F1-window W = [s, s+10], with s = 10 − u or s = 10 − u + x. Being an F2-row, W carries every label once.
- **The lengths.**
  - The first form needs ℓ1 ≥ 11.
  - The second form needs ℓ1 ≥ x + 11. Since ℓ1 ≤ u + 9, this gives x ≤ u − 2.
  - In both forms 1 ≤ s ≤ 9, so W meets R1 = [10,20] in [10, s+10].
- **The exchange.** Hence L(W ∖ R1) = L(R1 ∖ W).
  - W ∖ R1 = [s, 9] consists of b6 and t1-arm vertices of index ≤ u − 1, or of t1-arm vertices t1[x..u−1] alone. So L(W ∖ R1) ⊆ {v} ∪ S.
  - R1 ∖ W = [s+11, 20] contains b3: P1 = 10 − u + ℓ1 ≥ s + 11 by the length condition, and P1 ≤ 19.
- So w ∈ {v} ∪ S, which is false because w ∉ S. ∎

## 3. Two sub-cases closed

**(a) c′ = 1 and ℓ3 ≤ 9.**
- Here x = 0, and ℓ3 ≠ 10 since b3 is never on a cut.
- With ℓ3 ≤ 9, the offsets 10..19 are t1[10..1], so Q1 = t1[10..1], b6.
- Lemma AW excludes this.

**(b) c′ = 0 and ℓ3 < 10 − x.**
- Here Q1 = [10 − x, 20 − x] lies above b3, so Q1 = t1[x..x+10].
- Lemma AW excludes this.

So when c′ = 0, either b3 lies inside Q1 (10 − x < ℓ3 < 20 − x), or ℓ3 > 20 − x and Q1 = t3[10−x..20−x] is a pure t3-row.

## 4. c′ = 1 and ℓ3 ≥ 11: the window reduction

Here ℓ1 ≤ 9, so u ≤ 8, and the F2-rows are Q0 = b6, t3[1..10] and Q1 = t3[10..ℓ3−1], b3, t1[ℓ1−1..1], b6.

**The labels.**
- Z := L(t3[10]) is the only F2-cut label other than v. Since b(Z) = 1 and every S-label has a G2 t1-arm vertex, Z is a T_int-label.
- Every label other than v and Z has exactly one vertex in t3[1..9]. In particular w's G2-W lies there, and each S-label has G2 = {its t1-arm vertex, a vertex of t3[1..9]}.

**The window W.**
- In F1, t3[10..1], b6 is the window W = [P5 − 10, P5], which carries every label.
- If W were an F1-row, v and Z would also be F1-cut. So W contains exactly one F1-cut C strictly inside it. Put e = P5 − C and let Ra and Rb be the rows ending and starting at C.
- **Pieces of size 1.**
  - e = 1 puts v on the F1-cut C − 10.
  - 10 − e = 1 puts Z on Λ[1], at the F1-cut C + 10.
- **Pieces of size 2 or 3.** The pieces are:
  - W ∖ Ra = t3[e−1..1], b6;
  - W ∖ Rb = t3[e+1..10];
  - Ra ∖ W, a path inside S_23 or t3;
  - Rb ∖ W = Λ[1..10−e].

  These paths would repeat a label pair on a second H-edge, against (E).
- Hence **e ∈ {4,5,6}**, so C = 60 with **ℓ2 ∈ {9,10,11}**, or C = 70 with **ℓ2 ∈ {19,20,21}**.

**The two exchanges.**
- **(Rb)** L(Λ[1..10−e]) = {Z} ∪ L(t3[e+1..9]).
- **(Ra)** L(t3[1..e−1]) ∪ {v} = L(positions C−10..P5−11).
  - Those positions lie above P3 = 35 + ℓ1 ≤ 44. v has no t3-vertex, so v must have a V on t2 in S_23 inside them. This forces **ℓ3 ≤ e + 9**.
  - b3 (at P4 = P5 − ℓ3) then lies inside them, so **w = L(t3[d]) with 1 ≤ d ≤ e − 1**.

## 5. Type 2

Row reversal maps type 2 to type 12 and exchanges t1 with t2 (v160 §1). §§2–4 therefore hold for type 2 with r2 = 2, with t1 and t2 exchanged.

## 6. Result

**WRITTEN:**
- Lemma AW.
- L1 type 12 with r2 = 2 is impossible when c′ = 1 and ℓ3 ≤ 9, and when c′ = 0 and ℓ3 < 10 − x. The same holds for type 2 by the mirror.
- When c′ = 1 and ℓ3 ≥ 11: ℓ2 ∈ {9,10,11,19,20,21}, e ∈ {4,5,6}, ℓ3 ≤ e + 9, w = L(t3[d]) with d ≤ e − 1, and the exchanges (Ra), (Rb).

**OPEN (m = 9, L1):**
- Types 2 and 12 with r2 = 2:
  - c′ = 1 with ℓ3 ≥ 11, in the reduced form of §4;
  - c′ = 0 with b3 inside Q1, or with ℓ3 > 20 − x;
  - each also restricted by v160 and v165.
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
