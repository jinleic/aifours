# Hostile review: proof-ROT-ZX-v1 (SOURCE00 `ad2460b2…815b`) and notes-ZX-deps-v1 (SOURCE01 `f98eb3eb…2b33`)

I had no tools, so every check below was done by hand from the inlined LF-numbered sources. I read the candidate against SOURCE02 and the mandatory overlay V1–V9 (SOURCE03:24-32).

## Verdicts

| Claim | Verdict | Findings |
|---|---|---|
| Lemma ZX (SOURCE00:56-66, 81-160) | **ACCEPT**, complete modulo the imported MULT (i)–(iii) and (D) | m6, m11 (wording only) |
| Lemma S1(a) (SOURCE00:70, 183-188) | **ACCEPT** | none |
| Lemma S1(b) (SOURCE00:71-72, 189-199) | **ACCEPT**: proved, but no theorem depends on it | m6 |
| ROT-ZX, terminal form (SOURCE00:203-234; SOURCE01:76-81) | **ACCEPT-WITH-FIXES** | m1, m3, m4 |
| ROT-ZX, uniform form (SOURCE00:236-243; SOURCE01:83-85) | **ACCEPT-WITH-FIXES** | m2 |
| INV*-ZX (SOURCE00:247-251; SOURCE01:87-90) | **ACCEPT-WITH-FIXES** | m5, and m1 carries over |
| OLSON-ZX (SOURCE00:253-266; SOURCE01:92-94) | **ACCEPT** | none |

**Totals:** FATAL 0, MAJOR 0, MINOR 11. No step failed, so I have no counterexample. Instead, §1 gives two stress tests worked by hand.

## 1. Lemma ZX (audited)

**Step A**
- Y′ is zero-sum-free: a nonempty zero-sum V ⊆ Y′ would make ZV a longer zero-sum.
- L ≤ 2p−1 by (D), and L = R−|Z| ≥ 2p−k.
- Hence e = 2p−1−L = k−1−2κ+|Z| lies in [0, k−1], and 3e+2 ≤ 3k−1 ≤ 2p.
- So MULT (iii) and then (ii) apply to any value of maximal multiplicity. SOURCE05:63-68 places no other condition on g, and L > 0.
- (A1): e′ ≥ 2q, so m = L−q ≥ L−e′/2.
- (A2): d_j−1 ≤ e′ ≤ e, and e+1 ≤ m by MULT (iii).
- MULT's d_j are representatives in [3, 2p−1] (SOURCE05:76). Here d_j ≤ k ≤ p−2 (at p=5, k ≤ 3), so b_g(d_j g) = d_j.
- COMP: the interval-growing step is valid because d_j ≤ m ≤ M+1. Part (b) holds because a subsequence of weight 2p is a nonempty zero-sum.
- (A3): W′ ≥ L ≥ 2p−k ≥ p+2. (A4) is correct.

**(EX)**
- Y = Z ⊎ Y′, so (Z−U) ⊎ Q ⊆ Y.
- s is additive, and s(Z) ≡ 0 because ord g = 2p. So the sum of (Z−U)Q is (w(Q)−s(U))g = 0.
- Z is longest among all zero-sums, including the empty one. So |Z|−|U|+|Q| ≤ |Z| for every admissible Q, including when Z* = ∅. No parity input is needed.
- Remark (2) at SOURCE00:174 is accurate about (EX) itself. Take Y = (3g)(−3g)g³ in Z₁₀ and Z₀ = (3g)(−3g). Z₀ is inclusion-maximal, since g³ is zero-sum-free, yet U = {3g}, Q = g³ gives |Q| = 3 > |U| = 1.

**Steps C and D**
- Step C covers b ∈ [3, p], including (1,0), since every such b is < W′. Q = g^b if b ≤ m; otherwise COMP(a) and (A4) give |Q| ≥ 2. Either way (EX) contradicts.
- So Z = g^r T with every β ∈ [1, p−2].
- Step D: 2p−β ≥ p+2. If 2p−β ≤ W′, the same contradiction follows. Hence 2p−β ≥ W′+1 = 2p−e+e′, i.e. β ≤ e−e′.

