**Bottom line.** L6, K7-BLOCK and K7-PAIR are mathematically correct as written. I re-derived every step and found no counterexample to any stated claim. There are 0 FATAL, 0 MAJOR, 6 MINOR, 1 advisory and some cosmetic findings. The real defects are:
- P2's statement is broader than its proof.
- P3's sharpening uses Sun(5), outside the declared imports.
- Several dependency and labelling problems.

Nothing removes a class, and K7 stays OPEN.

| Item | Verdict | Findings |
|---|---|---|
| L6 (as used) | ACCEPT | C3 |
| K7-BLOCK (a) | ACCEPT | — |
| K7-BLOCK (b) | ACCEPT | — |
| K7-BLOCK (c) | ACCEPT | C1 |
| K7-BLOCK (d) | ACCEPT | — |
| K7-PAIR (i) | ACCEPT | — |
| K7-PAIR (ii) | ACCEPT | N4 |
| K7-PAIR (iii) | ACCEPT-WITH-FIXES | N3 |
| P1 | ACCEPT | N7 |
| P2 | ACCEPT-WITH-FIXES | N2 |
| P3 | ACCEPT-WITH-FIXES | N1 |
| Coverage summaries (SOURCE00:110–122, SOURCE01:108–118) | INCONCLUSIVE | N6 |

## 1. L6 and its uses through TWIN(d)

**Proof of L6 (SOURCE03:34–35), re-derived:**
- X·U_a = X = X·U_b, so XW = X.
- 1 ∈ X and U_vX = X give U_vW ⊆ U_vXW = X ⊆ U_vW.
- μ(X) = α_va/g_va < 1 by disjointness, so W ≠ G.
- U_a, U_b ≤ W give m | n_a and m | n_b, so m | g_ab.
- U_aU_b ⊆ W gives α_ab/g_ab ≤ 1/m.
- L0.1 gives μ(U_vW) = [U_v : U_v∩W]/m.

All correct.

**Uses:** SOURCE00:43, :51–52 and :61–62, and SOURCE01:29. In each, v, j, k are distinct and j ~ k, so TWIN(d) (SOURCE02:106) applies to every v, marked or not.

**TWIN(d) check.** I re-derived it from L1 and TWIN(b). The edges xz and yz are opposite unmarked vertices, so τ_min = b. Then μ(U_z(U_x∩U_y)) = τ/6 ≥ b/6 = μ(U_zU_x), which forces U_zU_x = U_z(U_x∩U_y) = U_zU_y.
- This meets the addendum's A4(a) sufficient condition: the α's are equal, and F7 holds with equality.
- W does not depend on the apex. SOURCE01 uses this implicitly.

## 2. Uses of L5

**Decomposition.** g_lU_l ∩ gH = x(U_l∩H). Translating by g⁻¹ gives pairwise disjoint left cosets in H, of index n_l·t_l/m. t_l counts the H-cosets that g_lU_l meets. Correct.

**Size of T.**
- K7-BLOCK uses |T| ≤ 4; structurally |S_C| ≤ 7 − s ≤ 4.
- K7-PAIR (i)–(iii), P1 and P2 use |T| ≤ 4.
- P3 uses |T| = 5 (see N1).
- Nowhere is |T| ≥ 6, Sun(7) or a least-order frame used.

**gcds.** Each λ is a {2,3,5}-smooth factor times w_l. The w's are pairwise coprime and prime to 30, and the m_z are pairwise coprime. I checked:
- SOURCE01:39 (the gcd is exactly 3);
- SOURCE00:105 and SOURCE01:67 (gcd(t, t′));
- SOURCE00:89–91, including gcd(2m_z, 2m_z′) = 2;
- the parity step at SOURCE00:102.

## 3. K7-BLOCK

- **(a):**
  - m/6 ∈ ℤ forces m = 6, and incidentally U_v ⊆ W.
  - Equal measure makes U_jU_k = ⟨U_j, U_k⟩.
  - W_jk ⊆ U_vW_jk = W_vj, and equal index gives equality.
  - L0.2 gives the distinct cosets.
- **(b):** for every v ∉ B, marked included, gcd(w_j, λ_v) = 1, so Sun(2) applies. The case w_j = 1 (U_j = W_B) is consistent.
- **(d):**
  - s = 6, 7: pigeonhole.
  - s = 5: both outside vertices are marked with α = 1, and their λ's are coprime.
  - s = 4: every pairwise gcd is ≤ 2, so each coset holds ≤ 2 vertices and Σα ≤ 4. Every row of the table holds; in row 2, z and z′ cannot share a coset.
  - s = 3 with M = ∅: valid.

*Remark (my own, unreviewed):* the same packing also excludes s = 3 with |M| = 1.
- If any unmarked outsider has t = 3, all three do. The coset z meets then holds {v₁, v₂, v₃, z}, with every gcd ≤ 3.
- If all three have t = 2, each coset holds exactly two of them, and z completes a triple with every gcd ≤ 2.
- With |M| = 2 the packing alone does not kill. Example: two unmarked vertices with t = 3, α_z = 2 with m_z = 3, and α_z′ = 3 with m_z′ = 2. Then gcd(λ_z, λ_z′) = 6.

## 4. K7-PAIR and corollaries

- **(i):** if m = 2, all seven vertices have t = 1. Some coset then holds ≥ 4 pieces with pairwise gcd 3, contradicting Sun(4). m = 1 would mean W = G.
- **(ii):** valid, including for marked z.
- **(iii):** U_jU_k = W, g_jW ≠ g_kW, and exclusivity all hold.
- **P1:** a single β = 3 rules out m = 3.
- **P2:** the count k₂ + k₃ ≤ c₂ + c₃ ≤ 4 < 5 holds.
- **P3:** the m = 3 rows hold: 7 > 6, and the light distributions (2,2,2) and (2,2,1). The m = 6 rows with k₄ ≤ 2 hold.

