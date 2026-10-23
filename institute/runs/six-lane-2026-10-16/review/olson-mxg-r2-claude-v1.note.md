# Audit of Theorem MXG (30-proof-MXG-r2.md)

## DISPOSITION: ACCEPT-WITH-FIXES

**Finding counts:** 0 FATAL, 0 MAJOR, 6 MINOR. All six are wording, notation or scope issues. No mathematical step needs to change.

- **Theorem MXG:** correct as a written proof from Lemma H0 (which rests on GR0). I re-derived every step for G-words from the inline lines.
- **Corollary:** the logic is correct. It depends on Theorem B0S r3, which I did not audit. Only 21:L1-30 is visible, and r3 itself is unreviewed (21:L4-6).
- I had no tools, so no hashes or files were checked. This is an audit of the inline text only, and it carries no gate or parent-acceptance authority.

## Findings

**MINOR-1, 30:L29.** The claim "I(empty) excludes 0 iff min(A,B) ≤ κ" is false mod p when A ≥ 2p.
- In that case the lower end is −min(p, A−κ−1, ⌊A/2⌋) = −p, which is ≡ 0 mod p, even if B < κ.
- This is harmless: the trivial cut at 30:L62 removes such words, and I(∅) is used only for V_0 and V_k.
- Repair: add "for A, B ≤ 2p−1".

**MINOR-2, notation clash: 30:L15, L28, L62, L74 versus 00:L25, L32, L56.**
- The cited G-word definition uses g for the number of empty runs and β(P) for the number of even boundary blocks.
- MXG reuses g := κ−B and β := the number of anti defects with φ ≤ −1.
- Repair: add one line to Sec. 1 saying that n_E is the empty-run count and that β(P) = 0 throughout.

**MINOR-3, 30:L41 versus 30:L84-86.** The two "uses only" lists for Lemma S do not match.
- L41 omits B−κ−1 < 0, which 31:L39-43 needs for U_∅ = −g−1.
- Neither list states two facts the proof uses, both true here:
  - intervals made only of empty runs have mass 0, which lies in [−B, D+B];
  - singletons are proper intervals because k ≥ 4.
- Repair: make the two lists agree and add these facts.

**MINOR-4, 30:L142.** "R*_G is contained in MXL's R*" compares data from different word classes.
- MXL's R* (31:L134-139) is RGR data, which has pairs and no empty runs.
- What is true is that (R1) and (R2') imply MXL's (R1) and (R2).
- The remark is unused. Repair: reword it or delete it.

**MINOR-5, 30:L171-173 (SPLIT).** The formula m(U*) = |U'| + m(E) − a(U') needs the adjacency multigraph between U'-runs and E-blocks to have no double edges.
- A double edge would mean either a U'-run flanked on both sides by the same E-block, or a C'-block flanked on both sides by the same E-block.
- Either case forces C = [k], which the hypothesis excludes. The text's "(no cycle, as U* ≠ [k])" covers this only implicitly.
- Repair: add one sentence saying so.
- With C ≠ [k] I checked that the formula is exact, that the per-block values at L176-177 are right, and that the greedy balancing is right.

**MINOR-6, scope at 30:L1 and L19-22.** The Corollary should say two things:
- B0S r3 is itself unreviewed.
- It does not give REFL(p). Theorem RED (01:L134-135; its hypotheses (I1)-(I4) were not audited) needs "no avoider in RES_<(p) with κ ≥ 2" for every k, and the case k ≥ p+1 is still open. 30:L253 says this, but only in the Remarks.
- Repair: add one sentence to the Corollary.

**Notes (no fix needed):**
- The bound at 30:L130 can be sharpened to 4g: the previous prefix has Φ ≤ 2g and one step adds at most 2g.
- The hypothesis A ≥ B at 30:L17 is implied, since D = 2p−k+2g > 0.

## Per-question summary

### Q1: Import map

No import is used merely by renaming.

