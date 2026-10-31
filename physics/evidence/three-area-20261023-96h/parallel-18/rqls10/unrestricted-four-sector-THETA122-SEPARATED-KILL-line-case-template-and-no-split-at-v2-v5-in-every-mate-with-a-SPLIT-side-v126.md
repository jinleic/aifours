# RQLS10 v126 — THETA(1,2,2) SEPARATED-KILL: in every mate with at least one SPLIT side, none of v2, v3, v4, v5 splits

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 02:10:08 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 1. Lemma SEPARATED-KILL (template)

**Setting.** At a row-pair v, suppose there are two 2×2 Latin class-pair blocks.

- S is a squeezing block: class pair σ1, σ2 in columns s, s'. Here σ1 sits at (v.1, s) and (v.2, s'), and σ2 sits at (v.1, s') and (v.2, s). Its cells are p1 = σ1(v.1), p2 = σ1(v.2), q1 = σ2(v.1) and q2 = σ2(v.2).
- O is another block, with columns o1 and o2. Its planes are O1 = Π^v_{o1} and O2 = Π^v_{o2}, and its hat is Ĥ(O).
- σ's other block O* sits at v* in the SAME columns o1, o2. Its planes are O1* and O2*.

The planes O1, O2, O1*, O2* form a v114 SQUARE. Suppose the SQUARE is in a LINE case, so that O2 ∩ O1* and O1 ∩ O2* are lines.

**Claim.** If v splits with Z-CELL third column z = o2, so that O2 = Ĥ(S), then MAX fails. By symmetry the same holds for z = o1.

**Proof.**
1. **Setting up.** W(S) = O2^⊥ ⊇ O1. Let b0 span O2 ∩ O1*. Each K_{σi}(S) lies in W(S), so it is ⊥ b0. By class, it is also ⊥ σi's cell in O1*.
2. **One σ-cell of O1* lies on b0.** If neither σ-cell of O1* were parallel to b0, ORTH2 (v123) would give W(S) ⊥ O1*. Then O1* ⊂ O2, which is a plane-equality case and is excluded. So exactly one is parallel to b0; say σ1's cell is.
3. **Where h1 lies.** ORTH2 then gives K_{σ2}(S) ⊥ O1*. Hence K_{σ2}(S) ⊥ O2 + O1* = O2 ⊕ span(h1), where h1 ∈ Ĥ(O) is the hat direction of O1*. It follows that h1 ∈ W(S) ⊖ K_{σ2}(S) = span(p1, p2). Write h1 = μ p1 + ν p2.
4. **Rows place O1's cells.** By rows, d_{O1} ∈ span(p2, q2) and e_{O1} ∈ span(p1, q1).
5. **Repeat from d_{O1}.** Write d_{O1} = κ p2 + λ q2. Since Ĥ(O) ⊥ O1, 0 = <h1|d_{O1}> = ν̄ κ. This uses p1 ⊥ p2 (class), p1 ⊥ q2 (column s) and p2 ⊥ q2 (row). If κ = 0, then d_{O1} ∥ q2, which is a repeat. So ν = 0 and h1 ∥ p1.
6. **Repeat from e_{O1}.** Write e_{O1} = κ' p1 + λ' q1. Then 0 = <h1|e_{O1}> = κ', so e_{O1} ∥ q1, which is a repeat. ∎

## 2. Theorem NO-SQUEEZED-SPLIT (S103 THETA(1,2,2), every mate with a SPLIT side)

In every (b-SPLIT, a-SPLIT), (b-SPLIT, a-BLOCK) or (b-BLOCK, a-SPLIT) mate, no MAX H6 splits at v2, v3, v4 or v5. Only v1 can split.

Proof.
- **SPLIT sides.** The squeezed row-pairs never split (v121, v123).
- **BLOCK side (mixed mates).** By v123 SQUARE-LINE, both SQUAREs are in line cases. Each Z-CELL third column is excluded as follows:
  - b-BLOCK v2 (S = P2 block, O = V2 block, O* = P5):
    - z = β': excluded by TOGETHER-KILL (v122);
    - z = Yb': excluded by DOMINO-THIRD and SQUARE-LINE (v125);
    - z ∈ {Xc', Ya'}: excluded by §1.
  - b-BLOCK v3 (S = U3, O = Q3, O* = U4):
    - z' = β: TOGETHER-KILL;
    - z' = Xb': excluded by v125;
    - z' ∈ {Xa', Yc'}: excluded by §1.
  - a-BLOCK v4 (S = Q4, O = U4, O* = Q3):
    - z = a_{y'}: TOGETHER-KILL;
    - z = Yb': excluded by v125;
    - z ∈ {Xa', Yc'}: excluded by §1.
  - a-BLOCK v5 (S = V5, O = P5, O* = V2):
    - z = a_y: TOGETHER-KILL;
    - z = Xb': excluded by v125;
    - z ∈ {Xc', Ya'}: excluded by §1. ∎

## 3. Consequences

- Every MAX H6 for a mate with a SPLIT side has v2..v5 non-split and both SQUAREs in line cases. The only possible split is at v1.
- For (b-BLOCK, a-BLOCK) mates, §1 still kills every separated split whose SQUARE is in a line case. The remaining BB splits are exactly those forced by the v124 plane-equality cases.

## 4. Status

THETA(1,2,2) H6 existence or exclusion remains OPEN. In particular, all-line-case H6 with non-split v2..v5 is open (with v1 split or not), as are the BB equality cases, the other THETA class patterns, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v101 SQUEEZE; v104 §2; v111; v113 Z-CELL; v114 SQUARE; v120 TWIN-LINE; v121; v122; v123 ORTH2/SQUARE-LINE; v124; v125; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S126. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112 and S114 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54 and v67 scope typos;
- the v64 parallel characterization-pin minor.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
