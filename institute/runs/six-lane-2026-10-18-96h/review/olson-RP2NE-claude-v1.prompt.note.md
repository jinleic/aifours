# Hostile review: RP-2NE and SIGN-2Z

**Scope.** I reviewed the frozen candidate `proof-RPdelta-two-neutral-v1.md` (`e6471758…`, lines 1–164) against only the packet's imported interfaces. I used no tools; the only arithmetic is hand-checking the stated formulas. No RP-LIFT theorem, SEG-k/TRANSFER/B/B′ material or addendum was used. I re-derived every R>p step independently.

## Summary

| Component | Verdict | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| Sec. 2: parameters, C₂ₚ window, (1) | ACCEPT-WITH-FIXES | 0 | 0 | m1 |
| Sec. 2: integer lift, (2) | ACCEPT-WITH-FIXES | 0 | 0 | m2 |
| Sec. 3: zero/marked counts, (3)–(4) | ACCEPT-WITH-FIXES | 0 | 0 | m3 (citation only) |
| SIGN-2Z, Cases A–D | ACCEPT-WITH-FIXES | 0 | 0 | m4, m5 |
| Theorem RP-2NE (assembly) | ACCEPT-WITH-FIXES | 0 | 0 | inherits m1–m5 |
| Sec. 5: added-cell arithmetic | ACCEPT | 0 | 0 | 0 |

None of the fixes changes a statement, a parameter range, a case split or a conclusion.

## 1. Parameters and fixed window (`proof-RPdelta-two-neutral-v1.md:37-58`)

**Parameters.**
- With o_F = k, (0.1) gives k = M + 2κ, where M = p − δ.
- δ=1: M is even and R = p+1 is even. δ=2: M is odd and R = p+2 is odd.
- In both cases U = p − ⌊R/2⌋ = (p−1)/2 = ⌈M/2⌉.

**Ranges of m.**
- 2κ ≤ M−3 gives L ≤ U−1 for both parities.
- κ ≥ δ+1 forces M ≥ 2δ+5.
- 2m ≤ 2U ≤ M+1 ≤ k−3. So CONNECT's conditions 1 ≤ m and 2m < k hold in every layer m ∈ [L,U].

**Fact 2.1, all E ∈ [0,R].**
- The lower condition is tight at m=L, E=0.
- The upper condition ⌊E/2⌋ ≤ (p+1)/2 = p−U is tight at m=U, E=R.
- R−E also lies in [0,R], so both endpoints are floor-type.
- Mixed runs enter only through E = A_P + B_{P^c}.

**Window equivalence.** It holds in both directions, including E=0 and E=R.
- R+1 ≤ 2p, so [−R,0] gives R+1 distinct classes.
- −R ≡ M, so the complement is exactly {1,…,M−1}.

**m1 (MINOR, l.51).** "The additive even-lift isomorphism onto the even subgroup" is not unique: every map x↦2cx qualifies. Line 55 ("its class in C is e(2u_P)") holds only for the CRT lift; x↦2x breaks it.
- Fix: define e(x) as the unique even class mod 2p that is ≡ x mod p, i.e. e(x) = (p+1)x̃ mod 2p.

## 2. Integer lift and (2) (`:61-74`)

**Uniqueness and constants.**
- Edge differences lie in [−(M−2), M−2], an interval of 2M−3 < 2p integers. So α_i has exactly one representative there.
- h_i is therefore the same in every layer. The constants c_m may differ.
- Complement cancellation needs only P^c ∈ F_m. So (2) is correct.

**Cross-check (not needed by the proof).** N(P)+N(P^c) lies in [2, 2M−2] and is ≡ M (mod 2p), so it equals M exactly.
- Hence c_m = (M−Σh)/2 for every m.
- This agrees with Σh ≡ D ≡ M (mod 2).

**Parity and zeros.**
- h_i ≡ d_i (mod 2).
- h_i = 0 iff α_i = 0.
- An empty run has an even h_i with |h_i| ≥ 2. An odd run has an odd h_i.
- No RP-LIFT nonzero-h conclusion is used.

**m2 (MINOR, l.64).** "All seven VL bindings apply" includes binding 2 (0 ≤ E ≤ p, representative in [1,p−1]). That binding is specific to R=p and is false here.
- Fix: "bindings 1, 3, 4, 6; (1) replaces binding 2; bindings 5 and 7 are used only for the generic stretch facts re-proved in Cases C and B."

## 3. Zero and marked counts (`:78-88`)

- **(NE)** holds by CRT. Zeros lie in nonempty even runs, because maximality gives θ_i ≠ 0 on empty runs (K0star l.25).
- **P0 authority.** Theorem P gives F + Σ⌊r_i/2⌋ ≤ 3p−2 for every G-avoider of length 4p−2, which yields o ≥ M. This step:
  - does not depend on how empty runs are classified;
  - needs no κ, B, purity or genuineness hypothesis;
  - is the same step used in accepted Fact 2.2's proof.
- **Counts.**
  - v ≤ δ, so z ≤ v ≤ δ ≤ 2.
  - g_E ≥ 2κ−2δ+v, which is consistent with P0's own bound v+g_E ≤ 2κ.
  - e−z ≥ 2(κ−δ)+(v−z) ≥ 2. This is where κ ≥ δ+1 is used.
- **Baseline.** It holds pointwise because Z and the zero set are disjoint. (4) gives S ≥ k+2.