**Checked as genuinely verbatim:**
- **31:L23-64 (Lemma S).** It uses only these facts:
  - every set of runs has mass in [−B, A];
  - the H0 windows with β = 0;
  - 2g+B ≤ p−1 and D ≥ p+2g;
  - A ≤ 2p−1 (giving G̃(D) = (D+B−1)/2);
  - avoidance.

  I re-checked the vertex sets (−B, D, D+B) and (−B, 0, D+B).
- **31:L72-82 (Lemma K and its Corollary).**
- **32:L50-53 (Fact F).** GIANT supplies 2p−d ≥ 2.
- **32:L56 (run classes).** Like pairs, empty runs have even bh.
- **32:L65-72 (Lemma KL).** Empty runs have d = 0, so D_P ≥ −B still holds.
- **32:L77-90 (Lemma W).** An empty run with φ ≥ 0 has bh = −2φ ≤ 0, so it is cheap.
- **32:L101-105 (Lemma B1).** Empty runs add d = 0 to Σ_S d.
- **32:L195-203 (Lemmas ZP and C).**
- **33:L27-55 (Lemma R4).**
  - Pairs of Z0 are replaced by empty defects, which are free with d = 0.
  - The anti mass is B.
  - k ≥ 11 still holds, because s ≥ 1, B ≥ s+2 and g ≥ B.

