# Original Tuscan-2(11), entire m = 9 distance-two branch, part 73: L1 type 12 with r2 = 3, c′ = 0 and n1 = 2 (and its type-2 mirror) is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-types12-2-r2eq4-closed-v185.md` (SHA256 `fb4c5f0ec9763615d80e7ffc590f05d4aee4dc7544f7638a628aff9af3a210ac`) and uses the type-12 setting of v185 §1. Imports:
- v117: the setting and Lemma OL (SHA256 `77faa481d25f322fffd2d68fc12f9441ae52bbc1e315a9a52685f72378842e96`);
- v152: the anatomy and (K-w) (SHA256 `62e80ecc4878699ad5edd15e9198a0f474eb8c9490c9e870a6dbfe611ee2a18f`);
- v160 §1: the type-2/type-12 mirror (SHA256 `3597c7633dcbf620c46f532ef3f7ba38e42627f029a738c4119bb3b96e888cff`);
- v165 §1: Lemma DP★ (SHA256 `17742d50676579486b49d783c8d589765f1d8013bc3f2ec14c79c7f2b32e657a`);
- v176 §1: Lemma A4 and (E) (SHA256 `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021`);
- the grid lemma (v184 §2, SHA256 `cc0f130b350b434119cfc43806a961b1c671f4416b3b5fdc495e079c79db5532`).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared.

## 1. Data of type 12 with r2 = 3

**Lengths.**
- F2 = S_31 has ℓ1 + ℓ3 = 30 positions.
- F1 has 80, so ℓ2 + λ = 15 + u. The arm needs λ ≥ u + 1.
- u ≥ 4 (A4), and ℓ1, ℓ3 ≤ 26 (OL).

**F1 positions.**
- P1 = 10 − u + ℓ1 (b3), P2 = P1 + ℓ2 (b6), P3 = 25 + ℓ1 (b6), P4 = P3 + ℓ2 (b3), P5 = 55 + ℓ2 (b6).
- t1[j] lies at 10 − u + j and t3[j] at P5 − j.
- R0 = ℓ, T_int, b6, t1[1..u], and c1 = L(t1[u]) is cut at 10.

**F2 offsets.** b6 at 0, t3[j] at j, b3 at ℓ3, t1[j] at 30 − j.

**w.** By (K-w), w has G2-W's = r2 − 1 = 2, so w = {ℓ, b3, two G2-W's on t1 or t3, one G1-W}.

**The case.** c′ = 0 and n1 = 2, so v's two V's lie on t1, n2 = n3 = nΛ = 0, and c = 1.

## 2. F2

v has no F2-cut, so its three F2 passages b6, t1V and t1V lie inside the three F2-rows Q0 = [−x, 10 − x] ∋ b6, Q1 and Q2, with 1 ≤ x ≤ 9.

Both t1V's follow b3 in F2, so b3 lies in Q0 or Q1. If b3 lay in Q0, then Q1 and Q2 would be consecutive pure t1-rows, which Lemma DP★ excludes (t1's other pass is in F1, in the opposite direction). So:
- b3 lies inside Q1;
- Q2 = t1[x..x+10] is a pure t1-row whose ends lie on F2-cuts.

**Grid.** Q2 occupies F1 positions 10 − u + x..20 − u + x. Its end labels are F2-cut, hence not F1-cut, and x ≠ u (c1 is F1-cut). Comparing Q2 with the two F1-rows meeting at the F1-cut inside leaves pieces of |x − u| and 10 − |x − u| vertices. So **|x − u| ∈ [4,6]**.

## 3. F1

v's F1 passages are b6 (R0), the two t1V's, P2, P3, P5 and b6 (R7). The five middle passages p1 < … < p5 cover R1..R6 with exactly one cut. If the cut is p_k, it sits at 10(k + 1), p_i lies in R_i for i < k, and p_i lies in R_{i+1} for i > k. Here p4 = P3 = 25 + ℓ1.

**k ≤ 3.** P3 ∈ R5, so ℓ1 ≥ 26. By OL, ℓ1 = 26 and ℓ3 = 4.
- b3 ∈ Q1 gives 10 − x < 4, so x ≥ 7.
- P1 = 36 − u. If u ≤ 5, then P1 ≥ 31, and R1 and R2 are consecutive pure t1-rows, which DP★ excludes. If u = 6, b3 sits on the cut 30.
- So u ≥ 7, and |x − u| ≤ 2, contradicting §2.

**k = 4.** P3 = 50, so ℓ1 = 25, ℓ3 = 5 and x ≥ 6.
- P1 = 35 − u. If u = 4, DP★ applies to R1 and R2. If u = 5, b3 sits on 30.
- So u ≥ 6, and |x − u| ≤ 3, contradicting §2.

**k = 5.** v's cut is P5 = 60, so ℓ2 = 5 and λ = 10 + u. Also P2 = P3 − λ = 15 + ℓ1 − u ∈ R3, so ℓ1 ≥ 16 + u ≥ 20.
- **P1 ∈ R2.** The second t1V lies in R2, so P1 ≥ 22, and R1 = t1[u..u+10] is pure. If P1 ≥ 31, then R2 would be pure too and DP★ applies. So P1 ∈ [22,29].
- **P4 ∈ R5.** P4 = P3 + 5 = 30 + ℓ1 ≥ 50. Since 50 is a cut, P4 ∈ R5.
- **w's two G2-W's.** In F2, w's b3 lies in Q1, so its two G2-W's lie one in Q0 and one in Q2.
  - **The Q2-W** is an interior t1[j]. It is not on the arm (S-labels), not on the cuts 10 and 20, and not in R2, which holds b3. So it lies in R1.
  - **The Q0-W.** Q0 = t1[x..1], b6, t3[1..10−x], and the ends of Q0 are F2-cuts. A t1-vertex of Q0 is either on the arm or lies in R1, which is already taken. So the Q0-W is t3[j′] with 1 ≤ j′ ≤ 9 − x, at F1 position 60 − j′ ∈ [51 + x, 59], in R5.
- **Contradiction.** R5 then holds both b3 (at P4) and the Q0-W, so w appears twice in R5.

Every k is impossible.

## 4. Result

**WRITTEN:** L1 type 12 with r2 = 3, c′ = 0 and both V's of v on t1 is impossible. By the mirror (v160 §1: type 12's t1 corresponds to type 2's t2), **L1 type 2 with r2 = 3, c′ = 0 and both V's of v on t2 is impossible**.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 = 2;
- types 2 and 12 with r2 = 3, except the case closed here;
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
