# Hostile review: C56W-v1 (`63cbcdb1…`) with parent erratum v1 (`cb084e51…`) applied

**Scope.** Theorem C56W is Core5(6) for finite G. It covers every E2/E3/E5 placement, any 2-power, r_i = 1 and unbounded cofactors. The erratum's corrected text governs. Remark (2), the conditional Sun(6) composition, is not reviewed.

**Method.** I re-derived everything by hand from the supplied text. I opened no files, recomputed no hashes and consulted no external source.

## Bottom line: 0 FATAL / 0 MAJOR / 4 MINOR

Every load-bearing step re-derives. The four minors are about presentation and source binding. None of them changes a step of the proof. My recommendation is that the mathematics is sound at the corrected scope, and a text-only erratum can repair the minors. The verdict remains yours.

| # | Claim | Lines | Verdict |
|---|---|---|---|
| 1 | Target and marker binding | 17-22 | 0F/0M/1m (m4) |
| 2 | Import boundary; no Sun(5)/Sun(6)/C5W/Core(5)/frame | 23-31, 126-135 | 0F/0M/1m (m3) |
| 3 | MU | 36-38 | 0F/0M/0m |
| 4 | INV | 43-47 | 0F/0M/1m (m1) |
| 5 | FC, including the Sun(2) proof | 49-58 | 0F/0M/1m (m2) |
| 6 | G1/G3/GE compatibility | 61-68 | 0F/0M/0m |
| 7 | G3 weights and E(a)-E(d) | 69-73 + erratum | 0F/0M/0m |
| 8 | P6 | 76-84 + erratum | 0F/0M/0m |
| 9 | A6 | 87-106 | 0F/0M/0m |
| 10 | Theorem | 109-119 | 0F/0M/0m |
| 11 | Parent erratum | erratum:5 | correct and sufficient |

## Independent re-derivations

**MU.** Write I = [G:U_i∩U_j]. Then lcm(n_i, n_j) = 5r_i r_j divides I. Also |U_iU_j|/|G| = I/(n_i n_j) = α/5. Disjointness is equivalent to g_i⁻¹g_j ∉ U_iU_j, so α ≤ 4. ✓

**INV, on the actual inverse configuration.**
- Set U_i* = g_iU_ig_i⁻¹ and g_i* = g_i⁻¹. Then g_i*U_i* = (g_iU_i)⁻¹, so the cosets stay disjoint.
- Indices are unchanged, so the r_i are the same. Hence E2 (with its class), E3 and E5 are the same.
- With h = g_i⁻¹g_j, we have g_i⁻¹(U_i*∩U_j*)g_i = U_i∩hU_jh⁻¹. So |U_ihU_j| = |U_i||U_j|/|U_i∩hU_jh⁻¹| = |G|α*/5.
- h ∉ U_iU_j, so the two double cosets U_iU_j and U_ihU_j are distinct, hence disjoint. This gives α + α* ≤ 5.
- MU applied to Γ* gives α* ≥ 1. So 4 → 1 and 3 → ≤ 2.
- Both matrices are symmetric by definition. The proof only compares α_vj with α*_vj for the same ordered pair, so no false symmetry is used. ✓

**FC.**
- λ_j = r_jα_vj and t_j = r_vα_vj. The apex's own r_v and marker never enter any label.
- The cosets g_juU_v (u ∈ U_j) coincide exactly when u⁻¹u′ ∈ U_j∩U_v. So g_jU_j meets exactly t_j fibres, and none of them is g_vU_v.
- Inside a fibre, the pieces are disjoint left cosets in U_v with indices λ_j. There are at most 5 of them.
- Sun(2) (the proof at LF55-56 is correct), Sun(3) and Sun(4) constrain every 2-, 3- and 4-subset. A 5-set is constrained only through its subsets.
- Summing over the n_v−1 fibres gives a strict bound of 1−1/n_v. This strictness is load-bearing, because many cases below reach a value of exactly 1. ✓

**Compatibility.** Labels share only the primes 2 and 3: α ≤ 4, and 5 divides at most one r. For plain vertices the label gcds are:
- 1 against anything: 1.
- 3–3: 3. 3–2 and 3–4: 1.
- 2–2 and 2–4: 2. 4–4: 4.

Admissible plain sets, at every size up to 5:
- G1: singletons only.
- G3: at most 3 members.
- GE: either {2,2}, or any set with at most one 2. This includes the 5-sets {4⁵} and {2,4⁴}.

**Weights.** All are feasible on every admissible set, including 5-sets.
- E(b): total weight on all 4s is 1.
- E(c): any admissible set has at most two 2s.
- E(d): {2,2} sums to 1; any set with at most one 2 sums to at most ½ + n₄·1/(2n₄) = 1.
- E(a) presupposes GE ≠ ∅. Every use of it (LF79, LF80, LF95) is in a branch where GE is non-empty or has the explicit G1 alternative.

**P6.** The cases below partition (n₁,n₂,n₃,n₄) with sum 5, exhaustively and disjointly.

| Case | Weighting | Value |
|---|---|---|
| n₃=5 | ⅓ on each G3 | 1 |
| n₃=4 | ⅓ on G3, plus G1 or E(a) | ≥1 |
| 1≤n₃≤3 | 1/m on G3; at least 2 other items | ≥3/5+2/5 |
| n₃=n₄=0 | G1, plus 0 / E(a) / E(c) | 1, 6/5, 1 |
| n₃=0, n₄≥1, n₁≥1 | E(b) + G1 | ≥1 |
| n₃=n₁=0, n₄∈{1,2} | E(d), with n₂∈{4,3} | 6/5, 1 |
| n₃=n₁=0, n₄≥3 | survivors 44444, 24444, 22444 | — |

