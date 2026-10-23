# Hostile delta review: proof-ROT-half-v2 (SOURCE00) against the accepted v1 (SOURCE02)

**Basis.** This is a written derivation only. Nothing was computed and hashes were not recomputed. The finite aids (SOURCE00:210-212, SOURCE03:47) were not used. The diff in SOURCE01 agrees with both texts. Its mathematical changes are:
- the hypothesis (G) and its consequences G1–G5;
- the closing inequality of Step 5 and the wrap case of Step 6;
- the (G) check and the (H) bound in ROT-ZS;
- the new ROT-HALF derivation;
- the two-branch deletion ledger in OLSON-ZS;
- Sec. 5.

Imports are taken as their accepted statements; for those I checked only that the hypotheses hold.

## Dispositions

| Claim | Disposition | FATAL/MAJOR/MINOR |
|---|---|---|
| Generalized Lemma ZS (SOURCE00:37-123) | **ACCEPT-WITH-FIXES** | 0/0/3 (Z1–Z3) |
| ROT-ZS and INV*-ZS (:149-169, :178-181) | **ACCEPT-WITH-FIXES** | 0/0/4 (R1–R4) |
| HALF deduction (:171-174, :179, :185) | **ACCEPT-WITH-FIXES** | 0/0/1 (H1) |
| OLSON-ZS (:183-196) | **ACCEPT-WITH-FIXES** | 0/0/1 (O1) |

There are three further scope MINORs (S1–S3); none of them affects a theorem. There is no FATAL or MAJOR finding: every implication holds within its stated range.

No step silently keeps v1's assumption k ≤ (p+1)/2. Each v1 use now has a new source:

| Use in v1 | Source in v2 |
|---|---|
| Step 1 | G1 |
| MULT | G2 |
| (C1) | G3 |
| Step 5 | G5 |
| (C4), Steps 6–7 | G4 |
| SHgen (H) | κ ≤ p−k |
| SHgen (K) | 3k ≤ 2p+1 |

## 1. Lemma ZS under (G)

**The consequences G1–G5 of (G).**
- G1: a minimum is at most an average, so κ ≤ (p−1)/2 and 4κ ≤ 2p−2.
- G2 is 3k ≤ 2p+1 itself. Through MULT it is the binding constraint.
- G3: (2p+1)/3 ≤ p−2 iff p ≥ 7. At p = 5, 3k ≤ 11 gives k ≤ 3 = p−2.
- G4 and G5 are immediate.
- For k ≤ (p+1)/2, (G) is exactly v1's hypothesis (:45).

**Steps 1–4.**
- **Step 1.** The prefix before the crossing factor has even length ≤ 2κ. So the crossing zero-sum has length in [2κ+2, 4κ] ⊆ [2κ+2, 2p−2]. If κ = 0, Y is zero-sum-free.
- **Step 2.** e = k−1−2κ+|Z| lies in [0, k−1]; the lower end comes from (D).
- **MULT prerequisites** (SOURCE06:63-68).
  - Y′ is zero-sum-free and odd, and 3e+2 ≤ 3k−1 ≤ 2p.
  - So m ≥ max(2, e+1), e′ ≤ e, and m ≥ 2p−1−2e ≥ 2p−2k+1.
- **COMP.** d_j ≤ e′+1 ≤ e+1 ≤ m.
- **(C1).** d_j ≤ k ≤ p−2, so the integer weights are the signed representatives.
- **(C4).** 2p−2k+1 ≥ k−1 iff 3k ≤ 2p+2.
- **The element (1,0).** It is excluded from Y′ by (C1). It is excluded from Z by Step 5 applied to a singleton, since τ = p lies in [k, 2p−k]. ✓

**Step 5.**
- τ(U) and τ(U^c) = 2p−τ(U) both lie in [k, 2p−k] ⊆ [1, W′] by (C2).
- The two inequalities are obtained separately. Their completions may overlap; only the numbers are added.
- Substituting e′ ≤ k−1−2κ+|Z| gives exactly |Z| ≥ 2p−2k+2.
- G5 gives |Z| ≤ 2κ ≤ 2p−2k, a gap of 2. This is the only use of κ ≤ p−k. ✓

