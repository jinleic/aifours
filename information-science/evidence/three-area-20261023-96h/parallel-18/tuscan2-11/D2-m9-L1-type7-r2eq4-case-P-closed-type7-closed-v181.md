# Original Tuscan-2(11), entire m = 9 distance-two branch, part 68: L1 type 7 with r2 = 4 — case (P) closed, so L1 type 7 is closed

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under parent direction v143. It continues `D2-m9-L1-type7-r2eq4-Q-cut30-40-closed-case-Q-closed-v180.md` (SHA256 `2f73f1ec54be8e77b7526abc95bc8e229fc6eddf0c16ced5bc4966d7d0f7180f`). Operative imports:
- v178 §§1 and 3: P3 ≤ 48 and the case list (SHA256 `a41c8e7f0fe6593befd2d88d87b3da3ea56ca4ff5196d6681f134f5896e70c78`);
- v173 §1: the F1/F2 position formulas and the arm exchange (SHA256 `0f399e93d91f26c7f5b0e7e9d8614601e84668f0b053360151e6a95f59ab93d8`);
- v152 §§1–2: the anatomy (an F1-cut label has a = 1, b = 4; an F2-cut label has a = 2, b = 3) and (K-w) (SHA256 `62e80ecc4878699ad5edd15e9198a0f474eb8c9490c9e870a6dbfe611ee2a18f`);
- v176 §1: Lemma A4 and exactness (E) (SHA256 `9d440953b7e4bc4eb2ff4972806f76f708331d5165efe31e48775864e9283021`);
- the type-7 mirror of v155 §5, exchanging t1 and t3 (SHA256 `660996ba8be146a445353c9bbb865b1fc880793ccc94bc94f9c8f2d704a1a72f`);
- for §7 only: v157 (SHA256 `458dce9de731858686a408c773870eb593a854937e2f5b1f46ac08bb40c724f2`), v177 (SHA256 `6997ee0e94802c406c350b3a6d5bf69f4872233a2bb97b1936f02b2a8f11c68c`), v179 (SHA256 `432c612df1c416a65ff411a42731aaa16d8e10405c73e8aba3408d3c73d7f228`) and v180.

It is written reasoning only: no interpreter, enumeration, solver or search was used. It is not reviewed, formal or novelty-cleared. Every variable of the case stays free until the deductions below.

## 1. Case (P) and first facts

Case (P) of v178 has c′ = 1, n1 = n2 = 1 and n3 = nΛ = 0. v's seven F1 passages, none of them a cut, are t ∈ R0, t1V ∈ R1, t2V12 ∈ R2, P2 ∈ R3, P3 ∈ R4, t2V23 ∈ R5 and P5 ∈ R6. Hence:
- P2 ∈ [31,39] and P3 ∈ [41,48] (v178 §1);
- 4 ≤ u ≤ 9 (Lemma A4, and |T_int| = 9 − u).

**w.** By (K-w), with G3 = ∅, r2 = 4 and β2 = 1, all three W's of w are G2-W's (on t1, t3 or Λ). So w has no t2-vertex.

**P1 ∈ [21,28].**
- If P1 ≤ 19, then R2 = [20,30] lies inside the S_12-run [P1 + 1, P2 − 1]. R2 would consist of t2-vertices only, and w ∈ R2 would lie on t2.
- P1 = 20 puts b3 on a cut.
- P1 is less than the position of t2V12, which is at most 29.

Consequently R1 = t1[u..u+10] is a pure t1-row, ℓ1 ≥ u + 11, and X20 := L(t1[u+10]) has its F1-cut at 20.

**P4 ∈ [52,59].** P4 = P3 + u + 5 ≥ 50, and P4 exceeds the position of t2V23, which is at least 51.

**w's vertices.** w's F1 passages are ℓ (R6 and R0), b3 at P1 ∈ R2 and at P4 ∈ R5, and the three W's, which must supply R1, R3 and R4. R1 is pure t1, R3 = t2, b6, Λ and R4 = Λ, b6, t2. So w = {ℓ, b3, a t1-W in R1, a Λ-W in R3, a Λ-W in R4}, and w has no t3-vertex.

