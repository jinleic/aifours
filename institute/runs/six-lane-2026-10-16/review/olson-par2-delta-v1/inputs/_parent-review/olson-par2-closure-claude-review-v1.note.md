DISPOSITION: ACCEPT-WITH-FIXES

There are no FATAL or MAJOR findings. Every new step and Lemma M0 was re-derived by hand from the packet. Nothing was executed, and all numbers below are hand computations.

Imports were treated in two ways:
- **Re-derived by hand, not just trusted:**
  - r2: Lemma S (fix-1 end-point bounds, the Claim's vertex sums), Lemma K and its Corollary, Lemma Phi/G/AV.
  - v2 parts of T2: Fact F, KL, W, B1, the counts of Theorem A and KS, AC, G1.
- **Checked only for hypothesis matching:** Lemma H, BC, K0, OR, K1, K1', S1', A1', KB, Lemma HW.

Abbreviations:
- T1 = `inverse-parity/mixdef-low/c2/proof-R4-closure.md`
- T2 = `.../c2/proof-Rstar-r3.md`
- T3 = `.../c2/proof-PAR-assembly-r1.md`
- T4 = `inverse-run-count/proof-RUNS.md`
- r2 = `.../c2/proof-MIX-low-partial-r2.md`
- Kp = `inverse-parity/proof-PAR-Kplus-partial-r2.md`

## Findings (all MINOR)

**MINOR-1** `inverse-parity/mixdef-low/c2/proof-R4-closure.md:40`
- **Problem:**
  - Theorem M cites Corollary' (`.../proof-Rstar-r3.md:198`) and the conditional end of `.../proof-PAR-assembly-r1.md:37-38`.
  - Both assume "no interval-feasible normalized data lie in R4". Lemma R4 does not prove that. It proves that no *avoider's* lift data lie in R4.
  - Its KL prefix may have several blocks, so interval-feasible R4 data are not excluded.
- **Corrected:** "By proof-Rstar-r3.md L138-140, L173-176, L192-193, every normalized MIX_low avoider with B >= 1 has lift data in R4. By Lemma R4, no avoider does."
- The logic of the proof is otherwise intact.

**MINOR-2** `inverse-parity/mixdef-low/c2/proof-R4-closure.md:33`
- **Problem:** "-(g+s+1) + 2s < 0" needs s <= g. That follows from (iii) (s <= B-2) and R** (B <= g), but the line does not cite it. It is also unnecessary.
- **Corrected:** "BH(S) <= 2s - delta+ <= s - g - 1 <= B - g - 3 < B. S != [k] because BH(S) < s + 1 + B = BH([k])."

**MINOR-3** `inverse-parity/mixdef-low/c2/proof-Rstar-r3.md:194-195`
- **Problem:** "so s <= alpha - 2" uses m(Z0+) >= 1, which is not justified. T1:18 then cites this place for "Z0+ is nonempty".
- **Insert:** "Z0+ != empty: otherwise 2phi(Z0+) + alpha = 0 < 2g + s + S_Z, contradicting R***. Hence m(Z0+) >= 1 and alpha >= s + 2 + S_Z."

**MINOR-4** `inverse-parity/mixdef-low/c2/proof-Rstar-r3.md:192` (same at :176)
- **Problem:** "every MIX_low avoider has lift data in R4". R* through R4 are sets of normalized data.
- **Corrected:** "every normalized MIX_low avoider (after Lemma M0, with B >= 1 and A <= 2p-1)".

**MINOR-5** `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r1.md:39`, with `.../proof-Rstar-r3.md:200-203`
- **Problem:** The Remark treats only normalized words. It uses 2g + B <= k-1 (that is, A <= 2p-1) and pure/pair runs, yet concludes "MIX_low(5) holds".
- **Corrected:** "Theorem P5: Sec. 2(b) (trivial cut; M0; B' = 0 by S1'), then the Remark for B' >= 1, then (a)."

**MINOR-6** `inverse-parity/mixdef-low/c2/proof-PAR-assembly-r1.md:70-73`; also `inverse-parity/proof-PAR-Kplus-partial-r2.md:133`
- **Problem:** Both are stale.
  - T3 still says PAR(p) for p >= 19 is open and needs emptiness of R4.
  - Kp:133 still says "1 <= B < kappa: OPEN".
- **Corrected:** "Superseded by proof-R4-closure.md (Lemma R4, [W], under review). That file proves the parenthetical alternative, no avoider data in R4, not emptiness of interval-feasible R4 data."

**MINOR-7** `inverse-parity/mixdef-low/c2/proof-R4-closure.md:47-48`
- **Problem:** Theorem P omits "F, R >= 1". It is implicit in "2k runs" and in proof-INV-reduction.md:21-28, and K0 (proof-PAR-K0.md:94), K1 and KB assume it.
- **Fix:** Add it to the statement.

**MINOR-8** `inverse-parity/mixdef-low/c2/proof-R4-closure.md:53-54`
- **Problem:** Corollary DR' (proof-DR.md:44-46) is stated with INV(p), not INV_Res(p).
- The claim is still valid after replacing Theorem DR by Theorem DR-Res (proof-INV-reduction.md:19-20), because DR' uses only Theorem DR's conclusion (proof-DR.md:57-58).
- **Corrected:** "ordered Olson for D_{2p} <= INV*(p) + PAR(p) + RUNS(p), by DR-Res + DR'."

**MINOR-9** `inverse-parity/mixdef-low/c2/proof-R4-closure.md:11-12` and `:64-65`
- **Problem:**
  - X and delta+ are attributed to r3 but are defined only in T1.
  - "Satisfying exactly the hypotheses used" is inaccurate. The replay assumes delta+ >= 2s - B, which is weaker than (iv), and it takes a derived Step-1 property ("heavier class BH >= s+1") as a hypothesis.
- **Corrected:** "defined here" and "a weakening of the facts used (evidence only)".

**MINOR-10** `inverse-parity/mixdef-low/c2/README.md:98-99`
- **Problem:** The log names the superseded finite statement "Theorem PF … [W] + [F]" without "conditional on unreviewed census code". T3:21 has since relabelled it Statement PF.
- **Fix:** Mark the log entry as superseded and conditional.

**MINOR-11** `inverse-parity/proof-PAR-K0.md:4`
- **Problem:** The status line "not yet hostile-reviewed" is stale (already explained at T2:19-21).
- **Fix:** Update it.

## 1. Completeness

**Verdict:** the proof is complete and correct from the stated imports. The only gaps are the citation and wording issues MINOR-1 to -5 and MINOR-7. I verified the chain below.

**MIX_low(p).** Let v satisfy the MIX_low hypotheses and avoid.
1. If A >= 2p, rho_1^{2p} kills. So A <= 2p-1. Since A = 2p - k + 2g + B, this means 2g + B <= k-1.
2. Iterate M0. The result v' avoids, with the same k, d_t, parities, theta and g, and B' = B - #steps.
   - (2a) B' = 0: then A' = A - B <= 2p-2 and R' = A' = 2p - k + 2g. Since k >= 2g+2, R' <= 2p-2, so S1' always applies. A1' and the trivial cut cited in T1:43 / T3:34 are never reached; this is harmless.
   - (2b) B' >= 1: v' is a normalized avoider, and r2 Lemma S gives lifts.
3. Data not in R*: MIX-R (via Lemma G and AV, or P* = Z0).
4. Then, in order:
   - B' >= g+1: W.
   - Some d >= 2p - B': B1.
   - Data in R* with some bh >= B'+1: Theorem A.
   - What remains is R**. By F(d), all d <= 2g+B-2, so all phi <= g-1.
5. Then:
   - All runs cheap: AC.
   - Some run not cheap and 2X + alpha <= 2g + s - 1 + S_Z: KS.
   - What remains is R***.
6. Then:
   - c(Z0+) >= g+1: ZP.
   - Some bh >= s+1: C (phi_t0 <= g-1 <= p-k+g).
   - What remains is R4.
7. R4: Lemma R4.

Every kill is a proper P with x(P) in I(P). Then u_P lies in I(P) mod p, and Lemma H gives an identity 2p-subword, which contradicts avoidance. G1 is not needed for all p (R4 forces g >= B >= s+2 >= 4), so T1:41 rightly omits it.

**PAR(p).**
- Setup: w is an inherited avoider with k <= p and F, R >= 1.
  - Normalize B <= A.
  - Avoidance gives A, B <= 2p-1 and B <= kappa.
  - (Pairs) gives kappa >= 0.
- kappa = 0: K0, so there is no even run.
- kappa >= 1: (V) gives o_F >= kappa+1 >= 2.
  - B = 0: OR, then S1' / A1' / trivial cut.
  - B = kappa: KB.
  - 1 <= B < kappa: OR, then Theorem M on w~.
- K1 and K1' are redundant (for kappa = 1, B is in {0, kappa}).
- No (kappa, B) is missed, since 0 <= B <= kappa.

Theorem PA (T3:18-19) is a correct conditional. Theorem M neither discharges its hypothesis nor needs it.

## 2. Lemma M0 (T4:402-414), checked independently against Lemma HW

**Every pattern P ⊆ [k], including ∅ and [k]:**
- f_j(P) and m(P) depend only on P, so they are unchanged.
- h(P) = Σ floor((l_j - f_j)/2). Only the run j0 changes: floor((l_j0 + 2 - f)/2) = floor((l_j0 - f)/2) + 1. So h' = h + 1 (equivalently H' = H + 1, with beta unchanged since l_j0 + 2 ≡ l_j0).
- E+: if t ∈ P one a_t is lost, if t ∉ P one b_t is lost; either way E+' = E+ - 1.
- E-' = (R - 2) - (E+ - 1) = E- - 1.