**Step 6 (revised).**
- A singleton U gives |b| ≤ k−1, which needs only k−1 < p.
- The first crossing satisfies k ≤ S_j ≤ 2k−2, and this can exceed p (p = 13, k = 9 gives 16).
- Then |rep(S_j)| ≥ min(k, 2p−2k+2) ≥ k by G4. Equivalently, τ = 2p−S_j lies in [2p−2k+2, 2p−k] ⊆ [k, 2p−k].
- For Z−, τ = T_j lies in [k, 2k−2] ⊆ [k, 2p−k], again by G4. So "Likewise" is valid; the case T_j = p, with representative +p, is harmless.
- |s(Z)| ≤ k−1 < 2p forces σ₊ = σ₋. ✓ See Z2 for the citation problem.

**Steps 7–9.**
- **Step 7.** If 2p−σ ≤ W′, then 2p+1 ≤ σ+k+|Z₋| ≤ 2σ+k ≤ 3k−2 ≤ 2p, which is impossible. The integer decrement gives W′ ≤ 2p−1−σ.
- **Step 8.** σ ≤ k−1 ≤ m, so Q = g^σ works. If σ = 0, then Z₋ = ∅.
- **Step 9.** cost = e′+2σ−|Z₊| ≤ e+σ−|Z₊| = k−1−2κ+|Z₋|+σ ≤ k−1. Also N = |Z₋| and cost = E+N. ✓

**Endpoints.**
- k = 1 forces κ = 0 and Y = g^{2p−1}.
- κ = 0 gives Z = ∅ and cost = e′.
- 3k = 2p+1 (p ≡ 1 mod 3):
  - MULT at 3e+2 = 2p still gives m ≥ e+1 = k.
  - At p = 13, k = 9, κ ≤ 4: Step 5 compares 10 with 8, Step 6 has 2p−2k+2 = k+1, and Step 7 has 3k−2 = 2p−1.
- At p = 7, k = 5, G3 and (C1) hold with equality.
- At p = 5 the lemma is identical to v1.

**Remarks (1) and (3).**
- Remark (1) correctly needs k ≤ (p+1)/2, and g does minimize the cost there.
- The example in Remark (3) is correct. It also satisfies (V), since R+H = 3p−2.

## 2. ROT-ZS and INV*-ZS

- **Normal form** (SOURCE08:30-43).
  - Length and rotation multiset are preserved, so F = |w|−R is preserved. PM* preserves F explicitly (SOURCE07:25-27), and fusions only re-read blocks.
  - k ≤ o and k ≡ o (mod 2) (SOURCE08:37).
- **The terminal κ.** κ_terminal = p−1−(F−k)/2 = κ(w)−(o−k)/2, a shift by a nonnegative integer. ✓
- **(G) at the terminal word.**
  - k ≥ 2.
  - 3k ≤ 3o ≤ 2p+1.
  - κ ≥ 0 (see R1).
  - κ ≤ k−1 by DAV (SOURCE08:42-43).
  - κ ≤ p−o−(o−k)/2 = p−k−3(o−k)/2 ≤ p−k. ✓
- **Weights.** g = Y(c) with c ≠ 0. The bound |b| ≤ k ≤ p−2 identifies b with b_x and rules out ρ₀.
- **(H).** 2H ≥ 2k−2 ≥ k−1 ≥ E.
- **(K).** η ≤ (k−1)/2 and a_max ≤ k reduce (K) to 5k ≤ 4p−1. This follows from 3k ≤ 2p+1 for p ≥ 4: 25 ≤ 27 at p = 7 and 45 ≤ 51 at p = 13. The old bound 5k ≤ 2p+4 is never used. ✓
- **SHgen-E.**
  - Expansions keep k, the block values and the empty runs (SOURCE08:52-59).
  - So every base word has length 4p−2, rotations in one nonzero pair, and o_F = k ≤ (2p+1)/3 ≤ p.
  - Hence conditions (0), (a), (b), (d) of REFL-few-odd hold at every induction level. ✓
