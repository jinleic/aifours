# Referee report: LS+ chain, Slice A (items 1–4), written proof only

## Verdict

**0 FATAL · 0 MAJOR · 16 MINOR.** All 16 are wording, explicitness or import-scope labels, and two of them are optional. I rechecked every load-bearing inequality at the stated ranges. No statement needs to change and no proof needs to be redesigned.

| # | Item / part | Verdict | Findings |
|---|---|---|---|
| **1** | **LS+-RED** | **ACCEPT-WITH-FIXES** | |
| 1.0 | §0 cut-down | ACCEPT | — |
| 1.1 | (A) §1: CT deficit, ≤ 2 heavy values, involution exclusion, one-heavy bound | ACCEPT | — |
| 1.2 | (A) §2 Step 1: case (β), unequal multiplicities, no-wrap ⇒ μ1 = 1, δ0 ≥ 3e−2 | ACCEPT | R-m1 (optional) |
| 1.3 | (A) §2 Step 2: split (i)–(iii), first crossings (iv)/(v), (vi) | ACCEPT | — |
| 1.4 | (B) §3 | ACCEPT-WITH-FIXES | R-m2, R-m3, R-m4 |
| 1.5 | §4 | Heuristic, not a claim | — |
| **2** | **Addendum 1 (a = −1)** | **ACCEPT-WITH-FIXES** | |
| 2.1 | Step 1, read only through the Editorial line | ACCEPT-WITH-FIXES | A1-m1 |
| 2.2–2.3 | Steps 2–3 | ACCEPT | A1-m2, A1-m4 |
| 2.4 | Step 4 | ACCEPT-WITH-FIXES | A1-m3 |
| 2.5 | "Remaining" | First sentence ACCEPT; the "lever" is not a claim | A1-m5 |
| **3** | **Addendum 2 (a = −1/2)** | **ACCEPT** | |
| 3.0–3.1 | §0 range and notation; §1 (F0)/(Fo)/(L*) | ACCEPT | A2-m2 (optional) |
| 3.2–3.3 | Lemma 0; Theorem LS+-RED-c Steps 1–4 | ACCEPT | — |
| 3.4 | Remark 4 (not load-bearing) | ACCEPT-WITH-FIXES | A2-m1 |
| 3.5 | §5 scope and retained list | ACCEPT | — |
| **4** | **LS+-lin** | **ACCEPT-WITH-FIXES** | |
| 4.1 | Upper bound and proof | ACCEPT | — |
| 4.2 | Sharpness of E2/E3 | ACCEPT-WITH-FIXES | L-m1 |
| 4.3 | Exceptional list, including BASE1 exclusions | ACCEPT | L-m2 |
| 4.4 | Relation to LS/STAB | ACCEPT-WITH-FIXES | L-m3, L-m4 |
| all | Stale status labels | — | G-m1 |

**Coverage.** All of this is at sequence level and relative to the imports below.
- **New result:** LS+(p,κ) holds for prime p, κ0+1 ≤ κ ≤ p−2, e ≥ 3 and p ≥ 10e−13.
  - For primes this is the same as p ≥ 10e−16, and the same as κ ≥ (9p−13)/10.
  - Together with the already accepted LS+2 (e = 2) and BASE1+, LS+ holds throughout the range except on LS+-lin's exceptional list.
- **Sharpness:** E2(κ) and E3(κ) attain 3κ+1 in every cell of the range. This follows from a direct CF(a) check (see 4.2).
- **Structural results** for e ≥ 3, p ≥ 9e−13:
  - LS+-RED (A) and (B).
  - Remark 4: in case a = −1/2, a long zero-sum forces E'' ≥ δ'+1.
- **Undecided:** e ≥ 3, prime p ≤ 10e−17, κ ≠ (2p+1)/3.
  - In the band 9e−13 ≤ p ≤ 10e−17, two subcases remain: a = −1, and a = −1/2 with E'' ≥ δ'+1.
  - Below p = 9e−13 this chain gives nothing.
- **Not concluded:** general LS+; STAB beyond the BASE1 cells; any new LS cell; TR; INV*; ordered Olson.

