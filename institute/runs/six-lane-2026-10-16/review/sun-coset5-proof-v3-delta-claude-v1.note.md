# Delta audit: Sun k = 5, proof-v1 → proof-v3

## Verdict: **ACCEPT-WITH-FIXES** (proof-v3 as text of record)

- **FATAL:** none. **MAJOR:** none.
- The new §2 proof of M-S Prop 4.5 is correct line by line, including the F-2 patch.
- Every listed fix is present in substance.
- The required repairs are all textual:
  - two inverted statements of Lemma K's pair condition;
  - three places where v3 is less complete than v1;
  - two unaudited claims about the code.

## 1. §2 re-derived against SOURCE10 (sizes in units of |G|)

- **(a) SOURCE00:63 ✓.** r_1 is odd and coprime to the others, so gcd(2r_1, 4r_i) = 2. By L0.3 (SOURCE05:40), α = 1 and |U_1U_i| = 1/2. This is M-S Lemma 4.1 (SOURCE10:396–406).
- **(b) SOURCE00:64–67 ✓ (math).**
  - lcm(2r_1, 8r_2r_3) = 8r_1r_2r_3, so |U_1(U_2∩U_3)| = T/(16r_1r_2r_3) ≥ 1/2. Hence U_1U_2 = U_1U_3.
  - Inverting gives U_2U_1 = U_3U_1. That is L3's first alternative at v = 2, S = {1,3}; the sum is 1/2 + 1/2 = 1.
  - This matches SOURCE10:473–484, where Cor 3.6 is applied with (U,V,W) = (U_2,U_1,U_3).
  - The text states the condition un-inverted; see m1.
- **(c) SOURCE00:68–73 ✓.**
  - lcm(2r_1, 4r_2, 4r_3) = 4r_1r_2r_3. Then 12r_2r_3 | 4r_1r_2r_3τ ⟺ 3 | r_1τ.
  - With [G:U_1∩U_3] = 4r_1r_3: |U_2(U_1∩U_3)| = T/(4r_2·4r_1r_3) = τ/4 ≤ |U_2U_1| = 1/2. So τ ∈ {1,2}, and therefore 3 | r_1.
  - This correctly replaces SOURCE10:485. Lemma 3.10 needs a common a with pairwise coprime cofactors (SOURCE10:359–360), and (2r_1, 4r_2, 4r_3) admits none.
  - L0.5 is the correct left-factor mirror of M-S 3.4(2). M-S applies its 3.4(2) (SOURCE10:277) to U_2U_1∩U_2U_3 without comment.
  - The double-coset unit is 1/gcd(4r_2, 4r_1r_3) = 1/4, so the size is 1/4 or 1/2.
  - Size 1/2 would give U_2U_1 ⊆ U_2U_3, whose inverse U_1U_2 ⊆ U_3U_2 is L3's condition at v = 1; the sum is 1/2 + 1/2 = 1. So the size is 1/4, and τ = 1, matching M-S's "α = 1" (SOURCE10:490).
- **(d) SOURCE00:74–78 ✓ (math).**
  - T2 gives τ ≤ α_24α_34 = 1. By T3, |U_2(U_4∩U_3)| = 1/4 = |U_2U_4|, so U_2U_4 ⊆ U_2U_3.
  - In {1,2,4}: |U_1(U_4∩U_2)| = T/(8r_1r_2r_4) ≥ 1/2, so U_1U_4 ⊆ U_1U_2. Likewise U_1U_4 ⊆ U_1U_3.
  - Inverting gives U_4U_1 ⊆ U_2U_1, U_4U_1 ⊆ U_3U_1 and U_4U_2 ⊆ U_3U_2. That is L3 at v = 4, S = {1,2,3}; the sum is 1/2 + 1/4 + 1/4 = 1.
  - This is the Prop 3.8 instance a = 4, a_1 = 2, Σ1/a_i = 1, gcd(2, r_1) = 1 (SOURCE10:332–352). M-S reaches the same inclusions at SOURCE10:346.
  - The text states the condition un-inverted; see m1.