**A6.** Here a = E2 and b = E3 ≠ a, so r_b is odd and 3 | r_b. The gcd of λ_b with each plain label:
- G1: 1.
- G3: exactly 3 for every β. Since v₃(λ_p) = 1, this holds even when β = 3 or v₃(r_b) ≥ 2.
- Multiplier 2: 1 if β is odd, 2 if β ∈ {2,4}.
- Multiplier 4: 1 if β is odd, 2 if β = 2, 4 if β = 4.

The other primes of r_b, including 5 when E3 = E5, are coprime to every r_p and every α.

| β | n₃∈{1,2}, or 3 with an even entry | n₃=3 with a 1, or n₃=4 | n₃=0 |
|---|---|---|---|
| 1 | killed (≥1) | 13/15 → S-i | b isolated: ≥1/5+4/5, killed |
| 2 | killed | 14/15 → S-i | b behaves as plain 2 → S-ii |
| 3 | killed | 15/15, killed (strict FC) | isolated: ≥3/5+4/5, killed |
| 4 | killed | 16/15, killed | b behaves as plain 4 → S-iii |

- **Zero weight on b (column 2).** Any admissible set through p* contains, besides p*, only b and G3 members, all of weight 0. Any set through the chosen GE member adds only b and GE members of weight 0.
- **⅓ weights (column 3).** There is no GE in this column, so b's only companions are G3 members. Any four of {b} ∪ G3 have all gcds equal to 3, so a fibre holds at most three of them.
- **b as a plain 2 or 4 (column 4).** The identification is exact at the level FC sees: the thresholds 2/3/4 and the mass β/5. n₃ = 0 removes the 3-part of λ_b.
  - For β = 4, the "no 4s" branch never occurs.
  - For β = 2 with n₄ ≤ 2, the row has at least three 2s, so E(d) applies.

All nine surviving (β, M) pairs match S-i to S-iii exactly.

**Theorem.**
- **Case split.** It is exhaustive. In Case 1 every neighbour of the apex is plain; E5 counts as plain.
- **Case 1.** The row of Γ contains {4,4,4}, so the row of Γ* contains {1,1,1}. No P6 survivor contains a 1.
- **Case 2, Γ in S-i.** M contains {3,3,3}, so at most one entry of M* is ≥ 3. Every survivor M has at least two entries ≥ 3:

  | M | 1333 | 3333 | 4444 | 2444 | 2244 |
  |---|---|---|---|---|---|
  | entries ≥ 3 | 3 | 4 | 4 | 3 | 2 |

- **Case 2, Γ in S-ii or S-iii.** M contains {4,4}, so M* has at least two 1s. Every survivor has at most one 1.
- **Coverage.** All 3×3 pairs of classes (Γ in X, Γ* in Y) are excluded, and β* is never used. ✓

**Premises.**
- Sun(5), Sun(6), C5W, Core(5) and the k6 rules, certificates and counts are not used anywhere in the logic.
- There is no least-order frame, no "proper subgroups satisfy Sun(6)" step and no induction on |G|.
- E2's 2-power, the 3-power of E3 beyond v₃ ≥ 1, E5 and private cofactors never enter. ✓

**Erratum.** The fixes at LF69, LF81/LF101 and LF83 are correct. After them, every empty-group boundary is explicit, and "no theorem change" is accurate.

## MINOR findings and smallest repairs

Paths are relative to `…/sun-coset7/continuations/core6-written-bridge/`.

- **m1 — `C56W-v1.md:45` (INV).** "As in C5W/KII-W" points to non-premise candidates, and the identity α*/5 = |U_ihU_j|/|G| is asserted rather than derived.
  - Repair: replace the citation with "g_i⁻¹(U_i*∩U_j*)g_i = U_i∩hU_jh⁻¹, so |U_ihU_j| = |U_i||U_j|/|U_i∩hU_jh⁻¹| = |G|α*_ij/5;".
- **m2 — `C56W-v1.md:53` (FC).** The section is headed "complete proofs", but the count of t_j fibres, none equal to g_vU_v, is asserted without proof.
  - Repair: insert "(g_juU_v = g_ju′U_v iff u⁻¹u′ ∈ U_j∩U_v; g_ju ∉ g_vU_v by disjointness)".
- **m3 — `C56W-v1.md:28` and `:55-56` (Zhu binding).** The supplied README lines 38, 40 and 49 neither quote Theorem 1.1 nor give arXiv:0807.2207.
  - The application needs this form: in any group, t ∈ {3,4} disjoint left cosets of finite-index subgroups, *not necessarily distinct*, have some pair with gcd ≥ t. "Not necessarily distinct" matters because U_j∩U_v = U_k∩U_v can occur within one fibre.
  - Repair: quote that statement in the import row and bind its actual source. I did not consult the paper.
- **m4 — `C56W-v1.md:18-20` (target).** The "verbatim" quote is an ASCII transliteration (… becomes ...). It also drops README:57's sentence about rules-k6-v1 L8. Dropping it is correct, since that is a non-premise and line 63 proves E5 never matters.
  - Repair: write "verbatim up to ASCII; L8 remark omitted as non-premise".

**Outside the theorem's scope (not counted):**
- `C56W-v1.md:122-123`: "computation-free" also presupposes R1(6) (README:25 says "not yet hostile-reviewed") and Prop 4.5 (README:41). Neither status is established in the supplied text.
  - Suggested wording: "would not use the k6 certificate; R1(6) and Prop 4.5 not assessed".
- `review-package-C56W-v1.md:38-39`: "not closed under that map" understates the argument. The theorem (LF117-119) actually excludes every cross pair of classes.

**Optional clarity at LF102-106:** state explicitly that FC admissibility depends only on which label gcds reach 2, 3 and 4, plus the masses.