**Step E**
- r ≤ 2κ ≤ 2k−2 < 2p and σ ≥ 0, so σ = r+2pt with t ≥ 0.
- Suppose t ≥ 1. Then T ≠ ∅, so e−e′ ≥ 1.
- 2m−2p+1 ≥ 2p−1−2e−e′ ≥ e−e′ holds iff 3e ≤ 2p−1, and indeed 3e ≤ 3k−3 ≤ 2p−2.
- I = [2p−m, m] ⊆ [1, 2p−1] because m ≤ L ≤ 2p−1.
- The least j with S_j ≥ 2p−m has j ≥ 1, since S₀ = 0 < 2p−m, and S_j ≤ 2p−m−1+|I| = m.
- There is no wrap-around case. The S_j are strictly increasing integers, nothing is reduced mod 2p before s(U) is formed, and both S_j and 2p−S_j lie in I. So g^{S_j} and g^{2p−S_j} are in Y′.
- The two (EX) calls are independent; that Q₁ and Q₂ may overlap does not matter.
- Adding the two inequalities gives 2p ≤ |Z| ≤ 2κ < 2p, a contradiction.
- If σ = 0 or Z = ∅, then t = 0 directly.

**Steps F and G**
- Step F: |Q| ≥ 2p−r−e′, and s(T) = −r uses Step E. Then 2p ≤ |Z|+e′ ≤ 2κ+e ≤ 3k−3 ≤ 2p−2, a contradiction.
- Step G: cost = e′+r ≤ (2p−1−r−L)+r = e. Every |b| is at most max(k, e) = k, so (1,0), with b = p > k, is excluded. The identity E+N = cost holds.

**Edge cases**
- κ = 0: Z = ∅, Steps C–E are vacuous, Step F is COMP(b), and cost = e′ ≤ k−1.
- k = 1: then κ = 0, e = 0, Y = g^{2p−1}, and cost = 0.
- 3k = 2p+1 (p=7, k=5; p=13, k=9): the bounds 3e+2 ≤ 2p, 3e ≤ 2p−2, W′ ≥ p+2 and 3k−3 ≤ 2p−2 are each exactly tight and still suffice. At p = 7, k = p−2 holds with equality.
- Remark (1): the zero-sums of g^{2p−1}(−g)^{k−1} are exactly the (g(−g))^j, and its cost is k−1.

**Stress tests**
- (i) p=7, k=5, κ=2: Y = g¹²(−3g), so R = 13. Its only zero-sum is g³(−3g), of length 4 = 2κ.
  - Then Z = g³(−3g), Y′ = g⁹, e = 4, e′ = 0, β = 3 ≤ e−e′, σ = r = 3.
  - cost = 3 ≤ e = 4 = k−1. Every step checks at the 3k = 2p+1 boundary.
- (ii) Step E's t ≥ 1 configuration refutes itself as claimed. Take p=7, k=5, κ=3, Y = g¹⁰(−3g)⁵ (R = 15), and the candidate Z = g(−3g)⁵, with σ = 15 = r+14.
  - Here m = 9, I = [5, 9], and S₂ = 6 ∈ I.
  - The exchanges produce g⁹(−3g)³ (length 12) and (−3g)²g⁶ (length 8), both longer than |Z| = 6.
  - So this Z is not longest, and indeed Y violates (S1).

## 2. Lemma S1 (audited)

**Part (a).**
- A minimal zero-sum has length ≤ 2p, by (D) applied after deleting one term.
- Its length is even, so (ZP) forces length ≤ 2κ.
- Write any zero-sum as a product of minimal ones. If it has length ≥ 2κ+2, the shortest such prefix has length in [2κ+2, 4κ] ⊆ [2κ+2, 2p−2], contradicting (ZP).

**Part (b).**
- |T| ≥ 2κ+2 together with (ZP) gives |T| ≥ 2p+2. This also holds when [2κ+2, 2p] is empty.
- Suppose at most one piece is long, and order it first. At the crossing index, j ≥ 2, l_{j−1} ≤ 2κ and |T_j| ≤ 2p−2κ. So l_j ∈ [2κ+2, 2p], contradicting (ZP).
- Long pieces have even length ≥ 2p−2κ+2.
- 4p−4κ+4 ≥ 2κ+2 holds iff 6κ ≤ 4p+2. Then (ZP) gives |P|+|P′| ≥ 2p+2, so 2κ ≥ p+1.
- Under (G′), 6κ ≤ 4p−4, as SOURCE00:77 states.

**Is (b) needed?** No. ZX, ROT-ZX, INV*-ZX and OLSON-ZX use only S1(a). Part (b) appears only in the residual descriptions at SOURCE00:296-298 and SOURCE01:97-99.

## 3. ROT-ZX (glue audited; engines imported)

