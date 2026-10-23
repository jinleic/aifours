# Hostile audit: SHgen v2, ROT-FEW v3, ELT0-FEW v2

All checks below are my own. SOURCE07 was not used as evidence.

## Dispositions

| Target | Disposition |
|---|---|
| **SOURCE00, SHgen v2** | **ACCEPT**, relative to the imports listed at the end. The minor items are optional wording fixes. |
| **SOURCE01, ROT-FEW v3** | **ACCEPT**. It is conditional only on SHgen, which I accept above, and on the imports GRX, PM* and (V). I re-derived every sequence lemma in full. |
| **SOURCE02, ELT0-FEW v2** | **ACCEPT-WITH-FIXES**. Every visible step is correct. The load-bearing import, ELT0-ROT, cannot be audited from this packet and has no parent acceptance (M1). An audited alternative route reaches the same conclusion. |

I found no counterexample to any theorem or lemma **as used**.

---

## FATAL

None.

## MAJOR

**M1. SOURCE02:6-9, 25-27: the final step rests on an import that is unaccepted and not inlined.**
- Corollary ELT0-ROT and its condition (FULL) come from proof-ELT0-v3.md. That file is not in the packet.
- SOURCE06:36 lists the ELT0 files among the "unreviewed and not covered" ones. The only review mentioned is of v2, not v3.
- So the interface "N = 4p−2, κ = 0, (FULL), w^ avoids, all-odd RGR-shape form ⇒ E = 0" cannot be checked here. Neither can ELT0-v3's own imports.
- Unlike SOURCE01:4, SOURCE02 does not label itself conditional, so downstream text could cite it as settled and SHgen-free.

**Repair (either one):**
- (a) Restate the result as "CONDITIONAL on Corollary ELT0-ROT of proof-ELT0-v3.md (unreviewed)". Inherit that file's import list.
- (b) Replace L27 with the following route, which I audited. It depends on SHgen instead.
  - **Case k = 1.** Here e = 0, so MULT(i) gives m ≥ 2p−1 = L. Hence Y = g^(2p−1): all rotations equal ρ_c. No import is needed.
  - **Case k ≥ 2.** Y is zero-sum-free, so g and −g never both occur. MULT gives Y = g^m (d_j g) with d_j ≤ e+1 = k.
  - Also k ≤ p−2: from 3k ≤ 2p+1, k ≤ 3 = p−2 at p = 5, and (2p+1)/3 ≤ p−2 for p ≥ 7.
  - So, relative to c, the heavies are exactly the d_j g, with SHgen weights d_j. None of them is ρ_0, since that would need d_j = p > k.
  - E = Σ(d_j−1) ≤ k−1.
  - (H) holds: 2H = 2p−2 ≥ k−1.
  - (K) holds: η ≤ (k−1)/2 and a_max ≤ k. Then (K) is equivalent to 4p ≥ 5k+1. That follows from 3k ≤ 2p+1 and p ≥ 4.
  - SHgen therefore forces η = 0, i.e. Y = g^(2p−k) and every rotation is ρ_c.

## MINOR

**SOURCE00 (SHgen)**

1. **SOURCE00:117-118.** The scope remark cites proof-SH3-v4.md. Per SOURCE03:26-28, v4's Lemma U is false without "w avoids". Cite v5 instead. This is not a premise of SHgen.
2. **SOURCE00:59-61.** The step "A°_G − B°_G ≥ 2p−1 ⇒ A°_G = A° = 2p−1" needs A° ≤ 2p−1. That comes from bullet 1 (L56), but it is never stated. Add "(A° ≤ 2p−1, else bullet 1)", as SOURCE03:34 does.
3. **SOURCE00:29.** Erratum m4 requires a frame at a gap outside I. Name one, for example the gap between the last letter of R_1 and the first letter of S_1. This gap exists because the runs are nonempty and F ≥ 2.
4. **SOURCE00:87.** The parity reason is "a is odd". Each size has the form m° − (a−1), m° − 2r₄ or m° + 1 − a + 2r₂. The phrase "every weight is odd" is the wrong justification.
5. **SOURCE00:26.** The lower bound on m is max(0, 2κ+2−Φ). This is harmless: in FLEXa, s₀ < 0 only strengthens (D2)&(U1).

**SOURCE01 (ROT-FEW)**

6. **SOURCE01:22.** As paraphrased, INC(b) is false without "odd".
   - Counterexample: in Z_10, the sequence 1·2·3 is zero-sum-free, but A = {0,…,6} has |A| = 7.
   - For odd terms the claim is correct, and SCHERK/GROW/SET use only odd terms. I re-derived it: the four odd sums x, y, z, x+y+z are distinct, and so are the four even sums 0, x+y, x+z, y+z.
   - Fix: add "odd".
