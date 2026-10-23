# Hostile review: Theorem U and Corollary U (RUH3-ext read with R3; residual read with erratum 1)

**Counts: FATAL 0 · MAJOR 0 · MINOR 4.** Every load-bearing step I re-derived by hand from the pasted text checked out. None of the four findings changes a theorem.

**Abbreviations:** R3 = proof-RUH3-v1; X = proof-RUH3-ext-v1; Res = residual-RUH3-v1; Err = erratum-1-residual-RUH3-v1.

## Claim-wise verdicts

| Claim (source) | Verdict and the checks behind it |
|---|---|
| **Word form and admissible lengths** (R3 LF33–43; X LF28–29) | **Correct.** All blocks are odd, so δ_GRX = N−Φ and C_max = Φ+2e−2. This holds for every placement of the e−1 extra pairs. With m ≤ e, every j lies in [m, m+e−1], so j ≤ 2e−1 ≤ p−2, and 2e+1−p ≤ 0. Signs: Σ_{z_i=+1} θ_i = Σ_{i∈P} τ_i because Σθ_i = 0. This matches the M2 group-law convention. |
| **Lemmas M, P, U, the window (W), A′ ≤ κ, A ≤ 2p−1** (R3 LF47–61; X LF30) | **Correct for e ≤ (p−1)/2.** Lemma P: n = max(p−1, 2κ+2−2m) corresponds to j = min((p+1)/2, m+e−1), and 2(p−1) ≤ R. Lemma U: 2(2κ+1)−R = p−2e+3 > 0. A ≤ 2p−1 uses R−2p = p−1−2e ≥ 0. Window gap: Λ−λ = p−2e+3+δ. |
| **MW** (R3 LF65–70) | **Correct.** RS(b) is applied with K = w0 to nonzero ω. The K_j are distinct because \|j−j′\| < e < p. Cauchy–Davenport gives min(p, w0+q). |
| **Lemma L\*** (X LF14–15, 38–46) | **Correct.** Case A: m ≤ k″ ≤ ⌊(p+2−e)/2⌋ ≤ ⌊(p+1−g)/2⌋, which holds iff g ≤ e−1. Case B, second branch: needs ⌊(p+1+g)/2⌋ ≥ e+⌈g/2⌉. At p = 2e+1 with g odd this is an equality and q = g+1 exactly, so the bound is tight but valid. The lemma never uses h, so Lemma H is not circular. |
| **Lemma H** (X LF16, 50–58) | **Correct.** k ≤ k″ because 2k ≤ e+2 ≤ p+2−e, and 2k−1 ≥ e, so low sets with m = k have d ≤ c−e. If P is high, P^c is low because d(P^c) = A−A′−d(P) ≤ c−1; hence d(P) ≥ Λ+e−1. The gap is p+1+δ. The toggle path keeps m = k (N = p+1 ≥ 2k+2). A removal step would need β_x ≥ p+1+δ > κ ≥ A′, which is impossible. Light sets: the contradiction is 0 ≥ 3+2δ. Counts: E+\|Q\| ≥ c+1 and E ≥ 2. |
| **Lemma S** (R3 LF102–110) | **Correct.** Y consists of empty runs, so no letter changes sign, and n/2 ≡ −j (mod p). The free and (N1) bounds on \|J\| are as stated. |
| **Lemma E\*** (X LF17–18, 62–77, with R3 LF112–158) | **Correct for 5 ≤ e ≤ (p+1)/2 and e ≤ c ≤ 2e−1.** Admissible and free on m(Y) ≤ M0, since M0+e−1 ≤ 3e/2 ≤ (p+1+c)/2; also e−μ ≤ M0. Additivity defect D: Case I gives D ∈ [−c, 2e−2], Case II gives D ∈ [1−2e, 2e−1] (using 2e ≤ p−1), so D = 0. The k6 argument fails as required (2k6 ≤ μ is impossible). (I.7) uses e−μ ≤ M0. C_E ≤ m(Y+)+m(Y−). All three Case I subcases give E+C_E ≤ e+ε−1. Case II gives C_E ≤ M0−1 and E+C_E ≤ e. See MINOR-1. |
| **Lemma POS\*** (X LF19, 81–91, with R3 LF162–188) | **Correct.** I re-derived the identity 2m(P)−1 = E−1+(2r_Q−o_end)+o_FF+o_in. Branches α/β/γ are exhaustive. (α): \|Q\| ≤ c−e+m(Q)−k″ and m(Q)−1 ≤ C_E+\|X\| give c+k″ ≤ p−2+ε, against c ≥ 2e (if k″ = e) or c+k″ ≥ e+2k″ ≥ p+1. (β): \|Q\| ≤ c−e < c+2−e. (γ): uses L\* only at m(P) ≤ k″ and at m(P′) = E/2+1 ≤ ⌊(e+1)/2⌋ < k″ (from 2k″ ≥ e+2, X LF46). In (iii-a), c_(l−1) has the right parity to be outside I, for odd end clusters and for even inner clusters. (iii-b): c+1 ≤ 3E/2, contradiction. |
| **Theorem A\*** (X LF97–99, with R3 LF194–205) | **Correct.** k0 = ⌊(c+1)/2⌋+1 ≤ k ≤ k″. The independence-number squeeze forces c odd, \|S\| = c+1, all paths even, and Q = ∅. j = e is admissible (m(Y) ≤ c+1 ≤ e) and free (2κ ≥ b iff p+1+c ≥ 2e). RS(b) with K = c+1 on the nonzero t_i gives \|M\| ≥ c+1, contradiction. |
| **THEOREM U** (X LF20–21, 92–93) | **Correct**: for every prime p, every 5 ≤ e ≤ (p−1)/2 and every 3 ≤ c ≤ 2e−1, under the full antecedent exactly as stated. Its only load-bearing imports are NF, GRX (if direction), RS(b) and Cauchy–Davenport, each at literal scope. No dependency is unresolved. |
| **COROLLARY U** (X LF22–23, 100–102) | **Correct, conditional on the accepted UH-A** (UH verdict LF9 and LF15, errata v1–v3) at its literal scope. κ ∈ [(p+1)/2, p−5] is equivalent to e ∈ [5, (p−1)/2], and this lies inside UH-A's range (p−1)/2 ≤ κ ≤ p−3, p ≥ 7. UH-A's 2κ+3 ≤ A ≤ 2p−1 is equivalent to 3 ≤ c ≤ 2e−1. The statement covers terminal k = p+1 and "some admissible NF" only. It is not a whole-κ or multiset-only statement. See MINOR-3. |
| **Residual with Err** (Res LF9–44; Err LF6–29) | **Accurate; does not overstate.** Err E1 checked: at e = (p+1)/2, k″ = ⌊(e+1)/2⌋, so 2k″−1 = e−1 for even e and k‴ is needed. Its route arithmetic, e+2k‴ ≥ p+2, checks. Err E2 checked: j ≤ e+g/2 ≤ p, since g ≤ c+A′ = p−1−δ. Lemma E\* does hold at e = (p+1)/2: Case I uses no h, and Case II is void there. R1b and MC1b are route statements only. See MINOR-4. |