**Normal form.**
- SOURCE07:33-39 fixes no order for the PM* merges and equal-value fusions, and proves no uniqueness. The terminal k may depend on the order chosen.
- The proof at SOURCE00:209-234 uses only properties that every terminal form has. So the theorem holds with "some normal form" (SOURCE01:76-77).
- The uniform corollary holds for every normal form, because k ≤ o always.
- "its normal form" at SOURCE00:203-204 must still be changed (m1).

**Parameters.**
- κ^ = κ(w) − (o−k)/2, and R = 4p−2−F = 2p+2κ^−k.
- k = 1: K1 gives 2p−1 equal rotations in a nonzero pair (SOURCE12:9), F = 2p−1 and κ^ = 0.
- κ^ ≥ 0 via the GRX all-plus selection with m = 0 (SOURCE06:37).
- κ^ ≤ k−1 via DAV (SOURCE07:42-43). So (G′) holds.
- (ZP) follows from GRX all-plus, since T = 0 because Σθ_i = 0 (SOURCE06:89), together with Y(x) = (1, x).

**Weights.**
- |b| ≤ k ≤ p−2 is established from ZX before b is identified with the SHgen weight (SOURCE00:220-222), as overlay item 4 requires.
- x = bc ≡ 0 is impossible because 0 < |b| < p.
- SHgen's E sums over heavies only. It equals ZX's E because lights contribute 0.

**SHgen hypotheses.**
- (H): 2H = 2p−2−2κ^ ≥ 2p−2k ≥ k−1 ≥ E holds iff 3k ≤ 2p+1. No κ ≤ p−k is needed. The bound is tight at p=7, k=5, κ^=4.
- (K): η ≤ E/2 and a_max ≤ E+1 reduce (K) to 5k ≤ 4p−1, which follows from 3k ≤ 2p+1 for p ≥ 4 (25 ≤ 27 at p=7; 45 ≤ 51 at p=13).
- SHgen's setting needs F ≥ k ≥ 2 and R ≥ η ≥ 1, which hold.

**SHgen-E.**
- REFL is needed only for the base words u°(h), where o_F = k (SOURCE07:66-70).
- k is invariant under expansion, and k ≤ (2p+1)/3 ≤ p. The obligation therefore holds, but the file cites the wrong discharge (m4).

**Uniform form.**
- 3k ≤ 3o ≤ 2p+1, and κ^ ≤ κ(w).
- F ≥ o+p−1 is equivalent to κ(w) ≤ (p−1)/2.
- The branch o ≤ (p+1)/2 uses DAV's κ^ ≤ k−1, which is valid only for k ≥ 2 (m2).

## 4. INV*-ZX and OLSON-ZX (glue audited)

**INV*-ZX.** REFL-few-odd is applied to w with its conditions (0), (a), (b) and (d). In the uniform case, o ≤ (2p+1)/3 ≤ p.

**OLSON-ZX, against SOURCE09:28-47.**
- Case 1: F ≥ 4p−3 and o ≤ (2p+1)/3 ≤ 2p−3, so (F−o)/2 ≥ p. The frame and conjugation follow SOURCE09:31-36.
- Case 2: (o, F) ↦ (o−1, F−1). The block stays nonempty, so nothing fuses. F′−o′ = F−o, so both branches of the hypothesis are preserved.
- Case 3: (o, F) ↦ (o or o−2, F).
  - An emptied run has two distinct neighbouring blocks: with a single block, the only run holds all R ≥ 3 rotations and cannot be emptied.
  - So F_i−o_i ≥ F−o and 3o_i ≤ 2p+1.
- The third rotation fixes the pair, the adjacency argument holds, and RGR-LONG (SOURCE11:7) finishes the proof.

## 5. Coverage, residual and overlay compliance

**Terminal pairs.** I recomputed the tables:
- New pairs: (5,3); (7,5); (8,6), (9,5), (9,6); (10,8), (11,7), (11,8).
- Residual pairs: (5,4); (7,6); (8,7), (9,7), (9,8); (10,9), (11,9), (11,10).

**Word conditions.**
- The new region is exactly (p+1)/2 < o, o+p−1 ≤ F ≤ 3o−4, with F ≡ o.
- p=7, o=5: F = 11. p=13, o=8: F = 20. p=13, o=9: F ∈ {21, 23}. These match SOURCE00:284-286.

**Wording.**
- There is no novelty or "first" claim (SOURCE00:18, 313).
- KAPPA01 is not used anywhere.
- The finite aid (SOURCE00:307-311) is correctly not a premise. I could not verify it.