w's F2 passages are b3 (offset 40 − ℓ1), the t1-W (offset 40 − jw, with jw ∈ [u + 1, u + 9]) and the two Λ-W's (offsets below λ).

## 2. The indices a and b

Put a = P2 − 30 ∈ [1,9] and b = 50 − P3 ∈ [2,9].
- Positions 30 and 50 lie on t2 (P1 ≤ 28 and P4 ≥ 52), so X30 = L(t2[a]) and X50 = L(t2[b]), and a ≠ b.
- Position 40 lies on Λ.

t2[j] has its passes at P2 − j = 30 + a − j and at P3 + j = 50 − b + j. Hence:
- its S_12-pass lies in R3 iff j < a, and in R2 iff j > a;
- its S_23-pass lies in R4 iff j < b, and in R5 iff j > b.

An F1-cut S-label has exactly one G1-vertex, which lies on t2 (S-labels have no T-vertex), and exactly four G2-vertices. If such a label lies in S, its t1-arm vertex lies inside R0, unless the label is c1, and its t3-arm vertex lies inside R6, unless the label is c5.

**(B-c5).** c5's four G2-vertices are:
- t3[u] (its cut at 60, covering R5 and R6);
- its t1-arm vertex (R0);
- a t1-vertex in R1 (R1 is pure t1);
- a fourth vertex q.

Its t2-vertex and q must supply R2, R3 and R4. The S_23-pass cannot be in R5, so it is in R4, and q supplies R2 or R3. **If q is a Λ-vertex, then q ∈ R3, the S_12-pass is in R2, and a < b.** Otherwise q is a t1-vertex in R2.

**(B-X20).** Suppose X20 ∈ S and X20 has a Λ-vertex. Then its four G2-vertices are t1[u+10] (its cut at 20, covering R1 and R2), its t1-arm vertex, its t3-arm vertex and the Λ-vertex. The t2-vertex and the Λ-vertex must supply R3, R4 and R5:
- the S_12-pass is not in R2, so it is in R3;
- the Λ-vertex is therefore in R4;
- the S_23-pass is in R5.

So b < j < a and **a > b**.

**(B-c1).** Suppose c1 has a t1-vertex in R2 and a Λ-vertex. Then its G2-vertices are t1[u] (its cut at 10), that t1-vertex, its t3-arm vertex and the Λ-vertex. The same reasoning puts the S_12-pass in R3, the Λ-vertex in R4 and the S_23-pass in R5, so **a > b**.

**(Λ-all).** If some F2-row consists of b6 and ten Λ-vertices, every label other than v has a Λ-vertex. By (B-c5), a < b.

## 3. The F2-cut inside R1

R1 occupies F2 offsets 30 − u..40 − u, with t1[j] at 40 − j. Its end vertices carry X20 and c1, which are F1-cut, so neither end is an F2-cut. Exactly one F2-cut offset lies strictly inside R1; write it as 40 − e and put d = e − u ∈ [1,9]. The F2-rows on either side of it are G = [40 − e, 50 − e] and G′ = [30 − e, 40 − e].

The rows on each side are compared with R1. Two rows carry the same labels, so the vertex-disjoint paths left after removing their common part carry equal label sets:
- **R1 against G′:** the two remaining paths are t1[u..e−1] and the offsets 30 − e..29 − u, with d vertices each.
  - d = 1 would put c1 on an F2-cut.
  - d = 2 or 3 contradicts (E).
- **R1 against G:** the two remaining paths are t1[e+1..u+10] and the offsets 41 − u..50 − e, with 10 − d vertices each.
  - 10 − d = 1 would put X20 on an F2-cut.
  - 10 − d = 2 or 3 contradicts (E).

Hence d ∈ {4,5,6} and e = u + d ∈ [8,15].

