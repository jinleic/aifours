# Hostile audit of SOURCE00: Lemma ZS, ROT-HALF, INV*-HALF, OLSON-HALF and the method obstruction

**Basis.** This is a written derivation only. Nothing was computed, and the finite aid at SOURCE00:164-166 played no part. Imports are taken as accepted statements. Their supplied proofs were read only to check hypotheses and that they do not depend on the range of k.

## Dispositions

| Item | Disposition | FATAL/MAJOR/MINOR |
|---|---|---|
| Lemma ZS (SOURCE00:29-102) | **ACCEPT** | 0/0/2, wording only, optional |
| ROT-HALF (SOURCE00:119-136) | **ACCEPT-WITH-FIXES** | 0/0/3 |
| INV*-HALF (SOURCE00:140-144) | **ACCEPT** | 0/0/0 |
| OLSON-HALF (SOURCE00:146-153) | **ACCEPT-WITH-FIXES** | 0/0/1 |
| Method obstruction (SOURCE00:109-115, 162) | **ACCEPT-WITH-FIXES** | 0/0/2 |

There is no FATAL or MAJOR finding.

**No step uses (F) 5k ≤ 2p+4.**
- ZS needs only k ≤ (p+1)/2.
- MULT needs only 3e+2 ≤ 2p (SOURCE01:68).
- The parts that carry (F) are never invoked: EXTRACT, WT, ROT-FEW Steps 1-5 and Theorem ROT-FEW-E (SOURCE01:162-164).

## 1. Lemma ZS: all nine steps re-derived

**Step 1** (:39-44): every zero-sum has length ≤ 2κ. ✓
- Removing one term from a minimal zero-sum leaves a zero-sum-free sequence, so its length is ≤ D = 2p.
- Odd terms force even length ≥ 2, so (ZP) gives length ≤ 2κ.
- At κ = 0 no minimal zero-sum exists, so Y is zero-sum-free. The text leaves this implicit, but it is correct.
- In the greedy prefix, the part before T_j has even length ≤ 2κ. So 2κ+2 ≤ |T_1⋯T_j| ≤ 4κ ≤ 4k−4 ≤ 2p−2.

**Step 2** (:46-49): splitting. ✓
- Later steps use only "Y′ is zero-sum-free".
- That holds for any inclusion-maximal zero-sum Z, and maximal length implies inclusion-maximal.
- No later step compares |Z| with other zero-sums, so the non-unique choice of Z is harmless.
- e = k−1−2κ+|Z| lies in [0, k−1].

**Step 3 and Lemma COMP** (:51-62). ✓
- Y′ is a zero-sum-free odd sequence and 3e+2 ≤ 3k−1 ≤ 2p. These are exactly MULT's hypotheses (SOURCE01:63-68).
- m ≥ 2 excludes g = (1,0) (SOURCE01:74).
- W′ = m+Σd_j = L+e′, by the interval structure (SOURCE01:74-80).
- COMP(a): d_j ≤ e′+1 ≤ e+1 ≤ m ≤ M+1, so the weight intervals extend at every stage. Integer-weight completeness holds.
- COMP(b): a subsequence of weight 2p would be a nonempty zero-sum. COMP(c) is exact.
- (C1): d_j ≤ k ≤ p−2 for p ≥ 5, so b(d_j g) = d_j and (1,0) is not in Y′.
- (C4) holds because 3k ≤ 2p+2.

**Step 4** (:64-68). U ⊆ Z and Q ⊆ Y′ are disjoint, (s(U)+τ(U))g = 0, and Step 1 bounds |UQ|. ✓

**Step 5** (:70-76): the new step. ✓
- s(Z) ≡ 0 mod 2p because g has order 2p. So τ(U^c) = 2p−τ(U), which also lies in [k, 2p−k].
- Both values are ≤ 2p−k ≤ L ≤ W′.
- Step 4 is applied **separately** to U and to U^c. That gives two distinct zero-sums UQ and U^cQ′, each bounded by Step 1. Q and Q′ may overlap; no simultaneous completion is needed.
- Adding: |Z|+2p−2e′ ≤ 4κ. With e′ ≤ e this gives 2p−2k+2 ≤ |Z| ≤ 2κ ≤ 2k−2, i.e. 4k ≥ 2p+4, a contradiction.

