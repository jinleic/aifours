# Referee report: `proof-S1-sharp-v1.md` (SHA `992ab63f…2150cb0c` as supplied; not re-hashed, since I had no tools)

**Basis.** I read only the inlined candidate and the four embedded records, at their recorded scopes. The candidate has no line numbers, so findings are located by section, step and quoted phrase.

## Verdicts

| Item | Verdict | FATAL | MAJOR | MINOR |
|---|---|---|---|---|
| **(A) Lemma S1-sharp** | **ACCEPT-WITH-FIXES** | 0 | 0 | 9 |
| **(B) Corollary S1-sharp-INV/OLSON** | **ACCEPT-WITH-FIXES** | 0 | 0 | 5 |

I re-derived every implication below and found no counterexample and no gap. All fixes are wording, attribution or scope labels, and no step's validity depends on any of them.

---

## (A) Independent re-derivation

**Conventions.** u = 2κ = p+δ. The inductive range (p+3)/2 ≤ κ ≤ ⌊2p/3⌋ is the same as: δ odd, δ ≥ 3, 3δ ≤ p.
- By parity, 3δ ≤ p is the same as p ≥ 3δ−1. The candidate's "6κ is even" remark is correct.
- For prime p, p ≠ 3δ, so in fact p ≥ 3δ+2.
- The inductive range is nonempty only for p ≥ 11.

**Step 1 (shortest long zero-sum).**
- (ZP) and even length give N ≥ 2p+2.
- A nonempty proper zero-sum T′ ⊆ T with |T′| ≥ u+2 would be a shorter admissible choice. Minimality alone gives this; (ZP) is idle here. So |T′| ≤ u.
- The complement of T′ gives |T′| ≥ l = N−u.
- D = 2u−N is even, D ≤ 2δ−2, and l ≥ p−δ+2.
- D ≥ 0 is not yet known at this point. It follows in Step 3 and is first used in Step 5. ✓

**Step 2 (all proper zero-sums minimal).**
- A nested T″ ⊊ T′ makes T″ and T′−T″ nonempty proper zero-sums of T.
- Then 2l ≤ u, so N ≤ 3κ.
- Since N ≥ 2p+2, the contradiction needs only **3κ ≤ 2p+1**, not 3κ ≤ 2p. ✓

**Step 3 (induction at κ−1 applied to T).**
- Suppose every nonempty proper zero-sum of T has length ≤ u−2. Then T's zero-sum lengths lie in [0, u−2] ∪ {N}, with N > 2p.
- So T satisfies (ZP_{κ−1}). The Lemma at κ−1 ∈ [(p+1)/2, ⌊2p/3⌋−1] (S1+ or the induction) then forces N ≤ u−2, which is false.
- The case "no proper zero-sum at all" is covered by the same argument, so no Davenport call is needed.
- Parity and Step 1 then give some Q with |Q| = u. Q′ = T−Q is nonempty and proper with |Q′| = l. Step 1 applied to Q′ gives l ≤ u, so D ≥ 0.
- Both Q and Q′ are minimal by Step 2. ✓
- **Scope point.** The κ−1 statement is applied to T, not to a rotation sequence, so the base must hold for sequences of arbitrary length. It does:
  - S1(a): one Davenport call gives N ≤ 4κ ≤ 2p−2.
  - The accepted S1(c) derivation works entirely inside T.

**Step 4 (index-one import).**
- Scope: Q is minimal over C_{2p}, n = 2p ≥ 10, and |Q| = p+δ ≥ p+3 ≥ ⌊n/2⌋+2. This is inside the recorded general statement (C_n, n ≥ 3).
- This is the first load-bearing use at a composite modulus. The record's prime-order paragraph is only an illustration and does not restrict the statement.
- Order of a, over the possible values {1, 2, p, 2p}:
  - ord 1: every term would be 0, which is even. The candidate omits this case.
  - ord p: a lies in 2Z_{2p}, so all multiples are even.
  - ord 2: a = p, every odd term has least coefficient 1, so the coefficient sum is |Q| = 2 ≠ p+δ.
- Hence a = g is an odd generator. Coefficients are odd, lie in [1, 2p−1], and sum to 2p.
- Derived facts, all correct:
  - mass(S_Q) = p−δ and |S_Q| ≤ (p−δ)/2.
  - m ≥ (p+3δ)/2.
  - S_Q ≠ ∅, since otherwise the coefficient sum would be p+δ.
  - b_min ≤ p−δ+1.
  - max S_Q ≤ (2p−m) − 3(|S_Q|−1) = p−δ−2|S_Q|+3.

