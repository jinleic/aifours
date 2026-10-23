DISPOSITION: ACCEPT-WITH-FIXES
ASSEMBLY: CORRECT conditional on (GC). Theorems A, B and C (branches C1-C6, exhaustive given Fact Z) and Corollaries B', D and E were re-derived by hand, and every hypothesis match holds. All fixes are documentation-level.
IMPORTS-NO-CLAUDE-REVIEW: re-derived line by line from the inlined text, and no mathematical error was found in any of these: the C0-B' chain (TL, KW, S1 Steps 0-4, Split, Depth, C0-B), A1, ALT, B0, the K0 extension, FWH, R2, BR, FW+, KBH/ZS, KB (capped and uncapped), S1', A1', OR, BC, RL, and Theorem B (U10). Lemma H/HW was checked only down to the Lemma WAS/GR interface. GC was not checked; it is the hypothesis.
INV*-SEPARATE: YES

Abbreviations: T = olson-runs-assembly-proof-v2.md; RUNS = olson/inverse-run-count/proof-RUNS.md; K0 = olson/inverse-parity/proof-PAR-K0.md; KP = olson/inverse-parity/proof-PAR-Kplus-partial-r2.md; KBH = olson/inverse-run-count/kappaB-high/proof-KBH.md; C2F = olson/inverse-run-count/mixdef-high/c2/proof-C2.md; MH = olson/inverse-run-count/mixdef-high/proof-MH.md; OBL = olson/inverse-parity/mixdef-low/c2/obligations-after-PAR.md; GC = olson/inverse-run-count/mixdef-high/c6/proof-GC.md; C3S = olson/inverse-run-count/mixdef-high/c3/proof-C-r1.md; R4 = olson/inverse-parity/mixdef-low/c2/proof-R4-closure-r1.md; INVR = olson/proof-INV-reduction.md; DR = olson/proof-DR.md; HWF = olson/inverse-run-count/README.md.

## FATAL
none

## MAJOR
none

## MINOR

**m1. T:L166, T:L200, T:L206, T:L238: (P) is over-attributed to C2. C2 uses no inherited condition.**
- In K0, (P) enters only at K0:L103, where it turns "an even run" into e_F >= 1 when the even run is a rotation run.
- Step 3 (K0:L128-131) needs only e_R ≡ e_F (mod 2). Hand check: R_{G0} ≡ c_{G0} - e_R ≡ c_{G0} - e_F = 1 (mod 2).
- That parity holds for every kappa = 0 word, since R = 2p - o_F ≡ o_F and R ≡ o_R.
- In C2, e_F = k - o_F >= 2 comes directly from o_F <= p - 1 < k.
- Corrected statement: "C2 uses only o_F >= 1 (automatic, Fact Z(iii))". This agrees with RUNS:L387-389 and L392-397.
- L206 should therefore read "(P) is never used in Theorem C".
- L238 should justify not claiming MIX_RUNS by C3's capped (D0) alone. That (D0) use is genuinely necessary, because type-(II) non-inherited avoiders exist (KBH:L111-113).
- No conclusion changes.

**m2. T:L224 (U6): the dependency list is incomplete.**
- Theorem C0-B (RUNS:L303-309) runs Theorem S1's Step 3 kill conditions (K1)-(K6) and its Step 4 greedy (RUNS:L224-243).
- C0-B' re-checks both at RUNS:L337.
- U6 lists only "Steps 0-2 (L188-222)". Correct it to L188-243. I verified L224-243.

**m3. Name collisions.**
- (a) "C2" means the file C2F at T:L23 ("C2 (R >= 2p - 2)"), but means the branch B = 0 = kappa at T:L163, L200 and L238.
- (b) "Theorem P" at T:L59, L179-180 and L186 is PAR (R4:L84-94).
- By contrast, INVR:L23 derives (P) from a different "Theorem P": the general-word gap theorem of proof-dihedral-partial.md (OBL:L58).
- Fix: add one sentence to Remark (1) so that no reader infers a circularity.

**m4. T:L149: the title wording reads as a false universal.**
- "kappa > B for every RGR word" suggests a claim about all RGR words.
- Corrected title: "...and every RGR word with 1 <= B < kappa".

