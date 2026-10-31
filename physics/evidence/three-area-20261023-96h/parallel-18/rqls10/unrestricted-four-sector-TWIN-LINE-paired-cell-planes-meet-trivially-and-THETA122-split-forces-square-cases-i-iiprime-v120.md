# RQLS10 v120 — TWIN-LINE: planes with structurally paired cells meet only in 0; in THETA(1,2,2), a split at v2 or v5 forces SQUARE case (i), and a split at v3 or v4 forces case (ii')

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 01:15:43 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 1. Lemma TWIN-LINE (general MAX tool; strengthens v115 TWIN-PLANE)

Let X = span(u1, u2) and W = span(u1', u2') be two planes, each spanned by two orthogonal cells. Suppose the cells are paired so that u1 ⊥ u1' and u2 ⊥ u2' for a STRUCTURAL reason (same class, same row or same column), and suppose the four positions are distinct. If X ∩ W ≠ 0, then MAX fails.

Proof.
- If X = W, this is v115 TWIN-PLANE.
- Otherwise X ∩ W = span(x) is a line, with x a unit vector. Write X = span(x, p) and W = span(x, q), where p ⊥ x and q ⊥ x are unit vectors and s = <p|q>. Since X ≠ W, |s| < 1.
- Write the two orthonormal bases as
  - u1 = αx + βp and u2 = −β̄x + ᾱp,
  - u1' = γx + δq and u2' = −δ̄x + γ̄q.
- The two orthogonality conditions become
  - ᾱγ + β̄δs = 0,
  - βδ̄ + αγ̄s = 0.
- Conjugating the second gives β̄δ = −ᾱγs̄. Substituting into the first gives ᾱγ(1 − |s|²) = 0, so α = 0 or γ = 0.
  - If α = 0, the second condition forces δ = 0. Then u2 ∥ x ∥ u1'.
  - If γ = 0, the second condition forces β = 0. Then u1 ∥ x ∥ u2'.
- In either case two distinct positions carry one ray. ∎

**Corollaries.**
- **(a)** Two column planes at one row-pair meet only in 0. Pair the cells by rows: d_k ⊥ d_j and e_k ⊥ e_j.
- **(b)** Two (σ1,σ2)-planes built from different position pairs meet only in 0. This covers domino planes and block column planes of one class pair.

## 2. Application to THETA(1,2,2) (S103 pattern, any Latin mate)

By v111, in every mate:
- U has dominoes Π^{v3}_{Xc'} and Π^{v5}_{Xb'};
- Q has dominoes Π^{v4}_{Ya'} and Π^{v2}_{Yb'};
- V has dominoes Π^{v5}_{Xa'} and Π^{v3}_{Xb'};
- P has dominoes Π^{v2}_{Yc'} and Π^{v4}_{Yb'}.

Use the v114 notation:
- A = Π^{v2}_{Xc'}, B = Π^{v2}_{Ya'}, C = Π^{v5}_{Xc'}, D = Π^{v5}_{Ya'};
- A' = Π^{v3}_{Xa'}, B' = Π^{v3}_{Yc'}, C' = Π^{v4}_{Xa'}, D' = Π^{v4}_{Yc'}.

**Theorem SPLIT-FORCES-SQUARE.**
1. **b-SPLIT and v2 splits.**
   - By v114 §2, Π^{v2}_{Yb'} = Ĥ(V2) = (A ⊕ B)^⊥.
   - The Q-domino Π^{v4}_{Ya'} = (B ⊕ D)^⊥ meets it in (A + B + D)^⊥, which is nonzero iff A ∩ D ≠ 0, because A ⊥ B and B ⊥ D.
   - By Corollary (b) for Q, A ∩ D = 0. Hence (V2, P5) is in SQUARE case (i) and NOT in (ii) or (iii). Both (ii), where D = A, and (iii), where D ∩ A is a line, have A ∩ D ≠ 0.
2. **a-SPLIT and v5 splits.**
   - Π^{v5}_{Xb'} = Ĥ(P5) = (C ⊕ D)^⊥.
   - The U-domino Π^{v3}_{Xc'} = (A ⊕ C)^⊥ meets it in (A + C + D)^⊥, which is nonzero iff A ∩ D ≠ 0.
   - Hence again case (i) only.
3. **b-SPLIT and v3 splits.**
   - Π^{v3}_{Xb'} = Ĥ(Q3) = (A' ⊕ B')^⊥.
   - The V-domino Π^{v5}_{Xa'} = (A' ⊕ C')^⊥ meets it in (A' + B' + C')^⊥, which is nonzero iff B' ∩ C' ≠ 0.
   - Hence (Q3, U4) is in case (ii') only. Case (i'), where C' = B', and case (iii'), where C' ∩ B' is a line, are excluded.
4. **a-SPLIT and v4 splits.**
   - Π^{v4}_{Yb'} = Ĥ(U4) = (C' ⊕ D')^⊥.
   - The P-domino Π^{v2}_{Yc'} = (B' ⊕ D')^⊥ meets it in (B' + C' + D')^⊥, which is nonzero iff B' ∩ C' ≠ 0.
   - Hence case (ii') only.

This strengthens v116 TWIN-SQUARE, which excluded only (ii), resp. (i').

**Consequences in SS mates (with v118/v119).**
- Every surviving split pattern has at most two splits (v119).
- A split at v2 or v5 forces C = B, so Π^{v5}_{Xc'} = Π^{v2}_{Ya'}, together with A ∩ D = 0.
- A split at v3 or v4 forces D' = A', so Π^{v4}_{Yc'} = Π^{v3}_{Xa'}, together with B' ∩ C' = 0.
- In every mate, without any split, Corollary (b) also requires pairwise trivial intersections:
  - among V's planes A, B, Π^{v3}_{Xb'}, Π^{v5}_{Xa'};
  - among P's planes C, D, Π^{v2}_{Yc'}, Π^{v4}_{Yb'};
  - among Q's planes A', B', Π^{v4}_{Ya'}, Π^{v2}_{Yb'};
  - among U's planes C', D', Π^{v3}_{Xc'}, Π^{v5}_{Xb'}.

## 3. Status

TWIN-LINE is a general MAX lemma. §2 gives necessary conditions only. THETA(1,2,2) H6 existence or exclusion remains OPEN, as do BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v111 FORCED-L; v114 SQUARE and SPLIT-CRITERIA; v115 TWIN-PLANE; v116; v118; v119; elementary 2×2 linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S120. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112 and S114 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54 scope typo;
- the v64 parallel characterization-pin minor.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