**Exact import closure.**
- **Item 1** uses:
  - CT with n = κ.
  - CTgen, involution clause only, at N = 3κ+2.
  - CF(a) read through E1, with respect to g = u in §2 and g in §3.
  - SLZ3, used only to cut Y down.
  - The index-one theorem at n = p, applied to a sequence of length |U'|+1 ≥ (p+3)/2.
  - The greedy step of LS+2 §3(C), with r := |U'|; its hypothesis S' ≤ p−1 < 2|U'| holds.
  - It does **not** use CF(b), ROW, DGM-p, AP, or any LS/LS+/STAB hypothesis.
- **Item 2** uses item 1, CF(a), CF(b) read through R4, and the greedy step (through 1(B)).
- **Item 3** uses item 1, CF(a) and CF(b) read through R4. It makes no direct use of the greedy step and does not use item 2.
- **Item 4:**
  - The upper bound uses LS+2 (for e = 2), SLZ3 and items 1–3.
  - Sharpness uses CF(a) only.
  - Two citations are bookkeeping only, not load-bearing, and lie outside this review's import whitelist: BASE1+ (delta verdict item 3) for the list exclusions, and LS-small/LS-lin (items 2 and 5) for the remark "no new LS cell".

**Non-claims.** Acceptance here is a correctness finding only. It implies nothing about novelty or priority. The index-one and greedy inputs are Savchev–Chen, and I did not assess classical routes. I did not review the DFS-probe line in item 4, and it is not a premise.

---

## Detailed checks

### 1. LS+-RED

**1.0 Cut-down.**
- T is a shortest zero-sum of length ≥ 2κ+2; under (ZP_κ) its length is ≥ 2p+2.
- SLZ3's range ⌊2p/3⌋+1 ≤ κ ≤ p−1 contains our κ, so |T| ≤ 3κ+1.
- Choose Y' with T ≤ Y' ≤ Y and |Y'| = 3κ+2. Y' inherits (ZP_κ) and still contains T.
- SLZ3 is used only to bound |T|, never |Y|. ✓

**1.1 §1 (part A).**
- **Deficit.** Apply CT with n = κ. Then |Y|−n = 2κ+2 is even and ≤ 2p.
  - CT gives Σ min(κ, v_x) ≤ 2p−e−2.
  - So the excess over κ is ≥ p−2e+4 ≥ e+5.
- **At most two heavy values.** Three heavy values would need 3κ ≤ 2p−e−2, i.e. p ≤ 2e−2. This contradicts p ≥ 3e+1.
- **Involution exclusion.** CTgen applies: κ ≥ (p−3)/2, N = 3κ+2 ≥ 2κ+3, and T is present.
  - It gives v_p ≤ κ, so every heavy value is an odd element ≠ p.
  - Every such element is a generator.
- **One heavy value.** v_g ≥ 2p−3e+4.
- **Two heavy values (case β).**
  - The remaining terms satisfy |R| ≤ e−2, and v_u+v_v ≥ 3p−4e+4.
  - Both ≥ p is impossible: u^p v^p would be a zero-sum of length 2p, since its C_p-sum is p(α+β) = 0.
  - Both ≤ p−1 is impossible: it gives p ≤ 4e−6.
  - Hence v_u ≥ p > v_v ≥ p−e+1, and v_u ≥ 2p−4e+5. ✓

**1.2 §2 Step 1.**
- v_u ≤ 2p−1, so δ0 ∈ [1, 4e−5].
- r ≤ p+e−3 gives |W|+2ρ ≤ p+3e−5 ≤ 2p, so (F*) holds.
- **Signed representatives.** Put t~_ρ = t_ρ ≤ δ0−1−2ρ when t_ρ ≤ v1; otherwise t~_ρ = t_ρ−p, which is ≥ −(e−2). So every t~_ρ lies in [−(e−2), 4e−8].
- **No-wrap.** D_ρ := t~_ρ + t~_1 − t~_{ρ+1} is ≡ 0 mod p and lies in [−(6e−12), 9e−18]. So D_ρ = 0, and t~_ρ = ρx~ for all ρ.
- **Sign of x~.**
  - x~ < 0 gives e−1 ≤ e−2, a contradiction.
  - x~ > 0 gives (e−1)(x~+2) ≤ 4e−6 < 4(e−1), so x~ = 1. Then μ1 = 1 (v = 3g) and δ0 ≥ 3e−2.