**Step 5 (MC).**
- (Q−Q₁)W has coefficient sum 2p − A_{Q₁} + A_W ≡ 0.
- It is empty exactly for (Q₁, W) = (Q, ∅) and equals T exactly for (∅, Q′). These are precisely the two excluded pairs.
- Otherwise Step 1 gives l ≤ u−|Q₁|+|W| ≤ u, which is |W| ≤ |Q₁| ≤ |W|+D. ✓

**Step 6 (every Q′-coefficient ≤ D+1).** Suppose c ≥ D+2.
- W = {z} is admissible: W ≠ ∅, and W ≠ Q′ because l ≥ 2δ+1.
- **c ≤ m:** take Q₁ = g^c. Its size c ≥ D+2 contradicts MC.
- **c > m:**
  - Z₀ ⊆ S_Q, inclusion-minimal with A ≥ c−m, exists because A_{S_Q} = 2p−m > c−m. It is nonempty.
  - Minimality gives A_{Z₀} ≤ c−m+b₀−1.
  - b₀ ≤ p−δ−2|S_Q|+3 ≤ m, since that only needs |S_Q| ≥ 3−2δ.
  - So 1 ≤ c−A_{Z₀} ≤ m, and Q₁ = Z₀·g^{c−A_{Z₀}} ⊆ Q has coefficient sum c and size c − mass(Z₀).
  - If size ≤ D+1, then b₀ ≥ m−D+|Z₀|.
- **|Z₀| = 1:** b₀ ≥ m−D+1 ≥ p−δ−|S_Q|+3 > p−δ−2|S_Q|+3 ≥ b₀. Contradiction, since |S_Q| ≥ 1.
- **|Z₀| ≥ 2:** mass(Z₀) ≥ 2(m−D+1) ≥ 2(p−δ−|S_Q|+3) ≥ (p−δ)+6 > mass(S_Q), using 2|S_Q| ≤ p−δ. Contradiction.
- This is equivalent to the candidate's route. ✓

**Step 7 (prefix argument, A_{Q′} = 2p).** Suppose A_{Q′} ≥ 4p.
- Take the shortest prefix W with A_W ≥ 2p.
- Its last coefficient is ≤ D+1, so r = A_W−2p ∈ [0, D].
- W ≠ Q′, since A_W ≤ 2p+D < 4p. And r ≠ 0, since Q′ is minimal.
- MC on (g^r, W) is admissible (r ≤ D < m) and gives |W| ≤ r, so mass(W) ≥ 2p.
- Let s = 2p − A_{W⁻}. Then s ∈ [1, D+1] and s ≤ m.
- MC on (Q−g^s, W⁻) is admissible (s ≥ 1, W⁻ ≠ Q′) and gives |W⁻| ≥ l−s, so mass(W⁻) ≤ 2p−l.
- So the last term has mass ≥ l but also ≤ D. Hence l ≤ D, so p+δ ≤ 2D ≤ 4δ−4, so p ≤ 3δ−4.
- This contradiction needs only **p ≥ 3δ−2**. ✓

**Step 8 (b_min not a sum of ≥ 2 terms of Q′).** MC on ({b_min}, W) is admissible, so A_W = b_min forces |W| ≤ 1.
- (8a) If t′ ≥ b_min, then g^{b_min} ⊆ Q′ has size b_min ≥ 3. Contradiction.
- (8b) Otherwise take Z·g^{b_min−A_Z}, with 1 ≤ b_min−A_Z ≤ t′ and size ≥ 2. Contradiction.
- (8c) Partial sums of Y_low start at 0 ≤ b_min−t′−1 (by 8a) and rise by at most t′ per term. So if A_{Y_low} ≥ b_min−t′, some partial sum lands in [b_min−t′, b_min−1], contradicting (8b).
- Hence |Y_low| ≤ (b_min−t′−1)/3, and this bound is ≥ 0. ✓