- **INV*-ZS.** Restricted REFL is applied afresh to the original w, with o_F(w) ≤ (2p+1)/3 ≤ p. Nothing is lifted backwards through PM*. ✓

## 3. HALF deduction

Take an avoider whose normal form has k ≥ 2. Applying (V) to that normal form gives κ(w) = κ+(o−k)/2 ≤ (k−1)+(o−k)/2 ≤ o−1.

Then o−1 ≤ p−o iff o ≤ (p+1)/2, and 3o ≤ (3p+3)/2 ≤ 2p+1. So HALF needs no added F hypothesis, and (V) is applied to the avoider's own normal form. The resulting statements coincide with the accepted SOURCE03:10-12.

The only gap is the k = 1 branch (H1).

## 4. OLSON-ZS

I re-derived this from SOURCE10:28-47, because the cited ledger is absent (O1).

- **Case 1.**
  - There is no INV* call.
  - (F−o)/2 ≥ (4p−3−o)/2 ≥ p, because o ≤ (2p+1)/3 ≤ 2p−3.
  - The frame starts at a rotation or at a value change, so the chosen pairs are adjacent.
  - The selection is conjugated back to the original order (SOURCE12:49, :59). ✓
- **Case 2 (odd-block deletion).** (o, F) becomes (o−1, F−1), and F−1 ≥ 3o−3 = 3o′. ✓
- **Case 3 (rotation deletion).** (o, F) becomes (o or o−2, F).
  - A run can empty only if other runs remain, since R ≥ 3.
  - By maximality at most one fusion occurs. Odd+odd gives even; every other fusion keeps the odd count.
  - So F ≥ 3o−2 ≥ 3o_i−2. ✓
- **No even-block deletion occurs.** It would give (o+1, F−1), which the hypothesis does not control. ✓
- **Low branch (o ≤ (p+1)/2).**
  - Each deletion word is an avoider of length 4p−2 with o′ ≤ (p+1)/2, so INV*-HALF applies.
  - Its F condition comes from (V) applied to that word, not from w. ✓
- **Reconstruction.**
  - In Case 2, the deleted letter goes back inside a constant block.
  - In Case 3, a third rotation identifies the two pairs, x₁ lies in w₂ and x₂ in w₁, and unequal adjacent reflections stay adjacent.
  - RGR-LONG(p) is stated in increasing original index order (SOURCE12:7). ✓

## 5. Findings (all MINOR) and required wording

**Z1 — SOURCE00:10, :7.**
- **Problem.**
  - "complete in-file proof" repeats wording that overlay 1 corrected (SOURCE03:38).
  - "The proof steps are the v1 steps" hides the new justifications in Steps 5 and 6.
- **Repair.**
  - Write: "complete modulo the imported Lemma MULT (i)–(iii) (SOURCE06:61-81) and (D); same nine-step structure, with new justifications in Step 5 (G5) and Step 6 (wrap case, G4)."
  - Optionally add: "If κ = 0, Y is zero-sum-free and Z = ∅; an inclusion-maximal Z suffices."

**Z2 — SOURCE00:102-104.**
- **Problem.**
  - Step 6 derives its contradiction from Step 5 in representative form.
  - v2 deleted the sentence giving that form (SOURCE01:120; SOURCE02:71), so Step 5 (:91) is now stated only through τ.
- **Repair.** Replace the representative sentence with: "Then τ({y₁,…,y_j}) = 2p−S_j ∈ [2p−2k+2, 2p−k] ⊆ [k, 2p−k] by (G4), contrary to Step 5. For Z₋, τ = T_j ∈ [k, 2k−2] ⊆ [k, 2p−k]."
- Alternatively, restore at :91: "Equivalently (k−1 < p), rep(s(U)) ∈ [−(k−1), k−1]."