**m5. T:L122, T:L146: "R^ >= 2p the trivial cut" is vacuous.**
- When B^ = 0, R^ = A^ <= A <= 2p - 1, so the case never arises.
- This is harmless; mark it as vacuous.

**m6. T:L173 and T:L223 (U5): C5 re-proves only the B < kappa half of RL.**
- RL's B = kappa half is C3 (KB).
- RL's B = 0 and kappa = 0 preliminaries are C1 and C2.
- Corrected statement: "RL = C3 + C5, given C1 and C2".

**m7. T:L17, T:L181: add "with F, R >= 1".**
- "Inherited" is only defined for F, R >= 1 (INVR:L12).
- This is harmless: no avoider of length 4p - 2 has F = 0 or R = 0.
  - R = 0 forces sigma_y^{4p-2}, which contains sigma_y^{2p} = 1.
  - F = 0 gives either A >= 2p, or A, B >= p and then rho_1^p rho_{-1}^p.

## ANSWERS Q1-Q8

### Q1 (Theorem C)

**Exhaustiveness.** Fact Z(ii) gives 0 <= B <= kappa (T:L157).
- B = 0 splits into kappa >= 1 (C1) or kappa = 0 (C2).
- B >= 1 splits into B = kappa (C3/C4) or B < kappa (C5/C6), each split again by o_F <= p versus o_F >= p + 1.
- The branches are disjoint and complete.

**C1.**
- OR needs o_F >= 1. Fact Z(iii) gives o_F >= 2kappa + 1 >= 3 here.
- w~ has B = 0, is all-odd, has k~ = o_F, and keeps R and kappa (KP:L27-28).
- o_F <= p: the hypotheses of S1' (KP:L164-166) hold on w~: all-odd, all rho_1, k~ <= p, kappa >= 1, R <= 2p - 2. A1' covers R = 2p - 1, and the cut covers R >= 2p (since A = R).
- o_F >= p + 1: C0-B' needs only all rho_1, all-odd, R <= 2p - 2 and kappa >= 1.
  - Internally k~ <= R <= 2p - 2, as TL requires (RUNS:L338).
  - kappa = 1 gives no defect (RUNS:L325-326), so kappa >= 2 and k >= 2kappa + 2 >= 6.
- A1 covers R = 2p - 1, with k~ = 2kappa + 1 >= 2m* + 1.
- No inherited condition of w~ is used anywhere in C1.
- The o_F split is unnecessary: C0-B' and A1 carry no bound on k.

**C2.** K0 uses k <= p in exactly two places, and both replacements are correct.
- (i) K0:L102, R >= p >= 5. This is consumed only in Step 4 (K0:L136-142: "R = 3", "R <= 4", "R = 2"). It is replaced by R >= k >= p + 1 >= 6.
- (ii) K0:L141, o_F <= p, used to get R + 1 >= p + 1. It is replaced by o_F = 2p - R <= p - 1.
  - Hand check, p = 5, k = 6: R >= 6, o_F <= 4, R + 1 >= 7 >= 6.
- Step 2 needs R <= 2p - 1, which follows from o_F >= 1.
- Step 3 with o_F = 1 needs k >= 2.
- Lemma BC (K0:L57-87) has no hypothesis on k.
- See m1 for (P).

**C3.** KB (KP:L238-241) is applied to w' itself.
- (V) is automatic.
- The uncapped case works on w~. It uses only D = 2p - k~ >= p and B <= k~ - 1, which are parameters OR preserves.
- The capped case uses (D0) of the unmerged w'. It enters at KP:L278 (c >= 2, r_1 <= p - 1) and gives R' = 2p - 1 - r_1 >= p (KP:L283).
- All of this matches T:L169.

**C4.** The hypotheses of KBH (KBH:L10-14) match: F, R >= 1, A >= B, B = kappa, o_F >= p + 1. No inherited condition is used.

**C5.**
- w~ is all-odd with k~ = o_F <= p and A >= B >= 1.
- B < kappa, and kappa <= k~ - 2 by Fact Z(iv).
- So w~ lies inside MIX_low (R4:L61-64).

**C6.** The inputs are exactly the hypotheses of MIX_DEF_HIGH (olson/inverse-run-count/mixdef-high/README.md:L13-14).

### Q2 (Fact T, Fact Z(iii), Fact K)