**Every place where the RGR chain really used nonempty runs or pairs is replaced:**
- **31:L90-92 and 32:L47:** the argument "the other runs are all anti" fails because they may be empty. GIANT replaces it.
- **32:L95-96 (a' ≥ 1):** replaced by W(R') ≥ 2g + s + a', where s + a' = 2p−1−d_T ≥ 1.
- **31:L106 (L_Z ≤ 2B):** replaced by L_Z ≤ 2B_Z + n_EZ, paid for by δ ≥ 2n_EZ.
- **32:L126-128:** these lines assume B_Y ≥ 1 when T is not aligned, which is false for an empty T. This, together with 32:L165-168 and 32:L174, is replaced by (R2') plus SPLIT. The re-derivation was necessary, not cosmetic.

### Q2: The new lemmas

**GIANT**
- If d_T ≥ 2p−1 then a_T = A = 2p−1, so s = 0 and n_E ≥ 2g.
- For each empty run t, L_t = G_1(D) = min(p−1, 2p−1−B−g, p−1) = p−1, so x_t ∈ [1−g, 0] with x_t ≠ 0.
- If g = 1 this is already a contradiction.
- Otherwise take S = the empty runs. Then c(S) ≥ 2g+1 and BH(S) ≤ −4g < B, and KL applies. ✓

**Φ′, G′, AV′**
- j = (2−a_Z−exc−2m)/2 is an integer because Φ = 2c.
- j ≤ L_Z/2 ≤ B_Z + n_EZ/2.
- Every prefix has BH ≤ max(0, B_Z − 3n_EZ/2) ≤ B.
- Each step raises Φ by at most 2φ_t + 2 ≤ 2g.
- The available fillers number at least (|Y| − 2m − exc − |Y_anti|)/2. This is ≥ j exactly when |Y_al| + |Y_E| + a_Z ≥ 2.
- Lowering the threshold from 3 (31:L125) to 2 is legitimate because Δ is even. ✓

**SPLIT**
- Each C'-block offers two class values that differ by at most 1.
- The total is at least |C'| − 2m(E).
- So min c ≥ (|C|+|E|−1)/2, and by integrality min c ≥ ⌊(|C|+|E|)/2⌋.
- The edge cases E = ∅ and C' = ∅ both work.
- BH(U*) + BH(V*) = BH(C) + BH(E) ≤ BH(C) − 2|E|. ✓

**Boundary cases**
- **k = p:**
  - Lemma S's endpoint bound (D−1)/2 − g ≥ g follows from p ≥ 2g+1.
  - In Lemma C, φ_t0 ≤ g.
  - In R4′(b), φ(N) ≥ g + |N| ≥ g+2. ✓
- **B = 1:**
  - Lemma W never applies (it would need g ≤ 0).
  - Lemma B1 is vacuous after GIANT.
  - The second branch of AC′ is exactly B = 1, s = 0, n_EZ = 0.
  - R4′(iii) forces B ≥ 3, so R4_G is empty and R4′ holds vacuously. ✓
- **B = κ−1 (g = 1):**
  - x_t ≥ 0 for every empty run, so there are no empty defects (n_EZ = 0) and SPLIT reduces to the alternating split.
  - Empty runs are Y-blockers with bh ≥ 2. ✓
- **p = 5:**
  - The only cases are (g, B) ∈ {(1,1), (1,2)}.
  - (1,2) is handled by Lemma W.
  - For (1,1), after A′ every bh ≤ 1, so no empty run survives. R4_G is then empty because R4′ would need B ≥ 3. ✓

### Q3: A′, KS′, AC′ and the R4 assembly

- **A′:** #cheap ≥ 2g + s + 2m + S_Z + (bh_T − 1 − B_Z) − n_EZ ≥ 2g+2−n_EZ. The BH sum is ≤ 1 + 2B_Z − 3n_EZ ≤ 2B+1. This works uniformly whether T is aligned, anti or empty.
- **KS′:** #cheap ≥ 4g + s + 1 + S_Z − α − 2φ(Z0⁺) − n_EZ, with the same BH bound.
- **AC′:** s ≤ B + n_EZ.
  - First branch: the BH sum is ≤ B + s − 2n_EZ ≤ 2B − n_EZ.
  - Second branch: k = 2g+2 with no empty runs.
- **R4′:** δ⁺ ≥ g+s+1 and BH(Y) ≥ 3s+g+4. Empty runs of Y in N have φ ≤ −1, which only pushes toward branch (a).
- **Elimination chain:** each lemma's negation is exactly the next conjunct of R4_G (30:L224-225).
  - The precondition for Lemma C (all φ ≤ g−1) follows from F′(d) and F′(c).
  - It is correct to drop M0, S1′ and G1: runs are pure, B = 0 goes to B0S, and g ≥ s+2 ≥ 3 comes out of R4′ itself.
- **Conclusion:** the final contradiction holds for all p ≥ 5, k ≤ p, B ≥ 1, g ≥ 1 and any number of empty runs n_E ≥ 0.

### Q4: Assumptions, circularity, finite premises, scope

- **Assumptions:** F, R ≥ 1 come from the G-word definition (00:L19-20). The standing assumption that w avoids is stated (30:L65-67). The fact that p is prime is used only to make 2 invertible.
- **Circularity:** none.
  - Dependency chain: GR0 → H0 → MXG.
  - B0S is used only for the Corollary, and RED only for the definition of RES_<(p).
  - Theorem M's statement (34) is never used.
- **Finite premises:** none. The replay at 30:L253-254 is an aid only. No census from 32 §7 or 33 §4 is used.
- **Scope:** correctly limited to rotations ρ_{±1}, odd blocks, pure-or-empty runs and k ≤ p (see MINOR-6).

## What I audited versus what I took as imports

**Fully audited:**
- All of 30 Secs. 1-8.
- The imported proofs 31:L21-82, 32:L43-105, 32:L195-203 and 33:L27-55, checked for G-words.
- The H0 algebra (00:L55-65), given GR0: c = H+m−β, E⁺ = D_P+B, and λ(P)−1 = G_m(D_P) when β = 0.

**Taken as imports:**
- GR0 (00:L40-54, the parent-accepted GRX).
- Theorem B0S r3, not audited.
- The definition of RES_<(p) (01:L132-133).
- RED's hypotheses (I1)-(I4), not seen.

## Unresolved core

- Avoiders in RES_<(p) with k ≥ p+1, for both B = 0 and B ≥ 1, are not ruled out. So **REFL(p) is not established**.
- INV*(p), the RUNS(p) residual and ordered Olson for D₂ₚ remain open.
- Nothing here endorses any of them.