v's F2 passages are b6(0), b6(λ) and t1V. t1V lies at offset 40 − j1, inside R1's interval. Exactly one of the three passages is an F2-cut, every F2-row contains exactly one v-passage, and λ < 40 − ℓ1 < 40 − j1.

## 4. e ∈ {8,9}

- **Where v lies.** Since e < 10, b6(0) lies inside G. So t1V is not in G, and it lies inside G′. The rows H1 = [10 − e, 20 − e] and H2 = [20 − e, 30 − e] are then supplied only by b6(λ), which must be the cut at 20 − e. So λ = 20 − e.
- **a < b.** H1 = Λ[10−e..19−e] together with b6(λ). By (Λ-all), a < b.
- **w's passage in H2 is b3.** The t1-W lies at offset ≥ 31 − u > 30 − e, and the Λ-W's lie below λ. So w's passage in H2 = [λ, λ + 10] is b3, strictly inside the row: 40 − ℓ1 < 30 − e, so ℓ1 ≥ e + 11.
- **c1 has a t1-vertex in R2.** G′ = t1[e..e+10] is a pure row, and G′ ∖ R1 = t1[u+11..e+10] sits at F1 positions 21..20 + d, inside R2 and to the left of P1. c1 = L(t1[u]) lies in L(R1 ∖ G′) = L(G′ ∖ R1), so c1 has a t1-vertex in R2.
- **a > b.** c1 also has a Λ-vertex, by (Λ-all). By (B-c1), a > b.

This is a contradiction.

## 5. e = 10

- **Where v lies.** The F2-cuts are 0, 10, 20 and 30, so v's cut is b6(0), which supplies [30,40] and [0,10]. t1V cannot lie in [30,40], so it lies inside [20,30], and b6(λ) lies inside [10,20]. Hence λ ∈ [11,19].
- **a < b.** [0,10] = b6(0), Λ[1..10]. By (Λ-all), a < b.
- **X20 ∈ S.** G = [30,40] = t1[10..1], b6(0). Comparing R1 with G gives L(t1[11..u+10]) = L(t1[1..u−1]) ∪ {v} = (S ∖ {c1}) ∪ {v}. Hence X20 ∈ S.
- **a > b.** X20 has a Λ-vertex by (Λ-all), so (B-X20) gives a > b.

This is a contradiction.

## 6. e ∈ [11,15]

**The rows.** The F2-cuts are 50 − e, 40 − e, 30 − e and 20 − e (mod 40). In cyclic order the rows are:
- H1 = [50 − e, 60 − e], which contains offset 0;
- H2 = [20 − e, 30 − e];
- G′ = [30 − e, 40 − e];
- G = [40 − e, 50 − e] = t1[e−10..e], a pure t1-row because ℓ1 ≥ u + 11 > e.

**H1.** b6(0) lies inside H1. b6(λ) can lie neither inside H1 nor at its end 20 − e, so λ ≥ 21 − e and H1 = t1[e−10..1], b6(0), Λ[1..20−e].

**X20 ∈ L(t1[e−9..u−1]).** Comparing R1 with G gives L(t1[e+1..u+10]) = L(t1[e−10..u−1]). Here t1[e−10] sits on an F2-cut, while X20 is F1-cut.

**(★) R0 against H1.** Their common vertices are b6 and t1[1..e−10], so

L(Λ[1..20−e]) = {w} ∪ T_int ∪ L(t1[e−9..u]).

So X20 has a Λ-vertex, and **(B-X20) gives a > b.**

The passages b6(λ) and t1V supply H2, G′ and G in that order, with exactly one cut between them.

**(iii-b) λ = 30 − e is the cut, and t1V lies inside G.** Then H2 = Λ[20−e..29−e] together with b6(λ). By (Λ-all), a < b, which is a contradiction.