- **(e) SOURCE00:79–81 ✓.**
  - α(i,j) ∈ {1,2,3} by L0.3 (left implicit). (b) removes 2, and (d) forces some α = 3.
  - If α_24 = α_34 = 1, then τ ≤ 1, so 12r_2r_3 | 4r_2r_3r_4 and 3 | r_4. That contradicts 3 | r_1.
  - This route differs from M-S's Prop 3.8 route (SOURCE10:501–502) but is valid. The 2↔3 swap preserves α_23.
- **(f) SOURCE00:82–85 ✓ (the α(3,4) = 1 subcase).**
  - 3 | r_4τ and 3 ∤ r_4, so 3 | τ.
  - T3 at apex 3: τ/(4α_24) = τ/12 ≥ 1/4 = |U_3U_4|. So U_3U_4 ⊆ U_3U_2, whose inverse U_4U_3 ⊆ U_2U_3 is L3's second alternative at v = 4; 3/4 + 1/4 = 1.
  - This matches SOURCE10:502–504, with Cor 3.6 applied as (U_4,U_3,U_2). α_34 = 2 is excluded by (b), which is left implicit.
- **(g) SOURCE00:86–94 ✓ (final count).**
  - Applying (c) to (2,3) and (2,4) gives unions of size 1/2 + 3/4 − 1/4 = 1. This makes explicit M-S's "same type of arguments" (SOURCE10:518–519).
  - gcd(4r_2, 12r_3r_4) = 4·gcd(r_2, 3) = 4. This is F-8, against SOURCE10:508.
  - The intersection has size ≥ 1/2. Size 3/4 would give U_2U_3 = U_2U_4, and L3 at v = 3, S = {2,4} gives 3/2. So the size is 1/2, and U_2U_3 ∪ U_2U_4 = G.
  - Lemma 3.1 (SOURCE10:254–257) gives 1/2 − 1/4 − 1/4 = 0, yet U_2 ⊆ R∩S∩T. The inline re-proof (SOURCE00:94) is correct and does not need properness.

Every Lemma K use is at the right vertex and set, and each is exactly K2 (SOURCE05:130–132), whose proof performs the inversion:

| step | K2 instance (v, j, k) |
|---|---|
| (b) | (1, 2, 3) |
| (c) | (2, 1, 3) |
| (f) | (3, 4, 2) |
| (g) | (2, 3, 4) |

## 2. Findings (all MINOR) and repairs

**Required before v3 is the text of record:**

- **m1. Orientation (SOURCE00:67, :77).** "The pair condition U_1U_2 ⊆ U_1U_3 holds" and "in the form 'U_iU_4 ⊆ U_iU_j'" are the *inverses* of L3's condition U_vU_i ⊆ U_jU_i (SOURCE05:114).
  - Repair: write "inverting gives U_2U_1 = U_3U_1 (L3, first alternative)" and "inverting gives U_4U_i ⊆ U_jU_i". Alternatively, cite K2 with the tuples in the table above.
- **m2. Lemma R proofs are not in v3 (SOURCE00:159).** The text says "As in proof-v2".
  - proof-v2 is not in the supplied record and was out of scope for the parent audit (SOURCE09:5, :312).
  - The audited v1 proofs contain the defective R5 step.
  - So the text of record holds no audited proof of an essential [NEW] lemma.
  - Repair: inline R1–R3 from SOURCE02:43–48 and R5′ from SOURCE06:149–152, and note that (R4) is deleted as unused.
- **m3. A hypothesis was dropped (SOURCE00:151).** v1's Setting began "Harmonic configuration (rules-v1 §0)" (SOURCE02:33). Read literally without it, (R1) and (R5) are false for overlapping cosets.
  - Repair: "Assume g_1U_1, …, g_5U_5 are pairwise disjoint (F-9)."
