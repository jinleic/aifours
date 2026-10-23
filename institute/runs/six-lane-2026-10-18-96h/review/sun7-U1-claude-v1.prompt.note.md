# Hostile referee report: K7-U1 (sha `d4e6cdc9…`)

**Overall: ACCEPT-WITH-FIXES. 0 FATAL, 1 MAJOR, 7 MINOR.**

- ROW-1*, CROSS*, LIGHT* and Theorem K7-U1 are correct at the stated scope: exactly one marked vertex z, with m_z = 2^E3^A5^B and all exponents unbounded, including E, A ≥ 1 together.
- The only MAJOR finding is in the §6 frontier sentence and the title, not in the proof.
- Full Sun(7) and class K7 remain open. The theorem does not cover 2- and 3-markers on different vertices. It also does not cover the case where 2 and 3 sit on z and the 5-marker sits on another vertex (MJ1).

## Verdict 1: ROW-1* is CORRECT (the text needs m1)

- **(G2) holds for every E, A, B.** λ_z = m_z w_z α_vz and λ_u = w_u α_vu. The w's are coprime to each other and to 30, so gcd(λ_z, λ_u) = gcd(m_z α_vz, α_vu), which divides α_vu.
- **Weights with y_z = 0 are feasible.** By heredity, T∖{z} is allowed whenever T is. Cross-class gcds on W∖{v} are 1, so ROW-U's class weights apply unchanged.
- **(a):** if 1 ≤ k5 ≤ 4, the R5 weights give 5 and the nonempty rest gives at least 1, so the total is ≥ 6. ✓
- **(b), k3 ∈ {1,2}:** R3 gives 3 and the remainder gives min(N,4) ≥ 3 with N ≥ 3. ✓
- **(b), k3 = 3 with remainder {4,x}:** the claim holds only with explicit weights.
  - x = 1: y = (1,1). The two elements are singleton classes. Value 5.
  - x ∈ {2,4}: y = (½,½). The only allowed non-singleton is the pair. Value 3 or 4.
  - Totals are 8, 6 and 7.
  - The text calls these "standard weights". The defined standard weights for b ≤ 2 (¼ on fours, ½ on twos) give a remainder value of 2 and a total of 5 < 6. The arithmetic is right; the label is literally false (m1).
- **k3 = 4:** y = 1 on the lone 4 (a singleton class) plus ⅓ on R3 gives 8. ✓ **k3 = 5** is vacuous. ✓
- **Final kill, α_vz ∈ {3,4,5}:** the weights are ⅓ on R3, 1 on R1, ½ on twos and ⅓ on z. Through z, for every m_z:
  - R1 is excluded, since its gcd with λ_z is 1.
  - {z,2,2} has all gcds dividing 2, so it is not allowed.
  - {z,3,3,3} has all gcds dividing 3, so it is not allowed.
  - {z,2} sums to 5/6.
  - {z,3,3} is allowed and sums to exactly 1.
  - The value is 5 + α_vz/3 ≥ 6. ✓
- **No ROW-1(c) is used.** Step 1 uses only (a), Step 2 uses only (b), and the z-row comes from ROW-U at z. The remark's reason is right: gcd(m_z α_vz, 2) = 2 whenever 2 | m_z.

## Verdict 2: CROSS* is CORRECT

- **Parameters.** γ = 6 at every apex; ℓ_z = m_z w_z, ℓ_a = w_a, ℓ_b = w_b.
- **τ_min = 4 for every E, A, B.** By (T1): edge zb gives 4 | w_aτ, so 4 | τ; edge za gives s_a | τ; edge ab gives x/gcd(x, m_z w_z) | τ, which divides x and hence 4.
- **τ_max.** (T2)/(T3) at apexes z, a, b give τ/(6x) ≤ s_a/6, τ/24 ≤ min(s_a,x)/6 and τ/(6s_a) ≤ min(4,x)/6. I re-derived the table: s_a = 1 gives 1, 2, 4 and s_a = 2 gives 2, 4, 8 (for x = 1, 2, 4).
- **Inverse.** The indices, ℓ and γ are unchanged. The edge values (za, zb, ab) are (4, s*_b, x*), so the table holds with a ↔ b and τ*_min = 4. (C1) and (C2) follow. ✓
- **(C3).** F7 at apex z reads 24 ≥ 6·x·s_a. The orientation is correct: the contained set belongs to the vertex whose z-edge appears in the hypothesis (a with s_a; in the inverse, b with s*_b).
- **§2 is load-bearing.** Without it, when A ≥ 1 and s_a = 2, x = 3 survives (τ_min = 4 ≤ τ_max = 6). When B ≥ 1, x = 5 survives. So Z2's "no 3-marker" assumption is genuinely replaced. For cross pairs, x = 5 could also be removed locally via x* = 1; x = 3 cannot.