## Findings (all MINOR)

**N1. P3, SOURCE01:81, :95, :101–102 and :104, against :11.**
- "At most 4 vertices per coset" and the rows k₄ = 4, 5 need Sun(5), but the file declares 2 ≤ |T| ≤ 4.
- Under the declared imports, a coset holding {h₁, h₂, h₃, h₄, l} passes every test with |T| ≤ 4: every triple contains two heavies and every 4-set contains three. So "k₄ = 3" is unproved there.
- The stated conclusion k₄ ≥ 3 needs only Sun(3).
- Fix: replace :104 with "k₄ ≥ 3" and drop the Sun(5) clauses. Alternatively, import Sun(5) (README:16; SOURCE06:60).
- k₄ ≥ 3 is the most this method gives: with m = 3 and k₄ = 3, the cosets {j, h₁, h₂, h₃}, {k, h₁, h₂, h₃} and {l₁, l₂} pass every test.

**N2. P2, SOURCE01:62 and :113.**
- The statement covers all of Q23, but the proof starts from P1, which needs at least two 2-classes (:54).
- K7-Q allows the one-class case to be filed under Q23 (SOURCE02:139).
- The claim still holds there. If m = 3, seven pieces with t = 1 and λ = 2w give 7 > 6 incidences. If m = 6, they give 10 > 8.
- Fix: add "with at least two 2-classes", or add these two lines.

**N3. (iii), SOURCE01:50 and :25.**
- It cites "K7-BLOCK's argument with s = 2", but K7-BLOCK assumes s ≥ 3 (SOURCE00:17).
- The argument is valid once U_jU_k = W is known: L6 gives t_v = α_vB, and L5 then applies.
- Fix: write these lines out, and note that |S_C| can reach 5 here (see N1).

**N4. SOURCE00:11; SOURCE01:7 and :34.** TWIN(c) is never actually needed:
- In (ii), evenness together with α ≤ 5 already gives {2, 4}.
- In (iii), α ≤ 4 is automatic.
- m = 2 forces α = 3 regardless.
- Fix: drop the import. The lemmas then rest only on TWIN(b) and TWIN(d), which use T alone.

**N5. Governance: SOURCE00:13 and SOURCE01:13, against SOURCE05:163–169 and SOURCE06:23, :26.**
- Both files say they are "not FH", but they are exactly "L5 with L6 as the subgroup source".
- A4(a)–(d) are in fact discharged:
  - (a) by TWIN(d);
  - (b) by m = 6, or m ∈ {3, 6};
  - (c) the domains are the cosets of W;
  - (d) |T| ≤ 5, with no least-order frame.
- L5 is not on the accepted list at SOURCE06:23.
- Fix: replace the disclaimer with this explicit A4 discharge, and record that acceptance presupposes acceptance of L6. This is for the parent to rule on.

**N6. SOURCE00:118–122 and SOURCE01:108–118.**
- Both coverage summaries depend on K7-Q (the trichotomy and the assignment of degenerate cases), on K7-Q5 and on K7-COV.
- "K7-COV data (ii)" should read (i).2.
- Fix: label both sections as conditional on K7-Q, K7-Q5 and K7-COV.

**N7. Advisory (P1–P3).** The K7-Q dependence is only definitional. K7-Q-free forms, which the proofs already establish:
- **P1′:** if some α_vB is odd, then m = 6.
- **P2′:** if M = ∅, a twin pair cannot have every α_vB ∈ {2, 3}.
- **P3′:** if M = ∅ and every α_vB ∈ {2, 4}, then at least three of them equal 4.

**Cosmetic:**
- C1: (c) is stated with |T| ≤ 6 (SOURCE00:33), against ≤ 4 at :10. Harmless, since |S_C| ≤ 4.
- C2: L0.6 is not "the Chinese remainder theorem" (:10).
- C3: SOURCE03:35 should state U_vX = X explicitly.
- C4: m_z clashes with the index m (SOURCE00:71).
- C5: SOURCE02:124 is garbled.
- C6: under overlay A-1 the 5-valuation should be h_i (SOURCE02:14).

## Item 5: silent assumptions

None found. Everything used follows from K7:
- n = 6w on U;
- the w's are pairwise coprime and prime to 30;
- the m_z are pairwise coprime;
- |M| ≤ 3;
- valuations are uncapped.

No CAP, τ, q or least-order frame is used. α_vB ≠ 1 relies on the explicit hypothesis that B is a full ~-class. Equal subgroups U_j = U_k are covered: they force w_j = 1 and m = 6.

## Unverified

- **Erratum W1:** not supplied. N1's fix works whichever |T| bound it sets.
- **SOURCE02:**
  - TWIN(b) and TWIN(d) were taken as stated (I spot-checked them).
  - K7-Q, K7-Q5, K7-COV and K7-U were not reviewed.
- **Imports:**
  - Zhu's Sun(3) and Sun(4) and the accepted Sun(5) are assumed.
  - I re-derived L5 rather than reading its predecessor record.
- **Hashes:** none were computed. The cross-reference prefixes match the supplied strings as text only.
- **Still open:**
  - s = 3 with |M| ≥ 2;
  - twin pairs with M ≠ ∅ beyond P1;
  - m = 3 twin pairs in Q24;
  - whether the surviving patterns are realisable.