**Overlay compliance.**
- Met:
  - V3 (SOURCE00:30, 214-215, 220-223);
  - V4's k = 1 case (SOURCE00:212);
  - V5 (SOURCE00:257-265);
  - V7;
  - V8 (SOURCE00:300-303, 275, 284);
  - V9 for the definition of o_F (SOURCE00:48).
- Gaps: V4's k ≥ 2 caveat (m2), V6 (m9), V9's INV* definition (m5), and a V1 analogue (m11).

## 6. Findings (FATAL 0, MAJOR 0)

- **m1 (SOURCE00:203-205, 247).** "its normal form" presupposes a uniqueness that is never proved.
  - Fix: write "a normal form produced by SOURCE07:30-43 (any order of moves)".
  - Define "covered by ROT-ZX" as: some such w^ has k = 1, or 3k ≤ 2p+1 and (S1) at κ^. This matches SOURCE01:76-77.
- **m2 (SOURCE00:240-241).** Insert "if k ≥ 2" before "κ^ ≤ k−1", and note that k = 1 is the first alternative. This is the V4 analogue.
- **m3 (SOURCE00:212).** Add "in one nonzero pair, so c ≠ 0 (SOURCE12:9)". The conclusion requires c ≠ 0.
- **m4 (SOURCE00:232-233).** Discharge the obligation in the file:
  - k is unchanged along expansions (SOURCE07:52-59);
  - every base word u°(h) has length 4p−2, rotations in one nonzero pair, and o_F = k ≤ (2p+1)/3 ≤ p (SOURCE07:66-70; SOURCE08:116-121).
  - Cite SOURCE03:26. Half-range overlay 3 was discharged only for k ≤ (p+1)/2.
- **m5 (SOURCE00:247-251).** Define INV* at the statement; the text is at SOURCE01:88-89. In the "in particular" clause, add o_F ≤ (2p+1)/3 ≤ p.
- **m6 (SOURCE00:13-15).**
  - L13 omits (G′); write "apart from (G′)".
  - "describes exactly" (L14-15): (b) proves only the necessary direction, and only under 6κ ≤ 4p+2. Either add the one-line converse (PP′ is a zero-sum of length ≥ 2p+2 > 2κ) or say "a necessary condition".
- **m7 (SOURCE00:270-286).** Add "whether avoiders or words with these parameters exist is not claimed", as SOURCE03:20 does.
- **m8 (SOURCE00:294-295).** The "type-II sequence" sentence is about sequences only. Any word realizing g^{2p−1}(−g)^{k−1} already has its rotations in {ρ_c, ρ_−c}, so it adds no ROT coverage. Say so.
- **m9 (SOURCE00:304-305).**
  - Replace "refutes … only at the one pair" with "bears only on (p, p−1); nothing is claimed at other pairs".
  - Add "no group word realizing it and no ordered-Olson counterexample is supplied" (V6).
- **m10 (SOURCE00:23, 33; SOURCE01:13-14, 58).**
  - (D) is not among SOURCE12's accepted statements; cite it as the classical D(C_n) = n.
  - The REFL text of record is r4 at L21-25, but the packet holds r5, where the statement is at SOURCE08:25-29. Re-verify the r4 line numbers.
- **m11 (SOURCE00:9-12).** Add "complete modulo the imported MULT (i)–(iii) and (D)" (V1 analogue).

## 7. Audited vs imported

**Audited here:**
- SOURCE00 §§1–3: ZX Steps A–G, COMP, (A1)–(A4), (EX), S1(a) and S1(b), and the ZS+ containment claims at L74-77.
- The glue arithmetic for ROT-ZX (terminal and uniform), INV*-ZX and OLSON-ZX.
- The deletion bookkeeping against SOURCE09:28-47.
- The §6 tables and examples, and the SOURCE01 restatements.

**Imported (only their hypotheses were checked):**
- (D) and MULT (i)–(iii) (SOURCE05:61-81).
- GRX/(ZP), PM* and K1 (SOURCE12).
- The normal form and DAV (SOURCE07:28-43). DAV's own proof is not in the packet.
- SHgen (SOURCE06:20-49) and SHgen-E (SOURCE07:45-70).
- REFL-few-odd: the r4 text of record is absent, so I read the statement and interface from r5 (SOURCE08:25-29, 116-123).
- RGR-LONG(p) (SOURCE11:7).

**Not checked:** the zs-check run1 output.