- **m4. Connecting steps and justifications were dropped.**
  - v3 has no counterpart to v1's "Each certificate shows that no Core(5) configuration with that pattern exists; L8 (M1, M2)…" (SOURCE02:23).
  - It also has no counterpart to the theorem closure "Hence no counterexample exists. ∎" (SOURCE02:29).
  - The S-D steps at SOURCE00:163, :165 and :167 lost derivations present at SOURCE02:61–62, :66–73 and :82:
    - R1/R2 forcing D_j = Y_j;
    - T1/T2 giving τ_023 = 2;
    - the T3 sizes;
    - gcd(q_0r_0, r_j) = gcd(q_0, r_j).
  - Repair: restore these lines, with the q rename and the q_0 = 1 route.
- **m6. Unaudited or inconsistent claims about the code (not load-bearing).**
  - SOURCE00:135 says `r_FH2` in check v2 "implements exactly this". No supplied review read check_v2 (SOURCE09:5, :315). The engine half is independently confirmed (SOURCE08:33; SOURCE09:97, :161, :182, :194).
  - SOURCE00:139 says check_v2 finds "0 survivors among all 2,125,764". SOURCE09:149–150, however, says that labelled counts including **SURVIVE 60** "equal the worker's core5_check_v2 counts". The two agree only if check_v2 encodes Lemma R.
  - Repair: label the check-v2 claims as lane self-report, and state exactly how check_v2 classifies the 60 S-D triples.

**Recommended:**

- **m5. Stale label (SOURCE00:96).** "R1(⇒)" is undefined after v3 relabelled the two directions (SOURCE00:45, :47), which is the same confusion F-6 fixed.
  - Repair: write "the Core(5) ⇒ Sun(5) direction".
  - Also, the fix map (SOURCE00:22) says "Added in §3", but the sentence is at the end of §2.
- **m7. Stale status (SOURCE00:141, :189; SOURCE04:38).** These say the parent replay is pending, but the bridge replay is PASS (SOURCE09:22, :200–202).
  - Repair: cite the verifier `2d7fff78…7659` and RESULT `d741396c…7278`, and keep "gate not claimed".
- **m8. Wording.**
  - SOURCE00:1 and :7 say "a public written proof". Add "candidate", to match SOURCE00:5 and SOURCE04:16 ("if it is verified").
  - "[NEW]" (SOURCE00:149, :180) is undefined in v3. Gloss it as "written in this lane; no novelty claim".
  - SOURCE04:12: append "(search miss, not a novelty claim)".
  - Write "Z. Gong" to avoid conflation with Zhu (2008), Thm 1.1.
- **m9. Nits.**
  - Cite L0.3 for α ≤ 3 at SOURCE00:79, and (b) for α_34 ≠ 2 at :82.
  - Cite L0.5 + L0.4 at :88.
  - At :90, rename R, S, T; they clash with K's set S and the triple index T.
  - At :169, the q_0 = 2 route is proof-v1's (SOURCE02:86–87).
  - "Self-contained" (SOURCE00:26, :41; SOURCE03:25) should read "self-contained modulo rules-v1 L0.3–L0.5 and L1–L3".
  - SOURCE00:175 says "imported as statements… re-proved", which contradicts itself.
- **m10. Outside the listed set.** The Cor 3.11 linking-vertex correction (SOURCE07:9–15; SOURCE09:245) appears in neither the v3 fix map nor SOURCE03. It may be in erratum-v1, which was not supplied. It is not load-bearing.

## 3. Fix-by-fix check