**m3 (MINOR, l.22/82).** Fact 2.2's *statement* does not contain o_R ≥ 2p−R.
- Fix: cite P0 directly (K0star-r2 l.73–75, accepted within the K0* r2 mathematics) and note that the same step appears in Fact 2.2's proof. This is what the packet's bridge already does.

## 4. SIGN-2Z (`:97-130`)

I checked SIGN-2Z as a standalone lemma. The zero signs are arbitrary, and each case lands inside [L,U].

**Case A.** S ≥ k+1 > M−2.

**Case B.**
- A zero-weight stretch consists only of zeros, so there are at most z of them. Hence S ≥ 2m0−z.
- Flipping the f lightest stretches of the lighter family removes exactly 2f boundaries and creates none, leaving 2U boundaries. The new sum is ≥ SU/m0.
- Strictness for z=2 comes from U/m0 < 1.
- In the application there is slack: 2U−z ≥ M−1 for both δ.

**Case C.**
- n ≥ k−4m0, and m0 ≤ κ, so n−2f ≥ M−2−2κ ≥ 1 and γ < 1. This is tight at δ=2, κ=(p−5)/2.
- Adjacent indices of J lie in one stretch interior, so independence in the paths implies independence on the cycle.
- The algebra gives a bound ≥ M−2 + (2m0−z) + (1−γ)e > M−2 for every placement 0 ≤ e_J ≤ e and 0 ≤ z_J ≤ z.

**Case D.** k > 2L, and S > k gives S(M−2)/k > M−2.

**m4 (MINOR, l.98–101), quantifiers.**
- Fix: "let z ≤ 2 be the number of zeros … then **there is** s with 2m changes, L ≤ m ≤ U, and Σs_ih_i > M−2."

**m5 (MINOR, l.110), nonadjacency in Case B.**
- Fix: add that stretches of equal parity differ by an even amount mod 2m0, while neighbours differ by ±1, and here m0 ≥ U+1 ≥ 4.

**Auxiliary counterexample versus avoider.** The hypothesis e > z is necessary.
- Take e = z = 0 and h ≡ 1. Then every admissible s has Σs_ih_i = k − 2|P^c| ≤ k − 2L = M−2.
- The lift data are internally consistent here: N(P) = |P| − κ lies in [1, M−1].
- This is a counterexample to the *auxiliary* assertion with e ≥ z. It is **not an avoider**: nothing shows that such an h arises from a word.
- At δ=2, κ=2, (3) allows v = g_E = 0, so this argument cannot reach that cell. The candidate correctly leaves it unclaimed (l.156–157).

## 5. RP-2NE assembly (`:134-138`)

- The positive set of the sign vector has 2m ≥ 6 changes, so it is a proper nonempty set with m ∈ [L,U]. This contradicts (2).
- W's cyclic selection becomes an increasing-original-index selection by conjugation (VL binding 1, K0star l.15).
- The normalisations preserve block lengths, maximality, genuineness, κ and R.
- "Any B" is literal: no purity, one-sign, B<κ or value restriction appears anywhere.

## 6. Added-cell arithmetic

Checked by hand from V5 l.40.

**δ=1.**
- New cells: [2, min((p−5)/2, ⌈(p+5)/4⌉−1)].
- SEG-num first meets the range at p=17 (in the cell {6}).
- p=11 adds {2,3}; p=13 adds {2,3,4}.

**δ=2.**
- New cells: [3, min((p−5)/2, ⌈(p+8)/4⌉−1)] ∪ {(p−5)/2}.
- SEG-num is first nonempty at p=23, where the new cells are [3,7] ∪ {9}.
- For p ≤ 19 the new cells are the whole range.
- p=11 adds {3}; the low interval and the top cell coincide and are counted once. p=13 adds {3,4}.

**K2P+** is disjoint from both ranges, and is empty at p=11, δ=2.

**(δ,κ) = (2,2)** is excluded by the hypothesis κ ≥ δ+1 and is asserted nowhere. Confirmed.

## Exact supported coverage

**Covered.** Take p ≥ 11 prime and δ ∈ {1,2}, with R = p+δ rotations all in one pair {ρ_x, ρ_−x}, x ≠ 0, and every maximal cyclic constant block odd. If **δ+1 ≤ κ ≤ (p−5)/2**, there is an increasing-index identity 2p-subword. This holds for any B, with no purity, B<κ, empty-run or value hypothesis.

**Not covered.**
- κ ≤ δ, including (1,1), (2,1) and (2,2).
- κ ≥ (p−3)/2.
- δ ≥ 3.
- p ∈ {5,7}, where the range is empty.

**Gap against I.14's numerical bands (arithmetic only).** For each δ, at least κ ∈ {(p−3)/2, (p−1)/2, (p+1)/2} remain outside both RP-2NE and those bands. No structural criteria or novelty were assessed. REFL, INV* and Olson remain OPEN.

## Non-binding remark (outside the frozen candidate; not a verdict or a coverage claim)

Line 127 justifies the upper bound correctly for z=2. At δ=1, however, z ≤ 1, so Case C stays strict through 2m0−z ≥ 1 even when γ = 1.
- On a hand check, the steps appear to go through at δ=1, κ=(p−3)/2, where L = U.
- At δ=2 the analogue fails, because n−2f can be −1.
- Any such cell needs its own frozen candidate and review.
