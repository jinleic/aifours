# RQLS10 v132 — THETA(1,2,2) S103: BALANCE identities W(P2) = W(U3), W(V5) = W(Q4), and BLOCK-KILL — every mate with a BLOCK side admits no MAX H6

Owner PhysicsRQLS10-2. Actual returned `/bin/date` BEFORE this NEW manuscript: **Tue Oct 27 02:59:33 PDT 2026**. AUTHOR-WRITTEN CANDIDATE: exact written linear algebra only. Not machine/kernel/formal checked. No scientific Eval/interpreter/CAS/program/enumeration/solver/replay.

**SEPARATE FUTURE ONLY:** frozen Mainv17/asofS72,4977LF,SHA256`59062f07f6e8aa1471cf1b806e780e11771a0eb40bfda9f3878944b1c544ee6e`, its input map/proofs and live151v2/S55 stay UNCHANGED. No automatic review admission/read/adoption.

## 0. Setting and inventory

S103 pattern, any Latin mate (v111), notation of v114/v120/v131. The positions used below hold in the stated side types (v111, v113, v118 §3, v120 §2, v125 §0):
- **Every mate.** Q3 block (v3; Xa', Yc'); U4 block (v4; Xa', Yc'); N1 block (v1; Xb', Yb'); the V-plane Π^5_{Xa'}, the P-plane Π^2_{Yc'}, the V-domino (v3; Xb'), the U-domino (v5; Xb'), the Q-domino (v2; Yb') and the P-domino (v4; Yb').
- **b-BLOCK.** P2 block (v2; Yc', β), U3 block (v3; Xc', β'), N-domino (v3; β), U-domino (v1; β).
- **a-BLOCK.** Q4 block (v4; Ya', a_y), V5 block (v5; Xa', a_{y'}), N-domino (v4; a_{y'}), Q-domino (v1; a_{y'}).

Hence, on a b-BLOCK side:
- row v3 = Q3 block + U3 block + Π^3_{Xb'} + Π^3_β;
- class U = W(U3) + W(U4) + Π^1_β + Π^5_{Xb'};
- column Xb' = Π^1_{Xb'} + Π^3_{Xb'} + Π^5_{Xb'};
- column β = Π^1_β + Π^2_β + Π^3_β.

On an a-BLOCK side:
- row v4 = U4 + Q4 + Π^4_{Yb'} + Π^4_{a_{y'}};
- class Q = W(Q3) + W(Q4) + Π^1_{a_{y'}} + Π^2_{Yb'};
- column Yb' = Π^1_{Yb'} + Π^2_{Yb'} + Π^4_{Yb'};
- column a_{y'} = Π^1_{a_{y'}} + Π^4_{a_{y'}} + Π^5_{a_{y'}}.

In every mate, column Xa' = A' + C' + Π^5_{Xa'} and column Yc' = Π^2_{Yc'} + B' + D'.

Each row-pair and each class pair has projection sum 2I. Each column has projection sum I. Each 2×2 Latin class-pair block is an orthonormal 4-frame (v107 BLOCK4).

## 1. Lemma BALANCE

- **(b) b-BLOCK side, any a-side:** 2P_{W(U3)} = P_{Π^5_{Xa'}} + P_{W(P2)} + P_{Π^1_{Xb'}}. Hence W(P2) = W(U3), and Π^5_{Xa'} ⊥ Π^1_{Xb'} with Π^5_{Xa'} ⊕ Π^1_{Xb'} = W(U3).
- **(a) a-BLOCK side, any b-side:** 2P_{W(Q4)} = P_{Π^2_{Yc'}} + P_{W(V5)} + P_{Π^1_{Yb'}}. Hence W(V5) = W(Q4), and Π^2_{Yc'} ⊕ Π^1_{Yb'} = W(Q4).

Proof of (b). The class-U identity gives

  U3 = 2I − U4 − U1β − U5x.