All verified.

**g'(E-1) <= g(E):**
- Term 1: p - m is the same.
- Term 2: (E-1) + m + (h+1) - p = E + m + h - p, the same.
- Term 3: floor((E-1)/2) <= floor(E/2).

So I'(P) ⊆ I(P) as integer intervals. An empty window stays empty (a' >= a > b >= b'). The Z_p value phi(P) = Σ(y_{i-1} - y_i)/2 is unchanged, so phi(P) ∉ I(P) mod p implies phi(P) ∉ I'(P) mod p. P = ∅ (the zero condition) is included. Full windows are irrelevant in this direction: w avoids, so it has none, and containment creates none. Verified.

**Run structure:**
- r_t >= 3 gives r_t - 2 >= 1, so no run vanishes or merges and k is unchanged.
- R' >= 1 and F' >= 1, so HW applies to w'.
- d_t and the parities are unchanged.
- A' = A - 1, B' = B - 1, R' = R - 2, H' = H + 1, kappa' = kappa - 1, so g is unchanged.

**Iteration:** R strictly decreases. The process stops exactly when every run is pure or (1,1). Only Lemma HW is used; no inherited hypothesis enters. Verified.

**Uses:**
- B' >= 1: all MIX_low hypotheses hold.
  - Parities are unchanged and k <= p.
  - A' - B' = D > 0.
  - kappa' - B' = g >= 1.
  - kappa' <= kappa <= k-1.
  - A' <= 2p-1.