## Verdict 3: LIGHT* is CORRECT

- μ(D_v) = α*_zv/6 by INV(b), and D_v ∩ X_v = ∅ by (V1). On a tight edge, D_v ⊆ Y_v with equal finite size, so D_v = Y_v.
- The local index is d_v = α*_zv·w_v, since v is unmarked; n_z never enters.
  - (L1): the pairwise gcds are ≤ 2 < 3.
  - (L2): a coprime index forces a singleton, by Sun(2).
  - (L3): the union of the D_v misses U_z, so its measure is at most 1 − 1/n_z, strictly below 1.
- **Mirror.** α** = α by the involution, so q* = α. With g_z = 1 we get g*_z = 1 and U*_z = U_z. A common left translation conjugates every U*_i by the same element, so α* is unchanged.

## Verdict 4: Theorem K7-U1 is CORRECT at the stated scope (|M| = 1)

- **Step 0.**
  - ROW-U at z needs only six unmarked neighbours; n_z enters only through "< 6". By E6 the same holds for α*.
  - Hence W = F ⊔ F* with |F| = |F*| = 3, and s_a, s*_b ∈ {1,2}.
  - Any 1 in the z-row lies in F*, and any 1 in the inverted z-row lies in F.
- **Step 1.**
  - k5 ∈ {0,5} propagates to all 15 W-pairs, so α* = 1 on every W-pair.
  - In the inverse LFC at v, λ*_u = w_u is coprime to λ*_z = m_z w_z α*_vz. So y ≡ 1 is feasible, with value 5 + α*_vz ≥ 6.
  - The mirror case uses α** = α. This works for any m_z.
- **Step 2.** If W3 is nonempty then |W3| ≥ 4, but W3 ⊆ F* and |F*| = 3. In the inverse, W3* ⊆ F. Both orientations are needed, because (C1) requires x* ∉ {3,5}.
- **T4.** (C2) gives α = α* = 4 on the pair (a0, b0), contradicting (C1). ✓
- **T3.**
  - α*_ab0 = 4 forces α_ab0 = 2, so X_a ⊆ X_b0.
  - Edge za is tight, so D_b0 ⊆ Y_b0 ⊆ Y_a = D_a.
  - μ(D_b0) = 1/6 > 0, so some right coset has {a, b0} ⊆ S_R, contradicting (L2). ✓
- **T2.** This is the exact mirror of T3. ✓
- **T1.**
  - All six z-edges are tight.
  - If b is "in", then D_b ⊆ D_a, so D_b ∩ D_b' = ∅ by (L1).
  - If at most one b were "out", the three D_b would be pairwise disjoint with measure ⅓ each, total 1. This contradicts the strict bound in (L3).
  - The same holds in the mirror. An out b and an out* a then give α = α* = 4 on (a, b), contradicting (C1). One out vertex per side already suffices. ✓
- **R0 lift.** The finite quotient G/N keeps the labelled index tuple, so the class and the unique marked vertex are preserved. ✓

## Findings

**FATAL:** none.

**MAJOR**

- **MJ1: the §6 "Covered" bullet (last sentence) and the title (a scope error; the proof is unaffected).**
  - The sentence "K7 is open only when the 2-marker and the 3-marker sit on two different vertices" is not established.
  - Counterexample to the claim: take E, A ≥ 1 on z and B ≥ 1 on some y ≠ z, so |M| = 2.
  - None of the cited results excludes this case:
    - K7-U1 needs |M| = 1.
    - K7-Z2 needs no 3-marker.
    - K7-M0 and K7-M1 need |M| ≤ 1.
  - The only supplied frontier (Z2 verdict `0f6b9aa3…`) leaves open two families: "both a 2- and a 3-marker" and "no 2-marker, with the 3- and 5-markers on different vertices". The second is the evident target of the unpinned "K7-35".
  - So unless K7-35's accepted scope also covers a 2-marker on the 3-marked vertex, the sentence records an open case as closed.
  - The title's "(in particular: 2- and 3-markers on one vertex)" overstates in the same way.