7. **SOURCE01:69-70.** "M ≤ 2p−2" is asserted but never proved, and it is not needed. The proof itself derives d + M ≤ 2p−1. Delete it.
8. **SOURCE01:75.** Replace the parenthetical with:
   - for e ≥ 1, 2p−1−2e ≥ e+1 ≥ 2;
   - for e = 0, m = L = 2p−1.
9. **SOURCE01:145-147.** "At most (2p+4)/5 in general" should read max((2p+4)/5, 3) for p = 5 and max((2p+4)/5, 4) for p ≥ 7, combining with ROT-o3 and ROT-o≤4 (SOURCE06:7-10).
10. **SOURCE01:154.** The list of uses of (F) is incomplete. All of these are implied by (F); this is an inventory fix only.
    - (F) is also the hypothesis G ≥ 2κ + w₊ of WT(c).
    - Step 3's |P| ≥ 4κ−2 needs 2p ≥ 5k−6.
    - Step 4 needs 2p ≥ 3k+1 when k ≥ 3, and p ≥ 2k−1.

**Shared (SOURCE00:21, SOURCE01:118, SOURCE02:19-20)**

11. The scope at SOURCE05:8 says only that PM* preserves avoidance and the rotation multiset. The three files additionally rely on preservation of length, F, H and the odd-block count.
    - I re-derived these for the merge R_iS_iR_{i+1}S_{i+1} → R_iR_{i+1}σ_{y_{i+1}}^{l_i+l_{i+1}} with l_i even.
    - Take z_i = z_{i+1} and split c′ = c_i + c_{i+1} with c_i even. Then the product, T(z) and C_max all match.
    - Hence a solution of the reduced word lifts to the original. Also ⌊(l_i+l_{i+1})/2⌋ = l_i/2 + ⌊l_{i+1}/2⌋, so H is preserved.
    - Merged runs stay nonempty.
    - Fix: state these properties explicitly at the cited lines.

---

## Key independent checks (abbreviated)

### SHgen

**Setting.**
- With all blocks odd, δ = k−Φ, so C_max = 2H+Φ. With m = 2p−C this gives m ∈ [2κ+2−Φ, 2p−Φ], m even, m ≤ R. This matches L24-28.
- (ZP) and κ ≥ 0 (L30) are correct.
- The odd integers in [−(p−2), p−2] are p−1 values, pairwise incongruent mod p (differences are even and smaller than 2p), and avoid 0.
- Every heavy has odd |b| ≥ 3, including b₀ = p.
- Expansion bookkeeping (L44-48) is correct: H drops by (a−1)/2, R and F shift by ∓(a−1), length is preserved, and F(u°) ≥ k.

**Lemma Ua.**
- The case split is exhaustive: A° ≥ 2p; B° ≥ κ°+1 (this needs κ° ≤ p−1, which holds); 1 ≤ B° ≤ κ°−1; B° = 0; B° = κ°.
- *Minority-copies capped case.* The k−1 nonempty runs outside G hold κ°−a+1 rotations of w. Then k−1 ≤ k−a, impossible since a ≥ 3.
- *Majority-copies capped case.* w has 2p−1−a majority lights and κ+(a−1)/2 minority lights. Since κ ≤ p−1−(a−1)/2 and a ≤ p ≤ 2p−3, also 2p−1−a ≥ κ+1. So (ρ_cρ_{−c})^{κ+1} violates (ZP) for w. This works for a = p as well.
- *Sanity check.* SOURCE03:27-28's p = 5 example is exactly this majority-capped branch, and there w fails via ρ₁ρ₋₁. This confirms the branch is needed and that the disjunctive statement of Ua is correct.

**Lemma FLEXa.**
- L₁ ≥ a_max+1 follows from κ ≥ 0 and (K).
- Both constructions preserve the value. Sizes are m°−2r₄ and m°+1−a+2r₂, and both sizes are even.
- The feasibility intervals are correct. (D1)/(D2)/(U1)/(U2) are exactly the emptiness or bound failures.
- The four intersections:
  - (D1)&(U1): L₁ ≤ a−2, a contradiction.
  - (D1)&(U2): s₁ ≤ a+η−2, so k ≥ Φ ≥ 2p−a−η+2, contradicting (K).
  - (D2)&(U1): L₁ ≤ 2κ+a−Φ, so k ≥ 2p−η−a, contradicting (K).
  - (D2)&(U2): (a+1)/2 ≤ i ≤ (a−1)/2, a contradiction.
- z → −z is legitimate because Σθ = 0 cyclically.
- The ρ₀ case works: its effective value 0 equals pc.

**Induction.**
- (H) passes to u°: 2H(u°) = 2H−(a−1) ≥ E(u°).
- (K) passes to u° because η and a_max do not increase.
- u° stays in the Sec. 0 form.

**Hidden assumptions.**
- Nonempty runs are used only at L63-64 and in the imports. FLEXa uses none.
- Maximality is never used.
- Cyclic wrap enters only through T(z), which is unchanged between w and u° (same block values), and through Σθ = 0.