R3-only SH machinery is not load-bearing for Theorem U (X LF31–34). This covers (MWe), the m = e path, Lemma L, POS(i), the original (I.5)–(I.7) bounds, Theorem R2 and Corollary SH. I spot-checked these and found nothing, but I have not adjudicated them here.

## Findings (all MINOR)

**MINOR-1: Lemma E\* Case II silently uses E ≥ 2.**
- *Step:* R3 LF151 writes "(E>=2)", and X LF62/72–73 imports it. X LF109 claims Lemma E\*'s proof "does not use h", but E ≥ 2 comes from the counts (R3 LF86 / X LF56), which depend on h. Also, (II.3)'s "e+1 ≤ R′" presumes E ≥ 1.
- *Consequence:* none for Theorem U. Lemma H supplies E ≥ 2 when e ≤ (p−1)/2. Case II is void at e = (p+1)/2. And E ≤ 1 satisfies both conclusions trivially (E+C_E ≤ 2 ≤ e). Still, LF109 is literally true only for Case I.
- *Repair:* open Case II with "if E ≤ 1 both conclusions are immediate". Restrict the LF109 remark to Case I.

**MINOR-2: unstated one-liners.**
- *Step:* X LF51 asserts "P high ⇒ P^c low" without the line d(P^c) = A−A′−d(P) ≤ c−1. X LF19 states POS\* as "Lemmas H and E\* contradictory", but the proof also uses Lemma L\* and the counts.
- *Consequence:* none.
- *Repair:* insert the line, and state POS\* as "H (with counts), L\* and E\* are jointly contradictory".