**MINOR**

- **m1: §1(b), case k3 = 3 with an entry 4.** The phrase "standard weights give 4+1, (4+2)/2, (4+4)/2" is false under the weights defined a few lines earlier.
- **m2: label collision.** LIGHT*'s "(L1)–(L3)", which T1–T3 cite, collide with rules-k7-v1's L1 (the triangle rule, which §3 cites as "(L1)") and with L2/L3 (rule K).
- **m3: §6 "replaced" item (ii).** "(and h_z = 0 to kill x = 5)" misdescribes Z2. Z2 allows a 5-marker at the centre, and it removes x = 5 because α + α* ≤ 6 forces x* = 1, which the inverse τ test then kills.
- **m4: unpinned references.** K7-M1 and K7-35 have no SHA or stated scope, either in the file or in the supplied sources. K7-Z2 is pinned only in the parent verdict. The re-proof claims and the §6 frontier both depend on these references (navigation only).
- **m5: F7 attribution.** The file credits verdict `73a25ba6…` with accepting addendum A1, but A1's own header says nothing in it is reviewed. The only supplied evidence of acceptance is the Z2 verdict ("general T/VFC/F7 rules"). This is not load-bearing: F7 at apex z re-derives directly (the T3 value meets the T2 bound, so the finite sets are equal and X_a = U_z(U_a ∩ U_b) ⊆ X_b).
- **m6: header notation.** e_z, f_z and h_z are never defined in the file; §0 uses E, A, B instead.
- **m7: symmetry used silently.** α and α* are used as symmetric without comment: in Step 1's propagation, Step 2's closure of W3 (and α_vz = α_zv against F), and CROSS*.

## Minimal repair (erratum text)

- **E-1 (MJ1).**
  - Title: "(in particular: 2- and 3-markers on one vertex, no other vertex marked)".
  - §6: replace the "With accepted…" sentence with: "If accepted, then together with K7-M0, K7-M1 and K7-Z2 [SHAs], K7 remains open for configurations with |M| ≥ 2 that carry both a 2-marker and a 3-marker. These markers either sit on different vertices (5-marker absent, on one of them, or on a third vertex), or sit on one vertex z with the 5-marker on y ≠ z. K7 also remains open for configurations with no 2-marker and the 3- and 5-markers on different vertices. Any part closed by K7-35 must be cited by SHA and exact scope."
- **E-2 (m1).** Replace the phrase with: "Explicit weights: if x = 1, put y = 1 on both remaining elements (different classes, so singleton allowed sets only). If x ∈ {2,4}, put y = ½ on both (the only allowed non-singleton is the pair, since gcd(4,x) ≥ 2). The values are 5, 3, 4. The standard ROW-U weights give only 2 here."
- **E-3 (m2).** Rename the LIGHT* items to (LT1)–(LT3) and (LT1*)–(LT3*), and update the citations in T1–T3.
- **E-4 (m3).** Replace the parenthetical with: "(Z2 removed x = 5 via α + α* ≤ 6 ⇒ x* = 1, which the inverse τ test kills; a 5-marker at the centre was allowed)".
- **E-5 (m4, m5).** Pin K7-M1, K7-Z2 and K7-35 by SHA with quoted scopes, or delete the claims that rely on them. Cite the record that actually accepted A1.
- **E-6 (m6, m7).** Add to §0: "e_z = E+1, f_z = A+1, h_z = B. α and α* are symmetric (I_ij = I_ji, and α* is the α-matrix of a configuration)."

## Verification boundary

- This is a hand check only: no tools, no computation, and no SHAs verified.
- I did not see the texts of K7-M1, K7-35, the Z2 candidate or erratum, verdict `73a25ba6…`, or README §§1, 5.
- Accepted imports (LFC (c)/(d), INV, ROW-U and its class analysis, E1–E8, L1, VFC (V1)–(V4), R0) were used at face value. F7 was re-derived.
- No novelty, Lean or human-review claim is made.