**Step 9 (counting).**
- From Step 7: A_Y = 2p−t′ and |Y| = l−t′.
- base = (3l−2p)/2 is an integer, because l = N−u is even.
- X = Σ_Y (c−3)/2 = t′ − base ≥ 0.
- base = (p+3δ−3D)/2 ≥ (p−3δ+6)/2 ≥ 3. For prime p this is in fact ≥ 4, since p ≥ 3δ+2.
- **t′ ≤ 2:** X ≤ −1 < 0, an immediate contradiction. The text's two-term argument also covers this case vacuously.
- **t′ ≥ 3:** two Y-terms above t′ would give X ≥ t′−2 > X.
- So |Y| ≤ |Y_low|+1, which gives 3l ≤ b_min+2t′+2 ≤ 3b_min.
- Then l ≤ b_min ≤ p−δ+1 < p−δ+2 ≤ l. Contradiction. ✓ The induction closes.

**Inputs used by the inductive step.** Only S1+ (through the induction) and the index-one theorem. There is no Davenport, no EGZ, and no use of S1(g) Steps 3–8, so the candidate's "No other input" is accurate.

**Consistency with accepted results.**
- The S1(g) range satisfies κ ≤ (2p−2)/3 (that is P1), which is inside ⌊2p/3⌋. The Lemma therefore subsumes S1(d) and S1(g) as statements and conflicts with neither.

### Hypothesis map: actual requirements

| Use | Condition actually needed | At κ = ⌊2p/3⌋+1, p ≡ 1 (mod 3) (p = 3δ−2) | At κ = ⌊2p/3⌋+1, p ≡ 2 (mod 3) (p = 3δ−4) |
|---|---|---|---|
| Step 2 | 3κ ≤ 2p+1 | holds (3κ = 2p+1) | proof lost (3κ = 2p+2 can equal N) |
| Step 4 | δ ≥ 3; p prime (divisors of 2p) | holds | holds |
| Step 7 | p ≥ 3δ−2 | holds | proof lost (l ≤ D is not contradictory) |
| Step 9 | 3δ ≤ p (base ≥ 3) | **fails** (base ≥ 2 only) | **fails** (base ≥ 1 only) |

The only binding use of 3δ ≤ p is Step 9.

### Sharp families: arithmetic

**F1 = g^{p+3}(3g)^{p−1}, all p ≥ 5.**
- Zero-sums are g^a(3g)^b with a+3b ∈ {0, 2p, 4p}.
- a+3b = 2p gives length 2p−2b, for ⌈(p−3)/3⌉ ≤ b ≤ ⌊2p/3⌋. The maximum proper length is 2⌊2p/3⌋+2. The only other nonempty zero-sum is the whole sequence, of length 2p+2.
- So (ZP_κ) holds exactly when κ ≥ ⌊2p/3⌋+1, and (S1_κ) fails exactly when κ ≤ p.
- The implication therefore fails for κ ∈ [⌊2p/3⌋+1, p] for every prime p. This extends the parent's six-prime enumeration by hand.

**F2 = g^{2p−1}(cg)³, p ≡ 1 (mod 3), c = (2p+1)/3 (odd).**
- a + cb ∈ {2p, 4p} with a ≤ 2p−1, b ≤ 3 has exactly the solutions (a, b) = ((4p−1)/3, 1), ((2p−2)/3, 2) and (2p−1, 3).
  - b = 0 would need a = 2p.
  - b = 2 with sum 4p would need a = (8p−2)/3 > 2p−1.
  - b = 3 with sum 2p would need a = −1.
- The lengths are (4p+2)/3, (2p+4)/3 and 2p+2, so the candidate's arithmetic is correct.
- (ZP) holds exactly for κ ≥ (2p+1)/3. (S1) fails only for κ ≤ p.

### Do the families fail ONLY the base ≥ 3 step? (remark only)

**p ≡ 1 (mod 3), κ = (2p+1)/3: yes, in the strong sense.**
- Steps 1–8 remain valid arguments for every Y at this κ, by the table above.
- F1: Q = g^{p+1}(3g)^{(p−1)/3}, Q′ = g²(3g)^{(2p−2)/3}, D = 2δ−2, m = (p+3δ)/2, t′ = 2, b_min = 3, base = 2, X = 0.
- F2: Q = g^{(4p−1)/3}(cg), Q′ = g^{c−1}(cg)², D = 2δ−2, t′ = c−1, b_min = c = p−δ+1, max Q′-coefficient = D+1, base = 2, X = c−3.
- Both meet every bound of Steps 1–8, several with equality. Both violate only "at most one term above t′".

