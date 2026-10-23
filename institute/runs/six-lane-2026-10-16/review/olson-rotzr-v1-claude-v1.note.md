# Audit of Theorem ROT-ZR v1 (SOURCE00)

**Bottom line.** I found no FATAL or MAJOR problem. I re-derived every step of REALIZE, ZSTRUCT, LAMBDA, EBOUND and the theorem's integration by hand. All are correct when the imports are used only at their accepted scopes. The fixes needed are all MINOR: statement completeness, the REFL interface wording, and novelty/scope. I found no counterexample, and the sequence bound is attained at κ̂ = 2.

| Claim | Verdict |
|---|---|
| REALIZE | ACCEPT |
| ZSTRUCT | ACCEPT (optional clarity, m2) |
| LAMBDA | ACCEPT |
| EBOUND | ACCEPT |
| Theorem ROT-ZR | ACCEPT-WITH-FIXES (m1, m3, m4) |
| ZR2 | ACCEPT |
| ZR3 | ACCEPT-WITH-FIXES (m5) |
| Uniform INV*/OLSON-ZR2/ZR3 | ACCEPT-WITH-FIXES (m6, m7) |

## 1. REALIZE (SOURCE00:32-47)

- **Length bound.** L ≤ X_i + n holds because each a_(j) with j < i is at least 1. Since L ≥ p+1, this gives X_i ≥ p+1−n.
- **The three n-cases.**
  - n = 1: W ≥ 2X_i + 1 ≥ 2p + 1.
  - 2 ≤ n ≤ p−1: (n+1)(p+1−n) is concave, so its minimum on [2, p−1] is min(3p−3, 2p) = 2p (p ≥ 3). Hence W ≥ 2p + n.
  - n ≥ p: W ≥ 3n.
  - Each case contradicts W ≤ 2p−1.
- **Edge cases.** m = 0 is covered (i = 1, n = h = L ≥ p+1). The claim also forces m ≥ a_(1) ≥ 3 whenever h ≥ 1.
- **Subset-sum fill.** The prefix property fills [0, W]. For each heavy value, the strictly smaller occurrences realize it; they are distinct from q and need at least two terms.
- **Two-term realizations.** Even s gives |Q| even, hence ≥ 2 (s = 2 is g·g). Odd s with |Q| = 1 is handled by the substitution.

No finding.

## 2. Setting (S) (SOURCE00:51-56)

Correct as written:
- |Z| = 2t ≤ 2κ by (S1).
- Y′ is zero-sum-free by maximality of Z.
- L ≥ 2p−k ≥ p+1, which is inside SC0's accepted scope (C_(2p), p ≥ 5, odd terms give odd a_i; SOURCE06:16).
- e′ is even, and m − slack ≥ 2L−2p+1+h ≥ 3.

**m1 (MINOR, SOURCE00:51).** (S) must state κ ∈ ℤ, because S1(a) is accepted only on the integer domain (SOURCE04:51). This is harmless for the theorem, where κ̂ is integral since F ≡ k (mod 2).

## 3. ZSTRUCT (SOURCE00:58-62)

- **Parity.** r is odd, so even r (including r = 2) cannot occur.
- **Case 3 ≤ r ≤ W.** Q ⊆ Y′ is disjoint from Z and σ(Q) = rg = z. So (Z−z)·Q is a zero-sum of length 2t−1+|Q| ≥ 2t+1, contradicting longestness. (S1) is not needed here.
- **Y(0).** W ≥ L ≥ p+1, so r = p falls in the previous case; hence Y(0) ∉ Z. Also Y(0) ∉ Y′, since a_i ≤ k ≤ p−1.
- **Case r ≥ W+1 ≥ p+2.** s = 2p−r ≤ slack ≤ m−3, so g^s·z is a zero-sum of length s+1 ≤ 2t.
- **Boundary.** r = 2p−1 forces slack ≥ 1, and slack = 0 forces t = 0.

**m2 (optional).** State "Y(0) ∉ Y" explicitly at SOURCE00:61; it is what excludes ρ_0 in EBOUND.

## 4. LAMBDA (SOURCE00:67-76)

- **Proof check.**
  - (Λ2) is correct.
  - In (Λ1), the worst induction step is P_2 ≤ 2(2t−1) = 4t−2 ≤ m, using g^{P_j} ⊆ Y′.
  - n₊ = 0 is vacuous (it would force Σs ≤ 0).
  - The arithmetic checks: 3L−2p+1 ≥ 8t−4 ⟺ 14t ≤ 4p+6κ−3k+5.
- **Attempted break** (p = 11, κ = 3, k ∈ {9, 10}, where the stated (Λ) fails):
  - The wrap Z = g(−5g)⁴(−3g) has Σs = 23 = n₊ + 22.
  - But s = 5 ≤ slack forces W ≤ 16, so e′ ≤ 4 and m ≥ 10 = 4t−2.
  - Then g¹⁰(−5g)² is a zero-sum of length 12 > 6, so this Z is not longest. No counterexample.
- **Optional sharpening** (reviewer-derived, unreviewed, not required):
  - ZSTRUCT gives s ≤ slack, so e′ ≤ 2p−1−L−s and m ≥ (3L−2p+1+s)/2.
  - The induction then needs only 6κ ≤ 4p−3k+4.
  - At κ = 3 this covers every k ≤ p−1 for p = 11 and p = 13.

## 5. EBOUND (SOURCE00:80-93)