**Z3 — SOURCE00:138-139, :144, :208.**
- **Problem.** These three phrases carry over v1 wording already flagged (SOURCE03:43; SOURCE04:89-91; SOURCE05:164-167):
  - "the lemma's conclusion itself fails at k = p";
  - "near k = p a proof must use…";
  - "(ZP)-only route cannot reach o_F = p".
- **Repair.** Replace them with:
  > The cost conclusion does not extend to the single pair (k, κ) = (p, p−1), which lies outside (G). There it follows neither from (ZP) nor from (ZP) and (V) together: Y = g^{2p−1}(3g)^{p−1} satisfies both. No obstruction is shown for any k < p. No group word realizing Y and no ordered-Olson counterexample is supplied. Additional avoidance information, for example nonconstant-sign GRX patterns, is one possible way forward.
- Keep :145, adding "by this route".

**R1 — SOURCE00:156, :20.**
- **Problem.** κ ≥ 0 is cited to the SHgen setting, which assumes nonempty runs (SOURCE07:22-24, :37). The normal form ŵ may have empty runs.
- **Repair.** Insert overlay 2 (SOURCE03:39): "If H ≥ p, GRX's all-plus pattern with m = 0 is already an identity selection. GRX holds for ŵ's representation with genuine empty runs (SOURCE08:23)."

**R2 — SOURCE00:159-161.**
- **Problem.** The SHgen weight is identified before |b| ≤ p−2 is stated (overlay 4, SOURCE03:41).
- **Repair.** State it in this order: "By Lemma ZS every |b| ≤ k ≤ p−2. Since b is odd with 0 < |b| < p and c ≢ 0, x = bc ≢ 0, so no rotation is ρ₀. And b is the unique odd integer in [−(p−2), p−2] with x ≡ bc, that is, b_x (SOURCE07:39-41)."

**R3 — SOURCE00:14-19, :152, :166-168.**
- **Problem.** Overlay 3 (SOURCE03:40) is missing.
- **Repair.** Add: "The normal form, DAV and SHgen-E are used at their own displayed hypotheses (SOURCE03:34). Their earlier 5o ≤ 2p+4 chain imposes no bound on k. SHgen-E's caller obligations (SOURCE09:134-138; SOURCE11:16) are discharged: k is unchanged along every expansion, and each base word has length 4p−2, one nonzero rotation pair, and o_F = k ≤ (2p+1)/3 ≤ p."

**R4 — SOURCE00:32, :178.**
- **Problem.** The definition of o_F omits "cyclic", and INV* is no longer defined: v2 dropped v1's definition (SOURCE02:141-142).
- **Repair.**
  - At :32: "o_F counts the odd blocks of the maximal cyclic constant reflection-block decomposition, not reflection runs (SOURCE03:8; SOURCE09:19-22)."
  - At :178, restore: "INV*: all rotations lie in one {ρ_c, ρ_−c}, c ≠ 0, and every maximal cyclic reflection run is constant."

**H1 — SOURCE00:173.**
- **Problem.** "With k and κ as above" covers only k ≥ 2, because κ and DAV are set up only there (:155; SOURCE08:42-43). For a normal form with k = 1, F ≥ 3o−2 is never verified, yet Theorem ROT-ZS formally assumes it.
- **Repair.** "If the normal form has k = 1, Proposition K1 gives the conclusion as in ROT-ZS. If k ≥ 2, then κ ≤ k−1 ≤ p−k, so the proof of ROT-ZS applies (equivalently κ(w) ≤ o−1 ≤ p−o)."