**(iii-a) b6(λ) lies inside H2, and t1V = t1[e] is the cut at 40 − e.**
- **ℓ1 < e + 10.** w's passage in G, which is all t1, is its t1-W. G′ contains no Λ (its offsets exceed λ) and cannot contain the t1-W again, so w's passage in G′ is b3, strictly inside: e < ℓ1 < e + 10.
- **c5's q.** Since a > b, (B-c5) rules out a Λ-vertex for q, so q is a t1-vertex t1[jq] in R2, with jq ∈ [u + 11, ℓ1 − 1]. Then c5 has no Λ-vertex.
- **c5's t1-arm vertex lies inside H1.** By (★), c5 ∉ L(t1[e−9..u]). So its t1-arm vertex t1[i5] has i5 ≤ e − 11, since i5 = e − 10 would put c5 on an F2-cut.
- **c5's R1-vertex lies inside G.** Since c5 ∉ L(t1[e−10..u−1]) = L(t1[e+1..u+10]), its R1-vertex is t1[j5] with u + 1 ≤ j5 ≤ e − 1. (j5 = e is t1V.)
- **c5's q lies inside G′.** Its offset 40 − jq lies in [41 − ℓ1, 29 − u], which is inside (30 − e, 40 − e) because ℓ1 ≤ e + 9 and d ≤ 6.
- **H2 contains the t3-arm.** c5's fourth F2-row, H2, must contain t3[u]: λ + u < 30 − e. Put g = 30 − e − λ, so g > u. Then H2 = Λ[20−e..λ−1], b6(λ), t3[1..g] contains b6(λ) and the whole t3-arm.
- **Y3 ∈ T_int.** By the arm exchange, L(Λ[20−e..λ−1] ∪ t3[u+1..g]) = {w} ∪ T_int. Y3 := L(t3[g]) sits on the F2-cut 30 − e, and w has no t3-vertex, so Y3 ∈ T_int. Here g < ℓ3, since b3 lies at offset 40 − ℓ1 > 30 − e.
- **Y3's vertices.** Y3 is an F2-cut T_int-label, so it has a T-vertex, one t2-vertex and three G2-vertices. These are t3[g], a t1-vertex in R1, and a Λ-vertex (by (★), T_int ⊆ L(Λ[1..20−e])).
- **a < b.** Y3's T-vertex supplies R0 and R6, its t1-vertex supplies R1, and t3[g] at F1 position 60 + u − g ∈ [51,59] supplies R5. So its t2-vertex and its Λ-vertex must supply R2, R3 and R4:
  - the S_23-pass is in R4, so j < b;
  - the Λ-vertex is then in R3;
  - the S_12-pass is in R2, so j > a.

  Hence a < b, which is a contradiction.

**Case (P) is impossible.** The type-7 mirror covers n3 = 1.

## 7. L1 type 7 is closed

The cases of type 7 with r2 = 4 are:
- (nΛ, n1, n3) = (2,0,0) with c′ = 0, and (1,0,0) with c′ = 1, impossible by v173;
- the c′ = 0 cases (1,1,0), (1,0,1), (0,2,0) and (0,0,2), impossible by v178;
- case (Q), impossible by v179 and v180;
- case (P) and its mirror, impossible by §§4–6.

So type 7 with r2 = 4 is impossible. For the other values of r2:
- r2 = 2 is impossible by v157;
- r2 = 3 is impossible by v177;
- r2 ≤ 4 holds by (K-w);
- r2 = 2 + n1 + n3 + nΛ + c′ ≥ 2.

**Hence L1 type 7 is impossible.**

## 8. Result

**WRITTEN:**
- Case (P) of v178 is impossible.
- Type 7 with r2 = 4 is impossible.
- L1 type 7 is closed for every allowed value of every variable.

**OPEN (m = 9, L1):**
- types 2 and 12;
- types 1 and 11 with r1 ∈ {4,5,6};
- type 8 with r1 ∈ {3,4}, and with r1 = 5 and ℓ1 − u ∈ [11,19].

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried. This candidate needs its own complete source-bound gate.