- **Same generator for all letters.** One fixed c (with g = Y(c)) is used throughout.
  - Y′ letters have b = a_i ≤ k ≤ p−1, so b ≤ p−2 by oddness.
  - Z letters are g (b = 1) or −sg (b = −s, with s ≤ 2κ−1 ≤ p−2).
  - So E = e′ + Σ(s_i − 1) is exactly SHgen's E (SOURCE09:39-42); lights contribute 0.
- **Algebra.** All of the following check:
  - e′ = k−1−2κ+2t−slack;
  - n₋ ≥ 2t/(s+1);
  - monotonicity in t;
  - G(1..5) = −1, −1, 0, 1, 2;
  - the AM-GM bound.
- **Sharpness** (sequence level only):
  - Take Y = g^{2p+2−k}((k−3)g)(−3g) with κ = 2 and even k, 6 ≤ k ≤ p−1. Its zero-sums are only g³(−3g), plus (3g)(−3g) when k = 6.
  - So (S1) holds, Z = g³(−3g), and E = k−2 = k−1+G(2).
  - Instances: p = 7: g¹⁰(3g)(−3g); p = 11: g¹⁴(7g)(−3g); p = 13: g¹⁶(9g)(−3g).
- **Optional.** Using integrality of n₋ improves G(3) to −1.

## 6. Theorem ROT-ZR (SOURCE00:97-106)

- **Setup.** R = 2p+2κ̂−k follows from F = 2H+k. (ZP) is GRX's all-plus pattern (Φ = 0, C_max = 2H, sizes in [2κ̂+2, 2p]).
- **(H).** E is an integer, so (H′) gives 2H ≥ E.
- **(K).** (K′) gives (K) through KETA's unconditional inequality η + a_max ≤ E + 2 (SOURCE08:16).
  - This use is correct.
  - KETA's "E ≤ k−1" form would fail once G > 0, i.e. κ̂ ≥ 4.
  - η = 0 ⟺ E = 0.
- **Hidden assumptions.**
  - c ≠ 0 holds because g has order 2p.
  - Empty runs are handled by SHgen-E.
  - κ̂ integrality and k ≥ 2 are explicit.
  - Consistency check: at κ̂ = 1 the theorem reproduces PAIR1's E ≤ k−2.
- **m3 (MINOR, SOURCE00:106).** Write o_F(u°) ≤ k ≤ p−1, which is the accepted REFL interface (SOURCE11:11), not "= k".
  - Spell out the discharge (SOURCE08:36; ZS overlay V3, SOURCE10:26): k is fixed along expansions, and the base words have length 4p−2 and a single nonzero pair.
  - REFL r4's "condition (d)" (SOURCE11:16) is not in this packet, so the transfer rests on the K01 discharge text.
- **m4 (MINOR, SOURCE00:103).** Cite that w^ has the SHgen-E form (SOURCE03:37-43) with F, R ≥ 1 and κ̂ ≥ 0 (SOURCE04:53).

## 7. Corollaries

**ZR2 (SOURCE00:108-109): ACCEPT.** 12 < 2p, (H′) is k ≤ 2p−4, (K′) is 2k ≤ 2p−1, and κ̂ = 2 ≤ (p−1)/2.

**ZR3 (SOURCE00:110-111).** The arithmetic is correct: 30 < 2p ⟺ p ≥ 17, and ⌊(4p−19)/3⌋ = 8 and 11 for p = 11 and 13.
- **m5 (MINOR).** There is no actual statement. Add: "p ≥ 17: every terminal (k, 3) with 4 ≤ k ≤ p−1; p = 11, 13: 4 ≤ k ≤ ⌊(4p−19)/3⌋."
- At p = 7 nothing is gained: (Λ1) gives k ≤ 3, below DAV's minimum of 4.

**Uniform corollaries (SOURCE00:113-122).** The case split is complete:
- k = 1 goes to K1.
- k = 2 forces κ̂ ≤ 1 by DAV, so ROT-K01 applies; so does every κ̂ ≤ 1.
- κ̂ = 2 forces k ≥ 3, so ZR2 applies; κ̂ = 3 forces k ≥ 4, so ZR3 applies.
- Deletion ledger: Case 1 needs o ≤ p−1 ≤ 2p−3. Cases 2 and 3 never raise o_F or lower F−o_F.

**m6 (MINOR, SOURCE00:117-118).** Cite three things:
- the exclusion of the terminal even block (SOURCE03:39-41);
- that K1 includes c ≠ 0 (SOURCE08:51);
- the relation κ̂ = κ(w) − (o_F−k)/2 (SOURCE04:71).

**m7 (MINOR, SOURCE00:126-130).** Novelty must be measured against K01 (F−o_F ≥ 2p−4, SOURCE08:5), not ZX alone.
- F−o_F is even, so the new uniform band is exactly F−o_F = 2p−6 (and = 2p−8 for p ≥ 17), with (2p+1)/3 < o_F ≤ p−1.
- At p = 11, only F = o_F+16 is new.
- p = 7, o_F = 6, F = 14 is also new and is missing from the examples.
- Derivable but unclaimed (needs its own review): p = 11 with o_F = 8 and F−o_F = 14; p = 13 with o_F ∈ {10, 11} and F−o_F = 18.

## What remains unverified

- **Imported proofs** were read only at their accepted scope, not re-proved:
  - the index-one theorem behind SC0, and S1(a);
  - GRX, PM*, the normal form, DAV and K1;
  - the internals of SHgen and SHgen-E;
  - REFL-few-odd, including condition (d);
  - RGR-LONG and OLSON Case 1.
- **Nothing was computed.** The sharpness family and the LAMBDA sharpening are my own derivations and have not been reviewed.
- **No existence claim.** Nothing here asserts that avoiders with these parameters exist.
