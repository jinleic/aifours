# KP2-EXCL v1: independent hostile review of the corrected snapshot

**Text reviewed.** The proof `8be43069…b002`, lines 1–256, with parent erratum v1 `4a6128d0…a7` applied last:
- MAJOR1 replaces lines 36–37.
- MINOR2 replaces lines 226–229.

This review is written mathematics only. I used no tools, ran no hash checks and did no computation.

## Verdict

- **Theorem KP2-EXCL** (p ≥ 7 prime): **ACCEPT**.
- **Theorem KP2-EXCL′**: **ACCEPT**.
- **Theorem EXCL-PM2**, with the pair hypothesis as an explicit antecedent: **ACCEPT**. The claim "only input GRX" is true. §4 logically subsumes it, so its value is as an independent route that uses GRX only.
- **Packet**: **ACCEPT-WITH-FIXES**.
  - FATAL: 0.
  - MAJOR: 0 open. The one MAJOR in raw v1 (lines 36–37) is correctly disposed of by erratum MAJOR1.
  - MINOR: 6. None affects validity.

## Per-claim verdicts

### §2: shape and selection rule

1. **§2.1 reduction (lines 61–64): ACCEPT.**
   - H^ = Σ(l_i−1)/2 = 1 with every l_i odd forces exactly one l_t = 3.
   - Hence F = p+3 and R = 3p−5 = 2p+2κ^−k.
   - w^ is an avoider by NF. This uses only NF's accepted original→reduced direction.

2. **§2.2 SEL2 and patterns P0/P1/P2/Pm (lines 66–82): ACCEPT.**
   - δ_GRX = #{f_i = 0} = p+1−Φ, so C_max = Φ+2 and C ∈ {Φ, Φ+2}.
   - For C = Φ+2, the long block contributes f_t+2 ∈ {2, 3}. This is within its parity cap: the cap is 2 when f_t = 0 and 3 when f_t = 1.
   - Bounds: 2p−Φ−2 ≥ 0 because Φ ≤ p+1, and 2p ≤ 3p−5 because p ≥ 5.
   - This is the same n-set as ROT-PP1 (SR) at κ^ = p−2.
   - T(z_P) = Σ_{P} τ_i by telescoping, and τ_i ≠ 0 on empty runs.

### §3: EXCL-PM2

3. **Lemma W2 (lines 90–96): ACCEPT.**
   - n = 2p−2m−2 for m ≤ (p−1)/2, and n = p−1 = 2p−2m at m = (p+1)/2. Every non-constant pattern is covered, with p−1 ≤ n ≤ 2p−4.
   - The q-range has size U−L+1 = min(n+1, E_−+1, E_++1, 3p−4−n), and each of the four branches is ≥ p.
   - p consecutive values of q, with 2c a unit, give every residue.

4. **Step 1 (lines 102–104): ACCEPT.**
   - At n = 2p−2 the sum is −2(q+1)c. It is zero only at q = p−1, which needs B ≥ p−1, so B ≤ p−2.
   - At n = 2p, q = 0 gives A ≤ 2p−1.
   - This leaves exactly three (A, B) pairs.

5. **Case (2p−3, p−2) (lines 105–111): ACCEPT.**
   - At most one run has a_i ≥ p−1, since 2p−2 > 2p−3.
   - So at least p runs have a_i ≤ b_i. At most p−2 of these are nonempty, so at least 2 runs are empty.
   - For an empty run, the attainable sums are −2jc with j ∈ [2,p−1] ∪ [2,p]. These miss only −2c, so τ_i = −2c.
   - For a pair of empty runs: T = −4c, and n = 2p−4 is admissible for m = 1 and m = 2. The letters c^(2p−4) are available because A = 2p−3.

6. **Case (2p−2, p−3) (lines 112–117): ACCEPT.**
   - For an empty run, j ∈ [1,p−2] ∪ [2,p−1] covers every nonzero residue. So no run is empty; this uses τ_i ≠ 0.
   - At most one run has a_i ≥ p, since 2p > 2p−2.
   - At least 3 runs have b_i = 0 and a_i = 1.
   - Any two such runs give E_− = p−1 and E_+ = 2p−4, so W2 applies.

7. **Case (2p−1, p−4) (lines 118–126): ACCEPT.**
   - At most one run has a_i ≥ p+1, since 2p+2 > 2p−1. So |Q| ≥ 4.
   - Q is not all runs because B ≥ 1. Hence every nonempty P ⊆ Q is non-constant, with E_− = p−4+a(P).
   - Each run adds at most 2 to a(·), so the first crossing above 2 lands in {3,4} ⊆ [3,p]. Therefore a(Q) ≤ 2, and at least 2 runs are empty.
   - For an empty run, j ∈ [1,p−3] ∪ [2,p−2] misses exactly {2c, 0}, so τ_i = 2c.
   - The selection (−c)^(p−4) c^p has 2p−4 letters, needs p ≤ A, and has sum 4c = T.

