# RQLS10 v136 — THETA(1,2,2) S103, SS residual: Gram-cycle consistency of the coupled squeezer system and a Bargmann-phase lock between the two orthogonal 3-spaces

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 03:33:39 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written algebra (complex Binet–Cauchy identity). Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

This is the SS residual with (V2, P5) in its line case, in the v128 notation and orientation:
- C6 = (B + C) ⊕ (A + D), an orthogonal sum of 3-spaces;
- normals nα = N(d_B, P1_C), nβ = N(e_B, P1_C), nγ = N(d_B, P2_C), nδ = N(e_B, P2_C) in B + C;
- normals mα = N(d_A, P1_D), mβ = N(e_A, P1_D), mγ = N(d_A, P2_D), mδ = N(e_A, P2_D) in A + D.

Each normal is a unit vector fixed up to a phase. By the v128 table, the eight squeezer cells are:

| Cell | Expression |
|---|---|
| π1 = P1(v2.1, Yc') | a1 nα + b1 mα |
| p22 = P1(v2.2, b1) | a2 nβ + b2 mβ |
| p21 = P2(v2.1, b2) | a3 nγ + b3 mγ |
| π2 = P2(v2.2, Yc') | a4 nδ + b4 mδ |
| ν1 = V2(v5.1, Xa') | c1 nα + e1 mδ |
| ν2 = V1(v5.2, Xa') | c2 nδ + e2 mα |
| v51 = V1(v5.1, a1) | c3 nβ + e3 mγ |
| v52 = V2(v5.2, a2) | c4 nγ + e4 mβ |

Put N_{xy} = <n_x|n_y> and M_{xy} = <m_x|m_y>. We call the configuration NONDEGENERATE if all sixteen coefficients are nonzero and the eight Gram entries N_{αβ}, N_{δγ}, N_{αγ}, N_{δβ}, M_{αβ}, M_{δγ}, M_{αγ}, M_{δβ} are nonzero.

## 1. Lemma GRAM-CYCLES

Of the ten squeezer orthogonalities (v128 §2), eight split into two 4-cycles of Gram labels.
- **Cycle I.** Using π1 ⊥ p22, π2 ⊥ p21, ν1 ⊥ v51 and ν2 ⊥ v52:
  - ā1 a2 N_{αβ} = −b̄1 b2 M_{αβ};
  - ā4 a3 N_{δγ} = −b̄4 b3 M_{δγ};
  - c̄1 c3 N_{αβ} = −ē1 e3 M_{δγ};
  - c̄2 c4 N_{δγ} = −ē2 e4 M_{αβ}.
- **Cycle II.** Using π1 ⊥ p21, π2 ⊥ p22, ν1 ⊥ v52 and ν2 ⊥ v51:
  - ā1 a3 N_{αγ} = −b̄1 b3 M_{αγ};
  - ā4 a2 N_{δβ} = −b̄4 b2 M_{δβ};
  - c̄1 c4 N_{αγ} = −ē1 e4 M_{δβ};
  - c̄2 c3 N_{δβ} = −ē2 e3 M_{αγ}.

In the nondegenerate case each cycle gives the same coefficient relation ρ_P = ρ_V, where

  ρ_P = (b̄1 b̄4 b2 b3)/(ā1 ā4 a2 a3),  ρ_V = (ē1 ē2 e3 e4)/(c̄1 c̄2 c3 c4).

It also gives the two Gram relations

  N_{αβ} N_{δγ} / (M_{αβ} M_{δγ}) = ρ_P = N_{αγ} N_{δβ} / (M_{αγ} M_{δβ}).

Proof. The cross terms vanish because B + C ⊥ A + D. Dividing the four equations of each cycle pairwise gives the relations, since (N_{αβ}/M_{αβ})(N_{δγ}/M_{δγ}) = (N_{αβ}/M_{δγ})(N_{δγ}/M_{αβ}). ∎

## 2. Theorem BARGMANN-PHASE LOCK

In the nondegenerate case,

  arg Φ_BC ≡ arg Φ_AD (mod π),

where
- Φ_BC = <e_B|P1_C><P1_C|d_B><d_B|P2_C><P2_C|e_B>;
- Φ_AD = <e_A|P1_D><P1_D|d_A><d_A|P2_D><P2_D|e_A>.

These are the four-vertex Bargmann invariants of the quadrilaterals formed by V's column-Ya' pair with P's column-Xc' pair, and by V's column-Xc' pair with P's column-Ya' pair. Both are gauge invariant.

Proof.
1. **Normals as cross products.** Take n(u, w) = conj(u × w) in coordinates of the 3-space. This vector is orthogonal to u and w.
2. **Binet–Cauchy.** The complex Binet–Cauchy identity gives <n(u,w)|n(u',w')> = <u'|u><w'|w> − <w'|u><u'|w>.
3. **The four Gram entries in B + C.** Using d_B ⊥ e_B and P1_C ⊥ P2_C:
   - N_{αβ} ∝ −<P1_C|d_B><e_B|P1_C>;
   - N_{δγ} ∝ −<P2_C|e_B><d_B|P2_C>;
   - N_{αγ} ∝ −<P2_C|d_B><d_B|P1_C>;
   - N_{δβ} ∝ −<P1_C|e_B><e_B|P2_C>.
4. **The two products.** For the cross-product normals, N_{αβ}N_{δγ} = Φ_BC/κ and N_{αγ}N_{δβ} = conj(Φ_BC)/κ, with the same positive normalisation κ. Changing the phases of the unit normals multiplies both products by the same unimodular factor: in both products nα and nδ occur once each as bras and nβ and nγ once each as kets. So the ratio Φ_BC/conj(Φ_BC) is independent of those phases.
5. **The same in A + D.** Likewise M_{αβ}M_{δγ}/(M_{αγ}M_{δβ}) = Φ_AD/conj(Φ_AD).
6. **Conclusion.** Lemma GRAM-CYCLES gives N_{αβ}N_{δγ}/(N_{αγ}N_{δβ}) = M_{αβ}M_{δγ}/(M_{αγ}M_{δβ}). So Φ_BC/conj(Φ_BC) = Φ_AD/conj(Φ_AD). ∎

**Mirror.** The (Q3, U4) square, with the v134 table, gives the same structure. The cycles are U(r1), U(r2), Q(c1), Q(c2) and U(c2), U(c1), Q(r1), Q(r2). The conclusion is that, in the nondegenerate case,

  arg Φ_{B'C'} ≡ arg Φ_{A'D'} (mod π),

with Φ_{B'C'} = <U1_{C'}|d_{B'}><d_{B'}|U2_{C'}><U2_{C'}|e_{B'}><e_{B'}|U1_{C'}> and Φ_{A'D'} the same with A', D' in place of B', C'.

## 3. Status

This is one real-codimension phase condition per SQUARE, valid for the nondegenerate SS residual. The degenerate subcases (a vanishing coefficient or overlap) are not treated here. No contradiction is claimed.

The SS line-case H6 remains OPEN, whether or not v1 splits. So do the other THETA(1,2,2) class patterns, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v127 LINE-GEOMETRY and SQUEEZER-NORMALS; v128 NORMAL-SHARING; v134 mirror table; elementary linear algebra (complex Binet–Cauchy). No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S136. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112, S114 and S130 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54, v67 and v76 scope typos;
- the v77 stray-space and characterization typos;
- the v78 checkpoint typo;
- the v80 stray space;
- the v64 parallel characterization-pin minor.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