**O1 — SOURCE00:24-26, :186-188, :194-195.**
- **Problem.** "gives what is needed" rests on proof-FEW-p5-lift-v3, which is absent (overlay 5, SOURCE03:42; SOURCE05:142).
- **Repair.**
  - Cite SOURCE10:37-46 and the parent's deletion argument.
  - State the ledger inline: odd-block deletion takes (o, F) to (o−1, F−1); rotation deletion takes (o, F) to (o or o−2, F); a deletion from an even block never occurs.
  - At :194-195, replace "F ≥ 3o_F−2 holds automatically (Corollary ROT-HALF)" with "INV*-HALF applies".

**S1 — SOURCE00:4-5, :200-204, :210-212.**
- **Status.**
  - HALF is already parent-accepted from v1 (SOURCE03:10-13).
  - v2 is a separate, unreviewed generalization and does not supersede the text of record (SOURCE03:49).
  - What v2 actually adds is the range (p+1)/2 < o_F ≤ (2p+1)/3 with F ≥ 3o_F−2, plus the corresponding Olson words.
- **"For p = 5 and p = 7 nothing is new" is false at p = 7.**
  - There 3·5 = 2p+1, so ROT/INV*-ZS cover o_F = 5 with F ≥ 13.
  - OLSON-ZS likewise covers length-27 words with o_F = 5 and F ≥ 13.
  - Both go beyond the accepted o_F ≤ 4. Whether such words exist is not claimed.
- **Union caveat.** The p = 5, o_F = 4 piece of the union rests on a finite computer-assisted input (SOURCE03:13).
- **Finite aid.** It tested only (p, k) = (11, 6) and (13, 7), both with k = (p+1)/2, so it probes no parameter that (G) newly allows.

**S2 — SOURCE00:8-9, :206-207.**
- **Problem.** "Exactly" overstates the residual, and "Type-II-like … lie there" reads as an existence claim.
- **Repair.**
  > Within 3o_F ≤ 2p+1, Theorem ROT-ZS as stated does not cover avoiders with F ≤ 3o_F−3; if the normal form has k ≥ 2, these have o_F > (p+1)/2. The proof itself also covers such avoiders whose normal form has k = 1 (by K1) or has κ_terminal ≤ p−k, which can happen when o_F−k ≥ 2. This is the residual of this route, not a necessity statement. A Davenport-tight avoider (κ(w) = o_F−1) with o_F > (p+1)/2, if one exists, would lie in it.

**S3 — SOURCE00:205, :208.**
- **KAPPA01.** It is an unaccepted auxiliary candidate (overlay 7, SOURCE03:44), not an input, and no slice is accepted through it. Write "would cover", not "still covers".
- **"Lemma MULT is unavailable."** Replace with: "Beyond 3o_F > 2p+1, this route's bound e ≤ k−1 no longer guarantees MULT (iii)'s hypothesis 3e+2 ≤ 2p. The separately accepted union still covers o_F ≤ 4."

## Audited / imported

**Audited here (written derivation):**
- Lemma ZS: G1–G5, Steps 1–9, COMP, the endpoints, and Remarks (1) and (3).
- ROT-ZS: the normal-form bookkeeping (F, k ≤ o, parity, κ_terminal), the (G) check, the weight identification, (H) and (K), and the SHgen-E/REFL call conditions.
- The INV*-ZS interface.
- The HALF deduction.
- OLSON-ZS: Cases 1–3, the deletion ledger, and the ordered reconstruction.
- The arithmetic in Sec. 5.

**Imported (hypotheses checked only):**
- (D).
- MULT (i)–(iii); SCHERK, GROW, SET and INC were not re-derived.
- GRX, PM* and K1.
- The normal form; DAV/(V), whose proof is not in the packet.
- Theorem SHgen (FLEXa and Ua not re-audited) and SHgen-E.
- REFL-few-odd r4. The packet holds the r5 errata, whose statement is the same.
- RGR-LONG(p).

**Not established:**
- Lemma ZS for p−k < κ ≤ k−1.
- ROT, INV* or ordered Olson outside the stated hypotheses.
- KAPPA01.
- Any word realizing the k = p sequence.
- Unrestricted ROT(p), INV*(p) or ordered Olson.