**Fact T.** After OR, the following use no inherited inequality: S1', A1', C0-B', A1, ALT, M0, uncapped KB, and Theorem M.
- (P) and (D0) can genuinely fail for w~ (KP:L37-42). KB's capped shape A_G = 2p - 1 is the example.
- After M0, none of NMH, FW+, GC, C0-B' or A1 uses an inherited inequality. The possible (P) failure at RUNS:L413 is therefore irrelevant.
- The target does not use K1'.
- B0 uses only o >= 1 (RUNS:L375).
- RL uses (V), a parameter OR keeps, and uses (D0) only through KB's capped case on w'.
- The MIX_DEF_HIGH reduction uses no inherited condition.
- T:L206-208 is correct apart from m1.

**Fact Z(iii).**
- R = A + B <= 2p - 1 + B, and R = 2p - o_F + 2kappa.
- Hence o_F >= 2kappa - B + 1 >= kappa + 1, using B <= kappa.
- This is exactly (V), since (V) is equivalent to kappa <= o_F - 1 (K0:L53). It also gives o_F >= 1, because kappa >= 0.
- Correct.

**Fact K.**
- With o_F = k, A = 2p - k + 2kappa - B <= 2p - 1, so 2kappa - B <= k - 1.
- B <= kappa - 1 gives 2kappa - B >= kappa + 1, so kappa <= k - 2.
- Correct, and consistent with R4:L66-67.

### Q3 (Theorem B)

**Cut and OR.**
- The cut works by Fact Z(i).
- k~ = o_F lies in [p + 1, 2p - 1], since o_F <= k <= 2p - 1 by (1.1).

**ALT (RUNS:L36-52), verified.**
- Dl = sum z_t d_t is odd, and k - (p + 1) = p - 2 >= 3 positions are free.
- Arc labels travel with the particles, so the walk ends at P_0^c.
- Steps of ±2 between Dl and -Dl must pass ±1, which gives {E+, E-} = {p - 1, p}.
- FW then applies with h(P) >= 0.

**M0 iteration.**
- Each step lowers B by 1, so there are at most B steps, and the iteration terminates.
- At the end, a run with a_t b_t >= 1 and r_t <= 2 is a (1,1)-pair.
- k, d_t, parities, phi, kB and D are preserved; A^ = A - s <= 2p - 1; every run stays nonempty because r_t - 2 >= 1.
- Every window shrinks, since g'(E - 1) <= g(E) (RUNS:L408-410). This holds for the empty pattern too.

**Exit B^ = 0.**
- kappa^ = kB >= 1 and R^ = A^ = D <= 2p - 1.
- C0-B' handles R^ <= 2p - 2. A1 handles R^ = 2p - 1, with k^ = 2kB + 1.

**Exit B^ >= 1.**
- w^ is all-odd, p + 1 <= k^ <= 2p - 2, and every run is pure or a (1,1)-pair.
- 1 <= B^ <= kappa^ - 1, B^ <= A^ (since A^ - B^ = D >= 0), and A^ <= 2p - 1.
- So every NMH hypothesis holds.

### Q4 (Theorem A)

**N1.** The FW+ hypotheses (C2F:L119-120) hold, with min(A, B) = B <= kappa - 1.

R2 verified:
- k = 2kappa + 2 and W = E + 3; there are >= 2k - 2p + 2 >= 4 singletons; W ≡ 1 or 3 (mod 4) according to kappa's parity.
- Claim 1'': E/2 >= ceil(kappa/2) = kappa + 1 - m0 and E/2 <= p - 1 - ceil(kappa/2) <= p - m0.
- Claim 2: the displacement after tau is <= 3 + E = W.
- All three cases close: kappa even, kappa odd with W = 3, and kappa odd with W >= 7 via Claim 3.

FWH (MH:L56-85) verified:
- All nine sums in Claim 1 check out.
- (a): steps <= 2p - k.
- (b): k >= 2m* + 1 holds iff 2kappa >= 2floor(kappa/2) + 3, i.e. iff kappa >= 3. This is exactly k >= 6.
- (c): 2m_lo <= k + 2 - kappa <= k - 2.
- [kappa, R - kappa] contains 2p - k + 1 integers, so steps of size <= 2p - k + 1 cannot jump over it.

The split |d_u| <= 2p - k + 1 versus |d_u| >= 2p - k + 2 = W + 1 is the exact integer complement.