**p ≡ 2 (mod 3), κ = (2p+2)/3: F1 only.**
- F1: Q = g^{p+2}(3g)^{(p−2)/3}, Q′ = g(3g)^{(2p−1)/3}, l = D, t′ = 1, base = 1.
- F1 meets the conclusions of Steps 1–8 and violates only base ≥ 3.
- However, the proofs of Steps 2 and 7 are also unavailable at this κ. So "fails only base ≥ 3" is true of the family but not of the argument in this residue class.

### (A) findings (all MINOR)

| # | Location | Issue | Smallest fix |
|---|---|---|---|
| A-m1 | §2 Step 4, "so ord(a) is not p … and not 2" | ord(a) = 1 is not excluded (trivial). | Add "nor 1 (every term would be 0, which is even)". |
| A-m2 | §2 Step 1, parenthetical "by (ZP_κ), have length ≥ 2p+2" | (ZP) is idle; minimality of N alone suffices. D ≥ 0 is only known after Step 3. | Write "contradicting the minimality of N". End Step 3 with "hence l ≤ u, D ≥ 0". |
| A-m3 | §3 first bullet (hypothesis map) | Overstates where p ≥ 3δ−1 binds: Step 2 needs only 3κ ≤ 2p+1, and Step 7 only p ≥ 3δ−2. As written ("3κ ≤ 2p") it is in tension with §3's own claim that the families pass Step 2 at 3κ = 2p+1. Primality (Step 4, S1+) is unlisted. | Replace with the table above: binding only in Step 9. |
| A-m4 | §0 Sharpness, F2 parenthetical "(S1) fails there"; F1 citation | (S1) fails only for κ ≤ p. F1's all-p claim rests only on the parent's six primes. | Write "(2p+1)/3 ≤ κ ≤ p". Add the one-line general F1 arithmetic above. |
| A-m5 | §3, "both families satisfy every step up to Step 8 and fail Step 9 exactly" and the p ≡ 2 line | Needs residue-class qualification. | Add the two-case statement above. |
| A-m6 | §2 Step 9, "two such terms would give X ≥ t′−2" | The t′ ≤ 2 case is handled only implicitly. | Add "if t′ ≤ 2 then X = t′−base < 0 already". |
| A-m7 | §1 first bullet (S1+) | The primary acceptance of S1+ is ZX/S1(c) Statement 2. Step 3 needs S1+ for sequences of arbitrary length. | Cite it and state the length-free form, with the justification given in Step 3 above. |
| A-m8 | §1 second bullet (index-one) | First load-bearing use at a composite modulus; within the recorded scope. | Add one sentence: "general C_n statement, n = 2p, length ≥ p+2; ord(a) = 2p derived from oddness". |
| A-m9 | §4 second bullet, "found F1 and F2 (and nothing else)" | The search space presupposes Steps 3–8, so it is neither an independent check nor a classification. | Add "not a premise; not a classification; circular with respect to Steps 3–8". |

---

## (B) Corollary: re-derivation of the substituted chain

Let w be an avoider of length 4p−2 with o = o_F and 3o ≤ 2p+1. κ̂ is an integer because F ≡ k (mod 2) (ZX overlay 1).

1. **Normal form and case split.** The accepted process outputs a normal form. Admissible forms have k ≤ o and k ≡ o (mod 2). The criterion is existential (overlay 2); the candidate's "every" is stronger and harmless.
   - k = 1 is handled by K1 (overlay 3).
   - For k ≥ 2, GRX gives κ̂ ≥ 0 and **DAV gives κ̂ ≤ k−1 ≤ o−1 ≤ ⌊(2p+1)/3⌋−1, so 3κ̂ ≤ 2p−2 ≤ 2p**. ✓
2. **(ZP) at κ̂.** (ZP) at κ̂ for ŵ's rotation sequence is supplied by the accepted framework. The ZX criterion's "κ̂ ≤ (p+1)/2 suffices" and the S1(g) chain both rely on exactly this.
   - The Lemma's hypotheses hold: integer 0 ≤ κ̂ ≤ ⌊2p/3⌋, odd elements of Z_{2p}, any length.
   - **The substitution is exact.** S1-sharp has the same "(ZP) ⇒ (S1)" form as S1(g)+, with a range that strictly contains it (P1 gives (p+δ*)/2 ≤ (2p−2)/3).
