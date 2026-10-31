# RQLS10 v114 — THETA(1,2,2), every Latin mate: a square-orthogonality trichotomy for the forced block pairs, and triple splits as hat equalities

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 00:26:12 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting

We use the S103 THETA(1,2,2) class pattern with ANY Latin mate. By v111 the following blocks are forced in every mate:
- V at (v2; Xc', Ya');
- Q at (v3; Xa', Yc');
- U at (v4; Xa', Yc');
- P at (v5; Xc', Ya');
- N at (v1; Xb', Yb').

Π^v_k denotes the H6 plane of column k at row-pair v. Ĥ denotes block hats (v107).

## 1. Lemma SQUARE (trichotomy)

Put A = Π^{v2}_{Xc'}, B = Π^{v2}_{Ya'}, C = Π^{v5}_{Xc'}, D = Π^{v5}_{Ya'} and H = Ĥ(V2). The four orthogonalities are:
- A ⊥ B (the V block);
- C ⊥ D (the P block);
- A ⊥ C (column Xc');
- B ⊥ D (column Ya').

Hence C ⊂ B ⊕ H and D ⊂ A ⊕ H. For c ∈ C and d ∈ D we get ⟨c, d⟩ = ⟨P_H c, P_H d⟩, because B, A and H are mutually orthogonal. So C ⊥ D says exactly that P_H C ⊥ P_H D inside the plane H. At least one of the following then holds:
- **(i)** C = B, i.e. Π^{v5}_{Xc'} = Π^{v2}_{Ya'}. Then Π^{v3}_{Xc'} = Ĥ(V2) and Π^{v4}_{Ya'} = Ĥ(P5).
- **(ii)** D = A, i.e. Π^{v5}_{Ya'} = Π^{v2}_{Xc'}. Then Π^{v3}_{Xc'} = Ĥ(P5) and Π^{v4}_{Ya'} = Ĥ(V2).
- **(iii)** P_H C and P_H D are complementary orthogonal lines of H. Then C ∩ B and D ∩ A are lines.

Case (iii) excludes (i) and (ii), but (i) and (ii) may hold together. In that case W(P5) = W(V2) and Π^{v3}_{Xc'} = Π^{v4}_{Ya'} = H. (Pre-pin draft correction: an earlier unpinned wording said "exactly one" of (i)–(iii). It was corrected to "at least one" before the first pin. A mis-anchored intermediate edit was also repaired before the first pin.)

The same trichotomy holds for the pair Q at v3 and U at v4, which share columns Xa' and Yc'. Their third planes are Π^{v5}_{Xa'} and Π^{v2}_{Yc'}.

## 2. Lemma SPLIT-CRITERIA ((b-SPLIT, a-SPLIT) mates)

By v112 the forced triples are those of v104 §3. In a split T | T', if the planes of T' sum to I then T is automatically orthogonal. This gives the following equivalences:
- v2 splits ⇔ Π^{v2}_{Yb'} = Ĥ(V2), since T' = {Xc', Ya', Yb'} and Xc' ⊥ Ya';
- v3 splits ⇔ Π^{v3}_{Xb'} = Ĥ(Q3);
- v4 splits ⇔ Π^{v4}_{Yb'} = Ĥ(U4);
- v5 splits ⇔ Π^{v5}_{Xb'} = Ĥ(P5);
- v1 splits ⇔ Π^{v1}_x = Ĥ(N1) for some x ∈ {a1, a2, b1, b2}.

Corollaries.
- **(a)** v112 SS-ALL-TRIPLE says these five equalities never all hold.
- **(b)** Suppose v3 and v5 both split. Column Xb' then forces Ĥ(Q3) ⊥ Ĥ(P5) and Π^{v1}_{Xb'} = (Ĥ(Q3) ⊕ Ĥ(P5))^⊥.
- **(c)** Suppose v2 and v4 both split. Then Ĥ(V2) ⊥ Ĥ(U4) and Π^{v1}_{Yb'} = (Ĥ(V2) ⊕ Ĥ(U4))^⊥.
- **(d)** In the situation of (b) and (c), W(N1) = Π^{v1}_{Xb'} ⊕ Π^{v1}_{Yb'} is determined by the four hats Ĥ(Q3), Ĥ(P5), Ĥ(V2) and Ĥ(U4).

## 3. Status

These are structural reformulations valid for every Latin mate (§1) and every SS mate (§2). They reduce the THETA(1,2,2) H6 question to explicit hat/plane identities. No H6 existence or exclusion is claimed. The BLOCK-separated cases, the non-triple H6, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6 remain OPEN. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v111 FORCED-L; v112 forced triples and SS-ALL-TRIPLE; v107 BLOCK4/hats; v101 SQUEEZE; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S114. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110 and S112 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54 scope typo.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