**Step 6** (:78-84). ✓
- Taking U to be a single term gives |b| ≤ k−1 on Z. This excludes from Z the only odd element of order 2, (1,0), which has b = p.
- Greedy partial sums land in [k, 2k−2] ⊆ [k, p−1]. They are their own representatives, contradicting Step 5.
- |s(Z)| ≤ k−1 < 2p forces σ₊ = σ₋.

**Step 7** (:86-90). ✓
- A subsequence Q of weight 2p−σ would make Z₊Q a zero-sum.
- Using |Z₋| ≤ σ (every |b| ≥ 1) gives 2p+1 ≤ 2σ+k ≤ 3k−2. This is impossible since 3k ≤ (3p+3)/2.
- The step is equivalent to e′ ≤ e−σ.

**Step 8** (:92-94). τ(Z₋) = σ ≤ k−1 ≤ m, so Z₋g^σ is a zero-sum. ✓

**Step 9** (:96-102). ✓
- cost = e′ + (σ−|Z₊|) + σ ≤ (e−σ) + 2σ − |Z₊| = k−1−2κ+|Z₋|+σ ≤ k−1.
- The sign-sensitive surcharge (negative terms pay |b|) appears only in the Z₋ term. Step 8 absorbs it exactly, because it bounds |Z₋| and σ together.
- cost = E+N term by term.

**Endpoints.**
- k = 1: κ = 0, Y is zero-sum-free of length 2p−1, e = 0, Y = g^{2p−1}, cost 0.
- κ = 0: Z = ∅ and cost = e′ ≤ k−1.
- k = (p+1)/2, including p = 5, k = 3:
  - 4κ ≤ 2p−2.
  - (3p+1)/2 ≤ 2p.
  - k ≤ p−2, with equality at p = 5.
  - Step 5 gives p+1 ≤ |Z| ≤ p−1, a contradiction.
  - Step 6 has S_j ≤ p−1.
  - Step 7 has (3p−1)/2 < 2p+1.
- Remark (1) (:104-105) is verified: the zero-sums of g^{2p−1}(−g)^κ are exactly g^a(−g)^a.

**Findings**
- **MINOR Z1**, SOURCE00:4-6. The text calls this a "complete in-file proof" that "replaces … MULT", but ZS still imports MULT (i)-(iii) and (D) (:51-53). Repair: "complete modulo MULT and (D)".
- **MINOR Z2**, SOURCE00:41 and :46, optional. Add "for κ = 0, Y is zero-sum-free and Z = ∅", and note that an inclusion-maximal Z suffices.

## 2. ROT-HALF

**Checked**
- **Normal form** (SOURCE03:30-43).
  - The o used there is o_F(w).
  - PM* (original-to-reduced direction, SOURCE09:8) and the equal-value re-reading preserve length, avoidance and the rotation multiset.
  - The result has k ≤ o_F, all blocks odd, and empty runs only between blocks of different values.
  - The one-even-block ending is ruled out by K1 (SOURCE03:39-41; SOURCE09:32).
  - k = 1 is handled by K1, with c ≠ 0. For k ≥ 2, R ≥ 2p−k > 0.
- **Bookkeeping.**
  - R = 2p+2κ−k.
  - DAV, with the frame in a boundary gap and F ≥ k ≥ 2, gives κ ≤ k−1.
  - The GRX all-plus pattern (Φ = 0, T = 0) is exactly ZS's (ZP).
- **Identification of g with c.**
  - g is a generator, so g = Y(c) with c ≠ 0, and bY(c) = (1, bc).
  - Since |b| ≤ k ≤ p−2, b is the unique odd integer in [−(p−2), p−2] with x ≡ bc. So the SHgen weight is b_x = b(Y(x)) (SOURCE02:39-41).
  - x = 0 is impossible, since 0 < |b| < p.
  - Lights are exactly the terms with b = ±1, and E_SHgen = E_ZS.