8. **Conditional reading (lines 32–34): ACCEPT.** ROT-PP1-TOP's conclusion for w transfers to w^, which has the same multiset.

9. **Vacuity remark (lines 36–38): REJECT as worded in raw v1; ACCEPT as replaced by erratum MAJOR1.** See R1 below.

### §4: KP2-EXCL′

10. **Lemma M: ACCEPT.**
    - The capped total is ≥ 2q in both regimes.
    - If x_i = x_{i+q}, one value would have q+1 copies, exceeding its cap.

11. **Lemma P: ACCEPT.**
    - If μ ≤ 2p−4 = R−(p−1), apply Lemma M with N = 3p−5 and q = p−1.
    - The fillers number n−(p−1) ∈ [0, p−3] and come from the p−3 unpaired letters. Each Q_I consists of n distinct actual letters.
    - RS(b) with K = p−1 = |S| and nonzero d_i gives p sums.
    - Its n equals ROT-PP1's max(p−1, 2κ+2−2m) at κ = p−2.

12. **Lemma U: ACCEPT.**
    - Uniqueness and a single class both follow from 2(2p−3) > 3p−5.
    - If a = 0: the block values give y_j = y_{j′}. The arc R_{j+1..j′} has 1 to p runs (empty runs allowed) and m = 1, so T = 0.
    - Then 2p−4 ≤ 2p−3 zero-valued letters sum to 0 under any signs.

13. **Step 1: ACCEPT.**
    - A′ ≤ p−2, using A ≥ A′ and a^(p−1)(−a)^(p−1) at n = 2p−2.
    - A ≤ 2p−1, using a^(2p) at n = 2p.
    - Hence A ≥ p−1.

14. **Step 2, window (W): ACCEPT.**
    - φ_a(z_P) = A−e(P) and φ_{−a}(z_P) = A′+e(P). This uses a ≠ −a, and that only the values ±a can have signed value ±a.
    - λ = A−2p+3 ≤ 2 and Λ = 2p−3−A′ ≥ p−1.
    - Λ−λ = 4p−6−(3p−5−δ) = p−1+δ.

15. **Step 3, heavy run: ACCEPT.**
    - The prefixes P_1, …, P_p are all non-constant, with e(P_1) ≤ λ < Λ ≤ e(P_p).
    - At the first passage, the jump is ≥ p−1+δ > 2 ≥ λ, which forces e_t ≥ Λ.
    - α_h ≥ Λ ≥ p−1, so run h is nonempty.
    - This holds at δ = 0.

16. **Step 4, light sets: ACCEPT.**
    - Disjointness gives A ≥ 2Λ, hence A′ ≥ p−1+δ ≥ p−1, which contradicts A′ ≤ p−2.
    - No assumption δ ≥ 1 is used.
    - The argument also covers sets made of empty runs.

17. **Step 5: ACCEPT.**
    - If λ ≤ −1, each of the p runs i ≠ h has β_i ≥ 1, so A′ ≥ p.
    - Hence b ∈ {p−2, p−3, p−4} and λ = p−2−b.
    - CT is not used.

18. **Step 6: ACCEPT.**
    - |P+| ≤ e(P+) ≤ λ.
    - A nonempty run other than h either lies in P+ or contains a letter from B. So there are at most b+λ = p−2 such runs, and at least 2 runs are empty.
    - No run is assumed nonempty.

19. **Step 7: ACCEPT.**
    - RS(b) with K = b = |B| and ω ≠ 0 gives |Σ(B)| ≥ b+1, so |M| ≤ p−1−b and 0 ∉ M.
    - Every n-set is J ∪ a^(n−|J|), with |J| ≤ b ≤ p−2 ≤ 2p−6 ≤ n. Such a set is feasible iff |J| ≥ n−A.
    - All n used are admissible.
    - **b = p−2:**
      - n = 2p−4 ≤ A gives M = {τ+4a}.
      - n = 2p−2 = A+1 excludes only nonempty J. So τ+2a lies in Σ(B) \ Σ_{≥1}(B) ⊆ {0}, i.e. τ = −2a for every empty run.
      - A pair of empty runs then gives T = −4a = (2p−4)a, a contradiction.
    - **b = p−3:** 2a, τ+2a and τ+4a all lie in M. They are distinct, since τ = −2a would put 0 ∈ M. That is 3 elements, but |M| ≤ 2.
    - **b = p−4:**
      - M = {2a, τ+2a, τ+4a}.
      - The crossed matching gives 4a = 0, which is impossible.
      - Let x ∉ {0, −1}. If the runs are adjacent, x = 1 and 4 ∈ {1,2,3}. If not adjacent, x = −1/2 and 2 ∈ {1, ½, 3/2}. Both are impossible for p ≥ 5.