Here U1β = P_{Π^1_β} = I − P_{Π^2_β} − P_{Π^3_β} by column β, and U5x = P_{Π^5_{Xb'}} = I − P_{Π^1_{Xb'}} − P_{Π^3_{Xb'}} by column Xb'. Substituting,

  U3 = −U4 + P_{Π^2_β} + P_{Π^1_{Xb'}} + (P_{Π^3_β} + P_{Π^3_{Xb'}}).

The row-v3 identity gives P_{Π^3_β} + P_{Π^3_{Xb'}} = 2I − Q3 − U3. Hence

  2U3 = 2I − Q3 − U4 + P_{Π^2_β} + P_{Π^1_{Xb'}}.

Columns Xa' and Yc' give Q3 + U4 = P_{A'} + P_{B'} + P_{C'} + P_{D'} = 2I − P_{Π^5_{Xa'}} − P_{Π^2_{Yc'}}. With P_{Π^2_{Yc'}} + P_{Π^2_β} = P_{W(P2)}, this gives the identity (trace 8 = 2 + 4 + 2).

The right side is a sum of positive operators. For x ⊥ W(U3), every term therefore vanishes, so W(P2) ⊂ W(U3), and the two are equal by dimension. Subtracting P_{W(U3)} leaves two rank-2 projections summing to a rank-4 projection, so they are orthogonal.

(a) is the same computation with row v4, class Q, and columns Yb' and a_{y'}. ∎

## 2. Theorem BLOCK-KILL

No MAX H6 exists for any S103 mate with at least one BLOCK side, i.e. for any (b-BLOCK, a-BLOCK), (b-BLOCK, a-SPLIT) or (b-SPLIT, a-BLOCK) mate.

Proof. By v123 (mates with a SPLIT side) and v131 (BB mates), (Q3, U4) is in its line case. Use its v127 line geometry: an orthonormal basis {a0', a1', b0', b1', h1', h2'} with
- A' = span(a0', a1'), B' = span(b0', b1') and Ĥ(Q3) = span(h1', h2');
- C' = span(b0', c) and D' = span(a0', d), where c = cos θ b1' + sin θ h1', d = cos φ a1' + sin φ h2', and sin θ·sin φ ≠ 0.

Then Π^5_{Xa'} = (A' ⊕ C')^⊥ = span(sin θ b1' − cos θ h1', h2') and Π^2_{Yc'} = (B' ⊕ D')^⊥ = span(sin φ a1' − cos φ h2', h1'). Their sum is 𝒲 := span(a1', b1', h1', h2') = span(a0', b0')^⊥. Write 𝓗 = span(a0', b0').

- **b-BLOCK side.**
  1. By BALANCE(b), both planes lie in W(U3) = W(P2). So W(U3) = 𝒲, and every U3 cell is ⊥ 𝓗.
  2. **a0' is parallel to a U-cell of D'.** A U3 cell of class Ui is ⊥ Ui's cell in D' (class) and ⊥ a0' ∈ D'. If a0' were parallel to neither U-cell of D', then W(U3) ⊥ D', so D' = 𝓗 ∋ b0'. But b0' ∈ C' ⊥ D'. Likewise b0' is parallel to a U-cell of C'.
  3. **Row v3.** Each U3 cell u_r at (v3.r, Xc') lies in 𝒲. It is ⊥ its row-mates q_r = α_r a0' + β_r a1' (column Xa') and q'_r = γ_r b0' + δ_r b1' (column Yc').
     - If some β_r = 0 or δ_r = 0, a Q3 cell is parallel to a0' or b0', hence to a U4 cell: a repeat.
     - Otherwise u_r ⊥ a1', b1' for r = 1, 2. Then Π^3_{Xc'} ⊂ 𝒲 ⊖ span(a1', b1') = Ĥ(Q3), so Π^3_{Xc'} = Ĥ(Q3). This makes {Xa', Yc', Xc'} an orthogonal triple at v3 that separates U3's columns Xc' and β', contradicting SQUEEZE (v101).
- **a-BLOCK side.**
  1. By BALANCE(a), both planes lie in W(Q4) = W(V5). So W(Q4) = 𝒲, and every Q4 cell is ⊥ 𝓗.
  2. **Q-cells.** A Q4 cell of class Qi is ⊥ Qi's cell in A' and ⊥ a0' ∈ A'. As in the b-BLOCK case, a0' is parallel to a Q-cell of A', since otherwise A' = 𝓗 ∋ b0' ⊥ A'. Likewise b0' is parallel to a Q-cell of B'.
  3. **Row v4.** Each Q4 cell w_r at (v4.r, Ya') lies in 𝒲. It is ⊥ its row-mates in C' = span(b0', c) and D' = span(a0', d).
     - A U4 cell parallel to b0' or a0' repeats a Q3 cell.
     - Otherwise w_r ⊥ c, d. Then Π^4_{Ya'} ⊂ 𝒲 ⊖ span(c, d) = span(sin θ b1' − cos θ h1', sin φ a1' − cos φ h2') = Ĥ(U4), so Π^4_{Ya'} = Ĥ(U4). This makes {Xa', Yc', Ya'} an orthogonal triple at v4 that separates Q4's columns Ya' and a_y, contradicting SQUEEZE. ∎

## 3. Consequences (prospective; no pinned file is edited)

- The S103 residual is now ONLY the (b-SPLIT, a-SPLIT) mates, in class (L): both SQUAREs in line cases, v2..v5 non-split (v126), v1 split or not. These are exactly the hypotheses of the v127/v128 normal forms.
- BLOCK-side structure theorems (v113 Z-CELL applications, v115 §3, v118 BLOCK-PAIR, v122, v124, v125, v126 for BLOCK sides, v129, v130 (E), v131 for BB) are now about mate types with no MAX H6. They stay valid as implications; they are not edited.
- BALANCE(b)/(a) are statements about any H6 configuration satisfying the listed incidences. They do not depend on the SQUARE cases.

## 4. Status

The S103 frontier is the SS-mate line-case system of v127/v128, with v2..v5 non-split and v1 split or not. Its existence or exclusion is OPEN. So are the other THETA(1,2,2) class patterns, BARBELL H6, C5 three-label patterns, dense frames, other placements, minimal-rank-3/higher-rank families and E6. All original irreducible10/4+6/5+5 branches remain OPEN.

Imports: v101 SQUEEZE; v107 BLOCK4; v111 FORCED-L; v113; v118 §3; v120 §2; v123 SQUARE-LINE; v125 §0; v127 line geometry; v131 EQUALITY-KILL; elementary linear algebra. No NR/classifier/Butson/Gaussian/code premise. WRITTEN only, not formal/kernel/family/vendor/human/checker/priority/current-openness/novelty clearance.

Only a NEW COMPLETE SEPARATE-FUTURE union may include S132. It must retain ALL older individual nodes/branches/S50/S33/E5/product/source audit/NR+BOTHflatfactorizations/process history, including:
- the v29 and v40 parallel-intent minors;
- the v30 dangling-reference defect;
- the v34 capture retry;
- the S98 zero-credit mental-decimal disclosure;
- the v46 parallel post-cell capture disclosure;
- the S103, S110, S112, S114 and S130 pre-pin draft corrections;
- the v53 two-replace ceiling;
- the v54, v67 and v76 scope typos;
- the v77 stray-space and characterization typos;
- the v64 parallel characterization-pin minor.

Parentv138 TWO full30m02/full31m10 PRECREATION cadence majors, NOT exact write/runtime, and Main156 preopaque/preACK-pinrelease MAJOR per109/110/111 NOTICES ONLY persist with ALL older findings/withdrawals/quarantines. Main111 is process-wake only; nothing opened from its caption. No extra GO/STOP/restart/continuous18way inference. Same HOLD/noGO/18/OWN/actual30min substantive cadence/cutoff2026-10-27T11:05:38-07:00/deadline12:35:38/noearlypark; metadata assembly separately characterized, not a clean global execution/cognition census.