- **(H):** 2H ≥ 2p−2k ≥ k−1 ≥ E, which needs 3k ≤ 2p+1.
- **(K):** η ≤ E/2 ≤ (k−1)/2 and a_max ≤ E+1 ≤ k. Then 2p−η−a_max−1 ≥ k reduces to 5k ≤ 4p−1. ✓
- **Empty runs.** SHgen-E's hypotheses (SOURCE03:47-48) hold.
  - Expansions keep k, the block values and the empty runs (SOURCE03:52-59).
  - Each base word u°(h) has length 4p−2, rotations in {ρ_c, ρ_−c}, and o_F = k ≤ (p+1)/2 ≤ p (SOURCE03:69). So conditions (0), (a), (b), (d) of SOURCE04:117-121 hold.
  - The caller obligations (SOURCE04:135-137; SOURCE08:16) are met because k never changes during the induction.
- **No circularity.** No full ROT, full INV* or unrestricted REFL is used, and REFL-few-odd uses no rotation-rigidity result (SOURCE04:74).

**Findings**
- **MINOR R1**, SOURCE00:124. κ ≥ 0 is asserted without reason, and ZS needs it. Repair: cite SOURCE02:37 (if H ≥ p, the all-plus pattern with m = 0 is admissible). That argument is valid with empty runs, because GRX is accepted for any representation (SOURCE09:7).
- **MINOR R2**, SOURCE00:13-14 and :133-135. The normal form (Sec. 0) and SHgen-E were accepted inside chains whose calls had 5k ≤ 2p+4 (SOURCE07:12).
  - Their supplied proofs (SOURCE03:30-43, 49-70) use no (F): only (H), (K) and REFL at o_F ≤ k. So the call at k ≤ (p+1)/2 is applicable.
  - DAV's source file carries the pin caveat at SOURCE11:34.
  - Repair: state that these are imported as lemma statements valid for any k, list both caller obligations as discharged, and have the parent verdict record this.
- **MINOR R3**, SOURCE00:126-128. The identification uses |b| ≤ p−2 one sentence before that bound is stated. Repair: reorder, and add the reason x ≠ 0.

## 3. INV*-HALF

Conditions (0), (a), (b), (d) of SOURCE04:117-121 hold for w itself. The rotation pair comes from ROT-HALF, not from any INV* hypothesis, and o_F(w) ≤ (p+1)/2 ≤ p. ✓ No findings.

## 4. OLSON-HALF

I re-ran SOURCE05:28-47 with B = (p+1)/2.

- **Case 1** (R ≤ 2). ✓
  - (F−o_F)/2 ≥ (4p−3−B)/2 ≥ p holds because B ≤ 2p−3.
  - The frame starts at a rotation (R ≥ 1) or at a value change (R = 0), so no block wraps.
  - The p disjoint adjacent pairs σ_yσ_y are consecutive within the selection, so its product is 1.
  - A cyclic shift w = uv → vu gives P_uP_v = P_u(P_vP_u)P_u⁻¹. So the selection is also an identity in the original increasing index order.
- **Case 2** (an odd block of length ≥ 3). The shortened block stays nonempty and becomes even, nothing fuses, and o_F(w′) = o_F−1 ≤ B. ✓
- **Case 3** (R ≥ 3). ✓
  - If a deleted rotation's run becomes empty, there are at least two rotation runs, so its two neighbours are distinct reflection runs.
  - The fusion parities give o_F(w_i) ∈ {o_F, o_F−2}.
  - A third rotation lies in both deletions and fixes the pair. x₁ lies in w₂ and x₂ in w₁, so every rotation is covered.
  - Adjacent unequal reflections stay adjacent after deleting a rotation.
  - RGR-LONG(p) (SOURCE10:7) then gives the contradiction.

