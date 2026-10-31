# Actual Tuscan-1(11), distinct-centre 4+4, class (b), d = 3, one gap: a fresh exclusion that does not use v73 LF60

NEW exact WRITTEN CANDIDATE (owner InfoRecursiveMDS18-2, slot info-4), under Main directions v215 and v217. It answers v150b-A v2 F-10 (`peer-review-v150b-A-v2.md`, MathSun8-2) by giving a new proof of the case that F-10 leaves NR. It is not a repair of v73 §§4-8 or v74, which stay ZERO and NONINPUT.

## 0. What this proof uses and avoids

**Inputs used:**
- v73 LF1-59 only, read at that exact raw range: §1 (setting), §2 (F_2's seven rows and the parameters β′, m1, m2, m3) and §3 (m3 = β′ ± 4).
- The class-(b) face words of v57/v73 §1: F_1 = T1 L_w T1^- L_v (4 rows), F_2 = T2 L_w^- T2^- L_v^- (7 rows), b = a + 15, p + q = 40 − 2a.
- Elementary facts: each row carries each of the 11 labels once; each label has exactly one cut; and the exchange identity. If two rows R, R′ have common vertex set C, then L(R∖C) = L(R′∖C).
- Lemma DP★′ (`author-response-v169-A-B-reviews-v1.md` §1, SHA256 `d731174cbf1c5b353b48e9f73dc5f8ff50828dc77d13f8d90c1edf5514e358bb`). Two steps of its proof are credited to BDP (InfoSPR7-2, `peer-review-v169-A-v1.md` §5.2). It is used once, in §4.3(iv).

**Avoided entirely:**
- v73 LF60, v73 §4 and later, v74;
- part19 physical line 843;
- v150b-B v2 lines 19, 69, 126 and 142;
- any v73/v74 route described in the reviews.

The heading at v73 LF59 names a quantity for "O_w and the loops", and the reviews describe what LF60 feeds. So this proof never relates F_1's cut grid to F_2's rows or cuts on any loop: no offset, shift or relative phase between the two faces' cut grids is defined or used. F_1 and F_2 are analysed separately. They are linked only through label-level facts (which labels have copies on which thread or loop, and how many) and through the global lengths a, p, q.

The author (the same agent identity) wrote v73 historically. LF60's content is not in the author's present context, and non-influence is not certifiable beyond this statement.

It is written reasoning only: no interpreter, enumeration, program, table or probe was used. It is not reviewed, formal or novelty-cleared.

## 1. Label types

**Copies.** Every non-branch vertex of H is a 2-vertex. In the support-8 split graph, each label other than v, w has five 2-vertices, and v, w have three each besides b_v, b_w.
- A 2-vertex on T1 is passed twice in F_1; one on T2 is passed twice in F_2.
- A loop 2-vertex is passed once in each face.
- A cut adds one row incidence in its face.

**Counts for a non-branch label x.** Let x have t1 copies on T1, t2 on T2 and l on the loops, with cut in F_1 (ε = 1) or F_2 (ε = 0). Then 2t1 + l + ε = 4, 2t2 + l + 1 − ε = 7 and t1 + t2 + l = 5. The solutions are:
- ε = 1: (1,3,1) **type I** or (0,2,3) **type II**;
- ε = 0: (2,3,0), (1,2,2) **type III** or (0,1,4) **type IV**.

**O_w.** In the one-gap case, the row O_w consists of L_w-vertices only, except that it touches b_w when m1 = 10 or m2 = 0. So every label other than w has an L_w-copy, and (2,3,0) is impossible. Every non-branch label has type I, II, III or IV.

**v and w.** The same counts give (t1, t2, lam, ε) ∈ {(1,2,0,0), (0,1,2,0), (0,2,1,1)}, as in v58 §1.
- For v, (1,2,0,0) is impossible because O_w needs an L_w v-copy. Call the options **V1 = (0,1,2,0)** and **V2 = (0,2,1,1)**.
- v has no L_v-copy: L_v's F_2 passage lies inside W_b0 ∪ W_f0, which both contain b_v. So t1(v) = 0, and v's loop copies are on L_w.
- For w, call the options **W1 = (0,1,2,0)**, **W2 = (0,2,1,1)** and **W3 = (1,2,0,0)**. W3 needs lam = 0, so it is possible only when O_w touches b_w.

## 2. The mirror: Case B reduces to Case A

v73 §3 leaves Case A (m3 = β′ + 4) and Case B (m3 = β′ − 4). Reversing every row gives an actual Tuscan-1 array with the same split graph and reversed faces. After re-orienting both loops, it is again class (b) with the same a, b, p, q, and O_w is again its only gap row, on L_w.

Take the new origin at the old b_v(2b + q), the b_v-visit before the reversed T2. Old positions x become (2b + q) − x. The cuts β′ + 10k become ≡ m3 (mod 10), so β′_new = m3. Similarly m3_new = β′ and m2_new = m2 + β′ − m3. So Case B with (β′, m2), where β′ ∈ [5, 9] and m2 ∈ [0, 5], maps to Case A with (β′ − 4, m2 + 4), where β′ − 4 ∈ [1, 5] and m2 + 4 ∈ [4, 9].

**It suffices to exclude Case A:** 1 ≤ β′ ≤ 5, 4 ≤ m2 ≤ 9, with
- a = 9 + β′ − m2,
- b = 24 + β′ − m2,
- q = 6 + 2m2,
- p = 16 − 2β′.

## 3. F_2 alone (Case A)

### 3.1 Rows and five exchange identities

The rows are those of v73 §2 with m3 = β′ + 4:
- W_f0 = L_v[10−β′..1], b_v, T2[1..β′]
- W_f1 = T2[β′..β′+10]
- W_f2 = T2[β′+10..b−1], b_w, L_w[q−1..m2+10]
- O_w = L_w[m2+10..m2]
- W_b2 = L_w[m2..1], b_w, T2[b−1..β′+14]
- W_b1 = T2[β′+14..β′+4]
- W_b0 = T2[β′+4..1], b_v, L_v[p−1..10−β′]

The F_2-cut vertices are T2[β′], T2[β′+10], L_w[m2+10], L_w[m2], T2[β′+14], T2[β′+4] and L_v[10−β′]. When m2 = 4, L_w[m2+10] = L_w[14] = b_w.

Cancelling common vertices gives:
- **(I1)** W_f1 against W_b1: L(T2[β′..β′+3]) = L(T2[β′+11..β′+14]) =: Q4.
- **(I2)** W_f1 against W_b0: L(T2[β′+5..β′+10]) = L(T2[1..β′−1]) ⊔ {v} ⊔ L(L_v[10−β′..p−1]).
- **(I3)** W_f2 against W_b1: L(T2[β′+4..β′+9]) = L(T2[β′+15..b−1]) ⊔ {w} ⊔ L(L_w[m2+10..q−1]). For m2 = 4 the last set is empty.
- **(I4)** W_f2 against W_b2, common part {b_w} ∪ T2[β′+14..b−1]: L(L_w[1..m2]) = L(T2[β′+10..β′+13]) ⊔ L(L_w[m2+10..q−1]).
- **(I5)** W_f0 against W_b0, common part {b_v, L_v[10−β′]} ∪ T2[1..β′]: L(L_v[1..9−β′]) = L(T2[β′+1..β′+4]) ⊔ L(L_v[11−β′..p−1]).

### 3.2 Named labels

- **κ1 and κ2.** Put κ1 = L(T2[β′]) and κ2 = L(T2[β′+14]). These are distinct cut labels. Then T2[β′+1..β′+3] carries Q4 ∖ {κ1} = {κ2, ρ1, ρ2}, and T2[β′+11..β′+13] carries Q4 ∖ {κ2} = {κ1, ρ1, ρ2}. So every Q4-label has t2 ≥ 2.
- **v, w ∉ Q4.** By (I2), v has a T2-copy in [β′+5, β′+10]; by (I3), w has one in [β′+4, β′+9]. A Q4 membership would give a third T2-copy, but t2 ≤ 2 for v and w.
- **κ1 and κ2 are type III.** They are F_2-cut with t2 ≥ 2.
- **Put χ2 = L(T2[β′+4]), χ1 = L(T2[β′+10]) and μ = L(L_v[10−β′]).** These are F_2-cut labels. Put Λ5 = L(L_v[11−β′..p−1]) (5 − β′ labels) and Τ1 = L(T2[1..β′−1]) (β′ − 1 labels).
- **W_f0** carries μ, L(L_v[1..9−β′]), v, Τ1 and κ1. With (I5) this gives the partition of all 11 labels: Q4 ⊔ X7, where X7 = {v, χ2, μ} ⊔ Λ5 ⊔ Τ1.
- **The labels on L_v.**
  - By (I5), L_v[1..9−β′] carries {κ2, ρ1, ρ2, χ2} ⊔ Λ5. L_v[10−β′] carries μ, and L_v[11−β′..p−1] carries Λ5.
  - So κ2, ρ1, ρ2, χ2 and μ have exactly one L_v-copy each, every Λ5-label has exactly two, and no other label is on L_v.
  - **L_v carries exactly 10 − β′ ≤ 9 distinct labels.**
- **G and H.** By (I2), T2[β′+4..β′+10] carries X7, so (I3) reads X7 ∖ {χ1} = G ⊔ {w} ⊔ H, with G := L(T2[β′+15..b−1]) (9 − m2 labels) and H := L(L_w[m2+10..q−1]) (m2 − 4 labels). By (I4), L_w[1..m2] carries {χ1, κ1, ρ1, ρ2} ⊔ H.
- **ρ1 and ρ2.**
  - λ2 := L(L_w[m2]) is an F_2-cut label on L_w[1..m2].
  - It is not χ1 or κ1, whose cuts are elsewhere.
  - It is not in H: H's members are classified in §3.3, and none of them has its cut at L_w[m2].
  - So λ2 ∈ {ρ1, ρ2}. Name it ρ1.
- **ρ1 is type III; ρ2 is type II.**
  - ρ1 has t2 = 2, is F_2-cut and has loops {L_v, L_w[m2]}.
  - ρ2 has T2-copies in both P4s, one L_v-copy, an L_w-copy in L_w[1..m2−1] and an O_w-copy. That is l = 3, so ρ2 is type II: F_1-cut, with no T1-copy and exactly one L_v-copy.
  - The O_w-copy is not L_w[m2+10]: that cut label is F_2-cut, and (0,2,3) is not an F_2-cut type.
- **κ1's and κ2's loops.** κ1 has loops {L_w[1..m2−1], O_w} and no L_v-copy. κ2 has loops {L_v, O_w}. Both have a T1-copy.

### 3.3 Classes of X7 (copies counted from §§3.1-3.2)

Here λ1 := L(L_w[m2+10]) for m2 ≥ 5. It lies in H, and its H-copy is its O_w-copy.

| class | forced copies | type |
|---|---|---|
| Λ5-label in G | 2 T2, 2 L_v, O_w | II |
| Λ5-label = χ1 or λ1 | 1 T2, 2 L_v, L_w-low, O_w or λ1 | IV |
| Λ5-label = w | 1 T2, 2 L_v; needs no O_w-copy | only if m2 = 4 (W1) |
| Τ1-label in G | 3 T2, O_w | I |
| Τ1-label = χ1 or λ1 | 2 T2, L_w-low, O_w or λ1 | III |
| Τ1-label in H ∖ {λ1} | 2 T2, O_w, H-copy, L_w-low | II |
| Τ1-label = w | 2 T2, O_w (W2, m2 ≥ 5); or 2 T2 and T1 (W3, m2 = 4) | — |
| χ2 or μ in G | 2 T2, one L_v, O_w | III |
| χ2 or μ in H | 1 T2, one L_v, O_w, H-copy, L_w-low | IV |
| χ2 or μ = w | 1 T2, one L_v, O_w | W1, m2 ≥ 5 |

Any other placement exceeds five copies (three for v, w) or gives an impossible tuple: (1,1,3), or (0,2,3) with an F_2 cut.

**Consequences.**
- **Type I labels lie in Τ1 ∩ G.** Their only loop copy is on L_w, and they have no L_v-copy.
- **N := the labels with t1 = 0, other than v and w.** These are exactly the type-II and type-IV labels, and N = {ρ2} ⊔ (Λ5 ∖ {w}) ⊔ ({χ2, μ} ∩ H) ⊔ (Τ1 ∩ H ∖ {λ1}).
- **For m2 ≥ 5:** w ∈ {χ2, μ} (W1, one L_v-copy) or w ∈ Τ1 (W2, with no L_v-copy and no T1-copy).
- **For m2 = 4** (O_w starts at b_w, so w's cut is b_w(b) in F_2, and H = ∅): w ∈ Λ5 (W1, two L_v-copies) or w ∈ Τ1 (W3). Also χ2, μ ∈ G.
- **T1's interior** (a − 1 vertices) carries the type-I and type-III labels, plus w under W3. So |N| = 9 − (a − 1 − t1(w)) = 10 − a + t1(w).

## 4. F_1 alone (Case A)

F_1 positions:
- b_v(0) and b_v(40);
- T1[j] at j and at P − j, where P = 2a + q = 24 + 2β′;
- b_w(a) and b_w(a+q);
- L_w[u] at a + u;
- L_v[y] at P + y.

Rows have 10 steps, and the cuts are 10 apart.

**Lemma P (no pure L_v row).** A row inside L_v would need 10 or 11 distinct labels from L_v's 10 − β′ ≤ 9.

**4.1 v's cut is not at a b_v-visit.**
- If v's F_1 cut is at b_v(0), the rows are [0,10], …, [30,40].
  - P = 30 would be a second v-cut.
  - P ∈ (30, 40) puts v twice in [30, 40].
  - P ∈ (20, 30) makes [30, 40] consist of b_v and 10 L_v-vertices. Lemma P forbids this.
- If v's cut is at b_v(P), then b_v(40) must avoid [P−10, P+10], so P + 10 < 40. Then [P, P+10] has 10 L_v-vertices, again against Lemma P.

**4.2 The cut grid.** By §4.1:
- both b_v-visits lie strictly inside different rows;
- there is a cut in (P, 40), and Lemma P allows only one: c_L = 40 − e;
- the row before c_L contains b_v(P), so 30 − e < P, and the row after contains b_v(40), so 1 ≤ e ≤ 9.

Call the rows:
- R_B = [−e, 10−e] ∋ b_v(0);
- R_C = [10−e, 20−e];
- R_D = [20−e, 30−e];
- R_A = [30−e, 40−e] ∋ b_v(P).

R_C and R_D contain no b_v, so they take v from L_w-copies: under V2, the one copy sits at the cut 20 − e. Since a ≤ 10 and a + q ≥ 20, the cut 20 − e lies inside L_w. Put J1 = 10 − e and J2 = P − (30 − e) = 2β′ − 6 + e.

**Row-saturation remark.**
- If a row contains b_v, b_w and a full T1-pass, then t1(w) = 0, since otherwise w appears twice. That row's loop vertices then carry exactly N, because the full T1-pass carries every T1-label.
- If a row contains no L_w-vertex, every N-label in it, and w when t1(w) = 0, comes from an L_v-copy or from that label's F_1 cut.

### 4.3 m2 ≥ 5

Here a = 9 + β′ − m2 ≤ 9 and a + q ≥ 21.

**(iv) a < 10 − e and a + q > 30 − e.** R_C and R_D are consecutive pure L_w-rows of one pass, with s = 10 − e − a ≥ 1 and s + 20 = 30 − e − a ≤ q − 1. **DP★′ excludes this.**

**(i) a > 10 − e and a + q < 30 − e.** R_A and R_B contain no L_w-vertex and no b_w.
- J1 < a and J2 < a, so T1[J1] and T1[J2] are T1-vertices at the cuts 10 − e and 30 − e. J1 ≠ J2, since no vertex has two cut visits.
- Their labels have a T1-copy and an F_1 cut, so they are type I. Each such label's only loop copy is on L_w.
- If J1 < J2: T1[J2] lies in R_C (forward) and at the cut 30 − e (rows R_D and R_A). Its fourth row R_B has no L_w. **Contradiction.**
- If J1 > J2: T1[J1] lies at the cut 10 − e (rows R_B and R_C) and in R_D (backward). Its fourth row R_A has no L_w. **Contradiction.**

**(v)/(vi) A b_w-visit is an F_1 cut.** This is w's cut, so w ∈ Τ1 is W2: it has one L_w-copy, no L_v-copy and no T1-copy.
- If the other b_w-visit's row is not R_A or R_B, then R_A or R_B contains none of w's vertices. **Contradiction.**
- Otherwise R_A and R_B each contain b_v, a b_w-visit and a full T1-pass. By the remark, all L_v-vertices (which lie in R_A ∪ R_B) carry N-labels. But κ2 is type III and lies on L_v. **Contradiction.**

**(ii) a < 10 − e and a + q < 30 − e.**
- R_B ⊇ {b_v(0), b_w(a)} ∪ T1-forward. So t1(w) = 0, and R_B's loop vertices (e on L_v, 10 − e − a on L_w) carry exactly N, with |N| = 10 − a = 1 + m2 − β′.
- R_A = T1[1..J2], b_v(P), L_v[1..16−2β′−e] has no L_w and no b_w.
  - So w ∈ N needs an L_v-copy: w ∈ {χ2, μ}.
  - Every N-label needs an L_v-copy in R_A's part. So Τ1 ∩ H ∖ {λ1} = ∅, and N = {ρ2} ⊔ Λ5 ⊔ ({χ2, μ} ∩ H).
  - Since w ∉ H, |{χ2, μ} ∩ H| = m2 − 5 ≤ 1, so m2 ∈ {5, 6}.
- The L_v-vertices only in R_B, L_v[17−2β′−e..15−2β′], carry N-labels. Those labels also have an L_v-copy in R_A's part, so they have two L_v-copies and lie in Λ5. Conversely, every Λ5-label has one copy in R_A's part and the other in R_B only. Hence e − 1 = 5 − β′, so **e = 6 − β′**.
- Then a < 10 − e reads 9 + β′ − m2 < 4 + β′, so m2 = 6, a = 3 + β′, and R_B's L_w-part is the single vertex L_w[1] at the cut 10 − e.
- R_B's loop vertices are: the 5 − β′ Λ5-copies; the cut vertex L_v[p−e] (the cut 40 − e); and L_w[1] (the cut 10 − e). Together they carry N = {ρ2} ⊔ Λ5 ⊔ {h}, where h ∈ {χ2, μ} ∩ H is type IV.
- So h sits on an F_1 cut. But type IV is F_2-cut. **Contradiction.**

**(iii) a > 10 − e and a + q > 30 − e.**
- R_A ⊇ {b_w(a+q), b_v(P)} ∪ T1-backward. So t1(w) = 0, and R_A's loop vertices (L_w[30−e−a..q−1] and L_v[1..p−e]) carry exactly N.
- R_B = L_v[p−e..p−1], b_v(0), T1[1..10−e] has no L_w and no b_w. As in (ii): w ∈ {χ2, μ}, N = {ρ2} ⊔ Λ5 ⊔ ({χ2, μ} ∩ H), and m2 ∈ {5, 6}.
- R_A's L_v-part carries N-labels only, so the non-N L_v-labels κ2, ρ1, w and the G-member of {χ2, μ} lie only in R_B.
- The L_v-vertices only in R_A (15 − 2β′ − e of them) carry N-labels that also appear in R_B's L_v-part, so they are Λ5-copies. This gives e ≥ 10 − β′.
- The T1-labels missing from T1[1..10−e] must enter R_B through L_v, so they lie in {κ2, ρ1} ∪ ({χ2, μ} ∩ G). Their number is a − 11 + e ≤ 8 − m2, which gives e ≤ 10 − β′. So **e = 10 − β′**.
- Then a + q > 30 − e reads 15 + β′ + m2 > 20 + β′, so m2 = 6.
- The R_A-only L_v-vertices are exactly the 5 − β′ second Λ5-copies. So the cut vertex L_v[p−e] is not a Λ5-label, and it is F_1-cut, so it carries ρ2.
- R_A's L_w-part is the single vertex at position 20 + β′ = 30 − e, an F_1 cut. It must carry the remaining N-label h (type IV). **Contradiction.**

These cases are exhaustive, so **Case A with m2 ≥ 5 is impossible.**

### 4.4 m2 = 4

Here a = 5 + β′, q = 14, a + q = 19 + β′, and w's cut is b_w(b) in F_2. So neither b_w-visit is an F_1 cut: a ≠ 10 − e and a + q ≠ 30 − e.

**(iv)** As in §4.3.

**(i)** As in §4.3. The two cut labels at T1[J1] and T1[J2] are type I, since w is F_2-cut under W1 and W3, and their only loop copies lie on L_w. **Contradiction.**

**(ii) a < 10 − e and a + q < 30 − e.**
- Here e < 5 − β′, and 30 − e < P gives e > 6 − 2β′. The only solution is β′ = 3, e = 1, with P = 30 and p = 10.
- Then R_A = [29, 39] contains L_v[1..9], the whole interior of L_v. So each Λ5-label (|Λ5| = 2) appears twice in R_A. **Contradiction.**

**(iii) a > 10 − e and a + q > 30 − e.**
- R_A ⊇ {b_w(a+q), b_v(P)} ∪ T1-backward. So W3 is impossible, w ∈ Λ5 (W1, with two L_v-copies), and R_A's loop vertices carry exactly N, which excludes w.
- Both of w's L_v-copies avoid R_A, including the cut L_v[p−e]. So both lie in L_v[p−e+1..p−1] ⊆ R_B, and w appears twice in R_B. **Contradiction.**

So **Case A with m2 = 4 is impossible.**

## 5. Result

**WRITTEN:** In distinct-centre 4+4 class (b) with d = 3, **the one-gap case (n_f = n_b = 3) is impossible**:
- Case A by §§3-4;
- Case B by the mirror of §2.

The proof uses v73 LF1-59, the exchange identity, the label-count types (re-derived in §1) and DP★′. It never uses v73 LF60, v73 §4 or later, v74, or any F_1/F_2 relative cut phase on a loop.

**Effect on the v150b-A v2 node map (author statement, not a review).**
- This would supply the d = 3 one-gap case that v150b-A v2 §3 marks as the only unrewritten line of W_44db.
- With the d = 1, 3 (two-gap), 5 and 7 parts already listed there (v75, v58, v57, v54), W_44db would be complete at the WRITTEN level.
- W_m8 would then compose at the WRITTEN level only conditionally on F0, A_m7, A_v12, A_R1 and A_R2, and on every NR root named by v150b-B v2 §3. No such adoption is made here.

**OPEN:**
- this proof's own review;
- every NR root named by either v150b review;
- the m = 9 residual;
- every m ≥ 10.

The support-9 statement is not made. Every m in 10..110 is unresolved.

**First unproved original step:** a literal 11x11 table with 110 distinct LINEAR adjacencies and 99 distinct LINEAR distance-two events, or a contradiction for every arbitrary array (which must use distance 2, v24 §7). Neither is supplied.

All of the following remain unchanged:
- the cadence histories, including the 39:33 lapse of checkpoint-071;
- the private-written-exactness, admission, clock and source histories;
- the checkpoint045 withdrawal;
- the parent-v60 intake-pause MAJOR.

The two parent cadence MAJORs of parent v138 are carried, and so is the Main217 parent process MAJOR with the author's recorded v215 exposure. This candidate needs its own complete source-bound gate.