### ROT-FEW

**SCHERK.**
- The e-transform identities hold: |A′|+|B′| = |A|+|B| and A′+B′ ⊆ A+B.
- The unique-zero hypothesis survives the transform: x = e+b ∉ A would force b = 0.

**GROW.**
- Arc count: |(B+x)∖B| = 1, so B is a single arc. 0 at an interior position would put −x into A(D−x), giving a zero-sum.
- The overlap formula is |I∩(I+r′)| = max(0, l−r′) + max(0, l−2p+r′). For 2 ≤ l ≤ 2p−2 it is ≥ l−1 only when r′ = ±1.

**SET.**
- When |A| ≥ 2p−1: d ≤ (p+1)/2, so 2d+2 ≤ 2p−1 for p ≥ 4.
- Otherwise, peel elements down to three: |A(D)| ≥ 8+2(d−3).

**MULT.**
- (i): the layers D_j are realised by disjoint copies, so SCHERK applies at each layer, giving extras ≥ L−m.
- (ii): there is no wrap-around because (2p−d)g would be a nonempty subset sum. d ≥ M+2 would give extras ≥ M ≥ e+1. Otherwise the extras increment is d−1, so Σ(d_j−1) ≤ e.
- (iii): 2p−1−2e ≥ e+1 is equivalent to 2p ≥ 3e+2.

**EXTRACT.**
- D(Z_{2p}) = 2p follows by prefix sums.
- Minimal zero-sums have length ≤ 2κ by parity and (ZP).
- The first crossing past 2κ+2 has length ≤ 4κ ≤ 2p.

**WT.**
- (a): the length 2p−r+1 is even.
- (b): s ≤ 2p−G−1+w₊ and the length is ≥ G+2−w₊.
- (c): at the stopping point, t−s ≥ G+1−w₊ ≥ 2κ+1 > 0, and t ≤ 4κ−2 ≤ |P| ≤ W_P. The total length lies in [2κ+2, 4κ].

**Steps 1-5.**
- L ≥ 2p−k and e ≤ k−1.
- G ≥ (4p−3k+1)/2.
- G ≥ 2κ+w₊ is equivalent to 4p ≥ 10k−8, which is (F).
- Negatives have r ≥ 2p−2κ+1 > k ≥ d_j.
- E ≤ 2p−1+2κ−R−|N| = k−1−|N|.
- (H) is equivalent to 2p ≥ 3k−1. (K) is equivalent to 4p ≥ 5k+1.
- For k = 2 there are no positive heavies and E = 0 directly.

**Sanity check and coverage table.**
- Applied to the avoider ρ₁⁹σ₀⁷ρ₋₁σ₀ (p = 5, k = 2, κ = 1): Z = g(−g), Y′ = g⁸ and E = 0, as expected.
- All 27 largest-k entries and all least-prime entries in Sec. 7 match k ≤ (2p+4)/5.

### ELT0-FEW (visible part)

- κ = 0 and R = 2p−k ≤ 2p−1, so (ZP) on [2, 2p] makes Y zero-sum-free. Then e = k−1 and 3e+2 ≤ 2p.
- d_j ≤ e+1 ≤ m, which gives the completeness ordering (FULL) as paraphrased.
- The range list at L34 is correct.

---

## Audited versus imported

### Audited here (re-derived)

- **SOURCE00:** the whole proof, apart from the imported lemmas invoked inside Ua. That covers:
  - the specialization of GRX;
  - (ZP) and κ ≥ 0;
  - weight uniqueness;
  - expansion;
  - Ua's case logic and both capped-case exclusions;
  - FLEXa;
  - the induction.
- **SOURCE01:**
  - INC(a) and INC(b) (odd terms);
  - SCHERK, GROW, SET, MULT, EXTRACT, WT;
  - all inequalities in Steps 1-5;
  - the coverage table.
- **SOURCE02:** L19-26, plus the alternative route in M1(b).
- **PM* properties used** (MINOR 11).
- **D(Z_{2p}) = 2p.** EGZ is not used by any of the three files.

### Imported (statements not inlined; not auditable here)

- **GRX:** SOURCE04, accepted in SOURCE05:7.
- **PM*:** accepted in SOURCE05:8.
- **K1:** accepted in SOURCE05:9. It is used only as a remark.
- **Davenport-alpha (V)** with erratum m4: accepted per SOURCE06:29. Its exact statement is absent from the packet; ROT-FEW's κ ≤ k−1 depends on it.
- **From the RUNS verdict**, which is not in the packet: Corollary B′(b), the C1 composition, KBH, and the uncapped implication of KB, including the definitions of "capped" and "OR-segment". SHgen's Ua depends on these.
- **Corollary ELT0-ROT / (FULL)** from ELT0-v3: unaccepted (M1).
- **ROT-o2/o3/o4:** used only for the combined coverage in SOURCE01 Sec. 7.
