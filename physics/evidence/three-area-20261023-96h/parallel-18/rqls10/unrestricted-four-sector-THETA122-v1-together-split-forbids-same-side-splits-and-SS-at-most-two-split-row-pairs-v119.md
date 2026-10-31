# RQLS10 v119 — THETA(1,2,2): a v1 split that keeps one side's columns together forbids splits on that side; SS mates have at most two split row-pairs

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 01:07:47 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

We use the S103 THETA(1,2,2) class pattern with a Latin mate that is b-SPLIT on the b-side (v111); the a-side is arbitrary. The notation is that of v118.
- Positions are written in the v103 orientation. Every b-SPLIT orientation is the same up to relabeling, because each step uses only the facts listed in v118 §0 and the crossing pattern "a class uses each column once".
- Suppose v1 splits as {Xb', Yb', a_y} | {b1, b2, a_o} (v104 §3 with x = a_y). Put:
  - R_s = Π^{v1}_{b_s} for s = 1, 2;
  - E = Π^{v1}_{a_o}.

  Then R1 ⊥ R2 ⊥ E.

## 1. Theorem V1-TOGETHER (b-side)

Under this v1 split, v3 does not split in any MAX H6. Symmetrically, v2 does not split either.

Proof for v3. Suppose v3 splits as {Xc', b1, b2}, so that S_s = Π^{v3}_{b_s} and G = Π^{v3}_{Xc'} are mutually orthogonal. Columns give R_s ⊥ S_s and Π^{v2}_{b_s} = (R_s ⊕ S_s)^⊥. Apply the v114 SQUARE trichotomy to A = R1, B = R2, C = S1, D = S2 and H = E.

**(i) S1 = R2.**
1. S1 contains U1(v3.1, b1) and R2 contains U1(v1.1, b2). The plane therefore holds two distinct U1-cells.
2. By TWIN-PLANE (v115 proof, one shared class suffices), U1(v1.1, b2) is parallel to N2(v3.2, b1). This is a repeat.

**(ii) S2 = R1.** Here U2(v3.2, b2) and U2(v1.2, b1) lie in one plane. The argument of (i) applies.

**(iii) Both projections into E are lines.** Choose an orthonormal basis {r1a, r1b, r2a, r2b, e1, e2} with R1 = (r1a, r1b), R2 = (r2a, r2b) and E = (e1, e2). Then:
- S1 = span(r2a, cos θ r2b + sin θ e1);
- S2 = span(r1a, cos φ r1b + sin φ e2);
- θ, φ ∈ (0, π/2];
- G = span(g1, g2), with g1 = sin θ r2b − cos θ e1 and g2 = sin φ r1b − cos φ e2;
- Π^{v2}_{b1} = span(g1, e2) and Π^{v2}_{b2} = span(g2, e1).

The v101 §4 forms at v3 are:
- U1(v1.1, b2) = α U2(v3.1, Xc') + β N2(v3.2, b1), lying in R2;
- U2(v1.2, b1) = α' N1(v3.1, b2) + β' U1(v3.2, Xc'), lying in R1.

All four coefficients are nonzero. Requiring the r1b, e2 (respectively r2b, e1) components to vanish gives:
- U2(v3.1, Xc') ∥ g1 and U1(v3.2, Xc') ∥ g2;
- the e1-component of N2(v3.2, b1) is nonzero exactly when cos θ ≠ 0, and the e2-component of N1(v3.1, b2) is nonzero exactly when cos φ ≠ 0.

There are three sub-cases.
- **cos φ ≠ 0.** N1(v2.1, b1) lies in span(g1, e2) and is orthogonal to N1(v3.1, b2), which lies in span(r1a, r1b, e2) with a nonzero e2-part. Hence N1(v2.1, b1) ∥ g1 ∥ U2(v3.1, Xc'). This is a repeat.
- **cos θ ≠ 0.** Symmetrically, N2(v2.2, b2) ∥ g2 ∥ U1(v3.2, Xc'). This is a repeat.
- **θ = φ = π/2.** Then S1 = (r2a, e1), S2 = (r1a, e2) and G = (r1b, r2b).
  1. The forms give N2(v3.2, b1) ∥ r2a and N1(v3.1, b2) ∥ r1a.
  2. Hence the remaining S2-cell satisfies U2(v3.2, b2) ∥ e2.
  3. Also U1(v1.1, b2) = α r2b + β r2a.
  4. P1(v1.2, b2) is its orthogonal complement in R2, so both of its components are nonzero.
  5. P1(v2.2, b1) lies in Π^{v2}_{b1} = span(r2b, e2) and is orthogonal to P1(v1.2, b2) (class P1). This forces P1(v2.2, b1) ∥ e2 ∥ U2(v3.2, b2), which is a repeat.

**v2 instead of v3.** The same proof applies after exchanging P ↔ U, v2 ↔ v3 and Yc' ↔ Xc', using the P-forms of v104 §4:
- (i) and (ii) give TWIN through P1 or P2;
- the non-right-angle sub-cases force N1(v3.1, b2) ∥ P1(v2.1, Yc') or N2(v3.2, b1) ∥ P2(v2.2, Yc');
- the right-angle sub-case forces U1(v3.1, b1) ∥ P2(v2.1, b2).

## 2. Mirror on the a-side

If the mate is a-SPLIT and v1 splits with x ∈ {b1, b2} (so the a-columns are together at v1), then neither v4 nor v5 splits. The proof is §1 with Q and V in place of P and U, and with the N-cells at v4 and v5.

## 3. Corollary AT-MOST-TWO ((b-SPLIT, a-SPLIT) mates)

Combine §1, §2 and v118 B/A-PAIR:
- if v1 splits with x ∈ {a1, a2}, the splits lie within {v1, v4} or {v1, v5};
- if v1 splits with x ∈ {b1, b2}, the splits lie within {v1, v2} or {v1, v3};
- if v1 does not split, the splits lie within {one of v2, v3} ∪ {one of v4, v5}.

So EVERY MAX H6 of an SS mate has at most TWO split row-pairs, and hence at least THREE non-split row-pairs.

For mixed side-types, §1 and v118 B-PAIR constrain the SPLIT side alone.

## 4. Status

THETA(1,2,2) H6 existence or exclusion remains OPEN. In particular, H6 structures with at least three non-split row-pairs, the BLOCK-side analogues of §1, separated BLOCK splits, the other THETA class patterns, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6 are all open. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v111 FORCED-L; v104 §3/§4 forced triples and forms; v101 §4; v114 SQUARE; v115 TWIN-PLANE (one-class form, contained in its proof); v118. Elementary linear algebra only. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S119. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
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