- **F-1.** R5′ is stated correctly (SOURCE00:157, :159, which match SOURCE06:149–152) and used correctly (SOURCE00:164, :167). Orientation (right U_v-cosets, then inversion to left cosets) is consistent with SOURCE02:45–51. The proof text itself is missing (m2).
- **F-2.** ✓ SOURCE00:69–71 matches SOURCE06:157–161 and SOURCE09:234–238. The defect description at SOURCE03:23 is accurate.
- **F-3.** ✓ in substance (SOURCE00:47, :55, :100); label issue in m5.
- **F-4.** ✓ SOURCE00:123–134 matches SOURCE06:222–231. That includes no forced separation of a and b in case (ii), and no coverage or balance constraint. The check-v2 half of SOURCE00:135 is covered by m6.
- **F-7.** ✓ SOURCE00:24, :51, :53, :102, :174. No citation of Zhu Thm 2.2 or 3.1 remains.
- **F-8.** ✓ SOURCE00:88.
- **F-9.** ✓ SOURCE00:26 matches SOURCE06:189–191.
- **F-10.** ✓ q_j is renamed throughout. E5 (SOURCE03:15) is correct for α = 1. The finite-index justification for the cores is at SOURCE00:37.
- **F-5 / F-6.** F-6 ✓. v3 does not repeat the false misprint claim.
- **Codex MAJOR (C4 wording).** ✓ SOURCE00:28, :138–139 match SOURCE08:5–7.
- **Codex MINOR.** ✓ SOURCE00:29, :140 and SOURCE03:42–51 match SOURCE08:9, :11.

## 4. Did anything else change?

- **Theorem and Core(5):** identical (SOURCE00:33 = SOURCE02:11; SOURCE00:43 = SOURCE02:16).
- **Prop 4.5 statement (SOURCE00:59):** same as SOURCE10:494–495, but extended from finite groups (SOURCE10:252) to all groups via R0. That is stronger, not weaker.
- **§3 framing:** "Suppose Sun(5) fails" (SOURCE00:100) replaces "Suppose Core(5) fails" (SOURCE02:18). This change *is* the F-3 correction.
- **Lemma R:**
  - the (R1) and (R5) conclusions are unchanged;
  - the bound in (R2) was moved from SOURCE02:55;
  - (R3) is less explicit but suffices for R5′;
  - (R4) is deleted, as unused after F-1;
  - the only defect is m3.
- **S-D:** the pattern at SOURCE00:146–147 is equivalent to SOURCE02:25–28. The new q_0 = 1 endgame is valid (SOURCE06:141).
- **§4:** the certificate semantics are new descriptive text consistent with SOURCE05 and SOURCE06 §3. No rule changed (SOURCE03:5).
- **No new hypothesis, no weakened quantifier.** K still requires every pair, T2 still applies at all apexes, and FH2 still requires every assignment rejected in both cases.
- **Losses are textual only:** m3 and m4, plus cosmetic deletions (per-rule counts, the FH1 note, run metadata).

## 5. Priority wording: PASS

- SOURCE00:6–8 and :191 say there is a prior unpublished claim, as reported by Sun. The sources are MO Q316709 (2010) and the 2024 slides, slide 38 (2009), matching SOURCE04:9–10.
- "First" and "novel" appear only in negated form (SOURCE00:8).
- Wording nits are in m8.

## 6. Audited versus imported

- **Audited here:**
  - §2 steps (a)–(g) and the Lemma 3.1 re-proof, against SOURCE10;
  - v3's R0 and R1 text;
  - L3 and K2 as used;
  - the Lemma R statements, R5′ as described, and both S-D endgames;
  - every fix-map row, against SOURCE06–09;
  - erratum-v2 E5–E7, against SOURCE05;
  - the priority wording.
- **Relied on, not re-derived:**
  - rules-v1 L0.1–L0.6 and L1–L8 (T, N2, F/H2, M1/M2), which were audited in SOURCE06/07/09 and are unchanged per SOURCE03:5;
  - the finite bridge (parent PASS, SOURCE09:22), not re-run here.
- **Imported as a statement:** Zhu Theorem 1.1 (k = 3, 4).
- **Unavailable, so not audited:**
  - proof-v2 (the Lemma R proof text);
  - erratum-v1 and README-addendum-v2;
  - the check_v2 code and its summary;
  - the priority record and the freeze file.
  - The SHA-256 values were taken as given, not recomputed.