**MINOR-3: implicit interface in Corollary U.**
- *Step:* X LF100–101 treats UH-A's class {a,−a} as the same as Lemma U's without saying why. They do coincide. Any class carrying a dominant signed value has at least 2κ+1 letters, and R < 4κ+2 (R3 LF53–54) allows only one such class. A, A′ and c are rotation-multiset data, identical for w and u.
- *Package wording:* package LF22 says "cells … empty", which drops "terminal k = p+1, some admissible NF".
- *Consequence:* none if read at X LF22–23 literally. Downstream readers must not quote "cell empty" as a whole-κ result.
- *Repair:* add one sentence on the identification, and restore the qualifier in the package.

**MINOR-4: wording in Res LF33–34 (G3).**
- *Step:* at e = (p+1)/2, A′ = R−A−δ = p−1−c−δ is an identity, not a bound. So the compatibility condition is (p+1−c)/2 ≤ p−1−c−δ, i.e. c+2δ ≤ p−3. The stated conclusion is correct.
- *Consequence:* none; this is route text.
- *Repair:* replace "≤" with "=".

## Requested checks

- **Odd/even critical windows.**
  - Lemma L\* is tight at p = 2e+1 with g odd, and still valid.
  - At p = 2e−1 the same inequality fails for odd g. This is exactly the excluded cell (X LF106–108; Res G1), so the exclusion is consistent.
  - Parity of e: 2k−1 ∈ {e, e+1} and 2M0 ∈ {e+1, e+2}.
  - Parity of c: the (N1) length is used only for odd c ≤ 2e−3, at j = e−μ−1 ∈ [1, e−1], and n = A+1 ≤ R because b ≥ 1.
  - Parity of E: in POS\*(iii), E is even because 2m(P) = E.
- **Arbitrary H placement.** Only the parities of the l_i enter, through C_max = Φ+2e−2. Nothing else depends on the block lengths.
- **Empty runs.** The only property used is τ_i ≠ 0 at empty runs, which gives t_i ≠ 0, θ_i ≠ 0 and the nonzero terms RS(b) needs in A\*(3). Run h is never empty (α_h ≥ p+1). Clusters on the path with h deleted are the same as the cyclic clusters.
- **Quantifiers and full-word antecedent.** Every step concerns one arbitrary admissible NF u. By NF/PM\*, u is an avoider with the same length and the same rotation multiset as w. The conclusion is therefore universal over all such u. No o_F, run or pair hypothesis is introduced.
- **Endpoints.**
  - p = 11, e = 5: k″ = 4, k = 3, N = 12. Example window: g = 3, m = 3 gives j ∈ [4, 7], so q = 4 = g+1.
  - p = 13, e = 5: k″ = e.
  - e = (p−1)/2: tight but valid (as above).
  - c = e: branch (α) would need 1 ≤ k″ ≤ c−e = 0, so it is immediately impossible.
  - c = 2e−1: this is Case II, with E+C_E ≤ e.
  - κ = (p−1)/2 is not claimed.
- **Imports at literal scope.**
  - RS(b) is always used with an integer K ≥ 0 and nonzero terms: K = p−1 (Lemma P), K = w0 (MW), K = b (Lemma S), K = c+1 (Theorem A\*).
  - Cauchy–Davenport is used only in MW.
  - UH-A is used only in Corollary U.
  - None of RUH2, KP3, KP4, R7 or UH-L/E/SH/MW/PH is a premise.

## Correctness versus other axes

- **Correctness:** as tabulated above.
- **Completeness:**
  - Corollary U covers exactly (p+1)/2 ≤ κ ≤ p−5.
  - κ = (p−1)/2 (residual R1b) remains open.
  - Not claimed: κ = p−3, κ = p−4, p = 7, UH-EXCL, and full Olson.
- **Process:** I cannot verify timestamps, freeze order, hashes or line ranges from here (the parent checked these), and nothing in this review relies on them.
- **Priority:** the packet claims no novelty or priority, and this review asserts none.
- **Computation:** the packet uses none. This review used only hand algebra on the pasted text, with no enumeration.

Not approved: the whole research target, UH-EXCL, or runtime.
