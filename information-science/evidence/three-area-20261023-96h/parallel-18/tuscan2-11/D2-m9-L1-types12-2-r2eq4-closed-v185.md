# Original Tuscan-2(11), entire m = 9 distance-two branch, part 72: L1 types 12 and 2 with r2 = 4 are closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-consolidated-status-L1-type7-type8r5-types1-11r6-closed-atlas-v184.md` (SHA256 `cc0f130b350b434119cfc43806a961b1c671f4416b3b5fdc495e079c79db5532`). Operative imports:
- v117 §§1–3: the setting, H with t + ℓ1 + ℓ2 + ℓ3 + λ = 55 edges, the faces of type 12, and Lemma OL (every thread and loop has length ≤ 26) (SHA256 `77faa481d25f322fffd2d68fc12f9441ae52bbc1e315a9a52685f72378842e96`);
- v152 §§1–2: the anatomy (G3 = ∅: an F1-cut label has a = 5 − r2 and b = r2; an F2-cut label has a = 6 − r2 and b = r2 − 1), and (K-w) (SHA256 `62e80ecc4878699ad5edd15e9198a0f474eb8c9490c9e870a6dbfe611ee2a18f`);
- v160 §1: type 2 is the row-reversal mirror of type 12 (SHA256 `3597c7633dcbf620c46f532ef3f7ba38e42627f029a738c4119bb3b96e888cff`);
- v165 §1: Lemma DP★ (SHA256 `17742d50676579486b49d783c8d589765f1d8013bc3f2ec14c79c7f2b32e657a`);
- v176 §1: Lemma A4 (u ≥ 4) and exactness (E) (SHA256 `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021`);
- the arm exchange (v173 §2, SHA256 `0f399e93d91f26c7f5b0e7e9d8614601e84668f0b053360151e6a95f59ab93d8`);
- the grid lemma (v184 §2).

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. Every variable stays free until the deductions below.

## 1. Data of type 12 with r2 = 4

**Rotation, faces and groups.**
- The rotation is (T, t1, t3, Λ+, t2, Λ−), so h1 = t1 and h5 = Λ−.
- F1 = S_T S_12 P− S_23 P+ and F2 = S_31.
- G1 = {T, t2, Λ} and G2 = {t1, t3}; G3 = ∅.