BR verified:
- The c = 0 case gives A = a_u + n_pi <= kappa, hence 3k + j >= 4p + 4.
- With j <= 2p - k - 2 this gives k >= p + 3, hence c_lo >= 2.
- Case (2'): k = p + 1, and M_{c-1} = max(kappa, p - 3, 3) <= p - 1.
- Case (3): N_alpha - tau = k - 1 + eps - kappa >= tau.

**N2.**
- C3S:L19-21 is exactly NMH ∩ {R <= 2p - 3}. k <= 2p - 2 is automatic, since k <= R. k = p + 1 is included.
- Delta0 = 2p - R >= 3.
- k = 2kappa + Delta0 >= 2(B + 1) + 3 >= 7, which matches GC:L28.
- Hand example, p = 5: k <= R <= 7 forces k = R = 7, E = 0, kappa = 2, B = 1, A = 6.
- The scope of (GC) (GC:L109-110, L24-28) covers exactly the words to which T applies it.

### Q5 (verification status, in the requested order)

- C0-B' with dependencies (RUNS:L65-101, L173-339): FULLY verified, including Steps 3-4 at L224-243.
  - Step 1, case (d): S >= 2p - k + (R + r_t - 1)/2 >= p - 1, using R + r_t + 1 >= k + 2 >= 2k - 2p + 2.
  - Depth Lemma (F1), m1 case: <= 2R - 2p + 3 - r_t <= 2p - 2.
  - Depth Lemma (F1), m2 case: <= 3R - 4p + 4 <= 2p - 2.
  - Depth Lemma (F1), m = 1 case: <= 5 + R - k <= 2p - 1.
  - (A'), both-reflection case: forces 4m <= R + 2k - 4p - 2 + r_t < 4m2, a contradiction.
  - (B'): R - 1 >= p - 2.
  - Greedy: delta_P <= k - i* - 2 and Phi(P) <= k + r_t + 1 <= R + 2 <= 2p.
  - Slack only, not an error: RUNS:L203 asks for S >= p - 1 where S >= p - 2 suffices.
- FWH: fully verified.
- RL (OBL:L40-48): fully verified.
- K0 extension (RUNS:L383-389, K0:L92-147): fully verified.
- KBH, all steps including ZS: fully verified.
  - The r >= 2 bound: sum lo <= (A - 2(B - 1))/2 = (D - B + 2)/2 <= D.
- R2 and BR: fully verified.
- KB: fully verified.
  - Uncapped case: (a) gives p + (k~ + D_N)/2 >= p + 1/2; the s = 0..3 and capped subcases of (b) all check; so does (c).
  - Capped case: lambda({t_1}) = floor((r_1 + kappa)/2) + 1 once r_1 >= kappa + 1, and the step sums are p + i - kappa + 1 and 2p + i - kappa.
- S1' and A1': fully verified.
  - (K4): 4kappa - 5 <= p + 2kappa - 1 <= R - 1.
  - (K5): 4kappa + 1 <= 2R - 2kappa - 2, using k <= p.
- ALT and A1: fully verified.
- B0: fully verified.
- OR: fully verified.
- Lemma BC: fully verified.
- Lemma H: verified only partially.
  - Its formulas equal HW's g_P, since E+ = D_Q + B and h = p - 1 - kappa - beta.
  - The empty-pattern window and the criterion "0 ∈ I(empty) iff A, B >= kappa + 1 (given A, B <= 2p - 1)" were checked.
- Lemma HW: checked only at the C_max = 2m + 2h bookkeeping step (HWF:L31-33). WAS/GR themselves are not inlined.

### Q6 (Corollary B' and Remark (2))

**Corollary B'(b)** is correct with no inherited hypothesis and any k.
- Fact Z(iv) gives o_F >= kappa + 2, which supplies Theorem M's kappa <= k~ - 1.
- (a) is the all-odd case of (b).

**Remark (2)** is correct and correctly scoped to inherited avoiders.
- For every k, branches C1 and C3-C6 exclude everything except B = kappa = 0. For k <= p, C4 and C6 are vacuous.
- The inherited hypothesis is needed only in C3's capped case, through (D0), together with K0's (P) for k <= p.
- The type-(II) non-inherited avoiders (KBH:L111-113) show it cannot be dropped.

### Q7 (INV*)

**INV* stays separate.**
- Every statement in the target and in its imports concerns RGR words, through HW/H (HWF:L17-36).
- Nothing treats rho_0, a third rotation value, or a non-constant reflection run, so neither half of INV* is implied.
- OBL:L54-57 and invstar/results.md:L67-71 confirm that both halves are open.
- T is right not to claim OO(p).

**Use of DR-Res and DR'.**
- Corollary D establishes INV_Res for all inherited avoiders, so INVR:L45-48's order (RUNS on one in-run deletion, then PAR) is satisfied.
- Corollary E is correct.
- DR' (DR:L47-58) uses INV only through Theorem DR's conclusion, so OO(p) ⇐ INV*(p) + Corollary E, exactly as stated at T:L63-64 and T:L129.

### Q8 (overreach, circularity, finite premises)

- Overreach: none beyond m3 and m4.
- Circularity: none.
  - Theorem C uses Theorem M, whose proof (R4:L65-78: M0, S1', Lemma S, R4) does not use RUNS or PAR.
  - PAR's Theorem P is used only in Corollary D.
- Finite computation as a premise: none. Each [F] item shadows a written proof:
  - RUNS:L53-54 and L100;
  - K0:L45-46;
  - MH:L94-98;
  - C2F:L53-57 and L109-115;
  - KBH Sec. 5;
  - GC Sec. 5.

## Verification lists

**FULLY CHECKED (line by line, by hand):**
- T: Facts Z, T, K; Theorems A, B, C; Corollaries B', D, E; Non-conclusion F; the Sec. 5 table; the Appendix.
- RUNS: L23-101 (FW, ALT, zero certificate, TL, KW); L173-339 (S1 Steps 0-4, Split, Depth, C0-B, C0-B'); L348-389 (A1, cut, OR, B0, the kappa = 0 extension); L402-414 (M0).
- MH: L11-14 and L56-85 (FWH).
- C2F: L17-51 (R2), L61-107 (BR), L119-123 (FW+).
- KBH: L29-108.
- OBL: L40-48 (RL).
- KP: L24-42 (OR), L164-234 (S1', A1'), L238-295 (KB).
- K0: L52-53, L57-87 (BC), L94-147 (K0).
- K0:L18-44 (Lemma H), only as the algebraic image of HW.

**HYPOTHESIS-MATCHED ONLY:**
- (GC): GC Lemma GEN, Lemma GC, Theorem NMH-iii, and the chain behind them (SEEDG-r2 GS/NW/TS, A0-r1 Corollary/C0-all, C0W). Only the scope was matched.
- Theorems M and P (R4:L61-64, L84-94).
- Lemma GR and Lemma WAS (not inlined), with HW's derivation beyond HWF:L31-33.
- C3S Sec. 0, read as the definition of the NMH setting.
- Theorem DR-Res, whose proof relies on EGZ, the dihedral-partial "Theorem P", Davenport-alpha and Doubling (not inlined).
- Theorem DR and Corollary DR': read, and found consistent; not re-reviewed beyond that.

## Conclusion

**Strongest conclusion endorsed.** For every prime p >= 5, assume:
- (GC);
- the accepted Theorems M and P;
- Lemmas GR/WAS through HW;
- Theorem DR-Res.

Then all of the following hold:
- NMH(p), MIX_DEF_HIGH(p), MIX_DEF(p), Corollary B'(b), RUNS(p) and INV_Res(p).
- Every inherited avoider in RGR_(4p-2)(p) with F, R >= 1 normalises to B = kappa = 0, with k <= p and all runs odd.
- Every word of RGR_(4p-1)(p) has an identity 2p-subword.

Also, RUNS for B = 0 holds with no inherited hypothesis, since C1 and C2 use none.

**Still open:**
- The independent review of (GC).
- INV*(p), both halves, and hence OO(p) for p >= 5.
- Second-family confirmation of U2-U8. This review supplies the Claude side for the items listed as fully checked.
- p = 3, which is outside this scope.

**Correctness versus significance.** This note judges only correctness. Conditional on (GC), I found the assembly and the re-derived imports correct, with documentation fixes only. I make no claim about novelty, priority or significance, and none should be read in. In particular, the result is an inverse-structure statement for RGR words, not ordered Olson for D_(2p). Its value for that goal depends on INV*(p), which remains unproved.