- B' = 0:
  - All letters are rho_1, all reflection runs odd, k <= p.
  - kappa' = g >= 1 and R' = 2p - k + 2kappa'.
  - These are exactly the hypotheses of S1', as noted in §1.

Verified.

## 3. Lemma ZP, Lemma C, and the R4 consequences (T2)

**Lemma ZP:**
- Z0+ is nonempty, since c(∅) = 0 < g+1.
- Z0+ is proper, since Y is nonempty (Σbh = k - 2g > 0).
- Free implies cheap, so d <= 2g+B by F(b), and phi <= g-1 by F(c).
- BH(Z0+) <= 0 <= B.
- KL applies. Verified, in the full setting (no R* needed).

**Lemma C:**
- [k]∖{t0} is a cyclic interval with m = 1.
- c = TOT - phi_t0 + 1 >= g + 1.
- BH = k - 2g - bh_t0 <= B.
- In R**, phi_t0 <= g-1 <= p - k + g because k <= p+1.
- KL applies. Verified.

**Consequences (T2:194-197), all verified:**
- s >= 1, because Y is nonempty and bh <= s.
- alpha >= 2m(Z0+) + s + S_Z, from c(Z0+) <= g and R***.
- Z0+ is nonempty (MINOR-3).
- s <= alpha - 2 <= B - 2 <= g - 2, using alpha <= anti mass <= B and B <= g.
- exc >= alpha + beta + pi_0 + s:
  - delta = 2phi(Z0+) - S_Z - n_d + (free anti mass) + Σ_(iv)(-bh).
  - This is >= 2g + s - n_d.
  - Then exc = |Z0| + delta - 2g gives the bound.