- **Consequences.** s ≥ (3p−3e+2) − (2p−3e+2) − (p−1) = 1, and v1 = p−3e+2+δ0−s. ✓

**1.3 §2 Step 2.**
- **Exhaustive split.** Each extra term has μ0 ∈ [2, p−1], since μ = 0 is g and μ = 1 is 3g, both used up.
  - If μ0 ≥ p+2−δ0: case (ii).
  - If μ0 ≤ p+1−δ0 and v1+μ0 ≥ p: case (i). Take W = 1^{p−μ0}{μ0}. Then ρ = 0 and |W| = p−μ0+1 ≥ δ0, contradicting (F*).
  - Otherwise: case (iii), with μ0 ≤ 3e−3−δ0+s ≤ s−1.
- **Case (ii).**
  - Take t = m+e−1 ≤ 5e−8 ≤ p−e+1 ≤ v1 (uses p ≥ 6e−9).
  - The sum is p+e−1, so ρ = e−1, and |W|+2(e−1) = m+3e−2.
  - (F*) then forces m ≤ δ0−3e+1.
- **Step (iv), first crossing of the positive terms.**
  - P_k ≤ 2(p−1−v1) ≤ 2s−2, and 1 ≤ p−P_k ≤ v1.
  - ρ = 0 and |W| ≥ p−2s+3 ≥ p−2e+7 ≥ δ0 (uses p ≥ 6e−12). Contradiction.
- **Step (v), first crossing of the negative terms.**
  - Each m+1 ≤ δ0−3e+2, so N_k ≤ 2e−6, and we need M_k+e−1 ≤ 3e−8 ≤ v1 copies of 1.
  - The sum is kp+e−1, and |W|+2(e−1) = N_k+3e−3 ≥ δ0. Contradiction.
- **Step (vi).**
  - (iv) gives δ0 ≤ 3e−3+s−P, and (v) gives δ0 ≥ N+3e−2.
  - So N+P ≤ s−1 < 2s ≤ N+P, a contradiction. This proves (A). ✓

**1.4 §3 (part B).**
- **(F*) and the core.**
  - r = p−3e+2+δ0 ≤ p−2, so (F*) holds.
  - Z0 may be empty. Since ρ(Z0) = 0, |Z0| ≤ δ0−1.
  - U' is zero-sum-free by maximality of Z0.
  - Applying (F*) to W' ∪ Z0 gives |W'|+2ρ(W') ≤ δ'−1 for W' ≤ U'.
- **Nonempty, minimal, index-one range.**
  - |U'| ≥ p−3e+3 ≥ 4, so σ(U') ≠ 0 and U'(−σ(U')) is minimal (R-m2).
  - Its length is ≥ p−3e+4 ≥ (p+3)/2, which holds iff p ≥ 6e−5.