20. **Line 212 (δ = 0 re-proves the pair case by another route): ACCEPT.**

### §5–6 and the erratum

21. **Labels: ACCEPT-WITH-FIXES** (MINOR 1).
22. **F1 as replaced by the erratum: ACCEPT-WITH-FIXES** (MINOR 6, wording only). **F2 and F3: ACCEPT.**
23. **"No step uses p ≥ 7 beyond p ≥ 5" (line 37): ACCEPT.**
    - p ≥ 5 is used only at line 70 (2p ≤ 3p−5), line 120 (B ≥ 1), line 193 (needs p ≥ 4) and lines 207/209.
    - This is not a p = 5 approval.
24. **Import table: ACCEPT-WITH-FIXES** (MINOR 2).
25. **Erratum MAJOR1 and MINOR2: ACCEPT, ACCEPT.**

### Checklist confirmations

- **No reliance on δ > 0.** δ appears only in Λ−λ = p−1+δ (Step 3 needs only > 2) and in A′ ≥ p−1+δ (Step 4). Both hold at δ = 0.
- **No silent nonempty-run assumption.**
  - (W) holds for every non-constant P, including sets of empty runs.
  - Nonemptiness is derived, never assumed: run h (Step 3), the p runs in Step 5 (via β_i ≥ 1), and the §3 Case 2 runs (via τ_i ≠ 0).
- **Avoidance direction.** The proof needs only w avoider ⇒ w^ avoider. It never uses the converse.

## Findings

**FATAL:** none.

**MAJOR:** none open.

**R1 (resolved; I concur).** Raw v1 lines 36–37 say the multisets ρ_c^A ρ_{−c}^(3p−5−A) "describe no avoider".
- That is a multiset-only exclusion. Nothing in §§2–4 addresses avoiders whose admissible normal forms have other (k, κ^).
- MAJOR (scope) is the right severity.
- The replacement is exact: ROT-PP1-TOP is vacuous under its full antecedent.
- No other line implies a multiset-only exclusion. I checked lines 30–34, 212 and 233–236.
- The corollary inherits the candidate status of KP2-EXCL.

**MINOR**

1. **Labels (lines 14–15, 160, 183, 187, 216–219).**
   - Gap:
     - The step labels are inconsistent: Step 6 is tagged [RE-DERIVED], Step 7 "[RE-DERIVED; valid for δ ≥ 0]", Step 4 [EXTENDED]. Yet §5 calls the δ = 0 validity of Steps 4, 6 and 7 NEW.
     - By the file's own definition, Steps 6 and 7 are [EXTENDED], because ROT-PP1 (line 151) places its Steps 6–9 under δ ≥ 1.
     - The header at line 160 omits ROT-PP1 Step 1, which the §4.4 preamble re-derives.
   - Fix:
     - Tag Steps 6 and 7 as "[RE-DERIVED; EXTENDED]".
     - Cite "Steps 1–2, 4–6, 8–9; Step 7 replaced by Step 5".
     - Optionally state the size of the extension:
       - Step 4 contradicts using A′ ≤ p−2 (ROT-PP1 Step 2) instead of b ≤ p−1.
       - ROT-PP1 Steps 7–9 depend on δ ≥ 1 only through its Step 6.
       - Step 5 is ROT-PP1 Step 7 with λ ≤ −1 in place of λ = −1; only the removal of CT is new.
   - All other labels are accurate:
     - EXCL-PM2 and W2 have no ROT-PP1 counterpart.
     - M, P, U, (W) and the heavy run are ROT-PP1's statements at κ^ = p−2. RS(b) at K = |S| replaces iterated Cauchy–Davenport and gives the same inequality.

2. **Import table, NF row (line 242) versus line 31.**
   - Gap: "Used in 2.1; 3; 4.3; 4.4 Steps 6–7" contradicts "Its only input is GRX". In §§3–4, the empty-run rule and the p+1 block count are hypotheses of KP2-EXCL′, not imports.
   - Fix: "Used in: 2.1 only; §§3–4 use its consequences as hypotheses of KP2-EXCL′."

3. **"Direct check" (lines 73–75).**
   - Gap:
     - The sentence "selected letters of S_t are consecutive in the selection" holds only after cyclically rotating the word so that S_t is not cut.
     - Rotation conjugates products, so avoidance is unaffected. The sentence is also not load-bearing, since GRX alone gives SEL2.
   - Fix: add "(after a cyclic rotation; GRX already covers this)", or delete the sentence.