3. **ZX terminal criterion.** 3k ≤ 3o ≤ 2p+1, so the original rotations lie in one nonzero pair.
   - The criterion's internal uses (SHgen-E discharge o_F = k ≤ (2p+1)/3 ≤ p, and (K) with 5k ≤ 4p−1) depend only on 3k ≤ 2p+1 and are unchanged. ✓
4. **Restricted REFL.** o ≤ (2p+1)/3 ≤ p, so INV* follows. ✓
5. **(b) Deletion ledger and RGR-LONG.**
   - Case 1 needs o ≤ 2p−3, which follows from 3o ≤ 2p+1.
   - Case 2 gives (o−1, F−1). Case 3 gives (o or o−2, F).
   - o never increases, so 3o′ ≤ 2p+1 persists. Deleting a letter of an avoider gives an avoider, so (a) applies, and RGR-LONG closes. ✓
6. **The removed side alternative is genuinely unnecessary.**
   - In both accepted chains, its only role was to force κ̂ ≤ (p+δ*)/2 (low branch via o−1, high branch via κ̂ ≤ κ(w)).
   - Restricted REFL (o ≤ p), the ledger (o ≤ 2p−3, o non-increasing) and SHgen-E/(K) (3k ≤ 2p+1) never use it.
   - Item 1 now lands in the Lemma's range unconditionally. ✓

**Robustness observation.** The Corollary uses the Lemma only at 3κ̂ ≤ 2p−2, which means p ≥ 3δ+4 and base ≥ 5. Neither the Lemma's endpoint κ = (2p−1)/3 nor the tight Step 9 margin is ever used.

**Coverage effect.**
- Every residual pair in S1(g) Statement 4, with κ̂ ≤ k−1 ≤ ⌊(2p+1)/3⌋−1 ≤ ⌊2p/3⌋, is discharged.
- At p = 31, the pair (21, 20) has κ̂ = 20, δ = 9 and 3δ = 27 ≤ 31, so it is covered. ✓
- New coverage exists only at p ≥ 31. For p ≤ 29 the Corollary restates accepted coverage.

### (B) findings (all MINOR)

| # | Location | Issue | Smallest fix |
|---|---|---|---|
| B-m1 | §5, "Effect on the residual map (bundle-v5 Sec. 5)…" | (Q1a), (Q1b), (Q2) and T4 are undefined in the record set, so these claims are unverifiable here. They are not part of the Corollary. | Label as unreviewed context, or replace with "every terminal pair of S1(g) Statement 4 is discharged; in particular (21, 20) at p = 31". |
| B-m2 | §5(a), "DAV gives 0 ≤ κ̂" | κ̂ ≥ 0 comes from GRX (ZX overlay 3); DAV gives only the upper bound. | Fix the attribution. |
| B-m3 | §5(a), "— the rotation multiset of w —" | The records state the conclusion as "the original rotations lie in one nonzero pair". The identification of multisets is consistent with the records but not stated in them. | Cite the terminal conclusion verbatim. |
| B-m4 | §1 third bullet, "proof-ROT-ZX-v1.md L204-206" | Line references to an unembedded file cannot be checked. | Cite ZX verdict Statement 3 with overlays 1–4 and 8. |
| B-m5 | §5(a) first sentence | The criterion is existential. The k = 1 / k ≥ 2 split is inherited from the accepted chain. | Write "some (indeed every) admissible normal form; case split as in ZX overlay 3; no new k-case is introduced". |

---

## Probe status (explicit)

The lane probe (RECEIPT-run1-v1 and run1.jsonl) is **not a premise** of (A) or (B). Neither Steps 1–9 nor §5 cite it.
- F2's arithmetic is verified by hand above, so even the sharpness remark does not depend on the probe.
- The probe's search space is built from Steps 3–8, so it cannot independently check the Lemma.
- The disclosed PID deviation and the not-yet-run independent control do not affect acceptance. Acceptance rests on the written proof.

## Scope

This is a dihedral partial result only, relative to the stated imports:
- S1+.
- The Savchev–Chen/Yuan index-one theorem, author statement only.
- The accepted ZX/GRX/DAV/K1/REFL/ledger/RGR-LONG interfaces at their recorded scopes.

It is **not** unrestricted INV\*(p), not ordered Olson for D_{2p} in general, and not the all-groups target. It does not touch k > (2p+1)/3 or reflection rigidity for o_F > p. No novelty or priority assessment, no Lean, no hash verification.