- **Index one.**
  - The coefficients are ≥ 1 and sum to p, and the coefficient of −σ(U') is ≥ 1.
  - So S' ≤ p−1 and δ'+E' ≤ 3e−3.
- **All integer subset sums.** The greedy step needs S' < 2|U'|, which holds (R-m3).
- **Signed representatives s_ρ.**
  - If s_ρ ≤ S': some W' has x-sum s_ρ, σ(W') ≡ ρ and |W'| ≥ s_ρ−E'. So s_ρ ≤ 3e−4−2ρ.
  - Otherwise s~_ρ ∈ [−(3e−4), −1].
- **No-wrap.**
  - D_ρ := s~_ρ + s~_1 − s~_{ρ+1} lies in [−(9e−14), 9e−16]. The text calls these "consecutive differences" (R-m4).
  - p ≥ 9e−13 is exactly what is needed to get D_ρ = 0, so the range is used sharply here.
- **Conclusion.**
  - x~ > 0 is impossible, since it gives e−1 ≤ e−2.
  - x~ < 0 gives |x~| ≤ 2. So a = −1 with δ'+E' ≤ 2e−2, or a = −1/2 with δ'+E' ≤ e−1. ✓
- **Binding inequalities** (recorded, not adopted): (A) needs only p ≥ 9e−17; (B) needs p ≥ 9e−13.

### 2. Addendum 1

The garbled Step 1 display is not used anywhere. Only the Editorial line is used.

- **Setting.**
  - n1 ≥ |U'|−E' ≥ p−5e+6, using δ'−E' ≥ 2δ'−2e+2.
  - E' ≤ 2e−3.
- **Step 1.** Take ζ_z ≤ S' and ζ_z > n1.
  - Let W = {z} ∪ W'. W' exists by the subset-sum property in 1(B).
  - The signed sum is 0, and
    |W| ≥ 1+ζ_z−E' ≥ 2+n1−E' ≥ 2+(p−3e+3−E')−E' ≥ p−7e+11 ≥ 3e−4 ≥ δ0 (for p ≥ 10e−15).
  - This contradicts (F*). The two inputs, n1 ≥ p−3e+3−E' and E' ≤ 2e−3, are valid.
  - So ζ_z ≤ n1. Then W = {z}(−g)^{ζ_z} gives ζ_z ≤ δ0−2.
  - Negative terms satisfy z~ ∈ [−(3e−4), −1]. ✓
- **Step 2.**
  - T1 ≤ max(e−1, 2e−4). The file's bound 2e−3 is looser, which is harmless.
  - The first crossing is ≤ 5e−10. The number of copies needed, ζ~−(e−1), is in [0, 4e−9] ⊆ [0, n1].
  - The signed sum is e−1, and |W|+2(e−1) ≥ 1+(δ0−e)+(e−1) = δ0. Contradiction.
  - So the positive part is ≤ 2e−4. ✓
- **Step 3.**
  - At the first crossing, p+ζ~ ∈ [S'−3e+5, S'] ⊆ [0, S'], so W'' exists (A1-m4).
  - The signed sum is −p, and |W| ≥ |U'|−3e+6 = p−6e+8+δ' ≥ |Z0|+δ' = δ0 (for p ≥ 9e−13). Contradiction. ✓
- **Step 4.**
  - The reduction to "|W*|+2ρ(W*) ≥ 2p+δ0" follows from CF(b) read through R4, using |W*| ≤ p−2. The file does not write this out (A1-m3).
  - If σ~ ≥ 0: the bound is ≤ 7e−13 < 2p.
  - If σ~ ≤ −1:
    - Then |Z''|+ζ~ ≥ δ0+1 and ζ~ ≥ 2.
    - Take ρ0 = min(ζ~, e−1); this needs ≤ e−3 copies of −g.
    - Then |W|+2ρ0 > δ0, a contradiction.
  - So there is no zero-sum of length ≥ 2p+2. ✓
- **Binding:** Step 1 needs p ≥ 10e−15; Steps 2–4 need at most p ≥ 9e−13.

### 3. Addendum 2

- **Range equivalence.**
  - For e ≥ 3: 10e−16 and 10e−14 are even and > 2, and 10e−15 = 5(2e−3) with 2e−3 ≥ 3 is composite.
  - So for primes, p ≥ 10e−16 ⇔ p ≥ 10e−15 ⇔ p ≥ 10e−13. This fails only at e = 2, where 10e−15 = 5 is prime.
  - Also 10e−16 ≥ 9e−13, so item 1 applies.
- **§0 notation.**
  - ξ ≡ 1 ⇔ μ = (p−1)/2 ⇔ c = p, i.e. the involution. ✓
  - n_P ≥ p−4e+5 and A ≤ 2e−2−2δ'. ✓
- **§1, parity of t.**
  - t = 0 gives ρ = 0; t odd

 gives ρ = (p−t)/2; t even ≥ 2 gives ρ = p−t/2 ≥ (p+1)/2 > e−1.
  - So (F0) and (Fo) together are exactly (F*). ✓
- **(L*).** This follows from CF(b) read through R4, using |W| ≤ r ≤ p−2.
  - ρ = 0 is impossible: it forces j ≥ p and so |W| ≥ 2p+δ0.
  - t odd gives |W| ≥ p+t+δ0 > r, which is impossible.
  - t even gives t ≤ |W|−δ0, with j = t/2 and length 2p+t.
  - Both directions hold. ✓
- **Optional observation (A2-m2).** A ≥ 0 always. P^{p−2e+2} would have t = p−2e+2, which is odd, and |W|+p−t = p > δ0−1, violating (Fo). So the "A ≤ 0" branch is just A = 0. This is harmless.

**Lemma 0 (involution as unit).**
- **Choice of θ.**
  - If τ0 ≤ p−2e+2, take θ = p−2e+2. It lies in [τ0, τ0+n_P] exactly when τ0 ≥ A+1.
  - If τ0 ≥ p−2e+3, then τ0 or τ0+1 is an odd number ≤ p (if τ0 is even, τ0 ≤ p−1). So s ≤ 1 ≤ n_P.
- **Availability.** The s copies P^s come from U', which is disjoint from V ⊆ Z0.
- **Conclusion.**
  - θ = p gives t = 0, and (F0) applies.
  - θ ≤ p−2 gives t = θ odd and ≥ p−2e+2, and (Fo) applies.
  - Both give |V|+p−τ0 ≤ δ0−1. ✓

**Theorem LS+-RED-c.**
- **Step 1.** If ζ_z ≥ A+1, Lemma 0 gives ζ_z ≥ p+2−δ0, so ν_z ∈ [1, δ0−2]. ✓
- **Step 2 (positive control).**
  - At the first crossing, P_V ≤ 2A ≤ 4e−8 < p.
  - Lemma 0 gives P_V ≥ p+2−δ0 ≥ p−3e+6 > 4e−8 (uses p ≥ 7e−13). Contradiction. ✓
- **Step 3 (negative control, copies of the core ones).**
  - For V ∪ P^{N_V}, the ξ-sum is −N_V+N_V ≡ 0. So Ω_V ≤ δ0−1 whenever N_V ≤ n_P.
  - At the first crossing, Ω_V ≤ 2δ0−2, so N_V ≤ 2δ0−3 ≤ 6e−11 ≤ p−4e+5 ≤ n_P. Contradiction.
  - This is the only place p ≥ 10e−16 is used. ✓
- **Step 4 (every long-zero-sum inequality).**
  - **Upper bound on τ:** τ ≤ S'+max(A,0) ≤ p−3.
    - If A ≥ 1: S'+A = p−2e+1+Σ_{x≥2}x, and x ≤ 2(x−1) for x ≥ 2, with E' ≤ e−2.
    - If A ≤ 0: S' ≤ p−2e+1.
  - **Lower bound on τ:** τ ≥ −(δ0−2).
  - **τ ≥ 0:** t = τ ≥ |W|−Ω_{V−} ≥ |W|−δ0+1.
  - **τ < 0:** t = p+τ ≥ p−3e+6 > r−δ0 = p−3e+2 ≥ |W|−δ0.
  - So t(W) > |W|−δ0 for every W, whatever the parity of t, and (L*) fails. ✓

**Remark 4 (even involution deletion).**
- Suppose W satisfies (L*) with even t ≥ 2 and contains at least t involutions, from Z0 or from U'.
  - Deleting t of them lowers the ξ-sum by t, giving t = 0 and size |W|−t ≥ δ0. This contradicts (F0).
  - Equivalently, it leaves a zero-sum of length 2p.
- So W has at least |W|−t+1 ≥ δ0+1 terms that are not the involution.
- U has at most |Z0|+E'' such terms, because in U' a term is not the involution exactly when x_u ≥ 2.
- Hence E'' ≥ δ'+1. ✓
- This is valid for p ≥ 9e−13, because (F0) and (L*) use only r ≤ p−2 and (p+1)/2 > e−1 (A2-m1).
- Remark 4 is not used in §3. It only shapes the retained-case description in §5.

**§5 (retained list).** The prime bands 9e−13 ≤ p ≤ 10e−17 are:
- e = 3: [14, 13], empty.
- e = 4: {23}.
- e = 5: [32, 33], no primes.
- e = 6: {41, 43}.
- e = 7: {53}.
- e = 8: {59, 61}.

This matches the stated first instances. ✓

### 4. LS+-lin

**4.1 Upper bound.**
- **e = 2:** use LS+2. κ = p−2 lies in the range exactly when p ≥ 7.
- **e ≥ 3:**
  - Use the SLZ3 cut-down, which keeps the long zero-sum T.
  - Then item 1 applies, since p ≥ 10e−13 ≥ 9e−13.
  - That gives a = −1 or a = −1/2, which items 2 and 3 exclude.
- So the coverage is exactly {e = 2} ∪ {e ≥ 3, p ≥ 10e−13} inside κ0+1 ≤ κ ≤ p−2. There is no general LS+, STAB or ordered-Olson claim. ✓

**4.2 Sharpness of E2/E3 (L-m1).**
- **E2(κ) with respect to g = h:**
  - M = 2p−3e+2 ≤ 2p−1, δ0 = 3e−2, and U = 1^{p−1}.
  - For W = 1^w we have ρ = w. If ρ ≤ e−1, then |W|+2ρ = 3w ≤ 3e−3 < δ0, so (F) holds. ✓
- **E3(κ) with respect to g = 3h (p ≠ 3):**
  - M = 2p−1, δ0 = 1, and U = (μ*)^{p−3e+2} with 3μ* ≡ −1.
  - For W = (μ*)^t with 1 ≤ t ≤ p−3e+2, having ρ ≤ e−1 would need t ≡ −3ρ ∈ {0} ∪ [p−3e+3, p−3]. That is impossible.
  - Also |W|+2ρ ≤ p−e ≤ 2p, so (F) holds. ✓
- **Long zero-sums.**
  - The coefficient sums are 4p and 6p.
  - The required exponents exist because 3κ ≥ 2p+1.
  - Both E2(κ) and E3(κ) have length 3κ+1.
- This is correct for every κ in the range. However, the parent's acceptance of LS+2 (delta verdict item 4) covers attainment only at κ = p−2.

**4.3 Exceptional list.**
- **Equivalences.**
  - e ≤ ⌊(p−1)/3⌋ ⇔ κ ≥ ⌊2p/3⌋+1, since p ≠ 3.
  - For primes with e ≥ 3: p < 10e−13 ⇔ p ≤ 10e−17 ⇔ κ ≤ (9p−17)/10.
- **BASE1 cells.** A BASE1 cell with p ≥ 10e−13 would need p ≤ 7. So every BASE1 cell with e ≥ 3 lies in the would-be exceptional set, and it is correctly removed from the list.
- **Per-p check, p ≤ 31:**

| p | κ range | Covered (LS+2 / this chain) | BASE1 | Exceptional (file) |
|---|---|---|---|---|
| 11 | 8–9 | 9 | — | 8 ✓ |
| 13 | 9–11 | 11 | 9 | 10 ✓ |
| 17 | 12–15 | 15, 14 (17 ≥ 17) | — | 12, 13 ✓ |
| 19 | 13–17 | 17, 16 | 13 | 14, 15 ✓ |
| 23 | 16–21 | 21, 20 | — | 16–19 ✓ |
| 29 | 20–27 | 27, 26, 25 | — | 20–24 ✓ |
| 31 | 21–29 | 29, 28, 27 | 21 | 22–26 ✓ |

- p = 5 has an empty range, and p = 7 has only κ = 5 (covered). ✓
- "Top 30%": (p − 0.9p)/(p/3) → 3/10. ✓

**4.4 Relation to LS/STAB.**
- LS+ implies LS, since 3κ+1 ≤ p+2κ.
- Covered cells with e ≥ 3 lie in LS-lin's range, since 10e−13 ≥ 6e−10. Covered cells with e = 2 are LS-small/LS+2 cells, not LS-lin cells (L-m3).
- In the STAB sentence, the factual parts are correct:
  - E3 is the case a = −1/3 with respect to g = 3h.
  - E2 has two heavy values: v_h = 2p−3e+2 > κ and v_{3h} = p−1 > κ.
- The claim "(B) also allows a = 1, −1/3" is unproved (L-m4).

### 5. Retained subcases versus excluded cells

| (p, e) | κ | Band check | Status |
|---|---|---|---|
| (23, 4) | 19 | 9e−13 = 23 = 10e−17 | **Undecided** (on the exceptional list) |
| (41, 6) | 35 | 41 ∈ [41, 43] | Undecided |
| (43, 6) | 37 | 43 ∈ [41, 43]; BASE1 there is κ = 29 | Undecided |
| (53, 7) | 46 | 53 ∈ [50, 53] | Undecided |

- **What is proved in these cells:** only LS+-RED (A)/(B) and Remark 4.
- **What remains:** all of a = −1, and a = −1/2 with E'' ≥ δ'+1.
- These cells must not be counted as LS+ coverage.

The excluded cells, i.e. those removed from the exceptional list, fall into three groups:
- e = 2, decided by LS+2.
- e ≥ 3 with p ≥ 10e−13, decided by this chain. Examples: (17,14), (19,16), (29,25), (31,27), (37,32).
- BASE1 cells (13,9), (19,13), (31,21), decided by BASE1+, not by this chain.

Cells below the band (p < 9e−13) get no reduction at all from this chain. Examples: (11,8), (13,10), (17,12), (17,13), (19,14), (19,15), (23,16)–(23,18).

### 6. Minimal repairs (all MINOR)

1. **G-m1 (all four items).** Relabel CT, CTgen, LS+2 and BASE1+ as parent-accepted (delta verdict `ac8ead13…`, items 3, 4, 6, 7, at their stated scopes). Read CF through E1 and R4; R4 is used only in items 2 and 3.
2. **R-m1 (optional; §2 Step 1).** Define "t~_ρ := t_ρ if t_ρ ≤ v1, else t_ρ−p" and "D_ρ := t~_ρ + t~_1 − t~_{ρ+1}".
3. **R-m2 (§3).** Insert: "U' is nonempty (|U'| ≥ p−3e+3 ≥ 4) and zero-sum-free, so σ(U') ≠ 0. U'(−σ(U')) is minimal: a proper zero-sum omitting −σ(U') lies in U', and one containing it has a nonempty zero-sum complement in U'. The coefficient of −σ(U') is ≥ 1, so S' ≤ p−1."
4. **R-m3 (§3).** Write: "greedy step of LS+2 §3(C) with r := |U'|; its hypothesis S' ≤ p−1 < p+1 ≤ 2|U'| holds."
5. **R-m4 (§3).** Replace "consecutive differences of the lifted sequence" with "D_ρ := s~_ρ + s~_1 − s~_{ρ+1}, where s~_ρ := s_ρ if s_ρ ≤ S', and s_ρ−p otherwise."
6. **A1-m1 (Step 1).** Delete the garbled display. The Editorial chain governs; state its inputs n1 ≥ p−3e+3−E' and E' ≤ 2e−3.
7. **A1-m2 (Steps 2–4).** Replace "integer sum X" with "signed-representative sum X (an integer ≡ σ(W) mod p)", following the D-5 m5.4 template.
8. **A1-m3 (Step 4).** Add: "(CF(b) read through R4; |W*| ≤ p−2, so ρ = 0 would force j ≥ p; otherwise the least j is p−ρ)."
9. **A1-m4 (Step 3).** Add: "p+ζ~ ∈ [S'−3e+5, S'] ⊆ [0, S'], so W'' exists by LS+-RED (B)."
10. **A1-m5 ("Remaining").** Mark the "Expected lever … two patterns" passage as an unproved heuristic, superseded by addendum 2.
11. **A2-m1 (Remark 4).** Add: "The §0 t-notation and the §1 (F0) and (L*) hold verbatim for p ≥ 9e−13; n_P and A are not used."
12. **A2-m2 (optional; §0).** Note that A ≥ 0.
13. **L-m1 (sharpness).** Cite the sharpness as a direct CF(a) check (the LS+2 §4 computation at general κ), not as parent-accepted scope.
14. **L-m2 (exceptional list).** State that the BASE1 exclusions rest on BASE1+, not on this chain, and that "not covered" means undecided, not a counterexample.
15. **L-m3 (LS relation).** Write "e ≥ 3 cells lie in LS-lin's range; e = 2 cells are LS-small/LS+2 cells."
16. **L-m4 (STAB relation).** Label the "(B) also allows a = 1, −1/3" sentence [INFERENCE]. The DFS line stays a non-premise.