4. **Notation collisions.**
   - Gap:
     - δ means the GRX parity count (lines 50/67) and also the count of letters off {±a} (line 161).
     - A, B, a, b are counts in §3 but a value, a set of letters and |B| in §4.4.
     - M names both Lemma M and the missing set. Q (line 119) collides with Q_I (line 146).
     - σ(Q_∅) collides with σ_y.
     - "z u_i" and "z_r u" conflate a letter with its value.
     - I found no error caused by this.
   - Fix: rename, for example δ_GRX, A_c/B_c, M_miss, and s_z(u) := z_r x_u.

5. **Unstated one-line justifications (lines 163, 190).**
   - Gap: "A′ ≤ p−2" uses A ≥ A′. "min(p, b+1) = b+1" uses b ≤ p−1, which comes from Step 5.
   - Fix: add "(A ≥ A′)" and "(b ≤ p−2, Step 5)".

6. **Erratum F1 wording.**
   - Gap: "Among the other letters" is ambiguous. The count is over all R letters: exactly R−(A−α_i)−β_i of them have z_{i}-signed value ≠ a. The pattern's T = τ_i and the admissibility of n = 2p−4 at m = 1 are left implicit.
   - Fix: state those three facts explicitly.
   - The derivation is otherwise correct. I checked:
     - K = p−1 nonzero deviations give all of Z_p.
     - At most p−1 fillers are needed. They are a-letters outside the run, disjoint from the chosen deviations.
     - The complement has 2p−4 letters.
     - At b = p−2, two runs failing the filler hypothesis would need 2p−2 > 2p−3 a-letters. That forces at least 2 empty runs.
   - F1 remains ancillary and unused by the proof.

## Import audit

| Input | Accepted scope (from the supplied verdicts) | Use here | Status |
|---|---|---|---|
| NF (ROT-few-E-v4 lines 28–43; fewodd addendum 1 line 12; ZX overlays 1–3; lowodd item 2, M1, M4) | Every length-4p−2 avoider, p ≥ 5. Existential "some normal form" (overlay 2). PM* preserves avoidance in the original→reduced direction only. | §2.1 only: w^ is an avoider, all blocks odd, empty-run rule. "Same multiset" is used only in lines 32–33. No DAV, no k = 1 branch, no maximality. | In scope |
| GRX "if" direction (notes-GRX lines 7–20; lowodd item 1, M2) | Every word over D_2p, every cyclic constant-block representation, empty runs allowed, the stated group law. | C ∈ {Φ, Φ+2}; patterns all-plus, every non-constant z_P, z_{i}, z_{i,i′}. θ_i and T are copied verbatim, so no convention is mixed. | In scope |
| RS(b) (ROW lines 16–27 with erratum-2 R5; CFXT item 4) | Integer K ≥ 0, all terms nonzero. | K = p−1 on d_i (Lemma P); K = b on ω (Step 7); K = p−1 in F1. Always K = \|S\|. | In scope |
| Cauchy–Davenport | Classical | Only inside RS(b) | In scope |
| CT | Permitted by the scope | Unused | n/a |
| Pending: ROT-PP1(-TOP), PP1-EXCL, ROT-SING(+), ONE-SHORT-LS, ASSEMBLY-P, (S1), Lev, S(p), LS+2, REFL | Not premises | ROT-PP1-TOP appears only as an antecedent (lines 32–34) and as the object of the vacuity corollary. PP1-EXCL's SR/OM′ appeared only in raw F1, which the erratum replaced. | No premise use |

## Trust boundary

- **Basis of validity.** The result holds relative to the accepted NF, GRX and RS(b) at the scopes above, plus classical Cauchy–Davenport. I re-read the written proof of RS(b) (ROW lines 20–27 with R5) as a sanity check. I did not re-review NF or GRX.
- **Not checked.** Per your instruction I used no tools, so I did not check:
  - any SHA256, byte count or line pin;
  - timestamps;
  - the freeze, one-pass and no-computation process claims;
  - the manifest's coverage claims.

  The supplied material does contain 15 ranges from 14 files besides the package and the erratum, which matches the package's description.
- **Scope of NF taken on trust.** Acceptance statuses come from the supplied verdict excerpts. That Sec. 0 of NF applies to every avoider, not only within ROT-FEW-E, is read off that verdict chain. The visible text of Sec. 0 is general, and KP2 uses only its terminal output.
- **No computer-assisted inputs.** This is visible for RS(b) in the CFXT "Limits" section. For NF and GRX it is taken from the package.
- **Context only.** ROT-PP1-v2 and its errata were read only to audit the labels and the vacuity wording.
- **Not reviewed and not approved:** other (k, κ^) cells, REFL/INV*, any o_F statement or assembly, full ordered Olson, p = 5, novelty or priority, Lean or human review.