- (anti mass in Z0) >= s + S_Z + 2m, from (R1) together with L_Z = alpha + beta + anti mass + pi_0.

**Used later:**
- s >= 1: T1:27.
- The alpha bound and Z0+ nonempty: T1:18-20.
- B >= s+2: T1:20, 24.
- s <= g: implicitly at T1:33.
- The delta bound: reused in delta+ form at T1:20-22.

The exc and anti-mass bounds are not used by T1. I used them in §9(b).

## 4. Lemma R4 (T1:16-35), line by line

**Facts:**
- (i) Verified: F(d) plus R** give all d <= 2g+B-2, and F(c) gives phi <= g-1.
- (ii) Verified: this is the definition of R4.
- (iii) Verified:
  - X + m(Z0+) <= g with m >= 1 gives X <= g-1.
  - With R***, alpha >= 2m(Z0+) + s + S_Z >= s+2, so B >= alpha >= s+2.
- (iv) Verified:
  - delta+ = 2X - D(Z0+) = 2X - S_Z - n_d + (free anti mass) >= 2X + alpha - S_Z - n_d >= 2g + s - n_d.
  - n_d <= X, since an aligned Z0 run has phi >= d/2 > 0, hence phi >= 1.
  - So delta+ >= g + s + 1.

**Step 1.**
- Y ≠ [k], so its maximal cyclic intervals are paths.
- In R4, |Z0| >= alpha >= 4 and k = 2g + B + s + 1 >= 15, so |Z0| = 1 and small k cannot occur.
- Independence holds anyway for any proper path once k >= 4: two path positions i < i' with i' - i >= 2 have cyclic distance >= min(2, k - (len - 1)) >= 2.
- BH(Y) = s + 1 + B + delta and delta >= delta+.
- The text claims BH(Y) >= 2s+3; in fact BH(Y) >= 3s + g + 4.
- BH(Q) >= BH(Y)/2 > s+1.
- Greedy N: s+1 <= BH(N) <= 2s, |N| >= 2 (since s >= 1), and N is independent.

All verified.