**v and lengths.**
- r2 = 1 + n1 + n3 + c′ = 4 and n1 + n2 + n3 + nΛ = 2. So c′ = 1 (v's cut is in F2), n1 + n3 = 2 and n2 = nΛ = 0.
- F2 has ℓ1 + ℓ3 = 40 positions. F1 has 70, so ℓ2 + λ = 5 + u.
- The Λ-arm Λ[λ−u..λ−1] needs λ ≥ u + 1, so ℓ2 ≤ 4.
- u ≥ 4 by Lemma A4, and ℓ1, ℓ3 ≤ 26 by Lemma OL.

**F1 positions** (with t = 10 − u):
- ℓ at 0; T_int at 1..9 − u; b6 at 10 − u.
- t1[j] at 10 − u + j; b3 at P1 = 10 − u + ℓ1.
- t2[j] at P2 − j; b6 at P2 = P1 + ℓ2.
- P−: Λ[k] at P3 − k, with b6 at P3 = 15 + ℓ1.
- t2[j] at P3 + j; b3 at P4 = P3 + ℓ2.
- t3[j] at P5 − j, with b6 at P5 = 55 + ℓ2.
- P+: Λ[k] at P5 + k; b6 at 60 + u; T_int at 61 + u..69; ℓ at 70.

The rows R0 and R6 are R0 = ℓ, T_int, b6, t1[1..u] and R6 = Λ[λ−u..λ−1], b6, T_int, ℓ. c1 = L(t1[u]) is cut at 10 and c5 = L(Λ[λ−u]) at 60. Since P5 ∈ [56,59], P5 lies in R5.

**F2 offsets:** b6 at 0 ≡ 40; t3[j] at j; b3 at ℓ3; t1[j] at 40 − j.

**Anatomy.**
- An F1-cut label has a = 1 and b = 4; an F2-cut label has a = 2 and b = 3.
- An S-label's Λ-arm vertex is a G1-vertex, so an F1-cut S-label has no other G1-vertex.
- By (K-w), w consists of ℓ, b3 and three G2-W's on t1 or t3.

**v in F1.** c = 0, so v's seven F1 passages lie in seven different rows, one in each. These passages are: b6 at 10 − u, its V's on t1, b6 at P2, b6 at P3, its V's on t3, b6 at P5, and b6 at 60 + u.

## 2. Pair-completeness

H has 55 edges, every edge joins two different labels, and by (E) different edges carry different label pairs. Since there are C(11,2) = 55 label pairs:

**(PC)** Every pair of different labels is joined by exactly one H-edge. Equivalently, for each label X, the H-neighbours of X's vertices carry each other label exactly once.

## 3. The F2-rows and Lemma DP★

**Case (i): b6 lies inside an F2-row.** Write Q0 = [−x, 10 − x] (1 ≤ x ≤ 9), Q1 = [10 − x, 20 − x], Q2 = [20 − x, 30 − x] and Q3 = [30 − x, 40 − x]. Every F2-row other than Q0 and the row containing b3 is a pure t3- or t1-row, and these threads have their other pass in F1, in the opposite direction. So b3 must lie inside Q2:
- if b3 lay in Q1, then Q2 and Q3 would be consecutive pure t1-rows;
- if b3 lay in Q3, then Q1 and Q2 would be consecutive pure t3-rows;
- if b3 lay in Q0, then Q1..Q3 would all be pure rows.

In each of these, Lemma DP★ applies. Hence Q1 = t3[10−x..20−x], Q3 = t1[x..x+10], and 20 − x < ℓ3 < 30 − x.

**Case (ii): b6 is v's F2-cut.** The F2-rows are Q0 = [0,10], Q1 = [10,20], Q2 = [20,30] and Q3 = [30,40], and b6 lies in Q0 and Q3.

## 4. (n1, n3) = (2,0)

- **The lengths.** v's F1 order puts the two t1V's in R1 and R2 and P3 in R4. So ℓ1 = P3 − 15 ≥ 26, hence ℓ1 = 26 (OL) and ℓ3 = 14. Then P1 = 36 − u.
- **u ≤ 6.** If u ≤ 5, then P1 ≥ 31 and R1 = t1[u..u+10], R2 = t1[u+10..u+20] are consecutive pure t1-rows, which Lemma DP★ excludes. If u = 6, b3 sits on the cut 30.
- **Case (i) with u ≥ 7.** By §3, Q1 = t3[10−x..20−x] is a pure t3-row whose ends are t3-vertices. v has no V on t3, so Q1 contains no v-passage. Contradiction.
- **Case (ii) with u ≥ 7.** b3 (offset 14) lies in Q1, so Q2 = t1[10..20] is a pure t1-row. Its ends lie on F2-cuts and occupy F1 positions 20 − u..30 − u. The only F1-cut inside is 20. Comparing Q2 with R1 leaves t1[u+11..20] and a path of the same size 10 − u ∈ {1,2,3}, which is excluded by "one cut per label" and (E). Contradiction.

## 5. (n1, n3) = (0,2)

- **The lengths.** v's F1 order puts P2 in R1, P3 in R2 and the t3V's in R3 and R4. So ℓ1 = P3 − 15 ≤ 14, hence ℓ3 = 26 (OL) and ℓ1 = 14.
- **Case (i).** Q3 is a pure t1-row and v has no V on t1, so Q3 contains no v-passage. Contradiction.
- **Case (ii): ℓ2 = 1.** Q1 = t3[10..20] is a pure t3-row with F2-cut ends. It occupies F1 positions 35 + ℓ2..45 + ℓ2, and the only F1-cut inside is 40. Comparing it with R4 leaves paths of 5 − ℓ2 vertices, so 5 − ℓ2 ∉ {1,2,3} and ℓ2 = 1.
- **Case (ii): the contradiction.** With ℓ2 = 1 we get λ = 4 + u, P2 = 25 − u ∈ R1 (so u ≥ 6) and P1 = 24 − u. Hence R1 = t1[u..13], b3, b6, Λ[...]. R1 shares t1[u..10] and the vertex b6 with Q3 = t1[10..1], b6. Comparing them gives L(t1[1..u−1]) = L(t1[11..13]) ∪ {w} ∪ L(R1's Λ-part). But t1[1..u−1] lie on the arm and carry S-labels, and w ∉ S. Contradiction.

## 6. (n1, n3) = (1,1), case (i)

v's F1 order gives t1V ∈ R1, P2 ∈ R2, P3 ∈ R3 and t3V ∈ R4. Hence ℓ1 = P3 − 15 ∈ [16,24]. Since b3 lies in Q2, ℓ3 < 30 − x, so ℓ1 ≥ 11 + x.

**The two grid conditions.**
- **Q3 against F1.** Q3 = t1[x..x+10] is a pure row with F2-cut ends, at F1 positions 10 − u + x..20 − u + x. Comparing it with the two F1-rows meeting at the F1-cut inside gives **|x − u| ∈ [4,6]**.
- **Q1 against F1.** Q1 = t3[10−x..20−x] lies at F1 positions 35 + ℓ2 + x..45 + ℓ2 + x. The F1-cut inside is 40 or 50. With 40, the first piece would have 5 − ℓ2 − x ≤ 3 vertices. So it is 50, and **ℓ2 + x ∈ [9,11]**. In particular x ≥ 5.

**x < u.** Then u ≥ x + 4 ≥ 9, so u = 9 and x = 5. Hence ℓ2 = 4, λ = 10, t = 1 (ℓ is adjacent to b6), T_int = ∅ and the arm is all of Λ[1..9].
- **w's three G2-W's.** By R0 against Q0, w ∈ L(t3[1..5]). w is not on the cut t3[5], and not on t3[1], which would give a second w–v edge besides ℓb6 (PC). So w lies on t3[2..4], in R5. By Q3 against R0, w lies on t1[10..14], in R1. By Q1 against R5, w lies on t3[10..14], in R4.
- **ℓ1 = 20.** b3 must therefore supply R2 and R3: P1 = 1 + ℓ1 ≥ 21 and P4 = 19 + ℓ1 ≤ 39. So ℓ1 = 20.
- **R2 against R3.** Then R2 = t1[19], b3, t2[3..1], b6, Λ[9..5] and R3 = Λ[5..1], b6, t2[1..3], b3, t3[19]. Removing their common vertices leaves {t1[19], Λ[6..9]} and {Λ[1..4], t3[19]}, which carry equal labels. The nine arm labels are distinct, so the four labels of Λ[6..9] would have to lie in {L(t3[19])}. **Impossible.**

**x > u.** Then x ∈ {8,9} and u ∈ {4,5}. Also P1 = 10 − u + ℓ1 ≥ 21 + (x − u) > 21, so R1 = t1[u..u+10] is a pure t1-row and b3's first F1 passage lies in R2 (P1 < P2 ≤ 29).
- **v's F2-cut.** If v's F2-cut were t1V = t1[x+10] (between Q2 and Q3), it would lie at F1 position 20 + (x − u) ≥ 24, outside R1. So v's F2-cut is t3V = t3[20 − x], and t1V = t1[j1] lies inside Q3 ∩ R1, with j1 ∈ [x+1, u+9].
- **P4 ∈ R3.** If P4 lay in R4, then R3 would consist of Λ, b6 and t2 only, so it could not contain w.
- **w's vertices.** Hence b3 supplies R2 and R3, and w's three G2-W's supply R1 (a t1-W), R4 (a t3-W, since R4 is pure t3) and R5 (a t3-W). In F2, w's b3 lies in Q2, so its W's lie in Q0, Q1 and Q3:
  - the t1-W is the only one that can lie in Q3;
  - the R4-W is t3[j] with j ≥ 6 + ℓ2 > 10 − x, so it lies in Q1, since Q2 already holds b3;
  - the R5-W is t3[j] with j ≤ 4 + ℓ2, and must lie in Q0, so j ≤ 9 − x.

  This forces **x = 8, u = 4 and w = L(t3[1])**. Then ℓ2 ≤ 3, and the F2-cuts are 2, 12, 22 and 32.
- **T_int.** By the arm exchange on Q0 = t1[8..1], b6, t3[1..2], we get L(t1[5..8] ∪ t3[1..2]) = {w} ∪ T_int. So T_int = L(t1[5..8]) ∪ {L(t3[2])}, and L(t1[8]) and L(t3[2]) are F2-cut.
- **The four F2-cut labels.** Comparing R1 = t1[4..14] with Q3 = t1[8..18] gives L(t1[15..18]) = {c1} ∪ L(t1[5..7]). So L(t1[18]), the F2-cut at 22, lies in T_int. The four F2-cut labels are therefore v, L(t3[2]), L(t1[8]) and L(t1[18]), and the other two T_int-labels, τa and τb, lie on t1[5..7] and are F1-cut.
- **Where τa and τb are cut.** X20 = L(t1[14]) is not one of t1[5..8]'s labels (R1 holds each label once), so τa, τb ≠ X20. Position 30 lies on Λ (P2 ≤ 29 < 30 < P3), and an F1-cut T_int-label has no G1-vertex besides T. So τa and τb are X40 = L(t3[15+ℓ2]) and X50 = L(t3[5+ℓ2]).
- **Their vertices.** Each has T, a t1-vertex on t1[5..7] (in R1), a t1-vertex in R2 (t1[15..ℓ1−1]) and two t3-vertices:
  - τa: its cut t3[15+ℓ2], and a t3-vertex in R5, which is t3[j] with 2 ≤ j ≤ 4 + ℓ2;
  - τb: its cut t3[5+ℓ2], and a t3-vertex in R3, which is t3[j] with j ≥ P5 − 39 = 16 + ℓ2.
- **(PC) at v.** v's vertices are b6, t1[j1] with j1 ∈ [9,13], and t3[12]:
  - b6's neighbours are T's last vertex, t1[1], t2[1] (or b3), t3[1], Λ[1] and Λ[λ−1];
  - t1[j1]'s neighbours lie on t1[8..14];
  - t3[12]'s neighbours are t3[11] and t3[13].

  None of τa's or τb's t1- or t3-vertices is among these. So τa and τb could each meet v only through T's last vertex, a single vertex with one label. **(PC) fails.**

## 7. (n1, n3) = (1,1), case (ii)

**The rows.** Q0 = b6, t3[1..10] and Q3 = t1[10..1], b6. In F2, t3V precedes b3 and b3 precedes t1V, so t3V lies in Q1 and t1V in Q2.

**ℓ2 = 1.** R5 = t3[5+ℓ2..1], b6, Λ[1..5−ℓ2]. Comparing it with Q0 leaves t3[6+ℓ2..10] and Λ[1..5−ℓ2], with 5 − ℓ2 vertices each:
- 5 − ℓ2 = 1 would put c5 on the F2-cut t3[10];
- 5 − ℓ2 ∈ {2,3} contradicts (E).

So ℓ2 = 1. Then λ = 4 + u, the arm is Λ[4..3+u], P2 = P1 + 1, P3 = 15 + ℓ1, P4 = 16 + ℓ1 and P5 = 56.

**b3 lies in Q1.**
- P2 ∈ R2 and P3 ∈ R3, so position 30 lies in the P− run, on Λ[P3 − 30] = Λ[ℓ1 − 15].
- X30 is F1-cut, so it has a = 1. A T_int-label would also have its T-vertex. So X30 ∈ S, and Λ[ℓ1 − 15] is its arm vertex.
- It is not Λ[4], whose label c5 is already cut at 60. Hence ℓ1 − 15 ∈ [5, 3 + u], so ℓ1 ≥ 20.
- ℓ1 = 20 would give ℓ3 = 20 and put b3 on the F2-cut 20. So ℓ1 ≥ 21, hence 11 ≤ ℓ3 ≤ 19 and b3 lies inside Q1.

**w's vertices.**
- **The F1 rows.** P1 = P2 − 1 ∈ [21,28], since 20 is a cut, and P4 = P3 + 1 ∈ [32,39], since 40 is a cut. So w's F1 passages ℓ (R6, R0), b3 at P1 (R2) and b3 at P4 (R3) leave R1, R4 and R5 to its three G2-W's.
- **The two t3-W's.** R4 = t3[16..6] is a pure t3-row, and R5 = t3[6..1], b6, Λ[1..4] has no t1-vertex. So w has a t3-W t3[j] in R4, with 7 ≤ j ≤ 15, and a t3-W t3[j′] in R5, with 1 ≤ j′ ≤ 5 (t3[6] carries the cut X50).
- **The F2 rows.** w's F2 passages are b3 in Q1 and one per W. t3[j′] lies in Q0. t3[j] lies in Q0 (j ≤ 9) or in Q1 (j ≥ 11), and j = 10 is an F2-cut. Both Q0 and Q1 already contain w. **Contradiction.**

So case (ii) is impossible.

## 8. Type 2, and result

Row reversal maps type 2 to type 12 and keeps r1, r2 and u (v160 §1), so type 2 with r2 = 4 is impossible as well.

**WRITTEN:** L1 types 12 and 2 with r2 = 4 are impossible for every allowed value of every variable.

**OPEN (m = 9, L1):**
- types 2 and 12 with r2 ∈ {2,3};
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
