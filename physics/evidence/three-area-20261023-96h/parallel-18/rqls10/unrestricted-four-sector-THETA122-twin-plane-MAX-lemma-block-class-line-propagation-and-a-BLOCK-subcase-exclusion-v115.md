# RQLS10 v115 — The TWIN-PLANE MAX lemma, class-line propagation for two-block pairs, and an excluded THETA(1,2,2) b-BLOCK sub-case

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 00:35:25 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 1. Lemma TWIN-PLANE (general MAX tool)

Let σ1 ≠ σ2 be classes. A **(σ1,σ2)-plane** is span(s1, s2), where s1 is a σ1-cell, s2 is a σ2-cell, and the two cells share a row or a column, so that s1 ⊥ s2. Examples of such planes:
- a domino plane;
- a column plane of a 2×2 class-pair block.

**Claim.** Two (σ1,σ2)-planes built from different position pairs never coincide in a MAX array.

**Proof.** Write Π = span(s1, s2) = span(s1', s2'), and assume first that s1 ≠ s1' as positions. Since s1 ⊥ s1' (same class) and s1 ⊥ s2, both s1' and s2 are parallel to s1^⊥ inside the 2-plane Π. So two distinct positions carry one ray. If instead s1 = s1', then s2 and s2' are distinct positions that both carry s1^⊥.

## 2. Lemma PROPAGATION (class pair with two blocks and two dominoes)

Suppose the twelve H6 cells of a class pair consist of two 2×2 blocks W1, W2 and two dominoes D, D', so that P_{W1} + P_{W2} + P_D + P_{D'} = 2I. If D ⊂ W1, then:
- D' = Ĥ1 = W1^⊥;
- W2 = (W1 ⊖ D) ⊕ Ĥ1.

**Proof.** The operator 2I − P_{W1} − P_D equals:
- 1 on W1 ⊖ D;
- 0 on D;
- 2 on Ĥ1.

It equals P_{W2} + P_{D'}, which forces Ĥ1 ⊂ W2 ∩ D'. By dimension, D' = Ĥ1, and then P_{W2} is the projection onto (W1 ⊖ D) ⊕ Ĥ1.

**Where it applies in THETA(1,2,2) b-BLOCK mates (v111).**
- P has blocks W(P2) and W(P5), with dominoes (v1, β') and (v4, Yb').
- U has blocks W(U3) and W(U4), with dominoes (v1, β) and (v5, Xb').

Combined with v113 Z-CELL:
- if v2 splits with third column z = β' then Π^{v4}_{Yb'} = Ĥ(P2);
- if z = Yb' then Π^{v1}_{β'} = Ĥ(P2);
- likewise for U at v3 with z' ∈ {β, Xb'}.

## 3. Theorem SUBCASE-EXCLUSION

Consider a b-BLOCK mate, any a-side. Suppose all of the following hold:
- v2 splits as {Yc', β, β'} | {Xc', Ya', Yb'}, i.e. z = β';
- v3 splits with third column z' = Xb';
- v5 has the orthogonal triple {Xc', Ya', Xb'}.

The last condition is automatic for a-SPLIT. For a-BLOCK it is equivalent to v5's third column being a_y. Under these hypotheses MAX fails.

**Proof.**
1. **Step (1).**
   - z = β' gives Π^{v2}_{β'} = Ĥ(P2).
   - Z-CELL gives Π^{v1}_{β'} ⊂ W(P2).
   - By §2, W(P5) = (W(P2) ⊖ Π^{v1}_{β'}) ⊕ Ĥ(P2).
   - Column β' gives Π^{v3}_{β'} = W(P2) ⊖ Π^{v1}_{β'}.
   - Hence W(P5) = Π^{v3}_{β'} ⊕ Ĥ(P2).
2. **Step (2).** The triple {Xc', Ya', Xb'} at v5, together with the P5 block, gives Π^{v5}_{Xb'} = Ĥ(P5), which is orthogonal to Π^{v3}_{β'}.
3. **Step (3).** By Z-CELL for U with z' = Xb', Π^{v5}_{Xb'} ⊂ W(U3) = Π^{v3}_{Xc'} ⊕ Π^{v3}_{β'}. With step (2) this gives Π^{v5}_{Xb'} = Π^{v3}_{Xc'}.
4. **Step (4).** Both planes are (U1,U2)-planes: the U domino at (v5, Xb') and the U3 block column Xc'. TWIN-PLANE then gives a repeat.

The image under the combinatorial symmetry τ is excluded in the same way. Here τ fixes v1, swaps v2↔v5 and v3↔v4, maps Xa'↔Yc', Xb'↔Yb', Xc'↔Ya' and a↔b, and sends classes P↔V, U↔Q, N↔N, with row relabeling. The result is the corresponding a-BLOCK sub-case.

## 4. Status

The new tools are TWIN-PLANE and PROPAGATION, and one family of BLOCK all-split configurations is excluded. The remaining BLOCK-separated sub-cases, the non-triple H6 structures and THETA(1,2,2) H6 existence are OPEN. So are BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v111 FORCED-L; v113 Z-CELL; v107 BLOCK4/hats/TRIPLE; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S115. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112 and S114 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54 scope typo.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