**Finding**
- **MINOR O1**, SOURCE00:20-21 and :152. The cited deletion ledger (proof-FEW-p5-lift-v3 §4.1) is not in the packet. Repair: cite SOURCE05:37-46 and SOURCE11:27; their content is re-derived above.

## 5. Method obstruction

**The counterexample is verified for every prime p ≥ 5.**
- Take Y = g^{2p−1}(3g)^{p−1}, k = p, κ = p−1, R = 3p−2.
- The (ZP) window is {2p}. Any g^a(3g)^b with a+b = 2p sums to 2bg. That is zero only for b ∈ {0, p}, and neither is available.
- Let h be any odd generator, with g = βh. β ≠ p because g is a generator.
  - If β ≠ 1, each copy of g costs at least 1, so the total is at least 2p−1.
  - If β = 1, then b(3g) = 3 (since 3 ≤ p−2), so the total is 2(p−1).
  - Both exceed p−1.
- The example also saturates (V): R+H = 3p−2 with H = 0.
- SHgen's (H) fails for every c (2H = 0 < E). So the whole cost-bound-plus-SHgen route fails at this configuration, not just ZS.

**What it refutes.**
- It refutes only ZS extended to (k, κ) = (p, p−1). It is a multiset in Z_2p, and no word is claimed.
- Suppose a length-(4p−2) avoider realized it (normal form: p singleton blocks, rotations ρ_c^{2p−1}ρ_{3c}^{p−1}). That word would contradict ROT(p)/INV*(p) at o_F = p.
- It would still not contradict ordered Olson at length 4p−1, because ordered Olson does not imply INV*.
- Whether such an avoider exists is neither claimed nor decided.
- The patterns with all signs + or all signs − are the only ones with Φ = 0, so the remark's "a proof must use Φ ≥ 2" is exact.

**Findings**
- **MINOR M1**, SOURCE00:114. "For k near p" overstates: only k = p is shown, and :115 itself leaves (p+3)/2 ≤ k ≤ p−1 open. Repair: "at k = p".
- **MINOR M2**, SOURCE00:162 and :109-110.
  - "(ZP)-only" should read "(ZP)+(V) on the rotation multiset", since the example satisfies both.
  - "Exactly when" at :110 describes where this proof's inequalities break, not where ZS fails. Step 1's condition is on κ, with worst case κ = k−1.

## 6. Ranges (Sec. 5)

- The arithmetic at :157-160 checks out:
  - (p+1)/2 gives 6, 7, 9, 10, 12, 15.
  - (2p+4)/5 gives 5, 6, 7, 8, 10, 12.
  - The old range is contained in the new one for p ≥ 3.
  - Nothing is new at p = 5 or 7.
- The combination with o_F ≤ 4 is a union only (SOURCE11:12). At p = 5 that piece rests on the computer-assisted C5 result (SOURCE11:5), which is not a premise of the new results.
- **MINOR S1**, :160-161. KAPPA01 is not parent-accepted (SOURCE07:18); label it as such.

## Audited / imported boundary

**Audited here**
- ZS Steps 1-9 and Lemma COMP.
- Remarks (1) and (3).
- ROT-HALF bookkeeping, the weight identification, (H)/(K), and every call condition.
- The INV*-HALF interface conditions.
- OLSON-HALF Cases 1-3, including the ordered cyclic products.
- The Sec. 5 arithmetic.

**Imported, applicability checked only**
- (D).
- MULT (i)-(iii): hypotheses checked; SCHERK, GROW and SET not re-derived.
- GRX, PM* and K1 (SOURCE09).
- DAV: its proof is not in the packet.
- The normal form and SHgen-E: proofs read only to confirm they do not depend on (F).
- Theorem SHgen: not re-audited.
- REFL-few-odd: accepted text is r4 (SOURCE08:6); the packet's r5 statement at SOURCE04:25-29 matches it.
- RGR-LONG(p).
- The OLSON-FEW proof.

**Not established**
- ZS for (p+3)/2 ≤ k ≤ p−1.
- ROT, INV* or ordered Olson for o_F > max(4, (p+1)/2).