**Step 2(a).**
- S' is proper (N ≠ ∅) and nonempty (S' ⊇ Z0).
- m(S') = |N|, because the complement of a nonempty independent set has |N| nonempty arcs.
- c(S') = TOT - phi(N) + |N| >= g + 1.
- BH(S') = (k - 2g) - BH(N) <= B.
- phi <= g-1 on S'.
- KL applies. Verified.

**Step 2(b).**
- phi(N) >= p - k + g + |N| >= g + 2.
- c(S) >= X + phi(N) + 1 >= g + 3.
- BH(S) <= s - g - 1, which is < 0 using s <= g (see MINOR-2; not needed).
- S is proper and nonempty, and phi <= g-1 on S.
- KL applies. Verified.

**No counterexample.** I could not build data meeting (i)-(iv) where a step fails. Every step is arithmetic on (i)-(iv), and both branch boundaries are tight but valid (§9b). Two observations:
- (iv) can be weakened to delta+ >= 2s - B.
- |N| >= 2 is not needed: with |N| = 1, c(S) >= g + 2 in (b).

## 5. Coverage, consistency, direction

**Coverage:** MIX-R, W, B1, A, AC, KS, ZP, C and R4 cover every normalized avoider (§1). G1 is needed only for P5.

**Definitions are consistent across files:**

| Symbol | Where defined |
|---|---|
| Z0 = {bh <= 0} | r2:86, T2:100 |
| Y | r2:87, T1:23 |
| Z0+ = free runs | T2:143, :182 |
| alpha | T2:142, T1:12 |
| beta: non-free Z0 runs = antis with phi <= -1 = the (iv)-antis | T2:146, :197 |
| S_Z | r2:140, T2:101 |
| s | T2:30, T1:12 |
| delta | r2:87, T1:25 |
| X, delta+ | T1 only |
| R* | r2:134-139 = T2:102-103 |
| R**, R***, R4 | T2:140, :175, :193 (also T3:18-19) |

The integer phi_t of T2 differs from the Z_p phi of T4; T3:33 refers to the Z_p one, correctly.

**Direction:** every kill is "avoider lift data in a region imply an identity 2p-subword". No emptiness claim about interval-feasible or relaxed data is used. The only exception is the citation in MINOR-1, whose content is not needed.

## 6. PAR chain hypotheses (T3 §2, T1 §3)

| Lemma | Hypotheses and where they come from |
|---|---|
| K0 | k <= p; (P) and (V) for w; kappa = 0; even run. Gives "all runs odd" because (P) gives e_R <= e_F. |
| OR | o_F >= 1 from (V). Keeps A, B, kappa; k~ = o_F <= k <= p. |
| S1' / A1' | k~ <= p, all reflection runs odd, B = 0, kappa >= 1. |
| KB | B = kappa, (V), o_F <= p, (D0) if capped. |
| MIX_low on w~ | k~ <= p; kappa <= o_F - 1 from (V); 1 <= B < kappa; A >= B. |

- K1 needs (V) and k <= p. K1' additionally needs (D0).
- The zero condition comes from A, B <= 2p-1 (Lemma H, proof-PAR-K0.md:23-31).
- All hypotheses are matched.

## 7. Census dependence

Sentences whose conclusions depend on census or replay output:
- **T1:** L4, L56-69 (including L62).
- **T2:** L11, L207-246 (bullets L216-217, L218-230, L231-236, L237-241, L242-246).
- **T3:** L6-7, L21-22, L41-54, L68, and L72 ("as a theorem rather than [W+F]").
- **c2/README:** L57-66, L78-84, L89-91, L98-99, L104.
- **Imports:** r2:148-155; proof-PAR-K0.md:45-46, 151-155, 159-162; Kp:61-63, 92-94, 113, 147-159, 296-300; T4:340-346; proof-DR.md:62-67.

Theorems M, P, PA and P5 depend on none of them, explicitly or silently. Statement PF is labelled conditional at T2:207-209, T3:6-7, :21 and :41, but not at c2/README:98-99 (MINOR-10).

## 8. Claims and status

- **Theorem statements:** no overclaim, given the imports.
- **Stale statements:** MINOR-6, -10 and -11. T2:12-13 and T3:8 are correct file-locally and are superseded only jointly with T1.
- **T1:53-54:** correct once read with DR-Res (MINOR-8).
- **Diff check, hunk by hunk:** header and imports (fix 5); KL anti-mass line (fix 3); Theorem A B_Y line (fix 4); §6 opening (fix 2); residual and Corollary (fix 1); additions (T2:182-203); §7 changes (6a, 6b, 6c); change log.
- **Unlisted change:** one §7 sentence (diff:142 = T2:241, "At p = 13 … CPU limits (UNKNOWN)"). It is evidence only, not a reviewed statement. No reviewed statement in §1-6 changed beyond the listed fixes.

## 9. Hand sanity checks (hand computations, not executions)

### (a) M0 at p = 5

**Word:**
- k = 5.
- Rotation runs: R_1 = (a,b) = (2,1), then R_2..R_5 = (2,0), (2,0), (1,0), (1,0).
- Reflection runs: l = (1,1,1,1,5).
- So A = 8, B = 1, R = 9, H = 2, kappa = 2, g = 1. This is a MIX_low word.

**M0 step:** apply it to R_1 (giving (1,0)) and add sigma sigma to S_5 (l_5 = 7). Then A' = 7, B' = 0, H' = 3, kappa' = 1, g' = 1.

**P = ∅** (g(E) = min(5, E + h - 5, floor(E/2))):

| | E+ | E- | g(E+) | g(E-) | Window |
|---|---|---|---|---|---|
| Before (h = 2) | 1 | 8 | -2 | 4 | I = [-4, -2] |

After the step (h' = 3, so g'(E) = min(5, E - 2, floor(E/2))): E+' = 0 and E-' = 7. Then g'(0) = -2 and g'(7) = 3, so I' = [-3, -2] ⊆ [-4, -2]. 0 lies in neither window mod 5.

**P = {1}** is the mixed run, so t ∈ P. Here m = 1, the boundary runs S_5 and S_1 are both odd, and g(E) = min(4, E + h - 4, floor(E/2)).
- **Before (h = 2):** E+ = a_1 = 2 and E- = 7. Then g(2) = 0 and g(7) = 3, so I = [-3, 0].
  - Lemma H gives the same window: lambda({1}) = min(5, 1, 2) = 1 and lambda({1}^c) = min(5, 6, 4) = 4.
- **After (h' = 3):** E+' = 1 and E-' = 6. Then g'(1) = min(4, 0, 0) = 0 and g'(6) = 3, so I' = [-3, 0] = I. Containment holds with equality.

**P = {2}** is a pure run, so t ∉ P. Its boundary runs S_1 and S_2 are odd.
- **Before:** E+ = a_2 + b_1 = 3 and E- = 6. Then g(3) = 1 and g(6) = 3, so I = [-3, 1].
- **After:** E+' = 2 and E-' = 5. Then g'(2) = 1 and g'(5) = 2, so I' = [-2, 1] ⊆ [-3, 1], strictly.
  - Lemma H gives the same window (B' = 0, kappa' = 1): lambda = min(5, 2, 2) = 2 and lambda(complement) = min(5, 5, 3) = 3.

In all three patterns, E+ and E- each drop by exactly 1, h rises by exactly 1, and the window shrinks. After this step B' = 0 and k = 5 >= 2kappa' + 2 (R' = 7 <= 8), so S1' applies, matching §2.

### (b) Data for Lemma R4

**s = 1 is impossible.**
- With all bh <= 1, every Y run has bh = 1, so exc = 0.
- But exc = |Z0| + delta - 2g >= |Z0| - n_d + s >= alpha + s >= 2s + 2 = 4.
- That is a contradiction.

**Consequences:**
- s >= 2, so B >= alpha >= s + 2 >= 4 and g >= B >= 4.
- Then k = 2g + B + s + 1 >= 15, so p >= 17.
- So R4 is empty by arithmetic alone for p <= 13, without any census.

**At p = 17** only two parameter sets are possible: (k, g, B, s) = (15, 4, 4, 2) and (17, 5, 4, 2).
- In both, alpha = B = 4 (four free antis with c = 1) and beta = pi_0 = S_Z = 0.
- X = g - 1, and every Y run is aligned with phi >= 0.
- phi(Y) is 7 in the first case and 6 in the second.
- Branch (b) would need phi(N) >= p - k + g + |N|, that is 6 + |N| or 5 + |N|. With |N| <= 3, this exceeds either 2(g - 1) or phi(Y).
- So only branch (a) can occur at p = 17.

**An instance with both branches at their thresholds.**

Parameters: p = 23, k = 21, g = B = 6, s = 2. Then D = 37, A = 43 <= 45, kappa = 12, TOT = 14 and Σbh = 9.

Runs:
- Position 1: a (iv)-anti with c = 2, bh = 0, phi = -1.
- Positions 2-4: aligned, d = 1, bh = -1, phi = 1.
- Positions 5-8: free antis with c = 1 and (phi, bh) = (1,-3), (1,-3), (0,-1), (0,-1).
- Positions 9-21: Y, aligned, with bh = (1,2,2,1,2,1,2,1,2,1,2,1,2).

Every fact Lemma R4 uses holds, several with equality:
- X = 5, m(Z0+) = 1 and c(Z0+) = 6 = g.
- alpha = 4 = 2m(Z0+) + s + S_Z.
- 2X + alpha = 14 = 2g + s + S_Z.
- delta+ = delta = 11 = 2g + s - n_d >= g + s + 1.
- exc = 7 = alpha + beta + pi_0 + s.
- (R1): Phi(Z0) = 10 <= 13.
- (R2): |Y_al| + a_Z = 13 - 11 = 2.
- phi(Y) = 10.

Step 1 on this instance:
- BH(Y) = 20 = s + 1 + B + delta.
- The heavier parity class {9, 11, ..., 21} has BH = 13.
- The greedy set is N = {9, 11}, with BH(N) = 3 = s + 1 and |N| = 2.

**Branch (a) at its threshold.** Take phi_9 = 5, phi_11 = 4, phi_10 = 1 and phi = 0 on the other Y runs (all d <= 16).
- phi(N) = 9 = p - k + g - 1 + |N|.
- S' = [21] ∖ N has m = 2, c = 7 = g + 1 and BH = 6 = B.
- The KL prefix is P = {1..8, 10}, with c = 7, D_P = 1, BH = -9, so x(P) = -4.
- U_P = G_2(1) = -4 and L_P = G_2(36) = 21.
- So -4 ∈ [-21, -4]: a kill exactly at the edge (Phi(P) = 2g + 2).

**Branch (b) at its threshold.** Take phi_9 = phi_11 = 5 = g - 1 and phi = 0 on the other Y runs.
- phi(N) = 10 = p - k + g + |N|.
- S = {2..8} ∪ N has c = 17 and BH = -8.
- The KL prefix is P = {2..9}, with c = 11 ∈ [7, 12], D_P = 10, BH = -10, so x(P) = 0.
- U_P = G_1(10) = 4 and L_P = G_1(27) = 16.
- So 0 ∈ [-16, 4]: a kill.

No step fails at any boundary. In branch (b), phi on the interval {2..9} is 10, but gam(10) = 5, so this instance violates Lemma S. It is arithmetic test data, not interval-feasible data. That is expected, because a KL kill on an interval contradicts Lemma S.

### (c) The Remark on MIX_low(5) and Theorem P5

At p = 5, 2g + B <= k - 1 <= 4 forces g = 1 and B ∈ {1, 2}. The cases:
- B = 2 >= g + 1: Lemma W.
- B = 1, data not in R*: MIX-R.
- B = 1, data in R*, some bh >= 2: Theorem A.
- d >= 9 cannot happen, because F(a) gives d <= 8, so B1 is vacuous.
- Otherwise F(d) excludes d ∈ [2, 8], so every d <= 1. Then G1 (g = 1, every aligned d <= 3) shows (R1) fails, which contradicts R*.

This is verified, for normalized words only (MINOR-5). R4 plays no part here, since it needs p >= 17.

Theorem P5 follows from T3 §2(b), then the Remark, then §2(a). Verified with the MINOR-5 fix. It is subsumed by Theorems M and P.

## Established

All verified by hand from the packet:
1. **Lemma M0** (T4:402-414) as stated, for every pattern including ∅ and [k], from Lemma HW alone. Also its uses in T3 §2(b) and T1:42-43; at B' = 0, S1' alone suffices.
2. **Lemma ZP and Lemma C** (T2:182-190) in the normalized MIX_low setting, and all six R4 consequences (T2:192-197). Z0+ being nonempty needs the one line from MINOR-3.
3. **Lemma R4** (T1:16-35), with the MINOR-2 rewording. In addition, R4 forces s >= 2, g >= B >= 4, k >= 15 and p >= 17.
4. **Theorem M**: MIX_low(p) holds for every prime p >= 5. This is relative to:
   - r2: Lemma S, Lemma K and its Corollary, Lemma Phi, Lemma G, Lemma AV, MIX-R;
   - the v2 parts of T2: Fact F, KL, W, B1, A, KS, AC;
   - Lemma M0, Proposition S1' and Lemma H.
5. **Theorem P**: PAR(p) holds for every prime p >= 5, with F, R >= 1. This is relative to K0, OR, S1'/A1', KB and Theorem M; K1 and K1' are redundant.
6. **Theorem P5** (subsumed, with MINOR-5) and **Theorem PA** (a correct conditional that Theorem M does not need).
7. **The r3 diff**: §1-6 changed only by the listed fixes plus the additions.

## Open

- RUNS(p) for all p, and INV*(p). Ordered Olson for D_{2p} needs PAR + RUNS + INV*, via DR-Res and DR'.
- A second independent review of T1 and the r3 additions. A model re-review of the r2 fixes is also still outstanding; I re-derived fixes 1 and 2 by hand, and fix 3 is a definition.
- Statement PF remains [W+F] and conditional on the census code. It becomes redundant if Theorems M and P are accepted.

## UNKNOWN

- The SHA-256 values (not computed) and the completeness and faithfulness of the parent diff (taken as given).
- Material outside the packet: proof-GR.md, repr-WAS.md, the derivation behind Lemma HW, and all census and replay code.
- The internal correctness of Lemma H, BC, K0, OR, K1, K1', S1', A1' and KB. For these I checked only that the hypotheses match at each use.
- Lines omitted from the excerpted files. None of them is used by the claim.
