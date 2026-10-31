# RQLS10 v121 — DOUBLE-PAIR lemma, and SPLIT-KILL: in THETA(1,2,2), a SPLIT side never splits at its squeezed row-pairs (v2, v3 on the b-side; v4, v5 on the a-side)

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 01:29:13 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 1. Lemma DOUBLE-PAIR (general MAX tool)

Let X be a plane with orthonormal basis (x1, x2). Let W be a plane carrying two orthonormal bases of cells, (w1, w2) and (w1', w2'), that share no ray. Suppose that x1 ⊥ w1, x2 ⊥ w2, x1 ⊥ w1' and x2 ⊥ w2'. Then X ⊥ W.

Proof.
1. Let M_ij = <x_i|w_j>. Then M11 = M22 = 0.
2. Write w_j' = Σ_k w_k R_kj with R unitary.
3. Then <x1|w1'> = M12·R21 = 0 and <x2|w2'> = M21·R12 = 0.
4. If R were diagonal, w_j' ∥ w_j, which is a shared ray. Hence R12 and R21 are nonzero, since |R12| = |R21|.
5. So M12 = M21 = 0, i.e. M = 0. ∎

In MAX arrays the orthogonalities come from rows, columns or classes, and two different cell bases of one plane share no ray.

## 2. Theorem SPLIT-KILL (S103 THETA(1,2,2) pattern, every Latin mate of v111)

- **(b)** If the mate is b-SPLIT, no MAX H6 splits at v2, and none splits at v3.
- **(a)** If the mate is a-SPLIT, no MAX H6 splits at v4, and none splits at v5.

Notation is that of v114 and v120. The ingredients are all forced in every mate by v111: the blocks V(v2; Xc',Ya'), Q(v3; Xa',Yc'), U(v4; Xa',Yc') and P(v5; Xc',Ya'), and the dominoes of v120 §2.

**Proof that v2 does not split (b-SPLIT).**
1. **The hat equation.** The forced split is {Yc', b1, b2} | {Xc', Ya', Yb'} (v104 §3). Hence Π^{v2}_{Yb'} = Ĥ(V2) = (A ⊕ B)^⊥ (v114 §2).
2. **Case (i) is forced.** By v120 SPLIT-FORCES-SQUARE (TWIN-LINE on Q's dominoes), A ∩ D = 0 and (V2, P5) is in case (i), C = B. Hence Π^{v3}_{Xc'} = (A ⊕ C)^⊥ = Ĥ(V2).
3. **Two cell bases on Ĥ(V2).** The plane Ĥ(V2) now carries two cell bases:
   - U's v3-domino: U_a(v3.1, Xc') and U_b(v3.2, Xc');
   - Q's v2-domino: Q1 and Q2 at (v2, Yb').
4. **DOUBLE-PAIR with Π^{v3}_{Xa'}.** Its cells are Q_c(v3.1, Xa') and Q_d(v3.2, Xa') from the Q block.
   - Rows: (v3.1, Xa') ⊥ U_a and (v3.2, Xa') ⊥ U_b.
   - Classes: Q_c(v3.1, Xa') ⊥ Q_c(v2, Yb') and Q_d(v3.2, Xa') ⊥ Q_d(v2, Yb').

   DOUBLE-PAIR gives Π^{v3}_{Xa'} ⊥ Ĥ(V2). The same argument gives Π^{v3}_{Yc'} ⊥ Ĥ(V2): its cells are Q_d(v3.1, Yc') and Q_c(v3.2, Yc').
5. **Ĥ(V2) is the hat of Q3.** Hence Ĥ(V2) ⊥ W(Q3), so Ĥ(V2) = Ĥ(Q3).
6. **A forbidden split at v3.** Π^{v3}_{Xc'} = Ĥ(Q3) is orthogonal to both Q-block planes at v3. So {Xa', Yc', Xc'} is an orthogonal triple at v3, and v3 splits as {Xa', Yc', Xc'} | {Xb', b1, b2}.
7. **SQUEEZE contradiction.** U squeezes v3 (v104 §2), and U_a's two v3-columns are Xc' and a b-column. These lie in different triples, contradicting v101 SQUEEZE. So MAX fails.

**Proof that v3 does not split (b-SPLIT).** The argument is symmetric.
1. The forced split {Xc', b1, b2} | {Xa', Xb', Yc'} gives Π^{v3}_{Xb'} = Ĥ(Q3).
2. TWIN-LINE on V's dominoes gives case (ii'), D' = A'. Hence Π^{v2}_{Yc'} = Ĥ(Q3).
3. Ĥ(Q3) then carries V's v3-domino and P's v2-domino.
4. DOUBLE-PAIR applies to the V-block planes A and B at v2: rows against P's (v2, Yc') cells, and class V against V's (v3, Xb') cells. This gives A, B ⊥ Ĥ(Q3), so Ĥ(Q3) = Ĥ(V2).
5. Then {Xc', Ya', Yc'} is an orthogonal triple at v2. This separates P's v2-columns Yc' and b_s, contradicting SQUEEZE.

**Proof of (a) (a-SPLIT).** This is the mirror of (b).
- **v5.** The split gives Π^{v5}_{Xb'} = Ĥ(P5) and case (i) via U's dominoes. Then Π^{v4}_{Ya'} = Ĥ(P5) carries U(v5, Xb') and Q(v4, Ya'). DOUBLE-PAIR against the U-block planes C' and D' at v4 gives Ĥ(P5) = Ĥ(U4). So {Xa', Yc', Ya'} is orthogonal at v4, which separates Q's v4-columns Ya' and a_s.
- **v4.** The split gives Π^{v4}_{Yb'} = Ĥ(U4) and case (ii') via P's dominoes. Then Π^{v5}_{Xa'} = Ĥ(U4) carries P(v4, Yb') and V(v5, Xa'). DOUBLE-PAIR against C and D at v5 gives Ĥ(U4) = Ĥ(P5). So {Xc', Ya', Xa'} is orthogonal at v5, which separates V's v5-columns Xa' and a_s.

## 3. Consequences (prospective; no pinned file is edited)

- **(1)** In every (b-SPLIT, a-SPLIT) mate, the ONLY row-pair that can split is v1, so at least four row-pairs are non-split. This supersedes, in strength:
  - v112 SS-ALL-TRIPLE;
  - v118 B/A-PAIR;
  - v119 AT-MOST-TWO.

  The statements of v112, v118 and v119 remain true. The hypotheses of v116 §2 and v117 were already empty by v118.
- **(2)** In mixed mates, the SPLIT side's squeezed row-pairs never split.
- **(3)** The surviving SS frontier consists of MAX H6 structures with v2, v3, v4 and v5 all non-split and v1 split or non-split. The BLOCK-side splits keep the v113/v115/v118 status.

## 4. Status

THETA(1,2,2) H6 existence or exclusion remains OPEN. In particular, the following are all open:
- non-split row-pairs and v1;
- BLOCK sides;
- the other THETA class patterns;
- BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6.

All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v101 §1 SQUEEZE; v104 §2/§3; v111 FORCED-L; v114 SQUARE and SPLIT-CRITERIA; v120 TWIN-LINE and SPLIT-FORCES-SQUARE; elementary 2×2 linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S121. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
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
